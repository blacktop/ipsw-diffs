## CoreBluetooth

> `/System/Library/Frameworks/CoreBluetooth.framework/Versions/A/CoreBluetooth`

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
-  __TEXT.__text: 0xe070c
+2700.46.1.1.0
+  __TEXT.__text: 0xe08f8
   __TEXT.__objc_methlist: 0xd64c
   __TEXT.__const: 0x2cf9
-  __TEXT.__oslogstring: 0x30d0
-  __TEXT.__cstring: 0x1b0b8
-  __TEXT.__gcc_except_tab: 0x264c
+  __TEXT.__oslogstring: 0x30e4
+  __TEXT.__cstring: 0x1b0ef
+  __TEXT.__gcc_except_tab: 0x2658
   __TEXT.__ustring: 0x82
   __TEXT.__unwind_info: 0x28c8
   __TEXT.__objc_stubs: 0x0

   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x5a30
+  __DATA_CONST.__const: 0x5a48
   __DATA_CONST.__objc_classlist: 0x350
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xf8

   - /System/Library/PrivateFrameworks/TCC.framework/Versions/A/TCC
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 5580
-  Symbols:   10198
-  CStrings:  5117
+  Functions: 5581
+  Symbols:   10197
+  CStrings:  5120
 
Symbols:
- _objc_msgSend$_parseProximityServiceHomeKitAccessoryControlPtr:end:
Functions:
+ sub_19c93c7e8
~ -[CBDeviceDataProximityService descriptionWithLevel:] : 2824 -> 2780
~ -[CBDevice descriptionWithLevel:] : 9136 -> 9272
~ -[CBDevice _parseProximityServiceSubType:src:end:dataChanged:] : 408 -> 428
~ -[CBDevice _parseProximityServiceHomeKitAccessoryControlPtr:end:] : 1064 -> 1168
~ _CBProximityServiceSubTypeToString : 176 -> 188
~ -[CBSpatialInteractionSession _activateXPCCompleted:reactivate:] : 1132 -> 1192
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
