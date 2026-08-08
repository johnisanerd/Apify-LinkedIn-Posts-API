# 📝 LinkedIn Posts API: Posts & Engagement to Structured JSON

> The most efficient, reliable, and developer-friendly way to use the LinkedIn Posts API.

**Actor page:** [apify.com/johnvc/linkedin-posts-api](https://apify.com/johnvc/linkedin-posts-api?fpr=9n7kx3)
**Input schema:** [apify.com/johnvc/linkedin-posts-api/input-schema](https://apify.com/johnvc/linkedin-posts-api/input-schema?fpr=9n7kx3)

Give it a public LinkedIn profile URL and it discovers that person's recent posts, or pass specific post URLs to fetch directly. You get back one clean JSON row per post: text, reactions, comments, shares, hashtags, media, and author details. It is built API-first and MCP-ready, so you can call it from Python or drive it as a tool from an AI agent.

## Video Walkthrough

[![Watch the walkthrough](https://img.youtube.com/vi/jREWahDGhJM/maxresdefault.jpg)](https://www.youtube.com/watch?v=jREWahDGhJM)

## Quick Start

### Prerequisites
- Python 3.11 or higher
- An Apify account and API key ([get a free key here](https://apify.com?fpr=9n7kx3))

1. **Clone the repository**
   ```bash
   git clone https://github.com/johnisanerd/Apify-LinkedIn-Posts-API.git
   cd Apify-LinkedIn-Posts-API
   ```

2. **Install dependencies with UV**
   ```bash
   # Install UV if you do not have it:
   curl -LsSf https://astral.sh/uv/install.sh | sh

   # Install project dependencies:
   uv sync
   ```

3. **Configure your API key**
   ```bash
   cp .env.example .env
   # Edit .env and add your Apify API key
   # Get your free API key at: https://apify.com?fpr=9n7kx3
   ```

4. **Run the example**
   ```bash
   uv run python linkedin-posts-api-example.py
   ```

### Alternative: set the API key directly
```bash
export APIFY_API_TOKEN="your_api_key_here"
uv run python linkedin-posts-api-example.py
```

## Why Use This LinkedIn Posts API?

**A URL in, structured data out.** You never touch collection infrastructure. Pass a profile URL (or specific post URLs) and get flat, predictable fields you can load straight into a sheet, a database, or a BI tool.

**Two ways to collect.** Discover a profile's recent posts (newest first, capped and optionally date-filtered), or fetch a known set of posts by URL, up to 1000 per run.

**Pay per post.** Billing is per post returned, with no per-run setup fee, so you only pay for what is delivered.

**Reliable and predictable.** Every post comes back with the same field shape, and a profile with no public posts returns a clear error row instead of failing the whole run.

**MCP-ready.** Call it as a tool from Claude, Cursor, and other AI agents (see the install sections below).

## Features

### Core Capabilities
- Discover a profile's recent posts by profile URL, or fetch specific posts by URL
- Post text, hashtags, media, and links, plus post type and date
- Reactions, comments, and shares on every post
- Author name, headline, follower count, and a sample of top comments

### Data Quality
- One consistent JSON row per post, every time
- A plain-language `summary` field on every row for quick scanning and AI use
- A clear error row for a profile with no public posts, so one empty profile never sinks the batch

## Usage Examples

### Discover a profile's posts
```json
{
  "profileUrls": ["https://www.linkedin.com/in/williamhgates"],
  "maxPostsPerProfile": 5
}
```

### Limit discovery to a date range
```json
{
  "profileUrls": ["https://www.linkedin.com/in/williamhgates"],
  "maxPostsPerProfile": 50,
  "startDate": "2025-01-01",
  "endDate": "2025-12-31"
}
```

### Fetch specific posts by URL
```json
{
  "postUrls": [
    "https://www.linkedin.com/posts/williamhgates_activity-7446904645010210816"
  ]
}
```

## Input Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `profileUrls` | `list[str]` | one of these | - | Public LinkedIn `/in/` profile URLs to discover posts from. Up to 25 per run. |
| `postUrls` | `list[str]` | one of these | - | Specific LinkedIn post URLs to fetch directly. Up to 1000 per run. |
| `maxPostsPerProfile` | `int` | No | `20` | Max posts per profile in discover mode (max 200). Caps cost. Ignored for post URLs. |
| `startDate` | `str` | No | - | Only discover posts on or after this date (YYYY-MM-DD). Discover mode only. |
| `endDate` | `str` | No | - | Only discover posts on or before this date (YYYY-MM-DD). Discover mode only. |

Supply at least one of `profileUrls` or `postUrls`.

## Output Format

Each post is returned as one JSON row:

```json
{
  "result_type": "post",
  "postId": "7446904645010210816",
  "postUrl": "https://www.linkedin.com/posts/williamhgates_activity-7446904645010210816",
  "postType": "post",
  "datePosted": "2025-06-01T12:00:00.000Z",
  "text": "A few books shaped how I think about clean energy this year...",
  "hashtags": ["cleanenergy", "books"],
  "authorName": "williamhgates",
  "authorHeadline": "Co-chair, Bill & Melinda Gates Foundation",
  "authorUrl": "https://www.linkedin.com/in/williamhgates",
  "authorFollowers": 37000000,
  "numLikes": 12045,
  "numComments": 843,
  "numShares": 210,
  "summary": "Post by williamhgates, 12,045 reactions, 843 comments, posted 2025-06-01"
}
```

The `numShares` field is returned when the post has shares.

---

## Install in Claude Cowork Desktop

![Install in Claude Cowork Desktop](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_claude_desktop.png)

Cowork is the desktop app's automation mode. To give it the LinkedIn Posts API as a tool, add the Apify MCP server as a connector.

1. Open the Claude desktop app and go to **Settings → Connectors** (or **Settings → Developer → Edit Config** to edit `claude_desktop_config.json` directly).
   - macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - Windows: `%APPDATA%\Claude\claude_desktop_config.json`
2. Add the Apify MCP server, preloaded with only this Actor:

```json
{
  "mcpServers": {
    "apify": {
      "command": "npx",
      "args": [
        "-y",
        "mcp-remote",
        "https://mcp.apify.com/?tools=actors,docs,johnvc/linkedin-posts-api"
      ]
    }
  }
}
```

3. Restart the app. When Cowork first calls the tool, complete the OAuth prompt in your browser, or add your Apify API token in the connector settings to skip OAuth.
4. In a Cowork chat, confirm the tool is available and ask it to run the LinkedIn Posts API.

Download the desktop app and start a free trial: https://claude.ai/referral/uIlpa7nPLg
More help: https://docs.apify.com/platform/integrations/claude-desktop

---

## Install in Claude Code

![Install in Claude Code](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_claude_code.png)

Claude Code is the command-line tool. Add the Actor's MCP server with one command:

```bash
claude mcp add --transport http apify \
  "https://mcp.apify.com/?tools=actors,docs,johnvc/linkedin-posts-api"
```

To use a token instead of browser OAuth:

```bash
claude mcp add --transport http apify \
  "https://mcp.apify.com/?tools=actors,docs,johnvc/linkedin-posts-api" \
  --header "Authorization: Bearer YOUR_APIFY_TOKEN"
```

Then verify with `claude mcp list`, or run `/mcp` inside a session. Ask Claude Code to call the LinkedIn Posts API.

Try Claude Code free: https://claude.ai/referral/uIlpa7nPLg
Claude Code MCP docs: https://code.claude.com/docs/en/mcp

---

## Install in Claude (website)

![Install in Claude (website)](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_claude_ai.png)

On claude.ai you add Apify as a connector, then enable just this Actor's tool.

1. Go to **Settings → Connectors → Browse connectors** and search for **Apify MCP server**. Install it (enable or update if prompted).
2. When connecting, authenticate with your Apify API token, and enable the tool `johnvc/linkedin-posts-api`.
3. In any chat, open **+ → Connectors** and turn on **Apify**.
4. Alternatively, choose **Add custom connector** and paste the full MCP URL `https://mcp.apify.com/?tools=actors,docs,johnvc/linkedin-posts-api`, using OAuth when prompted.
5. Ask Claude to run the LinkedIn Posts API.

Open Claude on the web: https://claude.ai/referral/uIlpa7nPLg

---

## Install in Cursor

![Install in Cursor](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_cursor.png)

Cursor reads MCP servers from a project file at `.cursor/mcp.json`.

1. In your project, create `.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "apify": {
      "url": "https://mcp.apify.com/?tools=actors,docs,johnvc/linkedin-posts-api"
    }
  }
}
```

2. If you prefer token auth over browser OAuth, add a header:

```json
{
  "mcpServers": {
    "apify": {
      "url": "https://mcp.apify.com/?tools=actors,docs,johnvc/linkedin-posts-api",
      "headers": { "Authorization": "Bearer YOUR_APIFY_TOKEN" }
    }
  }
}
```

3. Open **Cursor → Settings → MCP** and confirm the **apify** server is connected (green dot).
4. In Composer or Chat, ask Cursor to call the LinkedIn Posts API.

New to Cursor? Get it here: https://cursor.com/referral?code=XQP4VBLI3NNX

---

## Install in ChatGPT

![Install in ChatGPT](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_ChatGPT.png)

ChatGPT connects to the Apify MCP server through Developer mode (available on ChatGPT Pro, Plus, Business, Enterprise, and Education plans).

1. Click your profile icon, then go to **Settings > Apps**. If you do not see a **Create app** button, open **Advanced settings** and enable **Developer mode**.
2. Click **Create app** and fill out the form:
   - **Name:** Apify
   - **MCP Server URL:** `https://mcp.apify.com/?tools=actors,docs,johnvc/linkedin-posts-api`
   - **Authentication:** OAuth
3. Click **Create** and authorize the connection with Apify.
4. To use the app in a conversation, click **+** in the chat, choose **Developer mode**, and select **Apify**.

More help: https://docs.apify.com/platform/integrations/mcp

---

[**Made with care**](https://apify.com/johnvc?fpr=9n7kx3)

*Use the LinkedIn Posts API to power your content research, social listening, and engagement analytics with reliable, structured results.*

Last Updated: 2026.08.08
