## backupd

> `/System/Library/PrivateFrameworks/MobileBackup.framework/backupd`

```diff

-2349.80.18.0.0
-  __TEXT.__text: 0x2bbffc
-  __TEXT.__auth_stubs: 0x37a0
+2349.80.25.0.0
+  __TEXT.__text: 0x2bca58
+  __TEXT.__auth_stubs: 0x37d0
   __TEXT.__objc_stubs: 0x2c5a0
   __TEXT.__objc_methlist: 0x18bcc
-  __TEXT.__cstring: 0x736a1
-  __TEXT.__objc_methname: 0x3b2a1
+  __TEXT.__cstring: 0x736f7
+  __TEXT.__objc_methname: 0x3b2a2
   __TEXT.__const: 0x2590
   __TEXT.__constg_swiftt: 0xc9c
-  __TEXT.__swift5_typeref: 0x1203
+  __TEXT.__swift5_typeref: 0x1217
   __TEXT.__swift5_reflstr: 0x14c5
   __TEXT.__swift5_fieldmd: 0x1554
   __TEXT.__swift5_builtin: 0x17c

   __TEXT.__objc_classname: 0x21ba
   __TEXT.__objc_methtype: 0x6c57
   __TEXT.__swift5_capture: 0x404
-  __TEXT.__oslogstring: 0x337b8
+  __TEXT.__oslogstring: 0x33803
   __TEXT.__swift5_protos: 0x20
   __TEXT.__swift5_mpenum: 0x2c
   __TEXT.__gcc_except_tab: 0xd100
   __TEXT.__ustring: 0x8
-  __TEXT.__unwind_info: 0x7900
+  __TEXT.__unwind_info: 0x7920
   __TEXT.__eh_frame: 0x27f0
-  __DATA_CONST.__auth_got: 0x1be0
-  __DATA_CONST.__got: 0xf10
-  __DATA_CONST.__auth_ptr: 0x470
+  __DATA_CONST.__auth_got: 0x1bf8
+  __DATA_CONST.__got: 0xf18
+  __DATA_CONST.__auth_ptr: 0x478
   __DATA_CONST.__const: 0x9790
-  __DATA_CONST.__cfstring: 0x20300
+  __DATA_CONST.__cfstring: 0x20320
   __DATA_CONST.__objc_classlist: 0xb00
   __DATA_CONST.__objc_catlist: 0xc0
   __DATA_CONST.__objc_protolist: 0x298

   __DATA.__objc_selrefs: 0xcbb0
   __DATA.__objc_ivar: 0x1dec
   __DATA.__objc_data: 0x7a78
-  __DATA.__data: 0x2a10
+  __DATA.__data: 0x2a20
   __DATA.__common: 0x49
   __DATA.__bss: 0x3b00
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 10909
-  Symbols:   1498
-  CStrings:  25380
+  Functions: 10914
+  Symbols:   1502
+  CStrings:  25385
 
Symbols:
+ _$sSayxGSlsMc
+ _$ss12_ArrayBufferV20_consumeAndCreateNew14bufferIsUnique15minimumCapacity13growForAppendAByxGSb_SiSbtFyXl_Ts5
+ _malloc
+ _swift_isUniquelyReferenced_nonNull_bridgeObject
CStrings:
+ "\nSELECT assetSize\n FROM  RestorableAssets\n JOIN  Restorables ON\n      (RestorableAssets.inode = Restorables.inode\n   AND RestorableAssets.domainID = Restorables.domainID\n      )\n WHERE RestorableAssets.assetState = %u\n   AND Restorables.restoreState != %u\n   AND Restorables.restoreState != %u\n   AND RestorableAssets.domainID = %llu\n GROUP BY RestorableAssets.inode;"
+ "\nSELECT assetSize\n FROM  RestorableAssets\n JOIN  Restorables ON\n      (RestorableAssets.inode = Restorables.inode\n   AND RestorableAssets.domainID = Restorables.domainID\n      )\n WHERE RestorableAssets.assetState = %u\n   AND Restorables.restoreState != %u\n   AND Restorables.restoreState != %u\n GROUP BY RestorableAssets.inode;"
+ "-[MBCKManager _getBackupListWithOperationTracker:shouldFilter:error:]"
+ "-[MBCKManager _getBackupListWithOperationTracker:shouldFilter:error:]_block_invoke"
+ "-[MBCKManager _getBackupListWithOperationTracker:shouldFilter:error:]_block_invoke_4"
+ "Cannot restore domain root %@ for %@ as symlink"
+ "Cannot restore domain root as symlink"
+ "Unknown %@ server value %@"
+ "_getBackupListWithOperationTracker:shouldFilter:error:"
- "\nSELECT \n  SUM (assetSize)\n FROM  RestorableAssets\n JOIN  Restorables ON\n      (RestorableAssets.inode = Restorables.inode\n   AND RestorableAssets.domainID = Restorables.domainID\n      )\n WHERE RestorableAssets.assetState = %u\n   AND Restorables.restoreState != %u\n   AND Restorables.restoreState != %u\n GROUP BY RestorableAssets.inode;"
- "\nSELECT \n  SUM (assetSize),\n  COUNT(*)\n FROM  RestorableAssets\n JOIN  Restorables ON\n      (RestorableAssets.inode = Restorables.inode\n   AND RestorableAssets.domainID = Restorables.domainID\n      )\n WHERE RestorableAssets.assetState = %u\n   AND Restorables.restoreState != %u\n   AND Restorables.restoreState != %u\n   AND RestorableAssets.domainID = %llu\n GROUP BY RestorableAssets.inode;"
- "-[MBCKManager getBackupListWithOperationTracker:shouldFilter:error:]"
- "-[MBCKManager getBackupListWithOperationTracker:shouldFilter:error:]_block_invoke"
- "-[MBCKManager getBackupListWithOperationTracker:shouldFilter:error:]_block_invoke_4"
- "getBackupListWithOperationTracker:shouldFilter:error:"

```
