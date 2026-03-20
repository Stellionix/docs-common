# Configuration

## DeadChest - Configuration

Make sure you have installed the plugin before editing the configuration.

You can edit `config.yml` in the plugin folder. After any change, run `/dc reload`.

### Global

| Key | Type | Default | Description |
| --- | --- | --- | --- |
| `config-version` | integer | `2` | Configuration schema version. |

### Localization

| Key | Type | Default | Description |
| --- | --- | --- | --- |
| `localization.language` | string | `en` | Language file loaded from `plugins/DeadChest/localization/<language>.json`. |

### Chest

| Key | Type | Default | Description |
| --- | --- | --- | --- |
| `chest.owner-only-open` | boolean | `true` | Only owner can open chest except bypass permission. |
| `chest.duration-seconds` | integer | `300` | Chest lifetime in seconds. `0` means infinite. |
| `chest.block-type` | string | `chest` | `chest`, `player-head`, `barrel`, `shulker-box`, `ender-chest`. |

### Permissions

| Key | Type | Default | Description |
| --- | --- | --- | --- |
| `permissions.require-generate` | boolean | `false` | Require `deadchest.generate` on death. |
| `permissions.require-claim` | boolean | `false` | Require `deadchest.get` to retrieve items. |

### Visuals

| Key | Type | Default | Description |
| --- | --- | --- | --- |
| `visuals.effect-animation.enabled` | boolean | `true` | Enable orbit particles around active chests. |
| `visuals.pickup-animation.enabled` | boolean | `true` | Enable animation when a player claims a chest. |
| `visuals.sound.pickup.enabled` | boolean | `true` | Enable pickup sound. |

### Filters

| Key | Type | Default | Description |
| --- | --- | --- | --- |
| `filters.excluded-worlds` | list | example values | Worlds where generation is disabled. |
| `filters.excluded-items` | list | example values | Items not stored in DeadChest. |
| `filters.ignored-items` | list | example values | Items that keep vanilla death behavior. |

!!! note "Permission reference"
    `deadchest.admin`, `deadchest.generate`, `deadchest.get`,
    `deadchest.list.own`, `deadchest.list.other`, `deadchest.remove.own`,
    `deadchest.remove.other`, `deadchest.giveback`, `deadchest.chestPass`.
