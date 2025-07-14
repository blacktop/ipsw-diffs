## MobileInBoxUpdate

> `/System/Library/PrivateFrameworks/MobileInBoxUpdate.framework/MobileInBoxUpdate`

```diff

-63.140.19.0.0
-  __TEXT.__text: 0x2a04c
-  __TEXT.__auth_stubs: 0x9c0
-  __TEXT.__objc_methlist: 0x1438
+63.140.21.0.0
+  __TEXT.__text: 0x2a37c
+  __TEXT.__auth_stubs: 0x9d0
+  __TEXT.__objc_methlist: 0x1450
   __TEXT.__const: 0x1c31
-  __TEXT.__cstring: 0x126a
+  __TEXT.__cstring: 0x128a
   __TEXT.__oslogstring: 0x1d16
   __TEXT.__gcc_except_tab: 0x1b8
   __TEXT.__swift5_typeref: 0x98

   __TEXT.__unwind_info: 0x838
   __TEXT.__eh_frame: 0x80
   __TEXT.__objc_classname: 0x20d
-  __TEXT.__objc_methname: 0x28fd
+  __TEXT.__objc_methname: 0x291b
   __TEXT.__objc_methtype: 0x59b
-  __TEXT.__objc_stubs: 0x26c0
+  __TEXT.__objc_stubs: 0x2700
   __DATA_CONST.__got: 0x278
-  __DATA_CONST.__const: 0x1d50
+  __DATA_CONST.__const: 0x1d58
   __DATA_CONST.__objc_classlist: 0xb8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xcd8
+  __DATA_CONST.__objc_selrefs: 0xce8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x80
-  __DATA_CONST.__objc_arraydata: 0x1f0
-  __AUTH_CONST.__auth_got: 0x4f0
-  __AUTH_CONST.__const: 0x21e0
-  __AUTH_CONST.__cfstring: 0x16a0
+  __DATA_CONST.__objc_arraydata: 0x1f8
+  __AUTH_CONST.__auth_got: 0x4f8
+  __AUTH_CONST.__const: 0x2200
+  __AUTH_CONST.__cfstring: 0x16e0
   __AUTH_CONST.__objc_const: 0x2418
-  __AUTH_CONST.__objc_intobj: 0x1068
-  __AUTH_CONST.__objc_arrayobj: 0x300
+  __AUTH_CONST.__objc_intobj: 0x1098
+  __AUTH_CONST.__objc_arrayobj: 0x318
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH.__objc_data: 0x790
   __AUTH.__data: 0x28

   - /System/Library/PrivateFrameworks/MobileActivation.framework/MobileActivation
   - /System/Library/PrivateFrameworks/NearField.framework/NearField
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
+  - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libamsupport.dylib
   - /usr/lib/libauthinstall.dylib

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: DD93AD95-DA58-327D-B586-7BDD0B666CD8
-  Functions: 1087
-  Symbols:   4063
-  CStrings:  1231
+  UUID: 9BDB88ED-0672-34E1-BF16-30DBC7926D80
+  Functions: 1091
+  Symbols:   4078
+  CStrings:  1237
 
Symbols:
+ -[MIBUClient _isIPad]
+ -[MIBUClient isInPalletUpdateMode:]
+ -[MIBUNFCCommand _serializeSSUpdate].cold.28
+ GCC_except_table24
+ GCC_except_table35
+ GCC_except_table41
+ GCC_except_table56
+ _MGGetSInt32Answer
+ ___32-[MIBUNFCCommand _initWithAPDU:]_block_invoke.137
+ ___32-[MIBUNFCCommand _initWithAPDU:]_block_invoke.137.cold.1
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.239
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.239.cold.1
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.247
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.247.cold.1
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.255
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.255.cold.1
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.263
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.263.cold.1
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.271
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.271.cold.1
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.279
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.279.cold.1
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.287
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.287.cold.1
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.295
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.295.cold.1
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.303
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.303.cold.1
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.311
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.311.cold.1
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.319
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.319.cold.1
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.327
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.327.cold.1
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.335
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.335.cold.1
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.343
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.343.cold.1
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.351
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.351.cold.1
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.359
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.359.cold.1
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.367
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.367.cold.1
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.375
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.375.cold.1
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.383
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.383.cold.1
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.391
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.391.cold.1
+ ___37-[MIBUNFCCommand _serializeChallenge]_block_invoke.211
+ ___37-[MIBUNFCCommand _serializeChallenge]_block_invoke.211.cold.1
+ ___37-[MIBUNFCCommand _serializeHeartbeat]_block_invoke.160
+ ___37-[MIBUNFCCommand _serializeHeartbeat]_block_invoke.160.cold.1
+ ___37-[MIBUNFCCommand _serializeHeartbeat]_block_invoke.168
+ ___37-[MIBUNFCCommand _serializeHeartbeat]_block_invoke.168.cold.1
+ ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.446
+ ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.446.cold.1
+ ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.449
+ ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.449.cold.1
+ ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.452
+ ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.452.cold.1
+ ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.455
+ ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.455.cold.1
+ ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.458
+ ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.458.cold.1
+ ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.461
+ ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.461.cold.1
+ ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.464
+ ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.464.cold.1
+ ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.467
+ ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.467.cold.1
+ ___38-[MIBUNFCCommand _serializeRetryAfter]_block_invoke.147
+ ___38-[MIBUNFCCommand _serializeRetryAfter]_block_invoke.147.cold.1
+ ___39-[MIBUNFCCommand _deserializeChallenge]_block_invoke.439
+ ___39-[MIBUNFCCommand _deserializeChallenge]_block_invoke.439.cold.1
+ ___39-[MIBUNFCCommand _deserializeHeartbeat]_block_invoke.407
+ ___39-[MIBUNFCCommand _deserializeHeartbeat]_block_invoke.407.cold.1
+ ___39-[MIBUNFCCommand _deserializeHeartbeat]_block_invoke.410
+ ___39-[MIBUNFCCommand _deserializeHeartbeat]_block_invoke.410.cold.1
+ ___39-[MIBUNFCCommand _deserializeHeartbeat]_block_invoke.413
+ ___39-[MIBUNFCCommand _deserializeHeartbeat]_block_invoke.413.cold.1
+ ___39-[MIBUNFCCommand _deserializeHeartbeat]_block_invoke.416
+ ___39-[MIBUNFCCommand _deserializeHeartbeat]_block_invoke.416.cold.1
+ ___39-[MIBUNFCCommand _initWithCommandCode:]_block_invoke.99
+ ___39-[MIBUNFCCommand _initWithCommandCode:]_block_invoke.99.cold.1
+ ___40-[MIBUNFCCommand _deserializeRetryAfter]_block_invoke.399
+ ___40-[MIBUNFCCommand _deserializeRetryAfter]_block_invoke.399.cold.1
+ ___40-[MIBUNFCCommand _deserializeRetryAfter]_block_invoke.402
+ ___40-[MIBUNFCCommand _deserializeRetryAfter]_block_invoke.402.cold.1
+ ___40-[MIBUNFCCommand _serializeConfigureNFC]_block_invoke.178
+ ___40-[MIBUNFCCommand _serializeConfigureNFC]_block_invoke.178.cold.1
+ ___41-[MIBUNFCCommand _serializeTatsuPayload:]_block_invoke.185
+ ___41-[MIBUNFCCommand _serializeTatsuPayload:]_block_invoke.185.cold.1
+ ___41-[MIBUNFCCommand _serializeTatsuPayload:]_block_invoke.193
+ ___41-[MIBUNFCCommand _serializeTatsuPayload:]_block_invoke.193.cold.1
+ ___41-[MIBUNFCCommand _serializeTatsuPayload:]_block_invoke.201
+ ___41-[MIBUNFCCommand _serializeTatsuPayload:]_block_invoke.201.cold.1
+ ___42-[MIBUNFCCommand _deserializeConfigureNFC]_block_invoke.421
+ ___42-[MIBUNFCCommand _deserializeConfigureNFC]_block_invoke.421.cold.1
+ ___42-[MIBUNFCCommand _deserializeConfigureNFC]_block_invoke.424
+ ___42-[MIBUNFCCommand _deserializeConfigureNFC]_block_invoke.424.cold.1
+ ___42-[MIBUNFCCommand _deserializeTatsuPayload]_block_invoke.431
+ ___42-[MIBUNFCCommand _deserializeTatsuPayload]_block_invoke.431.cold.1
+ ___42-[MIBUNFCCommand _deserializeTatsuPayload]_block_invoke.434
+ ___42-[MIBUNFCCommand _deserializeTatsuPayload]_block_invoke.434.cold.1
+ ___block_literal_global.101
+ ___block_literal_global.139
+ ___block_literal_global.149
+ ___block_literal_global.151
+ ___block_literal_global.162
+ ___block_literal_global.170
+ ___block_literal_global.172
+ ___block_literal_global.180
+ ___block_literal_global.182
+ ___block_literal_global.187
+ ___block_literal_global.195
+ ___block_literal_global.203
+ ___block_literal_global.205
+ ___block_literal_global.213
+ ___block_literal_global.215
+ ___block_literal_global.241
+ ___block_literal_global.249
+ ___block_literal_global.257
+ ___block_literal_global.265
+ ___block_literal_global.273
+ ___block_literal_global.281
+ ___block_literal_global.289
+ ___block_literal_global.297
+ ___block_literal_global.305
+ ___block_literal_global.313
+ ___block_literal_global.321
+ ___block_literal_global.329
+ ___block_literal_global.337
+ ___block_literal_global.345
+ ___block_literal_global.353
+ ___block_literal_global.361
+ ___block_literal_global.369
+ ___block_literal_global.377
+ ___block_literal_global.385
+ ___block_literal_global.406
+ ___block_literal_global.418
+ ___block_literal_global.420
+ ___block_literal_global.423
+ ___block_literal_global.426
+ ___block_literal_global.428
+ ___block_literal_global.433
+ ___block_literal_global.436
+ ___block_literal_global.438
+ ___block_literal_global.441
+ ___block_literal_global.445
+ ___block_literal_global.448
+ ___block_literal_global.451
+ ___block_literal_global.454
+ ___block_literal_global.457
+ ___block_literal_global.460
+ ___block_literal_global.463
+ ___block_literal_global.466
+ ___block_literal_global.469
+ _kMIBUNFCCommandOperationTimeoutKey
+ _objc_msgSend$_isIPad
+ _objc_msgSend$isInBoxUpdateMode:
- GCC_except_table23
- GCC_except_table34
- GCC_except_table40
- GCC_except_table55
- ___32-[MIBUNFCCommand _initWithAPDU:]_block_invoke.101
- ___32-[MIBUNFCCommand _initWithAPDU:]_block_invoke.101.cold.1
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.215
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.215.cold.1
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.244
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.244.cold.1
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.252
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.252.cold.1
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.260
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.260.cold.1
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.268
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.268.cold.1
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.276
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.276.cold.1
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.284
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.284.cold.1
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.292
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.292.cold.1
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.300
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.300.cold.1
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.308
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.308.cold.1
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.316
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.316.cold.1
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.324
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.324.cold.1
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.332
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.332.cold.1
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.340
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.340.cold.1
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.348
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.348.cold.1
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.356
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.356.cold.1
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.364
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.364.cold.1
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.372
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.372.cold.1
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.380
- ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.380.cold.1
- ___37-[MIBUNFCCommand _serializeChallenge]_block_invoke.208
- ___37-[MIBUNFCCommand _serializeChallenge]_block_invoke.208.cold.1
- ___37-[MIBUNFCCommand _serializeHeartbeat]_block_invoke.157
- ___37-[MIBUNFCCommand _serializeHeartbeat]_block_invoke.157.cold.1
- ___37-[MIBUNFCCommand _serializeHeartbeat]_block_invoke.165
- ___37-[MIBUNFCCommand _serializeHeartbeat]_block_invoke.165.cold.1
- ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.435
- ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.435.cold.1
- ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.438
- ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.438.cold.1
- ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.441
- ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.441.cold.1
- ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.444
- ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.444.cold.1
- ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.447
- ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.447.cold.1
- ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.450
- ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.450.cold.1
- ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.453
- ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.453.cold.1
- ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.456
- ___38-[MIBUNFCCommand _deserializeSSUpdate]_block_invoke.456.cold.1
- ___38-[MIBUNFCCommand _serializeRetryAfter]_block_invoke.144
- ___38-[MIBUNFCCommand _serializeRetryAfter]_block_invoke.144.cold.1
- ___39-[MIBUNFCCommand _deserializeChallenge]_block_invoke.428
- ___39-[MIBUNFCCommand _deserializeChallenge]_block_invoke.428.cold.1
- ___39-[MIBUNFCCommand _deserializeHeartbeat]_block_invoke.396
- ___39-[MIBUNFCCommand _deserializeHeartbeat]_block_invoke.396.cold.1
- ___39-[MIBUNFCCommand _deserializeHeartbeat]_block_invoke.399
- ___39-[MIBUNFCCommand _deserializeHeartbeat]_block_invoke.399.cold.1
- ___39-[MIBUNFCCommand _deserializeHeartbeat]_block_invoke.402
- ___39-[MIBUNFCCommand _deserializeHeartbeat]_block_invoke.402.cold.1
- ___39-[MIBUNFCCommand _deserializeHeartbeat]_block_invoke.405
- ___39-[MIBUNFCCommand _deserializeHeartbeat]_block_invoke.405.cold.1
- ___39-[MIBUNFCCommand _initWithCommandCode:]_block_invoke.96
- ___39-[MIBUNFCCommand _initWithCommandCode:]_block_invoke.96.cold.1
- ___40-[MIBUNFCCommand _deserializeRetryAfter]_block_invoke.388
- ___40-[MIBUNFCCommand _deserializeRetryAfter]_block_invoke.388.cold.1
- ___40-[MIBUNFCCommand _deserializeRetryAfter]_block_invoke.391
- ___40-[MIBUNFCCommand _deserializeRetryAfter]_block_invoke.391.cold.1
- ___40-[MIBUNFCCommand _serializeConfigureNFC]_block_invoke.175
- ___40-[MIBUNFCCommand _serializeConfigureNFC]_block_invoke.175.cold.1
- ___41-[MIBUNFCCommand _serializeTatsuPayload:]_block_invoke.182
- ___41-[MIBUNFCCommand _serializeTatsuPayload:]_block_invoke.182.cold.1
- ___41-[MIBUNFCCommand _serializeTatsuPayload:]_block_invoke.190
- ___41-[MIBUNFCCommand _serializeTatsuPayload:]_block_invoke.190.cold.1
- ___41-[MIBUNFCCommand _serializeTatsuPayload:]_block_invoke.198
- ___41-[MIBUNFCCommand _serializeTatsuPayload:]_block_invoke.198.cold.1
- ___42-[MIBUNFCCommand _deserializeConfigureNFC]_block_invoke.410
- ___42-[MIBUNFCCommand _deserializeConfigureNFC]_block_invoke.410.cold.1
- ___42-[MIBUNFCCommand _deserializeConfigureNFC]_block_invoke.413
- ___42-[MIBUNFCCommand _deserializeConfigureNFC]_block_invoke.413.cold.1
- ___42-[MIBUNFCCommand _deserializeTatsuPayload]_block_invoke.420
- ___42-[MIBUNFCCommand _deserializeTatsuPayload]_block_invoke.420.cold.1
- ___42-[MIBUNFCCommand _deserializeTatsuPayload]_block_invoke.423
- ___42-[MIBUNFCCommand _deserializeTatsuPayload]_block_invoke.423.cold.1
- ___block_literal_global.146
- ___block_literal_global.148
- ___block_literal_global.159
- ___block_literal_global.165
- ___block_literal_global.169
- ___block_literal_global.179
- ___block_literal_global.181
- ___block_literal_global.192
- ___block_literal_global.200
- ___block_literal_global.202
- ___block_literal_global.210
- ___block_literal_global.212
- ___block_literal_global.214
- ___block_literal_global.246
- ___block_literal_global.254
- ___block_literal_global.262
- ___block_literal_global.270
- ___block_literal_global.278
- ___block_literal_global.286
- ___block_literal_global.294
- ___block_literal_global.302
- ___block_literal_global.310
- ___block_literal_global.318
- ___block_literal_global.326
- ___block_literal_global.334
- ___block_literal_global.342
- ___block_literal_global.350
- ___block_literal_global.358
- ___block_literal_global.366
- ___block_literal_global.374
- ___block_literal_global.382
- ___block_literal_global.384
- ___block_literal_global.387
- ___block_literal_global.390
- ___block_literal_global.407
- ___block_literal_global.417
- ___block_literal_global.419
- ___block_literal_global.422
- ___block_literal_global.425
- ___block_literal_global.427
- ___block_literal_global.432
- ___block_literal_global.434
- ___block_literal_global.437
- ___block_literal_global.440
- ___block_literal_global.446
- ___block_literal_global.449
- ___block_literal_global.452
- ___block_literal_global.455
- ___block_literal_global.458
- ___block_literal_global.98
Functions:
~ ___39+[MIBUSerializationUtil tagTypeMapping]_block_invoke : 1292 -> 1308
~ -[MIBUNFCCommand _serializeSSUpdate] : 2756 -> 2948
+ ___36-[MIBUNFCCommand _serializeSSUpdate]_block_invoke.391
~ -[MIBUNFCCommand _deserializeSSUpdate] : 2492 -> 2616
+ -[MIBUClient isInPalletUpdateMode:]
+ -[MIBUClient _isIPad]
~ -[MIBUNFCCommand _serializeSSUpdate].cold.20 : 204 -> 220
+ -[MIBUNFCCommand _serializeSSUpdate].cold.28
CStrings:
+ "DeviceClassNumber"
+ "OperationTimeout"
+ "_isIPad"
+ "isInPalletUpdateMode:"

```
