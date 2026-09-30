## NanoUniverse

> `/System/Library/PrivateFrameworks/NanoUniverse.framework/NanoUniverse`

```diff

 42.0.0.0.0
-  __TEXT.__text: 0x415c0
+  __TEXT.__text: 0x415e4
   __TEXT.__objc_methlist: 0x2434
   __TEXT.__const: 0x1eb74
   __TEXT.__cstring: 0x1b5e

   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__objc_doubleobj: 0x40
-  __AUTH_CONST.__auth_got: 0xbf0
+  __AUTH_CONST.__auth_got: 0xbf8
   __AUTH.__objc_data: 0x280
   __AUTH.__data: 0x118
   __DATA.__objc_ivar: 0x410

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 1462
-  Symbols:   2555
+  Symbols:   2556
   CStrings:  380
 
Symbols:
+ _objc_release_x10
Functions:
~ -[NUNICalliopeRenderer _renderOffscreenSceneWithScene:spheroids:viewport:commandBuffer:frameBufferIndex:drawableTexture:] : 2432 -> 2440
~ -[NUNICalliopeRenderer _setupBloomChainWithViewport:bloomTexture:] : 724 -> 716
~ -[NUNICalliopeRenderer _computeBloomChainTextures:] : 552 -> 556
~ -[NUNICalliopeRenderer spheroidAtPoint:scene:viewport:] : 824 -> 832
~ -[NUNICalliopeResourceManager patchTextureGroupForSpheroid:index:suffix:] : 608 -> 612
~ -[NUNIClassicGeometry addVertices:count:] : 120 -> 124
~ -[NUNIClassicRenderer renderWithScene:viewport:commandBuffer:passDescriptor:] : 960 -> 968
~ -[NUNIClassicRenderer renderOffscreenWithScene:viewport:commandBuffer:] : 824 -> 832
~ -[NUNIAegirResourceManager setPipelineConstants:] : 932 -> 924
~ sub_292a4cb10 -> sub_2937b1b2c : 3504 -> 3508
~ sub_292a4e278 -> sub_2937b3298 : 2064 -> 2068
```
