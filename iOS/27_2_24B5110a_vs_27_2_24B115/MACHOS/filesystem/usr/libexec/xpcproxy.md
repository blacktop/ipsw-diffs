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
-  __TEXT.__cstring: 0x1a4c
+  __TEXT.__cstring: 0x1a4e
   __TEXT.__dof_launchd: 0x2e5
   __TEXT.__unwind_info: 0x1f0
   __DATA_CONST.__const: 0x248
CStrings:
+ "@(#)VERSION:Darwin Bootstrapper Trampoline Version 7.0.0: Wed Oct  7 23:43:14 PDT 2026; root:libxpc_executables-3298.42.1~13/xpcproxy/RELEASE_ARM64E"
+ "Darwin Bootstrapper Trampoline Version 7.0.0: Wed Oct  7 23:43:14 PDT 2026; root:libxpc_executables-3298.42.1~13/xpcproxy/RELEASE_ARM64E"
- "@(#)VERSION:Darwin Bootstrapper Trampoline Version 7.0.0: Sat Oct  3 23:07:12 PDT 2026; root:libxpc_executables-3298.42.1~6/xpcproxy/RELEASE_ARM64E"
- "Darwin Bootstrapper Trampoline Version 7.0.0: Sat Oct  3 23:07:12 PDT 2026; root:libxpc_executables-3298.42.1~6/xpcproxy/RELEASE_ARM64E"
```
