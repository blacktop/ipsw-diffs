## com.apple.driver.AppleUSBXDCIARM

> `com.apple.driver.AppleUSBXDCIARM`

```diff

-847.60.7.0.0
+847.60.10.0.0
   __TEXT.__const: 0x38
-  __TEXT.__cstring: 0x4123
-  __TEXT.__os_log: 0x7431
-  __TEXT_EXEC.__text: 0x421c4
+  __TEXT.__cstring: 0x40ff
+  __TEXT.__os_log: 0x7403
+  __TEXT_EXEC.__text: 0x4224c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x1f0
-  __DATA_CONST.__auth_got: 0x338
+  __DATA_CONST.__auth_got: 0x330
   __DATA_CONST.__got: 0xd0
   __DATA_CONST.__mod_init_func: 0x58
   __DATA_CONST.__mod_term_func: 0x58
   __DATA_CONST.__const: 0x6ae0
   __DATA_CONST.__kalloc_type: 0x2c0
-  UUID: 5112794F-1792-3875-A1DF-40CD956BC5B2
+  UUID: 11B5F9B3-B7BE-3F4E-BD7E-FFB9F9282BEB
   Functions: 379
   Symbols:   0
-  CStrings:  331
+  CStrings:  333
 
Functions:
~ sub_fffffe000abee46c -> sub_fffffe000ab4be4c : 264 -> 272
~ sub_fffffe000abef294 -> sub_fffffe000ab4cc7c : 428 -> 532
~ __ZN15AppleUSBXDCIARM15updatePortStateEj : 4232 -> 4184
~ __ZN15AppleUSBXDCIARM19cableChangeOccurredEP18IOTimerEventSource : 1936 -> 2004
~ __ZN15AppleUSBXDCIARM17hardwareExceptionEiPKc : 1448 -> 1452
CStrings:
+ "%s@%s: %s::%s: Port-%s@%d %s: connected: %d (no IOPortTransportState)\n"
+ "%s@%s: %s::%s: Port-%s@%d %s: connected: %d (tunneled: %d, role: %s, trm: %d:%d)\n"
+ "%s@%s: %s::%s: Unauthorized protocol - %s %s\n"
+ "USB2"
+ "USB3"
- "%s@%s: %s::%s: Port-%s@%d %s: connected: %d -> %d (no IOPortTransportState)\n"
- "%s@%s: %s::%s: Port-%s@%d %s: connected: %d -> %d (tunneled: %d, role: %s, trm: %d:%d)\n"
- "%s@%s: %s::%s: event did not change USB2 connected (%d) or USB3 connected (%d)\n"

```
