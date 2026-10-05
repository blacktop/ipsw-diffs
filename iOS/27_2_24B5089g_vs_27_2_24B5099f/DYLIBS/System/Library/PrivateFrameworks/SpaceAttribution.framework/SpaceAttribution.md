## SpaceAttribution

> `/System/Library/PrivateFrameworks/SpaceAttribution.framework/SpaceAttribution`

```diff

-499.40.3.0.0
-  __TEXT.__text: 0x1317c
-  __TEXT.__objc_methlist: 0x14b0
+499.40.4.0.0
+  __TEXT.__text: 0x13320
+  __TEXT.__objc_methlist: 0x14d0
   __TEXT.__const: 0x160
-  __TEXT.__cstring: 0x1367
+  __TEXT.__cstring: 0x1372
   __TEXT.__oslogstring: 0x13e1
-  __TEXT.__gcc_except_tab: 0x6d0
-  __TEXT.__unwind_info: 0x898
+  __TEXT.__gcc_except_tab: 0x6f8
+  __TEXT.__unwind_info: 0x8a0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0xb0
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xe08
+  __DATA_CONST.__objc_selrefs: 0xe20
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x68
   __DATA_CONST.__objc_arraydata: 0x138
   __DATA_CONST.__got: 0x168
   __AUTH_CONST.__const: 0x140
-  __AUTH_CONST.__cfstring: 0x1420
-  __AUTH_CONST.__objc_const: 0x1ec8
+  __AUTH_CONST.__cfstring: 0x1440
+  __AUTH_CONST.__objc_const: 0x1ef8
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__auth_got: 0x0
-  __DATA.__objc_ivar: 0x140
+  __DATA.__objc_ivar: 0x144
   __DATA.__data: 0x180
   __DATA_DIRTY.__objc_data: 0x6e0
   __DATA_DIRTY.__bss: 0x20

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 598
-  Symbols:   966
-  CStrings:  328
+  Functions: 601
+  Symbols:   971
+  CStrings:  329
 
Symbols:
+ -[SAAppSizerResults addToVCCDetails:key:]
+ -[SAAppSizerResults setVccDetails:]
+ -[SAAppSizerResults vccDetails]
+ GCC_except_table102
+ GCC_except_table106
+ GCC_except_table113
+ _OBJC_IVAR_$_SAAppSizerResults._vccDetails
- GCC_except_table105
- GCC_except_table112
Functions:
~ -[SAAppSizerResults init] : 340 -> 360
+ -[SAAppSizerResults addToVCCDetails:key:]
~ -[SAAppSizerResults encodeWithCoder:] : 616 -> 636
~ -[SAAppSizerResults initWithCoder:] : 1940 -> 2044
+ -[SAAppSizerResults zeroSizeApps]
+ -[SAAppSizerResults setTotalPurgeableDataSize:]
~ -[SAAppSizerResults .cxx_destruct] : 236 -> 248
CStrings:
+ "vccDetails"
```
