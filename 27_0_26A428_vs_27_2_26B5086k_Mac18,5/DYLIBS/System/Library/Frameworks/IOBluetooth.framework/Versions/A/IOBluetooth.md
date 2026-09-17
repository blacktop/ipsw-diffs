## IOBluetooth

> `/System/Library/Frameworks/IOBluetooth.framework/Versions/A/IOBluetooth`

```diff

-2700.51.0.0.0
-  __TEXT.__text: 0x6d440
+2701.3.0.0.0
+  __TEXT.__text: 0x6d93c
   __TEXT.__objc_methlist: 0x8c4c
-  __TEXT.__cstring: 0xbea8
+  __TEXT.__cstring: 0xbee8
   __TEXT.__gcc_except_tab: 0x344
   __TEXT.__const: 0x49c
   __TEXT.__oslogstring: 0x4f93

   __DATA_CONST.__objc_classrefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x188
   __DATA_CONST.__objc_arraydata: 0x30
-  __DATA_CONST.__got: 0x4b0
+  __DATA_CONST.__got: 0x4a8
   __AUTH_CONST.__const: 0x8e0
-  __AUTH_CONST.__cfstring: 0x77e0
+  __AUTH_CONST.__cfstring: 0x7800
   __AUTH_CONST.__objc_const: 0xc7a0
   __AUTH_CONST.__objc_intobj: 0xc0
   __AUTH_CONST.__objc_arrayobj: 0x90

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 3526
-  Symbols:   6541
-  CStrings:  1934
+  Symbols:   6540
+  CStrings:  1935
 
Symbols:
- _CBManagerIsIOBluetoothShim
Functions:
~ -[IOBluetoothAutomaticDeviceSetup startLEScans] : 552 -> 540
~ -[IOBluetoothSDPDataElement(IOBluetoothSDPDataElementPrivate) initWithiOSBytes:maxLength:bytesUsed:] : 852 -> 860
~ _OBEXAddBodyHeader : 140 -> 164
~ _OBEXHeadersToBytes : 3784 -> 4152
~ _OBEXGetHeaders : 2328 -> 3284
~ -[IOBluetoothCoreBluetoothCoordinator init] : 1352 -> 1296
~ -[IOBluetoothDevicePair init] : 384 -> 372
CStrings:
+ "SDP element header exceeds buffer: maxLength=%u < 3-byte header"
```
