## ImageCaptureCore

> `/System/Library/Frameworks/ImageCaptureCore.framework/Versions/A/ImageCaptureCore`

### Sections with Same Size but Changed Content

- `__TEXT.__gcc_except_tab`
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
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH.__objc_data`
- `__DATA.__objc_ivar`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-2114.0.0.0.0
-  __TEXT.__text: 0x53008
-  __TEXT.__objc_methlist: 0x4acc
+2116.0.0.0.0
+  __TEXT.__text: 0x53078
+  __TEXT.__objc_methlist: 0x4af4
   __TEXT.__cstring: 0x6389
   __TEXT.__const: 0x1e4
   __TEXT.__oslogstring: 0x3f
   __TEXT.__ustring: 0x480
   __TEXT.__gcc_except_tab: 0xbe8
-  __TEXT.__unwind_info: 0x1018
+  __TEXT.__unwind_info: 0x1020
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2bc8
+  __DATA_CONST.__objc_selrefs: 0x2bd8
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0xf0
   __DATA_CONST.__objc_arraydata: 0x378
   __DATA_CONST.__got: 0x388
   __AUTH_CONST.__const: 0x1088
   __AUTH_CONST.__cfstring: 0x9280
-  __AUTH_CONST.__objc_const: 0x6a08
+  __AUTH_CONST.__objc_const: 0x6b28
   __AUTH_CONST.__objc_intobj: 0x210
   __AUTH_CONST.__objc_dictobj: 0x280
   __AUTH_CONST.__objc_arrayobj: 0x108

   - /System/Library/PrivateFrameworks/TCC.framework/Versions/A/TCC
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1817
-  Symbols:   3971
+  Functions: 1818
+  Symbols:   3976
   CStrings:  1217
 
Symbols:
+ -[ICCameraDevice deliveredObjectCount]
+ GCC_except_table125
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_ICMediaItemProtocol
+ __OBJC_$_PROTOCOL_REFS_ICMediaItemProtocol
+ _objc_msgSend$deliveredObjectCount
+ _objc_msgSend$mediaFiles
- GCC_except_table124
Functions:
+ -[ICCameraDevice deliveredObjectCount]
~ -[ICCameraDevice updateContentCatalogPercentCompleted] : 324 -> 288
~ -[ICCameraDevice filesOfType:] : 360 -> 352
~ -[ICCameraDevice containsRestrictedStorage] : 352 -> 344
~ -[ICCameraDevice addMediaFiles:] : 388 -> 412
~ -[ICCameraDevice removeItems:] : 784 -> 708
~ ___60-[ICCameraDevice requestCloseSessionWithOptions:completion:]_block_invoke_2 : 468 -> 484
~ -[ICCameraDevice removeFolder:] : 148 -> 168
```
