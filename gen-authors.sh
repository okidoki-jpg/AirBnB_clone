#!/bin/bash
# Original Source
# https://github.com/docker/docker/blob/master/hack/generate-authors.sh

{
	cat <<- 'EOH'
		# This file lists all individuals having contributed to the repository.
		# For how it is generated, see `gen-authors.sh`.
		EOH
		echo
		git log --format='%aN - <%aE>' | LC_ALL=C.UTF-8 sort -uf
} > AUTHORS
