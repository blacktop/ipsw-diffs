## Diagnostics

> `filesystem/Applications/Diagnostics.app/Diagnostics`

```diff

-1066.120.12.0.0
-  __TEXT.__text: 0x15f188
+1066.120.14.0.0
+  __TEXT.__text: 0x15f1e0
   __TEXT.__auth_stubs: 0x42d0
-  __TEXT.__objc_stubs: 0xab60
+  __TEXT.__objc_stubs: 0xab80
   __TEXT.__objc_methlist: 0x67a4
   __TEXT.__gcc_except_tab: 0xc84
-  __TEXT.__objc_methname: 0x11b15
+  __TEXT.__objc_methname: 0x11b55
   __TEXT.__objc_classname: 0x240b
   __TEXT.__objc_methtype: 0x4059
   __TEXT.__const: 0x98f4
   __TEXT.__cstring: 0x93ad
-  __TEXT.__oslogstring: 0x396d
+  __TEXT.__oslogstring: 0x397d
   __TEXT.__ustring: 0x64
   __TEXT.__constg_swiftt: 0x6438
   __TEXT.__swift5_typeref: 0x62f4

   __TEXT.__swift5_protos: 0x4c
   __TEXT.__swift5_mpenum: 0x20
   __TEXT.__swift5_acfuncs: 0x17c
-  __TEXT.__unwind_info: 0x4c88
+  __TEXT.__unwind_info: 0x4c90
   __TEXT.__eh_frame: 0x445c
   __DATA_CONST.__auth_got: 0x2178
-  __DATA_CONST.__got: 0x1288
+  __DATA_CONST.__got: 0x1290
   __DATA_CONST.__auth_ptr: 0x12b8
   __DATA_CONST.__const: 0xd570
   __DATA_CONST.__cfstring: 0x1ce0

   __DATA_CONST.__objc_arrayobj: 0x78
   __DATA_CONST.__objc_floatobj: 0x20
   __DATA.__objc_const: 0x1e508
-  __DATA.__objc_selrefs: 0x3b48
+  __DATA.__objc_selrefs: 0x3b50
   __DATA.__objc_ivar: 0x370
   __DATA.__objc_data: 0x93f8
   __DATA.__data: 0x7638

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 5EC83888-690F-3676-AC3E-B2E3DB121842
+  UUID: 35ECA4A0-73EC-3CD9-B78D-784D3C7A1520
   Functions: 7112
-  Symbols:   2003
-  CStrings:  4938
+  Symbols:   2004
+  CStrings:  4939
 
Symbols:
+ _OBJC_CLASS_$_ASTAuthInfoResultErrorObject
CStrings:
+ "Bad auth info certificate: %@ or attestation blob: %@"
+ "authInfoResultWithAttestation:certificate:type:errorObject:"
+ "errorObjectWithError:resultCode:"
- "Bad auth info certificate or attestation blob: %@"
- "authInfoResultWithAttestation:certificate:type:error:"

```
