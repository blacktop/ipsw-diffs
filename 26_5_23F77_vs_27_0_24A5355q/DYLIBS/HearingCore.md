## HearingCore

> `/System/Library/PrivateFrameworks/HearingCore.framework/HearingCore`

```diff

-496.22.0.0.0
-  __TEXT.__text: 0x7ca8
-  __TEXT.__auth_stubs: 0x740
-  __TEXT.__objc_methlist: 0x7c0
-  __TEXT.__const: 0xa8
-  __TEXT.__cstring: 0xa62
-  __TEXT.__oslogstring: 0x341
-  __TEXT.__gcc_except_tab: 0x120
-  __TEXT.__unwind_info: 0x3b0
-  __TEXT.__objc_classname: 0x80
-  __TEXT.__objc_methname: 0x17df
-  __TEXT.__objc_methtype: 0x2f3
-  __TEXT.__objc_stubs: 0x1520
-  __DATA_CONST.__got: 0x1a8
-  __DATA_CONST.__const: 0x3b8
+527.0.0.0.0
+  __TEXT.__text: 0x76c0
+  __TEXT.__objc_methlist: 0x988
+  __TEXT.__const: 0xb4
+  __TEXT.__gcc_except_tab: 0xe4
+  __TEXT.__cstring: 0xb12
+  __TEXT.__oslogstring: 0x3af
+  __TEXT.__unwind_info: 0x318
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x390
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_catlist: 0x18
+  __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x728
+  __DATA_CONST.__objc_selrefs: 0x830
   __DATA_CONST.__objc_superrefs: 0x30
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__auth_got: 0x3b0
-  __AUTH_CONST.__const: 0x480
-  __AUTH_CONST.__cfstring: 0xc60
-  __AUTH_CONST.__objc_const: 0x988
+  __DATA_CONST.__got: 0x1a0
+  __AUTH_CONST.__const: 0x4a0
+  __AUTH_CONST.__cfstring: 0xd40
+  __AUTH_CONST.__objc_const: 0xb60
   __AUTH_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_ivar: 0x64
+  __AUTH_CONST.__auth_got: 0x0
+  __DATA.__objc_ivar: 0x68
+  __DATA.__data: 0xc0
   __DATA.__bss: 0x139
   __DATA_DIRTY.__objc_data: 0x230
-  __DATA_DIRTY.__bss: 0x100
+  __DATA_DIRTY.__bss: 0x110
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Accelerate

   - /System/Library/PrivateFrameworks/AXCoreUtilities.framework/AXCoreUtilities
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/NanoPreferencesSync.framework/NanoPreferencesSync
-  - /System/Library/PrivateFrameworks/NanoRegistry.framework/NanoRegistry
+  - /System/Library/PrivateFrameworks/PairedDeviceRegistry.framework/PairedDeviceRegistry
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7ACD8048-BA0F-3F45-9E54-324A5240962C
-  Functions: 282
-  Symbols:   1134
-  CStrings:  575
+  UUID: 04C35FF1-B8B7-38D0-8191-DD22DF85216E
+  Functions: 247
+  Symbols:   1080
+  CStrings:  260
 
Symbols:
+ +[HCUtilities currentProcessIsRTTExtension]
+ +[HCUtilities deviceIsVision]
+ -[HCSettings pairedWatchDidChange]
+ -[HCSettings registry:didActivate:]
+ -[HCSettings registry:didUnpair:]
+ -[HCXPCClient requestedScanning]
+ -[HCXPCClient setRequestedScanning:]
+ GCC_except_table140
+ GCC_except_table146
+ GCC_except_table164
+ GCC_except_table186
+ GCC_except_table211
+ GCC_except_table223
+ GCC_except_table228
+ GCC_except_table245
+ _AXDeviceIsRealityDevice
+ _HCHandoffUserRequested
+ _HCHearingDeviceNameKey
+ _HCHearingWidgetBundleIdentifier
+ _HCLogHearingAidWidgets
+ _HCLogHearingAidWidgets.__logObj
+ _HCLogHearingAidWidgets.onceToken
+ _HCPeerNameKey
+ _HCReasonKey
+ _OBJC_CLASS_$_PDRRegistry
+ _OBJC_IVAR_$_HCXPCClient._requestedScanning
+ __OBJC_$_PROP_LIST_NSObject
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_PDRRegistryDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject
+ __OBJC_$_PROTOCOL_METHOD_TYPES_PDRRegistryDelegate
+ __OBJC_$_PROTOCOL_REFS_PDRRegistryDelegate
+ __OBJC_CLASS_PROTOCOLS_$_HCSettings
+ __OBJC_LABEL_PROTOCOL_$_NSObject
+ __OBJC_LABEL_PROTOCOL_$_PDRRegistryDelegate
+ __OBJC_PROTOCOL_$_NSObject
+ __OBJC_PROTOCOL_$_PDRRegistryDelegate
+ ___34-[HCSettings pairedWatchDidChange]_block_invoke
+ ___43+[HCUtilities currentProcessIsRTTExtension]_block_invoke
+ ___Block_byref_object_copy_.149
+ ___Block_byref_object_copy_.252
+ ___Block_byref_object_dispose_.150
+ ___Block_byref_object_dispose_.253
+ ___HCLogHearingAidWidgets_block_invoke
+ ___block_literal_global.133
+ ___block_literal_global.14
+ ___block_literal_global.159
+ ___block_literal_global.34
+ ___error
+ _currentProcessIsRTTExtension.AXIsRTTNotificationContentExtension
+ _currentProcessIsRTTExtension.onceToken
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$addDelegate:
+ _objc_msgSend$pairedWatchDidChange
+ _objc_msgSend$sharedInstance
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x4
+ _objc_retain_x8
- +[HCUtilities bluetoothManagerQueue].cold.1
- +[HCUtilities comfortSoundsAudioQueue].cold.1
- +[HCUtilities currentProcessIsAXUIServer].cold.1
- +[HCUtilities currentProcessIsCarousel].cold.1
- +[HCUtilities currentProcessIsHealth].cold.1
- +[HCUtilities currentProcessIsHeard].cold.1
- +[HCUtilities currentProcessIsInCallService].cold.1
- +[HCUtilities currentProcessIsPreferences].cold.1
- +[HCUtilities currentProcessIsRTTExternsion]
- +[HCUtilities currentProcessIsRTTExternsion].cold.1
- +[HCUtilities currentProcessIsSpringBoard].cold.1
- +[HCUtilities currentProcessIsSystemApp].cold.1
- +[HCUtilities deviceHasHomeButton].cold.1
- +[HCUtilities deviceIsBigPhone].cold.1
- +[HCUtilities deviceIsMultiUser].cold.1
- +[HCUtilities deviceIsPad].cold.1
- +[HCUtilities deviceIsPhone].cold.1
- +[HCUtilities deviceIsPod].cold.1
- +[HCUtilities deviceIsSmallPhone].cold.1
- +[HCUtilities deviceIsWatch].cold.1
- +[HCUtilities isBTLEAudioEnabled].cold.1
- +[HCUtilities isDeviceInDeveloperMode].cold.1
- +[HCUtilities isInternalInstall].cold.1
- +[HCUtilities isLEAudioEnabled].cold.1
- +[HCUtilities supportsAlwaysListening].cold.1
- +[HCUtilities supportsLEA2].cold.1
- -[HCDatabaseManager setupDatabase].cold.1
- -[HCServer handleReply:].cold.1
- -[HCSettings _switchFromRootUserIfNecessary:].cold.1
- -[HCSettings pairedWatchDidChange:]
- -[HCXPCMessage hasEntitlement:].cold.1
- -[NSNumber(HearingCore) localizedFormat].cold.1
- GCC_except_table0
- GCC_except_table10
- GCC_except_table13
- GCC_except_table15
- GCC_except_table17
- GCC_except_table35
- _HCApplicationGetMainBundleIdentifier.cold.1
- _HCDeviceGetType.cold.1
- _HCLogAudioAccommodations.cold.1
- _HCLogComfortSounds.cold.1
- _HCLogHearing.cold.1
- _HCLogHearingAids.cold.1
- _HCLogHearingHandoff.cold.1
- _HCLogHearingLiveListen.cold.1
- _HCLogHearingNearby.cold.1
- _HCLogHearingNearbyIDS.cold.1
- _HCLogHearingProtection.cold.1
- _HCLogHearingXPC.cold.1
- _HCLogSoundMeter.cold.1
- _HCProcessGetName.cold.1
- _NRPairedDeviceRegistryDeviceDidBecomeActive
- _NRPairedDeviceRegistryDeviceDidUnpairNotification
- _OUTLINED_FUNCTION_0
- ___24-[HCServer handleReply:]_block_invoke_2.cold.1
- ___35-[HCSettings pairedWatchDidChange:]_block_invoke
- ___44+[HCUtilities currentProcessIsRTTExternsion]_block_invoke
- ___block_descriptor_56_e8_32s40s48r_e5_v8?0lr48l8s32l8s40l8
- ___block_descriptor_56_e8_32s40s48r_e5_v8?0ls32l8s40l8r48l8
- ___block_literal_global.132
- _currentProcessIsRTTExternsion.AXIsRTTNotificationContentExtension
- _currentProcessIsRTTExternsion.onceToken
- _objc_retain_x24
- _objc_retain_x25
- _objc_retain_x27
CStrings:
+ "Caught exception '%@' while performing safe block; reason: '%@'. Stack trace: %@."
+ "DeviceSupportsAlwaysListening"
+ "DosimetryAutomation"
+ "Failed to seteuid back to root: %{darwin.errno}d"
+ "Failed to seteuid to mobile user (uid %u): %{darwin.errno}d"
+ "HCHearingAidWidgets"
+ "HandoffUserRequested"
+ "HearingDeviceName"
+ "HomeButtonType"
+ "PairingOnboardingFlow"
+ "PeerName"
+ "Reason"
+ "com.apple.HearingApp.HearingWidgetExtension"
- ".cxx_destruct"
- "@"
- "@\"<AXHeardServerDelegate>\""
- "@\"<AXHeardServerMessageDelegate>\""
- "@\"HCSettings\""
- "@\"HCXPCClient\""
- "@\"NPSDomainAccessor\""
- "@\"NSDictionary\""
- "@\"NSError\""
- "@\"NSManagedObjectContext\""
- "@\"NSMutableArray\""
- "@\"NSMutableDictionary\""
- "@\"NSMutableSet\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSObject<OS_xpc_object>\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@32@0:8@16@24"
- "@32@0:8@16Q24"
- "@32@0:8d16Q24"
- "@40@0:8@16#24@32"
- "@40@0:8@16@24@32"
- "B"
- "B16@0:8"
- "B24@0:8@16"
- "B24@0:8@?16"
- "B24@0:8Q16"
- "B28@0:8@16B24"
- "B32@0:8@16@?24"
- "Caught exception '%@' while performing safe block; reason: '%@'. Stacktrace: %@."
- "HCDatabaseManager"
- "HCServer"
- "HCSettings"
- "HCSettingsListenerHelper"
- "HCUtilities"
- "HCXPCClient"
- "HCXPCMessage"
- "HearingCore"
- "JwLB44/jEB8aFDpXQ16Tuw"
- "Q"
- "Q16@0:8"
- "T@\"<AXHeardServerDelegate>\",W,N,V_delegate"
- "T@\"<AXHeardServerMessageDelegate>\",W,N,V_messageDelegate"
- "T@\"HCXPCClient\",W,N,V_client"
- "T@\"NPSDomainAccessor\",&,N,V_domainAccessor"
- "T@\"NPSDomainAccessor\",&,N,V_globalDomainAccessor"
- "T@\"NSDictionary\",&,N,V_payload"
- "T@\"NSError\",&,N,V_error"
- "T@\"NSManagedObjectContext\",&,N,V_managedObjectContext"
- "T@\"NSMutableDictionary\",&,N,V_responseBlocks"
- "T@\"NSMutableDictionary\",&,N,V_updateBlocks"
- "T@\"NSMutableSet\",&,N,V_registeredNotifications"
- "T@\"NSMutableSet\",&,N,V_synchronizePreferences"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_connectionQueue"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_nanoDomainAccessorQueue"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_xpcQueue"
- "T@\"NSObject<OS_xpc_object>\",&,N,V_xpcConnection"
- "T@\"NSObject<OS_xpc_object>\",&,N,V_xpcMessage"
- "TB,N,V_deadConnection"
- "TB,R,N"
- "TQ,N,V_requestedUpdates"
- "Ti,R,N"
- "U+73bmG4kBGj6kpreQXUTQ"
- "URLForResource:withExtension:"
- "UTF8String"
- "UUID"
- "UUIDString"
- "_client"
- "_connectionQueue"
- "_contentProtectionNotifyToken"
- "_deadConnection"
- "_delegate"
- "_domainAccessor"
- "_error"
- "_globalDomainAccessor"
- "_handlePreferenceChanged:"
- "_listenerAddress"
- "_managedObjectContext"
- "_messageDelegate"
- "_nanoDomainAccessorQueue"
- "_payload"
- "_registerForNotification:"
- "_registeredNotifications"
- "_requestedUpdates"
- "_responseBlocks"
- "_selectorKeys"
- "_switchFromRootUserIfNecessary:"
- "_syncLock"
- "_synchronizeIfNecessary:"
- "_synchronizePreferences"
- "_updateBlocks"
- "_valueForPreferenceKey:"
- "_xpcConnection"
- "_xpcMessage"
- "_xpcQueue"
- "absoluteString"
- "addObject:"
- "addObserver:selector:name:object:"
- "addSelectorKey:"
- "additionalInfoForPrefenceUpdate"
- "apsConnectionMachServiceName"
- "array"
- "arrayWithObjects:count:"
- "ax_errorWithDomain:description:"
- "bluetoothManagerQueue"
- "boolValue"
- "boolValueForPreferenceKey:withDefaultValue:"
- "bundleForClass:"
- "bundleIdentifier"
- "callStackSymbols"
- "cgfloatValueForPreferenceKey:withDefaultValue:"
- "client"
- "clientWithConnection:"
- "cloudKitContainer"
- "comfortSoundsAudioQueue"
- "connectionQueue"
- "containerIdentifier"
- "containsObject:"
- "contentDidUpdate:"
- "contentDidUpdateRemotely:"
- "controllerInfoAndReturnError:"
- "copy"
- "copyXPCMessageFromDictionary:inReplyToXPCMessage:error:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "currentProcessIsAXUIServer"
- "currentProcessIsCarousel"
- "currentProcessIsHealth"
- "currentProcessIsHeard"
- "currentProcessIsInCallService"
- "currentProcessIsPreferences"
- "currentProcessIsRTTExternsion"
- "currentProcessIsSpringBoard"
- "currentProcessIsSystemApp"
- "d24@0:8d16"
- "d32@0:8@16d24"
- "databaseFilePath"
- "deadConnection"
- "dealloc"
- "defaultCenter"
- "delegate"
- "description"
- "deviceHasHomeButton"
- "deviceIsBigPhone"
- "deviceIsMultiUser"
- "deviceIsPad"
- "deviceIsPhone"
- "deviceIsPod"
- "deviceIsSmallPhone"
- "deviceIsWatch"
- "dictionary"
- "dictionaryFromXPCMessage:error:"
- "dictionaryWithDictionary:"
- "dictionaryWithObjects:forKeys:count:"
- "domainAccessor"
- "doubleValue"
- "enumerateObjectsUsingBlock:"
- "error"
- "fileURLWithPath:"
- "floatChannelData"
- "frameLength"
- "globalDomainAccessor"
- "handleMessageError:destructive:"
- "handleMessageWithPayload:forIdentifier:"
- "handleReply:"
- "hasChanges"
- "hasEntitlement:"
- "hcSafeAddObject:"
- "hearingServerDidDie:"
- "i"
- "i16@0:8"
- "indexesOfObjectsPassingTest:"
- "init"
- "initWithConnection:"
- "initWithContainerIdentifier:"
- "initWithContentsOfURL:"
- "initWithDomain:"
- "initWithFormat:"
- "initWithListenerAddress:andDelegate:"
- "initWithName:managedObjectModel:"
- "initWithOptions:"
- "initWithPayload:"
- "initWithURL:"
- "integerValue"
- "integerValueForKey:withDefaultValue:"
- "isBTLEAudioEnabled"
- "isConnected"
- "isDeviceInDeveloperMode"
- "isEqual:"
- "isEqualToString:"
- "isInternalInstall"
- "isLEAudioEnabled"
- "isProtectedDataAvailable"
- "keysMonitoredForUpdates"
- "keysToSync"
- "lastObject"
- "leaVersion"
- "length"
- "loadPersistentStoresWithCompletionHandler:"
- "localizedFormat"
- "logMessage:"
- "magnitudesWithLevelMultiplier:count:"
- "mainBundle"
- "managedObjectContext"
- "managedObjectModelName"
- "mergeChangesFromContextDidSaveNotification:"
- "messageDelegate"
- "messagePayloadFromDictionary:andIdentifier:"
- "messageWithPayload:"
- "messageWithPayload:xpcMessage:andClient:"
- "name"
- "nanoDomainAccessor"
- "nanoDomainAccessorQueue"
- "nanoPreferenceDomain"
- "notificationForPreferenceKey:"
- "now"
- "numberWithDouble:"
- "numberWithUnsignedLongLong:"
- "objectAtIndexedSubscript:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "objectValueForKey:withClass:andDefaultValue:"
- "pairedWatchDidChange:"
- "payload"
- "performBlock:"
- "performBlockAndWait:"
- "persistentStoreCoordinator"
- "persistentStores"
- "pid"
- "preferenceDomainForPreferenceKey:"
- "preferenceKeyForSelector:"
- "processInfo"
- "processName"
- "q16@0:8"
- "q32@0:8@16q24"
- "reason"
- "registerUpdateBlock:forRetrieveSelector:withListener:"
- "registeredNotifications"
- "removeObject:"
- "removeObjectForKey:"
- "removeObjectsAtIndexes:"
- "removeObserver:"
- "replyMessageWithPayload:"
- "requestedUpdates"
- "reset"
- "resetConnection"
- "resetValueForSelector:"
- "responseBlocks"
- "roundToPercentageValue:"
- "save:"
- "saveIfPossible"
- "saveUpdateInfoIfNeededForPreferenceKey:toDomain:"
- "sendMessage:errorBlock:"
- "sendMessageWithPayload:andIdentifier:"
- "sendMessageWithPayload:identifier:andResponseBlock:"
- "sendSynchronousMessageWithPayload:andIdentifier:"
- "sendSynchronousMessageWithPayloadAndGetResponse:andIdentifier:"
- "set"
- "setApsConnectionMachServiceName:"
- "setClient:"
- "setCloudKitContainerOptions:"
- "setConnectionQueue:"
- "setDateFormat:"
- "setDeadConnection:"
- "setDelegate:"
- "setDomainAccessor:"
- "setError:"
- "setGlobalDomainAccessor:"
- "setManagedObjectContext:"
- "setMessageDelegate:"
- "setMirroringDelegate:"
- "setNanoDomainAccessorQueue:"
- "setObject:forKey:"
- "setOption:forKey:"
- "setPayload:"
- "setPersistentStoreDescriptions:"
- "setRegisteredNotifications:"
- "setRequestedUpdates:"
- "setResponseBlocks:"
- "setSynchronizePreferences:"
- "setUpdateBlocks:"
- "setUseDeviceToDeviceEncryption:"
- "setValue:forKey:"
- "setValue:forPreferenceKey:"
- "setWantsUpdates:forIdentifier:"
- "setWithArray:"
- "setXpcConnection:"
- "setXpcMessage:"
- "setXpcQueue:"
- "setupDatabase"
- "setupServerIfNecessary"
- "shouldRestartOnInterruption:"
- "shouldSaveUpdateInfoForPreferenceKey:"
- "shouldStoreLocally"
- "startServerAndBoostPriority"
- "startServerWithDelegate:"
- "storesWillChange:"
- "stringByAppendingPathComponent:"
- "stringByAppendingPathExtension:"
- "stringByReplacingOccurrencesOfString:withString:"
- "stringFromDate:"
- "stringFromNumber:"
- "stringWithFormat:"
- "supportsAlwaysListening"
- "supportsLEA2"
- "synchronize"
- "synchronizeNanoDomain:keys:"
- "synchronizePreferences"
- "systemBootTime"
- "teardownConnection"
- "terminateConnectionAndNotify:"
- "unsignedLongLongValue"
- "updateBlocks"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8:16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8Q16"
- "v28@0:8@16B24"
- "v28@0:8B16Q20"
- "v32@0:8@16@24"
- "v32@0:8@16Q24"
- "v32@0:8@16^{__CFString=}24"
- "v40@0:8@16Q24@?32"
- "v40@0:8@?16:24@32"
- "valueForKey:"
- "viewContext"
- "wantsUpdatesForIdentifier:"
- "watchSupportsPairingHearingAids"
- "xpcConnection"
- "xpcMessage"
- "xpcQueue"
- "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"

```
