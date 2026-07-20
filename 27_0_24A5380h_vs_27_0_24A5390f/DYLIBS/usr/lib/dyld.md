## dyld

> `/usr/lib/dyld`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__DATA_CONST.__const`
- `__AUTH_CONST.__const`
- `__DATA.__data`
- `__DATA_DIRTY.__data`
- `__DATA_DIRTY.__all_image_info`

```diff

-27059.3.0.0.0
+27060.1.0.0.0
   __TEXT.__text: 0x9e8bc
   __TEXT.__const: 0x1978
-  __TEXT.__cstring: 0x12497
+  __TEXT.__cstring: 0x12499
   __TEXT.__unwind_info: 0x35b0
   __DATA_CONST.__const: 0x5590
   __AUTH_CONST.__const: 0x2758
CStrings:
+ "27060.1"
+ "@(#)VERSION:Darwin Ignition Sequence Version 1.0.0: Tue Jul 14 21:12:31 PDT 2026; root:libignition-64~11776/libignition_core/RELEASE_ARM64E"
+ "Darwin Ignition Sequence Version 1.0.0: Tue Jul 14 21:12:31 PDT 2026; root:libignition-64~11776/libignition_core/RELEASE_ARM64E"
- "27059.3"
- "@(#)VERSION:Darwin Ignition Sequence Version 1.0.0: Wed Jul  1 23:22:14 PDT 2026; root:libignition-64~9224/libignition_core/RELEASE_ARM64E"
- "Darwin Ignition Sequence Version 1.0.0: Wed Jul  1 23:22:14 PDT 2026; root:libignition-64~9224/libignition_core/RELEASE_ARM64E"
```
