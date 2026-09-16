## CallHistory

> `/System/Library/PrivateFrameworks/CallHistory.framework/CallHistory`

```diff

-153.100.1.2.29
-  __TEXT.__text: 0x1b179c
-  __TEXT.__objc_methlist: 0x3b5c
+156.200.70.2.2
+  __TEXT.__text: 0x1b2004
+  __TEXT.__objc_methlist: 0x3c04
   __TEXT.__const: 0x1e7e0
-  __TEXT.__cstring: 0x4264
-  __TEXT.__oslogstring: 0x62e9
+  __TEXT.__cstring: 0x42c4
+  __TEXT.__oslogstring: 0x6369
   __TEXT.__gcc_except_tab: 0x7e8
   __TEXT.__dlopen_cstrs: 0x147
   __TEXT.__constg_swiftt: 0x11538

   __TEXT.__swift_as_cont: 0x120
   __TEXT.__swift5_capture: 0x428
   __TEXT.__swift5_mpenum: 0x14
-  __TEXT.__unwind_info: 0xaed8
+  __TEXT.__unwind_info: 0xaf00
   __TEXT.__eh_frame: 0x7a88
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1630
+  __DATA_CONST.__const: 0x16a8
   __DATA_CONST.__objc_classlist: 0x478
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0xe8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x25e0
+  __DATA_CONST.__objc_selrefs: 0x2620
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x148
-  __DATA_CONST.__got: 0x9d8
+  __DATA_CONST.__got: 0x9e0
   __AUTH_CONST.__const: 0x5088
-  __AUTH_CONST.__cfstring: 0x3860
-  __AUTH_CONST.__objc_const: 0x154d0
+  __AUTH_CONST.__cfstring: 0x3880
+  __AUTH_CONST.__objc_const: 0x15510
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__auth_got: 0x13a8
   __AUTH.__objc_data: 0x1bd8

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 12466
-  Symbols:   5986
-  CStrings:  1080
+  Functions: 12479
+  Symbols:   6011
+  CStrings:  1086
 
Symbols:
+ +[CallHistoryDBHandle createWithDBManager:featureFlags:]
+ -[CHFeatureFlags applicationMigrationEnabled]
+ -[CHManager migrateAllDataFromExtensionWithApplicationID:toExtensionWithApplicationID:withCompletionHandler:]
+ -[CallDBManager initWithDeviceObserver:dbManager:]
+ -[CallHistoryDBClientHandle initWithDBStoreHandle:]
+ -[CallHistoryDBClientHandle initWithDBStoreHandleFactory:]
+ -[CallHistoryDBClientHandle migrateAllDataFromExtensionWithApplicationID:toExtensionWithApplicationID:withCompletionHandler:]
+ -[CallHistoryDBHandle initWithDBManager:featureFlags:]
+ -[CallHistoryDBHandle migrateAllDataFromExtensionWithApplicationID:toExtensionWithApplicationID:withCompletionHandler:]
+ -[SyncManager migrateAllDataFromExtensionWithApplicationID:toExtensionWithApplicationID:withCompletionHandler:]
+ GCC_except_table21
+ GCC_except_table30
+ GCC_except_table32
+ GCC_except_table52
+ GCC_except_table60
+ GCC_except_table62
+ GCC_except_table77
+ _CHAppMigrationErrorDomain
+ _OBJC_CLASS_$_NSError
+ ___109-[CHManager migrateAllDataFromExtensionWithApplicationID:toExtensionWithApplicationID:withCompletionHandler:]_block_invoke
+ ___125-[CallHistoryDBClientHandle migrateAllDataFromExtensionWithApplicationID:toExtensionWithApplicationID:withCompletionHandler:]_block_invoke
+ ___51-[CallHistoryDBClientHandle initWithDBStoreHandle:]_block_invoke
+ ___58-[CallHistoryDBClientHandle initWithDBStoreHandleFactory:]_block_invoke
+ ___58-[CallHistoryDBClientHandle initWithDBStoreHandleFactory:]_block_invoke_2
+ ___block_descriptor_33_e26_"CallHistoryDBHandle"8?0l
+ ___block_descriptor_40_e8_32s_e26_"CallHistoryDBHandle"8?0ls32l8
+ ___block_descriptor_48_e8_32s40bs_e5_v8?0ls32l8s40l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s48l8s56l8
+ _objc_msgSend$applicationMigrationEnabled
+ _objc_msgSend$errorWithDomain:code:userInfo:
+ _objc_msgSend$initWithDBManager:featureFlags:
+ _objc_msgSend$initWithDBStoreHandleFactory:
+ _objc_msgSend$initWithDeviceObserver:dbManager:
+ _objc_msgSend$migrateAllDataFromExtensionWithApplicationID:toExtensionWithApplicationID:withCompletionHandler:
- -[CallHistoryDBHandle initWithDBManager:]
- GCC_except_table16
- GCC_except_table24
- GCC_except_table44
- GCC_except_table46
- GCC_except_table56
- GCC_except_table73
- ___34-[CallHistoryDBClientHandle init:]_block_invoke_2
- ___block_descriptor_41_e8_32s_e5_v8?0ls32l8
CStrings:
+ "%ld calls found with service provider %@"
+ "156.200.70.2.2"
+ "156.200.70.2.2~3"
+ "@\"CallHistoryDBHandle\"8@?0"
+ "CallHistoryApplicationMigration"
+ "Migrating data from extension %@ to %@"
+ "Will not perform migration; feature is disabled"
+ "com.apple.CallHistory.application-migration"
- "153.100.1.2.29"
- "153.100.1.2.29~2"
```
