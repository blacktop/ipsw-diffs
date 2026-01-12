## com.apple.driver.AppleUSBXDCIARM

> `com.apple.driver.AppleUSBXDCIARM`

```diff

-847.80.2.0.0
+847.80.3.0.0
   __TEXT.__const: 0x38
-  __TEXT.__cstring: 0x40ff
-  __TEXT.__os_log: 0x7403
-  __TEXT_EXEC.__text: 0x4224c
+  __TEXT.__cstring: 0x4123
+  __TEXT.__os_log: 0x7431
+  __TEXT_EXEC.__text: 0x421c4
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x1f0
-  __DATA_CONST.__auth_got: 0x330
+  __DATA_CONST.__auth_got: 0x338
   __DATA_CONST.__got: 0xd0
   __DATA_CONST.__mod_init_func: 0x58
   __DATA_CONST.__mod_term_func: 0x58
   __DATA_CONST.__const: 0x6ae0
   __DATA_CONST.__kalloc_type: 0x2c0
-  UUID: 855B2417-F825-3BB6-BE16-A282CB2F4EB1
+  UUID: B62C0534-2F36-328D-A6FA-6B5D5EF319A4
   Functions: 379
   Symbols:   0
-  CStrings:  333
+  CStrings:  331
 
Functions:
~ sub_fffffe000ac3e92c -> sub_fffffe000ac46ffc : 272 -> 264
~ sub_fffffe000ac3f75c -> sub_fffffe000ac47e24 : 532 -> 428
~ __ZN15AppleUSBXDCIARM15updatePortStateEj : 4184 -> 4232
~ __ZN15AppleUSBXDCIARM19cableChangeOccurredEP18IOTimerEventSource : 2004 -> 1936
~ __ZN15AppleUSBXDCIARM17hardwareExceptionEiPKc : 1452 -> 1448
CStrings:
+ "%s@%s: %s::%s: Port-%s@%d %s: connected: %d -> %d (no IOPortTransportState)\n"
+ "%s@%s: %s::%s: Port-%s@%d %s: connected: %d -> %d (tunneled: %d, role: %s, trm: %d:%d)\n"
+ "%s@%s: %s::%s: event did not change USB2 connected (%d) or USB3 connected (%d)\n"
- "%s@%s: %s::%s: Port-%s@%d %s: connected: %d (no IOPortTransportState)\n"
- "%s@%s: %s::%s: Port-%s@%d %s: connected: %d (tunneled: %d, role: %s, trm: %d:%d)\n"
- "%s@%s: %s::%s: Unauthorized protocol - %s %s\n"
- "USB2"
- "USB3"

```
