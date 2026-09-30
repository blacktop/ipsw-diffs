## CPAnalytics

> `/System/Library/PrivateFrameworks/CPAnalytics.framework/CPAnalytics`

```diff

-840.1.250.0.0
-  __TEXT.__text: 0x129a8
+840.2.120.0.0
+  __TEXT.__text: 0x13158
   __TEXT.__auth_stubs: 0x590
-  __TEXT.__objc_methlist: 0x138c
+  __TEXT.__objc_methlist: 0x13d4
   __TEXT.__const: 0x180
   __TEXT.__gcc_except_tab: 0x160
-  __TEXT.__cstring: 0x1e38
+  __TEXT.__cstring: 0x1fd6
   __TEXT.__oslogstring: 0x1004
-  __TEXT.__unwind_info: 0x540
+  __TEXT.__unwind_info: 0x550
   __TEXT.__objc_classname: 0x3c1
-  __TEXT.__objc_methname: 0x35dd
+  __TEXT.__objc_methname: 0x36c8
   __TEXT.__objc_methtype: 0x4c0
-  __TEXT.__objc_stubs: 0x2f40
+  __TEXT.__objc_stubs: 0x3080
   __DATA_CONST.__got: 0x298
-  __DATA_CONST.__const: 0x880
+  __DATA_CONST.__const: 0x8b8
   __DATA_CONST.__objc_classlist: 0xd8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xd08
+  __DATA_CONST.__objc_selrefs: 0xd58
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0xb0
-  __DATA_CONST.__objc_arraydata: 0x20
+  __DATA_CONST.__objc_arraydata: 0x68
   __AUTH_CONST.__auth_got: 0x2d8
   __AUTH_CONST.__const: 0xe0
-  __AUTH_CONST.__cfstring: 0x25a0
+  __AUTH_CONST.__cfstring: 0x2740
   __AUTH_CONST.__objc_const: 0x25c0
-  __AUTH_CONST.__objc_intobj: 0x108
-  __AUTH_CONST.__objc_arrayobj: 0x18
+  __AUTH_CONST.__objc_intobj: 0x2a0
+  __AUTH_CONST.__objc_arrayobj: 0x30
   __DATA.__objc_ivar: 0x120
   __DATA.__data: 0x248
   __DATA.__bss: 0x19

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftDemangle.dylib
-  UUID: 9D9E3092-65A5-3E49-A796-33DB79506D08
-  Functions: 379
-  Symbols:   1861
-  CStrings:  1356
+  UUID: BE494D7B-AC3F-3F5F-85CC-8E2E63BC5FE3
+  Functions: 385
+  Symbols:   1887
+  CStrings:  1394
 
Symbols:
+ +[CPAnalyticsCoreAnalyticsHelper _librarySizeRangeEnum:]
+ +[CPAnalyticsCoreAnalyticsHelper upgradePayload:sourceEvent:]
+ +[PhotosAnalyticsSystemPropertyProvider deviceFreeSpaceEnum:]
+ -[CPAnalyticsAppStateDestination _computeSessionFeatureUsedData:sourceEvent:]
+ -[CPAnalyticsAppStateDestination _sendSessionFeatureUsedEvent:]
+ GCC_except_table367
+ _CPAnalyticsEventEditEntered
+ _CPAnalyticsEventFeatureUsed
+ __OBJC_$_CLASS_METHODS_PhotosAnalyticsSystemPropertyProvider
+ ___31+[CPAnalytics startAppTracking]_block_invoke.175
+ ___32+[CPAnalytics startViewTracking]_block_invoke.143
+ ___77-[CPAnalyticsAppStateDestination _computeSessionFeatureUsedData:sourceEvent:]_block_invoke
+ ___block_descriptor_40_e8_32s_e50_B24?0"CPAnalyticsEventCounter"8"NSDictionary"16ls32l8
+ ___block_literal_global.1060
+ ___block_literal_global.136
+ ___block_literal_global.145
+ _objc_msgSend$_computeSessionFeatureUsedData:sourceEvent:
+ _objc_msgSend$_librarySizeRangeEnum:
+ _objc_msgSend$_sendSessionFeatureUsedEvent:
+ _objc_msgSend$deviceFreeSpaceEnum:
+ _objc_msgSend$filteredArrayUsingPredicate:
+ _objc_msgSend$mutableCopy
+ _objc_msgSend$predicateWithBlock:
+ _objc_msgSend$setWithObjects:
+ _objc_msgSend$stringValue
+ _objc_msgSend$upgradePayload:sourceEvent:
- GCC_except_table361
- ___31+[CPAnalytics startAppTracking]_block_invoke.169
- ___32+[CPAnalytics startViewTracking]_block_invoke.137
- ___block_literal_global.1062
- ___block_literal_global.130
- ___block_literal_global.139
CStrings:
+ "B24@?0@\"CPAnalyticsEventCounter\"8@\"NSDictionary\"16"
+ "LibrarySizeRangeEmpty"
+ "LibrarySizeRangeLarge20K"
+ "LibrarySizeRangeLarge30K"
+ "LibrarySizeRangeLarge40K"
+ "LibrarySizeRangeLarge50K"
+ "LibrarySizeRangeMedium10K"
+ "LibrarySizeRangeMedium5K"
+ "LibrarySizeRangeSmall"
+ "LibrarySizeRangeVeryLarge"
+ "LibrarySizeRangeVerySmall"
+ "_computeSessionFeatureUsedData:sourceEvent:"
+ "_librarySizeRangeEnum:"
+ "_sendSessionFeatureUsedEvent:"
+ "com.apple.photos.CPAnalytics.editEntered"
+ "com.apple.photos.CPAnalytics.featureUsed"
+ "cpa_session_counter_editEntered"
+ "deviceFreeSpaceEnum:"
+ "filteredArrayUsingPredicate:"
+ "mutableCopy"
+ "predicateWithBlock:"
+ "setWithObjects:"
+ "stringValue"
+ "upgradePayload:sourceEvent:"

```
