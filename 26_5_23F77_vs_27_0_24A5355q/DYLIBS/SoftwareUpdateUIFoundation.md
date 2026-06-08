## SoftwareUpdateUIFoundation

> `/System/Library/PrivateFrameworks/SoftwareUpdateUIFoundation.framework/SoftwareUpdateUIFoundation`

```diff

-508.122.1.0.0
-  __TEXT.__text: 0xa4dc0
-  __TEXT.__auth_stubs: 0x1130
-  __TEXT.__objc_methlist: 0x1da4
-  __TEXT.__cstring: 0x5d58
-  __TEXT.__gcc_except_tab: 0x5750
-  __TEXT.__oslogstring: 0x9b07
-  __TEXT.__const: 0x1d40
-  __TEXT.__swift5_typeref: 0x6e3
-  __TEXT.__swift5_reflstr: 0x47e
-  __TEXT.__swift5_assocty: 0x390
-  __TEXT.__constg_swiftt: 0x48e
-  __TEXT.__swift5_builtin: 0xdc
-  __TEXT.__swift5_fieldmd: 0x30c
-  __TEXT.__swift5_proto: 0x148
-  __TEXT.__swift5_types: 0x60
+772.0.0.0.0
+  __TEXT.__text: 0xa2d78
+  __TEXT.__objc_methlist: 0x1f6c
+  __TEXT.__cstring: 0x65de
+  __TEXT.__gcc_except_tab: 0x21ec
+  __TEXT.__oslogstring: 0x9f67
+  __TEXT.__const: 0x2300
+  __TEXT.__swift5_typeref: 0x75d
+  __TEXT.__swift5_reflstr: 0x61e
+  __TEXT.__swift5_assocty: 0x468
+  __TEXT.__constg_swiftt: 0x502
+  __TEXT.__swift5_builtin: 0xc8
+  __TEXT.__swift5_fieldmd: 0x418
+  __TEXT.__swift5_proto: 0x1a4
+  __TEXT.__swift5_types: 0x70
   __TEXT.__swift5_protos: 0xc
   __TEXT.__swift5_capture: 0x328
   __TEXT.__swift_as_entry: 0x18
   __TEXT.__swift_as_ret: 0x38
+  __TEXT.__swift_as_cont: 0x48
   __TEXT.__swift5_types2: 0x4
-  __TEXT.__unwind_info: 0xfb8
-  __TEXT.__eh_frame: 0x9b0
-  __TEXT.__objc_classname: 0x670
-  __TEXT.__objc_methname: 0x5ef5
-  __TEXT.__objc_methtype: 0x1210
-  __TEXT.__objc_stubs: 0x3280
-  __DATA_CONST.__got: 0x3f8
-  __DATA_CONST.__const: 0x2058
-  __DATA_CONST.__objc_classlist: 0x160
+  __TEXT.__unwind_info: 0x1110
+  __TEXT.__eh_frame: 0xba8
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x2250
+  __DATA_CONST.__objc_classlist: 0x178
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1270
+  __DATA_CONST.__objc_selrefs: 0x1358
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0xe0
-  __AUTH_CONST.__auth_got: 0x8a8
-  __AUTH_CONST.__const: 0x1430
-  __AUTH_CONST.__cfstring: 0x37a0
-  __AUTH_CONST.__objc_const: 0x5af0
-  __AUTH_CONST.__objc_intobj: 0xc0
-  __AUTH.__objc_data: 0xdc0
+  __DATA_CONST.__objc_superrefs: 0xf8
+  __DATA_CONST.__got: 0x428
+  __AUTH_CONST.__const: 0x1750
+  __AUTH_CONST.__cfstring: 0x3b20
+  __AUTH_CONST.__objc_const: 0x6010
+  __AUTH_CONST.__objc_intobj: 0xd8
+  __AUTH_CONST.__auth_got: 0x948
+  __AUTH.__objc_data: 0xeb0
   __AUTH.__data: 0x40
-  __DATA.__objc_ivar: 0x224
-  __DATA.__data: 0xc58
-  __DATA.__bss: 0x2a10
+  __DATA.__objc_ivar: 0x254
+  __DATA.__data: 0xdd0
+  __DATA.__bss: 0x35f8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/UIKit.framework/UIKit

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
+  - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 02B657CA-1320-3B3B-89A2-BA2B03E09DCC
-  Functions: 1762
-  Symbols:   3780
-  CStrings:  2303
+  UUID: 3FB25277-A530-33CF-846F-41913BAE0332
+  Functions: 1985
+  Symbols:   4144
+  CStrings:  1374
 
Symbols:
+ +[SUUILoggingContext bridgeLogger]
+ +[SUUIRetryConfiguration supportsSecureCoding]
+ +[SUUIRetryConfiguration(Presets) defaultConfiguration]
+ +[SUUIRetryConfiguration(Presets) quickConfiguration]
+ +[SUUIRetryConfiguration(Presets) scanWaitConfiguration]
+ +[SUUIUserDefaults(Foundation) documentationMandatoryUpdateBodyEntry]
+ -[SUUIRetryCancellationToken cancel]
+ -[SUUIRetryCancellationToken description]
+ -[SUUIRetryCancellationToken init]
+ -[SUUIRetryCancellationToken isCancelled]
+ -[SUUIRetryConfiguration description]
+ -[SUUIRetryConfiguration encodeWithCoder:]
+ -[SUUIRetryConfiguration estimatedTotalTimeout]
+ -[SUUIRetryConfiguration hash]
+ -[SUUIRetryConfiguration initWithCoder:]
+ -[SUUIRetryConfiguration initWithMaxAttempts:initialDelay:maxDelay:multiplier:jitterEnabled:jitterRatio:]
+ -[SUUIRetryConfiguration initialDelay]
+ -[SUUIRetryConfiguration isEqual:]
+ -[SUUIRetryConfiguration jitterEnabled]
+ -[SUUIRetryConfiguration jitterRatio]
+ -[SUUIRetryConfiguration maxAttempts]
+ -[SUUIRetryConfiguration maxDelay]
+ -[SUUIRetryConfiguration multiplier]
+ -[SUUIRetryExecutor .cxx_destruct]
+ -[SUUIRetryExecutor _calculateNextDelay:]
+ -[SUUIRetryExecutor _completeWithResult:value:error:completion:]
+ -[SUUIRetryExecutor _executeAttempt:currentDelay:operation:completion:token:]
+ -[SUUIRetryExecutor _handleAttemptFinished:value:error:attemptNumber:currentDelay:operation:completion:token:]
+ -[SUUIRetryExecutor executeOperation:completion:]
+ -[SUUIRetryExecutor initWithConfiguration:identifier:]
+ -[SUUIRetryExecutor initWithConfiguration:identifier:completionQueue:]
+ -[SUUIUserDefaults(Foundation) documentationMandatoryUpdateBody:]
+ -[SUUIUserDefaults(Foundation) documentationMandatoryUpdateBody]
+ -[SUUIUserDefaultsBasedDocumentation mandatoryUpdateBodyString]
+ GCC_except_table158
+ GCC_except_table160
+ GCC_except_table163
+ GCC_except_table165
+ GCC_except_table170
+ GCC_except_table178
+ GCC_except_table183
+ GCC_except_table189
+ GCC_except_table191
+ GCC_except_table196
+ GCC_except_table206
+ GCC_except_table209
+ GCC_except_table212
+ GCC_except_table219
+ GCC_except_table227
+ GCC_except_table229
+ GCC_except_table233
+ GCC_except_table240
+ GCC_except_table248
+ GCC_except_table251
+ GCC_except_table253
+ GCC_except_table261
+ GCC_except_table264
+ GCC_except_table270
+ GCC_except_table334
+ _MA_PALLAS_AUDIENCE_NAME_DEMO_EXTERNAL
+ _MA_PALLAS_AUDIENCE_NAME_DEMO_INTERNAL
+ _MA_PALLAS_AUDIENCE_RELEASE_ALIGNED_CARRIER
+ _MA_PALLAS_AUDIENCE_RELEASE_ALIGNED_DEMO_EXTERNAL
+ _MA_PALLAS_AUDIENCE_RELEASE_ALIGNED_DEMO_INTERNAL
+ _MA_SANDBOX_EXTENSION_SHORT_TERM_LOCKS_KEY
+ _MA_SANDBOX_EXTENSION_SHORT_TERM_LOCKS_PATH_KEY
+ _OBJC_CLASS_$_SUUIRetryCancellationToken
+ _OBJC_CLASS_$_SUUIRetryConfiguration
+ _OBJC_CLASS_$_SUUIRetryExecutor
+ _OBJC_IVAR_$_SUUIRetryCancellationToken._cancelled
+ _OBJC_IVAR_$_SUUIRetryConfiguration._initialDelay
+ _OBJC_IVAR_$_SUUIRetryConfiguration._jitterEnabled
+ _OBJC_IVAR_$_SUUIRetryConfiguration._jitterRatio
+ _OBJC_IVAR_$_SUUIRetryConfiguration._maxAttempts
+ _OBJC_IVAR_$_SUUIRetryConfiguration._maxDelay
+ _OBJC_IVAR_$_SUUIRetryConfiguration._multiplier
+ _OBJC_IVAR_$_SUUIRetryExecutor._completionQueue
+ _OBJC_IVAR_$_SUUIRetryExecutor._configuration
+ _OBJC_IVAR_$_SUUIRetryExecutor._identifier
+ _OBJC_IVAR_$_SUUIRetryExecutor._internalQueue
+ _OBJC_IVAR_$_SUUIRetryExecutor._selfRetain
+ _OBJC_METACLASS_$_SUUIRetryCancellationToken
+ _OBJC_METACLASS_$_SUUIRetryConfiguration
+ _OBJC_METACLASS_$_SUUIRetryExecutor
+ __MergedGlobals
+ __OBJC_$_CLASS_METHODS_SUUIRetryConfiguration(Presets)
+ __OBJC_$_INSTANCE_METHODS_SUUIRetryCancellationToken
+ __OBJC_$_INSTANCE_METHODS_SUUIRetryConfiguration
+ __OBJC_$_INSTANCE_METHODS_SUUIRetryExecutor
+ __OBJC_$_INSTANCE_VARIABLES_SUUIRetryCancellationToken
+ __OBJC_$_INSTANCE_VARIABLES_SUUIRetryConfiguration
+ __OBJC_$_INSTANCE_VARIABLES_SUUIRetryExecutor
+ __OBJC_$_PROP_LIST_SUUIRetryCancellationToken
+ __OBJC_$_PROP_LIST_SUUIRetryConfiguration
+ __OBJC_CLASS_PROTOCOLS_$_SUUIRetryConfiguration
+ __OBJC_CLASS_RO_$_SUUIRetryCancellationToken
+ __OBJC_CLASS_RO_$_SUUIRetryConfiguration
+ __OBJC_CLASS_RO_$_SUUIRetryExecutor
+ __OBJC_METACLASS_RO_$_SUUIRetryCancellationToken
+ __OBJC_METACLASS_RO_$_SUUIRetryConfiguration
+ __OBJC_METACLASS_RO_$_SUUIRetryExecutor
+ ___100-[SUUIStatefulUIManager doUnenrollFromBetaUpdatesAfterPurgeConfirmation:activity:completionHandler:]_block_invoke.565
+ ___100-[SUUIStatefulUIManager doUnenrollFromBetaUpdatesAfterPurgeConfirmation:activity:completionHandler:]_block_invoke.567
+ ___100-[SUUIStatefulUIManager doUnenrollFromBetaUpdatesAfterPurgeConfirmation:activity:completionHandler:]_block_invoke.568
+ ___100-[SUUIStatefulUIManager doUnenrollFromBetaUpdatesAfterPurgeConfirmation:activity:completionHandler:]_block_invoke.569
+ ___102-[SUUIStatefulUIManager downloadAndInstall:operationDelegate:delegateCallbackQueue:completionHandler:]_block_invoke.409
+ ___102-[SUUIStatefulUIManager downloadAndInstall:operationDelegate:delegateCallbackQueue:completionHandler:]_block_invoke_2.410
+ ___104-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:afterPurgeConfirmation:activity:completionHandler:]_block_invoke.548
+ ___104-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:afterPurgeConfirmation:activity:completionHandler:]_block_invoke.550
+ ___104-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:afterPurgeConfirmation:activity:completionHandler:]_block_invoke.551
+ ___104-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:afterPurgeConfirmation:activity:completionHandler:]_block_invoke.552
+ ___108-[SUUIStatefulUIManager promoteTargetedUpdateToUserInitiatedStatus:delegateCallbackQueue:completionHandler:]_block_invoke.442
+ ___109-[SUUIStatefulUIManager downloadAndScheduleUpdate:operationDelegate:delegateCallbackQueue:completionHandler:]_block_invoke.417
+ ___109-[SUUIStatefulUIManager downloadAndScheduleUpdate:operationDelegate:delegateCallbackQueue:completionHandler:]_block_invoke_2.418
+ ___110-[SUUIRetryExecutor _handleAttemptFinished:value:error:attemptNumber:currentDelay:operation:completion:token:]_block_invoke
+ ___111-[SUUIStatefulUIManager unscheduleTargetedUpdateAutomaticInstallation:delegateCallbackQueue:completionHandler:]_block_invoke.452
+ ___165-[SUUIStatefulUIManager performUpdateOnDownloadByApplyingSelector:context:description:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:]_block_invoke.526
+ ___165-[SUUIStatefulUIManager performUpdateOnDownloadByApplyingSelector:context:description:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:]_block_invoke.528
+ ___165-[SUUIStatefulUIManager performUpdateOnDownloadByApplyingSelector:context:description:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:]_block_invoke.529
+ ___165-[SUUIStatefulUIManager performUpdateOnDownloadByApplyingSelector:context:description:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:]_block_invoke.530
+ ___165-[SUUIStatefulUIManager performUpdateOnDownloadByApplyingSelector:context:description:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:]_block_invoke.531
+ ___187-[SUUIStatefulUIManager performUpdateOperation:withDescriptor:byApplyingSelector:context:auxiliaryOperation:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:]_block_invoke.514
+ ___187-[SUUIStatefulUIManager performUpdateOperation:withDescriptor:byApplyingSelector:context:auxiliaryOperation:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:]_block_invoke.516
+ ___187-[SUUIStatefulUIManager performUpdateOperation:withDescriptor:byApplyingSelector:context:auxiliaryOperation:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:]_block_invoke.517
+ ___187-[SUUIStatefulUIManager performUpdateOperation:withDescriptor:byApplyingSelector:context:auxiliaryOperation:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:]_block_invoke.521
+ ___187-[SUUIStatefulUIManager performUpdateOperation:withDescriptor:byApplyingSelector:context:auxiliaryOperation:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:]_block_invoke.522
+ ___187-[SUUIStatefulUIManager performUpdateOperation:withDescriptor:byApplyingSelector:context:auxiliaryOperation:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:]_block_invoke.523
+ ___187-[SUUIStatefulUIManager performUpdateOperation:withDescriptor:byApplyingSelector:context:auxiliaryOperation:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:]_block_invoke.524
+ ___34+[SUUILoggingContext bridgeLogger]_block_invoke
+ ___41-[SUUIStatefulUIManager performFullScan:]_block_invoke.500
+ ___41-[SUUIStatefulUIManager performFullScan:]_block_invoke.502
+ ___41-[SUUIStatefulUIManager performFullScan:]_block_invoke.506
+ ___44-[SUUIStatefulUIManager performRefreshScan:]_block_invoke.510
+ ___46-[SUUIStatefulUIManager handleFailedFullScan:]_block_invoke.512
+ ___53+[SUUIRetryConfiguration(Presets) quickConfiguration]_block_invoke
+ ___55+[SUUIRetryConfiguration(Presets) defaultConfiguration]_block_invoke
+ ___56+[SUUIRetryConfiguration(Presets) scanWaitConfiguration]_block_invoke
+ ___59-[SUUIStatefulUIManager refreshStateWithCompletion:forced:]_block_invoke.389
+ ___63-[SUUIStatefulUIManager unenrollFromBetaUpdatesWithCompletion:]_block_invoke.467
+ ___63-[SUUIStatefulUIManager unenrollFromBetaUpdatesWithCompletion:]_block_invoke.469
+ ___63-[SUUIStatefulUIManager unenrollFromBetaUpdatesWithCompletion:]_block_invoke.471
+ ___63-[SUUIStatefulUIManager unenrollFromBetaUpdatesWithCompletion:]_block_invoke.473
+ ___63-[SUUIStatefulUIManager unenrollFromBetaUpdatesWithCompletion:]_block_invoke_2.472
+ ___64-[SUUIRetryExecutor _completeWithResult:value:error:completion:]_block_invoke
+ ___64-[SUUIStatefulUIManager notifyDelegateOfStateRefreshWithReason:]_block_invoke.587
+ ___69-[SUUIStatefulUIManager doUnenrollFromBetaUpdates:completionHandler:]_block_invoke.554
+ ___69-[SUUIStatefulUIManager doUnenrollFromBetaUpdates:completionHandler:]_block_invoke.556
+ ___69-[SUUIStatefulUIManager doUnenrollFromBetaUpdates:completionHandler:]_block_invoke.557
+ ___69-[SUUIStatefulUIManager doUnenrollFromBetaUpdates:completionHandler:]_block_invoke.558
+ ___69-[SUUIStatefulUIManager doUnenrollFromBetaUpdates:completionHandler:]_block_invoke.559
+ ___69-[SUUIStatefulUIManager doUnenrollFromBetaUpdates:completionHandler:]_block_invoke.563
+ ___69-[SUUIStatefulUIManager doUnenrollFromBetaUpdates:completionHandler:]_block_invoke.564
+ ___69-[SUUIStatefulUIManager doUnenrollFromBetaUpdates:completionHandler:]_block_invoke_2.560
+ ___69-[SUUIStatefulUIManager performFullScanWithScanResults:andScanError:]_block_invoke.508
+ ___69-[SUUIStatefulUIManager performFullScanWithScanResults:andScanError:]_block_invoke.509
+ ___70-[SUUIStatefulUIManager enrollInBetaUpdatesProgram:completionHandler:]_block_invoke.455
+ ___70-[SUUIStatefulUIManager enrollInBetaUpdatesProgram:completionHandler:]_block_invoke.460
+ ___70-[SUUIStatefulUIManager enrollInBetaUpdatesProgram:completionHandler:]_block_invoke.461
+ ___70-[SUUIStatefulUIManager enrollInBetaUpdatesProgram:completionHandler:]_block_invoke.462
+ ___70-[SUUIStatefulUIManager enrollInBetaUpdatesProgram:completionHandler:]_block_invoke.464
+ ___75-[SUUIStatefulUIManager refreshBetaUpdates:withRecheckForAvailableUpdates:]_block_invoke.474
+ ___75-[SUUIStatefulUIManager refreshBetaUpdates:withRecheckForAvailableUpdates:]_block_invoke.477
+ ___75-[SUUIStatefulUIManager refreshBetaUpdates:withRecheckForAvailableUpdates:]_block_invoke.478
+ ___75-[SUUIStatefulUIManager refreshBetaUpdates:withRecheckForAvailableUpdates:]_block_invoke.479
+ ___75-[SUUIStatefulUIManager refreshBetaUpdates:withRecheckForAvailableUpdates:]_block_invoke.482
+ ___75-[SUUIStatefulUIManager refreshBetaUpdates:withRecheckForAvailableUpdates:]_block_invoke.483
+ ___75-[SUUIStatefulUIManager refreshBetaUpdates:withRecheckForAvailableUpdates:]_block_invoke_2.484
+ ___77-[SUUIRetryExecutor _executeAttempt:currentDelay:operation:completion:token:]_block_invoke
+ ___77-[SUUIRetryExecutor _executeAttempt:currentDelay:operation:completion:token:]_block_invoke.14
+ ___77-[SUUIStatefulUIManager checkForAvailableUpdatesWithForcedReload:completion:]_block_invoke.386
+ ___80-[SUUIStatefulUIManager checkForUpdatesInBackgroundWithForcedReload:completion:]_block_invoke.394
+ ___81-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:activity:completionHandler:]_block_invoke.535
+ ___81-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:activity:completionHandler:]_block_invoke.537
+ ___81-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:activity:completionHandler:]_block_invoke.538
+ ___81-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:activity:completionHandler:]_block_invoke.539
+ ___81-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:activity:completionHandler:]_block_invoke.540
+ ___81-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:activity:completionHandler:]_block_invoke.545
+ ___81-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:activity:completionHandler:]_block_invoke.546
+ ___81-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:activity:completionHandler:]_block_invoke_2.541
+ ___85-[SUUIBetaUpdatesOperation checkForAvailableBetaProgramsForDevice:completionHandler:]_block_invoke.367
+ ___95-[SUUIStatefulUIManager performPostUpdateOperationRefreshWithDownload:error:completionHandler:]_block_invoke.532
+ ___97-[SUUIStatefulUIManager installUpdate:operationDelegate:delegateCallbackQueue:completionHandler:]_block_invoke.425
+ ___97-[SUUIStatefulUIManager installUpdate:operationDelegate:delegateCallbackQueue:completionHandler:]_block_invoke_2.428
+ ___98-[SUUIStatefulUIManager downloadUpdate:operationDelegate:delegateCallbackQueue:completionHandler:]_block_invoke.399
+ ___98-[SUUIStatefulUIManager downloadUpdate:operationDelegate:delegateCallbackQueue:completionHandler:]_block_invoke_2.402
+ ___98-[SUUIStatefulUIManager scheduleUpdate:operationDelegate:delegateCallbackQueue:completionHandler:]_block_invoke.435
+ ___block_descriptor_64_e8_32s40s48bs_e5_v8?0ls48l8s32l8s40l8
+ ___block_descriptor_88_e8_32s40bs48bs56w_e23_v28?0B812"NSError"20lw56l8s40l8s48l8s32l8
+ ___block_descriptor_88_e8_32s40bs48bs56w_e5_v8?0lw56l8s40l8s48l8s32l8
+ ___block_descriptor_97_e8_32s40s48s56s64bs72bs_e5_v8?0ls32l8s40l8s48l8s64l8s72l8s56l8
+ ___block_literal_global.36
+ ___block_literal_global.38
+ ___block_literal_global.40
+ ___block_literal_global.408
+ ___block_literal_global.415
+ ___block_literal_global.42
+ ___block_literal_global.423
+ ___block_literal_global.433
+ ___block_literal_global.44
+ ___block_literal_global.440
+ ___block_literal_global.450
+ ___block_literal_global.46
+ ___block_literal_global.48
+ ___block_literal_global.50
+ ___block_literal_global.504
+ ___block_literal_global.52
+ ___block_literal_global.54
+ ___block_literal_global.87
+ ___block_literal_global.89
+ ___isOSVersionAtLeast
+ ___isPlatformVersionAtLeast
+ ___os_log_helper_16_2_26_8_32_8_0_8_66_8_66_8_0_8_66_8_0_8_66_8_66_8_66_8_66_8_0_8_66_8_66_8_66_8_66_8_66_8_66_8_0_8_0_8_66_8_0_8_0_8_0_8_0_8_0
+ ___os_log_helper_16_2_3_8_32_8_64_8_0
+ ___os_log_helper_16_2_3_8_32_8_64_8_64
+ ___os_log_helper_16_2_4_8_32_8_64_8_0_8_0
+ ___os_log_helper_16_2_4_8_32_8_64_8_0_8_64
+ ___os_log_helper_16_2_5_8_32_8_64_8_0_8_0_8_0
+ ___swift_async_cont_functlets
+ ___swift_closure_destructor
+ ___swift_closure_destructor.101
+ ___swift_closure_destructor.105
+ ___swift_closure_destructor.109
+ ___swift_closure_destructor.113
+ ___swift_closure_destructor.117
+ ___swift_closure_destructor.121
+ ___swift_closure_destructor.125
+ ___swift_closure_destructor.129
+ ___swift_closure_destructor.133
+ ___swift_closure_destructor.137
+ ___swift_closure_destructor.14
+ ___swift_closure_destructor.140
+ ___swift_closure_destructor.143
+ ___swift_closure_destructor.147
+ ___swift_closure_destructor.151
+ ___swift_closure_destructor.155
+ ___swift_closure_destructor.160
+ ___swift_closure_destructor.163
+ ___swift_closure_destructor.166
+ ___swift_closure_destructor.17
+ ___swift_closure_destructor.170
+ ___swift_closure_destructor.174
+ ___swift_closure_destructor.178
+ ___swift_closure_destructor.182
+ ___swift_closure_destructor.186
+ ___swift_closure_destructor.190
+ ___swift_closure_destructor.194
+ ___swift_closure_destructor.20
+ ___swift_closure_destructor.24
+ ___swift_closure_destructor.27
+ ___swift_closure_destructor.30
+ ___swift_closure_destructor.34
+ ___swift_closure_destructor.38
+ ___swift_closure_destructor.42
+ ___swift_closure_destructor.46
+ ___swift_closure_destructor.49
+ ___swift_closure_destructor.53
+ ___swift_closure_destructor.57
+ ___swift_closure_destructor.61
+ ___swift_closure_destructor.66
+ ___swift_closure_destructor.69
+ ___swift_closure_destructor.72
+ ___swift_closure_destructor.75
+ ___swift_closure_destructor.78
+ ___swift_closure_destructor.81
+ ___swift_closure_destructor.85
+ ___swift_closure_destructor.89
+ ___swift_closure_destructor.93
+ ___swift_closure_destructor.97
+ ___swift_memcpy112_8
+ __availability_version_check
+ __initializeAvailabilityCheck
+ __swiftEmptyDictionarySingleton
+ __swift_FORCE_LOAD_$_swiftCoreLocation
+ __swift_FORCE_LOAD_$_swiftCoreLocation_$_SoftwareUpdateUIFoundation
+ __swift_isClassOrObjCExistentialType
+ _arc4random
+ _associated conformance 26SoftwareUpdateUIFoundation20SUUIDeviceDescriptorV12OSIdentifierVSHAASQ
+ _associated conformance 26SoftwareUpdateUIFoundation20SUUIDeviceDescriptorV12OSIdentifierVs26ExpressibleByStringLiteralAA0iJ4TypesAFP_s01_gh7BuiltiniJ0
+ _associated conformance 26SoftwareUpdateUIFoundation20SUUIDeviceDescriptorV12OSIdentifierVs26ExpressibleByStringLiteralAAs0gh23ExtendedGraphemeClusterJ0
+ _associated conformance 26SoftwareUpdateUIFoundation20SUUIDeviceDescriptorV12OSIdentifierVs33ExpressibleByUnicodeScalarLiteralAA0ijK4TypesAFP_s01_gh7BuiltinijK0
+ _associated conformance 26SoftwareUpdateUIFoundation20SUUIDeviceDescriptorV12OSIdentifierVs43ExpressibleByExtendedGraphemeClusterLiteralAA0ijkL4TypesAFP_s01_gh7BuiltinijkL0
+ _associated conformance 26SoftwareUpdateUIFoundation20SUUIDeviceDescriptorV12OSIdentifierVs43ExpressibleByExtendedGraphemeClusterLiteralAAs0gh13UnicodeScalarL0
+ _associated conformance 26SoftwareUpdateUIFoundation20SUUIDeviceDescriptorV16DeviceCapabilityOSHAASQ
+ _associated conformance 26SoftwareUpdateUIFoundation20SUUIDeviceDescriptorV23ProductFamilyIdentifierVSHAASQ
+ _associated conformance 26SoftwareUpdateUIFoundation20SUUIDeviceDescriptorV23ProductFamilyIdentifierVs26ExpressibleByStringLiteralAA0kL4TypesAFP_s01_ij7BuiltinkL0
+ _associated conformance 26SoftwareUpdateUIFoundation20SUUIDeviceDescriptorV23ProductFamilyIdentifierVs26ExpressibleByStringLiteralAAs0ij23ExtendedGraphemeClusterL0
+ _associated conformance 26SoftwareUpdateUIFoundation20SUUIDeviceDescriptorV23ProductFamilyIdentifierVs33ExpressibleByUnicodeScalarLiteralAA0klM4TypesAFP_s01_ij7BuiltinklM0
+ _associated conformance 26SoftwareUpdateUIFoundation20SUUIDeviceDescriptorV23ProductFamilyIdentifierVs43ExpressibleByExtendedGraphemeClusterLiteralAA0klmN4TypesAFP_s01_ij7BuiltinklmN0
+ _associated conformance 26SoftwareUpdateUIFoundation20SUUIDeviceDescriptorV23ProductFamilyIdentifierVs43ExpressibleByExtendedGraphemeClusterLiteralAAs0ij13UnicodeScalarN0
+ _associated conformance 26SoftwareUpdateUIFoundation20SUUIDeviceDescriptorV4RoleOSHAASQ
+ _associated conformance 26SoftwareUpdateUIFoundation20SUUIDeviceDescriptorVSHAASQ
+ _bridgeLogger.logger
+ _bridgeLogger.loggerOnce
+ _compatibilityInitializeAvailabilityCheck
+ _defaultConfiguration.config
+ _defaultConfiguration.onceToken
+ _dispatch_once_f
+ _dlsym
+ _fclose
+ _fopen
+ _fread
+ _fseek
+ _ftell
+ _initializeAvailabilityCheck
+ _kSUUILoggerKeysBridge
+ _kSUUIRetryConfigurationDefaultJitterRatio
+ _kSUUIRetryConfigurationKeyInitialDelay
+ _kSUUIRetryConfigurationKeyJitterEnabled
+ _kSUUIRetryConfigurationKeyJitterRatio
+ _kSUUIRetryConfigurationKeyMaxAttempts
+ _kSUUIRetryConfigurationKeyMaxDelay
+ _kSUUIRetryConfigurationKeyMultiplier
+ _kSUUIUserDefaultsDocumentationMandatoryUpdateBody
+ _malloc
+ _objc_msgSend$_calculateNextDelay:
+ _objc_msgSend$_completeWithResult:value:error:completion:
+ _objc_msgSend$_executeAttempt:currentDelay:operation:completion:token:
+ _objc_msgSend$_handleAttemptFinished:value:error:attemptNumber:currentDelay:operation:completion:token:
+ _objc_msgSend$decodeBoolForKey:
+ _objc_msgSend$decodeDoubleForKey:
+ _objc_msgSend$documentationMandatoryUpdateBody
+ _objc_msgSend$encodeBool:forKey:
+ _objc_msgSend$encodeDouble:forKey:
+ _objc_msgSend$estimatedTotalTimeout
+ _objc_msgSend$initWithConfiguration:identifier:completionQueue:
+ _objc_msgSend$initWithMaxAttempts:initialDelay:maxDelay:multiplier:jitterEnabled:jitterRatio:
+ _objc_msgSend$initialDelay
+ _objc_msgSend$isCancelled
+ _objc_msgSend$jitterEnabled
+ _objc_msgSend$jitterRatio
+ _objc_msgSend$mandatoryUpdateBodyString
+ _objc_msgSend$maxAttempts
+ _objc_msgSend$maxDelay
+ _objc_msgSend$multiplier
+ _quickConfiguration.config
+ _quickConfiguration.onceToken
+ _rewind
+ _scanWaitConfiguration.config
+ _scanWaitConfiguration.onceToken
+ _sscanf
+ _swift_getEnumCaseMultiPayload
+ _swift_getTupleTypeMetadata2
+ _swift_slowDealloc
+ _swift_storeEnumTagMultiPayload
+ _swift_willThrowTypedImpl
+ _symbolic _____ 26SoftwareUpdateUIFoundation20SUUIDeviceDescriptorV
+ _symbolic _____ 26SoftwareUpdateUIFoundation20SUUIDeviceDescriptorV12OSIdentifierV
+ _symbolic _____ 26SoftwareUpdateUIFoundation20SUUIDeviceDescriptorV16DeviceCapabilityO
+ _symbolic _____ 26SoftwareUpdateUIFoundation20SUUIDeviceDescriptorV23ProductFamilyIdentifierV
+ _symbolic _____ 26SoftwareUpdateUIFoundation20SUUIDeviceDescriptorV4RoleO
+ _type_layout_string 26SoftwareUpdateUIFoundation20SUUIDeviceDescriptorV
+ _type_layout_string 26SoftwareUpdateUIFoundation20SUUIDeviceDescriptorV12OSIdentifierV
- GCC_except_table156
- GCC_except_table159
- GCC_except_table161
- GCC_except_table164
- GCC_except_table169
- GCC_except_table177
- GCC_except_table182
- GCC_except_table188
- GCC_except_table190
- GCC_except_table195
- GCC_except_table205
- GCC_except_table208
- GCC_except_table210
- GCC_except_table218
- GCC_except_table226
- GCC_except_table228
- GCC_except_table231
- GCC_except_table239
- GCC_except_table247
- GCC_except_table250
- GCC_except_table252
- GCC_except_table260
- GCC_except_table263
- GCC_except_table269
- GCC_except_table333
- _MobileGestalt_get_current_device
- _MobileGestalt_get_internalBuild
- _MobileGestalt_get_wapiCapability
- ___100-[SUUIStatefulUIManager doUnenrollFromBetaUpdatesAfterPurgeConfirmation:activity:completionHandler:]_block_invoke.544
- ___100-[SUUIStatefulUIManager doUnenrollFromBetaUpdatesAfterPurgeConfirmation:activity:completionHandler:]_block_invoke.546
- ___100-[SUUIStatefulUIManager doUnenrollFromBetaUpdatesAfterPurgeConfirmation:activity:completionHandler:]_block_invoke.547
- ___100-[SUUIStatefulUIManager doUnenrollFromBetaUpdatesAfterPurgeConfirmation:activity:completionHandler:]_block_invoke.548
- ___102-[SUUIStatefulUIManager downloadAndInstall:operationDelegate:delegateCallbackQueue:completionHandler:]_block_invoke.388
- ___102-[SUUIStatefulUIManager downloadAndInstall:operationDelegate:delegateCallbackQueue:completionHandler:]_block_invoke_2.389
- ___104-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:afterPurgeConfirmation:activity:completionHandler:]_block_invoke.527
- ___104-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:afterPurgeConfirmation:activity:completionHandler:]_block_invoke.529
- ___104-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:afterPurgeConfirmation:activity:completionHandler:]_block_invoke.530
- ___104-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:afterPurgeConfirmation:activity:completionHandler:]_block_invoke.531
- ___108-[SUUIStatefulUIManager promoteTargetedUpdateToUserInitiatedStatus:delegateCallbackQueue:completionHandler:]_block_invoke.421
- ___109-[SUUIStatefulUIManager downloadAndScheduleUpdate:operationDelegate:delegateCallbackQueue:completionHandler:]_block_invoke.396
- ___109-[SUUIStatefulUIManager downloadAndScheduleUpdate:operationDelegate:delegateCallbackQueue:completionHandler:]_block_invoke_2.397
- ___111-[SUUIStatefulUIManager unscheduleTargetedUpdateAutomaticInstallation:delegateCallbackQueue:completionHandler:]_block_invoke.431
- ___165-[SUUIStatefulUIManager performUpdateOnDownloadByApplyingSelector:context:description:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:]_block_invoke.505
- ___165-[SUUIStatefulUIManager performUpdateOnDownloadByApplyingSelector:context:description:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:]_block_invoke.507
- ___165-[SUUIStatefulUIManager performUpdateOnDownloadByApplyingSelector:context:description:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:]_block_invoke.508
- ___165-[SUUIStatefulUIManager performUpdateOnDownloadByApplyingSelector:context:description:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:]_block_invoke.509
- ___165-[SUUIStatefulUIManager performUpdateOnDownloadByApplyingSelector:context:description:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:]_block_invoke.510
- ___187-[SUUIStatefulUIManager performUpdateOperation:withDescriptor:byApplyingSelector:context:auxiliaryOperation:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:]_block_invoke.493
- ___187-[SUUIStatefulUIManager performUpdateOperation:withDescriptor:byApplyingSelector:context:auxiliaryOperation:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:]_block_invoke.495
- ___187-[SUUIStatefulUIManager performUpdateOperation:withDescriptor:byApplyingSelector:context:auxiliaryOperation:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:]_block_invoke.496
- ___187-[SUUIStatefulUIManager performUpdateOperation:withDescriptor:byApplyingSelector:context:auxiliaryOperation:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:]_block_invoke.500
- ___187-[SUUIStatefulUIManager performUpdateOperation:withDescriptor:byApplyingSelector:context:auxiliaryOperation:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:]_block_invoke.501
- ___187-[SUUIStatefulUIManager performUpdateOperation:withDescriptor:byApplyingSelector:context:auxiliaryOperation:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:]_block_invoke.502
- ___187-[SUUIStatefulUIManager performUpdateOperation:withDescriptor:byApplyingSelector:context:auxiliaryOperation:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:]_block_invoke.503
- ___41-[SUUIStatefulUIManager performFullScan:]_block_invoke.479
- ___41-[SUUIStatefulUIManager performFullScan:]_block_invoke.481
- ___41-[SUUIStatefulUIManager performFullScan:]_block_invoke.485
- ___44-[SUUIStatefulUIManager performRefreshScan:]_block_invoke.489
- ___46-[SUUIStatefulUIManager handleFailedFullScan:]_block_invoke.491
- ___59-[SUUIStatefulUIManager refreshStateWithCompletion:forced:]_block_invoke.368
- ___63-[SUUIStatefulUIManager unenrollFromBetaUpdatesWithCompletion:]_block_invoke.446
- ___63-[SUUIStatefulUIManager unenrollFromBetaUpdatesWithCompletion:]_block_invoke.448
- ___63-[SUUIStatefulUIManager unenrollFromBetaUpdatesWithCompletion:]_block_invoke.450
- ___63-[SUUIStatefulUIManager unenrollFromBetaUpdatesWithCompletion:]_block_invoke.452
- ___63-[SUUIStatefulUIManager unenrollFromBetaUpdatesWithCompletion:]_block_invoke_2.451
- ___64-[SUUIStatefulUIManager notifyDelegateOfStateRefreshWithReason:]_block_invoke.566
- ___69-[SUUIStatefulUIManager doUnenrollFromBetaUpdates:completionHandler:]_block_invoke.533
- ___69-[SUUIStatefulUIManager doUnenrollFromBetaUpdates:completionHandler:]_block_invoke.535
- ___69-[SUUIStatefulUIManager doUnenrollFromBetaUpdates:completionHandler:]_block_invoke.536
- ___69-[SUUIStatefulUIManager doUnenrollFromBetaUpdates:completionHandler:]_block_invoke.537
- ___69-[SUUIStatefulUIManager doUnenrollFromBetaUpdates:completionHandler:]_block_invoke.538
- ___69-[SUUIStatefulUIManager doUnenrollFromBetaUpdates:completionHandler:]_block_invoke.542
- ___69-[SUUIStatefulUIManager doUnenrollFromBetaUpdates:completionHandler:]_block_invoke.543
- ___69-[SUUIStatefulUIManager doUnenrollFromBetaUpdates:completionHandler:]_block_invoke_2.539
- ___69-[SUUIStatefulUIManager performFullScanWithScanResults:andScanError:]_block_invoke.487
- ___69-[SUUIStatefulUIManager performFullScanWithScanResults:andScanError:]_block_invoke.488
- ___70-[SUUIStatefulUIManager enrollInBetaUpdatesProgram:completionHandler:]_block_invoke.434
- ___70-[SUUIStatefulUIManager enrollInBetaUpdatesProgram:completionHandler:]_block_invoke.439
- ___70-[SUUIStatefulUIManager enrollInBetaUpdatesProgram:completionHandler:]_block_invoke.440
- ___70-[SUUIStatefulUIManager enrollInBetaUpdatesProgram:completionHandler:]_block_invoke.441
- ___70-[SUUIStatefulUIManager enrollInBetaUpdatesProgram:completionHandler:]_block_invoke.443
- ___75-[SUUIStatefulUIManager refreshBetaUpdates:withRecheckForAvailableUpdates:]_block_invoke.453
- ___75-[SUUIStatefulUIManager refreshBetaUpdates:withRecheckForAvailableUpdates:]_block_invoke.456
- ___75-[SUUIStatefulUIManager refreshBetaUpdates:withRecheckForAvailableUpdates:]_block_invoke.457
- ___75-[SUUIStatefulUIManager refreshBetaUpdates:withRecheckForAvailableUpdates:]_block_invoke.458
- ___75-[SUUIStatefulUIManager refreshBetaUpdates:withRecheckForAvailableUpdates:]_block_invoke.461
- ___75-[SUUIStatefulUIManager refreshBetaUpdates:withRecheckForAvailableUpdates:]_block_invoke.462
- ___75-[SUUIStatefulUIManager refreshBetaUpdates:withRecheckForAvailableUpdates:]_block_invoke_2.463
- ___77-[SUUIStatefulUIManager checkForAvailableUpdatesWithForcedReload:completion:]_block_invoke.365
- ___80-[SUUIStatefulUIManager checkForUpdatesInBackgroundWithForcedReload:completion:]_block_invoke.373
- ___81-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:activity:completionHandler:]_block_invoke.514
- ___81-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:activity:completionHandler:]_block_invoke.516
- ___81-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:activity:completionHandler:]_block_invoke.517
- ___81-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:activity:completionHandler:]_block_invoke.518
- ___81-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:activity:completionHandler:]_block_invoke.519
- ___81-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:activity:completionHandler:]_block_invoke.524
- ___81-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:activity:completionHandler:]_block_invoke.525
- ___81-[SUUIStatefulUIManager doEnrollInBetaUpdatesProgram:activity:completionHandler:]_block_invoke_2.520
- ___85-[SUUIBetaUpdatesOperation checkForAvailableBetaProgramsForDevice:completionHandler:]_block_invoke.346
- ___95-[SUUIStatefulUIManager performPostUpdateOperationRefreshWithDownload:error:completionHandler:]_block_invoke.511
- ___97-[SUUIStatefulUIManager installUpdate:operationDelegate:delegateCallbackQueue:completionHandler:]_block_invoke.404
- ___97-[SUUIStatefulUIManager installUpdate:operationDelegate:delegateCallbackQueue:completionHandler:]_block_invoke_2.407
- ___98-[SUUIStatefulUIManager downloadUpdate:operationDelegate:delegateCallbackQueue:completionHandler:]_block_invoke.378
- ___98-[SUUIStatefulUIManager downloadUpdate:operationDelegate:delegateCallbackQueue:completionHandler:]_block_invoke_2.381
- ___98-[SUUIStatefulUIManager scheduleUpdate:operationDelegate:delegateCallbackQueue:completionHandler:]_block_invoke.414
- ___block_literal_global.33
- ___block_literal_global.35
- ___block_literal_global.37
- ___block_literal_global.387
- ___block_literal_global.39
- ___block_literal_global.394
- ___block_literal_global.402
- ___block_literal_global.41
- ___block_literal_global.412
- ___block_literal_global.419
- ___block_literal_global.429
- ___block_literal_global.43
- ___block_literal_global.45
- ___block_literal_global.47
- ___block_literal_global.483
- ___block_literal_global.49
- __swift_FORCE_LOAD_$_swiftAccelerate
- __swift_FORCE_LOAD_$_swiftAccelerate_$_SoftwareUpdateUIFoundation
- _bzero
- _statfs
- _symbolic _____ So22NSStringCompareOptionsV
- _symbolic _____Sg 10Foundation4DateV
- _symbolic ______A1023At s4Int8V
CStrings:
+ " ("
+ " ["
+ "%d.%d.%d"
+ "%s [%@]: Attempt %lu not finished, scheduling retry in %.2f seconds (next delay: %.2f)"
+ "%s [%@]: Executing attempt %lu of %lu"
+ "%s [%@]: Exhausted all %lu retry attempts"
+ "%s [%@]: Operation aborted on attempt %lu with error: %@"
+ "%s [%@]: Operation cancelled after attempt %lu"
+ "%s [%@]: Operation cancelled before attempt %lu"
+ "%s [%@]: Operation finished on attempt %lu"
+ "%s [%@]: Starting retry operation with configuration: %@"
+ "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tcurrentUpdateOperationType: %{public}@\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nA full-scan operation is currently running (operation: %p). Third-party scan results have arrived. Cancelling the current operation to use the fresh third-party results instead."
+ "): "
+ "): osName: "
+ ", buildVersion: "
+ ", deviceFamilyName: "
+ ", internalBuildCapability: "
+ ", productFamilyName: "
+ ", productVersion: "
+ ", productVersionExtra: "
+ ", rootsInstalledCapability: "
+ ", seedBuildCapability: "
+ ", wapiCapability: "
+ "-[SUUIRetryExecutor _executeAttempt:currentDelay:operation:completion:token:]"
+ "-[SUUIRetryExecutor _executeAttempt:currentDelay:operation:completion:token:]_block_invoke"
+ "-[SUUIRetryExecutor _handleAttemptFinished:value:error:attemptNumber:currentDelay:operation:completion:token:]"
+ "-[SUUIRetryExecutor _handleAttemptFinished:value:error:attemptNumber:currentDelay:operation:completion:token:]_block_invoke"
+ "-[SUUIRetryExecutor executeOperation:completion:]"
+ "/System/Library/CoreServices/SystemVersion.plist"
+ "220d35fc-bc97-422e-8c96-7ea2785548a1"
+ "55b4b4f0-0ecd-4a85-a72f-3e5e6feeac4d"
+ "5f33eae7-f1e0-4811-9713-07dd879f16d5"
+ "63efd5fa-738b-4560-913f-49a55bc873f4"
+ "71b10ce9-15df-40be-bfca-49113fff8fcc"
+ "<%@: %p; cancelled=%{BOOL}d>"
+ "<%@: %p; maxAttempts=%lu, initialDelay=%.1fs, maxDelay=%.1fs, multiplier=%.2f, jitterEnabled=%{BOOL}d, jitterRatio=%.2f, estimatedTimeout=%.1fs>"
+ "<SUUIDeviceDescriptor("
+ "Allocation byte count too large"
+ "Allocation capacity must be greater than or equal to zero"
+ "AllowScanOnBootstrapNetwork"
+ "Bridge"
+ "CFDataCreateWithBytesNoCopy"
+ "CFDictionaryGetValue"
+ "CFGetTypeID"
+ "CFPropertyListCreateFromXMLData"
+ "CFPropertyListCreateWithData"
+ "CFRelease"
+ "CFStringCreateWithCStringNoCopy"
+ "CFStringGetCString"
+ "CFStringGetTypeID"
+ "SUDocumentationMandatoryUpdateBody"
+ "Swift/Bitset.swift"
+ "Swift/BridgeObjectiveC.swift"
+ "Swift/TemporaryAllocation.swift"
+ "The message body for the mandatory update documentation."
+ "UnsafeMutablePointer.update(repeating:count:) with negative count"
+ "]"
+ "allowScanOnBootstrapNetwork"
+ "b9e3c9f6-a252-481e-a9ab-0bd3beeae429"
+ "c1b5ebc2-72ff-44a5-a761-50502d26fc66"
+ "com.apple.SoftwareUpdateUI.RetryExecutor.%@"
+ "completion must not be nil"
+ "configuration must not be nil"
+ "demo-external"
+ "demo-internal"
+ "disabled"
+ "enabled"
+ "fc098402-04dd-45c5-86f8-50e36d846af1"
+ "host"
+ "initialDelay"
+ "initialDelay must be non-negative"
+ "internal"
+ "jitterEnabled"
+ "jitterRatio"
+ "jitterRatio must be between 0.0 and 1.0"
+ "kCFAllocatorNull"
+ "key value "
+ "maxAttempts"
+ "maxAttempts must be greater than 0"
+ "maxDelay"
+ "maxDelay must be >= initialDelay"
+ "multiplier"
+ "multiplier must be >= 1.0"
+ "notSupported"
+ "operation must not be nil"
+ "r"
+ "roots"
+ "sandboxExtensionShortTermLocksKey"
+ "sandboxExtensionShortTermLocksPathKey"
+ "seed"
+ "target"
+ "v28@?0B8@12@\"NSError\"20"
+ "wapi"
- "#16@0:8"
- "(?=\"_heading\"q\"_body\"q)"
- ".cxx_destruct"
- "245326d2-3ddb-4c46-a08e-aab8b6060a1b"
- "85ff7a90-361b-42d1-a420-97dee860f018"
- "97d68e5c-95bb-4136-9aa0-f08964fcc0e1"
- "@\"<SUUIDescriptor>\""
- "@\"<SUUIDocumentation>\""
- "@\"<SUUIDownload>\""
- "@\"<SUUIScanOperation>\""
- "@\"<SUUIStatefulUIEnvironment>\""
- "@\"<SUUIStatefulUIManagerDelegate>\""
- "@\"<SUUIUpdateOperation>\""
- "@\"<SUUIUpdateOperationDelegate>\"16@0:8"
- "@\"NSArray\""
- "@\"NSData\""
- "@\"NSData\"16@0:8"
- "@\"NSDate\"16@0:8"
- "@\"NSDictionary\""
- "@\"NSDictionary\"16@0:8"
- "@\"NSError\""
- "@\"NSMutableArray\""
- "@\"NSMutableDictionary\""
- "@\"NSMutableSet\""
- "@\"NSNumber\"16@0:8"
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSObject<OS_os_log>\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSUserDefaults\""
- "@\"OS_dispatch_queue\"16@0:8"
- "@\"SDBetaManager\""
- "@\"SDBetaProgram\""
- "@\"SDDevice\""
- "@\"SUCoreDDMDeclaration\""
- "@\"SUCoreFSM\""
- "@\"SUUIScanOperationFullScanResults\""
- "@\"SUUIScanOperationScanResults\""
- "@\"SUUIScanResults\""
- "@\"SUUIStatefulDescriptor\""
- "@\"SUUIStatefulError\""
- "@\"SUUIStatefulUIManager\""
- "@\"SUUIUserDefaults\""
- "@\"SUUIUserDefaultsBasedDocumentation\""
- "@152@0:8@16B24B28@32@40B48@52B60B64@68@76@84@92B100Q104B112B116@120@128@136@144"
- "@16@0:8"
- "@20@0:8B16"
- "@20@0:8C16"
- "@24@0:8:16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@24@0:8B16B20"
- "@24@0:8Q16"
- "@24@0:8^{_NSZone=}16"
- "@24@0:8q16"
- "@28@0:8B16@20"
- "@32@0:8:16@24"
- "@32@0:8@16#24"
- "@32@0:8@16@24"
- "@32@0:8@16B24B28"
- "@32@0:8@16Q24"
- "@32@0:8B16B20@24"
- "@32@0:8q16@24"
- "@36@0:8@16@24B32"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@32"
- "@40@0:8@16@24Q32"
- "@40@0:8Q16@24@32"
- "@44@0:8@16@24@32B40"
- "@48@0:8@16@24@32@40"
- "@48@0:8q16@24@32@40"
- "@56@0:8q16@24@32@40Q48"
- "@76@0:8@16B24B28@32@40B48@52B60B64@68"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B24@0:8Q16"
- "B28@0:8@16B24"
- "B32@0:8@16@24"
- "B40@0:8@16@24@32"
- "C"
- "C16@0:8"
- "MarketingDeviceFamilyName"
- "NSCoding"
- "NSCopying"
- "NSObject"
- "NSSecureCoding"
- "OperationsContextGeneration"
- "OperationsResultsAssignment"
- "ProductVersionExtra"
- "Q16@0:8"
- "SUCoreFSMDelegate"
- "SUUIAnalyticsEvent"
- "SUUIAudienceTypeUtilities"
- "SUUIBetaUpdatesOperation"
- "SUUIBetaUpdatesOperationScanOptions"
- "SUUIBetaUpdatesOperationScanResults"
- "SUUICachingFingerprint"
- "SUUICustomDescribleObject"
- "SUUIDocumentation"
- "SUUIDownloadOptions"
- "SUUIDownloadPhaseUtilities"
- "SUUILoggingContext"
- "SUUIMDMSoftwareUpdatePathUtilities"
- "SUUIObjectDescriptionFormatter"
- "SUUIScanOperation"
- "SUUIScanOperationFullScanContext"
- "SUUIScanOperationFullScanResults"
- "SUUIScanOperationRefreshScanContext"
- "SUUIScanOperationScanResults"
- "SUUIScanResults"
- "SUUISoftwareUpdateTypeUtilities"
- "SUUISoftwareUpdateVersionTypeUtilities"
- "SUUIStatefulDescriptor"
- "SUUIStatefulError"
- "SUUIStatefulErrorToken"
- "SUUIStatefulUIManager"
- "SUUIStatefulUIManagerFSMParam"
- "SUUIStatefulUIOperation"
- "SUUIUpdateOperation"
- "SUUIUpdateOperationDownloadAndInstallContext"
- "SUUIUpdateOperationDownloadAndScheduleContext"
- "SUUIUpdateOperationDownloadAndScheduleResults"
- "SUUIUpdateOperationDownloadContext"
- "SUUIUpdateOperationDownloadResults"
- "SUUIUpdateOperationInstallContext"
- "SUUIUpdateOperationInstallResults"
- "SUUIUpdateOperationPurgeContext"
- "SUUIUpdateOperationPurgeResults"
- "SUUIUpdateOperationResults"
- "SUUIUpdateOperationScheduleContext"
- "SUUIUpdateOperationScheduleResults"
- "SUUIUpdateOperationUnscheduleContext"
- "SUUIUpdateOperationUnscheduleResults"
- "SUUIUpdateOperationUserPromotionContext"
- "SUUIUpdateOperationUserPromotionResults"
- "SUUIUserDefaults"
- "SUUIUserDefaultsBasedDocumentation"
- "SUUIUserDefaultsEntry"
- "SUUIUserDefaultsFoundationLoader"
- "SUUIUserDefaultsLoader"
- "SoftwareUpdateUIFoundation/SUUIPlatformEnvironment.swift"
- "T#,R"
- "T@\"<SUUIDescriptor>\",&,V_descriptor"
- "T@\"<SUUIDescriptor>\",R,N,V_alternateDescriptor"
- "T@\"<SUUIDescriptor>\",R,N,V_preferredDescriptor"
- "T@\"<SUUIDescriptor>\",R,V_descriptor"
- "T@\"<SUUIDocumentation>\",R"
- "T@\"<SUUIDownload>\",&"
- "T@\"<SUUIDownload>\",R,N,V_currentDownload"
- "T@\"<SUUIDownload>\",R,N,V_download"
- "T@\"<SUUIDownload>\",R,N,V_previousDownload"
- "T@\"<SUUIErrorTraits>\",R,N,Gtraits"
- "T@\"<SUUIScanOperation>\",&,V_currentFullScanOperation"
- "T@\"<SUUIScanOperation>\",&,V_currentRefreshScanOperation"
- "T@\"<SUUIStatefulUIEnvironment>\",W,N,V_environment"
- "T@\"<SUUIStatefulUIEnvironment>\",W,V_environment"
- "T@\"<SUUIStatefulUIManagerDelegate>\",W,V_delegate"
- "T@\"<SUUIUpdateOperation>\",&,V_currentUpdateOperation"
- "T@\"<SUUIUpdateOperationDelegate>\",R,N"
- "T@\"NSArray\",&,N,V_betaPrograms"
- "T@\"NSArray\",&,V_betaPrograms"
- "T@\"NSArray\",R,V_betaPrograms"
- "T@\"NSData\",R"
- "T@\"NSDictionary\",C,N,V_formatParameters"
- "T@\"NSDictionary\",R,N,V_payload"
- "T@\"NSError\",&,N,V_error"
- "T@\"NSMutableDictionary\",&,N,V_components"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_completionQueue"
- "T@\"NSObject<OS_dispatch_queue>\",&,V_delegateCallbackQueue"
- "T@\"NSObject<OS_os_log>\",R,&,N,V_oslog"
- "T@\"NSString\",&,N,ScomingSoonTipImageSystemName:"
- "T@\"NSString\",&,N,ScomingSoonTipLearnMoreLink:"
- "T@\"NSString\",&,N,ScomingSoonTipMessage:"
- "T@\"NSString\",&,N,ScomingSoonTipTitle:"
- "T@\"NSString\",&,N,SdocumentationLicenseAgreementPath:"
- "T@\"NSString\",&,N,SdocumentationReadMePath:"
- "T@\"NSString\",&,N,SdocumentationReadMeSummaryPath:"
- "T@\"NSString\",&,N,SdocumentationUpdateIconPath:"
- "T@\"NSString\",&,N,V_identifier"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,&,N,V_category"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,C,N"
- "T@\"NSString\",R,N"
- "T@\"NSString\",R,N,V_category"
- "T@\"NSString\",R,N,V_entryDescription"
- "T@\"NSString\",R,N,V_identifier"
- "T@\"NSString\",R,N,V_key"
- "T@\"OS_dispatch_queue\",&"
- "T@\"SDBetaManager\",&,N,V_betaManager"
- "T@\"SDBetaProgram\",&,N,V_enrolledBetaProgram"
- "T@\"SDBetaProgram\",&,V_enrolledBetaProgram"
- "T@\"SDBetaProgram\",R,V_enrolledBetaProgram"
- "T@\"SDDevice\",&,N,V_currentSeedingDevice"
- "T@\"SDDevice\",&,V_currentSeedingDevice"
- "T@\"SDDevice\",R,V_currentSeedingDevice"
- "T@\"SUCoreDDMDeclaration\",&,SsetDDMDeclaration:,V_ddmDeclaration"
- "T@\"SUCoreDDMDeclaration\",R,N,V_ddmDeclaration"
- "T@\"SUCoreFSM\",R,N,V_managerFSM"
- "T@\"SUUIScanOperationFullScanResults\",&,N,V_fullScanResults"
- "T@\"SUUIScanOperationScanResults\",&,N,V_refreshScanResults"
- "T@\"SUUIScanResults\",R,N,V_previousThirdPartyScanResults"
- "T@\"SUUIStatefulDescriptor\",&,V_alternateStatefulDescriptor"
- "T@\"SUUIStatefulDescriptor\",&,V_hiddenAlternateStatefulDescriptor"
- "T@\"SUUIStatefulDescriptor\",&,V_hiddenPreferredStatefulDescriptor"
- "T@\"SUUIStatefulDescriptor\",&,V_preferredStatefulDescriptor"
- "T@\"SUUIStatefulError\",&,N,V_error"
- "T@\"SUUIStatefulError\",&,V_scanError"
- "T@\"SUUIStatefulError\",&,V_updateDownloadError"
- "T@\"SUUIStatefulError\",R,N,V_alternateUpdateDownloadError"
- "T@\"SUUIStatefulError\",R,N,V_preferredUpdateDownloadError"
- "T@\"SUUIStatefulError\",R,N,V_previousEncounteredError"
- "T@\"SUUIStatefulError\",R,N,V_previousScanError"
- "T@\"SUUIStatefulError\",R,N,V_scanError"
- "T@\"SUUIStatefulError\",R,N,V_updateInstallationError"
- "T@\"SUUIStatefulUIManager\",W,V_ownerManager"
- "T@\"SUUIUserDefaults\",R,N"
- "T@\"SUUIUserDefaultsEntry\",R,N"
- "TB,GisClearingSpaceForDownload,V_clearingSpaceForDownload"
- "TB,GisDownloadable,V_updateDownloadable"
- "TB,N,SisNeRDProfileStatusInstalled:"
- "TB,N,SshouldBypassSystemRootWarning:"
- "TB,N,SshouldHideComingSoonTip:"
- "TB,N,SshouldKeepPreviousMockingKitSession:"
- "TB,N,SshouldShowComingSoonTip:"
- "TB,N,SshouldSkipMockingKitPIDValidation:"
- "TB,N,V_forceReload"
- "TB,N,V_forceReloadScanResults"
- "TB,N,V_forceScan"
- "TB,N,V_refreshHasAnyChanges"
- "TB,R"
- "TB,R,GisRollingBackSplatUpdate,V_rollingBackSplatUpdate"
- "TB,R,N"
- "TB,R,N,GisAlternateUpdateDownloadable,V_alternateUpdateDownloadable"
- "TB,R,N,GisAutoUpdateScheduled,V_autoUpdateScheduled"
- "TB,R,N,GisClearingSpaceForDownload,V_clearingSpaceForDownload"
- "TB,R,N,GisDelayingUpdate,V_delayingUpdate"
- "TB,R,N,GisEmptyScanResults,V_emptyScanResults"
- "TB,R,N,GisNotifyUser,V_notifyUser"
- "TB,R,N,GisPreferredUpdateDownloadable,V_preferredUpdateDownloadable"
- "TB,R,N,GisRollingBackSplatUpdate,V_rollingBackSplatUpdate"
- "TB,R,N,GisScheduled,V_scheduled"
- "TB,R,N,GisSuccess,V_success"
- "TB,R,N,GisUpdateReadyForInstallation,V_updateReadyForInstallation"
- "TB,R,N,GisUserRequested,V_userRequested"
- "TB,R,N,V_unattendedPurge"
- "TB,V_allowUnrestrictedCellularDownload"
- "TB,V_canEnrollInBetaUpdates"
- "TB,V_downloadErrorPreventingUpdate"
- "TB,V_downloadOnly"
- "TB,V_hidingAlternateDescriptor"
- "TB,V_hidingPreferredDescriptor"
- "TB,V_isAutoUpdateScheduled"
- "TB,V_userUpdateTonight"
- "TC,N,V_retries"
- "TQ,R"
- "TQ,R,N,V_mdmPathRestrictions"
- "TQ,R,N,V_options"
- "TQ,V_mdmPathRestrictions"
- "TQ,V_role"
- "Tq"
- "Tq,N,V_refreshPreviousState"
- "Tq,N,V_type"
- "Tq,R,N,V_eventType"
- "Tq,R,N,V_type"
- "Tq,V_currentState"
- "Tq,V_currentUpdateOperationType"
- "Tq,V_downloadFeeAgreementStatus"
- "Tq,V_termsAndConditionsAgreementStatus"
- "UTF8String"
- "UUID"
- "UUIDString"
- "Unexpectedly found nil while implicitly unwrapping an Optional value"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_allowUnrestrictedCellularDownload"
- "_alternateDescriptor"
- "_alternateStatefulDescriptor"
- "_alternateUpdateDownloadError"
- "_alternateUpdateDownloadable"
- "_autoUpdateScheduled"
- "_auxiliaryOperations"
- "_betaManager"
- "_betaPrograms"
- "_cachedLicenseAgreement"
- "_cachedReleaseNotes"
- "_cachedReleaseNotesSummary"
- "_cachedUpdateIcon"
- "_canEnrollInBetaUpdates"
- "_category"
- "_clearingSpaceForDownload"
- "_completionQueue"
- "_components"
- "_currentDownload"
- "_currentFullScanOperation"
- "_currentRefreshScanOperation"
- "_currentSeedingDevice"
- "_currentState"
- "_currentUpdateOperation"
- "_currentUpdateOperationType"
- "_ddmDeclaration"
- "_delayingUpdate"
- "_delegate"
- "_delegateCallbackQueue"
- "_descriptor"
- "_didAttemptLicenseAgreementLoad"
- "_didAttemptReleaseNotesLoad"
- "_didAttemptReleaseNotesSummaryLoad"
- "_didAttemptUpdateIconLoad"
- "_discoverAndRegisterLoaders"
- "_download"
- "_downloadErrorPreventingUpdate"
- "_downloadFeeAgreementStatus"
- "_downloadOnly"
- "_emptyScanResults"
- "_enrolledBetaProgram"
- "_entryDescription"
- "_environment"
- "_error"
- "_eventType"
- "_fallbackFingerprint:"
- "_forceReload"
- "_forceReloadScanResults"
- "_forceScan"
- "_formatParameters"
- "_fullScanCompletionCallbacks"
- "_fullScanResults"
- "_generateStateTable"
- "_hashArray:"
- "_hashData:"
- "_hashDictionary:"
- "_hiddenAlternateStatefulDescriptor"
- "_hiddenPreferredStatefulDescriptor"
- "_hidingAlternateDescriptor"
- "_hidingPreferredDescriptor"
- "_identifier"
- "_isAutoUpdateScheduled"
- "_key"
- "_licenseAgreementLock"
- "_lock"
- "_managerFSM"
- "_mdmPathRestrictions"
- "_mutationQueue"
- "_notifyUser"
- "_operationsQueue"
- "_options"
- "_originalDocumentation"
- "_oslog"
- "_overriddenDocumentation"
- "_ownerManager"
- "_payload"
- "_preferredDescriptor"
- "_preferredStatefulDescriptor"
- "_preferredUpdateDownloadError"
- "_preferredUpdateDownloadable"
- "_previousDownload"
- "_previousEncounteredError"
- "_previousScanError"
- "_previousThirdPartyScanResults"
- "_refreshHasAnyChanges"
- "_refreshPreviousState"
- "_refreshScanCompletionCallbacks"
- "_refreshScanResults"
- "_releaseNotesLock"
- "_releaseNotesSummaryLock"
- "_retries"
- "_role"
- "_rollingBackSplatUpdate"
- "_scanError"
- "_scanNotificationLock"
- "_scheduled"
- "_stateTable"
- "_stringValueForObject:"
- "_success"
- "_suiteName"
- "_termsAndConditionsAgreementStatus"
- "_type"
- "_unattendedPurge"
- "_updateDownloadError"
- "_updateDownloadable"
- "_updateIconLock"
- "_updateInstallationError"
- "_updateReadyForInstallation"
- "_userDefaults"
- "_userRequested"
- "_userUpdateTonight"
- "_value"
- "_workQueue"
- "addEntriesFromDictionary:"
- "addObject:"
- "allKeys"
- "allObjects"
- "allocWithZone:"
- "allowUnrestrictedCellularDownload"
- "alternateStatefulDescriptor"
- "analyticsLogger"
- "appendFormat:"
- "appendString:"
- "arrayForEntry:"
- "assignDescriptorOfType:fromSearchResults:"
- "assignDownloadAndScheduleUpdateResults:"
- "assignDownloadUpdateResults:"
- "assignFullScanResults:"
- "assignInstallUpdateResults:"
- "assignScanResults:"
- "assignScheduleUpdateResults:"
- "assignState:"
- "assignState:fromConcreteDownload:downloadable:downloadError:error:"
- "assignState:fromScanResults:withConcreteError:"
- "assignUnscheduleUpdateResults:"
- "assignUserPromotionUpdateResults:"
- "audienceType"
- "autorelease"
- "betaManager"
- "betaUpdatesManagementEnabled"
- "betaUpdatesOperationLogger"
- "betaUpdatesOperationWithManager:identifier:completionQueue:"
- "body"
- "bodyTokenWithStatefulDescriptor:download:"
- "bodyTokenWithType:"
- "bodyTokenWithType:parameters:"
- "boolForEntry:"
- "boolValue"
- "buildError:underlying:description:"
- "bytes"
- "canCurrentDeviceEnrollInBetaUpdates"
- "canEnrollInBetaUpdates"
- "cancel:"
- "cancelCurrentUpdateOperation"
- "category"
- "checkForAvailableBetaPrograms:completionHandler:"
- "checkForAvailableBetaProgramsForDevice:completionHandler:"
- "checkForAvailableBetaProgramsWithCompletionHandler:"
- "checkForAvailableUpdates"
- "checkForAvailableUpdates:"
- "checkForAvailableUpdates:forceScan:"
- "checkForAvailableUpdatesWithCompletion:"
- "checkForAvailableUpdatesWithCompletionHandler:"
- "checkForAvailableUpdatesWithContext:completionHandler:"
- "checkForAvailableUpdatesWithForcedReload:completion:"
- "checkForAvailableUpdatesWithRetriesCount:"
- "checkForUpdatesInBackground"
- "checkForUpdatesInBackground:"
- "checkForUpdatesInBackground:forceScan:"
- "checkForUpdatesInBackgroundWithCompletion:"
- "checkForUpdatesInBackgroundWithForcedReload:completion:"
- "class"
- "clearPastDownload:"
- "clearPastScanResults"
- "clearingSpaceForDownload"
- "code"
- "comingSoonTipImageSystemName"
- "comingSoonTipImageSystemName:"
- "comingSoonTipImageSystemNameEntry"
- "comingSoonTipLearnMoreLink"
- "comingSoonTipLearnMoreLink:"
- "comingSoonTipLearnMoreLinkEntry"
- "comingSoonTipMessage"
- "comingSoonTipMessage:"
- "comingSoonTipMessageEntry"
- "comingSoonTipTitle"
- "comingSoonTipTitle:"
- "comingSoonTipTitleEntry"
- "compare:"
- "compare:options:"
- "completionQueue"
- "componentValueForKey:"
- "components"
- "computeFingerprint"
- "conformsToProtocol:"
- "containsEntry:"
- "containsKey:"
- "contextForDownloadAndInstallUpdateOperation:"
- "contextForDownloadAndScheduleUpdateOperation:"
- "contextForDownloadUpdateOperation:"
- "contextForFullScanOperation:withThirdPartyScanResults:scanError:forceReloadScanResults:"
- "contextForInstallUpdateOperation:"
- "contextForPurgeUpdateOperation:forUserRequestedOperation:notifyUser:"
- "contextForRefreshScanOperation:withPreviouslyDiscoveredDownload:encounteredError:"
- "contextForScheduleUpdateOperation:"
- "contextForUserPromotionUpdateOperation:"
- "contextForUserUnscheduleUpdateOperation:"
- "controllerCurrentlyScanning:"
- "convertFSMStateToUIState:"
- "copy"
- "copyWithZone:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "currentInstalledNeRDInfo"
- "currentUpdateOperationType"
- "darwinup"
- "dataForEntry:"
- "dataWithContentsOfFile:options:error:"
- "dataWithJSONObject:options:error:"
- "dateForEntry:"
- "debugDescription"
- "decodeIntegerForKey:"
- "decodeObjectOfClass:forKey:"
- "decodeObjectOfClasses:forKey:"
- "defaultManager"
- "defaultsForSuiteName:"
- "defaultsToRegister"
- "delegate"
- "delegateCallbackQueue"
- "description"
- "description:"
- "descriptionDictionary"
- "descriptionForObject:"
- "descriptionForObject:options:"
- "descriptionForObject:properties:"
- "descriptionForObject:properties:options:"
- "diag"
- "dictionaryForEntry:"
- "dictionaryWithCapacity:"
- "dictionaryWithObjects:forKeys:count:"
- "didChangeValueForKey:"
- "doEnrollInBetaUpdatesProgram:activity:completionHandler:"
- "doEnrollInBetaUpdatesProgram:afterPurgeConfirmation:activity:completionHandler:"
- "doUnenrollFromBetaUpdates:completionHandler:"
- "doUnenrollFromBetaUpdatesAfterPurgeConfirmation:activity:completionHandler:"
- "documentationLicenseAgreementPath"
- "documentationLicenseAgreementPath:"
- "documentationLicenseAgreementPathEntry"
- "documentationReadMePath"
- "documentationReadMePath:"
- "documentationReadMePathEntry"
- "documentationReadMeSummaryPath"
- "documentationReadMeSummaryPath:"
- "documentationReadMeSummaryPathEntry"
- "documentationUpdateIconPath"
- "documentationUpdateIconPath:"
- "documentationUpdateIconPathEntry"
- "doesTargetedUpdateMatchDescriptor:"
- "doesTargetedUpdateMatchDescriptorRole:"
- "domain"
- "downloadAndInstall:operationDelegate:delegateCallbackQueue:completionHandler:"
- "downloadAndInstallUpdate:withContext:delegate:completionHandler:"
- "downloadAndScheduleUpdate:forInstallationTonightWithContext:delegate:completionHandler:"
- "downloadAndScheduleUpdate:operationDelegate:delegateCallbackQueue:completionHandler:"
- "downloadErrorPreventingUpdate"
- "downloadFeeAgreementStatus"
- "downloadOnly"
- "downloadUpdate:operationDelegate:delegateCallbackQueue:completionHandler:"
- "downloadUpdate:withContext:delegate:completionHandler:"
- "dumpTracked:dumpingTo:usingFilename:clearingStatistics:clearingHistory:"
- "ed5a1c1d-2a39-4993-8bcc-f260c4b42868"
- "encodeInteger:forKey:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "enrollDevice:inBetaProgram:completion:"
- "enrollDevice:inBetaProgram:completionHandler:"
- "enrollInBetaUpdatesProgram:completionHandler:"
- "enrolledBetaProgramForDevice:completion:"
- "entryDescription"
- "entryForKey:"
- "environment"
- "error"
- "errorWithDomain:code:userInfo:"
- "exceptionWithName:reason:userInfo:"
- "executeOperationOnDelegate:usingBlock:"
- "extendedStateQueue"
- "fb333b76-b463-401f-8899-96d82fc4c598"
- "fileExistsAtPath:"
- "fingerprintWithComponents:"
- "firstObject"
- "forceReload"
- "forceReloadScanResults"
- "forceScan"
- "formatParameters"
- "formatValue:withOptions:"
- "fsmAction_CheckForAvailableUpdate:error:"
- "fsmAction_RefreshScanResults:error:"
- "fsmAction_ReportNoUpdateFound:error:"
- "fsmAction_ReportRefreshScanResults:error:"
- "fsmAction_ReportRefreshScanResultsFailed:error:"
- "fsmAction_ReportScanFailed:error:"
- "fsmAction_ReportUpdatesAvailable:error:"
- "fsmAction_actionUnknownAction:error:"
- "fullScanResults"
- "fullUpdateName"
- "getCurrentDevice:"
- "getEnrollInBetaUpdatesStatus"
- "handleFailedFullScan:"
- "handleFullScanResults:"
- "handleRefreshScanResults:"
- "hasAcceptedTermsAndConditionsOfDescriptor:completionHandler:"
- "hasHiddenDescriptors"
- "hasSUPathRestrictions"
- "hasScanResultsCacheWithCompletion:"
- "hash"
- "heading"
- "headingTokenWithStatefulDescriptor:download:"
- "headingTokenWithType:"
- "headingTokenWithType:parameters:"
- "hiddenAlternateStatefulDescriptor"
- "hiddenPreferredStatefulDescriptor"
- "hideAlternateUpdate"
- "hideNonTargetedUpdateDescriptors"
- "hidePreferredUpdate"
- "hidingAlternateDescriptor"
- "hidingPreferredDescriptor"
- "inLockdownMode"
- "init"
- "initAsUserRequest:notifyUser:"
- "initForDescriptor:fromScanResults:managedBy:"
- "initFromError:"
- "initMachine:withTable:startingIn:usingDelegate:registeringAllInfoClass:"
- "initStorageEntryWithType:key:description:category:"
- "initWithArray:copyItems:"
- "initWithBool:"
- "initWithCategory:"
- "initWithCoder:"
- "initWithData:encoding:"
- "initWithDescriptor:"
- "initWithDictionary:copyItems:"
- "initWithDocumentation:"
- "initWithDocumentation:userDefaults:"
- "initWithDomain:code:userInfo:"
- "initWithDouble:"
- "initWithEnvironment:"
- "initWithEventType:"
- "initWithEventType:payload:"
- "initWithFormat:"
- "initWithFormat:arguments:"
- "initWithIdentifier:currentSeedingDevice:betaPrograms:"
- "initWithIdentifier:currentSeedingDevice:betaPrograms:enrolledBetaProgram:"
- "initWithIdentifier:environment:usingBetaManager:withCompletionQueue:"
- "initWithIdentifier:preferredUpdateDownloadable:alternateUpdateDownloadable:preferredUpdateDownloadError:alternateUpdateDownloadError:clearingSpaceForDownload:currentDownload:autoUpdateScheduled:updateReadyForInstallation:updateInstallationError:"
- "initWithIdentifier:preferredUpdateDownloadable:alternateUpdateDownloadable:preferredUpdateDownloadError:alternateUpdateDownloadError:clearingSpaceForDownload:currentDownload:autoUpdateScheduled:updateReadyForInstallation:updateInstallationError:preferredDescriptor:alternateDescriptor:scanError:emptyScanResults:mdmPathRestrictions:delayingUpdate:rollingBack:currentSeedingDevice:betaPrograms:enrolledBetaProgram:ddmDeclaration:"
- "initWithInteger:"
- "initWithInteractionType:"
- "initWithPreferredDescriptor:alternateDescriptor:"
- "initWithPreviousDownload:previousEncounteredError:"
- "initWithPreviousThirdPartyScanResults:previousScanError:forceReloadScanResults:"
- "initWithResult:"
- "initWithResult:andScheduleResult:download:"
- "initWithResult:download:"
- "initWithRetriesCount:"
- "initWithSuiteName:"
- "initWithType:key:description:category:"
- "initWithType:key:description:category:options:"
- "initWithUnattendedPurge:"
- "installUpdate:operationDelegate:delegateCallbackQueue:completionHandler:"
- "installUpdate:withContext:delegate:completionHandler:"
- "installationInProgress"
- "installationInvalidState"
- "installationRequiresKeybagOrPasswordUnlock"
- "intValue"
- "invalidateScanResultsCache:"
- "invocationWithMethodSignature:"
- "invoke"
- "isActive"
- "isAlternateUpdateDownloadable"
- "isAutoDownload"
- "isAutoUpdateScheduled"
- "isBetaEnrollmentDisabledByMDM"
- "isDelayingUpdate"
- "isDone"
- "isDownloadable"
- "isEmptyScanResults"
- "isEqual:"
- "isEqualToDescriptor:"
- "isEqualToDescriptor:includeDocumentationComparison:"
- "isEqualToDictionary:"
- "isEqualToString:"
- "isIntrinsicallyEquivalentToError:withStatefulDescriptor:download:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isNeRDProfileStatusInstalled"
- "isNeRDProfileStatusInstalled:"
- "isNeRDProfileStatusInstalledEntry"
- "isNonBlockingErrorForStatefulDescriptor:download:"
- "isNotifyUser"
- "isPerformingFullScan"
- "isPerformingRefresh"
- "isPerformingUpdate"
- "isPreferredUpdateDownloadable"
- "isPreferredUpdatePromotedAsAlternate"
- "isProxy"
- "isReadableFileAtPath:"
- "isRollingBackSplatUpdate"
- "isScheduled"
- "isStalled"
- "isSuccess"
- "isTargetedUpdateScheduledForAutoInstall"
- "isUninitialized"
- "isUserEditable"
- "isUserRemovable"
- "isUserRequested"
- "isUserVisible"
- "key"
- "latestUpdateStatefulDescriptor"
- "length"
- "licenseAgreement"
- "loadDataFromPath:"
- "localizedDescription"
- "managerFSM"
- "matchesFingerprintString:"
- "methodSignatureForSelector:"
- "mobileLogger"
- "mutableCopy"
- "nerdOperationLogger"
- "nerdOperationWithManager:identifier:completionQueue:"
- "networkUnavailable"
- "new"
- "noUpdateFound"
- "notifyDelegateOfStateRefresh"
- "notifyFullScanResultsDelegates:andError:"
- "notifyRefreshScanResultsDelegates:andError:"
- "null"
- "numberForEntry:"
- "numberWithBool:"
- "numberWithInteger:"
- "numberWithUnsignedInteger:"
- "objectAtIndexedSubscript:"
- "objectForKey:"
- "objectForKey:ofClass:"
- "objectForKeyedSubscript:"
- "operationType"
- "options"
- "oslog"
- "performAction:onEvent:inState:withInfo:nextState:error:"
- "performFullScan:"
- "performFullScanWithScanResults:andScanError:"
- "performPostUpdateOperationRefreshWithDownload:error:completionHandler:"
- "performRefreshScan:"
- "performSelector:"
- "performSelector:onTarget:withObject:withObject:withObject:withObject:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "performUpdateOnDownloadByApplyingSelector:context:description:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:"
- "performUpdateOperation:withDescriptor:byApplyingSelector:context:auxiliaryOperation:delegate:delegateCallbackQueue:resultsValidation:resultsAssignment:completion:"
- "platform"
- "postEvent:"
- "postEvent:endingActivity:"
- "postEvent:withInfo:"
- "postEvent:withInfo:endingActivity:"
- "preferredStatefulDescriptor"
- "previousDownload"
- "previousEncounteredError"
- "previousScanError"
- "previousThirdPartyScanResults"
- "processInfo"
- "productBuildVersion"
- "progress"
- "promoteAlternateUpdate"
- "promoteDownloadToUserInitiated:withContext:delegate:completionHandler:"
- "promoteTargetedUpdateToUserInitiatedStatus:delegateCallbackQueue:completionHandler:"
- "purgeDownload:withContext:delegate:completionHandler:"
- "q16@0:8"
- "q24@0:8@16"
- "q32@0:8@16^@24"
- "q64@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@40@\"NSString\"48^@56"
- "q64@0:8@16@24@32@40@48^@56"
- "queryProgramsForSystemAccountsWithPlatforms:completion:"
- "rapidReturnToService"
- "reactiveUILogger"
- "readScanResultsCacheExpectedTTLValue"
- "refreshBetaUpdates"
- "refreshBetaUpdates:"
- "refreshBetaUpdates:withRecheckForAvailableUpdates:"
- "refreshHasAnyChanges"
- "refreshPreviousState"
- "refreshScanResults"
- "refreshScanResultsWithPreferredUpdate:alternateUpdate:completionHandler:"
- "refreshScanResultsWithPreferredUpdate:alternateUpdate:context:completionHandler:"
- "refreshState"
- "refreshState:"
- "refreshStateWithCompletion:"
- "refreshStateWithCompletion:forced:"
- "registeredDefaults"
- "release"
- "releaseNotes"
- "releaseNotesSummary"
- "removeAllObjects"
- "removeComponentValueForKey:"
- "removeEntry:"
- "removeObject:"
- "removeObjectForKey:"
- "removePersistentDomainForName:"
- "reset"
- "resolveInstallationError:fromConcreteDownload:downloadable:downloadError:error:"
- "respondToTermsAndConditionsOfDescriptor:withResponse:completionHandler:"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "retries"
- "revealHiddenAlteranteUpdate"
- "revealHiddenPreferredUpdate"
- "reverseObjectEnumerator"
- "scanOperationLogger"
- "scanOperationWithManager:identifier:completionQueue:"
- "scanPropertiesForObject:"
- "scanResultsCacheExpectedTTLDuration"
- "scheduleUpdate:forInstallationTonightWithContext:delegate:completionHandler:"
- "scheduleUpdate:operationDelegate:delegateCallbackQueue:completionHandler:"
- "selectDelegateCallbackQueue:"
- "self"
- "setAllowUnrestrictedCellularDownload:"
- "setAlternateStatefulDescriptor:"
- "setArgument:atIndex:"
- "setArray:forEntry:"
- "setBetaManager:"
- "setBetaPrograms:"
- "setBool:forEntry:"
- "setCanEnrollInBetaUpdates:"
- "setClearingSpaceForDownload:"
- "setCompletionQueue:"
- "setComponentValue:forKey:"
- "setComponents:"
- "setCurrentDownload:"
- "setCurrentFullScanOperation:"
- "setCurrentRefreshScanOperation:"
- "setCurrentSeedingDevice:"
- "setCurrentState:"
- "setCurrentUpdateOperation:"
- "setCurrentUpdateOperationType:"
- "setDDMDeclaration:"
- "setData:forEntry:"
- "setDate:forEntry:"
- "setDelegate:"
- "setDelegateCallbackQueue:"
- "setDescriptor:"
- "setDictionary:forEntry:"
- "setDownloadErrorPreventingUpdate:"
- "setDownloadFeeAgreementStatus:"
- "setDownloadOnly:"
- "setEnrolledBetaProgram:"
- "setEnvironment:"
- "setError:"
- "setForceReload:"
- "setForceReloadScanResults:"
- "setForceScan:"
- "setFormatParameters:"
- "setFullScanResults:"
- "setHiddenAlternateStatefulDescriptor:"
- "setHiddenPreferredStatefulDescriptor:"
- "setHidingAlternateDescriptor:"
- "setHidingPreferredDescriptor:"
- "setIdentifier:"
- "setIsAutoUpdateScheduled:"
- "setMdmPathRestrictions:"
- "setNumber:forEntry:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "setOperationType:"
- "setOwnerManager:"
- "setPreferredStatefulDescriptor:"
- "setRefreshHasAnyChanges:"
- "setRefreshPreviousState:"
- "setRefreshScanResults:"
- "setRetries:"
- "setRole:"
- "setScanError:"
- "setSelector:"
- "setString:forEntry:"
- "setTarget:"
- "setTermsAndConditionsAgreementStatus:"
- "setType:"
- "setUpdateDownloadError:"
- "setUpdateDownloadable:"
- "setUserUpdateTonight:"
- "setWithObjects:"
- "setupFSM"
- "sharedCore"
- "sharedDefaults"
- "sharedManager"
- "shouldBypassSystemRootWarning"
- "shouldBypassSystemRootWarning:"
- "shouldBypassSystemRootWarningEntry"
- "shouldEnableUpdateOptionsWithStatefulDescriptor:download:"
- "shouldHideComingSoonTip"
- "shouldHideComingSoonTip:"
- "shouldHideComingSoonTipEntry"
- "shouldKeepPreviousMockingKitSession"
- "shouldKeepPreviousMockingKitSession:"
- "shouldKeepPreviousMockingKitSessionEntry"
- "shouldShowComingSoonTip"
- "shouldShowComingSoonTip:"
- "shouldShowComingSoonTipEntry"
- "shouldSkipMockingKitPIDValidation"
- "shouldSkipMockingKitPIDValidation:"
- "shouldSkipMockingKitPIDValidationEntry"
- "softwareUpdateUILogger"
- "sortedArrayUsingSelector:"
- "statefulErrorWithError:"
- "statefulUILogger"
- "statefulUIManager:descriptor:didTransitionFromDescriptorState:toState:"
- "statefulUIManager:didEnrollDevice:inBetaUpdatesProgram:withError:"
- "statefulUIManager:didFailToInstallUpdateWithDescriptor:error:"
- "statefulUIManager:didFailToScanForUpdatesWithError:"
- "statefulUIManager:didFinishScanningForUpdatesWithResults:"
- "statefulUIManager:didRefreshStateWithReason:"
- "statefulUIManager:didStartDownloadForDescriptor:withDownload:"
- "statefulUIManager:didStartInstallingUpdateWithDescriptor:"
- "statefulUIManager:didTransitionFromUIState:toState:"
- "statefulUIManager:didUnenrollDevice:fromBetaUpdatesProgram:"
- "statefulUIManager:requestPurgeConfirmationOfActiveDownload:toSwitchSelectedBetaProgram:completionHandler:"
- "statefulUIManagerDidRefreshBetaUpdates:"
- "statefulUIManagerDidRefreshState:"
- "stringByAppendingString:"
- "stringForEntry:"
- "stringValue"
- "stringWithCapacity:"
- "stringWithFormat:"
- "stringWithUTF8String:"
- "substringToIndex:"
- "suiteName"
- "superclass"
- "supportsSecureCoding"
- "targetedUpdateForDownload:"
- "targetedUpdateMatchingDescriptor:"
- "targetedUpdateStatefulDescriptor"
- "termsAndConditionsAgreementStatus"
- "timeIntervalSince1970"
- "trackAnomaly:forReason:withResult:withError:"
- "traits"
- "uiKitLogger"
- "unattendedPurge"
- "unenrollDevice:completion:"
- "unenrollDevice:completionHandler:"
- "unenrollFromBetaUpdatesWithCompletion:"
- "unlock"
- "unscheduleTargetedUpdateAutomaticInstallation:delegateCallbackQueue:completionHandler:"
- "unscheduleUpdate:forInstallationTonightWithContext:delegate:completionHandler:"
- "unsignedIntegerValue"
- "updateDescriptorsUsingScanResults:andWithConcreteError:"
- "updateIcon"
- "updateName"
- "updateNeRDVersion"
- "updateNeRDVersionWithOptions:"
- "updateOperationLogger"
- "updateOperationShouldPerformUnattendedPurge:"
- "updateOperationWithManager:identifier:delegateCallbackQueue:completionQueue:"
- "updateReadyForInstallation"
- "updateStateFromConcreteDownload:downloadable:downloadError:isUpdateReadyForInstallation:updateInstallationError:error:"
- "updateStateFromProgressedDownload:"
- "updateStateWithScanResults:andWithConcreteError:"
- "userDefaults"
- "userInfo"
- "userUpdateTonight"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8C16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@\"OS_dispatch_queue\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?@\"SUUIScanOperationFullScanResults\"@\"SUUIStatefulError\">16"
- "v24@0:8@?<v@?@\"SUUIStatefulError\">16"
- "v24@0:8@?<v@?B>16"
- "v24@0:8@?<v@?B@\"SUUIStatefulError\">16"
- "v24@0:8B16B20"
- "v24@0:8Q16"
- "v24@0:8q16"
- "v28@0:8@?16B24"
- "v28@0:8B16@20"
- "v28@0:8B16@?20"
- "v32@0:8:16@?24"
- "v32@0:8@\"<SUUIDescriptor>\"16@?<v@?B@\"SUUIStatefulError\">24"
- "v32@0:8@\"SUUIScanOperationFullScanContext\"16@?<v@?@\"SUUIScanOperationFullScanResults\"@\"SUUIStatefulError\">24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v32@0:8@16^^{suui_activity_s}24"
- "v32@0:8Q16@24"
- "v32@0:8^^{suui_activity_s}16@?24"
- "v40@0:8@\"<SUUIDescriptor>\"16@\"<SUUIDescriptor>\"24@?<v@?@\"SUUIScanOperationScanResults\"@\"SUUIStatefulError\">32"
- "v40@0:8@\"<SUUIDescriptor>\"16q24@?<v@?B@\"SUUIStatefulError\">32"
- "v40@0:8@16@24@?32"
- "v40@0:8@16@24^^{suui_activity_s}32"
- "v40@0:8@16^^{suui_activity_s}24@?32"
- "v40@0:8@16q24@?32"
- "v40@0:8q16@24@32"
- "v40@0:8q16^^{suui_activity_s}24@?32"
- "v48@0:8@\"<SUUIDescriptor>\"16@\"<SUUIDescriptor>\"24@\"SUUIScanOperationRefreshScanContext\"32@?<v@?@\"SUUIScanOperationScanResults\"@\"SUUIStatefulError\">40"
- "v48@0:8@\"<SUUIDescriptor>\"16@\"SUUIUpdateOperationDownloadAndInstallContext\"24@\"<SUUIUpdateOperationDelegate>\"32@?<v@?@\"SUUIUpdateOperationDownloadResults\"@\"SUUIStatefulError\">40"
- "v48@0:8@\"<SUUIDescriptor>\"16@\"SUUIUpdateOperationDownloadAndScheduleContext\"24@\"<SUUIUpdateOperationDelegate>\"32@?<v@?@\"SUUIUpdateOperationDownloadAndScheduleResults\"@\"SUUIStatefulError\">40"
- "v48@0:8@\"<SUUIDescriptor>\"16@\"SUUIUpdateOperationDownloadContext\"24@\"<SUUIUpdateOperationDelegate>\"32@?<v@?@\"SUUIUpdateOperationDownloadResults\"@\"SUUIStatefulError\">40"
- "v48@0:8@\"<SUUIDescriptor>\"16@\"SUUIUpdateOperationInstallContext\"24@\"<SUUIUpdateOperationDelegate>\"32@?<v@?@\"SUUIUpdateOperationInstallResults\"@\"SUUIStatefulError\">40"
- "v48@0:8@\"<SUUIDescriptor>\"16@\"SUUIUpdateOperationScheduleContext\"24@\"<SUUIUpdateOperationDelegate>\"32@?<v@?@\"SUUIUpdateOperationScheduleResults\"@\"SUUIStatefulError\">40"
- "v48@0:8@\"<SUUIDescriptor>\"16@\"SUUIUpdateOperationUnscheduleContext\"24@\"<SUUIUpdateOperationDelegate>\"32@?<v@?@\"SUUIUpdateOperationUnscheduleResults\"@\"SUUIStatefulError\">40"
- "v48@0:8@\"<SUUIDownload>\"16@\"SUUIUpdateOperationPurgeContext\"24@\"<SUUIUpdateOperationDelegate>\"32@?<v@?@\"SUUIUpdateOperationPurgeResults\"@\"SUUIStatefulError\">40"
- "v48@0:8@\"<SUUIDownload>\"16@\"SUUIUpdateOperationUserPromotionContext\"24@\"<SUUIUpdateOperationDelegate>\"32@?<v@?@\"SUUIUpdateOperationUserPromotionResults\"@\"SUUIStatefulError\">40"
- "v48@0:8@16@24@32@?40"
- "v48@0:8@16q24^^{suui_activity_s}32@?40"
- "v52@0:8@16@24B32@36@44"
- "v52@0:8q16@24B32@36@44"
- "v56@0:8@16B24@28B36@40@48"
- "v64@0:8:16@24@32@40@48@56"
- "v80@0:8:16@?24@32@40@48@?56@?64@?72"
- "v92@0:8q16@24:32@?40B48@52@60@?68@?76@?84"
- "valueForKey:"
- "willChangeValueForKey:"
- "zone"
- "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"
- "{os_unfair_recursive_lock_s=\"ourl_lock\"{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}\"ourl_count\"I}"

```
