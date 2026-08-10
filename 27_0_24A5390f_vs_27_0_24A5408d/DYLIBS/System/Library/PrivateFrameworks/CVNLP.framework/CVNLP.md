## CVNLP

> `/System/Library/PrivateFrameworks/CVNLP.framework/CVNLP`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__cstring`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__weak_got`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__weak_auth_got`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__AUTH.__thread_vars`
- `__DATA.__data`

```diff

-129.0.0.0.0
-  __TEXT.__text: 0xcb7a8
+130.0.0.0.0
+  __TEXT.__text: 0xcb888
   __TEXT.__objc_methlist: 0x19c4
   __TEXT.__const: 0x1e38
   __TEXT.__cstring: 0x6dda
-  __TEXT.__gcc_except_tab: 0xdea0
-  __TEXT.__oslogstring: 0x7ce
+  __TEXT.__gcc_except_tab: 0xdeb8
+  __TEXT.__oslogstring: 0x7f8
   __TEXT.__dlopen_cstrs: 0x86
   __TEXT.__unwind_info: 0x41c0
   __TEXT.__objc_stubs: 0x0

   - /usr/lib/libperfcheck.dylib
   Functions: 2684
   Symbols:   621
-  CStrings:  812
+  CStrings:  813
 
Functions:
~ _CVNLPLanguageModelCreate : 6600 -> 6824
CStrings:
+ "Failed to create CVNLP language model: %s"
```
