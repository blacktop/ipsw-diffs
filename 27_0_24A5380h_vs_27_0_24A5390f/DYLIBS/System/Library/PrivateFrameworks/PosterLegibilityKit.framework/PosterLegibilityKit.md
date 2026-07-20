## PosterLegibilityKit

> `/System/Library/PrivateFrameworks/PosterLegibilityKit.framework/PosterLegibilityKit`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__DATA_DIRTY.__objc_data`

```diff

-347.102.0.0.0
-  __TEXT.__text: 0x232ac
-  __TEXT.__objc_methlist: 0x25d8
+350.1.100.0.0
+  __TEXT.__text: 0x236e0
+  __TEXT.__objc_methlist: 0x25f0
   __TEXT.__const: 0x340
-  __TEXT.__cstring: 0x12ab
+  __TEXT.__cstring: 0x12ea
   __TEXT.__oslogstring: 0x11f5
-  __TEXT.__gcc_except_tab: 0x6dc
-  __TEXT.__unwind_info: 0xbb0
+  __TEXT.__gcc_except_tab: 0x720
+  __TEXT.__unwind_info: 0xbc8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x968
+  __DATA_CONST.__const: 0x990
   __DATA_CONST.__objc_classlist: 0x128
   __DATA_CONST.__objc_catlist: 0x60
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x18d0
+  __DATA_CONST.__objc_selrefs: 0x18e0
   __DATA_CONST.__objc_superrefs: 0x110
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__got: 0x4a0
-  __AUTH_CONST.__const: 0x320
+  __AUTH_CONST.__const: 0x340
   __AUTH_CONST.__cfstring: 0x16a0
   __AUTH_CONST.__objc_const: 0x6398
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH_CONST.__auth_got: 0x7f8
+  __AUTH_CONST.__auth_got: 0x808
   __DATA.__objc_ivar: 0x334
-  __DATA.__data: 0x600
-  __DATA.__bss: 0x138
+  __DATA.__data: 0x608
+  __DATA.__bss: 0x148
   __DATA_DIRTY.__objc_data: 0xb90
   __DATA_DIRTY.__bss: 0xb0
   - /System/Library/Frameworks/Accelerate.framework/Accelerate

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 907
-  Symbols:   2611
-  CStrings:  300
+  Functions: 914
+  Symbols:   2624
+  CStrings:  302
 
Symbols:
+ +[PLKImageRenderer plk_isImagePoolBacked:]
+ +[PLKImageRenderer plk_poolBackedImageFromImage:]
+ GCC_except_table26
+ ___69-[PLKCachedImageGenerator initWithCache:keyGenerator:imageGenerator:]_block_invoke
+ _____plk_poolReleaseQueue_block_invoke
+ _____plk_releasePoolDataOffMain_block_invoke
+ ___block_descriptor_40_e8_32bs_e20_"UIImage"24?0816ls32l8
+ ___plk_poolReleaseQueue.onceToken
+ ___plk_poolReleaseQueue.queue
+ ___plk_releasePoolDataOffMain
+ _dispatch_async
+ _dispatch_queue_attr_make_with_qos_class
+ _dispatch_queue_create
+ _kPLKImagePoolBackedKey
+ _objc_msgSend$plk_isImagePoolBacked:
+ _objc_msgSend$plk_poolBackedImageFromImage:
- GCC_except_table13
- GCC_except_table25
- _CGDataProviderCreateWithCFData
CStrings:
+ "@\"UIImage\"24@?0@8@16"
+ "com.apple.PosterLegibilityKit.poolRelease"
```
