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
-  __TEXT.__text: 0xc6038
+39.10.3.0.0
+  __TEXT.__text: 0xc614c
   __TEXT.__auth_stubs: 0x760
-  __TEXT.__cstring: 0x19c1e
+  __TEXT.__cstring: 0x19cde
   __TEXT.__const: 0x3890
   __TEXT.__oslogstring: 0xa2
-  __TEXT.__unwind_info: 0x1ae8
+  __TEXT.__unwind_info: 0x1af0
   __DATA_CONST.__got: 0x58
   __DATA_CONST.__const: 0x7b88
   __AUTH_CONST.__auth_got: 0x3b0

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
~ _xmlC14NProcessNodeList : 3860 -> 3872
~ _xmlSchemaValidateElem : 3444 -> 3128
+ _xmlSchemaIDCRegisterMatchers
~ _xmlSchemaVAttributesSimple : 120 -> 152
~ _xmlSchemaXPathProcessHistory : 2748 -> 2800
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.snlgNN/Sources/libxml2/libxml2/relaxng.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.snlgNN/Sources/libxml2/libxml2/schematron.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.snlgNN/Sources/libxml2/libxml2/xmlreader.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.snlgNN/Sources/libxml2/libxml2/xmlregexp.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.snlgNN/Sources/libxml2/libxml2/xmlschemas.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.snlgNN/Sources/libxml2/libxml2/xmlschemastypes.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.snlgNN/Sources/libxml2/libxml2/xpath.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.snlgNN/Sources/libxml2/libxml2/xpointer.c"
+ "calling xmlSchemaIDCRegisterMatchers()"
+ "negative `pos` at selector (`depth >= matcher->depth` invariant violated)"
+ "negative `pos` in field handler (`depth >= matcher->depth` invariant violated)"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.vZJUTz/Sources/libxml2/libxml2/relaxng.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.vZJUTz/Sources/libxml2/libxml2/schematron.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.vZJUTz/Sources/libxml2/libxml2/xmlreader.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.vZJUTz/Sources/libxml2/libxml2/xmlregexp.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.vZJUTz/Sources/libxml2/libxml2/xmlschemas.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.vZJUTz/Sources/libxml2/libxml2/xmlschemastypes.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.vZJUTz/Sources/libxml2/libxml2/xpath.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.vZJUTz/Sources/libxml2/libxml2/xpointer.c"
```
