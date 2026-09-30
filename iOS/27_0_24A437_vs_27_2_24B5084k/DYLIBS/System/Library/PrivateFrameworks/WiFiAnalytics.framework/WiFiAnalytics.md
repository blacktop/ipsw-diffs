## WiFiAnalytics

> `/System/Library/PrivateFrameworks/WiFiAnalytics.framework/WiFiAnalytics`

```diff

-825.58.0.0.0
-  __TEXT.__text: 0x152f84
-  __TEXT.__objc_methlist: 0x10690
-  __TEXT.__const: 0x3d8
+827.3.0.0.0
+  __TEXT.__text: 0x153054
+  __TEXT.__objc_methlist: 0x106a8
+  __TEXT.__const: 0x3e0
   __TEXT.__dlopen_cstrs: 0x56
-  __TEXT.__cstring: 0x14e24
-  __TEXT.__oslogstring: 0x11b30
+  __TEXT.__cstring: 0x14e23
+  __TEXT.__oslogstring: 0x11b46
   __TEXT.__constg_swiftt: 0x1e0
   __TEXT.__swift5_typeref: 0x154
   __TEXT.__swift5_reflstr: 0xb1

   __TEXT.__swift5_capture: 0x1b0
   __TEXT.__swift5_types: 0x4
   __TEXT.__gcc_except_tab: 0x2754
-  __TEXT.__unwind_info: 0x3070
+  __TEXT.__unwind_info: 0x3078
   __TEXT.__eh_frame: 0x2e0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8ce0
+  __DATA_CONST.__objc_selrefs: 0x8cf0
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x390
   __DATA_CONST.__objc_arraydata: 0xa40

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 6053
-  Symbols:   10791
+  Functions: 6056
+  Symbols:   10797
   CStrings:  4080
 
Symbols:
+ +[WAUtil setSamplingDisabledForTesting:]
+ -[WAEvent caSamplingPercentage]
+ -[WAEventRoamStatus caSamplingPercentage]
+ __samplingDisabledForTesting
+ _objc_msgSend$caSamplingPercentage
+ _objc_msgSend$canPerformActionWithSamplingPercentage:
Functions:
~ -[WAEvent submitEventToCA] : 128 -> 168
~ +[LinkChangePolicyHandler processJoinEvent:on:] : 2156 -> 2244
+ -[WAEvent eventDate]
~ +[WAUtil canPerformActionWithSamplingPercentage:] : 48 -> 72
+ +[WAUtil setSamplingDisabledForTesting:]
+ -[WAEventRoamStatus caSamplingPercentage]
CStrings:
+ "%{public}s::%d:User manual join ssid = %@ bssid = %@ joinReason = %@ subReason = %@, checking the most recent leave event from ssid = %@, bssid = %@, isLeaveByTD = %@ entity = %@ leaveReason = %@, isLeaveToManualJoinIntervalValid = %@ interval = %@, isLeaveFromSameJoinNetwork = %@, isAlreadyEdgeBSS = %@, neutralize auto-leave decision %@"
+ "WiFiAnalytics-827.3 Sep  4 2026 20:49:43"
- "%{public}s::%d:User manual join ssid = %@ bssid = %@ joinReason = %@ subReason = %@, checking the most recent leave event from ssid = %@, bssid = %@, isLeaveByTD = %@ entity = %@ leaveReason = %@, isLeaveToManualJoinIntervalValid = %@ interval = %@, isLeaveFromSameJoinNetwork = %@, disable isEdgeForLeave decision %@"
- "WiFiAnalytics-825.58 Aug 27 2026 20:48:17"
```
