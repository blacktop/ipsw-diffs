## AppleLockdownMode

> `/System/Library/Extensions/AppleLockdownMode.kext/AppleLockdownMode`

```diff

-80.0.5.0.0
+80.100.8.0.0
   __TEXT.__const: 0x110
-  __TEXT.__cstring: 0x46e2
-  __TEXT_EXEC.__text: 0x1467c
+  __TEXT.__cstring: 0x4892
+  __TEXT_EXEC.__text: 0x15000
   __TEXT_EXEC.__auth_stubs: 0x220
   __DATA.__data: 0xc6
   __DATA.__common: 0x38

   __DATA_CONST.__const: 0x5f0
   __DATA_CONST.__kalloc_type: 0x300
   __DATA_CONST.__kalloc_var: 0x14a0
-  UUID: A181E460-5E79-3724-AAE8-5FCC54BC47C9
-  Functions: 205
-  Symbols:   628
-  CStrings:  490
+  UUID: 6D9615DD-4B94-34A9-B01D-314B3CAFFF25
+  Functions: 211
+  Symbols:   638
+  CStrings:  494
 
Symbols:
+ /Library/Caches/com.apple.xbs/92F74E33-743A-4198-9C27-1F00DDAF8D62/TemporaryDirectory.3M1Y9m/Binaries/LockdownMode/install/TempContent/Objects/LockdownMode.build/AppleLockdownMode.build/DerivedSources/
+ /Library/Caches/com.apple.xbs/92F74E33-743A-4198-9C27-1F00DDAF8D62/TemporaryDirectory.3M1Y9m/Binaries/LockdownMode/install/TempContent/Objects/LockdownMode.build/AppleLockdownMode.build/Objects-normal/arm64e/AppleLockdownMode.o
+ /Library/Caches/com.apple.xbs/92F74E33-743A-4198-9C27-1F00DDAF8D62/TemporaryDirectory.3M1Y9m/Binaries/LockdownMode/install/TempContent/Objects/LockdownMode.build/AppleLockdownMode.build/Objects-normal/arm64e/AppleLockdownMode_info.o
+ /Library/Caches/com.apple.xbs/92F74E33-743A-4198-9C27-1F00DDAF8D62/TemporaryDirectory.3M1Y9m/Binaries/LockdownMode/install/TempContent/Objects/LockdownMode.build/AppleLockdownMode.build/Objects-normal/arm64e/AppleLockdownMode_vers.o
+ /Library/Caches/com.apple.xbs/92F74E33-743A-4198-9C27-1F00DDAF8D62/TemporaryDirectory.3M1Y9m/Sources/LockdownMode/AppleLockdownMode/
+ DeallocCredentialList.kalloc_type_view_1943
+ DeserializeCredentialList.kalloc_type_view_1905
+ LibCall_ACMContextLoadFromImage.kalloc_type_view_1570
+ LibCall_ACMContextLoadFromImage.kalloc_type_view_1631
+ _LibCall_ACMSecContextCopyCredentialsArrayEx
+ _LibCall_ACMSecCredentialsArrayDelete
+ _LibSer_ContextCredentialGetPropertyEx_Deserialize
+ _LibSer_ContextCredentialGetPropertyEx_GetSize
+ _LibSer_ContextCredentialGetPropertyEx_Serialize
+ _OUTLINED_FUNCTION_0
+ deserializeParameters.kalloc_type_view_204
- /Library/Caches/com.apple.xbs/Binaries/LockdownMode/install/TempContent/Objects/LockdownMode.build/AppleLockdownMode.build/DerivedSources/
- /Library/Caches/com.apple.xbs/Binaries/LockdownMode/install/TempContent/Objects/LockdownMode.build/AppleLockdownMode.build/Objects-normal/arm64e/AppleLockdownMode.o
- /Library/Caches/com.apple.xbs/Binaries/LockdownMode/install/TempContent/Objects/LockdownMode.build/AppleLockdownMode.build/Objects-normal/arm64e/AppleLockdownMode_info.o
- /Library/Caches/com.apple.xbs/Binaries/LockdownMode/install/TempContent/Objects/LockdownMode.build/AppleLockdownMode.build/Objects-normal/arm64e/AppleLockdownMode_vers.o
- /Library/Caches/com.apple.xbs/Sources/LockdownMode/AppleLockdownMode/
- DeallocCredentialList.kalloc_type_view_1935
- DeserializeCredentialList.kalloc_type_view_1897
- LibCall_ACMContextLoadFromImage.kalloc_type_view_1479
- LibCall_ACMContextLoadFromImage.kalloc_type_view_1540
- deserializeParameters.kalloc_type_view_196
CStrings:
+ "(ctxImage && ctxImageSize && ctxImageSize <= kACMContextImageMaxSize)"
+ "(data && dataLength && dataLength <= kACMControlMaxDataLength) || (!data && !dataLength)"
+ "(data && dataLength && dataLength <= kACMEnvironmentVariableMaxDataLength) || (!data && !dataLength)"
+ "(enrollmentState && enrollmentStateLength && enrollmentStateLength <= ENROLLMENT_STATE_MAX_SIZE) || (!enrollmentState && !enrollmentStateLength)"
+ "(keybagUuid && keybagUuidLength == UUID_LEN) || (!keybagUuid && !keybagUuidLength)"
+ "(policyLength <= MAX_POLICY_LENGTH)"
+ "(state && stateSize && stateSize <= kACMTRMMultiState_MaxSize) || (!state && !stateSize)"
+ "/Library/Caches/com.apple.xbs/1D43EACD-F3C7-46AB-AD58-2F164BD3EB02/TemporaryDirectory.9X72Ti/Sources/AppleCredentialManager_KernelLibs/ACMKernelLib/ACMKernelLib.cpp"
+ "/Library/Caches/com.apple.xbs/1D43EACD-F3C7-46AB-AD58-2F164BD3EB02/TemporaryDirectory.9X72Ti/Sources/AppleCredentialManager_KernelLibs/ACMKernelLib/ACMKernelTransport.cpp"
+ "/Library/Caches/com.apple.xbs/1D43EACD-F3C7-46AB-AD58-2F164BD3EB02/TemporaryDirectory.9X72Ti/Sources/AppleCredentialManager_KernelLibs/common/CommonMem.c"
+ "/Library/Caches/com.apple.xbs/1D43EACD-F3C7-46AB-AD58-2F164BD3EB02/TemporaryDirectory.9X72Ti/Sources/AppleCredentialManager_KernelLibs/common/CommonUtil.c"
+ "/Library/Caches/com.apple.xbs/1D43EACD-F3C7-46AB-AD58-2F164BD3EB02/TemporaryDirectory.9X72Ti/Sources/AppleCredentialManager_KernelLibs/common/LibCall.c"
+ "/Library/Caches/com.apple.xbs/1D43EACD-F3C7-46AB-AD58-2F164BD3EB02/TemporaryDirectory.9X72Ti/Sources/AppleCredentialManager_KernelLibs/common/LibSerialization.c"
+ "LibCall_ACMSecContextCopyCredentialsArrayEx"
+ "UTIL_OPTIONAL_ARRAY(parameters, parametersCount)"
+ "UTIL_OPTIONAL_BUFFER(outBuffer,outSize)"
+ "accUUIDsSize <= kACMTrustedAccessoriesUUIDsDataMaxSize"
+ "cmd = (acm_command_t *)acm_malloc_data(cmdSize)"
+ "credCount <= MAX_CREDENTIAL_LIST_LEN"
+ "dataLength <= kACMPassphraseMaxLength"
+ "dataLength == DATABASE_HASH_SIZE"
+ "dataLength == SCRED_UUID_SIZE"
+ "dataLength == USER_OUTPUT_HASH_SIZE"
+ "dataLength == USER_OUTPUT_SEID_SIZE"
+ "dataLength == UUID_LEN"
+ "inSize <= kACMContextDataMaxSize"
+ "os_add_overflow((uintptr_t)inBuffer, pos, (uintptr_t *)&readPtr) == 0 "
+ "os_add_overflow((uintptr_t)outBufferOpt, pos, (uintptr_t *)&writePtr) == 0 "
+ "os_add_overflow(pos, inDataSize, &end) == 0 "
+ "os_add_overflow(pos, outDataSize, &end) == 0 "
+ "os_add_overflow(sizeof(acm_command_t), dataSize, &cmdSize) == 0 "
+ "param->parameterDataLength && (param->parameterDataLength <= MAX_ACCESS_GROUPS_LEN)"
+ "param->parameterDataLength <= kACMParameterTypeACLMaxDataLength"
+ "param->parameterDataLength == UUID_LEN"
+ "param->parameterDataLength == sizeof(uint64_t)"
+ "parametersCount <= MAX_PARAMETERS_COUNT"
+ "paramsCount <= MAX_PARAMETERS_COUNT"
+ "policyLength <= MAX_POLICY_LENGTH"
+ "requirement->type == kACMRequirementTypePassphraseEntered"
+ "requirement->type == kACMRequirementTypeSecureIntent"
+ "subreqCount > 0 && subreqCount <= kACMRequirementSubRequirementMaxCount"
- "( ((outSize != nullptr && *outSize > 0) && outBuffer != nullptr) || ((outSize == nullptr || *outSize == 0) && outBuffer == nullptr) )"
- "( (parametersCount > 0 && parameters != ((void*)0)) || ((parametersCount == 0) && parameters == ((void*)0)) )"
- "(ctxImage && ctxImageSize && ctxImageSize <= (4 * 1024))"
- "(data && dataLength && dataLength <= 128) || (!data && !dataLength)"
- "(data && dataLength && dataLength <= 4096) || (!data && !dataLength)"
- "(enrollmentState && enrollmentStateLength && enrollmentStateLength <= (32 + (5 * 16))) || (!enrollmentState && !enrollmentStateLength)"
- "(keybagUuid && keybagUuidLength == 16) || (!keybagUuid && !keybagUuidLength)"
- "(policyLength <= 128)"
- "(state && stateSize && stateSize <= 8192) || (!state && !stateSize)"
- "/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_KernelLibs/ACMKernelLib/ACMKernelLib.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_KernelLibs/ACMKernelLib/ACMKernelTransport.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_KernelLibs/common/CommonMem.c"
- "/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_KernelLibs/common/CommonUtil.c"
- "/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_KernelLibs/common/LibCall.c"
- "/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_KernelLibs/common/LibSerialization.c"
- "__os_warn_unused(__builtin_add_overflow(((uintptr_t)inBuffer), (pos), ((uintptr_t *)&readPtr))) == 0 "
- "__os_warn_unused(__builtin_add_overflow(((uintptr_t)outBufferOpt), (pos), ((uintptr_t *)&writePtr))) == 0 "
- "__os_warn_unused(__builtin_add_overflow((pos), (inDataSize), (&end))) == 0 "
- "__os_warn_unused(__builtin_add_overflow((pos), (outDataSize), (&end))) == 0 "
- "__os_warn_unused(__builtin_add_overflow((sizeof(acm_command_t)), (dataSize), (&cmdSize))) == 0 "
- "accUUIDsSize <= (16 * 16)"
- "cmd = (acm_command_t *)({ size_t sizeVal = (cmdSize); void *ptr = acm_mem_alloc_data(sizeVal); acm_mem_alloc_info(\"<data>\", ptr, sizeVal, \"/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_KernelLibs/common/LibCall.c\", 22, __func__); ptr; })"
- "credCount <= 1000"
- "dataLength <= 128"
- "dataLength == 16"
- "dataLength == 24"
- "dataLength == 32"
- "inSize <= (3*1024 + 512)"
- "param->parameterDataLength && (param->parameterDataLength <= 1000)"
- "param->parameterDataLength <= 1024"
- "param->parameterDataLength == 16"
- "parametersCount <= 10"
- "paramsCount <= 10"
- "paramsLength"
- "policyLength <= 128"
- "requirement->type == kACMCredentialTypePassphraseEntered"
- "subreqCount > 0 && subreqCount <= 10"

```
