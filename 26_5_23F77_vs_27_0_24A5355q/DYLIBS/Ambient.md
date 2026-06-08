## Ambient

> `/System/Library/PrivateFrameworks/Ambient.framework/Ambient`

```diff

-81.4.1.0.0
-  __TEXT.__text: 0x5f58
-  __TEXT.__auth_stubs: 0x390
-  __TEXT.__objc_methlist: 0x98c
+101.0.100.0.0
+  __TEXT.__text: 0x5ab8
+  __TEXT.__objc_methlist: 0x9b4
   __TEXT.__const: 0x114
-  __TEXT.__cstring: 0x69b
-  __TEXT.__gcc_except_tab: 0xd4
-  __TEXT.__oslogstring: 0x528
-  __TEXT.__unwind_info: 0x330
-  __TEXT.__objc_classname: 0x1e7
-  __TEXT.__objc_methname: 0x228b
-  __TEXT.__objc_methtype: 0x3de
-  __TEXT.__objc_stubs: 0x14c0
-  __DATA_CONST.__got: 0x140
+  __TEXT.__cstring: 0x709
+  __TEXT.__gcc_except_tab: 0xc0
+  __TEXT.__oslogstring: 0x550
+  __TEXT.__unwind_info: 0x2d8
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x330
-  __DATA_CONST.__objc_classlist: 0x70
+  __DATA_CONST.__objc_classlist: 0x78
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7d8
+  __DATA_CONST.__objc_selrefs: 0x7f0
   __DATA_CONST.__objc_superrefs: 0x48
   __DATA_CONST.__objc_arraydata: 0x178
-  __AUTH_CONST.__auth_got: 0x1d8
+  __DATA_CONST.__got: 0x150
   __AUTH_CONST.__const: 0x80
-  __AUTH_CONST.__cfstring: 0x6e0
-  __AUTH_CONST.__objc_const: 0x1708
-  __AUTH_CONST.__objc_intobj: 0xa8
+  __AUTH_CONST.__cfstring: 0x720
+  __AUTH_CONST.__objc_const: 0x1ae8
+  __AUTH_CONST.__objc_intobj: 0xc0
   __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_floatobj: 0x20
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x230
   __DATA.__objc_ivar: 0xcc
   __DATA.__data: 0x120
-  __DATA.__bss: 0x30
-  __DATA_DIRTY.__objc_data: 0x230
-  __DATA_DIRTY.__bss: 0x10
+  __DATA.__bss: 0x20
+  __DATA_DIRTY.__objc_data: 0x280
+  __DATA_DIRTY.__bss: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMotion.framework/CoreMotion
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
   - /System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness
   - /System/Library/PrivateFrameworks/PrototypeTools.framework/PrototypeTools
+  - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A0FD65B7-D443-3678-B7F0-43D110AAFC7B
-  Functions: 208
-  Symbols:   896
-  CStrings:  597
+  UUID: 71BB78F9-E2BE-3D79-91C7-00F662E57B4B
+  Functions: 209
+  Symbols:   909
+  CStrings:  162
 
Symbols:
+ +[AMMotionDetectionTriggerManager attentionEventMask]
+ -[AMAmbientPresentationTriggerManager _isDeviceBatteryChargeStateRequirementFulfilled]
+ GCC_except_table33
+ GCC_except_table36
+ GCC_except_table40
+ _OBJC_CLASS_$_AMAmbientPolicyManager
+ _OBJC_METACLASS_$_AMAmbientPolicyManager
+ __OBJC_$_CLASS_METHODS_AMMotionDetectionTriggerManager
+ __OBJC_CLASS_PROTOCOLS_$_AMAmbientIlluminationTrigger
+ __OBJC_CLASS_RO_$_AMAmbientPolicyManager
+ __OBJC_METACLASS_RO_$_AMAmbientPolicyManager
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$_isDeviceBatteryChargeStateRequirementFulfilled
+ _objc_msgSend$attentionEventMask
+ _objc_msgSend$motionDetectionOverrideMask
+ _objc_opt_new
+ _objc_release_x26
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
- GCC_except_table32
- GCC_except_table35
- GCC_except_table39
- GCC_except_table55
- _OUTLINED_FUNCTION_0
- _objc_release_x27
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x22
- _objc_retain_x23
- _objc_retain_x25
- _objc_retain_x27
CStrings:
+ "AMMotionDetectionOverrideMask"
+ "AMSupportsCBClient"
+ "Updating ambient mount state : %{public}@ [ mountStatus : %{public}@ ; isChargingRequirementFulfilled : %{BOOL}d ; ignoreCharging : %{BOOL}d ; effectiveMountState : %{public}@ ]"
+ "Updating ambient trigger state : %{public}@ [ isMounted : %{BOOL}d ; mountStatus : %{public}@ ; isChargingRequirementFulfilled : %{BOOL}d ; ignoreCharging : %{BOOL}d ; effectiveMountState : %{public}@ ]"
+ "motionDetectionOverrideMask"
+ "supportsCBClient"
- "#16@0:8"
- ".cxx_destruct"
- "@\"<AMAmbientIlluminationTriggerDelegate>\""
- "@\"<AMMotionDetectionTriggerManagerObserver>\""
- "@\"AMAmbientDefaults\""
- "@\"AMAmbientIlluminationTrigger\""
- "@\"AMMotionDetectionSettings\""
- "@\"AMRedModeSettings\""
- "@\"AMRedModeTriggerManagerContext\""
- "@\"AWAttentionAwarenessClient\""
- "@\"BrightnessSystemClient\""
- "@\"CMMagicMountManager\""
- "@\"CMMagicMountState\""
- "@\"NSArray\""
- "@\"NSDate\""
- "@\"NSHashTable\""
- "@\"NSMutableArray\""
- "@\"NSNumber\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSString\"16@0:8"
- "@\"NSTimer\""
- "@\"_AMMotionDetectionDataSample\""
- "@16@0:8"
- "@20@0:8B16"
- "@24@0:8:16"
- "@24@0:8@16"
- "@24@0:8^{_NSZone=}16"
- "@24@0:8d16"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24f32f36"
- "AMAllowAmbientIdleTimerAttribute"
- "AMAmbientDefaults"
- "AMAmbientIlluminationTrigger"
- "AMAmbientIlluminationTriggerDelegate"
- "AMAmbientPresentationTriggerManager"
- "AMEnableMotionDetectionWakeAttribute"
- "AMMotionDetectionDomain"
- "AMMotionDetectionSettings"
- "AMMotionDetectionTriggerManager"
- "AMRedModeDomain"
- "AMRedModeSettings"
- "AMRedModeTriggerManager"
- "AMRedModeTriggerManagerContext"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B32@0:8@16o^@24"
- "NSObject"
- "PTSettingsKeyObserver"
- "Q16@0:8"
- "Q28@0:8@16B24"
- "T#,R"
- "T@\"<AMAmbientIlluminationTriggerDelegate>\",W,N,V_delegate"
- "T@\"<AMMotionDetectionTriggerManagerObserver>\",R,W,N,V_observer"
- "T@\"AMAmbientDefaults\",W,N,V_ambientDefaults"
- "T@\"AMAmbientIlluminationTrigger\",&,N,V_ambientIlluminationTrigger"
- "T@\"CMMagicMountManager\",&,N,V_magicMountManager"
- "T@\"CMMagicMountManager\",&,N,V_overridenMagicMountManager"
- "T@\"CMMagicMountState\",&,N,V_cachedMagicMountState"
- "T@\"NSArray\",&,N,V_data"
- "T@\"NSDictionary\",C,D,N"
- "T@\"NSHashTable\",&,N,V_observers"
- "T@\"NSNumber\",N,V_overriddenBatteryChargingState"
- "T@\"NSObject<OS_dispatch_queue>\",R,N,V_queue"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "TB,D,N"
- "TB,D,N,GisFirstPresentation"
- "TB,D,N,GisMotionDetectionEnabled"
- "TB,N,GhasMigratedClockCityWidget,V_migratedClockCityWidget"
- "TB,N,GisPresentationDetectionEnabled,V_presentationDetectionEnabled"
- "TB,N,GisRedModeDetectionEnabled,V_redModeDetectionEnabled"
- "TB,N,GisRedModeTriggered,S_setRedModeTriggered:,V_redModeTriggered"
- "TB,N,GisTriggered,S_setTriggered:,V_triggered"
- "TB,N,V_triggerTypeFilteredThresholdHigh"
- "TB,N,V_triggerTypeFilteredThresholdLow"
- "TB,N,V_triggerTypeFilteredThresholdMedium"
- "TB,N,V_triggerTypeThresholdHigh"
- "TB,N,V_triggerTypeThresholdLow"
- "TB,N,V_triggerTypeThresholdMedium"
- "TB,R,D,N"
- "TB,R,N,GisForSleepFocus,V_forSleepFocus"
- "TQ,D,N"
- "TQ,R"
- "TQ,R,N"
- "Td,N"
- "Td,N,G_ambientLux,S_setAmbientLux:,V_ambientLux"
- "Td,N,V_activationThresholdLux"
- "Td,N,V_deactivationThresholdLux"
- "Td,N,V_offLuxThreshold"
- "Td,N,V_onLuxThreshold"
- "Td,N,V_timestampSeconds"
- "Tq,D,N"
- "Tq,N,G_effectiveMountState,S_setEffectiveMountState:,V_effectiveMountState"
- "Tq,R,N"
- "UTF8String"
- "Updating ambient mount state : %{public}@ [ mountStatus : %{public}@ ; isCharging : %{BOOL}d ; ignoreCharging : %{BOOL}d ; effectiveMountState : %{public}@ ]"
- "Updating ambient trigger state : %{public}@ [ isMounted : %{BOOL}d ; mountStatus : %{public}@ ; isCharging : %{BOOL}d ; ignoreCharging : %{BOOL}d ; effectiveMountState : %{public}@ ]"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_AMMotionDetectionDataSample"
- "_AMMotionDetectionTriggerManagerObserverContext"
- "_accessQueue"
- "_accessQueue_setPublishedTriggers:"
- "_accessQueue_updatePublishedTriggers"
- "_activationThresholdLux"
- "_ambientDefaults"
- "_ambientIlluminationTrigger"
- "_ambientLux"
- "_analogousTriggerEvents"
- "_awClient"
- "_awClientOverride"
- "_batteryStateChangeTimestamp"
- "_bindAndRegisterDefaults"
- "_bindProperty:withDefaultKey:toDefaultValue:options:"
- "_brightnessSystemClient"
- "_cachedMagicMountState"
- "_computeThresholdMaskFromMotionData:filtered:"
- "_currentMountState"
- "_currentPresentationState"
- "_currentTriggerState"
- "_data"
- "_dataSample"
- "_deactivationThresholdLux"
- "_delegate"
- "_deviceBatteryStateChanged"
- "_disableMagicMountDetection"
- "_effectiveDeactivationThresholdLux"
- "_effectiveMountState"
- "_enabledTriggers"
- "_enumerateTriggerTypes:"
- "_evaluateTrigger"
- "_filteredMotionDensity"
- "_firstOrderLowPassArray:last:dt:tau:"
- "_forSleepFocus"
- "_getNewAmbientIlluminationTrigger"
- "_handleMotionDataSample:"
- "_handleMotionDetectBoolean:"
- "_ignoreBatteryChargingForPresentation"
- "_initWithDomain:"
- "_initializationContext"
- "_injectSyntheticMotionData:timestampSeconds:"
- "_injectSyntheticMotionDetectBoolean:timestamp:"
- "_isDeviceBatteryCharging"
- "_keyPathForTriggerTypeName:"
- "_magicMountEventTimestamp"
- "_magicMountManager"
- "_migratedClockCityWidget"
- "_motionDensityBackground"
- "_motionDetectionEnabled"
- "_notifyObserversUpdateMotionDetectionTriggerState:"
- "_notifyObserversUpdatedAmbientMountState:"
- "_notifyObserversUpdatedAmbientPresentationState:"
- "_notifyObserversUpdatedAmbientTriggerState:"
- "_observer"
- "_observerContexts"
- "_observers"
- "_offLuxThreshold"
- "_onLuxThreshold"
- "_overriddenBatteryChargingState"
- "_overridenMagicMountManager"
- "_presentationDetectionEnabled"
- "_publishedTriggers"
- "_queue"
- "_redModeDetectionEnabled"
- "_redModeSettings"
- "_redModeTriggered"
- "_setAmbientLux:"
- "_setDeviceBatteryMonitoringEnabled:"
- "_setEffectiveMountState:"
- "_setEnabledTriggers:"
- "_setMotionDetectionMonitoringEnabled:"
- "_setRedModeTriggered:"
- "_setTriggered:"
- "_settings"
- "_setupMagicMountDetectionIfNecessary"
- "_subtractArrayX:andY:"
- "_timestampSeconds"
- "_triggerState"
- "_triggerTypeFilteredThresholdHigh"
- "_triggerTypeFilteredThresholdLow"
- "_triggerTypeFilteredThresholdMedium"
- "_triggerTypeThresholdHigh"
- "_triggerTypeThresholdLow"
- "_triggerTypeThresholdMedium"
- "_triggered"
- "_unitIntervalClipArray:"
- "_updateAmbientMountState"
- "_updateAmbientTriggerState"
- "_updateEffectiveMountState"
- "_updateFilteredMotionDensity:"
- "_updateMotionDetectionTriggerMaskWithDataSample:andFilteredDataSample:"
- "_updateTriggerState"
- "_updateWatchdogTimer"
- "_watchdogTimeout"
- "_watchdogTimer"
- "actionWithSettingsKeyPath:"
- "activationThresholdLux"
- "addKeyObserver:"
- "addObject:"
- "addObserver:"
- "addObserver:queue:"
- "addObserver:selector:name:object:"
- "allObjects"
- "allowAmbientIdleTimer"
- "allowAmbientIdleTimerForSleepFocus"
- "ambientDefaults"
- "ambientIlluminationTrigger"
- "ambientIlluminationTrigger:didUpdateTriggered:"
- "ambientLux"
- "ambientPresentationManager:didUpdateMountState:"
- "ambientPresentationManager:didUpdatePresentationState:"
- "ambientPresentationManager:didUpdatePresentationState:analogousTriggerEvents:"
- "ambientPresentationManager:didUpdateTriggerState:analogousTriggerEvents:"
- "appendBool:"
- "appendBool:counterpart:"
- "appendBool:withName:ifEqualTo:"
- "appendFormat:"
- "array"
- "arrayWithObjects:count:"
- "autorelease"
- "batteryState"
- "boolValue"
- "build"
- "builder"
- "builderWithObject:"
- "builderWithObject:ofExpectedClass:"
- "cachedMagicMountState"
- "checkEntitlementSource:forSingleEntitlement:error:"
- "checkEntitlementSourceForRequiredEntitlements:error:"
- "class"
- "compare:"
- "componentsJoinedByString:"
- "componentsSeparatedByCharactersInSet:"
- "conformsToProtocol:"
- "copy"
- "copyPropertyForKey:"
- "copyWithZone:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "currentDevice"
- "d"
- "d16@0:8"
- "data"
- "date"
- "deactivationThresholdLux"
- "debugDescription"
- "decodeBoolForKey:"
- "defaultCenter"
- "delegate"
- "description"
- "domainGroupName"
- "domainName"
- "doubleValue"
- "effectiveMountState"
- "enableMotionDetectionWake"
- "enabledTriggers"
- "encodeBool:forKey:"
- "encodeWithCoder:"
- "encodeWithXPCDictionary:"
- "enumerateObjectsUsingBlock:"
- "floatValue"
- "hasMigratedClockCityWidget"
- "hash"
- "init"
- "initForSleepFocus:"
- "initWithAWClientOverride:"
- "initWithBrightnessSystemClient:"
- "initWithCapacity:"
- "initWithCoder:"
- "initWithContext:"
- "initWithMagicMountManager:"
- "initWithObserver:queue:"
- "initWithXPCDictionary:"
- "invalidate"
- "invalidateWithError:"
- "isEqual"
- "isEqual:"
- "isEqualToString:"
- "isForSleepFocus"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isMotionDetectionEnabled"
- "isMounted"
- "isPresentationDetectionEnabled"
- "isProxy"
- "isRedModeDetectionEnabled"
- "isRedModeTriggered"
- "isTriggered"
- "localizedDescription"
- "magicMountManager"
- "mainQueue"
- "minValue:maxValue:"
- "moduleWithTitle:contents:"
- "motionData"
- "motionDetectionEnabled"
- "motionDetectionManager:didUpdateMotionDetectionTriggerState:"
- "motionResult"
- "mountState"
- "mountStatus"
- "numberWithBool:"
- "numberWithFloat:"
- "objectAtIndexedSubscript:"
- "objectForKeyedSubscript:"
- "observeDefaults:onQueue:withBlock:"
- "observer"
- "observers"
- "overriddenBatteryChargingState"
- "overridenMagicMountManager"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "presentationDetectionEnabled"
- "presentationState"
- "q16@0:8"
- "queue"
- "redModeDetectionEnabled"
- "redModeTriggerManager:didUpdateRedModeTriggeredState:"
- "redModeTriggered"
- "registerNotificationBlock:forProperties:"
- "release"
- "removeObject:"
- "removeObjectsInArray:"
- "removeObserver:"
- "removeObserver:name:object:"
- "respondsToSelector:"
- "resumeWithError:"
- "retain"
- "retainCount"
- "rootSettings"
- "rootSettingsClass"
- "rowWithTitle:action:"
- "rowWithTitle:valueKeyPath:"
- "scheduledTimerWithTimeInterval:repeats:block:"
- "sectionWithRows:"
- "sectionWithRows:title:"
- "self"
- "setActivateMotionDetect:"
- "setActivationThresholdLux:"
- "setAmbientDefaults:"
- "setAmbientIlluminationTrigger:"
- "setAttentionLostTimeout:"
- "setCachedMagicMountState:"
- "setConfiguration:"
- "setData:"
- "setDeactivationThresholdLux:"
- "setDefaultValues"
- "setDelegate:"
- "setEnabledTriggers:"
- "setEventHandlerWithQueue:block:"
- "setEventMask:"
- "setIdentifier:"
- "setMagicMountConfiguration:"
- "setMagicMountManager:"
- "setMigratedClockCityWidget:"
- "setMotionDetectionEnabled:"
- "setObject:atIndexedSubscript:"
- "setObservers:"
- "setOffLuxThreshold:"
- "setOnLuxThreshold:"
- "setOverriddenBatteryChargingState:"
- "setOverridenMagicMountManager:"
- "setPresentationDetectionEnabled:"
- "setRedModeDetectionEnabled:"
- "setSampleWhileAbsent:"
- "setSamplingInterval:"
- "setTimestampSeconds:"
- "setTriggerTypeFilteredThresholdHigh:"
- "setTriggerTypeFilteredThresholdLow:"
- "setTriggerTypeFilteredThresholdMedium:"
- "setTriggerTypeThresholdHigh:"
- "setTriggerTypeThresholdLow:"
- "setTriggerTypeThresholdMedium:"
- "setValue:forKey:"
- "setWatchdogTimeout:"
- "settings:changedValueForKey:"
- "settingsControllerModule"
- "sortDescriptorWithKey:ascending:selector:"
- "sortedArrayUsingDescriptors:"
- "startMagicMountUpdatesToQueue:withHandler:"
- "stopMagicMountUpdates"
- "string"
- "stringWithFormat:"
- "stringWithUTF8String:"
- "superclass"
- "supportsSecureCoding"
- "testSetOverrideBatteryCharging:"
- "timeIntervalSinceDate:"
- "timestamp"
- "timestampSeconds"
- "triggerState"
- "triggerTypeFilteredThresholdHigh"
- "triggerTypeFilteredThresholdLow"
- "triggerTypeFilteredThresholdMedium"
- "triggerTypeThresholdHigh"
- "triggerTypeThresholdLow"
- "triggerTypeThresholdMedium"
- "triggered"
- "unsignedIntegerValue"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8Q16"
- "v24@0:8d16"
- "v24@0:8q16"
- "v28@0:8@\"AMAmbientIlluminationTrigger\"16B24"
- "v28@0:8@16B24"
- "v28@0:8B16d20"
- "v32@0:8@\"PTSettings\"16@\"NSString\"24"
- "v32@0:8@16@24"
- "v32@0:8@16d24"
- "valueForKey:"
- "watchdogTimeout"
- "weakObjectsHashTable"
- "whitespaceCharacterSet"
- "zeroMotionDataWithTimestamp:"
- "zone"

```
