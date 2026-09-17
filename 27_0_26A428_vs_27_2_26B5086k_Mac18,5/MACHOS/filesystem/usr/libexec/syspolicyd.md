## syspolicyd

> `/usr/libexec/syspolicyd`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__dof_security_`
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
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-823.1.1.0.0
-  __TEXT.__text: 0xb0590
-  __TEXT.__auth_stubs: 0x2c50
-  __TEXT.__objc_stubs: 0xa5e0
+823.40.10.0.0
+  __TEXT.__text: 0xb0a18
+  __TEXT.__auth_stubs: 0x2c60
+  __TEXT.__objc_stubs: 0xa620
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0x53bc
+  __TEXT.__objc_methlist: 0x53cc
   __TEXT.__const: 0x1ff8
-  __TEXT.__objc_methname: 0xd1f1
-  __TEXT.__cstring: 0x11bb3
+  __TEXT.__objc_methname: 0xd25a
+  __TEXT.__cstring: 0x11c33
   __TEXT.__objc_classname: 0x838
-  __TEXT.__objc_methtype: 0x280b
-  __TEXT.__oslogstring: 0xa0d6
-  __TEXT.__gcc_except_tab: 0x1c20
+  __TEXT.__objc_methtype: 0x27f0
+  __TEXT.__oslogstring: 0xa106
+  __TEXT.__gcc_except_tab: 0x1c3c
   __TEXT.__swift5_typeref: 0x410
   __TEXT.__swift5_capture: 0x1b4
   __TEXT.__constg_swiftt: 0x4a0

   __TEXT.__swift5_proto: 0x40
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__dof_security_: 0x325
-  __TEXT.__unwind_info: 0x33d0
+  __TEXT.__unwind_info: 0x33d8
   __TEXT.__eh_frame: 0x1b8
   __DATA_CONST.__const: 0x3c98
-  __DATA_CONST.__cfstring: 0x8d00
+  __DATA_CONST.__cfstring: 0x8e20
   __DATA_CONST.__objc_classlist: 0x318
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xa0

   __DATA_CONST.__objc_arraydata: 0x5a8
   __DATA_CONST.__objc_arrayobj: 0x2a0
   __DATA_CONST.__objc_dictobj: 0xa0
-  __DATA_CONST.__auth_got: 0x1640
+  __DATA_CONST.__auth_got: 0x1648
   __DATA_CONST.__got: 0x8f8
   __DATA_CONST.__auth_ptr: 0x208
-  __DATA.__objc_const: 0x9f70
-  __DATA.__objc_selrefs: 0x2f20
+  __DATA.__objc_const: 0x9f78
+  __DATA.__objc_selrefs: 0x2f30
   __DATA.__objc_ivar: 0x814
   __DATA.__objc_data: 0x2208
   __DATA.__data: 0xdb2

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3593
-  Symbols:   1065
-  CStrings:  5570
+  Functions: 3595
+  Symbols:   1066
+  CStrings:  5583
 
Symbols:
+ __CFBundleFlushBundleCaches
CStrings:
+ "Absent"
+ "Clean"
+ "DurationMs"
+ "Errno(%d)"
+ "HashLength"
+ "HashType"
+ "Online"
+ "Result"
+ "Unable to open %@ to refresh its localizations."
+ "bundleURL"
+ "com.apple.syspolicy.Gatekeeper.RevocationLookup"
+ "sendTicketLookupWithHashLength:withHashType:wasOnline:withResult:withDurationMs:"
+ "v44@0:8Q16I24B28i32d36"
```
