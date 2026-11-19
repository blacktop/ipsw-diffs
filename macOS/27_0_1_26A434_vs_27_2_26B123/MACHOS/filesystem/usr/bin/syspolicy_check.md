## syspolicy_check

> `/usr/bin/syspolicy_check`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_entry`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_dupclass`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-823.1.1.0.0
-  __TEXT.__text: 0x15a18
-  __TEXT.__auth_stubs: 0xd60
-  __TEXT.__objc_stubs: 0x1260
-  __TEXT.__objc_methlist: 0x6e4
-  __TEXT.__const: 0xae2
+823.40.13.0.0
+  __TEXT.__text: 0x15f68
+  __TEXT.__auth_stubs: 0xd90
+  __TEXT.__objc_stubs: 0x12a0
+  __TEXT.__objc_methlist: 0x6ec
+  __TEXT.__const: 0xaf2
   __TEXT.__cstring: 0x45f6
-  __TEXT.__oslogstring: 0xabe
+  __TEXT.__oslogstring: 0xb8e
   __TEXT.__gcc_except_tab: 0x2b4
-  __TEXT.__objc_methname: 0x1931
+  __TEXT.__objc_methname: 0x1991
   __TEXT.__objc_classname: 0x9a
-  __TEXT.__objc_methtype: 0x241
+  __TEXT.__objc_methtype: 0x24d
   __TEXT.__swift5_typeref: 0x1fe
   __TEXT.__swift5_reflstr: 0x54
   __TEXT.__swift5_assocty: 0x18

   __TEXT.__swift5_proto: 0x74
   __TEXT.__swift5_types: 0x24
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0x6c8
+  __TEXT.__unwind_info: 0x6d8
   __TEXT.__eh_frame: 0x258
   __DATA_CONST.__const: 0x6a0
   __DATA_CONST.__cfstring: 0x24c0

   __DATA_CONST.__objc_arrayobj: 0x150
   __DATA_CONST.__objc_dictobj: 0xf0
   __DATA_CONST.__objc_dupclass: 0x40
-  __DATA_CONST.__auth_got: 0x6c8
+  __DATA_CONST.__auth_got: 0x6e0
   __DATA_CONST.__got: 0x370
   __DATA_CONST.__auth_ptr: 0x188
-  __DATA.__objc_const: 0x1370
-  __DATA.__objc_selrefs: 0x6d8
-  __DATA.__objc_ivar: 0x12c
+  __DATA.__objc_const: 0x13b0
+  __DATA.__objc_selrefs: 0x6f0
+  __DATA.__objc_ivar: 0x134
   __DATA.__objc_data: 0x430
   __DATA.__data: 0x320
   __DATA.__common: 0x60

   - /usr/lib/swift/libswift_DarwinFoundation2.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 484
-  Symbols:   405
-  CStrings:  809
+  Functions: 488
+  Symbols:   408
+  CStrings:  820
 
Symbols:
+ _close
+ _fstat
+ _open
CStrings:
+ "Failed to stat target: %s error: %s"
+ "Target identity is not verified on %s: %s"
+ "Target is not the object that was scanned: (%d,%llu) != (%d,%llu), %s"
+ "URLByStandardizingPath"
+ "Unable to open target: %d, %s"
+ "Unable to stat target: %d, %s"
+ "_objectDev"
+ "_objectIno"
+ "i24@0:8^i16"
+ "openVerifiedDescriptorWithError:"
+ "pathComponents"
```
