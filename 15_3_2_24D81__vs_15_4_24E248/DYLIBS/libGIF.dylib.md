## libGIF.dylib

> `/System/Library/Frameworks/ImageIO.framework/Versions/A/Resources/libGIF.dylib`

```diff

-2661.3.5.0.0
-  __TEXT.__text: 0x4c2c
+2661.4.9.0.0
+  __TEXT.__text: 0x4bb0
   __TEXT.__auth_stubs: 0x130
   __TEXT.__cstring: 0x2b9
   __TEXT.__const: 0x43
-  __TEXT.__unwind_info: 0x158
+  __TEXT.__unwind_info: 0x150
   __DATA_CONST.__got: 0x10
   __AUTH_CONST.__auth_got: 0x98
   __DATA.__bss: 0x4
   - /usr/lib/libSystem.B.dylib
-  UUID: CF2F5003-DB41-3D7C-9CAE-878F0B76FCDF
-  Functions: 71
-  Symbols:   94
+  UUID: F4044D95-F8CB-3284-AED4-D4D6F52D5D56
+  Functions: 69
+  Symbols:   93
   CStrings:  25
 
Symbols:
- FreeLastSavedImage.cold.1
Functions:
~ __cg_DGifOpenFileHandle : 408 -> 468
~ __cg_DGifOpen : 440 -> 500
~ __cg_DGifGetImageDesc : 796 -> 724
~ _DGifSetupDecompress : 240 -> 244
~ _DGifDecompressLine : 1460 -> 1452
~ _DGifSavedExtensionToGCB : 152 -> 120
~ __cg_DGifCloseFile : 236 -> 248
~ _DGifDecompressInput : 500 -> 488
~ __cg_DGifSlurp : 668 -> 632
~ __cg_EGifOpenFileHandle : 248 -> 304
~ __cg_EGifOpen : 244 -> 300
~ _EGifGetGifVersion : 264 -> 232
~ __cg_EGifPutScreenDesc : 556 -> 560
~ _InternalWrite : 72 -> 64
~ __cg_EGifPutPixel : 152 -> 156
~ _EGifGCBToExtension : 84 -> 96
~ _EGifGCBToSavedExtension : 388 -> 372
~ __cg_EGifSpew : 548 -> 524
~ _EGifCompressOutput : 364 -> 340
~ _GifErrorString : 312 -> 380
- sub_1905e2350
~ __cg_GifMakeMapObject : 304 -> 300
~ _GifUnionColorMap : 808 -> 820
~ _GifAddExtensionBlock : 360 -> 328
~ _FreeLastSavedImage : 44 -> 128
~ _GifMakeSavedImage : 228 -> 236
~ __cg_GifQuantizeBuffer : 2508 -> 2400

```
