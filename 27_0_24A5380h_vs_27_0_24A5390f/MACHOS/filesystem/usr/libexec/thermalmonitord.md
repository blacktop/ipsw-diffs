## thermalmonitord

> `/usr/libexec/thermalmonitord`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_selrefs`
- `__DATA.__data`
- `__DATA.__bss`
- `__DATA.__common`

```diff

-2076.0.0.0.0
-  __TEXT.__text: 0x568a4
-  __TEXT.__auth_stubs: 0x13c0
+2081.0.0.0.1
+  __TEXT.__text: 0x5740c
+  __TEXT.__auth_stubs: 0x13d0
   __TEXT.__objc_stubs: 0x4f20
-  __TEXT.__objc_methlist: 0x4254
+  __TEXT.__objc_methlist: 0x426c
   __TEXT.__const: 0x1cc0
-  __TEXT.__objc_classname: 0x1461
+  __TEXT.__objc_classname: 0x1484
   __TEXT.__objc_methtype: 0x1b05
-  __TEXT.__objc_methname: 0x83a7
-  __TEXT.__cstring: 0x4da2
-  __TEXT.__gcc_except_tab: 0x390
-  __TEXT.__oslogstring: 0x9a88
-  __TEXT.__unwind_info: 0x12b0
-  __DATA_CONST.__const: 0x1450
-  __DATA_CONST.__cfstring: 0x6740
-  __DATA_CONST.__objc_classlist: 0x570
+  __TEXT.__objc_methname: 0x83da
+  __TEXT.__cstring: 0x4e09
+  __TEXT.__gcc_except_tab: 0x3ac
+  __TEXT.__oslogstring: 0x9d83
+  __TEXT.__unwind_info: 0x12d0
+  __DATA_CONST.__const: 0x1458
+  __DATA_CONST.__cfstring: 0x67e0
+  __DATA_CONST.__objc_classlist: 0x578
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_dictobj: 0x730
   __DATA_CONST.__objc_arrayobj: 0x2b8
   __DATA_CONST.__objc_doubleobj: 0x40
-  __DATA_CONST.__auth_got: 0x9f8
-  __DATA_CONST.__got: 0x680
+  __DATA_CONST.__auth_got: 0xa00
+  __DATA_CONST.__got: 0x688
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA.__objc_const: 0xd108
+  __DATA.__objc_const: 0xd1d8
   __DATA.__objc_selrefs: 0x1988
-  __DATA.__objc_ivar: 0xa70
-  __DATA.__objc_data: 0x3660
+  __DATA.__objc_ivar: 0xa78
+  __DATA.__objc_data: 0x36b0
   __DATA.__data: 0x370
   __DATA.__bss: 0xb05c
   __DATA.__common: 0x9f6

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2044
-  Symbols:   415
-  CStrings:  3743
+  Functions: 2056
+  Symbols:   416
+  CStrings:  3764
 
Symbols:
+ _CFDictionaryCreateMutableCopy
CStrings:
+ "<Error> Failed to upgrade NVRAM V2 to V3, resetting persistence"
+ "<Error> getBatteryPackCount: invalid pack count %d; defaulting to 1\n"
+ "<Error> getBatteryPackCount: no AppleSmartBattery service\n"
+ "<Error> getChemIDForPack: BatteryData NULL for PackID %d\n"
+ "<Error> getChemIDForPack: CFNumberCreate failed for PackID %d\n"
+ "<Error> getChemIDForPack: chemIDOut must not be NULL\n"
+ "<Error> getChemIDForPack: pack 0 present but unreadable; using default P0 threshold\n"
+ "<Error> getChemIDForPack: pack 1 present but unreadable; using default P0 threshold\n"
+ "<Notice> BackLightCCSingle: frame-based display power enabled at %d Hz"
+ "<Notice> getBatteryPackCount: %d"
+ "<Notice> getChemIDForPack: no AppleSmartBatteryBank for PackID %d"
+ "<Notice> getChemIDForPack: pack %d success %d chemID %d"
+ "AppleSmartBattery"
+ "BatteryPackCount"
+ "PackID"
+ "_fixedDisplayFrameRate"
+ "_usesFrameBasedDisplayPower"
+ "fixedDisplayFrameRate"
+ "frame_count"
+ "tm5142f10796d37035f25c6c85ab01b420"
+ "usesFrameBasedDisplayPower"
```
