## dyld

> `/usr/lib/dyld`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`

```diff
CStrings:
+ "@(#)VERSION:Darwin Ignition Sequence Version 1.0.0: Thu Aug 13 22:12:59 PDT 2026; root:libignition-64~19689/libignition_core/RELEASE_ARM64E"
+ "Darwin Ignition Sequence Version 1.0.0: Thu Aug 13 22:12:59 PDT 2026; root:libignition-64~19689/libignition_core/RELEASE_ARM64E"
- "@(#)VERSION:Darwin Ignition Sequence Version 1.0.0: Wed Aug  5 21:46:56 PDT 2026; root:libignition-64~17995/libignition_core/RELEASE_ARM64E"
- "Darwin Ignition Sequence Version 1.0.0: Wed Aug  5 21:46:56 PDT 2026; root:libignition-64~17995/libignition_core/RELEASE_ARM64E"
```
