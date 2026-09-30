## com.apple.driver.AppleH16ANEInterface

> `com.apple.driver.AppleH16ANEInterface`

```diff

-10.100.80.0.0
+10.101.100.0.0
+  __TEXT.__cstring: 0x11ddc
+  __TEXT.__os_log: 0x3dfe8
   __TEXT.__const: 0x1250
-  __TEXT.__cstring: 0x11d47
-  __TEXT.__os_log: 0x3d5f7
-  __TEXT_EXEC.__text: 0x152ba8
-  __TEXT_EXEC.__auth_stubs: 0x1280
-  __DATA.__data: 0x54f0
+  __TEXT_EXEC.__text: 0x154344
+  __TEXT_EXEC.__auth_stubs: 0x1290
+  __DATA.__data: 0x54f4
   __DATA.__common: 0x7e0
   __DATA_CONST.__mod_init_func: 0x300
   __DATA_CONST.__mod_term_func: 0x138
-  __DATA_CONST.__const: 0x10020
-  __DATA_CONST.__kalloc_type: 0x7040
+  __DATA_CONST.__const: 0x10058
   __DATA_CONST.__kalloc_var: 0x8c00
-  __DATA_CONST.__auth_got: 0x940
-  __DATA_CONST.__got: 0x140
+  __DATA_CONST.__kalloc_type: 0x7040
+  __DATA_CONST.__auth_got: 0x948
+  __DATA_CONST.__got: 0x148
   __DATA_CONST.__auth_ptr: 0x8
-  Functions: 5085
+  Functions: 5091
   Symbols:   0
-  CStrings:  5411
+  CStrings:  5447
 
CStrings:
+ "%s: %s: ANE Memory remap ack by mailbox offset: 0x%llx size: 0x%llx\n"
+ "%s: %s: ANE driver back-reference not set yet, reporting local max macho size 0x%llx\n"
+ "%s: %s: ANE%u: InjectTMSyncErr active -- allowing dispatch to proceed with dynamic power gating still active\n"
+ "%s: %s: ANE%u: InjectTMSyncErr active -- skipping disable dynamic power gating for this power assertion\n"
+ "%s: %s: ANE%u: recovery entry point reached -- clearing the skip-disable-DPG injection flag\n"
+ "%s: %s: ANEDevicePropertiesArrivalNotificationHandler: numANEs discovered so far: %u\n"
+ "%s: %s: Client specified ANE instance hint (core %u), skipping rotation bias\n"
+ "%s: %s: Core %u , client preference %u\n"
+ "%s: %s: Core %u, rotation bias preference %u\n"
+ "%s: %s: Firmware recovery completed... deferring ANEExclave notification until next power-on\n"
+ "%s: %s: Forcing bonded peer ANE%u through firmware timeout recovery after TM sync error on ANE%u\n"
+ "%s: %s: GetNextRotationTargetANE: %u -> %u (residencyMask 0x%x)\n"
+ "%s: %s: SUSPEND skipped for system-initiated power transition, requesting power policy %s for state %d\n"
+ "%s: %s: Servicing deferred firmware recovery notification to ANEExclave\n"
+ "%s: %s: Single-ANE rotation flipped preferred ANE to %u\n"
+ "%s: %s: Skipping SECURE mode transition ACK\n"
+ "%s: %s: WRK %-3u ANE %-3u HOL %-3u CLPC %-3u THROT %-3u clientPref %-3u PWR %-3u ROT %-3u\n"
+ "%s: %s: Waking from hibernate, clearing cached performance counters\n"
+ "%s: %s: Waking from hibernate, clearing cached performance counters (ActiveAction)\n"
+ "121111121222121212111222122222222222221222222012212021111112212211222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222221221221122122111112"
+ "12111122222222222222212222222222222221222222222222222122222222222222211110111101111122122112212212112111111211111122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222221221222212212212212212212212"
+ "2222222222222222222111121212222222222222222222222222222222222122"
+ "ANEDevicePropertiesArrivalNotificationHandler_block_invoke"
+ "ANE_GetStatus_gated"
+ "ANE_sendISPSurfaceRemapAck"
+ "GetNextRotationTargetANE"
+ "IOHibernateState"
+ "[ERROR] %s: %s: ANE:%u detected a TM SYNC Error event!!\n"
+ "[ERROR] %s: %s: BACK_CHANNEL_RPC: message too small for %u declared rpc items: messageSize=0x%llx required=0x%llx\n"
+ "[ERROR] %s: %s: CLPC work still outstanding at destruction (residency: 0x%x, status: %u) for programHandle: 0x%llx, transactionID: 0x%llx\n"
+ "[ERROR] %s: %s: Couldn't create matching dictionary for H11ANEIn device properties notification\n"
+ "[ERROR] %s: %s: Endpoint[%ld] message too small for command header: offset[0x%llx] size[0x%llx]\n"
+ "[ERROR] %s: %s: Endpoint[%ld] message too small for handshake info: offset[0x%llx] size[0x%llx]\n"
+ "[ERROR] %s: %s: Failed to enable ane power off timer after boot bring-up: 0x%x\n"
+ "[ERROR] %s: %s: Failed to send shared memory remap ack res=%d\n"
+ "[ERROR] %s: %s: GetNextRotationTargetANE returned out-of-range index %u (numANEs: %u), skipping flip\n"
+ "[ERROR] %s: %s: GetNextRotationTargetANE: residencyMask is empty, defaulting to ANE 0\n"
+ "[ERROR] %s: %s: Invalid offset[0x%llx] and size[0x%llx] for endpoint[%ld] bufferSize[0x%zx]. Out of bounds message"
+ "[ERROR] %s: %s: Shared memory alloc message too small: offset:0x%llx, size:0x%llx\n"
+ "[ERROR] %s: %s: Shared memory free message too small: offset:0x%llx, size:0x%llx\n"
+ "[ERROR] %s: %s: Shared memory message too small for command header: offset:0x%llx, size:0x%llx\n"
+ "[ERROR] %s: %s: Shared memory remap message too small: offset:0x%llx, size:0x%llx\n"
+ "[ERROR] %s: %s: rotationPreferredAneIdx %u out of range (max: %u), skipping rotation bias\n"
+ "endOutstandingPerfWork"
+ "forceBondedPeerRecovery"
- "\"ANE:%u detected a TM SYNC Error event!!\\n\" @%s:%d"
- "%s: %s: ANE Memory remap req by mailbox offset: 0x%llx size:  0x%llx\n"
- "%s: %s: Firmware recovery completed... notifying ANEExclave\n"
- "%s: %s: WRK %-3u ANE %-3u HOL %-3u CLPC %-3u THROT %-3u clientPref %-3u PWR %-3u\n"
- "1211111212221212121112221222222222222212222220122120211111122122112222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222212212211221221111"
- "121111222222222222222122222222222222212222222222222221222222222222222111101111011111221221122122121121111112111111222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222212212212212212212212212212"
- "222222222222222222211112121222222222222222222222222222222222122"
- "ANEScheduler: %s: Core %u , client preference %u\n"
- "[ERROR] %s: %s: Invalid offset[0x%llx] and size[0x%llx] for endpoint[%ld]. Oversized message"
```
