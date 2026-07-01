## 2024-05-22 - [Prompt Injection in Evaluation Scripts]
**Vulnerability:** Evaluation scripts like `custom_llm_eval.py` construct prompts using f-strings with XML-like tags (`<summary>{summary}</summary>`). Unsanitized inputs containing closing tags (e.g., `</summary>`) can break the prompt structure and inject instructions.
**Learning:** Even internal evaluation tools need input sanitization to prevent structure confusion, especially when grading potentially adversarial inputs.
**Prevention:** Always use `html.escape()` or similar sanitization on variable inputs before inserting them into XML-structured prompts.
## 2024-03-04 - Prompt Injection Vulnerability in XML tags
**Vulnerability:** User inputs were placed directly inside XML tags in LLM prompts without sanitization.
**Learning:** If a user input contains XML-like tags, it could confuse the LLM's understanding of the prompt structure and break prompt logic.
**Prevention:** Use `html.escape()` when inserting user inputs into prompts, particularly when the prompt structure relies on XML tags.
## 2024-05-24 - [Ineffective HTML escaping in LLM prompts]
**Vulnerability:** `html.escape()` was used to sanitize inputs before inserting them into XML-structured LLM prompts. This is an anti-pattern because LLMs process text and tokens, not HTML. Escaping characters into HTML entities (like `&lt;`) degrades prompt quality, introduces unnatural syntax, can break evaluation tests, and does not provide real security against prompt injection.
**Learning:** Standard web application sanitization techniques like `html.escape()` are not effective for securing LLM prompts and can negatively impact model performance.
**Prevention:** Avoid using HTML escaping for LLM prompts. Instead, prevent XML injection by stripping `<` and `>` characters from user inputs (e.g., `str(input).replace("<", "").replace(">", "")`), or rely on robust XML tagging conventions and LLM-based sanitization/validation steps.
