## libsystem_networkextension.dylib

> `/usr/lib/system/libsystem_networkextension.dylib`

```diff

-1838.80.4.0.0
-  __TEXT.__text: 0x15060
-  __TEXT.__auth_stubs: 0x8d0
+1838.102.2.0.0
+  __TEXT.__text: 0x15794
+  __TEXT.__auth_stubs: 0x8e0
   __TEXT.__const: 0x60
-  __TEXT.__cstring: 0x1849
-  __TEXT.__oslogstring: 0x2a32
-  __TEXT.__unwind_info: 0x358
+  __TEXT.__cstring: 0x187c
+  __TEXT.__oslogstring: 0x2b5e
+  __TEXT.__unwind_info: 0x364
   __DATA_CONST.__got: 0x68
-  __DATA_CONST.__const: 0xc30
-  __AUTH_CONST.__const: 0x1a0
-  __AUTH_CONST.__auth_got: 0x468
+  __DATA_CONST.__const: 0xc50
+  __AUTH_CONST.__const: 0x1c0
+  __AUTH_CONST.__auth_got: 0x470
   __DATA.__data: 0x37c
-  __DATA.__bss: 0x2c8
+  __DATA.__bss: 0x2e0
   __DATA_DIRTY.__data: 0xc
   __DATA_DIRTY.__common: 0x2
   __DATA_DIRTY.__bss: 0x140

   - /usr/lib/system/libsystem_sandbox.dylib
   - /usr/lib/system/libsystem_trace.dylib
   - /usr/lib/system/libxpc.dylib
-  UUID: 6EAD63AF-2B78-3147-A944-1C4BB3ABDD3F
-  Functions: 258
-  Symbols:   637
-  CStrings:  506
+  UUID: A2D157DF-EF92-35B8-8255-7F25D576ED4A
+  Functions: 262
+  Symbols:   647
+  CStrings:  515
 
Symbols:
+ _NEHelperCacheClearUUIDsForBundleID
+ _NEHelperCachePopulateUUIDsForConfiguration
+ ___block_descriptor_tmp.114
+ ___block_descriptor_tmp.12.231
+ ___block_descriptor_tmp.147
+ ___block_descriptor_tmp.154
+ ___block_descriptor_tmp.157
+ ___block_descriptor_tmp.169
+ ___block_descriptor_tmp.172
+ ___block_descriptor_tmp.173
+ ___block_descriptor_tmp.181
+ ___block_descriptor_tmp.184
+ ___block_descriptor_tmp.188
+ ___block_descriptor_tmp.190
+ ___block_descriptor_tmp.191
+ ___block_descriptor_tmp.192
+ ___block_descriptor_tmp.209
+ ___block_descriptor_tmp.212
+ ___block_descriptor_tmp.215
+ ___block_descriptor_tmp.219
+ ___block_descriptor_tmp.227
+ ___block_descriptor_tmp.228
+ ___block_descriptor_tmp.230
+ ___block_descriptor_tmp.241
+ ___block_descriptor_tmp.248
+ ___block_descriptor_tmp.258
+ ___block_descriptor_tmp.8.233
+ ___block_literal_global.149
+ ___block_literal_global.167
+ ___block_literal_global.211
+ ___block_literal_global.214
+ ___block_literal_global.225
+ ___block_literal_global.244
+ ___block_literal_global.256
+ ___get_flow_divert_token_from_session_manager_block_invoke.234
+ ___ne_copy_uuid_cache_locked_block_invoke
+ ___ne_session_get_info_with_parameters_block_invoke.183
+ ___ne_session_get_info_with_parameters_block_invoke_2.186
+ ___notify_client_block_invoke.178
+ _ne_copy_uuid_cache_locked.g_my_boot_session_uuid
+ _ne_copy_uuid_cache_locked.once_token
+ _ne_session_get_boot_session_uuid
+ _uuid_parse
- ___block_descriptor_tmp.109
- ___block_descriptor_tmp.12.235
- ___block_descriptor_tmp.150
- ___block_descriptor_tmp.151
- ___block_descriptor_tmp.153
- ___block_descriptor_tmp.164
- ___block_descriptor_tmp.167
- ___block_descriptor_tmp.168
- ___block_descriptor_tmp.174
- ___block_descriptor_tmp.176
- ___block_descriptor_tmp.182
- ___block_descriptor_tmp.183
- ___block_descriptor_tmp.186
- ___block_descriptor_tmp.204
- ___block_descriptor_tmp.207
- ___block_descriptor_tmp.210
- ___block_descriptor_tmp.214
- ___block_descriptor_tmp.218
- ___block_descriptor_tmp.222
- ___block_descriptor_tmp.225
- ___block_descriptor_tmp.231
- ___block_descriptor_tmp.252
- ___block_descriptor_tmp.262
- ___block_descriptor_tmp.8.237
- ___block_literal_global.157
- ___block_literal_global.206
- ___block_literal_global.209
- ___block_literal_global.220
- ___block_literal_global.248
- ___block_literal_global.260
- ___get_flow_divert_token_from_session_manager_block_invoke.229
- ___ne_session_get_info_with_parameters_block_invoke.178
- ___ne_session_get_info_with_parameters_block_invoke_2.181
- ___notify_client_block_invoke.173
CStrings:
+ "Failed to get kern.bootsessionuuid: [%d] %s"
+ "Failed to get the boot session uuid"
+ "Failed to get the current OS version"
+ "Not using the UUID cache because the current boot session UUID (%s) does not equal the cache boot session UUID (%s)"
+ "Populating the cache failed: %d"
+ "Sending a message to populate the cache with UUIDs from configuration %s"
+ "UUID cache hit (negative) for %s"
+ "boot-uuid"
+ "cache-app-bundle-id"
+ "kern.bootsessionuuid"
+ "sending a message to clear the UUIDs for %s from the cache"
- "Failed to get the current OS version, using the UUID cache"
- "Not using the UUID cache because the cache does not have an OS version"

```
