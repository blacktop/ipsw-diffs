## com.apple.driver.AppleSARService

> `com.apple.driver.AppleSARService`

```diff

 1391.0.0.0.0
-  __TEXT.__os_log: 0xf1ea
+  __TEXT.__os_log: 0xfdd1
   __TEXT.__const: 0xfd8
-  __TEXT.__cstring: 0xdab4
-  __TEXT_EXEC.__text: 0x72174
+  __TEXT.__cstring: 0xe277
+  __TEXT_EXEC.__text: 0x7631c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x128
-  __DATA.__common: 0x638
+  __DATA.__common: 0x648
   __DATA.__bss: 0x1498
-  __DATA_CONST.__auth_got: 0x290
-  __DATA_CONST.__got: 0xa8
+  __DATA_CONST.__auth_got: 0x298
+  __DATA_CONST.__got: 0xb8
   __DATA_CONST.__mod_init_func: 0x60
   __DATA_CONST.__mod_term_func: 0x68
-  __DATA_CONST.__const: 0x5838
-  __DATA_CONST.__kalloc_type: 0x3e00
+  __DATA_CONST.__const: 0x5910
+  __DATA_CONST.__kalloc_type: 0x3f80
   __DATA_CONST.__kalloc_var: 0x190
-  UUID: 0B9C8915-19F3-36F3-8AB1-B25DFA08E419
-  Functions: 642
+  UUID: 0B790459-6280-34B8-AB6E-E18EEBC7BBEA
+  Functions: 655
   Symbols:   0
-  CStrings:  1767
+  CStrings:  1831
 
CStrings:
+ "#D: %s::%s:%d: \n"
+ "#D: %s::%s:%d: All checks passed, proceed to write a message onto the buffer\n"
+ "#D: %s::%s:%d: Empty cache and BB is asleep, returning without performing any action\n"
+ "#D: %s::%s:%d: Invalid SAR message type received: %d\n"
+ "#D: %s::%s:%d: Nothing to write and BB is awake, sending sleep signal now\n"
+ "#D: %s::%s:%d: Returning without performing any action because the buffer is not ready yet\n"
+ "#D: %s::%s:%d: SAR Fusion: Voice: %s (Overriding: %s)\n"
+ "#D: %s::%s:%d: SAR Fusion: Wrist: %s (Overriding: %s)\n"
+ "#D: %s::%s:%d: Updating fCachedSARFusionIndicator ( ( %u | %u ) = %u )\n"
+ "#D: %s::%s:%d: Updating sequence number to %u\n"
+ "#D: %s::%s:%d: Valid cache but BB is asleep, sending wake signal now\n"
+ "#D: %s::%s:%d: Valid cache but already triggered a wake, returning without performing any action\n"
+ "#D: %s::%s:%d: Wake state: %s, Ready to fill: %d, Cache: %d\n"
+ "#D: %s::%s:%d: Whole SAR Fusion State is updating for DAL\n"
+ "#D: %s::%s:%d: Writing %lu bytes\n"
+ "%s fired!"
+ "%s::%s:%d: Abort OCP write due to %s state (AP is asleep or BB is resetting)\n"
+ "%s::%s:%d: Failed to send SAR Fusion data to baseband: ret: 0x%x\n"
+ "%s::%s:%d: Indicator: 0x%x, CRC16: 0x%02x%02x, SeqNum: %u\n"
+ "%s::%s:%d: Invalid state because a wake should not have been triggered for an empty cache\n"
+ "%s::%s:%d: Resetting OCP sequence number back to 0\n"
+ "%s::%s:%d: Resetting Write-Ready bit because of a successful write\n"
+ "%s::%s:%d: SAR Fusion Data object is NULL!\n"
+ "%s::%s:%d: SAR Fusion Data object is invalid, unable to reset sequence number\n"
+ "%s::%s:%d: Triggering the send data function from within the OCP READY_TO_FILL ISR"
+ "%s::%s:%d: Triggering the send data function from within the OCP WAKE_DONE ISR"
+ "12111112122212121111112112112112112112112112112112112112212121111221122"
+ "AppleSARFusion: %s fired!"
+ "OCP init interrupt"
+ "OCPDataReadyDAL"
+ "Unable to retrieve fusion object"
+ "Wake done interrupt"
+ "dal"
+ "readyToFillTimerExpired"
+ "sarFusionStateDAL"
+ "sarFusionStateDAL_block_invoke_2"
+ "sendOCPDataDalGated"
+ "static IOReturn AppleSARServiceUserClient::extSARFusionStateDAL(AppleSARService *, void *, IOExternalMethodArguments *)"
+ "wakeDoneTimerExpired"
+ "writeOCPWakeSignalGated_block_invoke"
- "12111112122212121111112112112112112112112112112112112212121111221122"

```
