## com.apple.driver.AppleM68Buttons

> `com.apple.driver.AppleM68Buttons`

```diff

 126.0.0.0.0
   __TEXT.__cstring: 0x4af1
-  __TEXT.__const: 0x140
+  __TEXT.__const: 0x148
   __TEXT.__os_log: 0x606
-  __TEXT_EXEC.__text: 0x1c744
+  __TEXT_EXEC.__text: 0x1c830
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xca
   __DATA.__common: 0x90

   __DATA_CONST.__const: 0x12b0
   __DATA_CONST.__kalloc_type: 0x400
   __DATA_CONST.__kalloc_var: 0x1400
-  UUID: E23AD890-5767-3D48-BAFC-E8475F658F89
-  Functions: 315
-  Symbols:   939
+  UUID: 3D4636B6-29E4-3C05-9428-438701DBCFBD
+  Functions: 317
+  Symbols:   948
   CStrings:  603
 
Symbols:
+ ACMKernelTransport.cold.1
+ _OUTLINED_FUNCTION_0
+ _OUTLINED_FUNCTION_1
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_7
+ _OUTLINED_FUNCTION_8
+ _ZN15AppleM68Buttons13setPropertiesEP8OSObject.cold.1
+ _ZN15AppleM68Buttons23_handle_nvram_sync_callEPv.cold.1
+ _ZN15AppleM68Buttons23_handle_nvram_sync_callEPv.cold.2
+ _ZN26AppleTimerQueueEventSource10setTimeoutEjjPv.cold.1
+ __MergedGlobals
+ acm_mem_free_data.cold.1
- LibCall_ACMKernelControl.cold.1
- LibCall_ACMSetEnvironmentVariable.cold.1
- LibCall_ACMSetEnvironmentVariable.cold.2
- LibCall_ACMSetEnvironmentVariable.cold.3
- __ZL15kButtonNameMenu
- __ZL16kButtonNamePower
- __isNullOrEqualMem2
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_KernelLibs/ACMKernelLib/ACMKernelLib.cpp"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_KernelLibs/ACMKernelLib/ACMKernelTransport.cpp"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_KernelLibs/common/CommonMem.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_KernelLibs/common/CommonUtil.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_KernelLibs/common/LibCall.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_KernelLibs/common/LibSerialization.c"
+ "cmd = (acm_command_t *)({ size_t sizeVal = (cmdSize); void *ptr = acm_mem_alloc_data(sizeVal); acm_mem_alloc_info(\"<data>\", ptr, sizeVal, \"/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_KernelLibs/common/LibCall.c\", 22, __func__); ptr; })"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_KernelLibs/ACMKernelLib/ACMKernelLib.cpp"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_KernelLibs/ACMKernelLib/ACMKernelTransport.cpp"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_KernelLibs/common/CommonMem.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_KernelLibs/common/CommonUtil.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_KernelLibs/common/LibCall.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_KernelLibs/common/LibSerialization.c"
- "cmd = (acm_command_t *)({ size_t sizeVal = (cmdSize); void *ptr = acm_mem_alloc_data(sizeVal); acm_mem_alloc_info(\"<data>\", ptr, sizeVal, \"/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_KernelLibs/common/LibCall.c\", 22, __func__); ptr; })"

```
