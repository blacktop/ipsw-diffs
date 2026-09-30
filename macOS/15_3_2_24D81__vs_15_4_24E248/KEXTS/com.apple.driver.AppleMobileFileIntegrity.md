## com.apple.driver.AppleMobileFileIntegrity

> `com.apple.driver.AppleMobileFileIntegrity`

```diff

-938.81.1.0.0
-  __TEXT.__const: 0x1ad0
-  __TEXT.__cstring: 0x19385
-  __TEXT.__os_log: 0x380
-  __TEXT_EXEC.__text: 0x32664
+938.101.1.0.0
+  __TEXT.__cstring: 0x1aa1e
+  __TEXT.__const: 0x1b50
+  __TEXT.__os_log: 0x47a
+  __TEXT_EXEC.__text: 0x3353c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x81a
   __DATA.__common: 0xb0
-  __DATA.__bss: 0x129
-  __DATA_CONST.__auth_got: 0x910
-  __DATA_CONST.__got: 0x158
-  __DATA_CONST.__auth_ptr: 0x20
+  __DATA.__bss: 0x121
+  __DATA_CONST.__auth_got: 0x928
+  __DATA_CONST.__got: 0x148
+  __DATA_CONST.__auth_ptr: 0x28
   __DATA_CONST.__mod_init_func: 0x20
   __DATA_CONST.__mod_term_func: 0x18
-  __DATA_CONST.__const: 0xb250
-  __DATA_CONST.__kalloc_type: 0x1200
-  __DATA_CONST.__kalloc_var: 0x11d0
-  UUID: 7281201C-127B-3429-8955-036CEEB40DEC
-  Functions: 909
-  Symbols:   1978
-  CStrings:  3117
+  __DATA_CONST.__const: 0xbb40
+  __DATA_CONST.__kalloc_type: 0x1240
+  __DATA_CONST.__kalloc_var: 0x1270
+  __DATA_CONST.__assert: 0xdc
+  UUID: 4D3FB3E9-4EB8-3557-8A9E-F4063C3F45AA
+  Functions: 971
+  Symbols:   2115
+  CStrings:  3254
 
Symbols:
+ ACMKernelTransport.cold.1
+ DeallocCredentialList.kalloc_type_view_1816
+ DeserializeCredentialList.kalloc_type_view_1778
+ _CEContextAccelerate
+ _CEContextCheckSubset
+ _CEContextDecelerate
+ _CEContextGetDictionary
+ _CEContextGetLegacyContext
+ _CEContextInitWithTypeLegacy
+ _CEContextSetLegacyContext
+ _CEContextValueForKey
+ _CEDictionaryIterate
+ _CEElementContainsData
+ _CEElementContainsString
+ _CEElementContainsStringWithCEString
+ _CEElementDeserialize
+ _CEElementDeserializeValueType
+ _CEElementGetBool
+ _CEElementGetCEBuffer
+ _CEElementGetData
+ _CEElementGetIndexCount
+ _CEElementGetInteger
+ _CEElementGetString
+ _CEElementIterate
+ _CEElementMatchBool
+ _CEElementMatchData
+ _CELogWithArgs
+ _CEStringBufferAppendN
+ _CEStringCompare
+ _CEStringComparePrefix
+ _OUTLINED_FUNCTION_0
+ _OUTLINED_FUNCTION_1
+ _PE_parse_boot_arg_str
+ _Z26validateAndRegisterProfileR21ProfileValidationData.cold.1
+ _Z26validateProfileWithContextPK25_ProfileValidationContextP9_CEString.cold.1
+ _Z26validateProfileWithContextPK25_ProfileValidationContextP9_CEString.cold.2
+ _Z26validateProfileWithContextPK25_ProfileValidationContextP9_CEString.cold.3
+ _ZN14OSEntitlements17adjustWithMonitorEPKv.cold.1
+ _ZN14OSEntitlements17adjustWithMonitorEPKv.cold.2
+ _ZN14OSEntitlements17initTransmutationEPKhm.cold.1
+ _ZN14OSEntitlements17initTransmutationEPKhm.cold.2
+ _ZN14OSEntitlements17initTransmutationEPKhm.cold.3
+ _ZN14OSEntitlements17initTransmutationEPKhm.cold.4
+ _ZN14OSEntitlements20adjustWithoutMonitorEPK7cs_blob.cold.1
+ _ZN14OSEntitlements20adjustWithoutMonitorEPK7cs_blob.cold.2
+ _ZN14OSEntitlements20adjustWithoutMonitorEPK7cs_blob.cold.3
+ _ZN14OSEntitlements20adjustWithoutMonitorEPK7cs_blob.cold.4
+ _ZN14OSEntitlements4freeEv.cold.1
+ _ZN3TLE10RefCountedD0Ev.46
+ _ZN3TLE10RefCountedD1Ev.50
+ _ZN3TLE9Operation12shouldIgnoreEv.32
+ _ZN7libkern15safe_allocationINS_20intrusive_shared_ptrIN3TLE9OperationENS2_14RefCountPolicyEEEN9os_detail21IOKit_typed_allocatorIS5_Lb0EEENS6_21panic_trapping_policyEED1Ev.39
+ _ZN9os_detail21panic_trapping_policy4trapEPKc.34
+ _ZTVN3TLE10RefCountedE.40
+ _ZZN3TLE10RefCounteddlEPvmE19kalloc_type_view_79.47
+ _ZZN9os_detail21IOKit_typed_allocatorIN7libkern20intrusive_shared_ptrIN3TLE9OperationENS3_14RefCountPolicyEEELb0EE7kt_viewEvE7kt_view.51
+ __Block_byref_object_copy_.59
+ __Block_byref_object_copy_.64
+ __Block_byref_object_copy_.76
+ __Block_byref_object_dispose_.60
+ __Block_byref_object_dispose_.65
+ __Block_byref_object_dispose_.77
+ __Z13amfiFreeIndexPK9CERuntimePvm
+ __Z14amfiAllocIndexPK9CERuntimem
+ __Z15isSimulatorTypej
+ __Z17getOSEntitlementsP4proc
+ __Z17getOSEntitlementsP5ucred
+ __Z18copyOSEntitlementsP4proc
+ __Z19constraintTelemetryRN3TLE4LWCRE19TLEConstraintType_tR22AbstractCSBlobAccessor
+ __Z19lwcrHasARequirementRN3TLE4LWCRE
+ __Z20parentProcHasChangedR15ProcessAccessorS0_
+ __Z21validateLocallySignedILb0EEbP7cs_blobPKhP14OSEntitlementsPKc
+ __Z21validateLocallySignedILb1EEbP7cs_blobPKhP14OSEntitlementsPKc
+ __Z24csBlobSetEntitlementsMapP14OSEntitlementsP7cs_blob
+ __Z25CEElementCreateAsOSObjectPK14der_vm_contextPPK8OSObject
+ __Z26evaluateConstraintCategory20ConstraintCategory_t24LCConstraintIdentifier_tR16MetaEncyclopediaS2_S2_R15ProcessAccessorS4_R23LaunchConstraintError_t
+ __Z26registerProfileWithContextPK25_ProfileValidationContextPK9_CEStringP7cs_blob
+ __Z26validateProfileWithContextPK25_ProfileValidationContextP9_CEString
+ __Z29CEContextCreateAsOSDictionaryPK10_CEContextPPK12OSDictionary
+ __Z30OSEntitlementsBridge_copyValuePKvPKcPPv
+ __Z30OSEntitlementsBridge_matchBoolPKvPKc
+ __Z31getOSEntitlementsFromProcSecureP4procP14OSEntitlements
+ __Z32OSEntitlementsBridge_matchStringPKvPKcS2_
+ __Z34OSEntitlementsBridge_createXMLBlobPvPP16__SC_GenericBlob
+ __Z35OSEntitlementsBridge_copyDictionaryPv
+ __Z36macos_dyld_policy_libsystem_overrideP4procP24amfi_dyld_policy_state_t
+ __Z38OSEntitlementsBridge_adjustWithMonitorPvP14CEQueryContextPKvPKcj
+ __Z38OSEntitlementsBridge_copyValueWithProcP4procPKcPPv
+ __Z38OSEntitlementsBridge_matchBoolWithProcP4procPKc
+ __Z40OSEntitlementsBridge_getTramsmutatedBlobPvPPK16__SC_GenericBlob
+ __Z40OSEntitlementsBridge_matchStringWithProcP4procPKcS2_
+ __Z40submitEnvironmentConstraintUsageAnalytic19TLEConstraintType_tR22AbstractCSBlobAccessor
+ __Z41OSEntitlementsBridge_adjustWithoutMonitorPvP7cs_blob
+ __Z43OSEntitlementsBridge_invalidateEntitlementsPv
+ __Z7amfiLogPK9CERuntimePKcz
+ __Z9amfiPanicPK9CERuntimePKcz
+ __ZL10deviceUDID
+ __ZL12freeOSObjectPKv
+ __ZL13appendOSArrayPvPKv
+ __ZL14allocateOSDataPK7_CEData
+ __ZL14deserializeEnv
+ __ZL14deviceUDIDSize
+ __ZL14postValidationR15ProcessAccessorR16FileGlobAccessorR11SystemFactsym
+ __ZL15allocateOSArrayv
+ __ZL15validateProfilePK25_ProfileValidationContextPK10_CEContextPK9_CEString
+ __ZL16allocateOSNumbery
+ __ZL16allocateOSStringPK9_CEString
+ __ZL16allocateOSSymbolPK9_CEString
+ __ZL17allocateOSBooleanb
+ __ZL17codeSigningConfig
+ __ZL18appendOSDictionaryPvPKvS1_
+ __ZL18entitlementsBitMap
+ __ZL19getProfileUniversalPK10_CEContext
+ __ZL20allocateOSDictionaryv
+ __ZL21_kern_return_to_errnoi
+ __ZL26trustCacheInterfaceVersion
+ __ZL28_CEClosureCallbackDictionaryPK15_CEKeyValuePairP14_CEIterateArgs
+ __ZL29shouldHardenSigningIdentifierPKcj
+ __ZL36_checkBrokenSignatureWithTeamIDFatalP8LazyPathP7cs_blob
+ __ZL36isIdentifierExemptFromPlatformPolicyPKc
+ __ZL38evaluateLibraryLoadConstraintOnLibraryR15ProcessAccessorR16FileGlobAccessorR11SystemFactsym
+ __ZL38evaluateLibraryLoadConstraintOnProcessR15ProcessAccessorR16FileGlobAccessorR11SystemFactsym
+ __ZN14OSEntitlements10getContextEv
+ __ZN14OSEntitlements10notMatchInEPK5match
+ __ZN14OSEntitlements11addIdentityEPKc
+ __ZN14OSEntitlements11matchStringEPKcS1_
+ __ZN14OSEntitlements12initIdentityEPKc
+ __ZN14OSEntitlements12withIdentityEPKc
+ __ZN14OSEntitlements13checkPresenceEPKc
+ __ZN14OSEntitlements13createXMLBlobEv
+ __ZN14OSEntitlements14copyDictionaryEv
+ __ZN14OSEntitlements15getReadOnlyDataEv
+ __ZN14OSEntitlements16initEntitlementsEPK10_CEContextm
+ __ZN14OSEntitlements16initReadOnlyDataEv
+ __ZN14OSEntitlements16withEntitlementsEPKhm
+ __ZN14OSEntitlements17adjustWithMonitorEPKv
+ __ZN14OSEntitlements17initTransmutationEPKhm
+ __ZN14OSEntitlements18markAsTransmutatedEPKhm
+ __ZN14OSEntitlements19checkLegacyDebuggerEv
+ __ZN14OSEntitlements19checkPlatformBinaryEv
+ __ZN14OSEntitlements19getTransmutatedBlobEv
+ __ZN14OSEntitlements20adjustWithoutMonitorEPK7cs_blob
+ __ZN14OSEntitlements20markAsPlatformBinaryEv
+ __ZN14OSEntitlements22invalidateEntitlementsEv
+ __ZN14OSEntitlements6adjustEPK7cs_blobPKv
+ __ZN14OSEntitlements7forEachEU13block_pointerF10CEReturn_tPK15_CEKeyValuePairP14_CEIterateArgsE
+ __ZN14OSEntitlements7matchInEPK5match
+ __ZN14OSEntitlements8getCountEv
+ __ZN14OSEntitlements9copyValueEPKc
+ __ZN14OSEntitlements9matchBoolEPKc
+ __ZN20LaunchTypeNonePolicy19launchTypeIsAllowedER11SystemFactsR15ProcessAccessorS3_R23LaunchConstraintError_t
+ __ZN20LaunchTypeNonePolicy21launchSatisfiesPolicyER11SystemFactsR15ProcessAccessorS3_R16MetaEncyclopediaS5_S5_R23LaunchConstraintError_t
+ __ZN21ConfigurationSettings13bootedWithCSMEv
+ __ZN21ConfigurationSettings13bootedWithPPLEv
+ __ZN21ConfigurationSettings13bootedWithTXMEv
+ __ZN21ConfigurationSettings30forceDisallowLibsystemOverrideEv
+ __ZN21ConfigurationSettings5MacOS14forceHardeningEv
+ __ZN21ConfigurationSettings5MacOS20forceAlmondHardeningEv
+ __ZN21ConfigurationSettings5MacOS26forceDefaultCoreDumpPolicyEv
+ __ZN21ConfigurationSettings5MacOS26forceDefaultTaskportPolicyEv
+ __ZN21ConfigurationSettings5MacOS28forcePlatformAOTInTrustCacheEv
+ __ZN21ConfigurationSettings5MacOS29forceDefaultDyldEnvVarsPolicyEv
+ __ZN21ConfigurationSettings5MacOS30forceHardenAllPlatformBinariesEv
+ __ZN21ConfigurationSettings5MacOS39forceDefaultHardenedRuntimeChrootPolicyEv
+ __ZN21ConfigurationSettings5MacOS41forcePlatformIdentifierRequiresTrustCacheEv
+ __ZN24AppleMobileFileIntegrity27submitAuxiliaryInfoAnalyticEP5vnodeP7cs_blob
+ __ZN27LaunchTypeApplicationPolicy19launchTypeIsAllowedER11SystemFactsR15ProcessAccessorS3_R23LaunchConstraintError_t
+ __ZN27LaunchTypeApplicationPolicy21launchSatisfiesPolicyER11SystemFactsR15ProcessAccessorS3_R16MetaEncyclopediaS5_S5_R23LaunchConstraintError_t
+ __ZN27LaunchTypeSysdiagnosePolicy19launchTypeIsAllowedER11SystemFactsR15ProcessAccessorS3_R23LaunchConstraintError_t
+ __ZN27LaunchTypeSysdiagnosePolicy21launchSatisfiesPolicyER11SystemFactsR15ProcessAccessorS3_R16MetaEncyclopediaS5_S5_R23LaunchConstraintError_t
+ __ZN29LaunchTypeSystemServicePolicy19launchTypeIsAllowedER11SystemFactsR15ProcessAccessorS3_R23LaunchConstraintError_t
+ __ZN29LaunchTypeSystemServicePolicy21launchSatisfiesPolicyER11SystemFactsR15ProcessAccessorS3_R16MetaEncyclopediaS5_S5_R23LaunchConstraintError_t
+ __ZN3TLE14RefCountPolicy7releaseERNS_10RefCountedE
+ __ZN7libkern15safe_allocationINS_20intrusive_shared_ptrIN3TLE9OperationENS2_14RefCountPolicyEEEN9os_detail21IOKit_typed_allocatorIS5_Lb0EEENS6_21panic_trapping_policyEE3endEv
+ __ZN7libkern15safe_allocationINS_20intrusive_shared_ptrIN3TLE9OperationENS2_14RefCountPolicyEEEN9os_detail21IOKit_typed_allocatorIS5_Lb0EEENS6_21panic_trapping_policyEED1Ev
+ __ZZ13amfiFreeIndexPK9CERuntimePvmE19kalloc_type_view_47
+ __ZZ14amfiAllocIndexPK9CERuntimemE19kalloc_type_view_43
+ __ZZ25_cred_label_update_execveP5ucredS0_P4procP5vnodexS4_P5labelS6_S6_PjPvmPiE6__desc
+ __ZZ25_cred_label_update_execveP5ucredS0_P4procP5vnodexS4_P5labelS6_S6_PjPvmPiE6__desc_0
+ __ZZ25_cred_label_update_execveP5ucredS0_P4procP5vnodexS4_P5labelS6_S6_PjPvmPiE6__desc_1
+ __ZZ25_cred_label_update_execveP5ucredS0_P4procP5vnodexS4_P5labelS6_S6_PjPvmPiE6__desc_2
+ __ZZ25_cred_label_update_execveP5ucredS0_P4procP5vnodexS4_P5labelS6_S6_PjPvmPiE6__desc_3
+ __ZZL19_cred_label_destroyP5labelE6__desc
+ __ZZL26_cacheJitCodeDirectoryHashPKhE20kalloc_type_view_431
+ __ZZL27_process_matches_constraintP4procyE21kalloc_type_view_5153
+ __ZZL27_process_matches_constraintP4procyE21kalloc_type_view_5176
+ __ZZL38evaluateLibraryLoadConstraintOnLibraryR15ProcessAccessorR16FileGlobAccessorR11SystemFactsymE11_os_log_fmt
+ __ZZL38evaluateLibraryLoadConstraintOnLibraryR15ProcessAccessorR16FileGlobAccessorR11SystemFactsymE11_os_log_fmt_0
+ __ZZL38evaluateLibraryLoadConstraintOnProcessR15ProcessAccessorR16FileGlobAccessorR11SystemFactsymE11_os_log_fmt
+ __ZZL38evaluateLibraryLoadConstraintOnProcessR15ProcessAccessorR16FileGlobAccessorR11SystemFactsymE11_os_log_fmt_0
+ __ZZN20StaticPlatformPolicyILb1ELb1ELb0ELb1ELb0ELb1ELb1ELb0ELb0ELb1ELb0ELb1ELb0ELb0ELb1ELb0ELj2ELb1ELb0EE15check_signatureEP13VnodeLazyPathiP7cs_blobPjS5_ibbbjPPcPmE21kalloc_type_view_2915
+ __ZZN20StaticPlatformPolicyILb1ELb1ELb0ELb1ELb0ELb1ELb1ELb0ELb0ELb1ELb0ELb1ELb0ELb0ELb1ELb0ELj2ELb1ELb0EE15check_signatureEP13VnodeLazyPathiP7cs_blobPjS5_ibbbjPPcPmE21kalloc_type_view_3149
+ __ZZN20StaticPlatformPolicyILb1ELb1ELb0ELb1ELb0ELb1ELb1ELb0ELb0ELb1ELb0ELb1ELb0ELb0ELb1ELb0ELj2ELb1ELb0EE15check_signatureEP13VnodeLazyPathiP7cs_blobPjS5_ibbbjPPcPmE6__desc
+ __ZZN20StaticPlatformPolicyILb1ELb1ELb0ELb1ELb0ELb1ELb1ELb0ELb0ELb1ELb0ELb1ELb0ELb0ELb1ELb0ELj2ELb1ELb0EE25validateCodeDirectoryHashEP8LazyPathP7cs_blobPjS5_P14OSEntitlementsihbbPcbbPbP25AMFIHashValidationResult_E6__desc
+ __ZZN20StaticPlatformPolicyILb1ELb1ELb1ELb1ELb1ELb1ELb1ELb0ELb1ELb0ELb1ELb0ELb1ELb1ELb0ELb0ELj1ELb1ELb0EE15check_signatureEP13VnodeLazyPathiP7cs_blobPjS5_ibbbjPPcPmE21kalloc_type_view_2915
+ __ZZN20StaticPlatformPolicyILb1ELb1ELb1ELb1ELb1ELb1ELb1ELb0ELb1ELb0ELb1ELb0ELb1ELb1ELb0ELb0ELj1ELb1ELb0EE15check_signatureEP13VnodeLazyPathiP7cs_blobPjS5_ibbbjPPcPmE21kalloc_type_view_3149
+ __ZZN20StaticPlatformPolicyILb1ELb1ELb1ELb1ELb1ELb1ELb1ELb0ELb1ELb0ELb1ELb0ELb1ELb1ELb0ELb0ELj1ELb1ELb0EE15check_signatureEP13VnodeLazyPathiP7cs_blobPjS5_ibbbjPPcPmE6__desc
+ __ZZN20StaticPlatformPolicyILb1ELb1ELb1ELb1ELb1ELb1ELb1ELb0ELb1ELb0ELb1ELb0ELb1ELb1ELb0ELb0ELj1ELb1ELb0EE25loadEntitlementsFromVnodeEPP14OSEntitlementsP5vnodexP4procPPKcE6__desc
+ __ZZN20StaticPlatformPolicyILb1ELb1ELb1ELb1ELb1ELb1ELb1ELb0ELb1ELb0ELb1ELb0ELb1ELb1ELb0ELb0ELj1ELb1ELb0EE25validateCodeDirectoryHashEP8LazyPathP7cs_blobPjS5_P14OSEntitlementsihbbPcbbPbP25AMFIHashValidationResult_E6__desc
+ ___ZN14OSEntitlements13createXMLBlobEv_block_invoke.cold.1
+ ___ZN14OSEntitlements13createXMLBlobEv_block_invoke.cold.2
+ ___ZN14OSEntitlements14copyDictionaryEv_block_invoke.cold.1
+ ____Z21validateLocallySignedILb0EEbP7cs_blobPKhP14OSEntitlementsPKc_block_invoke
+ ____Z21validateLocallySignedILb1EEbP7cs_blobPKhP14OSEntitlementsPKc_block_invoke
+ ____ZN14OSEntitlements10getContextEv_block_invoke
+ ____ZN14OSEntitlements10notMatchInEPK5match_block_invoke
+ ____ZN14OSEntitlements11matchStringEPKcS1__block_invoke
+ ____ZN14OSEntitlements12copyIdentityEv_block_invoke
+ ____ZN14OSEntitlements13checkPresenceEPKc_block_invoke
+ ____ZN14OSEntitlements13createXMLBlobEv_block_invoke
+ ____ZN14OSEntitlements14copyDictionaryEv_block_invoke
+ ____ZN14OSEntitlements19checkLegacyDebuggerEv_block_invoke
+ ____ZN14OSEntitlements19checkPlatformBinaryEv_block_invoke
+ ____ZN14OSEntitlements19getTransmutatedBlobEv_block_invoke
+ ____ZN14OSEntitlements7forEachEU13block_pointerF10CEReturn_tPK15_CEKeyValuePairP14_CEIterateArgsE_block_invoke
+ ____ZN14OSEntitlements7matchInEPK5match_block_invoke
+ ____ZN14OSEntitlements8getCountEv_block_invoke
+ ____ZN14OSEntitlements9copyValueEPKc_block_invoke
+ ____ZN14OSEntitlements9matchBoolEPKc_block_invoke
+ ____ZN20StaticPlatformPolicyILb1ELb1ELb0ELb1ELb0ELb1ELb1ELb0ELb0ELb1ELb0ELb1ELb0ELb0ELb1ELb0ELj2ELb1ELb0EE19processEntitlementsEP14OSEntitlementsPKhPjPbS6_S6_PKcP8LazyPathPPcPm_block_invoke
+ ____ZN20StaticPlatformPolicyILb1ELb1ELb1ELb1ELb1ELb1ELb1ELb0ELb1ELb0ELb1ELb0ELb1ELb1ELb0ELb0ELj1ELb1ELb0EE19processEntitlementsEP14OSEntitlementsPKhPjPbS6_S6_PKcP8LazyPathPPcPm_block_invoke
+ ___copy_helper_block_8_32b40r48r
+ ___copy_helper_block_8_32r40p2d57635
+ ___copy_helper_block_8_32r40r48p2d3225656p2d4261
+ ___copy_helper_block_8_32r40r48p2d3614
+ ___copy_helper_block_8_32r40r48p2d37662
+ ___copy_helper_block_8_32r40r48r56r64r72r80r
+ ___der_vm_iterate_count_block_invoke
+ ___destroy_helper_block_8_32b40r48r
+ ___destroy_helper_block_8_32r40
+ ___destroy_helper_block_8_32r40r48
+ ___destroy_helper_block_8_32r40r4856
+ ___destroy_helper_block_8_32r40r48r56r64r72r80r
+ __block_descriptor_tmp.10.212
+ __block_descriptor_tmp.132
+ __block_descriptor_tmp.190
+ __block_descriptor_tmp.203
+ __block_descriptor_tmp.30
+ __block_descriptor_tmp.33
+ __block_descriptor_tmp.337
+ __block_descriptor_tmp.36
+ __block_descriptor_tmp.37
+ __block_descriptor_tmp.373
+ __block_descriptor_tmp.40
+ __block_descriptor_tmp.41
+ __block_descriptor_tmp.414
+ __block_descriptor_tmp.431
+ __block_descriptor_tmp.48
+ __block_descriptor_tmp.5.338
+ __block_descriptor_tmp.50
+ __block_descriptor_tmp.54
+ __block_descriptor_tmp.63
+ __block_descriptor_tmp.67
+ __block_descriptor_tmp.69
+ __block_descriptor_tmp.7
+ __block_descriptor_tmp.76
+ __block_descriptor_tmp.9.339
+ _arrayIterate
+ _countIterate
+ _count_keys
+ _csblob_get_auxiliary_info
+ _csblob_get_trust_level
+ _csblob_set_auxiliary_info
+ _derVMIterateCallback
+ _der_decode_boolean
+ _der_decode_entitlements
+ _der_decode_number
+ _der_decode_numeric_string
+ _der_decode_string
+ _der_decode_utc_time
+ _der_validate_array
+ _der_vm_CEType_from_ccder_tag
+ _der_vm_data_from_context
+ _der_vm_execute_match_integer
+ _dictionaryIterate
+ _iterateKeyValuePairs
+ _mapToCEReturn
+ _matchInWithCEString
+ _osEntitlementsZone
+ _proc_orig_ppidversion
+ _proc_task
+ _sequenceSearchForValue
+ _stringMatchWithOptions
+ _string_match_prefix
+ _supportedUDID
+ _task_set_cs_auxiliary_info
+ _unload_trust_cache
+ _validateContextWithType
+ _validateDictionary
+ _validateDuplicateKeys
+ _validateDuplicateKeysSub
+ _validateKeyValuePair
+ _validateSingleType
+ _validateString
+ _validateValueTypePair
+ _versionUDID
+ _xml_size_string
+ acm_mem_free_data.cold.1
+ mapToCEReturn.1
+ mapToCEReturn.4
- LibCall_ACMKernelControl.cold.1
- LibCall_ACMSetEnvironmentVariable.cold.1
- LibCall_ACMSetEnvironmentVariable.cold.2
- LibCall_ACMSetEnvironmentVariable.cold.3
- _Assert
- _CECreateStringOpInplace
- _XNUHasMonitor
- _Z15fatal_error_fmtP8LazyPathPPcPmPKcz.cold.1
- _Z23precookExemptionProfilev.cold.1
- _Z23precookExemptionProfilev.cold.2
- _Z39submitLaunchConstraintViolationAnalyticR23LaunchConstraintError_tR15ProcessAccessorS2_R11LaunchFacts.cold.1
- _ZL15_policy_syscallP4prociy.cold.1
- _ZL9okOrPanic14der_vm_context.cold.1
- _ZN14OSEntitlements10getXMLBlobEv.cold.1
- _ZN14OSEntitlements10getXMLBlobEv.cold.2
- _ZN14OSEntitlements11initInvalidEPKc.cold.1
- _ZN14OSEntitlements24adjustContextWithMonitorEP14CEQueryContextPKvPKcj.cold.1
- _ZN14OSEntitlements24adjustContextWithMonitorEP14CEQueryContextPKvPKcj.cold.2
- _ZN14OSEntitlements24initWithValidationResultE18CEValidationResultP7cs_blobb.cold.1
- _ZN14OSEntitlements27adjustContextWithoutMonitorEP7cs_blob.cold.1
- _ZN14OSEntitlements27adjustContextWithoutMonitorEP7cs_blob.cold.2
- _ZN14OSEntitlements27adjustContextWithoutMonitorEP7cs_blob.cold.3
- _ZN3TLE10RefCountedD0Ev.18
- _ZN3TLE10RefCountedD1Ev.22
- _ZN3TLE9Operation12shouldIgnoreEv.4
- _ZN9os_detail21panic_trapping_policy4trapEPKc.6
- _ZTVN3TLE10RefCountedE.13
- _ZZN3TLE10RefCounteddlEPvmE19kalloc_type_view_79.19
- _ZZN9os_detail21IOKit_typed_allocatorIN7libkern20intrusive_shared_ptrIN3TLE9OperationENS3_14RefCountPolicyEEELb0EE7kt_viewEvE7kt_view.12
- __Block_byref_object_copy_.47
- __Block_byref_object_dispose_.48
- __Z15getEntitlementsP4proc
- __Z15getEntitlementsP5ucred
- __Z16copyEntitlementsP4proc
- __Z16copyEntitlementsP5ucred
- __Z18handleDictAdditionRK11OSSharedPtrI12OSDictionaryEP14der_vm_context
- __Z19constraintTelemetryRN3TLE4LWCRE19TLEConstraintType_tR15ProcessAccessor
- __Z21devModeStatusResolvedv
- __Z21manufacturingCallbackP24der_vm_iteration_context
- __Z22objectForActiveContextPK14der_vm_context
- __Z23precookExemptionProfilev
- __Z24CEQueryContextToOSObjectP14CEQueryContext
- __Z26evaluateConstraintCategory20ConstraintCategory_t24LCConstraintIdentifier_tR16MetaEncyclopediaS2_S2_R23LaunchConstraintError_t
- __Z28CEQueryContextToOSDictionaryP14CEQueryContext
- __Z33OSEntitlementsHaveEntitlementBoolP14OSEntitlementsPKc
- __Z40submitEnvironmentConstraintUsageAnalytic19TLEConstraintType_tR15ProcessAccessor
- __ZL10udidLength
- __ZL13cookedProfile
- __ZL13copySigningIDPKc
- __ZL13symbolFromKeyP17__opaque_amfi_keyPKc
- __ZL14intFromContextPK14der_vm_context
- __ZL14keyFromContextPK14der_vm_context
- __ZL15boolFromContextPK14der_vm_context
- __ZL15dataFromContextPK14der_vm_context
- __ZL15typeFromContextPK14der_vm_context
- __ZL15validateProfileR21ProfileValidationData14der_vm_context8CEBuffer
- __ZL16exemptionProfile
- __ZL16valueFromContextPK14der_vm_context
- __ZL17stringFromContextPK14der_vm_context
- __ZL19osentitlements_zone
- __ZL22udidEnforcementEnabled
- __ZL29evaluateLibraryLoadConstraintR15ProcessAccessorR16FileGlobAccessorR11SystemFactsym
- __ZL39__entitlements_failed_consistency_panicPK14OSEntitlementsPK19OSEntitlementsState
- __ZL4udid
- __ZL9okOrPanic14der_vm_context
- __ZN12OSDictionary9setObjectERK11OSSharedPtrIK8OSSymbolERKS0_IK15OSMetaClassBaseE
- __ZN14OSEntitlements10getXMLBlobEv
- __ZN14OSEntitlements10invalidateEv
- __ZN14OSEntitlements11initInvalidEPKc
- __ZN14OSEntitlements11makeInvalidEPKc
- __ZN14OSEntitlements12isCSPlatformEv
- __ZN14OSEntitlements15copyEntitlementEPKc
- __ZN14OSEntitlements16copyOSDictionaryEv
- __ZN14OSEntitlements16isLegacyDebuggerEv
- __ZN14OSEntitlements16markAsCSPlatformEv
- __ZN14OSEntitlements17getTransmutedBlobEv
- __ZN14OSEntitlements17queryEntitlementsEP16CEQueryOperationm
- __ZN14OSEntitlements18entitlementTypeForEPKcP8CEType_t
- __ZN14OSEntitlements18getEntitlementsForEv
- __ZN14OSEntitlements20withValidationResultE18CEValidationResultP7cs_blobb
- __ZN14OSEntitlements22queryEntitlementStringEPKcS1_
- __ZN14OSEntitlements23queryEntitlementBooleanEPKc
- __ZN14OSEntitlements24adjustContextWithMonitorEP14CEQueryContextPKvPKcj
- __ZN14OSEntitlements24initWithValidationResultE18CEValidationResultP7cs_blobb
- __ZN14OSEntitlements25queryEntitlementsUnlockedEP16CEQueryOperationm
- __ZN14OSEntitlements27adjustContextWithoutMonitorEP7cs_blob
- __ZN14OSEntitlements27executeEntitlementsUnlockedEP16CEQueryOperationm
- __ZN14OSEntitlements30queryEntitlementStringUnlockedEPKcS1_
- __ZN14OSEntitlements31queryEntitlementBooleanUnlockedEPKc
- __ZN14OSEntitlements6asDictEv
- __ZN14OSEntitlements9get_stateEv
- __ZN17macOSPolicyConfig22almondHardeningEnabledEv
- __ZN17macOSPolicyConfig25hardenAllPlatformBinariesEv
- __ZN17macOSPolicyConfig26forceDefaultCoreDumpPolicyEv
- __ZN17macOSPolicyConfig26forceDefaultTaskportPolicyEv
- __ZN17macOSPolicyConfig29forceDefaultDyldEnvVarsPolicyEv
- __ZN17macOSPolicyConfig39forceDefaultHardenedRuntimeChrootPolicyEv
- __ZN20LaunchTypeNonePolicy19launchTypeIsAllowedER11SystemFactsR15ProcessAccessorR23LaunchConstraintError_t
- __ZN20LaunchTypeNonePolicy21launchSatisfiesPolicyER11SystemFactsR15ProcessAccessorR16MetaEncyclopediaS5_S5_R23LaunchConstraintError_t
- __ZN20OSCollectionIterator14withCollectionEPK12OSCollection
- __ZN24AppleMobileFileIntegrity18copyEntitlementKeyEP4procP17__opaque_amfi_key
- __ZN24AppleMobileFileIntegrity18copyEntitlementKeyEP5ucredP17__opaque_amfi_key
- __ZN24AppleMobileFileIntegrity19AMFIGetQueryContextEP4procPP14CEQueryContext
- __ZN24AppleMobileFileIntegrity19AMFIGetQueryContextEP5ucredPP14CEQueryContext
- __ZN24AppleMobileFileIntegrity21AMFIEntitlementGetKeyEPKc
- __ZN24AppleMobileFileIntegrity25AMFIEntitlementReleaseKeyEP17__opaque_amfi_key
- __ZN24AppleMobileFileIntegrity26AMFIEntitlementGetConstKeyEPKc
- __ZN24AppleMobileFileIntegrity27AMFIEntitlementKeyIsPresentEP4procP17__opaque_amfi_keyPb
- __ZN24AppleMobileFileIntegrity27AMFIEntitlementKeyIsPresentEP5ucredP17__opaque_amfi_keyPb
- __ZN24AppleMobileFileIntegrity28AMFIEntitlementKeyIsBoolTrueEP4procP17__opaque_amfi_keyPb
- __ZN24AppleMobileFileIntegrity28AMFIEntitlementKeyIsBoolTrueEP5ucredP17__opaque_amfi_keyPb
- __ZN27LaunchTypeApplicationPolicy19launchTypeIsAllowedER11SystemFactsR15ProcessAccessorR23LaunchConstraintError_t
- __ZN27LaunchTypeApplicationPolicy21launchSatisfiesPolicyER11SystemFactsR15ProcessAccessorR16MetaEncyclopediaS5_S5_R23LaunchConstraintError_t
- __ZN27LaunchTypeSysdiagnosePolicy19launchTypeIsAllowedER11SystemFactsR15ProcessAccessorR23LaunchConstraintError_t
- __ZN27LaunchTypeSysdiagnosePolicy21launchSatisfiesPolicyER11SystemFactsR15ProcessAccessorR16MetaEncyclopediaS5_S5_R23LaunchConstraintError_t
- __ZN29LaunchTypeSystemServicePolicy19launchTypeIsAllowedER11SystemFactsR15ProcessAccessorR23LaunchConstraintError_t
- __ZN29LaunchTypeSystemServicePolicy21launchSatisfiesPolicyER11SystemFactsR15ProcessAccessorR16MetaEncyclopediaS5_S5_R23LaunchConstraintError_t
- __ZN3TLE5TupleINS_5ErrorEN7libkern20intrusive_shared_ptrINS_9OperationENS_14RefCountPolicyEEEED1Ev
- __ZN7OSArray9setObjectERK11OSSharedPtrIK15OSMetaClassBaseE
- __ZN7libkern20intrusive_shared_ptrIN3TLE9OperationENS1_14RefCountPolicyEEaSEOS4_
- __ZN8OSSymbol9metaClassE
- __ZNK11OSMetaClass12getClassNameEv
- __ZZ15emptyDictionaryvE5empty
- __ZZL26_cacheJitCodeDirectoryHashPKhE20kalloc_type_view_438
- __ZZL27_process_matches_constraintP4procyE21kalloc_type_view_5075
- __ZZL27_process_matches_constraintP4procyE21kalloc_type_view_5098
- __ZZL29evaluateLibraryLoadConstraintR15ProcessAccessorR16FileGlobAccessorR11SystemFactsymE11_os_log_fmt
- __ZZL29evaluateLibraryLoadConstraintR15ProcessAccessorR16FileGlobAccessorR11SystemFactsymE11_os_log_fmt_0
- __ZZN20StaticPlatformPolicyILb1ELb1ELb0ELb1ELb0ELb1ELb1ELb0ELb0ELb1ELb0ELb1ELb0ELb0ELb1ELb0ELj2ELb1ELb0EE15check_signatureEP13VnodeLazyPathiP7cs_blobPjS5_ibbbjPPcPmE21kalloc_type_view_2898
- __ZZN20StaticPlatformPolicyILb1ELb1ELb0ELb1ELb0ELb1ELb1ELb0ELb0ELb1ELb0ELb1ELb0ELb0ELb1ELb0ELj2ELb1ELb0EE15check_signatureEP13VnodeLazyPathiP7cs_blobPjS5_ibbbjPPcPmE21kalloc_type_view_3114
- __ZZN20StaticPlatformPolicyILb1ELb1ELb1ELb1ELb1ELb1ELb1ELb0ELb1ELb0ELb1ELb0ELb1ELb1ELb0ELb0ELj1ELb1ELb0EE15check_signatureEP13VnodeLazyPathiP7cs_blobPjS5_ibbbjPPcPmE21kalloc_type_view_2898
- __ZZN20StaticPlatformPolicyILb1ELb1ELb1ELb1ELb1ELb1ELb1ELb0ELb1ELb0ELb1ELb0ELb1ELb1ELb0ELb0ELj1ELb1ELb0EE15check_signatureEP13VnodeLazyPathiP7cs_blobPjS5_ibbbjPPcPmE21kalloc_type_view_3114
- ____ZL15validateProfileR21ProfileValidationData14der_vm_context8CEBuffer_block_invoke
- __block_descriptor_tmp.10.176
- __block_descriptor_tmp.108
- __block_descriptor_tmp.158
- __block_descriptor_tmp.169
- __block_descriptor_tmp.289
- __block_descriptor_tmp.38
- __block_descriptor_tmp.5.290
- __block_descriptor_tmp.9.291
- _amfiAllocIndex
- _amfiFreeIndex
- _amfiLog
- _amfiPanic
- _amfi_OSEntitlements_adjustContextWithMonitor
- _amfi_OSEntitlements_adjustContextWithoutMonitor
- _amfi_OSEntitlements_asDict_impl
- _amfi_OSEntitlements_copyEntitlementAsOSObject
- _amfi_OSEntitlements_copyEntitlementAsOSObjectWithProc
- _amfi_OSEntitlements_get_transmuted_impl
- _amfi_OSEntitlements_get_xml_impl
- _amfi_OSEntitlements_invalidate_impl
- _amfi_OSEntitlements_queryEntitlementBoolean
- _amfi_OSEntitlements_queryEntitlementBooleanWithProc
- _amfi_OSEntitlements_queryEntitlementString
- _amfi_OSEntitlements_queryEntitlementStringWithProc
- _amfi_OSEntitlements_query_impl
- _amfi_get_legacy_profile_exemptions_impl
- _amfi_query_context_to_object_impl
- _der_vm_execute_seq_nocopy
- _der_vm_iterate_nocopy
- _der_vm_key_is_present
- _der_vm_select_bool_for_key
- _der_vm_string_is_allowed_for_key
- _der_vm_trampoline
- _der_vm_type_for_key
- _initializeOSEntitlementsSupport
- _matchMacOSPlatform
- _matchNativePlatform
- amfiAllocIndex.kalloc_type_view_46
- amfiFreeIndex.kalloc_type_view_50
- validateSignatureRSA.cold.1
CStrings:
+ "\"%s: missing ChipID or UniqueChipID: %p | %p\" @%s:%d"
+ "\"AMFI: attempted to free OSEntitlements without invalidation\" @%s:%d"
+ "\"AMFI: attempted to reinitialize OSEntitlementsReadOnly ceCtx: %p\" @%s:%d"
+ "\"AMFI: attempted to reinitialize OSEntitlementsReadOnly data: %p\" @%s:%d"
+ "\"AMFI: attempted to reinitialize OSEntitlementsReadOnly identity: %p\" @%s:%d"
+ "\"AMFI: failed OSEntitlements back-reference: %p | %p\" @%s:%d"
+ "\"AMFI: failed to acquire UUID element from profile: %u\" @%s:%d"
+ "\"AMFI: failed to acquire UUID string from profile: %u\" @%s:%d"
+ "\"AMFI: failed to acquire entitlements buffer from profile: %u\" @%s:%d"
+ "\"AMFI: failed to acquire entitlements element from profile: %u\" @%s:%d"
+ "\"AMFI: failed to compute size for XML: %s\\n\" @%s:%d"
+ "\"AMFI: failed to compute size for deserialization: %s\\n\" @%s:%d"
+ "\"AMFI: failed to create OSDictionary copy: %u\\n\" @%s:%d"
+ "\"AMFI: failed to create profile context: %u\" @%s:%d"
+ "\"AMFI: failed to deserialize legacy context: %s\\n\" @%s:%d"
+ "\"AMFI: failed to evaluate provisioning profile: %d\" @%s:%d"
+ "\"AMFI: failed to serialize as XML: %s\\n\" @%s:%d"
+ "\"AMFI: failed to validate entitlements from profile: %u\" @%s:%d"
+ "\"AMFI: inconsistency between instance and csBlob context\" @%s:%d"
+ "\"AMFI: inconsistency between instance and monitor context: %u | %u\" @%s:%d"
+ "\"AMFI: inconsistency in DER entitlements length: %u | %lu\" @%s:%d"
+ "\"AMFI: marking as transmutated when already set\\n\" @%s:%d"
+ "\"AMFI: marking as transmutated without entitlements\\n\" @%s:%d"
+ "\"AMFI: unable to adjust without monitor: %u\" @%s:%d"
+ "\"AMFI: unable to update legacy context: %u\" @%s:%d"
+ "\"AMFI: underflow on transmutated blob\\n\" @%s:%d"
+ "\"AMFI: unexpected OSEntitlements adjustment with monitor\" @%s:%d"
+ "\"AMFI: unexpected OSEntitlements adjustment without monitor\" @%s:%d"
+ "\"AMFI: unexpected magic on transmutated blob: %u\\n\" @%s:%d"
+ "%08X-%016llX"
+ "%s: /chosen node not found\n"
+ "%s: /product is missing udid-version\n"
+ "%s: /product node not found\n"
+ "%s: /product/udid-version has unexpected length: %u\n"
+ "%s: /product/udid-version is not supported: %u\n"
+ "%s: UUID expected but not provided\n"
+ "%s: error copying in UUID: %d\n"
+ "&amp;"
+ "&apos;"
+ "&gt;"
+ "&lt;"
+ "&quot;"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_KernelLibs/ACMKernelLib/ACMKernelTransport.cpp"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_KernelLibs/common/CommonMem.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_KernelLibs/common/LibCall.c"
+ "21:11:26"
+ "23050"
+ "AMFI sanitizer policy allowing %s for %s: tfp(%d) gta(%d) sip(%d) dev(%d) defanged(%d) procunsigned(%d) sim(%d) tc(%d) ai(%d)\n"
+ "AMFI: %s\n"
+ "AMFI: %s not allowed with universal profile\n"
+ "AMFI: %s: cannot securely resolve entitlements from NULL proc\n"
+ "AMFI: Only launchd can set the system service launch type (parent changed: %d)\n"
+ "AMFI: UDID support enabled: %u\n"
+ "AMFI: XNU monitor refused profile\n"
+ "AMFI: [non-fatal] unable to accelerate context: %s | %u\n"
+ "AMFI: apple-internal profile allows all entitlements\n"
+ "AMFI: device UDID not enforced\n"
+ "AMFI: empty profile provided: %s\n"
+ "AMFI: evaluating provisioning profile: %.*s\n"
+ "AMFI: failed to copy profile data into kernel allocation\n"
+ "AMFI: failed to create OSObject copy: %u\n"
+ "AMFI: failed to create kernel allocation for profile\n"
+ "AMFI: failed to set auxiliary_info for auxiliary info\n"
+ "AMFI: failed to set filename for auxiliary info\n"
+ "AMFI: failed to set monitor for auxiliary info\n"
+ "AMFI: failed to set platform for auxiliary info\n"
+ "AMFI: failed to set research_variant for auxiliary info\n"
+ "AMFI: failed to set signing_identifier for auxiliary info\n"
+ "AMFI: failed to set team_identifier for auxiliary info\n"
+ "AMFI: failed to set trust_level for auxiliary info\n"
+ "AMFI: only sysdiagnose can set the sysdiagnose launch type (parent changed: %d)\n"
+ "AMFI: platform disallowing loading sanitizer runtime %s for %s"
+ "AMFI: profile disallowed due to developer mode\n"
+ "AMFI: profile does not provision any developer certificates\n"
+ "AMFI: profile does not provision any devices\n"
+ "AMFI: profile does not provision claimed entitlements\n"
+ "AMFI: profile does not provision current device\n"
+ "AMFI: profile does not provision developer certificate\n"
+ "AMFI: profile not registered with XNU monitor without cs_blob\n"
+ "AMFI: profile provisions claimed entitlements\n"
+ "AMFI: profile provisions current device\n"
+ "AMFI: profile provisions developer certificate\n"
+ "AMFI: research variant relaxes lock-state for trust caches: %u\n"
+ "AMFI: unable to validate entitlements: %u\n"
+ "AMFI: using emulated device UDID: %s\n"
+ "AMFI: using universal provisioning profile\n"
+ "Constraint category parent constraint can't be enforced because parent has changed"
+ "CoreEntitlements: %.*s | duplicated key\n"
+ "CoreEntitlements: %.*s | validate: 0x%04X\n"
+ "Denying libsystem override on SIP-enabled, AppleInternal system with force policy sysctl set\n"
+ "Denying libsystem override on SIP-enabled, non-AppleInternal system \n"
+ "Embedded parent constraint can't be enforced because parent has changed"
+ "Embedded self constraint can't be enforced because parent has changed"
+ "EntitlementPolicy.h"
+ "Entitlements element not allowed"
+ "Forcing CS_RUNTIME for hardened entitlement\n"
+ "Forcing CS_RUNTIME for system extension entitlement\n"
+ "Library Process Constraint Rejection: Rejecting loading of '%s' (Team ID: %s, platform: %s) for process '%s(%d)' (Team ID: %s, platform: %s), reason: %.*s"
+ "Mar 19 2025"
+ "PPL"
+ "Process violates library's library load constraint"
+ "S24@?0r^{_CEKeyValuePair={der_vm_context=^{CERuntime}{CEAccelerationContext=^{CEAccelerationElement}Q}QBB(?={ccder_read_blob=**}{?=**})}{_CEValueTypePair=I{der_vm_context=^{CERuntime}{CEAccelerationContext=^{CEAccelerationElement}Q}QBB(?={ccder_read_blob=**}{?=**})}}}8^{_CEIterateArgs=^vQQBS}16"
+ "Sanitizer load violates platform policy"
+ "Support.cpp"
+ "TXM"
+ "UTC Time element not allowed"
+ "Unknown DER entitlements encoding"
+ "Unknown UTC Time encoding"
+ "Unknown numeric string encoding"
+ "XNU"
+ "_unload_trust_cache"
+ "amfi.OSEntitlements"
+ "amfi_emulate_device_udid"
+ "auxiliary_info"
+ "cmd = (acm_command_t *)({ size_t sizeVal = (cmdSize); void *ptr = acm_mem_alloc_data(sizeVal); acm_mem_alloc_info(\"<data>\", ptr, sizeVal, \"/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_KernelLibs/common/LibCall.c\", 22, __func__); ptr; })"
+ "com.apple.CoreLocation.PrivateMode"
+ "com.apple.QuartzCore.global-capture"
+ "com.apple.QuartzCore.secure-capture"
+ "com.apple.QuartzCore.secure-mode"
+ "com.apple.accounts.appleaccount.fullaccess"
+ "com.apple.avfoundation.allow-capture-filter-rendering"
+ "com.apple.avfoundation.allow-still-image-capture-shutter-sound-manipulation"
+ "com.apple.backboardd.debugapplications"
+ "com.apple.backboardd.launchapplications"
+ "com.apple.basebandd.xpc.allow"
+ "com.apple.camera.iokit-user-access"
+ "com.apple.coretelephony.Identity.get"
+ "com.apple.cs-auxiliary-info"
+ "com.apple.diagnosticd.diagnostic"
+ "com.apple.dt.Xcode"
+ "com.apple.gcore"
+ "com.apple.hfs"
+ "com.apple.keystore.access-keychain-keys"
+ "com.apple.keystore.auth-token"
+ "com.apple.keystore.device"
+ "com.apple.keystore.devicebackup"
+ "com.apple.keystore.sik.access"
+ "com.apple.keystore.stash.access"
+ "com.apple.locationd.activity"
+ "com.apple.locationd.private_info"
+ "com.apple.migrationBaseSystemShove"
+ "com.apple.nvram.boot-args-set-allow"
+ "com.apple.private.CallHistory.read"
+ "com.apple.private.MobileContainerManager.allowed"
+ "com.apple.private.MobileGestalt.AllowProtectedKeys"
+ "com.apple.private.accounts.allaccounts"
+ "com.apple.private.amfi.can-check-trust-cache"
+ "com.apple.private.apfs.revert-to-snapshot"
+ "com.apple.private.assetsd.nebulad.access"
+ "com.apple.private.avfoundation.capture.nonstandard-client.allow"
+ "com.apple.private.cloudkit.spi"
+ "com.apple.private.contacts"
+ "com.apple.private.corespotlight.receiver"
+ "com.apple.private.email"
+ "com.apple.private.hid.manager.client"
+ "com.apple.private.kernel.system-override"
+ "com.apple.private.mediaexperience.suppressrecordingstatetosystemstatus"
+ "com.apple.private.osanalytics.defaults.allow"
+ "com.apple.private.osanalytics.defaults.read-all.allow"
+ "com.apple.private.photoanalysisd.access"
+ "com.apple.private.security.container-manager"
+ "com.apple.private.security.disk-device-access"
+ "com.apple.private.security.no-container"
+ "com.apple.private.security.no-sandbox"
+ "com.apple.private.security.storage-exempt.heritable"
+ "com.apple.private.security.storage.AppBundles"
+ "com.apple.private.security.storage.DiagnosticReports.read-write"
+ "com.apple.private.security.storage.Messages"
+ "com.apple.private.security.storage.Photos"
+ "com.apple.private.security.storage.trustd-private"
+ "com.apple.private.set-exception-port"
+ "com.apple.private.system-keychain"
+ "com.apple.private.tcc.allow.overridable"
+ "com.apple.private.thread-set-state"
+ "com.apple.private.uninstall.deletion"
+ "com.apple.private.vfs.snapshot"
+ "com.apple.quicklook.qlmanage"
+ "com.apple.sh"
+ "com.apple.ssh"
+ "com.apple.ssh-add"
+ "com.apple.suggest_tool"
+ "com.apple.vpn.installer_events"
+ "com.apple.wifi.manager-access"
+ "com.apple.wlan.authentication"
+ "copyOSEntitlements"
+ "der_decode_entitlements"
+ "der_decode_numeric_string"
+ "der_decode_utc_time"
+ "der_vm_container_from_context"
+ "evaluateLibraryLoadConstraintOnLibrary() could not copy out error msg '%s', error: %d"
+ "evaluateLibraryLoadConstraintOnProcess() could not copy out error msg '%s', error: %d"
+ "getOSEntitlements"
+ "getOSEntitlementsFromProcSecure"
+ "initUDIDEnforcement"
+ "libclang_rt.asan_ios_dynamic"
+ "libclang_rt.lsan_ios_dynamic"
+ "libclang_rt.tsan_ios_dynamic"
+ "libclang_rt.ubsan_ios_dynamic"
+ "libsystem override"
+ "modify-anchor-certificates"
+ "monitor"
+ "numeric string element not allowed"
+ "research_variant"
+ "run-unsigned-code"
+ "site.ACMCredentialRef"
+ "srd_allow_trust_caches_when_locked"
+ "task_for_pid-allow"
+ "trust_level"
+ "unable to create an OSObject for locally signed entitlement"
+ "unable to create an OSString for locally signed entitlement"
+ "unknown"
+ "v16@?0r^{_OSEntitlementsReadOnly=^{OSEntitlements}{_CEContext={_CEContextInfo=CI}{CEQueryContext={der_vm_context=^{CERuntime}{CEAccelerationContext=^{CEAccelerationElement}Q}QBB(?={ccder_read_blob=**}{?=**})}B}}^{_CEContext}*{?=^{__SC_GenericBlob}}{?=BB}}8"
- "\"AMFI: Cannot construct exemption profile.\" @%s:%d"
- "\"AMFI: DER entitlements anomaly in %s\" @%s:%d"
- "\"AMFI: DER entitlements validation anomaly in %s\" @%s:%d"
- "\"AMFI: Invalid context occured, this shouldn't happen\\n\" @%s:%d"
- "\"AMFI: OSEntitlement invariant violation: %d %d %d\\n\" @%s:%d"
- "\"AMFI: OSEntitlements::adjustContextWithMonitor NULL monitor\" @%s:%d"
- "\"AMFI: RO-Allocator mismatch for template and state\" @%s:%d"
- "\"AMFI: While evaluating profile for %s got invalid profile from amfid\\n\" @%s:%d"
- "\"AMFI: XML is larger than uint32_t\" @%s:%d"
- "\"AMFI: XML serialization failed too late in the process\" @%s:%d"
- "\"AMFI::%s passed invalid AMFIEntitlementKey %p\" @%s:%d"
- "\"Couldn't create entitlements context\\n\" @%s:%d"
- "\"Profile has invalid entitlements\\n\" @%s:%d"
- "\"Profile passed by amfid does not authorize the certificate\\n\" @%s:%d"
- "\"entitlements state %p points back to %p instead of %p\\n\" @%s:%d"
- "%08llX-%016llX"
- "%s called with NULL context\n"
- "%s called with NULL proc for entitlement: %s\n"
- "%s: %s disallowed without com.apple.private.security.restricted-application-groups"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_KernelLibs/ACMKernelLib/ACMKernelTransport.cpp"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_KernelLibs/common/CommonMem.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_KernelLibs/common/LibCall.c"
- "20:35:06"
- "<null>"
- "AMFI: %s"
- "AMFI: %s not allowed with Universal Provisioning Profile"
- "AMFI: '%s':invalid entitlement of type '%s' disallowed in local signed code\n"
- "AMFI: Couldn't allocate space for the profile\n"
- "AMFI: Couldn't copy buffer for the profile\n"
- "AMFI: Only launchd can set the system service launch type\n"
- "AMFI: Releasing transmuted blob for %s - %p %dx\n"
- "AMFI: UDID enforcement enabled\n"
- "AMFI: XNU monitor refused profile: %d\n"
- "AMFI: acquired profile with UUID: %.*s\n"
- "AMFI: couldn't serialize XML\n"
- "AMFI: couldn't size deserialize\n"
- "AMFI: couldn't size xml deserialization\n"
- "AMFI: device allowed\n"
- "AMFI: device is provisioned\n"
- "AMFI: device not allowed\n"
- "AMFI: entitlements have been validated\n"
- "AMFI: failed to acquire unmanaged context: %s"
- "AMFI: only sysdiagnose can set the sysdiagnose launch type\n"
- "AMFI: profile has not succesfully validated all entitlements\n"
- "AMFI: profile has successfully validated all entitlements\n"
- "AMFI: profile is not valid for the current platform"
- "AMFI: requested usage of a development profile without developer mode being enabled\n"
- "AMFI: skipping invalid entitlement of type '%s'\n"
- "AMFIEntitlementKeyIsBoolTrue"
- "AMFIEntitlementReleaseKey"
- "AMFIGetQueryContext"
- "B136@?0{?={der_vm_context=^{CERuntime}{CEAccelerationContext=^{CEAccelerationElement}Q}QBB(?={ccder_read_blob=**}{?=**})}{der_vm_context=^{CERuntime}{CEAccelerationContext=^{CEAccelerationElement}Q}QBB(?={ccder_read_blob=**}{?=**})}II^v}8"
- "CEQueryContextToOSDictionary"
- "CoreEntitlements: Couldn't iterate over DER entitlements\n"
- "CoreEntitlements: not a sequence"
- "CoreEntitlements: unknown DER type"
- "Couldn't build index for %s: %s\n"
- "Forcing CS_RUNTIME for entitlement: %s\n"
- "Jan 10 2025"
- "OSX"
- "Platform"
- "Support.c"
- "amfi.osentitlements"
- "amfi_OSEntitlements_copyEntitlementAsOSObjectWithProc"
- "amfi_OSEntitlements_queryEntitlementBooleanWithProc"
- "amfi_OSEntitlements_queryEntitlementStringWithProc"
- "amfi_query_context_to_object_impl"
- "cmd = (acm_command_t *)({ size_t sizeVal = (cmdSize); void *ptr = acm_mem_alloc_data(sizeVal); acm_mem_alloc_info(\"<data>\", ptr, sizeVal, \"/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_KernelLibs/common/LibCall.c\", 22, __func__); ptr; })"
- "com.apple.private.security.restricted-application-groups"
- "copyEntitlementKey"
- "copyEntitlements"
- "evaluateLibraryLoadConstraint() could not copy out error msg '%s', error: %d"
- "getEntitlements"
- "manufacturingCallback"
- "objectForActiveContext"

```
