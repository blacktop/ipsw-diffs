## SpaceAttribution

> `/System/Library/PrivateFrameworks/SpaceAttribution.framework/Versions/A/SpaceAttribution`

```diff

-496.0.1.0.0
-  __TEXT.__text: 0x141e8
-  __TEXT.__objc_methlist: 0x14b0
+499.40.4.0.1
+  __TEXT.__text: 0x143b4
+  __TEXT.__objc_methlist: 0x14d0
   __TEXT.__const: 0x160
-  __TEXT.__cstring: 0x1326
+  __TEXT.__cstring: 0x1331
   __TEXT.__oslogstring: 0x11e6
-  __TEXT.__gcc_except_tab: 0x6c0
-  __TEXT.__unwind_info: 0x688
+  __TEXT.__gcc_except_tab: 0x6e8
+  __TEXT.__unwind_info: 0x690
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0xb0
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xdf0
+  __DATA_CONST.__objc_selrefs: 0xe08
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x68
   __DATA_CONST.__objc_arraydata: 0x138
   __DATA_CONST.__got: 0x150
   __AUTH_CONST.__const: 0x5f0
-  __AUTH_CONST.__cfstring: 0x1400
-  __AUTH_CONST.__objc_const: 0x1ec8
+  __AUTH_CONST.__cfstring: 0x1420
+  __AUTH_CONST.__objc_const: 0x1ef8
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__auth_got: 0x0
-  __DATA.__objc_ivar: 0x140
+  __DATA.__objc_ivar: 0x144
   __DATA.__data: 0x180
   __DATA.__bss: 0x68
   __DATA_DIRTY.__objc_data: 0x6e0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 607
-  Symbols:   1224
-  CStrings:  314
+  Functions: 610
+  Symbols:   1230
+  CStrings:  315
 
Symbols:
+ -[SAAppSizerResults addToVCCDetails:key:]
+ -[SAAppSizerResults setVccDetails:]
+ -[SAAppSizerResults vccDetails]
+ GCC_except_table110
+ GCC_except_table114
+ GCC_except_table123
+ OBJC_IVAR_$_SAAppSizerResults._vccDetails
+ _objc_msgSend$vccDetails
- GCC_except_table113
- GCC_except_table122
Functions:
~ -[SAAppSizerResults init] : 380 -> 404
+ -[SAAppSizerResults addToVCCDetails:key:]
~ -[SAAppSizerResults encodeWithCoder:] : 632 -> 652
~ -[SAAppSizerResults initWithCoder:] : 2052 -> 2164
+ -[SAAppSizerResults zeroSizeApps]
+ -[SAAppSizerResults setTotalPurgeableDataSize:]
~ -[SAAppSizerResults .cxx_destruct] : 248 -> 260
CStrings:
+ "vccDetails"
```
