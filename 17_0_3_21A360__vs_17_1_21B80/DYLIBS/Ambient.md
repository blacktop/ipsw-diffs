## Ambient

> `/System/Library/PrivateFrameworks/Ambient.framework/Ambient`

```diff

-52.2.1.0.0
-  __TEXT.__text: 0x4e0c
-  __TEXT.__auth_stubs: 0x370
-  __TEXT.__objc_methlist: 0x720
+52.7.100.0.0
+  __TEXT.__text: 0x5a1c
+  __TEXT.__auth_stubs: 0x3a0
+  __TEXT.__objc_methlist: 0x840
   __TEXT.__const: 0xd4
-  __TEXT.__cstring: 0x5dd
+  __TEXT.__cstring: 0x6a4
   __TEXT.__gcc_except_tab: 0xa4
-  __TEXT.__oslogstring: 0x3f7
-  __TEXT.__unwind_info: 0x274
+  __TEXT.__oslogstring: 0x528
+  __TEXT.__unwind_info: 0x2b8
   __TEXT.__objc_classname: 0x1e7
-  __TEXT.__objc_methname: 0x1ddb
-  __TEXT.__objc_methtype: 0x3ae
-  __TEXT.__objc_stubs: 0x11a0
+  __TEXT.__objc_methname: 0x224d
+  __TEXT.__objc_methtype: 0x3d0
+  __TEXT.__objc_stubs: 0x1480
   __DATA_CONST.__got: 0x30
-  __DATA_CONST.__const: 0x2e8
+  __DATA_CONST.__const: 0x330
   __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x12f8
-  __DATA_CONST.__objc_selrefs: 0x620
+  __DATA_CONST.__objc_const: 0x13e0
+  __DATA_CONST.__objc_selrefs: 0x738
   __DATA_CONST.__objc_arraydata: 0x178
-  __AUTH_CONST.__cfstring: 0x660
+  __AUTH_CONST.__cfstring: 0x700
   __AUTH_CONST.__objc_const: 0x558
-  __AUTH_CONST.__objc_intobj: 0x90
+  __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__const: 0x80
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_floatobj: 0x20
-  __AUTH_CONST.__auth_got: 0x1c8
+  __AUTH_CONST.__auth_got: 0x1e0
   __AUTH.__objc_data: 0x230
-  __DATA.__objc_classrefs: 0xf0
-  __DATA.__objc_superrefs: 0x40
-  __DATA.__objc_ivar: 0xc0
+  __DATA.__objc_classrefs: 0x110
+  __DATA.__objc_superrefs: 0x48
+  __DATA.__objc_ivar: 0xcc
   __DATA.__data: 0x120
   __DATA.__bss: 0x40
   __DATA_DIRTY.__objc_data: 0x230

   - /System/Library/PrivateFrameworks/PrototypeTools.framework/PrototypeTools
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 172
-  Symbols:   802
-  CStrings:  483
+  Functions: 200
+  Symbols:   893
+  CStrings:  543
 
Symbols:
+ +[AMAllowAmbientIdleTimerAttribute allowAmbientIdleTimerForSleepFocus]
+ +[AMAllowAmbientIdleTimerAttribute supportsSecureCoding]
+ -[AMAllowAmbientIdleTimerAttribute copyWithZone:]
+ -[AMAllowAmbientIdleTimerAttribute description]
+ -[AMAllowAmbientIdleTimerAttribute encodeWithCoder:]
+ -[AMAllowAmbientIdleTimerAttribute encodeWithXPCDictionary:]
+ -[AMAllowAmbientIdleTimerAttribute hash]
+ -[AMAllowAmbientIdleTimerAttribute initForSleepFocus:]
+ -[AMAllowAmbientIdleTimerAttribute initWithCoder:]
+ -[AMAllowAmbientIdleTimerAttribute initWithXPCDictionary:]
+ -[AMAllowAmbientIdleTimerAttribute isEqual:]
+ -[AMAllowAmbientIdleTimerAttribute isForSleepFocus]
+ -[AMAmbientDefaults hasMigratedClockCityWidget]
+ -[AMAmbientDefaults setMigratedClockCityWidget:]
+ -[AMAmbientPresentationTriggerManager _currentMountState]
+ -[AMAmbientPresentationTriggerManager _currentTriggerState]
+ -[AMAmbientPresentationTriggerManager _effectiveMountState]
+ -[AMAmbientPresentationTriggerManager _notifyObserversUpdatedAmbientMountState:]
+ -[AMAmbientPresentationTriggerManager _notifyObserversUpdatedAmbientTriggerState:]
+ -[AMAmbientPresentationTriggerManager _setEffectiveMountState:]
+ -[AMAmbientPresentationTriggerManager _updateAmbientMountState]
+ -[AMAmbientPresentationTriggerManager _updateAmbientTriggerState]
+ -[AMAmbientPresentationTriggerManager _updateEffectiveMountState]
+ -[AMAmbientPresentationTriggerManager mountState]
+ -[AMAmbientPresentationTriggerManager triggerState]
+ GCC_except_table24
+ _AMStringForAmbientMountState
+ _AMStringForAmbientTriggerState
+ _OBJC_CLASS_$_BSDescriptionBuilder
+ _OBJC_CLASS_$_BSEqualsBuilder
+ _OBJC_CLASS_$_BSHashBuilder
+ _OBJC_IVAR_$_AMAllowAmbientIdleTimerAttribute._forSleepFocus
+ _OBJC_IVAR_$_AMAmbientDefaults._migratedClockCityWidget
+ _OBJC_IVAR_$_AMAmbientPresentationTriggerManager._effectiveMountState
+ __OBJC_$_INSTANCE_VARIABLES_AMAllowAmbientIdleTimerAttribute
+ __OBJC_$_INSTANCE_VARIABLES_AMAmbientDefaults
+ __OBJC_$_PROP_LIST_AMAllowAmbientIdleTimerAttribute
+ ___44-[AMAllowAmbientIdleTimerAttribute isEqual:]_block_invoke
+ ___80-[AMAmbientPresentationTriggerManager _notifyObserversUpdatedAmbientMountState:]_block_invoke
+ ___82-[AMAmbientPresentationTriggerManager _notifyObserversUpdatedAmbientTriggerState:]_block_invoke
+ ___block_descriptor_40_e8_32s_e5_B8?0ls32l8
+ _objc_msgSend$UTF8String
+ _objc_msgSend$_currentMountState
+ _objc_msgSend$_currentTriggerState
+ _objc_msgSend$_effectiveMountState
+ _objc_msgSend$_notifyObserversUpdatedAmbientMountState:
+ _objc_msgSend$_notifyObserversUpdatedAmbientTriggerState:
+ _objc_msgSend$_setEffectiveMountState:
+ _objc_msgSend$_updateAmbientMountState
+ _objc_msgSend$_updateAmbientTriggerState
+ _objc_msgSend$_updateEffectiveMountState
+ _objc_msgSend$ambientPresentationManager:didUpdateMountState:
+ _objc_msgSend$ambientPresentationManager:didUpdateTriggerState:analogousTriggerEvents:
+ _objc_msgSend$appendBool:
+ _objc_msgSend$appendBool:counterpart:
+ _objc_msgSend$appendBool:withName:ifEqualTo:
+ _objc_msgSend$build
+ _objc_msgSend$builder
+ _objc_msgSend$builderWithObject:
+ _objc_msgSend$builderWithObject:ofExpectedClass:
+ _objc_msgSend$decodeBoolForKey:
+ _objc_msgSend$encodeBool:forKey:
+ _objc_msgSend$hash
+ _objc_msgSend$initForSleepFocus:
+ _objc_msgSend$isEqual
+ _objc_release_x26
+ _xpc_dictionary_get_bool
+ _xpc_dictionary_set_bool
- -[AMAmbientPresentationTriggerManager _updateAmbientPresentationState]
- GCC_except_table13
- GCC_except_table21
- _AMAmbientPresentationStateForCMMagicMountStateStatus
- _objc_msgSend$_updateAmbientPresentationState
CStrings:
+ "\x024"
+ "@20@0:8B16"
+ "@24@0:8^{_NSZone=}16"
+ "A"
+ "AMAlwaysUpdateIconModelOnAmbientWidgetLayoutChange"
+ "AMMigratedClockCityWidget"
+ "B8@?0"
+ "TB,N,GhasMigratedClockCityWidget,V_migratedClockCityWidget"
+ "TB,R,D,N"
+ "TB,R,N,GisForSleepFocus,V_forSleepFocus"
+ "Tq,D,N"
+ "Tq,N,G_effectiveMountState,S_setEffectiveMountState:,V_effectiveMountState"
+ "UTF8String"
+ "Updating ambient effective mount state : %{public}@ [ mountStatus : %{public}@ ; analogousTriggerEvents : %{BOOL}d ]"
+ "Updating ambient mount state : %{public}@ [ mountStatus : %{public}@ ; isCharging : %{BOOL}d ; ignoreCharging : %{BOOL}d ; effectiveMountState : %{public}@ ]"
+ "Updating ambient trigger state : %{public}@ [ isMounted : %{BOOL}d ; mountStatus : %{public}@ ; isCharging : %{BOOL}d ; ignoreCharging : %{BOOL}d ; effectiveMountState : %{public}@ ]"
+ "_currentMountState"
+ "_currentTriggerState"
+ "_effectiveMountState"
+ "_forSleepFocus"
+ "_migratedClockCityWidget"
+ "_notifyObserversUpdatedAmbientMountState:"
+ "_notifyObserversUpdatedAmbientTriggerState:"
+ "_setEffectiveMountState:"
+ "_updateAmbientMountState"
+ "_updateAmbientTriggerState"
+ "_updateEffectiveMountState"
+ "allowAmbientIdleTimerForSleepFocus"
+ "alwaysOnMode"
+ "alwaysUpdateIconModelOnAmbientWidgetLayoutChange"
+ "ambientPresentationManager:didUpdateMountState:"
+ "ambientPresentationManager:didUpdateTriggerState:analogousTriggerEvents:"
+ "appendBool:"
+ "appendBool:counterpart:"
+ "appendBool:withName:ifEqualTo:"
+ "asserted"
+ "build"
+ "builder"
+ "builderWithObject:"
+ "builderWithObject:ofExpectedClass:"
+ "copyWithZone:"
+ "decodeBoolForKey:"
+ "effectiveMountState"
+ "encodeBool:forKey:"
+ "encodeWithCoder:"
+ "encodeWithXPCDictionary:"
+ "forSleepFocus"
+ "hasMigratedClockCityWidget"
+ "idle"
+ "initForSleepFocus:"
+ "initWithCoder:"
+ "initWithXPCDictionary:"
+ "isEqual"
+ "isForSleepFocus"
+ "migratedClockCityWidget"
+ "mountState"
+ "q"
+ "setMigratedClockCityWidget:"
+ "supportsSecureCoding"
- "\x02$"
- "1"
- "Updating ambient presentation state : %{public}@ [ isMounted : %{BOOL}d ; mountStatus : %{public}@ ; isCharging : %{BOOL}d ; ignoreCharging : %{BOOL}d ]"
- "_updateAmbientPresentationState"

```
