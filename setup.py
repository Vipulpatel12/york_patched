from setuptools import setup,find_packages

setup(
    name='york_patched',
    url='https://github.com/Vipulpatel12/york_patched',
    author='Vipul Patel',
    author_email='vipul108patel.vp@gmail.com',
    packages=['patchwork',
              'patchwork/steps','patchwork/steps/AnalyzeImpact','patchwork/steps/CallAPI','patchwork/steps/CallCode2Prompt','patchwork/steps/CommitChanges','patchwork/steps/CreateIssue','patchwork/steps/CreateIssueComment',
              'patchwork/patchflows','patchwork/patchflows/AutoFix','patchwork/patchflows/DependencyUpgrade','patchwork/patchflows/GenerateDocstring','patchwork/patchflows/GenerateREADME','patchwork/patchflows/PRReview','patchwork/patchflows/ResolveIssue','patchwork/patchflows/GenerateUnitTests','patchwork/steps/CallLLM','patchwork/steps/ExtractModelResponse','patchwork/steps/PreparePR','patchwork/steps/PreparePrompt','patchwork/steps/ReadPRDiffs','patchwork/steps/CreatePR','patchwork/steps/PreparePrompt','patchwork/steps/PreparePR','patchwork/steps/CreatePRComment','patchwork/steps/Combine',
              'patchwork/common','patchwork/common/client/llm','patchwork/common/context_strategy','patchwork/common/utils','patchwork/steps/ExtractDiff','patchwork/steps/ExtractPackageManagerFile','patchwork/steps/FilterBySimilarity','patchwork/steps/ExtractCode','patchwork/steps/ExtractCodeContexts','patchwork/steps/ExtractCodeMethodForCommentContexts','patchwork/steps/GenerateCodeRepositoryEmbeddings','patchwork/steps/GenerateEmbeddings','patchwork/steps/GetTypescriptTypeInfo','patchwork/steps/JoinList','patchwork/steps/LLM','patchwork/steps/ModifyCode','patchwork/steps/ModifyCodeOnce','patchwork/steps/PR','patchwork/steps/QueryEmbeddings','patchwork/steps/SimplifiedLLM','patchwork/steps/ReadFile','patchwork/steps/ReadIssues','patchwork/steps/ReadPRs','patchwork/steps/ScanDepscan','patchwork/steps/ScanSemgrep','patchwork/steps/SlackMessage'],
    include_package_data=True,
    version='1.0.1',
    license='MIT',
    description='An example of a python package from pre-existing code',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown', 
    classifiers=[                        # Metadata about the package
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
