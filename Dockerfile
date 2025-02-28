# syntax = docker/dockerfile-upstream:1-labs

FROM python:3.12-alpine
WORKDIR /app
STOPSIGNAL SIGTERM
ENV ENV=/app/.profile
RUN \
	--mount=type=cache,target=/var/cache/apk,sharing=locked \
	--mount=type=cache,target=/app/.cache/pip,uid=1000,gid=1000,sharing=locked \
	<<-EOF
	addgroup --gid 1000 rl
	adduser --disabled-password --home /app --uid 1000 --ingroup rl rl
	chown -R rl:rl /app
	pip install -U pip setuptools
EOF

COPY --chown=app:app ./pyproject.toml /app/pyproject.toml
COPY --chown=app:app ./requirements /app/requirements
COPY --chown=app:app ./rl /app/rl
USER rl
RUN --mount=type=cache,target=/app/.cache/pip,uid=1000,gid=1000,sharing=locked \
	pip install --no-warn-script-location -Ue .
ENTRYPOINT ["/usr/local/bin/python3", "-m", "rl"]
