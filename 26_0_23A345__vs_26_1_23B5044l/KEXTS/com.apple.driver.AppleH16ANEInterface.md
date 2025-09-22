## com.apple.driver.AppleH16ANEInterface

> `com.apple.driver.AppleH16ANEInterface`

```diff

-9.15.2.0.0
-  __TEXT.__const: 0xae8
-  __TEXT.__cstring: 0xede8
-  __TEXT.__os_log: 0x35763
-  __TEXT_EXEC.__text: 0x105670
+9.100.4.0.0
+  __TEXT.__const: 0xb68
+  __TEXT.__cstring: 0xee2c
+  __TEXT.__os_log: 0x35b13
+  __TEXT_EXEC.__text: 0x1062ec
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x3ed4
   __DATA.__common: 0x658
   __DATA.__bss: 0x628
-  __DATA_CONST.__auth_got: 0x968
+  __DATA_CONST.__auth_got: 0x988
   __DATA_CONST.__got: 0x148
   __DATA_CONST.__mod_init_func: 0x248
   __DATA_CONST.__mod_term_func: 0x110
-  __DATA_CONST.__const: 0xc278
-  __DATA_CONST.__kalloc_type: 0x3b40
+  __DATA_CONST.__const: 0xc2f8
+  __DATA_CONST.__kalloc_type: 0x3ac0
   __DATA_CONST.__kalloc_var: 0x3160
-  UUID: 48554E96-403F-3C37-B55D-DC655BE47A33
-  Functions: 3286
+  UUID: 8CD8CCFF-D451-3B36-A68A-8334B623071B
+  Functions: 3295
   Symbols:   0
-  CStrings:  4306
+  CStrings:  4323
 
CStrings:
+ "%s number of buffers（%u) or procID (%u) exceeds max\n"
+ "%s pInputsReady is NULL\n"
+ "%s pOutSetEnqueue is NULL\n"
+ "%s procID (%u) exceeds max\n"
+ "%s setID（%u) or procID (%u) exceeds max\n"
+ "%s: %s: Finished saving ANE Exclave state"
+ "%s: %s: ISP client is not going away... Force-updated its power state before powering OFF the ANE"
+ "%s: %s: No other ANE clients present, continue powering off\n"
+ "%s: %s: PMGR peer EP service NOT FOUND\n"
+ "%s: %s: PearlSEP client going away... can power OFF the ANE, retries=%d\n"
+ "%s: %s: PearlSEP client is not going away... Force-updated its power state before powering OFF the ANE"
+ "%s: %s: numOfNonBlockingInput: %d \n"
+ "%s: %s: pmgrEnableDPEFix PMGR property NOT FOUND\n"
+ "ANE_MemoryMapRequest()"
+ "ApplePMGR"
+ "CreationProperties"
+ "IOSurfaceHostOnly"
+ "[ERROR] %s: %s: Failed to get IOPM sleep assertion\n"
+ "[ERROR] %s: %s: IOSurface(%d) propertyValue is not an OSDictionary\n"
+ "[ERROR] %s: %s: Process freed while waiting for the ANE command - programHandle: 0x%llx, programId: %u, processId: %u, transactionId: 0x%llx"
+ "[ERROR] %s: %s: Program released while waiting for the aneCmdSend\n"
+ "[ERROR] %s: %s: Surface-id:0x%x does not have _kIOSurfaceHostOnly property or _kIOSurfaceHostOnly is false, no ISP surface remap\n"
+ "[ERROR] %s: %s: filePath is NULL or empty\n"
+ "ane_dpe_reset_caicos_enabled_2"
- "%s  :pInputsReady is NULL or number of buffers（%d） exceeds %d\n"
- "%s enqueue output :pOutSetEnqueue is NULL or setID（%d） exceeds %d\n"
- "%s: %s: FW setup for RTGraph failed: %x\n"
- "%s: %s: PearlSEP Client going away... can power OFF the ANE, retries=%d\n"
- "12212211"
- "numOfNonBlockingInput: %d \n"
- "site.ANEFirmwareManager"

```
