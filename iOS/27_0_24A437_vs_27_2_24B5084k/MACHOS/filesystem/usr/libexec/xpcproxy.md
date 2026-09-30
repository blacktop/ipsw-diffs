## xpcproxy

> `/usr/libexec/xpcproxy`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__dof_launchd`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA.__os_assumes_log`
- `__DATA.__data`

```diff

-3298.2.1.0.0
-  __TEXT.__text: 0x9a44
+3298.40.20.0.0
+  __TEXT.__text: 0x9a14
   __TEXT.__auth_stubs: 0xb30
   __TEXT.__lazy_helpers: 0x150
   __TEXT.__const: 0x190
   __TEXT.__xpcproxy: 0x1
   __TEXT.__oslogstring: 0x15ef
-  __TEXT.__cstring: 0x1a4c
+  __TEXT.__cstring: 0x1a33
   __TEXT.__dof_launchd: 0x2e5
   __TEXT.__unwind_info: 0x1f0
   __DATA_CONST.__const: 0x248

   - /usr/lib/libobjc.A.dylib
   Functions: 92
   Symbols:   202
-  CStrings:  302
+  CStrings:  301
 
Functions:
~ sub_10000126c : 2792 -> 2744
CStrings:
+ "@(#)VERSION:Darwin Bootstrapper Trampoline Version 7.0.0: Fri Sep  4 20:50:56 PDT 2026; root:libxpc_executables-3298.40.20~24/xpcproxy/RELEASE_ARM64E"
+ "Darwin Bootstrapper Trampoline Version 7.0.0: Fri Sep  4 20:50:56 PDT 2026; root:libxpc_executables-3298.40.20~24/xpcproxy/RELEASE_ARM64E"
- "@(#)VERSION:Darwin Bootstrapper Trampoline Version 7.0.0: Sat Aug  8 16:39:58 PDT 2026; root:libxpc_executables-3298.2.1~23/xpcproxy/RELEASE_ARM64E"
- "Darwin Bootstrapper Trampoline Version 7.0.0: Sat Aug  8 16:39:58 PDT 2026; root:libxpc_executables-3298.2.1~23/xpcproxy/RELEASE_ARM64E"
- "Unable to unpack bundle path"
```
