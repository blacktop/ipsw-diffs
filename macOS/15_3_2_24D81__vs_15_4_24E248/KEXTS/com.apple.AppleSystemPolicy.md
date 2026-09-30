## com.apple.AppleSystemPolicy

> `com.apple.AppleSystemPolicy`

```diff

-620.81.1.0.0
-  __TEXT.__const: 0x230
-  __TEXT.__cstring: 0x2050
+620.100.82.0.0
+  __TEXT.__const: 0x208
+  __TEXT.__cstring: 0x2063
   __TEXT.__os_log: 0x711
-  __TEXT_EXEC.__text: 0xc47c
+  __TEXT_EXEC.__text: 0xc7fc
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x858
   __DATA.__common: 0x1aa
   __DATA.__bss: 0x74
   __DATA_CONST.__auth_got: 0x490
-  __DATA_CONST.__got: 0x78
-  __DATA_CONST.__auth_ptr: 0x8
+  __DATA_CONST.__got: 0x70
+  __DATA_CONST.__auth_ptr: 0x10
   __DATA_CONST.__mod_init_func: 0x10
   __DATA_CONST.__mod_term_func: 0x10
   __DATA_CONST.__const: 0x19e8
   __DATA_CONST.__kalloc_type: 0x180
-  UUID: 6AC2AC45-1672-39BB-8227-703AAD8E49F6
-  Functions: 294
-  Symbols:   927
-  CStrings:  273
+  UUID: B0FEEE8A-6CB1-3B6A-8E6B-3B33E1B769E1
+  Functions: 293
+  Symbols:   926
+  CStrings:  274
 
Symbols:
+ ___ZN17AppleSystemPolicy16checkLibraryLoadEP14ASPProcessInfoP14ASPLibraryInfoxmb_block_invoke.89
+ ___ZN17AppleSystemPolicy22procNotifyExecCompleteEP4proc_block_invoke.65
+ __block_descriptor_tmp.66
+ __block_descriptor_tmp.84
+ __block_descriptor_tmp.90
+ __block_literal_global.92
- _ZN21NVRAMRecoveryBootMode15registerContentEb.cold.1
- ___ZN17AppleSystemPolicy16checkLibraryLoadEP14ASPProcessInfoP14ASPLibraryInfoxmb_block_invoke.88
- ___ZN17AppleSystemPolicy22procNotifyExecCompleteEP4proc_block_invoke.64
- __block_descriptor_tmp.65
- __block_descriptor_tmp.83
- __block_descriptor_tmp.89
- __block_literal_global.91
Functions:
~ __ZN17ASPEvaluationInfo16is_sip_protectedEv : 380 -> 376
~ _end_timer : 112 -> 128
~ __Z33consult_in_kernel_cache_for_vnodeP5vnodeP18evaluation_results : 344 -> 348
~ __ZL23vnode_has_cached_resultP5vnodeP18evaluation_results : 296 -> 300
~ __Z29record_result_in_kernel_cacheP5vnodeS0_P18evaluation_results : 560 -> 556
~ __Z20binarySearchCdhashesPK29syspolicyd_blocked_hash_entryyPKhh : 180 -> 184
~ __Z17binarySearchTeamsPK29syspolicyd_blocked_team_entryyPKc : 148 -> 164
~ __ZN13ASPVnodeCache20setEvaluationResultsEP5vnodeP18evaluation_results : 340 -> 356
~ ____ZN13ASPVnodeCache20setEvaluationResultsEP5vnodeP18evaluation_results_block_invoke : 152 -> 168
~ ____ZN13ASPVnodeCache20getEvaluationResultsEP5vnodeP18evaluation_results_block_invoke : 152 -> 168
~ __ZN13ASPVnodeCache21setDeveloperToolStateEP5vnodei : 320 -> 336
~ ____ZN13ASPVnodeCache17getProvenanceDataEP5vnodeP18TrackingAttributes_block_invoke : 64 -> 68
~ ____ZN13ASPVnodeCache17setProvenanceDataEP5vnodeP18TrackingAttributes_block_invoke : 88 -> 84
~ __ZN14ASPProcessInfoC2EP4proci : 112 -> 128
~ __ZN14ASPProcessInfo3pidEv : 68 -> 64
~ __ZN14ASPProcessInfo13cdhash_bufferEv : 120 -> 124
~ __ZN14ASPProcessInfo19responsible_processEv : 88 -> 92
~ __ZN21NVRAMRecoveryBootMode15registerContentEb : 944 -> 948
~ __ZN20ASPEvaluationManager20addEvaluationRequestEP21syspolicyd_evaluation : 160 -> 156
~ __ZN20ASPEvaluationManager23removeEvaluationRequestEP21syspolicyd_evaluation : 176 -> 168
~ __ZN20ASPEvaluationManager16waitOnEvaluationEP21syspolicyd_evaluation : 180 -> 196
~ __ZN27AppleSystemPolicyUserClient14externalMethodEjP25IOExternalMethodArgumentsP24IOExternalMethodDispatchP8OSObjectPv : 140 -> 152
~ __ZN27AppleSystemPolicyUserClient12getVnodeInfoEP8OSObjectPvP25IOExternalMethodArguments : 524 -> 532
~ __ZN27AppleSystemPolicyUserClient12setVnodeInfoEP8OSObjectPvP25IOExternalMethodArguments : 404 -> 412
~ __ZN16ASPBastionFilter17getMatchesForRuleEyP26syspolicyd_meta_rules_infoy : 160 -> 156
~ __ZN14ASPLibraryInfoC2EP8fileglobx : 88 -> 96
~ __ZN14ASPLibraryInfo13cdhash_bufferEv : 96 -> 100
~ __ZN17AppleSystemPolicyC2EPK11OSMetaClass : 672 -> 680
~ __ZN17AppleSystemPolicyC2Ev : 708 -> 716
~ __Z34asp_bastion_sandbox_event_callbackPKcP4procP5ucred : 624 -> 644
~ __ZN17AppleSystemPolicy33perform_malware_scan_if_necessaryEP14ASPProcessInfoP17ASPEvaluationInfoiP8ScanMetaPijiPx : 936 -> 924
~ __ZN17AppleSystemPolicy17waitForEvaluationEP21syspolicyd_evaluationiP17ASPEvaluationInfoPP5vnodeP18evaluation_resultsPxPKc : 712 -> 704
~ __ZN17AppleSystemPolicy19credLabelAssociatedEP5ucredS1_ : 208 -> 216
~ __ZN17AppleSystemPolicy21credLabelUpdateExecveEP5ucredS1_P4procP5vnodexS5_P5labelS7_S7_PjPvmPi : 276 -> 284
~ __ZN17AppleSystemPolicy13doExecLoggingEP14ASPProcessInfo : 428 -> 580
~ __ZN17AppleSystemPolicy19blockRevokedProcessEP14ASPProcessInfo : 480 -> 500
~ __ZN17AppleSystemPolicy19blockRevokedLibraryEP14ASPProcessInfoP14ASPLibraryInfoPPKc : 524 -> 544
~ __ZN17AppleSystemPolicy14evaluateScriptEP14ASPProcessInfoP13ASPScriptInfo : 2332 -> 2400
~ __ZN17AppleSystemPolicy22procNotifyExecCompleteEP4proc : 3916 -> 3976
~ __ZL23parent_process_action_bP4procU13block_pointerFvR14ASPProcessInfoE : 180 -> 184
~ ____ZN17AppleSystemPolicy22procNotifyExecCompleteEP4proc_block_invoke : 172 -> 192
~ __ZN17AppleSystemPolicy16checkLibraryLoadEP14ASPProcessInfoP14ASPLibraryInfoxmb : 3568 -> 3556
~ ____ZN17AppleSystemPolicy16checkLibraryLoadEP14ASPProcessInfoP14ASPLibraryInfoxmb_block_invoke : 172 -> 192
~ __ZN17AppleSystemPolicy26fileCheckLibraryValidationEP4procP8fileglobxxm : 280 -> 288
~ __ZN17AppleSystemPolicy13fileCheckMmapEP5ucredP8fileglobP5labeliiyPi : 636 -> 644
~ __ZN17AppleSystemPolicy4initEP12OSDictionary : 464 -> 448
~ _log_executable : 312 -> 328
~ _evaluate_exec : 548 -> 648
~ _evaluate_library_load : 488 -> 584
~ _evaluate_script : 400 -> 456
~ _handle_blocked_exec : 512 -> 520
~ _handle_blocked_load : 572 -> 596
~ _malware_scan : 328 -> 344
~ _bastion_violation : 356 -> 380
~ _do_tracking_sandbox : 336 -> 340
~ _tracking_gatekeeper_violation : 320 -> 336
- _ZN21NVRAMRecoveryBootMode15registerContentEb.cold.1
CStrings:
+ "com.apple.Terminal"

```
