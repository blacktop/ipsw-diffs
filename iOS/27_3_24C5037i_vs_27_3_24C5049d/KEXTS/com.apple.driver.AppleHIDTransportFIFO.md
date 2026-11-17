## com.apple.driver.AppleHIDTransportFIFO

> `com.apple.driver.AppleHIDTransportFIFO`

```diff

-10110.1.0.0.0
+10120.1.0.0.0
   __TEXT.__const: 0x8
-  __TEXT.__cstring: 0x2be7
-  __TEXT_EXEC.__text: 0x128fc
+  __TEXT.__cstring: 0x2c16
+  __TEXT_EXEC.__text: 0x129f8
   __TEXT_EXEC.__auth_stubs: 0x3e0
   __DATA.__data: 0xc8
   __DATA.__common: 0x60

   __DATA_CONST.__kalloc_type: 0x2c0
   __DATA_CONST.__auth_got: 0x1f0
   __DATA_CONST.__got: 0xb8
-  Functions: 333
+  Functions: 334
   Symbols:   0
-  CStrings:  289
+  CStrings:  290
 
Functions:
~ __ZN32AppleHIDTransportProtocolSCMFIFO14setReportGatedEPhS0_P18IOMemoryDescriptorP15IOHIDReportType : 3556 -> 3624
+ __ZN32AppleHIDTransportProtocolSCMFIFO14setReportGatedEPhS0_P18IOMemoryDescriptorP15IOHIDReportType.cold.19
CStrings:
+ "report->getLength() <= _controlPayloadCapacity"
```
