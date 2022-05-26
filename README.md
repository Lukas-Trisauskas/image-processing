## Image Processing
by Lukas Trišauskas, Thomas Nadin-Hepburn, Nicolas Suckling, John Merritt

## Workflow

![GitHub Workflow-2](https://user-images.githubusercontent.com/76224796/170488702-f753c7c3-a575-4a14-a078-1012850c244e.png)

[ !! ] The image-processing repository consists of three branches

- Main: also known as the production branch, it contains live, working version of the app, you can only merge to it after a code review has been completed and no more changes need to be made.
- Development: the default branch with the latest features and bug fixes that haven't been merged to production yet.
- Test: contains unit tests for all features, before any changes are merged to production, it must undergo testing.
- 
## Temporary Branches

[ !! ] When adding a new feature, trying to fix a bug, or adding a hotfix, always create a new branch and use the following naming conventions for branch names<br>

adding new feature: <br>
    
    feature_name_of_the_feature
    
bug fix: <br>

    bug_name_of_the_bug

hotfix: <br>

    hotfix_name_of_the_hotfix
    
## Creating a new branch

For example, if you wanted to add a new feature, you would create a new branch and name it e.g.

    git checkout -b feature_name_of_the_feature

Another example, if you wanted to add a bug fix, I would create a new branch and name it e.g.

    git checkout -b -bug_name_of_the_bug


## Semantic Versioning

![Blank diagram-3](https://user-images.githubusercontent.com/76224796/170488815-48c4b882-3fa0-4165-b490-e62c6699fc9f.png)

Major refers to when a working version of the app is released. Increment once develop branch has been merged with main branch. 

Minor refers to when new functionality or improvements have been introduced. Increment only when adding a new feature or making improvements to existing code. Patch is reset to 0 when minor version is incremented.

Patch refers to when bug fixes are introduced (a bug fix is defined as an internal change that fixes incorrect behaviour). Increment only when merging bug fix with main branch.

## Standards

### Variables<br>
The naming convention that will be used for variables is `snake_case`.<br>

    my_variable = 0
    my_variable_second = 0

### Functions<br>
The naming convention that will be used for naming functions is `camelCase`.<br>

    def myFunction():
      ...

### Classes<br>
The naming convention that will be used for naming classes is `CamelCase`, unlike the function naming convention, for classes all words must start with a capital letter.<br>

    class MyClass():
      ...

