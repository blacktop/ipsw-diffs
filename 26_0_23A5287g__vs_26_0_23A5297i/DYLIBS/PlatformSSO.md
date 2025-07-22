## PlatformSSO

> `/System/Library/PrivateFrameworks/PlatformSSO.framework/PlatformSSO`

```diff

-483.0.24.0.0
-  __TEXT.__text: 0x58d1c
+483.0.28.0.0
+  __TEXT.__text: 0x592d4
   __TEXT.__auth_stubs: 0xe70
-  __TEXT.__objc_methlist: 0x32ac
+  __TEXT.__objc_methlist: 0x32d4
   __TEXT.__const: 0x27a
-  __TEXT.__cstring: 0x8016
+  __TEXT.__cstring: 0x80b6
   __TEXT.__oslogstring: 0x2321
-  __TEXT.__gcc_except_tab: 0x1514
+  __TEXT.__gcc_except_tab: 0x1528
   __TEXT.__dlopen_cstrs: 0x110
   __TEXT.__swift5_typeref: 0xc2
   __TEXT.__swift5_capture: 0x118

   __TEXT.__swift5_types: 0x8
   __TEXT.__swift_as_entry: 0x2c
   __TEXT.__swift_as_ret: 0x50
-  __TEXT.__unwind_info: 0x1520
+  __TEXT.__unwind_info: 0x1530
   __TEXT.__eh_frame: 0x560
   __TEXT.__objc_classname: 0x3d6
-  __TEXT.__objc_methname: 0x9d11
-  __TEXT.__objc_methtype: 0x14fe
-  __TEXT.__objc_stubs: 0x6f00
+  __TEXT.__objc_methname: 0x9d3c
+  __TEXT.__objc_methtype: 0x151a
+  __TEXT.__objc_stubs: 0x6f20
   __DATA_CONST.__got: 0x430
-  __DATA_CONST.__const: 0xe60
+  __DATA_CONST.__const: 0xe88
   __DATA_CONST.__objc_classlist: 0x100
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2200
+  __DATA_CONST.__objc_selrefs: 0x2208
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0xc0
   __DATA_CONST.__objc_arraydata: 0x10
   __AUTH_CONST.__auth_got: 0x748
   __AUTH_CONST.__const: 0xc28
-  __AUTH_CONST.__cfstring: 0x3820
-  __AUTH_CONST.__objc_const: 0x8178
+  __AUTH_CONST.__cfstring: 0x3840
+  __AUTH_CONST.__objc_const: 0x81d0
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_doubleobj: 0x10

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: B3235421-F68D-3FBE-AAF7-C68830AE0F85
-  Functions: 2043
-  Symbols:   7219
-  CStrings:  3142
+  UUID: 0E57FB65-025F-313D-9AC4-CB35F2515D46
+  Functions: 2051
+  Symbols:   7246
+  CStrings:  3150
 
Symbols:
+ -[POExtensionAgentProcess authenticationMethodWithCompletion:]
+ -[POExtensionAgentProcess authenticationMethodWithCompletion:].cold.1
+ -[POLoginManager authenticationMethod]
+ -[POLoginManager authenticationMethod].cold.1
+ -[POServiceLoginManagerConnection authenticationMethodWithCompletion:]
+ GCC_except_table117
+ GCC_except_table125
+ GCC_except_table24
+ GCC_except_table282
+ GCC_except_table291
+ GCC_except_table44
+ GCC_except_table84
+ ___27-[POLoginManager ssoTokens]_block_invoke.21
+ ___27-[POLoginManager ssoTokens]_block_invoke.21.cold.1
+ ___27-[POLoginManager ssoTokens]_block_invoke.26
+ ___27-[POLoginManager ssoTokens]_block_invoke.26.cold.1
+ ___31-[POLoginManager setSsoTokens:]_block_invoke.36
+ ___31-[POLoginManager setSsoTokens:]_block_invoke.36.cold.1
+ ___31-[POLoginManager setSsoTokens:]_block_invoke.46
+ ___31-[POLoginManager setSsoTokens:]_block_invoke.46.cold.1
+ ___31-[POLoginManager setSsoTokens:]_block_invoke.52
+ ___31-[POLoginManager setSsoTokens:]_block_invoke.52.cold.1
+ ___31-[POLoginManager setSsoTokens:]_block_invoke.58
+ ___31-[POLoginManager setSsoTokens:]_block_invoke.58.cold.1
+ ___31-[POLoginManager setSsoTokens:]_block_invoke.68
+ ___31-[POLoginManager setSsoTokens:]_block_invoke.68.cold.1
+ ___31-[POLoginManager setSsoTokens:]_block_invoke.71
+ ___31-[POLoginManager setSsoTokens:]_block_invoke.71.cold.1
+ ___35-[POLoginManager setLoginUserName:]_block_invoke.6
+ ___35-[POLoginManager setLoginUserName:]_block_invoke.6.cold.1
+ ___36-[POLoginManager copyKeyForKeyType:]_block_invoke.88
+ ___36-[POLoginManager copyKeyForKeyType:]_block_invoke.88.cold.1
+ ___38-[POLoginManager authenticationMethod]_block_invoke
+ ___38-[POLoginManager authenticationMethod]_block_invoke_2
+ ___38-[POLoginManager authenticationMethod]_block_invoke_2.cold.1
+ ___38-[POLoginManager rotateKeyForKeyType:]_block_invoke.121
+ ___38-[POLoginManager rotateKeyForKeyType:]_block_invoke.121.cold.1
+ ___41-[POLoginManager copyIdentityForKeyType:]_block_invoke.95
+ ___41-[POLoginManager copyIdentityForKeyType:]_block_invoke.95.cold.1
+ ___42-[POLoginManager saveCertificate:keyType:]_block_invoke.82
+ ___48-[POLoginManager completeRotationKeyForKeyType:]_block_invoke.127
+ ___48-[POLoginManager completeRotationKeyForKeyType:]_block_invoke.127.cold.1
+ ___51-[POExtensionAgentProcess setSsoTokens:completion:]_block_invoke.117
+ ___51-[POExtensionAgentProcess setSsoTokens:completion:]_block_invoke.117.cold.1
+ ___51-[POExtensionAgentProcess setSsoTokens:completion:]_block_invoke.118
+ ___51-[POExtensionAgentProcess setSsoTokens:completion:]_block_invoke.118.cold.1
+ ___51-[POExtensionAgentProcess setSsoTokens:completion:]_block_invoke.122
+ ___51-[POExtensionAgentProcess setSsoTokens:completion:]_block_invoke.122.cold.1
+ ___51-[POExtensionAgentProcess setSsoTokens:completion:]_block_invoke.125
+ ___51-[POExtensionAgentProcess setSsoTokens:completion:]_block_invoke.125.cold.1
+ ___51-[POExtensionAgentProcess setSsoTokens:completion:]_block_invoke.129
+ ___51-[POExtensionAgentProcess setSsoTokens:completion:]_block_invoke.129.cold.1
+ ___51-[POExtensionAgentProcess setSsoTokens:completion:]_block_invoke.133
+ ___51-[POExtensionAgentProcess setSsoTokens:completion:]_block_invoke.133.cold.1
+ ___51-[POExtensionAgentProcess setSsoTokens:completion:]_block_invoke.137
+ ___51-[POExtensionAgentProcess ssoTokensWithCompletion:]_block_invoke.102
+ ___51-[POExtensionAgentProcess ssoTokensWithCompletion:]_block_invoke.102.cold.1
+ ___51-[POExtensionAgentProcess ssoTokensWithCompletion:]_block_invoke.108
+ ___51-[POExtensionAgentProcess ssoTokensWithCompletion:]_block_invoke.108.cold.1
+ ___51-[POExtensionAgentProcess ssoTokensWithCompletion:]_block_invoke.89
+ ___51-[POExtensionAgentProcess ssoTokensWithCompletion:]_block_invoke.89.cold.1
+ ___51-[POExtensionAgentProcess ssoTokensWithCompletion:]_block_invoke.90
+ ___51-[POExtensionAgentProcess ssoTokensWithCompletion:]_block_invoke.90.cold.1
+ ___51-[POExtensionAgentProcess ssoTokensWithCompletion:]_block_invoke.96
+ ___51-[POExtensionAgentProcess ssoTokensWithCompletion:]_block_invoke.96.cold.1
+ ___52-[POServiceLoginManagerConnection _connectToService]_block_invoke.95
+ ___52-[POServiceLoginManagerConnection _connectToService]_block_invoke.95.cold.1
+ ___55-[POExtensionAgentProcess loginUserNameWithCompletion:]_block_invoke.374
+ ___55-[POExtensionAgentProcess loginUserNameWithCompletion:]_block_invoke.374.cold.1
+ ___55-[POExtensionAgentProcess setLoginUserName:completion:]_block_invoke.382
+ ___55-[POExtensionAgentProcess setLoginUserName:completion:]_block_invoke.382.cold.1
+ ___55-[POExtensionAgentProcess setLoginUserName:completion:]_block_invoke.386
+ ___55-[POExtensionAgentProcess setLoginUserName:completion:]_block_invoke.386.cold.1
+ ___57-[POExtensionAgentProcess resetDeviceKeysWithCompletion:]_block_invoke.332
+ ___57-[POExtensionAgentProcess resetDeviceKeysWithCompletion:]_block_invoke.332.cold.1
+ ___57-[POExtensionAgentProcess resetDeviceKeysWithCompletion:]_block_invoke.335
+ ___57-[POExtensionAgentProcess resetDeviceKeysWithCompletion:]_block_invoke.335.cold.1
+ ___57-[POExtensionAgentProcess resetDeviceKeysWithCompletion:]_block_invoke.336
+ ___57-[POExtensionAgentProcess resetDeviceKeysWithCompletion:]_block_invoke.336.cold.1
+ ___58-[POExtensionAgentProcess rotateKeyForKeyType:completion:]_block_invoke.410
+ ___58-[POExtensionAgentProcess rotateKeyForKeyType:completion:]_block_invoke.410.cold.1
+ ___58-[POExtensionAgentProcess rotateKeyForKeyType:completion:]_block_invoke.413
+ ___58-[POExtensionAgentProcess rotateKeyForKeyType:completion:]_block_invoke.413.cold.1
+ ___58-[POExtensionAgentProcess rotateKeyForKeyType:completion:]_block_invoke.414
+ ___58-[POExtensionAgentProcess rotateKeyForKeyType:completion:]_block_invoke.414.cold.1
+ ___58-[POExtensionAgentProcess rotateKeyForKeyType:completion:]_block_invoke.417
+ ___58-[POExtensionAgentProcess rotateKeyForKeyType:completion:]_block_invoke.417.cold.1
+ ___58-[POExtensionAgentProcess rotateKeyForKeyType:completion:]_block_invoke.420
+ ___58-[POExtensionAgentProcess rotateKeyForKeyType:completion:]_block_invoke.420.cold.1
+ ___58-[POExtensionAgentProcess rotateKeyForKeyType:completion:]_block_invoke.426
+ ___58-[POExtensionAgentProcess rotateKeyForKeyType:completion:]_block_invoke.426.cold.1
+ ___60-[POExtensionAgentProcess setLoginConfiguration:completion:]_block_invoke.154
+ ___60-[POExtensionAgentProcess setLoginConfiguration:completion:]_block_invoke.154.cold.1
+ ___60-[POExtensionAgentProcess setLoginConfiguration:completion:]_block_invoke.160
+ ___60-[POExtensionAgentProcess setLoginConfiguration:completion:]_block_invoke.160.cold.1
+ ___60-[POExtensionAgentProcess setLoginConfiguration:completion:]_block_invoke.166
+ ___60-[POExtensionAgentProcess setLoginConfiguration:completion:]_block_invoke.166.cold.1
+ ___60-[POExtensionAgentProcess setLoginConfiguration:completion:]_block_invoke.172
+ ___60-[POExtensionAgentProcess setLoginConfiguration:completion:]_block_invoke.172.cold.1
+ ___60-[POExtensionAgentProcess setLoginConfiguration:completion:]_block_invoke.179
+ ___60-[POExtensionAgentProcess setLoginConfiguration:completion:]_block_invoke.179.cold.1
+ ___60-[POExtensionAgentProcess setLoginConfiguration:completion:]_block_invoke.185
+ ___60-[POExtensionAgentProcess setLoginConfiguration:completion:]_block_invoke.185.cold.1
+ ___60-[POExtensionAgentProcess setLoginConfiguration:completion:]_block_invoke.191
+ ___60-[POExtensionAgentProcess setLoginConfiguration:completion:]_block_invoke.191.cold.1
+ ___60-[POExtensionAgentProcess setLoginConfiguration:completion:]_block_invoke.197
+ ___60-[POExtensionAgentProcess setLoginConfiguration:completion:]_block_invoke.197.cold.1
+ ___60-[POExtensionAgentProcess setLoginConfiguration:completion:]_block_invoke.203
+ ___60-[POExtensionAgentProcess setLoginConfiguration:completion:]_block_invoke.203.cold.1
+ ___60-[POExtensionAgentProcess setLoginConfiguration:completion:]_block_invoke.209
+ ___60-[POExtensionAgentProcess setLoginConfiguration:completion:]_block_invoke.209.cold.1
+ ___60-[POExtensionAgentProcess setLoginConfiguration:completion:]_block_invoke.215
+ ___60-[POExtensionAgentProcess setLoginConfiguration:completion:]_block_invoke.215.cold.1
+ ___60-[POExtensionAgentProcess setLoginConfiguration:completion:]_block_invoke.221
+ ___60-[POExtensionAgentProcess setLoginConfiguration:completion:]_block_invoke.221.cold.1
+ ___60-[POExtensionAgentProcess setLoginConfiguration:completion:]_block_invoke.227
+ ___60-[POExtensionAgentProcess setLoginConfiguration:completion:]_block_invoke.227.cold.1
+ ___60-[POExtensionAgentProcess setLoginConfiguration:completion:]_block_invoke.234
+ ___60-[POExtensionAgentProcess setLoginConfiguration:completion:]_block_invoke.234.cold.1
+ ___60-[POExtensionAgentProcess setLoginConfiguration:completion:]_block_invoke.240
+ ___60-[POExtensionAgentProcess setLoginConfiguration:completion:]_block_invoke.240.cold.1
+ ___60-[POExtensionAgentProcess setLoginConfiguration:completion:]_block_invoke.246
+ ___60-[POExtensionAgentProcess setLoginConfiguration:completion:]_block_invoke.246.cold.1
+ ___60-[POExtensionAgentProcess setLoginConfiguration:completion:]_block_invoke.252
+ ___60-[POExtensionAgentProcess setLoginConfiguration:completion:]_block_invoke.252.cold.1
+ ___60-[POExtensionAgentProcess setLoginConfiguration:completion:]_block_invoke.258
+ ___60-[POExtensionAgentProcess setLoginConfiguration:completion:]_block_invoke.258.cold.1
+ ___60-[POExtensionAgentProcess setLoginConfiguration:completion:]_block_invoke.264
+ ___60-[POExtensionAgentProcess setLoginConfiguration:completion:]_block_invoke.264.cold.1
+ ___62-[POExtensionAgentProcess authenticationMethodWithCompletion:]_block_invoke
+ ___62-[POExtensionAgentProcess authenticationMethodWithCompletion:]_block_invoke.cold.1
+ ___64-[POExtensionAgentProcess setUserLoginConfiguration:completion:]_block_invoke.402
+ ___64-[POExtensionAgentProcess setUserLoginConfiguration:completion:]_block_invoke.402.cold.1
+ ___65-[POExtensionAgentProcess setCertificateData:keyType:completion:]_block_invoke.281
+ ___65-[POExtensionAgentProcess setCertificateData:keyType:completion:]_block_invoke.281.cold.1
+ ___65-[POExtensionAgentProcess setCertificateData:keyType:completion:]_block_invoke.282
+ ___65-[POExtensionAgentProcess setCertificateData:keyType:completion:]_block_invoke.282.cold.1
+ ___65-[POExtensionAgentProcess setCertificateData:keyType:completion:]_block_invoke.288
+ ___65-[POExtensionAgentProcess setCertificateData:keyType:completion:]_block_invoke.288.cold.1
+ ___67-[POExtensionAgentProcess resetUserSecureEnclaveKeyWithCompletion:]_block_invoke.347
+ ___67-[POExtensionAgentProcess resetUserSecureEnclaveKeyWithCompletion:]_block_invoke.347.cold.1
+ ___67-[POExtensionAgentProcess resetUserSecureEnclaveKeyWithCompletion:]_block_invoke.350
+ ___67-[POExtensionAgentProcess resetUserSecureEnclaveKeyWithCompletion:]_block_invoke.350.cold.1
+ ___67-[POExtensionAgentProcess resetUserSecureEnclaveKeyWithCompletion:]_block_invoke.351
+ ___67-[POExtensionAgentProcess resetUserSecureEnclaveKeyWithCompletion:]_block_invoke.351.cold.1
+ ___67-[POExtensionAgentProcess resetUserSecureEnclaveKeyWithCompletion:]_block_invoke.357
+ ___67-[POExtensionAgentProcess resetUserSecureEnclaveKeyWithCompletion:]_block_invoke.357.cold.1
+ ___67-[POExtensionAgentProcess resetUserSecureEnclaveKeyWithCompletion:]_block_invoke.363
+ ___67-[POExtensionAgentProcess resetUserSecureEnclaveKeyWithCompletion:]_block_invoke.363.cold.1
+ ___67-[POExtensionAgentProcess userNeedsReauthenticationWithCompletion:]_block_invoke.313
+ ___68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.437
+ ___68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.437.cold.1
+ ___68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.440
+ ___68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.440.cold.1
+ ___68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.441
+ ___68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.441.cold.1
+ ___68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.444
+ ___68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.444.cold.1
+ ___68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.447
+ ___68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.447.cold.1
+ ___68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.451
+ ___68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.451.cold.1
+ ___68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.454
+ ___68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.454.cold.1
+ ___70-[POExtensionAgentProcess userRegistrationsNeedsRepairWithCompletion:]_block_invoke.326
+ ___70-[POServiceLoginManagerConnection authenticationMethodWithCompletion:]_block_invoke
+ ___70-[POServiceLoginManagerConnection authenticationMethodWithCompletion:]_block_invoke.cold.1
+ ___72-[POExtensionAgentProcess deviceRegistrationsNeedsRepairWithCompletion:]_block_invoke.320
+ ___block_descriptor_40_e8_32r_e20_v20?0i8"NSError"12lr32l8
+ ___block_literal_global.104
+ ___block_literal_global.115
+ ___block_literal_global.117
+ ___block_literal_global.126
+ ___block_literal_global.228
+ ___block_literal_global.31
+ ___block_literal_global.662
+ ___block_literal_global.70
+ _objc_msgSend$authenticationMethodWithCompletion:
- GCC_except_table115
- GCC_except_table123
- GCC_except_table21
- GCC_except_table278
- GCC_except_table287
- GCC_except_table79
- ___27-[POLoginManager ssoTokens]_block_invoke.13
- ___27-[POLoginManager ssoTokens]_block_invoke.13.cold.1
- ___27-[POLoginManager ssoTokens]_block_invoke.22
- ___27-[POLoginManager ssoTokens]_block_invoke.22.cold.1
- ___31-[POLoginManager setSsoTokens:]_block_invoke.28
- ___31-[POLoginManager setSsoTokens:]_block_invoke.28.cold.1
- ___31-[POLoginManager setSsoTokens:]_block_invoke.38
- ___31-[POLoginManager setSsoTokens:]_block_invoke.38.cold.1
- ___31-[POLoginManager setSsoTokens:]_block_invoke.48
- ___31-[POLoginManager setSsoTokens:]_block_invoke.48.cold.1
- ___31-[POLoginManager setSsoTokens:]_block_invoke.54
- ___31-[POLoginManager setSsoTokens:]_block_invoke.54.cold.1
- ___31-[POLoginManager setSsoTokens:]_block_invoke.60
- ___31-[POLoginManager setSsoTokens:]_block_invoke.60.cold.1
- ___31-[POLoginManager setSsoTokens:]_block_invoke.67
- ___31-[POLoginManager setSsoTokens:]_block_invoke.67.cold.1
- ___35-[POLoginManager setLoginUserName:]_block_invoke.2
- ___35-[POLoginManager setLoginUserName:]_block_invoke.2.cold.1
- ___36-[POLoginManager copyKeyForKeyType:]_block_invoke.84
- ___36-[POLoginManager copyKeyForKeyType:]_block_invoke.84.cold.1
- ___38-[POLoginManager rotateKeyForKeyType:]_block_invoke.117
- ___38-[POLoginManager rotateKeyForKeyType:]_block_invoke.117.cold.1
- ___41-[POLoginManager copyIdentityForKeyType:]_block_invoke.91
- ___41-[POLoginManager copyIdentityForKeyType:]_block_invoke.91.cold.1
- ___42-[POLoginManager saveCertificate:keyType:]_block_invoke.78
- ___48-[POLoginManager completeRotationKeyForKeyType:]_block_invoke.123
- ___48-[POLoginManager completeRotationKeyForKeyType:]_block_invoke.123.cold.1
- ___51-[POExtensionAgentProcess setSsoTokens:completion:]_block_invoke.115
- ___51-[POExtensionAgentProcess setSsoTokens:completion:]_block_invoke.115.cold.1
- ___51-[POExtensionAgentProcess setSsoTokens:completion:]_block_invoke.116
- ___51-[POExtensionAgentProcess setSsoTokens:completion:]_block_invoke.116.cold.1
- ___51-[POExtensionAgentProcess setSsoTokens:completion:]_block_invoke.120
- ___51-[POExtensionAgentProcess setSsoTokens:completion:]_block_invoke.120.cold.1
- ___51-[POExtensionAgentProcess setSsoTokens:completion:]_block_invoke.123
- ___51-[POExtensionAgentProcess setSsoTokens:completion:]_block_invoke.123.cold.1
- ___51-[POExtensionAgentProcess setSsoTokens:completion:]_block_invoke.127
- ___51-[POExtensionAgentProcess setSsoTokens:completion:]_block_invoke.127.cold.1
- ___51-[POExtensionAgentProcess setSsoTokens:completion:]_block_invoke.131
- ___51-[POExtensionAgentProcess setSsoTokens:completion:]_block_invoke.131.cold.1
- ___51-[POExtensionAgentProcess setSsoTokens:completion:]_block_invoke.135
- ___51-[POExtensionAgentProcess ssoTokensWithCompletion:]_block_invoke.100
- ___51-[POExtensionAgentProcess ssoTokensWithCompletion:]_block_invoke.100.cold.1
- ___51-[POExtensionAgentProcess ssoTokensWithCompletion:]_block_invoke.106
- ___51-[POExtensionAgentProcess ssoTokensWithCompletion:]_block_invoke.106.cold.1
- ___51-[POExtensionAgentProcess ssoTokensWithCompletion:]_block_invoke.87
- ___51-[POExtensionAgentProcess ssoTokensWithCompletion:]_block_invoke.87.cold.1
- ___51-[POExtensionAgentProcess ssoTokensWithCompletion:]_block_invoke.88
- ___51-[POExtensionAgentProcess ssoTokensWithCompletion:]_block_invoke.88.cold.1
- ___51-[POExtensionAgentProcess ssoTokensWithCompletion:]_block_invoke.94
- ___51-[POExtensionAgentProcess ssoTokensWithCompletion:]_block_invoke.94.cold.1
- ___52-[POServiceLoginManagerConnection _connectToService]_block_invoke.93
- ___52-[POServiceLoginManagerConnection _connectToService]_block_invoke.93.cold.1
- ___55-[POExtensionAgentProcess loginUserNameWithCompletion:]_block_invoke.372
- ___55-[POExtensionAgentProcess loginUserNameWithCompletion:]_block_invoke.372.cold.1
- ___55-[POExtensionAgentProcess setLoginUserName:completion:]_block_invoke.380
- ___55-[POExtensionAgentProcess setLoginUserName:completion:]_block_invoke.380.cold.1
- ___55-[POExtensionAgentProcess setLoginUserName:completion:]_block_invoke.384
- ___55-[POExtensionAgentProcess setLoginUserName:completion:]_block_invoke.384.cold.1
- ___57-[POExtensionAgentProcess resetDeviceKeysWithCompletion:]_block_invoke.330
- ___57-[POExtensionAgentProcess resetDeviceKeysWithCompletion:]_block_invoke.330.cold.1
- ___57-[POExtensionAgentProcess resetDeviceKeysWithCompletion:]_block_invoke.333
- ___57-[POExtensionAgentProcess resetDeviceKeysWithCompletion:]_block_invoke.333.cold.1
- ___57-[POExtensionAgentProcess resetDeviceKeysWithCompletion:]_block_invoke.334
- ___57-[POExtensionAgentProcess resetDeviceKeysWithCompletion:]_block_invoke.334.cold.1
- ___58-[POExtensionAgentProcess rotateKeyForKeyType:completion:]_block_invoke.408
- ___58-[POExtensionAgentProcess rotateKeyForKeyType:completion:]_block_invoke.408.cold.1
- ___58-[POExtensionAgentProcess rotateKeyForKeyType:completion:]_block_invoke.411
- ___58-[POExtensionAgentProcess rotateKeyForKeyType:completion:]_block_invoke.411.cold.1
- ___58-[POExtensionAgentProcess rotateKeyForKeyType:completion:]_block_invoke.412
- ___58-[POExtensionAgentProcess rotateKeyForKeyType:completion:]_block_invoke.412.cold.1
- ___58-[POExtensionAgentProcess rotateKeyForKeyType:completion:]_block_invoke.415
- ___58-[POExtensionAgentProcess rotateKeyForKeyType:completion:]_block_invoke.415.cold.1
- ___58-[POExtensionAgentProcess rotateKeyForKeyType:completion:]_block_invoke.418
- ___58-[POExtensionAgentProcess rotateKeyForKeyType:completion:]_block_invoke.418.cold.1
- ___58-[POExtensionAgentProcess rotateKeyForKeyType:completion:]_block_invoke.424
- ___58-[POExtensionAgentProcess rotateKeyForKeyType:completion:]_block_invoke.424.cold.1
- ___60-[POExtensionAgentProcess setLoginConfiguration:completion:]_block_invoke.152
- ___60-[POExtensionAgentProcess setLoginConfiguration:completion:]_block_invoke.152.cold.1
- ___60-[POExtensionAgentProcess setLoginConfiguration:completion:]_block_invoke.158
- ___60-[POExtensionAgentProcess setLoginConfiguration:completion:]_block_invoke.158.cold.1
- ___60-[POExtensionAgentProcess setLoginConfiguration:completion:]_block_invoke.164
- ___60-[POExtensionAgentProcess setLoginConfiguration:completion:]_block_invoke.164.cold.1
- ___60-[POExtensionAgentProcess setLoginConfiguration:completion:]_block_invoke.170
- ___60-[POExtensionAgentProcess setLoginConfiguration:completion:]_block_invoke.170.cold.1
- ___60-[POExtensionAgentProcess setLoginConfiguration:completion:]_block_invoke.177
- ___60-[POExtensionAgentProcess setLoginConfiguration:completion:]_block_invoke.177.cold.1
- ___60-[POExtensionAgentProcess setLoginConfiguration:completion:]_block_invoke.183
- ___60-[POExtensionAgentProcess setLoginConfiguration:completion:]_block_invoke.183.cold.1
- ___60-[POExtensionAgentProcess setLoginConfiguration:completion:]_block_invoke.189
- ___60-[POExtensionAgentProcess setLoginConfiguration:completion:]_block_invoke.189.cold.1
- ___60-[POExtensionAgentProcess setLoginConfiguration:completion:]_block_invoke.195
- ___60-[POExtensionAgentProcess setLoginConfiguration:completion:]_block_invoke.195.cold.1
- ___60-[POExtensionAgentProcess setLoginConfiguration:completion:]_block_invoke.201
- ___60-[POExtensionAgentProcess setLoginConfiguration:completion:]_block_invoke.201.cold.1
- ___60-[POExtensionAgentProcess setLoginConfiguration:completion:]_block_invoke.207
- ___60-[POExtensionAgentProcess setLoginConfiguration:completion:]_block_invoke.207.cold.1
- ___60-[POExtensionAgentProcess setLoginConfiguration:completion:]_block_invoke.213
- ___60-[POExtensionAgentProcess setLoginConfiguration:completion:]_block_invoke.213.cold.1
- ___60-[POExtensionAgentProcess setLoginConfiguration:completion:]_block_invoke.219
- ___60-[POExtensionAgentProcess setLoginConfiguration:completion:]_block_invoke.219.cold.1
- ___60-[POExtensionAgentProcess setLoginConfiguration:completion:]_block_invoke.225
- ___60-[POExtensionAgentProcess setLoginConfiguration:completion:]_block_invoke.225.cold.1
- ___60-[POExtensionAgentProcess setLoginConfiguration:completion:]_block_invoke.232
- ___60-[POExtensionAgentProcess setLoginConfiguration:completion:]_block_invoke.232.cold.1
- ___60-[POExtensionAgentProcess setLoginConfiguration:completion:]_block_invoke.238
- ___60-[POExtensionAgentProcess setLoginConfiguration:completion:]_block_invoke.238.cold.1
- ___60-[POExtensionAgentProcess setLoginConfiguration:completion:]_block_invoke.244
- ___60-[POExtensionAgentProcess setLoginConfiguration:completion:]_block_invoke.244.cold.1
- ___60-[POExtensionAgentProcess setLoginConfiguration:completion:]_block_invoke.250
- ___60-[POExtensionAgentProcess setLoginConfiguration:completion:]_block_invoke.250.cold.1
- ___60-[POExtensionAgentProcess setLoginConfiguration:completion:]_block_invoke.256
- ___60-[POExtensionAgentProcess setLoginConfiguration:completion:]_block_invoke.256.cold.1
- ___60-[POExtensionAgentProcess setLoginConfiguration:completion:]_block_invoke.262
- ___60-[POExtensionAgentProcess setLoginConfiguration:completion:]_block_invoke.262.cold.1
- ___64-[POExtensionAgentProcess setUserLoginConfiguration:completion:]_block_invoke.400
- ___64-[POExtensionAgentProcess setUserLoginConfiguration:completion:]_block_invoke.400.cold.1
- ___65-[POExtensionAgentProcess setCertificateData:keyType:completion:]_block_invoke.279
- ___65-[POExtensionAgentProcess setCertificateData:keyType:completion:]_block_invoke.279.cold.1
- ___65-[POExtensionAgentProcess setCertificateData:keyType:completion:]_block_invoke.280
- ___65-[POExtensionAgentProcess setCertificateData:keyType:completion:]_block_invoke.280.cold.1
- ___65-[POExtensionAgentProcess setCertificateData:keyType:completion:]_block_invoke.286
- ___65-[POExtensionAgentProcess setCertificateData:keyType:completion:]_block_invoke.286.cold.1
- ___67-[POExtensionAgentProcess resetUserSecureEnclaveKeyWithCompletion:]_block_invoke.345
- ___67-[POExtensionAgentProcess resetUserSecureEnclaveKeyWithCompletion:]_block_invoke.345.cold.1
- ___67-[POExtensionAgentProcess resetUserSecureEnclaveKeyWithCompletion:]_block_invoke.348
- ___67-[POExtensionAgentProcess resetUserSecureEnclaveKeyWithCompletion:]_block_invoke.348.cold.1
- ___67-[POExtensionAgentProcess resetUserSecureEnclaveKeyWithCompletion:]_block_invoke.349
- ___67-[POExtensionAgentProcess resetUserSecureEnclaveKeyWithCompletion:]_block_invoke.349.cold.1
- ___67-[POExtensionAgentProcess resetUserSecureEnclaveKeyWithCompletion:]_block_invoke.355
- ___67-[POExtensionAgentProcess resetUserSecureEnclaveKeyWithCompletion:]_block_invoke.355.cold.1
- ___67-[POExtensionAgentProcess resetUserSecureEnclaveKeyWithCompletion:]_block_invoke.361
- ___67-[POExtensionAgentProcess resetUserSecureEnclaveKeyWithCompletion:]_block_invoke.361.cold.1
- ___67-[POExtensionAgentProcess userNeedsReauthenticationWithCompletion:]_block_invoke.311
- ___68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.435
- ___68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.435.cold.1
- ___68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.438
- ___68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.438.cold.1
- ___68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.439
- ___68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.439.cold.1
- ___68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.442
- ___68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.442.cold.1
- ___68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.445
- ___68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.445.cold.1
- ___68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.449
- ___68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.449.cold.1
- ___68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.452
- ___68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.452.cold.1
- ___70-[POExtensionAgentProcess userRegistrationsNeedsRepairWithCompletion:]_block_invoke.324
- ___72-[POExtensionAgentProcess deviceRegistrationsNeedsRepairWithCompletion:]_block_invoke.318
- ___block_literal_global.100
- ___block_literal_global.103
- ___block_literal_global.105
- ___block_literal_global.121
- ___block_literal_global.122
- ___block_literal_global.220
- ___block_literal_global.27
- ___block_literal_global.658
- ___block_literal_global.66
CStrings:
+ "-[POExtensionAgentProcess authenticationMethodWithCompletion:]"
+ "-[POLoginManager authenticationMethod]"
+ "Ti,R,N"
+ "authenticationMethodWithCompletion:"
+ "failed to retrieve authenticationMethod"
+ "v20@?0i8@\"NSError\"12"
+ "v24@0:8@?<v@?i@\"NSError\">16"

```
