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
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-2483.40.19.0.0
-  __TEXT.__text: 0xc6920
+2483.60.6.0.0
+  __TEXT.__text: 0xc69d8
   __TEXT.__auth_stubs: 0x2a20
   __TEXT.__objc_stubs: 0x134a0
   __TEXT.__objc_methlist: 0x6214
   __TEXT.__const: 0x138e
   __TEXT.__gcc_except_tab: 0x1210
   __TEXT.__oslogstring: 0x100b0
-  __TEXT.__cstring: 0xaa4a
+  __TEXT.__cstring: 0xaa6a
   __TEXT.__objc_methname: 0x16c37
   __TEXT.__objc_classname: 0xbfe
   __TEXT.__objc_methtype: 0x23b2

   __TEXT.__swift5_capture: 0x80
   __TEXT.__unwind_info: 0x26c0
   __TEXT.__eh_frame: 0x190
-  __DATA_CONST.__const: 0x3048
-  __DATA_CONST.__cfstring: 0x8740
+  __DATA_CONST.__const: 0x3050
+  __DATA_CONST.__cfstring: 0x8760
   __DATA_CONST.__objc_classlist: 0x2f8
   __DATA_CONST.__objc_catlist: 0x1e8
   __DATA_CONST.__objc_protolist: 0x78

   - /usr/lib/swift/libswiftos.dylib
   Functions: 2738
   Symbols:   1819
-  CStrings:  5782
+  CStrings:  5783
 
Functions:
~ sub_10006d9d4 : 2120 -> 2136
~ sub_100078178 -> sub_100078188 : 1008 -> 1096
~ sub_100078814 -> sub_10007887c : 1148 -> 1228
CStrings:
+ "ignoreUnrestrictableAppsList"
```
