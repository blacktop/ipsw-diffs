## ImageCaptureDevices

> `/System/Library/PrivateFrameworks/ImageCaptureDevices.framework/ImageCaptureDevices`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_dictobj`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-2114.0.0.0.0
-  __TEXT.__text: 0x1a380
-  __TEXT.__objc_methlist: 0x1d3c
+2116.0.0.0.0
+  __TEXT.__text: 0x1a4d4
+  __TEXT.__objc_methlist: 0x1d64
   __TEXT.__const: 0xa0
   __TEXT.__gcc_except_tab: 0x5b4
   __TEXT.__cstring: 0x695a
   __TEXT.__oslogstring: 0x34
   __TEXT.__ustring: 0x1c
-  __TEXT.__unwind_info: 0x5d0
+  __TEXT.__unwind_info: 0x5d8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0x98
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1328
+  __DATA_CONST.__objc_selrefs: 0x1348
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x98
   __DATA_CONST.__objc_arraydata: 0x2880
   __DATA_CONST.__got: 0x188
   __AUTH_CONST.__const: 0x1a0
   __AUTH_CONST.__cfstring: 0x71c0
-  __AUTH_CONST.__objc_const: 0x2970
+  __AUTH_CONST.__objc_const: 0x29a0
   __AUTH_CONST.__objc_intobj: 0x6c0
   __AUTH_CONST.__objc_dictobj: 0x21c0
   __AUTH_CONST.__auth_got: 0x0
-  __DATA.__objc_ivar: 0x268
+  __DATA.__objc_ivar: 0x26c
   __DATA.__data: 0x2b8
   __DATA.__bss: 0x38
   __DATA.__common: 0x8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 667
-  Symbols:   1493
+  Functions: 670
+  Symbols:   1498
   CStrings:  957
 
Symbols:
+ -[ICOrderedMediaSet mediaItemWithIdentifier:]
+ -[ICOrderedMediaSet mediaItemsByIdentifier]
+ -[ICOrderedMediaSet setMediaItemsByIdentifier:]
+ _OBJC_IVAR_$_ICOrderedMediaSet._mediaItemsByIdentifier
+ _objc_msgSend$mediaItemIdentifier
Functions:
~ -[ICOrderedMediaSet initWithTypes:] : 372 -> 392
~ -[ICOrderedMediaSet addMediaItemToIndex:] : 344 -> 404
~ -[ICOrderedMediaSet removeMediaItemFromIndex:] : 156 -> 212
~ -[ICOrderedMediaSet removeAllItems] : 288 -> 296
+ -[ICOrderedMediaSet mediaItemWithIdentifier:]
+ -[ICOrderedMediaSet mediaItemsByIdentifier]
+ -[ICOrderedMediaSet .cxx_destruct]
```
