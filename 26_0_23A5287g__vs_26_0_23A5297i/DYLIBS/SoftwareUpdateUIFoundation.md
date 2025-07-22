## SoftwareUpdateUIFoundation

> `/System/Library/PrivateFrameworks/SoftwareUpdateUIFoundation.framework/SoftwareUpdateUIFoundation`

```diff

-508.0.1.502.1
-  __TEXT.__text: 0x7290c
-  __TEXT.__auth_stubs: 0x9e0
-  __TEXT.__objc_methlist: 0x175c
-  __TEXT.__cstring: 0x4c25
-  __TEXT.__gcc_except_tab: 0x4454
-  __TEXT.__oslogstring: 0x6f1f
-  __TEXT.__const: 0xe38
-  __TEXT.__constg_swiftt: 0x2ea
+508.0.30.0.0
+  __TEXT.__text: 0x790e0
+  __TEXT.__auth_stubs: 0xa90
+  __TEXT.__objc_methlist: 0x1784
+  __TEXT.__cstring: 0x4c15
+  __TEXT.__gcc_except_tab: 0x5270
+  __TEXT.__oslogstring: 0x863b
+  __TEXT.__const: 0xe48
+  __TEXT.__constg_swiftt: 0x2f2
   __TEXT.__swift5_typeref: 0x2fc
   __TEXT.__swift5_builtin: 0xb4
   __TEXT.__swift5_reflstr: 0x253

   __TEXT.__swift_as_entry: 0xc
   __TEXT.__swift_as_ret: 0x8
   __TEXT.__swift5_types2: 0x4
-  __TEXT.__unwind_info: 0xb20
+  __TEXT.__unwind_info: 0xb70
   __TEXT.__eh_frame: 0x618
-  __TEXT.__objc_classname: 0x5a4
-  __TEXT.__objc_methname: 0x5099
-  __TEXT.__objc_methtype: 0x7f2
-  __TEXT.__objc_stubs: 0x2bc0
-  __DATA_CONST.__got: 0x2c8
-  __DATA_CONST.__const: 0x19d8
+  __TEXT.__objc_classname: 0x5b5
+  __TEXT.__objc_methname: 0x50f3
+  __TEXT.__objc_methtype: 0x86e
+  __TEXT.__objc_stubs: 0x2c20
+  __DATA_CONST.__got: 0x2d0
+  __DATA_CONST.__const: 0x19e0
   __DATA_CONST.__objc_classlist: 0x148
+  __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xf40
+  __DATA_CONST.__objc_selrefs: 0xf60
   __DATA_CONST.__objc_superrefs: 0xd0
-  __AUTH_CONST.__auth_got: 0x500
-  __AUTH_CONST.__const: 0x578
-  __AUTH_CONST.__cfstring: 0x2fe0
-  __AUTH_CONST.__objc_const: 0x4388
+  __AUTH_CONST.__auth_got: 0x558
+  __AUTH_CONST.__const: 0x598
+  __AUTH_CONST.__cfstring: 0x2fa0
+  __AUTH_CONST.__objc_const: 0x43c8
   __AUTH.__objc_data: 0xcd0
   __AUTH.__data: 0x128
   __DATA.__objc_ivar: 0x1c8
   __DATA.__data: 0x6d0
-  __DATA.__bss: 0x1380
+  __DATA.__bss: 0x1390
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/UIKit.framework/UIKit

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 853AA4CB-170F-3562-9595-373FE0A39461
-  Functions: 1089
-  Symbols:   2997
-  CStrings:  1837
+  UUID: 0CA8A1E8-38CC-3087-A9FD-5D75AF388F62
+  Functions: 1113
+  Symbols:   3052
+  CStrings:  1896
 
Symbols:
+ -[SUCoreFSM(SoftwareUpdateUI) postEvent:endingActivity:]
+ -[SUCoreFSM(SoftwareUpdateUI) postEvent:withInfo:endingActivity:]
+ -[SUUIStatefulDescriptor setDownloadErrorPreventingUpdate:]
+ -[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:activity:completionHandler:]
+ -[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:afterPurgeConfirmation:activity:completionHandler:]
+ GCC_except_table102
+ GCC_except_table105
+ GCC_except_table106
+ GCC_except_table115
+ GCC_except_table122
+ GCC_except_table132
+ GCC_except_table145
+ GCC_except_table161
+ GCC_except_table164
+ GCC_except_table166
+ GCC_except_table168
+ GCC_except_table171
+ GCC_except_table194
+ GCC_except_table196
+ GCC_except_table214
+ GCC_except_table216
+ GCC_except_table217
+ GCC_except_table224
+ GCC_except_table233
+ GCC_except_table236
+ GCC_except_table238
+ GCC_except_table241
+ GCC_except_table243
+ GCC_except_table248
+ GCC_except_table313
+ GCC_except_table41
+ GCC_except_table45
+ GCC_except_table48
+ GCC_except_table52
+ GCC_except_table55
+ GCC_except_table59
+ GCC_except_table62
+ GCC_except_table66
+ GCC_except_table69
+ GCC_except_table73
+ GCC_except_table76
+ GCC_except_table80
+ GCC_except_table88
+ GCC_except_table97
+ __Block_object_dispose
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_SUCoreFSM_$_SoftwareUpdateUI
+ __OBJC_$_CATEGORY_SUCoreFSM_$_SoftwareUpdateUI
+ __SUUIActivityCleanup
+ __SUUISignpostCreate
+ __SUUISignpostCreateWithIdentifier
+ __SUUISignpostGetNanoseconds
+ __SUUISignpostGetNanoseconds.onceToken
+ __SUUISignpostGetNanoseconds.timebase_info
+ ___102-[SUUIStatefulUIManager downloadAndInstall:operationDelegate:delegateCallbackQueue:completionHandler:]_block_invoke.340
+ ___102-[SUUIStatefulUIManager downloadAndInstall:operationDelegate:delegateCallbackQueue:completionHandler:]_block_invoke_2.341
+ ___104-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:afterPurgeConfirmation:activity:completionHandler:]_block_invoke
+ ___104-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:afterPurgeConfirmation:activity:completionHandler:]_block_invoke.502
+ ___104-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:afterPurgeConfirmation:activity:completionHandler:]_block_invoke.504
+ ___104-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:afterPurgeConfirmation:activity:completionHandler:]_block_invoke.505
+ ___104-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:afterPurgeConfirmation:activity:completionHandler:]_block_invoke.506
+ ___104-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:afterPurgeConfirmation:activity:completionHandler:]_block_invoke_2
+ ___108-[SUUIStatefulUIManager promoteTargetedUpdateToUserInitiatedStatus:delegateCallbackQueue:completionHandler:]_block_invoke.388
+ ___108-[SUUIStatefulUIManager promoteTargetedUpdateToUserInitiatedStatus:delegateCallbackQueue:completionHandler:]_block_invoke_2.389
+ ___109-[SUUIStatefulUIManager downloadAndScheduleUpdate:operationDelegate:delegateCallbackQueue:completionHandler:]_block_invoke.351
+ ___109-[SUUIStatefulUIManager downloadAndScheduleUpdate:operationDelegate:delegateCallbackQueue:completionHandler:]_block_invoke_2.352
+ ___111-[SUUIStatefulUIManager unscheduleTargetedUpdateAutomaticInstallation:delegateCallbackQueue:completionHandler:]_block_invoke.399
+ ___111-[SUUIStatefulUIManager unscheduleTargetedUpdateAutomaticInstallation:delegateCallbackQueue:completionHandler:]_block_invoke_2.400
+ ___165-[SUUIStatefulUIManager performUpdateOnDownloadByApplyingSelector:context:description:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:]_block_invoke.481
+ ___165-[SUUIStatefulUIManager performUpdateOnDownloadByApplyingSelector:context:description:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:]_block_invoke.483
+ ___165-[SUUIStatefulUIManager performUpdateOnDownloadByApplyingSelector:context:description:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:]_block_invoke.484
+ ___165-[SUUIStatefulUIManager performUpdateOnDownloadByApplyingSelector:context:description:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:]_block_invoke.486
+ ___189-[SUUIStatefulUIManager performUpdateWithDescriptor:byApplyingSelector:context:description:auxiliaryOperation:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:]_block_invoke.469
+ ___189-[SUUIStatefulUIManager performUpdateWithDescriptor:byApplyingSelector:context:description:auxiliaryOperation:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:]_block_invoke.471
+ ___189-[SUUIStatefulUIManager performUpdateWithDescriptor:byApplyingSelector:context:description:auxiliaryOperation:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:]_block_invoke.472
+ ___189-[SUUIStatefulUIManager performUpdateWithDescriptor:byApplyingSelector:context:description:auxiliaryOperation:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:]_block_invoke.477
+ ___189-[SUUIStatefulUIManager performUpdateWithDescriptor:byApplyingSelector:context:description:auxiliaryOperation:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:]_block_invoke.478
+ ___189-[SUUIStatefulUIManager performUpdateWithDescriptor:byApplyingSelector:context:description:auxiliaryOperation:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:]_block_invoke.479
+ ___41-[SUUIStatefulUIManager performFullScan:]_block_invoke.459
+ ___41-[SUUIStatefulUIManager performFullScan:]_block_invoke.460
+ ___44-[SUUIStatefulUIManager performRefreshScan:]_block_invoke.464
+ ___46-[SUUIStatefulUIManager handleFailedFullScan:]_block_invoke.467
+ ___47-[SUUIStatefulUIManager handleFullScanResults:]_block_invoke.466
+ ___59-[SUUIStatefulUIManager refreshStateWithCompletion:forced:]_block_invoke.317
+ ___63-[SUUIStatefulUIManager unenrollFromBetaUpdatesWithCompletion:]_block_invoke.418
+ ___63-[SUUIStatefulUIManager unenrollFromBetaUpdatesWithCompletion:]_block_invoke.419
+ ___63-[SUUIStatefulUIManager unenrollFromBetaUpdatesWithCompletion:]_block_invoke.422
+ ___63-[SUUIStatefulUIManager unenrollFromBetaUpdatesWithCompletion:]_block_invoke.424
+ ___63-[SUUIStatefulUIManager unenrollFromBetaUpdatesWithCompletion:]_block_invoke.431
+ ___63-[SUUIStatefulUIManager unenrollFromBetaUpdatesWithCompletion:]_block_invoke.432
+ ___63-[SUUIStatefulUIManager unenrollFromBetaUpdatesWithCompletion:]_block_invoke_2.425
+ ___63-[SUUIStatefulUIManager unenrollFromBetaUpdatesWithCompletion:]_block_invoke_2.427
+ ___69-[SUUIStatefulUIManager performFullScanWithScanResults:andScanError:]_block_invoke.462
+ ___69-[SUUIStatefulUIManager performFullScanWithScanResults:andScanError:]_block_invoke.463
+ ___70-[SUUIStatefulUIManager enrollInBetaUpdatesProgram:completionHandler:]_block_invoke.406
+ ___70-[SUUIStatefulUIManager enrollInBetaUpdatesProgram:completionHandler:]_block_invoke.410
+ ___70-[SUUIStatefulUIManager enrollInBetaUpdatesProgram:completionHandler:]_block_invoke.412
+ ___70-[SUUIStatefulUIManager enrollInBetaUpdatesProgram:completionHandler:]_block_invoke.413
+ ___75-[SUUIStatefulUIManager refreshBetaUpdates:withRecheckForAvailableUpdates:]_block_invoke.434
+ ___75-[SUUIStatefulUIManager refreshBetaUpdates:withRecheckForAvailableUpdates:]_block_invoke.436
+ ___75-[SUUIStatefulUIManager refreshBetaUpdates:withRecheckForAvailableUpdates:]_block_invoke.437
+ ___75-[SUUIStatefulUIManager refreshBetaUpdates:withRecheckForAvailableUpdates:]_block_invoke_2.443
+ ___77-[SUUIStatefulUIManager checkForAvailableUpdatesWithForcedReload:completion:]_block_invoke.314
+ ___80-[SUUIStatefulUIManager checkForUpdatesInBackgroundWithForcedReload:completion:]_block_invoke.322
+ ___81-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:activity:completionHandler:]_block_invoke
+ ___81-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:activity:completionHandler:]_block_invoke.490
+ ___81-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:activity:completionHandler:]_block_invoke.492
+ ___81-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:activity:completionHandler:]_block_invoke.493
+ ___81-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:activity:completionHandler:]_block_invoke.494
+ ___81-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:activity:completionHandler:]_block_invoke.495
+ ___81-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:activity:completionHandler:]_block_invoke.499
+ ___81-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:activity:completionHandler:]_block_invoke.500
+ ___81-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:activity:completionHandler:]_block_invoke_2
+ ___81-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:activity:completionHandler:]_block_invoke_2.496
+ ___81-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:activity:completionHandler:]_block_invoke_3
+ ___95-[SUUIStatefulUIManager performPostUpdateOperationRefreshWithDownload:error:completionHandler:]_block_invoke.487
+ ___97-[SUUIStatefulUIManager installUpdate:operationDelegate:delegateCallbackQueue:completionHandler:]_block_invoke.362
+ ___97-[SUUIStatefulUIManager installUpdate:operationDelegate:delegateCallbackQueue:completionHandler:]_block_invoke_2.365
+ ___98-[SUUIStatefulUIManager downloadUpdate:operationDelegate:delegateCallbackQueue:completionHandler:]_block_invoke.327
+ ___98-[SUUIStatefulUIManager downloadUpdate:operationDelegate:delegateCallbackQueue:completionHandler:]_block_invoke_2.330
+ ___98-[SUUIStatefulUIManager scheduleUpdate:operationDelegate:delegateCallbackQueue:completionHandler:]_block_invoke.375
+ ___98-[SUUIStatefulUIManager scheduleUpdate:operationDelegate:delegateCallbackQueue:completionHandler:]_block_invoke_2.378
+ ____SUUISignpostGetNanoseconds_block_invoke
+ ___block_descriptor_64_e8_32bs40r48w_e8_v12?0B8lw48l8s32l8r40l8
+ ___block_descriptor_64_e8_32s40s48bs56r_e8_v16?0q8ls32l8s40l8r56l8s48l8
+ ___block_descriptor_65_e8_32bs40r48w_e54_v24?0"SUUIScanOperationFullScanResults"8"NSError"16lr40l8w48l8s32l8
+ ___block_descriptor_72_e8_32r40w_e64_v24?0"SUUIScanOperationFullScanResults"8"SUUIStatefulError"16lw40l8r32l8
+ ___block_descriptor_72_e8_32s40bs48r56w_e17_v16?0"NSError"8lw56l8s40l8s32l8r48l8
+ ___block_descriptor_72_e8_32s40bs48r56w_e5_v8?0lw56l8s40l8s32l8r48l8
+ ___block_descriptor_72_e8_32s40bs48w_e63_v24?0"SUUIUpdateOperationPurgeResults"8"SUUIStatefulError"16lw48l8s40l8s32l8
+ ___block_descriptor_73_e8_32s40bs48r56w_e5_v8?0ls32l8r48l8w56l8s40l8
+ ___block_descriptor_80_e8_32s40bs48w_e5_v8?0lw48l8s40l8s32l8
+ ___block_descriptor_80_e8_32s40r48w_e60_v24?0"SUUIScanOperationScanResults"8"SUUIStatefulError"16lw48l8s32l8r40l8
+ ___block_descriptor_80_e8_32s40r48w_e64_v24?0"SUUIScanOperationFullScanResults"8"SUUIStatefulError"16lw48l8s32l8r40l8
+ ___block_descriptor_80_e8_32s40s48bs56r64w_e54_v24?0"SUUIScanOperationFullScanResults"8"NSError"16lw64l8s48l8r56l8s32l8s40l8
+ ___block_descriptor_80_e8_32s40s48bs56r64w_e60_v24?0"SUUIScanOperationScanResults"8"SUUIStatefulError"16lw64l8s48l8s32l8s40l8r56l8
+ ___block_descriptor_81_e8_32bs40r48w_e57_v24?0"SUUIBetaUpdatesOperationScanResults"8"NSError"16lw48l8s32l8r40l8
+ ___block_descriptor_88_e8_32s40s48s56bs64r72w_e5_v8?0ls32l8w72l8s56l8r64l8s40l8s48l8
+ ___block_descriptor_97_e8_32s40s48bs56r64w_e5_v8?0lw64l8s48l8s32l8s40l8r56l8
+ ___block_literal_global.339
+ ___block_literal_global.349
+ ___block_literal_global.360
+ ___block_literal_global.373
+ ___block_literal_global.386
+ ___block_literal_global.397
+ ___os_log_helper_16_0_0
+ ___os_log_helper_16_0_1_4_2
+ ___os_log_helper_16_0_2_4_2_4_2
+ ___os_log_helper_16_0_2_8_0_8_0
+ ___os_log_helper_16_0_3_8_0_8_0_4_2
+ ___os_log_helper_16_0_4_8_0_8_0_4_2_4_2
+ ___os_log_helper_16_2_1_8_66
+ ___os_log_helper_16_2_2_8_0_8_66
+ ___os_log_helper_16_2_2_8_66_8_66
+ ___os_log_helper_16_2_3_4_2_4_2_8_66
+ ___os_log_helper_16_2_4_8_0_4_2_4_2_8_66
+ ___os_log_helper_16_2_4_8_0_8_0_8_66_8_66
+ __os_activity_create
+ __os_activity_current
+ __os_signpost_emit_with_name_impl
+ _mach_continuous_time
+ _mach_timebase_info
+ _malloc_type_calloc
+ _objc_msgSend$doEnrollInBetaUpdatesProgram:activity:completionHandler:
+ _objc_msgSend$doEnrollInBetaUpdatesProgram:afterPurgeConfirmation:activity:completionHandler:
+ _objc_msgSend$ownerManager
+ _objc_msgSend$postEvent:
+ _objc_msgSend$setDownloadErrorPreventingUpdate:
+ _os_activity_scope_enter
+ _os_activity_scope_leave
+ _os_signpost_enabled
+ _os_signpost_id_generate
+ _os_signpost_id_make_with_pointer
- -[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:afterPurgeConfirmation:completionHandler:]
- -[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:completionHandler:]
- GCC_except_table100
- GCC_except_table103
- GCC_except_table104
- GCC_except_table113
- GCC_except_table118
- GCC_except_table139
- GCC_except_table144
- GCC_except_table148
- GCC_except_table151
- GCC_except_table153
- GCC_except_table158
- GCC_except_table162
- GCC_except_table170
- GCC_except_table181
- GCC_except_table198
- GCC_except_table203
- GCC_except_table204
- GCC_except_table220
- GCC_except_table223
- GCC_except_table225
- GCC_except_table228
- GCC_except_table230
- GCC_except_table235
- GCC_except_table300
- GCC_except_table39
- GCC_except_table43
- GCC_except_table46
- GCC_except_table50
- GCC_except_table53
- GCC_except_table57
- GCC_except_table60
- GCC_except_table64
- GCC_except_table67
- GCC_except_table71
- GCC_except_table74
- GCC_except_table78
- GCC_except_table86
- GCC_except_table95
- _MA_AUTO_ASSET_SHORT_TERM_LOCK_FILESYSTEM_SPECIFIC
- ___102-[SUUIStatefulUIManager downloadAndInstall:operationDelegate:delegateCallbackQueue:completionHandler:]_block_invoke.343
- ___102-[SUUIStatefulUIManager downloadAndInstall:operationDelegate:delegateCallbackQueue:completionHandler:]_block_invoke_2.344
- ___108-[SUUIStatefulUIManager promoteTargetedUpdateToUserInitiatedStatus:delegateCallbackQueue:completionHandler:]_block_invoke.391
- ___108-[SUUIStatefulUIManager promoteTargetedUpdateToUserInitiatedStatus:delegateCallbackQueue:completionHandler:]_block_invoke_2.392
- ___109-[SUUIStatefulUIManager downloadAndScheduleUpdate:operationDelegate:delegateCallbackQueue:completionHandler:]_block_invoke.354
- ___109-[SUUIStatefulUIManager downloadAndScheduleUpdate:operationDelegate:delegateCallbackQueue:completionHandler:]_block_invoke_2.355
- ___111-[SUUIStatefulUIManager unscheduleTargetedUpdateAutomaticInstallation:delegateCallbackQueue:completionHandler:]_block_invoke.402
- ___111-[SUUIStatefulUIManager unscheduleTargetedUpdateAutomaticInstallation:delegateCallbackQueue:completionHandler:]_block_invoke_2.403
- ___165-[SUUIStatefulUIManager performUpdateOnDownloadByApplyingSelector:context:description:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:]_block_invoke.487
- ___165-[SUUIStatefulUIManager performUpdateOnDownloadByApplyingSelector:context:description:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:]_block_invoke.488
- ___165-[SUUIStatefulUIManager performUpdateOnDownloadByApplyingSelector:context:description:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:]_block_invoke.489
- ___165-[SUUIStatefulUIManager performUpdateOnDownloadByApplyingSelector:context:description:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:]_block_invoke.490
- ___189-[SUUIStatefulUIManager performUpdateWithDescriptor:byApplyingSelector:context:description:auxiliaryOperation:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:]_block_invoke.473
- ___189-[SUUIStatefulUIManager performUpdateWithDescriptor:byApplyingSelector:context:description:auxiliaryOperation:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:]_block_invoke.475
- ___189-[SUUIStatefulUIManager performUpdateWithDescriptor:byApplyingSelector:context:description:auxiliaryOperation:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:]_block_invoke.480
- ___189-[SUUIStatefulUIManager performUpdateWithDescriptor:byApplyingSelector:context:description:auxiliaryOperation:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:]_block_invoke.481
- ___189-[SUUIStatefulUIManager performUpdateWithDescriptor:byApplyingSelector:context:description:auxiliaryOperation:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:]_block_invoke.482
- ___189-[SUUIStatefulUIManager performUpdateWithDescriptor:byApplyingSelector:context:description:auxiliaryOperation:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:]_block_invoke.483
- ___41-[SUUIStatefulUIManager performFullScan:]_block_invoke.463
- ___41-[SUUIStatefulUIManager performFullScan:]_block_invoke.464
- ___44-[SUUIStatefulUIManager performRefreshScan:]_block_invoke.468
- ___46-[SUUIStatefulUIManager handleFailedFullScan:]_block_invoke.471
- ___47-[SUUIStatefulUIManager handleFullScanResults:]_block_invoke.470
- ___59-[SUUIStatefulUIManager refreshStateWithCompletion:forced:]_block_invoke.320
- ___63-[SUUIStatefulUIManager unenrollFromBetaUpdatesWithCompletion:]_block_invoke.421
- ___63-[SUUIStatefulUIManager unenrollFromBetaUpdatesWithCompletion:]_block_invoke.427
- ___63-[SUUIStatefulUIManager unenrollFromBetaUpdatesWithCompletion:]_block_invoke.428
- ___63-[SUUIStatefulUIManager unenrollFromBetaUpdatesWithCompletion:]_block_invoke.430
- ___63-[SUUIStatefulUIManager unenrollFromBetaUpdatesWithCompletion:]_block_invoke.435
- ___63-[SUUIStatefulUIManager unenrollFromBetaUpdatesWithCompletion:]_block_invoke.436
- ___63-[SUUIStatefulUIManager unenrollFromBetaUpdatesWithCompletion:]_block_invoke_2.429
- ___63-[SUUIStatefulUIManager unenrollFromBetaUpdatesWithCompletion:]_block_invoke_2.431
- ___69-[SUUIStatefulUIManager performFullScanWithScanResults:andScanError:]_block_invoke.466
- ___69-[SUUIStatefulUIManager performFullScanWithScanResults:andScanError:]_block_invoke.467
- ___70-[SUUIStatefulUIManager enrollInBetaUpdatesProgram:completionHandler:]_block_invoke.409
- ___70-[SUUIStatefulUIManager enrollInBetaUpdatesProgram:completionHandler:]_block_invoke.414
- ___70-[SUUIStatefulUIManager enrollInBetaUpdatesProgram:completionHandler:]_block_invoke.416
- ___70-[SUUIStatefulUIManager enrollInBetaUpdatesProgram:completionHandler:]_block_invoke.418
- ___72-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:completionHandler:]_block_invoke
- ___72-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:completionHandler:]_block_invoke.494
- ___72-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:completionHandler:]_block_invoke.496
- ___72-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:completionHandler:]_block_invoke.497
- ___72-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:completionHandler:]_block_invoke.498
- ___72-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:completionHandler:]_block_invoke.499
- ___72-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:completionHandler:]_block_invoke.503
- ___72-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:completionHandler:]_block_invoke.504
- ___72-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:completionHandler:]_block_invoke_2
- ___72-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:completionHandler:]_block_invoke_2.500
- ___72-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:completionHandler:]_block_invoke_3
- ___75-[SUUIStatefulUIManager refreshBetaUpdates:withRecheckForAvailableUpdates:]_block_invoke.440
- ___75-[SUUIStatefulUIManager refreshBetaUpdates:withRecheckForAvailableUpdates:]_block_invoke.445
- ___75-[SUUIStatefulUIManager refreshBetaUpdates:withRecheckForAvailableUpdates:]_block_invoke.446
- ___75-[SUUIStatefulUIManager refreshBetaUpdates:withRecheckForAvailableUpdates:]_block_invoke_2.447
- ___77-[SUUIStatefulUIManager checkForAvailableUpdatesWithForcedReload:completion:]_block_invoke.317
- ___80-[SUUIStatefulUIManager checkForUpdatesInBackgroundWithForcedReload:completion:]_block_invoke.325
- ___95-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:afterPurgeConfirmation:completionHandler:]_block_invoke
- ___95-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:afterPurgeConfirmation:completionHandler:]_block_invoke.506
- ___95-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:afterPurgeConfirmation:completionHandler:]_block_invoke.508
- ___95-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:afterPurgeConfirmation:completionHandler:]_block_invoke.509
- ___95-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:afterPurgeConfirmation:completionHandler:]_block_invoke.510
- ___95-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:afterPurgeConfirmation:completionHandler:]_block_invoke_2
- ___95-[SUUIStatefulUIManager performPostUpdateOperationRefreshWithDownload:error:completionHandler:]_block_invoke.491
- ___97-[SUUIStatefulUIManager installUpdate:operationDelegate:delegateCallbackQueue:completionHandler:]_block_invoke.365
- ___97-[SUUIStatefulUIManager installUpdate:operationDelegate:delegateCallbackQueue:completionHandler:]_block_invoke_2.368
- ___98-[SUUIStatefulUIManager downloadUpdate:operationDelegate:delegateCallbackQueue:completionHandler:]_block_invoke.330
- ___98-[SUUIStatefulUIManager downloadUpdate:operationDelegate:delegateCallbackQueue:completionHandler:]_block_invoke_2.333
- ___98-[SUUIStatefulUIManager scheduleUpdate:operationDelegate:delegateCallbackQueue:completionHandler:]_block_invoke.378
- ___98-[SUUIStatefulUIManager scheduleUpdate:operationDelegate:delegateCallbackQueue:completionHandler:]_block_invoke_2.381
- ___block_descriptor_48_e8_32w_e64_v24?0"SUUIScanOperationFullScanResults"8"SUUIStatefulError"16lw32l8
- ___block_descriptor_56_e8_32bs40w_e8_v12?0B8lw40l8s32l8
- ___block_descriptor_56_e8_32s40s48bs_e8_v16?0q8ls32l8s40l8s48l8
- ___block_descriptor_56_e8_32s40w_e60_v24?0"SUUIScanOperationScanResults"8"SUUIStatefulError"16lw40l8s32l8
- ___block_descriptor_56_e8_32s40w_e64_v24?0"SUUIScanOperationFullScanResults"8"SUUIStatefulError"16lw40l8s32l8
- ___block_descriptor_57_e8_32bs40w_e54_v24?0"SUUIScanOperationFullScanResults"8"NSError"16lw40l8s32l8
- ___block_descriptor_57_e8_32bs40w_e57_v24?0"SUUIBetaUpdatesOperationScanResults"8"NSError"16lw40l8s32l8
- ___block_descriptor_64_e8_32s40bs48w_e17_v16?0"NSError"8lw48l8s40l8s32l8
- ___block_descriptor_64_e8_32s40bs48w_e63_v24?0"SUUIUpdateOperationPurgeResults"8"SUUIStatefulError"16lw48l8s40l8s32l8
- ___block_descriptor_65_e8_32s40bs48w_e5_v8?0ls32l8w48l8s40l8
- ___block_descriptor_72_e8_32s40bs48w_e5_v8?0lw48l8s40l8s32l8
- ___block_descriptor_72_e8_32s40s48bs56w_e54_v24?0"SUUIScanOperationFullScanResults"8"NSError"16lw56l8s48l8s32l8s40l8
- ___block_descriptor_72_e8_32s40s48bs56w_e60_v24?0"SUUIScanOperationScanResults"8"SUUIStatefulError"16lw56l8s48l8s32l8s40l8
- ___block_descriptor_73_e8_32s40s48bs56w_e5_v8?0lw56l8s48l8s32l8s40l8
- ___block_descriptor_80_e8_32s40s48s56bs64w_e5_v8?0ls32l8w64l8s56l8s40l8s48l8
- ___block_literal_global.342
- ___block_literal_global.352
- ___block_literal_global.363
- ___block_literal_global.376
- ___block_literal_global.389
- ___block_literal_global.400
- _objc_msgSend$doEnrollInBetaUpdatesProgram:afterPurgeConfirmation:completionHandler:
- _objc_msgSend$doEnrollInBetaUpdatesProgram:completionHandler:
CStrings:
+ "-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:activity:completionHandler:]_block_invoke"
+ "-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:activity:completionHandler:]_block_invoke_2"
+ "-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:activity:completionHandler:]_block_invoke_3"
+ "-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:afterPurgeConfirmation:activity:completionHandler:]_block_invoke"
+ "-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:afterPurgeConfirmation:activity:completionHandler:]_block_invoke_2"
+ "BEGIN [%lld]: FullScan Begins full scan  ScanIdentifier=%{public,signpost.telemetry:string1,name=ScanIdentifier}@  enableTelemetry=YES "
+ "BEGIN [%lld]: FullScan Begins full scan /w 3rd party results  HasScanResults=%{public,signpost.telemetry:number1,name=HasScanResults}d  ScanError=%{public,signpost.telemetry:number2,name=ScanError}d  ScanIdentifier=%{public,signpost.telemetry:string1,name=ScanIdentifier}@  enableTelemetry=YES "
+ "BEGIN [%lld]: RefreshBetaUpdates Refreshing beta updates  ScanIdentifier=%{public,signpost.telemetry:string1,name=ScanIdentifier}@  enableTelemetry=YES "
+ "BEGIN [%lld]: RefreshScan Begins refresh scan  HasScanResults=%{public,signpost.telemetry:number1,name=HasScanResults}d  ScanError=%{public,signpost.telemetry:number2,name=ScanError}d  ScanIdentifier=%{public,signpost.telemetry:string1,name=ScanIdentifier}@  enableTelemetry=YES "
+ "Begins full scan  ScanIdentifier=%{public,signpost.telemetry:string1,name=ScanIdentifier}@  enableTelemetry=YES "
+ "Begins full scan /w 3rd party results  HasScanResults=%{public,signpost.telemetry:number1,name=HasScanResults}d  ScanError=%{public,signpost.telemetry:number2,name=ScanError}d  ScanIdentifier=%{public,signpost.telemetry:string1,name=ScanIdentifier}@  enableTelemetry=YES "
+ "Begins refresh scan  HasScanResults=%{public,signpost.telemetry:number1,name=HasScanResults}d  ScanError=%{public,signpost.telemetry:number2,name=ScanError}d  ScanIdentifier=%{public,signpost.telemetry:string1,name=ScanIdentifier}@  enableTelemetry=YES "
+ "END [%lld] %fs: FullScan "
+ "END [%lld] %fs: RefreshBetaUpdates Finished to refresh the beta updates programs  Error=%{public,signpost.telemetry:number1,name=Error}d  BetaPrograms=%{public,signpost.telemetry:number2,name=BetaPrograms}d "
+ "END [%lld] %fs: RefreshScan "
+ "EVENT [%lld] %fs: FullScan Full scan /w 3rd-party results failed Error=%{public,signpost.telemetry:number1,name=Error}d "
+ "EVENT [%lld] %fs: FullScan Full scan /w 3rd-party results finished successfully PreferredUpdate=%{public,signpost.telemetry:string1,name=PreferredUpdate}@  AlternateUpdate=%{public,signpost.telemetry:string2,name=AlternateUpdate}@ "
+ "EVENT [%lld] %fs: FullScan Full scan failed Error=%{public,signpost.telemetry:number1,name=Error}d "
+ "EVENT [%lld] %fs: FullScan Full scan finished successfully PreferredUpdate=%{public,signpost.telemetry:string1,name=PreferredUpdate}@  AlternateUpdate=%{public,signpost.telemetry:string2,name=AlternateUpdate}@ "
+ "EVENT [%lld] %fs: RefreshScan Refresh scan failed Error=%{public,signpost.telemetry:number1,name=Error}d "
+ "EVENT [%lld] %fs: RefreshScan Refresh scan finished successfully"
+ "Failed to create an activity for: com.apple.SoftwareUpdateUI.StatefulUI.Manager.DownloadOnly"
+ "Failed to create an activity for: com.apple.SoftwareUpdateUI.StatefulUI.Manager.FullScan"
+ "Failed to create an activity for: com.apple.SoftwareUpdateUI.StatefulUI.Manager.InstallNow"
+ "Failed to create an activity for: com.apple.SoftwareUpdateUI.StatefulUI.Manager.NeRDInfo"
+ "Failed to create an activity for: com.apple.SoftwareUpdateUI.StatefulUI.Manager.PostUpdateRefresh"
+ "Failed to create an activity for: com.apple.SoftwareUpdateUI.StatefulUI.Manager.PromoteToUserInitiated"
+ "Failed to create an activity for: com.apple.SoftwareUpdateUI.StatefulUI.Manager.RefreshBetaUpdates"
+ "Failed to create an activity for: com.apple.SoftwareUpdateUI.StatefulUI.Manager.RefreshScan"
+ "Failed to create an activity for: com.apple.SoftwareUpdateUI.StatefulUI.Manager.Schedule"
+ "Failed to create an activity for: com.apple.SoftwareUpdateUI.StatefulUI.Manager.ThirdPartyFullScan"
+ "Failed to create an activity for: com.apple.SoftwareUpdateUI.StatefulUI.Manager.UnenrollFromBetaUpdates"
+ "Failed to create an activity for: com.apple.SoftwareUpdateUI.StatefulUI.Manager.Unschedule"
+ "Failed to create an activity for: com.apple.SoftwareUpdateUI.StatefulUI.Manager.UpdateNeRD"
+ "Failed to create an activity for: com.apple.SoftwareUpdateUI.StatefulUI.Manager.UpdateNow"
+ "Failed to create an activity for: com.apple.SoftwareUpdateUI.StatefulUI.Manager.UpdateTonight"
+ "Finished to refresh the beta updates programs  Error=%{public,signpost.telemetry:number1,name=Error}d  BetaPrograms=%{public,signpost.telemetry:number2,name=BetaPrograms}d "
+ "Full scan /w 3rd-party results failed Error=%{public,signpost.telemetry:number1,name=Error}d "
+ "Full scan /w 3rd-party results finished successfully PreferredUpdate=%{public,signpost.telemetry:string1,name=PreferredUpdate}@  AlternateUpdate=%{public,signpost.telemetry:string2,name=AlternateUpdate}@ "
+ "Full scan failed Error=%{public,signpost.telemetry:number1,name=Error}d "
+ "Full scan finished successfully PreferredUpdate=%{public,signpost.telemetry:string1,name=PreferredUpdate}@  AlternateUpdate=%{public,signpost.telemetry:string2,name=AlternateUpdate}@ "
+ "FullScan"
+ "Refresh scan failed Error=%{public,signpost.telemetry:number1,name=Error}d "
+ "Refresh scan finished successfully"
+ "RefreshBetaUpdates"
+ "RefreshScan"
+ "Refreshing beta updates  ScanIdentifier=%{public,signpost.telemetry:string1,name=ScanIdentifier}@  enableTelemetry=YES "
+ "T@\"<SUUIDescriptor>\",&,V_descriptor"
+ "T@\"SUUIStatefulError\",&,V_updateDownloadError"
+ "T@\"SUUIStatefulUIManager\",W,V_ownerManager"
+ "TB,GisDownloadable,V_updateDownloadable"
+ "TB,V_downloadErrorPreventingUpdate"
+ "TQ,V_role"
+ "com.apple.SoftwareUpdateUI.StatefulUI.Manager.DownloadOnly"
+ "com.apple.SoftwareUpdateUI.StatefulUI.Manager.FullScan"
+ "com.apple.SoftwareUpdateUI.StatefulUI.Manager.InstallNow"
+ "com.apple.SoftwareUpdateUI.StatefulUI.Manager.NeRDInfo"
+ "com.apple.SoftwareUpdateUI.StatefulUI.Manager.PostUpdateRefresh"
+ "com.apple.SoftwareUpdateUI.StatefulUI.Manager.PromoteToUserInitiated"
+ "com.apple.SoftwareUpdateUI.StatefulUI.Manager.RefreshBetaUpdates"
+ "com.apple.SoftwareUpdateUI.StatefulUI.Manager.RefreshScan"
+ "com.apple.SoftwareUpdateUI.StatefulUI.Manager.Schedule"
+ "com.apple.SoftwareUpdateUI.StatefulUI.Manager.ThirdPartyFullScan"
+ "com.apple.SoftwareUpdateUI.StatefulUI.Manager.UnenrollFromBetaUpdates"
+ "com.apple.SoftwareUpdateUI.StatefulUI.Manager.Unschedule"
+ "com.apple.SoftwareUpdateUI.StatefulUI.Manager.UpdateNeRD"
+ "com.apple.SoftwareUpdateUI.StatefulUI.Manager.UpdateNow"
+ "com.apple.SoftwareUpdateUI.StatefulUI.Manager.UpdateTonight"
+ "doEnrollInBetaUpdatesProgram:activity:completionHandler:"
+ "doEnrollInBetaUpdatesProgram:afterPurgeConfirmation:activity:completionHandler:"
+ "postEvent:"
+ "postEvent:endingActivity:"
+ "postEvent:withInfo:endingActivity:"
+ "setDownloadErrorPreventingUpdate:"
+ "v32@0:8@16^^{suui_activity_s}24"
+ "v40@0:8@16@24^^{suui_activity_s}32"
+ "v40@0:8@16^^{suui_activity_s}24@?32"
+ "v48@0:8@16q24^^{suui_activity_s}32@?40"
- "-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:afterPurgeConfirmation:completionHandler:]_block_invoke"
- "-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:afterPurgeConfirmation:completionHandler:]_block_invoke_2"
- "-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:completionHandler:]_block_invoke"
- "-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:completionHandler:]_block_invoke_2"
- "-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:completionHandler:]_block_invoke_3"
- "ReactiveManager"
- "T@\"<SUUIDescriptor>\",&,N,V_descriptor"
- "T@\"SUUIStatefulError\",&,N,V_updateDownloadError"
- "T@\"SUUIStatefulUIManager\",W,N,V_ownerManager"
- "TB,N,GisDownloadable,V_updateDownloadable"
- "TB,R,N,V_downloadErrorPreventingUpdate"
- "TQ,N,V_role"
- "Tq,N,V_currentState"
- "doEnrollInBetaUpdatesProgram:afterPurgeConfirmation:completionHandler:"
- "doEnrollInBetaUpdatesProgram:completionHandler:"
- "specific"
- "v40@0:8@16q24@?32"

```
