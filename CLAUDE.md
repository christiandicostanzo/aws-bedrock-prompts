# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

A Python project for experimenting with AWS Bedrock (prompting foundation models via the Bedrock Runtime API). The codebase is currently a fresh scaffold — `main.py` is empty and no architecture has been established yet.

## Setup

```bash
pip install -r requirements.txt
```

The only declared dependency is `boto3`, used for the Bedrock and Bedrock Runtime clients. AWS credentials must be configured (via `~/.aws/credentials`, environment variables, or an SSO profile) with access to the target Bedrock models/region before any Bedrock API calls will succeed.

## Running

```bash
python main.py
```
