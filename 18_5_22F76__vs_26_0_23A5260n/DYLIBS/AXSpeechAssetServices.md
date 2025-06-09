## AXSpeechAssetServices

> `/System/Library/PrivateFrameworks/AXSpeechAssetServices.framework/AXSpeechAssetServices`

```diff

-3148.15.26.0.0
-  __TEXT.__text: 0x1f80
-  __TEXT.__auth_stubs: 0x3e0
-  __TEXT.__objc_methlist: 0x3bc
-  __TEXT.__const: 0x38
-  __TEXT.__cstring: 0x234
-  __TEXT.__oslogstring: 0x188
-  __TEXT.__gcc_except_tab: 0x18
-  __TEXT.__dlopen_cstrs: 0x58
-  __TEXT.__unwind_info: 0x110
-  __TEXT.__objc_classname: 0xab
-  __TEXT.__objc_methname: 0xa02
-  __TEXT.__objc_methtype: 0x2e0
-  __TEXT.__objc_stubs: 0x520
-  __DATA_CONST.__got: 0xb0
-  __DATA_CONST.__const: 0xf0
-  __DATA_CONST.__objc_classlist: 0x20
+3180.6.1.0.0
+  __TEXT.__text: 0xd98
+  __TEXT.__auth_stubs: 0x200
+  __TEXT.__objc_methlist: 0x29c
+  __TEXT.__const: 0x8
+  __TEXT.__cstring: 0x158
+  __TEXT.__oslogstring: 0xb
+  __TEXT.__unwind_info: 0xa0
+  __TEXT.__objc_classname: 0x71
+  __TEXT.__objc_methname: 0x6b4
+  __TEXT.__objc_methtype: 0x282
+  __TEXT.__objc_stubs: 0x300
+  __DATA_CONST.__got: 0x50
+  __DATA_CONST.__const: 0x40
+  __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2a8
-  __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0x200
-  __AUTH_CONST.__const: 0x80
-  __AUTH_CONST.__cfstring: 0x260
-  __AUTH_CONST.__objc_const: 0x620
+  __DATA_CONST.__objc_selrefs: 0x1f0
+  __DATA_CONST.__objc_superrefs: 0x10
+  __AUTH_CONST.__auth_got: 0x108
+  __AUTH_CONST.__const: 0x40
+  __AUTH_CONST.__cfstring: 0x200
+  __AUTH_CONST.__objc_const: 0x3e8
   __AUTH.__objc_data: 0xa0
-  __DATA.__objc_ivar: 0x2c
-  __DATA.__data: 0x190
-  __DATA.__bss: 0x1a
-  __DATA_DIRTY.__objc_data: 0xa0
-  __DATA_DIRTY.__bss: 0x38
+  __DATA.__objc_ivar: 0x10
+  __DATA.__data: 0x180
+  __DATA.__bss: 0x10
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/AccessibilityUI.framework/AccessibilityUI
   - /System/Library/PrivateFrameworks/AccessibilityUtilities.framework/AccessibilityUtilities
   - /System/Library/PrivateFrameworks/AssistantServices.framework/AssistantServices
-  - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/TextToSpeech.framework/TextToSpeech
   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4E2468C6-9222-3EE0-82E8-551319A9D580
-  Functions: 58
-  Symbols:   337
-  CStrings:  207
+  UUID: 4DBC832F-0998-3BAB-B5E4-3E74BE73B6FA
+  Functions: 22
+  Symbols:   165
+  CStrings:  149
 
Symbols:
+ ___block_literal_global.365
- +[AXSettingsVoiceAssetManager sharedInstance]
- +[AXSettingsVoiceAssetManager sharedInstance].cold.1
- +[AXSpeechAssetMonitorHelper sharedInstance]
- +[AXSpeechAssetMonitorHelper sharedInstance].cold.1
- -[AXSettingsVoiceAssetManager _updateAllowedToDownload]
- -[AXSettingsVoiceAssetManager allowedToDownloadVoiceAssets]
- -[AXSettingsVoiceAssetManager dealloc]
- -[AXSpeechAssetMonitorHelper .cxx_destruct]
- -[AXSpeechAssetMonitorHelper _assetUpdaterClient]
- -[AXSpeechAssetMonitorHelper _monitorForNetworkChanges]
- -[AXSpeechAssetMonitorHelper _monitorSpeechAssetChanges]
- -[AXSpeechAssetMonitorHelper _platformSupportsMobileAssetVoices]
- -[AXSpeechAssetMonitorHelper _registerForReachabilityNotifications]
- -[AXSpeechAssetMonitorHelper _unregisterForReachabilityNotifications]
- -[AXSpeechAssetMonitorHelper _updateSpeechSourceIdentifiersIfNeeded]
- -[AXSpeechAssetMonitorHelper handeDeviceFirstUnlock]
- -[AXSpeechAssetMonitorHelper init]
- -[AXSpeechAssetMonitorHelper longOperationQueue]
- -[AXSpeechAssetMonitorHelper migrationQueue]
- -[AXSpeechAssetMonitorHelper setLongOperationQueue:]
- -[AXSpeechAssetMonitorHelper setMigrationQueue:]
- -[AXSpeechAssetMonitorHelper startMigrationOnDeviceUnlock]
- GCC_except_table2
- _AVSpeechSynthesisVoiceIdentifierFred
- _AVSpeechSynthesisVoiceIdentifierVictoria
- _AXAssetLoaderLibraryCore.frameworkLibrary
- _AXDeviceIsUnlocked
- _AXLanguageCanonicalFormToGeneralLanguage
- _AXLogSpeechAssetDownload
- _AXLogUI
- _AXPerformBlockOnMainThreadAfterDelay
- _AXSpeechSourceKeySpeechFeatures
- _AXSpeechSourceKeySwitchControl
- _AXSpeechSourceKeyVoiceOver
- _AXkMobileKeyBagLockStatusNotificationID
- _AllowedToDownload
- _AllowedToDownloadIsSet
- _CFCopyDescription
- _CFNotificationCenterAddObserver
- _CFNotificationCenterGetDarwinNotifyCenter
- _CFRelease
- _OBJC_CLASS_$_AXSettings
- _OBJC_CLASS_$_AXSettingsVoiceAssetManager
- _OBJC_CLASS_$_AXSpeechAssetMonitorHelper
- _OBJC_CLASS_$_NSNumber
- _OBJC_CLASS_$_TTSAXResourceMigrationUtilities
- _OBJC_IVAR_$_AXSettingsVoiceAssetManager._reachability
- _OBJC_IVAR_$_AXSpeechAssetMonitorHelper._assetService
- _OBJC_IVAR_$_AXSpeechAssetMonitorHelper._lastVoiceAssetUpdateTime
- _OBJC_IVAR_$_AXSpeechAssetMonitorHelper._longOperationQueue
- _OBJC_IVAR_$_AXSpeechAssetMonitorHelper._migrationQueue
- _OBJC_IVAR_$_AXSpeechAssetMonitorHelper._reachability
- _OBJC_IVAR_$_AXSpeechAssetMonitorHelper._speechAssetClient
- _OBJC_METACLASS_$_AXSettingsVoiceAssetManager
- _OBJC_METACLASS_$_AXSpeechAssetMonitorHelper
- _SCNetworkReachabilityCreateWithAddress
- _SCNetworkReachabilityGetFlags
- _SCNetworkReachabilitySetCallback
- _SCNetworkReachabilitySetDispatchQueue
- _TTSPreferencesCopyDefaultOutputLanguageIdentifierForUserPreferences
- __Block_object_dispose
- __NSConcreteStackBlock
- __OBJC_$_CLASS_METHODS_AXSettingsVoiceAssetManager
- __OBJC_$_CLASS_METHODS_AXSpeechAssetMonitorHelper
- __OBJC_$_INSTANCE_METHODS_AXSettingsVoiceAssetManager
- __OBJC_$_INSTANCE_METHODS_AXSpeechAssetMonitorHelper
- __OBJC_$_INSTANCE_VARIABLES_AXSettingsVoiceAssetManager
- __OBJC_$_INSTANCE_VARIABLES_AXSpeechAssetMonitorHelper
- __OBJC_$_PROP_LIST_AXSpeechAssetMonitorHelper
- __OBJC_CLASS_RO_$_AXSettingsVoiceAssetManager
- __OBJC_CLASS_RO_$_AXSpeechAssetMonitorHelper
- __OBJC_METACLASS_RO_$_AXSettingsVoiceAssetManager
- __OBJC_METACLASS_RO_$_AXSpeechAssetMonitorHelper
- __Unwind_Resume
- ___34-[AXSpeechAssetMonitorHelper init]_block_invoke
- ___34-[AXSpeechAssetMonitorHelper init]_block_invoke_2
- ___34-[AXSpeechAssetMonitorHelper init]_block_invoke_3
- ___34-[AXSpeechAssetMonitorHelper init]_block_invoke_4
- ___44+[AXSpeechAssetMonitorHelper sharedInstance]_block_invoke
- ___45+[AXSettingsVoiceAssetManager sharedInstance]_block_invoke
- ___58-[AXSpeechAssetMonitorHelper startMigrationOnDeviceUnlock]_block_invoke
- ___58-[AXSpeechAssetMonitorHelper startMigrationOnDeviceUnlock]_block_invoke.289
- ___AXAssetLoaderLibraryCore_block_invoke
- ___ReachabilityCallback
- ___block_descriptor_40_e5_v8?0l
- ___block_descriptor_40_e8_32r_e5_v8?0lr32l8
- ___block_descriptor_40_e8_32s_e34_v24?0"NSDictionary"8"NSError"16ls32l8
- ___block_descriptor_40_e8_32s_e5_v8?0ls32l8
- ___block_literal_global.362
- ___getAXAssetsServiceClass_block_invoke
- ___getAXAssetsServiceClass_block_invoke.cold.1
- ___objc_personality_v0
- __deviceLockStateChanged
- __dispatch_main_q
- __sl_dlopen
- _abort_report_np
- _audit_stringAXAssetLoader
- _deviceHasBeenUnlockedOnce
- _dispatch_after
- _dispatch_queue_attr_make_with_autorelease_frequency
- _dispatch_queue_attr_make_with_qos_class
- _dispatch_queue_create
- _dispatch_time
- _free
- _getAXAssetsServiceClass.softClass
- _getpid
- _kCFAllocatorDefault
- _objc_alloc_init
- _objc_getClass
- _objc_msgSend$_monitorSpeechAssetChanges
- _objc_msgSend$_registerForReachabilityNotifications
- _objc_msgSend$_unregisterForReachabilityNotifications
- _objc_msgSend$_updateAllowedToDownload
- _objc_msgSend$_updateSpeechSourceIdentifiersIfNeeded
- _objc_msgSend$componentCacheChanged
- _objc_msgSend$downloadCompactResourceIfNeededForIdentifier:
- _objc_msgSend$handeDeviceFirstUnlock
- _objc_msgSend$invalidate:
- _objc_msgSend$migrationQueue
- _objc_msgSend$numberWithInt:
- _objc_msgSend$restartMigrationIfNeeded
- _objc_msgSend$runFirstBootTasks:
- _objc_msgSend$runFirstUnlockTasks
- _objc_msgSend$siriAutoUpdateListInitialized
- _objc_msgSend$speechVoiceIdentifierForLanguage:sourceKey:exists:
- _objc_msgSend$startMigrationOnDeviceUnlock
- _objc_retainAutorelease
- _objc_retain_x19
- _objc_retain_x21
- _sharedInstance.Manager
- _sharedInstance.Monitor
- _sharedInstance.onceToken
- _startMigrationOnDeviceUnlock.onceToken
CStrings:
- "$"
- "%s"
- "@\"AXAssetsService\""
- "@\"AXUIClient\""
- "@\"NSObject<OS_dispatch_queue>\""
- "AXAssetAndDataServer-migrate-siri-list-%@"
- "AXAssetsService"
- "AXSAM.operation"
- "AXSettingsVoiceAssetManager"
- "AXSpeechAssetMonitorHelper"
- "AXSpeechAssetMonitorHelper: Migration task timer set for 5 minutes."
- "AXSpeechAssetMonitorHelper: Running migration from SpringBoard after first unlock."
- "AXSpeechAssetMonitorHelper: Updating super compact voice identifiers for all speech sources if needed."
- "Got reachability change"
- "Looks like we're reachable, try again"
- "Making new speech migration client: %@"
- "PREMIUM: Is reachable: %d"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_longOperationQueue"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_migrationQueue"
- "Unable to find class %s"
- "^{__SCNetworkReachability=}"
- "_assetService"
- "_lastVoiceAssetUpdateTime"
- "_longOperationQueue"
- "_migrationQueue"
- "_monitorForNetworkChanges"
- "_monitorSpeechAssetChanges"
- "_platformSupportsMobileAssetVoices"
- "_reachability"
- "_registerForReachabilityNotifications"
- "_speechAssetClient"
- "_unregisterForReachabilityNotifications"
- "_updateAllowedToDownload"
- "_updateSpeechSourceIdentifiersIfNeeded"
- "allowedToDownloadVoiceAssets"
- "com.apple.accessibility.migrationQueue"
- "com.apple.speech.synthesis.voice.Fred"
- "com.apple.speech.synthesis.voice.Victoria"
- "componentCacheChanged"
- "d"
- "downloadCompactResourceIfNeededForIdentifier:"
- "handeDeviceFirstUnlock"
- "invalidate:"
- "longOperationQueue"
- "migrationQueue"
- "numberWithInt:"
- "restartMigrationIfNeeded"
- "runFirstBootTasks:"
- "runFirstUnlockTasks"
- "setLongOperationQueue:"
- "setMigrationQueue:"
- "siriAutoUpdateListInitialized"
- "softlink:r:path:/System/Library/PrivateFrameworks/AXAssetLoader.framework/AXAssetLoader"
- "speechVoiceIdentifierForLanguage:sourceKey:exists:"
- "startMigrationOnDeviceUnlock"

```
