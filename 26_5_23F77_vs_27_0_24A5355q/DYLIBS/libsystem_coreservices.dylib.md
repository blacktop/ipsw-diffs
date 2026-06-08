## libsystem_coreservices.dylib

> `/usr/lib/system/libsystem_coreservices.dylib`

```diff

-191.4.5.0.0
-  __TEXT.__text: 0x1980
-  __TEXT.__auth_stubs: 0x2e0
-  __TEXT.__const: 0x68
-  __TEXT.__cstring: 0x376
-  __TEXT.__oslogstring: 0x1c2
+201.0.0.0.0
+  __TEXT.__text: 0x1888
+  __TEXT.__const: 0x70
+  __TEXT.__cstring: 0x335
+  __TEXT.__oslogstring: 0x1e7
   __TEXT.__unwind_info: 0xd8
-  __DATA_CONST.__got: 0x10
+  __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x928
-  __AUTH_CONST.__auth_got: 0x170
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x80
+  __AUTH_CONST.__auth_got: 0x160
+  __DATA.__crash_info: 0x148
   __DATA.__bss: 0x820
   __DATA_DIRTY.__bss: 0x20
   __DATA_DIRTY.__common: 0x88

   - /usr/lib/system/libsystem_pthread.dylib
   - /usr/lib/system/libsystem_sandbox.dylib
   - /usr/lib/system/libsystem_trace.dylib
-  UUID: 1BB86E58-04EB-38D6-8B47-F013D51135C3
-  Functions: 45
-  Symbols:   192
+  UUID: 9F093324-C474-3C6D-A5D0-ACF0DF27CFE8
+  Functions: 46
+  Symbols:   189
   CStrings:  62
 
Symbols:
+ ____dirhelper_relative_internal_block_invoke.10
+ __dirhelper_relative_internal.onceToken.9
+ __log
+ __log.cold.1
+ _gCRAnnotations
+ _getenv_copy_np
+ _sandbox_container_path_for_pid
+ _strerror
+ _validate_user_dir_suffix.cold.1
+ _validate_user_dir_suffix.cold.2
+ _validate_user_dir_suffix.cold.3
+ _validate_user_dir_suffix.cold.4
- _OUTLINED_FUNCTION_3
- _OUTLINED_FUNCTION_4
- _OUTLINED_FUNCTION_5
- ____dirhelper_relative_internal_block_invoke.15
- ____dirhelper_relative_internal_block_invoke.15.cold.1
- ___block_descriptor_tmp.16
- ___block_literal_global.18
- __dirhelper_relative_internal.cold.5
- __dirhelper_relative_internal.cold.6
- __dirhelper_relative_internal.onceToken.14
- __dirhelper_update_tmpdir.cold.1
- __dyld_get_image_uuid
- __dyld_get_shared_cache_range
- __dyld_get_shared_cache_uuid
- __os_log_simple
- _container_create_or_lookup_path_for_current_user
- _makeDirectory.cold.1
- _makeDirectory.cold.2
CStrings:
+ "%s: error for relativepath %s: %s (%d)"
+ "%s: no result for relativepath %s, err=%s (%d)"
+ "mkdir: path=%{public}s mode=%o: %s (%d"
- "%s: error for relativepath %s: %{errno}d"
- "%s: no result for relativepath %s, err=%{errno}d"
- "mkdir: path=%{public}s mode= %{darwin.mode}d: %{darwin.errno}d"

```
