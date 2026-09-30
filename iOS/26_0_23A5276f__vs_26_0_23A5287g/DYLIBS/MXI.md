## MXI

> `/System/Library/PrivateFrameworks/MXI.framework/MXI`

```diff

-29.0.15.0.2
-  __TEXT.__text: 0x3cb58
+29.0.18.0.1
+  __TEXT.__text: 0x40264
   __TEXT.__auth_stubs: 0x8d0
-  __TEXT.__objc_methlist: 0xe48
-  __TEXT.__const: 0x9d30
-  __TEXT.__gcc_except_tab: 0x53c8
-  __TEXT.__cstring: 0x33b4
-  __TEXT.__oslogstring: 0x169e
-  __TEXT.__unwind_info: 0xbd8
+  __TEXT.__objc_methlist: 0xe68
+  __TEXT.__const: 0x9d40
+  __TEXT.__gcc_except_tab: 0x5d60
+  __TEXT.__cstring: 0x397c
+  __TEXT.__oslogstring: 0x2b58
+  __TEXT.__unwind_info: 0xc00
   __TEXT.__objc_classname: 0x16c
-  __TEXT.__objc_methname: 0x3b22
-  __TEXT.__objc_methtype: 0x9a0
-  __TEXT.__objc_stubs: 0x3460
-  __DATA_CONST.__got: 0x320
-  __DATA_CONST.__const: 0x5d0
+  __TEXT.__objc_methname: 0x3ce3
+  __TEXT.__objc_methtype: 0x9af
+  __TEXT.__objc_stubs: 0x3580
+  __DATA_CONST.__got: 0x338
+  __DATA_CONST.__const: 0x5d8
   __DATA_CONST.__objc_classlist: 0x88
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xef0
+  __DATA_CONST.__objc_selrefs: 0xf38
   __DATA_CONST.__objc_superrefs: 0x68
   __AUTH_CONST.__auth_got: 0x478
   __AUTH_CONST.__const: 0x3c8
-  __AUTH_CONST.__cfstring: 0x3000
-  __AUTH_CONST.__objc_const: 0x1e08
+  __AUTH_CONST.__cfstring: 0x3420
+  __AUTH_CONST.__objc_const: 0x1e88
   __AUTH_CONST.__objc_intobj: 0x2a0
   __AUTH.__objc_data: 0x550
-  __DATA.__objc_ivar: 0x1cc
+  __DATA.__objc_ivar: 0x1dc
   __DATA.__data: 0x128
   __DATA.__bss: 0x4188
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 11EB14C3-0F7B-30D6-8D48-76AB8E3AE50C
-  Functions: 719
-  Symbols:   445
-  CStrings:  1812
+  UUID: 7353533B-4779-3C70-843B-A08F5516A798
+  Functions: 726
+  Symbols:   450
+  CStrings:  1977
 
Symbols:
+ _MXISceneBuilderConfigurationIncludeBackingPlane
+ _OBJC_CLASS_$_MPSImageGaussianBlur
+ __Z8WriteKTXPN5image6WriterEP7NSArrayIPU21objcproto10MTLTexture11objc_objectE14MTLTextureType
+ __ZNK5tiled9Processor8GetAtlasEPU15__autoreleasingPU21objcproto10MTLTexture11objc_objectPjbbfjPU15__autoreleasingP7NSError
+ __ZNK5tiled9Processor8GetAtlasERNSt3__16vectorIU8__strongPU21objcproto10MTLTexture11objc_objectNS1_9allocatorIS5_EEEEbbfjPU15__autoreleasingP7NSError
+ __ZNSt13runtime_errorC1EPKc
+ __ZNSt13runtime_errorD1Ev
+ __ZTISt13runtime_error
- __ZNK5tiled9Processor8GetAtlasEPjbbfjPU15__autoreleasingP7NSError
- __ZNK5tiled9Processor8GetAtlasEbbfjPU15__autoreleasingP7NSError
- _printf
CStrings:
+ "(_tileSize & (_tileSize - 1)) == 0"
+ "-[MXISceneBuilder getLayerRange:]"
+ "-[MXISceneBuilder getLayerViewMatrix:]"
+ "Could not add layer (%ld), face (%ld)"
+ "Could not add shader graph"
+ "Could not capture color texture"
+ "Could not capture depth texture"
+ "Could not capture normal texture"
+ "Could not compress to ASTC"
+ "Could not create face slice indices property"
+ "Could not create face vertex indices property"
+ "Could not create faces property"
+ "Could not create mesh node"
+ "Could not create node for RealityKitComponent"
+ "Could not create points property"
+ "Could not create primvars property"
+ "Could not create sphere invert normal node"
+ "Could not create sphere material node"
+ "Could not create sphere node"
+ "Could not create sphere normal node"
+ "Could not create subdivision scheme property"
+ "Could not get inputs file property"
+ "Could not get resource from path: %@"
+ "Could not get texture 2D array from path: %@"
+ "Could not read ktx"
+ "Could not write ktx: %@"
+ "MXISceneBuilderBase.mm"
+ "Mismatched max threads per threadgroup"
+ "USDZ face indices is not a multiple of 3"
+ "USDZ has no face slice indices property"
+ "USDZ has no face vertex indices property"
+ "USDZ has no points property"
+ "USDZ has no primvars uv property"
+ "USDZ points and uv mismatched sizes"
+ "Unable to open usdz reader for file: %@"
+ "Unexpected thread execution width"
+ "[Image/ImageASTC.mm:157] Codec config init failed: %s\n"
+ "[Image/ImageASTC.mm:164] Codec context alloc failed: %s\n"
+ "[Image/ImageASTC.mm:193] ASTC encode failed"
+ "[Image/ImageASTC.mm:202] Codec compress failed: %s\n"
+ "[Image/ImageASTC.mm:281] [ImageASTC] failed initializing compute pipeline: %s"
+ "[Image/ImageASTC.mm:385] Unexpected astc size"
+ "[Image/ImageASTC.mm:481] Unexpected astc size"
+ "[Image/ImageASTC.mm:543] Failed creating ASTCEncoder"
+ "[Image/ImageASTC.mm:583] [ImageASTC] command buffer failed with error: %s"
+ "[Image/ImageASTC.mm:625] Failed creating ASTCEncoder"
+ "[Image/ImageASTC.mm:669] [ImageASTC] command buffer failed with error: %s"
+ "[Image/ImageASTC.mm:706] Failed creating ASTCEncoder"
+ "[Image/ImageASTC.mm:751] [ImageASTC] command buffer failed with error: %s"
+ "[Image/ImageASTC.mm:786] Failed creating ASTCEncoder"
+ "[Image/ImageASTC.mm:806] [ImageASTC] command buffer failed with error: %s"
+ "[Image/ImageKTX.mm:242] Invalid format reading ktx"
+ "[Image/ImageKTX.mm:344] Texture array with 0 slices"
+ "[Image/ImageKTX.mm:351] Invalid texture pixel format writing ktx"
+ "[MXI.framework/MXIRenderer.mm:173] [MXI] scene.colorTextures.count (%d) > ATLAS_SLICES_CAPACITY (%d)"
+ "[MXI.framework/MXIScene.mm:1021] "
+ "[MXI.framework/MXIScene.mm:186] Unable to open usdz reader for file: %@"
+ "[MXI.framework/MXIScene.mm:192] %@"
+ "[MXI.framework/MXIScene.mm:200] %@"
+ "[MXI.framework/MXIScene.mm:820] %@"
+ "[MXI.framework/MXIScene.mm:847] %@"
+ "[MXI.framework/MXIScene.mm:867] %@"
+ "[MXI.framework/MXIScene.mm:878] %@"
+ "[MXI.framework/MXIScene.mm:985] %@"
+ "[MXI.framework/MXISceneBuilderBase.mm:158] getLayerRange should not be used if layer depths was overridden"
+ "[MXI.framework/MXISceneBuilderBase.mm:166] getLayerViewMatrix should not be used if layer depths was overridden"
+ "[MXI.framework/MXISceneBuilderBase.mm:230] Cannot compress MXIScene: scene already compressed"
+ "[MXI.framework/MXISceneBuilderBase.mm:342] Could not capture color texture"
+ "[MXI.framework/MXISceneBuilderBase.mm:349] Could not capture depth texture"
+ "[MXI.framework/MXISceneBuilderBase.mm:377] Could not capture color texture"
+ "[MXI.framework/MXISceneBuilderBase.mm:384] Could not capture depth texture"
+ "[MXI.framework/MXISceneBuilderBase.mm:571] Could not capture color texture"
+ "[MXI.framework/MXISceneBuilderBase.mm:576] Could not capture normal texture"
+ "[MXI.framework/MXISceneBuilderTiled.mm:102] Cannot recognize ASTC quality option %@"
+ "[MXI.framework/MXISceneBuilderTiled.mm:158] Failed on creating TiledProcessor"
+ "[MXI.framework/MXISceneBuilderTiled.mm:206] Could not add layer (%ld), face (%ld)"
+ "[MXI.framework/MXISceneBuilderTiled.mm:247] Could not create the atlas"
+ "[MXI.framework/MXISceneBuilderTiled.mm:253] Could not create the atlas"
+ "[MXI.framework/MXISceneBuilderTiled.mm:61] TiledProcessor cannot move forward with nil MTLDevice"
+ "[MXI.framework/MXISceneUSDZReader.mm:127] No mesh node"
+ "[MXI.framework/MXISceneUSDZReader.mm:132] USDZ has no points property"
+ "[MXI.framework/MXISceneUSDZReader.mm:138] USDZ has no primvars uv property"
+ "[MXI.framework/MXISceneUSDZReader.mm:144] USDZ has no face vertex indices property"
+ "[MXI.framework/MXISceneUSDZReader.mm:150] USDZ has no face slice indices property"
+ "[MXI.framework/MXISceneUSDZReader.mm:154] USDZ points and uv mismatched sizes"
+ "[MXI.framework/MXISceneUSDZReader.mm:157] USDZ face indices is not a multiple of 3"
+ "[MXI.framework/MXISceneUSDZReader.mm:184] Could not get texture 2D array from path: %@"
+ "[MXI.framework/MXISceneUSDZReader.mm:190] Could not get inputs file property"
+ "[MXI.framework/MXISceneUSDZReader.mm:196] Could not get resource from path: %@"
+ "[MXI.framework/MXISceneUSDZReader.mm:207] Could not read ktx"
+ "[MXI.framework/MXISceneUSDZWriter.mm:1108] Could not write ktx: %@"
+ "[MXI.framework/MXISceneUSDZWriter.mm:1119] Could not write ktx: %@"
+ "[MXI.framework/MXISceneUSDZWriter.mm:1132] Could not write ktx: %@"
+ "[MXI.framework/MXISceneUSDZWriter.mm:1139] Could not add shader graph"
+ "[MXI.framework/MXISceneUSDZWriter.mm:1170] Could not write ktx: %@"
+ "[MXI.framework/MXISceneUSDZWriter.mm:1175] Could not add shader graph"
+ "[MXI.framework/MXISceneUSDZWriter.mm:130] Could not create sphere material node"
+ "[MXI.framework/MXISceneUSDZWriter.mm:136] Could not create sphere normal node"
+ "[MXI.framework/MXISceneUSDZWriter.mm:143] Could not create sphere invert normal node"
+ "[MXI.framework/MXISceneUSDZWriter.mm:171] Could not create sphere node"
+ "[MXI.framework/MXISceneUSDZWriter.mm:184] Could not create node for RealityKitComponent"
+ "[MXI.framework/MXISceneUSDZWriter.mm:192] Could not create node for RealityKitComponent"
+ "[MXI.framework/MXISceneUSDZWriter.mm:208] Could not create mesh node"
+ "[MXI.framework/MXISceneUSDZWriter.mm:216] Could not create subdivision scheme property"
+ "[MXI.framework/MXISceneUSDZWriter.mm:223] Could not create points property"
+ "[MXI.framework/MXISceneUSDZWriter.mm:261] Could not create primvars property"
+ "[MXI.framework/MXISceneUSDZWriter.mm:269] Could not create primvars property"
+ "[MXI.framework/MXISceneUSDZWriter.mm:277] Could not create primvars property"
+ "[MXI.framework/MXISceneUSDZWriter.mm:286] Could not create faces property"
+ "[MXI.framework/MXISceneUSDZWriter.mm:294] Could not create face vertex indices property"
+ "[MXI.framework/MXISceneUSDZWriter.mm:301] Could not create face slice indices property"
+ "[MXI.framework] [MXIScene] scene created with %lu slices, resolution %u x %u"
+ "[MXI.framework] [MXIScene] wrote to URL %@ with options %@"
+ "[Tiled/TiledProcessor.mm:1238] Could not compress to ASTC"
+ "[Tiled/TiledProcessor.mm:1386] Could not compress to ASTC"
+ "[Tiled/TiledProcessor.mm:1399] Could not compress to ASTC"
+ "[Tiled/TiledProcessor.mm:352] [TiledProcessor] WARNING: nil MTLBinaryArchive for mxi_archive, error %@"
+ "[Tiled/TiledProcessor.mm:393] Packing in compressed atlas is not supported, continuing without it."
+ "[Tiled/TiledProcessor.mm:464] Unexpected thread execution width"
+ "[Tiled/TiledProcessor.mm:467] Mismatched max threads per threadgroup"
+ "[Tiled/TiledProcessor.mm:555] Number of atlas slices exceeds MAX_FIXED_ATLAS_SLICES."
+ "[Tiled/TiledProcessor.mm:584] Failed to allocate atlas."
+ "[Tiled/TiledProcessor.mm:600] Failed to allocate atlas view"
+ "[Tiled/TiledProcessor.mm:613] Failed to allocate atlas."
+ "[Tiled/TiledProcessor.mm:630] Failed to allocate atlas view"
+ "[Tiled/TiledProcessor.mm:650] Unexpected color texture width"
+ "[Tiled/TiledProcessor.mm:651] Unexpected color texture height"
+ "[Tiled/TiledProcessor.mm:776] Not enough threads per threadgroup for tile size"
+ "_atlasSize"
+ "_backingPlane"
+ "_skipFirstTile"
+ "_tileSize"
+ "_tileSize >= 32"
+ "copyFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:"
+ "debugDescription"
+ "description"
+ "encodeToCommandBuffer:inPlaceTexture:fallbackCopyAllocator:"
+ "error"
+ "frag_mxi_backing_plane"
+ "frag_mxi_backing_plane_array"
+ "generateBackingPlaneMesh:atDepth:"
+ "generateBackingPlaneTexture:forScene:"
+ "include_backing_plane"
+ "initForBackingPlaneWithDevice:colorPixelFormat:depthPixelFormat:sampleCount:error:"
+ "initWithDevice:sigma:"
+ "mxi_expect(!_overriddenLayerDepths, \"getLayerRange should not be used if layer depths was overridden\")"
+ "mxi_expect(!_overriddenLayerDepths, \"getLayerViewMatrix should not be used if layer depths was overridden\")"
+ "v28@0:8^v16f24"
- "(tileSize & (tileSize - 1)) == 0"
- "GetAtlas curren: %llu MB peak: %llu MB\n"
- "[MXI.framework/MXIRenderer.mm:117] [MXI] scene.colorTextures.count (%d) > ATLAS_SLICES_CAPACITY (%d)"
- "[MXI.framework/MXISceneBuilderBase.mm:229] Cannot compress MXIScene: scene already compressed"
- "[MXI.framework/MXISceneBuilderTiled.mm:145] Failed on creating TiledProcessor"
- "[MXI.framework/MXISceneBuilderTiled.mm:90] Cannot recognize ASTC quality option %@"
- "[MXI.framework] [MXISceneBuilderTiled] building tiled scene with options %@"
- "[MXI.framework] [MXISceneBuilder] Initializing builder for MXIType %s with %ld layers in %f and %f range with material description and options %@"
- "[MXI.framework] [MXIScene] wrote to URL with options %@"
- "[Tiled/TiledProcessor.mm:389] Packing in compressed atlas is not supported, continuing without it."
- "[Tiled/TiledProcessor.mm:550] Number of atlas slices exceeds MAX_FIXED_ATLAS_SLICES."
- "[Tiled/TiledProcessor.mm:579] Failed to allocate atlas."
- "[Tiled/TiledProcessor.mm:595] Failed to allocate atlas view"
- "[Tiled/TiledProcessor.mm:608] Failed to allocate atlas."
- "[Tiled/TiledProcessor.mm:625] Failed to allocate atlas view"
- "tileSize >= 32"

```
