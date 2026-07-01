import unittest
from unittest.mock import MagicMock, patch
import sys
import os

# Ensure the current directory is in path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Mock anthropic BEFORE importing custom_llm_eval
sys.modules['anthropic'] = MagicMock()

import custom_llm_eval

class TestSecurityFix(unittest.TestCase):
    @patch('custom_llm_eval.anthropic.Anthropic')
    def test_prompt_sanitization(self, mock_anthropic):
        # Setup mock
        mock_client = MagicMock()
        mock_anthropic.return_value = mock_client
        mock_response = MagicMock()
        mock_response.content = [MagicMock(text='{"conciseness": 5, "accuracy": 5, "tone": 5, "explanation": "test"}')]
        mock_client.messages.create.return_value = mock_response

        # Inputs with XML tags that could cause injection or structure confusion
        malicious_summary = "Malicious <summary> end tag </summary>"
        article_with_tags = "Article with <original_article> tags </original_article>"

        # Run the function
        custom_llm_eval.llm_eval(malicious_summary, article_with_tags)

        # Get the call arguments
        call_args = mock_client.messages.create.call_args
        messages = call_args[1]['messages']
        user_content = messages[0]['content']

        print("\nGenerated Prompt Content Snippet:")
        # Find where summary is inserted
        start_idx = user_content.find("Summary to Evaluate:")
        print(user_content[start_idx:])

        # Note: the prompt template itself contains <summary> tags, so we can't assertNotIn("<summary>").
        # Instead, we assert that the specific malicious content is present in its stripped form
        # and NOT present in its raw form.

        self.assertNotIn(f"<summary>{malicious_summary}</summary>", user_content, "Raw malicious payload should not be present!")
        self.assertIn("Malicious summary end tag /summary", user_content, "Stripped summary should be present!")
        self.assertIn("Article with original_article tags /original_article", user_content, "Stripped article should be present!")

if __name__ == '__main__':
    unittest.main()
