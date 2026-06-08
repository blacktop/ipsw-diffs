## com.apple.driver.AppleSMCWirelessCharger

> `com.apple.driver.AppleSMCWirelessCharger`

```diff

-118.100.7.0.0
-  __TEXT.__const: 0x60 sha256:ec9b44cd1cc92b13b00949cbe72680df516ef7b5aad4acb1e522003e86ffdfed
-  __TEXT.__cstring: 0x2bdc sha256:9ad451a13dbd6fb704a4fd824f11fa72cecfd98436b5f1bda99c4e1a747a76e9
-  __TEXT.__os_log: 0x553 sha256:8aea89e51c8b94b426227e8ed89a8610424dfad6e9607aa53bfff3378d2304f6
-  __TEXT_EXEC.__text: 0xf0a0 sha256:68ba9e247e537bb6c34a559db8ef8b2ffc63895254d7496b091fc4b22af8ada8
+147.0.0.0.1
+  __TEXT.__const: 0x60 sha256:29e3ab1cf43707e93df1b3d5cc6d5c428ac410f880053dcdcf3dbb5d86f50c83
+  __TEXT.__cstring: 0x36fa sha256:7ac8c789626e6c3e02de0e01d3930e0a7bfdb6eac0af51f50991ece0dfaa0877
+  __TEXT.__os_log: 0x5b1 sha256:3e7b1498c3b67909b90e465f444f03e46d33e1c5ac5c17ac53b73773bc78d2f2
+  __TEXT_EXEC.__text: 0x10bf8 sha256:a53f68bd0c1db78836d4761f996be13dfdec2d092ebf10b6847c41b67ab6c443
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0xc8 sha256:47f6cd77a70620449f250d307fc78f184d836a9f1e8eb7b09f8a6b96c356cfa2
-  __DATA.__common: 0x68 sha256:39f37f8d1931b3bdf767e7510dd69509fbf23af1f7654933d0a4d291cbdd4418
-  __DATA.__bss: 0x7c sha256:7b8ec8dd836b564f0c85ad088fc744de820345204e154bc1503e04e9d6fdd9f1
-  __DATA_CONST.__auth_got: 0x2b0 sha256:b334bb937b34a5d266de7c14e161fea9923e47d66dce57cbe45038717996ef2f
-  __DATA_CONST.__got: 0xa8 sha256:ba212c6983cdbee043971042c95bd0716a628cc1a4bfab26fa61312c120b87dd
-  __DATA_CONST.__auth_ptr: 0x8 sha256:90bebeb3208e6d02f60b7d05d3bf492d2ce3771c47bbceeeae88ccab4e61dff2
-  __DATA_CONST.__mod_init_func: 0x8 sha256:3364cc4fb201acaff344832931cee198e30b1663fd547cc69a231a5074365723
-  __DATA_CONST.__mod_term_func: 0x8 sha256:c0825ac32b29bf53c70ee29267bd2bef0b6dae1b0b5b608c085450190e20367d
-  __DATA_CONST.__const: 0xee0 sha256:eb889d4b49aa0e9116e354ffccd4d8c7932752b22f423404175d95b983005579
-  __DATA_CONST.__kalloc_type: 0x80 sha256:90e46c117f60ff8e358482c1961e822d3caa2a0b906cb0003f032a70f487a52f
-  __DATA_CONST.__kalloc_var: 0x1e0 sha256:312679e5e853a3a42095026120f28b326bfc51379482c54dd0d55e6a945bda3d
-  UUID: F457530C-E59E-3BCF-8773-4A7865B1F93F
-  Functions: 180
+  __DATA.__data: 0xcd sha256:f382bec9f9246e113ba235348455d01a27dc74ac417189547974ca8fbc729d12
+  __DATA.__common: 0x90 sha256:81c611f35bff79491538b2f7cf201c7597a661a5c549633541c62bdc8af1613f
+  __DATA.__bss: 0x8c sha256:24045c10c12a89f4c11e3b88ea34558fcdf926a8c1008cd08cc33bc71407c774
+  __DATA_CONST.__mod_init_func: 0x8 sha256:9ded697acad52c9fdfc5711c57154c99cd21c7a2d4637350810be4a14f7f6bb6
+  __DATA_CONST.__mod_term_func: 0x8 sha256:4ed5a14ba1bf138fc3f55ef8657aecaef763b762b5da27542943fd4dcda0633e
+  __DATA_CONST.__const: 0x1040 sha256:a8483df86c4e897b46569f35495896a7277dbcdec53afdb99952dd2bbe10d22d
+  __DATA_CONST.__kalloc_type: 0xc0 sha256:3f3701a4ecc8df03652a7a277a0f59588e564510e1daeffbca8f0e15dfbfe36a
+  __DATA_CONST.__kalloc_var: 0x1e0 sha256:7c9852f4bfa6032ced90f1a229feab64953ae8d2390688999b6d6d964ab4df95
+  __DATA_CONST.__auth_got: 0x2d0 sha256:45131210bbc0016a378ed75e1013b0be3b6eb30ae8af3151f0dbe2a98402afc1
+  __DATA_CONST.__got: 0xc0 sha256:28bcbeb2f888cad7b90fc9aabe54cf1c39426d574c26908d9bf82f5e48c35543
+  __DATA_CONST.__auth_ptr: 0x8 sha256:c911f8f82b49879927ca33157372c7231a3677a9cd8f41b5672aea47ca0be241
+  UUID: E06352AC-2138-39D5-8CD5-28528317762F
+  Functions: 210
   Symbols:   0
-  CStrings:  391
+  CStrings:  457
 
CStrings:
+ "\"%s\" @%s:%d"
+ "%s failed to set SMC WATS key (ret=%d)\n"
+ "%s: Tx: not ready to send; _commsDisabled (%d)\n"
+ "%s: failed CPMS admission check\n"
+ "%s: failed CPMS client registration\n"
+ "%s: failed to read fw mode: ret=0x%x\n"
+ "%s: failed to register inductive fw log channel (ret=%d)\n"
+ "%s: failed to write to WAEB key for CPMS esp budget\n"
+ "%s: inductive rcv CPMS esp budget update: %dmW\n"
+ "%s: inductive rcv CPMS esp update but no 1s UPO budget\n"
+ "%s: kInBandCommsStateChange(kInBandCommsEventEspressoInfoUpdated) payload=0x%02x\n"
+ "%s: log entry too large (%d bytes)"
+ "%s: peripheral log collection method: %d\n"
+ "%s: read SMC key: WASM=%d\n"
+ "%s: received CPMS esp budget: %dmW (requested %d)\n"
+ "%s: successfully registered inductive fw log channel\n"
+ "%s::%s id:%d fw_mode:%d encoding:%s idx:%d max_idx:%d payload:%s\n"
+ "%s::%s:_ppmService=null\n"
+ "%s::%s:ackClientBudget failed\n"
+ "%s::%s:failed casting to RTBuddyService\n"
+ "%s::%s:failed to add binary log entry handler\n"
+ "%s::%s:failed to alloc strings\n"
+ "%s::%s:failed to allocate log channel class\n"
+ "%s::%s:failed to find matching PPM service\n"
+ "%s::%s:failed to set service\n"
+ "%s::%s:inductive rcv esp budget %dmW for reason %d\n"
+ "%s::%s:no RTBuddyService found\n"
+ "%s::%s:no matchingService for RTBuddy with SMC endpoint\n"
+ "%s::%s:ppmKernelClient null\n"
+ "1211111212221212122122111222122111112121211122222111111111111111111111111111112222222222222222222222222112211111211121111111111111111121"
+ "1222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222"
+ "AppleC26FWLogChannel"
+ "AppleInductive"
+ "ApplePPM"
+ "ESP: err, received OOBP evt while detached\n"
+ "ESP: err, received OOBP+ evt while detached\n"
+ "ESP: host_bt_addr avail notif [0x%02x 0x%02x 0x%02x 0x%02x 0x%02x 0x%02x]\n"
+ "ESP: host_bt_addr property rd fail\n"
+ "ESP: set property %s = %d\n"
+ "ESP: set property %s = (%d) [0x%02x 0x%02x 0x%02x 0x%02x 0x%02x 0x%02x 0x%02x 0x%02x 0x%02x 0x%02x 0x%02x 0x%02x 0x%02x 0x%02x 0x%02x 0x%02x 0x%02x 0x%02x 0x%02x 0x%02x 0x%02x 0x%02x 0x%02x 0x%02x 0x%02x 0x%02x 0x%02x 0x%02x 0x%02x 0x%02x 0x%02x 0x%02x]\n"
+ "ESP: set property %s = (%d) [0x%02x 0x%02x 0x%02x 0x%02x 0x%02x 0x%02x]\n"
+ "ESP: set property %s = [0x%02x 0x%02x 0x%02x 0x%02x 0x%02x 0x%02x 0x%02x]\n"
+ "ESP: smcReadKey(WABI) failed with ret=0x%x\n"
+ "ESP: smcReadKey(WABO) failed with ret=0x%x\n"
+ "ESP: smcReadKey(WBOP) failed with ret=0x%x\n"
+ "ESP: smcWriteKey(WBHB) failed with ret=0x%x\n"
+ "IOAccessoryManagerInductiveOOBPairingAccessoryData"
+ "IOAccessoryManagerInductiveOOBPairingAccessoryInfo"
+ "IOAccessoryManagerInductiveOOBPairingEarlyInfo"
+ "IOAccessoryManagerInductiveOOBPairingHostInfo"
+ "OSBoundedPtr.h"
+ "RTBuddyService"
+ "SMC"
+ "This bounded_ptr is pointing to memory outside of what can be represented by a native pointer."
+ "backlight-detection"
+ "bounded_ptr<T>::operator->: Accessing a member through this pointer would access memory outside of the bounds set originally"
+ "chg-dis-ccoex"
+ "chg-espresso-debug"
+ "handlePPMServiceArrivalNotification"
+ "has-espresso"
+ "registerForPPMArrivalNotification"
+ "registerKernelClientToApplePPMFunction"
+ "registerWithRTBuddySMCService"
+ "role"
+ "setBudgetToKernelClientFunction"
+ "setEspressoPowerBudget"
+ "site.AppleC26FWLogChannel"
+ "writeFWLogDataToOSLog"
- "%s::%s id:%d encoding:%s idx:%d max_idx:%d payload:%s\n"
- "12111112122212121221211122212211111212121112222211111111111111111111111112222222222222222222222222112211111211121111111111111111121"

```
