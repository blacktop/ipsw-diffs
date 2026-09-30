## tvremoted

> `/usr/libexec/tvremoted`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-627.0.28.0.0
-  __TEXT.__text: 0x10e7c
+627.10.45.0.0
+  __TEXT.__text: 0x1107c
   __TEXT.__auth_stubs: 0x510
-  __TEXT.__objc_stubs: 0x2620
-  __TEXT.__objc_methlist: 0xf44
+  __TEXT.__objc_stubs: 0x2640
+  __TEXT.__objc_methlist: 0xf54
   __TEXT.__const: 0xca
   __TEXT.__gcc_except_tab: 0x1a4
   __TEXT.__cstring: 0xb5d
-  __TEXT.__objc_methname: 0x32b7
-  __TEXT.__oslogstring: 0x26d7
+  __TEXT.__objc_methname: 0x32e0
+  __TEXT.__oslogstring: 0x2716
   __TEXT.__objc_classname: 0x13d
   __TEXT.__objc_methtype: 0xf7a
-  __TEXT.__unwind_info: 0x520
+  __TEXT.__unwind_info: 0x528
   __DATA_CONST.__const: 0x6c8
   __DATA_CONST.__cfstring: 0x960
   __DATA_CONST.__objc_classlist: 0x28

   __DATA_CONST.__auth_got: 0x298
   __DATA_CONST.__got: 0x220
   __DATA.__objc_const: 0xe60
-  __DATA.__objc_selrefs: 0xcc8
+  __DATA.__objc_selrefs: 0xcd0
   __DATA.__objc_ivar: 0x7c
   __DATA.__objc_data: 0x190
   __DATA.__data: 0x360

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 333
+  Functions: 334
   Symbols:   164
-  CStrings:  938
+  CStrings:  940
 
Functions:
~ sub_100008cd4 : 464 -> 524
+ sub_10000f858
CStrings:
+ "Not relinquishing %@ - a client connection is still interested"
+ "_hasInterestedClientConnectionForDevice:"
```
