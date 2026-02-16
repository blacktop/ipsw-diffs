## com.apple.driver.AppleM68Buttons

> `com.apple.driver.AppleM68Buttons`

```diff

-128.0.0.0.0
-  __TEXT.__cstring: 0x4cc9
-  __TEXT.__const: 0x218
+130.0.0.0.0
+  __TEXT.__cstring: 0x4e79
+  __TEXT.__const: 0x208
   __TEXT.__os_log: 0x61f
-  __TEXT_EXEC.__text: 0x1d54c
+  __TEXT_EXEC.__text: 0x1d028
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xca
   __DATA.__common: 0x88

   __DATA_CONST.__const: 0xbd8
   __DATA_CONST.__kalloc_type: 0x400
   __DATA_CONST.__kalloc_var: 0x14a0
-  UUID: 2ADF74C0-D8F9-3BC7-881D-1595F6CAFA73
-  Functions: 324
+  UUID: 380C9B05-1790-3B84-9BE4-8622D0DBE670
+  Functions: 328
   Symbols:   0
-  CStrings:  624
+  CStrings:  628
 
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
