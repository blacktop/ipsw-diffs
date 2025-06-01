## FeedbackLogger

> `/System/Library/PrivateFrameworks/FeedbackLogger.framework/FeedbackLogger`

```diff

-3304.72.1.0.0
-  __TEXT.__text: 0x1dbec
+3305.15.1.1.2
+  __TEXT.__text: 0x1ddc8
   __TEXT.__auth_stubs: 0xf00
-  __TEXT.__objc_methlist: 0xeb8
+  __TEXT.__objc_methlist: 0xee8
   __TEXT.__const: 0x1348
   __TEXT.__cstring: 0x2400
   __TEXT.__swift5_typeref: 0x40f

   __TEXT.__swift5_assocty: 0xc0
   __TEXT.__swift5_types: 0x2c
   __TEXT.__gcc_except_tab: 0x140
-  __TEXT.__oslogstring: 0x1688
-  __TEXT.__unwind_info: 0x9dc
+  __TEXT.__oslogstring: 0x16ab
+  __TEXT.__unwind_info: 0x9e0
   __TEXT.__eh_frame: 0x5a8
   __TEXT.__objc_classname: 0x134
-  __TEXT.__objc_methname: 0x2be4
-  __TEXT.__objc_methtype: 0x6a3
-  __TEXT.__objc_stubs: 0x1e00
+  __TEXT.__objc_methname: 0x2d20
+  __TEXT.__objc_methtype: 0x6b7
+  __TEXT.__objc_stubs: 0x1e40
   __DATA_CONST.__got: 0x198
   __DATA_CONST.__const: 0x378
   __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x1930
-  __DATA_CONST.__objc_selrefs: 0xa80
+  __DATA_CONST.__objc_const: 0x1960
+  __DATA_CONST.__objc_selrefs: 0xaa8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_classrefs: 0x128
   __DATA_CONST.__objc_superrefs: 0x38

   __AUTH_CONST.__auth_got: 0x790
   __AUTH.__objc_data: 0x1f0
   __AUTH.__data: 0x448
-  __DATA.__objc_ivar: 0x11c
-  __DATA.__data: 0x6c0
+  __DATA.__objc_ivar: 0x120
+  __DATA.__data: 0x6d8
   __DATA.__common: 0x108
-  __DATA.__bss: 0x20b0
+  __DATA.__bss: 0x2088
   __DATA_DIRTY.__const: 0x20
   __DATA_DIRTY.__objc_const: 0x2c8
   __DATA_DIRTY.__objc_data: 0x280
   __DATA_DIRTY.__common: 0x8
-  __DATA_DIRTY.__bss: 0x28
+  __DATA_DIRTY.__bss: 0x38
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 24F0C28F-F4D1-312A-A5A5-60D4715DECDF
-  Functions: 971
-  Symbols:   1605
-  CStrings:  1005
+  UUID: DA7DEA3D-CB44-32EA-998A-518154F6BA21
+  Functions: 975
+  Symbols:   1616
+  CStrings:  1014
 
Symbols:
+ -[FLLoggingContext initWithFileManager:userDefaults:autoBugCapture:containerStorePathManager:]
+ -[FLLoggingContext setStoreIdToUserCachesDirectoryPathMap:]
+ -[FLLoggingContext storeIdToUserCachesDirectoryPathMap]
+ -[FLLoggingContext userCachesDirectoryPathForStore:]
+ GCC_except_table299
+ _OBJC_IVAR_$_FLLoggingContext._storeIdToUserCachesDirectoryPathMap
+ __OBJC_$_PROP_LIST_FLLoggingContext.123
+ __OBJC_$_PROP_LIST_NSObject.778
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.779
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.780
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.781
+ ___Block_byref_object_copy_.396
+ ___Block_byref_object_dispose_.397
+ ___block_literal_global.415
+ ___block_literal_global.509
+ ___block_literal_global.607
+ ___block_literal_global.787
+ _objc_msgSend$initWithFileManager:userDefaults:autoBugCapture:containerStorePathManager:
+ _objc_msgSend$storeIdToUserCachesDirectoryPathMap
+ _objc_msgSend$stringByRemovingPercentEncoding
+ _objc_msgSend$userCachesDirectoryPathForStore:
+ _sqlite3_close_v2
- GCC_except_table295
- __OBJC_$_PROP_LIST_FLLoggingContext.114
- __OBJC_$_PROP_LIST_NSObject.779
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.780
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.781
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.782
- ___Block_byref_object_copy_.395
- ___Block_byref_object_dispose_.396
- ___block_literal_global.414
- ___block_literal_global.510
- ___block_literal_global.608
- ___block_literal_global.788
- _objc_msgSend$integerValue
- _objc_msgSend$isDPGBundleID:
- _sqlite3_close
CStrings:
+ "\a"
+ "@48@0:8@16@24@32@40"
+ "SQLite close connection failed: %d"
+ "T@\"NSMutableDictionary\",C,N,V_storeIdToUserCachesDirectoryPathMap"
+ "_storeIdToUserCachesDirectoryPathMap"
+ "initWithFileManager:userDefaults:autoBugCapture:containerStorePathManager:"
+ "setStoreIdToUserCachesDirectoryPathMap:"
+ "storeIdToUserCachesDirectoryPathMap"
+ "stringByRemovingPercentEncoding"
+ "userCachesDirectoryPathForStore:"
- "\x06"

```
