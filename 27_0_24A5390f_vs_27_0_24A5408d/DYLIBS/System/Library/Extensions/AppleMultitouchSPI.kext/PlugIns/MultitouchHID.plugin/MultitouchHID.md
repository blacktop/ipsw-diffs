## MultitouchHID

> `/System/Library/Extensions/AppleMultitouchSPI.kext/PlugIns/MultitouchHID.plugin/MultitouchHID`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__weak_got`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__weak_auth_got`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-10100.40.2.0.0
-  __TEXT.__text: 0x510a4
+10100.44.0.0.0
+  __TEXT.__text: 0x514fc
   __TEXT.__objc_methlist: 0x1e4
-  __TEXT.__const: 0x18f1
-  __TEXT.__cstring: 0x53b0
+  __TEXT.__const: 0x1901
+  __TEXT.__cstring: 0x5456
   __TEXT.__gcc_except_tab: 0xc84
-  __TEXT.__oslogstring: 0x361a
+  __TEXT.__oslogstring: 0x3630
   __TEXT.__unwind_info: 0x1588
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x780
+  __DATA_CONST.__const: 0x7c0
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__objc_arraydata: 0x20
   __DATA_CONST.__got: 0x188
-  __AUTH_CONST.__const: 0x2a78
-  __AUTH_CONST.__cfstring: 0x5d40
+  __AUTH_CONST.__const: 0x2a98
+  __AUTH_CONST.__cfstring: 0x5ee0
   __AUTH_CONST.__objc_const: 0x2e0
   __AUTH_CONST.__weak_auth_got: 0x18
   __AUTH_CONST.__objc_arrayobj: 0x18

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1598
-  Symbols:   2415
-  CStrings:  1290
+  Functions: 1601
+  Symbols:   2421
+  CStrings:  1306
 
Symbols:
+ _MGGetSInt32Answer
+ ____ZN18MultitouchHIDClass5probeEPK14__CFDictionaryjPi_block_invoke
+ ____ZN18MultitouchHIDClass5probeEPK14__CFDictionaryjPi_block_invoke_2
+ _analytics_send_event_lazy
+ _xpc_dictionary_create
+ _xpc_dictionary_set_int64
CStrings:
+ "AirPlay"
+ "Audio"
+ "BT-AACP"
+ "Blocked Transport: %@"
+ "BluetoothLowEnergy"
+ "DeviceClassNumber"
+ "FIFO"
+ "I2C"
+ "Inductive In-Band"
+ "SPI"
+ "SPU"
+ "Serial"
+ "Virtual"
+ "^v8@?0"
+ "com.apple.MultitouchSupport.TransportMatching"
+ "iAP"
```
