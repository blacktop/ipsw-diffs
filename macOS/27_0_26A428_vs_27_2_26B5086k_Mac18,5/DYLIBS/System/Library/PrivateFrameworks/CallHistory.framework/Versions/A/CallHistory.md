## CallHistory

> `/System/Library/PrivateFrameworks/CallHistory.framework/Versions/A/CallHistory`

```diff

-153.100.1.1.25
-  __TEXT.__text: 0x1b5dd0
-  __TEXT.__objc_methlist: 0x39e4
+156.200.70.1.2
+  __TEXT.__text: 0x1b679c
+  __TEXT.__objc_methlist: 0x3a84
   __TEXT.__const: 0x1e6b0
-  __TEXT.__cstring: 0x4246
-  __TEXT.__oslogstring: 0x6379
-  __TEXT.__gcc_except_tab: 0x7dc
+  __TEXT.__cstring: 0x42b6
+  __TEXT.__oslogstring: 0x63f9
+  __TEXT.__gcc_except_tab: 0x7e0
   __TEXT.__dlopen_cstrs: 0xe3
   __TEXT.__constg_swiftt: 0x114cc
   __TEXT.__swift5_typeref: 0x524b

   __TEXT.__swift_as_cont: 0x104
   __TEXT.__swift5_capture: 0x3e0
   __TEXT.__swift5_mpenum: 0x14
-  __TEXT.__unwind_info: 0xabd8
+  __TEXT.__unwind_info: 0xac08
   __TEXT.__eh_frame: 0x7900
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x990
+  __DATA_CONST.__const: 0x9b8
   __DATA_CONST.__objc_classlist: 0x468
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0xd0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x25a8
+  __DATA_CONST.__objc_selrefs: 0x25e8
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x140
-  __DATA_CONST.__got: 0x9e0
-  __AUTH_CONST.__const: 0x5c48
-  __AUTH_CONST.__cfstring: 0x3740
-  __AUTH_CONST.__objc_const: 0x14af8
+  __DATA_CONST.__got: 0x9e8
+  __AUTH_CONST.__const: 0x5ca8
+  __AUTH_CONST.__cfstring: 0x3760
+  __AUTH_CONST.__objc_const: 0x14b38
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__auth_got: 0x11c0
   __AUTH.__objc_data: 0x1b88

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 12374
-  Symbols:   5936
-  CStrings:  1075
+  Functions: 12389
+  Symbols:   5962
+  CStrings:  1081
 
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
+ GCC_except_table16
+ GCC_except_table23
+ GCC_except_table29
+ GCC_except_table33
+ GCC_except_table37
+ GCC_except_table39
+ GCC_except_table41
+ GCC_except_table43
+ GCC_except_table61
+ GCC_except_table65
+ GCC_except_table67
+ GCC_except_table69
+ GCC_except_table73
+ GCC_except_table75
+ GCC_except_table77
+ GCC_except_table92
+ _CHAppMigrationErrorDomain
+ _OBJC_CLASS_$_NSError
+ __58-[CallHistoryDBClientHandle initWithDBStoreHandleFactory:]_block_invoke
+ ___109-[CHManager migrateAllDataFromExtensionWithApplicationID:toExtensionWithApplicationID:withCompletionHandler:]_block_invoke
+ ___125-[CallHistoryDBClientHandle migrateAllDataFromExtensionWithApplicationID:toExtensionWithApplicationID:withCompletionHandler:]_block_invoke
+ ___51-[CallHistoryDBClientHandle initWithDBStoreHandle:]_block_invoke
+ ___58-[CallHistoryDBClientHandle initWithDBStoreHandleFactory:]_block_invoke
+ ___block_descriptor_33_e26_"CallHistoryDBHandle"8?0l
+ ___block_descriptor_40_e8_32s_e26_"CallHistoryDBHandle"8?0l
+ ___block_descriptor_48_e8_32s40bs_e5_v8?0l
+ ___block_descriptor_64_e8_32s40s48s56bs_e5_v8?0l
+ ___copy_helper_block_e8_32s40s48s56b
+ ___destroy_helper_block_e8_32s40s48s56s
+ _objc_msgSend$applicationMigrationEnabled
+ _objc_msgSend$errorWithDomain:code:userInfo:
+ _objc_msgSend$initWithDBManager:featureFlags:
+ _objc_msgSend$initWithDBStoreHandleFactory:
+ _objc_msgSend$initWithDeviceObserver:dbManager:
+ _objc_msgSend$migrateAllDataFromExtensionWithApplicationID:toExtensionWithApplicationID:withCompletionHandler:
- -[CallHistoryDBHandle initWithDBManager:]
- GCC_except_table15
- GCC_except_table22
- GCC_except_table28
- GCC_except_table32
- GCC_except_table34
- GCC_except_table36
- GCC_except_table38
- GCC_except_table56
- GCC_except_table60
- GCC_except_table62
- GCC_except_table64
- GCC_except_table68
- GCC_except_table7
- GCC_except_table70
- GCC_except_table72
- GCC_except_table87
- __34-[CallHistoryDBClientHandle init:]_block_invoke
- ___block_descriptor_41_e8_32s_e5_v8?0l
CStrings:
+ "%ld calls found with service provider %@"
+ "156.200.70.1.2"
+ "156.200.70.1.2~1"
+ "@\"CallHistoryDBHandle\"8@?0"
+ "CallHistoryApplicationMigration"
+ "Migrating data from extension %@ to %@"
+ "Will not perform migration; feature is disabled"
+ "com.apple.CallHistory.application-migration"
- "153.100.1.1.25"
- "153.100.1.1.25~16"
```
