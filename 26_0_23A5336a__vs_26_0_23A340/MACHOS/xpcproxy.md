## xpcproxy

> `/usr/libexec/xpcproxy`

```diff

 3089.0.11.0.0
-  __TEXT.__text: 0x62dc
-  __TEXT.__auth_stubs: 0xb20
+  __TEXT.__text: 0x6368
+  __TEXT.__auth_stubs: 0xb30
   __TEXT.__const: 0x88
   __TEXT.__cstring: 0xd2a
-  __TEXT.__oslogstring: 0x15a5
+  __TEXT.__oslogstring: 0x162d
   __TEXT.__xpcproxy: 0x1
   __TEXT.__dof_launchd: 0x2e5
   __TEXT.__unwind_info: 0x148
-  __DATA_CONST.__auth_got: 0x590
+  __DATA_CONST.__auth_got: 0x598
   __DATA_CONST.__got: 0x90
   __DATA_CONST.__const: 0x1c8
   __DATA.__os_assumes_log: 0x8

   - /usr/lib/libcryptex_trampoline.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsandbox.1.dylib
-  UUID: B66C4E8D-AE4C-31BA-BC24-7BB5D561C25A
-  Functions: 123
-  Symbols:   198
-  CStrings:  200
+  UUID: C8C1D139-D4F3-3E3B-828E-0ED5BB639C8F
+  Functions: 124
+  Symbols:   199
+  CStrings:  201
 
Symbols:
+ _posix_spawnattr_set_use_sec_transition_shims_np
Functions:
~ sub_100001b4c : 3284 -> 3316
+ sub_100006560
CStrings:
+ "@(#)VERSION:Darwin Bootstrapper Trampoline Version 7.0.0: Sat Aug  2 22:00:34 PDT 2025; root:libxpc_executables-3089.0.11~250/xpcproxy/RELEASE_ARM64E"
+ "Darwin Bootstrapper Trampoline Version 7.0.0: Sat Aug  2 22:00:34 PDT 2025; root:libxpc_executables-3089.0.11~250/xpcproxy/RELEASE_ARM64E"
+ "assertion failure: \"posix_spawnattr_set_use_sec_transition_shims_np(&ctx->psattr, attr->checked_allocations_posix_spawn_flags)\" -> %llu"
- "@(#)VERSION:Darwin Bootstrapper Trampoline Version 7.0.0: Wed Aug 27 22:21:32 PDT 2025; root:libxpc_executables-3089.0.11~717/xpcproxy/RELEASE_ARM64E"
- "Darwin Bootstrapper Trampoline Version 7.0.0: Wed Aug 27 22:21:32 PDT 2025; root:libxpc_executables-3089.0.11~717/xpcproxy/RELEASE_ARM64E"

```
