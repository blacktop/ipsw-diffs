## com.apple.driver.AppleSPMIPMU

> `com.apple.driver.AppleSPMIPMU`

```diff

-1350.0.1.0.0
-  __TEXT.__cstring: 0x2517
+1356.100.2.0.0
+  __TEXT.__cstring: 0x25ca
   __TEXT.__const: 0x26
-  __TEXT_EXEC.__text: 0xc4b0
+  __TEXT_EXEC.__text: 0xcb3c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x320
   __DATA.__common: 0xc0

   __DATA_CONST.__mod_term_func: 0x10
   __DATA_CONST.__const: 0x17c0
   __DATA_CONST.__kalloc_type: 0x140
-  UUID: F0511AFA-62E4-3384-A54F-192DF3317367
-  Functions: 154
-  Symbols:   603
-  CStrings:  342
+  UUID: 2F04BBE1-E9F5-310E-A3FC-EEDCA6F9B515
+  Functions: 155
+  Symbols:   604
+  CStrings:  350
 
Symbols:
+ _ZN18AppleDialogSPMIPMU28_updateLpemLogDataPropertiesEPh.cold.1
+ __ZN18AppleDialogSPMIPMU13_lpemCtrlDictEhhhhhhh
+ __ZN18AppleDialogSPMIPMU13_setLpemStateEhhhhhhh
+ __ZN18AppleDialogSPMIPMU17_writeLpemLogDataEv
- _ZN17PMURTCNVRAMHelper13nvramReadSI64EPx.cold.1
- __ZN18AppleDialogSPMIPMU13_lpemCtrlDictEhhhhh
- __ZN18AppleDialogSPMIPMU13_setLpemStateEhhhhh
CStrings:
+ "\"lpmLogDataEntries[] has invalid size\\n\" @%s:%d"
+ "%s::%s Unable to write LPM log (%x)\n\n"
+ "%s::%s%sBoot Reason LPMSU\n\n"
+ "%s::handleStart: %s _pmuNub: %p ** configuration not found ** built 21:11:37 Mar 19 2025\n"
+ "%s::handleStart: ro=%d nvram=%d helper=%d %s _pmuNub: %p 0x%04x:0x%04x-0x%04x built 21:11:37 Mar 19 2025\n"
+ "%s::start: %s _pmuNub: %p ** configuration not found ** built 21:11:37 Mar 19 2025\n"
+ "%s::start: %s _pmuNub: %p built 21:11:37 Mar 19 2025\n"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleDialogPMU/SPMI/AppleDialogSPMIPMU.cpp"
+ "IOPMUBootReasonLPMSU"
+ "_writeLpemLogData"
+ "lpm3"
+ "lpm4"
+ "seaship-su-boot"
- "%s::handleStart: %s _pmuNub: %p ** configuration not found ** built 20:12:38 Jan  2 2025\n"
- "%s::handleStart: ro=%d nvram=%d helper=%d %s _pmuNub: %p 0x%04x:0x%04x-0x%04x built 20:12:38 Jan  2 2025\n"
- "%s::start: %s _pmuNub: %p ** configuration not found ** built 20:12:38 Jan  2 2025\n"
- "%s::start: %s _pmuNub: %p built 20:12:38 Jan  2 2025\n"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleDialogPMU/SPMI/AppleDialogSPMIPMU.cpp"

```
