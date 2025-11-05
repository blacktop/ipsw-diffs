## com.apple.driver.AppleCredentialManager

> `com.apple.driver.AppleCredentialManager`

```diff

-758.80.2.0.0
-  __TEXT.__cstring: 0x16ad5
-  __TEXT.__const: 0x378
-  __TEXT_EXEC.__text: 0x67e50
+758.100.60.0.0
+  __TEXT.__cstring: 0x170bc
+  __TEXT.__const: 0x3e8
+  __TEXT_EXEC.__text: 0x6a4c0
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x34c1
+  __DATA.__data: 0x35d1
   __DATA.__common: 0x1d8
-  __DATA.__bss: 0x25d1
+  __DATA.__bss: 0x25c9
   __DATA_CONST.__auth_got: 0x330
   __DATA_CONST.__got: 0xb8
   __DATA_CONST.__auth_ptr: 0x10

   __DATA_CONST.__const: 0x2de8
   __DATA_CONST.__kalloc_type: 0x780
   __DATA_CONST.__kalloc_var: 0x1450
-  UUID: 984AB73C-86EE-3623-A852-EB8C89BBA29D
-  Functions: 1135
-  Symbols:   1860
-  CStrings:  2450
+  UUID: D9831B98-CF25-3EDB-B970-799DC25E4EA1
+  Functions: 1163
+  Symbols:   1882
+  CStrings:  2479
 
Symbols:
+ ACMKernelTransport.cold.1
+ AttestationFromRequirement.cold.1
+ AuthMethod_EncodeToDER.cold.1
+ CredSet_FindCredSetEntry.cold.1
+ InitCredentialEngine.kalloc_type_view_10560
+ InitCredentialEngine.kalloc_type_view_10663
+ ProcessAcl.cold.1
+ Timer_GetRemainingTimeAndState.cold.1
+ Timer_RestartTimerAtTime.cold.1
+ Timer_Stop.cold.1
+ _DataProvider_Epoch
+ _OUTLINED_FUNCTION_0
+ _OUTLINED_FUNCTION_1
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_6
+ _ZN16ACMKernelService11isProdFusedEv.cold.1
+ _ZN16ACMKernelService16checkEntitlementEP4taskPKc.cold.1
+ _ZN16ACMRMEnvironment15validateOrPanicENS_7BoolKeyE.cold.1
+ _ZN16ACMRMEnvironment15validateOrPanicENS_9UInt32KeyE.cold.1
+ _ZN22AppleCredentialManager14getSEPEndpointEv.cold.1
+ _ZN22AppleCredentialManager14getSEPEndpointEv.cold.2
+ _ZN22AppleCredentialManager15resetOOLBuffersEv.cold.1
+ _ZN30ACMRestrictedModeKernelService28_onDaemonStartedInBaseSystemEv.cold.1
+ __MergedGlobals
+ __ZL20loadValueFromBootArgR16ACMRMEnvironmentNS_9UInt32KeyEPKc
+ __ZL20loadValueFromEDTPropR16ACMRMEnvironmentNS_9UInt32KeyEPKcS3_
+ __ZN14ACMKernelUtils18initU32FromBootArgEPKcj
+ __ZN14ACMKernelUtils18initU32FromEDTPropEPKcS1_j
+ __ZN16ACMRMEnvironment11setBootModeENS_8BootModeE
+ __ZN16ACMRMEnvironment15validateOrPanicENS_7BoolKeyE
+ __ZN16ACMRMEnvironment15validateOrPanicENS_9UInt32KeyE
+ __ZN16ACMRMEnvironment3setENS_7BoolKeyEb
+ __ZN16ACMRMEnvironment3setENS_9UInt32KeyEj
+ __ZN16ACMRMEnvironment5resetEv
+ __ZN30ACMRestrictedModeKernelService19_onEnvSetPolicyModeEjPbb
+ __ZN30ACMRestrictedModeKernelService19_onEnvSetTRMProfileEjPbb
+ __ZN30ACMRestrictedModeKernelService19_startTRMEnrollmentEv
+ __ZN30ACMRestrictedModeKernelService20_finishTRMEnrollmentEv
+ __ZN30ACMRestrictedModeKernelService21_startHIDRMEnrollmentEv
+ __ZN30ACMRestrictedModeKernelService22_finishHIDRMEnrollmentEv
+ __ZN30ACMRestrictedModeKernelService23_onEnvSetTRMGracePeriodEjPbb
+ __ZN30ACMRestrictedModeKernelService24_onEnvSetTRMGlobalSwitchEjPbb
+ __ZN30ACMRestrictedModeKernelService26_onEnvSetHIDRMGlobalSwitchEjPbb
+ __ZN30ACMRestrictedModeKernelService44_onEnvSetDoPolicyRefreshUsingTRMGlobalSwitchEb
+ __ZN39ACMRestrictedModeAnalyticsKernelService14setEnvironmentEP16ACMRMEnvironment
+ __ZNK16ACMRMEnvironment11getBootModeEv
+ __ZNK16ACMRMEnvironment12getOrDefaultENS_9UInt32KeyEj
+ __ZNK16ACMRMEnvironment19isInRecoverySessionEv
+ __ZNK16ACMRMEnvironment21isInBaseSystemSessionEv
+ __ZNK16ACMRMEnvironment2isENS_7BoolKeyE
+ __ZNK16ACMRMEnvironment3getENS_9UInt32KeyE
+ __ZNK16ACMRMEnvironment41isTRMEnabledByDeviceTreeOrBootArgOverrideEv
+ __ZNK16ACMRMEnvironment43isHIDRMEnabledByDeviceTreeOrBootArgOverrideEv
+ __ZNK16ACMRMEnvironment5isSetENS_9UInt32KeyE
+ __ZNK30ACMRestrictedModeKernelService13_publishHIDRMEPKc
+ __ZNK30ACMRestrictedModeKernelService19_onEnvGetPolicyModeEPj
+ __ZNK30ACMRestrictedModeKernelService20_getHIDRMStatusFlagsEv
+ __ZNK30ACMRestrictedModeKernelService22_isTRMEnrollmentNeededEPK22ACMTRMPersistentPolicy
+ __ZNK30ACMRestrictedModeKernelService24_isHIDRMEnrollmentNeededEPK22ACMTRMPersistentPolicy
+ __ZNK30ACMRestrictedModeKernelService25_getHIDRMDisablementFlagsEv
+ __ZNK30ACMRestrictedModeKernelService29_isHIDRMEnabledByGlobalSwitchEv
+ __ZNK30ACMRestrictedModeKernelService31_getHIDRMDisablementFlagsAtBootEv
+ __ZNK30ACMRestrictedModeKernelService36_onEnvGetPolicyModePresentationFlagsEPj
+ __ZNK30ACMRestrictedModeKernelService9_onEnvGetE12ACMTRMEnvKeyPj
+ __ZZNK30ACMRestrictedModeKernelService17_mapAndPublishTRMERKNS_17IOStateChangeListEE8curState
+ __ZZNK30ACMRestrictedModeKernelService17_mapAndPublishTRMERKNS_17IOStateChangeListEE8trmState
+ ___acm_der_key_acl_param_up_offwrist_acc
+ _acm_der_key_acl_param_up_offwrist_acc
+ _findValidCredential.cold.1
+ acm_mem_free_data.cold.1
+ addCredential.cold.1
+ addCredential.cold.2
+ addCredential.cold.3
+ addCredential.cold.4
+ copyCredentials.kalloc_type_view_9031
+ createCredentialSet.kalloc_type_view_2430
+ createCredentialSet.kalloc_type_view_2471
+ deleteCredentialSetEntry.kalloc_type_view_1367
+ findValidCredential.cold.1
+ removeCredEntryFromListDealloc.kalloc_type_view_961
+ removeCredential.cold.1
+ verifyIDVRequirement.cold.1
+ verifyIDVRequirement.cold.2
- InitCredentialEngine.kalloc_type_view_10542
- InitCredentialEngine.kalloc_type_view_10639
- LibCall_ACMKernelControl.cold.1
- LibCall_ACMSetEnvironmentVariable.cold.1
- LibCall_ACMSetEnvironmentVariable.cold.2
- LibCall_ACMSetEnvironmentVariable.cold.3
- TRMMultiState_ReadFromBuffer.cold.1
- TRMMultiState_ReadFromBuffer.cold.2
- _ZN17ACMTRMEnvironment15validateOrPanicENS_7BoolKeyE.cold.1
- _ZZNK30ACMRestrictedModeKernelService17_mapAndPublishTRMERKNS_17IOStateChangeListEE8curState.0
- _ZZNK30ACMRestrictedModeKernelService17_mapAndPublishTRMERKNS_17IOStateChangeListEE8curState.1
- _ZZNK30ACMRestrictedModeKernelService17_mapAndPublishTRMERKNS_17IOStateChangeListEE8curState.10
- _ZZNK30ACMRestrictedModeKernelService17_mapAndPublishTRMERKNS_17IOStateChangeListEE8curState.11
- _ZZNK30ACMRestrictedModeKernelService17_mapAndPublishTRMERKNS_17IOStateChangeListEE8curState.12
- _ZZNK30ACMRestrictedModeKernelService17_mapAndPublishTRMERKNS_17IOStateChangeListEE8curState.13
- _ZZNK30ACMRestrictedModeKernelService17_mapAndPublishTRMERKNS_17IOStateChangeListEE8curState.14
- _ZZNK30ACMRestrictedModeKernelService17_mapAndPublishTRMERKNS_17IOStateChangeListEE8curState.15
- _ZZNK30ACMRestrictedModeKernelService17_mapAndPublishTRMERKNS_17IOStateChangeListEE8curState.2
- _ZZNK30ACMRestrictedModeKernelService17_mapAndPublishTRMERKNS_17IOStateChangeListEE8curState.3
- _ZZNK30ACMRestrictedModeKernelService17_mapAndPublishTRMERKNS_17IOStateChangeListEE8curState.4
- _ZZNK30ACMRestrictedModeKernelService17_mapAndPublishTRMERKNS_17IOStateChangeListEE8curState.5
- _ZZNK30ACMRestrictedModeKernelService17_mapAndPublishTRMERKNS_17IOStateChangeListEE8curState.6
- _ZZNK30ACMRestrictedModeKernelService17_mapAndPublishTRMERKNS_17IOStateChangeListEE8curState.7
- _ZZNK30ACMRestrictedModeKernelService17_mapAndPublishTRMERKNS_17IOStateChangeListEE8curState.8
- _ZZNK30ACMRestrictedModeKernelService17_mapAndPublishTRMERKNS_17IOStateChangeListEE8curState.9
- _ZZNK30ACMRestrictedModeKernelService17_mapAndPublishTRMERKNS_17IOStateChangeListEE8trmState.0
- _ZZNK30ACMRestrictedModeKernelService17_mapAndPublishTRMERKNS_17IOStateChangeListEE8trmState.1
- _ZZNK30ACMRestrictedModeKernelService17_mapAndPublishTRMERKNS_17IOStateChangeListEE8trmState.10
- _ZZNK30ACMRestrictedModeKernelService17_mapAndPublishTRMERKNS_17IOStateChangeListEE8trmState.11
- _ZZNK30ACMRestrictedModeKernelService17_mapAndPublishTRMERKNS_17IOStateChangeListEE8trmState.12
- _ZZNK30ACMRestrictedModeKernelService17_mapAndPublishTRMERKNS_17IOStateChangeListEE8trmState.13
- _ZZNK30ACMRestrictedModeKernelService17_mapAndPublishTRMERKNS_17IOStateChangeListEE8trmState.14
- _ZZNK30ACMRestrictedModeKernelService17_mapAndPublishTRMERKNS_17IOStateChangeListEE8trmState.15
- _ZZNK30ACMRestrictedModeKernelService17_mapAndPublishTRMERKNS_17IOStateChangeListEE8trmState.2
- _ZZNK30ACMRestrictedModeKernelService17_mapAndPublishTRMERKNS_17IOStateChangeListEE8trmState.3
- _ZZNK30ACMRestrictedModeKernelService17_mapAndPublishTRMERKNS_17IOStateChangeListEE8trmState.4
- _ZZNK30ACMRestrictedModeKernelService17_mapAndPublishTRMERKNS_17IOStateChangeListEE8trmState.5
- _ZZNK30ACMRestrictedModeKernelService17_mapAndPublishTRMERKNS_17IOStateChangeListEE8trmState.6
- _ZZNK30ACMRestrictedModeKernelService17_mapAndPublishTRMERKNS_17IOStateChangeListEE8trmState.7
- _ZZNK30ACMRestrictedModeKernelService17_mapAndPublishTRMERKNS_17IOStateChangeListEE8trmState.8
- _ZZNK30ACMRestrictedModeKernelService17_mapAndPublishTRMERKNS_17IOStateChangeListEE8trmState.9
- __ZN14ACMKernelUtils23initValueFromBootArgU32EPKcj
- __ZN14ACMKernelUtils26initValueFromDTPropertyU32EPKcS1_j
- __ZN17ACMTRMEnvironment11setBootModeENS_8BootModeE
- __ZN17ACMTRMEnvironment15validateOrPanicENS_7BoolKeyE
- __ZN17ACMTRMEnvironment3setENS_7BoolKeyEb
- __ZN17ACMTRMEnvironment5resetEv
- __ZN30ACMRestrictedModeKernelService16_startEnrollmentEv
- __ZN30ACMRestrictedModeKernelService17_finishEnrollmentEv
- __ZN30ACMRestrictedModeKernelService9_onEnvGetE12ACMTRMEnvKeyPj
- __ZN39ACMRestrictedModeAnalyticsKernelService14setEnvironmentEP17ACMTRMEnvironment
- __ZNK17ACMTRMEnvironment11getBootModeEv
- __ZNK17ACMTRMEnvironment19isInRecoverySessionEv
- __ZNK17ACMTRMEnvironment21isInBaseSystemSessionEv
- __ZNK17ACMTRMEnvironment2isENS_7BoolKeyE
- __ZNK30ACMRestrictedModeKernelService19_isEnrollmentNeededEPK22ACMTRMPersistentPolicy
- __ZNK30ACMRestrictedModeKernelService21_loadEnabledByDefaultEv
- __ZNK30ACMRestrictedModeKernelService25_queryEnabledByDeviceTreeEv
- __ZNK30ACMRestrictedModeKernelService28_loadAllPolicyModesSupportedEv
- __ZNK30ACMRestrictedModeKernelService32_loadPolicySupportedInBaseSystemEv
- __credentialStore
- __credentialsAllocatedMemory
- __envTableIsSynced
- __isNullOrEqualMem2
- __lockerInterface
- copyCredentials.kalloc_type_view_9013
- createCredentialSet.kalloc_type_view_2428
- createCredentialSet.kalloc_type_view_2469
- deleteCredentialSetEntry.kalloc_type_view_1365
- removeCredEntryFromListDealloc.kalloc_type_view_959
- verifyConstraintKeyRef.cold.1
CStrings:
+ "!_env.is(ACMRMEnvironment::boBaseSystemBooted)"
+ "!_env.is(ACMRMEnvironment::boBaseSystemExited)"
+ "!_env.is(ACMRMEnvironment::boRecoveryEntered)"
+ "\"ACM: UInt32Key(%u) out of range!\" @%s:%d"
+ "\"ACM: Unexpected boot flow - ACM BaseSystem daemon started before ACMTRMBaseSystemBootedWithBootMode() xcdis call!\" @%s:%d"
+ "%s: %s: %s %s(%u) HIDRM=%s.\n"
+ "%s: %s: ACM: Unexpected boot flow - ACM BaseSystem daemon started before ACMTRMBaseSystemBootedWithBootMode() xcdis call!.\n"
+ "%s: %s: BaseSystem booted (bootMode='%s') - TRM disabled, TRM won't start in BS.\n"
+ "%s: %s: BaseSystem booted (bootMode='%s') - TRM enabled, TRM will start from BS daemon.\n"
+ "%s: %s: BaseSystem exited - TRM already started in BS.\n"
+ "%s: %s: BaseSystem exited - TRM enabled, TRM will start from daemon.\n"
+ "%s: %s: LocationBasedTrustComputer policy is not available on this platform.\n"
+ "%s: %s: TRM profile changed: %s(%u) -> %s(%u), clearCache=%s.\n"
+ "%s: %s: The UPP/SecureChannel is not supported. Epoch is unavailable.\n"
+ "%s: %s: UInt32Key(%u) out of range!.\n"
+ "%s: %s: [TRM ENABLED=%s] (mask=%x, DISABLED BY: Def=%s%s Arg=%s%s HW=%s%s DT=%s%s Env=%s%s Ext=%s%s Dev=%s%s SEP=%s%s SR=%s%s | MC=%s%s DW=%s%s CB=%s%s GS=%s%s CP=%s%s BS=%s%s MB=%s%s SC=%s%s AS=%s%s IB=%s%s DM=%s%s).\n"
+ "%s: %s: caller=%s ver=%u flg=%x gSw=%u GP=%u Pro=%u iPro=%u hSw=%u.\n"
+ "%s: %s: enrollmentReason: OSX=YES eraseInstall=%s updateFromPreTRMSystem=%s.\n"
+ "%s: %s: enrollmentReason: eraseInstall=%s updateFromPreHIDRMSystem=%s.\n"
+ "%s: %s: exiting with no task.\n"
+ "%s: %s: get Env(%u) failed: unknown key.\n"
+ "%s: %s: get Env(%u) succeeded -> %u.\n"
+ "%s: %s: returning, err = %ld, get Env(%u) failed.\n"
+ "%s: %s: returning, err = %ld, set Env(%u)=%u failed.\n"
+ "%s: %s: sending kIOMessageServicePropertyChange(#changes=%u) while %s(%u), TRM: %u/%c(%u) %u/%c(%u) M=%u/%u/%u %s(%u)/%s(%u) L=%u BS=%u R=%u RP=%u/%u UP=%u/%u HID=%u, CUR: %c(%u) %c(%u).\n"
+ "%s: %s: sent kACMHIDRMMessage_EnrollmentPending() 0x%x -> 0x%x.\n"
+ "%s: %s: set Env(%u)=%u failed: read-only.\n"
+ "%s: %s: set Env(%u)=%u failed: unknown key.\n"
+ "%s: %s: set Env(%u)=%u succeeded (valueChanged=%s).\n"
+ "%s: %s: unexpected PolicyMode configuration [TRM Profile: %s(%u), HIDRM GlobalSwitch: %s].\n"
+ "((_persistentConfig.hidrmGlobalSwitch)==(kACMHIDRMConfig_GlobalSwitch_On) || (_persistentConfig.hidrmGlobalSwitch)==(kACMHIDRMConfig_GlobalSwitch_Off))"
+ "((value)==(kACMHIDRMConfig_GlobalSwitch_On) || (value)==(kACMHIDRMConfig_GlobalSwitch_Off))"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_KernelLibs/ACMKernelLib/ACMKernelLib.cpp"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_KernelLibs/ACMKernelLib/ACMKernelTransport.cpp"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_KernelLibs/common/LibCall.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/AppleCredentialManager/ACMKernelUtils.cpp"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/AppleCredentialManager/AppleCredentialManager.cpp"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/AppleCredentialManager/AppleCredentialManagerShared.cpp"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/AppleCredentialManager/AppleCredentialManagerUserClient.cpp"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/AppleCredentialManager/Services/ACMAccessoryCacheKernelService.cpp"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/AppleCredentialManager/Services/ACMBridgeKernelService.cpp"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/AppleCredentialManager/Services/ACMFirstResponderKernelService.cpp"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/AppleCredentialManager/Services/ACMKernelService.cpp"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/AppleCredentialManager/Services/ACMKeybagKernelService.cpp"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/AppleCredentialManager/Services/ACMLockdownModeKernelService.cpp"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/AppleCredentialManager/Services/ACMPersistentStoreKernelService.cpp"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/AppleCredentialManager/Services/ACMRestrictedModeAnalyticsKernelService.cpp"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/AppleCredentialManager/Services/ACMRestrictedModeKernelService.cpp"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/common/CommonMem.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/common/CommonTRMLegacy.h"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/common/CommonUtil.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/common/CoreAuthMethod.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/common/CoreCmd.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/common/CoreCred.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/common/CoreCredSet.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/common/CoreDER.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/common/CoreEnv.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/common/CoreExec.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/common/CorePrague.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/common/CoreReqAlgo.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/common/CoreSEPControl.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/common/CoreStorage.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/common/CoreTRMAccCache.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/common/CoreTRMMultiState.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/common/CoreTimer.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/common/CoreUserIntent.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/common/CoreUtil.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/common/CredUtil.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/common/Credentials.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/common/LibSerialization.c"
+ "/options"
+ "11"
+ "121111112222222222222222222222221223232323232323232323232323232323232323232323232323232323232323232323232323232323232323232323232323232323232323232323232323232323111111121111111111221222222222222222212222222222222222222222222222222222222222"
+ "12111121221112212221112212221112212221112212221112212222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222"
+ "ACMRestrictedModeEnvironment.cpp"
+ "DataProvider_Epoch"
+ "HIDRMGlobalSwitch"
+ "HIDRM_EnrollmentPending"
+ "HIDRM_PolicyEnabled"
+ "LocationBasedTrustComputer"
+ "Mar 19 2025, 21:18:07"
+ "PolicyMode"
+ "TRM profile changed"
+ "TRMGlobalSwitch"
+ "TRMGracePeriod"
+ "TRMProfile"
+ "_finishHIDRMEnrollment"
+ "_finishTRMEnrollment"
+ "_getIOService()->setProperty(\"HIDRM_EnrollmentPending\", value)"
+ "_getIOService()->setProperty(\"HIDRM_PolicyEnabled\", (bool)trmState.hidrmPolicyEnabled)"
+ "_isHIDRMEnrollmentNeeded"
+ "_isTRMEnrollmentNeeded"
+ "_onEnvGetPolicyMode"
+ "_onEnvGetPolicyModePresentationFlags"
+ "_onEnvSetDoPolicyRefreshUsingTRMGlobalSwitch"
+ "_onEnvSetHIDRMGlobalSwitch"
+ "_onEnvSetPolicyMode"
+ "_onEnvSetTRMGlobalSwitch"
+ "_onEnvSetTRMGracePeriod"
+ "_onEnvSetTRMProfile"
+ "_publishHIDRM"
+ "_startHIDRMEnrollment"
+ "_startTRMEnrollment"
+ "cmd = (acm_command_t *)({ size_t sizeVal = (cmdSize); void *ptr = acm_mem_alloc_data(sizeVal); acm_mem_alloc_info(\"<data>\", ptr, sizeVal, \"/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_KernelLibs/common/LibCall.c\", 22, __func__); ptr; })"
+ "hidrm-enabled"
+ "hidrm_default"
+ "hidrm_enabled"
+ "initU32FromBootArg"
+ "initU32FromEDTProp"
+ "stress-rack"
+ "trm_unification"
- " (changed)"
- "!_env.is(ACMTRMEnvironment::bkBaseSystemBooted)"
- "!_env.is(ACMTRMEnvironment::bkBaseSystemExited)"
- "!_env.is(ACMTRMEnvironment::bkRecoveryEntered)"
- "%s: %s: ACM daemon started in BaseSystem....\n"
- "%s: %s: BaseSystem booted (bootMode='%s', enablePolicy=NO) - disabling TRM.\n"
- "%s: %s: BaseSystem booted (bootMode='%s', enablePolicy=YES) - starting TRM.\n"
- "%s: %s: BaseSystem exited (policyAlreadyEnabled=NO) - enabling TRM.\n"
- "%s: %s: BaseSystem exited (policyAlreadyEnabled=YES).\n"
- "%s: %s: [TRM ENABLED=%s] (mask=%x, DISABLED BY: Def=%s%s Arg=%s%s HW=%s%s DT=%s%s Env=%s%s Ext=%s%s Dev=%s%s SEP=%s%s | MC=%s%s DW=%s%s CB=%s%s GS=%s%s CP=%s%s BS=%s%s MB=%s%s SC=%s%s AS=%s%s IB=%s%s DM=%s%s).\n"
- "%s: %s: caller=%s ver=%u gSw=%u GP=%u Pro=%u iPro=%u.\n"
- "%s: %s: clientID=%u enableRM=%s request ignored, reason: policy permanently disabled at boot.\n"
- "%s: %s: denied / read-only Env(%u).\n"
- "%s: %s: enabled: %s (boot-arg=%s edt-prop=%s).\n"
- "%s: %s: enrollmentReason: eraseInstall=%s upgradeFromPreTRMSystem=%s.\n"
- "%s: %s: got Env(%u)=%u.\n"
- "%s: %s: profile changed: %s(%u) -> %s(%u), clearCache=%s.\n"
- "%s: %s: returning, err = %ld, Env(%u).\n"
- "%s: %s: returning, err = %ld, Env(%u)=%u.\n"
- "%s: %s: sending kIOMessageServicePropertyChange(#changes=%u) while %s(%u), TRM: %u/%c(%u) %u/%c(%u) M=%u/%u/%u %s(%u)/%s(%u) L=%u BS=%u R=%u RP=%u/%u UP=%u/%u, CUR: %c(%u) %c(%u).\n"
- "%s: %s: set Env(%u)=%u%s.\n"
- "%s: %s: unhandled Env(%u).\n"
- "-"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/AppleCredentialManager/ACMKernelUtils.cpp"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/AppleCredentialManager/AppleCredentialManager.cpp"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/AppleCredentialManager/AppleCredentialManagerShared.cpp"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/AppleCredentialManager/AppleCredentialManagerUserClient.cpp"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/AppleCredentialManager/Services/ACMAccessoryCacheKernelService.cpp"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/AppleCredentialManager/Services/ACMBridgeKernelService.cpp"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/AppleCredentialManager/Services/ACMFirstResponderKernelService.cpp"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/AppleCredentialManager/Services/ACMKernelService.cpp"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/AppleCredentialManager/Services/ACMKeybagKernelService.cpp"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/AppleCredentialManager/Services/ACMLockdownModeKernelService.cpp"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/AppleCredentialManager/Services/ACMPersistentStoreKernelService.cpp"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/AppleCredentialManager/Services/ACMRestrictedModeAnalyticsKernelService.cpp"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/AppleCredentialManager/Services/ACMRestrictedModeKernelService.cpp"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/common/CommonMem.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/common/CommonTRMLegacy.h"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/common/CommonUtil.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/common/CoreAuthMethod.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/common/CoreCmd.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/common/CoreCred.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/common/CoreCredSet.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/common/CoreDER.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/common/CoreEnv.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/common/CoreExec.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/common/CorePrague.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/common/CoreReqAlgo.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/common/CoreSEPControl.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/common/CoreStorage.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/common/CoreTRMAccCache.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/common/CoreTRMMultiState.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/common/CoreTimer.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/common/CoreUserIntent.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/common/CoreUtil.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/common/CredUtil.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/common/Credentials.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager/common/LibSerialization.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_KernelLibs/ACMKernelLib/ACMKernelLib.cpp"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_KernelLibs/ACMKernelLib/ACMKernelTransport.cpp"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_KernelLibs/common/LibCall.c"
- "10"
- "12111111222221223232323232323232323232323232323232323232323232323232323232323232323232323232323232323232323232323232323232323232323232323232323111111121111111111221222222222222222212222222222222222222222222222222222222222"
- "121111212211122122211122122211122122211122122211122122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222"
- "ACMTRMEnvironment.cpp"
- "GlobalSwitch"
- "Jan  2 2025, 20:37:41"
- "Profile"
- "_finishEnrollment"
- "_isEnrollmentNeeded"
- "_loadAllPolicyModesSupported"
- "_loadEnabledByDefault"
- "_loadPolicySupportedInBaseSystem"
- "_queryEnabledByDeviceTree"
- "_startEnrollment"
- "all policy modes supported"
- "cmd = (acm_command_t *)({ size_t sizeVal = (cmdSize); void *ptr = acm_mem_alloc_data(sizeVal); acm_mem_alloc_info(\"<data>\", ptr, sizeVal, \"/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_KernelLibs/common/LibCall.c\", 22, __func__); ptr; })"
- "enabled by default"
- "initValueFromBootArgU32"
- "initValueFromDTPropertyU32"
- "policy supported in BaseSystem"
- "profile changed"

```
