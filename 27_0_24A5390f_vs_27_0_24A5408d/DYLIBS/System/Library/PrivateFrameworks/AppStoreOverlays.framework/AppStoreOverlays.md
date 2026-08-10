## AppStoreOverlays

> `/System/Library/PrivateFrameworks/AppStoreOverlays.framework/AppStoreOverlays`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-27.0.45.0.0
-  __TEXT.__text: 0x5da8
+27.0.46.2.1
+  __TEXT.__text: 0x5db4
   __TEXT.__objc_methlist: 0xb8c
   __TEXT.__const: 0xb0
   __TEXT.__cstring: 0x650

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x798
+  __DATA_CONST.__objc_selrefs: 0x7a0
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x50
   __DATA_CONST.__got: 0x118

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 213
-  Symbols:   722
+  Symbols:   723
   CStrings:  96
 
Symbols:
+ _objc_msgSend$setSizesWindowToScene:
Functions:
~ -[ASOOverlayViewController initWithNibName:bundle:] : 224 -> 236
```
