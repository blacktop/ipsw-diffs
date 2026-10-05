## BTLEServer

> `/usr/sbin/BTLEServer`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-2701.2.0.0.0
-  __TEXT.__text: 0x7e0e8
+2701.4.0.0.0
+  __TEXT.__text: 0x7e3e8
   __TEXT.__auth_stubs: 0x1100
-  __TEXT.__objc_stubs: 0xcfc0
-  __TEXT.__objc_methlist: 0x7ec4
+  __TEXT.__objc_stubs: 0xd020
+  __TEXT.__objc_methlist: 0x7ed4
   __TEXT.__const: 0x900
-  __TEXT.__cstring: 0x3694
-  __TEXT.__objc_methname: 0x133bc
-  __TEXT.__oslogstring: 0xd8d6
+  __TEXT.__cstring: 0x369f
+  __TEXT.__objc_methname: 0x1340d
+  __TEXT.__oslogstring: 0xd9c0
   __TEXT.__objc_classname: 0x900
   __TEXT.__objc_methtype: 0x318a
   __TEXT.__gcc_except_tab: 0x13c4

   __TEXT.__ustring: 0xc6
   __TEXT.__unwind_info: 0x26a0
   __DATA_CONST.__const: 0x17c0
-  __DATA_CONST.__cfstring: 0x4d00
+  __DATA_CONST.__cfstring: 0x4d40
   __DATA_CONST.__objc_classlist: 0x2c8
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0xd8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x280
-  __DATA_CONST.__objc_intobj: 0xa80
+  __DATA_CONST.__objc_intobj: 0xac8
   __DATA_CONST.__objc_arraydata: 0x2f8
   __DATA_CONST.__objc_arrayobj: 0x138
   __DATA_CONST.__objc_dictobj: 0x118
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA_CONST.__auth_got: 0x898
-  __DATA_CONST.__got: 0x9b0
+  __DATA_CONST.__got: 0x9b8
   __DATA_CONST.__auth_ptr: 0x20
   __DATA.__objc_const: 0xfcc8
-  __DATA.__objc_selrefs: 0x4308
+  __DATA.__objc_selrefs: 0x4320
   __DATA.__objc_ivar: 0x8a0
   __DATA.__objc_data: 0x1bd0
   __DATA.__data: 0xa50

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3168
-  Symbols:   573
-  CStrings:  5265
+  Functions: 3169
+  Symbols:   574
+  CStrings:  5273
 
Symbols:
+ _OBJC_CLASS_$_UARPDeviceProperties
CStrings:
+ "Classic"
+ "LE"
+ "decOpportunisticConnection only supported for LE peripherals (%u)"
+ "decOpportunisticConnection refCount:%ld %@ (%@)"
+ "deviceInactivityTimeout for device %@"
+ "didUpdateNotificationStateForCharacteristic - peripheral:%@ characteristic:%@ error:%@ transport:%@"
+ "incOpportunisticConnection only supported for LE peripherals. Current peripheral is connected over %@ (%@)"
+ "incOpportunisticConnection refCount:%ld %@ (%@)"
+ "initWithUUID:delegate:delegateQueue:deviceProperties:"
+ "setNumPacketRetries:"
+ "setTimeoutActivity:"
+ "setTimeoutPacketRetry:"
- "decOpportunisticConnection refCount:%ld %@"
- "didUpdateNotificationStateForCharacteristic - peripheral:%@ characteristic:%@ error:%@"
- "incOpportunisticConnection refCount:%ld %@"
- "initWithUUID:delegate:delegateQueue:"
```
