## AirPlayRoutePrediction

> `/System/Library/PrivateFrameworks/AirPlayRoutePrediction.framework/Versions/A/AirPlayRoutePrediction`

```diff

-1892.6.3.0.0
-  __TEXT.__text: 0x1601c
+1892.20.1.0.0
+  __TEXT.__text: 0x16000
   __TEXT.__auth_stubs: 0x480
-  __TEXT.__objc_methlist: 0xacc
+  __TEXT.__objc_methlist: 0xb1c
   __TEXT.__const: 0x120
-  __TEXT.__cstring: 0x12d6
-  __TEXT.__oslogstring: 0x1431
-  __TEXT.__gcc_except_tab: 0x48c
-  __TEXT.__unwind_info: 0x568
+  __TEXT.__cstring: 0x1366
+  __TEXT.__oslogstring: 0x144d
+  __TEXT.__gcc_except_tab: 0x4c4
+  __TEXT.__unwind_info: 0x580
   __TEXT.__objc_classname: 0x1b4
   __TEXT.__objc_methname: 0x2ee4
   __TEXT.__objc_methtype: 0x34b
   __TEXT.__objc_stubs: 0x2460
   __DATA_CONST.__got: 0x238
-  __DATA_CONST.__const: 0x1c8
+  __DATA_CONST.__const: 0x1d8
   __DATA_CONST.__objc_classlist: 0x78
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8

   __AUTH_CONST.__auth_got: 0x250
   __AUTH_CONST.__const: 0x790
   __AUTH_CONST.__cfstring: 0x920
-  __AUTH_CONST.__objc_const: 0x19e0
+  __AUTH_CONST.__objc_const: 0x1968
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH.__objc_data: 0x4b0

   - /System/Library/PrivateFrameworks/SoftLinking.framework/Versions/A/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: AB7F5254-E876-360D-AADB-C78EDCB20D14
-  Functions: 407
-  Symbols:   1214
-  CStrings:  806
+  UUID: CA41A68A-69F2-3E8D-B825-1318456480D9
+  Functions: 410
+  Symbols:   1217
+  CStrings:  808
 
Symbols:
+ ARPFeedbackLog.cold.1
+ ARPHomeControlLog.cold.1
+ ARPLog.cold.1
+ GCC_except_table13
CStrings:
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CoreDuet/AirPlayRoutePrediction/AirPlayRoutePrediction/ARPCorrelationTask.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CoreDuet/AirPlayRoutePrediction/AirPlayRoutePrediction/ARPFeedback.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CoreDuet/AirPlayRoutePrediction/AirPlayRoutePrediction/ARPRoutePredictor.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CoreDuet/AirPlayRoutePrediction/AirPlayRoutePrediction/ARPRoutingSession.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CoreDuet/AirPlayRoutePrediction/HomeControl/ARPHomeControlSuggester.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CoreDuet/AirPlayRoutePrediction/HomeControl/CorrelationTasks/ARPHomeControlCorrelationUtilities.m"
+ "/System/AppleInternal/Library/Frameworks/BiomeStreams.framework/BiomeStreams"
+ "/System/AppleInternal/Library/Frameworks/HomeKit.framework/HomeKit"
+ "CoreDuet: ARPCollectAndSendAnalyticsEvents"
+ "CoreDuet: ARPCorrelationTask execute"
+ "CoreDuet: ARPHomeControlMicrolocationCorrelationTask execute"
+ "CoreDuet: ARPHomeControlNextActionCorrelationTask execute"
+ "CoreDuet: ARPRoutePredictor _reloadLatestMicroLocationEvent"
+ "CoreDuet: ARPRoutePredictor _reloadPersistedSessions"
+ "CoreDuet: ARPRoutePredictor predictionsForContext:"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/CoreDuet/AirPlayRoutePrediction/AirPlayRoutePrediction/ARPCorrelationTask.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/CoreDuet/AirPlayRoutePrediction/AirPlayRoutePrediction/ARPFeedback.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/CoreDuet/AirPlayRoutePrediction/AirPlayRoutePrediction/ARPRoutePredictor.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/CoreDuet/AirPlayRoutePrediction/AirPlayRoutePrediction/ARPRoutingSession.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/CoreDuet/AirPlayRoutePrediction/HomeControl/ARPHomeControlSuggester.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/CoreDuet/AirPlayRoutePrediction/HomeControl/CorrelationTasks/ARPHomeControlCorrelationUtilities.m"
- "Duet: ARPCollectAndSendAnalyticsEvents"
- "Duet: ARPCorrelationTask execute"
- "Duet: ARPHomeControlMicrolocationCorrelationTask execute"
- "Duet: ARPHomeControlNextActionCorrelationTask execute"
- "Duet: ARPRoutePredictor _reloadLatestMicroLocationEvent"
- "Duet: ARPRoutePredictor _reloadPersistedSessions"
- "Duet: ARPRoutePredictor predictionsForContext:"

```
