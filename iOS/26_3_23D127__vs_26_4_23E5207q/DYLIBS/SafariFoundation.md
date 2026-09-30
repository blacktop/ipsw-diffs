## SafariFoundation

> `/System/Library/PrivateFrameworks/SafariFoundation.framework/SafariFoundation`

```diff

-623.2.7.10.4
-  __TEXT.__text: 0x2aaa4
-  __TEXT.__auth_stubs: 0xa90
-  __TEXT.__objc_methlist: 0x1ffc
-  __TEXT.__cstring: 0x2c3c
+624.1.11.10.3
+  __TEXT.__text: 0x2bb34
+  __TEXT.__auth_stubs: 0x9f0
+  __TEXT.__objc_methlist: 0x2014
+  __TEXT.__cstring: 0x2887
   __TEXT.__const: 0x21c
-  __TEXT.__gcc_except_tab: 0x1358
+  __TEXT.__gcc_except_tab: 0x1338
   __TEXT.__oslogstring: 0x115a
   __TEXT.__dlopen_cstrs: 0x203
   __TEXT.__ustring: 0x224

   __TEXT.__swift5_capture: 0x128
   __TEXT.__swift_as_entry: 0x2c
   __TEXT.__swift_as_ret: 0x2c
-  __TEXT.__unwind_info: 0x1078
+  __TEXT.__unwind_info: 0x10a8
   __TEXT.__eh_frame: 0x518
-  __TEXT.__objc_classname: 0x4b1
-  __TEXT.__objc_methname: 0x7ed0
-  __TEXT.__objc_methtype: 0xbf9
-  __TEXT.__objc_stubs: 0x4c60
-  __DATA_CONST.__got: 0x4d8
-  __DATA_CONST.__const: 0x1400
+  __TEXT.__objc_classname: 0x527
+  __TEXT.__objc_methname: 0x80a2
+  __TEXT.__objc_methtype: 0xdc1
+  __TEXT.__objc_stubs: 0x4ee0
+  __DATA_CONST.__got: 0x4d0
+  __DATA_CONST.__const: 0x1428
   __DATA_CONST.__objc_classlist: 0x118
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x18a8
+  __DATA_CONST.__objc_selrefs: 0x18b8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0xb0
   __DATA_CONST.__objc_arraydata: 0x110
-  __AUTH_CONST.__auth_got: 0x560
+  __AUTH_CONST.__auth_got: 0x510
   __AUTH_CONST.__const: 0x730
-  __AUTH_CONST.__cfstring: 0x1de0
-  __AUTH_CONST.__objc_const: 0x33f0
+  __AUTH_CONST.__cfstring: 0x1e20
+  __AUTH_CONST.__objc_const: 0x3420
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH.__objc_data: 0x1f0
   __AUTH.__data: 0x78
-  __DATA.__objc_ivar: 0x1c8
+  __DATA.__objc_ivar: 0x1d0
   __DATA.__data: 0x480
-  __DATA.__bss: 0x90
+  __DATA.__bss: 0x88
   __DATA_DIRTY.__objc_data: 0x960
-  __DATA_DIRTY.__bss: 0xb8
+  __DATA_DIRTY.__bss: 0xc0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: BEEDD266-BC16-324A-927F-A39CF6ACB669
-  Functions: 1068
-  Symbols:   3612
-  CStrings:  1842
+  UUID: E30BA406-3B45-34CD-8D5E-BBA4350765D0
+  Functions: 1077
+  Symbols:   3665
+  CStrings:  1835
 
Symbols:
+ +[SFSafariCredentialStore _fetchPasswordCredentialIdentitiesMatchingDomains:withProxy:completion:]
+ +[SFSafariCredentialStore _isEnabledCredentialProviderAppID:enabledExtensions:]
+ -[SFAppAutoFillOneTimeCodeProvider _oneTimeCodesFromSavedAccounts:context:]
+ -[SFAppAutoFillOneTimeCodeProvider _oneTimeCodesSortedByLastedUsedDateOfSavedAccount:]
+ -[SFAutoFillFeatureManager test_overrideShouldAutoFillPasswords:]
+ -[SFSuggestedUserProvider _userNameFromSavedAccount:]
+ GCC_except_table127
+ GCC_except_table53
+ _OBJC_IVAR_$_SFAutoFillFeatureManager._overrideShouldAutoFillPasswordsValue
+ _OBJC_IVAR_$_SFAutoFillFeatureManager._shouldOverrideShouldAutoFillPasswords
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_6
+ ___114-[SFAppAutoFillOneTimeCodeProvider currentOneTimeCodesWithAppIdentifier:website:usernameHint:fieldClassification:]_block_invoke.59
+ ___75-[SFAppAutoFillOneTimeCodeProvider _oneTimeCodesFromSavedAccounts:context:]_block_invoke
+ ___75-[SFAppAutoFillOneTimeCodeProvider _oneTimeCodesFromSavedAccounts:context:]_block_invoke_2
+ ___86-[SFAppAutoFillOneTimeCodeProvider _oneTimeCodesSortedByLastedUsedDateOfSavedAccount:]_block_invoke
+ ___block_descriptor_40_e8_32s_e62_"NSMutableOrderedSet"24?0"WBSPair"8"NSMutableOrderedSet"16ls32l8
+ ___block_descriptor_40_e8_32w_e17_v16?0"NSTimer"8lw32l8
+ ___block_descriptor_48_e8_32s40s_e47_"SFSuggestedUser"16?0"WBSSavedAccountMatch"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40w_e5_v8?0lw40l8s32l8
+ ___block_descriptor_56_e8_32s40s48r_e36_v16?0"WBSSavedAccountMatchResult"8lr48l8s32l8s40l8
+ ___block_literal_global.113
+ ___block_literal_global.169
+ ___block_literal_global.174
+ ___block_literal_global.176
+ ___block_literal_global.178
+ ___block_literal_global.180
+ ___block_literal_global.74
+ ___block_literal_global.80
+ ___block_literal_global.82
+ ___block_literal_global.93
+ _objc_msgSend$_fetchPasswordCredentialIdentitiesMatchingDomains:withProxy:completion:
+ _objc_msgSend$_isEnabledCredentialProviderAppID:enabledExtensions:
+ _objc_msgSend$_oneTimeCodesFromSavedAccounts:context:
+ _objc_msgSend$_oneTimeCodesSortedByLastedUsedDateOfSavedAccount:
+ _objc_msgSend$_userNameFromSavedAccount:
+ _objc_msgSend$deleteRecoveryKeyForVolumeID:serialNumber:completion:
+ _objc_msgSend$deviceModel
+ _objc_msgSend$deviceVariant
+ _objc_msgSend$init
+ _objc_msgSend$initWithVolumeID:serialNumber:recoveryKey:displayName:
+ _objc_msgSend$initWithVolumeID:serialNumber:recoveryKey:displayName:creationDate:
+ _objc_msgSend$isSavedInPasswordsApp
+ _objc_msgSend$isSharedInGroup
+ _objc_msgSend$localizedStringWithFormat:
+ _objc_msgSend$recoveryKey
+ _objc_msgSend$recoveryKeyForVolumeID:serialNumber:completion:
+ _objc_msgSend$recoveryKeysForSerialNumber:completion:
+ _objc_msgSend$saveRecoveryKeyWithRequest:completion:
+ _objc_msgSend$serialNumber
+ _objc_msgSend$setDeviceModel:
+ _objc_msgSend$setDeviceVariant:
+ _objc_msgSend$setIsSavedInPasswordsApp:
+ _objc_msgSend$setIsSharedInGroup:
+ _objc_msgSend$volumeID
- +[SFAppAutoFillOneTimeCodeProvider setUseUserNotificationsOneTimeCodeSupport:]
- +[SFAppAutoFillOneTimeCodeProvider useUserNotificationsOneTimeCodeSupport]
- +[SFSafariCredentialStore isAppEligibleForSavingPasswords:isEnabledAsCredentialProvider:]
- -[SFAppAutoFillOneTimeCodeProvider _sortedOneTimeCodesFromSavedAccounts:context:]
- GCC_except_table126
- _WBSUseUserNotificationsOneTimeCodeSupportKey
- ___114-[SFAppAutoFillOneTimeCodeProvider currentOneTimeCodesWithAppIdentifier:website:usernameHint:fieldClassification:]_block_invoke.58
- ___61-[SFAppAutoFillOneTimeCodeProvider consumeCurrentOneTimeCode]_block_invoke_2
- ___81-[SFAppAutoFillOneTimeCodeProvider _sortedOneTimeCodesFromSavedAccounts:context:]_block_invoke
- ___81-[SFAppAutoFillOneTimeCodeProvider _sortedOneTimeCodesFromSavedAccounts:context:]_block_invoke_2
- ___81-[SFAppAutoFillOneTimeCodeProvider _sortedOneTimeCodesFromSavedAccounts:context:]_block_invoke_3
- ___block_descriptor_40_e8_32s_e17_v16?0"NSTimer"8ls32l8
- ___block_descriptor_40_e8_32s_e47_"SFSuggestedUser"16?0"WBSSavedAccountMatch"8ls32l8
- ___block_descriptor_40_e8_32s_e48_"NSMutableSet"24?0"WBSPair"8"NSMutableSet"16ls32l8
- ___block_descriptor_40_e8_32s_e48_v32?0"NSNumber"8"SFAutoFillOneTimeCode"16^B24ls32l8
- ___block_literal_global.111
- ___block_literal_global.166
- ___block_literal_global.168
- ___block_literal_global.170
- ___block_literal_global.175
- ___block_literal_global.177
- ___block_literal_global.71
- ___block_literal_global.79
- ___block_literal_global.81
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$_sortedOneTimeCodesFromSavedAccounts:context:
- _objc_msgSend$enumerateKeysAndObjectsUsingBlock:
- _objc_msgSend$isAppEligibleForSavingPasswords:isEnabledAsCredentialProvider:
- _objc_msgSend$useUserNotificationsOneTimeCodeSupport
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x10
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x6
- _objc_retain_x7
- _objc_retain_x9
CStrings:
+ "@\"NSMutableOrderedSet\"24@?0@\"WBSPair\"8@\"NSMutableOrderedSet\"16"
+ "REVIEWERS"
+ "_fetchPasswordCredentialIdentitiesMatchingDomains:withProxy:completion:"
+ "_isEnabledCredentialProviderAppID:enabledExtensions:"
+ "_oneTimeCodesFromSavedAccounts:context:"
+ "_oneTimeCodesSortedByLastedUsedDateOfSavedAccount:"
+ "_overrideShouldAutoFillPasswordsValue"
+ "_shouldOverrideShouldAutoFillPasswords"
+ "_userNameFromSavedAccount:"
+ "com.apple.AppleIDSetupUIService"
+ "localizedStringWithFormat:"
+ "test_overrideShouldAutoFillPasswords:"
- "@\"NSMutableSet\"24@?0@\"WBSPair\"8@\"NSMutableSet\"16"
- "_sortedOneTimeCodesFromSavedAccounts:context:"
- "enumerateKeysAndObjectsUsingBlock:"
- "isAppEligibleForSavingPasswords:isEnabledAsCredentialProvider:"
- "setUseUserNotificationsOneTimeCodeSupport:"
- "useUserNotificationsOneTimeCodeSupport"
- "v32@?0@\"NSNumber\"8@\"SFAutoFillOneTimeCode\"16^B24"

```
