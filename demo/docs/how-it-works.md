# How It Works

## Runtime Flow

This page is useful to validate medium-density explanatory content.

1. A player dies.
2. The plugin evaluates generation rules and integrations.
3. Items are either stored, filtered or ignored.
4. A temporary chest or equivalent container is created.
5. Recovery, timeout and cleanup policies apply afterward.

## Decision Points

| Stage | What is evaluated |
| --- | --- |
| Death | World, game mode, permissions, PvP |
| Storage | Filters, ignored items, capacity, target block |
| Retrieval | Ownership, bypass permission, timeout state |

!!! info "Why this page matters"
    Technical documentation rarely looks like a landing page. This type of page
    helps validate the pacing of headings, paragraphs and tables.
