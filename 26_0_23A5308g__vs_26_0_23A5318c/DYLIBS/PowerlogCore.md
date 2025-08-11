## PowerlogCore

> `/System/Library/PrivateFrameworks/PowerlogCore.framework/PowerlogCore`

```diff

-2964.0.137.0.0
-  __TEXT.__text: 0xdc328
+2964.2.3.0.0
+  __TEXT.__text: 0xdc4f0
   __TEXT.__auth_stubs: 0x1ad0
   __TEXT.__objc_methlist: 0x8a48
   __TEXT.__const: 0x1880
-  __TEXT.__cstring: 0x3ac8e
-  __TEXT.__oslogstring: 0x7cef
+  __TEXT.__cstring: 0x3acdd
+  __TEXT.__oslogstring: 0x7daa
   __TEXT.__gcc_except_tab: 0x29e4
-  __TEXT.__unwind_info: 0x2e00
+  __TEXT.__unwind_info: 0x2e08
   __TEXT.__objc_classname: 0x90f
   __TEXT.__objc_methname: 0x1303f
   __TEXT.__objc_methtype: 0x1909

   __DATA_CONST.__objc_selrefs: 0x5160
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x2b0
-  __DATA_CONST.__objc_arraydata: 0x3c9e0
+  __DATA_CONST.__objc_arraydata: 0x3ca00
   __AUTH_CONST.__auth_got: 0xd80
   __AUTH_CONST.__const: 0x23e0
-  __AUTH_CONST.__cfstring: 0x5f080
+  __AUTH_CONST.__cfstring: 0x5f0e0
   __AUTH_CONST.__objc_const: 0x9440
   __AUTH_CONST.__objc_intobj: 0x4818
   __AUTH_CONST.__objc_doubleobj: 0x10c0

   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libsystemstats.dylib
   - /usr/lib/libz.1.dylib
-  UUID: C9630ABA-D276-3BB7-804B-E273C4AB0F27
-  Functions: 4584
-  Symbols:   16013
-  CStrings:  29346
+  UUID: 8EDD3326-80F8-3F7E-8B20-531B4DAB8DD0
+  Functions: 4587
+  Symbols:   16031
+  CStrings:  29355
 
Symbols:
+ -[PLSubmissionFileSP copyAndPrepareLog].cold.7
+ -[PLSubmissionFileSP copyAndPrepareLog].cold.8
+ -[PLSubmissionFileSP copyAndPrepareLog].cold.9
+ ___27-[PLArchiveManager migrate]_block_invoke.584
+ ___35-[PLArchiveManager migrateArchive:]_block_invoke.568
+ ___46-[PLArchiveManager trimExtendedPersistenceLog]_block_invoke.546
+ ___47-[PLArchiveManager trimBackgroundProcessingLog]_block_invoke.547
+ ___block_literal_global.536
+ _migrateArchive:.classDebugEnabled.567
+ _migrateArchive:.defaultOnce.566
- ___27-[PLArchiveManager migrate]_block_invoke.578
- ___35-[PLArchiveManager migrateArchive:]_block_invoke.562
- ___46-[PLArchiveManager trimExtendedPersistenceLog]_block_invoke.540
- ___47-[PLArchiveManager trimBackgroundProcessingLog]_block_invoke.541
- ___block_literal_global.493
- _migrateArchive:.classDebugEnabled.561
- _migrateArchive:.defaultOnce.560
CStrings:
+ "HeartRateCoordinator"
+ "SMC_AccumulatedLookUpTable_1_2"
+ "SMC_InstantLookUpTable_2_2"
+ "Stopping due to nil dates: startDateInSystem=%@, endDateInSystem=%@"
+ "Stopping due to nil tag: serializedTag=%@"
+ "Stopping since startDate > endDate: startDateInSystem=%@, endDateInSystem=%@"

```
