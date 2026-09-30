## SystemStatus

> `/System/Library/PrivateFrameworks/SystemStatus.framework/SystemStatus`

```diff

-210.5.4.0.0
-  __TEXT.__text: 0x56a94
+239.0.0.0.0
+  __TEXT.__text: 0x57aa4
   __TEXT.__auth_stubs: 0x6b0
-  __TEXT.__objc_methlist: 0x7f58
+  __TEXT.__objc_methlist: 0x8090
   __TEXT.__const: 0x100
-  __TEXT.__cstring: 0x3aa5
+  __TEXT.__cstring: 0x3cce
   __TEXT.__oslogstring: 0x146a
   __TEXT.__gcc_except_tab: 0x470
-  __TEXT.__unwind_info: 0x2028
-  __TEXT.__objc_classname: 0x19cd
-  __TEXT.__objc_methname: 0xabd4
-  __TEXT.__objc_methtype: 0x16e1
-  __TEXT.__objc_stubs: 0x5780
+  __TEXT.__unwind_info: 0x2050
+  __TEXT.__objc_classname: 0x19ed
+  __TEXT.__objc_methname: 0xae8f
+  __TEXT.__objc_methtype: 0x170b
+  __TEXT.__objc_stubs: 0x5900
   __DATA_CONST.__got: 0x570
-  __DATA_CONST.__const: 0x19a8
-  __DATA_CONST.__objc_classlist: 0x570
+  __DATA_CONST.__const: 0x19e0
+  __DATA_CONST.__objc_classlist: 0x578
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x118
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1e60
+  __DATA_CONST.__objc_selrefs: 0x1ec0
   __DATA_CONST.__objc_protorefs: 0x30
-  __DATA_CONST.__objc_superrefs: 0x3d8
+  __DATA_CONST.__objc_superrefs: 0x3e0
   __DATA_CONST.__objc_arraydata: 0x18
   __AUTH_CONST.__auth_got: 0x368
   __AUTH_CONST.__const: 0x8c0
-  __AUTH_CONST.__cfstring: 0x4420
-  __AUTH_CONST.__objc_const: 0xec98
+  __AUTH_CONST.__cfstring: 0x45c0
+  __AUTH_CONST.__objc_const: 0xef48
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH.__objc_data: 0x3c0
-  __DATA.__objc_ivar: 0x4e8
+  __AUTH.__objc_data: 0x320
+  __DATA.__objc_ivar: 0x504
   __DATA.__data: 0xd28
   __DATA.__common: 0x10
-  __DATA_DIRTY.__objc_ivar: 0xa0
-  __DATA_DIRTY.__objc_data: 0x32a0
+  __DATA_DIRTY.__objc_ivar: 0xac
+  __DATA_DIRTY.__objc_data: 0x3390
   __DATA_DIRTY.__bss: 0x170
   __DATA_DIRTY.__common: 0x40
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9DED2645-1D3A-3A79-AB06-54AAF3005B11
-  Functions: 3036
-  Symbols:   9185
-  CStrings:  3292
+  UUID: 982DAA4F-EED8-360F-8A67-24430E44B0E5
+  Functions: 3066
+  Symbols:   9276
+  CStrings:  3348
 
Symbols:
+ +[STStatusBarDataPrivacyEntry entryWithCamera:microphone:location:]
+ +[STStatusBarDataPrivacyEntry supportsBSXPCSecureCoding]
+ +[STStatusBarDataPrivacyEntry supportsSecureCoding]
+ -[STMutableStatusBarData setExternalPrivacyEntry:]
+ -[STMutableStatusBarDataAdditionsStatusDomainData(AvatarProperty) setAvatarEntry:]
+ -[STMutableStewieStatusDomainData setMaxStewieSignalStrengthBars:]
+ -[STMutableStewieStatusDomainData setStewieSignalStrengthBars:]
+ -[STStatusBarData externalPrivacyEntry]
+ -[STStatusBarDataAdditionsStatusDomainData(AvatarProperty) avatarEntry]
+ -[STStatusBarDataPrivacyEntry _equalsBuilderWithObject:]
+ -[STStatusBarDataPrivacyEntry _hashBuilder]
+ -[STStatusBarDataPrivacyEntry camera]
+ -[STStatusBarDataPrivacyEntry encodeWithBSXPCCoder:]
+ -[STStatusBarDataPrivacyEntry encodeWithCoder:]
+ -[STStatusBarDataPrivacyEntry initWithBSXPCCoder:]
+ -[STStatusBarDataPrivacyEntry initWithCoder:]
+ -[STStatusBarDataPrivacyEntry location]
+ -[STStatusBarDataPrivacyEntry microphone]
+ -[STStatusBarDataPrivacyEntry succinctDescriptionBuilder]
+ -[STStatusDomainPublisher _lock_isInvalidated]
+ -[STStatusDomainPublisher internalStateLock]
+ -[STStewieStatusDomainData maxStewieSignalStrengthBars]
+ -[STStewieStatusDomainData stewieSignalStrengthBars]
+ -[STStewieStatusDomainDataDiff initWithStewieActiveChangedValue:stewieConnectedChangedValue:stewieSignalStrengthBarsChangedValue:maxStewieSignalStrengthBarsChangedValue:]
+ OBJC_IVAR_$_STStatusBarData._externalPrivacyEntry
+ OBJC_IVAR_$_STStewieStatusDomainData._maxStewieSignalStrengthBars
+ OBJC_IVAR_$_STStewieStatusDomainData._stewieSignalStrengthBars
+ _OBJC_CLASS_$_STStatusBarDataPrivacyEntry
+ _OBJC_IVAR_$_STStatusDomain._lock
+ _OBJC_IVAR_$_STStatusDomain._lock_dataChangedBlock
+ _OBJC_IVAR_$_STStatusDomain._lock_dataChangedWithContextBlock
+ _OBJC_IVAR_$_STStatusDomain._lock_invalidated
+ _OBJC_IVAR_$_STStatusDomainPublisher._lock
+ _OBJC_IVAR_$_STStatusDomainPublisher._lock_invalidated
+ _OBJC_IVAR_$_STStewieStatusDomainDataDiff._maxStewieSignalStrengthBarsChangedValue
+ _OBJC_IVAR_$_STStewieStatusDomainDataDiff._stewieSignalStrengthBarsChangedValue
+ _OBJC_IVAR_$_STUserInteractionHandlingStatusDomainPublisher._lock_userInteractionHandlerBlock
+ _OBJC_METACLASS_$_STStatusBarDataPrivacyEntry
+ _STStatusBarDataEntryExternalPrivacyKey
+ __OBJC_$_CLASS_METHODS_STStatusBarDataPrivacyEntry
+ __OBJC_$_INSTANCE_METHODS_STMutableStatusBarDataAdditionsStatusDomainData(AvatarProperty)
+ __OBJC_$_INSTANCE_METHODS_STStatusBarDataAdditionsStatusDomainData(AvatarProperty)
+ __OBJC_$_INSTANCE_METHODS_STStatusBarDataPrivacyEntry
+ __OBJC_$_INSTANCE_VARIABLES_STStatusBarDataPrivacyEntry
+ __OBJC_$_PROP_LIST_STStatusBarDataPrivacyEntry
+ __OBJC_CLASS_RO_$_STStatusBarDataPrivacyEntry
+ __OBJC_METACLASS_RO_$_STStatusBarDataPrivacyEntry
+ __STBackgroundActivityIdentifierAccessibilityGuestPass
+ __STBackgroundActivityIdentifierContinuityCaptureMicOnly
+ __STBackgroundActivityIdentifierHealthWorkout
+ __STBackgroundActivityIdentifierReplayKitCallRecording
+ __STBackgroundActivityIdentifierReplayKitCallRecordingReady
+ ___36-[STStewieStatusDomainData isEqual:]_block_invoke_3
+ ___36-[STStewieStatusDomainData isEqual:]_block_invoke_4
+ ___40-[STStewieStatusDomainDataDiff isEqual:]_block_invoke_3
+ ___40-[STStewieStatusDomainDataDiff isEqual:]_block_invoke_4
+ ___56-[STStatusBarDataPrivacyEntry _equalsBuilderWithObject:]_block_invoke
+ ___56-[STStatusBarDataPrivacyEntry _equalsBuilderWithObject:]_block_invoke_2
+ ___56-[STStatusBarDataPrivacyEntry _equalsBuilderWithObject:]_block_invoke_3
+ ___block_literal_global.864
+ _objc_msgSend$_lock_isInvalidated
+ _objc_msgSend$camera
+ _objc_msgSend$entry
+ _objc_msgSend$internalStateLock
+ _objc_msgSend$location
+ _objc_msgSend$maxStewieSignalStrengthBars
+ _objc_msgSend$microphone
+ _objc_msgSend$personNameEntry
+ _objc_msgSend$setMaxStewieSignalStrengthBars:
+ _objc_msgSend$setPersonNameEntry:
+ _objc_msgSend$setStewieSignalStrengthBars:
+ _objc_msgSend$stewieSignalStrengthBars
- -[STStewieStatusDomainDataDiff initWithStewieActiveChangedValue:stewieConnectedChangedValue:]
- _OBJC_IVAR_$_STStatusDomain._dataChangedBlock
- _OBJC_IVAR_$_STStatusDomain._dataChangedWithContextBlock
- _OBJC_IVAR_$_STStatusDomain._invalidated
- _OBJC_IVAR_$_STStatusDomainPublisher._invalidated
- _OBJC_IVAR_$_STUserInteractionHandlingStatusDomainPublisher._userInteractionHandlerBlock
- __OBJC_$_INSTANCE_METHODS_STMutableStatusBarDataAdditionsStatusDomainData
- __OBJC_$_INSTANCE_METHODS_STStatusBarDataAdditionsStatusDomainData
- __OBJC_$_PROP_LIST_STMutableStatusBarDataAdditionsStatusDomainData
- __OBJC_$_PROP_LIST_STStatusBarDataAdditionsStatusDomainData
- ___block_literal_global.833
CStrings:
+ "@\"STStatusBarDataPrivacyEntry\""
+ "@28@0:8B16B20B24"
+ "STStatusBarDataPrivacyEntry"
+ "T@\"STStatusBarDataPersonNameEntry\",R,C,N"
+ "T@\"STStatusBarDataPrivacyEntry\",C,D,N"
+ "T@\"STStatusBarDataPrivacyEntry\",R,N,V_externalPrivacyEntry"
+ "TB,R,N,V_camera"
+ "TB,R,N,V_location"
+ "TB,R,N,V_microphone"
+ "TQ,R,N,V_maxStewieSignalStrengthBars"
+ "TQ,R,N,V_stewieSignalStrengthBars"
+ "T^{os_unfair_lock_s=I},R,N"
+ "^{os_unfair_lock_s=I}16@0:8"
+ "_camera"
+ "_externalPrivacyEntry"
+ "_location"
+ "_lock_dataChangedBlock"
+ "_lock_dataChangedWithContextBlock"
+ "_lock_isInvalidated"
+ "_lock_userInteractionHandlerBlock"
+ "_maxStewieSignalStrengthBars"
+ "_maxStewieSignalStrengthBarsChangedValue"
+ "_microphone"
+ "_stewieSignalStrengthBars"
+ "_stewieSignalStrengthBarsChangedValue"
+ "com.apple.systemstatus.background-activity.continuitycapture.mic-only"
+ "com.apple.systemstatus.background-activity.guestpass"
+ "com.apple.systemstatus.background-activity.replaykit.callrecording.ready"
+ "com.apple.systemstatus.background-activity.replaykit.callrecording.recording"
+ "com.apple.systemstatus.background-activity.workout"
+ "entryWithCamera:microphone:location:"
+ "externalPrivacyEntry"
+ "internalStateLock"
+ "maxStewieSignalStrengthBars"
+ "maxStewieSignalStrengthBarsChanged"
+ "maxStewieSignalStrengthBarsChangedValue"
+ "microphone"
+ "setExternalPrivacyEntry:"
+ "setMaxStewieSignalStrengthBars:"
+ "setStewieSignalStrengthBars:"
+ "stewieSignalStrengthBars"
+ "stewieSignalStrengthBarsChanged"
+ "stewieSignalStrengthBarsChangedValue"
- "@\"STStatusBarDataPersonNameEntry\""
- "T@\"STStatusBarDataPersonNameEntry\",C,D,N"
- "_dataChangedBlock"
- "_dataChangedWithContextBlock"
- "_invalidated"
- "_userInteractionHandlerBlock"

```
