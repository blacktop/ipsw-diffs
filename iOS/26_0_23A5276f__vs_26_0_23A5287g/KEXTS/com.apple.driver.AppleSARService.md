## com.apple.driver.AppleSARService

> `com.apple.driver.AppleSARService`

```diff

-1377.2.0.0.0
-  __TEXT.__os_log: 0xedb2
+1380.0.0.0.0
+  __TEXT.__os_log: 0xf0f3
   __TEXT.__const: 0xfd8
-  __TEXT.__cstring: 0xd5f8
-  __TEXT_EXEC.__text: 0x70e6c
+  __TEXT.__cstring: 0xd97b
+  __TEXT_EXEC.__text: 0x71e50
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x128
   __DATA.__common: 0x638
   __DATA.__bss: 0x1498
   __DATA_CONST.__auth_got: 0x290
-  __DATA_CONST.__got: 0xa0
+  __DATA_CONST.__got: 0xa8
   __DATA_CONST.__mod_init_func: 0x60
   __DATA_CONST.__mod_term_func: 0x68
-  __DATA_CONST.__const: 0x5810
+  __DATA_CONST.__const: 0x5868
   __DATA_CONST.__kalloc_type: 0x3e00
   __DATA_CONST.__kalloc_var: 0x190
-  UUID: 3761830A-1562-3ADF-B07A-760C52D77B61
-  Functions: 638
+  UUID: D966FE29-FD8E-35AF-B927-9828C2DB7C89
+  Functions: 646
   Symbols:   0
-  CStrings:  1726
+  CStrings:  1756
 
CStrings:
+ "#D: %s::%s:%d: AppleSARFusion: Skipping SPMI coredump due to cleared sar debug boot-arg"
+ "%s::%s:%d: AP has woken up\n"
+ "%s::%s:%d: AP will sleep soon\n"
+ "%s::%s:%d: AppleSARFusion: Triggering SPMI coredump via kernel"
+ "%s::%s:%d: Attaching all interrupt sources due to AP wake\n"
+ "%s::%s:%d: Crashing baseband due to %u failed OCP transactions in a row"
+ "%s::%s:%d: Detaching all interrupt sources due to AP sleep\n"
+ "%s::%s:%d: Failed to crash baseband, continuing with OCP protocol"
+ "%s::%s:%d: Failed to trigger coredump via user client (ret: 0x%x), falling back to kernel method\n"
+ "%s::%s:%d: Invalid user client callback\n"
+ "%s::%s:%d: Invalid user client object\n"
+ "%s::%s:%d: Invalid user client reference\n"
+ "%s::%s:%d: Processing OCP transaction failure (%u failed transactions in a row)"
+ "%s::%s:%d: Received a WAKE_DONE signal from BB when in %s state, drop the signal\n"
+ "%s::%s:%d: Setting ready to fill flag and restoring indicator due to a READY_TO_FILL timeout"
+ "%s::%s:%d: Skipping OCP transaction failure processing due to %s state (AP is asleep or BB is resetting)"
+ "%s::%s:%d: Triggering coredump due to a SPMI error\n"
+ "%s::%s:%d: Triggering coredump via user client\n"
+ "12111112122212121111112112112112112112112112112112112212121111221122"
+ "ABORT"
+ "attachAllInterruptSources"
+ "detachAllInterruptSources"
+ "transactionFailureGated"
+ "triggerCoredump"
+ "triggerCoredumpViaKernel"
+ "triggerCoredumpViaUserClient"
- "#D: %s::%s:%d: AppleSARFusion: Skipping SPMI coredump for release builds"
- "%s::%s:%d: AppleSARFusion: Triggering SPMI coredump"
- "%s::%s:%d: Attaching the interrupt sources after waking up the system\n"
- "%s::%s:%d: Cellular SAR Mode Boost Mode: %s"
- "%s::%s:%d: Detaching the interrupt sources due to sleeping of the system\n"
- "1211111212221212111111211211211211211211211211211211221212111122112"
- "performFeaturesAfterBasebandReset"
- "setCellularSARBoost_block_invoke"
- "triggerSPMICoredump"

```
