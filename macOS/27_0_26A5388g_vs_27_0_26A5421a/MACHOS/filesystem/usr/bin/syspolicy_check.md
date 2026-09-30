## syspolicy_check

> `/usr/bin/syspolicy_check`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_entry`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_dupclass`
- `__DATA_CONST.__got`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-823.0.3.0.0
-  __TEXT.__text: 0x15d1c
+823.1.1.0.0
+  __TEXT.__text: 0x15f88
   __TEXT.__auth_stubs: 0xd60
-  __TEXT.__objc_stubs: 0x1240
-  __TEXT.__objc_methlist: 0x6bc
+  __TEXT.__objc_stubs: 0x1260
+  __TEXT.__objc_methlist: 0x6e4
   __TEXT.__const: 0xae2
-  __TEXT.__cstring: 0x4546
+  __TEXT.__cstring: 0x45f6
   __TEXT.__oslogstring: 0xabe
   __TEXT.__gcc_except_tab: 0x2b4
-  __TEXT.__objc_methname: 0x18b1
+  __TEXT.__objc_methname: 0x1931
   __TEXT.__objc_classname: 0x9a
   __TEXT.__objc_methtype: 0x241
   __TEXT.__swift5_typeref: 0x1fe

   __TEXT.__swift5_proto: 0x74
   __TEXT.__swift5_types: 0x24
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0x500
+  __TEXT.__unwind_info: 0x508
   __TEXT.__eh_frame: 0x258
   __DATA_CONST.__const: 0x6a0
-  __DATA_CONST.__cfstring: 0x2460
+  __DATA_CONST.__cfstring: 0x24c0
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x30

   __DATA_CONST.__auth_got: 0x6c8
   __DATA_CONST.__got: 0x370
   __DATA_CONST.__auth_ptr: 0x188
-  __DATA.__objc_const: 0x1340
-  __DATA.__objc_selrefs: 0x6c0
-  __DATA.__objc_ivar: 0x128
+  __DATA.__objc_const: 0x1370
+  __DATA.__objc_selrefs: 0x6d8
+  __DATA.__objc_ivar: 0x12c
   __DATA.__objc_data: 0x430
   __DATA.__data: 0x320
   __DATA.__common: 0x60

   - /usr/lib/swift/libswift_DarwinFoundation2.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 480
+  Functions: 484
   Symbols:   405
-  CStrings:  801
+  CStrings:  809
 
CStrings:
+ "Passed codesign check"
+ "Re-sign the application using the codesign command after the bundle is fully assembled."
+ "T@\"NSURL\",&,N,V_quarantineOverrideURL"
+ "The code signature does not fully cover the bundle's Info.plist."
+ "_quarantineOverrideURL"
+ "ensureQuarantineStateChecked"
+ "quarantineOverrideURL"
+ "setQuarantineOverrideURL:"
```
