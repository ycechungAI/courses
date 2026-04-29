## 2024-05-22 - [Prompt Injection in Evaluation Scripts]
**Vulnerability:** Evaluation scripts like `custom_llm_eval.py` construct prompts using f-strings with XML-like tags (`<summary>{summary}</summary>`). Unsanitized inputs containing closing tags (e.g., `</summary>`) can break the prompt structure and inject instructions.
**Learning:** Even internal evaluation tools need input sanitization to prevent structure confusion, especially when grading potentially adversarial inputs.
**Prevention:** Always use `html.escape()` or similar sanitization on variable inputs before inserting them into XML-structured prompts.
## 2024-03-04 - Prompt Injection Vulnerability in XML tags
**Vulnerability:** User inputs were placed directly inside XML tags in LLM prompts without sanitization.
**Learning:** If a user input contains XML-like tags, it could confuse the LLM's understanding of the prompt structure and break prompt logic.
**Prevention:** Use `html.escape()` when inserting user inputs into prompts, particularly when the prompt structure relies on XML tags.
## 2024-05-22 - [Crash in promptfoo Custom Assert Scripts]
**Vulnerability:** In prompt_evaluations/07_prompt_foo_custom_graders/count.py, the output from the model was assumed to always be a string, and output.lower() was invoked. However, when promptfoo passes a dictionary (e.g. JSON structured output), this throws an AttributeError.
**Learning:** Custom assertion scripts must handle cases where model outputs or pipeline artifacts are passed as dictionaries rather than plain strings. Unhandled exceptions in evaluations could mask underlying logic failures or create denial-of-service in testing pipelines.
**Prevention:** Always verify the type of output (e.g. isinstance(output, dict)) and extract the relevant string or use json.dumps() before performing text operations.
