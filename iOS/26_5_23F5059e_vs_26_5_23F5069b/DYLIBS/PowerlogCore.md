## PowerlogCore

> `/System/Library/PrivateFrameworks/PowerlogCore.framework/PowerlogCore`

```diff

-3031.120.25.0.0
-  __TEXT.__text: 0xe6390
-  __TEXT.__auth_stubs: 0x1ab0
-  __TEXT.__objc_methlist: 0x8ac0
+3031.122.1.0.0
+  __TEXT.__text: 0xe6704
+  __TEXT.__auth_stubs: 0x1ac0
+  __TEXT.__objc_methlist: 0x8ad8
   __TEXT.__const: 0x1b70
-  __TEXT.__cstring: 0x3cbdc
-  __TEXT.__oslogstring: 0x7ded
+  __TEXT.__cstring: 0x3d012
+  __TEXT.__oslogstring: 0x7ef8
   __TEXT.__gcc_except_tab: 0x2944
-  __TEXT.__unwind_info: 0x3038
+  __TEXT.__unwind_info: 0x3030
   __TEXT.__objc_classname: 0x90f
-  __TEXT.__objc_methname: 0x13144
+  __TEXT.__objc_methname: 0x1319e
   __TEXT.__objc_methtype: 0x1917
-  __TEXT.__objc_stubs: 0xfb00
+  __TEXT.__objc_stubs: 0xfb40
   __DATA_CONST.__got: 0x7a8
   __DATA_CONST.__const: 0x2598
   __DATA_CONST.__objc_classlist: 0x350

   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x51b8
+  __DATA_CONST.__objc_selrefs: 0x51c8
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x2b0
-  __DATA_CONST.__objc_arraydata: 0x3ef30
-  __AUTH_CONST.__auth_got: 0xd70
+  __DATA_CONST.__objc_arraydata: 0x3f1d0
+  __AUTH_CONST.__auth_got: 0xd78
   __AUTH_CONST.__const: 0x2440
-  __AUTH_CONST.__cfstring: 0x62320
-  __AUTH_CONST.__objc_const: 0x9440
+  __AUTH_CONST.__cfstring: 0x62820
+  __AUTH_CONST.__objc_const: 0x9470
   __AUTH_CONST.__objc_intobj: 0x4968
   __AUTH_CONST.__objc_doubleobj: 0x12d0
   __AUTH_CONST.__objc_arrayobj: 0x1158
-  __AUTH_CONST.__objc_dictobj: 0xf168
+  __AUTH_CONST.__objc_dictobj: 0xf190
   __AUTH.__objc_data: 0x460
-  __DATA.__objc_ivar: 0x654
+  __DATA.__objc_ivar: 0x658
   __DATA.__data: 0x4a0
   __DATA.__bss: 0x1621
   __DATA.__common: 0x10

   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libsystemstats.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 7C8D6143-1A48-355C-9ED9-F998768933DB
-  Functions: 4629
-  Symbols:   16329
-  CStrings:  30176
+  UUID: 4351C2FD-0E2C-30BA-8D42-B2ABC0561BAA
+  Functions: 4633
+  Symbols:   16339
+  CStrings:  30265
 
Symbols:
+ -[PLSubmissionConfig mssCycleInterval]
+ -[PLSubmissionConfig setMssCycleInterval:]
+ -[PLSubmissions taskingCleanup].cold.1
+ -[PLSubmissions taskingModeSetup].cold.2
+ _OBJC_IVAR_$_PLSubmissionConfig._mssCycleInterval
+ ___33-[PLSubmissions taskingModeSetup]_block_invoke.350
+ ___33-[PLSubmissions taskingModeSetup]_block_invoke.365
+ ___33-[PLSubmissions taskingModeSetup]_block_invoke_2.360
+ ___42+[PLSubmissionConfig clearTaskingDefaults]_block_invoke.390
+ ___42+[PLSubmissionConfig clearTaskingDefaults]_block_invoke.396
+ ___42+[PLSubmissionConfig clearTaskingDefaults]_block_invoke.402
+ ___45-[PLSubmissionConfig shouldStartTaskingToday]_block_invoke.422
+ ___45-[PLSubmissionConfig shouldStartTaskingToday]_block_invoke.428
+ ___45-[PLSubmissionConfig shouldStartTaskingToday]_block_invoke.438
+ ___45-[PLSubmissionConfig shouldStartTaskingToday]_block_invoke.449
+ ___45-[PLSubmissionConfig shouldStartTaskingToday]_block_invoke.455
+ ___45-[PLSubmissionConfig shouldStartTaskingToday]_block_invoke.464
+ ___45-[PLSubmissionConfig shouldStartTaskingToday]_block_invoke.486
+ ___45-[PLSubmissionConfig shouldStartTaskingToday]_block_invoke.492
+ ___45-[PLSubmissionConfig shouldStartTaskingToday]_block_invoke.498
+ ___45-[PLSubmissionConfig shouldStartTaskingToday]_block_invoke.505
+ ___block_literal_global.387
+ ___block_literal_global.507
+ ___block_literal_global.516
+ _clearTaskingDefaults.classDebugEnabled.389
+ _clearTaskingDefaults.classDebugEnabled.395
+ _clearTaskingDefaults.classDebugEnabled.401
+ _clearTaskingDefaults.defaultOnce.388
+ _clearTaskingDefaults.defaultOnce.394
+ _clearTaskingDefaults.defaultOnce.400
+ _objc_msgSend$mssCycleInterval
+ _objc_msgSend$setMssCycleInterval:
+ _shouldStartTaskingToday.classDebugEnabled.421
+ _shouldStartTaskingToday.classDebugEnabled.427
+ _shouldStartTaskingToday.classDebugEnabled.448
+ _shouldStartTaskingToday.classDebugEnabled.454
+ _shouldStartTaskingToday.classDebugEnabled.463
+ _shouldStartTaskingToday.classDebugEnabled.485
+ _shouldStartTaskingToday.classDebugEnabled.491
+ _shouldStartTaskingToday.classDebugEnabled.497
+ _shouldStartTaskingToday.defaultOnce.420
+ _shouldStartTaskingToday.defaultOnce.426
+ _shouldStartTaskingToday.defaultOnce.447
+ _shouldStartTaskingToday.defaultOnce.453
+ _shouldStartTaskingToday.defaultOnce.462
+ _shouldStartTaskingToday.defaultOnce.484
+ _shouldStartTaskingToday.defaultOnce.490
+ _shouldStartTaskingToday.defaultOnce.496
+ _systemstats_set_microstackshot_cycle_interval_xlog_tasking
- ___33-[PLSubmissions taskingModeSetup]_block_invoke.347
- ___33-[PLSubmissions taskingModeSetup]_block_invoke.362
- ___33-[PLSubmissions taskingModeSetup]_block_invoke_2.357
- ___42+[PLSubmissionConfig clearTaskingDefaults]_block_invoke.387
- ___42+[PLSubmissionConfig clearTaskingDefaults]_block_invoke.393
- ___42+[PLSubmissionConfig clearTaskingDefaults]_block_invoke.399
- ___45-[PLSubmissionConfig shouldStartTaskingToday]_block_invoke.419
- ___45-[PLSubmissionConfig shouldStartTaskingToday]_block_invoke.425
- ___45-[PLSubmissionConfig shouldStartTaskingToday]_block_invoke.435
- ___45-[PLSubmissionConfig shouldStartTaskingToday]_block_invoke.446
- ___45-[PLSubmissionConfig shouldStartTaskingToday]_block_invoke.452
- ___45-[PLSubmissionConfig shouldStartTaskingToday]_block_invoke.461
- ___45-[PLSubmissionConfig shouldStartTaskingToday]_block_invoke.483
- ___45-[PLSubmissionConfig shouldStartTaskingToday]_block_invoke.489
- ___45-[PLSubmissionConfig shouldStartTaskingToday]_block_invoke.495
- ___45-[PLSubmissionConfig shouldStartTaskingToday]_block_invoke.502
- ___block_literal_global.349
- ___block_literal_global.384
- ___block_literal_global.504
- ___block_literal_global.513
- _clearTaskingDefaults.classDebugEnabled.386
- _clearTaskingDefaults.classDebugEnabled.392
- _clearTaskingDefaults.classDebugEnabled.398
- _clearTaskingDefaults.defaultOnce.385
- _clearTaskingDefaults.defaultOnce.391
- _clearTaskingDefaults.defaultOnce.397
- _shouldStartTaskingToday.classDebugEnabled.418
- _shouldStartTaskingToday.classDebugEnabled.424
- _shouldStartTaskingToday.classDebugEnabled.445
- _shouldStartTaskingToday.classDebugEnabled.451
- _shouldStartTaskingToday.classDebugEnabled.460
- _shouldStartTaskingToday.classDebugEnabled.482
- _shouldStartTaskingToday.classDebugEnabled.488
- _shouldStartTaskingToday.classDebugEnabled.494
- _shouldStartTaskingToday.defaultOnce.417
- _shouldStartTaskingToday.defaultOnce.423
- _shouldStartTaskingToday.defaultOnce.444
- _shouldStartTaskingToday.defaultOnce.450
- _shouldStartTaskingToday.defaultOnce.459
- _shouldStartTaskingToday.defaultOnce.481
- _shouldStartTaskingToday.defaultOnce.487
- _shouldStartTaskingToday.defaultOnce.493
CStrings:
+ "Failed to restore MSS cycle interval to default: %d"
+ "Failed to set MSS cycle interval override to %llu: %d"
+ "PLTaskingMSSCycleInterval"
+ "Pipeline"
+ "PipelineProgress"
+ "Restoring MSS cycle interval to systemstats default"
+ "Setting MSS cycle interval from tasking blob: %llu cycles"
+ "Setting MSS cycle interval to default: %llu cycles"
+ "T@\"NSNumber\",&,V_mssCycleInterval"
+ "_mssCycleInterval"
+ "allKnownItems"
+ "completeness"
+ "completenessFirstTimeInterval"
+ "completenessSecondTimeInterval"
+ "completenessThirdTimeInterval"
+ "days"
+ "donatedItems"
+ "donationsSinceLastReport"
+ "eligibleItems"
+ "instantProcessedItemsSinceLastReport"
+ "instantUnprocessedItemsSinceLastReport"
+ "itemsAwaitingIndexProcessing"
+ "itemsAwaitingJournalProcessing"
+ "itemsAwaitingRedonation"
+ "itemsAwaitingReindex"
+ "itemsFailedProcessingSinceLastReport"
+ "itemsNeedProcessing"
+ "itemsNeedUpdate"
+ "itemsNeedingDonation"
+ "itemsNeedingDonationForRedonationRequests"
+ "itemsProcessed"
+ "itemsProcessedSinceLastReport"
+ "itemsUnprocessedWithProcessingError"
+ "itemsWithProcessingResults"
+ "itemsWithProcessingResultsSinceLastReport"
+ "itemsWithSecondaryResult"
+ "journalsPurgedBeforeAllProcessingCompleteSinceLastReport"
+ "mssCycleInterval"
+ "partiallyDonatedItems"
+ "priorityProcessedItemsSinceLastReport"
+ "priorityUnprocessedItemsSinceLastReport"
+ "processedRedonationsRequestedSinceLastReport"
+ "redonationsRequestedSinceLastReport"
+ "score"
+ "setMssCycleInterval:"
+ "timeSinceLastReport"
+ "timeSinceNewestUndonatedItem"
+ "timeSinceNewestUnprocessedItem"
+ "timeSpentProcessingSinceLastReport"

```
