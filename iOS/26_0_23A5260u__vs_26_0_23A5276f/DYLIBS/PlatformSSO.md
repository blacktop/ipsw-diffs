## PlatformSSO

> `/System/Library/PrivateFrameworks/PlatformSSO.framework/PlatformSSO`

```diff

-483.0.6.0.1
-  __TEXT.__text: 0x58884
-  __TEXT.__auth_stubs: 0xe10
-  __TEXT.__objc_methlist: 0x324c
-  __TEXT.__const: 0x262
-  __TEXT.__cstring: 0x7f56
-  __TEXT.__oslogstring: 0x21a1
+483.0.19.0.0
+  __TEXT.__text: 0x58a40
+  __TEXT.__auth_stubs: 0xe50
+  __TEXT.__objc_methlist: 0x3294
+  __TEXT.__const: 0x282
+  __TEXT.__cstring: 0x8036
+  __TEXT.__oslogstring: 0x2241
   __TEXT.__gcc_except_tab: 0x1514
   __TEXT.__dlopen_cstrs: 0x110
   __TEXT.__swift5_typeref: 0xc1

   __TEXT.__swift5_types: 0x8
   __TEXT.__swift_as_entry: 0x2c
   __TEXT.__swift_as_ret: 0x50
-  __TEXT.__unwind_info: 0x1510
-  __TEXT.__eh_frame: 0x558
+  __TEXT.__unwind_info: 0x1518
+  __TEXT.__eh_frame: 0x560
   __TEXT.__objc_classname: 0x3d6
-  __TEXT.__objc_methname: 0x9b1e
+  __TEXT.__objc_methname: 0x9c8f
   __TEXT.__objc_methtype: 0x14fe
-  __TEXT.__objc_stubs: 0x6e00
-  __DATA_CONST.__got: 0x418
-  __DATA_CONST.__const: 0xe80
+  __TEXT.__objc_stubs: 0x6f00
+  __DATA_CONST.__got: 0x430
+  __DATA_CONST.__const: 0xe60
   __DATA_CONST.__objc_classlist: 0x100
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x21b0
+  __DATA_CONST.__objc_selrefs: 0x21f0
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0xc0
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__auth_got: 0x718
+  __AUTH_CONST.__auth_got: 0x738
   __AUTH_CONST.__const: 0xc28
-  __AUTH_CONST.__cfstring: 0x3720
-  __AUTH_CONST.__objc_const: 0x8118
-  __AUTH_CONST.__objc_intobj: 0x90
+  __AUTH_CONST.__cfstring: 0x3820
+  __AUTH_CONST.__objc_const: 0x8148
+  __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH.__objc_data: 0xa00
-  __DATA.__objc_ivar: 0x340
+  __DATA.__objc_ivar: 0x344
   __DATA.__data: 0x620
   __DATA.__bss: 0x2d0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCryptoTokenKit.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 8892FAA7-C0BA-3501-A352-9F0B85C2DE7E
-  Functions: 2026
-  Symbols:   7155
-  CStrings:  3103
+  UUID: 889CD0B6-1DC4-32B8-B698-31A489350E01
+  Functions: 2040
+  Symbols:   7215
+  CStrings:  3134
 
Symbols:
+ -[POAgentAuthenticationProcess performLoginForCurrentUserWithPasswordContext:tokenId:forceLogin:]
+ -[POAgentAuthenticationProcess performLoginForCurrentUserWithPasswordContext:tokenId:forceLogin:].cold.1
+ -[POAgentAuthenticationProcess performLoginForCurrentUserWithPasswordContext:tokenId:forceLogin:].cold.2
+ -[POAgentAuthenticationProcess performLoginForCurrentUserWithPasswordContext:tokenId:forceLogin:].cold.3
+ -[POAgentAuthenticationProcess requestUserAuthenticationWithUserInfo:forceLogin:]
+ -[POAgentAuthenticationProcess requestUserAuthenticationWithUserInfo:forceLogin:].cold.1
+ -[POConfigurationManager enablePlatformSSORulesAndDefaultsIfNeeded:]
+ -[POConfigurationManager restorePlatformSSORulesAndDefaultsIfNeeded]
+ -[PODaemonConnection deviceConfigurationForIdentifier:completion:]
+ -[PODaemonConnection disablePlatformSSORulesAndDefaults:]
+ -[PODaemonConnection enablePlatformSSORulesAndDefaults:]
+ -[PODaemonConnection loginConfigurationForIdentifier:completion:]
+ -[PODaemonConnection removeDeviceConfigurationForIdentifier:completion:]
+ -[PODaemonConnection removeLoginConfigurationForIdentifier:completion:]
+ -[PODaemonConnection retrievePendingSSOTokenForIdentifier:completion:]
+ -[PODaemonConnection retrieveStashedDecryptionContextForIdentifier:completion:]
+ -[PODaemonConnection retrieveStashedSSOTokenForIdentifier:completion:]
+ -[PODaemonConnection saveDeviceConfiguration:identifier:completion:]
+ -[PODaemonConnection saveDeviceConfigurationSyncAllConfigToPreboot:identifier:completion:]
+ -[PODaemonConnection saveLoginConfiguration:identifier:completion:]
+ -[PODaemonConnection savePendingSSOTokens:identifier:completion:]
+ -[PODaemonConnection saveStashedDecryptionContext:identifier:completion:]
+ -[PODaemonConnection saveStashedSSOTokens:identifier:completion:]
+ -[PODaemonProcess _disableAccessKeyDefaults]
+ -[PODaemonProcess _disableAccessKeyDefaults].cold.1
+ -[PODaemonProcess _disableTemporarySessionDefaults]
+ -[PODaemonProcess _disableTemporarySessionDefaults].cold.1
+ -[PODaemonProcess _enableAccessKeyDefaults]
+ -[PODaemonProcess _enableAccessKeyDefaults].cold.1
+ -[PODaemonProcess _enableAccessKeyDefaults].cold.2
+ -[PODaemonProcess _enableAccessKeyDefaults].cold.3
+ -[PODaemonProcess _enableAccessKeyDefaults].cold.4
+ -[PODaemonProcess _enableTemporarySessionDefaults]
+ -[PODaemonProcess _enableTemporarySessionDefaults].cold.1
+ -[PODaemonProcess _enableTemporarySessionDefaults].cold.2
+ -[PODaemonProcess _enableTemporarySessionDefaults].cold.3
+ -[PODaemonProcess _enableTemporarySessionDefaults].cold.4
+ -[PODaemonProcess _removeDeviceConfigurationForIdentifier:syncToPreboot:error:]
+ -[PODaemonProcess _removeLoginConfigurationForIdentifier:syncToPreboot:error:]
+ -[PODaemonProcess _saveDeviceConfiguration:identifier:syncToPreboot:error:]
+ -[PODaemonProcess _saveDeviceConfiguration:identifier:syncToPreboot:error:].cold.1
+ -[PODaemonProcess _saveLoginConfiguration:identifier:syncToPreboot:error:]
+ -[PODaemonProcess _saveLoginConfiguration:identifier:syncToPreboot:error:].cold.1
+ -[PODaemonProcess disablePlatformSSORulesAndDefaults:]
+ -[PODaemonProcess disablePlatformSSORulesAndDefaults:].cold.1
+ -[PODaemonProcess enablePlatformSSORulesAndDefaults:]
+ -[PODaemonProcess enablePlatformSSORulesAndDefaults:].cold.1
+ -[PODaemonProcess removeDeviceConfigurationForIdentifier:completion:]
+ -[PODaemonProcess removeLoginConfigurationForIdentifier:completion:]
+ -[PODaemonProcess saveDeviceConfiguration:identifier:completion:]
+ -[PODaemonProcess saveDeviceConfigurationSyncAllConfigToPreboot:identifier:completion:]
+ -[PODaemonProcess saveLoginConfiguration:identifier:completion:]
+ -[POExtensionAgentProcess bundleIdentifierForXPCConnection:]
+ -[POExtensionAgentProcess bundleIdentifierForXPCConnection:].cold.1
+ -[POProfile setTemporarySessionQuickLogin:]
+ -[POProfile temporarySessionQuickLogin]
+ GCC_except_table60
+ _CFPreferencesCopyValue
+ _CFPreferencesSetValue
+ _CFPreferencesSynchronize
+ _OBJC_IVAR_$_POProfile._temporarySessionQuickLogin
+ ___43-[PODaemonProcess _enableAccessKeyDefaults]_block_invoke
+ ___43-[PODaemonProcess _enableAccessKeyDefaults]_block_invoke.cold.1
+ ___44-[PODaemonProcess _disableAccessKeyDefaults]_block_invoke
+ ___44-[PODaemonProcess _disableAccessKeyDefaults]_block_invoke.cold.1
+ ___50-[PODaemonProcess _enableTemporarySessionDefaults]_block_invoke
+ ___50-[PODaemonProcess _enableTemporarySessionDefaults]_block_invoke.cold.1
+ ___51-[PODaemonProcess _disableTemporarySessionDefaults]_block_invoke
+ ___51-[PODaemonProcess _disableTemporarySessionDefaults]_block_invoke.cold.1
+ ___53-[PODaemonProcess enablePlatformSSORulesAndDefaults:]_block_invoke
+ ___54-[PODaemonProcess disablePlatformSSORulesAndDefaults:]_block_invoke
+ ___54-[PODaemonProcess saveAppSSOConfiguration:completion:]_block_invoke.102
+ ___56-[PODaemonConnection enablePlatformSSORulesAndDefaults:]_block_invoke
+ ___56-[PODaemonConnection enablePlatformSSORulesAndDefaults:]_block_invoke.cold.1
+ ___57-[PODaemonConnection disablePlatformSSORulesAndDefaults:]_block_invoke
+ ___57-[PODaemonConnection disablePlatformSSORulesAndDefaults:]_block_invoke.cold.1
+ ___60-[POExtensionAgentProcess bundleIdentifierForXPCConnection:]_block_invoke
+ ___60-[POExtensionAgentProcess bundleIdentifierForXPCConnection:]_block_invoke.50
+ ___60-[POExtensionAgentProcess bundleIdentifierForXPCConnection:]_block_invoke.50.cold.1
+ ___60-[POExtensionAgentProcess bundleIdentifierForXPCConnection:]_block_invoke.cold.1
+ ___65-[PODaemonConnection loginConfigurationForIdentifier:completion:]_block_invoke
+ ___65-[PODaemonConnection loginConfigurationForIdentifier:completion:]_block_invoke.cold.1
+ ___65-[PODaemonConnection savePendingSSOTokens:identifier:completion:]_block_invoke
+ ___65-[PODaemonConnection savePendingSSOTokens:identifier:completion:]_block_invoke.cold.1
+ ___65-[PODaemonConnection saveStashedSSOTokens:identifier:completion:]_block_invoke
+ ___65-[PODaemonConnection saveStashedSSOTokens:identifier:completion:]_block_invoke.cold.1
+ ___66-[PODaemonConnection deviceConfigurationForIdentifier:completion:]_block_invoke
+ ___66-[PODaemonConnection deviceConfigurationForIdentifier:completion:]_block_invoke.cold.1
+ ___67-[PODaemonConnection saveLoginConfiguration:identifier:completion:]_block_invoke
+ ___67-[PODaemonConnection saveLoginConfiguration:identifier:completion:]_block_invoke.cold.1
+ ___68-[POConfigurationManager enablePlatformSSORulesAndDefaultsIfNeeded:]_block_invoke
+ ___68-[POConfigurationManager restorePlatformSSORulesAndDefaultsIfNeeded]_block_invoke
+ ___68-[PODaemonConnection saveDeviceConfiguration:identifier:completion:]_block_invoke
+ ___68-[PODaemonConnection saveDeviceConfiguration:identifier:completion:]_block_invoke.cold.1
+ ___70-[PODaemonConnection retrievePendingSSOTokenForIdentifier:completion:]_block_invoke
+ ___70-[PODaemonConnection retrievePendingSSOTokenForIdentifier:completion:]_block_invoke.cold.1
+ ___70-[PODaemonConnection retrieveStashedSSOTokenForIdentifier:completion:]_block_invoke
+ ___70-[PODaemonConnection retrieveStashedSSOTokenForIdentifier:completion:]_block_invoke.cold.1
+ ___71-[PODaemonConnection removeLoginConfigurationForIdentifier:completion:]_block_invoke
+ ___71-[PODaemonConnection removeLoginConfigurationForIdentifier:completion:]_block_invoke.cold.1
+ ___72-[PODaemonConnection removeDeviceConfigurationForIdentifier:completion:]_block_invoke
+ ___72-[PODaemonConnection removeDeviceConfigurationForIdentifier:completion:]_block_invoke.cold.1
+ ___73-[PODaemonConnection saveStashedDecryptionContext:identifier:completion:]_block_invoke
+ ___73-[PODaemonConnection saveStashedDecryptionContext:identifier:completion:]_block_invoke.cold.1
+ ___74-[PODaemonProcess _saveLoginConfiguration:identifier:syncToPreboot:error:]_block_invoke
+ ___74-[PODaemonProcess _saveLoginConfiguration:identifier:syncToPreboot:error:]_block_invoke.cold.1
+ ___75-[PODaemonProcess _saveDeviceConfiguration:identifier:syncToPreboot:error:]_block_invoke
+ ___75-[PODaemonProcess _saveDeviceConfiguration:identifier:syncToPreboot:error:]_block_invoke.cold.1
+ ___78-[PODaemonProcess _removeLoginConfigurationForIdentifier:syncToPreboot:error:]_block_invoke
+ ___78-[PODaemonProcess _removeLoginConfigurationForIdentifier:syncToPreboot:error:]_block_invoke.cold.1
+ ___79-[PODaemonConnection retrieveStashedDecryptionContextForIdentifier:completion:]_block_invoke
+ ___79-[PODaemonConnection retrieveStashedDecryptionContextForIdentifier:completion:]_block_invoke.cold.1
+ ___79-[PODaemonProcess _removeDeviceConfigurationForIdentifier:syncToPreboot:error:]_block_invoke
+ ___79-[PODaemonProcess _removeDeviceConfigurationForIdentifier:syncToPreboot:error:]_block_invoke.cold.1
+ ___81-[POAgentAuthenticationProcess requestUserAuthenticationWithUserInfo:forceLogin:]_block_invoke
+ ___90-[PODaemonConnection saveDeviceConfigurationSyncAllConfigToPreboot:identifier:completion:]_block_invoke
+ ___90-[PODaemonConnection saveDeviceConfigurationSyncAllConfigToPreboot:identifier:completion:]_block_invoke.cold.1
+ ___97-[POAgentAuthenticationProcess performLoginForCurrentUserWithPasswordContext:tokenId:forceLogin:]_block_invoke
+ ___97-[POAgentAuthenticationProcess performLoginForCurrentUserWithPasswordContext:tokenId:forceLogin:]_block_invoke.91
+ ___97-[POAgentAuthenticationProcess performLoginForCurrentUserWithPasswordContext:tokenId:forceLogin:]_block_invoke.91.cold.1
+ ___97-[POAgentAuthenticationProcess performLoginForCurrentUserWithPasswordContext:tokenId:forceLogin:]_block_invoke.95
+ ___97-[POAgentAuthenticationProcess performLoginForCurrentUserWithPasswordContext:tokenId:forceLogin:]_block_invoke.95.cold.1
+ ___97-[POAgentAuthenticationProcess performLoginForCurrentUserWithPasswordContext:tokenId:forceLogin:]_block_invoke.99
+ ___97-[POAgentAuthenticationProcess performLoginForCurrentUserWithPasswordContext:tokenId:forceLogin:]_block_invoke.99.cold.1
+ ___97-[POAgentAuthenticationProcess performLoginForCurrentUserWithPasswordContext:tokenId:forceLogin:]_block_invoke.cold.1
+ ___block_literal_global.287
+ ___block_literal_global.291
+ ___block_literal_global.844
+ ___block_literal_global.848
+ ___kCFBooleanFalse
+ _dispatch_time
+ _kCFPreferencesAnyUser
+ _kCFPreferencesCurrentHost
+ _kGroupDisplayNamesRequestTimeoutSeconds
+ _kProfilePictureRequestTimeoutSeconds
+ _objc_msgSend$_deviceConfigurationForIdentifier:
+ _objc_msgSend$_disableAccessKeyDefaults
+ _objc_msgSend$_disableTemporarySessionDefaults
+ _objc_msgSend$_enableAccessKeyDefaults
+ _objc_msgSend$_enableTemporarySessionDefaults
+ _objc_msgSend$_removeDeviceConfigurationForIdentifier:syncToPreboot:error:
+ _objc_msgSend$_removeLoginConfigurationForIdentifier:syncToPreboot:error:
+ _objc_msgSend$_saveDeviceConfiguration:identifier:syncToPreboot:error:
+ _objc_msgSend$_saveLoginConfiguration:identifier:syncToPreboot:error:
+ _objc_msgSend$bundleIdentifierForXPCConnection:
+ _objc_msgSend$createUserLoginTypes
+ _objc_msgSend$deviceConfigurationForIdentifier:completion:
+ _objc_msgSend$disablePlatformSSORulesAndDefaults:
+ _objc_msgSend$enablePlatformSSORulesAndDefaults:
+ _objc_msgSend$loginConfigurationForIdentifier:completion:
+ _objc_msgSend$performLoginForCurrentUserWithPasswordContext:tokenId:forceLogin:
+ _objc_msgSend$removeDeviceConfigurationForIdentifier:completion:
+ _objc_msgSend$removeLoginConfigurationForIdentifier:completion:
+ _objc_msgSend$requestUserAuthenticationWithUserInfo:forceLogin:
+ _objc_msgSend$retrievePendingSSOTokenForIdentifier:completion:
+ _objc_msgSend$retrieveStashedDecryptionContextForIdentifier:completion:
+ _objc_msgSend$retrieveStashedSSOTokenForIdentifier:completion:
+ _objc_msgSend$saveDeviceConfiguration:identifier:completion:
+ _objc_msgSend$saveDeviceConfigurationSyncAllConfigToPreboot:identifier:completion:
+ _objc_msgSend$saveLoginConfiguration:identifier:completion:
+ _objc_msgSend$savePendingSSOTokens:identifier:completion:
+ _objc_msgSend$saveStashedDecryptionContext:identifier:completion:
+ _objc_msgSend$saveStashedSSOTokens:identifier:completion:
+ _objc_msgSend$setTemporarySessionQuickLogin:
+ _objc_msgSend$supportsCreateTemporaryUsers
+ _objc_msgSend$temporarySessionQuickLogin
- -[POAgentAuthenticationProcess performLoginForCurrentUserWithPasswordContext:tokenId:]
- -[POAgentAuthenticationProcess performLoginForCurrentUserWithPasswordContext:tokenId:].cold.1
- -[POAgentAuthenticationProcess performLoginForCurrentUserWithPasswordContext:tokenId:].cold.2
- -[POAgentAuthenticationProcess performLoginForCurrentUserWithPasswordContext:tokenId:].cold.3
- -[POAgentAuthenticationProcess requestUserAuthenticationWithUserInfo:]
- -[POAgentAuthenticationProcess requestUserAuthenticationWithUserInfo:].cold.1
- -[POConfigurationManager enablePlatformSSORulesIfNeeded:]
- -[POConfigurationManager restorePlatformSSORulesIfNeeded]
- -[PODaemonConnection deviceConfigurationForIdentifer:completion:]
- -[PODaemonConnection disablePlatformSSORules:]
- -[PODaemonConnection enablePlatformSSORules:]
- -[PODaemonConnection loginConfigurationForIdentifer:completion:]
- -[PODaemonConnection removeDeviceConfigurationForIdentifer:completion:]
- -[PODaemonConnection removeLoginConfigurationForIdentifer:completion:]
- -[PODaemonConnection retrievePendingSSOTokenForIdentifer:completion:]
- -[PODaemonConnection retrieveStashedDecryptionContextForIdentifer:completion:]
- -[PODaemonConnection retrieveStashedSSOTokenForIdentifer:completion:]
- -[PODaemonConnection saveDeviceConfiguration:identifer:completion:]
- -[PODaemonConnection saveDeviceConfigurationSyncAllConfigToPreboot:identifer:completion:]
- -[PODaemonConnection saveLoginConfiguration:identifer:completion:]
- -[PODaemonConnection savePendingSSOTokens:identifer:completion:]
- -[PODaemonConnection saveStashedDecryptionContext:identifer:completion:]
- -[PODaemonConnection saveStashedSSOTokens:identifer:completion:]
- -[PODaemonProcess _removeDeviceConfigurationForIdentifer:syncToPreboot:error:]
- -[PODaemonProcess _removeLoginConfigurationForIdentifer:syncToPreboot:error:]
- -[PODaemonProcess _saveDeviceConfiguration:identifer:syncToPreboot:error:]
- -[PODaemonProcess _saveDeviceConfiguration:identifer:syncToPreboot:error:].cold.1
- -[PODaemonProcess _saveLoginConfiguration:identifer:syncToPreboot:error:]
- -[PODaemonProcess _saveLoginConfiguration:identifer:syncToPreboot:error:].cold.1
- -[PODaemonProcess disablePlatformSSORules:]
- -[PODaemonProcess disablePlatformSSORules:].cold.1
- -[PODaemonProcess enablePlatformSSORules:]
- -[PODaemonProcess enablePlatformSSORules:].cold.1
- -[PODaemonProcess removeDeviceConfigurationForIdentifer:completion:]
- -[PODaemonProcess removeLoginConfigurationForIdentifer:completion:]
- -[PODaemonProcess saveDeviceConfiguration:identifer:completion:]
- -[PODaemonProcess saveDeviceConfigurationSyncAllConfigToPreboot:identifer:completion:]
- -[PODaemonProcess saveLoginConfiguration:identifer:completion:]
- -[POExtensionAgentProcess bundleIdentiferForXPCConnection:]
- -[POExtensionAgentProcess bundleIdentiferForXPCConnection:].cold.1
- GCC_except_table57
- ___42-[PODaemonProcess enablePlatformSSORules:]_block_invoke
- ___43-[PODaemonProcess disablePlatformSSORules:]_block_invoke
- ___45-[PODaemonConnection enablePlatformSSORules:]_block_invoke
- ___45-[PODaemonConnection enablePlatformSSORules:]_block_invoke.cold.1
- ___46-[PODaemonConnection disablePlatformSSORules:]_block_invoke
- ___46-[PODaemonConnection disablePlatformSSORules:]_block_invoke.cold.1
- ___54-[PODaemonProcess saveAppSSOConfiguration:completion:]_block_invoke.70
- ___57-[POConfigurationManager enablePlatformSSORulesIfNeeded:]_block_invoke
- ___57-[POConfigurationManager restorePlatformSSORulesIfNeeded]_block_invoke
- ___59-[POExtensionAgentProcess bundleIdentiferForXPCConnection:]_block_invoke
- ___59-[POExtensionAgentProcess bundleIdentiferForXPCConnection:]_block_invoke.50
- ___59-[POExtensionAgentProcess bundleIdentiferForXPCConnection:]_block_invoke.50.cold.1
- ___59-[POExtensionAgentProcess bundleIdentiferForXPCConnection:]_block_invoke.cold.1
- ___64-[PODaemonConnection loginConfigurationForIdentifer:completion:]_block_invoke
- ___64-[PODaemonConnection loginConfigurationForIdentifer:completion:]_block_invoke.cold.1
- ___64-[PODaemonConnection savePendingSSOTokens:identifer:completion:]_block_invoke
- ___64-[PODaemonConnection savePendingSSOTokens:identifer:completion:]_block_invoke.cold.1
- ___64-[PODaemonConnection saveStashedSSOTokens:identifer:completion:]_block_invoke
- ___64-[PODaemonConnection saveStashedSSOTokens:identifer:completion:]_block_invoke.cold.1
- ___65-[PODaemonConnection deviceConfigurationForIdentifer:completion:]_block_invoke
- ___65-[PODaemonConnection deviceConfigurationForIdentifer:completion:]_block_invoke.cold.1
- ___66-[PODaemonConnection saveLoginConfiguration:identifer:completion:]_block_invoke
- ___66-[PODaemonConnection saveLoginConfiguration:identifer:completion:]_block_invoke.cold.1
- ___67-[PODaemonConnection saveDeviceConfiguration:identifer:completion:]_block_invoke
- ___67-[PODaemonConnection saveDeviceConfiguration:identifer:completion:]_block_invoke.cold.1
- ___69-[PODaemonConnection retrievePendingSSOTokenForIdentifer:completion:]_block_invoke
- ___69-[PODaemonConnection retrievePendingSSOTokenForIdentifer:completion:]_block_invoke.cold.1
- ___69-[PODaemonConnection retrieveStashedSSOTokenForIdentifer:completion:]_block_invoke
- ___69-[PODaemonConnection retrieveStashedSSOTokenForIdentifer:completion:]_block_invoke.cold.1
- ___70-[POAgentAuthenticationProcess requestUserAuthenticationWithUserInfo:]_block_invoke
- ___70-[PODaemonConnection removeLoginConfigurationForIdentifer:completion:]_block_invoke
- ___70-[PODaemonConnection removeLoginConfigurationForIdentifer:completion:]_block_invoke.cold.1
- ___71-[PODaemonConnection removeDeviceConfigurationForIdentifer:completion:]_block_invoke
- ___71-[PODaemonConnection removeDeviceConfigurationForIdentifer:completion:]_block_invoke.cold.1
- ___72-[PODaemonConnection saveStashedDecryptionContext:identifer:completion:]_block_invoke
- ___72-[PODaemonConnection saveStashedDecryptionContext:identifer:completion:]_block_invoke.cold.1
- ___73-[PODaemonProcess _saveLoginConfiguration:identifer:syncToPreboot:error:]_block_invoke
- ___73-[PODaemonProcess _saveLoginConfiguration:identifer:syncToPreboot:error:]_block_invoke.cold.1
- ___74-[PODaemonProcess _saveDeviceConfiguration:identifer:syncToPreboot:error:]_block_invoke
- ___74-[PODaemonProcess _saveDeviceConfiguration:identifer:syncToPreboot:error:]_block_invoke.cold.1
- ___77-[PODaemonProcess _removeLoginConfigurationForIdentifer:syncToPreboot:error:]_block_invoke
- ___77-[PODaemonProcess _removeLoginConfigurationForIdentifer:syncToPreboot:error:]_block_invoke.cold.1
- ___78-[PODaemonConnection retrieveStashedDecryptionContextForIdentifer:completion:]_block_invoke
- ___78-[PODaemonConnection retrieveStashedDecryptionContextForIdentifer:completion:]_block_invoke.cold.1
- ___78-[PODaemonProcess _removeDeviceConfigurationForIdentifer:syncToPreboot:error:]_block_invoke
- ___78-[PODaemonProcess _removeDeviceConfigurationForIdentifer:syncToPreboot:error:]_block_invoke.cold.1
- ___86-[POAgentAuthenticationProcess performLoginForCurrentUserWithPasswordContext:tokenId:]_block_invoke
- ___86-[POAgentAuthenticationProcess performLoginForCurrentUserWithPasswordContext:tokenId:]_block_invoke.91
- ___86-[POAgentAuthenticationProcess performLoginForCurrentUserWithPasswordContext:tokenId:]_block_invoke.91.cold.1
- ___86-[POAgentAuthenticationProcess performLoginForCurrentUserWithPasswordContext:tokenId:]_block_invoke.95
- ___86-[POAgentAuthenticationProcess performLoginForCurrentUserWithPasswordContext:tokenId:]_block_invoke.95.cold.1
- ___86-[POAgentAuthenticationProcess performLoginForCurrentUserWithPasswordContext:tokenId:]_block_invoke.99
- ___86-[POAgentAuthenticationProcess performLoginForCurrentUserWithPasswordContext:tokenId:]_block_invoke.99.cold.1
- ___86-[POAgentAuthenticationProcess performLoginForCurrentUserWithPasswordContext:tokenId:]_block_invoke.cold.1
- ___89-[PODaemonConnection saveDeviceConfigurationSyncAllConfigToPreboot:identifer:completion:]_block_invoke
- ___89-[PODaemonConnection saveDeviceConfigurationSyncAllConfigToPreboot:identifer:completion:]_block_invoke.cold.1
- ___block_literal_global.253
- ___block_literal_global.279
- ___block_literal_global.843
- ___block_literal_global.847
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swiftDarwin_$_PlatformSSO
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_PlatformSSO
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_PlatformSSO
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_PlatformSSO
- _objc_msgSend$_deviceConfigurationForIdentifer:
- _objc_msgSend$_removeDeviceConfigurationForIdentifer:syncToPreboot:error:
- _objc_msgSend$_removeLoginConfigurationForIdentifer:syncToPreboot:error:
- _objc_msgSend$_saveDeviceConfiguration:identifer:syncToPreboot:error:
- _objc_msgSend$_saveLoginConfiguration:identifer:syncToPreboot:error:
- _objc_msgSend$bundleIdentiferForXPCConnection:
- _objc_msgSend$deviceConfigurationForIdentifer:completion:
- _objc_msgSend$disablePlatformSSORules:
- _objc_msgSend$enablePlatformSSORules:
- _objc_msgSend$loginConfigurationForIdentifer:completion:
- _objc_msgSend$performLoginForCurrentUserWithPasswordContext:tokenId:
- _objc_msgSend$removeDeviceConfigurationForIdentifer:completion:
- _objc_msgSend$removeLoginConfigurationForIdentifer:completion:
- _objc_msgSend$requestUserAuthenticationWithUserInfo:
- _objc_msgSend$retrievePendingSSOTokenForIdentifer:completion:
- _objc_msgSend$retrieveStashedDecryptionContextForIdentifer:completion:
- _objc_msgSend$retrieveStashedSSOTokenForIdentifer:completion:
- _objc_msgSend$saveDeviceConfiguration:identifer:completion:
- _objc_msgSend$saveDeviceConfigurationSyncAllConfigToPreboot:identifer:completion:
- _objc_msgSend$saveLoginConfiguration:identifer:completion:
- _objc_msgSend$savePendingSSOTokens:identifer:completion:
- _objc_msgSend$saveStashedDecryptionContext:identifer:completion:
- _objc_msgSend$saveStashedSSOTokens:identifer:completion:
CStrings:
+ "-[POAgentAuthenticationProcess performLoginForCurrentUserWithPasswordContext:tokenId:forceLogin:]"
+ "-[POAgentAuthenticationProcess requestUserAuthenticationWithUserInfo:forceLogin:]"
+ "-[PODaemonProcess _removeDeviceConfigurationForIdentifier:syncToPreboot:error:]"
+ "-[PODaemonProcess _removeLoginConfigurationForIdentifier:syncToPreboot:error:]"
+ "-[PODaemonProcess _saveDeviceConfiguration:identifier:syncToPreboot:error:]"
+ "-[PODaemonProcess _saveLoginConfiguration:identifier:syncToPreboot:error:]"
+ "-[PODaemonProcess removeDeviceConfigurationForIdentifier:completion:]"
+ "-[PODaemonProcess removeLoginConfigurationForIdentifier:completion:]"
+ "-[PODaemonProcess saveDeviceConfiguration:identifier:completion:]"
+ "-[PODaemonProcess saveDeviceConfigurationSyncAllConfigToPreboot:identifier:completion:]"
+ "-[PODaemonProcess saveLoginConfiguration:identifier:completion:]"
+ "Failed to create key during user registration because touchID or watch is not available."
+ "Failed to synchronize defaults"
+ "Not configured for Access Key"
+ "Not configured for temporary session"
+ "PreloadedTokens"
+ "QuickLogin"
+ "Resetting SmartCard defaults"
+ "Resetting session logout defaults"
+ "TB,V_temporarySessionQuickLogin"
+ "TemporarySessionQuickLogin"
+ "Update login rules and defaults"
+ "Updating SmartCard defaults"
+ "Updating session logout defaults"
+ "UserPairing"
+ "_deviceConfigurationForIdentifier:"
+ "_disableAccessKeyDefaults"
+ "_disableTemporarySessionDefaults"
+ "_enableAccessKeyDefaults"
+ "_enableTemporarySessionDefaults"
+ "_removeDeviceConfigurationForIdentifier:syncToPreboot:error:"
+ "_removeLoginConfigurationForIdentifier:syncToPreboot:error:"
+ "_saveDeviceConfiguration:identifier:syncToPreboot:error:"
+ "_saveLoginConfiguration:identifier:syncToPreboot:error:"
+ "_temporarySessionQuickLogin"
+ "bundleIdentifierForXPCConnection:"
+ "com.apple.PlatformSSO.AccessKey"
+ "com.apple.security.smartcard"
+ "com.apple.sessionlogoutd"
+ "createUserLoginTypes"
+ "deviceConfigurationForIdentifier:completion:"
+ "disablePlatformSSORulesAndDefaults:"
+ "enablePlatformSSORulesAndDefaults:"
+ "enablePlatformSSORulesAndDefaultsIfNeeded:"
+ "loginConfigurationForIdentifier:completion:"
+ "performLoginForCurrentUserWithPasswordContext:tokenId:forceLogin:"
+ "removeDeviceConfigurationForIdentifier:completion:"
+ "removeLoginConfigurationForIdentifier:completion:"
+ "requestUserAuthenticationWithUserInfo:forceLogin:"
+ "restorePlatformSSORulesAndDefaultsIfNeeded"
+ "retrievePendingSSOTokenForIdentifier:completion:"
+ "retrieveStashedDecryptionContextForIdentifier:completion:"
+ "retrieveStashedSSOTokenForIdentifier:completion:"
+ "saveDeviceConfiguration:identifier:completion:"
+ "saveDeviceConfigurationSyncAllConfigToPreboot:identifier:completion:"
+ "saveLoginConfiguration:identifier:completion:"
+ "savePendingSSOTokens:identifier:completion:"
+ "saveStashedDecryptionContext:identifier:completion:"
+ "saveStashedSSOTokens:identifier:completion:"
+ "setTemporarySessionQuickLogin:"
+ "supportsCreateTemporaryUsers"
+ "temporarySessionQuickLogin"
- "%s identifer = %{public}@ on %@"
- "-[POAgentAuthenticationProcess performLoginForCurrentUserWithPasswordContext:tokenId:]"
- "-[POAgentAuthenticationProcess requestUserAuthenticationWithUserInfo:]"
- "-[PODaemonProcess _removeDeviceConfigurationForIdentifer:syncToPreboot:error:]"
- "-[PODaemonProcess _removeLoginConfigurationForIdentifer:syncToPreboot:error:]"
- "-[PODaemonProcess _saveDeviceConfiguration:identifer:syncToPreboot:error:]"
- "-[PODaemonProcess _saveLoginConfiguration:identifer:syncToPreboot:error:]"
- "-[PODaemonProcess removeDeviceConfigurationForIdentifer:completion:]"
- "-[PODaemonProcess removeLoginConfigurationForIdentifer:completion:]"
- "-[PODaemonProcess saveDeviceConfiguration:identifer:completion:]"
- "-[PODaemonProcess saveDeviceConfigurationSyncAllConfigToPreboot:identifer:completion:]"
- "-[PODaemonProcess saveLoginConfiguration:identifer:completion:]"
- "Failed to create key durng user user registration because touchID or watch is not available."
- "Update login rules"
- "_deviceConfigurationForIdentifer:"
- "_removeDeviceConfigurationForIdentifer:syncToPreboot:error:"
- "_removeLoginConfigurationForIdentifer:syncToPreboot:error:"
- "_saveDeviceConfiguration:identifer:syncToPreboot:error:"
- "_saveLoginConfiguration:identifer:syncToPreboot:error:"
- "bundleIdentiferForXPCConnection:"
- "deviceConfigurationForIdentifer:completion:"
- "disablePlatformSSORules:"
- "enablePlatformSSORules:"
- "enablePlatformSSORulesIfNeeded:"
- "loginConfigurationForIdentifer:completion:"
- "performLoginForCurrentUserWithPasswordContext:tokenId:"
- "removeDeviceConfigurationForIdentifer:completion:"
- "removeLoginConfigurationForIdentifer:completion:"
- "requestUserAuthenticationWithUserInfo:"
- "restorePlatformSSORulesIfNeeded"
- "retrievePendingSSOTokenForIdentifer:completion:"
- "retrieveStashedDecryptionContextForIdentifer:completion:"
- "retrieveStashedSSOTokenForIdentifer:completion:"
- "saveDeviceConfiguration:identifer:completion:"
- "saveDeviceConfigurationSyncAllConfigToPreboot:identifer:completion:"
- "saveLoginConfiguration:identifer:completion:"
- "savePendingSSOTokens:identifer:completion:"
- "saveStashedDecryptionContext:identifer:completion:"
- "saveStashedSSOTokens:identifer:completion:"

```
