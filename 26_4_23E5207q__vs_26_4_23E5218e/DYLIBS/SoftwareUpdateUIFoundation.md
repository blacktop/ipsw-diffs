## SoftwareUpdateUIFoundation

> `/System/Library/PrivateFrameworks/SoftwareUpdateUIFoundation.framework/SoftwareUpdateUIFoundation`

```diff

-508.100.172.0.0
-  __TEXT.__text: 0xa4f54
+508.100.173.0.0
+  __TEXT.__text: 0xa4dc0
   __TEXT.__auth_stubs: 0x1130
-  __TEXT.__objc_methlist: 0x1d94
-  __TEXT.__cstring: 0x5c18
-  __TEXT.__gcc_except_tab: 0x5744
-  __TEXT.__oslogstring: 0x9ac7
+  __TEXT.__objc_methlist: 0x1da4
+  __TEXT.__cstring: 0x5d58
+  __TEXT.__gcc_except_tab: 0x5750
+  __TEXT.__oslogstring: 0x9b07
   __TEXT.__const: 0x1d40
   __TEXT.__swift5_typeref: 0x6e3
   __TEXT.__swift5_reflstr: 0x47e

   __TEXT.__unwind_info: 0xfb8
   __TEXT.__eh_frame: 0x9b0
   __TEXT.__objc_classname: 0x670
-  __TEXT.__objc_methname: 0x5ee8
+  __TEXT.__objc_methname: 0x5ef5
   __TEXT.__objc_methtype: 0x1210
-  __TEXT.__objc_stubs: 0x32e0
+  __TEXT.__objc_stubs: 0x3280
   __DATA_CONST.__got: 0x3f8
-  __DATA_CONST.__const: 0x1ec0
+  __DATA_CONST.__const: 0x2058
   __DATA_CONST.__objc_classlist: 0x160
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1268
+  __DATA_CONST.__objc_selrefs: 0x1270
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0xe0
   __AUTH_CONST.__auth_got: 0x8a8
   __AUTH_CONST.__const: 0x1430
-  __AUTH_CONST.__cfstring: 0x3600
+  __AUTH_CONST.__cfstring: 0x37a0
   __AUTH_CONST.__objc_const: 0x5af0
   __AUTH_CONST.__objc_intobj: 0xc0
   __AUTH.__objc_data: 0xdc0

   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
+  - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 6AE19483-105E-32F8-8FC4-C8D5458E4285
-  Functions: 1761
-  Symbols:   3729
-  CStrings:  2275
+  UUID: C1091A9E-E0B3-3966-BAD5-94AED3085E75
+  Functions: 1762
+  Symbols:   3780
+  CStrings:  2303
 
Symbols:
+ -[SUUIUserDefaults userDefaults]
+ _MABrainLoadErrorDomain
+ _MA_FORCE_MOBILEASSETBRAIN_UPDATE_KEY
+ _MA_PALLAS_AUDIENCE_INTERNAL_UNTESTED
+ _MA_PALLAS_AUDIENCE_NAME_CUSTOMER
+ _MA_PALLAS_AUDIENCE_NAME_EXTERNAL_PRE_RELEASE
+ _MA_PALLAS_AUDIENCE_NAME_LIVABLE
+ _MA_PALLAS_AUDIENCE_NAME_SEED_STAGING
+ _MA_PALLAS_AUDIENCE_NAME_UNTESTED
+ _MA_PALLAS_AUDIENCE_RELEASE_ALIGNED_CUSTOMER
+ _MA_PALLAS_AUDIENCE_RELEASE_ALIGNED_EXT_PRERELEASE
+ _MA_PALLAS_AUDIENCE_RELEASE_ALIGNED_LIVABLE
+ _MA_PALLAS_AUDIENCE_RELEASE_ALIGNED_SEED_STAGING
+ _MA_PALLAS_AUDIENCE_RELEASE_ALIGNED_UNTESTED
+ ___100-[SUUIStatefulUIManager doUnenrollFromBetaUpdatesAfterPurgeConfirmation:activity:completionHandler:]_block_invoke.544
+ ___100-[SUUIStatefulUIManager doUnenrollFromBetaUpdatesAfterPurgeConfirmation:activity:completionHandler:]_block_invoke.546
+ ___100-[SUUIStatefulUIManager doUnenrollFromBetaUpdatesAfterPurgeConfirmation:activity:completionHandler:]_block_invoke.547
+ ___100-[SUUIStatefulUIManager doUnenrollFromBetaUpdatesAfterPurgeConfirmation:activity:completionHandler:]_block_invoke.548
+ ___102-[SUUIStatefulUIManager downloadAndInstall:operationDelegate:delegateCallbackQueue:completionHandler:]_block_invoke.388
+ ___102-[SUUIStatefulUIManager downloadAndInstall:operationDelegate:delegateCallbackQueue:completionHandler:]_block_invoke_2.389
+ ___104-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:afterPurgeConfirmation:activity:completionHandler:]_block_invoke.527
+ ___104-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:afterPurgeConfirmation:activity:completionHandler:]_block_invoke.529
+ ___104-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:afterPurgeConfirmation:activity:completionHandler:]_block_invoke.530
+ ___104-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:afterPurgeConfirmation:activity:completionHandler:]_block_invoke.531
+ ___108-[SUUIStatefulUIManager promoteTargetedUpdateToUserInitiatedStatus:delegateCallbackQueue:completionHandler:]_block_invoke.421
+ ___109-[SUUIStatefulUIManager downloadAndScheduleUpdate:operationDelegate:delegateCallbackQueue:completionHandler:]_block_invoke.396
+ ___109-[SUUIStatefulUIManager downloadAndScheduleUpdate:operationDelegate:delegateCallbackQueue:completionHandler:]_block_invoke_2.397
+ ___111-[SUUIStatefulUIManager unscheduleTargetedUpdateAutomaticInstallation:delegateCallbackQueue:completionHandler:]_block_invoke.431
+ ___165-[SUUIStatefulUIManager performUpdateOnDownloadByApplyingSelector:context:description:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:]_block_invoke.505
+ ___165-[SUUIStatefulUIManager performUpdateOnDownloadByApplyingSelector:context:description:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:]_block_invoke.507
+ ___165-[SUUIStatefulUIManager performUpdateOnDownloadByApplyingSelector:context:description:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:]_block_invoke.508
+ ___165-[SUUIStatefulUIManager performUpdateOnDownloadByApplyingSelector:context:description:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:]_block_invoke.509
+ ___165-[SUUIStatefulUIManager performUpdateOnDownloadByApplyingSelector:context:description:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:]_block_invoke.510
+ ___187-[SUUIStatefulUIManager performUpdateOperation:withDescriptor:byApplyingSelector:context:auxiliaryOperation:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:]_block_invoke.493
+ ___187-[SUUIStatefulUIManager performUpdateOperation:withDescriptor:byApplyingSelector:context:auxiliaryOperation:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:]_block_invoke.495
+ ___187-[SUUIStatefulUIManager performUpdateOperation:withDescriptor:byApplyingSelector:context:auxiliaryOperation:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:]_block_invoke.496
+ ___187-[SUUIStatefulUIManager performUpdateOperation:withDescriptor:byApplyingSelector:context:auxiliaryOperation:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:]_block_invoke.500
+ ___187-[SUUIStatefulUIManager performUpdateOperation:withDescriptor:byApplyingSelector:context:auxiliaryOperation:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:]_block_invoke.501
+ ___187-[SUUIStatefulUIManager performUpdateOperation:withDescriptor:byApplyingSelector:context:auxiliaryOperation:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:]_block_invoke.502
+ ___187-[SUUIStatefulUIManager performUpdateOperation:withDescriptor:byApplyingSelector:context:auxiliaryOperation:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:]_block_invoke.503
+ ___41+[SUUIUserDefaults defaultsForSuiteName:]_block_invoke.8
+ ___41-[SUUIStatefulUIManager performFullScan:]_block_invoke.479
+ ___41-[SUUIStatefulUIManager performFullScan:]_block_invoke.481
+ ___41-[SUUIStatefulUIManager performFullScan:]_block_invoke.485
+ ___44-[SUUIStatefulUIManager performRefreshScan:]_block_invoke.489
+ ___46-[SUUIStatefulUIManager handleFailedFullScan:]_block_invoke.491
+ ___59-[SUUIStatefulUIManager refreshStateWithCompletion:forced:]_block_invoke.368
+ ___63-[SUUIStatefulUIManager unenrollFromBetaUpdatesWithCompletion:]_block_invoke.446
+ ___63-[SUUIStatefulUIManager unenrollFromBetaUpdatesWithCompletion:]_block_invoke.448
+ ___63-[SUUIStatefulUIManager unenrollFromBetaUpdatesWithCompletion:]_block_invoke.450
+ ___63-[SUUIStatefulUIManager unenrollFromBetaUpdatesWithCompletion:]_block_invoke.452
+ ___63-[SUUIStatefulUIManager unenrollFromBetaUpdatesWithCompletion:]_block_invoke_2.451
+ ___64-[SUUIStatefulUIManager notifyDelegateOfStateRefreshWithReason:]_block_invoke.566
+ ___69-[SUUIStatefulUIManager doUnenrollFromBetaUpdates:completionHandler:]_block_invoke.533
+ ___69-[SUUIStatefulUIManager doUnenrollFromBetaUpdates:completionHandler:]_block_invoke.535
+ ___69-[SUUIStatefulUIManager doUnenrollFromBetaUpdates:completionHandler:]_block_invoke.536
+ ___69-[SUUIStatefulUIManager doUnenrollFromBetaUpdates:completionHandler:]_block_invoke.537
+ ___69-[SUUIStatefulUIManager doUnenrollFromBetaUpdates:completionHandler:]_block_invoke.538
+ ___69-[SUUIStatefulUIManager doUnenrollFromBetaUpdates:completionHandler:]_block_invoke.542
+ ___69-[SUUIStatefulUIManager doUnenrollFromBetaUpdates:completionHandler:]_block_invoke.543
+ ___69-[SUUIStatefulUIManager doUnenrollFromBetaUpdates:completionHandler:]_block_invoke_2.539
+ ___69-[SUUIStatefulUIManager performFullScanWithScanResults:andScanError:]_block_invoke.487
+ ___69-[SUUIStatefulUIManager performFullScanWithScanResults:andScanError:]_block_invoke.488
+ ___70-[SUUIStatefulUIManager enrollInBetaUpdatesProgram:completionHandler:]_block_invoke.434
+ ___70-[SUUIStatefulUIManager enrollInBetaUpdatesProgram:completionHandler:]_block_invoke.439
+ ___70-[SUUIStatefulUIManager enrollInBetaUpdatesProgram:completionHandler:]_block_invoke.440
+ ___70-[SUUIStatefulUIManager enrollInBetaUpdatesProgram:completionHandler:]_block_invoke.441
+ ___70-[SUUIStatefulUIManager enrollInBetaUpdatesProgram:completionHandler:]_block_invoke.443
+ ___75-[SUUIStatefulUIManager refreshBetaUpdates:withRecheckForAvailableUpdates:]_block_invoke.453
+ ___75-[SUUIStatefulUIManager refreshBetaUpdates:withRecheckForAvailableUpdates:]_block_invoke.456
+ ___75-[SUUIStatefulUIManager refreshBetaUpdates:withRecheckForAvailableUpdates:]_block_invoke.457
+ ___75-[SUUIStatefulUIManager refreshBetaUpdates:withRecheckForAvailableUpdates:]_block_invoke.458
+ ___75-[SUUIStatefulUIManager refreshBetaUpdates:withRecheckForAvailableUpdates:]_block_invoke.461
+ ___75-[SUUIStatefulUIManager refreshBetaUpdates:withRecheckForAvailableUpdates:]_block_invoke.462
+ ___75-[SUUIStatefulUIManager refreshBetaUpdates:withRecheckForAvailableUpdates:]_block_invoke_2.463
+ ___77-[SUUIStatefulUIManager checkForAvailableUpdatesWithForcedReload:completion:]_block_invoke.365
+ ___80-[SUUIStatefulUIManager checkForUpdatesInBackgroundWithForcedReload:completion:]_block_invoke.373
+ ___81-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:activity:completionHandler:]_block_invoke.514
+ ___81-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:activity:completionHandler:]_block_invoke.516
+ ___81-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:activity:completionHandler:]_block_invoke.517
+ ___81-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:activity:completionHandler:]_block_invoke.518
+ ___81-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:activity:completionHandler:]_block_invoke.519
+ ___81-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:activity:completionHandler:]_block_invoke.524
+ ___81-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:activity:completionHandler:]_block_invoke.525
+ ___81-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:activity:completionHandler:]_block_invoke_2.520
+ ___85-[SUUIBetaUpdatesOperation checkForAvailableBetaProgramsForDevice:completionHandler:]_block_invoke.346
+ ___95-[SUUIStatefulUIManager performPostUpdateOperationRefreshWithDownload:error:completionHandler:]_block_invoke.511
+ ___97-[SUUIStatefulUIManager installUpdate:operationDelegate:delegateCallbackQueue:completionHandler:]_block_invoke.404
+ ___97-[SUUIStatefulUIManager installUpdate:operationDelegate:delegateCallbackQueue:completionHandler:]_block_invoke_2.407
+ ___98-[SUUIStatefulUIManager downloadUpdate:operationDelegate:delegateCallbackQueue:completionHandler:]_block_invoke.378
+ ___98-[SUUIStatefulUIManager downloadUpdate:operationDelegate:delegateCallbackQueue:completionHandler:]_block_invoke_2.381
+ ___98-[SUUIStatefulUIManager scheduleUpdate:operationDelegate:delegateCallbackQueue:completionHandler:]_block_invoke.414
+ ___block_literal_global.387
+ ___block_literal_global.394
+ ___block_literal_global.402
+ ___block_literal_global.412
+ ___block_literal_global.419
+ ___block_literal_global.429
+ ___block_literal_global.483
+ __swift_FORCE_LOAD_$_swiftSpatial
+ __swift_FORCE_LOAD_$_swiftSpatial_$_SoftwareUpdateUIFoundation
+ _objc_msgSend$userDefaults
+ _sharedDefaults._suui_once_t1
+ _sharedDefaults._suui_once_v2
- _MA_PALLAS_AUDIENCE_CUSTOMER_XROS
- _MA_PALLAS_AUDIENCE_CUSTOMER_XROS_ALT
- _MA_PALLAS_AUDIENCE_CUSTOMER_XROS_GENERIC
- ___100-[SUUIStatefulUIManager doUnenrollFromBetaUpdatesAfterPurgeConfirmation:activity:completionHandler:]_block_invoke.505
- ___100-[SUUIStatefulUIManager doUnenrollFromBetaUpdatesAfterPurgeConfirmation:activity:completionHandler:]_block_invoke.507
- ___100-[SUUIStatefulUIManager doUnenrollFromBetaUpdatesAfterPurgeConfirmation:activity:completionHandler:]_block_invoke.508
- ___100-[SUUIStatefulUIManager doUnenrollFromBetaUpdatesAfterPurgeConfirmation:activity:completionHandler:]_block_invoke.509
- ___102-[SUUIStatefulUIManager downloadAndInstall:operationDelegate:delegateCallbackQueue:completionHandler:]_block_invoke.349
- ___102-[SUUIStatefulUIManager downloadAndInstall:operationDelegate:delegateCallbackQueue:completionHandler:]_block_invoke_2.350
- ___104-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:afterPurgeConfirmation:activity:completionHandler:]_block_invoke.488
- ___104-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:afterPurgeConfirmation:activity:completionHandler:]_block_invoke.490
- ___104-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:afterPurgeConfirmation:activity:completionHandler:]_block_invoke.491
- ___104-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:afterPurgeConfirmation:activity:completionHandler:]_block_invoke.492
- ___108-[SUUIStatefulUIManager promoteTargetedUpdateToUserInitiatedStatus:delegateCallbackQueue:completionHandler:]_block_invoke.382
- ___109-[SUUIStatefulUIManager downloadAndScheduleUpdate:operationDelegate:delegateCallbackQueue:completionHandler:]_block_invoke.357
- ___109-[SUUIStatefulUIManager downloadAndScheduleUpdate:operationDelegate:delegateCallbackQueue:completionHandler:]_block_invoke_2.358
- ___111-[SUUIStatefulUIManager unscheduleTargetedUpdateAutomaticInstallation:delegateCallbackQueue:completionHandler:]_block_invoke.392
- ___165-[SUUIStatefulUIManager performUpdateOnDownloadByApplyingSelector:context:description:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:]_block_invoke.466
- ___165-[SUUIStatefulUIManager performUpdateOnDownloadByApplyingSelector:context:description:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:]_block_invoke.468
- ___165-[SUUIStatefulUIManager performUpdateOnDownloadByApplyingSelector:context:description:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:]_block_invoke.469
- ___165-[SUUIStatefulUIManager performUpdateOnDownloadByApplyingSelector:context:description:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:]_block_invoke.470
- ___165-[SUUIStatefulUIManager performUpdateOnDownloadByApplyingSelector:context:description:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:]_block_invoke.471
- ___187-[SUUIStatefulUIManager performUpdateOperation:withDescriptor:byApplyingSelector:context:auxiliaryOperation:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:]_block_invoke.454
- ___187-[SUUIStatefulUIManager performUpdateOperation:withDescriptor:byApplyingSelector:context:auxiliaryOperation:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:]_block_invoke.456
- ___187-[SUUIStatefulUIManager performUpdateOperation:withDescriptor:byApplyingSelector:context:auxiliaryOperation:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:]_block_invoke.457
- ___187-[SUUIStatefulUIManager performUpdateOperation:withDescriptor:byApplyingSelector:context:auxiliaryOperation:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:]_block_invoke.461
- ___187-[SUUIStatefulUIManager performUpdateOperation:withDescriptor:byApplyingSelector:context:auxiliaryOperation:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:]_block_invoke.462
- ___187-[SUUIStatefulUIManager performUpdateOperation:withDescriptor:byApplyingSelector:context:auxiliaryOperation:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:]_block_invoke.463
- ___187-[SUUIStatefulUIManager performUpdateOperation:withDescriptor:byApplyingSelector:context:auxiliaryOperation:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:]_block_invoke.464
- ___41+[SUUIUserDefaults defaultsForSuiteName:]_block_invoke.7
- ___41-[SUUIStatefulUIManager performFullScan:]_block_invoke.440
- ___41-[SUUIStatefulUIManager performFullScan:]_block_invoke.442
- ___41-[SUUIStatefulUIManager performFullScan:]_block_invoke.446
- ___44-[SUUIStatefulUIManager performRefreshScan:]_block_invoke.450
- ___46-[SUUIStatefulUIManager handleFailedFullScan:]_block_invoke.452
- ___59-[SUUIStatefulUIManager refreshStateWithCompletion:forced:]_block_invoke.329
- ___63-[SUUIStatefulUIManager unenrollFromBetaUpdatesWithCompletion:]_block_invoke.407
- ___63-[SUUIStatefulUIManager unenrollFromBetaUpdatesWithCompletion:]_block_invoke.409
- ___63-[SUUIStatefulUIManager unenrollFromBetaUpdatesWithCompletion:]_block_invoke.411
- ___63-[SUUIStatefulUIManager unenrollFromBetaUpdatesWithCompletion:]_block_invoke.413
- ___63-[SUUIStatefulUIManager unenrollFromBetaUpdatesWithCompletion:]_block_invoke_2.412
- ___64-[SUUIStatefulUIManager notifyDelegateOfStateRefreshWithReason:]_block_invoke.527
- ___69-[SUUIStatefulUIManager doUnenrollFromBetaUpdates:completionHandler:]_block_invoke.494
- ___69-[SUUIStatefulUIManager doUnenrollFromBetaUpdates:completionHandler:]_block_invoke.496
- ___69-[SUUIStatefulUIManager doUnenrollFromBetaUpdates:completionHandler:]_block_invoke.497
- ___69-[SUUIStatefulUIManager doUnenrollFromBetaUpdates:completionHandler:]_block_invoke.498
- ___69-[SUUIStatefulUIManager doUnenrollFromBetaUpdates:completionHandler:]_block_invoke.499
- ___69-[SUUIStatefulUIManager doUnenrollFromBetaUpdates:completionHandler:]_block_invoke.503
- ___69-[SUUIStatefulUIManager doUnenrollFromBetaUpdates:completionHandler:]_block_invoke.504
- ___69-[SUUIStatefulUIManager doUnenrollFromBetaUpdates:completionHandler:]_block_invoke_2.500
- ___69-[SUUIStatefulUIManager performFullScanWithScanResults:andScanError:]_block_invoke.448
- ___69-[SUUIStatefulUIManager performFullScanWithScanResults:andScanError:]_block_invoke.449
- ___70-[SUUIStatefulUIManager enrollInBetaUpdatesProgram:completionHandler:]_block_invoke.395
- ___70-[SUUIStatefulUIManager enrollInBetaUpdatesProgram:completionHandler:]_block_invoke.400
- ___70-[SUUIStatefulUIManager enrollInBetaUpdatesProgram:completionHandler:]_block_invoke.401
- ___70-[SUUIStatefulUIManager enrollInBetaUpdatesProgram:completionHandler:]_block_invoke.402
- ___70-[SUUIStatefulUIManager enrollInBetaUpdatesProgram:completionHandler:]_block_invoke.404
- ___75-[SUUIStatefulUIManager refreshBetaUpdates:withRecheckForAvailableUpdates:]_block_invoke.414
- ___75-[SUUIStatefulUIManager refreshBetaUpdates:withRecheckForAvailableUpdates:]_block_invoke.417
- ___75-[SUUIStatefulUIManager refreshBetaUpdates:withRecheckForAvailableUpdates:]_block_invoke.418
- ___75-[SUUIStatefulUIManager refreshBetaUpdates:withRecheckForAvailableUpdates:]_block_invoke.419
- ___75-[SUUIStatefulUIManager refreshBetaUpdates:withRecheckForAvailableUpdates:]_block_invoke.422
- ___75-[SUUIStatefulUIManager refreshBetaUpdates:withRecheckForAvailableUpdates:]_block_invoke.423
- ___75-[SUUIStatefulUIManager refreshBetaUpdates:withRecheckForAvailableUpdates:]_block_invoke_2.424
- ___77-[SUUIStatefulUIManager checkForAvailableUpdatesWithForcedReload:completion:]_block_invoke.326
- ___80-[SUUIStatefulUIManager checkForUpdatesInBackgroundWithForcedReload:completion:]_block_invoke.334
- ___81-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:activity:completionHandler:]_block_invoke.475
- ___81-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:activity:completionHandler:]_block_invoke.477
- ___81-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:activity:completionHandler:]_block_invoke.478
- ___81-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:activity:completionHandler:]_block_invoke.479
- ___81-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:activity:completionHandler:]_block_invoke.480
- ___81-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:activity:completionHandler:]_block_invoke.485
- ___81-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:activity:completionHandler:]_block_invoke.486
- ___81-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:activity:completionHandler:]_block_invoke_2.481
- ___85-[SUUIBetaUpdatesOperation checkForAvailableBetaProgramsForDevice:completionHandler:]_block_invoke.307
- ___95-[SUUIStatefulUIManager performPostUpdateOperationRefreshWithDownload:error:completionHandler:]_block_invoke.472
- ___97-[SUUIStatefulUIManager installUpdate:operationDelegate:delegateCallbackQueue:completionHandler:]_block_invoke.365
- ___97-[SUUIStatefulUIManager installUpdate:operationDelegate:delegateCallbackQueue:completionHandler:]_block_invoke_2.368
- ___98-[SUUIStatefulUIManager downloadUpdate:operationDelegate:delegateCallbackQueue:completionHandler:]_block_invoke.339
- ___98-[SUUIStatefulUIManager downloadUpdate:operationDelegate:delegateCallbackQueue:completionHandler:]_block_invoke_2.342
- ___98-[SUUIStatefulUIManager scheduleUpdate:operationDelegate:delegateCallbackQueue:completionHandler:]_block_invoke.375
- ___block_literal_global.348
- ___block_literal_global.355
- ___block_literal_global.363
- ___block_literal_global.373
- ___block_literal_global.380
- ___block_literal_global.390
- ___block_literal_global.444
- _objc_msgSend$boolForEntry:
- _objc_msgSend$setBool:forEntry:
- _objc_msgSend$setString:forEntry:
- _objc_msgSend$stringForEntry:
- _sharedDefaults._suui_once_t0
- _sharedDefaults._suui_once_v1
CStrings:
+ "245326d2-3ddb-4c46-a08e-aab8b6060a1b"
+ "85ff7a90-361b-42d1-a420-97dee860f018"
+ "97d68e5c-95bb-4136-9aa0-f08964fcc0e1"
+ "ForceMABrainUpdate"
+ "Loading the Software Update UI User Defaults entries catalog"
+ "MABrainLoadError"
+ "b1f792b1-0797-48f1-8603-107cefcf1d45"
+ "customer"
+ "ed5a1c1d-2a39-4993-8bcc-f260c4b42868"
+ "external-pre-release"
+ "fb333b76-b463-401f-8899-96d82fc4c598"
+ "livable"
+ "seed-staging"
+ "untested"
+ "userDefaults"

```
