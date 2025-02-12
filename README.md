York-Patched automates development gruntwork like PR reviews, bug fixing, security patching, and more using a self-hosted CLI agent and your preferred LLMs. Try the hosted version [here](https://app.patched.codes/signin).

## Key Components

- **Steps**: Reusable atomic actions like create PR, commit changes or call an LLM.
- **Prompt Templates**: Customizable LLM prompts optimized for a chore like library updates, code generation, issue analysis or vulnerability remediation.
- **Patchflows**: LLM-assisted automations such as PR reviews, code fixing, documentation etc. built by combining steps and prompts.

## Installation

### Using Pip

The following optional dependency groups are available.

- `security`: Installs `semgrep` and `depscan` with `pip York-Patched 'patchwork-cli[security]'` and is required for **AutoFix** and **DependencyUpgrade** patchflows.
- `rag`: Installs `chromadb` with `pip install 'patchwork-cli[rag]'` and is required for the **ResolveIssue** patchflow.
- `notifications`: Used by steps sending notifications, e.g. slack messages.
- `all`: installs everything.
- Not specifying any dependency group (`pip install patchwork-cli`) will install a core set of dependencies that are sufficient to run the **GenerateDocstring** and **GenerateREADME** patchflows.

### Using Poetry

If you'd like to build from source using poetry, please see detailed documentation [here](INSTALL.md) .

## York-Patched CLI

The CLI runs Patchflows, as follows:

```
patchwork <PatchFlow> <?Arguments>
```

Where
- **Arguments**: Allow for overriding default/optional attributes of the Patchflow in the format of `key=value`. If `key` does not have any value, it is considered a boolean `True` flag.

### Example

For an GenerateDocstring patchflow which patches vulnerabilities based on a scan using Semgrep:

```bash
patchwork GenerateDocstring openai_api_key=<YOUR_OPENAI_API_KEY>  gerrit_username=<GERRIT_USERNAME>  gerrit_http_password=<GERRIT_PASSWORD>
```

## Patchflows

York-Patched comes with predefined patchflows, with more added over time. Sample patchflows include:

- [**GenerateDocstring**](patchwork/patchflows/GenerateDocstring): Generate docstrings for methods in your code.
- [**GenerateREADME**](patchwork/patchflows/GenerateREADME): Create a README markdown file for a given folder, to add documentation to your repository.

## Prompt Templates

Prompt templates are used by patchflows and passed as queries to LLMs. Templates contain prompts with placeholder variables enclosed by `{{}}` which are replaced by the data from the steps or inputs on every run. 

Below is a sample prompt template:

```json
{
  "id": "diffreview_summary",
    "prompts": [
      {
        "role": "user",
        "content": "Summarize the following code change descriptions in 1 paragraph. {{diffreviews}}"
      }
    ]
}
```

Each patchflow comes with an optimized default prompt template. But you can specify your own using the `prompt_template_file=/path/to/prompt/template/file` option. 

## Contributing

Contributions for new patchflows and steps, or to the core framework are welcome. Please look at open issues for details.

- To create a new patchflow, follow [these instructions](patchwork/patchflows/README.md).
- To create a new step, follow [these instructions](patchwork/steps/README.md).

## Roadmap

### Short Term
- Expand patchflow library and integration options
- Patchflow debugger and validation module
- Bug fixing and performance improvements
- Refactor code and documentation

### Long Term
- Support large-scale code embeddings in patchflows
- Support parallelization and branching
- Fine-tuned models that can be self-hosted
- Open-source GUI
