## SidecarRelay

> `/usr/libexec/SidecarRelay`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__swift5_entry`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__cstring`
- `__TEXT.__swift5_capture`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__bss`
- `__DATA.__common`

```diff

-400.39.0.0.0
-  __TEXT.__text: 0x8788c
+400.40.0.0.0
+  __TEXT.__text: 0x87b0c
   __TEXT.__auth_stubs: 0x1ce0
-  __TEXT.__objc_stubs: 0x1a40
+  __TEXT.__objc_stubs: 0x1a60
   __TEXT.__objc_methlist: 0xb40
-  __TEXT.__const: 0x49cd
+  __TEXT.__const: 0x49dd
   __TEXT.__swift5_entry: 0x8
   __TEXT.__constg_swiftt: 0x2004
   __TEXT.__swift5_typeref: 0x1c9c

   __TEXT.__objc_classname: 0xba5
   __TEXT.__objc_methtype: 0x106f
   __TEXT.__swift5_protos: 0x40
-  __TEXT.__objc_methname: 0x2539
+  __TEXT.__objc_methname: 0x2549
   __TEXT.__cstring: 0x14ed
   __TEXT.__oslogstring: 0x2602
   __TEXT.__swift5_capture: 0x3e64

   __DATA_CONST.__objc_protorefs: 0x78
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__auth_got: 0xe78
-  __DATA_CONST.__got: 0x4f8
+  __DATA_CONST.__got: 0x500
   __DATA_CONST.__auth_ptr: 0x640
   __DATA.__objc_const: 0x2ce0
-  __DATA.__objc_selrefs: 0x820
+  __DATA.__objc_selrefs: 0x828
   __DATA.__objc_ivar: 0x14
   __DATA.__objc_data: 0x1638
-  __DATA.__data: 0x38f8
+  __DATA.__data: 0x3908
   __DATA.__bss: 0x5720
   __DATA.__common: 0x110
   - /System/Library/Frameworks/Combine.framework/Combine

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 4566
-  Symbols:   773
-  CStrings:  879
+  Symbols:   774
+  CStrings:  880
 
Symbols:
+ _RPOptionStatusFlags
CStrings:
+ "400.40"
+ "initWithUnsignedLongLong:"
- "400.39"
```
