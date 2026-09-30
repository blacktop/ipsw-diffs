## dyld

> `usr/lib/dyld`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`

```diff
CStrings:
+ "@(#)VERSION:Darwin Ignition Sequence Version 1.0.0: Tue Aug 18 16:43:47 PDT 2026; root:libignition-58~38639/libignition_core/RELEASE_ARM64E"
+ "Darwin Ignition Sequence Version 1.0.0: Tue Aug 18 16:43:47 PDT 2026; root:libignition-58~38639/libignition_core/RELEASE_ARM64E"
- "@(#)VERSION:Darwin Ignition Sequence Version 1.0.0: Thu Aug 13 21:22:22 PDT 2026; root:libignition-58~38630/libignition_core/RELEASE_ARM64E"
- "Darwin Ignition Sequence Version 1.0.0: Thu Aug 13 21:22:22 PDT 2026; root:libignition-58~38630/libignition_core/RELEASE_ARM64E"
```
