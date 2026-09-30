## LightSourceSupport

> `/System/Library/PrivateFrameworks/LightSourceSupport.framework/LightSourceSupport`

```diff

-7.0.67.1.105
-  __TEXT.__text: 0xd95c
+7.0.70.0.0
+  __TEXT.__text: 0xd9dc
   __TEXT.__auth_stubs: 0x770
   __TEXT.__objc_methlist: 0x9f4
-  __TEXT.__const: 0xbc
-  __TEXT.__cstring: 0xb35
+  __TEXT.__const: 0xdc
+  __TEXT.__cstring: 0xab7
   __TEXT.__oslogstring: 0x681
-  __TEXT.__gcc_except_tab: 0x458
+  __TEXT.__gcc_except_tab: 0x470
   __TEXT.__unwind_info: 0x570
   __TEXT.__objc_classname: 0x299
-  __TEXT.__objc_methname: 0x12b3
+  __TEXT.__objc_methname: 0x12c5
   __TEXT.__objc_methtype: 0xa7d
   __TEXT.__objc_stubs: 0xd40
   __DATA_CONST.__got: 0x130
-  __DATA_CONST.__const: 0x418
+  __DATA_CONST.__const: 0x410
   __DATA_CONST.__objc_classlist: 0xd0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x40

   __DATA_CONST.__objc_superrefs: 0xa0
   __AUTH_CONST.__auth_got: 0x3d0
   __AUTH_CONST.__const: 0x300
-  __AUTH_CONST.__cfstring: 0x660
-  __AUTH_CONST.__objc_const: 0x29b8
-  __AUTH_CONST.__objc_doubleobj: 0x140
-  __AUTH_CONST.__objc_intobj: 0x30
+  __AUTH_CONST.__cfstring: 0x580
+  __AUTH_CONST.__objc_const: 0x29d8
+  __AUTH_CONST.__objc_doubleobj: 0x110
+  __AUTH_CONST.__objc_intobj: 0x18
   __AUTH.__objc_data: 0x230
-  __DATA.__objc_ivar: 0x228
+  __DATA.__objc_ivar: 0x22c
   __DATA.__data: 0x308
   __DATA_DIRTY.__objc_data: 0x5f0
   __DATA_DIRTY.__bss: 0x158

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1F6F591F-A51E-32D1-BDE7-4513A374F2ED
-  Functions: 355
-  Symbols:   1589
-  CStrings:  676
+  UUID: 98B82C89-AFEC-3CF4-8324-534AF7897722
+  Functions: 356
+  Symbols:   1593
+  CStrings:  663
 
Symbols:
+ -[LSSController init].cold.9
+ _OBJC_IVAR_$_LSSController._responsiveMotion
+ ___21-[LSSController init]_block_invoke.23
+ ___21-[LSSController init]_block_invoke_3
+ ___block_literal_global.121
+ ___block_literal_global.155
+ ___block_literal_global.159
+ ___block_literal_global.164
+ ___block_literal_global.170
+ ___block_literal_global.175
- _LSSProviderOptionVisage
- ___21-[LSSController init]_block_invoke.20
- ___block_literal_global.117
- ___block_literal_global.187
- ___block_literal_global.191
- ___block_literal_global.196
- ___block_literal_global.202
- ___block_literal_global.207
Functions:
~ -[LSSController init] : 1372 -> 1580
+ ___21-[LSSController init]_block_invoke_3
~ -[LSSController .cxx_destruct] : 164 -> 176
~ +[LSSSettings _defaultSettings] : 952 -> 840
~ -[LSSController _setProviderTo:] : 696 -> 672
CStrings:
+ "\v"
+ "[32{?=\"time\"d\"intensity\"d\"direction\"\"referenceOrientation\"{?=\"vector\"}\"expectPause\"B}]"
+ "_responsiveMotion"
+ "responsiveMotion"
- "\n"
- "[16{?=\"time\"d\"intensity\"d\"direction\"\"referenceOrientation\"{?=\"vector\"}\"expectPause\"B}]"
- "visage"
- "visage_perimeterBias"
- "visage_segmentBias"
- "visage_segmentCount"
- "visage_sizeScale"
- "visage_temporalSmoothing"
- "visage_useSegments"
- "visage_yUpBias"

```
