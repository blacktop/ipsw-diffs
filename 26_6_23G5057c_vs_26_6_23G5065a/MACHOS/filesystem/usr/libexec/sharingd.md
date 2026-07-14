## sharingd

> `/usr/libexec/sharingd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
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

-  __TEXT.__text: 0x7a4ef0
+  __TEXT.__text: 0x7a50cc
   __TEXT.__auth_stubs: 0x9e30
   __TEXT.__objc_stubs: 0x389e0
   __TEXT.__objc_methlist: 0x20244
-  __TEXT.__cstring: 0x42863
+  __TEXT.__cstring: 0x42893
   __TEXT.__objc_methname: 0x50a75
   __TEXT.__objc_classname: 0x65e7
   __TEXT.__objc_methtype: 0xbc4a
   __TEXT.__const: 0x1d6c0
   __TEXT.__gcc_except_tab: 0x6e30
-  __TEXT.__oslogstring: 0x40b73
+  __TEXT.__oslogstring: 0x40bc3
   __TEXT.__ustring: 0x94
   __TEXT.__dlopen_cstrs: 0x438
   __TEXT.__swift5_typeref: 0xa990

   __TEXT.__swift5_capture: 0x5328
   __TEXT.__swift_as_ret: 0x1058
   __TEXT.__swift5_mpenum: 0x1c
-  __TEXT.__unwind_info: 0x17a40
+  __TEXT.__unwind_info: 0x17a38
   __TEXT.__eh_frame: 0x29e54
   __DATA_CONST.__auth_got: 0x4f28
   __DATA_CONST.__got: 0x3608

   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 29416
   Symbols:   4560
-  CStrings:  28658
+  CStrings:  28660
 
CStrings:
+ "Paired Contact Manager: process %d tried to connect, but it was not entitled"
+ "com.apple.private.sharing.paired-contacts"
```
