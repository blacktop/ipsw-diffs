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
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__DATA.__objc_ivar`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-2114.0.0.0.0
-  __TEXT.__text: 0x2cb38
-  __TEXT.__objc_methlist: 0x29c4
+2116.0.0.0.0
+  __TEXT.__text: 0x2cb9c
+  __TEXT.__objc_methlist: 0x29ec
   __TEXT.__const: 0x78
   __TEXT.__gcc_except_tab: 0x988
   __TEXT.__cstring: 0x2798
   __TEXT.__oslogstring: 0x3f
   __TEXT.__ustring: 0x478
-  __TEXT.__unwind_info: 0xa10
+  __TEXT.__unwind_info: 0xa18
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1d10
+  __DATA_CONST.__objc_selrefs: 0x1d20
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x60
   __DATA_CONST.__objc_arraydata: 0x58
   __DATA_CONST.__got: 0x228
   __AUTH_CONST.__const: 0x140
   __AUTH_CONST.__cfstring: 0x3c40
-  __AUTH_CONST.__objc_const: 0x3460
+  __AUTH_CONST.__objc_const: 0x3580
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__objc_arrayobj: 0x60

   - /System/Library/PrivateFrameworks/TCC.framework/TCC
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1026
-  Symbols:   2328
+  Functions: 1027
+  Symbols:   2333
   CStrings:  521
 
Symbols:
+ -[ICCameraDevice deliveredObjectCount]
+ GCC_except_table116
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_ICMediaItemProtocol
+ __OBJC_$_PROTOCOL_REFS_ICMediaItemProtocol
+ _objc_msgSend$deliveredObjectCount
+ _objc_msgSend$mediaFiles
- GCC_except_table115
Functions:
+ -[ICCameraDevice deliveredObjectCount]
~ -[ICCameraDevice updateContentCatalogPercentCompleted] : 324 -> 288
~ -[ICCameraDevice filesOfType:] : 344 -> 336
~ -[ICCameraDevice containsRestrictedStorage] : 340 -> 332
~ -[ICCameraDevice addMediaFiles:] : 368 -> 392
~ -[ICCameraDevice removeItems:] : 748 -> 672
~ ___60-[ICCameraDevice requestCloseSessionWithOptions:completion:]_block_invoke_2 : 464 -> 480
~ -[ICCameraDevice removeFolder:] : 136 -> 156
```
