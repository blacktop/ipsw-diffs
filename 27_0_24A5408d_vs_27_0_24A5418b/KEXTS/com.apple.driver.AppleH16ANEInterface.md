## com.apple.driver.AppleH16ANEInterface

> `com.apple.driver.AppleH16ANEInterface`

```diff

-10.19.2.0.0
+10.19.6.0.0
   __TEXT.__const: 0x1000
-  __TEXT.__cstring: 0x11971
-  __TEXT.__os_log: 0x3b223
-  __TEXT_EXEC.__text: 0x14e24c
+  __TEXT.__cstring: 0x11982
+  __TEXT.__os_log: 0x3b5dc
+  __TEXT_EXEC.__text: 0x14e9a4
   __TEXT_EXEC.__auth_stubs: 0x1280
   __DATA.__data: 0x482c
   __DATA.__common: 0x7b8
   __DATA.__bss: 0x818
   __DATA_CONST.__mod_init_func: 0x2f0
   __DATA_CONST.__mod_term_func: 0x128
-  __DATA_CONST.__const: 0xfa20
+  __DATA_CONST.__const: 0xfa38
   __DATA_CONST.__kalloc_type: 0x6dc0
   __DATA_CONST.__kalloc_var: 0x8b10
   __DATA_CONST.__auth_got: 0x940
   __DATA_CONST.__got: 0x140
   __DATA_CONST.__auth_ptr: 0x8
-  Functions: 4952
+  Functions: 4958
   Symbols:   0
-  CStrings:  5252
+  CStrings:  5263
 
CStrings:
+ "%s: %s: ANE%u: InjectTMSyncErr active -- allowing dispatch to proceed with dynamic power gating still active\n"
+ "%s: %s: ANE%u: InjectTMSyncErr active -- skipping disable dynamic power gating for this power assertion\n"
+ "%s: %s: ANE%u: recovery entry point reached -- clearing the skip-disable-DPG injection flag\n"
+ "%s: %s: DPG disable completed on device %u (result: 0x%x), waking pending requests queue\n"
+ "%s: %s: Dynamic power gating enable raced a TdBaseOn power assertion, re-issuing disable\n"
+ "%s: %s: Forcing bonded peer ANE%u through firmware timeout recovery after TM sync error on ANE%u\n"
+ "2222222222222222221111212122222222222222222222222222222222122"
+ "[ERROR] %s: %s: ANE:%u detected a TM SYNC Error event!!\n"
+ "[ERROR] %s: %s: Could not allocate the DPG transition message for the scheduler\n"
+ "[ERROR] %s: %s: Re-issuing dynamic power gating disable after raced enable failed: 0x%x\n"
+ "[ERROR] %s: %s: processPowerEvent failed for the DPG transition. result: 0x%x\n"
+ "[ERROR] %s: %s: waitForPowerAssertion: timed out waiting for the DPG command ack\n"
+ "forceBondedPeerRecovery"
+ "notifySchedulerOfDynamicPowerGatingDisable"
- "\"ANE:%u detected a TM SYNC Error event!!\\n\" @%s:%d"
- "%s: %s: Powering ON\n"
- "222222222222222222111121212222222222222222222222222222222122"
```
