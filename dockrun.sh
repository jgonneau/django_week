#!/bin/bash
git submodule init;
git submodule update;
docker-compose build;
docker-compose up -d;
