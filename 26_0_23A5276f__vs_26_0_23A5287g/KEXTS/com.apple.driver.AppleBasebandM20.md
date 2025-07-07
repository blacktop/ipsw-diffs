## com.apple.driver.AppleBasebandM20

> `com.apple.driver.AppleBasebandM20`

```diff

-1026.0.0.0.0
+1029.0.0.0.0
   __TEXT.__const: 0x435
-  __TEXT.__cstring: 0x93af
-  __TEXT.__os_log: 0x87a4
-  __TEXT_EXEC.__text: 0x491ac
+  __TEXT.__cstring: 0x9960
+  __TEXT.__os_log: 0x8c9a
+  __TEXT_EXEC.__text: 0x4aa08
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x190
   __DATA.__common: 0x2c8
   __DATA.__bss: 0x2d1
   __DATA_CONST.__auth_got: 0x2c0
-  __DATA_CONST.__got: 0xb0
+  __DATA_CONST.__got: 0xb8
   __DATA_CONST.__mod_init_func: 0x90
   __DATA_CONST.__mod_term_func: 0x90
-  __DATA_CONST.__const: 0x6330
+  __DATA_CONST.__const: 0x6398
   __DATA_CONST.__kalloc_type: 0x580
   __DATA_CONST.__kalloc_var: 0x320
-  UUID: 3B734BBF-D7BD-3386-835D-EBAF16EE10E0
-  Functions: 812
+  UUID: E349B958-CFEA-31E5-95E4-5AF49758A5B6
+  Functions: 822
   Symbols:   0
-  CStrings:  1363
+  CStrings:  1405
 
CStrings:
+ "%06ld.%06d %s::%s: AP is going to sleep, will detach all SPMI interrupts"
+ "%06ld.%06d %s::%s: AP is waking up, attaching all SPMI interrupts now"
+ "%06ld.%06d %s::%s: Aborting billboard transaction failure processing due to %s state"
+ "%06ld.%06d %s::%s: Aborting billboard write due to %s state\n"
+ "%06ld.%06d %s::%s: Coredump triggered successfully via kernel\n"
+ "%06ld.%06d %s::%s: Crashing baseband due to %u failed billboard transactions\n"
+ "%06ld.%06d %s::%s: Failed to crash baseband, continuing with billboard protocol\n"
+ "%06ld.%06d %s::%s: Failed to get PPMClient class for %s\n"
+ "%06ld.%06d %s::%s: Failed to trigger SPMI coredump interrupt, ret = 0x%x\n"
+ "%06ld.%06d %s::%s: Failed to trigger coredump via user client (ret: 0x%x), falling back to kernel method\n"
+ "%06ld.%06d %s::%s: Invalid SPMI HEB object"
+ "%06ld.%06d %s::%s: Invalid SPMI HEB object, coredump will not be triggered\n"
+ "%06ld.%06d %s::%s: Received a WAKE_DONE signal from BB when in %s state, dropping the signal\n"
+ "%06ld.%06d %s::%s: Resetting billboard ready flag because of a successful write\n"
+ "%06ld.%06d %s::%s: Setting fBillboardReadyToFill back to true due to a READY_TO_FILL timeout\n"
+ "%06ld.%06d %s::%s: Successfully received a fresh budget from client %s\n"
+ "%06ld.%06d %s::%s: Triggering a coredump via kernel\n"
+ "%06ld.%06d %s::%s: Triggering coredump due to a SPMI error\n"
+ "%06ld.%06d %s::%s: Triggering coredump via user client\n"
+ "12111112122212121112111111112112"
+ "ABORT"
+ "attachAllInterruptSources"
+ "billboardTransactionFailureGated"
+ "billboardWriteGated"
+ "detachAllInterruptSources"
+ "powerStateDidChangeTo_block_invoke"
+ "powerStateWillChangeTo_block_invoke"
+ "triggerBillboardWritingInterruptSource"
+ "triggerCoredump"
+ "triggerCoredumpViaKernel"
+ "triggerCoredumpViaUserClient"
- "%06ld.%06d %s::%s: Failed to get PPMClient client class\n"
- "%06ld.%06d %s::%s: Resetting billboard ready flag and cache because of a successful write\n"
- "1211111212221212111211111111211"
- "budgetWritingGated"
- "powerStateDidChangeTo"
- "powerStateWillChangeTo"

```
