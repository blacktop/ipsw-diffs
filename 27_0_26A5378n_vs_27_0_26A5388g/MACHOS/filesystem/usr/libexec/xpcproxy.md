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
-  __TEXT.__text: 0xaf88
-  __TEXT.__auth_stubs: 0xc50
+3298.0.21.0.0
+  __TEXT.__text: 0xb038
+  __TEXT.__auth_stubs: 0xc60
   __TEXT.__lazy_helpers: 0x1a4
   __TEXT.__const: 0x1b0
   __TEXT.__xpcproxy: 0x1
-  __TEXT.__oslogstring: 0x199f
+  __TEXT.__oslogstring: 0x1a1b
   __TEXT.__cstring: 0x1be9
   __TEXT.__dof_launchd: 0x2e5
   __TEXT.__unwind_info: 0x188
   __DATA_CONST.__const: 0x260
-  __DATA_CONST.__auth_got: 0x628
+  __DATA_CONST.__auth_got: 0x630
   __DATA_CONST.__got: 0xa0
   __DATA.__lazy_load_got: 0x28
   __DATA.__os_assumes_log: 0x8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 101
-  Symbols:   224
-  CStrings:  331
+  Symbols:   225
+  CStrings:  332
 
Symbols:
+ _posix_spawnattr_set_shared_region_config_np
Functions:
~ sub_10000266c : 8216 -> 8392
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.5v8qSb/Binaries/libxpc_executables/install/Symbols/xpcproxy"
+ "@(#)VERSION:Darwin Bootstrapper Trampoline Version 7.0.0: Mon Jul 13 21:49:43 PDT 2026; root:libxpc_executables-3298.0.21~90/xpcproxy/RELEASE_ARM64E"
+ "Darwin Bootstrapper Trampoline Version 7.0.0: Mon Jul 13 21:49:43 PDT 2026; root:libxpc_executables-3298.0.21~90/xpcproxy/RELEASE_ARM64E"
+ "assertion failure: \"posix_spawnattr_set_shared_region_config_np(&ctx->psattr, attr->ps_shared_region_config_flags)\" -> %llu"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.YpZto6/Binaries/libxpc_executables/install/Symbols/xpcproxy"
- "@(#)VERSION:Darwin Bootstrapper Trampoline Version 7.0.0: Tue Jun 30 21:12:07 PDT 2026; root:libxpc_executables-3298.0.10~59/xpcproxy/RELEASE_ARM64E"
- "Darwin Bootstrapper Trampoline Version 7.0.0: Tue Jun 30 21:12:07 PDT 2026; root:libxpc_executables-3298.0.10~59/xpcproxy/RELEASE_ARM64E"
```
