## xpcproxy

> `/usr/libexec/xpcproxy`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__cstring`
- `__TEXT.__dof_launchd`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__got`
- `__DATA.__os_assumes_log`
- `__DATA.__data`

```diff

-3298.0.10.0.0
-  __TEXT.__text: 0x989c
-  __TEXT.__auth_stubs: 0xb00
+3298.0.21.0.0
+  __TEXT.__text: 0x9948
+  __TEXT.__auth_stubs: 0xb10
   __TEXT.__lazy_helpers: 0x150
   __TEXT.__const: 0x190
   __TEXT.__xpcproxy: 0x1
-  __TEXT.__oslogstring: 0x1696
+  __TEXT.__oslogstring: 0x1712
   __TEXT.__cstring: 0x19d2
   __TEXT.__dof_launchd: 0x2e5
   __TEXT.__unwind_info: 0x178
   __DATA_CONST.__const: 0x248
-  __DATA_CONST.__auth_got: 0x580
+  __DATA_CONST.__auth_got: 0x588
   __DATA_CONST.__got: 0x88
   __DATA.__lazy_load_got: 0x20
   __DATA.__os_assumes_log: 0x8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 92
-  Symbols:   199
-  CStrings:  297
+  Symbols:   200
+  CStrings:  298
 
Symbols:
+ _posix_spawnattr_set_shared_region_config_np
Functions:
~ sub_100001ee4 : 7896 -> 8068
CStrings:
+ "@(#)VERSION:Darwin Bootstrapper Trampoline Version 7.0.0: Fri Jul 10 23:07:02 PDT 2026; root:libxpc_executables-3298.0.21~14/xpcproxy/RELEASE_ARM64E"
+ "Darwin Bootstrapper Trampoline Version 7.0.0: Fri Jul 10 23:07:02 PDT 2026; root:libxpc_executables-3298.0.21~14/xpcproxy/RELEASE_ARM64E"
+ "assertion failure: \"posix_spawnattr_set_shared_region_config_np(&ctx->psattr, attr->ps_shared_region_config_flags)\" -> %llu"
- "@(#)VERSION:Darwin Bootstrapper Trampoline Version 7.0.0: Sat Jun 27 00:45:30 PDT 2026; root:libxpc_executables-3298.0.10~15/xpcproxy/RELEASE_ARM64E"
- "Darwin Bootstrapper Trampoline Version 7.0.0: Sat Jun 27 00:45:30 PDT 2026; root:libxpc_executables-3298.0.10~15/xpcproxy/RELEASE_ARM64E"
```
