## IOKit

> `/System/Library/CoreAccessories/PlugIns/Platform/IOKit.platform/IOKit`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-1210.0.0.502.1
+1216.0.0.0.0
   __TEXT.__text: 0xd67c
   __TEXT.__objc_methlist: 0xf5c
   __TEXT.__const: 0xa8
-  __TEXT.__cstring: 0x1208
+  __TEXT.__cstring: 0x1224
   __TEXT.__oslogstring: 0x2204
   __TEXT.__unwind_info: 0x2e8
   __TEXT.__objc_stubs: 0x0

   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x848
+  __DATA_CONST.__const: 0x858
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_superrefs: 0x30
   __DATA_CONST.__got: 0xe8
   __AUTH_CONST.__const: 0x220
-  __AUTH_CONST.__cfstring: 0x12c0
+  __AUTH_CONST.__cfstring: 0x12e0
   __AUTH_CONST.__objc_const: 0x1768
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__auth_got: 0x0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 416
-  Symbols:   1081
-  CStrings:  309
+  Symbols:   1083
+  CStrings:  310
 
Symbols:
+ _ACCUserDefaultsKey_BLEPairingAuthTimeoutValueS
+ _kCFACCUserDefaultsKey_BLEPairingAuthTimeoutValueS
CStrings:
+ "BLEPairingAuthTimeoutValueS"
```
