## backboardd

> `/usr/libexec/backboardd`

```diff

-598.50.0.0.0
-  __TEXT.__text: 0x999cc
-  __TEXT.__auth_stubs: 0x1c20
-  __TEXT.__objc_stubs: 0xe900
-  __TEXT.__objc_methlist: 0x661c
+599.124.0.0.0
+  __TEXT.__text: 0x99e7c
+  __TEXT.__auth_stubs: 0x1c00
+  __TEXT.__objc_stubs: 0xe980
+  __TEXT.__objc_methlist: 0x667c
   __TEXT.__const: 0x3e8
-  __TEXT.__gcc_except_tab: 0x3e5c
-  __TEXT.__objc_methname: 0x149d4
-  __TEXT.__cstring: 0x74fc
-  __TEXT.__oslogstring: 0x97cc
-  __TEXT.__objc_classname: 0x1a17
-  __TEXT.__objc_methtype: 0x3fd5
+  __TEXT.__gcc_except_tab: 0x3e84
+  __TEXT.__objc_methname: 0x14b0c
+  __TEXT.__cstring: 0x747b
+  __TEXT.__objc_classname: 0x1a87
+  __TEXT.__objc_methtype: 0x408a
+  __TEXT.__oslogstring: 0x96e4
   __TEXT.__ustring: 0x2a
   __TEXT.__dlopen_cstrs: 0x62
-  __TEXT.__unwind_info: 0x2834
+  __TEXT.__unwind_info: 0x286c
   __TEXT.__eh_frame: 0x38
-  __DATA_CONST.__auth_got: 0xe28
-  __DATA_CONST.__got: 0x3c0
+  __DATA_CONST.__auth_got: 0xe18
+  __DATA_CONST.__got: 0x388
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x4b48
-  __DATA_CONST.__cfstring: 0x8080
-  __DATA_CONST.__objc_classlist: 0x570
+  __DATA_CONST.__const: 0x4bc8
+  __DATA_CONST.__cfstring: 0x8020
+  __DATA_CONST.__objc_classlist: 0x578
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x1e8
+  __DATA_CONST.__objc_protolist: 0x200
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_protorefs: 0x68
+  __DATA_CONST.__objc_classrefs: 0xa50
+  __DATA_CONST.__objc_superrefs: 0x3f0
   __DATA_CONST.__linkguard: 0x18
   __DATA_CONST.__objc_intobj: 0x348
   __DATA_CONST.__objc_doubleobj: 0x40
   __DATA_CONST.__objc_arraydata: 0x30
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0x12e88
-  __DATA.__objc_selrefs: 0x4458
-  __DATA.__objc_protorefs: 0x58
-  __DATA.__objc_classrefs: 0xa48
-  __DATA.__objc_superrefs: 0x3f0
-  __DATA.__objc_ivar: 0xe58
-  __DATA.__objc_data: 0x3660
-  __DATA.__data: 0x1790
+  __DATA.__objc_const: 0x130d0
+  __DATA.__objc_selrefs: 0x4488
+  __DATA.__objc_ivar: 0xe68
+  __DATA.__objc_data: 0x36b0
+  __DATA.__data: 0x18b0
   __DATA.__bss: 0x3c8
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsp.dylib
-  UUID: D479D5BB-1F9F-3405-BFAA-254435395FF3
-  Functions: 3035
-  Symbols:   752
-  CStrings:  7158
+  UUID: 53FD0335-077D-312D-81B6-5397BA6762D8
+  Functions: 3046
+  Symbols:   743
+  CStrings:  7167
 
Symbols:
+ _BKSHIDEventSetSmartCoverInfo
+ _BKSProximitySensorBSServiceName
+ _OBJC_CLASS_$_BKSProximityDetectionMaskChangeEvent
+ _OBJC_CLASS_$_BKSWindowServerHitTestSecurityAnalysis
- _BKSHIDEventSetSmartCoverState
- _MGGetBoolAnswer
- _OBJC_CLASS_$_BKSMutableHIDEventDeferringPredicate
- _OBJC_CLASS_$_BKSMutableWindowServerHitTestSecurityAnalysis
- __AXSClarityBoardEnabled
- _kCAWindowServerHitTestSecurityAnalysisCumulativeLayerTransform
- _kCAWindowServerHitTestSecurityAnalysisCumulativeOpacity
- _kCAWindowServerHitTestSecurityAnalysisIsInsecureFiltered
- _kCAWindowServerHitTestSecurityAnalysisOcclusionType
- _kCAWindowServerHitTestSecurityAnalysisParentsHaveInsecureLayerProperties
- _kCAWindowServerOcclusionTypeBorder
- _kCAWindowServerOcclusionTypeClipped
- _kCAWindowServerOcclusionTypeLayer
CStrings:
+ "\x11$#"
+ "%s %{public}@ Blanked: %@"
+ "%s Blanked: %@"
+ "@\"BKSProximityDetectionMaskChangeEvent\""
+ "@\"BKSProximityDetectionMaskChangeEvent\"24@0:8@\"NSNumber\"16"
+ "BKDisplayNotifySetDisplayBlanked"
+ "BKProximityServerClientRecord"
+ "BKSProximitySensorClient_IPC"
+ "BKSProximitySensorServer_IPC"
+ "BSDescriptionStreaming"
+ "Notify"
+ "Notifying (but not setting) CoreBrightness backlight factor:%f with fade duration:%f"
+ "Set"
+ "T@\"NSString\",?,R,C"
+ "Vv24@0:8@\"BKSProximityDetectionMaskChangeEvent\"16"
+ "_BKDisplayXXNotifySetDisplayBlanked"
+ "_BKHIDXXNotifySetBacklightFactorWithFadeDurationAsync"
+ "_lastObservedEvent"
+ "_lock_lastEvent"
+ "_lock_postDetectionMaskChangeToObservers"
+ "_lock_shouldSuppressTouchesWhileObjectWithinProximity"
+ "_locked_notifyIfNeededCurrentDetectionMaskChangeWithTimstamp:"
+ "_observingProximityConnections"
+ "appendCustomFormatForValue:withCustomFormatForName:"
+ "appendDescriptionToStream:"
+ "detectionMask"
+ "proximityDetectionMaskDidChange:"
+ "securityAnalysisFromCAHitTestDictionary:errorString:"
+ "setDetectionMask:"
+ "setMode:"
+ "setObservesProximitySensorDetectionMaskChanges:"
+ "setTimestamp:"
+ "stylusOpaqueTouchDigitizer"
+ "v16@?0@\"BKSMutableProximityEvent\"8"
+ "v24@0:8@\"BSDescriptionStream\"16"
+ "\x82"
- "2#"
- "3kmXfug8VcxLI5yEmsqQKw"
- "BKDisplaySetDisplayBlanked"
- "Cleaning up objects for display %{public}@ since there are no digitizers left"
- "DisplayStateControlSupported"
- "R"
- "Set %{public}@ Blanked: %@"
- "Set Blanked: %@"
- "Updating (but not setting) CoreBrightness backlight factor:%f with fade duration:%f"
- "Updating (but not setting) backlight factor pending: %f"
- "_BKDisplayXXSetDisplayBlanked"
- "_BKHIDXXSetBacklightFactorWithFadeDurationAsync"
- "_shouldSuppressTouchesWhileObjectWithinProximity"
- "destinationsStartingFromPID:deferringPredicate:"
- "hitTestSecurityAnalysisOcclusionPercent"
- "occlusionType is unexpected class:%{public}@"
- "occlusionTypeMask is %X, but there is no percentage"
- "setOcclusionMask:"
- "setOcclusionPercentage:"
- "setOcclusionType:"
- "setParentsHaveInsecureLayerProperties:"
- "setPrimaryPage:primaryUsage:"
- "v16@?0@\"BKSMutableHIDEventSenderDescriptor\"8"
- "v16@?0@\"BKSMutableWindowServerHitTestSecurityAnalysis\"8"

```
