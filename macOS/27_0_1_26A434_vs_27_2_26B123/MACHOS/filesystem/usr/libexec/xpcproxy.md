## xpcproxy

> `/usr/libexec/xpcproxy`

### Sections with Same Size but Changed Content

- `__TEXT.__dof_launchd`
- `__DATA_CONST.__const`
- `__DATA.__data`

```diff

-3298.1.1.0.0
-  __TEXT.__text: 0xb0f8
+3298.40.28.0.0
+  __TEXT.__text: 0xb2fc
   __TEXT.__auth_stubs: 0xc80
   __TEXT.__lazy_helpers: 0x1a4
-  __TEXT.__const: 0x1b0
+  __TEXT.__const: 0x1c0
   __TEXT.__xpcproxy: 0x1
-  __TEXT.__info_plist: 0x4d5
-  __TEXT.__oslogstring: 0x18f8
-  __TEXT.__cstring: 0x1c46
+  __TEXT.__info_plist: 0x4d1
+  __TEXT.__oslogstring: 0x1977
+  __TEXT.__cstring: 0x1c95
   __TEXT.__dof_launchd: 0x2e5
-  __TEXT.__unwind_info: 0x218
+  __TEXT.__unwind_info: 0x220
   __DATA_CONST.__const: 0x260
   __DATA_CONST.__auth_got: 0x640
   __DATA_CONST.__got: 0xa0

   __DATA.__common: 0x1
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 101
+  Functions: 103
   Symbols:   227
-  CStrings:  335
+  CStrings:  339
 
CStrings:
+ "@(#)VERSION:Darwin Bootstrapper Trampoline Version 7.0.0: Sat Oct  3 17:03:01 PDT 2026; root:libxpc_executables-3298.40.28~144/xpcproxy/RELEASE_ARM64E"
+ "ASP"
+ "Darwin Bootstrapper Trampoline Version 7.0.0: Sat Oct  3 17:03:01 PDT 2026; root:libxpc_executables-3298.40.28~144/xpcproxy/RELEASE_ARM64E"
+ "Unable to set system policy bundle path"
+ "Unable to unpack bundle path"
+ "assertion failure: \"posix_spawnattr_setmacpolicyinfo_np(&ctx->psattr, \"ASP\", &ctx->asp_attrs, sizeof(ctx->asp_attrs))\" -> %llu"
- "@(#)VERSION:Darwin Bootstrapper Trampoline Version 7.0.0: Sat Aug 22 16:54:50 PDT 2026; root:libxpc_executables-3298.1.1~67/xpcproxy/RELEASE_ARM64E"
- "Darwin Bootstrapper Trampoline Version 7.0.0: Sat Aug 22 16:54:50 PDT 2026; root:libxpc_executables-3298.1.1~67/xpcproxy/RELEASE_ARM64E"
```
