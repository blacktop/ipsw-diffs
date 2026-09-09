## AppleLockdownMode

> `/System/Library/Extensions/AppleLockdownMode.kext/AppleLockdownMode`

### Sections with Same Size but Changed Content

- `__DATA.__data`
- `__DATA_CONST.__mod_init_func`
- `__DATA_CONST.__mod_term_func`
- `__DATA_CONST.__const`
- `__DATA_CONST.__auth_ptr`

```diff

 128.0.8.0.0
   __TEXT.__const: 0x110
   __TEXT.__cstring: 0x4918
-  __TEXT_EXEC.__text: 0x15180
+  __TEXT_EXEC.__text: 0x1540c
   __TEXT_EXEC.__auth_stubs: 0x220
   __DATA.__data: 0xc6
   __DATA.__common: 0x38
Functions:
~ __ZN17AppleLockdownMode9MetaClassC1Ev : 72 -> 76
~ __ZN17AppleLockdownModeC2EPK11OSMetaClass : 52 -> 56
~ __ZN17AppleLockdownModeC1EPK11OSMetaClass : 52 -> 56
~ __ZN17AppleLockdownModeD0Ev : 68 -> 72
~ __ZN17AppleLockdownMode9MetaClassC2Ev : 72 -> 76
~ __ZNK17AppleLockdownMode9MetaClass5allocEv : 104 -> 108
~ __ZN17AppleLockdownModeC1Ev : 88 -> 92
~ __ZN17AppleLockdownModeC2Ev : 88 -> 92
~ __Z20PlatformSupportsXARTv : 112 -> 116
~ __Z22LDMShouldEnforceParityv : 792 -> 796
~ __Z14LDMCheckParityPv : 248 -> 252
~ __ZN17AppleLockdownMode5startEP9IOService : 208 -> 212
~ _GLOBAL__sub_I_AppleLockdownMode.cpp : 80 -> 84
~ _ACMKernelTransport : 1480 -> 1484
~ _LibCall_BuildCommand : 520 -> 524
~ _LibCall_ACMContextCreate : 964 -> 968
~ _LibCall_ACMContextCreateWithExternalForm : 1012 -> 1016
~ _LibCall_ACMContextDelete : 468 -> 472
~ _LibCall_ACMContexAddCredentialWithScope : 736 -> 740
~ _LibCall_ACMContextContainsCredentialTypeEx : 764 -> 768
~ _LibCall_ACMContexRemoveCredentialsByTypeAndScope : 556 -> 560
~ _LibCall_ACMContextRemoveCredentialsByValueAndScope : 736 -> 740
~ _LibCall_ACMContextVerifyPolicyAndCopyRequirementEx : 1504 -> 1508
~ _LibCall_ACMRequirementDelete : 348 -> 352
~ _LibCall_ACMKernelControl : 564 -> 568
~ _LibCall_ACMCredentialSetProperty : 2684 -> 2688
~ _LibCall_ACMCredentialGetPropertyData : 1876 -> 1880
~ _LibCall_ACMSecContextCopyCredentialsArrayEx : 864 -> 868
~ _LibCall_ACMRequirementGetPropertyData : 1752 -> 1756
~ _LibCall_ACMPing : 392 -> 396
~ _LibCall_ACMKernDoubleClickNotify : 336 -> 340
~ _LibCall_ACMContextCredentialGetProperty : 956 -> 960
~ _LibCall_ACMGlobalContextCredentialGetProperty : 624 -> 628
~ _LibCall_ACMContextVerifyPolicyEx : 332 -> 336
~ _LibCall_ACMSecContextVerifyPolicyAndCopyRequirementEx : 328 -> 332
~ _LibCall_ACMGlobalContextVerifyPolicyEx : 476 -> 480
~ _LibCall_ACMGetEnvironmentVariable : 400 -> 404
~ _LibCall_ACMSetEnvironmentVariable : 800 -> 804
~ _LibCall_ACMTRMLoadState : 396 -> 400
~ _LibCall_ACMTRMSaveState : 444 -> 448
~ _LibCall_ACMContextLoadFromImage : 960 -> 964
~ _LibCall_ACMContextUnloadToImage : 816 -> 820
~ _LibCall_ACMContextSetData : 944 -> 948
~ _LibCall_ACMContextGetData : 876 -> 880
~ _LibCall_ACMContextCopyData : 508 -> 512
~ _LibCall_ACMPublishTrustedAccessories : 664 -> 668
~ _LibCall_ACMContextGetInfo : 624 -> 628
~ _verifyAclConstraintInternal : 1296 -> 1300
~ _LibCall_ACMSecContextProcessAcl : 84 -> 88
~ _processAclCommandInternal : 2528 -> 2532
~ _LibCall_ACMSecContextProcessAclAndCopyAuthMethod : 88 -> 92
~ _LibCall_ACMSecContextVerifyAclConstraintAndCopyRequirement : 564 -> 568
~ _LibCall_ACMSecCredentialProviderEnrollmentStateChangedForUser : 716 -> 720
~ _LibCall_ACMSecSetBuiltinBiometry : 260 -> 264
~ _LibCall_ACMSecSetBiometryAvailability : 492 -> 496
~ _LibCall_ACMSecContextGetUnlockSecret : 964 -> 968
~ _LibCall_ACMSEPControl : 1044 -> 1048
~ _aclRequiresPasscodeInternal : 676 -> 680
~ _acm_mem_alloc_data : 128 -> 132
~ _acm_mem_free_data : 132 -> 136
~ _acm_mem_free_info : 284 -> 288
~ _GetSerializedVerifyPolicySize : 360 -> 364
~ _getLengthOfParameters : 416 -> 420
~ _SerializeVerifyPolicy : 740 -> 744
~ _serializeParameters : 484 -> 488
~ _DeserializeVerifyPolicy : 1052 -> 1056
~ _deserializeParameters : 1016 -> 1020
~ _GetSerializedVerifyAclConstraintSize : 400 -> 404
~ _SerializeVerifyAclConstraint : 728 -> 732
~ _DeserializeVerifyAclConstraint : 1520 -> 1524
~ _GetSerializedProcessAclSize : 376 -> 380
~ _SerializeProcessAcl : 716 -> 720
~ _DeserializeProcessAcl : 1460 -> 1464
~ _GetSerializedRequirementSize : 580 -> 584
~ _SerializeRequirement : 828 -> 832
~ _DeserializeRequirement : 1360 -> 1364
~ _GetSerializedCredentialSize : 220 -> 224
~ _SerializeCredential : 444 -> 448
~ _DeserializeCredential : 1444 -> 1448
~ _CopyCredential : 376 -> 380
~ _CompareCredentials : 780 -> 784
~ _GetSerializedAddCredentialSize : 296 -> 300
~ _SerializeAddCredential : 548 -> 552
~ _DeserializeAddCredential : 508 -> 512
~ _DeserializeAddCredentialType : 156 -> 160
~ _LibSer_GetSerializedContainsCredential_Serialize : 176 -> 180
~ _GetSerializedRemoveCredentialSize : 112 -> 116
~ _SerializeRemoveCredential : 112 -> 116
~ _DeserializeRemoveCredential : 112 -> 116
~ _GetSerializedReplacePassphraseCredentialSize : 112 -> 116
~ _SerializeReplacePassphraseCredential : 112 -> 116
~ _DeserializeReplacePassphraseCredential : 112 -> 116
~ _SerializeCredentialList : 432 -> 436
~ _DeserializeCredentialList : 580 -> 584
~ _DeallocCredentialList : 244 -> 248
~ _SerializeGetContextProperty : 248 -> 252
~ _DeserializeGetContextProperty : 288 -> 292
~ _LibSer_GetAclAuthMethod_Serialize : 244 -> 248
~ _LibSer_GetAclAuthMethod_Deserialize : 192 -> 196
~ _LibSer_ContextCredentialGetProperty_Serialize : 248 -> 252
~ _LibSer_ContextCredentialGetProperty_Deserialize : 288 -> 292
~ _LibSer_ContextCredentialGetPropertyEx_GetSize : 204 -> 208
~ _LibSer_ContextCredentialGetPropertyEx_Serialize : 484 -> 488
~ _LibSer_ContextCredentialGetPropertyEx_Deserialize : 536 -> 540
~ _LibSer_GlobalContextCredentialGetProperty_Serialize : 200 -> 204
~ _LibSer_GlobalContextCredentialGetProperty_Deserialize : 240 -> 244
~ _LibSer_RemoveCredentialByType_Serialize : 248 -> 252
~ _LibSer_RemoveCredentialByType_Deserialize : 288 -> 292
~ _LibSer_DeleteContext_Serialize : 244 -> 248
~ _LibSer_DeleteContext_Deserialize : 192 -> 196
~ _LibSer_StorageAnyCmd_DeserializeCommonFields : 168 -> 172
~ _LibSer_StorageSetData_GetSize : 224 -> 228
~ _LibSer_StorageSetData_Serialize : 564 -> 568
~ _LibSer_StorageSetData_Deserialize : 468 -> 472
~ _LibSer_StorageGetData_GetSize : 196 -> 200
~ _LibSer_StorageGetData_Serialize : 536 -> 540
~ _LibSer_StorageGetData_Deserialize : 320 -> 324
~ _LibSer_GetUnlockSecret_GetSize : 196 -> 200
~ _LibSer_GetUnlockSecret_Serialize : 472 -> 476
~ _LibSer_GetUnlockSecret_Deserialize : 288 -> 292
~ _LibSer_GetUnlockSecretResponse_Serialize : 236 -> 240
~ _LibSer_GetUnlockSecretResponse_Deserialize : 172 -> 176
~ _LibSer_SEPControl_GetSize : 224 -> 228
~ _LibSer_SEPControl_Serialize : 500 -> 504
~ _LibSer_SEPControl_Deserialize : 496 -> 500
~ _LibSer_SEPControlResponse_Serialize : 240 -> 244
~ _LibSer_SEPControlResponse_Deserialize : 288 -> 292
~ _LibSer_ACMDeserializeEnvironmentVariableType : 284 -> 288
~ _LibSer_ACMDeserializeSEPControlCode : 480 -> 484
~ _checkParameter : 812 -> 816
~ _Util_WriteToBuffer : 480 -> 484
~ _Util_ReadFromBuffer : 476 -> 480
~ _Util_DeallocCredential : 1280 -> 1284
~ _Util_AllocCredential : 1212 -> 1216
~ _Util_AllocRequirement : 2004 -> 2008
~ _Util_CreateRequirement : 228 -> 232
~ _Util_DeallocRequirement : 2048 -> 2052
~ _ACMKernContextCreate : 212 -> 216
~ _ACMKernContextCreateWithExternalForm : 220 -> 224
~ _ACMKernContextDelete : 208 -> 212
~ _ACMKernContextAddCredentialWithScope : 216 -> 220
~ _ACMKernGlobalContextAddCredential : 348 -> 352
~ _ACMKernContextRemoveCredentialsByTypeAndScope : 216 -> 220
~ _ACMKernGlobalContextRemoveCredentialsByType : 280 -> 284
~ _ACMKernContextVerifyPolicyAndCopyRequirementEx : 268 -> 272
~ _ACMKernGlobalContextVerifyPolicyAndCopyRequirementEx : 376 -> 380
~ _ACMKernRequirementDelete : 176 -> 180
~ _ACMKernCredentialCreate : 180 -> 184
~ _ACMKernCredentialDelete : 132 -> 136
~ _ACMKernDoubleClickNotify : 184 -> 188
~ _ACMKernPingOnDoubleClick : 188 -> 192
~ _ACMKernControl : 240 -> 244
~ _ACMKernSetEnvironmentVariable : 228 -> 232
~ _ACMKernGetEnvironmentVariable : 216 -> 220
~ _ACMKernContextCredentialGetProperty : 248 -> 252
~ _ACMKernContextSetData : 240 -> 244
~ _ACMKernContextGetData : 532 -> 536
~ _ACMKernContextGetDataProperty : 212 -> 216
~ _Z22LDMShouldEnforceParityv.cold.1 : 452 -> 456
~ _Z22LDMShouldEnforceParityv.cold.2 : 116 -> 120
~ _Z22LDMShouldEnforceParityv.cold.3 : 116 -> 120
~ ACMKernelTransport.cold.1 : 172 -> 176
~ acm_mem_free_data.cold.1 : 88 -> 92
```
