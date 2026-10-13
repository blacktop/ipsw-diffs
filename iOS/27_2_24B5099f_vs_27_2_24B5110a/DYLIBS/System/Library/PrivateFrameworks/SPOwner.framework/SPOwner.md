## SPOwner

> `/System/Library/PrivateFrameworks/SPOwner.framework/SPOwner`

```diff

-449.31.6.16.25
-  __TEXT.__text: 0x755b0
-  __TEXT.__objc_methlist: 0xbc24
-  __TEXT.__const: 0x5b8
+449.31.6.16.29
+  __TEXT.__text: 0x763a8
+  __TEXT.__objc_methlist: 0xbd54
+  __TEXT.__const: 0x5f8
   __TEXT.__gcc_except_tab: 0x15a0
-  __TEXT.__cstring: 0x6b49
-  __TEXT.__oslogstring: 0x8078
+  __TEXT.__cstring: 0x6ca9
+  __TEXT.__oslogstring: 0x81d8
   __TEXT.__dlopen_cstrs: 0x5a
-  __TEXT.__constg_swiftt: 0x148
-  __TEXT.__swift5_typeref: 0x133
-  __TEXT.__swift5_builtin: 0x28
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
-  __TEXT.__unwind_info: 0x3040
+  __TEXT.__unwind_info: 0x30a0
   __TEXT.__eh_frame: 0x330
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x21b8
-  __DATA_CONST.__objc_classlist: 0x450
+  __DATA_CONST.__const: 0x21e0
+  __DATA_CONST.__objc_classlist: 0x458
   __DATA_CONST.__objc_protolist: 0x1c8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3df8
+  __DATA_CONST.__objc_selrefs: 0x3e80
   __DATA_CONST.__objc_protorefs: 0xc8
-  __DATA_CONST.__objc_superrefs: 0x380
+  __DATA_CONST.__objc_superrefs: 0x388
   __DATA_CONST.__objc_arraydata: 0x18
-  __DATA_CONST.__got: 0x600
-  __AUTH_CONST.__const: 0xbd8
-  __AUTH_CONST.__cfstring: 0x5f00
-  __AUTH_CONST.__objc_const: 0x143d0
+  __DATA_CONST.__got: 0x608
+  __AUTH_CONST.__const: 0xbf8
+  __AUTH_CONST.__cfstring: 0x6020
+  __AUTH_CONST.__objc_const: 0x145e0
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__auth_got: 0x698
-  __AUTH.__objc_data: 0x98
-  __DATA.__objc_ivar: 0xf1c
-  __DATA.__data: 0x15c0
+  __AUTH.__objc_data: 0xe8
+  __DATA.__objc_ivar: 0xf34
+  __DATA.__data: 0x15c8
   __DATA.__common: 0x20
   __DATA_DIRTY.__objc_data: 0x2a98
   __DATA_DIRTY.__data: 0x1a8

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 4423
-  Symbols:   7366
-  CStrings:  1583
+  Functions: 4454
+  Symbols:   7410
+  CStrings:  1606
 
Symbols:
+ +[SPCommand disableBTCSReflectorWithBeaconUUID:]
+ +[SPCommand enableBTCSReflectorWithBeaconUUID:withOptions:]
+ +[SPFindingSessionEvent supportsSecureCoding]
+ -[SPBTFindingSession didUpdateAccessoryStateCallback]
+ -[SPBTFindingSession setDidUpdateAccessoryStateCallback:]
+ -[SPBTFindingSession startBTCSForBeacon:completion:]
+ -[SPBTFindingSession stopBTCSForBeacon:completion:]
+ -[SPBTFindingSession updateAccessoryEvent:]
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
+ _OBJC_CLASS_$_SPFindingSessionEvent
+ _OBJC_IVAR_$_SPBTFindingSession._didUpdateAccessoryStateCallback
+ _OBJC_IVAR_$_SPCommand._antennaSelectionOption
+ _OBJC_IVAR_$_SPFindingSessionEvent._beaconID
+ _OBJC_IVAR_$_SPFindingSessionEvent._event
+ _OBJC_IVAR_$_SPFindingSessionEvent._motionState
+ _OBJC_IVAR_$_SPFindingSessionEvent._peripheralID
+ _OBJC_METACLASS_$_SPFindingSessionEvent
+ _SPBeaconTaskNameBTChannelSounding
+ _SPBeaconTaskNameDisableBTCSReflector
+ _SPBeaconTaskNameEnableBTCSReflector
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
+ ___52-[SPBTFindingSession startBTCSForBeacon:completion:]_block_invoke
+ ___52-[SPBTFindingSession startBTCSForBeacon:completion:]_block_invoke_2
+ _symbolic _____ So25SPFindingSessionEventTypeV
- -[SPCommand initWithBeaconUUID:type:expiration:duration:playSoundContext:playSoundOptions:handle:lostModeEmail:lostModeMessage:lostModePhoneNumber:obfuscatedIdentifier:identifier:enableLostMode:lockModePasscode:emailUpdates:]
- ___51-[SPOwnerSessionLocationFetch invalidationHandler:]_block_invoke_2
CStrings:
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
+ "SPBTCSFindingSession.start"
+ "SPBTCSFindingSession.stop"
+ "antennaSelectionOption"
+ "beaconID"
+ "com.apple.icloud.spowner.task.btChannelSounding"
+ "com.apple.icloud.spowner.task.disableBTCSReflector"
+ "com.apple.icloud.spowner.task.enableBTCSReflector"
+ "event"
+ "motionState"
+ "peripheralID"
+ "updateAccessoryEvent() called from daemon"
```
