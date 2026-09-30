## sysdiagnose_helper

> `/usr/libexec/sysdiagnose_helper`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

 1598.40.4.0.0
-  __TEXT.__text: 0x24fe0
+  __TEXT.__text: 0x25124
   __TEXT.__auth_stubs: 0xfe0
   __TEXT.__objc_stubs: 0x17c0
   __TEXT.__objc_methlist: 0x5e4
   __TEXT.__const: 0x490
   __TEXT.__gcc_except_tab: 0x7c4
   __TEXT.__oslogstring: 0x2781
-  __TEXT.__cstring: 0x995c
+  __TEXT.__cstring: 0x99af
   __TEXT.__objc_classname: 0xfc
   __TEXT.__objc_methtype: 0x2a9
   __TEXT.__objc_methname: 0x1735

   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 365
   Symbols:   357
-  CStrings:  2207
+  CStrings:  2210
 
Functions:
~ sub_100011cf0 : 68644 -> 68968
CStrings:
+ "OpenBandExtraSensesOnLastWLPerMode"
+ "OpenBandExtraSensesPerMode"
+ "OpenBandReadsPerMode"
```
