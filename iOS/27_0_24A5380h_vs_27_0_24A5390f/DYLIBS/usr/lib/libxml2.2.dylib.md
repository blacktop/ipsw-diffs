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
-  __TEXT.__text: 0xc6758
-  __TEXT.__cstring: 0x19aee
+39.10.3.0.0
+  __TEXT.__text: 0xc6844
+  __TEXT.__cstring: 0x19bae
   __TEXT.__const: 0x3890
   __TEXT.__oslogstring: 0xa2
-  __TEXT.__unwind_info: 0x1b98
+  __TEXT.__unwind_info: 0x1ba0
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x7b88
   __DATA_CONST.__got: 0x0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 2628
-  Symbols:   3098
-  CStrings:  3983
+  Functions: 2629
+  Symbols:   3099
+  CStrings:  3986
 
Symbols:
+ _xmlSchemaIDCRegisterMatchers
Functions:
~ _xmlAddChild : 504 -> 540
~ _xmlC14NProcessNodeList : 3856 -> 3868
~ _xmlSchemaValidateElem : 3544 -> 3188
+ _xmlSchemaIDCRegisterMatchers
~ _xmlSchemaVAttributesSimple : 120 -> 152
~ _xmlSchemaXPathProcessHistory : 2768 -> 2820
CStrings:
+ "calling xmlSchemaIDCRegisterMatchers()"
+ "negative `pos` at selector (`depth >= matcher->depth` invariant violated)"
+ "negative `pos` in field handler (`depth >= matcher->depth` invariant violated)"
```
