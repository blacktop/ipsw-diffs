## libsystem_sandbox.dylib

> `/usr/lib/system/libsystem_sandbox.dylib`

```diff

-2401.81.2.0.0
-  __TEXT.__text: 0x4b08
+2401.101.1.0.0
+  __TEXT.__text: 0x47b0
   __TEXT.__auth_stubs: 0x4a0
   __TEXT.__const: 0x178
-  __TEXT.__cstring: 0xbed
-  __TEXT.__unwind_info: 0x208
+  __TEXT.__cstring: 0xbc6
+  __TEXT.__unwind_info: 0x200
   __DATA_CONST.__got: 0x8
   __DATA_CONST.__const: 0xb8
   __AUTH_CONST.__auth_got: 0x250

   - /usr/lib/system/libsystem_kernel.dylib
   - /usr/lib/system/libsystem_malloc.dylib
   - /usr/lib/system/libsystem_platform.dylib
-  UUID: BF38E17B-6A57-3EE2-A805-8E9B35542182
-  Functions: 148
-  Symbols:   277
-  CStrings:  114
+  UUID: C719032B-72A5-386F-A970-7D706F39E633
+  Functions: 141
+  Symbols:   272
+  CStrings:  110
 
Symbols:
+ rootless_mkdir_protected.cold.1
+ rootless_path_is_in_user_home_directory.cold.1
- _SANDBOX_EXTENSION_MAGIC
- _SANDBOX_EXTENSION_UNRESOLVED
- _sandbox_extension_issue_iokit_user_client_class
- _sandbox_extension_issue_posix_ipc
- _sandbox_init_with_extensions
- _sandbox_issue_extension
- _sandbox_issue_fs_rw_extension
CStrings:
+ "%s: unsupported data volume path: %s"
+ "/System/Volumes/Data"
+ "sandbox_enable_root_translation"
- "%s: %s for %s"
- "*"
- "denied by sandbox policy"
- "failed POSIX permissions check"
- "failed canonical check"
- "file-write-unlink"
- "unknown failure"

```
