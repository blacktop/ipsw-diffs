## xpcproxy

> `/usr/libexec/xpcproxy`

### Sections with Same Size but Changed Content

- `__TEXT.__dof_launchd`
- `__DATA_CONST.__const`
- `__DATA.__data`

```diff

-3298.1.1.0.0
+3298.40.20.0.0
   __TEXT.__text: 0xb0f8
   __TEXT.__auth_stubs: 0xc80
   __TEXT.__lazy_helpers: 0x1a4
-  __TEXT.__const: 0x1b0
+  __TEXT.__const: 0x1c0
   __TEXT.__xpcproxy: 0x1
   __TEXT.__oslogstring: 0x18f8
-  __TEXT.__cstring: 0x1c46
+  __TEXT.__cstring: 0x1c4a
   __TEXT.__dof_launchd: 0x2e5
   __TEXT.__unwind_info: 0x218
   __DATA_CONST.__const: 0x260
CStrings:
+ "@(#)VERSION:Darwin Bootstrapper Trampoline Version 7.0.0: Fri Sep  4 20:48:39 PDT 2026; root:libxpc_executables-3298.40.20~23/xpcproxy/RELEASE_ARM64E"
+ "Darwin Bootstrapper Trampoline Version 7.0.0: Fri Sep  4 20:48:39 PDT 2026; root:libxpc_executables-3298.40.20~23/xpcproxy/RELEASE_ARM64E"
- "@(#)VERSION:Darwin Bootstrapper Trampoline Version 7.0.0: Sat Aug 22 16:54:50 PDT 2026; root:libxpc_executables-3298.1.1~67/xpcproxy/RELEASE_ARM64E"
- "Darwin Bootstrapper Trampoline Version 7.0.0: Sat Aug 22 16:54:50 PDT 2026; root:libxpc_executables-3298.1.1~67/xpcproxy/RELEASE_ARM64E"
```
