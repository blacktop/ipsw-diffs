## dyld

> `/usr/lib/dyld`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`
- `__DATA_CONST.__const`
- `__AUTH_CONST.__const`
- `__DATA.__data`
- `__DATA_DIRTY.__all_image_info`
- `__DATA_DIRTY.__data`

```diff
CStrings:
+ "@(#)VERSION:Darwin Ignition Sequence Version 1.0.0: Sat Jul 11 14:52:06 PDT 2026; root:libignition-58~38555/libignition_core/RELEASE_ARM64E"
+ "Darwin Ignition Sequence Version 1.0.0: Sat Jul 11 14:52:06 PDT 2026; root:libignition-58~38555/libignition_core/RELEASE_ARM64E"
- "@(#)VERSION:Darwin Ignition Sequence Version 1.0.0: Thu Jul  9 23:19:47 PDT 2026; root:libignition-58~38524/libignition_core/RELEASE_ARM64E"
- "Darwin Ignition Sequence Version 1.0.0: Thu Jul  9 23:19:47 PDT 2026; root:libignition-58~38524/libignition_core/RELEASE_ARM64E"
```
