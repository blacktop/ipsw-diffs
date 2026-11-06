## com.apple.driver.AppleOLYHAL

> `com.apple.driver.AppleOLYHAL`

```diff

-531.7.0.0.0
+535.4.0.0.0
   __TEXT.__const: 0x1f88
-  __TEXT.__cstring: 0x50bb
-  __TEXT_EXEC.__text: 0x1edc4
+  __TEXT.__cstring: 0x505d
+  __TEXT_EXEC.__text: 0x1ef04
   __TEXT_EXEC.__auth_stubs: 0x7a0
   __DATA.__data: 0x18c
   __DATA.__common: 0x170

   __DATA_CONST.__kalloc_type: 0x600
   __DATA_CONST.__auth_got: 0x3d0
   __DATA_CONST.__got: 0xf8
-  Functions: 589
+  Functions: 586
   Symbols:   1041
-  CStrings:  543
+  CStrings:  540
 
Symbols:
+ __ZZN32AppleOLYHALPortInterfacePCIeAMFM23processAMFMMessageGatedEjPvmE21kalloc_type_view_1409
+ ___ZN11AppleOLYHAL31requestDextInitFailureChipResetEv_block_invoke
- _OUTLINED_FUNCTION_5
- __ZZN32AppleOLYHALPortInterfacePCIeAMFM23processAMFMMessageGatedEjPvmE21kalloc_type_view_1426
CStrings:
+ "\"AppleOLYHAL Panic: AppleBCMWLAN dext init failure unrecoverable after %u chip resets\" @%s:%d"
+ "%s::%s: Dext is unavailable. skip PreparePCIeError\n"
+ "%s::%s: FCR begin during dext crash! Saving device state.\n"
+ "%s::%s: FCR end during dext crash! Restoring device state.\n"
+ "%s::%s: FLR result: 0x%08x\n"
+ "%s::%s: Received Dext Publish Notification (%p)\n"
+ "%s::%s: Received Dext Termination Notification (%p)\n"
+ "%s::%s: Received IOPCIDevice gIOPublish Notification (%p)\n"
+ "%s::%s: Received IOPCIDevice gIOWillTerminate Notification (%p)\n"
+ "%s::%s: Recovering dext crash (FCR: %d)"
+ "%s::%s: Recovering dext crash (FLR: %u, 0x%08x, %p)\n"
+ "%s::%s: Triggering FLR\n"
+ "%s::%s: allowing external full reset to proceed with missing wifi dext\n"
+ "Init-failure chip reset limit (%u) reached; WiFi unrecoverable, panicking\n"
- "\"%s:%u:\" \"!is_enabled\" @%s:%d"
- "\"%s:%u:\" \"pActionType == kAppleOLYHALPortInterfacePowerActionTypeHardReset\" @%s:%d"
- "\"Pending powerOn never arrived\\n\" @%s:%d"
- "%s::%s: Dext Recovery was paused. Wait until AMFM completes its 3 sequence handshakes\n"
- "%s::%s: Dext recovery is paused. skip PreparePCIeError\n"
- "%s::%s: No pending AMFM messages\n"
- "%s::%s: Received Dext Publish Notification\n"
- "%s::%s: Received Dext Termination Notification\n"
- "%s::%s: Received IOPCIDevice gIOPublish Notification\n"
- "%s::%s: Received IOPCIDevice gIOWillTerminate Notification\n"
- "%s::%s: Sleep until pending powerOn completes\n"
- "%s::%s: Using pre-existing powercycle as the recovery mechanism\n"
- "Init-failure chip reset limit (%u) reached; leaving WiFi down\n"
- "OLYHAL initFailureChipResetComplete -> restoreDeviceState()\n"
- "OLYHAL reset -> saveDeviceState() (captured cfg pre power-cycle)\n"
- "handleDextPublish"
- "handleDextTerminate"
```
