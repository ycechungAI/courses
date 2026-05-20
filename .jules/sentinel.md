## 2024-05-22 - [Prompt Injection in Evaluation Scripts]
**Vulnerability:** Evaluation scripts like `custom_llm_eval.py` construct prompts using f-strings with XML-like tags (`<summary>{summary}</summary>`). Unsanitized inputs containing closing tags (e.g., `</summary>`) can break the prompt structure and inject instructions.
**Learning:** Even internal evaluation tools need input sanitization to prevent structure confusion, especially when grading potentially adversarial inputs.
**Prevention:** Always use `html.escape()` or similar sanitization on variable inputs before inserting them into XML-structured prompts.
## 2024-03-04 - Prompt Injection Vulnerability in XML tags
**Vulnerability:** User inputs were placed directly inside XML tags in LLM prompts without sanitization.
**Learning:** If a user input contains XML-like tags, it could confuse the LLM's understanding of the prompt structure and break prompt logic.
**Prevention:** Use `html.escape()` when inserting user inputs into prompts, particularly when the prompt structure relies on XML tags.
## 2024-05-24 - [Prompt Injection in Jupyter Notebook Tutorials]
**Vulnerability:** Prompt generation logic explicitly detailed in Jupyter notebook lessons (like `prompt_evaluations/05_prompt_foo_code_graded_animals/lesson.ipynb` and `prompt_evaluations/06_prompt_foo_code_graded_classification/lesson.ipynb`) did not sanitize variables using `html.escape()` when inserting them into XML tags in prompt templates, teaching unsafe prompt construction techniques.
**Learning:** Educational materials and code blocks inside Jupyter notebooks must reflect secure implementations since users copy and learn from them. The vulnerability was present in the `.ipynb` files while the actual scripts were protected.
**Prevention:** Always verify and update educational materials (`.ipynb` files) to ensure they mirror the security patches applied to the corresponding source scripts. Ensure `html.escape()` is presented as a fundamental part of prompt construction involving variables and XML structure.
