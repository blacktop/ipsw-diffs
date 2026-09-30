## smd

> `/usr/libexec/smd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-3298.1.1.0.0
+3298.40.20.0.0
   __TEXT.__text: 0x10404
   __TEXT.__auth_stubs: 0xc80
   __TEXT.__objc_stubs: 0x1500

   __TEXT.__objc_classname: 0x1b1
   __TEXT.__objc_methtype: 0xa85
   __TEXT.__objc_methname: 0x14d1
-  __TEXT.__cstring: 0x134d
+  __TEXT.__cstring: 0x1351
   __TEXT.__gcc_except_tab: 0x2dc
   __TEXT.__unwind_info: 0x4a8
   __DATA_CONST.__const: 0x518
CStrings:
+ "@(#)VERSION:Darwin Privileged Tool Bootstrapper Version 2.0.0: Fri Sep  4 20:48:20 PDT 2026; root:libxpc_executables-3298.40.20~23/smd/RELEASE_ARM64E"
+ "Darwin Privileged Tool Bootstrapper Version 2.0.0: Fri Sep  4 20:48:20 PDT 2026; root:libxpc_executables-3298.40.20~23/smd/RELEASE_ARM64E"
- "@(#)VERSION:Darwin Privileged Tool Bootstrapper Version 2.0.0: Sat Aug 22 16:54:35 PDT 2026; root:libxpc_executables-3298.1.1~67/smd/RELEASE_ARM64E"
- "Darwin Privileged Tool Bootstrapper Version 2.0.0: Sat Aug 22 16:54:35 PDT 2026; root:libxpc_executables-3298.1.1~67/smd/RELEASE_ARM64E"
```
