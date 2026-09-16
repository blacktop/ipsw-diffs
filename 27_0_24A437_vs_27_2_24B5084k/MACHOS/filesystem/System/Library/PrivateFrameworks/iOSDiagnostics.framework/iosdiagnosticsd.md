## iosdiagnosticsd

> `/System/Library/PrivateFrameworks/iOSDiagnostics.framework/iosdiagnosticsd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1374.2.2.0.0
+1374.40.35.0.0
   __TEXT.__text: 0xd5a8
   __TEXT.__auth_stubs: 0x690
-  __TEXT.__objc_stubs: 0x2600
+  __TEXT.__objc_stubs: 0x25e0
   __TEXT.__objc_methlist: 0x16dc
-  __TEXT.__cstring: 0xc88
-  __TEXT.__objc_methname: 0x3609
+  __TEXT.__cstring: 0xcad
+  __TEXT.__objc_methname: 0x35ef
   __TEXT.__objc_classname: 0x32f
   __TEXT.__objc_methtype: 0x110b
   __TEXT.__const: 0x78

   __TEXT.__oslogstring: 0xdd5
   __TEXT.__unwind_info: 0x5c0
   __DATA_CONST.__const: 0x5d0
-  __DATA_CONST.__cfstring: 0xd60
+  __DATA_CONST.__cfstring: 0xd80
   __DATA_CONST.__objc_classlist: 0xd0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x78

   __DATA_CONST.__objc_intobj: 0x18
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA_CONST.__auth_got: 0x358
-  __DATA_CONST.__got: 0x288
+  __DATA_CONST.__got: 0x278
   __DATA.__objc_const: 0x4820
-  __DATA.__objc_selrefs: 0xd88
+  __DATA.__objc_selrefs: 0xd80
   __DATA.__objc_ivar: 0x164
   __DATA.__objc_data: 0x820
   __DATA.__data: 0x5a0

   - /System/Library/PrivateFrameworks/IDS.framework/IDS
   - /System/Library/PrivateFrameworks/MobileInBoxUpdate.framework/MobileInBoxUpdate
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
-  - /System/Library/PrivateFrameworks/NanoRegistry.framework/NanoRegistry
+  - /System/Library/PrivateFrameworks/PairedDeviceRegistry.framework/PairedDeviceRegistry
   - /System/Library/PrivateFrameworks/Sharing.framework/Sharing
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 419
-  Symbols:   195
+  Symbols:   193
   CStrings:  968
 
Symbols:
+ _OBJC_CLASS_$_PDRDevice
- _NRDevicePropertyIsPaired
- _OBJC_CLASS_$_NRDevice
- _OBJC_CLASS_$_NRPairedDeviceRegistry
CStrings:
+ "00000000-0000-0000-0000-000000000000"
+ "bluetoothIdentifier"
+ "isEqualToPDRDevice:"
+ "isPaired"
- "deviceIDForNRDevice:"
- "isEqualToNRDevice:"
- "isEqualToNumber:"
- "valueForProperty:"
```
