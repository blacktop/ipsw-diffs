## com.apple.driver.AppleMesaSEPDriver

> `com.apple.driver.AppleMesaSEPDriver`

```diff

-10301.0.0.0.5
-  __TEXT.__const: 0x150 sha256:4d5f28e36746da4a2da9b70bb5a727c3d5fc5ad150e63dd69e909ea865918284
-  __TEXT.__cstring: 0x6443 sha256:b8b7c9de58bc8c578099f9aba9918ce4bcf9861c7617583c305408805958f3e7
-  __TEXT.__os_log: 0x32a9 sha256:a4f32ef3660e4feff930e8243d1e38e5f834d14a95655b05a604aa87c107a505
-  __TEXT_EXEC.__text: 0x30570 sha256:607f280c15e4cf18351c556276a7669f07e80aeae075e7db07d3a632b6dfb5fc
-  __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0xc4 sha256:d9ee06a3473d9ea58b645fe2b70254a4e7f9e5c288ca7ae1ee9874419421a0c9
+10308.0.0.0.0
+  __TEXT.__const: 0x150 sha256:3fc4d0e96be789e888e01f493ac05353109896c52b1426c221ff3522efd15f56
+  __TEXT.__cstring: 0x6b1c sha256:56e857e78b7d9655f1d35c60be86e37024e6cf17b7927a7ff0a8a466da59cacc
+  __TEXT.__os_log: 0x36f7 sha256:2fb6674cc10805712621b5bdd880b80d5a4931ab9348d4c6fde93fafe50f1f16
+  __TEXT_EXEC.__text: 0x31ca0 sha256:7be298a9aa2345130cd6e2c904e0c54d0600db6eb22bebf9cb7cb85b436fc93b
+  __TEXT_EXEC.__auth_stubs: 0x740 sha256:11d65dc2437be5eca9a9cddb3bf3ec2c1593dba20df117fbec44263930676484
+  __DATA.__data: 0xc4 sha256:7b4ed3f64b286a3c33c0cacf0f440c9afb9e6c9dd2b342abd4aca31960033afa
   __DATA.__common: 0x2b0 sha256:334e61fade598d87a35822d34aaa6adec70d9edb5a441ea134552eeb2afd813e
-  __DATA.__bss: 0x19 sha256:61126de1b795b976f3ac878f48e88fa77a87d7308ba57c7642b9e1068403a496
-  __DATA_CONST.__mod_init_func: 0x38 sha256:709f118016283aa84895eb62a628d7e6ef240282c55856458dcff9711f19aae6
-  __DATA_CONST.__mod_term_func: 0x38 sha256:2eb36f198eb03784b2161006f4a1d87f60ba7857990a1dab6921b418f9201c52
-  __DATA_CONST.__const: 0x4678 sha256:50c646a88cc932cf77feacc05289327d53ff81179b55117a41d8bbd251cd5be7
-  __DATA_CONST.__kalloc_type: 0x5c0 sha256:328dcec55a6c880256784c8202ecfb663fdffb9ecf7c431ec0d3163689b70a79
-  __DATA_CONST.__kalloc_var: 0x140 sha256:9dd9cc2a8f3980eb187c29b7ef7b378d0dbb3760d9cb4e5342cfd80d5cba0305
-  __DATA_CONST.__auth_got: 0x3a0 sha256:9d605fecf9f6272a5803ef5b2b8f59f33e26b5520b105c4179fc454f02e1f137
-  __DATA_CONST.__got: 0xc8 sha256:cb657403ef9c14a7e4fc271a8fa18f58118c5b30fc13b730883bd090a83644a0
-  UUID: 4B2ABB04-FB43-3C40-AC91-1E3FE27C0B56
-  Functions: 615
-  Symbols:   1621
-  CStrings:  1012
+  __DATA.__bss: 0x21 sha256:7f9c9e31ac8256ca2f258583df262dbc7d6f68f2a03043d5c99a4ae5a7396ce9
+  __DATA_CONST.__mod_init_func: 0x38 sha256:8a0694946602afd392dd5af2001f74a42622c2f0b628f7d0c1de29e55ffb9fdb
+  __DATA_CONST.__mod_term_func: 0x38 sha256:6c744008b8615f1457620fc408bba923db76dd65d027268c57deda6fc7a2566d
+  __DATA_CONST.__const: 0x46d8 sha256:a62bcc5167be8c328abc1e2176c42e29b1fcae7e8c14a38c95ddd03f05df20be
+  __DATA_CONST.__kalloc_type: 0x5c0 sha256:d3119e743faf7ff7c7ee69f6b7aec7639acd9050c81e7dc8ef8cbfad8fa01532
+  __DATA_CONST.__kalloc_var: 0x140 sha256:4a1aec4c691b73440b9455aab05e6fa8efb827b49ffc767172995c76fbf75645
+  __DATA_CONST.__auth_got: 0x3a0 sha256:bdb4d19c186cc4ed79c95dd6ff916f7aef5053c94abf0ac96b1e02b3ed6a5e81
+  __DATA_CONST.__got: 0xc8 sha256:13e5173bfb4d96aacf9e4c2d61871d93b7f547977d157541f2301ba0b74b6f1d
+  UUID: BCA8DA34-EF8A-381E-A395-4EF5D0C1F01A
+  Functions: 626
+  Symbols:   1657
+  CStrings:  1054
 
Symbols:
+ _ZN18AppleMesaSEPDriver11diagnosticsEPKvmP18IOMemoryDescriptorPj.cold.1
+ _ZN18AppleMesaSEPDriver28changeResetStageToWithResultEN11IOBiometric10ResetStageEim.cold.1
+ _ZN18AppleMesaSEPDriver28changeResetStageToWithResultEN11IOBiometric10ResetStageEim.cold.2
+ __ZN11IOBiometric29CommandGateBasedLockPrimitiveIP20AppleBiometricSensorLNS_8LockTypeE1EE6deinitEv
+ __ZN11IOBiometric29CommandGateBasedLockPrimitiveIP20AppleBiometricSensorLNS_8LockTypeE1EE8_tryLockEv
+ __ZN11IOBiometric29CommandGateBasedLockPrimitiveIP20AppleBiometricSensorLNS_8LockTypeE1EED1Ev
+ __ZN17IOMesaCaptureData4initE11OSSharedPtrIK8OSObjectE
+ __ZN18AppleMesaAccessory10handleOpenEP9IOServicejPv
+ __ZN18AppleMesaAccessory11handleCloseEP9IOServicej
+ __ZN18AppleMesaAccessory13willTerminateEP9IOServicej
+ __ZN18AppleMesaSEPDriver20deferredResetHandlerEP18IOTimerEventSource
+ __ZN18AppleMesaSEPDriver28changeResetStageToWithResultEN11IOBiometric10ResetStageEim
+ __ZN22IOMesaCaptureDataLocal4initE11OSSharedPtrIK20AppleBiometricSensorES0_I6OSDataE
+ __ZN22IOMesaCaptureDataLocal6createE11OSSharedPtrIK20AppleBiometricSensorES0_I6OSDataE
+ __ZNK11IOBiometric29CommandGateBasedLockPrimitiveIP20AppleBiometricSensorLNS_8LockTypeE1EE22_validatePreconditionsEv
+ __ZNK11IOBiometric29CommandGateBasedLockPrimitiveIP20AppleBiometricSensorLNS_8LockTypeE1EE22isGuardedResourceValidEv
+ __ZNK11IOBiometric29CommandGateBasedLockPrimitiveIP20AppleBiometricSensorLNS_8LockTypeE1EE25getGuardedResourceAsConstEv
+ __ZNK18AppleMesaSEPDriver13RecoveryTimes10logSummaryEv
+ __ZZN11IOBiometric29CommandGateBasedLockPrimitiveIP20AppleBiometricSensorLNS_8LockTypeE1EE15lockWithTimeoutEjE11_os_log_fmt_1
+ __ZZN11IOBiometric29CommandGateBasedLockPrimitiveIP20AppleBiometricSensorLNS_8LockTypeE1EE6deinitEvE11_os_log_fmt
+ __ZZN11IOBiometric29CommandGateBasedLockPrimitiveIP20AppleBiometricSensorLNS_8LockTypeE1EE8_tryLockEvE11_os_log_fmt_1
+ __ZZN11IOBiometric29CommandGateBasedLockPrimitiveIP20AppleBiometricSensorLNS_8LockTypeE1EE8_tryLockEvE11_os_log_fmt_2
+ __ZZN11IOBiometric29CommandGateBasedLockPrimitiveIP20AppleBiometricSensorLNS_8LockTypeE1EE8_tryLockEvE11_os_log_fmt_3
+ __ZZN18AppleMesaAccessory10handleOpenEP9IOServicejPvE11_os_log_fmt
+ __ZZN18AppleMesaAccessory10handleOpenEP9IOServicejPvE11_os_log_fmt_0
+ __ZZN18AppleMesaAccessory11handleCloseEP9IOServicejE11_os_log_fmt
+ __ZZN18AppleMesaAccessory11handleCloseEP9IOServicejE11_os_log_fmt_0
+ __ZZN18AppleMesaAccessory21intReportQueueHandlerEP18IOTimerEventSourceE11_os_log_fmt_0
+ __ZZN18AppleMesaAccessory21intReportQueueHandlerEP18IOTimerEventSourceE11_os_log_fmt_1
+ __ZZN18AppleMesaAccessory26fingerDetectTimeoutHandlerEP18IOTimerEventSourceE11_os_log_fmt_2
+ __ZZN18AppleMesaAccessory26fingerDetectTimeoutHandlerEP18IOTimerEventSourceE11_os_log_fmt_3
+ __ZZN18AppleMesaSEPDriver11handleMatchEbP17IOMesaCaptureDatabPbhE21kalloc_type_view_8760
+ __ZZN18AppleMesaSEPDriver11handleMatchEbP17IOMesaCaptureDatabPbhE21kalloc_type_view_9073
+ __ZZN18AppleMesaSEPDriver12RequestResetEON11IOBiometric18SensorResetRequestEE11_os_log_fmt_3
+ __ZZN18AppleMesaSEPDriver12RequestResetEON11IOBiometric18SensorResetRequestEE11_os_log_fmt_4
+ __ZZN18AppleMesaSEPDriver12RequestResetEON11IOBiometric18SensorResetRequestEE21extraRecoveryAttempts
+ __ZZN18AppleMesaSEPDriver16sendEnrollResultEP16enroll_result_v2E21kalloc_type_view_7344
+ __ZZN18AppleMesaSEPDriver16sendEnrollResultEP16enroll_result_v2E21kalloc_type_view_7353
+ __ZZN18AppleMesaSEPDriver19applyPostponedMatchEP24postponed_match_result_tbE22kalloc_type_view_10764
+ __ZZN18AppleMesaSEPDriver19applyPostponedMatchEP24postponed_match_result_tbE22kalloc_type_view_10816
+ __ZZN18AppleMesaSEPDriver20deferredResetHandlerEP18IOTimerEventSourceE11_os_log_fmt
+ __ZZN18AppleMesaSEPDriver20deferredResetHandlerEP18IOTimerEventSourceE11_os_log_fmt_0
+ __ZZN18AppleMesaSEPDriver20deferredResetHandlerEP18IOTimerEventSourceE11_os_log_fmt_1
+ __ZZN18AppleMesaSEPDriver20deferredResetHandlerEP18IOTimerEventSourceE11_os_log_fmt_2
+ __ZZN18AppleMesaSEPDriver26sendTemplateListUpdatedMsgEP25template_update_info_v2_tE21kalloc_type_view_7414
+ __ZZN18AppleMesaSEPDriver26sendTemplateListUpdatedMsgEP25template_update_info_v2_tE21kalloc_type_view_7423
+ __ZZN18AppleMesaSEPDriver28changeResetStageToWithResultEN11IOBiometric10ResetStageEimE11_os_log_fmt
+ __ZZN18AppleMesaSEPDriver28changeResetStageToWithResultEN11IOBiometric10ResetStageEimE11_os_log_fmt_0
+ __ZZN18AppleMesaSEPDriver28changeResetStageToWithResultEN11IOBiometric10ResetStageEimE11_os_log_fmt_1
+ __ZZN18AppleMesaSEPDriver29sendTemplateListNotUpdatedMsgEP17bgops_result_v2_tE21kalloc_type_view_7446
+ __ZZN18AppleMesaSEPDriver29sendTemplateListNotUpdatedMsgEP17bgops_result_v2_tE21kalloc_type_view_7455
+ __ZZN18AppleMesaSEPDriver31sendEnrollProgresWithEnrollInfoEhP20enrollment_info_v2_tE21kalloc_type_view_7314
+ __ZZN18AppleMesaSEPDriver31sendEnrollProgresWithEnrollInfoEhP20enrollment_info_v2_tE21kalloc_type_view_7323
+ __ZZNK18AppleMesaSEPDriver13RecoveryTimes10logSummaryEvE11_os_log_fmt
+ __ZZZN18AppleMesaAccessory14setCommandModeE13MACommandModebU13block_pointerFvibEEUb_E11_os_log_fmt
+ __ZZZN18AppleMesaAccessory15readFingerStateEU13block_pointerFvibEEUb0_E11_os_log_fmt
+ __ZZZZN18AppleMesaAccessory15readFingerStateEU13block_pointerFvibEEUb0_EUb1_E11_os_log_fmt
+ __ZZZZN18AppleMesaAccessory26fingerDetectTimeoutHandlerEP18IOTimerEventSourceEUb2_EUb3_E11_os_log_fmt
+ ____ZN11IOBiometric29CommandGateBasedLockPrimitiveIP20AppleBiometricSensorLNS_8LockTypeE1EE6deinitEv_block_invoke
+ ____ZN18AppleMesaAccessory13willTerminateEP9IOServicej_block_invoke
+ ____ZN18AppleMesaAccessory4stopEP9IOService_block_invoke
+ __block_descriptor_tmp.24
+ __block_descriptor_tmp.25
+ __block_descriptor_tmp.40
+ __block_descriptor_tmp.407
+ __block_descriptor_tmp.420
+ __block_descriptor_tmp.422
+ __block_descriptor_tmp.423
+ __block_descriptor_tmp.48
+ __block_descriptor_tmp.52
+ __block_descriptor_tmp.56
+ __block_descriptor_tmp.60
+ __block_descriptor_tmp.641
+ __block_descriptor_tmp.83
+ __block_descriptor_tmp.86
+ __block_descriptor_tmp.91
+ __block_descriptor_tmp.92
+ _thread_tid
- _OUTLINED_FUNCTION_33
- _ZN18AppleMesaSEPDriver28changeResetStageToWithResultEN11IOBiometric10ResetStageEi.cold.1
- _ZN18AppleMesaSEPDriver28changeResetStageToWithResultEN11IOBiometric10ResetStageEi.cold.2
- __ZN10IOWorkLoop8workLoopEv
- __ZN11IOBiometric29CommandGateBasedLockPrimitiveIP20AppleBiometricSensorLNS_8LockTypeE1EE22isGuardedResourceValidEv
- __ZN11IOBiometric29CommandGateBasedLockPrimitiveIP20AppleBiometricSensorLNS_8LockTypeE1EE25getGuardedResourceAsConstEv
- __ZN17IOMesaCaptureData4initE11OSSharedPtrI8OSObjectE
- __ZN18AppleMesaSEPDriver13RecoveryTimes10logSummaryEv
- __ZN18AppleMesaSEPDriver28changeResetStageToWithResultEN11IOBiometric10ResetStageEi
- __ZN22IOMesaCaptureDataLocal4initE11OSSharedPtrI20AppleBiometricSensorES0_I6OSDataE
- __ZN22IOMesaCaptureDataLocal6createE11OSSharedPtrI20AppleBiometricSensorES0_I6OSDataE
- __ZZN18AppleMesaSEPDriver11handleMatchEbP17IOMesaCaptureDatabPbhE21kalloc_type_view_8652
- __ZZN18AppleMesaSEPDriver11handleMatchEbP17IOMesaCaptureDatabPbhE21kalloc_type_view_8965
- __ZZN18AppleMesaSEPDriver13RecoveryTimes10logSummaryEvE11_os_log_fmt
- __ZZN18AppleMesaSEPDriver16sendEnrollResultEP16enroll_result_v2E21kalloc_type_view_7232
- __ZZN18AppleMesaSEPDriver16sendEnrollResultEP16enroll_result_v2E21kalloc_type_view_7241
- __ZZN18AppleMesaSEPDriver19applyPostponedMatchEP24postponed_match_result_tbE22kalloc_type_view_10653
- __ZZN18AppleMesaSEPDriver19applyPostponedMatchEP24postponed_match_result_tbE22kalloc_type_view_10705
- __ZZN18AppleMesaSEPDriver26sendTemplateListUpdatedMsgEP25template_update_info_v2_tE21kalloc_type_view_7302
- __ZZN18AppleMesaSEPDriver26sendTemplateListUpdatedMsgEP25template_update_info_v2_tE21kalloc_type_view_7311
- __ZZN18AppleMesaSEPDriver28changeResetStageToWithResultEN11IOBiometric10ResetStageEiE11_os_log_fmt
- __ZZN18AppleMesaSEPDriver28changeResetStageToWithResultEN11IOBiometric10ResetStageEiE11_os_log_fmt_0
- __ZZN18AppleMesaSEPDriver28changeResetStageToWithResultEN11IOBiometric10ResetStageEiE11_os_log_fmt_1
- __ZZN18AppleMesaSEPDriver29sendTemplateListNotUpdatedMsgEP17bgops_result_v2_tE21kalloc_type_view_7334
- __ZZN18AppleMesaSEPDriver29sendTemplateListNotUpdatedMsgEP17bgops_result_v2_tE21kalloc_type_view_7343
- __ZZN18AppleMesaSEPDriver31sendEnrollProgresWithEnrollInfoEhP20enrollment_info_v2_tE21kalloc_type_view_7202
- __ZZN18AppleMesaSEPDriver31sendEnrollProgresWithEnrollInfoEhP20enrollment_info_v2_tE21kalloc_type_view_7211
- __ZZZZN18AppleMesaAccessory15readFingerStateEU13block_pointerFvibEEUb_EUb0_E11_os_log_fmt
- __ZZZZN18AppleMesaAccessory26fingerDetectTimeoutHandlerEP18IOTimerEventSourceEUb1_EUb2_E11_os_log_fmt
- __block_descriptor_tmp.26
- __block_descriptor_tmp.35
- __block_descriptor_tmp.39
- __block_descriptor_tmp.403
- __block_descriptor_tmp.416
- __block_descriptor_tmp.418
- __block_descriptor_tmp.419
- __block_descriptor_tmp.47
- __block_descriptor_tmp.69
- __block_descriptor_tmp.72
- __block_descriptor_tmp.78
- __block_descriptor_tmp.79
CStrings:
+ " and a holder still present"
+ "!!! CRITICAL !!! LockGuard destroyed outside its command gate. Lock will remain held until process death."
+ "!!! NULL DEREFERENCE !!! Attempting to dereference null guarded resource pointer!"
+ "!!! NULL DEREFERENCE !!! Attempting to dereference null lock pointer!"
+ "!__c11_atomic_load(&_isCancelled, memory_order_relaxed)"
+ "!__c11_atomic_load(&_isInitialized, memory_order_acquire)"
+ "!_commandGate->onThread()"
+ "!_isTerminating"
+ "%s <- Reset request category: %s\n"
+ "%s <- Retrying deferred reset (category %s)\n"
+ "%s: Lock contended on workloop thread — deferring reset\n"
+ "%s: RecoveryTiming: RequestApproved (%llu) + %dms -> SensorUp (%llu) + %dms -> SessionEstablished (%llu) + %dms -> PatchLoaded (%llu) + %dms -> End (%llu) = Total: %dms after %u attempt(s)\n"
+ "%s: Sensor reset request approved\n"
+ "%s: Sensor reset request approved (workloop fast path)\n"
+ "(_thread != ((thread_t) nullptr)) || (_count == 0)"
+ "(_thread == ((thread_t) nullptr)) || (_count > 0)"
+ "/AppleInternal/Library/BuildRoots/4~CR6iugDuHhwgPiDy-yfRCmWToIhob78o1_60ToM/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/System/Library/Frameworks/Kernel.framework/PrivateHeaders/IOKit/biometric/IOBiometricSynchronization.h"
+ "/AppleInternal/Library/BuildRoots/4~CR6iugDuHhwgPiDy-yfRCmWToIhob78o1_60ToM/Library/Caches/com.apple.xbs/TemporaryDirectory.actPQQ/Sources/Mesa/AppleMesaSEPDriver/AppleMesaSEPDriver/AppleMesaAccessory/AppleMesaAccessory.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CR6iugDuHhwgPiDy-yfRCmWToIhob78o1_60ToM/Library/Caches/com.apple.xbs/TemporaryDirectory.actPQQ/Sources/Mesa/AppleMesaSEPDriver/AppleMesaSEPDriver/AppleMesaAccessory/MesaAccessoryManager.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CR6iugDuHhwgPiDy-yfRCmWToIhob78o1_60ToM/Library/Caches/com.apple.xbs/TemporaryDirectory.actPQQ/Sources/Mesa/AppleMesaSEPDriver/AppleMesaSEPDriver/AppleMesaSEPDriver.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CR6iugDuHhwgPiDy-yfRCmWToIhob78o1_60ToM/Library/Caches/com.apple.xbs/TemporaryDirectory.actPQQ/Sources/Mesa/AppleMesaSEPDriver/AppleMesaSEPDriver/IOMesaLogging.cpp"
+ "121111121222121211212111111111111111111111211211222222221221111111222222222222222222222222222222222221111222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222212222211211121121222221112222122121222222222222222221212222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222221111111111111"
+ "AppleMesaAccessory::%s: Service is being terminated. Skipping execution.\n"
+ "AppleMesaAccessory::%s: Service is being terminated. Skipping handler execution.\n"
+ "AssertMacros: %s (value = 0x%lx), version: Mesa-10308~3331, %s file: %s, line: %d\n"
+ "Attempting to call close() when not being the client that called open()!"
+ "Attempting to open a service that's already opened!"
+ "Attempting to open a service that's being terminated!"
+ "ERROR: %s: Mesa lock could not be safely deinitialized! Lock is being held!\n\n"
+ "ERROR: IOBiometricSynchronization::%s: !!! CRITICAL !!! %s() drain timed out with %u waiter(s)%s. Proceeding with teardown; leaked waiters will fault on access.\n\n"
+ "ERROR: IOBiometricSynchronization::%s: !!! CRITICAL !!! Lock (0x%p) automatic teardown failed: lock held by thread (0x%llx). This is an unrecoverable lifecycle bug.\n\n"
+ "ERROR: IOBiometricSynchronization::%s: !!! CRITICAL !!! Lock (0x%p) deinit: block did not complete (0x%x); dropping state out-of-gate.\n\n"
+ "ERROR: IOBiometricSynchronization::%s: !!! TIMEOUT !!! Thread (0x%llx) timed out waiting for lock (0x%p).\n\n"
+ "ERROR: IOBiometricSynchronization::%s: Invariant violation: Lock (0x%p) deinit: initialized but gate is null. Falling through to recovery.\n\n"
+ "ERROR: IOBiometricSynchronization::%s: Lifecycle violation: Lock (0x%p) destroyed without calling deinit(). Attempting automatic teardown.\n\n"
+ "ERROR: IOBiometricSynchronization::%s: Thread (0x%llx) internal error (0x%x) when acquiring lock (0x%p).\n\n"
+ "Error: Lock was torn down while waiting!"
+ "Error: Trying to lock from the workloop's own thread — this would result in a stall!"
+ "Error: lock is in a cancelled state!"
+ "IOBiometricSynchronization::%s: Deinit called when not initialized: nothing to do.\n"
+ "IOBiometricSynchronization::%s: Thread (0x%llx) acquired free lock (0x%p).\n"
+ "IOBiometricSynchronization::%s: Thread (0x%llx) could not acquire lock (0x%p): held by thread (0x%llx).\n"
+ "IOBiometricSynchronization::%s: Thread (0x%llx) fully released lock (0x%p).\n"
+ "IOBiometricSynchronization::%s: Thread (0x%llx) lock acquisition on lock (0x%p) refused.\n"
+ "IOBiometricSynchronization::%s: Thread (0x%llx) partially unlocked lock (0x%p, new count: %u).\n"
+ "IOBiometricSynchronization::%s: Thread (0x%llx) recursively acquired lock (0x%p, new count: %u).\n"
+ "IOBiometricSynchronization::%s: Thread (0x%llx) refused lock (0x%p): guarded resource invalidated.\n"
+ "IOBiometricSynchronization::%s: Thread (0x%llx) refused lock (0x%p): lock cancelled.\n"
+ "IOBiometricSynchronization::%s: Thread (0x%llx) sleeping on lock (0x%p) (timeout: %ums).\n"
+ "IOBiometricSynchronization::%s: Thread (0x%llx) woken up: wait_result_t (%d).\n"
+ "Invariant Error: Attempting to unlock from a non-lock-holding thread!"
+ "Invariant Error: Command gate is null during unlock!"
+ "Invariant Error: Lock is free but lock count is non-zero!"
+ "Invariant Error: Lock is held but lock count is zero!"
+ "Invariant Error: Lock owner's count is zero; over-unlock detected!"
+ "Invariant Error: Pointer-like resource in an invalidated state must be null!"
+ "Invariant broken! Valid pointer to TrustedAccessory required!"
+ "Invariant: gate null while initialized and not cancelled!"
+ "Precondition failed: caller not on gate!"
+ "Precondition failed: lock is cancelled!"
+ "Precondition failed: lock not initialized!"
+ "__c11_atomic_load(&_isInitialized, memory_order_acquire)"
+ "_deferredResetEventSource"
+ "_drainAcquiredOnGate"
+ "_guardedResource == nullptr"
+ "_lock->_commandGate && _lock->_commandGate->getWorkLoop()->inGate()"
+ "_lock->_guardedResource"
+ "_validatePreconditions"
+ "_validatePreconditions() == kBiometricResultSuccess"
+ "_workLoop->inGate()"
+ "commandGate"
+ "deferredResetHandler"
+ "deinit"
+ "handleClose"
+ "handleOpen"
+ "tryLock"
+ "workloop"
+ "~CommandGateBasedLockPrimitive"
- "!!! WARNING !!! Attempting to dereference null lock pointer!"
- "!_commandGate"
- "%s <- Reset with category %s has been requested!\n"
- "%s: RecoveryTiming: RequestApproved (%llu) + %dms -> SensorUp (%llu) + %dms -> SessionEstablished (%llu) + %dms -> PatchLoaded (%llu) + %dms -> End (%llu) = Total: %dms\n"
- "%s: Sensor reset request has been approved!\n"
- "(_thread != nullptr) || (_count == 0)"
- "(_thread == nullptr) || (_count > 0)"
- "/AppleInternal/Library/BuildRoots/4~CQl3ugCiLabnJhm8pC-jDp7tdhZNAhfrKfESA10/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/System/Library/Frameworks/Kernel.framework/PrivateHeaders/IOKit/biometric/IOBiometricSynchronization.h"
- "/AppleInternal/Library/BuildRoots/4~CQl3ugCiLabnJhm8pC-jDp7tdhZNAhfrKfESA10/Library/Caches/com.apple.xbs/TemporaryDirectory.9exzWy/Sources/Mesa/AppleMesaSEPDriver/AppleMesaSEPDriver/AppleMesaAccessory/AppleMesaAccessory.cpp"
- "/AppleInternal/Library/BuildRoots/4~CQl3ugCiLabnJhm8pC-jDp7tdhZNAhfrKfESA10/Library/Caches/com.apple.xbs/TemporaryDirectory.9exzWy/Sources/Mesa/AppleMesaSEPDriver/AppleMesaSEPDriver/AppleMesaAccessory/MesaAccessoryManager.cpp"
- "/AppleInternal/Library/BuildRoots/4~CQl3ugCiLabnJhm8pC-jDp7tdhZNAhfrKfESA10/Library/Caches/com.apple.xbs/TemporaryDirectory.9exzWy/Sources/Mesa/AppleMesaSEPDriver/AppleMesaSEPDriver/AppleMesaSEPDriver.cpp"
- "/AppleInternal/Library/BuildRoots/4~CQl3ugCiLabnJhm8pC-jDp7tdhZNAhfrKfESA10/Library/Caches/com.apple.xbs/TemporaryDirectory.9exzWy/Sources/Mesa/AppleMesaSEPDriver/AppleMesaSEPDriver/IOMesaLogging.cpp"
- "121111121222121211212111111111111111111111211211222222221221111111222222222222222222222222222222222111122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222221222221112112122222111222212212122222222222222222121222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222111111111111"
- "AssertMacros: %s (value = 0x%lx), version: Mesa-10301.0.0.0.5~671, %s file: %s, line: %d\n"
- "ERROR: IOBiometricSynchronization::%s: !!! TIMEOUT !!! Thread (0x%p) timed out waiting for lock (0x%p) due to lock-holding thread (0x%p).\n\n"
- "ERROR: IOBiometricSynchronization::%s: Thread (0x%p) experienced internal error (0x%x) when waiting for lock (0x%p).\n\n"
- "Error: Attempting to unlock from a non-lock-holding thread!"
- "Error: Trying to get read-only guarded resource when not initialized!"
- "Error: Trying to get read-only guarded resource without holding the gate!"
- "Error: Trying to lock when not initialized!"
- "Error: Trying to lock without holding the gate!"
- "Error: Trying to set lock wait timeout when not initialized!"
- "Error: Trying to set lock wait timeout without holding the gate!"
- "Error: Trying to unlock when not initialized!"
- "Error: Trying to verify guarded resource when not initialized!"
- "Error: Trying to verify guarded resource without holding the gate!"
- "IOBiometricSynchronization::%s: Thread (0x%p) acquired free lock (0x%p).\n"
- "IOBiometricSynchronization::%s: Thread (0x%p) failed to acquire lock. Reason: contention with lock-holding thread (0x%p). Going to sleep with timeout: %ums.\n"
- "IOBiometricSynchronization::%s: Thread (0x%p) fully released lock (0x%p).\n"
- "IOBiometricSynchronization::%s: Thread (0x%p) partially unlocked lock (0x%p, new count: %u).\n"
- "IOBiometricSynchronization::%s: Thread (0x%p) recursively acquired lock (0x%p, new count: %u).\n"
- "IOBiometricSynchronization::%s: Thread (0x%p) woken up: wait_result_t (%d).\n"
- "Implementation error: Lock is free but lock count is non-zero!"
- "Implementation error: Lock is held but lock count is zero!"
- "Implementation error: Lock owner's count is zero or less; over-unlock detected!"
- "close_block_invoke"

```
