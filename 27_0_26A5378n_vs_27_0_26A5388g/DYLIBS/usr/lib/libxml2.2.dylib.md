## libxml2.2.dylib

> `/usr/lib/libxml2.2.dylib`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__AUTH_CONST.__const`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__data`

```diff

-39.10.2.0.0
-  __TEXT.__text: 0xc672c
-  __TEXT.__cstring: 0x19c1e
+39.10.3.0.0
+  __TEXT.__text: 0xc6810
+  __TEXT.__cstring: 0x19cde
   __TEXT.__const: 0x3890
   __TEXT.__oslogstring: 0xa2
-  __TEXT.__unwind_info: 0x1b98
+  __TEXT.__unwind_info: 0x1ba0
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x7b88
   __DATA_CONST.__got: 0x0

   __AUTH.__data: 0x130
   __DATA.__data: 0x338
   __DATA.__bss: 0xba0
-  __DATA.__common: 0xbc
+  __DATA.__common: 0x64
   __DATA_DIRTY.__data: 0x250
   __DATA_DIRTY.__bss: 0x448
-  __DATA_DIRTY.__common: 0x18
+  __DATA_DIRTY.__common: 0x70
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 2628
-  Symbols:   3106
-  CStrings:  3983
+  Functions: 2629
+  Symbols:   3107
+  CStrings:  3986
 
Symbols:
+ _xmlSchemaIDCRegisterMatchers
Functions:
~ _xmlAddChild : 504 -> 540
~ _xmlC14NProcessNodeList : 3856 -> 3868
~ _xmlSchemaValidateElem : 3532 -> 3168
+ _xmlSchemaIDCRegisterMatchers
~ _xmlSchemaVAttributesSimple : 120 -> 152
~ _xmlSchemaXPathProcessHistory : 2744 -> 2796
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.qGEmm8/Sources/libxml2/libxml2/relaxng.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.qGEmm8/Sources/libxml2/libxml2/schematron.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.qGEmm8/Sources/libxml2/libxml2/xmlreader.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.qGEmm8/Sources/libxml2/libxml2/xmlregexp.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.qGEmm8/Sources/libxml2/libxml2/xmlschemas.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.qGEmm8/Sources/libxml2/libxml2/xmlschemastypes.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.qGEmm8/Sources/libxml2/libxml2/xpath.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.qGEmm8/Sources/libxml2/libxml2/xpointer.c"
+ "calling xmlSchemaIDCRegisterMatchers()"
+ "negative `pos` at selector (`depth >= matcher->depth` invariant violated)"
+ "negative `pos` in field handler (`depth >= matcher->depth` invariant violated)"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.PbE6l6/Sources/libxml2/libxml2/relaxng.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.PbE6l6/Sources/libxml2/libxml2/schematron.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.PbE6l6/Sources/libxml2/libxml2/xmlreader.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.PbE6l6/Sources/libxml2/libxml2/xmlregexp.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.PbE6l6/Sources/libxml2/libxml2/xmlschemas.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.PbE6l6/Sources/libxml2/libxml2/xmlschemastypes.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.PbE6l6/Sources/libxml2/libxml2/xpath.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.PbE6l6/Sources/libxml2/libxml2/xpointer.c"
```
