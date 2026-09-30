## xpcproxy

> `/usr/libexec/xpcproxy`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`
- `__TEXT.__dof_launchd`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA.__data`

```diff

 3298.2.1.0.0
-  __TEXT.__text: 0x9a90
+  __TEXT.__text: 0x9a98
   __TEXT.__auth_stubs: 0xb30
   __TEXT.__lazy_helpers: 0x150
   __TEXT.__const: 0x190
Functions:
~ sub_100006c34 : 220 -> 224
~ sub_100006d10 -> sub_100006d14 : 608 -> 612
CStrings:
+ "@(#)VERSION:Darwin Bootstrapper Trampoline Version 7.0.0: Sat Aug  8 16:39:58 PDT 2026; root:libxpc_executables-3298.2.1~23/xpcproxy/RELEASE_ARM64E"
+ "Darwin Bootstrapper Trampoline Version 7.0.0: Sat Aug  8 16:39:58 PDT 2026; root:libxpc_executables-3298.2.1~23/xpcproxy/RELEASE_ARM64E"
- "@(#)VERSION:Darwin Bootstrapper Trampoline Version 7.0.0: Sat Aug  8 19:40:41 PDT 2026; root:libxpc_executables-3298.2.1~26/xpcproxy/RELEASE_ARM64E"
- "Darwin Bootstrapper Trampoline Version 7.0.0: Sat Aug  8 19:40:41 PDT 2026; root:libxpc_executables-3298.2.1~26/xpcproxy/RELEASE_ARM64E"
```
