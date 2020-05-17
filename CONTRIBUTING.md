# Important note

If in doubt, and you want to contribute, **just do it**. Send a pull request and
I'll help you out in getting it in order.

# Contributing Guidelines

Based on [git/git's patch guidelines](https://github.com/git/git/blob/master/Documentation/SubmittingPatches)
with a *lot* of scaling down. As this is a general template written for all my
projects, not all may apply.

## Too much?

These rules were mostly written for myself to organise my own commits. If you
want to make a quick pull request, please do it the normal way as you would
anywhere else on GitHub, and I'll help with getting it nicely formatted as
below. The pull request template (if present) should help with this.

## Branches

Typically while in active development before the first release, `master` is
where all development happens. After the first release (tagged), development
will usually happen in feature branches that will be pull requested to master
after checks and tests.

## Formatting

Typically all formatting should follow:

- Hard tabs for indentation, not spaces.
- Spaces for alignment (e.g. aligning comments in a series of statements)
- NO trailing whitespace
- Newline at end of file
- Braces on new line (e.g. in C/C++)

For variable naming, follow the language convention and/or see existing files to
infer the preferred naming style.

If there is a separate formatting document or something like `.clang_format` or
a rustfmt configuration, follow that instead.

These rules are overwritten by specific language recommendations (e.g. 2 spaces
for indentation and brace on same line in Scala, 4 spaces for indent in Python).

If in doubt, check existing files and infer.

## Base branch

In general, always base your work on the oldest branch that your
change is relevant to.

- A bugfix should be based on the latest release tag in general. For example, if
  `v0.2.3` and `v0.2.4` tags are present, base the bug fix on `v0.2.4`. If the
  bug is not present in the latest release, base it on `master`. For a bug
  that's not yet in `master`, find the branch that the bug is found in and base
  your work on the tip of that branch.

- A new feature should be based on `master` in general. If the new feature
  depends on another branch, base your work on the tip of that branch.

## Separate commits

Unless your change is really trivial, every pull request should contain a series
of commits with complete commit messages.

If your description starts to get too long, that's a sign that you probably need
to split up your commit to finer grained pieces. Ensure that the description
summarizes the changes well and adheres to the commit message format described
below.

## Commit message

The first line of the commit should be a short description in imperative form,
with a prefixed "area: " describing the file / area of code being modified, e.g.

- docs: add usage examples
- README.md: fix typos in Usage
- src/main.c: improve error handling

Both the imperative summary and area prefix should begin in lowercase unless the
filename is capitalized.

The commit body should list specific changes made with bullet points.

For example,

```
src/main.c: improve error handling

- Remove ungraceful exit upon invalid input
- Add error message describing expected input
```

## Imperative mood

Describe your changes in imperative mood, e.g. "make xyzzy do frotz" instead of
"[This patch] makes xyzzy do frotz" or "[I] changed xyzzy to do frotz", as if
you are giving orders to the codebase to change its behavior. Try to make sure
your explanation can be understood without external resources.

