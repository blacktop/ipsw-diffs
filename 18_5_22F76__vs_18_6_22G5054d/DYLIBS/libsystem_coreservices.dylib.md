## libsystem_coreservices.dylib

> `/usr/lib/system/libsystem_coreservices.dylib`

```diff

-178.0.0.0.0
-  __TEXT.__text: 0x1848
-  __TEXT.__auth_stubs: 0x280
-  __TEXT.__const: 0x68
-  __TEXT.__cstring: 0x30a
-  __TEXT.__oslogstring: 0x1fe
-  __TEXT.__unwind_info: 0xc0
+178.1.0.0.0
+  __TEXT.__text: 0x1ac4
+  __TEXT.__auth_stubs: 0x2f0
+  __TEXT.__const: 0x60
+  __TEXT.__cstring: 0x3b4
+  __TEXT.__oslogstring: 0x19b
+  __TEXT.__unwind_info: 0xd0
   __DATA_CONST.__got: 0x10
   __DATA_CONST.__const: 0x928
-  __AUTH_CONST.__auth_got: 0x140
+  __AUTH_CONST.__auth_got: 0x178
   __AUTH_CONST.__const: 0x80
   __DATA.__bss: 0x820
   __DATA_DIRTY.__bss: 0x20

   - /usr/lib/system/libsystem_pthread.dylib
   - /usr/lib/system/libsystem_sandbox.dylib
   - /usr/lib/system/libsystem_trace.dylib
-  UUID: 73204B18-51E4-31C7-9760-32F1E9595912
-  Functions: 40
-  Symbols:   176
-  CStrings:  58
+  UUID: E144EB8D-5415-3C6F-A066-133B268F9B57
+  Functions: 43
+  Symbols:   184
+  CStrings:  62
 
Symbols:
+ ____dirhelper_relative_internal_block_invoke.21
+ ____dirhelper_relative_internal_block_invoke.21.cold.1
+ ___block_descriptor_tmp.12
+ ___block_descriptor_tmp.17
+ ___block_descriptor_tmp.22
+ ___block_literal_global.14
+ ___block_literal_global.19
+ ___block_literal_global.24
+ __dirhelper_relative_internal.onceToken.20
+ __dirhelper_remove_test
+ __dirhelper_test
+ __dyld_get_image_uuid
+ __dyld_get_shared_cache_range
+ __dyld_get_shared_cache_uuid
+ __os_log_simple
+ _getegid
+ _lchown
+ _makeDirectory
+ _makeDirectoryWithUIDAndGID
+ _modes
+ _strerror
+ _validate_user_dir_suffix
- ____dirhelper_relative_internal_block_invoke.22
- ____dirhelper_relative_internal_block_invoke.22.cold.1
- ___block_descriptor_tmp.13
- ___block_descriptor_tmp.18
- ___block_descriptor_tmp.23
- ___block_literal_global.15
- ___block_literal_global.20
- ___block_literal_global.25
- ___makeDirectory
- ___makeDirectory.cold.1
- ___makeDirectory.cold.2
- ___makeDirectory.cold.3
- __dirhelper_relative_internal.onceToken.21
CStrings:
+ "%s: chmod error: %s (%d)"
+ "%s: chown error for uid=%d, gid=%d: %s (%d)"
+ "%s: created %s"
+ "%s: mkdir: path=%s mode=%o: %s (%d)"
+ "%s: set uid=%d, gid=%d"
+ "makeDirectoryWithUIDAndGID"
- "__makeDirectory: created %{public}s"
- "mkdir: path=%{public}s mode= %{darwin.mode}d: %{darwin.errno}d"

```
