# API

## DeadChest - API

### API class

```java
public interface DeadChestApi {
    Optional<DeadChest> find(UUID ownerId);
    Collection<DeadChest> list(UUID ownerId);
}
```

### Methods

- `find(UUID ownerId)` returns a single active chest when relevant.
- `list(UUID ownerId)` returns all active chests for a player.
- `remove(UUID chestId)` would typically require an admin use case.

### Events

- `DeadChestCreateEvent`
- `DeadChestClaimEvent`
- `DeadChestExpireEvent`

### Notes

This page is here to validate developer-facing docs with code blocks and compact lists.
