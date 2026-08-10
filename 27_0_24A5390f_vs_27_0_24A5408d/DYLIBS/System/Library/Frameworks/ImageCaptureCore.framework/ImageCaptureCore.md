## ImageCaptureCore

> `/System/Library/Frameworks/ImageCaptureCore.framework/ImageCaptureCore`

### Sections with Same Size but Changed Content

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
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__DATA.__objc_ivar`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-2116.0.0.0.0
-  __TEXT.__text: 0x2cb9c
-  __TEXT.__objc_methlist: 0x29ec
+2118.0.0.0.0
+  __TEXT.__text: 0x2cb38
+  __TEXT.__objc_methlist: 0x29dc
   __TEXT.__const: 0x78
   __TEXT.__gcc_except_tab: 0x988
   __TEXT.__cstring: 0x2798
   __TEXT.__oslogstring: 0x3f
   __TEXT.__ustring: 0x478
-  __TEXT.__unwind_info: 0xa18
+  __TEXT.__unwind_info: 0xa10
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1d20
+  __DATA_CONST.__objc_selrefs: 0x1d18
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x60
   __DATA_CONST.__objc_arraydata: 0x58

   - /System/Library/PrivateFrameworks/TCC.framework/TCC
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1027
-  Symbols:   2333
+  Functions: 1026
+  Symbols:   2330
   CStrings:  521
 
Symbols:
+ GCC_except_table115
- -[ICCameraDevice deliveredObjectCount]
- GCC_except_table116
- _objc_msgSend$deliveredObjectCount
- _objc_msgSend$mediaFiles
Functions:
- -[ICCameraDevice deliveredObjectCount]
~ -[ICCameraDevice updateContentCatalogPercentCompleted] : 288 -> 324
~ -[ICCameraDevice filesOfType:] : 336 -> 344
~ -[ICCameraDevice containsRestrictedStorage] : 332 -> 340
~ -[ICCameraDevice addMediaFiles:] : 392 -> 368
~ -[ICCameraDevice removeItems:] : 672 -> 748
~ ___60-[ICCameraDevice requestCloseSessionWithOptions:completion:]_block_invoke_2 : 480 -> 464
~ -[ICCameraDevice removeFolder:] : 156 -> 136
```
