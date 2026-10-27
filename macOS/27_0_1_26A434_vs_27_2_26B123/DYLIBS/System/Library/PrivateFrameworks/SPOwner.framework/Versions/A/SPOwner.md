## SPOwner

> `/System/Library/PrivateFrameworks/SPOwner.framework/Versions/A/SPOwner`

```diff

-449.20.6.14.21
-  __TEXT.__text: 0x7de2c
-  __TEXT.__objc_methlist: 0xbe34
-  __TEXT.__const: 0x5e8
+449.21.6.16.28
+  __TEXT.__text: 0x7f434
+  __TEXT.__objc_methlist: 0xbf7c
+  __TEXT.__const: 0x628
   __TEXT.__gcc_except_tab: 0x1514
-  __TEXT.__cstring: 0x6a49
-  __TEXT.__oslogstring: 0x8378
-  __TEXT.__constg_swiftt: 0x148
-  __TEXT.__swift5_typeref: 0x133
-  __TEXT.__swift5_builtin: 0x28
+  __TEXT.__cstring: 0x6c39
+  __TEXT.__oslogstring: 0x8598
+  __TEXT.__constg_swiftt: 0x168
+  __TEXT.__swift5_typeref: 0x139
+  __TEXT.__swift5_builtin: 0x3c
   __TEXT.__swift5_reflstr: 0x85
   __TEXT.__swift5_assocty: 0x30
-  __TEXT.__swift5_proto: 0x40
-  __TEXT.__swift5_types: 0x1c
+  __TEXT.__swift5_proto: 0x44
+  __TEXT.__swift5_types: 0x20
   __TEXT.__swift5_fieldmd: 0xfc
   __TEXT.__swift5_capture: 0x60
   __TEXT.__swift_as_entry: 0x1c
   __TEXT.__swift_as_ret: 0x18
   __TEXT.__swift_as_cont: 0x8
-  __TEXT.__unwind_info: 0x24f8
+  __TEXT.__unwind_info: 0x2560
   __TEXT.__eh_frame: 0x330
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x878
-  __DATA_CONST.__objc_classlist: 0x460
+  __DATA_CONST.__const: 0x8a0
+  __DATA_CONST.__objc_classlist: 0x468
   __DATA_CONST.__objc_protolist: 0x1d0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3ea0
+  __DATA_CONST.__objc_selrefs: 0x3f28
   __DATA_CONST.__objc_protorefs: 0xc8
-  __DATA_CONST.__objc_superrefs: 0x388
+  __DATA_CONST.__objc_superrefs: 0x390
   __DATA_CONST.__objc_arraydata: 0x28
-  __DATA_CONST.__got: 0x610
-  __AUTH_CONST.__const: 0x2208
-  __AUTH_CONST.__cfstring: 0x6080
-  __AUTH_CONST.__objc_const: 0x14938
+  __DATA_CONST.__got: 0x618
+  __AUTH_CONST.__const: 0x2228
+  __AUTH_CONST.__cfstring: 0x61a0
+  __AUTH_CONST.__objc_const: 0x14ba8
   __AUTH_CONST.__objc_intobj: 0xd8
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__auth_got: 0x5f8
-  __AUTH_CONST.__auth_ptr: 0x128
-  __AUTH.__objc_data: 0x188
-  __DATA.__objc_ivar: 0xf6c
-  __DATA.__data: 0x15f8
-  __DATA.__bss: 0x660
+  __AUTH_CONST.__auth_ptr: 0x130
+  __AUTH.__objc_data: 0x1d8
+  __DATA.__objc_ivar: 0xf8c
+  __DATA.__data: 0x1600
+  __DATA.__bss: 0x6e0
   __DATA_DIRTY.__objc_data: 0x2a48
   __DATA_DIRTY.__data: 0x1d0
   __DATA_DIRTY.__bss: 0x4c0

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 4426
-  Symbols:   8982
-  CStrings:  1591
+  Functions: 4468
+  Symbols:   9054
+  CStrings:  1620
 
Symbols:
+ +[SPCommand disableBTCSReflectorWithBeaconUUID:]
+ +[SPCommand enableBTCSReflectorWithBeaconUUID:withOptions:]
+ +[SPFindingSessionEvent supportsSecureCoding]
+ -[SPBTFindingSession didUpdateAccessoryStateCallback]
+ -[SPBTFindingSession setDidUpdateAccessoryStateCallback:]
+ -[SPBTFindingSession startBTCSForBeacon:completion:]
+ -[SPBTFindingSession stopBTCSForBeacon:completion:]
+ -[SPBTFindingSession updateAccessoryEvent:]
+ -[SPBeaconManager submitDeviceEvent:source:timestamp:attachedTo:completion:]
+ -[SPCommand antennaSelectionOption]
+ -[SPCommand initWithBeaconUUID:type:expiration:duration:playSoundContext:playSoundOptions:handle:lostModeEmail:lostModeMessage:lostModePhoneNumber:obfuscatedIdentifier:identifier:enableLostMode:antennaSelectionOptions:lockModePasscode:emailUpdates:]
+ -[SPCommand setAntennaSelectionOption:]
+ -[SPFindingSessionEvent .cxx_destruct]
+ -[SPFindingSessionEvent beaconID]
+ -[SPFindingSessionEvent copyWithZone:]
+ -[SPFindingSessionEvent description]
+ -[SPFindingSessionEvent encodeWithCoder:]
+ -[SPFindingSessionEvent event]
+ -[SPFindingSessionEvent initWithBeaconID:event:peripheralID:motionState:]
+ -[SPFindingSessionEvent initWithCoder:]
+ -[SPFindingSessionEvent motionState]
+ -[SPFindingSessionEvent peripheralID]
+ -[SPOwnerSessionLocationFetch callbackQueue]
+ -[SPOwnerSessionLocationFetch queue]
+ OBJC_IVAR_$_SPBTFindingSession._didUpdateAccessoryStateCallback
+ OBJC_IVAR_$_SPCommand._antennaSelectionOption
+ OBJC_IVAR_$_SPFindingSessionEvent._beaconID
+ OBJC_IVAR_$_SPFindingSessionEvent._event
+ OBJC_IVAR_$_SPFindingSessionEvent._motionState
+ OBJC_IVAR_$_SPFindingSessionEvent._peripheralID
+ OBJC_IVAR_$_SPOwnerSessionLocationFetch._callbackQueue
+ OBJC_IVAR_$_SPOwnerSessionLocationFetch._queue
+ _OBJC_CLASS_$_SPFindingSessionEvent
+ _OBJC_METACLASS_$_SPFindingSessionEvent
+ _OUTLINED_FUNCTION_4
+ _SPBeaconTaskNameBTChannelSounding
+ _SPBeaconTaskNameDisableBTCSReflector
+ _SPBeaconTaskNameEnableBTCSReflector
+ __51-[SPBTFindingSession stopBTCSForBeacon:completion:]_block_invoke
+ __51-[SPBTFindingSession stopBTCSForBeacon:completion:]_block_invoke_2
+ __52-[SPBTFindingSession startBTCSForBeacon:completion:]_block_invoke
+ __52-[SPBTFindingSession startBTCSForBeacon:completion:]_block_invoke_2
+ __55-[SPOwnerSessionLocationFetch receivedUpdatedLocation:]_block_invoke
+ __59-[SPOwnerSessionLocationFetch receivedUpdatedDeviceEvents:]_block_invoke
+ __78-[SPOwnerSessionLocationFetch subscribeAndFetchLocationForContext:completion:]_block_invoke_3
+ __OBJC_$_CLASS_METHODS_SPFindingSessionEvent
+ __OBJC_$_CLASS_PROP_LIST_SPFindingSessionEvent
+ __OBJC_$_INSTANCE_METHODS_SPFindingSessionEvent
+ __OBJC_$_INSTANCE_VARIABLES_SPFindingSessionEvent
+ __OBJC_$_PROP_LIST_SPFindingSessionEvent
+ __OBJC_CLASS_PROTOCOLS_$_SPFindingSessionEvent
+ __OBJC_CLASS_RO_$_SPFindingSessionEvent
+ __OBJC_METACLASS_RO_$_SPFindingSessionEvent
+ ___43-[SPBTFindingSession updateAccessoryEvent:]_block_invoke
+ ___51-[SPBTFindingSession stopBTCSForBeacon:completion:]_block_invoke
+ ___51-[SPBTFindingSession stopBTCSForBeacon:completion:]_block_invoke_2
+ ___51-[SPOwnerSessionLocationFetch invalidationHandler:]_block_invoke
+ ___52-[SPBTFindingSession startBTCSForBeacon:completion:]_block_invoke
+ ___52-[SPBTFindingSession startBTCSForBeacon:completion:]_block_invoke_2
+ ___61-[SPOwnerSessionLocationFetch locationForContext:completion:]_block_invoke_2
+ ___72-[SPOwnerSessionLocationFetch unsubscribeLocationUpdatesWithCompletion:]_block_invoke
+ ___76-[SPBeaconManager submitDeviceEvent:source:timestamp:attachedTo:completion:]_block_invoke
+ ___78-[SPOwnerSessionLocationFetch subscribeAndFetchLocationForContext:completion:]_block_invoke_3
+ ___block_descriptor_76_e8_32s40s48s56s64bs_e5_v8?0l
+ _objc_msgSend$antennaSelectionOption
+ _objc_msgSend$beaconID
+ _objc_msgSend$containsValueForKey:
+ _objc_msgSend$didUpdateAccessoryStateCallback
+ _objc_msgSend$event
+ _objc_msgSend$initWithBeaconID:event:peripheralID:motionState:
+ _objc_msgSend$initWithBeaconUUID:type:expiration:duration:playSoundContext:playSoundOptions:handle:lostModeEmail:lostModeMessage:lostModePhoneNumber:obfuscatedIdentifier:identifier:enableLostMode:antennaSelectionOptions:lockModePasscode:emailUpdates:
+ _objc_msgSend$lastContext
+ _objc_msgSend$motionState
+ _objc_msgSend$peripheralID
+ _objc_msgSend$setLastContext:
+ _objc_msgSend$startBTCS:completion:
+ _objc_msgSend$stopBTCS:completion:
+ _objc_msgSend$submitDeviceEvent:source:timestamp:attachedTo:completion:
+ _symbolic _____ So25SPFindingSessionEventTypeV
- -[SPBeaconManager submitDeviceEvent:source:attachedTo:completion:]
- -[SPCommand initWithBeaconUUID:type:expiration:duration:playSoundContext:playSoundOptions:handle:lostModeEmail:lostModeMessage:lostModePhoneNumber:obfuscatedIdentifier:identifier:enableLostMode:lockModePasscode:emailUpdates:]
- __78-[SPOwnerSessionLocationFetch subscribeAndFetchLocationForContext:completion:]_block_invoke_2
- ___66-[SPBeaconManager submitDeviceEvent:source:attachedTo:completion:]_block_invoke
- ___block_descriptor_68_e8_32s40s48s56bs_e5_v8?0l
- _objc_msgSend$initWithBeaconUUID:type:expiration:duration:playSoundContext:playSoundOptions:handle:lostModeEmail:lostModeMessage:lostModePhoneNumber:obfuscatedIdentifier:identifier:enableLostMode:lockModePasscode:emailUpdates:
- _objc_msgSend$submitDeviceEvent:source:attachedTo:completion:
CStrings:
+ "\t"
+ "\r"
+ "-[SPBTCSFindingSession start]"
+ "-[SPBTCSFindingSession start] completion"
+ "-[SPBTCSFindingSession start] completion. Error %{public}@"
+ "-[SPBTCSFindingSession stop]"
+ "-[SPBTCSFindingSession stop] completion)"
+ "-[SPBTCSFindingSession stop] completion. Error %{public}@"
+ ".accessoryConnectedToCompanion"
+ ".accessoryInitiatedDisconnect"
+ ".motionStateUpdated"
+ ".peripheralConnected"
+ "<%@ %p: event: %d>"
+ "NVRAM data (length %lu) failed to deserialize as a property list: %@"
+ "NVRAM data deserialized to %@ instead of NSDictionary (data length %lu) - treating as absent"
+ "No NVRAM data present for fm-spkeys"
+ "SPBTCSFindingSession.start"
+ "SPBTCSFindingSession.stop"
+ "antennaSelectionOption"
+ "beaconID"
+ "com.apple.icloud.searchpartyd.SPOwnerSessionLocationFetch"
+ "com.apple.icloud.searchpartyd.SPOwnerSessionLocationFetch.callback"
+ "com.apple.icloud.spowner.task.btChannelSounding"
+ "com.apple.icloud.spowner.task.disableBTCSReflector"
+ "com.apple.icloud.spowner.task.enableBTCSReflector"
+ "event"
+ "motionState"
+ "peripheralID"
+ "updateAccessoryEvent() called from daemon"
```
