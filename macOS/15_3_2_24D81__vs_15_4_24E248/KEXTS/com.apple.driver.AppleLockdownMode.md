## com.apple.driver.AppleLockdownMode

> `com.apple.driver.AppleLockdownMode`

```diff

-71.60.2.0.0
+71.100.5.0.0
   __TEXT.__const: 0x40
   __TEXT.__cstring: 0x450a
-  __TEXT_EXEC.__text: 0x13b2c
+  __TEXT_EXEC.__text: 0x13cac
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc6
   __DATA.__common: 0x40

   __DATA_CONST.__const: 0x9b0
   __DATA_CONST.__kalloc_type: 0x300
   __DATA_CONST.__kalloc_var: 0x1400
-  UUID: FD4B60BA-1C87-3B69-8D95-E480CABFC70C
-  Functions: 204
+  UUID: 4B6DDBEB-C336-355F-8001-15D91B0B1C60
+  Functions: 196
   Symbols:   607
   CStrings:  469
 
Symbols:
+ ACMKernelTransport.cold.1
+ _Z22LDMShouldEnforceParityv.cold.1
+ _Z22LDMShouldEnforceParityv.cold.2
+ _Z22LDMShouldEnforceParityv.cold.3
+ acm_mem_free_data.cold.1
- LibCall_ACMKernelControl.cold.1
- LibCall_ACMSetEnvironmentVariable.cold.1
- LibCall_ACMSetEnvironmentVariable.cold.2
- LibCall_ACMSetEnvironmentVariable.cold.3
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
