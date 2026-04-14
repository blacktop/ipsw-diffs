## MobileInBoxUpdate

> `/System/Library/PrivateFrameworks/MobileInBoxUpdate.framework/MobileInBoxUpdate`

```diff

-176.120.8.0.0
-  __TEXT.__text: 0x3179c
-  __TEXT.__auth_stubs: 0xdb0
-  __TEXT.__objc_methlist: 0x17b0
+176.120.15.0.0
+  __TEXT.__text: 0x32480
+  __TEXT.__auth_stubs: 0xdd0
+  __TEXT.__objc_methlist: 0x17d0
   __TEXT.__const: 0x5f58
-  __TEXT.__cstring: 0x1605
-  __TEXT.__oslogstring: 0x2459
-  __TEXT.__gcc_except_tab: 0x214
+  __TEXT.__gcc_except_tab: 0x22c
+  __TEXT.__cstring: 0x1665
+  __TEXT.__oslogstring: 0x24b9
   __TEXT.__swift5_typeref: 0xdc
   __TEXT.__swift5_fieldmd: 0x30
   __TEXT.__constg_swiftt: 0x64
   __TEXT.__swift5_capture: 0x20
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0xb78
+  __TEXT.__unwind_info: 0xbb0
   __TEXT.__eh_frame: 0x80
   __TEXT.__objc_classname: 0x2f0
-  __TEXT.__objc_methname: 0x2e1b
-  __TEXT.__objc_methtype: 0x698
-  __TEXT.__objc_stubs: 0x2aa0
+  __TEXT.__objc_methname: 0x2e7b
+  __TEXT.__objc_methtype: 0x6a8
+  __TEXT.__objc_stubs: 0x2ae0
   __DATA_CONST.__got: 0x2b8
-  __DATA_CONST.__const: 0x3d00
+  __DATA_CONST.__const: 0x3d40
   __DATA_CONST.__objc_classlist: 0xc8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xe60
+  __DATA_CONST.__objc_selrefs: 0xe78
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x80
-  __DATA_CONST.__objc_arraydata: 0x268
-  __AUTH_CONST.__auth_got: 0x6e8
-  __AUTH_CONST.__const: 0x26c8
-  __AUTH_CONST.__cfstring: 0x1ae0
+  __DATA_CONST.__objc_arraydata: 0x280
+  __AUTH_CONST.__auth_got: 0x6f8
+  __AUTH_CONST.__const: 0x2788
+  __AUTH_CONST.__cfstring: 0x1b60
   __AUTH_CONST.__objc_const: 0x2818
-  __AUTH_CONST.__objc_intobj: 0x11e8
-  __AUTH_CONST.__objc_arrayobj: 0x348
+  __AUTH_CONST.__objc_intobj: 0x1278
+  __AUTH_CONST.__objc_arrayobj: 0x390
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH.__objc_data: 0x7f0

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 145EDAC6-D5DA-32E4-85C9-FDC61D58AF73
-  Functions: 1296
-  Symbols:   4949
-  CStrings:  1403
+  UUID: 41C9AC0F-FA5C-3CE8-A84F-762499A0144F
+  Functions: 1315
+  Symbols:   5014
+  CStrings:  1417
 
Symbols:
+ +[MIBUPersonalizationManager requestTatsuTicketForDevice:withTimeout:error:]
+ +[MIBUPersonalizationManager requestTatsuTicketForDevice:withTimeout:error:].cold.1
+ +[MIBUPersonalizationManager requestTatsuTicketForDevice:withTimeout:error:].cold.2
+ -[MIBUNFCCommand _deserializeShutdown]
+ -[MIBUNFCCommand _deserializeShutdown].cold.1
+ -[MIBUNFCCommand _initWithAPDU:].cold.14
+ -[MIBUNFCCommand _serializeSSUpdate].cold.32
+ -[MIBUNFCCommand _serializeShutdown]
+ -[MIBUNFCCommand _serializeShutdown].cold.1
+ -[MIBUNFCCommand _serializeShutdown].cold.2
+ GCC_except_table6
+ ___32-[MIBUNFCCommand _initWithAPDU:]_block_invoke.146
+ ___32-[MIBUNFCCommand _initWithAPDU:]_block_invoke.146.cold.1
+ ___32-[MIBUNFCCommand _initWithAPDU:]_block_invoke.149
+ ___32-[MIBUNFCCommand _initWithAPDU:]_block_invoke.149.cold.1
+ ___32-[MIBUNFCCommand _initWithAPDU:]_block_invoke.152
+ ___32-[MIBUNFCCommand _initWithAPDU:]_block_invoke.152.cold.1
+ ___32-[MIBUNFCCommand _initWithAPDU:]_block_invoke.155
+ ___32-[MIBUNFCCommand _initWithAPDU:]_block_invoke.155.cold.1
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.251
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.251.cold.1
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.254
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.254.cold.1
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.257
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.257.cold.1
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.260
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.260.cold.1
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.268
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.268.cold.1
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.276
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.276.cold.1
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.284
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.284.cold.1
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.292
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.292.cold.1
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.300
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.300.cold.1
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.308
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.308.cold.1
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.316
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.316.cold.1
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.324
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.324.cold.1
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.332
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.332.cold.1
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.340
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.340.cold.1
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.348
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.348.cold.1
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.356
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.356.cold.1
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.364
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.364.cold.1
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.372
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.372.cold.1
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.380
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.380.cold.1
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.388
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.388.cold.1
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.396
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.396.cold.1
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.404
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.404.cold.1
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.412
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.412.cold.1
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.420
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.420.cold.1
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.428
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.428.cold.1
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.436
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.436.cold.1
+ ___36-[MIBUNFCCommand _serializeShutdown]_block_invoke
+ ___36-[MIBUNFCCommand _serializeShutdown]_block_invoke.451
+ ___36-[MIBUNFCCommand _serializeShutdown]_block_invoke.451.cold.1
+ ___36-[MIBUNFCCommand _serializeShutdown]_block_invoke.cold.1
+ ___37-[MIBUNFCCommand _serializeChallenge]_block_invoke.229
+ ___37-[MIBUNFCCommand _serializeChallenge]_block_invoke.229.cold.1
+ ___37-[MIBUNFCCommand _serializeHeartbeat]_block_invoke.178
+ ___37-[MIBUNFCCommand _serializeHeartbeat]_block_invoke.178.cold.1
+ ___37-[MIBUNFCCommand _serializeHeartbeat]_block_invoke.186
+ ___37-[MIBUNFCCommand _serializeHeartbeat]_block_invoke.186.cold.1
+ ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.506
+ ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.506.cold.1
+ ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.509
+ ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.509.cold.1
+ ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.512
+ ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.512.cold.1
+ ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.515
+ ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.515.cold.1
+ ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.518
+ ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.518.cold.1
+ ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.521
+ ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.521.cold.1
+ ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.524
+ ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.524.cold.1
+ ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.527
+ ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.527.cold.1
+ ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.530
+ ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.530.cold.1
+ ___38-[MIBUNFCCommand _deserializeShutdown]_block_invoke
+ ___38-[MIBUNFCCommand _deserializeShutdown]_block_invoke.cold.1
+ ___38-[MIBUNFCCommand _serializeRetryAfter]_block_invoke.165
+ ___38-[MIBUNFCCommand _serializeRetryAfter]_block_invoke.165.cold.1
+ ___39-[MIBUNFCCommand _deserializeChallenge]_block_invoke.499
+ ___39-[MIBUNFCCommand _deserializeChallenge]_block_invoke.499.cold.1
+ ___39-[MIBUNFCCommand _deserializeHeartbeat]_block_invoke.467
+ ___39-[MIBUNFCCommand _deserializeHeartbeat]_block_invoke.467.cold.1
+ ___39-[MIBUNFCCommand _deserializeHeartbeat]_block_invoke.470
+ ___39-[MIBUNFCCommand _deserializeHeartbeat]_block_invoke.470.cold.1
+ ___39-[MIBUNFCCommand _deserializeHeartbeat]_block_invoke.473
+ ___39-[MIBUNFCCommand _deserializeHeartbeat]_block_invoke.473.cold.1
+ ___39-[MIBUNFCCommand _deserializeHeartbeat]_block_invoke.476
+ ___39-[MIBUNFCCommand _deserializeHeartbeat]_block_invoke.476.cold.1
+ ___39-[MIBUNFCCommand _initWithCommandCode:]_block_invoke.114
+ ___39-[MIBUNFCCommand _initWithCommandCode:]_block_invoke.114.cold.1
+ ___40-[MIBUNFCCommand _deserializeRetryAfter]_block_invoke.459
+ ___40-[MIBUNFCCommand _deserializeRetryAfter]_block_invoke.459.cold.1
+ ___40-[MIBUNFCCommand _deserializeRetryAfter]_block_invoke.462
+ ___40-[MIBUNFCCommand _deserializeRetryAfter]_block_invoke.462.cold.1
+ ___40-[MIBUNFCCommand _serializeConfigureNFC]_block_invoke.196
+ ___40-[MIBUNFCCommand _serializeConfigureNFC]_block_invoke.196.cold.1
+ ___41-[MIBUNFCCommand _serializeTatsuPayload:]_block_invoke.203
+ ___41-[MIBUNFCCommand _serializeTatsuPayload:]_block_invoke.203.cold.1
+ ___41-[MIBUNFCCommand _serializeTatsuPayload:]_block_invoke.211
+ ___41-[MIBUNFCCommand _serializeTatsuPayload:]_block_invoke.211.cold.1
+ ___41-[MIBUNFCCommand _serializeTatsuPayload:]_block_invoke.219
+ ___41-[MIBUNFCCommand _serializeTatsuPayload:]_block_invoke.219.cold.1
+ ___42-[MIBUNFCCommand _deserializeConfigureNFC]_block_invoke.481
+ ___42-[MIBUNFCCommand _deserializeConfigureNFC]_block_invoke.481.cold.1
+ ___42-[MIBUNFCCommand _deserializeConfigureNFC]_block_invoke.484
+ ___42-[MIBUNFCCommand _deserializeConfigureNFC]_block_invoke.484.cold.1
+ ___42-[MIBUNFCCommand _deserializeTatsuPayload]_block_invoke.491
+ ___42-[MIBUNFCCommand _deserializeTatsuPayload]_block_invoke.491.cold.1
+ ___42-[MIBUNFCCommand _deserializeTatsuPayload]_block_invoke.494
+ ___42-[MIBUNFCCommand _deserializeTatsuPayload]_block_invoke.494.cold.1
+ ___64+[MIBUPersonalizationManager requestTatsuTicketForDevice:error:]_block_invoke.102
+ ___64+[MIBUPersonalizationManager requestTatsuTicketForDevice:error:]_block_invoke.102.cold.1
+ ___64+[MIBUPersonalizationManager requestTatsuTicketForDevice:error:]_block_invoke.114
+ ___64+[MIBUPersonalizationManager requestTatsuTicketForDevice:error:]_block_invoke.114.cold.1
+ ___64+[MIBUPersonalizationManager requestTatsuTicketForDevice:error:]_block_invoke.120
+ ___64+[MIBUPersonalizationManager requestTatsuTicketForDevice:error:]_block_invoke.120.cold.1
+ ___64+[MIBUPersonalizationManager requestTatsuTicketForDevice:error:]_block_invoke.123
+ ___64+[MIBUPersonalizationManager requestTatsuTicketForDevice:error:]_block_invoke.123.cold.1
+ ___64+[MIBUPersonalizationManager requestTatsuTicketForDevice:error:]_block_invoke.129
+ ___64+[MIBUPersonalizationManager requestTatsuTicketForDevice:error:]_block_invoke.129.cold.1
+ ___64+[MIBUPersonalizationManager requestTatsuTicketForDevice:error:]_block_invoke.20
+ ___64+[MIBUPersonalizationManager requestTatsuTicketForDevice:error:]_block_invoke.20.cold.1
+ ___64+[MIBUPersonalizationManager requestTatsuTicketForDevice:error:]_block_invoke.60
+ ___64+[MIBUPersonalizationManager requestTatsuTicketForDevice:error:]_block_invoke.60.cold.1
+ ___64+[MIBUPersonalizationManager requestTatsuTicketForDevice:error:]_block_invoke.63
+ ___64+[MIBUPersonalizationManager requestTatsuTicketForDevice:error:]_block_invoke.63.cold.1
+ ___64+[MIBUPersonalizationManager requestTatsuTicketForDevice:error:]_block_invoke.66
+ ___64+[MIBUPersonalizationManager requestTatsuTicketForDevice:error:]_block_invoke.66.cold.1
+ ___64+[MIBUPersonalizationManager requestTatsuTicketForDevice:error:]_block_invoke.72
+ ___64+[MIBUPersonalizationManager requestTatsuTicketForDevice:error:]_block_invoke.72.cold.1
+ ___64+[MIBUPersonalizationManager requestTatsuTicketForDevice:error:]_block_invoke.75
+ ___64+[MIBUPersonalizationManager requestTatsuTicketForDevice:error:]_block_invoke.75.cold.1
+ ___64+[MIBUPersonalizationManager requestTatsuTicketForDevice:error:]_block_invoke.78
+ ___64+[MIBUPersonalizationManager requestTatsuTicketForDevice:error:]_block_invoke.78.cold.1
+ ___64+[MIBUPersonalizationManager requestTatsuTicketForDevice:error:]_block_invoke.81
+ ___64+[MIBUPersonalizationManager requestTatsuTicketForDevice:error:]_block_invoke.81.cold.1
+ ___64+[MIBUPersonalizationManager requestTatsuTicketForDevice:error:]_block_invoke.87
+ ___64+[MIBUPersonalizationManager requestTatsuTicketForDevice:error:]_block_invoke.87.cold.1
+ ___64+[MIBUPersonalizationManager requestTatsuTicketForDevice:error:]_block_invoke.93
+ ___64+[MIBUPersonalizationManager requestTatsuTicketForDevice:error:]_block_invoke.93.cold.1
+ ___64+[MIBUPersonalizationManager requestTatsuTicketForDevice:error:]_block_invoke.96
+ ___64+[MIBUPersonalizationManager requestTatsuTicketForDevice:error:]_block_invoke.96.cold.1
+ ___67+[MIBUPersonalizationManager _createBaseAMAIObjectForDevice:error:]_block_invoke.140
+ ___67+[MIBUPersonalizationManager _createBaseAMAIObjectForDevice:error:]_block_invoke.140.cold.1
+ ___67+[MIBUPersonalizationManager _createBaseAMAIObjectForDevice:error:]_block_invoke.146
+ ___67+[MIBUPersonalizationManager _createBaseAMAIObjectForDevice:error:]_block_invoke.146.cold.1
+ ___67+[MIBUPersonalizationManager _createBaseAMAIObjectForDevice:error:]_block_invoke.152
+ ___67+[MIBUPersonalizationManager _createBaseAMAIObjectForDevice:error:]_block_invoke.152.cold.1
+ ___67+[MIBUPersonalizationManager _createBaseAMAIObjectForDevice:error:]_block_invoke.158
+ ___67+[MIBUPersonalizationManager _createBaseAMAIObjectForDevice:error:]_block_invoke.158.cold.1
+ ___67+[MIBUPersonalizationManager _createBaseAMAIObjectForDevice:error:]_block_invoke.164
+ ___67+[MIBUPersonalizationManager _createBaseAMAIObjectForDevice:error:]_block_invoke.164.cold.1
+ ___67+[MIBUPersonalizationManager _createBaseAMAIObjectForDevice:error:]_block_invoke.170
+ ___67+[MIBUPersonalizationManager _createBaseAMAIObjectForDevice:error:]_block_invoke.170.cold.1
+ ___76+[MIBUPersonalizationManager requestTatsuTicketForDevice:withTimeout:error:]_block_invoke
+ ___76+[MIBUPersonalizationManager requestTatsuTicketForDevice:withTimeout:error:]_block_invoke_2
+ ___76+[MIBUPersonalizationManager requestTatsuTicketForDevice:withTimeout:error:]_block_invoke_2.cold.1
+ ___block_descriptor_64_e8_32s40s48r56r_e5_v8?0lr48l8s32l8r56l8s40l8
+ ___block_literal_global.104
+ ___block_literal_global.116
+ ___block_literal_global.125
+ ___block_literal_global.14
+ ___block_literal_global.151
+ ___block_literal_global.154
+ ___block_literal_global.160
+ ___block_literal_global.162
+ ___block_literal_global.166
+ ___block_literal_global.172
+ ___block_literal_global.180
+ ___block_literal_global.181
+ ___block_literal_global.198
+ ___block_literal_global.200
+ ___block_literal_global.202
+ ___block_literal_global.205
+ ___block_literal_global.213
+ ___block_literal_global.231
+ ___block_literal_global.233
+ ___block_literal_global.253
+ ___block_literal_global.256
+ ___block_literal_global.259
+ ___block_literal_global.262
+ ___block_literal_global.270
+ ___block_literal_global.278
+ ___block_literal_global.286
+ ___block_literal_global.294
+ ___block_literal_global.302
+ ___block_literal_global.310
+ ___block_literal_global.318
+ ___block_literal_global.326
+ ___block_literal_global.334
+ ___block_literal_global.342
+ ___block_literal_global.350
+ ___block_literal_global.358
+ ___block_literal_global.366
+ ___block_literal_global.374
+ ___block_literal_global.382
+ ___block_literal_global.390
+ ___block_literal_global.398
+ ___block_literal_global.406
+ ___block_literal_global.414
+ ___block_literal_global.422
+ ___block_literal_global.430
+ ___block_literal_global.438
+ ___block_literal_global.464
+ ___block_literal_global.469
+ ___block_literal_global.472
+ ___block_literal_global.475
+ ___block_literal_global.478
+ ___block_literal_global.480
+ ___block_literal_global.483
+ ___block_literal_global.486
+ ___block_literal_global.490
+ ___block_literal_global.493
+ ___block_literal_global.496
+ ___block_literal_global.498
+ ___block_literal_global.501
+ ___block_literal_global.503
+ ___block_literal_global.505
+ ___block_literal_global.508
+ ___block_literal_global.511
+ ___block_literal_global.514
+ ___block_literal_global.517
+ ___block_literal_global.520
+ ___block_literal_global.523
+ ___block_literal_global.526
+ ___block_literal_global.529
+ ___block_literal_global.532
+ ___block_literal_global.534
+ ___block_literal_global.62
+ ___block_literal_global.74
+ ___block_literal_global.80
+ ___block_literal_global.89
+ ___block_literal_global.95
+ ___block_literal_global.98
+ _dispatch_get_global_queue
+ _dispatch_time
+ _kMIBUNFCCommandEnableLPMSUKey
+ _kMIBUNFCCommandPostUpdateTimeoutKey
+ _kMIBUNFCCommandShutdownDelayKey
+ _objc_msgSend$_deserializeShutdown
+ _objc_msgSend$_serializeShutdown
- ___32-[MIBUNFCCommand _initWithAPDU:]_block_invoke.110
- ___32-[MIBUNFCCommand _initWithAPDU:]_block_invoke.110.cold.1
- ___32-[MIBUNFCCommand _initWithAPDU:]_block_invoke.113
- ___32-[MIBUNFCCommand _initWithAPDU:]_block_invoke.113.cold.1
- ___32-[MIBUNFCCommand _initWithAPDU:]_block_invoke.116
- ___32-[MIBUNFCCommand _initWithAPDU:]_block_invoke.116.cold.1
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.224
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.224.cold.1
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.227
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.227.cold.1
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.230
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.230.cold.1
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.233
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.233.cold.1
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.256
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.256.cold.1
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.264
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.264.cold.1
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.272
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.272.cold.1
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.280
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.280.cold.1
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.288
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.288.cold.1
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.296
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.296.cold.1
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.304
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.304.cold.1
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.312
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.312.cold.1
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.320
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.320.cold.1
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.328
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.328.cold.1
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.336
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.336.cold.1
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.344
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.344.cold.1
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.352
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.352.cold.1
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.360
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.360.cold.1
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.368
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.368.cold.1
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.376
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.376.cold.1
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.384
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.384.cold.1
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.392
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.392.cold.1
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.400
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.400.cold.1
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.408
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.408.cold.1
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.416
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.416.cold.1
- ___37-[MIBUNFCCommand _serializeChallenge]_block_invoke.217
- ___37-[MIBUNFCCommand _serializeChallenge]_block_invoke.217.cold.1
- ___37-[MIBUNFCCommand _serializeHeartbeat]_block_invoke.166
- ___37-[MIBUNFCCommand _serializeHeartbeat]_block_invoke.166.cold.1
- ___37-[MIBUNFCCommand _serializeHeartbeat]_block_invoke.174
- ___37-[MIBUNFCCommand _serializeHeartbeat]_block_invoke.174.cold.1
- ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.471
- ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.471.cold.1
- ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.474
- ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.474.cold.1
- ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.477
- ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.477.cold.1
- ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.480
- ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.480.cold.1
- ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.483
- ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.483.cold.1
- ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.486
- ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.486.cold.1
- ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.489
- ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.489.cold.1
- ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.492
- ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.492.cold.1
- ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.495
- ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.495.cold.1
- ___38-[MIBUNFCCommand _serializeRetryAfter]_block_invoke.153
- ___38-[MIBUNFCCommand _serializeRetryAfter]_block_invoke.153.cold.1
- ___39-[MIBUNFCCommand _deserializeChallenge]_block_invoke.464
- ___39-[MIBUNFCCommand _deserializeChallenge]_block_invoke.464.cold.1
- ___39-[MIBUNFCCommand _deserializeHeartbeat]_block_invoke.432
- ___39-[MIBUNFCCommand _deserializeHeartbeat]_block_invoke.432.cold.1
- ___39-[MIBUNFCCommand _deserializeHeartbeat]_block_invoke.435
- ___39-[MIBUNFCCommand _deserializeHeartbeat]_block_invoke.435.cold.1
- ___39-[MIBUNFCCommand _deserializeHeartbeat]_block_invoke.438
- ___39-[MIBUNFCCommand _deserializeHeartbeat]_block_invoke.438.cold.1
- ___39-[MIBUNFCCommand _deserializeHeartbeat]_block_invoke.441
- ___39-[MIBUNFCCommand _deserializeHeartbeat]_block_invoke.441.cold.1
- ___39-[MIBUNFCCommand _initWithCommandCode:]_block_invoke.105
- ___39-[MIBUNFCCommand _initWithCommandCode:]_block_invoke.105.cold.1
- ___40-[MIBUNFCCommand _deserializeRetryAfter]_block_invoke.424
- ___40-[MIBUNFCCommand _deserializeRetryAfter]_block_invoke.424.cold.1
- ___40-[MIBUNFCCommand _deserializeRetryAfter]_block_invoke.427
- ___40-[MIBUNFCCommand _deserializeRetryAfter]_block_invoke.427.cold.1
- ___40-[MIBUNFCCommand _serializeConfigureNFC]_block_invoke.184
- ___40-[MIBUNFCCommand _serializeConfigureNFC]_block_invoke.184.cold.1
- ___41-[MIBUNFCCommand _serializeTatsuPayload:]_block_invoke.191
- ___41-[MIBUNFCCommand _serializeTatsuPayload:]_block_invoke.191.cold.1
- ___41-[MIBUNFCCommand _serializeTatsuPayload:]_block_invoke.199
- ___41-[MIBUNFCCommand _serializeTatsuPayload:]_block_invoke.199.cold.1
- ___41-[MIBUNFCCommand _serializeTatsuPayload:]_block_invoke.207
- ___41-[MIBUNFCCommand _serializeTatsuPayload:]_block_invoke.207.cold.1
- ___42-[MIBUNFCCommand _deserializeConfigureNFC]_block_invoke.446
- ___42-[MIBUNFCCommand _deserializeConfigureNFC]_block_invoke.446.cold.1
- ___42-[MIBUNFCCommand _deserializeConfigureNFC]_block_invoke.449
- ___42-[MIBUNFCCommand _deserializeConfigureNFC]_block_invoke.449.cold.1
- ___42-[MIBUNFCCommand _deserializeTatsuPayload]_block_invoke.456
- ___42-[MIBUNFCCommand _deserializeTatsuPayload]_block_invoke.456.cold.1
- ___42-[MIBUNFCCommand _deserializeTatsuPayload]_block_invoke.459
- ___42-[MIBUNFCCommand _deserializeTatsuPayload]_block_invoke.459.cold.1
- ___64+[MIBUPersonalizationManager requestTatsuTicketForDevice:error:]_block_invoke.109
- ___64+[MIBUPersonalizationManager requestTatsuTicketForDevice:error:]_block_invoke.109.cold.1
- ___64+[MIBUPersonalizationManager requestTatsuTicketForDevice:error:]_block_invoke.115
- ___64+[MIBUPersonalizationManager requestTatsuTicketForDevice:error:]_block_invoke.115.cold.1
- ___64+[MIBUPersonalizationManager requestTatsuTicketForDevice:error:]_block_invoke.118
- ___64+[MIBUPersonalizationManager requestTatsuTicketForDevice:error:]_block_invoke.118.cold.1
- ___64+[MIBUPersonalizationManager requestTatsuTicketForDevice:error:]_block_invoke.124
- ___64+[MIBUPersonalizationManager requestTatsuTicketForDevice:error:]_block_invoke.124.cold.1
- ___64+[MIBUPersonalizationManager requestTatsuTicketForDevice:error:]_block_invoke.17
- ___64+[MIBUPersonalizationManager requestTatsuTicketForDevice:error:]_block_invoke.17.cold.1
- ___64+[MIBUPersonalizationManager requestTatsuTicketForDevice:error:]_block_invoke.55
- ___64+[MIBUPersonalizationManager requestTatsuTicketForDevice:error:]_block_invoke.55.cold.1
- ___64+[MIBUPersonalizationManager requestTatsuTicketForDevice:error:]_block_invoke.58
- ___64+[MIBUPersonalizationManager requestTatsuTicketForDevice:error:]_block_invoke.58.cold.1
- ___64+[MIBUPersonalizationManager requestTatsuTicketForDevice:error:]_block_invoke.61
- ___64+[MIBUPersonalizationManager requestTatsuTicketForDevice:error:]_block_invoke.61.cold.1
- ___64+[MIBUPersonalizationManager requestTatsuTicketForDevice:error:]_block_invoke.67
- ___64+[MIBUPersonalizationManager requestTatsuTicketForDevice:error:]_block_invoke.67.cold.1
- ___64+[MIBUPersonalizationManager requestTatsuTicketForDevice:error:]_block_invoke.70
- ___64+[MIBUPersonalizationManager requestTatsuTicketForDevice:error:]_block_invoke.70.cold.1
- ___64+[MIBUPersonalizationManager requestTatsuTicketForDevice:error:]_block_invoke.73
- ___64+[MIBUPersonalizationManager requestTatsuTicketForDevice:error:]_block_invoke.73.cold.1
- ___64+[MIBUPersonalizationManager requestTatsuTicketForDevice:error:]_block_invoke.76
- ___64+[MIBUPersonalizationManager requestTatsuTicketForDevice:error:]_block_invoke.76.cold.1
- ___64+[MIBUPersonalizationManager requestTatsuTicketForDevice:error:]_block_invoke.82
- ___64+[MIBUPersonalizationManager requestTatsuTicketForDevice:error:]_block_invoke.82.cold.1
- ___64+[MIBUPersonalizationManager requestTatsuTicketForDevice:error:]_block_invoke.88
- ___64+[MIBUPersonalizationManager requestTatsuTicketForDevice:error:]_block_invoke.88.cold.1
- ___64+[MIBUPersonalizationManager requestTatsuTicketForDevice:error:]_block_invoke.91
- ___64+[MIBUPersonalizationManager requestTatsuTicketForDevice:error:]_block_invoke.91.cold.1
- ___64+[MIBUPersonalizationManager requestTatsuTicketForDevice:error:]_block_invoke.97
- ___64+[MIBUPersonalizationManager requestTatsuTicketForDevice:error:]_block_invoke.97.cold.1
- ___67+[MIBUPersonalizationManager _createBaseAMAIObjectForDevice:error:]_block_invoke.135
- ___67+[MIBUPersonalizationManager _createBaseAMAIObjectForDevice:error:]_block_invoke.135.cold.1
- ___67+[MIBUPersonalizationManager _createBaseAMAIObjectForDevice:error:]_block_invoke.141
- ___67+[MIBUPersonalizationManager _createBaseAMAIObjectForDevice:error:]_block_invoke.141.cold.1
- ___67+[MIBUPersonalizationManager _createBaseAMAIObjectForDevice:error:]_block_invoke.147
- ___67+[MIBUPersonalizationManager _createBaseAMAIObjectForDevice:error:]_block_invoke.147.cold.1
- ___67+[MIBUPersonalizationManager _createBaseAMAIObjectForDevice:error:]_block_invoke.153
- ___67+[MIBUPersonalizationManager _createBaseAMAIObjectForDevice:error:]_block_invoke.153.cold.1
- ___67+[MIBUPersonalizationManager _createBaseAMAIObjectForDevice:error:]_block_invoke.159
- ___67+[MIBUPersonalizationManager _createBaseAMAIObjectForDevice:error:]_block_invoke.159.cold.1
- ___67+[MIBUPersonalizationManager _createBaseAMAIObjectForDevice:error:]_block_invoke.165
- ___67+[MIBUPersonalizationManager _createBaseAMAIObjectForDevice:error:]_block_invoke.165.cold.1
- ___block_literal_global.107
- ___block_literal_global.109
- ___block_literal_global.111
- ___block_literal_global.117
- ___block_literal_global.120
- ___block_literal_global.126
- ___block_literal_global.134
- ___block_literal_global.137
- ___block_literal_global.143
- ___block_literal_global.147
- ___block_literal_global.149
- ___block_literal_global.150
- ___block_literal_global.155
- ___block_literal_global.161
- ___block_literal_global.168
- ___block_literal_global.175
- ___block_literal_global.176
- ___block_literal_global.178
- ___block_literal_global.186
- ___block_literal_global.193
- ___block_literal_global.201
- ___block_literal_global.209
- ___block_literal_global.211
- ___block_literal_global.219
- ___block_literal_global.226
- ___block_literal_global.229
- ___block_literal_global.232
- ___block_literal_global.258
- ___block_literal_global.266
- ___block_literal_global.274
- ___block_literal_global.282
- ___block_literal_global.290
- ___block_literal_global.298
- ___block_literal_global.306
- ___block_literal_global.314
- ___block_literal_global.322
- ___block_literal_global.330
- ___block_literal_global.338
- ___block_literal_global.346
- ___block_literal_global.354
- ___block_literal_global.362
- ___block_literal_global.370
- ___block_literal_global.378
- ___block_literal_global.386
- ___block_literal_global.394
- ___block_literal_global.402
- ___block_literal_global.410
- ___block_literal_global.418
- ___block_literal_global.420
- ___block_literal_global.423
- ___block_literal_global.426
- ___block_literal_global.429
- ___block_literal_global.431
- ___block_literal_global.434
- ___block_literal_global.437
- ___block_literal_global.440
- ___block_literal_global.443
- ___block_literal_global.448
- ___block_literal_global.451
- ___block_literal_global.463
- ___block_literal_global.468
- ___block_literal_global.470
- ___block_literal_global.473
- ___block_literal_global.476
- ___block_literal_global.479
- ___block_literal_global.482
- ___block_literal_global.485
- ___block_literal_global.491
- ___block_literal_global.494
- ___block_literal_global.497
- ___block_literal_global.60
- ___block_literal_global.63
- ___block_literal_global.69
- ___block_literal_global.84
- ___block_literal_global.90
- ___block_literal_global.93
CStrings:
+ "%{public}@: Failed to request Tatsu ticket before timeout: %lu"
+ "%{public}@: Requesting personalization ticket..."
+ "@40@0:8@16Q24^@32"
+ "EnableLPMSU"
+ "Failed to deserialize shutdown command"
+ "Failed to request Tatsu ticket before timeout: %lu"
+ "PostUpdateTimeout"
+ "ShutdownDelay"
+ "_deserializeShutdown"
+ "_serializeShutdown"
+ "requestTatsuTicketForDevice:withTimeout:error:"
- "%{public}@: Requesting personalization ticket ..."

```
