## iMessage

> `System/Library/Messages/PlugIns/iMessage.imservice/Contents/MacOS/iMessage`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__auth_ptr`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1450.700.71.0.0
-  __TEXT.__text: 0xd4998
+1450.700.71.1.2
+  __TEXT.__text: 0xd49cc
   __TEXT.__auth_stubs: 0x1af0
   __TEXT.__objc_stubs: 0xd000
   __TEXT.__objc_methlist: 0x29bc
   __TEXT.__const: 0xfe0
   __TEXT.__gcc_except_tab: 0xa040
   __TEXT.__cstring: 0x32dd
-  __TEXT.__oslogstring: 0x1748b
+  __TEXT.__oslogstring: 0x174eb
   __TEXT.__objc_classname: 0x68f
   __TEXT.__objc_methname: 0x12743
   __TEXT.__objc_methtype: 0x2ca9

   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 1899
   Symbols:   854
-  CStrings:  4601
+  CStrings:  4602
 
Functions:
~ sub_7978 : 4848 -> 4856
~ sub_17608 -> sub_17610 : 3336 -> 3344
~ sub_19bd8 -> sub_19be8 : 1584 -> 1592
~ sub_1dd70 -> sub_1dd88 : 2312 -> 2316
~ sub_2e798 -> sub_2e7b4 : 4624 -> 4548
~ sub_9c6b0 -> sub_9c680 : 3652 -> 3660
~ sub_9db04 -> sub_9dadc : 944 -> 1036
CStrings:
+ "Early return receiving message before first unlock, ignoring incoming message of type Other from %@"
```
