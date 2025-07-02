import nox

@nox.session
def tests(session):
    session.install(".", "--group", "test")
    session.run("pytest", *session.posargs)
