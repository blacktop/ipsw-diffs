## com.apple.driver.AppleH16ANEInterface

> `com.apple.driver.AppleH16ANEInterface`

```diff

-9.10.3.0.0
-  __TEXT.__const: 0xab8
-  __TEXT.__cstring: 0xef03
-  __TEXT.__os_log: 0x34949
-  __TEXT_EXEC.__text: 0x10365c
+9.11.2.0.0
+  __TEXT.__const: 0xac8
+  __TEXT.__cstring: 0xeec5
+  __TEXT.__os_log: 0x34a3b
+  __TEXT_EXEC.__text: 0x103b78
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x39c0
+  __DATA.__data: 0x3a7c
   __DATA.__common: 0x658
   __DATA.__bss: 0x628
   __DATA_CONST.__auth_got: 0x970

   __DATA_CONST.__mod_term_func: 0x110
   __DATA_CONST.__const: 0xc290
   __DATA_CONST.__kalloc_type: 0x3b40
-  __DATA_CONST.__kalloc_var: 0x30c0
-  UUID: 18B59025-A430-32A2-A5E3-FF27EC39EA6A
-  Functions: 3288
+  __DATA_CONST.__kalloc_var: 0x3160
+  UUID: CD2CD7A2-608D-3A5B-BFE5-20B404E90002
+  Functions: 3289
   Symbols:   0
-  CStrings:  4270
+  CStrings:  4267
 
CStrings:
+ "%s: %s: blocked on Fences\n"
+ "%s: %s: op_idx=%d IOIndex = %d symbolIndex=%d liveInParamComputedValue=0x%llx\n"
+ "1112221222222121112211222112221122211222211111222222222222222221112221122211122222222"
+ "ANEExclave_C.c"
+ "AneEngine_C.c"
+ "DisableCPUClocksAndPowerForM11"
+ "[ERROR] %s: %s: Failed allocate a new intermediateUnion result=0x%x\n"
+ "[ERROR] %s: %s: Failed free a new intermediateUnion result=0x%x\n"
+ "[ERROR] %s: %s: Failed to dartMap resources. result=0x%x\n"
+ "[ERROR] %s: %s: Failed to wire resources. result=0x%x\n"
+ "[ERROR] %s: %s: Firmware timeout detected deltaTimeSeconds=%d timeoutInSeconds=%d, opcode=0x%x timestampFW=%lld\n"
+ "[INFO] %s: %s: Free intermediateBuffer(0x%llx) and allocate new one for F2F request\n"
+ "[INFO] %s: %s: Shared intermediateUnion used for F2F requests, allocate a new one\n"
- "%s: %s: Found peer PMGR service. Look for DPR Reset Flag\n"
- "%s: %s: PMGR peer EP service NOT FOUND\n"
- "%s: %s: pmgrSupportsDPEResetUpdate PMGR Found with value: %d\n"
- "%s: %s: pmgrSupportsDPEResetUpdate PMGR property NOT FOUND\n"
- "111222122222212111221122211222112221122221111122222222222222222111222112211122222222"
- "ANEExclaveClient_tightbeam.c"
- "AneEngine_tightbeam.c"
- "ApplePMGR"
- "DisableCPUClocksAndPowerForWatch"
- "[DEBUG] %s: %s: ANEUnionResource: buffer is in use useCount: %u size of IOMD: 0x%llx required resource size: 0x%llx\n"
- "[DEBUG] %s: %s: ANEUnionResource: skip update memoryDescriptor current size (0x%llx) is larger than the required resource size (0x%llx\n)"
- "[ERROR] %s: %s: Failed to allocate ANERequest\n"
- "[ERROR] %s: %s: Failed to dartMap request resources. result=0x%x\n"
- "[ERROR] %s: %s: Failed to wire request resources. result=0x%x\n"
- "[ERROR] %s: %s: Firmware timeout detected deltaTimeSeconds=%d timeoutInSeconds=%d\n"
- "ane_dpe_reset_caicos_enabled"

```
