#!/bin/bash

set -e

script/bootstrap
puppet apply --test --modulepath modules:third-party manifests/site
