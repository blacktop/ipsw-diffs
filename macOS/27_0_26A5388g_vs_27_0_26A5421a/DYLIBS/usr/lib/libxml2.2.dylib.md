## libxml2.2.dylib

> `/usr/lib/libxml2.2.dylib`

```diff

-39.10.3.0.0
-  __TEXT.__text: 0xc6810
+40.1.0.0.0
+  __TEXT.__text: 0xc69d0
   __TEXT.__cstring: 0x19cde
   __TEXT.__const: 0x3890
   __TEXT.__oslogstring: 0xa2
-  __TEXT.__unwind_info: 0x1ba0
+  __TEXT.__unwind_info: 0x1ba8
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x7b88
   __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0xac0
-  __AUTH_CONST.__auth_got: 0x3b0
+  __AUTH_CONST.__auth_got: 0x3b8
   __AUTH.__data: 0x130
   __DATA.__data: 0x338
   __DATA.__bss: 0xba0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 2629
-  Symbols:   3107
+  Functions: 2632
+  Symbols:   3111
   CStrings:  3986
 
Symbols:
+ _strstr
+ _xmlEncodingErr
+ _xmlGrowArray_type
+ _xmlParseLookupString
Functions:
~ _xmlParseTryOrFinish : 5116 -> 5036
~ _xmlOutputBufferWrite : 564 -> 588
~ _xmlOutputBufferFlush : 344 -> 380
+ _xmlEncodingErr
~ _xmlCharEncInFunc : 440 -> 456
~ _xmlCharEncOutFunc : 864 -> 876
+ _xmlParseLookupString
~ _xmlRelaxNGNewDefine : 252 -> 260
~ _xmlRelaxNGAddValidError : 540 -> 544
~ _xmlRelaxNGElemPush : 200 -> 208
~ _xmlRelaxNGFreeStates : 256 -> 260
~ _xmlRelaxNGCleanupTree : 4892 -> 4900
~ _xmlRelaxNGGetElements : 412 -> 440
~ _xmlRelaxNGAddStates : 416 -> 424
+ _xmlGrowArray_type
```
