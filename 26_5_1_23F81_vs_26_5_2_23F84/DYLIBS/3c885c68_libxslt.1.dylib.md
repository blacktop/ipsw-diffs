## libxslt.1.dylib

> `/usr/lib/libxslt.1.dylib`

```diff

-  __TEXT.__text: 0x21e00
-  __TEXT.__auth_stubs: 0xde0
+  __TEXT.__text: 0x21dfc
+  __TEXT.__auth_stubs: 0xdc0
   __TEXT.__cstring: 0x7255
   __TEXT.__const: 0xc0
   __TEXT.__unwind_info: 0x4e0
   __DATA_CONST.__got: 0x48
   __DATA_CONST.__const: 0x228
-  __AUTH_CONST.__auth_got: 0x6f0
+  __AUTH_CONST.__auth_got: 0x6e0
   __AUTH_CONST.__const: 0x40
   __DATA.__data: 0x28
   __DATA.__bss: 0x461

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libxml2.2.dylib
   Functions: 393
-  Symbols:   821
+  Symbols:   819
   CStrings:  892
 
Sections:
~ __TEXT.__cstring : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __AUTH_CONST.__const : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__data : content changed
Symbols:
+ _arc4random_buf
- _random
- _srandom
- _time
Functions:
~ _xsltAttribute : 1240 -> 1256
~ __initBaseValue : 68 -> 16
~ _xsltInitCtxtKey : 1340 -> 1348
~ _xsltApplySequenceConstructor : 2204 -> 2184
~ _xsltPreCompEval : 108 -> 124
~ _xsltPreCompEvalToBoolean : 108 -> 124
~ _xsltParseTemplateContent : 1120 -> 1128
~ _xsltComputeSortResultInternal : 540 -> 544

```
