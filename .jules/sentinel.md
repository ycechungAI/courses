## 2026-07-22 - [Improper LLM Prompt Sanitization with html.escape()]
**Vulnerability:** User inputs were sanitized using `html.escape()` before being inserted into LLM prompts. This escapes characters into HTML entities (e.g., `&lt;`) which degrade prompt quality, introduce unnatural syntax, and can break evaluation tests since LLMs process text/tokens, not HTML.
**Learning:** `html.escape()` should not be used for LLM prompt inputs. It is for HTML contexts.
**Prevention:** Mitigate XML prompt injection by explicitly stripping structural characters like `<` and `>` from user inputs (e.g., `str(input).replace('<', '').replace('>', '')`).
## 2024-05-22 - [Prompt Injection in Evaluation Scripts]
**Vulnerability:** Evaluation scripts like `custom_llm_eval.py` construct prompts using f-strings with XML-like tags (`<summary>{summary}</summary>`). Unsanitized inputs containing closing tags (e.g., `</summary>`) can break the prompt structure and inject instructions.
**Learning:** Even internal evaluation tools need input sanitization to prevent structure confusion, especially when grading potentially adversarial inputs.
**Prevention:** Always use `str(input).replace('<', '').replace('>', '')` or similar sanitization on variable inputs before inserting them into XML-structured prompts to avoid structural tags, instead of using `html.escape()`.
## 2024-03-04 - Prompt Injection Vulnerability in XML tags
**Vulnerability:** User inputs were placed directly inside XML tags in LLM prompts without sanitization.
**Learning:** If a user input contains XML-like tags, it could confuse the LLM's understanding of the prompt structure and break prompt logic.
**Prevention:** Use `str(input).replace('<', '').replace('>', '')` when inserting user inputs into prompts, particularly when the prompt structure relies on XML tags, avoiding `html.escape()`.
