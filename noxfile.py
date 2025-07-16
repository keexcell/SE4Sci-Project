import nox

nox.options.sessions = ["lint", "tests"]


@nox.session
def tests(session):
    session.install(".", "--group", "test")
    session.run("pytest", *session.posargs)


@nox.session
def lint(session: nox.Session) -> None:
    session.install("pre-commit")
    session.run(
        "pre-commit", "run", "--show-diff-on-failure", "--all-files", *session.posargs
    )
