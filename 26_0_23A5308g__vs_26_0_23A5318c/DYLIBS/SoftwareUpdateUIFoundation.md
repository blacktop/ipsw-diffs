## SoftwareUpdateUIFoundation

> `/System/Library/PrivateFrameworks/SoftwareUpdateUIFoundation.framework/SoftwareUpdateUIFoundation`

```diff

   __TEXT.__text: 0x790e0
   __TEXT.__auth_stubs: 0xa90
   __TEXT.__objc_methlist: 0x1784
-  __TEXT.__cstring: 0x4c15
+  __TEXT.__cstring: 0x4c25
   __TEXT.__gcc_except_tab: 0x5270
   __TEXT.__oslogstring: 0x863b
   __TEXT.__const: 0xe48

   __TEXT.__objc_methtype: 0x86e
   __TEXT.__objc_stubs: 0x2c20
   __DATA_CONST.__got: 0x2d0
-  __DATA_CONST.__const: 0x19e0
+  __DATA_CONST.__const: 0x1a00
   __DATA_CONST.__objc_classlist: 0x148
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x38

   __DATA_CONST.__objc_superrefs: 0xd0
   __AUTH_CONST.__auth_got: 0x558
   __AUTH_CONST.__const: 0x598
-  __AUTH_CONST.__cfstring: 0x2fa0
+  __AUTH_CONST.__cfstring: 0x2fc0
   __AUTH_CONST.__objc_const: 0x43c8
   __AUTH.__objc_data: 0xcd0
   __AUTH.__data: 0x128

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 2B4A00BF-756E-33C1-B99B-D14EABCCFB23
+  UUID: BB33F9D0-6780-3713-AC6E-94DC874E720D
   Functions: 1113
-  Symbols:   3052
-  CStrings:  1896
+  Symbols:   3056
+  CStrings:  1898
 
Symbols:
+ _MA_AUTO_ASSET_SHORT_TERM_LOCK_FILESYSTEM_SPECIFIC
+ ___102-[SUUIStatefulUIManager downloadAndInstall:operationDelegate:delegateCallbackQueue:completionHandler:]_block_invoke.343
+ ___102-[SUUIStatefulUIManager downloadAndInstall:operationDelegate:delegateCallbackQueue:completionHandler:]_block_invoke_2.344
+ ___104-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:afterPurgeConfirmation:activity:completionHandler:]_block_invoke.507
+ ___104-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:afterPurgeConfirmation:activity:completionHandler:]_block_invoke.508
+ ___104-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:afterPurgeConfirmation:activity:completionHandler:]_block_invoke.509
+ ___108-[SUUIStatefulUIManager promoteTargetedUpdateToUserInitiatedStatus:delegateCallbackQueue:completionHandler:]_block_invoke.391
+ ___108-[SUUIStatefulUIManager promoteTargetedUpdateToUserInitiatedStatus:delegateCallbackQueue:completionHandler:]_block_invoke_2.392
+ ___109-[SUUIStatefulUIManager downloadAndScheduleUpdate:operationDelegate:delegateCallbackQueue:completionHandler:]_block_invoke.354
+ ___109-[SUUIStatefulUIManager downloadAndScheduleUpdate:operationDelegate:delegateCallbackQueue:completionHandler:]_block_invoke_2.355
+ ___111-[SUUIStatefulUIManager unscheduleTargetedUpdateAutomaticInstallation:delegateCallbackQueue:completionHandler:]_block_invoke.402
+ ___111-[SUUIStatefulUIManager unscheduleTargetedUpdateAutomaticInstallation:delegateCallbackQueue:completionHandler:]_block_invoke_2.403
+ ___165-[SUUIStatefulUIManager performUpdateOnDownloadByApplyingSelector:context:description:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:]_block_invoke.487
+ ___165-[SUUIStatefulUIManager performUpdateOnDownloadByApplyingSelector:context:description:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:]_block_invoke.488
+ ___165-[SUUIStatefulUIManager performUpdateOnDownloadByApplyingSelector:context:description:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:]_block_invoke.489
+ ___189-[SUUIStatefulUIManager performUpdateWithDescriptor:byApplyingSelector:context:description:auxiliaryOperation:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:]_block_invoke.474
+ ___189-[SUUIStatefulUIManager performUpdateWithDescriptor:byApplyingSelector:context:description:auxiliaryOperation:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:]_block_invoke.475
+ ___189-[SUUIStatefulUIManager performUpdateWithDescriptor:byApplyingSelector:context:description:auxiliaryOperation:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:]_block_invoke.480
+ ___189-[SUUIStatefulUIManager performUpdateWithDescriptor:byApplyingSelector:context:description:auxiliaryOperation:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:]_block_invoke.481
+ ___189-[SUUIStatefulUIManager performUpdateWithDescriptor:byApplyingSelector:context:description:auxiliaryOperation:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:]_block_invoke.482
+ ___41-[SUUIStatefulUIManager performFullScan:]_block_invoke.462
+ ___41-[SUUIStatefulUIManager performFullScan:]_block_invoke.463
+ ___44-[SUUIStatefulUIManager performRefreshScan:]_block_invoke.467
+ ___46-[SUUIStatefulUIManager handleFailedFullScan:]_block_invoke.470
+ ___47-[SUUIStatefulUIManager handleFullScanResults:]_block_invoke.469
+ ___59-[SUUIStatefulUIManager refreshStateWithCompletion:forced:]_block_invoke.320
+ ___63-[SUUIStatefulUIManager unenrollFromBetaUpdatesWithCompletion:]_block_invoke.421
+ ___63-[SUUIStatefulUIManager unenrollFromBetaUpdatesWithCompletion:]_block_invoke.425
+ ___63-[SUUIStatefulUIManager unenrollFromBetaUpdatesWithCompletion:]_block_invoke.427
+ ___63-[SUUIStatefulUIManager unenrollFromBetaUpdatesWithCompletion:]_block_invoke.429
+ ___63-[SUUIStatefulUIManager unenrollFromBetaUpdatesWithCompletion:]_block_invoke.434
+ ___63-[SUUIStatefulUIManager unenrollFromBetaUpdatesWithCompletion:]_block_invoke.435
+ ___63-[SUUIStatefulUIManager unenrollFromBetaUpdatesWithCompletion:]_block_invoke_2.428
+ ___63-[SUUIStatefulUIManager unenrollFromBetaUpdatesWithCompletion:]_block_invoke_2.430
+ ___69-[SUUIStatefulUIManager performFullScanWithScanResults:andScanError:]_block_invoke.465
+ ___69-[SUUIStatefulUIManager performFullScanWithScanResults:andScanError:]_block_invoke.466
+ ___70-[SUUIStatefulUIManager enrollInBetaUpdatesProgram:completionHandler:]_block_invoke.409
+ ___70-[SUUIStatefulUIManager enrollInBetaUpdatesProgram:completionHandler:]_block_invoke.416
+ ___70-[SUUIStatefulUIManager enrollInBetaUpdatesProgram:completionHandler:]_block_invoke.418
+ ___75-[SUUIStatefulUIManager refreshBetaUpdates:withRecheckForAvailableUpdates:]_block_invoke.439
+ ___75-[SUUIStatefulUIManager refreshBetaUpdates:withRecheckForAvailableUpdates:]_block_invoke.440
+ ___75-[SUUIStatefulUIManager refreshBetaUpdates:withRecheckForAvailableUpdates:]_block_invoke.444
+ ___75-[SUUIStatefulUIManager refreshBetaUpdates:withRecheckForAvailableUpdates:]_block_invoke.445
+ ___75-[SUUIStatefulUIManager refreshBetaUpdates:withRecheckForAvailableUpdates:]_block_invoke_2.446
+ ___77-[SUUIStatefulUIManager checkForAvailableUpdatesWithForcedReload:completion:]_block_invoke.317
+ ___80-[SUUIStatefulUIManager checkForUpdatesInBackgroundWithForcedReload:completion:]_block_invoke.325
+ ___81-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:activity:completionHandler:]_block_invoke.496
+ ___81-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:activity:completionHandler:]_block_invoke.497
+ ___81-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:activity:completionHandler:]_block_invoke.498
+ ___81-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:activity:completionHandler:]_block_invoke.502
+ ___81-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:activity:completionHandler:]_block_invoke.503
+ ___81-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:activity:completionHandler:]_block_invoke_2.499
+ ___95-[SUUIStatefulUIManager performPostUpdateOperationRefreshWithDownload:error:completionHandler:]_block_invoke.490
+ ___97-[SUUIStatefulUIManager installUpdate:operationDelegate:delegateCallbackQueue:completionHandler:]_block_invoke.365
+ ___97-[SUUIStatefulUIManager installUpdate:operationDelegate:delegateCallbackQueue:completionHandler:]_block_invoke_2.368
+ ___98-[SUUIStatefulUIManager downloadUpdate:operationDelegate:delegateCallbackQueue:completionHandler:]_block_invoke.330
+ ___98-[SUUIStatefulUIManager downloadUpdate:operationDelegate:delegateCallbackQueue:completionHandler:]_block_invoke_2.333
+ ___98-[SUUIStatefulUIManager scheduleUpdate:operationDelegate:delegateCallbackQueue:completionHandler:]_block_invoke.378
+ ___98-[SUUIStatefulUIManager scheduleUpdate:operationDelegate:delegateCallbackQueue:completionHandler:]_block_invoke_2.381
+ ___block_literal_global.342
+ ___block_literal_global.352
+ ___block_literal_global.363
+ ___block_literal_global.376
+ ___block_literal_global.389
+ ___block_literal_global.400
- ___102-[SUUIStatefulUIManager downloadAndInstall:operationDelegate:delegateCallbackQueue:completionHandler:]_block_invoke.340
- ___102-[SUUIStatefulUIManager downloadAndInstall:operationDelegate:delegateCallbackQueue:completionHandler:]_block_invoke_2.341
- ___104-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:afterPurgeConfirmation:activity:completionHandler:]_block_invoke.502
- ___104-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:afterPurgeConfirmation:activity:completionHandler:]_block_invoke.504
- ___104-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:afterPurgeConfirmation:activity:completionHandler:]_block_invoke.506
- ___108-[SUUIStatefulUIManager promoteTargetedUpdateToUserInitiatedStatus:delegateCallbackQueue:completionHandler:]_block_invoke.388
- ___108-[SUUIStatefulUIManager promoteTargetedUpdateToUserInitiatedStatus:delegateCallbackQueue:completionHandler:]_block_invoke_2.389
- ___109-[SUUIStatefulUIManager downloadAndScheduleUpdate:operationDelegate:delegateCallbackQueue:completionHandler:]_block_invoke.351
- ___109-[SUUIStatefulUIManager downloadAndScheduleUpdate:operationDelegate:delegateCallbackQueue:completionHandler:]_block_invoke_2.352
- ___111-[SUUIStatefulUIManager unscheduleTargetedUpdateAutomaticInstallation:delegateCallbackQueue:completionHandler:]_block_invoke.399
- ___111-[SUUIStatefulUIManager unscheduleTargetedUpdateAutomaticInstallation:delegateCallbackQueue:completionHandler:]_block_invoke_2.400
- ___165-[SUUIStatefulUIManager performUpdateOnDownloadByApplyingSelector:context:description:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:]_block_invoke.481
- ___165-[SUUIStatefulUIManager performUpdateOnDownloadByApplyingSelector:context:description:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:]_block_invoke.483
- ___165-[SUUIStatefulUIManager performUpdateOnDownloadByApplyingSelector:context:description:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:]_block_invoke.485
- ___189-[SUUIStatefulUIManager performUpdateWithDescriptor:byApplyingSelector:context:description:auxiliaryOperation:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:]_block_invoke.469
- ___189-[SUUIStatefulUIManager performUpdateWithDescriptor:byApplyingSelector:context:description:auxiliaryOperation:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:]_block_invoke.471
- ___189-[SUUIStatefulUIManager performUpdateWithDescriptor:byApplyingSelector:context:description:auxiliaryOperation:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:]_block_invoke.476
- ___189-[SUUIStatefulUIManager performUpdateWithDescriptor:byApplyingSelector:context:description:auxiliaryOperation:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:]_block_invoke.477
- ___189-[SUUIStatefulUIManager performUpdateWithDescriptor:byApplyingSelector:context:description:auxiliaryOperation:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:]_block_invoke.478
- ___41-[SUUIStatefulUIManager performFullScan:]_block_invoke.459
- ___41-[SUUIStatefulUIManager performFullScan:]_block_invoke.460
- ___44-[SUUIStatefulUIManager performRefreshScan:]_block_invoke.464
- ___46-[SUUIStatefulUIManager handleFailedFullScan:]_block_invoke.467
- ___47-[SUUIStatefulUIManager handleFullScanResults:]_block_invoke.466
- ___59-[SUUIStatefulUIManager refreshStateWithCompletion:forced:]_block_invoke.317
- ___63-[SUUIStatefulUIManager unenrollFromBetaUpdatesWithCompletion:]_block_invoke.418
- ___63-[SUUIStatefulUIManager unenrollFromBetaUpdatesWithCompletion:]_block_invoke.419
- ___63-[SUUIStatefulUIManager unenrollFromBetaUpdatesWithCompletion:]_block_invoke.423
- ___63-[SUUIStatefulUIManager unenrollFromBetaUpdatesWithCompletion:]_block_invoke.424
- ___63-[SUUIStatefulUIManager unenrollFromBetaUpdatesWithCompletion:]_block_invoke.431
- ___63-[SUUIStatefulUIManager unenrollFromBetaUpdatesWithCompletion:]_block_invoke.432
- ___63-[SUUIStatefulUIManager unenrollFromBetaUpdatesWithCompletion:]_block_invoke_2.425
- ___63-[SUUIStatefulUIManager unenrollFromBetaUpdatesWithCompletion:]_block_invoke_2.427
- ___69-[SUUIStatefulUIManager performFullScanWithScanResults:andScanError:]_block_invoke.462
- ___69-[SUUIStatefulUIManager performFullScanWithScanResults:andScanError:]_block_invoke.463
- ___70-[SUUIStatefulUIManager enrollInBetaUpdatesProgram:completionHandler:]_block_invoke.406
- ___70-[SUUIStatefulUIManager enrollInBetaUpdatesProgram:completionHandler:]_block_invoke.410
- ___70-[SUUIStatefulUIManager enrollInBetaUpdatesProgram:completionHandler:]_block_invoke.412
- ___75-[SUUIStatefulUIManager refreshBetaUpdates:withRecheckForAvailableUpdates:]_block_invoke.434
- ___75-[SUUIStatefulUIManager refreshBetaUpdates:withRecheckForAvailableUpdates:]_block_invoke.436
- ___75-[SUUIStatefulUIManager refreshBetaUpdates:withRecheckForAvailableUpdates:]_block_invoke.438
- ___75-[SUUIStatefulUIManager refreshBetaUpdates:withRecheckForAvailableUpdates:]_block_invoke.442
- ___75-[SUUIStatefulUIManager refreshBetaUpdates:withRecheckForAvailableUpdates:]_block_invoke_2.443
- ___77-[SUUIStatefulUIManager checkForAvailableUpdatesWithForcedReload:completion:]_block_invoke.314
- ___80-[SUUIStatefulUIManager checkForUpdatesInBackgroundWithForcedReload:completion:]_block_invoke.322
- ___81-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:activity:completionHandler:]_block_invoke.490
- ___81-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:activity:completionHandler:]_block_invoke.492
- ___81-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:activity:completionHandler:]_block_invoke.494
- ___81-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:activity:completionHandler:]_block_invoke.499
- ___81-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:activity:completionHandler:]_block_invoke.500
- ___81-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:activity:completionHandler:]_block_invoke_2.496
- ___95-[SUUIStatefulUIManager performPostUpdateOperationRefreshWithDownload:error:completionHandler:]_block_invoke.487
- ___97-[SUUIStatefulUIManager installUpdate:operationDelegate:delegateCallbackQueue:completionHandler:]_block_invoke.362
- ___97-[SUUIStatefulUIManager installUpdate:operationDelegate:delegateCallbackQueue:completionHandler:]_block_invoke_2.365
- ___98-[SUUIStatefulUIManager downloadUpdate:operationDelegate:delegateCallbackQueue:completionHandler:]_block_invoke.327
- ___98-[SUUIStatefulUIManager downloadUpdate:operationDelegate:delegateCallbackQueue:completionHandler:]_block_invoke_2.330
- ___98-[SUUIStatefulUIManager scheduleUpdate:operationDelegate:delegateCallbackQueue:completionHandler:]_block_invoke.375
- ___98-[SUUIStatefulUIManager scheduleUpdate:operationDelegate:delegateCallbackQueue:completionHandler:]_block_invoke_2.378
- ___block_literal_global.339
- ___block_literal_global.349
- ___block_literal_global.360
- ___block_literal_global.373
- ___block_literal_global.386
- ___block_literal_global.397
CStrings:
+ "specific"

```
