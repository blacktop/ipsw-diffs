## com.apple.driver.AppleH16ANEInterface

> `com.apple.driver.AppleH16ANEInterface`

```diff

-9.100.0.0.0
+9.101.0.0.0
   __TEXT.__const: 0xaf8
-  __TEXT.__cstring: 0xedec
-  __TEXT.__os_log: 0x35a7d
-  __TEXT_EXEC.__text: 0x1060d0
+  __TEXT.__cstring: 0xee1f
+  __TEXT.__os_log: 0x35d44
+  __TEXT_EXEC.__text: 0x106710
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x3eb4
+  __DATA.__data: 0x3ed4
   __DATA.__common: 0x658
   __DATA.__bss: 0x628
-  __DATA_CONST.__auth_got: 0x970
+  __DATA_CONST.__auth_got: 0x988
   __DATA_CONST.__got: 0x148
   __DATA_CONST.__mod_init_func: 0x248
   __DATA_CONST.__mod_term_func: 0x110
   __DATA_CONST.__const: 0xc2f8
   __DATA_CONST.__kalloc_type: 0x3ac0
   __DATA_CONST.__kalloc_var: 0x3160
-  UUID: F559A7A5-4A12-32A0-B652-18EA8B7538B9
-  Functions: 3295
+  UUID: D2BB6904-61AF-3979-B6CC-AA7680994035
+  Functions: 3296
   Symbols:   0
-  CStrings:  4317
+  CStrings:  4328
 
CStrings:
+ "%s: %s: Cleaning up partially created programHandle: 0x%llx due to failure\n"
+ "%s: %s: PMGR peer EP service NOT FOUND\n"
+ "%s: %s: numOfNonBlockingInput: %d \n"
+ "%s: %s: pmgrEnableDPEFix PMGR property NOT FOUND\n"
+ "ANE_MemoryMapRequest()"
+ "ApplePMGR"
+ "[ERROR] %s: %s: Bailing out of ANE_ProgramCreate_gated due to failure on ANE%d\n"
+ "[ERROR] %s: %s: Error: could not find programResource\n"
+ "[ERROR] %s: %s: Error: no programANEMap\n"
+ "[ERROR] %s: %s: Error: programBuffers array NULL\n"
+ "[ERROR] %s: %s: Failed to allocate memory for programANEMap->clients\n"
+ "[ERROR] %s: %s: Failed to allocate memory for programANEMap->fPendingRequests\n"
+ "[ERROR] %s: %s: Failed to allocated mmmory for ANEDriverClientContext\n"
+ "[ERROR] %s: %s: Failed to allocated mmmory for fProgramList\n"
+ "[ERROR] %s: %s: Failed to get IOPM sleep assertion\n"
+ "[ERROR] %s: %s: osProgramMap is NULL\n"
+ "[ERROR] %s: %s: program size from ANE is invalid clientProgramSize: %ld, modelSizeLimitForClient: %llu, fANEMaxSystemMemSize: %llu\n"
+ "[ERROR] %s: %s: programANEMap is NULL\n"
+ "ane_dpe_reset_caicos_enabled_2"
- "%s: %s: Error: could not find programResource\n"
- "%s: %s: Error: no programANEMap\n"
- "%s: %s: Error: programBuffers array NULL\n"
- "%s: %s: osProgramMap is NULL\n"
- "%s: %s: programANEMap is NULL\n"
- "ProgramAbort"
- "[ERROR] %s: %s: program size from ANE is invalid = %ld\n"
- "numOfNonBlockingInput: %d \n"

```
