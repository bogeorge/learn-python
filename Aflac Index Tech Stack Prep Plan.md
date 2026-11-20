# Aflac Index Tech Stack Prep Plan

Nov 18, 2026 · @Bo

## Where to spend the time

Window: Nov 18 to your start date (about three weeks, with Thanksgiving in week 2). Assumes roughly 1 to 1.5 hours a day; scale up or down. Aflac Index is very likely the Datacap replacement (AI document extraction is "integral"), so every exercise below uses documents, not toy chat apps.

| Area | Where you are | Time share | Goal by day one |
| --- | --- | --- | --- |
| Python | Little | 35% | Read and write idiomatic, typed Python Lambdas without looking things up constantly. |
| Bedrock + Claude document extraction | None | 30% | Explain and build a PDF/image to validated JSON pipeline, with cost and accuracy trade-offs. |
| Agents + AI coding tools (Kiro, Copilot) | Some general AI use | 15% | Comfortable with spec-driven work in Kiro and agent mode in Copilot; know Strands/AgentCore vocabulary. |
| AWS infra + Lambda | Solid | 10% | Refresh on the serverless pieces an IDP pipeline uses; learn the IaC tool they use once you know it. |
| React / Angular | Solid | 10% | Catch up on recent Angular changes (standalone components, signals); no React work needed. |

**Principle:** your differentiator on this team is not knowing Python syntax. It is that you already understand capture (batches, verification, downstream contracts) from the Datacap study guide and can connect that to LLM extraction. Lean into that.

## Week 1 (Nov 18 to 24): Python for a TypeScript engineer

Learn it by mapping, not from zero.

