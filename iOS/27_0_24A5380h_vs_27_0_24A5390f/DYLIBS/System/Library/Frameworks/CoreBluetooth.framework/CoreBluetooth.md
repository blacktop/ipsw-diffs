## CoreBluetooth

> `/System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-2700.43.0.0.0
-  __TEXT.__text: 0xd7a60
+2700.46.1.1.0
+  __TEXT.__text: 0xd7c3c
   __TEXT.__objc_methlist: 0xd6a4
   __TEXT.__const: 0x2d09
-  __TEXT.__oslogstring: 0x3110
-  __TEXT.__cstring: 0x1ae30
-  __TEXT.__gcc_except_tab: 0x25ec
+  __TEXT.__oslogstring: 0x3124
+  __TEXT.__cstring: 0x1ae67
+  __TEXT.__gcc_except_tab: 0x25f8
   __TEXT.__ustring: 0x82
   __TEXT.__unwind_info: 0x29e8
   __TEXT.__objc_stubs: 0x0

   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x68a0
+  __DATA_CONST.__const: 0x68b8
   __DATA_CONST.__objc_classlist: 0x358
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xf8

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 5532
-  Symbols:   10156
-  CStrings:  5108
+  Functions: 5533
+  Symbols:   10155
+  CStrings:  5111
 
Symbols:
- _objc_msgSend$_parseProximityServiceHomeKitAccessoryControlPtr:end:
Functions:
~ -[CBDevice descriptionWithLevel:] : 8524 -> 8644
+ sub_20749fda0
~ -[CBDeviceDataProximityService descriptionWithLevel:] : 2692 -> 2648
~ -[CBDevice _parseProximityServiceSubType:src:end:dataChanged:] : 408 -> 428
~ -[CBDevice _parseProximityServiceHomeKitAccessoryControlPtr:end:] : 944 -> 1048
~ _CBProximityServiceSubTypeToString : 176 -> 188
~ -[CBSpatialInteractionSession _activateXPCCompleted:reactivate:] : 1092 -> 1152
CStrings:
+ "%{public}s - pairingcode:0x%{private}016llX -> str:%{private}@"
+ "%{public}s - str:%{private}@ -> pairingcode:0x%{private}016llX"
+ ", OTA <private>"
+ ", stID <private>"
+ "MobileBluetooth-2700.46.1.1"
+ "RemoteDiagnostics"
- "%{public}s - pairingcode:0x%016llX -> str:%{public}@"
- "%{public}s - str:%{public}@ -> pairingcode:0x%016llX"
- "MobileBluetooth-2700.43"
```
