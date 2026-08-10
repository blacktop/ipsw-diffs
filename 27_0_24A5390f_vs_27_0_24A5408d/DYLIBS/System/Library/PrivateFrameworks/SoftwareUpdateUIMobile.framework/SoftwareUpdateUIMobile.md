## SoftwareUpdateUIMobile

> `/System/Library/PrivateFrameworks/SoftwareUpdateUIMobile.framework/SoftwareUpdateUIMobile`

### Sections with Same Size but Changed Content

- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`

```diff

-772.0.10.0.0
-  __TEXT.__text: 0x75d1c
-  __TEXT.__objc_methlist: 0x27d4
-  __TEXT.__cstring: 0x4727
-  __TEXT.__oslogstring: 0x77f0
-  __TEXT.__gcc_except_tab: 0x11b4
-  __TEXT.__const: 0x3f0
+772.0.20.0.0
+  __TEXT.__text: 0x7ccc8
+  __TEXT.__objc_methlist: 0x2864
+  __TEXT.__const: 0x450
+  __TEXT.__cstring: 0x4a27
+  __TEXT.__oslogstring: 0x8418
+  __TEXT.__gcc_except_tab: 0x1464
   __TEXT.__constg_swiftt: 0xf0
-  __TEXT.__swift5_typeref: 0x22d
+  __TEXT.__swift5_typeref: 0x235
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_reflstr: 0xe6
   __TEXT.__swift5_fieldmd: 0xb4
   __TEXT.__swift5_assocty: 0x60
   __TEXT.__swift5_proto: 0x18
   __TEXT.__swift5_types: 0xc
-  __TEXT.__swift5_capture: 0x3c0
+  __TEXT.__swift5_capture: 0x3a0
   __TEXT.__swift_as_entry: 0x14
   __TEXT.__swift_as_ret: 0x8
   __TEXT.__swift_as_cont: 0xc
-  __TEXT.__unwind_info: 0xe30
+  __TEXT.__unwind_info: 0xeb0
   __TEXT.__eh_frame: 0x388
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x9330
+  __DATA_CONST.__const: 0x9300
   __DATA_CONST.__objc_classlist: 0x120
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0xd8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1878
+  __DATA_CONST.__objc_selrefs: 0x18f8
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0xd8
-  __DATA_CONST.__got: 0x8e0
-  __AUTH_CONST.__const: 0x988
-  __AUTH_CONST.__cfstring: 0x1fe0
-  __AUTH_CONST.__objc_const: 0x7f30
-  __AUTH_CONST.__auth_got: 0x6d0
+  __DATA_CONST.__got: 0x918
+  __AUTH_CONST.__const: 0x938
+  __AUTH_CONST.__cfstring: 0x2080
+  __AUTH_CONST.__objc_const: 0x7f88
+  __AUTH_CONST.__auth_got: 0x6e0
   __AUTH.__objc_data: 0xc90
   __AUTH.__data: 0x58
-  __DATA.__objc_ivar: 0x214
+  __DATA.__objc_ivar: 0x218
   __DATA.__data: 0xda0
   __DATA.__bss: 0x310
   __DATA.__common: 0x40

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1148
-  Symbols:   2561
-  CStrings:  665
+  Functions: 1160
+  Symbols:   2604
+  CStrings:  693
 
