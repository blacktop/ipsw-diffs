## HearingUtilities

> `/System/Library/PrivateFrameworks/HearingUtilities.framework/HearingUtilities`

```diff

-403.0.0.0.0
-  __TEXT.__text: 0x7ba00
-  __TEXT.__auth_stubs: 0xd10
-  __TEXT.__objc_methlist: 0x5658
+406.1.3.0.0
+  __TEXT.__text: 0x7dd6c
+  __TEXT.__auth_stubs: 0xd20
+  __TEXT.__objc_methlist: 0x5870
   __TEXT.__const: 0x1a8
-  __TEXT.__gcc_except_tab: 0x1968
-  __TEXT.__cstring: 0xa734
-  __TEXT.__oslogstring: 0x187c
-  __TEXT.__dlopen_cstrs: 0x532
-  __TEXT.__unwind_info: 0x1b18
-  __TEXT.__objc_classname: 0x69d
-  __TEXT.__objc_methname: 0xe9e7
-  __TEXT.__objc_methtype: 0x1ae3
-  __TEXT.__objc_stubs: 0xae20
+  __TEXT.__gcc_except_tab: 0x1a3c
+  __TEXT.__cstring: 0xabc2
+  __TEXT.__oslogstring: 0x1a1a
+  __TEXT.__dlopen_cstrs: 0x4dc
+  __TEXT.__unwind_info: 0x1b64
+  __TEXT.__objc_classname: 0x6ca
+  __TEXT.__objc_methname: 0xf09b
+  __TEXT.__objc_methtype: 0x1b48
+  __TEXT.__objc_stubs: 0xb0e0
   __DATA_CONST.__got: 0x248
-  __DATA_CONST.__const: 0x2588
-  __DATA_CONST.__objc_classlist: 0x178
+  __DATA_CONST.__const: 0x25a0
+  __DATA_CONST.__objc_classlist: 0x180
   __DATA_CONST.__objc_catlist: 0x28
-  __DATA_CONST.__objc_protolist: 0xa8
+  __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xc138
-  __DATA_CONST.__objc_selrefs: 0x3430
-  __DATA_CONST.__objc_arraydata: 0x310
-  __AUTH_CONST.__const: 0xa00
-  __AUTH_CONST.__cfstring: 0x70c0
-  __AUTH_CONST.__objc_const: 0x1580
+  __DATA_CONST.__objc_const: 0xc730
+  __DATA_CONST.__objc_selrefs: 0x3540
+  __DATA_CONST.__objc_arraydata: 0x330
+  __AUTH_CONST.__const: 0x9c0
+  __AUTH_CONST.__cfstring: 0x74a0
+  __AUTH_CONST.__objc_const: 0x15c8
   __AUTH_CONST.__objc_intobj: 0x738
   __AUTH_CONST.__objc_arrayobj: 0x198
-  __AUTH_CONST.__objc_dictobj: 0x2f8
+  __AUTH_CONST.__objc_dictobj: 0x348
   __AUTH_CONST.__objc_doubleobj: 0x1450
-  __AUTH_CONST.__auth_got: 0x698
-  __AUTH.__objc_data: 0xc80
-  __DATA.__objc_classrefs: 0x350
-  __DATA.__objc_superrefs: 0x158
-  __DATA.__objc_ivar: 0x730
-  __DATA.__data: 0x980
-  __DATA.__bss: 0x218
+  __AUTH_CONST.__auth_got: 0x6a0
+  __AUTH.__objc_data: 0xcd0
+  __DATA.__objc_classrefs: 0x340
+  __DATA.__objc_superrefs: 0x160
+  __DATA.__objc_ivar: 0x760
+  __DATA.__data: 0x9e0
+  __DATA.__bss: 0x210
   __DATA_DIRTY.__objc_data: 0x230
-  __DATA_DIRTY.__bss: 0x138
+  __DATA_DIRTY.__bss: 0x130
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 5F2075AC-3DEC-3BE9-A486-86B37E2C9687
-  Functions: 2567
-  Symbols:   8611
-  CStrings:  5090
+  UUID: 1E1D2DFE-C4AF-3380-B091-5A50243868BA
+  Functions: 2617
+  Symbols:   8757
+  CStrings:  5234
 
Symbols:
+ -[AXHALiveListenController _connectUnits]
+ -[AXHALiveListenController _setupAudioUnitsWithAudioFormat:]
+ -[AXHALiveListenController _setupMixerUnitWithAudioFormat:]
+ -[AXHALiveListenController _setupRioUnitWithAudioFormat:]
+ -[AXHALiveListenController _setupSession]
+ -[AXHALiveListenController startListeningWithCompletion:]
+ -[AXHALiveListenController stopListeningWithCompletion:]
+ -[AXHAServer _registerUpdateBlock:forIdentifier:listenerHash:]
+ -[AXHAServer registerUpdateBlock:forIdentifier:withListener:]
+ -[AXHAServer registerUpdateBlock:forIdentifier:withListener:listenerHash:]
+ -[AXHAServer unregisterLiveListenLevelListener:]
+ -[AXHAServer unregisterLiveListenListener:]
+ -[HUAccessoryHearingSyncManager listeningModesChangedState:]
+ -[HUAccessoryHearingSyncManager persistentDeviceListeningState]
+ -[HUAccessoryHearingSyncManager setPersistentDeviceListeningState:]
+ -[HUAccessoryHearingSyncManager setWatchListeningState:]
+ -[HUAccessoryHearingSyncManager watchListeningState]
+ -[HUComfortSoundsController blankScreenToken]
+ -[HUComfortSoundsController deviceScreenStatusDidChange:systemLocked:]
+ -[HUComfortSoundsController isDeviceLockedWithPasscode]
+ -[HUComfortSoundsController isScreenBlank]
+ -[HUComfortSoundsController keybagLockStateToken]
+ -[HUComfortSoundsController lockStateNotifyToken]
+ -[HUComfortSoundsController registerHasBlankedScreenNotification]
+ -[HUComfortSoundsController setBlankScreenToken:]
+ -[HUComfortSoundsController setIsDeviceLockedWithPasscode:]
+ -[HUComfortSoundsController setIsScreenBlank:]
+ -[HUComfortSoundsController setKeybagLockStateToken:]
+ -[HUComfortSoundsController setLockStateNotifyToken:]
+ -[HUNearbyController availableWatches]
+ -[HUNearbyController logNearbyDevices:withTitle:]
+ -[HUNearbyController processIDSDevices:]
+ -[HUNearbyController sendMessageToWatchDevices:toDevicesWithDomain:withPriority:]
+ -[HUNearbyController service:activeAccountsChanged:]
+ -[HUNearbyController service:devicesChanged:]
+ -[HUNearbyDevice isWatch]
+ -[HUNearbyHearingAidController descriptionForHandoffReason:]
+ -[HUNearbyHearingAidController handleSessionMessage:]
+ -[HUNearbyHearingAidController processingConnection]
+ -[HUNearbyHearingAidController processingTransition]
+ -[HUNearbyHearingAidController resetHandoff]
+ -[HUNearbyHearingAidController sessionManager]
+ -[HUNearbyHearingAidController setProcessingConnection:]
+ -[HUNearbyHearingAidController setProcessingTransition:]
+ -[HUNearbyHearingAidController setSessionManager:]
+ -[HUSessionManager .cxx_destruct]
+ -[HUSessionManager dealloc]
+ -[HUSessionManager delegate]
+ -[HUSessionManager init]
+ -[HUSessionManager registerForSessionNotifications]
+ -[HUSessionManager setDelegate:]
+ -[HUSessionManager unregisterForSessionNotifications]
+ -[HUSessionManager userLoggedOut:]
+ GCC_except_table31
+ GCC_except_table55
+ _AXCFormattedString
+ _OBJC_CLASS_$_HUSessionManager
+ _OBJC_IVAR_$_AXHALiveListenController._audioUnitsQueue
+ _OBJC_IVAR_$_HUAccessoryHearingSyncManager._persistentDeviceListeningState
+ _OBJC_IVAR_$_HUAccessoryHearingSyncManager._watchListeningState
+ _OBJC_IVAR_$_HUComfortSoundsController._blankScreenToken
+ _OBJC_IVAR_$_HUComfortSoundsController._isDeviceLockedWithPasscode
+ _OBJC_IVAR_$_HUComfortSoundsController._isScreenBlank
+ _OBJC_IVAR_$_HUComfortSoundsController._keybagLockStateToken
+ _OBJC_IVAR_$_HUComfortSoundsController._lockStateNotifyToken
+ _OBJC_IVAR_$_HUNearbyController._availableWatches
+ _OBJC_IVAR_$_HUNearbyHearingAidController._processingConnection
+ _OBJC_IVAR_$_HUNearbyHearingAidController._processingTransition
+ _OBJC_IVAR_$_HUNearbyHearingAidController._sessionManager
+ _OBJC_IVAR_$_HUSessionManager._delegate
+ _OBJC_METACLASS_$_HUSessionManager
+ __OBJC_$_INSTANCE_METHODS_HUSessionManager
+ __OBJC_$_INSTANCE_VARIABLES_HUSessionManager
+ __OBJC_$_PROP_LIST_HUSessionManager
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_HUSessionManagerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HUSessionManagerDelegate
+ __OBJC_$_PROTOCOL_REFS_HUSessionManagerDelegate
+ __OBJC_CLASS_PROTOCOLS_$_HUNearbyHearingAidController
+ __OBJC_CLASS_RO_$_HUSessionManager
+ __OBJC_LABEL_PROTOCOL_$_HUSessionManagerDelegate
+ __OBJC_METACLASS_RO_$_HUSessionManager
+ __OBJC_PROTOCOL_$_HUSessionManagerDelegate
+ ___37-[HUNearbyHearingAidController start]_block_invoke.107
+ ___37-[HUNearbyHearingAidController start]_block_invoke_2.108
+ ___40-[HUNearbyController processIDSDevices:]_block_invoke
+ ___40-[HUNearbyController processIDSDevices:]_block_invoke_2
+ ___40-[HUNearbyController processIDSDevices:]_block_invoke_3
+ ___42-[HUNearbyController setAvailableDevices:]_block_invoke
+ ___43-[AXHAServer comfortSoundsAssetsDidUpdate:]_block_invoke.140
+ ___44-[HUNearbyHearingAidController resetHandoff]_block_invoke
+ ___54-[HUNearbyHearingAidController requestHandoffForMedia]_block_invoke.44
+ ___56-[AXHALiveListenController stopListeningWithCompletion:]_block_invoke
+ ___56-[HUAccessoryHearingSyncManager listeningModeDidChange:]_block_invoke.108
+ ___57-[AXHALiveListenController startListeningWithCompletion:]_block_invoke
+ ___57-[HUNearbyHearingAidController device:didReceiveMessage:]_block_invoke.156
+ ___59-[HUNearbyHearingAidController requestConnectionForReason:]_block_invoke.57
+ ___60-[HUAccessoryHearingSyncManager listeningModesChangedState:]_block_invoke
+ ___60-[HUAccessoryHearingSyncManager listeningModesChangedState:]_block_invoke.147
+ ___60-[HUAccessoryHearingSyncManager listeningModesChangedState:]_block_invoke.154
+ ___62-[AXHAServer _registerUpdateBlock:forIdentifier:listenerHash:]_block_invoke
+ ___65-[HUComfortSoundsController registerHasBlankedScreenNotification]_block_invoke
+ ___65-[HUComfortSoundsController registerHasBlankedScreenNotification]_block_invoke.103
+ ___65-[HUComfortSoundsController registerHasBlankedScreenNotification]_block_invoke.107
+ ___67-[HUAccessoryHearingSyncManager _registerForNearbyControllerUpdate]_block_invoke.102
+ ___67-[HUAccessoryHearingSyncManager _registerForNearbyControllerUpdate]_block_invoke.83
+ ___67-[HUAccessoryHearingSyncManager _registerForNearbyControllerUpdate]_block_invoke.93
+ ___67-[HUAccessoryHearingSyncManager _registerForNearbyControllerUpdate]_block_invoke_2.97
+ ___67-[HUNearbyController sendMessage:toDevicesWithDomain:withPriority:]_block_invoke
+ ___68-[HUNearbyHearingAidController checkConnectionRequestedAfterTimeout]_block_invoke.46
+ ___68-[HUNearbyHearingAidController checkConnectionRequestedAfterTimeout]_block_invoke_2
+ ___69-[HUNearbyLiveListenControllerPhone _stopLiveListenFromRemoteDevice:]_block_invoke
+ ___69-[HUNearbyLiveListenControllerPhone _stopLiveListenFromRemoteDevice:]_block_invoke.cold.1
+ ___70-[HUNearbyLiveListenControllerPhone _startLiveListenFromRemoteDevice:]_block_invoke
+ ___70-[HUNearbyLiveListenControllerPhone _startLiveListenFromRemoteDevice:]_block_invoke.cold.1
+ ___71-[HUNearbyHearingAidController checkConnectionRelinquishedAfterTimeout]_block_invoke.71
+ ___74-[AXHAServer registerUpdateBlock:forIdentifier:withListener:listenerHash:]_block_invoke
+ ___81-[HUNearbyController sendMessageToWatchDevices:toDevicesWithDomain:withPriority:]_block_invoke
+ ___block_descriptor_48_e8_32s40s_e20_v20?0B8"NSError"12ls32l8s40l8
+ ___block_descriptor_56_e8_32s40bs_e5_v8?0ls32l8s40l8
+ ___block_descriptor_64_e5_v8?0l
+ ___block_descriptor_76_e8_32s40s48s56s_e5_v8?0ls32l8s40l8s48l8s56l8
+ ___block_literal_global.104
+ ___block_literal_global.158
+ ___block_literal_global.19
+ ___block_literal_global.231
+ ___block_literal_global.32
+ ___block_literal_global.329
+ ___block_literal_global.96
+ ___getCallStatus_block_invoke
+ ___getCallStatus_block_invoke_2
+ __unnamed_array_storage.108
+ __unnamed_array_storage.112
+ __unnamed_array_storage.129
+ __unnamed_array_storage.130
+ __unnamed_array_storage.133
+ __unnamed_array_storage.134
+ __unnamed_array_storage.145
+ __unnamed_array_storage.146
+ _getCallStatus
+ _objc_msgSend$_connectUnits
+ _objc_msgSend$_registerUpdateBlock:forIdentifier:listenerHash:
+ _objc_msgSend$_setupAudioUnitsWithAudioFormat:
+ _objc_msgSend$_setupMixerUnitWithAudioFormat:
+ _objc_msgSend$_setupRioUnitWithAudioFormat:
+ _objc_msgSend$_setupSession
+ _objc_msgSend$availableWatches
+ _objc_msgSend$deviceScreenStatusDidChange:systemLocked:
+ _objc_msgSend$handleSessionMessage:
+ _objc_msgSend$hearingAidsIsLEA2:
+ _objc_msgSend$isDeviceLockedWithPasscode
+ _objc_msgSend$isScreenBlank
+ _objc_msgSend$isWatch
+ _objc_msgSend$listeningModesChangedState:
+ _objc_msgSend$logNearbyDevices:withTitle:
+ _objc_msgSend$persistentDeviceListeningState
+ _objc_msgSend$processIDSDevices:
+ _objc_msgSend$processingConnection
+ _objc_msgSend$processingTransition
+ _objc_msgSend$registerForSessionNotifications
+ _objc_msgSend$registerHasBlankedScreenNotification
+ _objc_msgSend$registerUpdateBlock:forIdentifier:withListener:
+ _objc_msgSend$registerUpdateBlock:forIdentifier:withListener:listenerHash:
+ _objc_msgSend$rioUnit
+ _objc_msgSend$sendMessageToWatchDevices:toDevicesWithDomain:withPriority:
+ _objc_msgSend$service:devicesChanged:
+ _objc_msgSend$session
+ _objc_msgSend$setPersistentDeviceListeningState:
+ _objc_msgSend$setProcessingConnection:
+ _objc_msgSend$setProcessingTransition:
+ _objc_msgSend$setWatchListeningState:
+ _objc_msgSend$startListeningWithCompletion:
+ _objc_msgSend$stopListeningWithCompletion:
+ _objc_msgSend$unregisterForSessionNotifications
+ _objc_msgSend$watchListeningState
+ _objc_setProperty_atomic_copy
- -[AXHALiveListenController startListeningWithError:]
- -[AXHALiveListenController stopListeningWithError:]
- -[AXHAServer _registerUpdateBlock:forIdentier:listenerHash:]
- -[AXHAServer registerUpdateBlock:forIdentier:withListener:]
- -[AXHAServer registerUpdateBlock:forIdentier:withListener:listenerHash:]
- -[HUNearbyDevice representsAWatch]
- -[HUNearbyHearingAidController processingHandoff]
- -[HUNearbyHearingAidController setProcessingHandoff:]
- -[HUNearbyHearingAidController systemStatusDidChange:]
- -[HUNearbyLiveListenControllerPhone _startLiveListenFromRemoteDevice:].cold.1
- -[HUNearbyLiveListenControllerPhone _stopLiveListenFromRemoteDevice:].cold.1
- GCC_except_table30
- GCC_except_table36
- _OBJC_CLASS_$_NSDateComponents
- _OBJC_CLASS_$_NSDateComponentsFormatter
- _OBJC_IVAR_$_HUNearbyHearingAidController._processingHandoff
- ___33-[HUComfortSoundsController init]_block_invoke.67
- ___37-[HUNearbyHearingAidController start]_block_invoke.93
- ___37-[HUNearbyHearingAidController start]_block_invoke_2.101
- ___43-[AXHAServer comfortSoundsAssetsDidUpdate:]_block_invoke.132
- ___43-[HUComfortSoundsController hasCurrentCall]_block_invoke
- ___43-[HUComfortSoundsController hasCurrentCall]_block_invoke_2
- ___51-[AXHALiveListenController stopListeningWithError:]_block_invoke
- ___51-[HUNearbyController service:nearbyDevicesChanged:]_block_invoke
- ___51-[HUNearbyController service:nearbyDevicesChanged:]_block_invoke_2
- ___51-[HUNearbyController service:nearbyDevicesChanged:]_block_invoke_3
- ___52-[HUNearbyHearingAidController callStatusDidChange:]_block_invoke_2
- ___52-[HUNearbyHearingAidController callStatusDidChange:]_block_invoke_3
- ___54-[HUNearbyHearingAidController requestHandoffForMedia]_block_invoke.53
- ___56-[HUAccessoryHearingSyncManager listeningModeDidChange:]_block_invoke.102
- ___57-[HUNearbyHearingAidController device:didReceiveMessage:]_block_invoke.155
- ___59-[HUNearbyHearingAidController requestConnectionForReason:]_block_invoke.66
- ___60-[AXHAServer _registerUpdateBlock:forIdentier:listenerHash:]_block_invoke
- ___67-[HUAccessoryHearingSyncManager _registerForNearbyControllerUpdate]_block_invoke.80
- ___67-[HUAccessoryHearingSyncManager _registerForNearbyControllerUpdate]_block_invoke.87
- ___67-[HUAccessoryHearingSyncManager _registerForNearbyControllerUpdate]_block_invoke.96
- ___67-[HUAccessoryHearingSyncManager _registerForNearbyControllerUpdate]_block_invoke_2.91
- ___68-[HUNearbyHearingAidController checkConnectionRequestedAfterTimeout]_block_invoke.55
- ___68-[HUNearbyHearingAidController shouldRelinquishConnectionForReason:]_block_invoke
- ___68-[HUNearbyHearingAidController shouldRelinquishConnectionForReason:]_block_invoke_2
- ___71-[HUNearbyHearingAidController checkConnectionRelinquishedAfterTimeout]_block_invoke.85
- ___72-[AXHAServer registerUpdateBlock:forIdentier:withListener:listenerHash:]_block_invoke
- ___block_descriptor_32_e8_v12?0i8l
- ___block_descriptor_56_e8_32r40r48r_e5_v8?0lr32l8r40l8r48l8
- ___block_descriptor_64_e8_32r40r48r56r_e5_v8?0lr32l8r40l8r48l8r56l8
- ___block_descriptor_72_e8_32s40s48s56s_e5_v8?0ls32l8s40l8s48l8s56l8
- ___block_literal_global.157
- ___block_literal_global.18
- ___block_literal_global.212
- ___block_literal_global.304
- ___block_literal_global.49
- ___block_literal_global.70
- ___block_literal_global.72
- ___block_literal_global.89
- __unnamed_array_storage.110
- __unnamed_array_storage.114
- __unnamed_array_storage.137
- __unnamed_array_storage.138
- _objc_autorelease
- _objc_msgSend$_registerUpdateBlock:forIdentier:listenerHash:
- _objc_msgSend$localizedStringFromDateComponents:unitsStyle:
- _objc_msgSend$localizedStringWithFormat:
- _objc_msgSend$processingHandoff
- _objc_msgSend$registerUpdateBlock:forIdentier:withListener:
- _objc_msgSend$registerUpdateBlock:forIdentier:withListener:listenerHash:
- _objc_msgSend$representsAWatch
- _objc_msgSend$service:nearbyDevicesChanged:
- _objc_msgSend$setHour:
- _objc_msgSend$setMinute:
- _objc_msgSend$setProcessingHandoff:
- _objc_msgSend$startListeningWithError:
- _objc_msgSend$stopListeningWithError:
CStrings:
+ "\x04\x8a"
+ "\x06"
+ "\x11b"
+ "\x1a"
+ "%1$d"
+ "%1$d%2$d"
+ "%d"
+ "-[AXHALiveListenController startListeningWithCompletion:]_block_invoke"
+ "-[AXHALiveListenController stopListeningWithCompletion:]_block_invoke"
+ "-[HUAccessoryHearingSyncManager listeningModesChangedState:]"
+ "-[HUAccessoryHearingSyncManager listeningModesChangedState:]_block_invoke"
+ "-[HUComfortSoundsController deviceScreenStatusDidChange:systemLocked:]"
+ "-[HUComfortSoundsController registerHasBlankedScreenNotification]"
+ "-[HUComfortSoundsController registerHasBlankedScreenNotification]_block_invoke"
+ "3\x14"
+ "@\"<HUSessionManagerDelegate>\""
+ "@\"HUSessionManager\""
+ "@56@0:8{AudioStreamBasicDescription=dIIIIIIII}16"
+ "Added listening mode %@, for device: %@"
+ "Connection processing has been finished"
+ "Devices changed"
+ "Discovered new devices count: %@"
+ "HUSessionManager"
+ "HUSessionManagerDelegate"
+ "Handled device lock with passcode: %@ %@"
+ "Handled keybag lock: %@ %@"
+ "Handled screen wake: %@ %@"
+ "Headphone Selected %d, Listening modes Watch saved: %@, new: %@"
+ "Headphone is selected, processing Accessory info"
+ "IDS sent message: %@, GUID: %@"
+ "LIMIT_100DB"
+ "LIMIT_80DB"
+ "LIMIT_85DB"
+ "LIMIT_90DB"
+ "LIMIT_95DB"
+ "Listening modes added AccessoryChangeWatch"
+ "Listening modes changed AccessoryChangeAll"
+ "Listening modes current: %@ new: %@"
+ "Listening modes no changes AccessoryChangeNone"
+ "Listening modes persistent: %@ new: %@"
+ "Listening modes removed AccessoryChangeWatch"
+ "New devices"
+ "Phone call [pending = %d, active = %d, avc = %d, endpoint = %d] - [connected = %d, should request = %d] - %@"
+ "Process IDS Devices"
+ "Registered blank screen state: %@ %@"
+ "Registered keybag lock state: %@ %@"
+ "Registered lock screen state: %@ %@"
+ "Removed listening mode %@, for device: %@"
+ "Reset Transitioning State"
+ "Saved devices"
+ "Screen blank status has changed - %d, %d, %d"
+ "Sending Accessory state message to discovered devices: %@"
+ "Sending to Watches Accessory state message: %@"
+ "Sending to all Accessory state message: %@"
+ "Set listening mode %@, for device: %@"
+ "Should relinquish: %d Reason: %@, Call: [pending: %d, active: %d, endpoint: %d]"
+ "System status has changed userLoggedOut: %@"
+ "T@\"<HUSessionManagerDelegate>\",W,N,V_delegate"
+ "T@\"AXHearingAidMode\",&,VcurrentLeftProgram"
+ "T@\"AXHearingAidMode\",&,VcurrentLeftStreamingProgram"
+ "T@\"AXHearingAidMode\",&,VcurrentRightProgram"
+ "T@\"AXHearingAidMode\",&,VcurrentRightStreamingProgram"
+ "T@\"CBPeripheral\",&,VleftPeripheral"
+ "T@\"CBPeripheral\",&,VrightPeripheral"
+ "T@\"HUSessionManager\",&,N,V_sessionManager"
+ "T@\"NSArray\",C,V_leftPrograms"
+ "T@\"NSArray\",C,V_rightPrograms"
+ "T@\"NSArray\",C,VleftPrograms"
+ "T@\"NSArray\",C,VrightPrograms"
+ "T@\"NSArray\",R,C"
+ "T@\"NSArray\",R,N,V_availableWatches"
+ "T@\"NSDate\",&,V_leftBatteryLowDate"
+ "T@\"NSDate\",&,V_rightBatteryLowDate"
+ "T@\"NSDate\",R,&"
+ "T@\"NSDictionary\",&,N,V_watchListeningState"
+ "T@\"NSMutableArray\",&,V_manufacturer"
+ "T@\"NSMutableArray\",&,V_model"
+ "T@\"NSMutableArray\",&,Vmanufacturer"
+ "T@\"NSMutableArray\",&,Vmodel"
+ "T@\"NSMutableArray\",R,&"
+ "T@\"NSMutableDictionary\",&,N,V_persistentDeviceListeningState"
+ "T@\"NSMutableDictionary\",&,VleftPropertiesLoadCount"
+ "T@\"NSMutableDictionary\",&,VrightPropertiesLoadCount"
+ "T@\"NSString\",&,V_leftFirmwareVersion"
+ "T@\"NSString\",&,V_leftHardwareVersion"
+ "T@\"NSString\",&,V_leftPeripheralUUID"
+ "T@\"NSString\",&,V_leftUUID"
+ "T@\"NSString\",&,V_name"
+ "T@\"NSString\",&,V_rightFirmwareVersion"
+ "T@\"NSString\",&,V_rightHardwareVersion"
+ "T@\"NSString\",&,V_rightPeripheralUUID"
+ "T@\"NSString\",&,V_rightUUID"
+ "T@\"NSString\",&,VleftFirmwareVersion"
+ "T@\"NSString\",&,VleftHardwareVersion"
+ "T@\"NSString\",&,VleftPeripheralUUID"
+ "T@\"NSString\",&,VleftUUID"
+ "T@\"NSString\",&,Vname"
+ "T@\"NSString\",&,VrightFirmwareVersion"
+ "T@\"NSString\",&,VrightHardwareVersion"
+ "T@\"NSString\",&,VrightPeripheralUUID"
+ "T@\"NSString\",&,VrightUUID"
+ "T@\"NSString\",R,&"
+ "TB,N,V_isDeviceLockedWithPasscode"
+ "TB,N,V_isScreenBlank"
+ "TB,V_processingConnection"
+ "TB,V_processingTransition"
+ "TB,VisListening"
+ "The device is locked. Comfort sounds should stop on lock"
+ "Ti,N,V_blankScreenToken"
+ "Ti,N,V_keybagLockStateToken"
+ "Ti,N,V_lockStateNotifyToken"
+ "Transition processing has been finished"
+ "Updated nearbyDevicesListeningState: %@"
+ "UserRequested"
+ "_audioUnitsQueue"
+ "_availableWatches"
+ "_blankScreenToken"
+ "_connectUnits"
+ "_isDeviceLockedWithPasscode"
+ "_isScreenBlank"
+ "_keybagLockStateToken"
+ "_lockStateNotifyToken"
+ "_persistentDeviceListeningState"
+ "_processingConnection"
+ "_processingTransition"
+ "_registerUpdateBlock:forIdentifier:listenerHash:"
+ "_sessionManager"
+ "_setupAudioUnitsWithAudioFormat:"
+ "_setupMixerUnitWithAudioFormat:"
+ "_setupRioUnitWithAudioFormat:"
+ "_setupSession"
+ "_watchListeningState"
+ "activeAccountsChanged: %@"
+ "availableWatches"
+ "blankScreenToken"
+ "ccom.apple.springboard.passcodeLockedOrBlocked"
+ "com.apple.mobile.keybagd.lock_status"
+ "com.apple.springboard.hasBlankedScreen"
+ "connectedPeer: %@, Reachable HA: %@, isConnected: %@, audioReachable: %@"
+ "deviceScreenStatusDidChange:systemLocked:"
+ "ha_livelisten_audiounits_queue"
+ "handleSessionMessage:"
+ "isDeviceLockedWithPasscode"
+ "isScreenBlank"
+ "isWatch"
+ "keybagLockStateToken"
+ "listeningModesChangedState:"
+ "lockStateNotifyToken"
+ "logNearbyDevices:withTitle:"
+ "persistentDeviceListeningState"
+ "processIDSDevices:"
+ "processingConnection"
+ "processingTransition"
+ "registerForSessionNotifications"
+ "registerHasBlankedScreenNotification"
+ "registerUpdateBlock:forIdentifier:withListener:"
+ "registerUpdateBlock:forIdentifier:withListener:listenerHash:"
+ "resetHandoff"
+ "screenUnlocked - Sending ControllerConnected: %@"
+ "sendMessageToWatchDevices:toDevicesWithDomain:withPriority:"
+ "sessionManager"
+ "setBlankScreenToken:"
+ "setIsDeviceLockedWithPasscode:"
+ "setIsScreenBlank:"
+ "setKeybagLockStateToken:"
+ "setLockStateNotifyToken:"
+ "setPersistentDeviceListeningState:"
+ "setProcessingConnection:"
+ "setProcessingTransition:"
+ "setSessionManager:"
+ "setWatchListeningState:"
+ "startListeningWithCompletion:"
+ "stopListeningWithCompletion:"
+ "unregisterForSessionNotifications"
+ "unregisterLiveListenLevelListener:"
+ "unregisterLiveListenListener:"
+ "userLoggedOut:"
+ "v24@0:8i16i20"
+ "watchListeningState"
- "\x04j"
- "\x19"
- "%d - [%d, %d, %d]"
- "-[AXHALiveListenController startListeningWithError:]"
- "-[AXHALiveListenController stopListeningWithError:]"
- "-[HUNearbyHearingAidController callStatusDidChange:]"
- "-[HUNearbyHearingAidController callStatusDidChange:]_block_invoke"
- "-[HUNearbyHearingAidController shouldRelinquishConnectionForReason:]"
- "-[HUNearbyHearingAidController stop]"
- "3\x13"
- "B24@0:8^@16"
- "Current listening modes %@ - %@"
- "Device lock changed %d, %d"
- "Handoff processing has been finished"
- "Headphone is selected, this device is primary, sending Accessory info"
- "IDS sent message GUID: %@"
- "Phone call [pending = %d, active = %d, avc = %d, endpoint = %d] - [connected = %d, should = %d] - %@"
- "T@\"AXHearingAidMode\",&,N,VcurrentLeftProgram"
- "T@\"AXHearingAidMode\",&,N,VcurrentLeftStreamingProgram"
- "T@\"AXHearingAidMode\",&,N,VcurrentRightProgram"
- "T@\"AXHearingAidMode\",&,N,VcurrentRightStreamingProgram"
- "T@\"CBPeripheral\",&,N,VleftPeripheral"
- "T@\"CBPeripheral\",&,N,VrightPeripheral"
- "T@\"NSArray\",C,N,V_leftPrograms"
- "T@\"NSArray\",C,N,V_rightPrograms"
- "T@\"NSArray\",C,N,VleftPrograms"
- "T@\"NSArray\",C,N,VrightPrograms"
- "T@\"NSArray\",R,C,N"
- "T@\"NSDate\",R,&,N"
- "T@\"NSMutableArray\",&,N,V_manufacturer"
- "T@\"NSMutableArray\",&,N,V_model"
- "T@\"NSMutableArray\",&,N,Vmanufacturer"
- "T@\"NSMutableArray\",&,N,Vmodel"
- "T@\"NSMutableArray\",R,&,N"
- "T@\"NSMutableDictionary\",&,N,VleftPropertiesLoadCount"
- "T@\"NSMutableDictionary\",&,N,VrightPropertiesLoadCount"
- "T@\"NSString\",&,N,V_leftPeripheralUUID"
- "T@\"NSString\",&,N,V_rightPeripheralUUID"
- "T@\"NSString\",&,N,VleftFirmwareVersion"
- "T@\"NSString\",&,N,VleftHardwareVersion"
- "T@\"NSString\",&,N,VleftPeripheralUUID"
- "T@\"NSString\",&,N,VleftUUID"
- "T@\"NSString\",&,N,Vname"
- "T@\"NSString\",&,N,VrightFirmwareVersion"
- "T@\"NSString\",&,N,VrightHardwareVersion"
- "T@\"NSString\",&,N,VrightPeripheralUUID"
- "T@\"NSString\",&,N,VrightUUID"
- "TB,N,V_processingHandoff"
- "TB,N,VisListening"
- "_processingHandoff"
- "_registerUpdateBlock:forIdentier:listenerHash:"
- "a"
- "com.apple.springboard.lockstate"
- "connectedPeer: %@, Reachable HA: %@, isReachable: %@, audioReachable: %@"
- "localizedStringFromDateComponents:unitsStyle:"
- "localizedStringWithFormat:"
- "processingHandoff"
- "r"
- "registerUpdateBlock:forIdentier:withListener:"
- "registerUpdateBlock:forIdentier:withListener:listenerHash:"
- "representsAWatch"
- "setHour:"
- "setMinute:"
- "setProcessingHandoff:"
- "startListeningWithError:"
- "stopListeningWithError:"
- "systemStatusDidChange:"

```
