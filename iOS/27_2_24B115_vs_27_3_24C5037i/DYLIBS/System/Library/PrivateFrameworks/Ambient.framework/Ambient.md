## Ambient

> `/System/Library/PrivateFrameworks/Ambient.framework/Ambient`

```diff

-109.1.1.0.0
-  __TEXT.__text: 0x5ae4
-  __TEXT.__objc_methlist: 0x9e4
-  __TEXT.__const: 0x114
-  __TEXT.__cstring: 0x771
+109.3.6.0.0
+  __TEXT.__text: 0x72cc
+  __TEXT.__objc_methlist: 0xb8c
+  __TEXT.__const: 0x194
+  __TEXT.__cstring: 0x9c0
   __TEXT.__gcc_except_tab: 0xd8
-  __TEXT.__oslogstring: 0x5f2
-  __TEXT.__unwind_info: 0x360
+  __TEXT.__oslogstring: 0xacf
+  __TEXT.__unwind_info: 0x3f0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x330
+  __DATA_CONST.__const: 0x368
   __DATA_CONST.__objc_classlist: 0x78
-  __DATA_CONST.__objc_protolist: 0x18
+  __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x810
-  __DATA_CONST.__objc_superrefs: 0x48
-  __DATA_CONST.__objc_arraydata: 0x178
-  __DATA_CONST.__got: 0x158
-  __AUTH_CONST.__const: 0x80
-  __AUTH_CONST.__cfstring: 0x780
-  __AUTH_CONST.__objc_const: 0x1b48
-  __AUTH_CONST.__objc_intobj: 0xc0
-  __AUTH_CONST.__objc_doubleobj: 0x20
+  __DATA_CONST.__objc_selrefs: 0x990
+  __DATA_CONST.__objc_superrefs: 0x50
+  __DATA_CONST.__objc_arraydata: 0x1a0
+  __DATA_CONST.__got: 0x198
+  __AUTH_CONST.__const: 0xc0
+  __AUTH_CONST.__cfstring: 0xa20
+  __AUTH_CONST.__objc_const: 0x20a0
+  __AUTH_CONST.__objc_intobj: 0x150
+  __AUTH_CONST.__objc_arrayobj: 0x60
+  __AUTH_CONST.__objc_doubleobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0xf0
-  __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_floatobj: 0x20
   __AUTH_CONST.__auth_got: 0x0
-  __DATA.__objc_ivar: 0xd4
-  __DATA.__data: 0x120
+  __DATA.__objc_ivar: 0xec
+  __DATA.__data: 0x1e0
   __DATA_DIRTY.__objc_data: 0x4b0
-  __DATA_DIRTY.__bss: 0x20
+  __DATA_DIRTY.__bss: 0x28
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMotion.framework/CoreMotion
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
   - /System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness
   - /System/Library/PrivateFrameworks/PrototypeTools.framework/PrototypeTools
+  - /System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 215
-  Symbols:   528
-  CStrings:  112
+  Functions: 263
+  Symbols:   609
+  CStrings:  157
 
Symbols:
+ +[AMAmbientPolicyManager isModernStandByDevice]
+ +[AMAmbientPolicyManager standBySupportsOffCharge]
+ -[AMAmbientDefaults isOnboardingPending]
+ -[AMAmbientDefaults markOnboardingCompleted]
+ -[AMAmbientDefaults usesModernOnboarding]
+ -[AMAmbientIlluminationTrigger dealloc]
+ -[AMAmbientIlluminationTrigger initWithDisplayID:]
+ -[AMAmbientIlluminationTrigger notifyQueue]
+ -[AMAmbientIlluminationTrigger observeValue:forKey:andHandle:withContext:]
+ -[AMAmbientIlluminationTrigger properties]
+ -[AMAmbientPresentationTriggerManager _currentMagicPose]
+ -[AMAmbientPresentationTriggerManager _currentTabletopPoseAlwaysRequiresCharging]
+ -[AMAmbientPresentationTriggerManager _effectiveMagicPoseState]
+ -[AMAmbientPresentationTriggerManager _isMagicPoseBatteryChargeStateRequirementFulfilled]
+ -[AMAmbientPresentationTriggerManager _isSupportedTabletopPose]
+ -[AMAmbientPresentationTriggerManager _notifyObserversUpdatedAmbientMagicPose:]
+ -[AMAmbientPresentationTriggerManager _resetEffectiveMagicPoseState]
+ -[AMAmbientPresentationTriggerManager _setEffectiveMagicPoseState:]
+ -[AMAmbientPresentationTriggerManager _shouldIgnoreMagicMountState]
+ -[AMAmbientPresentationTriggerManager _supportedTabletopPoses]
+ -[AMAmbientPresentationTriggerManager _updateAmbientMagicPoseState]
+ -[AMAmbientPresentationTriggerManager _updateEffectiveMagicPoseState]
+ -[AMAmbientPresentationTriggerManager currentPose]
+ -[AMAmbientPresentationTriggerManager initWithDevicePoseProvider:]
+ -[AMAmbientPresentationTriggerManager init]
+ -[AMAmbientPresentationTriggerManager poseProvider:didUpdateFromPose:toPose:]
+ -[AMAmbientPresentationTriggerManager poseProvider]
+ -[AMAmbientPresentationTriggerManager setCurrentPose:]
+ -[AMRedModeTriggerManagerContext displayID]
+ -[AMRedModeTriggerManagerContext setDisplayID:]
+ GCC_except_table38
+ GCC_except_table42
+ GCC_except_table49
+ _AMStringForAmbientMagicPose
+ _MGCopyAnswer
+ _MGGetProductType
+ _NSStringFromClass
+ _NSStringFromSelector
+ _OBJC_CLASS_$_AWWifiMotionDetectAttentionEvent
+ _OBJC_CLASS_$_CBClient
+ _OBJC_CLASS_$_NSProcessInfo
+ _OBJC_CLASS_$_NSSet
+ _OBJC_CLASS_$_NSUserDefaults
+ _OBJC_IVAR_$_AMAmbientIlluminationTrigger._cbClient
+ _OBJC_IVAR_$_AMAmbientIlluminationTrigger._cbDisplayClient
+ _OBJC_IVAR_$_AMAmbientPresentationTriggerManager._batteryChargingInitiatedTimestamp
+ _OBJC_IVAR_$_AMAmbientPresentationTriggerManager._currentPose
+ _OBJC_IVAR_$_AMAmbientPresentationTriggerManager._effectiveMagicPoseState
+ _OBJC_IVAR_$_AMAmbientPresentationTriggerManager._poseProvider
+ _OBJC_IVAR_$_AMRedModeTriggerManagerContext._displayID
+ _OUTLINED_FUNCTION_0
+ _OUTLINED_FUNCTION_1
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_4
+ _SBFStringForCMMagicPoseDeviceOrientationType
+ _SBFStringForCMMagicPoseHingeStateType
+ _SBFStringForCMMagicPoseTabletopPoseType
+ __OBJC_$_CLASS_METHODS_AMAmbientPolicyManager
+ __OBJC_$_CLASS_PROP_LIST_AMAmbientPolicyManager
+ __OBJC_$_PROP_LIST_CBPropertyObserver
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CBPropertyObserver
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SBFDevicePoseProviderObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CBPropertyObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SBFDevicePoseProviderObserver
+ __OBJC_$_PROTOCOL_REFS_CBPropertyObserver
+ __OBJC_$_PROTOCOL_REFS_SBFDevicePoseProviderObserver
+ __OBJC_CLASS_PROTOCOLS_$_AMAmbientPresentationTriggerManager
+ __OBJC_LABEL_PROTOCOL_$_CBPropertyObserver
+ __OBJC_LABEL_PROTOCOL_$_SBFDevicePoseProviderObserver
+ __OBJC_PROTOCOL_$_CBPropertyObserver
+ __OBJC_PROTOCOL_$_SBFDevicePoseProviderObserver
+ ___47+[AMAmbientPolicyManager isModernStandByDevice]_block_invoke
+ ___50+[AMAmbientPolicyManager standBySupportsOffCharge]_block_invoke
+ ___79-[AMAmbientPresentationTriggerManager _notifyObserversUpdatedAmbientMagicPose:]_block_invoke
+ __bs_set_crash_log_message
+ __os_feature_enabled_impl
+ __os_log_default
+ _bzero
+ _isModernStandByDevice.onceToken
+ _isModernStandByDevice.supported
+ _memcpy
+ _objc_release_x28
+ _objc_retainAutorelease
+ _standBySupportsOffCharge.onceToken
+ _standBySupportsOffCharge.supported
- -[AMAmbientPresentationTriggerManager initWithMagicMountManager:]
- GCC_except_table24
- GCC_except_table28
- GCC_except_table34
- _OBJC_IVAR_$_AMAmbientPresentationTriggerManager._batteryStateChangeTimestamp
CStrings:
+ "AMAmbientFirstModernPresentation"
+ "AMAmbientIlluminationTrigger: Initialized with _ambientLux for displayID %lu: %{public}0.4f"
+ "AMCoverDisplayEnabled"
+ "AMInnerDisplayEnabled"
+ "AMOnlyWhileCharging"
+ "AMRedModeTriggerManager.m"
+ "AMSupportBookUpsideDown"
+ "AMSupportsClosedLandscapeLeft"
+ "Ambient magic pose event detected [ tabletopPose : %{public}@ ; hingeState : %{public}@ ; deviceOrientation : %{public}@ ; deviceOrientationForCover: %{public}@ ; deviceOrientationForInner : @=%{public}@ ]"
+ "Andromino"
+ "Creating CBDisplayClient for displayID: %lu"
+ "DeviceSupportsAlwaysOnDisplay"
+ "Failed to activate CBClient: %{public}@"
+ "Failed to create CBDisplayClient for displayID %lu: %{public}@"
+ "Failed to read initial lux for displayID %lu: %{public}@"
+ "Failed to register CBPropertyObserver for displayID %lu: %{public}@"
+ "Ignoring invalid trustedLux: %{public}0.4f"
+ "Initial trustedLux for displayID %lu is invalid (%{public}0.4f); deferring to first observed update"
+ "Invalid condition not satisfying: %@"
+ "No display ID provided in initialization context. Using legacy lux observation."
+ "Rushmore"
+ "StandByInfra"
+ "Updating ambient effective magic pose state : %{public}@ [ magicPose: %{public}@ ]"
+ "Updating ambient magic pose state: %{public}@ [ tabletopPose : %{public}@ ; effectiveMagicPose : %{public}@ ]"
+ "Updating ambient trigger state : %{public}@ [ isMounted : %{BOOL}d ; mountStatus : %{public}@ ; isChargingRequirementFulfilled : %{BOOL}d ; ignoreCharging : %{BOOL}d ; effectiveMountState : %{public}@ ; isMagicPoseSupported : %{BOOL}d ; magicPose : %{public}@ ; magicPoseState : %{public}@ ]"
+ "Using CBClient lux observation."
+ "[context displayID]"
+ "[nil error]"
+ "book"
+ "bookUpsideDown"
+ "closedLandscapeRight"
+ "coverDisplayEnabled"
+ "failure in %{public}@ of <%{public}@:%p> (%{public}@:%i) : %{public}@"
+ "firstModernPresentation"
+ "forceStandByAlwaysOnIfCapable"
+ "innerDisplayEnabled"
+ "observed any value... str: %@"
+ "observed new lux value: %{public}0.2f"
+ "onlyWhileCharging"
+ "openFlatLandscapeLeft"
+ "openFlatLandscapeRight"
+ "other"
+ "supported"
+ "supportsBookUpsideDown"
+ "supportsClosedLandscapeLeft"
+ "tent"
+ "unsupported"
- "A"
- "Updating ambient trigger state : %{public}@ [ isMounted : %{BOOL}d ; mountStatus : %{public}@ ; isChargingRequirementFulfilled : %{BOOL}d ; ignoreCharging : %{BOOL}d ; effectiveMountState : %{public}@ ]"
```
