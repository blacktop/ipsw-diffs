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
-  __TEXT.__text: 0xb038
-  __TEXT.__auth_stubs: 0xc60
+3298.1.1.0.0
+  __TEXT.__text: 0xb150
+  __TEXT.__auth_stubs: 0xc80
   __TEXT.__lazy_helpers: 0x1a4
   __TEXT.__const: 0x1b0
   __TEXT.__xpcproxy: 0x1
-  __TEXT.__oslogstring: 0x1a1b
-  __TEXT.__cstring: 0x1be9
+  __TEXT.__oslogstring: 0x18f8
+  __TEXT.__cstring: 0x1c46
   __TEXT.__dof_launchd: 0x2e5
   __TEXT.__unwind_info: 0x188
   __DATA_CONST.__const: 0x260
-  __DATA_CONST.__auth_got: 0x630
+  __DATA_CONST.__auth_got: 0x640
   __DATA_CONST.__got: 0xa0
   __DATA.__lazy_load_got: 0x28
   __DATA.__os_assumes_log: 0x8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 101
-  Symbols:   225
-  CStrings:  332
+  Symbols:   227
+  CStrings:  335
 
Symbols:
+ _fcntl
+ _posix_spawn_file_actions_adddup2
Functions:
~ sub_10000225c : 436 -> 448
~ sub_10000266c -> sub_100002678 : 8392 -> 8660
CStrings:
+ "@(#)VERSION:Darwin Bootstrapper Trampoline Version 7.0.0: Mon Aug 10 01:08:51 PDT 2026; root:libxpc_executables-3298.1.1~29/xpcproxy/RELEASE_ARM64E"
+ "Darwin Bootstrapper Trampoline Version 7.0.0: Mon Aug 10 01:08:51 PDT 2026; root:libxpc_executables-3298.1.1~29/xpcproxy/RELEASE_ARM64E"
+ "Unable to open stderr path (%s)"
+ "Unable to open stdin path (%s)"
+ "Unable to open stdout path (%s)"
+ "assertion failure: \"posix_spawn_file_actions_adddup2(&ctx->filact, fd, 0)\" -> %llu"
+ "assertion failure: \"posix_spawn_file_actions_adddup2(&ctx->filact, fd, 1)\" -> %llu"
+ "assertion failure: \"posix_spawn_file_actions_adddup2(&ctx->filact, fd, 2)\" -> %llu"
- "@(#)VERSION:Darwin Bootstrapper Trampoline Version 7.0.0: Mon Jul 13 21:49:43 PDT 2026; root:libxpc_executables-3298.0.21~90/xpcproxy/RELEASE_ARM64E"
- "Darwin Bootstrapper Trampoline Version 7.0.0: Mon Jul 13 21:49:43 PDT 2026; root:libxpc_executables-3298.0.21~90/xpcproxy/RELEASE_ARM64E"
- "assertion failure: \"posix_spawn_file_actions_addopen(&ctx->filact, 0, stdin_path, 0x00000200|0x0000|0x00020000, (0000400|0000200|0000040|0000020|0000004|0000002))\" -> %llu"
- "assertion failure: \"posix_spawn_file_actions_addopen(&ctx->filact, 1, stdout_path, 0x00000200|0x0002|0x00000008|0x00020000, (0000400|0000200|0000040|0000020|0000004|0000002))\" -> %llu"
- "assertion failure: \"posix_spawn_file_actions_addopen(&ctx->filact, 2, stderr_path, 0x00000200|0x0002|0x00000008|0x00020000, (0000400|0000200|0000040|0000020|0000004|0000002))\" -> %llu"
```
