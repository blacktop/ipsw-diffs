## profiled

> `/usr/libexec/profiled`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_proto`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

 2483.40.19.0.0
-  __TEXT.__text: 0xc68b8
-  __TEXT.__auth_stubs: 0x2a00
-  __TEXT.__objc_stubs: 0x13480
+  __TEXT.__text: 0xc6920
+  __TEXT.__auth_stubs: 0x2a20
+  __TEXT.__objc_stubs: 0x134a0
   __TEXT.__objc_methlist: 0x6214
   __TEXT.__const: 0x138e
   __TEXT.__gcc_except_tab: 0x1210
   __TEXT.__oslogstring: 0x100b0
-  __TEXT.__cstring: 0xaa0a
-  __TEXT.__objc_methname: 0x16c17
+  __TEXT.__cstring: 0xaa4a
+  __TEXT.__objc_methname: 0x16c37
   __TEXT.__objc_classname: 0xbfe
   __TEXT.__objc_methtype: 0x23b2
   __TEXT.__constg_swiftt: 0xe94

   __TEXT.__unwind_info: 0x26c0
   __TEXT.__eh_frame: 0x190
   __DATA_CONST.__const: 0x3048
-  __DATA_CONST.__cfstring: 0x8700
+  __DATA_CONST.__cfstring: 0x8740
   __DATA_CONST.__objc_classlist: 0x2f8
   __DATA_CONST.__objc_catlist: 0x1e8
   __DATA_CONST.__objc_protolist: 0x78

   __DATA_CONST.__objc_arraydata: 0x38
   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA_CONST.__objc_dictobj: 0x50
-  __DATA_CONST.__auth_got: 0x1510
-  __DATA_CONST.__got: 0x2148
+  __DATA_CONST.__auth_got: 0x1520
+  __DATA_CONST.__got: 0x2150
   __DATA_CONST.__auth_ptr: 0x300
   __DATA.__objc_const: 0x7090
-  __DATA.__objc_selrefs: 0x54d8
+  __DATA.__objc_selrefs: 0x54e0
   __DATA.__objc_ivar: 0x204
   __DATA.__objc_data: 0x1ea8
   __DATA.__data: 0x900

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   Functions: 2738
-  Symbols:   1816
-  CStrings:  5779
+  Symbols:   1819
+  CStrings:  5782
 
Symbols:
+ _MCFeaturePairingWithHomeDevicesAllowed
+ _MCGestaltIsHomeAccessory
+ _MCLocalizedStringInTable
Functions:
~ sub_10001f3ec : 12 -> 68
~ sub_10001fdcc -> sub_10001fe04 : 12 -> 20
~ sub_100042984 -> sub_1000429c4 : 1092 -> 1116
~ sub_100046824 -> sub_10004687c : 336 -> 352
CStrings:
+ "INSTALL_PAIRED_COMPANION_CHOOSE_ACCESSORIES"
+ "Localizable-J490"
+ "areAnyHomeAccessoriesConfigured"
+ "restriction_allowPairingWithHomeDevices"
- "INSTALL_PAIRED_COMPANION_HOMEPOD"
```
