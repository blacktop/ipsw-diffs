## AppleMediaDiscovery

> `/System/Library/PrivateFrameworks/AppleMediaDiscovery.framework/AppleMediaDiscovery`

```diff

-1.4.6.0.0
-  __TEXT.__text: 0xf24c4
+1.4.8.0.0
+  __TEXT.__text: 0xf2b60
   __TEXT.__auth_stubs: 0x1710
-  __TEXT.__objc_methlist: 0x3b50
+  __TEXT.__objc_methlist: 0x3b58
   __TEXT.__const: 0x8b8
-  __TEXT.__cstring: 0xb018
-  __TEXT.__oslogstring: 0x44f7
+  __TEXT.__cstring: 0xb088
+  __TEXT.__oslogstring: 0x4547
   __TEXT.__gcc_except_tab: 0x3018
   __TEXT.__dlopen_cstrs: 0xcc
   __TEXT.__swift5_typeref: 0x554

   __TEXT.__unwind_info: 0x1360
   __TEXT.__eh_frame: 0x660
   __TEXT.__objc_classname: 0x67d
-  __TEXT.__objc_methname: 0x9dca
+  __TEXT.__objc_methname: 0x9e82
   __TEXT.__objc_methtype: 0xddb
-  __TEXT.__objc_stubs: 0x8f00
-  __DATA_CONST.__got: 0x6b0
+  __TEXT.__objc_stubs: 0x8f60
+  __DATA_CONST.__got: 0x6b8
   __DATA_CONST.__const: 0xdb0
   __DATA_CONST.__objc_classlist: 0x2e8
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x27f8
+  __DATA_CONST.__objc_selrefs: 0x2810
   __DATA_CONST.__objc_superrefs: 0x110
   __DATA_CONST.__objc_arraydata: 0x12c0
   __AUTH_CONST.__auth_got: 0xb98
   __AUTH_CONST.__const: 0xf98
-  __AUTH_CONST.__cfstring: 0xda60
+  __AUTH_CONST.__cfstring: 0xdba0
   __AUTH_CONST.__objc_const: 0x62d0
   __AUTH_CONST.__objc_intobj: 0xcd8
   __AUTH_CONST.__objc_dictobj: 0x1068

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: A8A1958B-8849-33C8-9476-D418593A65F0
-  Functions: 1901
-  Symbols:   5318
-  CStrings:  6136
+  UUID: 7BF820ED-A7D0-3F8B-B886-0314A0D986FC
+  Functions: 1902
+  Symbols:   5324
+  CStrings:  6160
 
Symbols:
+ +[AMDBiomeIntegration writeToAppEventEngagementBiomeStream:withError:]
+ _OBJC_CLASS_$_BMAppEventEngagement
+ _objc_msgSend$EventEngagement
+ _objc_msgSend$initWithAppId:purchased:priceBucket:usage:frequency:recency:normalizedUsage:eventImpression:eventClick:appIsDownloaded:
+ _objc_msgSend$writeToAppEventEngagementBiomeStream:withError:
Functions:
~ +[AMDBiomeIntegration writeToBiome:withError:] : 1004 -> 1112
+ +[AMDBiomeIntegration writeToAppEventEngagementBiomeStream:withError:]
CStrings:
+ "AppEventEngagement"
+ "BMAppEventEngagement stream not available for iOS version < 26.1, skipping %lu events"
+ "EventEngagement"
+ "appId"
+ "appIsDownloaded"
+ "eventClick"
+ "eventImpression"
+ "frequency"
+ "initWithAppId:purchased:priceBucket:usage:frequency:recency:normalizedUsage:eventImpression:eventClick:appIsDownloaded:"
+ "priceBucket"
+ "purchased"
+ "recency"
+ "usage"
+ "writeToAppEventEngagementBiomeStream:withError:"

```
