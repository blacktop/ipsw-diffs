## xpcproxy

> `/usr/libexec/xpcproxy`

```diff

-3089.82.3.0.0
-  __TEXT.__text: 0x6344
-  __TEXT.__auth_stubs: 0xb20
-  __TEXT.__const: 0x88
-  __TEXT.__cstring: 0xd20
-  __TEXT.__oslogstring: 0x162d
+3102.100.97.502.1
+  __TEXT.__text: 0x5d98
+  __TEXT.__auth_stubs: 0xb30
+  __TEXT.__const: 0x80
+  __TEXT.__cstring: 0xd6f
+  __TEXT.__oslogstring: 0x1692
   __TEXT.__xpcproxy: 0x1
   __TEXT.__dof_launchd: 0x2e5
   __TEXT.__unwind_info: 0x140
-  __DATA_CONST.__auth_got: 0x590
+  __DATA_CONST.__auth_got: 0x598
   __DATA_CONST.__got: 0x90
   __DATA_CONST.__const: 0x188
   __DATA.__os_assumes_log: 0x8

   - /usr/lib/libcryptex_trampoline.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsandbox.1.dylib
-  UUID: F6C80DFD-5539-395D-84D2-F070136C8C62
-  Functions: 122
-  Symbols:   198
-  CStrings:  200
+  UUID: 42F1C903-B644-378D-AE1B-E2CF052EFCC1
+  Functions: 121
+  Symbols:   199
+  CStrings:  201
 
Symbols:
+ _posix_spawnattr_set_telemetry_np
CStrings:
+ "/Library/Caches/com.apple.xbs/DBDC5F08-F6B7-4380-AD47-2805B60E9849/TemporaryDirectory.NUDTMJ/Binaries/libxpc_executables/install/Symbols/xpcproxy"
+ "@(#)VERSION:Darwin Bootstrapper Trampoline Version 7.0.0: Thu Feb  5 21:37:40 PST 2026; root:libxpc_executables-3102.100.97.502.1~2/xpcproxy/RELEASE_ARM64E"
+ "Darwin Bootstrapper Trampoline Version 7.0.0: Thu Feb  5 21:37:40 PST 2026; root:libxpc_executables-3102.100.97.502.1~2/xpcproxy/RELEASE_ARM64E"
+ "assertion failure: \"posix_spawnattr_set_telemetry_np(&ctx->psattr, PSA_TELEMETRY_PAGEIN, 0)\" -> %llu"
- "/Library/Caches/com.apple.xbs/Binaries/libxpc_executables/install/Symbols/xpcproxy"
- "@(#)VERSION:Darwin Bootstrapper Trampoline Version 7.0.0: Wed Jan 21 22:10:09 PST 2026; root:libxpc_executables-3089.82.3~1/xpcproxy/RELEASE_ARM64E"
- "Darwin Bootstrapper Trampoline Version 7.0.0: Wed Jan 21 22:10:09 PST 2026; root:libxpc_executables-3089.82.3~1/xpcproxy/RELEASE_ARM64E"

```