| TypeScript / Node | Python equivalent to learn | Docs |
| --- | --- | --- |
| npm, package.json, node_modules | uv (or pip + venv), pyproject.toml, virtual environments | [uv](https://docs.astral.sh/uv/) · [venv](https://docs.python.org/3/library/venv.html) · [Writing pyproject.toml](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/) |
| tsc / strict mode | Type hints + mypy or pyright | [typing module](https://docs.python.org/3/library/typing.html) · [mypy](https://mypy.readthedocs.io/en/stable/) · [pyright](https://microsoft.github.io/pyright/) |
| Zod | Pydantic models (this matters most: it is how you define extraction schemas) | [Pydantic docs](https://docs.pydantic.dev/latest/) · [Models](https://docs.pydantic.dev/latest/concepts/models/) |
| Jest / Vitest | pytest, fixtures, parametrize | [pytest](https://docs.pytest.org/en/stable/) · [Fixtures](https://docs.pytest.org/en/stable/how-to/fixtures.html) · [Parametrize](https://docs.pytest.org/en/stable/how-to/parametrize.html) |
| async/await, Promise.all | asyncio, gather; note most Lambda Python code is sync | [asyncio](https://docs.python.org/3/library/asyncio.html) · [Coroutines, tasks and gather](https://docs.python.org/3/library/asyncio-task.html) |
| AWS SDK v3 | boto3 (clients, paginators, waiters) | [boto3 docs](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) · [Paginators](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/paginators.html) |
| ESLint + Prettier | ruff (lint + format) | [ruff](https://docs.astral.sh/ruff/) |
| Lambda handler in TS | Lambda handler in Python, layers vs container images, Powertools for AWS Lambda | [Lambda with Python](https://docs.aws.amazon.com/lambda/latest/dg/lambda-python.html) · [Python layers](https://docs.aws.amazon.com/lambda/latest/dg/python-layers.html) · [Python container images](https://docs.aws.amazon.com/lambda/latest/dg/python-image.html) · [Powertools](https://docs.powertools.aws.dev/lambda/python/latest/) |

**Daily rhythm:**

1. Day 1 to 2: Python tutorial essentials (data structures, comprehensions, dataclasses, exceptions, modules). Skip what you already know conceptually.
2. Day 3: Typing, Pydantic v2, validation errors.
3. Day 4: pytest; write tests for a small parsing module.
4. Day 5 to 6: boto3 + Lambda. Port one of your own TS Lambdas to Python with Powertools, deploy it, add a test.
5. Day 7: Use Kiro or Copilot to review your Python and explain what is unidiomatic. Good practice for both.

## Week 2 (Nov 25 to Dec 1): Bedrock + Claude document extraction

Lighter week for Thanksgiving, but this is the core of the job.

**Concepts to own:**

- **Bedrock basics.** Model access per account/region, IAM permissions, model IDs and inference profiles, quotas, pricing per input/output token.
- **Converse API.** The model-agnostic chat API in boto3. Learn message structure, system prompts, document blocks (PDF) and image blocks.
- **PDF and image input.** Claude on Bedrock reads PDFs including charts and tables, and Bedrock added Citations support for Claude in mid-2025. Understand the difference between text-only and full visual document processing modes, and when to send page images instead.
- **Getting reliable JSON.** Tool use (define a tool whose input schema is your Pydantic model) and native structured outputs. Then validate with Pydantic and retry on failure.
- **Classification + extraction.** Classify pages or packets first, then extract per document type. Same shape as Datacap's PageID > Recognize steps.
- **Confidence and human review.** LLMs do not give per-field OCR confidence. Learn the patterns: self-assessment prompts, cross-checks against lookups, validation rules, and routing low-confidence results to a reviewer (A2I or a custom UI).
- **Cost and scale.** Token math per page, prompt caching for long shared instructions, batch inference for non-urgent volume, Haiku vs Sonnet vs Opus tiering.
- **Evaluation.** A golden set of labeled documents and field-level accuracy metrics. This is how you will prove you beat Datacap.
- **Data protection.** PHI in prompts, logging hygiene, Guardrails, encryption, VPC endpoints. Expect this to be scrutinized at Aflac.

**Hands-on:**

1. Get Bedrock access in a personal AWS account and enable a Claude model.
2. Send a PDF via the Converse API and get a summary.
3. Define a Pydantic schema for a claim-like form, extract via tool use, validate, and log token usage.
4. Read the AWS GenAI IDP Accelerator "Pattern 2" (Bedrock classification + extraction with Claude). It is close to what Aflac Index likely looks like.

Use synthetic or blank public forms only. No real PHI in a personal account.

## Week 3 (Dec 2 to 8): agents, AI coding tools, infra, Angular

**AI coding tools (Kiro and Copilot).** The email says agents are used heavily to write the app, so fluency here is table stakes.

- **Kiro:** AWS's agentic IDE built on VS Code. Its core idea is spec-driven development: a prompt becomes requirements.md, design.md and tasks.md, then agents implement the tasks. Learn specs, *steering files* (project rules the agent follows), *agent hooks* (event-driven automations like generating tests on save) and MCP integrations. Build your capstone with it.
- **Copilot:** agent mode, custom instructions files, and code review. Try the same small feature in both tools and note where each is better.
- **Prompt engineering for frontier models:** clear role and task, explicit output schema, examples of edge cases, XML-tagged sections, asking for reasoning before answers when accuracy matters. Anthropic's prompt engineering guide is the reference since the models are Claude.

**Agents on AWS (vocabulary level).**

- **Strands Agents:** AWS's open-source Python SDK for writing agents (model + tools + loop).
- **Bedrock AgentCore:** managed platform to run agents in production (runtime, memory, gateway, identity, observability). Generally available since Oct 2025.
- **MCP:** how agents and IDEs connect to tools and data. Kiro uses it.

**AWS infra refresh (half a day).** S3 events, SQS, Step Functions (Map state for per-page fan-out), DynamoDB, API Gateway, IAM least privilege, CloudWatch. Ask which IaC tool they use (CDK, SAM or Terraform) before investing in one.

**Angular refresh (half a day).** Standalone components, signals, new control flow syntax, and whatever Angular version the team is on. React needs nothing from you.

## Capstone: a mini Aflac Index

Build it across weeks 2 and 3, using Kiro specs to drive the work. It exercises every item in the email.

1. Upload a PDF or phone photo of a claim-like form to S3.
2. S3 event triggers a Python Lambda (Powertools for logging and tracing).
3. Lambda calls Claude on Bedrock: classify the document, then extract fields into a Pydantic schema via tool use.
4. Validate: required fields, formats, a fake policy-number lookup. Mark anything failing or low confidence for review.
5. Store results and status in DynamoDB.
6. Small Angular (or React) review screen: image on the left, fields on the right, approve or correct.
7. Track tokens and cost per document, and accuracy against 10 to 20 hand-labeled samples.

**Stretch:** wrap extraction in a Strands agent that can call a lookup tool, and compare its accuracy and cost to the plain Lambda call.

You will arrive with real opinions on cost, accuracy, latency and failure modes, which is worth more than any course.

## Questions to bring on day one

1. Is Aflac Index the Datacap replacement, or a separate product that uses some of the same capture?
2. Which Claude models and regions are approved on Bedrock? Any cross-region inference restrictions?
3. What are the rules for PHI in prompts, logs and test data? Is there a sanctioned sandbox with synthetic data?
4. How is extraction quality measured today? Is there a golden set and an evaluation harness?
5. Which parts are Angular and which are React, and why both?
6. IaC tool, Python version, package manager, and testing standards?
7. Are agents part of the runtime (Strands, AgentCore, LangGraph?) or only used for writing code?
8. Kiro vs Copilot: is there a team standard, shared steering files or instruction files, and a policy on what code agents may touch?
9. How do humans review extractions today, and who owns that UI?

## Resources

**Python**

- [Python official tutorial](https://docs.python.org/3/tutorial/)
- [Pydantic docs](https://docs.pydantic.dev/)
- [Powertools for AWS Lambda (Python)](https://docs.powertools.aws.dev/lambda/python/latest/)

**Bedrock + Claude extraction**

- [Claude PDF support (includes the Bedrock section)](https://platform.claude.com/docs/en/build-with-claude/pdf-support.md)
- [AWS: Citations API and PDF support for Claude in Bedrock](https://aws.amazon.com/about-aws/whats-new/2025/06/citations-api-pdf-claude-models-amazon-bedrock)
- [GenAI IDP Accelerator, Pattern 2: Bedrock classification and extraction](https://aws-solutions-library-samples.github.io/accelerated-intelligent-document-processing-on-aws/pattern-2)
- [AWS blog: Intelligent document processing with Bedrock and Claude](https://aws.amazon.com/blogs/machine-learning/intelligent-document-processing-using-amazon-bedrock-and-anthropic-claude)
- [AWS blog: Scalable IDP with Bedrock and human review (A2I)](https://aws.amazon.com/blogs/machine-learning/scalable-intelligent-document-processing-using-amazon-bedrock/)
- [Instructor: structured outputs with Bedrock](https://python.useinstructor.com/integrations/bedrock/)
- [Anthropic prompt engineering overview](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/overview)

**Agents and tools**

- [Strands: deploy to Bedrock AgentCore (Python)](https://strandsagents.com/docs/user-guide/deploy/deploy_to_bedrock_agentcore/python/)
- [AWS News: Introducing Bedrock AgentCore](https://aws.amazon.com/de/blogs/aws/introducing-amazon-bedrock-agentcore-securely-deploy-and-operate-ai-agents-at-any-scale/)
- [Strands Agents vs AgentCore explained](https://builder.aws.com/content/3CJ46VRteYg1vg0FIqbvcQBrGt8/strands-agents-and-agentcore-two-pieces-of-the-same-puzzle)
- [Kiro: spec-driven development (Marc Brooker)](https://kiro.dev/blog/kiro-and-the-future-of-software-development/)
- [AWS Builder: Kiro specs, hooks and MCP](https://builder.aws.com/content/3IzauLJFRVlmhL4uZ5rnehxfLMT/aws-kiro-transforming-ai-assisted-development-with-spec-driven-engineering)
