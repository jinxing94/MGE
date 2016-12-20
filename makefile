ifeq ($(shell uname -s), Darwin)
	CC = clang
else
	CC = gcc
	CFLAGS += -pthread -lm
endif

CFLAGS += -Ofast -std=c99

all: mge.c
	${CC} mge.c ${CFLAGS} -o mge
