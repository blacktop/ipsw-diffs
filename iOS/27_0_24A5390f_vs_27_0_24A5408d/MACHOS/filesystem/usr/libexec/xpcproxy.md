## xpcproxy

> `/usr/libexec/xpcproxy`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__dof_launchd`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__got`
- `__DATA.__os_assumes_log`
- `__DATA.__data`

```diff

-3298.0.21.0.0
-  __TEXT.__text: 0x9948
-  __TEXT.__auth_stubs: 0xb10
+3298.0.26.502.1
+  __TEXT.__text: 0x9a90
+  __TEXT.__auth_stubs: 0xb30
   __TEXT.__lazy_helpers: 0x150
   __TEXT.__const: 0x190
   __TEXT.__xpcproxy: 0x1
-  __TEXT.__oslogstring: 0x1712
-  __TEXT.__cstring: 0x19d2
+  __TEXT.__oslogstring: 0x15ef
+  __TEXT.__cstring: 0x1a58
   __TEXT.__dof_launchd: 0x2e5
   __TEXT.__unwind_info: 0x178
   __DATA_CONST.__const: 0x248
-  __DATA_CONST.__auth_got: 0x588
+  __DATA_CONST.__auth_got: 0x598
   __DATA_CONST.__got: 0x88
   __DATA.__lazy_load_got: 0x20
   __DATA.__os_assumes_log: 0x8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 92
-  Symbols:   200
-  CStrings:  298
+  Symbols:   202
+  CStrings:  302
 
Symbols:
+ _fcntl
+ _posix_spawn_file_actions_adddup2
Functions:
~ sub_100001278 : 2744 -> 2792
~ sub_100001d30 -> sub_100001d60 : 436 -> 448
~ sub_100001ee4 -> sub_100001f20 : 8068 -> 8336
CStrings:
+ "@(#)VERSION:Darwin Bootstrapper Trampoline Version 7.0.0: Wed Aug  5 00:09:34 PDT 2026; root:libxpc_executables-3298.0.26.502.1~2/xpcproxy/RELEASE_ARM64E"
+ "Darwin Bootstrapper Trampoline Version 7.0.0: Wed Aug  5 00:09:34 PDT 2026; root:libxpc_executables-3298.0.26.502.1~2/xpcproxy/RELEASE_ARM64E"
+ "Unable to open stderr path (%s)"
+ "Unable to open stdin path (%s)"
+ "Unable to open stdout path (%s)"
+ "Unable to unpack bundle path"
+ "assertion failure: \"posix_spawn_file_actions_adddup2(&ctx->filact, fd, 0)\" -> %llu"
+ "assertion failure: \"posix_spawn_file_actions_adddup2(&ctx->filact, fd, 1)\" -> %llu"
+ "assertion failure: \"posix_spawn_file_actions_adddup2(&ctx->filact, fd, 2)\" -> %llu"
- "@(#)VERSION:Darwin Bootstrapper Trampoline Version 7.0.0: Fri Jul 10 23:07:02 PDT 2026; root:libxpc_executables-3298.0.21~14/xpcproxy/RELEASE_ARM64E"
- "Darwin Bootstrapper Trampoline Version 7.0.0: Fri Jul 10 23:07:02 PDT 2026; root:libxpc_executables-3298.0.21~14/xpcproxy/RELEASE_ARM64E"
- "assertion failure: \"posix_spawn_file_actions_addopen(&ctx->filact, 0, stdin_path, 0x00000200|0x0000|0x00020000, (0000400|0000200|0000040|0000020|0000004|0000002))\" -> %llu"
- "assertion failure: \"posix_spawn_file_actions_addopen(&ctx->filact, 1, stdout_path, 0x00000200|0x0002|0x00000008|0x00020000, (0000400|0000200|0000040|0000020|0000004|0000002))\" -> %llu"
- "assertion failure: \"posix_spawn_file_actions_addopen(&ctx->filact, 2, stderr_path, 0x00000200|0x0002|0x00000008|0x00020000, (0000400|0000200|0000040|0000020|0000004|0000002))\" -> %llu"
```
