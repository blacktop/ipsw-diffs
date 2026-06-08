## libsystem_coreservices.dylib

> `/usr/lib/system/libsystem_coreservices.dylib`

```diff

-191.4.5.0.0
-  __TEXT.__text: 0x1980 sha256:22b32186da1a94e1af93c71929f6e68f5e27a717f66c8a056a8291166392f15a
-  __TEXT.__auth_stubs: 0x2e0 sha256:a9df4d08918d892783e658235e657108911deb3b7f9d8dcd19df82a6462c04ee
-  __TEXT.__const: 0x68 sha256:0f0441b4910752bb208f84d11fba4ac0c32cbf6a0e467695b675b79a23399ba6
-  __TEXT.__cstring: 0x376 sha256:1b20b7c2b15edbf65399011629ee70702371996f5b5892f379c8ca553dd73d7a
-  __TEXT.__oslogstring: 0x1c2 sha256:aa21fc7fee94e88c12baa8c519455e97abd1100b88724d8d72ad4ceecb584ac0
-  __TEXT.__unwind_info: 0xd8 sha256:f519d3b9cfdac30a8df0e9ec715de49d9f6157178d09dd93a7d7c2f526a74484
-  __DATA_CONST.__got: 0x10 sha256:374708fff7719dd5979ec875d56cd2286f6d3cf7ec317a3b25632aab28ec37bb
-  __DATA_CONST.__const: 0x928 sha256:20c97cf865a7b02eb350f2d33423b308fc40642f04316474d090ba1ca79c3273
-  __AUTH_CONST.__auth_got: 0x170 sha256:71818ecc26433c32172dd9a3544657971c7078daa2257da7c3c303e08693cb23
-  __AUTH_CONST.__const: 0x80 sha256:9adea4658e26066be88d99d7e70bf5797ed720a177e5d7c43717413a702820a6
+201.0.0.0.0
+  __TEXT.__text: 0x1888 sha256:2b8b48adcb2f22eb2dd095faf3f61d2cc4d75c48ad91646f84c50cf6be9181ce
+  __TEXT.__const: 0x70 sha256:4d0ccce913b5ce914439434314618618b9cd378c99b2193db1e1f3a3e11b36e5
+  __TEXT.__cstring: 0x335 sha256:06a0fc082fa8f9108a69de2305f3bcf7792ed1729ddc174c18d8e4d10c0079c6
+  __TEXT.__oslogstring: 0x1e7 sha256:e286c22f48582926a32ad8dc90e34750001c9886d32c82b4ceaa2e79b8142b71
+  __TEXT.__unwind_info: 0xd8 sha256:f7085ee5a979f8808259502d5b350fe073de3dadfab9cfd1b7039dd90372dfc6
+  __TEXT.__auth_stubs: 0x0
+  __DATA_CONST.__const: 0x928 sha256:e9a07fc5025bf19509e9ce7c8fd677914c3c4a45531fb71f76d041f36f1b5856
+  __DATA_CONST.__got: 0x0
+  __AUTH_CONST.__const: 0x80 sha256:ede253cea2dd89ab6f33777ca16cf460e7f53281fc89232c139694ba0cf9b62d
+  __AUTH_CONST.__auth_got: 0x160 sha256:627f6149015f853f26db2f3dffba1b7c30b3b74b87c5cfb9f346c1616e3636d0
+  __DATA.__crash_info: 0x148 sha256:6da6349e97370e8d430272961ce52dff296ff7c22208bd465045a16f557b12e4
   __DATA.__bss: 0x820 sha256:74ad040475ba3d4aac1053a289121a2c5922daac47e395648debf7165ec7e08f
   __DATA_DIRTY.__bss: 0x20 sha256:66687aadf862bd776c8fc18b8e9f8e20089714856ee233b3902a591d0d5f2925
   __DATA_DIRTY.__common: 0x88 sha256:b707241545a346265aab1ffb32ff64b55bf8f8dc1b56a46ef33ce3d15db11d33

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
