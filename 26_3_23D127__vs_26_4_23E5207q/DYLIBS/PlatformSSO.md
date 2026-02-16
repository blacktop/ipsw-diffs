## PlatformSSO

> `/System/Library/PrivateFrameworks/PlatformSSO.framework/PlatformSSO`

```diff

-483.80.8.0.0
-  __TEXT.__text: 0x598e4
-  __TEXT.__auth_stubs: 0xe90
-  __TEXT.__objc_methlist: 0x33a4
-  __TEXT.__const: 0x2c8
-  __TEXT.__cstring: 0x8126
-  __TEXT.__oslogstring: 0x22c1
-  __TEXT.__gcc_except_tab: 0x1534
+483.100.68.0.0
+  __TEXT.__text: 0x5b8f0
+  __TEXT.__auth_stubs: 0xe00
+  __TEXT.__objc_methlist: 0x3314
+  __TEXT.__const: 0x2e2
+  __TEXT.__cstring: 0x7e76
+  __TEXT.__oslogstring: 0x2271
+  __TEXT.__gcc_except_tab: 0x1520
   __TEXT.__dlopen_cstrs: 0x110
   __TEXT.__swift5_typeref: 0xc2
   __TEXT.__swift5_capture: 0x118

   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_reflstr: 0x9
   __TEXT.__swift5_assocty: 0x18
-  __TEXT.__swift5_proto: 0x4
+  __TEXT.__swift5_proto: 0x8
   __TEXT.__swift5_types: 0x8
   __TEXT.__swift_as_entry: 0x2c
   __TEXT.__swift_as_ret: 0x50
-  __TEXT.__unwind_info: 0x1530
-  __TEXT.__eh_frame: 0x560
-  __TEXT.__objc_classname: 0x3df
-  __TEXT.__objc_methname: 0x9f69
-  __TEXT.__objc_methtype: 0x151a
-  __TEXT.__objc_stubs: 0x6f60
-  __DATA_CONST.__got: 0x438
-  __DATA_CONST.__const: 0xea8
+  __TEXT.__unwind_info: 0x1448
+  __TEXT.__eh_frame: 0x600
+  __TEXT.__objc_classname: 0x3e5
+  __TEXT.__objc_methname: 0x9d6e
+  __TEXT.__objc_methtype: 0x1548
+  __TEXT.__objc_stubs: 0x7140
+  __DATA_CONST.__got: 0x428
+  __DATA_CONST.__const: 0xea0
   __DATA_CONST.__objc_classlist: 0x108
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2258
+  __DATA_CONST.__objc_selrefs: 0x21f0
   __DATA_CONST.__objc_protorefs: 0x30
-  __DATA_CONST.__objc_superrefs: 0xc0
+  __DATA_CONST.__objc_superrefs: 0xc8
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__auth_got: 0x758
-  __AUTH_CONST.__const: 0xc28
-  __AUTH_CONST.__cfstring: 0x38c0
-  __AUTH_CONST.__objc_const: 0x83f0
-  __AUTH_CONST.__objc_intobj: 0xa8
+  __AUTH_CONST.__auth_got: 0x710
+  __AUTH_CONST.__const: 0xc08
+  __AUTH_CONST.__cfstring: 0x37e0
+  __AUTH_CONST.__objc_const: 0x83a0
+  __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH.__objc_data: 0xa00
   __DATA.__objc_ivar: 0x368
   __DATA.__data: 0x620
-  __DATA.__bss: 0x2e0
+  __DATA.__bss: 0x340
   __DATA_DIRTY.__objc_data: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /System/Library/PrivateFrameworks/UserManagement.framework/UserManagement
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 7680CBA2-D09F-3FE6-BE87-DD83A46CC6FB
-  Functions: 2072
-  Symbols:   7319
-  CStrings:  3178
+  UUID: FC3EB1EA-4E75-31D7-B193-433D271669D1
+  Functions: 2062
+  Symbols:   7321
+  CStrings:  3140
 
Symbols:
+ -[POConfigurationManager saveCurrentUserConfiguration]
+ -[POConfigurationManager saveUserConfiguration:forUserName:]
+ -[POConfigurationManager saveUserConfiguration:forUserName:].cold.1
+ -[PODaemonConnection saveUserConfiguration:forIdentifier:completion:]
+ -[PODaemonConnection saveUserConfigurationData:forIdentifier:completion:]
+ -[PODaemonProcess _removeDeviceConfigurationForIdentifier:error:]
+ -[PODaemonProcess _removeLoginConfigurationForIdentifier:error:]
+ -[PODaemonProcess _removeUserConfigurationForIdentifier:error:]
+ -[PODaemonProcess _saveDeviceConfiguration:identifier:error:]
+ -[PODaemonProcess _saveDeviceConfiguration:identifier:error:].cold.1
+ -[PODaemonProcess _saveLoginConfiguration:identifier:error:]
+ -[PODaemonProcess _saveLoginConfiguration:identifier:error:].cold.1
+ -[PODaemonProcess _saveUserConfigurationData:forIdentifier:error:]
+ -[PODaemonProcess _saveUserConfigurationData:forIdentifier:error:].cold.1
+ -[PODaemonProcess saveUserConfiguration:forIdentifier:completion:]
+ -[PODaemonProcess saveUserConfigurationData:forIdentifier:completion:]
+ GCC_except_table47
+ GCC_except_table56
+ GCC_except_table59
+ GCC_except_table88
+ _OBJC_METACLASS_$_POCoreConfigurationUtil
+ _OUTLINED_FUNCTION_13
+ _OUTLINED_FUNCTION_14
+ _OUTLINED_FUNCTION_15
+ ___39-[PODaemonConnection _connectToService]_block_invoke.95
+ ___39-[PODaemonConnection _connectToService]_block_invoke.95.cold.1
+ ___54-[POConfigurationManager saveCurrentUserConfiguration]_block_invoke
+ ___54-[POConfigurationManager saveCurrentUserConfiguration]_block_invoke.cold.1
+ ___54-[PODaemonProcess saveAppSSOConfiguration:completion:]_block_invoke.97
+ ___55-[POConfigurationManager userConfigurationForUserName:]_block_invoke.131
+ ___60-[POConfigurationManager saveUserConfiguration:forUserName:]_block_invoke
+ ___60-[POConfigurationManager saveUserConfiguration:forUserName:]_block_invoke.139
+ ___60-[POConfigurationManager saveUserConfiguration:forUserName:]_block_invoke.cold.1
+ ___60-[PODaemonProcess _saveLoginConfiguration:identifier:error:]_block_invoke
+ ___60-[PODaemonProcess _saveLoginConfiguration:identifier:error:]_block_invoke.cold.1
+ ___61-[POConfigurationManager removeUserConfigurationForUserName:]_block_invoke.146
+ ___61-[PODaemonProcess _saveDeviceConfiguration:identifier:error:]_block_invoke
+ ___61-[PODaemonProcess _saveDeviceConfiguration:identifier:error:]_block_invoke.cold.1
+ ___63-[PODaemonProcess _removeUserConfigurationForIdentifier:error:]_block_invoke
+ ___63-[PODaemonProcess _removeUserConfigurationForIdentifier:error:]_block_invoke.cold.1
+ ___64-[PODaemonProcess _removeLoginConfigurationForIdentifier:error:]_block_invoke
+ ___64-[PODaemonProcess _removeLoginConfigurationForIdentifier:error:]_block_invoke.cold.1
+ ___65-[PODaemonProcess _removeDeviceConfigurationForIdentifier:error:]_block_invoke
+ ___65-[PODaemonProcess _removeDeviceConfigurationForIdentifier:error:]_block_invoke.cold.1
+ ___66-[PODaemonProcess _saveUserConfigurationData:forIdentifier:error:]_block_invoke
+ ___66-[PODaemonProcess _saveUserConfigurationData:forIdentifier:error:]_block_invoke.cold.1
+ ___66-[PODaemonProcess saveUserConfiguration:forIdentifier:completion:]_block_invoke
+ ___67-[POConfigurationManager _tokensForExtensionIdentifier:identifier:]_block_invoke.166
+ ___67-[POConfigurationManager _tokensForExtensionIdentifier:identifier:]_block_invoke.166.cold.1
+ ___69-[PODaemonConnection saveUserConfiguration:forIdentifier:completion:]_block_invoke
+ ___69-[PODaemonConnection saveUserConfiguration:forIdentifier:completion:]_block_invoke.cold.1
+ ___73-[PODaemonConnection saveUserConfigurationData:forIdentifier:completion:]_block_invoke
+ ___73-[PODaemonConnection saveUserConfigurationData:forIdentifier:completion:]_block_invoke.cold.1
+ ___83-[POConfigurationManager _setTokens:identifier:extensionIdentifier:returningError:]_block_invoke.175
+ ___83-[POConfigurationManager _setTokens:identifier:extensionIdentifier:returningError:]_block_invoke.175.cold.1
+ ___block_literal_global.142
+ ___block_literal_global.273
+ ___block_literal_global.274
+ _objc_msgSend$_removeDeviceConfigurationForIdentifier:error:
+ _objc_msgSend$_removeLoginConfigurationForIdentifier:error:
+ _objc_msgSend$_removeUserConfigurationForIdentifier:error:
+ _objc_msgSend$_saveDeviceConfiguration:identifier:error:
+ _objc_msgSend$_saveLoginConfiguration:identifier:error:
+ _objc_msgSend$_saveUserConfigurationData:forIdentifier:error:
+ _objc_msgSend$_startDeviceRegistration
+ _objc_msgSend$_startUserRegistrationWithCompletionHandler:
+ _objc_msgSend$analyticsForRegistrationType:options:result:
+ _objc_msgSend$cleanupUserConfigAfterMigrationToShared
+ _objc_msgSend$completeLegacyUserRegistration
+ _objc_msgSend$createOrRepairDeviceConfigurationWithError:
+ _objc_msgSend$createOrRepairUserConfigurationWithError:
+ _objc_msgSend$createUserConfigurationForBuddyUser
+ _objc_msgSend$decimalValue
+ _objc_msgSend$enablePlatformSSORulesAndDefaultsIfNeeded:
+ _objc_msgSend$failDeviceRegistrationPostRegistrationWithUserInteractionAllowed:
+ _objc_msgSend$findExistingSmartCardBinding
+ _objc_msgSend$handleAuthorizationForNewUsers
+ _objc_msgSend$handleUserAuthorizationForRegistration
+ _objc_msgSend$newUserBindingComplete
+ _objc_msgSend$registrationNeedsToShowUI
+ _objc_msgSend$removeBindingForNonPasswordAuth
+ _objc_msgSend$removeUserConfigurationForUserName:
+ _objc_msgSend$requestAndBindSmartCardForUser
+ _objc_msgSend$saveCurrentUserConfiguration
+ _objc_msgSend$saveUserConfiguration:forIdentifier:completion:
+ _objc_msgSend$saveUserConfiguration:forUserName:
+ _objc_msgSend$saveUserConfigurationData:forIdentifier:completion:
+ _objc_msgSend$setJwksCache:forExtensionIdentifier:
+ _objc_msgSend$setupDeviceRegistrationOptions
+ _objc_msgSend$setupUserRegistrationOptions
+ _objc_msgSend$storeCredentialAndUpdatePasswordHint
- +[POConfigurationUtil platformSSOEnabled].cold.2
- +[POConfigurationUtil platformSSOTriggerFile]
- +[POConfigurationUtil updateTriggerFile]
- +[POConfigurationUtil updateTriggerFile].cold.1
- +[POConfigurationUtil updateTriggerFile].cold.2
- +[POConfigurationUtil updateTriggerFile].cold.3
- +[PODaemonProcess _prebootSyncQueue]
- +[PODaemonProcess _prebootSyncQueue].cold.1
- +[PODaemonProcess setSyncPending:]
- +[PODaemonProcess setSyncTimer:]
- +[PODaemonProcess syncPending]
- +[PODaemonProcess syncTimer]
- -[POConfigurationManager saveCurrentUserConfigurationAndSyncToPreboot:]
- -[POConfigurationManager saveDeviceConfigurationSyncAllConfigToPreboot:]
- -[POConfigurationManager saveDeviceConfigurationSyncAllConfigToPreboot:].cold.1
- -[POConfigurationManager saveUserConfiguration:forUserName:syncToPreboot:]
- -[POConfigurationManager saveUserConfiguration:forUserName:syncToPreboot:].cold.1
- -[PODaemonConnection saveDeviceConfigurationSyncAllConfigToPreboot:identifier:completion:]
- -[PODaemonConnection saveUserConfiguration:forIdentifier:syncToPreboot:completion:]
- -[PODaemonConnection saveUserConfigurationData:forIdentifier:syncToPreboot:completion:]
- -[PODaemonProcess _removeDeviceConfigurationForIdentifier:syncToPreboot:error:]
- -[PODaemonProcess _removeLoginConfigurationForIdentifier:syncToPreboot:error:]
- -[PODaemonProcess _removeUserConfigurationForIdentifier:syncToPreboot:error:]
- -[PODaemonProcess _saveDeviceConfiguration:identifier:syncToPreboot:error:]
- -[PODaemonProcess _saveDeviceConfiguration:identifier:syncToPreboot:error:].cold.1
- -[PODaemonProcess _saveLoginConfiguration:identifier:syncToPreboot:error:]
- -[PODaemonProcess _saveLoginConfiguration:identifier:syncToPreboot:error:].cold.1
- -[PODaemonProcess _saveUserConfigurationData:forIdentifier:syncToPreboot:error:]
- -[PODaemonProcess _saveUserConfigurationData:forIdentifier:syncToPreboot:error:].cold.1
- -[PODaemonProcess saveDeviceConfigurationSyncAllConfigToPreboot:identifier:completion:]
- -[PODaemonProcess saveUserConfiguration:forIdentifier:syncToPreboot:completion:]
- -[PODaemonProcess saveUserConfigurationData:forIdentifier:syncToPreboot:completion:]
- GCC_except_table113
- GCC_except_table45
- GCC_except_table60
- GCC_except_table65
- GCC_except_table92
- __OBJC_$_CLASS_METHODS_PODaemonProcess
- __OBJC_$_CLASS_PROP_LIST_PODaemonProcess
- ___36+[PODaemonProcess _prebootSyncQueue]_block_invoke
- ___39-[PODaemonConnection _connectToService]_block_invoke.98
- ___39-[PODaemonConnection _connectToService]_block_invoke.98.cold.1
- ___40+[POConfigurationUtil updateTriggerFile]_block_invoke
- ___40+[POConfigurationUtil updateTriggerFile]_block_invoke.12
- ___40+[POConfigurationUtil updateTriggerFile]_block_invoke.12.cold.1
- ___40+[POConfigurationUtil updateTriggerFile]_block_invoke.18
- ___40+[POConfigurationUtil updateTriggerFile]_block_invoke.18.cold.1
- ___40+[POConfigurationUtil updateTriggerFile]_block_invoke.25
- ___40+[POConfigurationUtil updateTriggerFile]_block_invoke.25.cold.1
- ___40+[POConfigurationUtil updateTriggerFile]_block_invoke.cold.1
- ___54-[PODaemonProcess saveAppSSOConfiguration:completion:]_block_invoke.102
- ___55-[POConfigurationManager userConfigurationForUserName:]_block_invoke.137
- ___61-[POConfigurationManager removeUserConfigurationForUserName:]_block_invoke.152
- ___67-[POConfigurationManager _tokensForExtensionIdentifier:identifier:]_block_invoke.172
- ___67-[POConfigurationManager _tokensForExtensionIdentifier:identifier:]_block_invoke.172.cold.1
- ___71-[POConfigurationManager saveCurrentUserConfigurationAndSyncToPreboot:]_block_invoke
- ___71-[POConfigurationManager saveCurrentUserConfigurationAndSyncToPreboot:]_block_invoke.cold.1
- ___72-[POConfigurationManager saveDeviceConfigurationSyncAllConfigToPreboot:]_block_invoke
- ___74-[POConfigurationManager saveUserConfiguration:forUserName:syncToPreboot:]_block_invoke
- ___74-[POConfigurationManager saveUserConfiguration:forUserName:syncToPreboot:]_block_invoke.145
- ___74-[POConfigurationManager saveUserConfiguration:forUserName:syncToPreboot:]_block_invoke.cold.1
- ___74-[PODaemonProcess _saveLoginConfiguration:identifier:syncToPreboot:error:]_block_invoke
- ___74-[PODaemonProcess _saveLoginConfiguration:identifier:syncToPreboot:error:]_block_invoke.cold.1
- ___75-[PODaemonProcess _saveDeviceConfiguration:identifier:syncToPreboot:error:]_block_invoke
- ___75-[PODaemonProcess _saveDeviceConfiguration:identifier:syncToPreboot:error:]_block_invoke.cold.1
- ___77-[PODaemonProcess _removeUserConfigurationForIdentifier:syncToPreboot:error:]_block_invoke
- ___77-[PODaemonProcess _removeUserConfigurationForIdentifier:syncToPreboot:error:]_block_invoke.cold.1
- ___78-[PODaemonProcess _removeLoginConfigurationForIdentifier:syncToPreboot:error:]_block_invoke
- ___78-[PODaemonProcess _removeLoginConfigurationForIdentifier:syncToPreboot:error:]_block_invoke.cold.1
- ___79-[PODaemonProcess _removeDeviceConfigurationForIdentifier:syncToPreboot:error:]_block_invoke
- ___79-[PODaemonProcess _removeDeviceConfigurationForIdentifier:syncToPreboot:error:]_block_invoke.cold.1
- ___80-[PODaemonProcess _saveUserConfigurationData:forIdentifier:syncToPreboot:error:]_block_invoke
- ___80-[PODaemonProcess _saveUserConfigurationData:forIdentifier:syncToPreboot:error:]_block_invoke.cold.1
- ___80-[PODaemonProcess saveUserConfiguration:forIdentifier:syncToPreboot:completion:]_block_invoke
- ___83-[POConfigurationManager _setTokens:identifier:extensionIdentifier:returningError:]_block_invoke.181
- ___83-[POConfigurationManager _setTokens:identifier:extensionIdentifier:returningError:]_block_invoke.181.cold.1
- ___83-[PODaemonConnection saveUserConfiguration:forIdentifier:syncToPreboot:completion:]_block_invoke
- ___83-[PODaemonConnection saveUserConfiguration:forIdentifier:syncToPreboot:completion:]_block_invoke.cold.1
- ___87-[PODaemonConnection saveUserConfigurationData:forIdentifier:syncToPreboot:completion:]_block_invoke
- ___87-[PODaemonConnection saveUserConfigurationData:forIdentifier:syncToPreboot:completion:]_block_invoke.cold.1
- ___90-[PODaemonConnection saveDeviceConfigurationSyncAllConfigToPreboot:identifier:completion:]_block_invoke
- ___90-[PODaemonConnection saveDeviceConfigurationSyncAllConfigToPreboot:identifier:completion:]_block_invoke.cold.1
- ___block_literal_global.145
- ___block_literal_global.281
- ___block_literal_global.29
- ___block_literal_global.291
- __prebootSyncQueue.onceToken
- __prebootSyncQueue.queue
- __swift_FORCE_LOAD_$_swiftAccelerate
- __swift_FORCE_LOAD_$_swiftAccelerate_$_PlatformSSO
- __syncLock
- __syncPending
- __syncTimer
- _kPlatformSSOConfigurationPath
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$_removeDeviceConfigurationForIdentifier:syncToPreboot:error:
- _objc_msgSend$_removeLoginConfigurationForIdentifier:syncToPreboot:error:
- _objc_msgSend$_removeUserConfigurationForIdentifier:syncToPreboot:error:
- _objc_msgSend$_saveDeviceConfiguration:identifier:syncToPreboot:error:
- _objc_msgSend$_saveLoginConfiguration:identifier:syncToPreboot:error:
- _objc_msgSend$_saveUserConfigurationData:forIdentifier:syncToPreboot:error:
- _objc_msgSend$contentsOfDirectoryAtPath:error:
- _objc_msgSend$fileExistsAtPath:
- _objc_msgSend$platformSSOTriggerFile
- _objc_msgSend$removeItemAtPath:error:
- _objc_msgSend$saveCurrentUserConfigurationAndSyncToPreboot:
- _objc_msgSend$saveDeviceConfigurationSyncAllConfigToPreboot:
- _objc_msgSend$saveDeviceConfigurationSyncAllConfigToPreboot:identifier:completion:
- _objc_msgSend$saveUserConfiguration:forIdentifier:syncToPreboot:completion:
- _objc_msgSend$saveUserConfiguration:forUserName:syncToPreboot:
- _objc_msgSend$saveUserConfigurationData:forIdentifier:syncToPreboot:completion:
- _objc_msgSend$stringByAppendingPathComponent:
- _objc_msgSend$writeToFile:options:error:
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x6
- _objc_retain_x9
CStrings:
+ "-[POConfigurationManager saveUserConfiguration:forUserName:]"
+ "-[PODaemonProcess _removeDeviceConfigurationForIdentifier:error:]"
+ "-[PODaemonProcess _removeLoginConfigurationForIdentifier:error:]"
+ "-[PODaemonProcess _removeUserConfigurationForIdentifier:error:]"
+ "-[PODaemonProcess _saveDeviceConfiguration:identifier:error:]"
+ "-[PODaemonProcess _saveLoginConfiguration:identifier:error:]"
+ "-[PODaemonProcess _saveUserConfigurationData:forIdentifier:error:]"
+ "-[PODaemonProcess saveUserConfiguration:forIdentifier:completion:]"
+ "-[PODaemonProcess saveUserConfigurationData:forIdentifier:completion:]"
+ "_removeDeviceConfigurationForIdentifier:error:"
+ "_removeLoginConfigurationForIdentifier:error:"
+ "_removeUserConfigurationForIdentifier:error:"
+ "_saveDeviceConfiguration:identifier:error:"
+ "_saveLoginConfiguration:identifier:error:"
+ "_saveUserConfigurationData:forIdentifier:error:"
+ "saveCurrentUserConfiguration"
+ "saveUserConfiguration:forIdentifier:completion:"
+ "saveUserConfiguration:forUserName:"
+ "saveUserConfigurationData:forIdentifier:completion:"
+ "v40@0:8@\"POUserConfiguration\"16@\"NSString\"24@?<v@?B@\"NSError\">32"
- "+[POConfigurationUtil updateTriggerFile]"
- "-[POConfigurationManager saveDeviceConfigurationSyncAllConfigToPreboot:]"
- "-[POConfigurationManager saveUserConfiguration:forUserName:syncToPreboot:]"
- "-[PODaemonProcess _removeDeviceConfigurationForIdentifier:syncToPreboot:error:]"
- "-[PODaemonProcess _removeLoginConfigurationForIdentifier:syncToPreboot:error:]"
- "-[PODaemonProcess _removeUserConfigurationForIdentifier:syncToPreboot:error:]"
- "-[PODaemonProcess _saveDeviceConfiguration:identifier:syncToPreboot:error:]"
- "-[PODaemonProcess _saveLoginConfiguration:identifier:syncToPreboot:error:]"
- "-[PODaemonProcess _saveUserConfigurationData:forIdentifier:syncToPreboot:error:]"
- "-[PODaemonProcess saveDeviceConfigurationSyncAllConfigToPreboot:identifier:completion:]"
- "-[PODaemonProcess saveUserConfiguration:forIdentifier:syncToPreboot:completion:]"
- "-[PODaemonProcess saveUserConfigurationData:forIdentifier:syncToPreboot:completion:]"
- "/var/mobile/Library/ExtensibleSSO/Configuration/com.apple.AppSSO.configuration.plist"
- "B20@0:8B16"
- "B36@0:8@16B24^@28"
- "B44@0:8@16@24B32^@36"
- "Did not find configuration files."
- "Failed to create trigger file"
- "Failed to remove trigger file."
- "Failed to set trigger file attributes"
- "Platform SSO is configured."
- "T@\"NSTimer\",&,D"
- "TB,D"
- "_prebootSyncQueue"
- "_removeDeviceConfigurationForIdentifier:syncToPreboot:error:"
- "_removeLoginConfigurationForIdentifier:syncToPreboot:error:"
- "_removeUserConfigurationForIdentifier:syncToPreboot:error:"
- "_saveDeviceConfiguration:identifier:syncToPreboot:error:"
- "_saveLoginConfiguration:identifier:syncToPreboot:error:"
- "_saveUserConfigurationData:forIdentifier:syncToPreboot:error:"
- "com.apple.PlatformSSO.sync-queue"
- "contentsOfDirectoryAtPath:error:"
- "deviceConfiguration sync all"
- "fileExistsAtPath:"
- "loginConfiguration sync all"
- "platformSSOTriggerFile"
- "removeItemAtPath:error:"
- "saveCurrentUserConfigurationAndSyncToPreboot:"
- "saveDeviceConfigurationSyncAllConfigToPreboot:"
- "saveDeviceConfigurationSyncAllConfigToPreboot:identifier:completion:"
- "saveUserConfiguration:forIdentifier:syncToPreboot:completion:"
- "saveUserConfiguration:forUserName:syncToPreboot:"
- "saveUserConfigurationData:forIdentifier:syncToPreboot:completion:"
- "setSyncPending:"
- "setSyncTimer:"
- "stringByAppendingPathComponent:"
- "syncPending"
- "syncTimer"
- "trigger file created"
- "trigger file removed"
- "v44@0:8@\"NSData\"16@\"NSString\"24B32@?<v@?B@\"NSError\">36"
- "v44@0:8@\"POUserConfiguration\"16@\"NSString\"24B32@?<v@?B@\"NSError\">36"
- "writeToFile:options:error:"

```
