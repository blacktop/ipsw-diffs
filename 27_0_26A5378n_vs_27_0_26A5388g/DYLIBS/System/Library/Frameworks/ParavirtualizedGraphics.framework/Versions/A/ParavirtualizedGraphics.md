## ParavirtualizedGraphics

> `/System/Library/Frameworks/ParavirtualizedGraphics.framework/Versions/A/ParavirtualizedGraphics`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH.__objc_data`
- `__DATA.__data`

```diff

-71.0.8.0.0
-  __TEXT.__text: 0x4cd20
+71.0.12.0.0
+  __TEXT.__text: 0x4cdb0
   __TEXT.__objc_methlist: 0x2df0
   __TEXT.__const: 0x3551
   __TEXT.__gcc_except_tab: 0x3a84
   __TEXT.__cstring: 0x4fe4
-  __TEXT.__oslogstring: 0x279e
+  __TEXT.__oslogstring: 0x27fc
   __TEXT.__unwind_info: 0x17e0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1618
-  Symbols:   3192
-  CStrings:  798
+  Functions: 1617
+  Symbols:   3191
+  CStrings:  799
 
Symbols:
+ __ZN5PGPtrIP39PGResourceManagerDeserializationContextED1Ev
- _OUTLINED_FUNCTION_10
- __ZN5PGPtrIPU36objcproto25MTLDeserializationContext11objc_objectED1Ev
CStrings:
+ "Mapping id(%u) clientAddressOffset out of range (0x%x >= PAGE_SIZE)"
+ "Mapping id(%u) integer overflow calculating page count (surfaceSize=0x%llx, clientAddressOffset=0x%x)"
- "Mapping id(%u) integer overflow calculating page count (surfaceSize=0x%llx)"
```
