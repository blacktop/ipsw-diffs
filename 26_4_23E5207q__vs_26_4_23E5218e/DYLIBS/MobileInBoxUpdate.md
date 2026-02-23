## MobileInBoxUpdate

> `/System/Library/PrivateFrameworks/MobileInBoxUpdate.framework/MobileInBoxUpdate`

```diff

-176.100.32.0.0
-  __TEXT.__text: 0x3113c
+176.100.41.0.0
+  __TEXT.__text: 0x3179c
   __TEXT.__auth_stubs: 0xdb0
-  __TEXT.__objc_methlist: 0x1790
+  __TEXT.__objc_methlist: 0x17b0
   __TEXT.__const: 0x5f58
-  __TEXT.__cstring: 0x15c5
+  __TEXT.__cstring: 0x1605
   __TEXT.__oslogstring: 0x2459
   __TEXT.__gcc_except_tab: 0x214
   __TEXT.__swift5_typeref: 0xdc

   __TEXT.__constg_swiftt: 0x64
   __TEXT.__swift5_capture: 0x20
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0xb68
+  __TEXT.__unwind_info: 0xb78
   __TEXT.__eh_frame: 0x80
   __TEXT.__objc_classname: 0x2f0
-  __TEXT.__objc_methname: 0x2dd7
-  __TEXT.__objc_methtype: 0x688
-  __TEXT.__objc_stubs: 0x2a80
+  __TEXT.__objc_methname: 0x2e1b
+  __TEXT.__objc_methtype: 0x698
+  __TEXT.__objc_stubs: 0x2aa0
   __DATA_CONST.__got: 0x2b8
-  __DATA_CONST.__const: 0x3cf8
+  __DATA_CONST.__const: 0x3d00
   __DATA_CONST.__objc_classlist: 0xc8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xe48
+  __DATA_CONST.__objc_selrefs: 0xe60
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x80
-  __DATA_CONST.__objc_arraydata: 0x260
+  __DATA_CONST.__objc_arraydata: 0x268
   __AUTH_CONST.__auth_got: 0x6e8
-  __AUTH_CONST.__const: 0x2668
-  __AUTH_CONST.__cfstring: 0x1a80
+  __AUTH_CONST.__const: 0x26c8
+  __AUTH_CONST.__cfstring: 0x1ae0
   __AUTH_CONST.__objc_const: 0x2818
-  __AUTH_CONST.__objc_intobj: 0x11b8
-  __AUTH_CONST.__objc_arrayobj: 0x330
+  __AUTH_CONST.__objc_intobj: 0x11e8
+  __AUTH_CONST.__objc_arrayobj: 0x348
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH.__objc_data: 0x7f0

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 83D2050F-FDC3-3235-A791-3B15C27B947C
-  Functions: 1284
-  Symbols:   4910
-  CStrings:  1393
+  UUID: 7B373714-7B1B-33A8-96CB-5368982A6CE3
+  Functions: 1296
+  Symbols:   4949
+  CStrings:  1403
 
Symbols:
+ -[MIBUDeviceNFC _startDiagWithEntitlement:error:]
+ -[MIBUDeviceNFC _startDiagWithEntitlement:error:].cold.1
+ -[MIBUDeviceNFC _startDiagWithEntitlement:error:].cold.2
+ -[MIBUDeviceNFC _startDiagWithEntitlement:error:].cold.3
+ -[MIBUDeviceNFC _startDiagWithEntitlement:error:].cold.4
+ -[MIBUDeviceNFC _startDiagWithEntitlement:error:].cold.5
+ -[MIBUDeviceNFC _startDiagWithEntitlement:error:].cold.6
+ -[MIBUDeviceNFC startDiagnostics:]
+ -[MIBUDeviceNFC updateDeviceStatus:]
+ -[MIBUDeviceNFC updateDeviceStatus:].cold.1
+ -[MIBUNFCCommand _serializeSSUpdate].cold.31
+ ___26-[MIBUDeviceNFC shutdown:]_block_invoke.89
+ ___26-[MIBUDeviceNFC shutdown:]_block_invoke.89.cold.1
+ ___26-[MIBUDeviceNFC shutdown:]_block_invoke.92
+ ___26-[MIBUDeviceNFC shutdown:]_block_invoke.92.cold.1
+ ___27-[MIBUDeviceNFC endSession]_block_invoke.103
+ ___27-[MIBUDeviceNFC endSession]_block_invoke.103.cold.1
+ ___32-[MIBUNFCCommand _initWithAPDU:]_block_invoke.143
+ ___32-[MIBUNFCCommand _initWithAPDU:]_block_invoke.143.cold.1
+ ___36-[MIBUDeviceNFC configureNFC:error:]_block_invoke.75
+ ___36-[MIBUDeviceNFC configureNFC:error:]_block_invoke.75.cold.1
+ ___36-[MIBUDeviceNFC updateDeviceStatus:]_block_invoke
+ ___36-[MIBUDeviceNFC updateDeviceStatus:]_block_invoke.cold.1
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.248
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.248.cold.1
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.256
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.256.cold.1
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.264
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.264.cold.1
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.272
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.272.cold.1
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.280
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.280.cold.1
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.288
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.288.cold.1
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.296
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.296.cold.1
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.304
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.304.cold.1
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.312
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.312.cold.1
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.320
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.320.cold.1
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.328
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.328.cold.1
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.336
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.336.cold.1
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.344
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.344.cold.1
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.352
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.352.cold.1
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.360
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.360.cold.1
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.368
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.368.cold.1
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.376
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.376.cold.1
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.384
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.384.cold.1
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.392
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.392.cold.1
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.400
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.400.cold.1
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.408
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.408.cold.1
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.416
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.416.cold.1
+ ___37-[MIBUNFCCommand _serializeChallenge]_block_invoke.217
+ ___37-[MIBUNFCCommand _serializeChallenge]_block_invoke.217.cold.1
+ ___37-[MIBUNFCCommand _serializeHeartbeat]_block_invoke.166
+ ___37-[MIBUNFCCommand _serializeHeartbeat]_block_invoke.166.cold.1
+ ___37-[MIBUNFCCommand _serializeHeartbeat]_block_invoke.174
+ ___37-[MIBUNFCCommand _serializeHeartbeat]_block_invoke.174.cold.1
+ ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.471
+ ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.471.cold.1
+ ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.474
+ ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.474.cold.1
+ ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.477
+ ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.477.cold.1
+ ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.480
+ ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.480.cold.1
+ ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.483
+ ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.483.cold.1
+ ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.486
+ ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.486.cold.1
+ ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.489
+ ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.489.cold.1
+ ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.492
+ ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.492.cold.1
+ ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.495
+ ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.495.cold.1
+ ___38-[MIBUNFCCommand _serializeRetryAfter]_block_invoke.153
+ ___38-[MIBUNFCCommand _serializeRetryAfter]_block_invoke.153.cold.1
+ ___39-[MIBUNFCCommand _deserializeChallenge]_block_invoke.464
+ ___39-[MIBUNFCCommand _deserializeChallenge]_block_invoke.464.cold.1
+ ___39-[MIBUNFCCommand _deserializeHeartbeat]_block_invoke.432
+ ___39-[MIBUNFCCommand _deserializeHeartbeat]_block_invoke.432.cold.1
+ ___39-[MIBUNFCCommand _deserializeHeartbeat]_block_invoke.435
+ ___39-[MIBUNFCCommand _deserializeHeartbeat]_block_invoke.435.cold.1
+ ___39-[MIBUNFCCommand _deserializeHeartbeat]_block_invoke.438
+ ___39-[MIBUNFCCommand _deserializeHeartbeat]_block_invoke.438.cold.1
+ ___39-[MIBUNFCCommand _deserializeHeartbeat]_block_invoke.441
+ ___39-[MIBUNFCCommand _deserializeHeartbeat]_block_invoke.441.cold.1
+ ___39-[MIBUNFCCommand _initWithCommandCode:]_block_invoke.105
+ ___39-[MIBUNFCCommand _initWithCommandCode:]_block_invoke.105.cold.1
+ ___40-[MIBUNFCCommand _deserializeRetryAfter]_block_invoke.424
+ ___40-[MIBUNFCCommand _deserializeRetryAfter]_block_invoke.424.cold.1
+ ___40-[MIBUNFCCommand _deserializeRetryAfter]_block_invoke.427
+ ___40-[MIBUNFCCommand _deserializeRetryAfter]_block_invoke.427.cold.1
+ ___40-[MIBUNFCCommand _serializeConfigureNFC]_block_invoke.184
+ ___40-[MIBUNFCCommand _serializeConfigureNFC]_block_invoke.184.cold.1
+ ___41-[MIBUNFCCommand _serializeTatsuPayload:]_block_invoke.191
+ ___41-[MIBUNFCCommand _serializeTatsuPayload:]_block_invoke.191.cold.1
+ ___41-[MIBUNFCCommand _serializeTatsuPayload:]_block_invoke.199
+ ___41-[MIBUNFCCommand _serializeTatsuPayload:]_block_invoke.199.cold.1
+ ___41-[MIBUNFCCommand _serializeTatsuPayload:]_block_invoke.207
+ ___41-[MIBUNFCCommand _serializeTatsuPayload:]_block_invoke.207.cold.1
+ ___42-[MIBUNFCCommand _deserializeConfigureNFC]_block_invoke.446
+ ___42-[MIBUNFCCommand _deserializeConfigureNFC]_block_invoke.446.cold.1
+ ___42-[MIBUNFCCommand _deserializeConfigureNFC]_block_invoke.449
+ ___42-[MIBUNFCCommand _deserializeConfigureNFC]_block_invoke.449.cold.1
+ ___42-[MIBUNFCCommand _deserializeTatsuPayload]_block_invoke.456
+ ___42-[MIBUNFCCommand _deserializeTatsuPayload]_block_invoke.456.cold.1
+ ___42-[MIBUNFCCommand _deserializeTatsuPayload]_block_invoke.459
+ ___42-[MIBUNFCCommand _deserializeTatsuPayload]_block_invoke.459.cold.1
+ ___49-[MIBUDeviceNFC _startDiagWithEntitlement:error:]_block_invoke
+ ___49-[MIBUDeviceNFC _startDiagWithEntitlement:error:]_block_invoke.49
+ ___49-[MIBUDeviceNFC _startDiagWithEntitlement:error:]_block_invoke.49.cold.1
+ ___49-[MIBUDeviceNFC _startDiagWithEntitlement:error:]_block_invoke.56
+ ___49-[MIBUDeviceNFC _startDiagWithEntitlement:error:]_block_invoke.56.cold.1
+ ___49-[MIBUDeviceNFC _startDiagWithEntitlement:error:]_block_invoke.59
+ ___49-[MIBUDeviceNFC _startDiagWithEntitlement:error:]_block_invoke.59.cold.1
+ ___49-[MIBUDeviceNFC _startDiagWithEntitlement:error:]_block_invoke.cold.1
+ ___block_literal_global.105
+ ___block_literal_global.107
+ ___block_literal_global.145
+ ___block_literal_global.150
+ ___block_literal_global.157
+ ___block_literal_global.168
+ ___block_literal_global.176
+ ___block_literal_global.178
+ ___block_literal_global.186
+ ___block_literal_global.188
+ ___block_literal_global.193
+ ___block_literal_global.201
+ ___block_literal_global.209
+ ___block_literal_global.211
+ ___block_literal_global.219
+ ___block_literal_global.221
+ ___block_literal_global.250
+ ___block_literal_global.258
+ ___block_literal_global.266
+ ___block_literal_global.274
+ ___block_literal_global.282
+ ___block_literal_global.290
+ ___block_literal_global.298
+ ___block_literal_global.306
+ ___block_literal_global.314
+ ___block_literal_global.322
+ ___block_literal_global.330
+ ___block_literal_global.338
+ ___block_literal_global.346
+ ___block_literal_global.354
+ ___block_literal_global.362
+ ___block_literal_global.370
+ ___block_literal_global.378
+ ___block_literal_global.386
+ ___block_literal_global.394
+ ___block_literal_global.402
+ ___block_literal_global.410
+ ___block_literal_global.431
+ ___block_literal_global.443
+ ___block_literal_global.445
+ ___block_literal_global.448
+ ___block_literal_global.451
+ ___block_literal_global.453
+ ___block_literal_global.458
+ ___block_literal_global.461
+ ___block_literal_global.463
+ ___block_literal_global.466
+ ___block_literal_global.470
+ ___block_literal_global.473
+ ___block_literal_global.476
+ ___block_literal_global.479
+ ___block_literal_global.482
+ ___block_literal_global.485
+ ___block_literal_global.488
+ ___block_literal_global.491
+ ___block_literal_global.494
+ ___block_literal_global.497
+ ___block_literal_global.51
+ ___block_literal_global.77
+ ___block_literal_global.85
+ _kMIBUNFCCommandMulticastKeysBlobKey
+ _objc_msgSend$_startDiagWithEntitlement:error:
- -[MIBUDeviceNFC startDiag:].cold.1
- -[MIBUDeviceNFC startDiag:].cold.2
- -[MIBUDeviceNFC startDiag:].cold.3
- -[MIBUDeviceNFC startDiag:].cold.4
- ___26-[MIBUDeviceNFC shutdown:]_block_invoke.78
- ___26-[MIBUDeviceNFC shutdown:]_block_invoke.78.cold.1
- ___26-[MIBUDeviceNFC shutdown:]_block_invoke.81
- ___26-[MIBUDeviceNFC shutdown:]_block_invoke.81.cold.1
- ___27-[MIBUDeviceNFC endSession]_block_invoke.92
- ___27-[MIBUDeviceNFC endSession]_block_invoke.92.cold.1
- ___27-[MIBUDeviceNFC startDiag:]_block_invoke
- ___27-[MIBUDeviceNFC startDiag:]_block_invoke.50
- ___27-[MIBUDeviceNFC startDiag:]_block_invoke.50.cold.1
- ___27-[MIBUDeviceNFC startDiag:]_block_invoke.53
- ___27-[MIBUDeviceNFC startDiag:]_block_invoke.53.cold.1
- ___27-[MIBUDeviceNFC startDiag:]_block_invoke.cold.1
- ___32-[MIBUNFCCommand _initWithAPDU:]_block_invoke.107
- ___32-[MIBUNFCCommand _initWithAPDU:]_block_invoke.107.cold.1
- ___36-[MIBUDeviceNFC configureNFC:error:]_block_invoke.64
- ___36-[MIBUDeviceNFC configureNFC:error:]_block_invoke.64.cold.1
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.221
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.221.cold.1
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.253
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.253.cold.1
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.261
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.261.cold.1
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.269
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.269.cold.1
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.277
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.277.cold.1
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.285
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.285.cold.1
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.293
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.293.cold.1
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.301
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.301.cold.1
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.309
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.309.cold.1
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.317
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.317.cold.1
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.325
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.325.cold.1
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.333
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.333.cold.1
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.341
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.341.cold.1
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.349
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.349.cold.1
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.357
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.357.cold.1
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.365
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.365.cold.1
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.373
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.373.cold.1
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.381
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.381.cold.1
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.389
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.389.cold.1
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.397
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.397.cold.1
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.405
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.405.cold.1
- ___37-[MIBUNFCCommand _serializeChallenge]_block_invoke.214
- ___37-[MIBUNFCCommand _serializeChallenge]_block_invoke.214.cold.1
- ___37-[MIBUNFCCommand _serializeHeartbeat]_block_invoke.163
- ___37-[MIBUNFCCommand _serializeHeartbeat]_block_invoke.163.cold.1
- ___37-[MIBUNFCCommand _serializeHeartbeat]_block_invoke.171
- ___37-[MIBUNFCCommand _serializeHeartbeat]_block_invoke.171.cold.1
- ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.460
- ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.460.cold.1
- ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.463
- ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.463.cold.1
- ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.466
- ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.466.cold.1
- ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.469
- ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.469.cold.1
- ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.472
- ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.472.cold.1
- ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.475
- ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.475.cold.1
- ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.478
- ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.478.cold.1
- ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.481
- ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.481.cold.1
- ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.484
- ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.484.cold.1
- ___38-[MIBUNFCCommand _serializeRetryAfter]_block_invoke.150
- ___38-[MIBUNFCCommand _serializeRetryAfter]_block_invoke.150.cold.1
- ___39-[MIBUNFCCommand _deserializeChallenge]_block_invoke.453
- ___39-[MIBUNFCCommand _deserializeChallenge]_block_invoke.453.cold.1
- ___39-[MIBUNFCCommand _deserializeHeartbeat]_block_invoke.421
- ___39-[MIBUNFCCommand _deserializeHeartbeat]_block_invoke.421.cold.1
- ___39-[MIBUNFCCommand _deserializeHeartbeat]_block_invoke.424
- ___39-[MIBUNFCCommand _deserializeHeartbeat]_block_invoke.424.cold.1
- ___39-[MIBUNFCCommand _deserializeHeartbeat]_block_invoke.427
- ___39-[MIBUNFCCommand _deserializeHeartbeat]_block_invoke.427.cold.1
- ___39-[MIBUNFCCommand _deserializeHeartbeat]_block_invoke.430
- ___39-[MIBUNFCCommand _deserializeHeartbeat]_block_invoke.430.cold.1
- ___39-[MIBUNFCCommand _initWithCommandCode:]_block_invoke.102
- ___39-[MIBUNFCCommand _initWithCommandCode:]_block_invoke.102.cold.1
- ___40-[MIBUNFCCommand _deserializeRetryAfter]_block_invoke.413
- ___40-[MIBUNFCCommand _deserializeRetryAfter]_block_invoke.413.cold.1
- ___40-[MIBUNFCCommand _deserializeRetryAfter]_block_invoke.416
- ___40-[MIBUNFCCommand _deserializeRetryAfter]_block_invoke.416.cold.1
- ___40-[MIBUNFCCommand _serializeConfigureNFC]_block_invoke.181
- ___40-[MIBUNFCCommand _serializeConfigureNFC]_block_invoke.181.cold.1
- ___41-[MIBUNFCCommand _serializeTatsuPayload:]_block_invoke.188
- ___41-[MIBUNFCCommand _serializeTatsuPayload:]_block_invoke.188.cold.1
- ___41-[MIBUNFCCommand _serializeTatsuPayload:]_block_invoke.196
- ___41-[MIBUNFCCommand _serializeTatsuPayload:]_block_invoke.196.cold.1
- ___41-[MIBUNFCCommand _serializeTatsuPayload:]_block_invoke.204
- ___41-[MIBUNFCCommand _serializeTatsuPayload:]_block_invoke.204.cold.1
- ___42-[MIBUNFCCommand _deserializeConfigureNFC]_block_invoke.435
- ___42-[MIBUNFCCommand _deserializeConfigureNFC]_block_invoke.435.cold.1
- ___42-[MIBUNFCCommand _deserializeConfigureNFC]_block_invoke.438
- ___42-[MIBUNFCCommand _deserializeConfigureNFC]_block_invoke.438.cold.1
- ___42-[MIBUNFCCommand _deserializeTatsuPayload]_block_invoke.445
- ___42-[MIBUNFCCommand _deserializeTatsuPayload]_block_invoke.445.cold.1
- ___42-[MIBUNFCCommand _deserializeTatsuPayload]_block_invoke.448
- ___42-[MIBUNFCCommand _deserializeTatsuPayload]_block_invoke.448.cold.1
- ___block_literal_global.104
- ___block_literal_global.144
- ___block_literal_global.152
- ___block_literal_global.154
- ___block_literal_global.173
- ___block_literal_global.183
- ___block_literal_global.185
- ___block_literal_global.187
- ___block_literal_global.198
- ___block_literal_global.206
- ___block_literal_global.208
- ___block_literal_global.216
- ___block_literal_global.218
- ___block_literal_global.220
- ___block_literal_global.255
- ___block_literal_global.263
- ___block_literal_global.271
- ___block_literal_global.279
- ___block_literal_global.287
- ___block_literal_global.295
- ___block_literal_global.303
- ___block_literal_global.311
- ___block_literal_global.319
- ___block_literal_global.327
- ___block_literal_global.335
- ___block_literal_global.343
- ___block_literal_global.351
- ___block_literal_global.359
- ___block_literal_global.367
- ___block_literal_global.375
- ___block_literal_global.383
- ___block_literal_global.391
- ___block_literal_global.399
- ___block_literal_global.407
- ___block_literal_global.409
- ___block_literal_global.412
- ___block_literal_global.415
- ___block_literal_global.432
- ___block_literal_global.442
- ___block_literal_global.444
- ___block_literal_global.447
- ___block_literal_global.450
- ___block_literal_global.452
- ___block_literal_global.457
- ___block_literal_global.459
- ___block_literal_global.462
- ___block_literal_global.465
- ___block_literal_global.471
- ___block_literal_global.474
- ___block_literal_global.477
- ___block_literal_global.480
- ___block_literal_global.483
- ___block_literal_global.486
- ___block_literal_global.74
- ___block_literal_global.80
CStrings:
+ "B32@0:8Q16^@24"
+ "Failed to get tatsu ticket: %@"
+ "MulticastKeysBlob"
+ "Updating device status..."
+ "_startDiagWithEntitlement:error:"
+ "startDiagnostics:"
+ "updateDeviceStatus:"

```
