## Pegasus

> `/System/Library/PrivateFrameworks/Pegasus.framework/Pegasus`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`

```diff

-310.0.0.0.0
-  __TEXT.__text: 0x4404c
-  __TEXT.__objc_methlist: 0x4674
+310.100.0.0.0
+  __TEXT.__text: 0x44284
+  __TEXT.__objc_methlist: 0x469c
   __TEXT.__const: 0x232
   __TEXT.__cstring: 0x47de
   __TEXT.__oslogstring: 0x1acc

   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1c60
+  __DATA_CONST.__const: 0x1c88
   __DATA_CONST.__objc_classlist: 0x1b8
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0xc8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2d30
+  __DATA_CONST.__objc_selrefs: 0x2d48
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x1a0
   __DATA_CONST.__objc_arraydata: 0x70
   __DATA_CONST.__got: 0x488
   __AUTH_CONST.__const: 0x400
   __AUTH_CONST.__cfstring: 0x2f40
-  __AUTH_CONST.__objc_const: 0xada0
+  __AUTH_CONST.__objc_const: 0xadd0
   __AUTH_CONST.__objc_intobj: 0x318
   __AUTH_CONST.__objc_doubleobj: 0x40
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__auth_got: 0x530
   __AUTH.__objc_data: 0xcd0
-  __DATA.__objc_ivar: 0x5e4
+  __DATA.__objc_ivar: 0x5e8
   __DATA.__data: 0x990
   __DATA.__bss: 0xd8
   __DATA_DIRTY.__objc_data: 0x460

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1764
-  Symbols:   4365
+  Functions: 1768
+  Symbols:   4373
   CStrings:  666
 
Symbols:
+ -[PGButtonGroupView _shouldHitTest]
+ -[PGPictureInPictureViewController hostedContentSizeOverride]
+ -[PGPictureInPictureViewController setHostedContentSizeOverride:]
+ GCC_except_table5
+ _OBJC_IVAR_$_PGPictureInPictureViewController._hostedContentSizeOverride
+ ___58-[PGPictureInPictureViewController viewWillLayoutSubviews]_block_invoke
+ ___block_descriptor_88_e8_32s_e5_v8?0ls32l8
+ _objc_msgSend$presentationLayer
```
