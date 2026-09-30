## com.apple.driver.AppleUSBXDCIARM

> `com.apple.driver.AppleUSBXDCIARM`

```diff

-847.80.2.0.0
+847.80.3.0.0
   __TEXT.__const: 0x38
-  __TEXT.__cstring: 0x40ff
-  __TEXT.__os_log: 0x7403
-  __TEXT_EXEC.__text: 0x42804
+  __TEXT.__cstring: 0x4123
+  __TEXT.__os_log: 0x7431
+  __TEXT_EXEC.__text: 0x4277c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x1f0
-  __DATA_CONST.__auth_got: 0x330
+  __DATA_CONST.__auth_got: 0x338
   __DATA_CONST.__got: 0xd0
   __DATA_CONST.__mod_init_func: 0x58
   __DATA_CONST.__mod_term_func: 0x58
   __DATA_CONST.__const: 0x9420
   __DATA_CONST.__kalloc_type: 0x2c0
-  UUID: 96495D8E-BB4B-3F70-ACB9-4495E4D68577
+  UUID: F96D8D9F-CC26-36AF-BDF5-23BAF3362893
   Functions: 379
-  Symbols:   1371
-  CStrings:  333
+  Symbols:   1372
+  CStrings:  331
 
Symbols:
+ __ZNK20IOPortTransportState8isActiveEv
Functions:
~ ____ZN15AppleUSBXDCIARM21powerStateDidChangeToEmmP9IOService_block_invoke : 272 -> 264
~ __ZN15AppleUSBXDCIARM8powerOffEv : 532 -> 428
~ __ZN15AppleUSBXDCIARM15updatePortStateEj : 4200 -> 4248
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
