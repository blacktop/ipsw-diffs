## CoreMediaIO

> `/System/Library/Frameworks/CoreMediaIO.framework/CoreMediaIO`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__cstring`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__got`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_superrefs`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

 5617.100.5.0.0
-  __TEXT.__text: 0x422f0
+  __TEXT.__text: 0x424bc
   __TEXT.__auth_stubs: 0xe30
   __TEXT.__objc_methlist: 0x204c
   __TEXT.__const: 0xe8
   __TEXT.__gcc_except_tab: 0x16b0
   __TEXT.__cstring: 0x877b
-  __TEXT.__oslogstring: 0x4266
+  __TEXT.__oslogstring: 0x4280
   __TEXT.__dlopen_cstrs: 0xb8
   __TEXT.__unwind_info: 0xcb0
   __TEXT.__objc_classname: 0x3bc

   - /usr/lib/libobjc.A.dylib
   Functions: 1380
   Symbols:   2270
-  CStrings:  1945
+  CStrings:  1946
 
Functions:
~ -[CMIOExtensionProviderHostContext setStreamPropertyValuesWithStreamID:propertyValues:reply:] : 748 -> 1208
CStrings:
+ "%s:%d:%s SetProperty - %@"
```
