## xpcproxy

> `/usr/libexec/xpcproxy`

### Sections with Same Size but Changed Content

- `__TEXT.__dof_launchd`
- `__DATA_CONST.__const`
- `__DATA.__data`

```diff

   __TEXT.__const: 0x190
   __TEXT.__xpcproxy: 0x1
   __TEXT.__oslogstring: 0x15ef
-  __TEXT.__cstring: 0x1a33
+  __TEXT.__cstring: 0x1a35
   __TEXT.__dof_launchd: 0x2e5
   __TEXT.__unwind_info: 0x1f0
   __DATA_CONST.__const: 0x248
CStrings:
+ "@(#)VERSION:Darwin Bootstrapper Trampoline Version 7.0.0: Sun Sep 13 20:55:09 PDT 2026; root:libxpc_executables-3298.40.20~223/xpcproxy/RELEASE_ARM64E"
+ "Darwin Bootstrapper Trampoline Version 7.0.0: Sun Sep 13 20:55:09 PDT 2026; root:libxpc_executables-3298.40.20~223/xpcproxy/RELEASE_ARM64E"
- "@(#)VERSION:Darwin Bootstrapper Trampoline Version 7.0.0: Fri Sep  4 20:50:56 PDT 2026; root:libxpc_executables-3298.40.20~24/xpcproxy/RELEASE_ARM64E"
- "Darwin Bootstrapper Trampoline Version 7.0.0: Fri Sep  4 20:50:56 PDT 2026; root:libxpc_executables-3298.40.20~24/xpcproxy/RELEASE_ARM64E"
```
