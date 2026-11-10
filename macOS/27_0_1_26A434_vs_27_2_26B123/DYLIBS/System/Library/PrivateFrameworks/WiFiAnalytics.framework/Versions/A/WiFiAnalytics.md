## WiFiAnalytics

> `/System/Library/PrivateFrameworks/WiFiAnalytics.framework/Versions/A/WiFiAnalytics`

```diff

-830.55.0.0.0
-  __TEXT.__text: 0x161394
-  __TEXT.__objc_methlist: 0x10690
-  __TEXT.__const: 0x3e8
+832.2.0.0.0
+  __TEXT.__text: 0x161474
+  __TEXT.__objc_methlist: 0x106a8
+  __TEXT.__const: 0x3f0
   __TEXT.__dlopen_cstrs: 0x56
-  __TEXT.__cstring: 0x14cf1
-  __TEXT.__oslogstring: 0x11a0f
+  __TEXT.__cstring: 0x14d19
+  __TEXT.__oslogstring: 0x11a25
   __TEXT.__constg_swiftt: 0x1e0
   __TEXT.__swift5_typeref: 0x154
   __TEXT.__swift5_reflstr: 0xb1

   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8cd0
+  __DATA_CONST.__objc_selrefs: 0x8ce0
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x390
   __DATA_CONST.__objc_arraydata: 0xa40

   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__auth_got: 0x748
   __AUTH_CONST.__auth_ptr: 0x0
-  __AUTH.__objc_data: 0x458
+  __AUTH.__objc_data: 0x408
   __DATA.__objc_ivar: 0xff4
   __DATA.__data: 0x398
-  __DATA.__bss: 0x1c
-  __DATA.__common: 0x410
+  __DATA.__bss: 0x20
   __DATA_DIRTY.__objc_ivar: 0x120
-  __DATA_DIRTY.__objc_data: 0x2b48
+  __DATA_DIRTY.__objc_data: 0x2b98
   __DATA_DIRTY.__data: 0xa0
-  __DATA_DIRTY.__bss: 0x168
-  __DATA_DIRTY.__common: 0xde8
+  __DATA_DIRTY.__bss: 0x170
+  __DATA_DIRTY.__common: 0x11f8
   - /System/Library/Frameworks/CoreData.framework/Versions/A/CoreData
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreLocation.framework/Versions/A/CoreLocation

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 6098
-  Symbols:   10794
-  CStrings:  4063
+  Functions: 6101
+  Symbols:   10800
+  CStrings:  4064
 
Symbols:
+ +[WAUtil setSamplingDisabledForTesting:]
+ -[WAEvent caSamplingPercentage]
+ -[WAEventRoamStatus caSamplingPercentage]
+ __samplingDisabledForTesting
+ _objc_msgSend$caSamplingPercentage
+ _objc_msgSend$canPerformActionWithSamplingPercentage:
CStrings:
+ "%{public}s::%d:User manual join ssid = %@ bssid = %@ joinReason = %@ subReason = %@, checking the most recent leave event from ssid = %@, bssid = %@, isLeaveByTD = %@ entity = %@ leaveReason = %@, isLeaveToManualJoinIntervalValid = %@ interval = %@, isLeaveFromSameJoinNetwork = %@, isAlreadyEdgeBSS = %@, neutralize auto-leave decision %@"
+ "WiFiAnalytics-832.2 Oct  3 2026 17:38:37"
+ "WiFiAnalytics-832.2 Oct  3 2026 17:38:38"
- "%{public}s::%d:User manual join ssid = %@ bssid = %@ joinReason = %@ subReason = %@, checking the most recent leave event from ssid = %@, bssid = %@, isLeaveByTD = %@ entity = %@ leaveReason = %@, isLeaveToManualJoinIntervalValid = %@ interval = %@, isLeaveFromSameJoinNetwork = %@, disable isEdgeForLeave decision %@"
- "WiFiAnalytics-830.55 Sep 18 2026 21:57:18"
```
