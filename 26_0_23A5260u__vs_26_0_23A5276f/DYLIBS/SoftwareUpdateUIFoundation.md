## SoftwareUpdateUIFoundation

> `/System/Library/PrivateFrameworks/SoftwareUpdateUIFoundation.framework/SoftwareUpdateUIFoundation`

```diff

-486.0.0.0.4
-  __TEXT.__text: 0x69f98
-  __TEXT.__auth_stubs: 0x9c0
-  __TEXT.__objc_methlist: 0x172c
-  __TEXT.__cstring: 0x4b15
-  __TEXT.__gcc_except_tab: 0x2820
-  __TEXT.__oslogstring: 0x717f
+492.0.0.0.5
+  __TEXT.__text: 0x70924
+  __TEXT.__auth_stubs: 0x9e0
+  __TEXT.__objc_methlist: 0x1744
+  __TEXT.__cstring: 0x4b25
+  __TEXT.__gcc_except_tab: 0x4418
+  __TEXT.__oslogstring: 0x6a94
   __TEXT.__const: 0xe28
   __TEXT.__constg_swiftt: 0x2ea
   __TEXT.__swift5_typeref: 0x2fc

   __TEXT.__swift_as_entry: 0xc
   __TEXT.__swift_as_ret: 0x8
   __TEXT.__swift5_types2: 0x4
-  __TEXT.__unwind_info: 0xb40
-  __TEXT.__eh_frame: 0x730
-  __TEXT.__objc_classname: 0x5a3
-  __TEXT.__objc_methname: 0x4fae
-  __TEXT.__objc_methtype: 0x781
-  __TEXT.__objc_stubs: 0x2b00
+  __TEXT.__unwind_info: 0xb10
+  __TEXT.__eh_frame: 0x618
+  __TEXT.__objc_classname: 0x5a4
+  __TEXT.__objc_methname: 0x5053
+  __TEXT.__objc_methtype: 0x7f2
+  __TEXT.__objc_stubs: 0x2b60
   __DATA_CONST.__got: 0x2c8
-  __DATA_CONST.__const: 0x19a8
+  __DATA_CONST.__const: 0x1990
   __DATA_CONST.__objc_classlist: 0x148
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xf20
+  __DATA_CONST.__objc_selrefs: 0xf30
   __DATA_CONST.__objc_superrefs: 0xd0
-  __AUTH_CONST.__auth_got: 0x4f0
+  __AUTH_CONST.__auth_got: 0x500
   __AUTH_CONST.__const: 0x550
-  __AUTH_CONST.__cfstring: 0x2f80
-  __AUTH_CONST.__objc_const: 0x4378
+  __AUTH_CONST.__cfstring: 0x2fc0
+  __AUTH_CONST.__objc_const: 0x4388
   __AUTH.__objc_data: 0xcd0
   __AUTH.__data: 0x128
   __DATA.__objc_ivar: 0x1c8

   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 7BB95E55-BB5B-39E1-B5DA-A1EF367FC793
-  Functions: 1086
-  Symbols:   2992
-  CStrings:  1819
+  UUID: 15212FC4-C741-3147-9AB8-30C2BE3A1D09
+  Functions: 1082
+  Symbols:   2983
+  CStrings:  1828
 
Symbols:
+ -[SUUIStatefulUIManager refreshStateWithCompletion:forced:]
+ -[SUUIUserDefaults comingSoonTipImageSystemName:]
+ -[SUUIUserDefaults comingSoonTipImageSystemName]
+ GCC_except_table100
+ GCC_except_table103
+ GCC_except_table112
+ GCC_except_table117
+ GCC_except_table138
+ GCC_except_table143
+ GCC_except_table147
+ GCC_except_table150
+ GCC_except_table152
+ GCC_except_table154
+ GCC_except_table157
+ GCC_except_table160
+ GCC_except_table167
+ GCC_except_table172
+ GCC_except_table178
+ GCC_except_table180
+ GCC_except_table185
+ GCC_except_table195
+ GCC_except_table198
+ GCC_except_table200
+ GCC_except_table208
+ GCC_except_table217
+ GCC_except_table220
+ GCC_except_table222
+ GCC_except_table225
+ GCC_except_table227
+ GCC_except_table232
+ GCC_except_table297
+ GCC_except_table32
+ GCC_except_table36
+ GCC_except_table39
+ GCC_except_table43
+ GCC_except_table46
+ GCC_except_table50
+ GCC_except_table53
+ GCC_except_table57
+ GCC_except_table60
+ GCC_except_table64
+ GCC_except_table67
+ GCC_except_table71
+ GCC_except_table74
+ GCC_except_table78
+ GCC_except_table86
+ GCC_except_table95
+ OBJC_IVAR_$_SUUIStatefulUIManager._canEnrollInBetaUpdates
+ OBJC_IVAR_$_SUUIStatefulUIManager._clearingSpaceForDownload
+ OBJC_IVAR_$_SUUIStatefulUIManager._ddmDeclaration
+ OBJC_IVAR_$_SUUIStatefulUIManager._lock
+ OBJC_IVAR_$_SUUIStatefulUIManager._rollingBackSplatUpdate
+ ___102-[SUUIStatefulUIManager downloadAndInstall:operationDelegate:delegateCallbackQueue:completionHandler:]_block_invoke.340
+ ___102-[SUUIStatefulUIManager downloadAndInstall:operationDelegate:delegateCallbackQueue:completionHandler:]_block_invoke_2.341
+ ___108-[SUUIStatefulUIManager promoteTargetedUpdateToUserInitiatedStatus:delegateCallbackQueue:completionHandler:]_block_invoke.388
+ ___108-[SUUIStatefulUIManager promoteTargetedUpdateToUserInitiatedStatus:delegateCallbackQueue:completionHandler:]_block_invoke_2.389
+ ___109-[SUUIStatefulUIManager downloadAndScheduleUpdate:operationDelegate:delegateCallbackQueue:completionHandler:]_block_invoke.351
+ ___109-[SUUIStatefulUIManager downloadAndScheduleUpdate:operationDelegate:delegateCallbackQueue:completionHandler:]_block_invoke_2.352
+ ___111-[SUUIStatefulUIManager unscheduleTargetedUpdateAutomaticInstallation:delegateCallbackQueue:completionHandler:]_block_invoke.399
+ ___111-[SUUIStatefulUIManager unscheduleTargetedUpdateAutomaticInstallation:delegateCallbackQueue:completionHandler:]_block_invoke_2.400
+ ___165-[SUUIStatefulUIManager performUpdateOnDownloadByApplyingSelector:context:description:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:]_block_invoke.481
+ ___165-[SUUIStatefulUIManager performUpdateOnDownloadByApplyingSelector:context:description:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:]_block_invoke.483
+ ___165-[SUUIStatefulUIManager performUpdateOnDownloadByApplyingSelector:context:description:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:]_block_invoke.485
+ ___189-[SUUIStatefulUIManager performUpdateWithDescriptor:byApplyingSelector:context:description:auxiliaryOperation:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:]_block_invoke.469
+ ___189-[SUUIStatefulUIManager performUpdateWithDescriptor:byApplyingSelector:context:description:auxiliaryOperation:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:]_block_invoke.471
+ ___189-[SUUIStatefulUIManager performUpdateWithDescriptor:byApplyingSelector:context:description:auxiliaryOperation:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:]_block_invoke.476
+ ___189-[SUUIStatefulUIManager performUpdateWithDescriptor:byApplyingSelector:context:description:auxiliaryOperation:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:]_block_invoke.477
+ ___189-[SUUIStatefulUIManager performUpdateWithDescriptor:byApplyingSelector:context:description:auxiliaryOperation:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:]_block_invoke.478
+ ___41-[SUUIStatefulUIManager performFullScan:]_block_invoke.460
+ ___41-[SUUIStatefulUIManager performFullScan:]_block_invoke.461
+ ___44-[SUUIStatefulUIManager performRefreshScan:]_block_invoke.465
+ ___44-[SUUIStatefulUIManager refreshBetaUpdates:]_block_invoke.435
+ ___44-[SUUIStatefulUIManager refreshBetaUpdates:]_block_invoke.437
+ ___44-[SUUIStatefulUIManager refreshBetaUpdates:]_block_invoke.442
+ ___44-[SUUIStatefulUIManager refreshBetaUpdates:]_block_invoke.443
+ ___44-[SUUIStatefulUIManager refreshBetaUpdates:]_block_invoke_2.444
+ ___47-[SUUIStatefulUIManager handleFullScanResults:]_block_invoke.467
+ ___59-[SUUIStatefulUIManager refreshStateWithCompletion:forced:]_block_invoke
+ ___59-[SUUIStatefulUIManager refreshStateWithCompletion:forced:]_block_invoke.317
+ ___63-[SUUIStatefulUIManager unenrollFromBetaUpdatesWithCompletion:]_block_invoke.418
+ ___63-[SUUIStatefulUIManager unenrollFromBetaUpdatesWithCompletion:]_block_invoke.420
+ ___63-[SUUIStatefulUIManager unenrollFromBetaUpdatesWithCompletion:]_block_invoke.432
+ ___69-[SUUIStatefulUIManager performFullScanWithScanResults:andScanError:]_block_invoke.463
+ ___69-[SUUIStatefulUIManager performFullScanWithScanResults:andScanError:]_block_invoke.464
+ ___70-[SUUIStatefulUIManager enrollInBetaUpdatesProgram:completionHandler:]_block_invoke.406
+ ___70-[SUUIStatefulUIManager enrollInBetaUpdatesProgram:completionHandler:]_block_invoke.413
+ ___70-[SUUIStatefulUIManager enrollInBetaUpdatesProgram:completionHandler:]_block_invoke.415
+ ___72-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:completionHandler:]_block_invoke.490
+ ___72-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:completionHandler:]_block_invoke.492
+ ___72-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:completionHandler:]_block_invoke.494
+ ___72-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:completionHandler:]_block_invoke.499
+ ___72-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:completionHandler:]_block_invoke.500
+ ___72-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:completionHandler:]_block_invoke_2.496
+ ___80-[SUUIStatefulUIManager checkForUpdatesInBackgroundWithForcedReload:completion:]_block_invoke.322
+ ___95-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:afterPurgeConfirmation:completionHandler:]_block_invoke.502
+ ___95-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:afterPurgeConfirmation:completionHandler:]_block_invoke.504
+ ___95-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:afterPurgeConfirmation:completionHandler:]_block_invoke.506
+ ___95-[SUUIStatefulUIManager performPostUpdateOperationRefreshWithDownload:error:completionHandler:]_block_invoke.487
+ ___97-[SUUIStatefulUIManager installUpdate:operationDelegate:delegateCallbackQueue:completionHandler:]_block_invoke.362
+ ___97-[SUUIStatefulUIManager installUpdate:operationDelegate:delegateCallbackQueue:completionHandler:]_block_invoke_2.365
+ ___98-[SUUIStatefulUIManager downloadUpdate:operationDelegate:delegateCallbackQueue:completionHandler:]_block_invoke.327
+ ___98-[SUUIStatefulUIManager downloadUpdate:operationDelegate:delegateCallbackQueue:completionHandler:]_block_invoke_2.330
+ ___98-[SUUIStatefulUIManager scheduleUpdate:operationDelegate:delegateCallbackQueue:completionHandler:]_block_invoke.375
+ ___98-[SUUIStatefulUIManager scheduleUpdate:operationDelegate:delegateCallbackQueue:completionHandler:]_block_invoke_2.378
+ ___block_descriptor_48_e8_32w_e64_v24?0"SUUIScanOperationFullScanResults"8"SUUIStatefulError"16lw32l8
+ ___block_descriptor_88_e8_32s40s48bs56bs64w72w_e5_v8?0lw64l8s48l8w72l8s32l8s40l8s56l8
+ ___block_literal_global.339
+ ___block_literal_global.349
+ ___block_literal_global.360
+ ___block_literal_global.373
+ ___block_literal_global.386
+ ___block_literal_global.397
+ ___os_log_helper_16_2_24_8_32_8_0_8_66_8_66_8_0_8_66_8_0_8_66_8_66_8_66_8_66_8_0_8_66_8_66_8_66_8_66_8_66_8_0_8_0_8_66_8_0_8_0_8_0_8_0
+ ___os_log_helper_16_2_25_8_32_8_0_8_66_8_66_8_0_8_66_8_0_8_66_8_66_8_66_8_66_8_0_8_66_8_66_8_66_8_66_8_66_8_0_8_0_8_66_8_0_8_0_8_0_8_0_4_0
+ ___os_log_helper_16_2_25_8_32_8_0_8_66_8_66_8_0_8_66_8_0_8_66_8_66_8_66_8_66_8_0_8_66_8_66_8_66_8_66_8_66_8_0_8_0_8_66_8_0_8_0_8_0_8_0_8_66
+ ___os_log_helper_16_2_26_8_32_8_0_8_66_8_66_8_0_8_66_8_0_8_66_8_66_8_66_8_66_8_0_8_66_8_66_8_66_8_66_8_66_8_0_8_0_8_66_8_0_8_0_8_0_8_0_8_0_8_0
+ ___os_log_helper_16_2_26_8_32_8_0_8_66_8_66_8_0_8_66_8_0_8_66_8_66_8_66_8_66_8_0_8_66_8_66_8_66_8_66_8_66_8_0_8_0_8_66_8_0_8_0_8_0_8_0_8_64_8_0
+ ___os_log_helper_16_2_26_8_32_8_0_8_66_8_66_8_0_8_66_8_0_8_66_8_66_8_66_8_66_8_0_8_66_8_66_8_66_8_66_8_66_8_0_8_0_8_66_8_0_8_0_8_0_8_0_8_66_8_66
+ ___os_log_helper_16_2_27_8_32_8_0_8_66_8_66_8_0_8_66_8_0_8_66_8_66_8_66_8_66_8_0_8_66_8_66_8_66_8_66_8_66_8_0_8_0_8_66_8_0_8_0_8_0_8_0_8_0_8_0_8_66
+ ___os_log_helper_16_2_27_8_32_8_0_8_66_8_66_8_0_8_66_8_0_8_66_8_66_8_66_8_66_8_0_8_66_8_66_8_66_8_66_8_66_8_0_8_0_8_66_8_0_8_0_8_0_8_0_8_66_8_0_8_0
+ ___os_log_helper_16_2_27_8_32_8_0_8_66_8_66_8_0_8_66_8_0_8_66_8_66_8_66_8_66_8_0_8_66_8_66_8_66_8_66_8_66_8_0_8_0_8_66_8_0_8_0_8_0_8_0_8_66_8_66_8_66
+ ___os_log_helper_16_2_28_8_32_8_0_8_66_8_66_8_0_8_66_8_0_8_66_8_66_8_66_8_66_8_0_8_66_8_66_8_66_8_66_8_66_8_0_8_0_8_66_8_0_8_0_8_0_8_0_8_66_8_0_8_0_8_66
+ ___os_log_helper_16_2_28_8_32_8_0_8_66_8_66_8_0_8_66_8_0_8_66_8_66_8_66_8_66_8_0_8_66_8_66_8_66_8_66_8_66_8_0_8_0_8_66_8_0_8_0_8_0_8_0_8_66_8_0_8_66_8_0
+ ___os_log_helper_16_2_28_8_32_8_0_8_66_8_66_8_0_8_66_8_0_8_66_8_66_8_66_8_66_8_0_8_66_8_66_8_66_8_66_8_66_8_0_8_0_8_66_8_0_8_0_8_0_8_0_8_66_8_66_8_66_8_66
+ ___os_log_helper_16_2_29_8_32_8_0_8_66_8_66_8_0_8_66_8_0_8_66_8_66_8_66_8_66_8_0_8_66_8_66_8_66_8_66_8_66_8_0_8_0_8_66_8_0_8_0_8_0_8_0_8_0_8_66_8_66_8_0_8_0
+ ___os_log_helper_16_2_9_8_32_8_0_8_66_8_66_8_0_8_66_8_0_8_66_8_66
+ _kSUUIUserDefaultsComingSoonTipImageSystemName
+ _kSU_E_FullScanFailed
+ _kSU_E_FullScanNoUpdateAvailable
+ _kSU_E_FullScanUpdatesAvailable
+ _kSU_E_RefreshNoUpdateAvailable
+ _kSU_E_RefreshUpdatesAvailable
+ _objc_msgSend$currentFullScanOperation
+ _objc_msgSend$currentRefreshScanOperation
+ _objc_msgSend$environment
+ _objc_msgSend$hiddenAlternateStatefulDescriptor
+ _objc_msgSend$hiddenPreferredStatefulDescriptor
+ _objc_msgSend$refreshStateWithCompletion:forced:
+ _objc_setProperty_atomic
+ _os_unfair_recursive_lock_lock_with_options
- -[SUUIStatefulUIManager fsmAction_ThirdPartyScanDuringRefresh:error:]
- GCC_except_table102
- GCC_except_table105
- GCC_except_table113
- GCC_except_table118
- GCC_except_table139
- GCC_except_table144
- GCC_except_table148
- GCC_except_table151
- GCC_except_table153
- GCC_except_table155
- GCC_except_table158
- GCC_except_table161
- GCC_except_table168
- GCC_except_table173
- GCC_except_table179
- GCC_except_table181
- GCC_except_table186
- GCC_except_table196
- GCC_except_table199
- GCC_except_table202
- GCC_except_table209
- GCC_except_table218
- GCC_except_table221
- GCC_except_table223
- GCC_except_table226
- GCC_except_table228
- GCC_except_table230
- GCC_except_table303
- GCC_except_table31
- GCC_except_table35
- GCC_except_table38
- GCC_except_table42
- GCC_except_table45
- GCC_except_table49
- GCC_except_table52
- GCC_except_table56
- GCC_except_table59
- GCC_except_table63
- GCC_except_table66
- GCC_except_table70
- GCC_except_table73
- GCC_except_table77
- GCC_except_table94
- OBJC_IVAR_$_SUUIStatefulUIManager._performThirdPartyScan
- _OBJC_IVAR_$_SUUIStatefulUIManager._canEnrollInBetaUpdates
- _OBJC_IVAR_$_SUUIStatefulUIManager._clearingSpaceForDownload
- _OBJC_IVAR_$_SUUIStatefulUIManager._ddmDeclaration
- _OBJC_IVAR_$_SUUIStatefulUIManager._rollingBackSplatUpdate
- ___102-[SUUIStatefulUIManager downloadAndInstall:operationDelegate:delegateCallbackQueue:completionHandler:]_block_invoke.339
- ___102-[SUUIStatefulUIManager downloadAndInstall:operationDelegate:delegateCallbackQueue:completionHandler:]_block_invoke_2.340
- ___108-[SUUIStatefulUIManager promoteTargetedUpdateToUserInitiatedStatus:delegateCallbackQueue:completionHandler:]_block_invoke.387
- ___108-[SUUIStatefulUIManager promoteTargetedUpdateToUserInitiatedStatus:delegateCallbackQueue:completionHandler:]_block_invoke_2.388
- ___109-[SUUIStatefulUIManager downloadAndScheduleUpdate:operationDelegate:delegateCallbackQueue:completionHandler:]_block_invoke.350
- ___109-[SUUIStatefulUIManager downloadAndScheduleUpdate:operationDelegate:delegateCallbackQueue:completionHandler:]_block_invoke_2.351
- ___111-[SUUIStatefulUIManager unscheduleTargetedUpdateAutomaticInstallation:delegateCallbackQueue:completionHandler:]_block_invoke.398
- ___111-[SUUIStatefulUIManager unscheduleTargetedUpdateAutomaticInstallation:delegateCallbackQueue:completionHandler:]_block_invoke_2.399
- ___165-[SUUIStatefulUIManager performUpdateOnDownloadByApplyingSelector:context:description:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:]_block_invoke.487
- ___165-[SUUIStatefulUIManager performUpdateOnDownloadByApplyingSelector:context:description:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:]_block_invoke.488
- ___165-[SUUIStatefulUIManager performUpdateOnDownloadByApplyingSelector:context:description:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:]_block_invoke.489
- ___189-[SUUIStatefulUIManager performUpdateWithDescriptor:byApplyingSelector:context:description:auxiliaryOperation:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:]_block_invoke.474
- ___189-[SUUIStatefulUIManager performUpdateWithDescriptor:byApplyingSelector:context:description:auxiliaryOperation:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:]_block_invoke.475
- ___189-[SUUIStatefulUIManager performUpdateWithDescriptor:byApplyingSelector:context:description:auxiliaryOperation:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:]_block_invoke.480
- ___189-[SUUIStatefulUIManager performUpdateWithDescriptor:byApplyingSelector:context:description:auxiliaryOperation:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:]_block_invoke.481
- ___189-[SUUIStatefulUIManager performUpdateWithDescriptor:byApplyingSelector:context:description:auxiliaryOperation:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:]_block_invoke.482
- ___38-[SUUIStatefulUIManager refreshState:]_block_invoke
- ___41-[SUUIStatefulUIManager performFullScan:]_block_invoke.463
- ___41-[SUUIStatefulUIManager performFullScan:]_block_invoke.464
- ___44-[SUUIStatefulUIManager performRefreshScan:]_block_invoke.468
- ___44-[SUUIStatefulUIManager refreshBetaUpdates:]_block_invoke.436
- ___44-[SUUIStatefulUIManager refreshBetaUpdates:]_block_invoke.440
- ___44-[SUUIStatefulUIManager refreshBetaUpdates:]_block_invoke.445
- ___44-[SUUIStatefulUIManager refreshBetaUpdates:]_block_invoke.446
- ___44-[SUUIStatefulUIManager refreshBetaUpdates:]_block_invoke_2.447
- ___47-[SUUIStatefulUIManager handleFullScanResults:]_block_invoke.470
- ___52-[SUUIStatefulUIManager refreshStateWithCompletion:]_block_invoke
- ___52-[SUUIStatefulUIManager refreshStateWithCompletion:]_block_invoke.317
- ___63-[SUUIStatefulUIManager unenrollFromBetaUpdatesWithCompletion:]_block_invoke.417
- ___63-[SUUIStatefulUIManager unenrollFromBetaUpdatesWithCompletion:]_block_invoke.419
- ___63-[SUUIStatefulUIManager unenrollFromBetaUpdatesWithCompletion:]_block_invoke.422
- ___63-[SUUIStatefulUIManager unenrollFromBetaUpdatesWithCompletion:]_block_invoke.434
- ___63-[SUUIStatefulUIManager unenrollFromBetaUpdatesWithCompletion:]_block_invoke_3.431
- ___69-[SUUIStatefulUIManager fsmAction_ThirdPartyScanDuringRefresh:error:]_block_invoke
- ___69-[SUUIStatefulUIManager performFullScanWithScanResults:andScanError:]_block_invoke.466
- ___69-[SUUIStatefulUIManager performFullScanWithScanResults:andScanError:]_block_invoke.467
- ___70-[SUUIStatefulUIManager enrollInBetaUpdatesProgram:completionHandler:]_block_invoke.405
- ___70-[SUUIStatefulUIManager enrollInBetaUpdatesProgram:completionHandler:]_block_invoke.410
- ___70-[SUUIStatefulUIManager enrollInBetaUpdatesProgram:completionHandler:]_block_invoke.414
- ___72-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:completionHandler:]_block_invoke.496
- ___72-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:completionHandler:]_block_invoke.497
- ___72-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:completionHandler:]_block_invoke.498
- ___72-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:completionHandler:]_block_invoke.502
- ___72-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:completionHandler:]_block_invoke.503
- ___72-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:completionHandler:]_block_invoke_2.499
- ___80-[SUUIStatefulUIManager checkForUpdatesInBackgroundWithForcedReload:completion:]_block_invoke.321
- ___95-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:afterPurgeConfirmation:completionHandler:]_block_invoke.507
- ___95-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:afterPurgeConfirmation:completionHandler:]_block_invoke.508
- ___95-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:afterPurgeConfirmation:completionHandler:]_block_invoke.509
- ___95-[SUUIStatefulUIManager performPostUpdateOperationRefreshWithDownload:error:completionHandler:]_block_invoke.490
- ___97-[SUUIStatefulUIManager installUpdate:operationDelegate:delegateCallbackQueue:completionHandler:]_block_invoke.361
- ___97-[SUUIStatefulUIManager installUpdate:operationDelegate:delegateCallbackQueue:completionHandler:]_block_invoke_2.364
- ___98-[SUUIStatefulUIManager downloadUpdate:operationDelegate:delegateCallbackQueue:completionHandler:]_block_invoke.326
- ___98-[SUUIStatefulUIManager downloadUpdate:operationDelegate:delegateCallbackQueue:completionHandler:]_block_invoke_2.329
- ___98-[SUUIStatefulUIManager scheduleUpdate:operationDelegate:delegateCallbackQueue:completionHandler:]_block_invoke.374
- ___98-[SUUIStatefulUIManager scheduleUpdate:operationDelegate:delegateCallbackQueue:completionHandler:]_block_invoke_2.377
- ___block_descriptor_40_e8_32s_e64_v24?0"SUUIScanOperationFullScanResults"8"SUUIStatefulError"16ls32l8
- ___block_descriptor_72_e8_32s40bs48bs56w_e5_v8?0lw56l8s40l8s32l8s48l8
- ___block_literal_global.338
- ___block_literal_global.348
- ___block_literal_global.359
- ___block_literal_global.372
- ___block_literal_global.385
- ___block_literal_global.396
- ___os_log_helper_16_2_25_8_32_8_0_8_66_8_66_8_0_8_66_8_0_8_66_8_66_8_66_8_66_8_0_8_66_8_66_8_66_8_66_8_66_8_66_8_0_8_0_8_66_8_0_8_0_8_0_8_0
- ___os_log_helper_16_2_26_8_32_8_0_8_66_8_66_8_0_8_66_8_0_8_66_8_66_8_66_8_66_8_0_8_66_8_66_8_66_8_66_8_66_8_66_8_0_8_0_8_66_8_0_8_0_8_0_8_0_4_0
- ___os_log_helper_16_2_26_8_32_8_0_8_66_8_66_8_0_8_66_8_0_8_66_8_66_8_66_8_66_8_0_8_66_8_66_8_66_8_66_8_66_8_66_8_0_8_0_8_66_8_0_8_0_8_0_8_0_8_66
- ___os_log_helper_16_2_27_8_32_8_0_8_66_8_66_8_0_8_66_8_0_8_66_8_66_8_66_8_66_8_0_8_66_8_66_8_66_8_66_8_66_8_66_8_0_8_0_8_66_8_0_8_0_8_0_8_0_8_0_8_0
- ___os_log_helper_16_2_27_8_32_8_0_8_66_8_66_8_0_8_66_8_0_8_66_8_66_8_66_8_66_8_0_8_66_8_66_8_66_8_66_8_66_8_66_8_0_8_0_8_66_8_0_8_0_8_0_8_0_8_64_8_0
- ___os_log_helper_16_2_27_8_32_8_0_8_66_8_66_8_0_8_66_8_0_8_66_8_66_8_66_8_66_8_0_8_66_8_66_8_66_8_66_8_66_8_66_8_0_8_0_8_66_8_0_8_0_8_0_8_0_8_66_8_2
- ___os_log_helper_16_2_27_8_32_8_0_8_66_8_66_8_0_8_66_8_0_8_66_8_66_8_66_8_66_8_0_8_66_8_66_8_66_8_66_8_66_8_66_8_0_8_0_8_66_8_0_8_0_8_0_8_0_8_66_8_66
- ___os_log_helper_16_2_28_8_32_8_0_8_66_8_66_8_0_8_66_8_0_8_66_8_66_8_66_8_66_8_0_8_66_8_66_8_66_8_66_8_66_8_66_8_0_8_0_8_66_8_0_8_0_8_0_8_0_8_0_8_0_8_66
- ___os_log_helper_16_2_28_8_32_8_0_8_66_8_66_8_0_8_66_8_0_8_66_8_66_8_66_8_66_8_0_8_66_8_66_8_66_8_66_8_66_8_66_8_0_8_0_8_66_8_0_8_0_8_0_8_0_8_66_8_0_8_0
- ___os_log_helper_16_2_28_8_32_8_0_8_66_8_66_8_0_8_66_8_0_8_66_8_66_8_66_8_66_8_0_8_66_8_66_8_66_8_66_8_66_8_66_8_0_8_0_8_66_8_0_8_0_8_0_8_0_8_66_8_66_8_66
- ___os_log_helper_16_2_29_8_32_8_0_8_66_8_66_8_0_8_66_8_0_8_66_8_66_8_66_8_66_8_0_8_66_8_66_8_66_8_66_8_66_8_66_8_0_8_0_8_66_8_0_8_0_8_0_8_0_8_66_8_0_8_0_8_66
- ___os_log_helper_16_2_29_8_32_8_0_8_66_8_66_8_0_8_66_8_0_8_66_8_66_8_66_8_66_8_0_8_66_8_66_8_66_8_66_8_66_8_66_8_0_8_0_8_66_8_0_8_0_8_0_8_0_8_66_8_0_8_66_8_0
- ___os_log_helper_16_2_29_8_32_8_0_8_66_8_66_8_0_8_66_8_0_8_66_8_66_8_66_8_66_8_0_8_66_8_66_8_66_8_66_8_66_8_66_8_0_8_0_8_66_8_0_8_0_8_0_8_0_8_66_8_66_8_34_8_66
- ___os_log_helper_16_2_30_8_32_8_0_8_66_8_66_8_0_8_66_8_0_8_66_8_66_8_66_8_66_8_0_8_66_8_66_8_66_8_66_8_66_8_66_8_0_8_0_8_66_8_0_8_0_8_0_8_0_8_0_8_66_8_66_8_0_8_0
- ___os_log_helper_16_2_3_8_32_8_0_8_32
- ___os_log_helper_16_2_9_8_32_8_0_8_66_8_66_8_0_8_66_8_0_8_32_8_32
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swiftDarwin_$_SoftwareUpdateUIFoundation
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_SoftwareUpdateUIFoundation
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_SoftwareUpdateUIFoundation
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_SoftwareUpdateUIFoundation
- _kSU_A_ThirdPartyScanDuringRefresh
- _kSU_E_PerformThirdPartyScan
- _kSU_E_PerformUpdateOperation
- _kSU_E_RefreshScanResultsSuccess
- _kSU_S_PerformingThirdPartyScan
- _objc_msgSend$fsmAction_ThirdPartyScanDuringRefresh:error:
- _objc_msgSend$refreshState
- _objc_msgSend$refreshState:
CStrings:
+ "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\n"
+ "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nA full scan operation is already running. Skipping on this refresh request. This should never happen."
+ "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nA full scan operation is already running. Skipping on this refresh requestwithout transitioning to the RefreshingScanResults state."
+ "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nA full-scan operation is already running. Skipping on this full-scan request."
+ "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nA full-scan request has been received for third-party scan results. We got a non up-to-date third-party scan error - Skipping.\nscanError: %{public}@\nscanResults: %{public}@"
+ "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nA refresh operation is already running. Skipping on this refresh request without transitioning to the RefreshingScanResults state."
+ "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nA refresh operation is already running. Skipping on this refresh request. This should never happen."
+ "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nA refresh operation is currently running. Canceling it as we start a full-scan."
+ "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nA targeted update exists when attempting to enroll in beta program: %ld (%p). Asking to purge the targeted update."
+ "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nAttempts to enroll in beta program: %ld (%p) using Beta Updates operation ID: %{public}@"
+ "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nAttempts to unenroll from Beta Updates program using operation ID: %{public}@"
+ "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nBeginning a NeRD Info operation with ID: %{public}@ "
+ "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nBeginning a beta updates scan operation with operation ID: %{public}@ (full scan FSM: %p, refresh scan FSM: %p)"
+ "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nBeginning a full scan operation with scan ID: %{public}@ (full scan FSM: %p, refresh scan FSM: %p)"
+ "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nBeginning a full scan operation with with existing scan results (results: %p, error: %{public}@), using scan ID: %{public}@ (full scan FSM: %p, refresh scan FSM: %p)"
+ "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nBeginning a post download refresh operation with scan ID: %{public}@"
+ "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nBeginning to refresh the current scan results with scan ID: %{public}@ (full scan FSM: %p, refresh scan FSM: %p)"
+ "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nCan not enroll in beta updates as we have not discovered a seeding device."
+ "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nCan not register to the beta progra \"%ld\" (%p) as no beta programs have been discovered by the Stateful UI. Attempts to perform a full re-scan."
+ "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nCan not unenroll from beta updates as we have not discovered a seeding device."
+ "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nFinished to enroll in beta program: %ld (%p); error: %{public}@"
+ "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nFinished to perform a beta updates scan with ID: %{public}@.\nError: %{public}@;\nEnrolled to a different beta program: %{public}@\nResults: %{public}@"
+ "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nFinished to perform a full-scan with ID: %{public}@.\nResults: %{public}@"
+ "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nFinished to perform a full-scan with error: %{public}@"
+ "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nFinished to perform the post-update refresh for update operation \"%{public}@\", using update operation identifier: %{public}@"
+ "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nFinished to perform the update operation \"%{public}@\" using operation identifier: %{public}@"
+ "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nFinished to refresh the current scan results with ID: %{public}@.\nResults: %{public}@"
+ "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nPost update request refresh operation completed successfully: %{public}@ with error: %{public}@; scan results: %{public}@"
+ "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nPurge result: %{public}@; error: %{public}@"
+ "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nReporting on available updates:\n\tPreferred update: %{public}@ (%p)\n\tAlternate update: %{public}@ (%p)"
+ "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nStarting to perform the update operation \"%{public}@\" into: %{public}@, using operation identifier: %{public}@"
+ "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nStarting to perform the update operation \"%{public}@\" on download: %{public}@, using operation identifier: %{public}@"
+ "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nThe Stateful UI delegate doesn't implement the purge confirmation dialog.Approving without user consent. This is not recommended."
+ "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nThe descriptors states and errors are identical to the previous values (refreshHasAnyChanges = YES). Dropping the refresh request."
+ "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nThe descriptors states and errors are identical to the previous values (refreshHasAnyChanges = YES). Force load was requested - proceeding to ask the delegate to reload the UI."
+ "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nThe full scan yielded empty scan results - cancelling the currently active update operation"
+ "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nThe full scan yielded results that are different than the previously discovered results - cancelling the currently active update operation.\n\tresults.preferredDescriptor: %{public}@\n\tresults.alternateDescriptor: %{public}@"
+ "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nThe given descriptor role, %@ (%ld), is invalid."
+ "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nThere is already an update operation running. Ignoring update request \"%{public}@\", into: %{public}@"
+ "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nUn-enroll from beta program success: %d"
+ "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nUser responded to the targeted update purge request of %{public}@, for beta program %ld (%p): %{public}@"
+ "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nisScanning: %{public}@; error: %{public}@"
+ "%s [%p]: %{public}@ descriptor assignment: Replacing the current descriptor with a new descriptor.\n\tCurrent: %{public}@ (%p)\n\tNew: %{public}@ (%p)\n\tHiding: Preferred - %{public}@; Alternate: %{public}@"
+ "%s [%p]: %{public}@ descriptor assignment: the given descriptor is equal to the current stateful descriptor. Updating internal state instead of creation of an entirely new one.\n\tCurrent: %{public}@ (%p)\n\tNew: %{public}@ (%p)\n\tHiding: Preferred - %{public}@; Alternate: %{public}@"
+ "%s [%p]: canEnrollInBetaUpdates status changed to: %{public}@"
+ "-[SUUIStatefulUIManager refreshStateWithCompletion:forced:]_block_invoke"
+ "-[SUUIStatefulUIManager refreshStateWithCompletion:forced:]_block_invoke_2"
+ "FullScanFailed"
+ "FullScanNoUpdateAvailable"
+ "FullScanUpdatesAvailable"
+ "RefreshNoUpdateAvailable"
+ "RefreshUpdatesAvailable"
+ "SUComingSoonTipImageSystemName"
+ "T@\"<SUUIDownload>\",&"
+ "T@\"<SUUIScanOperation>\",&,V_currentFullScanOperation"
+ "T@\"<SUUIScanOperation>\",&,V_currentRefreshScanOperation"
+ "T@\"<SUUIStatefulUIEnvironment>\",W,V_environment"
+ "T@\"<SUUIStatefulUIManagerDelegate>\",W,V_delegate"
+ "T@\"<SUUIUpdateOperation>\",&,V_currentUpdateOperation"
+ "T@\"NSArray\",&,V_betaPrograms"
+ "T@\"NSObject<OS_dispatch_queue>\",&,V_delegateCallbackQueue"
+ "T@\"NSString\",&,N,ScomingSoonTipImageSystemName:"
+ "T@\"SDBetaProgram\",&,V_enrolledBetaProgram"
+ "T@\"SUCoreDDMDeclaration\",&,SsetDDMDeclaration:,V_ddmDeclaration"
+ "T@\"SUUIStatefulDescriptor\",&,V_alternateStatefulDescriptor"
+ "T@\"SUUIStatefulDescriptor\",&,V_hiddenAlternateStatefulDescriptor"
+ "T@\"SUUIStatefulDescriptor\",&,V_hiddenPreferredStatefulDescriptor"
+ "T@\"SUUIStatefulDescriptor\",&,V_preferredStatefulDescriptor"
+ "T@\"SUUIStatefulError\",&,V_scanError"
+ "TB,GisClearingSpaceForDownload,V_clearingSpaceForDownload"
+ "TB,R,GisRollingBackSplatUpdate,V_rollingBackSplatUpdate"
+ "TB,V_hidingAlternateDescriptor"
+ "TB,V_hidingPreferredDescriptor"
+ "TB,V_isAutoUpdateScheduled"
+ "TQ,V_mdmPathRestrictions"
+ "The image system name for the \"Coming Soon\" tip. This field will override the value returned by Constellation."
+ "Tq,V_currentState"
+ "comingSoonTipImageSystemName"
+ "comingSoonTipImageSystemName:"
+ "refreshStateWithCompletion:forced:"
+ "v28@0:8@?16B24"
+ "{os_unfair_recursive_lock_s=\"ourl_lock\"{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}\"ourl_count\"I}"
- "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tthirdPartyScan: %{public}@\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\n"
- "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tthirdPartyScan: %{public}@\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nA full scan operation is already running. Skipping on this refresh request. This should never happen."
- "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tthirdPartyScan: %{public}@\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nA full scan operation is already running. Skipping on this refresh requestwithout transitioning to the RefreshingScanResults state."
- "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tthirdPartyScan: %{public}@\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nA full-scan operation is already running. Skipping on this full-scan request."
- "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tthirdPartyScan: %{public}@\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nA full-scan request has been received for third-party scan results. We got a non up-to-date third-party scan error - Skipping.\nscanError: %{public}@\nscanResults: %{public}@"
- "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tthirdPartyScan: %{public}@\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nA refresh operation is already running. Skipping on this refresh request without transitioning to the RefreshingScanResults state."
- "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tthirdPartyScan: %{public}@\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nA refresh operation is already running. Skipping on this refresh request. This should never happen."
- "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tthirdPartyScan: %{public}@\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nA refresh operation is currently running. Canceling it as we start a full-scan."
- "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tthirdPartyScan: %{public}@\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nA targeted update exists when attempting to enroll in beta program: %ld (%p). Asking to purge the targeted update."
- "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tthirdPartyScan: %{public}@\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nAttempts to enroll in beta program: %ld (%p) using Beta Updates operation ID: %{public}@"
- "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tthirdPartyScan: %{public}@\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nAttempts to unenroll from Beta Updates program using operation ID: %{public}@"
- "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tthirdPartyScan: %{public}@\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nBeginning a NeRD Info operation with ID: %{public}@ "
- "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tthirdPartyScan: %{public}@\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nBeginning a beta updates scan operation with operation ID: %{public}@ (full scan FSM: %p, refresh scan FSM: %p)"
- "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tthirdPartyScan: %{public}@\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nBeginning a full scan operation with scan ID: %{public}@ (full scan FSM: %p, refresh scan FSM: %p)"
- "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tthirdPartyScan: %{public}@\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nBeginning a full scan operation with with existing scan results (results: %p, error: %{public}@), usoing scan ID: %{public}@ (full scan FSM: %p, refresh scan FSM: %p)"
- "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tthirdPartyScan: %{public}@\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nBeginning a post download refresh operation with scan ID: %{public}@"
- "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tthirdPartyScan: %{public}@\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nBeginning to refresh the current scan results with scan ID: %{public}@ (full scan FSM: %p, refresh scan FSM: %p)"
- "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tthirdPartyScan: %{public}@\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nCan not enroll in beta updates as we have not discovered a seeding device."
- "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tthirdPartyScan: %{public}@\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nCan not register to the beta progra \"%ld\" (%p) as no beta programs have been discovered by the Stateful UI. Attempts to perform a full re-scan."
- "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tthirdPartyScan: %{public}@\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nCan not unenroll from beta updates as we have not discovered a seeding device."
- "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tthirdPartyScan: %{public}@\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nCancelling a refresh request as a third-party scan has been initiated.\nRefresh scan UUID: %{public}@; Refresh Scan: %{public}p"
- "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tthirdPartyScan: %{public}@\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nFinished to enroll in beta program: %ld (%p); error: %{public}@"
- "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tthirdPartyScan: %{public}@\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nFinished to perform a beta updates scan with ID: %{public}@.\nError: %{public}@;\nEnrolled to a different beta program: %{public}s\nResults: %{public}@"
- "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tthirdPartyScan: %{public}@\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nFinished to perform a full-scan with ID: %{public}@.\nResults: %{public}@"
- "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tthirdPartyScan: %{public}@\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nFinished to perform a full-scan with error: %{public}@"
- "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tthirdPartyScan: %{public}@\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nFinished to perform the post-update refresh for update operation \"%{public}@\", using update operation identifier: %{public}@"
- "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tthirdPartyScan: %{public}@\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nFinished to perform the update operation \"%{public}@\" using operation identifier: %{public}@"
- "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tthirdPartyScan: %{public}@\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nFinished to refresh the current scan results with ID: %{public}@.\nResults: %{public}@"
- "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tthirdPartyScan: %{public}@\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nPost update request refresh operation completed successfully: %{public}@ with error: %{public}@; scan results: %{public}@"
- "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tthirdPartyScan: %{public}@\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nPurge result: %{public}@; error: %{public}@"
- "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tthirdPartyScan: %{public}@\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nReporting on available updates:\n\tPreferred update: %{public}@ (%p)\n\tAlternate update: %{public}@ (%p)"
- "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tthirdPartyScan: %{public}@\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nStarting to perform the update operation \"%{public}@\" into: %{public}@, using operation identifier: %{public}@"
- "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tthirdPartyScan: %{public}@\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nStarting to perform the update operation \"%{public}@\" on download: %{public}@, using operation identifier: %{public}@"
- "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tthirdPartyScan: %{public}@\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nThe Stateful UI delegate doesn't implement the purge confirmation dialog.Approving without user consent. This is not recommended."
- "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tthirdPartyScan: %{public}@\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nThe descriptors states and errors are identical to the previous values (refreshHasAnyChanges = YES). Dropping the refresh request."
- "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tthirdPartyScan: %{public}@\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nThe descriptors states and errors are identical to the previous values (refreshHasAnyChanges = YES). Force load was requested - proceeding to ask the delegate to reload the UI."
- "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tthirdPartyScan: %{public}@\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nThe full scan yielded empty scan results - cancelling the currently active update operation"
- "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tthirdPartyScan: %{public}@\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nThe full scan yielded results that are different than the previously discovered results - cancelling the currently active update operation.\n\tresults.preferredDescriptor: %{public}@\n\tresults.alternateDescriptor: %{public}@"
- "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tthirdPartyScan: %{public}@\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nThe given descriptor role, %@ (%ld), is invalid."
- "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tthirdPartyScan: %{public}@\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nThere is already an update operation running. Ignoring update request \"%{public}@\", into: %{public}@"
- "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tthirdPartyScan: %{public}@\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nUn-enroll from beta program success: %d"
- "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tthirdPartyScan: %{public}@\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nUser responded to the targeted update purge request of %{public}@, for beta program %ld (%p): %{public}@"
- "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tthirdPartyScan: %{public}@\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nisScanning: %{public}@; error: %{public}@"
- "%s [%p]: %{public}@ descriptor assignment: Replacing the current descriptor with a new descriptor.\n\tCurrent: %{public}@ (%p)\n\tNew: %{public}@ (%p)\n\tHiding: Preferred - %s; Alternate: %s"
- "%s [%p]: %{public}@ descriptor assignment: the given descriptor is equal to the current stateful descriptor. Updating internal state instead of creation of an entirely new one.\n\tCurrent: %{public}@ (%p)\n\tNew: %{public}@ (%p)\n\tHiding: Preferred - %s; Alternate: %s"
- "%s [%p]: canEnrollInBetaUpdates status changed to %s"
- "-[SUUIStatefulUIManager fsmAction_ThirdPartyScanDuringRefresh:error:]"
- "-[SUUIStatefulUIManager fsmAction_ThirdPartyScanDuringRefresh:error:]_block_invoke"
- "-[SUUIStatefulUIManager refreshState:]_block_invoke"
- "-[SUUIStatefulUIManager refreshStateWithCompletion:]_block_invoke"
- "PerformThirdPartyScan"
- "PerformUpdateOperation"
- "PerformingThirdPartyScan"
- "RefreshScanResultsSuccess"
- "T@\"<SUUIDownload>\",&,N,V_currentDownload"
- "T@\"<SUUIScanOperation>\",&,N,V_currentFullScanOperation"
- "T@\"<SUUIScanOperation>\",&,N,V_currentRefreshScanOperation"
- "T@\"<SUUIStatefulUIEnvironment>\",W,N,V_environment"
- "T@\"<SUUIStatefulUIManagerDelegate>\",W,N,V_delegate"
- "T@\"<SUUIUpdateOperation>\",&,N,V_currentUpdateOperation"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_delegateCallbackQueue"
- "T@\"SUCoreDDMDeclaration\",&,N,SsetDDMDeclaration:,V_ddmDeclaration"
- "T@\"SUUIStatefulDescriptor\",&,N,V_alternateStatefulDescriptor"
- "T@\"SUUIStatefulDescriptor\",&,N,V_hiddenAlternateStatefulDescriptor"
- "T@\"SUUIStatefulDescriptor\",&,N,V_hiddenPreferredStatefulDescriptor"
- "T@\"SUUIStatefulDescriptor\",&,N,V_preferredStatefulDescriptor"
- "T@\"SUUIStatefulError\",&,N,V_scanError"
- "TB,N,GisClearingSpaceForDownload,V_clearingSpaceForDownload"
- "TB,N,V_hidingAlternateDescriptor"
- "TB,N,V_hidingPreferredDescriptor"
- "TB,N,V_isAutoUpdateScheduled"
- "TQ,N,V_mdmPathRestrictions"
- "ThirdPartyScanDuringRefresh"
- "_performThirdPartyScan"
- "fsmAction_ThirdPartyScanDuringRefresh:error:"

```
