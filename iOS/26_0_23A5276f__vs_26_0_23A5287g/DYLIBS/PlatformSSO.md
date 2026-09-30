## PlatformSSO

> `/System/Library/PrivateFrameworks/PlatformSSO.framework/PlatformSSO`

```diff

-483.0.19.0.0
-  __TEXT.__text: 0x58a40
-  __TEXT.__auth_stubs: 0xe50
-  __TEXT.__objc_methlist: 0x3294
-  __TEXT.__const: 0x282
-  __TEXT.__cstring: 0x8036
-  __TEXT.__oslogstring: 0x2241
+483.0.24.0.0
+  __TEXT.__text: 0x58d1c
+  __TEXT.__auth_stubs: 0xe70
+  __TEXT.__objc_methlist: 0x32ac
+  __TEXT.__const: 0x27a
+  __TEXT.__cstring: 0x8016
+  __TEXT.__oslogstring: 0x2321
   __TEXT.__gcc_except_tab: 0x1514
   __TEXT.__dlopen_cstrs: 0x110
-  __TEXT.__swift5_typeref: 0xc1
+  __TEXT.__swift5_typeref: 0xc2
   __TEXT.__swift5_capture: 0x118
   __TEXT.__constg_swiftt: 0x4c
   __TEXT.__swift5_builtin: 0x28

   __TEXT.__swift5_types: 0x8
   __TEXT.__swift_as_entry: 0x2c
   __TEXT.__swift_as_ret: 0x50
-  __TEXT.__unwind_info: 0x1518
+  __TEXT.__unwind_info: 0x1520
   __TEXT.__eh_frame: 0x560
   __TEXT.__objc_classname: 0x3d6
-  __TEXT.__objc_methname: 0x9c8f
+  __TEXT.__objc_methname: 0x9d11
   __TEXT.__objc_methtype: 0x14fe
   __TEXT.__objc_stubs: 0x6f00
   __DATA_CONST.__got: 0x430

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x21f0
+  __DATA_CONST.__objc_selrefs: 0x2200
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0xc0
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__auth_got: 0x738
+  __AUTH_CONST.__auth_got: 0x748
   __AUTH_CONST.__const: 0xc28
   __AUTH_CONST.__cfstring: 0x3820
-  __AUTH_CONST.__objc_const: 0x8148
+  __AUTH_CONST.__objc_const: 0x8178
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH.__objc_data: 0xa00
-  __DATA.__objc_ivar: 0x344
+  __DATA.__objc_ivar: 0x348
   __DATA.__data: 0x620
   __DATA.__bss: 0x2d0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 889CD0B6-1DC4-32B8-B698-31A489350E01
-  Functions: 2040
-  Symbols:   7215
-  CStrings:  3134
+  UUID: B3235421-F68D-3FBE-AAF7-C68830AE0F85
+  Functions: 2043
+  Symbols:   7219
+  CStrings:  3142
 
Symbols:
+ -[POExtensionAgentProcess bundleIdentifierForXPCConnection:].cold.2
+ -[POProfile enableRegistrationDuringSetup]
+ -[POProfile setEnableRegistrationDuringSetup:]
+ GCC_except_table115
+ GCC_except_table123
+ GCC_except_table278
+ GCC_except_table287
+ GCC_except_table82
+ _OBJC_IVAR_$_POProfile._enableRegistrationDuringSetup
+ _SecTaskGetCodeSignStatus
+ ___51-[POExtensionAgentProcess setSsoTokens:completion:]_block_invoke.115
+ ___51-[POExtensionAgentProcess setSsoTokens:completion:]_block_invoke.115.cold.1
+ ___51-[POExtensionAgentProcess setSsoTokens:completion:]_block_invoke.116
+ ___51-[POExtensionAgentProcess setSsoTokens:completion:]_block_invoke.116.cold.1
+ ___51-[POExtensionAgentProcess setSsoTokens:completion:]_block_invoke.120
+ ___51-[POExtensionAgentProcess setSsoTokens:completion:]_block_invoke.120.cold.1
+ ___51-[POExtensionAgentProcess setSsoTokens:completion:]_block_invoke.123
+ ___51-[POExtensionAgentProcess setSsoTokens:completion:]_block_invoke.123.cold.1
+ ___51-[POExtensionAgentProcess setSsoTokens:completion:]_block_invoke.127
+ ___51-[POExtensionAgentProcess setSsoTokens:completion:]_block_invoke.127.cold.1
+ ___51-[POExtensionAgentProcess setSsoTokens:completion:]_block_invoke.131
+ ___51-[POExtensionAgentProcess setSsoTokens:completion:]_block_invoke.131.cold.1
+ ___51-[POExtensionAgentProcess setSsoTokens:completion:]_block_invoke.135
+ ___51-[POExtensionAgentProcess ssoTokensWithCompletion:]_block_invoke.87
+ ___51-[POExtensionAgentProcess ssoTokensWithCompletion:]_block_invoke.87.cold.1
+ ___51-[POExtensionAgentProcess ssoTokensWithCompletion:]_block_invoke.88
+ ___51-[POExtensionAgentProcess ssoTokensWithCompletion:]_block_invoke.88.cold.1
+ ___54-[POExtensionAgentProcess isCallerCurrentSSOExtension]_block_invoke.53
+ ___54-[POExtensionAgentProcess isCallerCurrentSSOExtension]_block_invoke.53.cold.1
+ ___55-[POExtensionAgentProcess loginUserNameWithCompletion:]_block_invoke.372
+ ___55-[POExtensionAgentProcess loginUserNameWithCompletion:]_block_invoke.372.cold.1
+ ___55-[POExtensionAgentProcess setLoginUserName:completion:]_block_invoke.380
+ ___55-[POExtensionAgentProcess setLoginUserName:completion:]_block_invoke.380.cold.1
+ ___55-[POExtensionAgentProcess setLoginUserName:completion:]_block_invoke.384
+ ___55-[POExtensionAgentProcess setLoginUserName:completion:]_block_invoke.384.cold.1
+ ___57-[POExtensionAgentProcess resetDeviceKeysWithCompletion:]_block_invoke.330
+ ___57-[POExtensionAgentProcess resetDeviceKeysWithCompletion:]_block_invoke.330.cold.1
+ ___57-[POExtensionAgentProcess resetDeviceKeysWithCompletion:]_block_invoke.333
+ ___57-[POExtensionAgentProcess resetDeviceKeysWithCompletion:]_block_invoke.333.cold.1
+ ___57-[POExtensionAgentProcess resetDeviceKeysWithCompletion:]_block_invoke.334
+ ___57-[POExtensionAgentProcess resetDeviceKeysWithCompletion:]_block_invoke.334.cold.1
+ ___58-[POExtensionAgentProcess rotateKeyForKeyType:completion:]_block_invoke.408
+ ___58-[POExtensionAgentProcess rotateKeyForKeyType:completion:]_block_invoke.408.cold.1
+ ___58-[POExtensionAgentProcess rotateKeyForKeyType:completion:]_block_invoke.411
+ ___58-[POExtensionAgentProcess rotateKeyForKeyType:completion:]_block_invoke.411.cold.1
+ ___58-[POExtensionAgentProcess rotateKeyForKeyType:completion:]_block_invoke.412
+ ___58-[POExtensionAgentProcess rotateKeyForKeyType:completion:]_block_invoke.412.cold.1
+ ___58-[POExtensionAgentProcess rotateKeyForKeyType:completion:]_block_invoke.415
+ ___58-[POExtensionAgentProcess rotateKeyForKeyType:completion:]_block_invoke.415.cold.1
+ ___59-[POExtensionAgentProcess registrationTokenWithCompletion:]_block_invoke.73
+ ___59-[POExtensionAgentProcess registrationTokenWithCompletion:]_block_invoke.73.cold.1
+ ___60-[POExtensionAgentProcess setLoginConfiguration:completion:]_block_invoke.152
+ ___60-[POExtensionAgentProcess setLoginConfiguration:completion:]_block_invoke.152.cold.1
+ ___60-[POExtensionAgentProcess setLoginConfiguration:completion:]_block_invoke.177
+ ___60-[POExtensionAgentProcess setLoginConfiguration:completion:]_block_invoke.177.cold.1
+ ___60-[POExtensionAgentProcess setLoginConfiguration:completion:]_block_invoke.232
+ ___60-[POExtensionAgentProcess setLoginConfiguration:completion:]_block_invoke.232.cold.1
+ ___64-[POExtensionAgentProcess setUserLoginConfiguration:completion:]_block_invoke.400
+ ___64-[POExtensionAgentProcess setUserLoginConfiguration:completion:]_block_invoke.400.cold.1
+ ___65-[POExtensionAgentProcess setCertificateData:keyType:completion:]_block_invoke.279
+ ___65-[POExtensionAgentProcess setCertificateData:keyType:completion:]_block_invoke.279.cold.1
+ ___65-[POExtensionAgentProcess setCertificateData:keyType:completion:]_block_invoke.280
+ ___65-[POExtensionAgentProcess setCertificateData:keyType:completion:]_block_invoke.280.cold.1
+ ___67-[POExtensionAgentProcess resetUserSecureEnclaveKeyWithCompletion:]_block_invoke.345
+ ___67-[POExtensionAgentProcess resetUserSecureEnclaveKeyWithCompletion:]_block_invoke.345.cold.1
+ ___67-[POExtensionAgentProcess resetUserSecureEnclaveKeyWithCompletion:]_block_invoke.348
+ ___67-[POExtensionAgentProcess resetUserSecureEnclaveKeyWithCompletion:]_block_invoke.348.cold.1
+ ___67-[POExtensionAgentProcess resetUserSecureEnclaveKeyWithCompletion:]_block_invoke.349
+ ___67-[POExtensionAgentProcess resetUserSecureEnclaveKeyWithCompletion:]_block_invoke.349.cold.1
+ ___67-[POExtensionAgentProcess userNeedsReauthenticationWithCompletion:]_block_invoke.311
+ ___68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.435
+ ___68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.435.cold.1
+ ___68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.438
+ ___68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.438.cold.1
+ ___68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.439
+ ___68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.439.cold.1
+ ___68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.442
+ ___68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.442.cold.1
+ ___68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.449
+ ___68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.449.cold.1
+ ___68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.452
+ ___68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.452.cold.1
+ ___70-[POExtensionAgentProcess userRegistrationsNeedsRepairWithCompletion:]_block_invoke.324
+ ___72-[POExtensionAgentProcess deviceRegistrationsNeedsRepairWithCompletion:]_block_invoke.318
+ ___block_literal_global.295
+ ___block_literal_global.658
+ _block_copy_helper.107
+ _block_copy_helper.14
+ _block_copy_helper.17
+ _block_copy_helper.2
+ _block_copy_helper.20
+ _block_copy_helper.23
+ _block_copy_helper.30
+ _block_copy_helper.33
+ _block_copy_helper.5
+ _block_copy_helper.8
+ _block_copy_helper.88
+ _block_copy_helper.91
+ _block_copy_helper.94
+ _block_descriptor.10
+ _block_descriptor.109
+ _block_descriptor.16
+ _block_descriptor.19
+ _block_descriptor.22
+ _block_descriptor.25
+ _block_descriptor.32
+ _block_descriptor.35
+ _block_descriptor.4
+ _block_descriptor.7
+ _block_descriptor.90
+ _block_descriptor.93
+ _block_descriptor.96
+ _block_destroy_helper.108
+ _block_destroy_helper.15
+ _block_destroy_helper.18
+ _block_destroy_helper.21
+ _block_destroy_helper.24
+ _block_destroy_helper.3
+ _block_destroy_helper.31
+ _block_destroy_helper.34
+ _block_destroy_helper.6
+ _block_destroy_helper.89
+ _block_destroy_helper.9
+ _block_destroy_helper.92
+ _block_destroy_helper.95
+ _objectdestroy.39Tm
+ _objectdestroy.43Tm
- GCC_except_table124
- GCC_except_table279
- GCC_except_table288
- GCC_except_table83
- ___51-[POExtensionAgentProcess setSsoTokens:completion:]_block_invoke.121
- ___51-[POExtensionAgentProcess setSsoTokens:completion:]_block_invoke.121.cold.1
- ___51-[POExtensionAgentProcess setSsoTokens:completion:]_block_invoke.122
- ___51-[POExtensionAgentProcess setSsoTokens:completion:]_block_invoke.122.cold.1
- ___51-[POExtensionAgentProcess setSsoTokens:completion:]_block_invoke.126
- ___51-[POExtensionAgentProcess setSsoTokens:completion:]_block_invoke.126.cold.1
- ___51-[POExtensionAgentProcess setSsoTokens:completion:]_block_invoke.129
- ___51-[POExtensionAgentProcess setSsoTokens:completion:]_block_invoke.129.cold.1
- ___51-[POExtensionAgentProcess setSsoTokens:completion:]_block_invoke.133
- ___51-[POExtensionAgentProcess setSsoTokens:completion:]_block_invoke.133.cold.1
- ___51-[POExtensionAgentProcess setSsoTokens:completion:]_block_invoke.137
- ___51-[POExtensionAgentProcess setSsoTokens:completion:]_block_invoke.137.cold.1
- ___51-[POExtensionAgentProcess setSsoTokens:completion:]_block_invoke.141
- ___51-[POExtensionAgentProcess ssoTokensWithCompletion:]_block_invoke.112
- ___51-[POExtensionAgentProcess ssoTokensWithCompletion:]_block_invoke.112.cold.1
- ___51-[POExtensionAgentProcess ssoTokensWithCompletion:]_block_invoke.93
- ___51-[POExtensionAgentProcess ssoTokensWithCompletion:]_block_invoke.93.cold.1
- ___54-[POExtensionAgentProcess isCallerCurrentSSOExtension]_block_invoke.59
- ___54-[POExtensionAgentProcess isCallerCurrentSSOExtension]_block_invoke.59.cold.1
- ___55-[POExtensionAgentProcess loginUserNameWithCompletion:]_block_invoke.378
- ___55-[POExtensionAgentProcess loginUserNameWithCompletion:]_block_invoke.378.cold.1
- ___55-[POExtensionAgentProcess setLoginUserName:completion:]_block_invoke.386
- ___55-[POExtensionAgentProcess setLoginUserName:completion:]_block_invoke.386.cold.1
- ___55-[POExtensionAgentProcess setLoginUserName:completion:]_block_invoke.390
- ___55-[POExtensionAgentProcess setLoginUserName:completion:]_block_invoke.390.cold.1
- ___57-[POExtensionAgentProcess resetDeviceKeysWithCompletion:]_block_invoke.336
- ___57-[POExtensionAgentProcess resetDeviceKeysWithCompletion:]_block_invoke.336.cold.1
- ___57-[POExtensionAgentProcess resetDeviceKeysWithCompletion:]_block_invoke.339
- ___57-[POExtensionAgentProcess resetDeviceKeysWithCompletion:]_block_invoke.339.cold.1
- ___57-[POExtensionAgentProcess resetDeviceKeysWithCompletion:]_block_invoke.340
- ___57-[POExtensionAgentProcess resetDeviceKeysWithCompletion:]_block_invoke.340.cold.1
- ___58-[POExtensionAgentProcess rotateKeyForKeyType:completion:]_block_invoke.414
- ___58-[POExtensionAgentProcess rotateKeyForKeyType:completion:]_block_invoke.414.cold.1
- ___58-[POExtensionAgentProcess rotateKeyForKeyType:completion:]_block_invoke.417
- ___58-[POExtensionAgentProcess rotateKeyForKeyType:completion:]_block_invoke.417.cold.1
- ___58-[POExtensionAgentProcess rotateKeyForKeyType:completion:]_block_invoke.421
- ___58-[POExtensionAgentProcess rotateKeyForKeyType:completion:]_block_invoke.421.cold.1
- ___58-[POExtensionAgentProcess rotateKeyForKeyType:completion:]_block_invoke.430
- ___58-[POExtensionAgentProcess rotateKeyForKeyType:completion:]_block_invoke.430.cold.1
- ___59-[POExtensionAgentProcess registrationTokenWithCompletion:]_block_invoke.79
- ___59-[POExtensionAgentProcess registrationTokenWithCompletion:]_block_invoke.79.cold.1
- ___60-[POExtensionAgentProcess bundleIdentifierForXPCConnection:]_block_invoke.50
- ___60-[POExtensionAgentProcess bundleIdentifierForXPCConnection:]_block_invoke.50.cold.1
- ___60-[POExtensionAgentProcess setLoginConfiguration:completion:]_block_invoke.176
- ___60-[POExtensionAgentProcess setLoginConfiguration:completion:]_block_invoke.176.cold.1
- ___60-[POExtensionAgentProcess setLoginConfiguration:completion:]_block_invoke.231
- ___60-[POExtensionAgentProcess setLoginConfiguration:completion:]_block_invoke.231.cold.1
- ___60-[POExtensionAgentProcess setLoginConfiguration:completion:]_block_invoke.268
- ___60-[POExtensionAgentProcess setLoginConfiguration:completion:]_block_invoke.268.cold.1
- ___64-[POExtensionAgentProcess setUserLoginConfiguration:completion:]_block_invoke.406
- ___64-[POExtensionAgentProcess setUserLoginConfiguration:completion:]_block_invoke.406.cold.1
- ___65-[POExtensionAgentProcess setCertificateData:keyType:completion:]_block_invoke.285
- ___65-[POExtensionAgentProcess setCertificateData:keyType:completion:]_block_invoke.285.cold.1
- ___65-[POExtensionAgentProcess setCertificateData:keyType:completion:]_block_invoke.292
- ___65-[POExtensionAgentProcess setCertificateData:keyType:completion:]_block_invoke.292.cold.1
- ___67-[POExtensionAgentProcess resetUserSecureEnclaveKeyWithCompletion:]_block_invoke.351
- ___67-[POExtensionAgentProcess resetUserSecureEnclaveKeyWithCompletion:]_block_invoke.351.cold.1
- ___67-[POExtensionAgentProcess resetUserSecureEnclaveKeyWithCompletion:]_block_invoke.354
- ___67-[POExtensionAgentProcess resetUserSecureEnclaveKeyWithCompletion:]_block_invoke.354.cold.1
- ___67-[POExtensionAgentProcess resetUserSecureEnclaveKeyWithCompletion:]_block_invoke.367
- ___67-[POExtensionAgentProcess resetUserSecureEnclaveKeyWithCompletion:]_block_invoke.367.cold.1
- ___67-[POExtensionAgentProcess userNeedsReauthenticationWithCompletion:]_block_invoke.317
- ___68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.441
- ___68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.441.cold.1
- ___68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.444
- ___68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.444.cold.1
- ___68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.448
- ___68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.448.cold.1
- ___68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.451
- ___68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.451.cold.1
- ___68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.455
- ___68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.455.cold.1
- ___68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.458
- ___68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.458.cold.1
- ___70-[POExtensionAgentProcess userRegistrationsNeedsRepairWithCompletion:]_block_invoke.330
- ___72-[POExtensionAgentProcess deviceRegistrationsNeedsRepairWithCompletion:]_block_invoke.324
- ___block_literal_global.287
- ___block_literal_global.664
- _block_copy_helper.102
- _block_copy_helper.12
- _block_copy_helper.18
- _block_copy_helper.21
- _block_copy_helper.24
- _block_copy_helper.27
- _block_copy_helper.39
- _block_copy_helper.42
- _block_copy_helper.6
- _block_copy_helper.9
- _block_copy_helper.92
- _block_copy_helper.95
- _block_copy_helper.98
- _block_descriptor.100
- _block_descriptor.104
- _block_descriptor.11
- _block_descriptor.14
- _block_descriptor.20
- _block_descriptor.23
- _block_descriptor.26
- _block_descriptor.29
- _block_descriptor.41
- _block_descriptor.44
- _block_descriptor.8
- _block_descriptor.94
- _block_descriptor.97
- _block_destroy_helper.10
- _block_destroy_helper.103
- _block_destroy_helper.13
- _block_destroy_helper.19
- _block_destroy_helper.22
- _block_destroy_helper.25
- _block_destroy_helper.28
- _block_destroy_helper.40
- _block_destroy_helper.43
- _block_destroy_helper.7
- _block_destroy_helper.93
- _block_destroy_helper.96
- _block_destroy_helper.99
- _objectdestroy.48Tm
- _objectdestroy.52Tm
CStrings:
+ "EnableRegistrationDuringSetup"
+ "TB,V_enableRegistrationDuringSetup"
+ "_enableRegistrationDuringSetup"
+ "bundleIdentifier: SecTaskCopySigningIdentifier() failed %{public}@"
+ "bundleIdentifier: SecTaskCreateWithAuditToken() failed"
+ "bundleIdentifier: The entitlements are not valid."
+ "bundleIdentifier: using SecTaskCopySigningIdentifier()"
+ "enableRegistrationDuringSetup"
+ "setEnableRegistrationDuringSetup:"
- "bundleIdentifier: SecTaskCreateWithAuditToken() failed."

```
