## dyld

> `/usr/lib/dyld`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__cstring`
- `__DATA_CONST.__const`
- `__AUTH_CONST.__const`
- `__DATA.__data`

```diff

-27059.3.0.0.0
+27060.0.0.0.0
   __TEXT.__text: 0xa5334
   __TEXT.__const: 0x1a38
   __TEXT.__cstring: 0x137aa
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.tCuco9/Binaries/libignition/install/Symbols/ignition_core"
+ "27060"
+ "@(#)VERSION:Darwin Ignition Sequence Version 1.0.0: Tue Jul 14 21:20:30 PDT 2026; root:libignition-64~11775/libignition_core/RELEASE_ARM64E"
+ "Darwin Ignition Sequence Version 1.0.0: Tue Jul 14 21:20:30 PDT 2026; root:libignition-64~11775/libignition_core/RELEASE_ARM64E"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.tOgvla/Binaries/libignition/install/Symbols/ignition_core"
- "27059.3"
- "@(#)VERSION:Darwin Ignition Sequence Version 1.0.0: Mon Jun 29 21:04:38 PDT 2026; root:libignition-64~8882/libignition_core/RELEASE_ARM64E"
- "Darwin Ignition Sequence Version 1.0.0: Mon Jun 29 21:04:38 PDT 2026; root:libignition-64~8882/libignition_core/RELEASE_ARM64E"
```
