#! /bin/bash

python3 -m venv .venv

./.venv/bin/pip3 install flask
if [$? = 0]; then
    echo "Successfully installed flask"
else
    echo "Failed to install flask"
    exit 1
fi
./.venv/bin/pip3 install html-to-markdown
if [$? = 0]; then
    echo "Successfully installed html-to-markdown"
else
    echo "Failed to install html-to-markdown"
    exit 2
fi
./.venv/bin/pip3 install markdown
if [$? = 0]; then
    echo "Successfully installed markdown"
else
    echo "Failed to install markdown"
    exit 3
fi
./.venv/bin/pip3 install calendar
if [$? = 0]; then
    echo "Successfully installed calendar"
else
    echo "Failed to install calendar"
    exit 4
fi
./.venv/bin/pip3 install datetime
if [$? = 0]; then
    echo "Successfully installed datetime"
else
    echo "Failed to install datetime"
    exit 5
fi

echo "Successfully installed all dependencies!"