# code-snap-action

This action snaps all the source files in a particular folder and saves them into another folder inside the workflow

## USAGE
```yml
Sample workflow file

name: CODE SNAP CI
on:
  push:
    branches: [ master ]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - name: Checkout
      uses: actions/checkout@v2
    - name: Generate pngs
      uses: sharadcodes/code-snap-action@v1.0
      with:
        source_folder: "my_code_files" # This field is required and it is the folder which contains the source files.
        output_folder: "snaps" # This field is required and it is the folder which contains the snaps.
        syntax_theme: "emacs" # This field is required and it is the syntax highlighting theme that will be used.
```
