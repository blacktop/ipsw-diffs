## SoftwareUpdateUIFoundation

> `/System/Library/PrivateFrameworks/SoftwareUpdateUIFoundation.framework/SoftwareUpdateUIFoundation`

```diff

-508.62.1.0.0
+508.80.78.0.0
   __TEXT.__text: 0x8312c
   __TEXT.__auth_stubs: 0xa90
   __TEXT.__objc_methlist: 0x194c
-  __TEXT.__cstring: 0x51a5
+  __TEXT.__cstring: 0x5135
   __TEXT.__gcc_except_tab: 0x60a4
   __TEXT.__oslogstring: 0x95e4
   __TEXT.__const: 0xecc

   __TEXT.__objc_methtype: 0x92c
   __TEXT.__objc_stubs: 0x2ec0
   __DATA_CONST.__got: 0x2f0
-  __DATA_CONST.__const: 0x1b90
+  __DATA_CONST.__const: 0x1b30
   __DATA_CONST.__objc_classlist: 0x150
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x40

   __DATA_CONST.__objc_superrefs: 0xd8
   __AUTH_CONST.__auth_got: 0x558
   __AUTH_CONST.__const: 0x630
-  __AUTH_CONST.__cfstring: 0x3220
+  __AUTH_CONST.__cfstring: 0x31c0
   __AUTH_CONST.__objc_const: 0x4c40
   __AUTH.__objc_data: 0xd20
   __AUTH.__data: 0x128

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: BE3EA0B3-3CA1-3652-A272-E8770F272466
+  UUID: D291117A-7DD8-3D10-8DA8-E7FFD6BCA3F5
   Functions: 1159
-  Symbols:   3260
-  CStrings:  2007
+  Symbols:   3248
+  CStrings:  2001
 
Symbols:
+ ___100-[SUUIStatefulUIManager doUnenrollFromBetaUpdatesAfterPurgeConfirmation:activity:completionHandler:]_block_invoke.501
+ ___100-[SUUIStatefulUIManager doUnenrollFromBetaUpdatesAfterPurgeConfirmation:activity:completionHandler:]_block_invoke.503
+ ___100-[SUUIStatefulUIManager doUnenrollFromBetaUpdatesAfterPurgeConfirmation:activity:completionHandler:]_block_invoke.504
+ ___100-[SUUIStatefulUIManager doUnenrollFromBetaUpdatesAfterPurgeConfirmation:activity:completionHandler:]_block_invoke.505
+ ___102-[SUUIStatefulUIManager downloadAndInstall:operationDelegate:delegateCallbackQueue:completionHandler:]_block_invoke.340
+ ___102-[SUUIStatefulUIManager downloadAndInstall:operationDelegate:delegateCallbackQueue:completionHandler:]_block_invoke_2.341
+ ___104-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:afterPurgeConfirmation:activity:completionHandler:]_block_invoke.484
+ ___104-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:afterPurgeConfirmation:activity:completionHandler:]_block_invoke.486
+ ___104-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:afterPurgeConfirmation:activity:completionHandler:]_block_invoke.487
+ ___104-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:afterPurgeConfirmation:activity:completionHandler:]_block_invoke.488
+ ___108-[SUUIStatefulUIManager promoteTargetedUpdateToUserInitiatedStatus:delegateCallbackQueue:completionHandler:]_block_invoke.376
+ ___108-[SUUIStatefulUIManager promoteTargetedUpdateToUserInitiatedStatus:delegateCallbackQueue:completionHandler:]_block_invoke_2.377
+ ___109-[SUUIStatefulUIManager downloadAndScheduleUpdate:operationDelegate:delegateCallbackQueue:completionHandler:]_block_invoke.348
+ ___109-[SUUIStatefulUIManager downloadAndScheduleUpdate:operationDelegate:delegateCallbackQueue:completionHandler:]_block_invoke_2.349
+ ___111-[SUUIStatefulUIManager unscheduleTargetedUpdateAutomaticInstallation:delegateCallbackQueue:completionHandler:]_block_invoke.387
+ ___111-[SUUIStatefulUIManager unscheduleTargetedUpdateAutomaticInstallation:delegateCallbackQueue:completionHandler:]_block_invoke_2.388
+ ___165-[SUUIStatefulUIManager performUpdateOnDownloadByApplyingSelector:context:description:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:]_block_invoke.462
+ ___165-[SUUIStatefulUIManager performUpdateOnDownloadByApplyingSelector:context:description:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:]_block_invoke.464
+ ___165-[SUUIStatefulUIManager performUpdateOnDownloadByApplyingSelector:context:description:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:]_block_invoke.465
+ ___165-[SUUIStatefulUIManager performUpdateOnDownloadByApplyingSelector:context:description:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:]_block_invoke.466
+ ___165-[SUUIStatefulUIManager performUpdateOnDownloadByApplyingSelector:context:description:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:]_block_invoke.467
+ ___187-[SUUIStatefulUIManager performUpdateOperation:withDescriptor:byApplyingSelector:context:auxiliaryOperation:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:]_block_invoke.450
+ ___187-[SUUIStatefulUIManager performUpdateOperation:withDescriptor:byApplyingSelector:context:auxiliaryOperation:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:]_block_invoke.452
+ ___187-[SUUIStatefulUIManager performUpdateOperation:withDescriptor:byApplyingSelector:context:auxiliaryOperation:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:]_block_invoke.453
+ ___187-[SUUIStatefulUIManager performUpdateOperation:withDescriptor:byApplyingSelector:context:auxiliaryOperation:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:]_block_invoke.457
+ ___187-[SUUIStatefulUIManager performUpdateOperation:withDescriptor:byApplyingSelector:context:auxiliaryOperation:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:]_block_invoke.458
+ ___187-[SUUIStatefulUIManager performUpdateOperation:withDescriptor:byApplyingSelector:context:auxiliaryOperation:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:]_block_invoke.460
+ ___41-[SUUIStatefulUIManager performFullScan:]_block_invoke.435
+ ___41-[SUUIStatefulUIManager performFullScan:]_block_invoke.437
+ ___41-[SUUIStatefulUIManager performFullScan:]_block_invoke.441
+ ___44-[SUUIStatefulUIManager performRefreshScan:]_block_invoke.445
+ ___46-[SUUIStatefulUIManager handleFailedFullScan:]_block_invoke.448
+ ___47-[SUUIStatefulUIManager handleFullScanResults:]_block_invoke.447
+ ___59-[SUUIStatefulUIManager refreshStateWithCompletion:forced:]_block_invoke.320
+ ___63-[SUUIStatefulUIManager unenrollFromBetaUpdatesWithCompletion:]_block_invoke.403
+ ___63-[SUUIStatefulUIManager unenrollFromBetaUpdatesWithCompletion:]_block_invoke.404
+ ___63-[SUUIStatefulUIManager unenrollFromBetaUpdatesWithCompletion:]_block_invoke.406
+ ___63-[SUUIStatefulUIManager unenrollFromBetaUpdatesWithCompletion:]_block_invoke.408
+ ___63-[SUUIStatefulUIManager unenrollFromBetaUpdatesWithCompletion:]_block_invoke_2.407
+ ___69-[SUUIStatefulUIManager doUnenrollFromBetaUpdates:completionHandler:]_block_invoke.490
+ ___69-[SUUIStatefulUIManager doUnenrollFromBetaUpdates:completionHandler:]_block_invoke.492
+ ___69-[SUUIStatefulUIManager doUnenrollFromBetaUpdates:completionHandler:]_block_invoke.493
+ ___69-[SUUIStatefulUIManager doUnenrollFromBetaUpdates:completionHandler:]_block_invoke.494
+ ___69-[SUUIStatefulUIManager doUnenrollFromBetaUpdates:completionHandler:]_block_invoke.495
+ ___69-[SUUIStatefulUIManager doUnenrollFromBetaUpdates:completionHandler:]_block_invoke.500
+ ___69-[SUUIStatefulUIManager doUnenrollFromBetaUpdates:completionHandler:]_block_invoke_2.496
+ ___69-[SUUIStatefulUIManager performFullScanWithScanResults:andScanError:]_block_invoke.443
+ ___69-[SUUIStatefulUIManager performFullScanWithScanResults:andScanError:]_block_invoke.444
+ ___70-[SUUIStatefulUIManager enrollInBetaUpdatesProgram:completionHandler:]_block_invoke.391
+ ___70-[SUUIStatefulUIManager enrollInBetaUpdatesProgram:completionHandler:]_block_invoke.395
+ ___70-[SUUIStatefulUIManager enrollInBetaUpdatesProgram:completionHandler:]_block_invoke.397
+ ___70-[SUUIStatefulUIManager enrollInBetaUpdatesProgram:completionHandler:]_block_invoke.398
+ ___75-[SUUIStatefulUIManager refreshBetaUpdates:withRecheckForAvailableUpdates:]_block_invoke.409
+ ___75-[SUUIStatefulUIManager refreshBetaUpdates:withRecheckForAvailableUpdates:]_block_invoke.412
+ ___75-[SUUIStatefulUIManager refreshBetaUpdates:withRecheckForAvailableUpdates:]_block_invoke.413
+ ___75-[SUUIStatefulUIManager refreshBetaUpdates:withRecheckForAvailableUpdates:]_block_invoke.414
+ ___75-[SUUIStatefulUIManager refreshBetaUpdates:withRecheckForAvailableUpdates:]_block_invoke.417
+ ___75-[SUUIStatefulUIManager refreshBetaUpdates:withRecheckForAvailableUpdates:]_block_invoke_2.419
+ ___77-[SUUIStatefulUIManager checkForAvailableUpdatesWithForcedReload:completion:]_block_invoke.317
+ ___80-[SUUIStatefulUIManager checkForUpdatesInBackgroundWithForcedReload:completion:]_block_invoke.325
+ ___81-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:activity:completionHandler:]_block_invoke.471
+ ___81-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:activity:completionHandler:]_block_invoke.473
+ ___81-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:activity:completionHandler:]_block_invoke.474
+ ___81-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:activity:completionHandler:]_block_invoke.475
+ ___81-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:activity:completionHandler:]_block_invoke.476
+ ___81-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:activity:completionHandler:]_block_invoke.481
+ ___81-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:activity:completionHandler:]_block_invoke_2.477
+ ___95-[SUUIStatefulUIManager performPostUpdateOperationRefreshWithDownload:error:completionHandler:]_block_invoke.468
+ ___97-[SUUIStatefulUIManager installUpdate:operationDelegate:delegateCallbackQueue:completionHandler:]_block_invoke.356
+ ___97-[SUUIStatefulUIManager installUpdate:operationDelegate:delegateCallbackQueue:completionHandler:]_block_invoke_2.359
+ ___98-[SUUIStatefulUIManager downloadUpdate:operationDelegate:delegateCallbackQueue:completionHandler:]_block_invoke.330
+ ___98-[SUUIStatefulUIManager downloadUpdate:operationDelegate:delegateCallbackQueue:completionHandler:]_block_invoke_2.333
+ ___98-[SUUIStatefulUIManager scheduleUpdate:operationDelegate:delegateCallbackQueue:completionHandler:]_block_invoke.366
+ ___98-[SUUIStatefulUIManager scheduleUpdate:operationDelegate:delegateCallbackQueue:completionHandler:]_block_invoke_2.369
+ ___block_literal_global.339
+ ___block_literal_global.346
+ ___block_literal_global.354
+ ___block_literal_global.364
+ ___block_literal_global.374
+ ___block_literal_global.385
+ ___block_literal_global.439
- _INTERNAL_PALLAS_SERVER_URL_V2_AUTH
- _MA_PALLAS_AUDIENCE_CUSTOMER_SEASHIP
- _MA_PALLAS_AUDIENCE_INTERNAL_SEASHIP
- ___100-[SUUIStatefulUIManager doUnenrollFromBetaUpdatesAfterPurgeConfirmation:activity:completionHandler:]_block_invoke.510
- ___100-[SUUIStatefulUIManager doUnenrollFromBetaUpdatesAfterPurgeConfirmation:activity:completionHandler:]_block_invoke.512
- ___100-[SUUIStatefulUIManager doUnenrollFromBetaUpdatesAfterPurgeConfirmation:activity:completionHandler:]_block_invoke.513
- ___100-[SUUIStatefulUIManager doUnenrollFromBetaUpdatesAfterPurgeConfirmation:activity:completionHandler:]_block_invoke.514
- ___102-[SUUIStatefulUIManager downloadAndInstall:operationDelegate:delegateCallbackQueue:completionHandler:]_block_invoke.349
- ___102-[SUUIStatefulUIManager downloadAndInstall:operationDelegate:delegateCallbackQueue:completionHandler:]_block_invoke_2.350
- ___104-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:afterPurgeConfirmation:activity:completionHandler:]_block_invoke.493
- ___104-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:afterPurgeConfirmation:activity:completionHandler:]_block_invoke.495
- ___104-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:afterPurgeConfirmation:activity:completionHandler:]_block_invoke.496
- ___104-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:afterPurgeConfirmation:activity:completionHandler:]_block_invoke.497
- ___108-[SUUIStatefulUIManager promoteTargetedUpdateToUserInitiatedStatus:delegateCallbackQueue:completionHandler:]_block_invoke.385
- ___108-[SUUIStatefulUIManager promoteTargetedUpdateToUserInitiatedStatus:delegateCallbackQueue:completionHandler:]_block_invoke_2.386
- ___109-[SUUIStatefulUIManager downloadAndScheduleUpdate:operationDelegate:delegateCallbackQueue:completionHandler:]_block_invoke.357
- ___109-[SUUIStatefulUIManager downloadAndScheduleUpdate:operationDelegate:delegateCallbackQueue:completionHandler:]_block_invoke_2.358
- ___111-[SUUIStatefulUIManager unscheduleTargetedUpdateAutomaticInstallation:delegateCallbackQueue:completionHandler:]_block_invoke.396
- ___111-[SUUIStatefulUIManager unscheduleTargetedUpdateAutomaticInstallation:delegateCallbackQueue:completionHandler:]_block_invoke_2.397
- ___165-[SUUIStatefulUIManager performUpdateOnDownloadByApplyingSelector:context:description:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:]_block_invoke.471
- ___165-[SUUIStatefulUIManager performUpdateOnDownloadByApplyingSelector:context:description:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:]_block_invoke.473
- ___165-[SUUIStatefulUIManager performUpdateOnDownloadByApplyingSelector:context:description:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:]_block_invoke.474
- ___165-[SUUIStatefulUIManager performUpdateOnDownloadByApplyingSelector:context:description:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:]_block_invoke.475
- ___165-[SUUIStatefulUIManager performUpdateOnDownloadByApplyingSelector:context:description:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:]_block_invoke.476
- ___187-[SUUIStatefulUIManager performUpdateOperation:withDescriptor:byApplyingSelector:context:auxiliaryOperation:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:]_block_invoke.461
- ___187-[SUUIStatefulUIManager performUpdateOperation:withDescriptor:byApplyingSelector:context:auxiliaryOperation:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:]_block_invoke.462
- ___187-[SUUIStatefulUIManager performUpdateOperation:withDescriptor:byApplyingSelector:context:auxiliaryOperation:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:]_block_invoke.466
- ___187-[SUUIStatefulUIManager performUpdateOperation:withDescriptor:byApplyingSelector:context:auxiliaryOperation:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:]_block_invoke.467
- ___187-[SUUIStatefulUIManager performUpdateOperation:withDescriptor:byApplyingSelector:context:auxiliaryOperation:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:]_block_invoke.468
- ___187-[SUUIStatefulUIManager performUpdateOperation:withDescriptor:byApplyingSelector:context:auxiliaryOperation:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:]_block_invoke.469
- ___41-[SUUIStatefulUIManager performFullScan:]_block_invoke.444
- ___41-[SUUIStatefulUIManager performFullScan:]_block_invoke.446
- ___41-[SUUIStatefulUIManager performFullScan:]_block_invoke.450
- ___44-[SUUIStatefulUIManager performRefreshScan:]_block_invoke.454
- ___46-[SUUIStatefulUIManager handleFailedFullScan:]_block_invoke.457
- ___47-[SUUIStatefulUIManager handleFullScanResults:]_block_invoke.456
- ___59-[SUUIStatefulUIManager refreshStateWithCompletion:forced:]_block_invoke.329
- ___63-[SUUIStatefulUIManager unenrollFromBetaUpdatesWithCompletion:]_block_invoke.412
- ___63-[SUUIStatefulUIManager unenrollFromBetaUpdatesWithCompletion:]_block_invoke.413
- ___63-[SUUIStatefulUIManager unenrollFromBetaUpdatesWithCompletion:]_block_invoke.415
- ___63-[SUUIStatefulUIManager unenrollFromBetaUpdatesWithCompletion:]_block_invoke.417
- ___63-[SUUIStatefulUIManager unenrollFromBetaUpdatesWithCompletion:]_block_invoke_2.416
- ___69-[SUUIStatefulUIManager doUnenrollFromBetaUpdates:completionHandler:]_block_invoke.501
- ___69-[SUUIStatefulUIManager doUnenrollFromBetaUpdates:completionHandler:]_block_invoke.502
- ___69-[SUUIStatefulUIManager doUnenrollFromBetaUpdates:completionHandler:]_block_invoke.503
- ___69-[SUUIStatefulUIManager doUnenrollFromBetaUpdates:completionHandler:]_block_invoke.504
- ___69-[SUUIStatefulUIManager doUnenrollFromBetaUpdates:completionHandler:]_block_invoke.508
- ___69-[SUUIStatefulUIManager doUnenrollFromBetaUpdates:completionHandler:]_block_invoke.509
- ___69-[SUUIStatefulUIManager doUnenrollFromBetaUpdates:completionHandler:]_block_invoke_2.505
- ___69-[SUUIStatefulUIManager performFullScanWithScanResults:andScanError:]_block_invoke.452
- ___69-[SUUIStatefulUIManager performFullScanWithScanResults:andScanError:]_block_invoke.453
- ___70-[SUUIStatefulUIManager enrollInBetaUpdatesProgram:completionHandler:]_block_invoke.404
- ___70-[SUUIStatefulUIManager enrollInBetaUpdatesProgram:completionHandler:]_block_invoke.406
- ___70-[SUUIStatefulUIManager enrollInBetaUpdatesProgram:completionHandler:]_block_invoke.407
- ___70-[SUUIStatefulUIManager enrollInBetaUpdatesProgram:completionHandler:]_block_invoke.409
- ___75-[SUUIStatefulUIManager refreshBetaUpdates:withRecheckForAvailableUpdates:]_block_invoke.421
- ___75-[SUUIStatefulUIManager refreshBetaUpdates:withRecheckForAvailableUpdates:]_block_invoke.422
- ___75-[SUUIStatefulUIManager refreshBetaUpdates:withRecheckForAvailableUpdates:]_block_invoke.423
- ___75-[SUUIStatefulUIManager refreshBetaUpdates:withRecheckForAvailableUpdates:]_block_invoke.426
- ___75-[SUUIStatefulUIManager refreshBetaUpdates:withRecheckForAvailableUpdates:]_block_invoke.427
- ___75-[SUUIStatefulUIManager refreshBetaUpdates:withRecheckForAvailableUpdates:]_block_invoke_2.428
- ___77-[SUUIStatefulUIManager checkForAvailableUpdatesWithForcedReload:completion:]_block_invoke.326
- ___80-[SUUIStatefulUIManager checkForUpdatesInBackgroundWithForcedReload:completion:]_block_invoke.334
- ___81-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:activity:completionHandler:]_block_invoke.480
- ___81-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:activity:completionHandler:]_block_invoke.483
- ___81-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:activity:completionHandler:]_block_invoke.484
- ___81-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:activity:completionHandler:]_block_invoke.485
- ___81-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:activity:completionHandler:]_block_invoke.490
- ___81-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:activity:completionHandler:]_block_invoke.491
- ___81-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:activity:completionHandler:]_block_invoke_2.486
- ___95-[SUUIStatefulUIManager performPostUpdateOperationRefreshWithDownload:error:completionHandler:]_block_invoke.477
- ___97-[SUUIStatefulUIManager installUpdate:operationDelegate:delegateCallbackQueue:completionHandler:]_block_invoke.365
- ___97-[SUUIStatefulUIManager installUpdate:operationDelegate:delegateCallbackQueue:completionHandler:]_block_invoke_2.368
- ___98-[SUUIStatefulUIManager downloadUpdate:operationDelegate:delegateCallbackQueue:completionHandler:]_block_invoke.339
- ___98-[SUUIStatefulUIManager downloadUpdate:operationDelegate:delegateCallbackQueue:completionHandler:]_block_invoke_2.342
- ___98-[SUUIStatefulUIManager scheduleUpdate:operationDelegate:delegateCallbackQueue:completionHandler:]_block_invoke.375
- ___98-[SUUIStatefulUIManager scheduleUpdate:operationDelegate:delegateCallbackQueue:completionHandler:]_block_invoke_2.378
- ___block_literal_global.348
- ___block_literal_global.355
- ___block_literal_global.363
- ___block_literal_global.373
- ___block_literal_global.383
- ___block_literal_global.394
- ___block_literal_global.448
CStrings:
- "cd060049-2465-43e3-bbb5-d769a66da2d7"
- "ffc25f86-b83c-4139-b8ad-91131d0e5429"
- "https://gdmf-auth-stg.apple.com/v2/assets"

```
