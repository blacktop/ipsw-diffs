## CoreBrightness

> `/System/Library/PrivateFrameworks/CoreBrightness.framework/Versions/A/CoreBrightness`

```diff

-2300.0.18.0.0
-  __TEXT.__text: 0x1616b8
-  __TEXT.__objc_methlist: 0xd17c
-  __TEXT.__cstring: 0xcc95
-  __TEXT.__const: 0x13900
-  __TEXT.__gcc_except_tab: 0x1f88
-  __TEXT.__oslogstring: 0x183cd
+2300.1.2.0.0
+  __TEXT.__text: 0x163b44
+  __TEXT.__objc_methlist: 0xd31c
+  __TEXT.__const: 0x12750
+  __TEXT.__oslogstring: 0x185dd
+  __TEXT.__cstring: 0xcdc5
+  __TEXT.__gcc_except_tab: 0x1fc8
   __TEXT.__dlopen_cstrs: 0x10d
   __TEXT.__swift5_typeref: 0xeaf
   __TEXT.__constg_swiftt: 0xc34

   __TEXT.__swift5_proto: 0x308
   __TEXT.__swift5_types: 0x120
   __TEXT.__swift5_mpenum: 0x28
-  __TEXT.__unwind_info: 0x52d0
+  __TEXT.__unwind_info: 0x5348
   __TEXT.__eh_frame: 0xb88
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x11c8
-  __DATA_CONST.__objc_classlist: 0x6e0
+  __DATA_CONST.__const: 0x11d8
+  __DATA_CONST.__objc_classlist: 0x6f0
   __DATA_CONST.__objc_catlist: 0x18
-  __DATA_CONST.__objc_protolist: 0x330
+  __DATA_CONST.__objc_protolist: 0x338
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0x5638
+  __DATA_CONST.__objc_selrefs: 0x56c8
   __DATA_CONST.__objc_protorefs: 0x130
-  __DATA_CONST.__objc_superrefs: 0x5a8
-  __DATA_CONST.__objc_arraydata: 0xba0
+  __DATA_CONST.__objc_superrefs: 0x5b8
+  __DATA_CONST.__objc_arraydata: 0xb90
   __DATA_CONST.__got: 0x760
-  __AUTH_CONST.__const: 0x5880
-  __AUTH_CONST.__cfstring: 0xe540
-  __AUTH_CONST.__objc_const: 0x33968
+  __AUTH_CONST.__const: 0x5860
+  __AUTH_CONST.__cfstring: 0xe5c0
+  __AUTH_CONST.__objc_const: 0x34b28
   __AUTH_CONST.__weak_auth_got: 0x20
-  __AUTH_CONST.__objc_intobj: 0xcf0
-  __AUTH_CONST.__objc_floatobj: 0x180
+  __AUTH_CONST.__objc_intobj: 0xcd8
   __AUTH_CONST.__objc_doubleobj: 0x40
   __AUTH_CONST.__objc_dictobj: 0x5f0
-  __AUTH_CONST.__objc_arrayobj: 0x2b8
-  __AUTH_CONST.__auth_got: 0x1278
-  __AUTH.__objc_data: 0x25e0
+  __AUTH_CONST.__objc_floatobj: 0x180
+  __AUTH_CONST.__objc_arrayobj: 0x2a0
+  __AUTH_CONST.__auth_got: 0x1288
+  __AUTH.__objc_data: 0x2680
   __AUTH.__data: 0x630
-  __DATA.__objc_ivar: 0x1730
-  __DATA.__data: 0x5a670
+  __DATA.__objc_ivar: 0x1768
+  __DATA.__data: 0x66f50
   __DATA.__bss: 0x63e0
   __DATA.__common: 0x10
   __DATA_DIRTY.__objc_data: 0x21e8

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 8150
-  Symbols:   12759
-  CStrings:  4631
+  Functions: 8200
+  Symbols:   12859
+  CStrings:  4652
 
Symbols:
+ +[CBAnalytics illuminanceHistogram:displayID:alsID:]
+ +[CBAnalytics luminanceHistogram:withName:displayID:]
+ +[CBDisplayStateUtilities isActiveDisplayMode:]
+ -[AABCHistograms displayID]
+ -[AABCHistograms pushIlluminance:weight:forAlsID:]
+ -[AABCHistograms setDisplayID:]
+ -[BacklightdExportedObj clientSetProperty:forKey:andHandle:]
+ -[BrightnessSystemClient setSyncProperty:forKey:withHandle:error:]
+ -[BrightnessSystemClientInternal setSyncProperty:forKey:handle:error:]
+ -[CBALSEvent channelAveragedColorVendorData]
+ -[CBALSEvent copyChannelAveragedColorDataFromEvent:]
+ -[CBALSEvent setChannelAveragedColorVendorData:]
+ -[CBBrightnessBroadcaster activate]
+ -[CBBrightnessBroadcaster cancel]
+ -[CBBrightnessBroadcaster dealloc]
+ -[CBBrightnessBroadcaster displayModeProvidersUpdate:]
+ -[CBBrightnessBroadcaster encodeBrightnessState:]
+ -[CBBrightnessBroadcaster initWithDisplayManager:]
+ -[CBBrightnessBroadcaster initWithDisplayManager:notifier:]
+ -[CBBrightnessBroadcaster reevaluateAndNotify]
+ -[CBBrightnessBroadcaster sendNotificationForKey:value:origin:]
+ -[CBCEModule _paramsFromAlsEvent:]
+ -[CBCEModule copyInferenceForEvent:]
+ -[CBCEModule setModelInputWithParameters:]
+ -[CBColorFilter activeALSServices]
+ -[CBColorPolicyFilter biLinearInterpBetweenIndices:forPoint1:andPoint2:strengthLUT:luxCount:luxArray:nitsArray:]
+ -[CBDarwinBrightnessLevelNotifier dealloc]
+ -[CBDarwinBrightnessLevelNotifier init]
+ -[CBDarwinBrightnessLevelNotifier publishState:]
+ -[CBDisplayBrightnessClient isRingLightEnabledWithError:]
+ -[CBDisplayBrightnessClient setProperties:]
+ -[CBRingLight isActive]
+ GCC_except_table41
+ GCC_except_table49
+ GCC_except_table50
+ OBJC_IVAR_$_AABCHistograms._EPerAls
+ OBJC_IVAR_$_AABCHistograms._displayID
+ OBJC_IVAR_$_AABCHistograms._eBins
+ OBJC_IVAR_$_CBALSEvent._channelAveragedColorVendorData
+ OBJC_IVAR_$_CBBrightnessBroadcaster._brightnessByDisplay
+ OBJC_IVAR_$_CBBrightnessBroadcaster._hasPublished
+ OBJC_IVAR_$_CBBrightnessBroadcaster._lastPublishedRawState
+ OBJC_IVAR_$_CBBrightnessBroadcaster._logHandle
+ OBJC_IVAR_$_CBBrightnessBroadcaster._manager
+ OBJC_IVAR_$_CBBrightnessBroadcaster._notifier
+ OBJC_IVAR_$_CBColorFilter._activeALSServices
+ OBJC_IVAR_$_CBDarwinBrightnessLevelNotifier._logHandle
+ OBJC_IVAR_$_CBDarwinBrightnessLevelNotifier._token
+ OBJC_IVAR_$_CBDisplayBrightnessClient._properties
+ _A_SDRGF
+ _D_SDRGF
+ _L_SDRGF
+ _OBJC_CLASS_$_CBBrightnessBroadcaster
+ _OBJC_CLASS_$_CBDarwinBrightnessLevelNotifier
+ _OBJC_METACLASS_$_CBBrightnessBroadcaster
+ _OBJC_METACLASS_$_CBDarwinBrightnessLevelNotifier
+ __24-[AABCHistograms submit]_block_invoke
+ __60-[BacklightdExportedObj clientSetProperty:forKey:andHandle:]_block_invoke
+ __OBJC_$_INSTANCE_METHODS_CBBrightnessBroadcaster
+ __OBJC_$_INSTANCE_METHODS_CBDarwinBrightnessLevelNotifier
+ __OBJC_$_INSTANCE_VARIABLES_CBBrightnessBroadcaster
+ __OBJC_$_INSTANCE_VARIABLES_CBDarwinBrightnessLevelNotifier
+ __OBJC_$_PROP_LIST_CBBrightnessBroadcaster
+ __OBJC_$_PROP_LIST_CBDarwinBrightnessLevelNotifier
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CBBrightnessLevelNotifier
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CBBrightnessLevelNotifier
+ __OBJC_$_PROTOCOL_REFS_CBBrightnessLevelNotifier
+ __OBJC_CLASS_PROTOCOLS_$_CBBrightnessBroadcaster
+ __OBJC_CLASS_PROTOCOLS_$_CBDarwinBrightnessLevelNotifier
+ __OBJC_CLASS_RO_$_CBBrightnessBroadcaster
+ __OBJC_CLASS_RO_$_CBDarwinBrightnessLevelNotifier
+ __OBJC_LABEL_PROTOCOL_$_CBBrightnessLevelNotifier
+ __OBJC_METACLASS_RO_$_CBBrightnessBroadcaster
+ __OBJC_METACLASS_RO_$_CBDarwinBrightnessLevelNotifier
+ __OBJC_PROTOCOL_$_CBBrightnessLevelNotifier
+ __Z22shouldDarwinReactivatefff
+ __ZL13getVendorDataI32CBChannelAveragedColorVendorDataENSt3__18optionalIPT_EEP12__IOHIDEvent
+ __ZL14enabled_80_100
+ __ZL15enabled_100_135
+ __ZL15enabled_135_180
+ __ZL15reenable_80_100
+ __ZL16reenable_100_135
+ __ZL16reenable_135_180
+ __ZNK14DisplayCoexLUTIfhLl12ELl26EEclEff
+ __ZNK14DisplayCoexLUTIfhLl23ELl24EEclEff
+ __ZNK14DisplayCoexLUTIfhLl28ELl23EEclEff
+ __ZNK14DisplayCoexLUTIfhLl28ELl24EEclEff
+ __ZNK14DisplayCoexLUTIfhLl30ELl25EEclEff
+ __ZNK14DisplayCoexLUTIfhLl7ELl24EEclEff
+ ___52+[CBAnalytics illuminanceHistogram:displayID:alsID:]_block_invoke
+ ___52+[CBAnalytics illuminanceHistogram:displayID:alsID:]_block_invoke_2
+ ___53+[CBAnalytics luminanceHistogram:withName:displayID:]_block_invoke
+ ___53+[CBAnalytics luminanceHistogram:withName:displayID:]_block_invoke_2
+ ___60-[BacklightdExportedObj clientSetProperty:forKey:andHandle:]_block_invoke
+ ___66-[BrightnessSystemClientInternal setProperty:forKey:handle:error:]_block_invoke_2
+ ___67-[CBDisplayManager observeValueForKeyPath:ofObject:change:context:]_block_invoke
+ ___70-[BrightnessSystemClientInternal setSyncProperty:forKey:handle:error:]_block_invoke
+ ___block_descriptor_40_e8_32o_e45_v32?0"NSNumber"8"CBHistogramBuilder"16^B24l
+ ___block_descriptor_40_e8_32o_e45_v32?0"NSString"8"CBHistogramBuilder"16^B24l
+ ___block_descriptor_56_e8_32o40o48o_e34_v32?0Q8"NSString"16"NSNumber"24l
+ ___block_descriptor_72_e8_32o40o48o56o_e26_"NSMutableDictionary"8?0l
+ _notify_post
+ _notify_set_state
+ _objc_msgSend$_paramsFromAlsEvent:
+ _objc_msgSend$activeALSServices
+ _objc_msgSend$addDelegate:
+ _objc_msgSend$addDisplayModeObserver:
+ _objc_msgSend$biLinearInterpBetweenIndices:forPoint1:andPoint2:strengthLUT:luxCount:luxArray:nitsArray:
+ _objc_msgSend$channelAveragedColorVendorData
+ _objc_msgSend$clientSetProperty:forKey:andHandle:
+ _objc_msgSend$copyChannelAveragedColorDataFromEvent:
+ _objc_msgSend$copyInferenceForEvent:
+ _objc_msgSend$encodeBrightnessState:
+ _objc_msgSend$illuminanceHistogram:displayID:alsID:
+ _objc_msgSend$initWithDisplayManager:notifier:
+ _objc_msgSend$luminanceHistogram:withName:displayID:
+ _objc_msgSend$publishState:
+ _objc_msgSend$pushIlluminance:weight:forAlsID:
+ _objc_msgSend$reevaluateAndNotify
+ _objc_msgSend$removeDelegate:
+ _objc_msgSend$removeDisplayModeObserver:
+ _objc_msgSend$removeObjectsForKeys:
+ _objc_msgSend$setDisplayID:
+ _objc_msgSend$setModelInputWithParameters:
+ _objc_msgSend$setProperties:
+ _objc_msgSend$setSyncProperty:forKey:handle:error:
- +[CBAnalytics illuminanceHistogram:]
- +[CBAnalytics luminanceHistogram:withName:]
- -[CBCEModule setModelInputWithXtalkArr:alsArr:alsRatioArr:X:Y:Z:CCT:u:v:lux:nits:iTime:gain:x:y:a:b:ceInput:]
- -[CBColorPolicyFilter biLinearInterpBetweenIndices:forPoint1:andPoint2:]
- -[CBColorPolicyFilter interpolateBetweenX1:Y1:X2:Y2:X:]
- -[CBRingLight getTargetMinNits]
- GCC_except_table37
- GCC_except_table44
- GCC_except_table46
- __ZZ14isDarwinStableE6map_80
- __ZZ14isDarwinStableE7map_100
- __ZZ14isDarwinStableE7map_180
- ___36+[CBAnalytics illuminanceHistogram:]_block_invoke
- ___36+[CBAnalytics illuminanceHistogram:]_block_invoke_2
- ___43+[CBAnalytics luminanceHistogram:withName:]_block_invoke
- ___43+[CBAnalytics luminanceHistogram:withName:]_block_invoke_2
- ___block_descriptor_32_e45_v32?0"NSString"8"CBHistogramBuilder"16^B24l
- ___block_descriptor_40_e8_32o_e34_v32?0Q8"NSString"16"NSNumber"24l
- ___block_descriptor_48_e8_32o40o_e34_v32?0Q8"NSString"16"NSNumber"24l
- ___block_descriptor_56_e8_32o40o_e19_"NSDictionary"8?0l
- ___block_descriptor_64_e8_32o40o48o_e19_"NSDictionary"8?0l
- _objc_msgSend$biLinearInterpBetweenIndices:forPoint1:andPoint2:
- _objc_msgSend$illuminanceHistogram:
- _objc_msgSend$interpolateBetweenX1:Y1:X2:Y2:X:
- _objc_msgSend$luminanceHistogram:withName:
- _objc_msgSend$setModelInputWithXtalkArr:alsArr:alsRatioArr:X:Y:Z:CCT:u:v:lux:nits:iTime:gain:x:y:a:b:ceInput:
CStrings:
+ "%s: key=%@ error=%@"
+ "-[BacklightdExportedObj clientSetProperty:forKey:andHandle:]_block_invoke"
+ "CBBrightnessBroadcaster - init"
+ "CE"
+ "Clock has shifted backwards, adjusting the ramp"
+ "Input features: %@"
+ "MinNitsPanel"
+ "Per-ALS mitigation: serviceID=%@ model=%u threshold=%f"
+ "UIBacklightLevelChangedNotification"
+ "Unable to read kern.darkboot!"
+ "WARN: CBCE model %@ failed to load — copyInference will return nil"
+ "[Color Mitigation] Aggregated (active set): anyTriggered=%d minFilteredStrength=%f"
+ "[Color Mitigation] active ALS orientation=%d placement=%d triggered=%d filteredStrength=%f"
+ "[Color Mitigation] lux=%.1f nits=%.1f mitigated=%d ceEnabled=%d ceAttempted=%d source=%s confidence=%.3f threshold=%.3f crossedThreshold=%d strength=%.3f"
+ "_model is nil, skipping inference"
+ "alsID"
+ "baseline"
+ "com.apple.CoreBrightness.BrightnessBroadcaster"
+ "com.apple.CoreBrightness.BrightnessLevelNotifier"
+ "internal-%u"
+ "kern.darkboot"
+ "non-AARMBL init: darkBoot=%d factor=%f current=%f"
+ "notify_register_check failed for %{public}@ (status=%u)"
+ "orientation = %d, placement = %d, color mitigation = %d, ce-model = %d, ce-threshold = %f"
+ "publishing brightness state=%llu"
+ "setSyncProperty"
+ "v32@?0@\"NSNumber\"8@\"CBHistogramBuilder\"16^B24"
- "Per-ALS CE: serviceID=%@ model=%u threshold=%f"
- "[Color Mitigation] ALS orientation=%d placement=%d triggered=%d filteredStrength=%f"
- "[Color Mitigation] Aggregated mitigation: count=%lu anyTriggered=%d minFilteredStrength=%f"
- "[New Event] MIB dcpRoleID mismatch! Expected: %d, Received: %d"
- "[V2.1] Input features: %@"
- "brightness.device.current %f -> factor %f"
```
