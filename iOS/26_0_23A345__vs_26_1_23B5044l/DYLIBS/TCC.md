## TCC

> `/System/Library/PrivateFrameworks/TCC.framework/TCC`

```diff

-854.0.1.0.0
-  __TEXT.__text: 0x12a58
-  __TEXT.__auth_stubs: 0xac0
+857.0.7.0.0
+  __TEXT.__text: 0x1306c
+  __TEXT.__auth_stubs: 0xae0
   __TEXT.__objc_methlist: 0x11c
-  __TEXT.__cstring: 0x2aed
+  __TEXT.__cstring: 0x2b7e
+  __TEXT.__oslogstring: 0x101b
   __TEXT.__const: 0x398
-  __TEXT.__oslogstring: 0xf9f
-  __TEXT.__unwind_info: 0x510
+  __TEXT.__unwind_info: 0x530
   __TEXT.__objc_classname: 0x120
   __TEXT.__objc_methname: 0x147
   __TEXT.__objc_methtype: 0xb5
   __DATA_CONST.__got: 0xc8
-  __DATA_CONST.__const: 0x14a8
+  __DATA_CONST.__const: 0x1538
   __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xa8
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x560
+  __AUTH_CONST.__auth_got: 0x570
   __AUTH_CONST.__const: 0x298
-  __AUTH_CONST.__cfstring: 0x13e0
+  __AUTH_CONST.__cfstring: 0x1420
   __AUTH_CONST.__objc_const: 0xe50
   __AUTH.__objc_data: 0xf0
   __AUTH.__data: 0x1e0
-  __DATA.__data: 0x8a0
+  __DATA.__data: 0x8a8
   __DATA.__bss: 0x70
   __DATA_DIRTY.__objc_data: 0x320
   __DATA_DIRTY.__bss: 0x90

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9F6350C4-C5B0-3AAD-9F1A-17DF3195A0BB
-  Functions: 478
-  Symbols:   1491
-  CStrings:  729
+  UUID: 6645B72D-B372-3059-88BF-FE3706921F2C
+  Functions: 488
+  Symbols:   1516
+  CStrings:  742
 
Symbols:
+ _CFStringGetMaximumSizeForEncoding
+ _CFUUIDCreateString
+ _TCCAccessResetAll
+ ___TCCAccessCopyBundleIdentifiersDisabledForService_block_invoke.373
+ ___TCCAccessCopyBundleIdentifiersForService_block_invoke.368
+ ___TCCAccessRequest_block_invoke.284
+ ___TCCAccessRequest_block_invoke_2.289
+ ___TCCAccessResetAll_block_invoke
+ ___TCCAccessResetAll_block_invoke_2
+ ___TCCAccessResetAll_block_invoke_2.cold.1
+ ___TCCAccessResetAll_block_invoke_2.cold.2
+ ____tcc_server_send_get_authorization_records_block_invoke.114
+ ____tcc_server_send_get_authorization_records_by_services_block_invoke.151
+ ____tcc_server_send_get_authorization_records_by_services_block_invoke.151.cold.1
+ ____tcc_server_send_get_authorization_records_by_services_block_invoke.157
+ ____tcc_server_send_get_identity_for_credential_block_invoke.127
+ ____tcc_server_send_get_identity_for_credential_block_invoke_2.131
+ ____tcc_server_send_get_identity_for_credential_block_invoke_2.131.cold.1
+ ____tcc_server_send_get_identity_for_credential_block_invoke_2.131.cold.2
+ ____tcc_server_send_prompt_authorization_value_block_invoke.100
+ ____tcc_server_send_prompt_authorization_value_block_invoke_2.104
+ ____tcc_server_send_prompt_authorization_value_block_invoke_2.104.cold.1
+ ____tcc_server_send_prompt_authorization_value_block_invoke_2.104.cold.2
+ ____tcc_server_send_report_resource_use_block_invoke.139
+ ____tcc_server_send_report_resource_use_block_invoke_2.143
+ ____tcc_server_send_report_resource_use_block_invoke_2.143.cold.1
+ ____tcc_server_send_report_resource_use_block_invoke_2.143.cold.2
+ ____tcc_server_send_request_authorization_block_invoke.71
+ ____tcc_server_send_request_authorization_block_invoke.94
+ ____tcc_server_send_request_authorization_block_invoke_2.98
+ ___block_descriptor_tmp.102
+ ___block_descriptor_tmp.103
+ ___block_descriptor_tmp.105
+ ___block_descriptor_tmp.106
+ ___block_descriptor_tmp.116
+ ___block_descriptor_tmp.117
+ ___block_descriptor_tmp.118
+ ___block_descriptor_tmp.129
+ ___block_descriptor_tmp.130
+ ___block_descriptor_tmp.132
+ ___block_descriptor_tmp.133
+ ___block_descriptor_tmp.140
+ ___block_descriptor_tmp.141
+ ___block_descriptor_tmp.142
+ ___block_descriptor_tmp.144
+ ___block_descriptor_tmp.156
+ ___block_descriptor_tmp.158
+ ___block_descriptor_tmp.160
+ ___block_descriptor_tmp.164
+ ___block_descriptor_tmp.259
+ ___block_descriptor_tmp.260
+ ___block_descriptor_tmp.264
+ ___block_descriptor_tmp.272
+ ___block_descriptor_tmp.273
+ ___block_descriptor_tmp.275
+ ___block_descriptor_tmp.285
+ ___block_descriptor_tmp.287
+ ___block_descriptor_tmp.288
+ ___block_descriptor_tmp.290
+ ___block_descriptor_tmp.297
+ ___block_descriptor_tmp.299
+ ___block_descriptor_tmp.305
+ ___block_descriptor_tmp.306
+ ___block_descriptor_tmp.307
+ ___block_descriptor_tmp.324
+ ___block_descriptor_tmp.325
+ ___block_descriptor_tmp.363
+ ___block_descriptor_tmp.364
+ ___block_descriptor_tmp.374
+ ___block_descriptor_tmp.375
+ ___block_descriptor_tmp.376
+ ___block_descriptor_tmp.398
+ ___block_descriptor_tmp.403
+ ___block_descriptor_tmp.404
+ ___block_descriptor_tmp.410
+ ___block_descriptor_tmp.412
+ ___block_descriptor_tmp.413
+ ___block_descriptor_tmp.418
+ ___block_descriptor_tmp.419
+ ___block_descriptor_tmp.420
+ ___block_descriptor_tmp.425
+ ___block_descriptor_tmp.426
+ ___block_descriptor_tmp.436
+ ___block_descriptor_tmp.437
+ ___block_descriptor_tmp.444
+ ___block_descriptor_tmp.445
+ ___block_descriptor_tmp.473
+ ___block_descriptor_tmp.474
+ ___block_descriptor_tmp.48
+ ___block_descriptor_tmp.480
+ ___block_descriptor_tmp.497
+ ___block_descriptor_tmp.507
+ ___block_descriptor_tmp.508
+ ___block_descriptor_tmp.511
+ ___block_descriptor_tmp.512
+ ___block_descriptor_tmp.60
+ ___block_descriptor_tmp.63
+ ___block_descriptor_tmp.70
+ ___block_descriptor_tmp.72
+ ___block_descriptor_tmp.95
+ ___block_descriptor_tmp.99
+ ___block_literal_global.108
+ ___block_literal_global.135
+ ___block_literal_global.262
+ ___block_literal_global.301
+ ___block_literal_global.304
+ ___block_literal_global.417
+ ___block_literal_global.496
+ ___block_literal_global.499
+ ___block_literal_global.62
+ ___block_literal_global.65
+ ___tcc_server_message_set_authorization_value_block_invoke
+ _createCStringFromCFUUID
+ _createCStringFromCFUUID.cold.1
+ _createCStringFromCFUUID.cold.2
+ _kTCCServiceEnergyKitGuidance
+ _tcc_message_options_get_prompt_string_type
+ _tcc_message_options_set_prompt_string_type
- ___TCCAccessCopyBundleIdentifiersDisabledForService_block_invoke.369
- ___TCCAccessCopyBundleIdentifiersForService_block_invoke.364
- ___TCCAccessRequest_block_invoke.280
- ___TCCAccessRequest_block_invoke_2.285
- ____tcc_server_send_get_authorization_records_block_invoke.109
- ____tcc_server_send_get_authorization_records_by_services_block_invoke.146
- ____tcc_server_send_get_authorization_records_by_services_block_invoke.146.cold.1
- ____tcc_server_send_get_authorization_records_by_services_block_invoke.147
- ____tcc_server_send_get_identity_for_credential_block_invoke.122
- ____tcc_server_send_get_identity_for_credential_block_invoke_2.126
- ____tcc_server_send_get_identity_for_credential_block_invoke_2.126.cold.1
- ____tcc_server_send_get_identity_for_credential_block_invoke_2.126.cold.2
- ____tcc_server_send_prompt_authorization_value_block_invoke.95
- ____tcc_server_send_prompt_authorization_value_block_invoke_2.99
- ____tcc_server_send_prompt_authorization_value_block_invoke_2.99.cold.1
- ____tcc_server_send_prompt_authorization_value_block_invoke_2.99.cold.2
- ____tcc_server_send_report_resource_use_block_invoke.134
- ____tcc_server_send_report_resource_use_block_invoke_2.138
- ____tcc_server_send_report_resource_use_block_invoke_2.138.cold.1
- ____tcc_server_send_report_resource_use_block_invoke_2.138.cold.2
- ____tcc_server_send_request_authorization_block_invoke.66
- ____tcc_server_send_request_authorization_block_invoke.89
- ____tcc_server_send_request_authorization_block_invoke_2.93
- ___block_descriptor_tmp.100
- ___block_descriptor_tmp.111
- ___block_descriptor_tmp.112
- ___block_descriptor_tmp.113
- ___block_descriptor_tmp.123
- ___block_descriptor_tmp.124
- ___block_descriptor_tmp.125
- ___block_descriptor_tmp.127
- ___block_descriptor_tmp.135
- ___block_descriptor_tmp.136
- ___block_descriptor_tmp.137
- ___block_descriptor_tmp.139
- ___block_descriptor_tmp.148
- ___block_descriptor_tmp.150
- ___block_descriptor_tmp.151
- ___block_descriptor_tmp.154
- ___block_descriptor_tmp.256
- ___block_descriptor_tmp.257
- ___block_descriptor_tmp.261
- ___block_descriptor_tmp.268
- ___block_descriptor_tmp.269
- ___block_descriptor_tmp.271
- ___block_descriptor_tmp.281
- ___block_descriptor_tmp.283
- ___block_descriptor_tmp.284
- ___block_descriptor_tmp.286
- ___block_descriptor_tmp.291
- ___block_descriptor_tmp.293
- ___block_descriptor_tmp.294
- ___block_descriptor_tmp.301
- ___block_descriptor_tmp.303
- ___block_descriptor_tmp.320
- ___block_descriptor_tmp.321
- ___block_descriptor_tmp.359
- ___block_descriptor_tmp.360
- ___block_descriptor_tmp.366
- ___block_descriptor_tmp.367
- ___block_descriptor_tmp.368
- ___block_descriptor_tmp.390
- ___block_descriptor_tmp.395
- ___block_descriptor_tmp.396
- ___block_descriptor_tmp.397
- ___block_descriptor_tmp.402
- ___block_descriptor_tmp.408
- ___block_descriptor_tmp.411
- ___block_descriptor_tmp.414
- ___block_descriptor_tmp.416
- ___block_descriptor_tmp.421
- ___block_descriptor_tmp.422
- ___block_descriptor_tmp.432
- ___block_descriptor_tmp.433
- ___block_descriptor_tmp.440
- ___block_descriptor_tmp.441
- ___block_descriptor_tmp.471
- ___block_descriptor_tmp.485
- ___block_descriptor_tmp.488
- ___block_descriptor_tmp.493
- ___block_descriptor_tmp.498
- ___block_descriptor_tmp.499
- ___block_descriptor_tmp.55
- ___block_descriptor_tmp.58
- ___block_descriptor_tmp.65
- ___block_descriptor_tmp.67
- ___block_descriptor_tmp.90
- ___block_descriptor_tmp.91
- ___block_descriptor_tmp.92
- ___block_descriptor_tmp.94
- ___block_descriptor_tmp.98
- ___block_literal_global.103
- ___block_literal_global.130
- ___block_literal_global.259
- ___block_literal_global.297
- ___block_literal_global.300
- ___block_literal_global.413
- ___block_literal_global.487
- ___block_literal_global.490
- ___block_literal_global.57
- ___block_literal_global.60
CStrings:
+ "CFStringRef get C string error"
+ "CFUUID get CFStringRef error"
+ "Invalid identity type"
+ "TCCAccessResetAll"
+ "TCCAccessResetAll_block_invoke_2"
+ "TCCResetAll() IPC"
+ "Thunderbolt"
+ "USB"
+ "kTCCServiceEnergyKitGuidance"
+ "request_prompt_string_type"
+ "tcc_authorization_set_authorization_value IPC"

```
