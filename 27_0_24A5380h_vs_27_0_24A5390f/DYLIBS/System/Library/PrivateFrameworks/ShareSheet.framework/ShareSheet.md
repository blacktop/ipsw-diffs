## ShareSheet

> `/System/Library/PrivateFrameworks/ShareSheet.framework/ShareSheet`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-2124.10.2.2.2
-  __TEXT.__text: 0xc6e3c
-  __TEXT.__objc_methlist: 0x1130c
+2126.10.4.0.0
+  __TEXT.__text: 0xc7544
+  __TEXT.__objc_methlist: 0x11314
   __TEXT.__const: 0x620
-  __TEXT.__gcc_except_tab: 0x2044
-  __TEXT.__oslogstring: 0x7110
+  __TEXT.__gcc_except_tab: 0x202c
+  __TEXT.__oslogstring: 0x7195
   __TEXT.__cstring: 0x7128
   __TEXT.__dlopen_cstrs: 0xaaf
   __TEXT.__ustring: 0x104
-  __TEXT.__unwind_info: 0x3528
+  __TEXT.__unwind_info: 0x3530
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x3a8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8c10
+  __DATA_CONST.__objc_selrefs: 0x8c30
   __DATA_CONST.__objc_protorefs: 0x58
   __DATA_CONST.__objc_superrefs: 0x400
   __DATA_CONST.__objc_arraydata: 0x678

   - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 5894
-  Symbols:   13901
-  CStrings:  1611
+  Functions: 5897
+  Symbols:   13907
+  CStrings:  1613
 
Symbols:
+ -[UIMessageActivity _insertCompositionContentForText:]
+ GCC_except_table183
+ GCC_except_table186
+ GCC_except_table196
+ __UIActivityItemsContainMixedContent
+ _objc_msgSend$_insertCompositionContentForText:
+ _objc_msgSend$insertCompositionText:
+ _objc_msgSend$setSuppressesShelfStaging:
+ _objc_msgSend$supportsCompositionTextInsertion
- GCC_except_table182
- GCC_except_table185
- GCC_except_table194
CStrings:
+ "Disabled shelf staging because activity items contains mixed content."
+ "Preparing activityItems - canInterweaveMessageContent=%{BOOL}d"
```
