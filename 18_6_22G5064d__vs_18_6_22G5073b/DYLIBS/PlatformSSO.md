## PlatformSSO

> `/System/Library/PrivateFrameworks/PlatformSSO.framework/PlatformSSO`

```diff

-417.140.2.0.0
-  __TEXT.__text: 0x4f080
-  __TEXT.__auth_stubs: 0xa30
+417.140.3.0.0
+  __TEXT.__text: 0x4f1c4
+  __TEXT.__auth_stubs: 0xa40
   __TEXT.__objc_methlist: 0x2dcc
   __TEXT.__const: 0x110
-  __TEXT.__cstring: 0x7c14
-  __TEXT.__oslogstring: 0x1d3c
+  __TEXT.__cstring: 0x7bdc
+  __TEXT.__oslogstring: 0x1e1f
   __TEXT.__gcc_except_tab: 0x14dc
   __TEXT.__dlopen_cstrs: 0x110
   __TEXT.__unwind_info: 0x1210

   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0xb8
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__auth_got: 0x528
+  __AUTH_CONST.__auth_got: 0x530
   __AUTH_CONST.__const: 0x720
-  __AUTH_CONST.__cfstring: 0x36a0
+  __AUTH_CONST.__cfstring: 0x3680
   __AUTH_CONST.__objc_const: 0x7438
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__objc_doubleobj: 0x20

   - /System/Library/PrivateFrameworks/UserManagement.framework/UserManagement
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A6E2A4C3-A2C1-38D2-B421-D6602121CFEC
+  UUID: 28C7457C-2964-37CD-915A-3F8FC6676B66
   Functions: 1771
-  Symbols:   6680
-  CStrings:  2930
+  Symbols:   6679
+  CStrings:  2932
 
Symbols:
+ -[POExtensionAgentProcess bundleIdentiferForXPCConnection:].cold.2
+ GCC_except_table117
+ GCC_except_table125
+ GCC_except_table282
+ GCC_except_table291
+ GCC_except_table82
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
+ ___55-[POExtensionAgentProcess loginUserNameWithCompletion:]_block_invoke.377
+ ___55-[POExtensionAgentProcess loginUserNameWithCompletion:]_block_invoke.377.cold.1
+ ___55-[POExtensionAgentProcess setLoginUserName:completion:]_block_invoke.385
+ ___55-[POExtensionAgentProcess setLoginUserName:completion:]_block_invoke.385.cold.1
+ ___55-[POExtensionAgentProcess setLoginUserName:completion:]_block_invoke.389
+ ___55-[POExtensionAgentProcess setLoginUserName:completion:]_block_invoke.389.cold.1
+ ___57-[POExtensionAgentProcess resetDeviceKeysWithCompletion:]_block_invoke.335
+ ___57-[POExtensionAgentProcess resetDeviceKeysWithCompletion:]_block_invoke.335.cold.1
+ ___57-[POExtensionAgentProcess resetDeviceKeysWithCompletion:]_block_invoke.338
+ ___57-[POExtensionAgentProcess resetDeviceKeysWithCompletion:]_block_invoke.338.cold.1
+ ___57-[POExtensionAgentProcess resetDeviceKeysWithCompletion:]_block_invoke.339
+ ___57-[POExtensionAgentProcess resetDeviceKeysWithCompletion:]_block_invoke.339.cold.1
+ ___58-[POExtensionAgentProcess rotateKeyForKeyType:completion:]_block_invoke.413
+ ___58-[POExtensionAgentProcess rotateKeyForKeyType:completion:]_block_invoke.413.cold.1
+ ___58-[POExtensionAgentProcess rotateKeyForKeyType:completion:]_block_invoke.416
+ ___58-[POExtensionAgentProcess rotateKeyForKeyType:completion:]_block_invoke.416.cold.1
+ ___58-[POExtensionAgentProcess rotateKeyForKeyType:completion:]_block_invoke.417
+ ___58-[POExtensionAgentProcess rotateKeyForKeyType:completion:]_block_invoke.417.cold.1
+ ___58-[POExtensionAgentProcess rotateKeyForKeyType:completion:]_block_invoke.420
+ ___58-[POExtensionAgentProcess rotateKeyForKeyType:completion:]_block_invoke.420.cold.1
+ ___59-[POExtensionAgentProcess registrationTokenWithCompletion:]_block_invoke.73
+ ___59-[POExtensionAgentProcess registrationTokenWithCompletion:]_block_invoke.73.cold.1
+ ___60-[POExtensionAgentProcess setLoginConfiguration:completion:]_block_invoke.152
+ ___60-[POExtensionAgentProcess setLoginConfiguration:completion:]_block_invoke.152.cold.1
+ ___60-[POExtensionAgentProcess setLoginConfiguration:completion:]_block_invoke.177
+ ___60-[POExtensionAgentProcess setLoginConfiguration:completion:]_block_invoke.177.cold.1
+ ___60-[POExtensionAgentProcess setLoginConfiguration:completion:]_block_invoke.232
+ ___60-[POExtensionAgentProcess setLoginConfiguration:completion:]_block_invoke.232.cold.1
+ ___64-[POExtensionAgentProcess setUserLoginConfiguration:completion:]_block_invoke.405
+ ___64-[POExtensionAgentProcess setUserLoginConfiguration:completion:]_block_invoke.405.cold.1
+ ___65-[POExtensionAgentProcess setCertificateData:keyType:completion:]_block_invoke.279
+ ___65-[POExtensionAgentProcess setCertificateData:keyType:completion:]_block_invoke.279.cold.1
+ ___65-[POExtensionAgentProcess setCertificateData:keyType:completion:]_block_invoke.280
+ ___65-[POExtensionAgentProcess setCertificateData:keyType:completion:]_block_invoke.280.cold.1
+ ___67-[POExtensionAgentProcess resetUserSecureEnclaveKeyWithCompletion:]_block_invoke.350
+ ___67-[POExtensionAgentProcess resetUserSecureEnclaveKeyWithCompletion:]_block_invoke.350.cold.1
+ ___67-[POExtensionAgentProcess resetUserSecureEnclaveKeyWithCompletion:]_block_invoke.353
+ ___67-[POExtensionAgentProcess resetUserSecureEnclaveKeyWithCompletion:]_block_invoke.353.cold.1
+ ___67-[POExtensionAgentProcess resetUserSecureEnclaveKeyWithCompletion:]_block_invoke.354
+ ___67-[POExtensionAgentProcess resetUserSecureEnclaveKeyWithCompletion:]_block_invoke.354.cold.1
+ ___67-[POExtensionAgentProcess userNeedsReauthenticationWithCompletion:]_block_invoke.311
+ ___68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.440
+ ___68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.440.cold.1
+ ___68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.443
+ ___68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.443.cold.1
+ ___68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.444
+ ___68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.444.cold.1
+ ___68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.447
+ ___68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.447.cold.1
+ ___68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.454
+ ___68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.454.cold.1
+ ___68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.457
+ ___68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.457.cold.1
+ ___70-[POExtensionAgentProcess userRegistrationsNeedsRepairWithCompletion:]_block_invoke.324
+ ___72-[POExtensionAgentProcess deviceRegistrationsNeedsRepairWithCompletion:]_block_invoke.318
+ ___block_literal_global.664
- GCC_except_table118
- GCC_except_table126
- GCC_except_table283
- GCC_except_table292
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
- ___55-[POExtensionAgentProcess loginUserNameWithCompletion:]_block_invoke.383
- ___55-[POExtensionAgentProcess loginUserNameWithCompletion:]_block_invoke.383.cold.1
- ___55-[POExtensionAgentProcess setLoginUserName:completion:]_block_invoke.391
- ___55-[POExtensionAgentProcess setLoginUserName:completion:]_block_invoke.391.cold.1
- ___55-[POExtensionAgentProcess setLoginUserName:completion:]_block_invoke.395
- ___55-[POExtensionAgentProcess setLoginUserName:completion:]_block_invoke.395.cold.1
- ___57-[POExtensionAgentProcess resetDeviceKeysWithCompletion:]_block_invoke.341
- ___57-[POExtensionAgentProcess resetDeviceKeysWithCompletion:]_block_invoke.341.cold.1
- ___57-[POExtensionAgentProcess resetDeviceKeysWithCompletion:]_block_invoke.344
- ___57-[POExtensionAgentProcess resetDeviceKeysWithCompletion:]_block_invoke.344.cold.1
- ___57-[POExtensionAgentProcess resetDeviceKeysWithCompletion:]_block_invoke.345
- ___57-[POExtensionAgentProcess resetDeviceKeysWithCompletion:]_block_invoke.345.cold.1
- ___58-[POExtensionAgentProcess rotateKeyForKeyType:completion:]_block_invoke.419
- ___58-[POExtensionAgentProcess rotateKeyForKeyType:completion:]_block_invoke.419.cold.1
- ___58-[POExtensionAgentProcess rotateKeyForKeyType:completion:]_block_invoke.422
- ___58-[POExtensionAgentProcess rotateKeyForKeyType:completion:]_block_invoke.422.cold.1
- ___58-[POExtensionAgentProcess rotateKeyForKeyType:completion:]_block_invoke.426
- ___58-[POExtensionAgentProcess rotateKeyForKeyType:completion:]_block_invoke.426.cold.1
- ___58-[POExtensionAgentProcess rotateKeyForKeyType:completion:]_block_invoke.435
- ___58-[POExtensionAgentProcess rotateKeyForKeyType:completion:]_block_invoke.435.cold.1
- ___59-[POExtensionAgentProcess bundleIdentiferForXPCConnection:]_block_invoke.50
- ___59-[POExtensionAgentProcess bundleIdentiferForXPCConnection:]_block_invoke.50.cold.1
- ___59-[POExtensionAgentProcess registrationTokenWithCompletion:]_block_invoke.79
- ___59-[POExtensionAgentProcess registrationTokenWithCompletion:]_block_invoke.79.cold.1
- ___60-[POExtensionAgentProcess setLoginConfiguration:completion:]_block_invoke.176
- ___60-[POExtensionAgentProcess setLoginConfiguration:completion:]_block_invoke.176.cold.1
- ___60-[POExtensionAgentProcess setLoginConfiguration:completion:]_block_invoke.231
- ___60-[POExtensionAgentProcess setLoginConfiguration:completion:]_block_invoke.231.cold.1
- ___60-[POExtensionAgentProcess setLoginConfiguration:completion:]_block_invoke.268
- ___60-[POExtensionAgentProcess setLoginConfiguration:completion:]_block_invoke.268.cold.1
- ___64-[POExtensionAgentProcess setUserLoginConfiguration:completion:]_block_invoke.411
- ___64-[POExtensionAgentProcess setUserLoginConfiguration:completion:]_block_invoke.411.cold.1
- ___65-[POExtensionAgentProcess setCertificateData:keyType:completion:]_block_invoke.285
- ___65-[POExtensionAgentProcess setCertificateData:keyType:completion:]_block_invoke.285.cold.1
- ___65-[POExtensionAgentProcess setCertificateData:keyType:completion:]_block_invoke.292
- ___65-[POExtensionAgentProcess setCertificateData:keyType:completion:]_block_invoke.292.cold.1
- ___67-[POExtensionAgentProcess resetUserSecureEnclaveKeyWithCompletion:]_block_invoke.356
- ___67-[POExtensionAgentProcess resetUserSecureEnclaveKeyWithCompletion:]_block_invoke.356.cold.1
- ___67-[POExtensionAgentProcess resetUserSecureEnclaveKeyWithCompletion:]_block_invoke.359
- ___67-[POExtensionAgentProcess resetUserSecureEnclaveKeyWithCompletion:]_block_invoke.359.cold.1
- ___67-[POExtensionAgentProcess resetUserSecureEnclaveKeyWithCompletion:]_block_invoke.372
- ___67-[POExtensionAgentProcess resetUserSecureEnclaveKeyWithCompletion:]_block_invoke.372.cold.1
- ___67-[POExtensionAgentProcess userNeedsReauthenticationWithCompletion:]_block_invoke.317
- ___68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.446
- ___68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.446.cold.1
- ___68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.449
- ___68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.449.cold.1
- ___68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.453
- ___68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.453.cold.1
- ___68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.456
- ___68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.456.cold.1
- ___68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.460
- ___68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.460.cold.1
- ___68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.463
- ___68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.463.cold.1
- ___70-[POExtensionAgentProcess userRegistrationsNeedsRepairWithCompletion:]_block_invoke.330
- ___72-[POExtensionAgentProcess deviceRegistrationsNeedsRepairWithCompletion:]_block_invoke.324
- ___block_literal_global.670
Functions (modified):
~ -[POExtensionAgentProcess bundleIdentiferForXPCConnection:] : 560 -> 940
~ ___51-[POExtensionAgentProcess ssoTokensWithCompletion:]_block_invoke.106 : 124 -> 140

Functions (added):
+ -[POExtensionAgentProcess bundleIdentiferForXPCConnection:].cold.2

Functions (removed):
- ___68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.449
CStrings:
+ "bundleIdentifier: SecTaskCopySigningIdentifier() failed %{public}@"
+ "bundleIdentifier: SecTaskCreateWithAuditToken() failed"
+ "bundleIdentifier: The entitlements are not valid."
+ "bundleIdentifier: using SecTaskCopySigningIdentifier()"
- "bundleIdentifier: SecTaskCreateWithAuditToken() failed."

```
