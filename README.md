# Tic-Tac-Toe

A simple graphical Tic-Tac-Toe game.

## Docker

```sh
podman build -t tic-tac-toe .
podman run --rm -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=$DISPLAY localhost/tic-tac-toe:latest
```
