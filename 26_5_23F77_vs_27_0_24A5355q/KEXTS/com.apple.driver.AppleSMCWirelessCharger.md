## com.apple.driver.AppleSMCWirelessCharger

> `com.apple.driver.AppleSMCWirelessCharger`

```diff

-118.100.7.0.0
+147.0.0.0.1
   __TEXT.__const: 0x60
-  __TEXT.__cstring: 0x2bdc
-  __TEXT.__os_log: 0x553
-  __TEXT_EXEC.__text: 0xf0a0
+  __TEXT.__cstring: 0x36fa
+  __TEXT.__os_log: 0x5b1
+  __TEXT_EXEC.__text: 0x10bf8
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0xc8
-  __DATA.__common: 0x68
-  __DATA.__bss: 0x7c
-  __DATA_CONST.__auth_got: 0x2b0
-  __DATA_CONST.__got: 0xa8
-  __DATA_CONST.__auth_ptr: 0x8
+  __DATA.__data: 0xcd
+  __DATA.__common: 0x90
+  __DATA.__bss: 0x8c
   __DATA_CONST.__mod_init_func: 0x8
   __DATA_CONST.__mod_term_func: 0x8
-  __DATA_CONST.__const: 0xee0
-  __DATA_CONST.__kalloc_type: 0x80
+  __DATA_CONST.__const: 0x1040
+  __DATA_CONST.__kalloc_type: 0xc0
   __DATA_CONST.__kalloc_var: 0x1e0
-  UUID: F457530C-E59E-3BCF-8773-4A7865B1F93F
-  Functions: 180
+  __DATA_CONST.__auth_got: 0x2d0
+  __DATA_CONST.__got: 0xc0
+  __DATA_CONST.__auth_ptr: 0x8
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
