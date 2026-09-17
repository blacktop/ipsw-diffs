## PencilKit

> `/System/Library/Frameworks/PencilKit.framework/Versions/A/PencilKit`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`

```diff

-616.0.0.0.0
-  __TEXT.__text: 0x158bb4
+621.0.0.0.0
+  __TEXT.__text: 0x158bf8
   __TEXT.__objc_methlist: 0xd690
   __TEXT.__const: 0x59b8
   __TEXT.__cstring: 0x44f0

   __DATA_CONST.__got: 0xd78
   __AUTH_CONST.__const: 0x7490
   __AUTH_CONST.__cfstring: 0x3fe0
-  __AUTH_CONST.__objc_const: 0x167d0
+  __AUTH_CONST.__objc_const: 0x167f0
   __AUTH_CONST.__weak_auth_got: 0x30
   __AUTH_CONST.__objc_intobj: 0x2a0
   __AUTH_CONST.__objc_doubleobj: 0x70
   __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH_CONST.__objc_dictobj: 0x140
-  __AUTH_CONST.__auth_got: 0x12d8
+  __AUTH_CONST.__auth_got: 0x12e0
   __AUTH.__objc_data: 0x3f28
   __AUTH.__data: 0x570
-  __DATA.__objc_ivar: 0x10ec
+  __DATA.__objc_ivar: 0x10f0
   __DATA.__data: 0x1600
   __DATA.__common: 0xc8
   __DATA_DIRTY.__objc_ivar: 0x170

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 8306
-  Symbols:   17986
+  Symbols:   17988
   CStrings:  1059
 
Symbols:
+ OBJC_IVAR_$_PKMetalRendererController._updateCycleRendererReadySemaphore
+ _swift_stdlib_random
Functions:
~ -[PKMetalRendererController initWithPixelSize:actualSize:pixelFormat:sixChannelBlendingMode:wantsExtendedDynamicRangeContent:metalConfig:] : 920 -> 924
~ -[PKMetalRendererController setStrokeTransform:] : 148 -> 152
~ -[PKMetalRendererController setPaperTransform:] : 148 -> 152
~ ___45-[PKMetalRendererController setCanvasOffset:]_block_invoke : 72 -> 76
~ -[PKMetalRendererController strokeTransform] : 20 -> 24
~ -[PKMetalRendererController paperTransform] : 20 -> 24
~ -[PKMetalRendererController .cxx_destruct] : 248 -> 260
~ _$s9PencilKit16LiveStrokeCanvasC12drawingBegan10inputPoint10forPreviewyAA05InputI0V_SbtF : 2880 -> 2912
CStrings:
+ "\xf0\xf0\xf0\xf0Q\x92"
- "\xf0\xf0\xf0\xf0A\x92"
```
