## libxml2.2.dylib

> `/usr/lib/libxml2.2.dylib`

```diff

-  __TEXT.__text: 0xc5fd0
+  __TEXT.__text: 0xc60e4
   __TEXT.__auth_stubs: 0x760
-  __TEXT.__cstring: 0x19aee
+  __TEXT.__cstring: 0x19bae
   __TEXT.__const: 0x3890
   __TEXT.__oslogstring: 0xa2
-  __TEXT.__unwind_info: 0x1b48
+  __TEXT.__unwind_info: 0x1b50
   __DATA_CONST.__got: 0x58
   __DATA_CONST.__const: 0x7b88
   __AUTH_CONST.__auth_got: 0x3b0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 2628
-  Symbols:   4067
-  CStrings:  3983
+  Functions: 2629
+  Symbols:   4069
+  CStrings:  3986
 
Sections:
~ __DATA_CONST.__const : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH.__data : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__data : content changed
Symbols:
+ _xmlSchemaIDCRegisterMatchers
Functions:
~ _xmlAddChild : 504 -> 540
~ _xmlC14NProcessNodeList : 3860 -> 3872
~ _xmlSchemaValidateElem : 3444 -> 3128
+ _xmlSchemaIDCRegisterMatchers
~ _xmlSchemaVAttributesSimple : 120 -> 152
~ _xmlSchemaXPathProcessHistory : 2748 -> 2800
CStrings:
+ "calling xmlSchemaIDCRegisterMatchers()"
+ "negative `pos` at selector (`depth >= matcher->depth` invariant violated)"
+ "negative `pos` in field handler (`depth >= matcher->depth` invariant violated)"

```
