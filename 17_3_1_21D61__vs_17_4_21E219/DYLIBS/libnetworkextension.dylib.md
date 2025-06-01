## libnetworkextension.dylib

> `/usr/lib/libnetworkextension.dylib`

```diff

-1838.80.4.0.0
-  __TEXT.__text: 0x2a760
-  __TEXT.__auth_stubs: 0x1750
+1838.102.2.0.0
+  __TEXT.__text: 0x2b394
+  __TEXT.__auth_stubs: 0x1790
   __TEXT.__objc_methlist: 0x14
   __TEXT.__const: 0x108
-  __TEXT.__cstring: 0x2330
-  __TEXT.__oslogstring: 0x6540
-  __TEXT.__unwind_info: 0x638
+  __TEXT.__cstring: 0x2454
+  __TEXT.__oslogstring: 0x6680
+  __TEXT.__unwind_info: 0x648
   __TEXT.__objc_classname: 0x13
   __TEXT.__objc_methname: 0x11b
   __TEXT.__objc_methtype: 0x11
   __TEXT.__objc_stubs: 0x140
   __DATA_CONST.__got: 0x100
-  __DATA_CONST.__const: 0x1678
+  __DATA_CONST.__const: 0x17a0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x48
   __DATA_CONST.__objc_selrefs: 0x50
-  __AUTH_CONST.__cfstring: 0x360
-  __AUTH_CONST.__const: 0x160
+  __DATA_CONST.__objc_classrefs: 0x20
+  __AUTH_CONST.__cfstring: 0x5c0
+  __AUTH_CONST.__const: 0x1e0
   __AUTH_CONST.__objc_const: 0x48
-  __AUTH_CONST.__auth_got: 0xbb0
+  __AUTH_CONST.__auth_got: 0xbd0
   __AUTH.__objc_data: 0x50
-  __DATA.__objc_classrefs: 0x20
-  __DATA.__data: 0x504
-  __DATA.__common: 0x45
-  __DATA.__bss: 0x3a0
-  __DATA_DIRTY.__const: 0x160
-  __DATA_DIRTY.__data: 0xc
-  __DATA_DIRTY.__bss: 0x4e8
+  __DATA.__data: 0x73c
+  __DATA.__common: 0x3d
+  __DATA.__bss: 0x390
+  __DATA_DIRTY.__const: 0xe0
+  __DATA_DIRTY.__data: 0x8
+  __DATA_DIRTY.__bss: 0x2f8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Network.framework/Network

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 706ECC20-44E4-3F8A-B45C-A1182E5AC57E
-  Functions: 511
-  Symbols:   1415
-  CStrings:  863
+  UUID: 7A1C7D2E-5D23-3AC4-8A08-4ECFC466ACE8
+  Functions: 517
+  Symbols:   1434
+  CStrings:  909
 
Symbols:
+ _CFDictionaryCreate
+ _NEFlowCopyStateDictionary
+ _NEFlowDirectorFetchFlowStates
+ ___NEFlowDirectorFetchFlowStates_block_invoke
+ ___block_descriptor_tmp.102
+ ___block_descriptor_tmp.108
+ ___block_descriptor_tmp.110
+ ___block_descriptor_tmp.111
+ ___block_descriptor_tmp.116
+ ___block_descriptor_tmp.117
+ ___block_descriptor_tmp.119
+ ___block_descriptor_tmp.12.404
+ ___block_descriptor_tmp.120
+ ___block_descriptor_tmp.121
+ ___block_descriptor_tmp.123
+ ___block_descriptor_tmp.125
+ ___block_descriptor_tmp.13.405
+ ___block_descriptor_tmp.13.518
+ ___block_descriptor_tmp.133
+ ___block_descriptor_tmp.14
+ ___block_descriptor_tmp.147
+ ___block_descriptor_tmp.148
+ ___block_descriptor_tmp.154
+ ___block_descriptor_tmp.157
+ ___block_descriptor_tmp.157.277
+ ___block_descriptor_tmp.158
+ ___block_descriptor_tmp.159
+ ___block_descriptor_tmp.160.101
+ ___block_descriptor_tmp.163
+ ___block_descriptor_tmp.169
+ ___block_descriptor_tmp.171
+ ___block_descriptor_tmp.172
+ ___block_descriptor_tmp.172.106
+ ___block_descriptor_tmp.173
+ ___block_descriptor_tmp.173.104
+ ___block_descriptor_tmp.177
+ ___block_descriptor_tmp.18.415
+ ___block_descriptor_tmp.181
+ ___block_descriptor_tmp.184
+ ___block_descriptor_tmp.188
+ ___block_descriptor_tmp.188.143
+ ___block_descriptor_tmp.19.416
+ ___block_descriptor_tmp.190
+ ___block_descriptor_tmp.190.150
+ ___block_descriptor_tmp.191
+ ___block_descriptor_tmp.192
+ ___block_descriptor_tmp.194
+ ___block_descriptor_tmp.196
+ ___block_descriptor_tmp.198
+ ___block_descriptor_tmp.20.367
+ ___block_descriptor_tmp.20.417
+ ___block_descriptor_tmp.200
+ ___block_descriptor_tmp.202
+ ___block_descriptor_tmp.205
+ ___block_descriptor_tmp.208
+ ___block_descriptor_tmp.209
+ ___block_descriptor_tmp.212
+ ___block_descriptor_tmp.215
+ ___block_descriptor_tmp.219
+ ___block_descriptor_tmp.227
+ ___block_descriptor_tmp.228
+ ___block_descriptor_tmp.230
+ ___block_descriptor_tmp.241
+ ___block_descriptor_tmp.29
+ ___block_descriptor_tmp.296
+ ___block_descriptor_tmp.30.373
+ ___block_descriptor_tmp.35.451
+ ___block_descriptor_tmp.358
+ ___block_descriptor_tmp.41.426
+ ___block_descriptor_tmp.410
+ ___block_descriptor_tmp.42.424
+ ___block_descriptor_tmp.48.472
+ ___block_descriptor_tmp.50.477
+ ___block_descriptor_tmp.64.493
+ ___block_literal_global.104
+ ___block_literal_global.122
+ ___block_literal_global.149
+ ___block_literal_global.165
+ ___block_literal_global.167
+ ___block_literal_global.175
+ ___block_literal_global.211
+ ___block_literal_global.214
+ ___block_literal_global.225
+ ___block_literal_global.294
+ ___block_literal_global.360
+ ___block_literal_global.408
+ ___flow_director_handle_data_block_invoke.170
+ ___flow_director_handle_flow_states_block_invoke
+ ___flow_startup_block_invoke.191
+ ___flow_startup_block_invoke.193
+ ___get_flow_divert_token_from_session_manager_block_invoke.234
+ ___ne_copy_uuid_cache_locked_block_invoke
+ ___ne_filter_request_xpc_connection_block_invoke.24
+ ___ne_filter_request_xpc_connection_block_invoke.28
+ ___ne_filter_stats_report_register_block_invoke_2
+ ___ne_session_get_info_with_parameters_block_invoke.183
+ ___ne_session_get_info_with_parameters_block_invoke_2.186
+ ___notify_client_block_invoke.178
+ _ne_copy_uuid_cache_locked.g_my_boot_session_uuid
+ _ne_copy_uuid_cache_locked.once_token
+ _ne_session_get_boot_session_uuid
+ _ne_session_trim_domain.domain_buffer.206
+ _uuid_parse
+ _xpc_connection_get_context
+ _xpc_connection_set_context
- ___block_descriptor_tmp.100
- ___block_descriptor_tmp.101
- ___block_descriptor_tmp.104
- ___block_descriptor_tmp.109
- ___block_descriptor_tmp.113
- ___block_descriptor_tmp.12.403
- ___block_descriptor_tmp.122
- ___block_descriptor_tmp.129
- ___block_descriptor_tmp.13.387
- ___block_descriptor_tmp.13.511
- ___block_descriptor_tmp.131
- ___block_descriptor_tmp.137
- ___block_descriptor_tmp.139
- ___block_descriptor_tmp.141
- ___block_descriptor_tmp.143
- ___block_descriptor_tmp.145
- ___block_descriptor_tmp.146
- ___block_descriptor_tmp.150
- ___block_descriptor_tmp.151.274
- ___block_descriptor_tmp.153
- ___block_descriptor_tmp.164
- ___block_descriptor_tmp.167
- ___block_descriptor_tmp.174
- ___block_descriptor_tmp.176
- ___block_descriptor_tmp.18.412
- ___block_descriptor_tmp.182
- ___block_descriptor_tmp.183
- ___block_descriptor_tmp.186
- ___block_descriptor_tmp.19.413
- ___block_descriptor_tmp.20.414
- ___block_descriptor_tmp.207
- ___block_descriptor_tmp.21
- ___block_descriptor_tmp.214
- ___block_descriptor_tmp.218
- ___block_descriptor_tmp.222
- ___block_descriptor_tmp.225
- ___block_descriptor_tmp.231
- ___block_descriptor_tmp.293
- ___block_descriptor_tmp.30.377
- ___block_descriptor_tmp.31.368
- ___block_descriptor_tmp.35.448
- ___block_descriptor_tmp.355
- ___block_descriptor_tmp.407
- ___block_descriptor_tmp.41.423
- ___block_descriptor_tmp.42.141
- ___block_descriptor_tmp.42.421
- ___block_descriptor_tmp.48.465
- ___block_descriptor_tmp.48.53
- ___block_descriptor_tmp.50.147
- ___block_descriptor_tmp.50.470
- ___block_descriptor_tmp.51
- ___block_descriptor_tmp.52.148
- ___block_descriptor_tmp.54.146
- ___block_descriptor_tmp.56
- ___block_descriptor_tmp.57
- ___block_descriptor_tmp.58
- ___block_descriptor_tmp.59
- ___block_descriptor_tmp.60
- ___block_descriptor_tmp.64.183
- ___block_descriptor_tmp.64.486
- ___block_descriptor_tmp.74
- ___block_descriptor_tmp.76
- ___block_descriptor_tmp.92.210
- ___block_descriptor_tmp.93
- ___block_descriptor_tmp.94
- ___block_descriptor_tmp.99
- ___block_literal_global.106
- ___block_literal_global.116
- ___block_literal_global.119
- ___block_literal_global.15
- ___block_literal_global.157
- ___block_literal_global.206
- ___block_literal_global.209
- ___block_literal_global.220
- ___block_literal_global.291
- ___block_literal_global.400
- ___block_literal_global.405
- ___block_literal_global.44
- ___flow_director_handle_data_block_invoke.111
- ___flow_startup_block_invoke.132
- ___flow_startup_block_invoke.134
- ___get_flow_divert_token_from_session_manager_block_invoke.229
- ___ne_filter_request_xpc_connection_block_invoke.25
- ___ne_filter_request_xpc_connection_block_invoke.29
- ___ne_session_get_info_with_parameters_block_invoke.178
- ___ne_session_get_info_with_parameters_block_invoke_2.181
- ___notify_client_block_invoke.173
- _g_stats_globals
- _ne_filter_stats_destroy
- _ne_session_trim_domain.domain_buffer.205
CStrings:
+ "(%u): Cannot find flow with ID from flow state (%u)"
+ "(%u): Destroying, client tx %llu, client rx %llu, kernel rx %llu, kernel tx %llu"
+ "(%u): Got a flow state TLV with an invalid length: %u"
+ "(%u): Got a non-state TLV: %u"
+ "(%u): Got flow states, but no callback is available"
+ "(%u): Wrote %ld bytes to the kernel (total bytes written = %llu)"
+ "Agent"
+ "BytesReceivedByProvider"
+ "BytesReceivedFromAgent"
+ "BytesReceivedFromKernel"
+ "BytesSentByApp"
+ "BytesSentByProvider"
+ "BytesSentToAgent"
+ "BytesSentToKernel"
+ "Failed to get kern.bootsessionuuid: [%d] %s"
+ "Failed to get the boot session uuid"
+ "Failed to get the current OS version"
+ "HasReadHandler"
+ "ID"
+ "Kernel"
+ "Not using the UUID cache because the current boot session UUID (%s) does not equal the cache boot session UUID (%s)"
+ "ReadBufferSize"
+ "RemoteEndpoint"
+ "RemoteHostname"
+ "SendBufferSize"
+ "SendWindow"
+ "SourceApp"
+ "TCP"
+ "UDP"
+ "boot-uuid"
+ "kern.bootsessionuuid"
+ "ne_filter_stats_report_register - dispatch_source_create failed"
- "(%u): Destroying, client tx %u, client rx %u, kernel rx %u, kernel tx %u"
- "(%u): Wrote %ld bytes to the kernel (total bytes written = %u)"
- "Failed to get the current OS version, using the UUID cache"
- "Not using the UUID cache because the cache does not have an OS version"
- "Stats toggle - dispatch_source_create failed"

```
