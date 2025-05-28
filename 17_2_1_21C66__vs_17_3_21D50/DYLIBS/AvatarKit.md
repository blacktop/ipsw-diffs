## AvatarKit

> `/System/Library/PrivateFrameworks/AvatarKit.framework/AvatarKit`

```diff

-342.208.0.0.0
-  __TEXT.__text: 0x6e090
+342.301.0.0.0
+  __TEXT.__text: 0x6dfb4
   __TEXT.__auth_stubs: 0xda0
-  __TEXT.__objc_methlist: 0x47a8
+  __TEXT.__objc_methlist: 0x47a0
   __TEXT.__const: 0x8d8
   __TEXT.__oslogstring: 0x23b8
-  __TEXT.__cstring: 0x19fad
-  __TEXT.__gcc_except_tab: 0xd34
+  __TEXT.__cstring: 0x19fbc
+  __TEXT.__gcc_except_tab: 0xd28
   __TEXT.__ustring: 0x52
-  __TEXT.__unwind_info: 0x1908
+  __TEXT.__unwind_info: 0x1900
   __TEXT.__objc_classname: 0x8cb
-  __TEXT.__objc_methname: 0xff6a
-  __TEXT.__objc_methtype: 0x25bd
-  __TEXT.__objc_stubs: 0xc7a0
+  __TEXT.__objc_methname: 0xff38
+  __TEXT.__objc_methtype: 0x25dc
+  __TEXT.__objc_stubs: 0xc740
   __DATA_CONST.__got: 0x4d0
   __DATA_CONST.__const: 0x2528
   __DATA_CONST.__objc_classlist: 0x248
   __DATA_CONST.__objc_catlist: 0xa0
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x9d70
-  __DATA_CONST.__objc_selrefs: 0x39d8
+  __DATA_CONST.__objc_const: 0x9d90
+  __DATA_CONST.__objc_selrefs: 0x39c0
   __DATA_CONST.__objc_arraydata: 0x55c00
-  __AUTH_CONST.__cfstring: 0x20680
+  __AUTH_CONST.__cfstring: 0x20660
   __AUTH_CONST.__objc_const: 0x21f8
-  __AUTH_CONST.__const: 0x880
+  __AUTH_CONST.__const: 0x8a0
   __AUTH_CONST.__objc_floatobj: 0x30
   __AUTH_CONST.__objc_intobj: 0x240
   __AUTH_CONST.__objc_arrayobj: 0x5310

   __DATA.__objc_protorefs: 0x8
   __DATA.__objc_classrefs: 0x558
   __DATA.__objc_superrefs: 0x198
-  __DATA.__objc_ivar: 0x994
-  __DATA.__data: 0xa58
-  __DATA.__bss: 0x500
+  __DATA.__objc_ivar: 0x998
+  __DATA.__data: 0xa48
+  __DATA.__bss: 0x510
   __DATA_DIRTY.__objc_data: 0x118
   __DATA_DIRTY.__bss: 0x10
   - /System/Library/Frameworks/ARKit.framework/ARKit

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2327
-  Symbols:   25630
-  CStrings:  7714
+  Functions: 2326
+  Symbols:   25627
+  CStrings:  7713
 
Symbols:
+ -[SCNRenderer(AVTSceneRenderer) avt_simdUnprojectPoint:]
+ -[SCNView(AVTSceneRenderer) avt_simdUnprojectPoint:]
+ GCC_except_table46
+ _OBJC_IVAR_$_AVTStickerGenerator._workQueue
+ ___38-[AVTStickerGenerator initWithAvatar:]_block_invoke
+ ___79-[AVTStickerGenerator stickerImageWithConfiguration:options:completionHandler:]_block_invoke.115
+ ___79-[AVTStickerGenerator stickerImageWithConfiguration:options:completionHandler:]_block_invoke_2.116
+ _initWithAvatar:.onceToken
+ _initWithAvatar:.sharedWorkQueue
+ _objc_msgSend$blackColor
- +[AVTStickerGenerator workQueue]
- -[SCNRenderer(AVTSceneRenderer) avt_simdPUnprojectPoint:]
- -[SCNView(AVTSceneRenderer) avt_simdPUnprojectPoint:]
- ___32+[AVTStickerGenerator workQueue]_block_invoke
- ___79-[AVTStickerGenerator stickerImageWithConfiguration:options:completionHandler:]_block_invoke.119
- ___79-[AVTStickerGenerator stickerImageWithConfiguration:options:completionHandler:]_block_invoke_2.120
- _objc_msgSend$cStringUsingEncoding:
- _objc_msgSend$rendererDelegate
- _objc_msgSend$setRendererDelegate:
- _objc_msgSend$workQueue
- _workQueue.onceToken
- _workQueue.workQueue
CStrings:
+ "\x04\x11"
+ "@\"NSObject<OS_dispatch_queue>\""
+ "_workQueue"
+ "avt_simdUnprojectPoint:"
+ "blackColor"
+ "com.apple.avatarkit.AVTStickerGenerator"
- "\x03\x11"
- "avt_simdPUnprojectPoint:"
- "cStringUsingEncoding:"
- "com.apple.avatarkit.%@%p"
- "rendererDelegate"
- "setRendererDelegate:"
- "workQueue"

```
