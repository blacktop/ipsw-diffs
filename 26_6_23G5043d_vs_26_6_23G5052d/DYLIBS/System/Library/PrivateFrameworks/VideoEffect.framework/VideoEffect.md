## VideoEffect

> `/System/Library/PrivateFrameworks/VideoEffect.framework/VideoEffect`

```diff

-  __TEXT.__text: 0x9eec
-  __TEXT.__auth_stubs: 0x7f0
+  __TEXT.__text: 0xa1a4
+  __TEXT.__auth_stubs: 0x810
   __TEXT.__objc_methlist: 0x894
   __TEXT.__const: 0x1b2
   __TEXT.__cstring: 0xccb

   __TEXT.__objc_methname: 0x1b73
   __TEXT.__objc_methtype: 0x42a
   __TEXT.__objc_stubs: 0x11e0
-  __DATA_CONST.__got: 0x2d8
+  __DATA_CONST.__got: 0x308
   __DATA_CONST.__const: 0x148
   __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_protolist: 0x18

   __DATA_CONST.__objc_selrefs: 0x5a0
   __DATA_CONST.__objc_superrefs: 0x68
   __DATA_CONST.__objc_arraydata: 0x68
-  __AUTH_CONST.__auth_got: 0x408
+  __AUTH_CONST.__auth_got: 0x418
   __AUTH_CONST.__cfstring: 0x6e0
   __AUTH_CONST.__objc_const: 0x3a70
-  __AUTH_CONST.__objc_intobj: 0x120
+  __AUTH_CONST.__objc_intobj: 0x138
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH.__objc_data: 0x410
   __DATA.__objc_ivar: 0x160

   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia
   - /System/Library/Frameworks/CoreVideo.framework/CoreVideo
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/IOSurface.framework/IOSurface
   - /System/Library/Frameworks/Metal.framework/Metal
   - /System/Library/PrivateFrameworks/DeepVideoProcessingCore.framework/DeepVideoProcessingCore
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 281
-  Symbols:   1223
+  Functions: 283
+  Symbols:   1235
   CStrings:  495
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__const : content changed
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH.__objc_data : content changed
~ __DATA.__data : content changed
Symbols:
+ _IOSurfaceCreate
+ _IOSurfaceGetBytesPerRow
+ _createPlanar16HalfIOSurface
+ _createTextureViaPlanar16HalfIOSurface
+ _kIOSurfaceAllocSize
+ _kIOSurfaceBytesPerElement
+ _kIOSurfaceBytesPerRow
+ _kIOSurfaceHeight
+ _kIOSurfacePixelFormat
+ _kIOSurfaceWidth

```
