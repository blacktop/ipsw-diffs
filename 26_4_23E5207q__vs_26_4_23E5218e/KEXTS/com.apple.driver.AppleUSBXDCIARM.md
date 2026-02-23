## com.apple.driver.AppleUSBXDCIARM

> `com.apple.driver.AppleUSBXDCIARM`

```diff

-847.100.24.0.0
-  __TEXT.__const: 0x38
-  __TEXT.__cstring: 0x43ac
-  __TEXT.__os_log: 0x773a
-  __TEXT_EXEC.__text: 0x3c030
+847.100.25.0.0
+  __TEXT.__const: 0x50
+  __TEXT.__cstring: 0x43d0
+  __TEXT.__os_log: 0x7754
+  __TEXT_EXEC.__text: 0x3c35c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x1f0
-  __DATA_CONST.__auth_got: 0x338
+  __DATA_CONST.__auth_got: 0x330
   __DATA_CONST.__got: 0xd0
   __DATA_CONST.__mod_init_func: 0x58
   __DATA_CONST.__mod_term_func: 0x58
   __DATA_CONST.__const: 0x6da0
   __DATA_CONST.__kalloc_type: 0x2c0
-  UUID: FD21FE84-7F21-312C-BBFF-3BCFF1E18356
+  UUID: ED9B5C6E-CB6D-3F3F-BD61-4DC22A5871D1
   Functions: 395
   Symbols:   0
-  CStrings:  361
+  CStrings:  365
 
Functions:
~ sub_fffffe000a1d706c -> sub_fffffe000a1b058c : 7248 -> 7264
~ __ZN17AppleT8027USBXDCI7powerOnEv : 1588 -> 1600
~ __ZN17AppleT8130USBXDCI7powerOnEv -> sub_fffffe000a1b6ee8 : 7248 -> 7264
~ sub_fffffe000a1e2c88 -> sub_fffffe000a1bc1d4 : 7356 -> 7372
~ __ZN17AppleT8122USBXDCI5startEP9IOService -> __ZN17AppleT8122USBXDCI7powerOnEv : 12272 -> 12288
~ __ZN17AppleT8132USBXDCI7powerOnEv : 12272 -> 12288
~ __ZN15AppleUSBXDCIARM5startEP9IOService : 8176 -> 8148
~ sub_fffffe000a1f8a38 -> sub_fffffe000a1d1f98 : 240 -> 260
~ __ZN15AppleUSBXDCIARM15updatePortStateEj : 3828 -> 3940
~ __ZN15AppleUSBXDCIARM19cableChangeOccurredEP18IOTimerEventSource : 1772 -> 2332
~ __ZN15AppleUSBXDCIARM17hardwareExceptionEiPKc : 1376 -> 1384
~ __ZN17AppleT8140USBXDCI7powerOnEv -> __ZN17AppleT8140USBXDCI5startEP9IOService : 7248 -> 7264
~ __ZN17AppleT8103USBXDCI5startEP9IOService -> sub_fffffe000a1e04fc : 7248 -> 7264
~ __ZN17AppleT8142USBXDCI7powerOnEv -> __ZN17AppleT8142USBXDCI5startEP9IOService : 11928 -> 11944
CStrings:
+ "%s@%s: %s::%s: Port-%s@%d %s: connected: %d (tunneled: %d, role: %s, trm: %d:%d, authorized: %d -> %d)\n"
+ "%s@%s: %s::%s: Port-%s@%d %s: connected: %d-> %d (no IOPortTransportState)\n"
+ "%s@%s: %s::%s: USB restricted, powering off\n"
+ "%s@%s: %s::%s: Unauthorized protocol - %s %s\n"
+ "USB2"
+ "USB3"
- "%s@%s: %s::%s: Port-%s@%d %s: connected: %d -> %d (no IOPortTransportState)\n"
- "%s@%s: %s::%s: Port-%s@%d %s: connected: %d -> %d (tunneled: %d, role: %s, trm: %d:%d)\n"
- "%s@%s: %s::%s: event did not change USB2 connected (%d) or USB3 connected (%d)\n"

```
