## otherbsd

> `/usr/libexec/otherbsd`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-3298.0.21.0.0
+3298.1.1.0.0
   __TEXT.__text: 0x1518
   __TEXT.__auth_stubs: 0x4a0
   __TEXT.__objc_stubs: 0x40
   __TEXT.__const: 0x48
-  __TEXT.__cstring: 0x558
+  __TEXT.__cstring: 0x556
   __TEXT.__oslogstring: 0xc5
   __TEXT.__objc_methname: 0x2d
   __TEXT.__unwind_info: 0xb0
CStrings:
+ "@(#)VERSION:Darwin Auxiliary Bootstrapper Version 1.0.0: Mon Aug 10 01:08:25 PDT 2026; root:libxpc_executables-3298.1.1~29/otherbsd/RELEASE_ARM64E"
+ "Darwin Auxiliary Bootstrapper Version 1.0.0: Mon Aug 10 01:08:25 PDT 2026; root:libxpc_executables-3298.1.1~29/otherbsd/RELEASE_ARM64E"
- "@(#)VERSION:Darwin Auxiliary Bootstrapper Version 1.0.0: Mon Jul 13 21:49:06 PDT 2026; root:libxpc_executables-3298.0.21~90/otherbsd/RELEASE_ARM64E"
- "Darwin Auxiliary Bootstrapper Version 1.0.0: Mon Jul 13 21:49:06 PDT 2026; root:libxpc_executables-3298.0.21~90/otherbsd/RELEASE_ARM64E"
```
