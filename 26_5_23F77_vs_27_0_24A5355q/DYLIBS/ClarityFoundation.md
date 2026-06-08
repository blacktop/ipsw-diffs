## ClarityFoundation

> `/System/Library/PrivateFrameworks/ClarityFoundation.framework/ClarityFoundation`

```diff

-3191.35.0.0.0
-  __TEXT.__text: 0x6ef4
-  __TEXT.__auth_stubs: 0x4d0
-  __TEXT.__objc_methlist: 0xabc
-  __TEXT.__const: 0x27e
-  __TEXT.__gcc_except_tab: 0xb0
-  __TEXT.__cstring: 0x826
-  __TEXT.__oslogstring: 0x3ca
-  __TEXT.__dlopen_cstrs: 0x152
+3229.1.6.0.0
+  __TEXT.__text: 0x7408
+  __TEXT.__objc_methlist: 0xae4
+  __TEXT.__const: 0x288
+  __TEXT.__dlopen_cstrs: 0x1a3
+  __TEXT.__cstring: 0x847
   __TEXT.__constg_swiftt: 0x38
   __TEXT.__swift5_typeref: 0x52
   __TEXT.__swift5_builtin: 0x14

   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_proto: 0x1c
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x388
-  __TEXT.__objc_classname: 0x267
-  __TEXT.__objc_methname: 0x16a1
-  __TEXT.__objc_methtype: 0x200
-  __TEXT.__objc_stubs: 0xc20
-  __DATA_CONST.__got: 0x100
-  __DATA_CONST.__const: 0x218
+  __TEXT.__gcc_except_tab: 0xf4
+  __TEXT.__oslogstring: 0x4a3
+  __TEXT.__unwind_info: 0x370
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x230
   __DATA_CONST.__objc_classlist: 0xa0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6a0
+  __DATA_CONST.__objc_selrefs: 0x6e0
   __DATA_CONST.__objc_superrefs: 0xb0
-  __AUTH_CONST.__auth_got: 0x278
+  __DATA_CONST.__got: 0x110
   __AUTH_CONST.__const: 0x148
   __AUTH_CONST.__cfstring: 0xa40
-  __AUTH_CONST.__objc_const: 0x1338
-  __AUTH.__objc_data: 0x3c0
+  __AUTH_CONST.__objc_const: 0x1328
+  __AUTH_CONST.__auth_got: 0x280
+  __AUTH.__objc_data: 0x460
   __DATA.__objc_ivar: 0x1c
   __DATA.__data: 0x150
-  __DATA.__bss: 0x3f0
-  __DATA_DIRTY.__objc_data: 0x280
-  __DATA_DIRTY.__bss: 0x78
+  __DATA.__bss: 0x448
+  __DATA_DIRTY.__objc_data: 0x1e0
+  __DATA_DIRTY.__bss: 0x30
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/AXCoreUtilities.framework/AXCoreUtilities

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: F3C18DB2-2235-3FF5-9E94-BA25CEBF0619
-  Functions: 254
-  Symbols:   927
-  CStrings:  507
+  UUID: FAB404F1-E48E-3EA2-9366-14847ECAA29B
+  Functions: 225
+  Symbols:   886
+  CStrings:  204
 
Symbols:
+ -[CLFSettings_GeneratedCode bluetoothDeviceIdentifiersToConnect]
+ -[CLFSettings_GeneratedCode setBluetoothDeviceIdentifiersToConnect:]
+ -[CLFSystemShellSwitcher _deviceIdentifiersForDevices:]
+ -[CLFSystemShellSwitcher _noteConnectedBluetoothDevices]
+ -[CLFSystemShellSwitcher _performRebootForEnabled:error:]
+ -[CLFSystemShellSwitcher _prepareStateForEnteringClarityBoard]
+ GCC_except_table147
+ GCC_except_table155
+ GCC_except_table157
+ GCC_except_table161
+ _CoreBluetoothLibraryCore.frameworkLibrary
+ _OBJC_CLASS_$_NSDate
+ _OBJC_CLASS_$_NSRunLoop
+ ___CoreBluetoothLibraryCore_block_invoke
+ ___block_literal_global.102
+ ___block_literal_global.243
+ ___block_literal_global.274
+ ___block_literal_global.331
+ ___block_literal_global.376
+ ___block_literal_global.514
+ ___block_literal_global.556
+ ___block_literal_global.57
+ ___getCBDiscoveryClass_block_invoke
+ _audit_stringCoreBluetooth
+ _getCBDiscoveryClass.softClass
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$_deviceIdentifiersForDevices:
+ _objc_msgSend$_noteConnectedBluetoothDevices
+ _objc_msgSend$_performRebootForEnabled:error:
+ _objc_msgSend$_prepareStateForEnteringClarityBoard
+ _objc_msgSend$archivalStringValue
+ _objc_msgSend$currentRunLoop
+ _objc_msgSend$dateWithTimeIntervalSinceNow:
+ _objc_msgSend$devicesWithDiscoveryFlags:error:
+ _objc_msgSend$identifier
+ _objc_msgSend$runUntilDate:
+ _objc_msgSend$setBluetoothDeviceIdentifiersToConnect:
+ _objc_retainAutorelease
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x3
+ _objc_retain_x8
+ _sharedInstance.SharedSettings.244
+ _sharedInstance.SharedSettings.275
+ _sharedInstance.SharedSettings.332
+ _sharedInstance.SharedSettings.515
+ _sharedInstance.SharedSettings.557
+ _sharedInstance.onceToken.242
+ _sharedInstance.onceToken.273
+ _sharedInstance.onceToken.330
+ _sharedInstance.onceToken.375
+ _sharedInstance.onceToken.513
+ _sharedInstance.onceToken.555
- +[CLFAppAvailabilityChecker sharedInstance].cold.1
- +[CLFCameraSettings_GeneratedCode sharedInstance].cold.1
- +[CLFLog backlightLog]
- +[CLFMessagesSettings_GeneratedCode sharedInstance].cold.1
- +[CLFMusicSettings_GeneratedCode sharedInstance].cold.1
- +[CLFPhoneFaceTimeSettings_GeneratedCode sharedInstance].cold.1
- +[CLFPhotosSettings_GeneratedCode sharedInstance].cold.1
- +[CLFSettings_GeneratedCode sharedInstance].cold.1
- +[CLFSystemShellSwitcher sharedSystemShellSwitcher].cold.1
- -[CLFAppAvailabilityChecker requiresPreflightForBundleIdentifier:].cold.1
- -[CLFAppAvailabilityChecker requiresPreflightForBundleIdentifier:].cold.2
- -[CLFBaseCommunicationLimitSettings(Additions) setOutgoingCommunicationLimit:].cold.1
- -[CLFBaseSettings preferenceKeysBySelectorName]
- -[CLFSettings_GeneratedCode restrictPhoneCall]
- -[CLFSettings_GeneratedCode setRestrictPhoneCall:]
- -[CLFSystemShellSwitcher _createFileWithError:].cold.1
- -[CLFSystemShellSwitcher _createFileWithError:].cold.2
- -[CLFSystemShellSwitcher _removeFileWithError:].cold.1
- -[CLFSystemShellSwitcher setClarityBoardEnabled:error:].cold.1
- -[NSString(CLFCommunicationLimit) isLessRestrictiveThanCommunicationLimit:].cold.1
- GCC_except_table11
- GCC_except_table13
- GCC_except_table2
- _AppProtectionLibrary
- _CLFLogBacklight
- _CLFSortedCommunicationLimits.cold.1
- _OUTLINED_FUNCTION_0
- _OUTLINED_FUNCTION_1
- _OUTLINED_FUNCTION_2
- _OUTLINED_FUNCTION_3
- _PhotosLibrary
- ___getAPApplicationClass_block_invoke.cold.1
- ___getAPSubjectClass_block_invoke.cold.1
- ___getLSApplicationRecordClass_block_invoke.cold.1
- ___getPDCPreflightManagerClass_block_invoke.cold.1
- ___getPHAssetCollectionClass_block_invoke.cold.1
- ___getPHPhotoLibraryClass_block_invoke.cold.1
- _objc_msgSend$stringValue
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x23
- _objc_retain_x24
- _objc_retain_x25
CStrings:
+ "BluetoothDeviceIdentifiersToConnect"
+ "CBDiscovery"
+ "Initiating user-space reboot after %f second delay..."
+ "Unable to get connected Bluetooth devices: %@"
+ "Unable to get identifier for connected Bluetooth device: %@"
+ "Will attempt to reconnect Bluetooth device if needed: %@"
+ "softlink:r:path:/System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth"
- "#16@0:8"
- ".cxx_destruct"
- ":"
- ":16@0:8"
- "@\"<APSubjectMonitorSubscription>\""
- "@\"CLFBaseSettings\""
- "@\"NSMutableDictionary\""
- "@\"NSString\"16@0:8"
- "@\"PDCPreflightManager\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@24@0:8@?16"
- "@32@0:8:16@24"
- "@32@0:8:16@?24"
- "@32@0:8@16:24"
- "@40@0:8:16@24@32"
- "@?"
- "@?16@0:8"
- "APSubjectMonitor"
- "Additions"
- "Additions_Internal"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B24@0:8^@16"
- "B28@0:8B16^@20"
- "BSInvalidatable"
- "CLFAppAvailabilityChecker"
- "CLFBaseCommunicationLimitSettings"
- "CLFBaseCommunicationLimitSettings_GeneratedCode"
- "CLFBaseSettings"
- "CLFCameraSettings"
- "CLFCameraSettings_GeneratedCode"
- "CLFCommunicationLimit"
- "CLFLog"
- "CLFMessagesSettings"
- "CLFMessagesSettings_GeneratedCode"
- "CLFMusicSettings"
- "CLFMusicSettings_GeneratedCode"
- "CLFPhoneFaceTimeSettings"
- "CLFPhoneFaceTimeSettings_GeneratedCode"
- "CLFPhotosSettings"
- "CLFPhotosSettings_GeneratedCode"
- "CLFSettings"
- "CLFSettings_GeneratedCode"
- "Migration"
- "NSObject"
- "Q16@0:8"
- "RestrictPhoneCall"
- "T#,R"
- "T:,N,V_settingsSelector"
- "T@\"<APSubjectMonitorSubscription>\",&,N,V_subscription"
- "T@\"CLFAppAvailabilityChecker\",R,N"
- "T@\"CLFBaseSettings\",W,N,V_settings"
- "T@\"CLFCameraSettings\",R,N"
- "T@\"CLFMessagesSettings\",R,N"
- "T@\"CLFMusicSettings\",R,N"
- "T@\"CLFPhoneFaceTimeSettings\",R,N"
- "T@\"CLFPhotosSettings\",R,N"
- "T@\"CLFSettings\",R,N"
- "T@\"CLFSystemShellSwitcher\",R,N"
- "T@\"NSArray\",&,N"
- "T@\"NSArray\",R,N"
- "T@\"NSObject<OS_os_log>\",R,N"
- "T@\"NSString\",&,N"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,N"
- "T@\"PDCPreflightManager\",R,N,V_privacyPreflightManager"
- "T@?,C,N,V_handler"
- "TB,N"
- "TB,N,GisClarityBoardEnabled,V_clarityBoardEnabled"
- "TB,R,N"
- "TQ,R"
- "URLByAppendingPathComponent:"
- "URLByAppendingPathComponent:isDirectory:"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_CLFAppAvailabilityObserver"
- "_CLFSettingsObserver"
- "_clarityBoardEnabled"
- "_createFileWithError:"
- "_deleteAllKeys"
- "_directoryURL"
- "_handler"
- "_migrateSelectedSharedAlbumNamesIfNecessary"
- "_preferenceKeysBySelectorName"
- "_privacyPreflightManager"
- "_removeFileWithError:"
- "_saveSelectedSharedAlbumCloudIdentifiersForNames:"
- "_settings"
- "_settingsSelector"
- "_subscription"
- "_switchFromRootUserIfNecessary:"
- "addMonitor:subjectMask:"
- "addObject:"
- "adminPasscodeRecoveryAppleID"
- "allPreferenceSelectorsAsStrings"
- "allowAccessibilityShortcut"
- "allowPhotoCapture"
- "allowPinchToZoom"
- "allowSelfieCapture"
- "allowSelfieVideoCapture"
- "allowSiri"
- "allowVideoCapture"
- "appProtectionSubjectsChanged:forSubscription:"
- "applicationBundleIdentifiers"
- "applicationWithBundleIdentifier:"
- "array"
- "arrayByAddingObjectsFromArray:"
- "arrayWithObjects:count:"
- "autorelease"
- "backlightLog"
- "batteryMonitoringEnabled"
- "boolValueForPreferenceKey:defaultValue:"
- "bundleForClass:"
- "bundleWithPath:"
- "clarityBoardEnabled"
- "clarityBundleIdentifierForStandardBundleIdentifier:"
- "class"
- "cloudIdentifier"
- "cloudIdentifierMappingsForLocalIdentifiers:"
- "code"
- "commonLog"
- "conformsToProtocol:"
- "conversationDetailsEnabled"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "createDirectoryAtURL:withIntermediateDirectories:attributes:error:"
- "data"
- "debugDescription"
- "defaultManager"
- "deleteAllKeys"
- "description"
- "dialerKeypadEnabled"
- "dictionary"
- "dictionaryWithContentsOfFile:"
- "dictionaryWithObjects:forKeys:count:"
- "domain"
- "domainName"
- "domainNameForPreferenceKey:"
- "emergencyKeypadEnabled"
- "emojiKeyboardEnabled"
- "enumerateObjectsUsingBlock:"
- "error"
- "errorWithDomain:code:userInfo:"
- "fetchAssetCollectionsWithType:subtype:options:"
- "fileURLWithPath:"
- "fullScreenCompatibilityMode"
- "handler"
- "hasMigratedFileProtections"
- "hash"
- "inCallKeypadEnabled"
- "includeSharedAlbums"
- "incomingCommunicationLimit"
- "indexOfObject:"
- "init"
- "initWithBundleIdentifier:allowPlaceholder:error:"
- "initWithHandler:"
- "initWithSettings:settingsSelector:"
- "initWithSuiteName:"
- "initWithTargetQueue:"
- "invalidate"
- "isAppAvailableForBundleIdentifier:"
- "isClarityBoardEnabled"
- "isEqual:"
- "isEqualToString:"
- "isHidden"
- "isHiddenByUserForBundleIdentifier:"
- "isKindOfClass:"
- "isLessRestrictiveThanCommunicationLimit:"
- "isMemberOfClass:"
- "isProxy"
- "legacyDialerKeypadEnabled"
- "legacyIncomingCommunicationLimit"
- "legacyOutgoingCommunicationLimit"
- "length"
- "listLayout"
- "load"
- "localIdentifier"
- "localizedTitle"
- "lockScreenClockEnabled"
- "lockScreenDateEnabled"
- "migrateCommunicationLimitsIfNecessary"
- "muteEnabled"
- "needsMigrationFor117558856"
- "notificationsEnabled"
- "numberWithBool:"
- "numberWithInt:"
- "numberWithUnsignedLongLong:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "objectValueForPreferenceKey:ofClass:defaultValue:"
- "observeUpdatesForSelector:handler:"
- "observeUpdatesWithHandler:"
- "oneTapUnlock"
- "outgoingCommunicationLimit"
- "overrideNonClarityApplicationBundleIdentifiers"
- "pathForResource:ofType:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "photoKeyboardEnabled"
- "preferenceKeyForSelector:"
- "privacyPreflightManager"
- "recentsEnabled"
- "registerUpdateBlock:forRetrieveSelector:withListener:"
- "registerUpdateBlock:withListener:"
- "release"
- "removeItemAtURL:error:"
- "removePersistentDomainForName:"
- "requiresMoreRestrictiveOutgoingCommunicationLimit"
- "requiresPreflightForApplicationRecord:"
- "requiresPreflightForBundleIdentifier:"
- "respondsToSelector:"
- "restartReason"
- "restrictPhoneCall"
- "retain"
- "retainCount"
- "selectedPlaylists"
- "selectedSharedAlbumCloudIdentifiers"
- "self"
- "setAdminPasscodeRecoveryAppleID:"
- "setAllowAccessibilityShortcut:"
- "setAllowPhotoCapture:"
- "setAllowPinchToZoom:"
- "setAllowSelfieCapture:"
- "setAllowSelfieVideoCapture:"
- "setAllowSiri:"
- "setAllowVideoCapture:"
- "setApplicationBundleIdentifiers:"
- "setBatteryMonitoringEnabled:"
- "setClarityBoardEnabled:"
- "setClarityBoardEnabled:error:"
- "setConversationDetailsEnabled:"
- "setEmergencyKeypadEnabled:"
- "setEmojiKeyboardEnabled:"
- "setFullScreenCompatibilityMode:"
- "setHandler:"
- "setHasMigratedFileProtections:"
- "setInCallKeypadEnabled:"
- "setIncludeSharedAlbums:"
- "setIncomingCommunicationLimit:"
- "setLegacyDialerKeypadEnabled:"
- "setLegacyIncomingCommunicationLimit:"
- "setListLayout:"
- "setLockScreenClockEnabled:"
- "setLockScreenDateEnabled:"
- "setMuteEnabled:"
- "setNeedsMigrationFor117558856:"
- "setNotificationsEnabled:"
- "setObject:forKeyedSubscript:"
- "setOneTapUnlock:"
- "setOutgoingCommunicationLimit:"
- "setOverrideNonClarityApplicationBundleIdentifiers:"
- "setPhotoKeyboardEnabled:"
- "setRecentsEnabled:"
- "setRestartReason:"
- "setRestrictPhoneCall:"
- "setSelectedPlaylists:"
- "setSelectedSharedAlbumCloudIdentifiers:"
- "setSettings:"
- "setSettingsSelector:"
- "setShouldShowTripleClickInstructions:"
- "setShowTimeInStatusBar:"
- "setSilentModeToggleEnabled:"
- "setSoftwareKeyboardEnabled:"
- "setSpeakerOptionEnabled:"
- "setSubscription:"
- "setTapToSpeakEnabled:"
- "setValue:forPreferenceKey:"
- "setVideoRecordingEnabled:"
- "setVolumeButtonsEnabled:"
- "settings"
- "settingsSelector"
- "sharedInstance"
- "sharedPhotoLibrary"
- "sharedSystemShellSwitcher"
- "shouldShowTripleClickInstructions"
- "showTimeInStatusBar"
- "signalSiriAvailability"
- "silentModeToggleEnabled"
- "softwareKeyboardEnabled"
- "speakerOptionEnabled"
- "standardBundleIdentifierForClarityBundleIdentifier:"
- "stringValue"
- "stringWithFormat:"
- "subjectMonitorRegistry"
- "subscription"
- "superclass"
- "tapToSpeakEnabled"
- "unregisterUpdateBlockForRetrieveSelector:withListenerID:"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8:16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v32@0:8@\"NSArray\"16@\"<APSubjectMonitorSubscription>\"24"
- "v32@0:8@16@24"
- "v32@0:8@?16@24"
- "valueForPreferenceKey:"
- "videoRecordingEnabled"
- "volumeButtonsEnabled"
- "writeToURL:options:error:"
- "zone"

```
