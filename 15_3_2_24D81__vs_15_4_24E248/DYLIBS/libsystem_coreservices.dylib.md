## libsystem_coreservices.dylib

> `/usr/lib/system/libsystem_coreservices.dylib`

```diff

-171.1.0.0.0
-  __TEXT.__text: 0x4f68
-  __TEXT.__auth_stubs: 0x560
-  __TEXT.__const: 0xd0
-  __TEXT.__cstring: 0x446
-  __TEXT.__oslogstring: 0x6bd
-  __TEXT.__unwind_info: 0x140
-  __DATA_CONST.__got: 0x30
+178.0.0.0.0
+  __TEXT.__text: 0x4a30
+  __TEXT.__auth_stubs: 0x550
+  __TEXT.__const: 0xb8
+  __TEXT.__cstring: 0x43b
+  __TEXT.__oslogstring: 0x671
+  __TEXT.__unwind_info: 0x130
+  __DATA_CONST.__got: 0x20
   __DATA_CONST.__const: 0x928
-  __AUTH_CONST.__auth_got: 0x2b0
+  __AUTH_CONST.__auth_got: 0x2a8
   __AUTH_CONST.__const: 0x60
   __DATA.__bss: 0x30
   __DATA.__common: 0x88

   - /usr/lib/system/libsystem_sandbox.dylib
   - /usr/lib/system/libsystem_trace.dylib
   - /usr/lib/system/libxpc.dylib
-  UUID: 579E4601-365D-346F-9CD9-37851FB2874C
-  Functions: 89
-  Symbols:   234
-  CStrings:  110
+  UUID: 5E6A695D-8EE0-34C4-97F4-8B5777CD8EE7
+  Functions: 92
+  Symbols:   282
+  CStrings:  108
 
Symbols:
+ NSGetNextSearchPathEnumerationStatic.cold.1
+ NSStartSearchPathEnumerationStatic.cold.1
+ __create_or_fix_relative_directory.cold.5
+ __create_or_fix_relative_directory.cold.6
+ __create_or_fix_relative_directory.cold.7
+ __create_or_fix_relative_directory.cold.8
+ __create_or_fix_relative_directory.cold.9
+ __makeDirectory.cold.1
+ __makeDirectory.cold.2
+ __makeRootlessDirectory.cold.10
+ __makeRootlessDirectory.cold.11
+ __makeRootlessDirectory.cold.12
+ __makeRootlessDirectory.cold.13
+ __makeRootlessDirectory.cold.14
+ __makeRootlessDirectory.cold.15
+ __makeRootlessDirectory.cold.16
+ __makeRootlessDirectory.cold.17
+ __makeRootlessDirectory.cold.18
+ __makeRootlessDirectory.cold.9
+ __user_local_dirname.cold.4
+ __user_local_dirname.cold.5
+ __user_local_dirname.cold.6
+ _dirhelper_internal.cold.12
+ _dirhelper_internal.cold.13
+ _dirhelper_internal.cold.14
+ _dirhelper_internal.cold.15
+ _dirhelper_internal.cold.16
+ _dirhelper_internal.cold.17
+ _dirhelper_internal.cold.18
+ _dirhelper_internal.cold.19
+ _dirhelper_internal.cold.20
+ _dirhelper_internal.cold.21
+ _dirhelper_internal.cold.22
+ _dirhelper_internal.cold.23
+ _dirhelper_internal.cold.24
+ _dirhelper_internal.cold.25
+ _dirhelper_internal.cold.26
+ _dirhelper_internal.cold.27
+ _dirhelper_internal.cold.28
+ _dirhelper_relative_internal.cold.3
+ _dirhelper_relative_internal.cold.4
+ _get_user_dir_suffix.cold.1
+ _get_user_dir_suffix.cold.2
+ _idle_exit.cold.3
+ _idle_exit.cold.4
+ _idle_exit.cold.5
+ _set_group_delete_acl.cold.5
+ _set_group_delete_acl.cold.6
+ _set_group_delete_acl.cold.7
+ _set_group_delete_acl.cold.8
+ _set_user_dir_suffix.cold.2
+ _set_user_dir_suffix.cold.3
+ _statfs_ext
- _OUTLINED_FUNCTION_15
- _getattrlist
- _ministatfs
- _statfs
- ministatfs.cold.1
CStrings:
- "%s: getattrlist result=%d, error=%{errno}d, calling statfs for '%{public}s'"
- "ministatfs"

```
