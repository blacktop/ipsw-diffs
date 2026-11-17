## CoreBrightness

> `/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`

```diff

-2300.60.30.0.0
-  __TEXT.__text: 0x17f44c
-  __TEXT.__objc_methlist: 0xe140
-  __TEXT.__cstring: 0xd5da
-  __TEXT.__const: 0x1bb80
-  __TEXT.__oslogstring: 0x1bdda
-  __TEXT.__gcc_except_tab: 0x2ae4
+2300.60.34.0.2
+  __TEXT.__text: 0x185a10
+  __TEXT.__objc_methlist: 0xe390
+  __TEXT.__cstring: 0xd83a
+  __TEXT.__const: 0x1bbe8
+  __TEXT.__oslogstring: 0x1c2dd
+  __TEXT.__gcc_except_tab: 0x2ac8
   __TEXT.__dlopen_cstrs: 0x218
-  __TEXT.__swift5_typeref: 0xf3c
-  __TEXT.__constg_swiftt: 0xd64
+  __TEXT.__swift5_typeref: 0xf8c
+  __TEXT.__constg_swiftt: 0xd88
   __TEXT.__swift5_builtin: 0x118
-  __TEXT.__swift5_reflstr: 0xadc
-  __TEXT.__swift5_fieldmd: 0x10e8
+  __TEXT.__swift5_reflstr: 0xaf4
+  __TEXT.__swift5_fieldmd: 0x111c
   __TEXT.__swift5_assocty: 0x288
   __TEXT.__swift5_proto: 0x328
-  __TEXT.__swift5_types: 0x138
-  __TEXT.__swift5_capture: 0x3d0
-  __TEXT.__swift5_mpenum: 0x28
+  __TEXT.__swift5_types: 0x13c
   __TEXT.__swift5_protos: 0x8
-  __TEXT.__unwind_info: 0x7c88
-  __TEXT.__eh_frame: 0xb98
+  __TEXT.__swift5_capture: 0x3e0
+  __TEXT.__swift5_mpenum: 0x28
+  __TEXT.__unwind_info: 0x7e40
+  __TEXT.__eh_frame: 0xc48
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x3330
-  __DATA_CONST.__objc_classlist: 0x7b8
+  __DATA_CONST.__const: 0x3438
+  __DATA_CONST.__objc_classlist: 0x7c8
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x3b0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0x5e80
+  __DATA_CONST.__objc_selrefs: 0x5fa0
   __DATA_CONST.__objc_protorefs: 0x158
   __DATA_CONST.__objc_superrefs: 0x658
   __DATA_CONST.__objc_arraydata: 0xdc0
-  __DATA_CONST.__got: 0x7f8
-  __AUTH_CONST.__const: 0x3fe0
-  __AUTH_CONST.__cfstring: 0xf140
-  __AUTH_CONST.__objc_const: 0x3a140
+  __DATA_CONST.__got: 0x820
+  __AUTH_CONST.__const: 0x40b8
+  __AUTH_CONST.__cfstring: 0xf320
+  __AUTH_CONST.__objc_const: 0x3a5e0
   __AUTH_CONST.__weak_auth_got: 0x28
+  __AUTH_CONST.__objc_arrayobj: 0x468
   __AUTH_CONST.__objc_doubleobj: 0x80
   __AUTH_CONST.__objc_intobj: 0xdc8
-  __AUTH_CONST.__objc_arrayobj: 0x468
-  __AUTH_CONST.__objc_dictobj: 0x5f0
   __AUTH_CONST.__objc_floatobj: 0x1b0
-  __AUTH_CONST.__auth_got: 0x1400
-  __AUTH.__objc_data: 0x2e20
-  __AUTH.__data: 0x788
-  __DATA.__objc_ivar: 0x190c
-  __DATA.__data: 0x35280
+  __AUTH_CONST.__objc_dictobj: 0x5f0
+  __AUTH_CONST.__auth_got: 0x1430
+  __AUTH.__objc_data: 0x2f00
+  __AUTH.__data: 0x7d8
+  __DATA.__objc_ivar: 0x1964
+  __DATA.__data: 0x352a8
   __DATA.__common: 0x10
   __DATA_DIRTY.__objc_data: 0x2238
   __DATA_DIRTY.__data: 0x4e8

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 9230
-  Symbols:   10895
-  CStrings:  4992
+  Functions: 9380
+  Symbols:   10991
+  CStrings:  5057
 
Symbols:
+ +[CBDisplayContaineriOS brightnessFrom:]
+ -[CBALSService orientation]
+ -[CBColorFilter frontPlacement]
+ -[CBColorFilter setSyncDisplayPolicy:]
+ -[CBColorFilter syncDisplayPolicy]
+ -[CBColorModuleShared applyALSSelectionPolicies]
+ -[CBColorModuleShared applySeededWPMatrix]
+ -[CBColorModuleShared colorSyncPropertyHandler:]
+ -[CBColorModuleShared copyColorSyncState]
+ -[CBColorModuleShared copyTelemetrySnapshot]
+ -[CBColorModuleShared displayTransitionSuppressionPropertyHandler:]
+ -[CBColorModuleShared displayTransitionSyncModePropertyHandler:]
+ -[CBDisplayBrightnessClient .cxx_construct]
+ -[CBDisplayBrightnessClient .cxx_destruct]
+ -[CBDisplayBrightnessClient brightnessObserver]
+ -[CBDisplayContaineriOS .cxx_construct]
+ -[CBDisplayContaineriOS copyPropertyForKeyNoQueue:]
+ -[CBDisplayContaineriOS copyTelemetrySnapshot]
+ -[CBDisplayContaineriOS handleExtGenericAvailability:from:]
+ -[CBDisplayModuleExtGeneric announceAvailability:]
+ -[CBDisplayModuleExtGeneric endFirstReadSignpost:]
+ -[CBDisplayModuleExtGeneric firstReadSucceededWithCurrent:max:]
+ -[CBDisplayModuleExtGeneric handleFirstRead:linkNotReady:]
+ -[CBDisplayModuleExtGeneric performFirstRead]
+ -[CBDisplayModuleExtGeneric scheduleFirstReadAfter:]
+ -[CBIndicatorBrightnessModule canJumpToTargetIndicatorBrightness]
+ -[CBIndicatorBrightnessModule isPipelineStalled]
+ -[CBIndicatorBrightnessModule isThermalPressureCritical]
+ -[CBIndicatorBrightnessModule jumpTo:forReason:withForce:]
+ -[CBIndicatorBrightnessModule recordSwapStall:]
+ -[CBIndicatorBrightnessModule setThermalPressure:]
+ -[CBIndicatorBrightnessModule startMonitoringForSwapStalls]
+ -[CBIndicatorBrightnessModule stopMonitoringForSwapStalls]
+ GCC_except_table113
+ GCC_except_table122
+ GCC_except_table130
+ GCC_except_table137
+ GCC_except_table142
+ GCC_except_table145
+ GCC_except_table171
+ GCC_except_table201
+ _CBU_IsMultiPanelTelemetryEnabled
+ _CFXClearForceAdaptationOnNextAmbientChange
+ _CFXGetCurrentHarmonyMatrix
+ _CFXSetLogIdentity
+ _IOAVServiceGetLinkData
+ _IOAVServiceGetProtectionStatus
+ _OBJC_CLASS_$_CBMultiPanelTelemetry
+ _OBJC_CLASS_$_CBMultiPanelTelemetryState
+ _OBJC_IVAR_$_CBALSService._orientation
+ _OBJC_IVAR_$_CBColorFilter._syncDisplayPolicy
+ _OBJC_IVAR_$_CBColorModuleShared._colorSelectionPolicyNative
+ _OBJC_IVAR_$_CBColorModuleShared._colorSelectionPolicySync
+ _OBJC_IVAR_$_CBColorModuleShared._firstALSSelectionPolicyNative
+ _OBJC_IVAR_$_CBColorModuleShared._firstALSSelectionPolicySync
+ _OBJC_IVAR_$_CBColorModuleShared._seededHarmonyMatrix
+ _OBJC_IVAR_$_CBColorModuleShared._syncDisplayPolicy
+ _OBJC_IVAR_$_CBColorModuleShared._transitionHold
+ _OBJC_IVAR_$_CBDisplayBrightnessClient._brightnessGranularity
+ _OBJC_IVAR_$_CBDisplayBrightnessClient._brightnessObserver
+ _OBJC_IVAR_$_CBDisplayBrightnessClient._lastBrightness
+ _OBJC_IVAR_$_CBDisplayBrightnessClient._observerLock
+ _OBJC_IVAR_$_CBDisplayContaineriOS._cachedSlider
+ _OBJC_IVAR_$_CBDisplayContaineriOS._significantSliderChange
+ _OBJC_IVAR_$_CBDisplayModuleExtGeneric._firstReadAttempts
+ _OBJC_IVAR_$_CBDisplayModuleExtGeneric._firstReadGeneration
+ _OBJC_IVAR_$_CBDisplayModuleExtGeneric._firstReadSignpost
+ _OBJC_IVAR_$_CBDisplayModuleExtGeneric._firstReadStart
+ _OBJC_IVAR_$_CBDisplayModuleExtGeneric._linkWaitExpired
+ _OBJC_IVAR_$_CBDisplayModuleExtGeneric._live
+ _OBJC_IVAR_$_CBIndicatorBrightnessModule._consecutiveSwapStalledCount
+ _OBJC_IVAR_$_CBIndicatorBrightnessModule._lastSILOffRequestTimestampUs
+ _OBJC_IVAR_$_CBIndicatorBrightnessModule._lastSILOnRequestTimestampUs
+ _OBJC_IVAR_$_CBIndicatorBrightnessModule._swapStallObserverToken
+ _OBJC_METACLASS_$_CBMultiPanelTelemetry
+ _OBJC_METACLASS_$_CBMultiPanelTelemetryState
+ __CFXSharedLogHandle.log
+ __CFXSharedLogHandle.once
+ __DATA_CBMultiPanelTelemetry
+ __DATA_CBMultiPanelTelemetryState
+ __INSTANCE_METHODS_CBMultiPanelTelemetry
+ __INSTANCE_METHODS_CBMultiPanelTelemetryState
+ __IVARS_CBMultiPanelTelemetry
+ __IVARS_CBMultiPanelTelemetryState
+ __METACLASS_DATA_CBMultiPanelTelemetry
+ __METACLASS_DATA_CBMultiPanelTelemetryState
+ __OBJC_$_PROP_LIST_CBDisplayBrightnessClientProtocol
+ __OBJC_$_PROTOCOL_CLASS_METHODS_CBDisplayBrightnessClientProtocol
+ __PROPERTIES_CBMultiPanelTelemetryState
+ __ZL11readControlP13__IOAVServicehPU19objcproto9OS_os_log8NSObject
+ __ZL12kReadBackoff
+ __ZL16ioReturnToStringi
+ __ZN4AABC30UpdateMultiPanelTelemetryStateEP26CBMultiPanelTelemetryState
+ ___45-[CBDisplayModuleExtGeneric performFirstRead]_block_invoke
+ ___45-[CBDisplayModuleExtGeneric performFirstRead]_block_invoke_2
+ ___47-[CBIndicatorBrightnessModule recordSwapStall:]_block_invoke
+ ___51-[CBDisplayContaineriOS copyPropertyForKeyNoQueue:]_block_invoke
+ ___51-[CBDisplayContaineriOS copyPropertyForKeyNoQueue:]_block_invoke_2
+ ___52-[CBDisplayModuleExtGeneric scheduleFirstReadAfter:]_block_invoke
+ ___59-[CBDisplayContaineriOS handleExtGenericAvailability:from:]_block_invoke
+ ___59-[CBIndicatorBrightnessModule startMonitoringForSwapStalls]_block_invoke
+ ____CFXSharedLogHandle_block_invoke
+ ____ZN4AABC15registerDisplayEP9__DisplayP16CBDisplayContext_block_invoke
+ ____ZN4AABC30UpdateMultiPanelTelemetryStateEP26CBMultiPanelTelemetryState_block_invoke
+ ___block_descriptor_40_e36_v16?0"CBMultiPanelTelemetryState"8l
+ ___block_descriptor_40_e8_32o_e20_v40?0{?=QIBBBffff}8ls32l8
+ ___block_descriptor_40_e8_32o_e35_v24?0^{__IOHIDServiceClient=}8^v16ls32l8
+ ___block_descriptor_40_e8_32r_e20_v40?0{?=QIBBBffff}8lr32l8
+ ___block_descriptor_65_e8_32o40o_e5_v8?0ls32l8s40l8
+ ___block_descriptor_68_e8_32o_e5_v8?0ls32l8
+ ___swift_memcpy21_8
+ _kCBDisplayBrightnessValue
+ _objc_storeWeak
+ _os_release
+ _os_variant_has_internal_content
+ _symbolic Sf1x_Sf1ySf1ztSg
+ _symbolic So26CBMultiPanelTelemetryStateCIeyBy_
+ _symbolic _____ 14CoreBrightness9ALSSample33_ADFF7477EA2E5A35BDDA6C6C9A26C148LLV
+ _symbolic _____y__________G s18_DictionaryStorageC s5Int32V 14CoreBrightness9ALSSample33_ADFF7477EA2E5A35BDDA6C6C9A26C148LLV
+ _type_layout_string 14CoreBrightness9ALSSample33_ADFF7477EA2E5A35BDDA6C6C9A26C148LLV
- -[CBDisplayModuleExtGeneric readControl:currentValue:maxValue:]
- -[CBIndicatorBrightnessModule jumpTo:]
- GCC_except_table100
- GCC_except_table102
- GCC_except_table111
- GCC_except_table120
- GCC_except_table123
- GCC_except_table135
- GCC_except_table136
- GCC_except_table169
- GCC_except_table198
- GCC_except_table47
- GCC_except_table68
- GCC_except_table84
- _OBJC_IVAR_$_CBDisplayBrightnessClient._observers
- _OBJC_IVAR_$_CBIndicatorBrightnessModule._lastSILOffTimestampUs
- _OBJC_IVAR_$_CBIndicatorBrightnessModule._lastSILOnTimestampUs
- __CFXLogHandle.log
- __CFXLogHandle.once
- ___44-[CBDisplayContaineriOS copyPropertyForKey:]_block_invoke_2
- ___44-[CBDisplayContaineriOS copyPropertyForKey:]_block_invoke_3
- ___44-[CBDisplayContaineriOS copyPropertyForKey:]_block_invoke_4
- ____CFXLogHandle_block_invoke
- ___block_descriptor_40_e8_32o_e19_v40?0{?=QIBBffff}8ls32l8
CStrings:
+ "AABTelemetrySnapshot"
+ "AOD"
+ "Backboardd restarted"
+ "CBDisplayTelemetrySnapshot"
+ "Color filter display sync policy %s; valid services: %{public}@"
+ "ColorSync"
+ "ColorTelemetrySnapshot"
+ "ExtGeneric: module created, probing for displayID=%u"
+ "ExtGenericAvailability"
+ "ExtGenericFirstRead"
+ "ExtGenericReadControl"
+ "ExtGenericWriteControl"
+ "Jumping to target indicator brightness: %f for reason: %s (forced=%d)"
+ "NACK"
+ "Ramp too long"
+ "ReadAttempts"
+ "Render pipeline stalled"
+ "SharedColorState"
+ "Swap stall state changed: stalled=%d (%u consecutive)"
+ "Thermal pressure critical"
+ "WPMatrix"
+ "[Handoff] AOD in progress - dropping seeded harmony matrix"
+ "[Handoff] Color state captured. Target WP is %f/%f"
+ "[Handoff] Color sync should always arrive before display on"
+ "[Handoff] Display sync policy %s -> %s"
+ "[Handoff] Not enabling transition hold due to harmony being off"
+ "[Handoff] State is not ready to be transferred."
+ "[Handoff] applied seeded harmony matrix led to WP=%f/%f"
+ "[Handoff] color state from displayID=%lu to displayID=%lu"
+ "[Handoff] color state received - matrix=%s"
+ "[Handoff] color transition hold %s -> %s"
+ "[Handoff] color transition hold - not applying sample %{public}@"
+ "[Handoff] harmony not enabled - dropping seeded harmony matrix"
+ "[Harmony thresholds] 1.5D Harmony: deltauv=%f, uv_thr1(new_ramp)=%f, uv_thr2(interrupt)=%f Lux=%f"
+ "[Harmony thresholds] Mitigation triggered -> 1D Harmony: deltauv=%f, uv_thr1(new_ramp)=%f, uv_thr2(interrupt)=%f Lux=%f"
+ "[Linear Weighted] ALS services: %@"
+ "[Linear Weighted] service %p xy= %f | %f ratio=%f"
+ "[Service:0x%llX] Failed to create CBHIDEvent -> dropping event"
+ "__ObjC.CBMultiPanelTelemetry"
+ "bad reply"
+ "brightness control read failed for display %u: %{public}s (%{public}s 0x%08x) after %u attempts"
+ "color-sync"
+ "colorALSMask"
+ "colorX_%d"
+ "colorY_%d"
+ "colorZ_%d"
+ "com.apple.CoreBrightness.ColorEffects.%d"
+ "com.apple.CoreBrightness.ExtGeneric"
+ "content protection negotiating"
+ "control=0x%02x"
+ "control=0x%02x value=%u"
+ "defer"
+ "display"
+ "display %u online — brightness %u/%u (%.2f) after %u attempt(s)"
+ "display %u: %.0f ms since start, reading without checking the link"
+ "display %u: %{public}s, deferring read for %.0f ms"
+ "display %u: brightness control %{public}s"
+ "display %u: probing brightness control, first read in %.0f ms"
+ "display %u: read control attempt %u/%u: %{public}s (%{public}s 0x%08x), retrying in %.0f ms"
+ "display %u: stop (live %d, %u read attempt(s))"
+ "display %u: write control 0x%02x failed: %{public}s 0x%08x, level %u"
+ "display=%u"
+ "display=%u available=%d"
+ "harmonyStrength"
+ "id=0x%lX location=%lu internal=%d orientation=%lu placement=%lu"
+ "link down"
+ "lux_%d"
+ "not read"
+ "ok"
+ "outcome=%{public}s attempts=%u elapsed=%.0fms"
+ "read control 0x%02x: bad reply %{public}.*P"
+ "reply failed"
+ "request failed"
+ "result=%{public}s ret=0x%08x current=%u max=%u"
+ "ret=0x%08x"
+ "significant-slider-change"
+ "stale handle"
+ "stopped"
+ "triggers"
+ "trustedALS"
+ "unknown"
+ "v16@?0@\"CBMultiPanelTelemetryState\"8"
+ "v40@?0{?=QIBBBffff}8"
+ "write incomplete"
+ "\x81"
- "ExtGeneric: module started for displayID=%u"
- "Ignore ALS with placement %d for panel with placement = %d"
- "InternalBuild"
- "Jumping to target indicator brightness: %f"
- "The response didn't contain brightness or it had wrong type"
- "Thermal Pressure Critical! Snapping to target indicator brightness %f"
- "[Harmony thresholds] 1.5D Harmony: uv_thr1(new_ramp)=%f, uv_thr2(interrupt)=%f Lux=%f"
- "[Harmony thresholds] Mitigation triggered -> 1D Harmony: uv_thr1(new_ramp)=%f, uv_thr2(interrupt)=%f Lux=%f"
- "brightness control read failed for display %u"
- "display %u online — brightness %u/%u (%.2f)"
- "id=0x%lX location=%lu internal=%d placement=%lu"
- "read control reply failed: 0x%x"
- "read control request failed: 0x%x"
- "read control: bad reply — opcode=0x%02x (expected 0x%02x) result=0x%02x (expected 0x%02x) control=0x%02x (expected 0x%02x)"
- "readControl: opcode=0x%02x (avService=%p)"
- "start: displayId=%u"
- "start: probe OK — cur=%u max=%u userBrightness=%.4f"
- "stop: displayId=%u avService=%p"
- "v40@?0{?=QIBBffff}8"
- "write control 0x%02x failed: 0x%x"
```