Symbols:
+ +[SUUIUserDefaults(Mobile) scanResultsCacheResponseDelayEntry]
+ -[SUUIMobileScanOperation applyScanResultsCacheResponseDelayIfNeeded]
+ -[SUUIMobileScanOperation hasScanResultsCacheLocalCheckWithCompletion:]
+ -[SUUIMobileScanOperation verifyCacheConsistencyWithController:completion:]
+ -[SUUIMobileStatefulError companionUnreachable]
+ -[SUUIMobileUpdateOperation beginPromotionOperationWithDownload:]
+ -[SUUIMobileUpdateOperation fsmAction_PromoteDownload:error:]
+ -[SUUIMobileUpdateOperation promoteDownloadCompletion]
+ -[SUUIMobileUpdateOperation setPromoteDownloadCompletion:]
+ -[SUUIUserDefaults(Mobile) scanResultsCacheResponseDelay:]
+ -[SUUIUserDefaults(Mobile) scanResultsCacheResponseDelay]
+ GCC_except_table111
+ GCC_except_table113
+ GCC_except_table115
+ GCC_except_table125
+ GCC_except_table32
+ GCC_except_table35
+ GCC_except_table40
+ GCC_except_table45
+ GCC_except_table55
+ GCC_except_table62
+ GCC_except_table67
+ GCC_except_table74
+ GCC_except_table76
+ GCC_except_table77
+ GCC_except_table82
+ GCC_except_table86
+ GCC_except_table87
+ _MA_PALLAS_AUDIENCE_RELEASE_ALIGNED_SEED_STAGING_EXT_PRERELEASE
+ _OBJC_CLASS_$_NSThread
+ _OBJC_IVAR_$_SUUIMobileUpdateOperation._promoteDownloadCompletion
+ _SoftwareUpdateUIMobileVersionNumber
+ _SoftwareUpdateUIMobileVersionString
+ ___61-[SUUIMobileScanOperation hasScanResultsCacheWithCompletion:]_block_invoke
+ ___61-[SUUIMobileUpdateOperation fsmAction_PromoteDownload:error:]_block_invoke
+ ___74-[SUUIMobileStatefulUIManager client:installTonightScheduled:operationID:]_block_invoke
+ ___75-[SUUIMobileScanOperation verifyCacheConsistencyWithController:completion:]_block_invoke
+ ___block_descriptor_40_e8_32bs_e30_v20?0B8"SUUIStatefulError"12ls32l8
+ ___block_descriptor_41_e8_32bs_e5_v8?0ls32l8
+ ___block_descriptor_48_e8_32w_e44_v24?0"SUAutoInstallOperation"8"NSError"16lw32l8
+ ___block_descriptor_56_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_65_e8_32s40s48s56r_e5_v8?0ls32l8s40l8r56l8s48l8
+ ___block_descriptor_72_e8_32s40s48r56w_e8_v12?0B8lw56l8s32l8r48l8s40l8
+ ___block_descriptor_80_e8_32s40s48s56bs64w_e35_v24?0"SUScanResults"8"NSError"16lw64l8s32l8s56l8s40l8s48l8
+ ___os_log_helper_16_2_5_8_32_8_66_8_66_8_0_8_66
+ ___os_log_helper_16_2_5_8_32_8_66_8_66_8_34_8_66
+ ___os_log_helper_16_2_6_8_32_8_66_8_66_4_0_8_66_8_66
+ ___os_log_helper_16_2_6_8_32_8_66_8_66_8_66_8_66_8_66
+ _kSUUIUserDefaultsScanResultsCacheResponseDelay
+ _kSU_A_PromoteDownload
+ _kSU_E_BeginPromoteDownload
+ _kSU_E_PromoteDownloadFailed
+ _kSU_E_PromoteDownloadSuccess
+ _kSU_E_UpdateOpPromoteToUserInitiated
+ _kSU_S_PromotingDownload
+ _objc_msgSend$applyScanResultsCacheResponseDelayIfNeeded
+ _objc_msgSend$beginPromotionOperationWithDownload:
+ _objc_msgSend$clientCompletionQueue
+ _objc_msgSend$descriptors:
+ _objc_msgSend$doubleValue
+ _objc_msgSend$fsmAction_PromoteDownload:error:
+ _objc_msgSend$hasScanResultsCacheLocalCheckWithCompletion:
+ _objc_msgSend$notifyDelegateOfStateRefreshWithReason:
+ _objc_msgSend$queryProgramsForSystemAccountsWithPlatforms:retryConfiguration:identifier:completion:
+ _objc_msgSend$quickConfiguration
+ _objc_msgSend$scanResultsCacheResponseDelay
+ _objc_msgSend$sleepForTimeInterval:
+ _objc_msgSend$verifyCacheConsistencyWithController:completion:
+ _objc_setProperty_atomic_copy
+ _symbolic _____Sg 26SoftwareUpdateUIFoundation20SUUIDeviceDescriptorV12OSIdentifierV
- GCC_except_table24
- GCC_except_table27
- GCC_except_table31
- GCC_except_table33
- GCC_except_table36
- GCC_except_table44
- GCC_except_table61
- GCC_except_table63
- GCC_except_table69
- GCC_except_table71
- GCC_except_table81
- GCC_except_table84
- _MA_PALLAS_AUDIENCE_CUSTOMER_SEASHIP
- _MA_PALLAS_AUDIENCE_INTERNAL_SEASHIP
- ___99-[SUUIMobileUpdateOperation promoteDownloadToUserInitiated:withContext:delegate:completionHandler:]_block_invoke
- ___block_descriptor_48_e8_32s40bs_e20_v20?0B8"NSError"12ls40l8s32l8
- ___os_log_helper_16_2_1_8_64
- ___os_log_helper_16_2_2_8_32_8_64
- ___os_log_helper_16_2_3_8_32_8_0_8_64
- ___os_log_helper_16_2_4_8_32_8_66_8_66_8_64
- ___os_log_helper_16_2_5_8_32_8_66_8_66_8_0_8_64
- ___os_log_helper_16_2_5_8_32_8_66_8_66_8_32_8_66
- ___os_log_helper_16_2_5_8_32_8_66_8_66_8_64_8_66
- ___os_log_helper_16_2_5_8_32_8_66_8_66_8_66_8_64
- ___os_log_helper_16_2_6_8_32_8_66_8_66_4_0_8_66_8_64
- ___os_log_helper_16_2_6_8_32_8_66_8_66_8_64_8_0_8_66
- _objc_msgSend$queryProgramsForSystemAccountsWithPlatforms:completion:
CStrings:
+ " [Automation Mode]"
+ "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tcurrentUpdateOperationType: %{public}@\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nCould not fetch the scheduled auto-install operation (error: %{public}@); falling back to refreshState."
+ "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tcurrentUpdateOperationType: %{public}@\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\nCould not resolve the targeted update from the current download. Skipping on the downloadDidFinish event and performing a new scan instead."
+ "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tcurrentUpdateOperationType: %{public}@\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\ninstallTonightScheduled: scheduled=%{public}@ operationID=%{public}@ — updating auto-install state directly, skipping refreshState"
+ "%s [%p]: Error: %{public}@"
+ "%s [%{public}@|%{public}@]: Cache inconsistent with controller — invalidating and performing full scan"
+ "%s [%{public}@|%{public}@]: Cancel has been requested. Skipping on %{public}@"
+ "%s [%{public}@|%{public}@]: Found path restriction: %{public}@ (%ld); error: %{public}@"
+ "%s [%{public}@|%{public}@]: Got the device available Beta Programs (count: %ld): %{public}@"
+ "%s [%{public}@|%{public}@]: Is rolling back? %d; error: %{public}@; rollback descriptor: %{public}@"
+ "%s [%{public}@|%{public}@]: Refreshed current beta program: %{public}@ (program ID: %{public}@"
+ "%s [%{public}@|%{public}@]: Reporting a %{public}s scan of type: %{public}@"
+ "%s [%{public}@|%{public}@]: Simulating a %.1fs cached scan-results response delay (SUScanResultsCacheResponseDelay)."
+ "%s [%{public}@|%{public}@]: error: %{public}@; eligible rollback descriptor: %{public}@"
+ "%s [%{public}@|%{public}@]: verifyCacheConsistencyWithController: cached state — preferredDescriptor: %{public}@, alternateDescriptor: %{public}@"
+ "%s [%{public}@|%{public}@]: verifyCacheConsistencyWithController: caching not supported (returning consistent — nothing to invalidate)"
+ "%s [%{public}@|%{public}@]: verifyCacheConsistencyWithController: controller call failed (returning inconsistent — forcing fresh scan): %{public}@"
+ "%s [%{public}@|%{public}@]: verifyCacheConsistencyWithController: controller state — preferredDescriptor: %{public}@, alternateDescriptor: %{public}@"
+ "%s [%{public}@|%{public}@]: verifyCacheConsistencyWithController: preferred matches: %{public}@, alternate matches: %{public}@, cache is %{public}@ consistent with controller"
+ "%s [%{public}@|%{public}@]: verifyCacheConsistencyWithController: starting consistency check with controller"
+ "%s [->%{public}@]: Can not promote a nil download to user-initiated."
+ "%s [->%{public}@]: The promotion attempt has failed but there's no error assigned to it. result: %{BOOL}d; updateError: %{public}@"
+ "%s [->%{public}@]: User-Promotion result: %{BOOL}d; error: %{public}@"
+ "%s: Can not perform the promotion operation: The class delegate must not be nil."
+ "%s: Polling aborted with error: %{public}@"
+ "(nil)"
+ "-[SUUIMobileScanOperation applyScanResultsCacheResponseDelayIfNeeded]"
+ "-[SUUIMobileScanOperation hasScanResultsCacheLocalCheckWithCompletion:]"
+ "-[SUUIMobileScanOperation verifyCacheConsistencyWithController:completion:]"
+ "-[SUUIMobileScanOperation verifyCacheConsistencyWithController:completion:]_block_invoke"
+ "-[SUUIMobileScanOperation verifyCacheConsistencyWithController:completion:]_block_invoke_2"
+ "-[SUUIMobileStatefulUIManager client:installTonightScheduled:operationID:]_block_invoke"
+ "-[SUUIMobileUpdateOperation beginPromotionOperationWithDownload:]"
+ "-[SUUIMobileUpdateOperation fsmAction_PromoteDownload:error:]"
+ "-[SUUIMobileUpdateOperation fsmAction_PromoteDownload:error:]_block_invoke"
+ "11"
+ "165413ff-a1b0-4e64-b0a0-25ca4fa99e4a"
+ "A delay, in seconds, applied while loading cached scan results (simulates a slow cached-scan response). 0/nil = no delay."
+ "Failed to copyRegistrationStatus from CoreTelephony. %{public}@"
+ "Failed to get preferred CTXPCServiceSubscriptionContext. %{public}@"
+ "Ignoring downloadDidFinish for SPLAT-only update \"%{public}@\": owned by BSI, not triggering a scan."
+ "Ignoring downloadDidStart for SPLAT-only update \"%{public}@\": owned by BSI, not triggering a scan."
+ "Mobile Platform Environment initialized successfully%{public}s\nHost Device: %{public}s\nTarget Device: %{public}s\nEffective Policy: %{public}s\nStatefulUI Environment: %{public}s 0x%{public}s (%{public}s)"
+ "Mobile automation state changed to %{bool,public}d"
+ "SUScanResultsCacheResponseDelay"
+ "SUUIMobilePlatformEnvironment.create: Creating environment for identifier '%{public}s'"
+ "The machine is currently in a middle of a scan."
+ "download.descriptor"
+ "in"
+ "queryRootsInstalledCapability: rooted from darwinup snapshot %{public}s"
+ "queryRootsInstalledCapability: statfs(\"/\") failed with errno: %{public}d"
+ "v20@?0B8@\"SUUIStatefulError\"12"
- "$+"
- "%s [%p]: %{public}@ Checkpoint\n\tcurrentState: %{public}@ (%ld)\n\tdelegate: %{public}@ (%p)\n\tscanError: %{public}@\n\tpreferredDescriptor: %{public}@\n\talternateDescriptor: %{public}@\n\tdownload: %{public}@ (%p)\n\tcurrentUpdateOperationType: %{public}@\n\tscheduledForAutoInstall: %{public}@\n\thiddenUpdatesPostSelection: preferred[%{public}@, %{public}@]; alternate[%{public}@, %{public}@];\n\tselectedBetaProgram: %lu (count: %ld, enrollable: %{public}@)\n\tOpFSMs: scan[%p]; refresh[%p]; update[%p]; auxiliaryOperationsCount[%lu]\n\ninstallTonightScheduled called, start to refresh state"
- "%s [%p]: Error: %@"
- "%s [%{public}@|%{public}@]: Cancel has been requested. Skipping on %@"
- "%s [%{public}@|%{public}@]: Found path restriction: %@ (%ld); error: %{public}@"
- "%s [%{public}@|%{public}@]: Got the device available Beta Programs (count: %ld): %@"
- "%s [%{public}@|%{public}@]: Is rolling back? %d; error: %{public}@; rollback descriptor: %@"
- "%s [%{public}@|%{public}@]: Refreshed current beta program: %@ (program ID: %{public}@"
- "%s [%{public}@|%{public}@]: Reporting a %s scan of type: %{public}@"
- "%s [%{public}@|%{public}@]: error: %{public}@; eligible rollback descriptor: %@"
- "%s: Polling aborted with error: %@"
- "%s: User-Promotion result: %{public}@; error: %{public}@"
- "-[SUUIMobileScanOperation hasScanResultsCacheWithCompletion:]"
- "-[SUUIMobileUpdateOperation promoteDownloadToUserInitiated:withContext:delegate:completionHandler:]_block_invoke"
- "Failed to copyRegistrationStatus from CoreTelephony. %@"
- "Failed to get preferred CTXPCServiceSubscriptionContext. %@"
- "Mobile Platform Environment initialized successfully\nHost Device: %s\nTarget Device: %s\nEffective Policy: %s\nStatefulUI Environment: %s 0x%s (%s)\nAutomation Mode: %{bool}d"
- "Mobile automation state changed to %{bool}d"
- "SUUIMobilePlatformEnvironment.create: Creating environment for identifier '%s'"
- "cd060049-2465-43e3-bbb5-d769a66da2d7"
- "ffc25f86-b83c-4139-b8ad-91131d0e5429"
- "q"
- "queryRootsInstalledCapability: rooted from darwinup snapshot %s"
- "queryRootsInstalledCapability: statfs(\"/\") failed with errno: %d"
```
