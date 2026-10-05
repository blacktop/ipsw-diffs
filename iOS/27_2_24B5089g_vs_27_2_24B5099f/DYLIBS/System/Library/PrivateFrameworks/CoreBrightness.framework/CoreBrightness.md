## CoreBrightness

> `/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`

```diff

-2300.40.39.0.0
-  __TEXT.__text: 0x179808
-  __TEXT.__objc_methlist: 0xde50
-  __TEXT.__cstring: 0xd345
-  __TEXT.__const: 0x1b6e0
-  __TEXT.__oslogstring: 0x1aefd
-  __TEXT.__gcc_except_tab: 0x28e8
+2300.40.47.0.4
+  __TEXT.__text: 0x17b894
+  __TEXT.__objc_methlist: 0xdf50
+  __TEXT.__cstring: 0xd3d5
+  __TEXT.__const: 0x1b6c8
+  __TEXT.__oslogstring: 0x1b59d
+  __TEXT.__gcc_except_tab: 0x2a40
   __TEXT.__dlopen_cstrs: 0x218
   __TEXT.__swift5_typeref: 0xf3b
   __TEXT.__constg_swiftt: 0xd64
   __TEXT.__swift5_builtin: 0x118
-  __TEXT.__swift5_reflstr: 0xade
+  __TEXT.__swift5_reflstr: 0xace
   __TEXT.__swift5_fieldmd: 0x10e8
   __TEXT.__swift5_assocty: 0x288
   __TEXT.__swift5_proto: 0x328
   __TEXT.__swift5_types: 0x138
+  __TEXT.__swift5_protos: 0x8
   __TEXT.__swift5_capture: 0x3d0
   __TEXT.__swift5_mpenum: 0x28
-  __TEXT.__swift5_protos: 0x8
-  __TEXT.__unwind_info: 0x7a78
+  __TEXT.__unwind_info: 0x7b38
   __TEXT.__eh_frame: 0xb98
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x3220
+  __DATA_CONST.__const: 0x3270
   __DATA_CONST.__objc_classlist: 0x7a0
-  __DATA_CONST.__objc_catlist: 0x18
+  __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x3a0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0x5d70
+  __DATA_CONST.__objc_selrefs: 0x5de8
   __DATA_CONST.__objc_protorefs: 0x158
   __DATA_CONST.__objc_superrefs: 0x640
   __DATA_CONST.__objc_arraydata: 0xcf8
-  __DATA_CONST.__got: 0x7e8
+  __DATA_CONST.__got: 0x7f8
   __AUTH_CONST.__const: 0x3fc0
-  __AUTH_CONST.__cfstring: 0xedc0
-  __AUTH_CONST.__objc_const: 0x392c0
+  __AUTH_CONST.__cfstring: 0xee80
+  __AUTH_CONST.__objc_const: 0x394c0
   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__objc_doubleobj: 0x80
   __AUTH_CONST.__objc_intobj: 0xd98

   __AUTH_CONST.__auth_got: 0x13b0
   __AUTH.__objc_data: 0x2d30
   __AUTH.__data: 0x788
-  __DATA.__objc_ivar: 0x1888
+  __DATA.__objc_ivar: 0x18b4
   __DATA.__data: 0x351c0
   __DATA.__common: 0x10
   __DATA_DIRTY.__objc_data: 0x2238

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 9094
-  Symbols:   10737
-  CStrings:  4877
+  Functions: 9138
+  Symbols:   10779
+  CStrings:  4916
 
Symbols:
+ -[BrightnessSystemClient observerSlug:]
+ -[BrightnessSystemClient refreshKeys]
+ -[CBDisplayBrightnessClient description]
+ -[CBDisplayClient description]
+ -[CBDisplayTransitionPolicy isDeviceStableOpen]
+ -[CBDisplayTransitionPolicy isSourceSettled:target:]
+ -[CBDisplayTransitionPolicy isTopToBottomHandoffFromSource:toTarget:]
+ -[CBDisplayTransitionPolicy panelPlacementForContainer:]
+ -[CBDisplayTransitionPolicy updateAngle:]
+ -[CBIndicatorBrightnessModule registerForThermalPressureNotifications]
+ -[CBIndicatorBrightnessModule thermalPressureNotificationHandler:]
+ -[CBPreset alwaysRequestMaxHeadroom]
+ -[CBPreset maxPotentialEDRHeadroom]
+ -[CBPresetsParser alwaysRequestMaxHeadroom:]
+ -[CBPresetsParser maxPotentialEDRHeadroomForDisplay:]
+ -[CBSystemContext frameInfoProvider]
+ -[CBSystemContext setFrameInfoProvider:]
+ -[NSArray(PrimitiveDataProvider) copyFloatVector]
+ -[NSSet(PrettyDescription) prettyDescription]
+ GCC_except_table101
+ GCC_except_table111
+ GCC_except_table120
+ GCC_except_table140
+ GCC_except_table143
+ GCC_except_table148
+ GCC_except_table153
+ GCC_except_table158
+ GCC_except_table159
+ GCC_except_table169
+ GCC_except_table198
+ GCC_except_table42
+ GCC_except_table68
+ GCC_except_table74
+ GCC_except_table84
+ _OBJC_CLASS_$_NSHashTable
+ _OBJC_IVAR_$_BLControl._transitionPolicy
+ _OBJC_IVAR_$_BrightnessSystemClient._observedKeys
+ _OBJC_IVAR_$_BrightnessSystemClient._observersCount
+ _OBJC_IVAR_$_CBAODModule._alsNodes
+ _OBJC_IVAR_$_CBDisplayTransitionPolicy._currentAngleDegrees
+ _OBJC_IVAR_$_CBDisplayTransitionPolicy._hasAngleSample
+ _OBJC_IVAR_$_CBDisplayTransitionPolicy._lastAngleBelowCriticalThresholdTime
+ _OBJC_IVAR_$_CBIndicatorBrightnessModule._thermalPressure
+ _OBJC_IVAR_$_CBIndicatorBrightnessModule._thermalPressureNotificationToken
+ _OBJC_IVAR_$_CBPreset._alwaysRequestMaxHeadroom
+ _OBJC_IVAR_$_CBPreset._maxPotentialEDRHeadroom
+ _OBJC_IVAR_$_CBSystemContext._frameInfoProvider
+ _OUTLINED_FUNCTION_35
+ _OUTLINED_FUNCTION_36
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSSet_$_PrettyDescription
+ __OBJC_$_CATEGORY_NSSet_$_PrettyDescription
+ __OBJC_$_PROP_LIST_NSSet_$_PrettyDescription
+ __ZN14CoreBrightness19lookupValueWithAxisIfEET_NSt3__16vectorIS1_NS2_9allocatorIS1_EEEES6_S1_
+ __ZN4AABC22BrightnessRestrictionsD2Ev
+ __ZN4AABC39BrightnessRestrictionMultiPointValues_saSERKS0_
+ ___70-[CBIndicatorBrightnessModule registerForThermalPressureNotifications]_block_invoke
+ ___block_descriptor_108_e8_32o40r_e23_v24?0"CBALSNode"8^B16ls32l8r40l8
+ ___block_descriptor_40_e8_32b_e33_v16?0r^{?=IIQQQQIBBBfffQIBQQfB}8ls32l8
+ ___block_descriptor_40_e8_32r_e8_v12?0i8lr32l8
+ ___block_descriptor_49_e8_32o40o_e15_v32?08Q16^B24ls32l8s40l8
+ _kOSThermalNotificationPressureLevelName
- -[CBDisplayTransitionPolicy isSourceSettled:]
- GCC_except_table110
- GCC_except_table119
- GCC_except_table134
- GCC_except_table139
- GCC_except_table141
- GCC_except_table142
- GCC_except_table149
- GCC_except_table154
- GCC_except_table155
- GCC_except_table194
- GCC_except_table39
- GCC_except_table62
- GCC_except_table67
- GCC_except_table70
- GCC_except_table83
- _OBJC_IVAR_$_CBAODModule._alsServiceClients
- ___block_descriptor_108_e8_32o40r_e33_v32?0"HIDServiceClient"8Q16^B24ls32l8r40l8
- ___block_descriptor_40_e8_32b_e32_v16?0r^{?=IIQQQQIBBBfffQIBQQf}8ls32l8
CStrings:
+ "%@<%@>"
+ "%@@%@ with %@"
+ "-[BrightnessSystemClient unregisterObserver:]"
+ "Display on seeded by handoff — skipping snap to own curve"
+ "DisplayPanelPlacement"
+ "EXBrightSILStateTrusted"
+ "Ignoring %{public}@: expected %zu levels, got %lu"
+ "Ignoring %{public}@: not ascending: %{public}@"
+ "IlluminanceToLuminanceAggregated_AOD: nits cap = %f, ceiling = %f, AOD L = %f >>> L %f"
+ "Initial thermal pressure level: %llu"
+ "Loaded Restriction Dictionary (Dynamic Slider Configuration) from defaults (StoreDemoMode = %d): %@"
+ "Presets(%lu): always request max headroom = %d"
+ "Presets(%lu): maxPotentialEDRHeadroom: %@"
+ "Semantic ambient lux levels: %{public}@"
+ "Thermal Pressure Critical! Snapping to target indicator brightness %f"
+ "Thermal pressure level changed: %llu -> %llu"
+ "[%@]"
+ "[Dynamic Slider] MAX - failed to convert thresholds or factors to a float vector"
+ "[Dynamic Slider] MAX - missing thresholds or factors"
+ "[Dynamic Slider] MAX - thresholds and factors differ in size (%zu vs %zu)"
+ "[Dynamic Slider] MAX - thresholds and factors need at least 1 entry"
+ "[Dynamic Slider] MAX - thresholds or factors are not arrays"
+ "[Dynamic Slider] MAX - thresholds or factors not sorted in ascending order"
+ "[Dynamic Slider] MIN - failed to convert thresholds or factors to a float vector"
+ "[Dynamic Slider] MIN - missing thresholds or factors"
+ "[Dynamic Slider] MIN - thresholds and factors differ in size (%zu vs %zu)"
+ "[Dynamic Slider] MIN - thresholds and factors need at least 1 entry"
+ "[Dynamic Slider] MIN - thresholds or factors are not arrays"
+ "[Dynamic Slider] MIN - thresholds or factors not sorted in ascending order"
+ "[Handoff] angle at %.0f degrees, no dip below %.0f degrees for %.1fs - not a hinge-open motion, skipping grace period, fast-ramping target instead"
+ "[Handoff] source is exiting AOD - skipping grace period, fast-ramping target instead"
+ "[Handoff] source is in fast ramp - skipping grace period, fast-ramping target instead"
+ "[Observer] Adding %@"
+ "[Observer] Not adding %@ - no observable properties"
+ "[Observer] Observed keys 🔑: %@ - %@ + %@ = %@"
+ "[Observer] Refreshing %@"
+ "[Observer] Removing %@ since the set of properties become empty."
+ "[Observer] Unregistering %@"
+ "[dcpRoleID=%d] [ReadBack] Couldn't fetch SIL state!"
+ "[dcpRoleID=%d] [ReadBack] SIL=%d"
+ "[dcpRoleID=%d] [ReadBack] SIL=%d, sessionID=%u"
+ "[dcpRoleID=%d] [WillSend] SIL=%d"
+ "[dcpRoleID=%d] [WillSend] SIL=%d failed!"
+ "com.apple.demo-settings"
+ "crgb lookup: found=%d parsed=%d value=%d"
+ "notify_get_state failed with %d for token %d"
+ "notify_register_dispatch failed with %d for %s"
+ "semantic-lux-levels"
+ "v16@?0r^{?=IIQQQQIBBBfffQIBQQfB}8"
+ "v24@?0@\"CBALSNode\"8^B16"
- "/var/mobile/Library/Preferences/com.apple.demo-settings"
- "BrightnessRestrictions were loaded from CFPreferences (StoreDemoMode = %s)"
- "Failed to load BrightnessRestrictions from CFPreferences (StoreDemoMode = %s)"
- "IlluminanceToLuminanceAggregated_AOD: E(Lux) = %f | normal L(Nits) = %f | restricted normal L(Nits) = %f | AOD L(Nits) = %f >>> L %f"
- "Registered observer %@ with handle %@, properties %@. Subscribing to the following new keys: %@"
- "Removing observer %@ with handle %@. Unregistering the following keys: %@"
- "[Handoff] source exiting AOD, not settled"
- "[Handoff] source in fast ramp, not settled"
- "[Handoff] source not settled - skip grace period"
- "[dcpRoleID=%d] SIL=%d, monotonicTimeUS=%llu. Sending to EXBright: %@."
- "v16@?0r^{?=IIQQQQIBBBfffQIBQQf}8"
```
