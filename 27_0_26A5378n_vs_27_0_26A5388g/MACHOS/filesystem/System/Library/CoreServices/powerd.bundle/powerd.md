## powerd

> `/System/Library/CoreServices/powerd.bundle/powerd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`
- `__DATA.__common`

```diff

-2043.0.13.0.2
-  __TEXT.__text: 0x6db20
-  __TEXT.__auth_stubs: 0x1d60
+2043.0.31.0.0
+  __TEXT.__text: 0x6dd18
+  __TEXT.__auth_stubs: 0x1d90
   __TEXT.__objc_stubs: 0x4480
   __TEXT.__objc_methlist: 0x1dbc
   __TEXT.__const: 0x360
-  __TEXT.__cstring: 0x7a77
+  __TEXT.__cstring: 0x7a48
   __TEXT.__objc_methname: 0x5c5c
-  __TEXT.__oslogstring: 0xbcf4
+  __TEXT.__oslogstring: 0xbe0f
   __TEXT.__objc_classname: 0x2a8
   __TEXT.__objc_methtype: 0x7b1
   __TEXT.__gcc_except_tab: 0x3d4
   __TEXT.__dlopen_cstrs: 0x152
-  __TEXT.__unwind_info: 0x13b0
+  __TEXT.__unwind_info: 0x13c8
   __DATA_CONST.__const: 0x2570
-  __DATA_CONST.__cfstring: 0x6b20
+  __DATA_CONST.__cfstring: 0x6ae0
   __DATA_CONST.__objc_classlist: 0xb0
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_dictobj: 0xf0
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA_CONST.__objc_arrayobj: 0x348
-  __DATA_CONST.__auth_got: 0xec0
+  __DATA_CONST.__auth_got: 0xed8
   __DATA_CONST.__got: 0x380
   __DATA_CONST.__auth_ptr: 0x18
   __DATA.__objc_const: 0x3648

   __DATA.__objc_ivar: 0x2b8
   __DATA.__objc_data: 0x6e0
   __DATA.__data: 0x8f8
-  __DATA.__bss: 0xf28
+  __DATA.__bss: 0xf38
   __DATA.__common: 0x1270
   __CGPreLoginApp.__cgpreloginapp: 0x0
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libspindump.dylib
   - /usr/lib/libsystemstats.dylib
-  Functions: 2326
-  Symbols:   589
-  CStrings:  3687
+  Functions: 2330
+  Symbols:   592
+  CStrings:  3692
 
Symbols:
+ _IOPSLimitBatteryLevel
+ _IOPSLimitBatteryLevelCancel
+ _IOPSLimitBatteryLevelRegister
CStrings:
+ "3.2"
+ "ShipChargeLimit: Cleared battery level limit\n"
+ "ShipChargeLimit: Failed to %s battery limit: %#x\n"
+ "ShipChargeLimit: Failed to clear battery level limit %#x\n"
+ "ShipChargeLimit: Failed to register battery limit token: %#x\n"
+ "ShipChargeLimit: Failed to set battery level limit: %#x\n"
+ "ShipChargeLimit: Set battery level limit\n"
+ "clear"
+ "set"
- "3.1"
- "ShipChargeLimitCompliant"
- "ShipChargeLimitData incomplete\n"
- "ShippingChargeLimitSystemStatus"
```
