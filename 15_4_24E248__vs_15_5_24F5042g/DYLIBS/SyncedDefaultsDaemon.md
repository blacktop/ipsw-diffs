## SyncedDefaultsDaemon

> `/System/Library/PrivateFrameworks/SyncedDefaultsDaemon.framework/Versions/A/SyncedDefaultsDaemon`

```diff

-2250.21.0.0.0
-  __TEXT.__text: 0x3be98
+2260.0.0.0.0
+  __TEXT.__text: 0x3c9b8
   __TEXT.__auth_stubs: 0x970
-  __TEXT.__objc_methlist: 0x1650
+  __TEXT.__objc_methlist: 0x1698
   __TEXT.__const: 0x136
-  __TEXT.__gcc_except_tab: 0x10b8
-  __TEXT.__cstring: 0x2139
-  __TEXT.__oslogstring: 0x6aad
+  __TEXT.__gcc_except_tab: 0x10f4
+  __TEXT.__cstring: 0x2169
+  __TEXT.__oslogstring: 0x6c56
   __TEXT.__dlopen_cstrs: 0xb5
   __TEXT.__swift5_typeref: 0x5
-  __TEXT.__unwind_info: 0xbc8
+  __TEXT.__unwind_info: 0xbf0
   __TEXT.__objc_classname: 0x1c8
-  __TEXT.__objc_methname: 0x5bc1
-  __TEXT.__objc_methtype: 0xd2b
-  __TEXT.__objc_stubs: 0x4e20
+  __TEXT.__objc_methname: 0x5cc1
+  __TEXT.__objc_methtype: 0xd3b
+  __TEXT.__objc_stubs: 0x4ee0
   __DATA_CONST.__got: 0x430
   __DATA_CONST.__const: 0x1c0
   __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x16b8
+  __DATA_CONST.__objc_selrefs: 0x16f0
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x38
   __DATA_CONST.__objc_arraydata: 0x1f8
   __AUTH_CONST.__auth_got: 0x4c8
   __AUTH_CONST.__const: 0xcd0
-  __AUTH_CONST.__cfstring: 0x2160
-  __AUTH_CONST.__objc_const: 0x1880
+  __AUTH_CONST.__cfstring: 0x2180
+  __AUTH_CONST.__objc_const: 0x1890
   __AUTH_CONST.__objc_intobj: 0xf0
   __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH_CONST.__objc_dictobj: 0x348

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 1152
-  Symbols:   2513
-  CStrings:  1891
+  Functions: 1167
+  Symbols:   2536
+  CStrings:  1907
 
Symbols:
+ +[SYDSyncManager isDataSeparated]
+ -[SYDCoreDataStore hasPerformedOneTimeDataSeparatedLocalDataReset]
+ -[SYDCoreDataStore resetPersistentStore]
+ -[SYDCoreDataStore resetPersistentStore].cold.1
+ -[SYDCoreDataStore resetPersistentStore].cold.2
+ -[SYDCoreDataStore resetPersistentStore].cold.3
+ -[SYDCoreDataStore setHasPerformedOneTimeDataSeparatedLocalDataReset:error:]
+ -[SYDCoreDataStore setHasPerformedOneTimeDataSeparatedLocalDataReset:error:].cold.1
+ -[SYDSyncManager performOneTimeDataSeparatedLocalDataResetIfNecessary]
+ -[SYDSyncManager setEngine:]
+ GCC_except_table101
+ GCC_except_table102
+ GCC_except_table119
+ GCC_except_table87
+ __49-[SYDCoreDataStore persistentContainerWithError:]_block_invoke.207
+ __49-[SYDCoreDataStore persistentContainerWithError:]_block_invoke.207.cold.1
+ __49-[SYDCoreDataStore persistentContainerWithError:]_block_invoke.207.cold.2
+ __49-[SYDCoreDataStore persistentContainerWithError:]_block_invoke.207.cold.3
+ __49-[SYDCoreDataStore persistentContainerWithError:]_block_invoke.209
+ __49-[SYDCoreDataStore persistentContainerWithError:]_block_invoke.209.cold.1
+ __49-[SYDCoreDataStore persistentContainerWithError:]_block_invoke.209.cold.2
+ __76-[SYDCoreDataStore setHasPerformedOneTimeDataSeparatedLocalDataReset:error:]_block_invoke.cold.1
+ __76-[SYDCoreDataStore setHasPerformedOneTimeDataSeparatedLocalDataReset:error:]_block_invoke.cold.2
+ ___66-[SYDCoreDataStore hasPerformedOneTimeDataSeparatedLocalDataReset]_block_invoke
+ ___70-[SYDSyncManager performOneTimeDataSeparatedLocalDataResetIfNecessary]_block_invoke
+ ___76-[SYDCoreDataStore setHasPerformedOneTimeDataSeparatedLocalDataReset:error:]_block_invoke
+ _objc_msgSend$hasPerformedOneTimeDataSeparatedLocalDataReset
+ _objc_msgSend$isDataSeparated
+ _objc_msgSend$performOneTimeDataSeparatedLocalDataResetIfNecessary
+ _objc_msgSend$resetPersistentStore
+ _objc_msgSend$setHasPerformedOneTimeDataSeparatedLocalDataReset:
+ _objc_msgSend$setHasPerformedOneTimeDataSeparatedLocalDataReset:error:
- GCC_except_table114
- GCC_except_table98
- __49-[SYDCoreDataStore persistentContainerWithError:]_block_invoke.202
- __49-[SYDCoreDataStore persistentContainerWithError:]_block_invoke.202.cold.1
- __49-[SYDCoreDataStore persistentContainerWithError:]_block_invoke.202.cold.2
- __49-[SYDCoreDataStore persistentContainerWithError:]_block_invoke.202.cold.3
- __49-[SYDCoreDataStore persistentContainerWithError:]_block_invoke.204
- __49-[SYDCoreDataStore persistentContainerWithError:]_block_invoke.204.cold.1
- __49-[SYDCoreDataStore persistentContainerWithError:]_block_invoke.204.cold.2
CStrings:
+ "About to set hasPerformedOneTimeDataSeparatedLocalDataReset=%d"
+ "B32@0:8^B16^@24"
+ "Detected data separated device that hasn't performed a one time local data reset. Performing reset now."
+ "Error fetching managed database while setting hasPerformedOneTimeDataSeparatedLocalDataReset: %@"
+ "Executing resetPersistentStore"
+ "Failed to reset persistent store due to error: %@"
+ "Reset persistent store"
+ "Saving hasPerformedOneTimeDataSeparatedLocalDataReset=%d"
+ "T@\"CKSyncEngine\",&,N,V_engine"
+ "did set hasPerformedOneTimeDataSeparatedLocalDataReset"
+ "hasPerformedOneTimeDataSeparatedLocalDataReset"
+ "isDataSeparated"
+ "performOneTimeDataSeparatedLocalDataResetIfNecessary"
+ "resetPersistentStore"
+ "setEngine:"
+ "setHasPerformedOneTimeDataSeparatedLocalDataReset:"
+ "setHasPerformedOneTimeDataSeparatedLocalDataReset:error:"
- "T@\"CKSyncEngine\",R,N,V_engine"

```
