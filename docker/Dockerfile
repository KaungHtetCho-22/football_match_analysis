FROM python:3.12 AS devel

# Install dependencies
RUN apt-get update && apt-get install --no-install-recommends -y sudo libgl1

# Set up user and permissions
ARG USERNAME=football
ARG USER_UID=1000
ARG USER_GID=1000

RUN groupadd -g $USER_GID $USERNAME \
    && useradd -rm -d /home/$USERNAME -s /bin/bash -g $USER_GID -G sudo -u $USER_UID $USERNAME \
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME

USER $USERNAME

WORKDIR /home/$USERNAME

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Production stage
FROM python:3.12 AS prod

# Install dependencies
RUN apt-get update && apt-get install --no-install-recommends -y libgl1

WORKDIR /app

ENV PYTHONPATH=/app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "main.py"]
