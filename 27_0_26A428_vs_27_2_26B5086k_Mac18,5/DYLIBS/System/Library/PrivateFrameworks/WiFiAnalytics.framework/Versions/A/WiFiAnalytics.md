## WiFiAnalytics

> `/System/Library/PrivateFrameworks/WiFiAnalytics.framework/Versions/A/WiFiAnalytics`

```diff

-830.55.0.0.0
-  __TEXT.__text: 0x15e0b4
-  __TEXT.__objc_methlist: 0x10690
-  __TEXT.__const: 0x3e8
+832.2.0.0.0
+  __TEXT.__text: 0x15e190
+  __TEXT.__objc_methlist: 0x106a8
+  __TEXT.__const: 0x3f0
   __TEXT.__dlopen_cstrs: 0x56
-  __TEXT.__cstring: 0x14d1b
-  __TEXT.__oslogstring: 0x11a0f
+  __TEXT.__cstring: 0x14cf0
+  __TEXT.__oslogstring: 0x11a25
   __TEXT.__constg_swiftt: 0x1e0
   __TEXT.__swift5_typeref: 0x154
   __TEXT.__swift5_reflstr: 0xb1

   __TEXT.__swift5_capture: 0x1b0
   __TEXT.__swift5_types: 0x4
   __TEXT.__gcc_except_tab: 0x26b0
-  __TEXT.__unwind_info: 0x3118
+  __TEXT.__unwind_info: 0x3120
   __TEXT.__eh_frame: 0x2e0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8cd0
+  __DATA_CONST.__objc_selrefs: 0x8ce0
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x390
   __DATA_CONST.__objc_arraydata: 0xa40

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 6098
-  Symbols:   10794
-  CStrings:  4064
+  Functions: 6101
+  Symbols:   10800
+  CStrings:  4063
 
Symbols:
+ +[WAUtil setSamplingDisabledForTesting:]
+ -[WAEvent caSamplingPercentage]
+ -[WAEventRoamStatus caSamplingPercentage]
+ __samplingDisabledForTesting
+ _objc_msgSend$caSamplingPercentage
+ _objc_msgSend$canPerformActionWithSamplingPercentage:
CStrings:
+ "%{public}s::%d:User manual join ssid = %@ bssid = %@ joinReason = %@ subReason = %@, checking the most recent leave event from ssid = %@, bssid = %@, isLeaveByTD = %@ entity = %@ leaveReason = %@, isLeaveToManualJoinIntervalValid = %@ interval = %@, isLeaveFromSameJoinNetwork = %@, isAlreadyEdgeBSS = %@, neutralize auto-leave decision %@"
+ "WiFiAnalytics-832.2 Sep  4 2026 23:05:07"
- "%{public}s::%d:User manual join ssid = %@ bssid = %@ joinReason = %@ subReason = %@, checking the most recent leave event from ssid = %@, bssid = %@, isLeaveByTD = %@ entity = %@ leaveReason = %@, isLeaveToManualJoinIntervalValid = %@ interval = %@, isLeaveFromSameJoinNetwork = %@, disable isEdgeForLeave decision %@"
- "WiFiAnalytics-830.55 Aug  9 2026 20:48:25"
- "WiFiAnalytics-830.55 Aug  9 2026 20:48:26"
```
