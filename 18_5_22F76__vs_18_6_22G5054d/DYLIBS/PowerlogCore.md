## PowerlogCore

> `/System/Library/PrivateFrameworks/PowerlogCore.framework/PowerlogCore`

```diff

-2423.120.12.0.0
-  __TEXT.__text: 0xdaa34
+2423.140.8.0.0
+  __TEXT.__text: 0xda8dc
   __TEXT.__auth_stubs: 0x1a00
   __TEXT.__objc_methlist: 0x8598
   __TEXT.__const: 0x1828
-  __TEXT.__cstring: 0x38d3e
+  __TEXT.__cstring: 0x38d65
   __TEXT.__gcc_except_tab: 0x2af0
-  __TEXT.__oslogstring: 0x765d
-  __TEXT.__unwind_info: 0x2cc8
+  __TEXT.__oslogstring: 0x7666
+  __TEXT.__unwind_info: 0x2cb8
   __TEXT.__objc_classname: 0x87e
   __TEXT.__objc_methname: 0x12b56
   __TEXT.__objc_methtype: 0x17a1

   __DATA_CONST.__objc_selrefs: 0x4f90
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x2a0
-  __DATA_CONST.__objc_arraydata: 0x38a60
+  __DATA_CONST.__objc_arraydata: 0x38b50
   __AUTH_CONST.__auth_got: 0xd18
   __AUTH_CONST.__const: 0x1e20
-  __AUTH_CONST.__cfstring: 0x59940
+  __AUTH_CONST.__cfstring: 0x59ae0
   __AUTH_CONST.__objc_const: 0x8f80
   __AUTH_CONST.__objc_intobj: 0x47a0
   __AUTH_CONST.__objc_doubleobj: 0x1080

   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libsystemstats.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 4823940B-C6E2-3A90-93FE-C3B164796AFA
+  UUID: 319854A8-C675-331E-A7B3-D13207B8EF9F
   Functions: 4414
-  Symbols:   15653
-  CStrings:  27837
+  Symbols:   15651
+  CStrings:  27862
 
Symbols:
+ -[PPSSQLStorage setupDBConnections].cold.6
+ ___27-[PLArchiveManager migrate]_block_invoke.497
+ ___35-[PLArchiveManager migrateArchive:]_block_invoke.481
+ ___38-[PLArchiveManager trimCleanEnergyLog]_block_invoke.457
+ ___42+[PLSubmissionConfig clearTaskingDefaults]_block_invoke.383
+ ___42+[PLSubmissionConfig clearTaskingDefaults]_block_invoke.389
+ ___42+[PLSubmissionConfig clearTaskingDefaults]_block_invoke.395
+ ___45-[PLSubmissionConfig shouldStartTaskingToday]_block_invoke.408
+ ___45-[PLSubmissionConfig shouldStartTaskingToday]_block_invoke.414
+ ___45-[PLSubmissionConfig shouldStartTaskingToday]_block_invoke.424
+ ___45-[PLSubmissionConfig shouldStartTaskingToday]_block_invoke.435
+ ___45-[PLSubmissionConfig shouldStartTaskingToday]_block_invoke.441
+ ___45-[PLSubmissionConfig shouldStartTaskingToday]_block_invoke.450
+ ___45-[PLSubmissionConfig shouldStartTaskingToday]_block_invoke.472
+ ___45-[PLSubmissionConfig shouldStartTaskingToday]_block_invoke.478
+ ___45-[PLSubmissionConfig shouldStartTaskingToday]_block_invoke.484
+ ___45-[PLSubmissionConfig shouldStartTaskingToday]_block_invoke.491
+ ___46-[PLArchiveManager trimExtendedPersistenceLog]_block_invoke.458
+ ___47-[PLArchiveManager trimBackgroundProcessingLog]_block_invoke.459
+ ___block_literal_global.261
+ ___block_literal_global.455
+ ___block_literal_global.493
+ ___block_literal_global.502
+ _clearTaskingDefaults.classDebugEnabled.382
+ _clearTaskingDefaults.classDebugEnabled.388
+ _clearTaskingDefaults.classDebugEnabled.394
+ _clearTaskingDefaults.defaultOnce.381
+ _clearTaskingDefaults.defaultOnce.387
+ _clearTaskingDefaults.defaultOnce.393
+ _migrateArchive:.classDebugEnabled.480
+ _migrateArchive:.defaultOnce.479
+ _shouldStartTaskingToday.classDebugEnabled.407
+ _shouldStartTaskingToday.classDebugEnabled.413
+ _shouldStartTaskingToday.classDebugEnabled.434
+ _shouldStartTaskingToday.classDebugEnabled.440
+ _shouldStartTaskingToday.classDebugEnabled.449
+ _shouldStartTaskingToday.classDebugEnabled.471
+ _shouldStartTaskingToday.classDebugEnabled.477
+ _shouldStartTaskingToday.classDebugEnabled.483
+ _shouldStartTaskingToday.defaultOnce.406
+ _shouldStartTaskingToday.defaultOnce.412
+ _shouldStartTaskingToday.defaultOnce.433
+ _shouldStartTaskingToday.defaultOnce.439
+ _shouldStartTaskingToday.defaultOnce.448
+ _shouldStartTaskingToday.defaultOnce.470
+ _shouldStartTaskingToday.defaultOnce.476
+ _shouldStartTaskingToday.defaultOnce.482
- -[PLArchiveManager deprecateTablesBGSQL].cold.1
- -[PLArchiveManager trimBackgroundProcessingLog].cold.1
- ___27-[PLArchiveManager migrate]_block_invoke.499
- ___35-[PLArchiveManager migrateArchive:]_block_invoke.483
- ___38-[PLArchiveManager trimCleanEnergyLog]_block_invoke.459
- ___42+[PLSubmissionConfig clearTaskingDefaults]_block_invoke.384
- ___42+[PLSubmissionConfig clearTaskingDefaults]_block_invoke.390
- ___42+[PLSubmissionConfig clearTaskingDefaults]_block_invoke.396
- ___45-[PLSubmissionConfig shouldStartTaskingToday]_block_invoke.409
- ___45-[PLSubmissionConfig shouldStartTaskingToday]_block_invoke.415
- ___45-[PLSubmissionConfig shouldStartTaskingToday]_block_invoke.425
- ___45-[PLSubmissionConfig shouldStartTaskingToday]_block_invoke.436
- ___45-[PLSubmissionConfig shouldStartTaskingToday]_block_invoke.442
- ___45-[PLSubmissionConfig shouldStartTaskingToday]_block_invoke.451
- ___45-[PLSubmissionConfig shouldStartTaskingToday]_block_invoke.473
- ___45-[PLSubmissionConfig shouldStartTaskingToday]_block_invoke.479
- ___45-[PLSubmissionConfig shouldStartTaskingToday]_block_invoke.485
- ___45-[PLSubmissionConfig shouldStartTaskingToday]_block_invoke.492
- ___46-[PLArchiveManager trimExtendedPersistenceLog]_block_invoke.460
- ___47-[PLArchiveManager trimBackgroundProcessingLog]_block_invoke.461
- ___block_literal_global.269
- ___block_literal_global.457
- ___block_literal_global.494
- ___block_literal_global.503
- _clearTaskingDefaults.classDebugEnabled.383
- _clearTaskingDefaults.classDebugEnabled.389
- _clearTaskingDefaults.classDebugEnabled.395
- _clearTaskingDefaults.defaultOnce.382
- _clearTaskingDefaults.defaultOnce.388
- _clearTaskingDefaults.defaultOnce.394
- _migrateArchive:.classDebugEnabled.482
- _migrateArchive:.defaultOnce.481
- _shouldStartTaskingToday.classDebugEnabled.408
- _shouldStartTaskingToday.classDebugEnabled.414
- _shouldStartTaskingToday.classDebugEnabled.435
- _shouldStartTaskingToday.classDebugEnabled.441
- _shouldStartTaskingToday.classDebugEnabled.450
- _shouldStartTaskingToday.classDebugEnabled.472
- _shouldStartTaskingToday.classDebugEnabled.478
- _shouldStartTaskingToday.classDebugEnabled.484
- _shouldStartTaskingToday.defaultOnce.407
- _shouldStartTaskingToday.defaultOnce.413
- _shouldStartTaskingToday.defaultOnce.434
- _shouldStartTaskingToday.defaultOnce.440
- _shouldStartTaskingToday.defaultOnce.449
- _shouldStartTaskingToday.defaultOnce.471
- _shouldStartTaskingToday.defaultOnce.477
- _shouldStartTaskingToday.defaultOnce.483
CStrings:
+ "BasebandMetrics_TelephonyActivity_1_2"
+ "BasebandMetrics_TelephonyRegistration_1_2"
+ "F0St"
+ "F0TE"
+ "FEna"
+ "Rcp0"
+ "Rcu0"
+ "mlPm"
+ "mlpR"
+ "voBi"
+ "voKi"
+ "voPk"
+ "voPs"
+ "voSi"
+ "voWi"
- "Background Processing dB disabled"
- "PLArchiveManager::trimBGSQL: disabled"
- "background_processing_db"

```
