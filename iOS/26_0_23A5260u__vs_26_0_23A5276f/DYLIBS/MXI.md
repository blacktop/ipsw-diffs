## MXI

> `/System/Library/PrivateFrameworks/MXI.framework/MXI`

```diff

-29.0.12.500.2
-  __TEXT.__text: 0x3c890
+29.0.15.0.2
+  __TEXT.__text: 0x3cb58
   __TEXT.__auth_stubs: 0x8d0
-  __TEXT.__objc_methlist: 0xe90
+  __TEXT.__objc_methlist: 0xe48
   __TEXT.__const: 0x9d30
-  __TEXT.__gcc_except_tab: 0x5410
-  __TEXT.__cstring: 0x3335
-  __TEXT.__oslogstring: 0x16bc
-  __TEXT.__unwind_info: 0xc00
-  __TEXT.__objc_classname: 0x16e
-  __TEXT.__objc_methname: 0x3c0a
-  __TEXT.__objc_methtype: 0xa00
-  __TEXT.__objc_stubs: 0x34e0
+  __TEXT.__gcc_except_tab: 0x53c8
+  __TEXT.__cstring: 0x33b4
+  __TEXT.__oslogstring: 0x169e
+  __TEXT.__unwind_info: 0xbd8
+  __TEXT.__objc_classname: 0x16c
+  __TEXT.__objc_methname: 0x3b22
+  __TEXT.__objc_methtype: 0x9a0
+  __TEXT.__objc_stubs: 0x3460
   __DATA_CONST.__got: 0x320
-  __DATA_CONST.__const: 0x5f0
+  __DATA_CONST.__const: 0x5d0
   __DATA_CONST.__objc_classlist: 0x88
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xf20
+  __DATA_CONST.__objc_selrefs: 0xef0
   __DATA_CONST.__objc_superrefs: 0x68
   __AUTH_CONST.__auth_got: 0x478
   __AUTH_CONST.__const: 0x3c8
-  __AUTH_CONST.__cfstring: 0x2f40
-  __AUTH_CONST.__objc_const: 0x1e28
+  __AUTH_CONST.__cfstring: 0x3000
+  __AUTH_CONST.__objc_const: 0x1e08
   __AUTH_CONST.__objc_intobj: 0x2a0
   __AUTH.__objc_data: 0x550
-  __DATA.__objc_ivar: 0x1d0
+  __DATA.__objc_ivar: 0x1cc
   __DATA.__data: 0x128
   __DATA.__bss: 0x4188
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 82247B68-F0B2-382A-A4B5-156C805A93C9
-  Functions: 722
-  Symbols:   448
-  CStrings:  1810
+  UUID: 11EB14C3-0F7B-30D6-8D48-76AB8E3AE50C
+  Functions: 719
+  Symbols:   445
+  CStrings:  1812
 
Symbols:
+ _MXISceneBuilderASTCQualityThorough
+ __ZN5image7ToASTCsEPU15__autoreleasingKPU21objcproto10MTLTexture11objc_objectjhhfjj
- _MXISceneBuilderConfigurationAspectRatio
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
CStrings:
+ "/'0"
+ "B48@0:8r^v16@24I32f36^@40"
+ "Failed ot create USDZ writer."
+ "Failed serializing scene."
+ "Failed writing scene to file."
+ "Failed writing to file."
+ "MXI: Remove Layer Mesh Overlap"
+ "MXI_ATLAS_DATA"
+ "Number of slices: %lu\nResolution: %u x %u"
+ "[Core/CoreSerialization.mm:489] Error while reading from compression stream. (source length: %d, read source length: %d, dest length: %d, written dest length: %d)"
+ "[Core/MXIError.m:72] MXI error: %@"
+ "[Image] [ASTCEncoder] Initializing with block width %u and height %u, rank modes count ratio %f fast skip threshold %u"
+ "[MXI.framework/MXIScene.mm:864] Texture not available"
+ "[MXI.framework/MXISceneBuilderBase.mm:490] Unknown color primaries specified %@"
+ "[MXI.framework/MXISceneBuilderBase.mm:495] Unknown color primaries specified %@"
+ "[MXI.framework/MXISceneBuilderBase.mm:509] Layer depths should be overridden with NSArray<NSNumber*>, but the value is not NSArray"
+ "[MXI.framework/MXISceneBuilderBase.mm:511] Layer depths array size (%u) shold match number of layers (%u)"
+ "[MXI.framework/MXISceneBuilderBase.mm:518] Failed parsing depth for layer %u"
+ "[MXI.framework/MXISceneBuilderTiled.mm:145] Failed on creating TiledProcessor"
+ "[MXI.framework/MXISceneBuilderTiled.mm:90] Cannot recognize ASTC quality option %@"
+ "[Tiled/TiledProcessor.mm:389] Packing in compressed atlas is not supported, continuing without it."
+ "[Tiled/TiledProcessor.mm:550] Number of atlas slices exceeds MAX_FIXED_ATLAS_SLICES."
+ "[Tiled/TiledProcessor.mm:579] Failed to allocate atlas."
+ "[Tiled/TiledProcessor.mm:595] Failed to allocate atlas view"
+ "[Tiled/TiledProcessor.mm:608] Failed to allocate atlas."
+ "[Tiled/TiledProcessor.mm:625] Failed to allocate atlas view"
+ "astc_thorough"
+ "init_vtx_idx_map"
+ "kern_init_vertex_index_map"
+ "kern_remove_layer_overlap"
- "/%0"
- "@\"<MTLCommandQueue>\""
- "Failed writing to file"
- "MXISceneBuilder (processLayer:%ld forFace:%ld)"
- "Output writer not available"
- "[Core/CoreSerialization.mm:482] Error while reading from compression stream. (source length: %d, read source length: %d, dest length: %d, written dest length: %d)"
- "[Image] [ASTCEncoder] Initializing with block width %u and height %u"
- "[MXI.framework/MXIScene.mm:872] Texture not available"
- "[MXI.framework/MXISceneBuilderBase.mm:535] Unknown color primaries specified %@"
- "[MXI.framework/MXISceneBuilderBase.mm:540] Unknown color primaries specified %@"
- "[MXI.framework/MXISceneBuilderBase.mm:554] Layer depths should be overridden with NSArray<NSNumber*>, but the value is not NSArray"
- "[MXI.framework/MXISceneBuilderBase.mm:556] Layer depths array size (%u) shold match number of layers (%u)"
- "[MXI.framework/MXISceneBuilderBase.mm:563] Failed parsing depth for layer %u"
- "[MXI.framework/MXISceneBuilderTiled.mm:143] Failed on creating TiledProcessor"
- "[MXI.framework/MXISceneBuilderTiled.mm:88] Cannot recognize ASTC quality option %@"
- "[MXI.framework] [MXISceneBuilderBase] Processing layer %ld for face %ld with color and depth"
- "[MXI.framework] [MXISceneBuilder] Processing layer %ld for face %ld with color"
- "[Tiled/TiledProcessor.mm:386] Packing in compressed atlas is not supported, continuing without it."
- "[Tiled/TiledProcessor.mm:533] Number of atlas slices exceeds MAX_FIXED_ATLAS_SLICES."
- "[Tiled/TiledProcessor.mm:562] Failed to allocate atlas."
- "[Tiled/TiledProcessor.mm:578] Failed to allocate atlas view"
- "[Tiled/TiledProcessor.mm:591] Failed to allocate atlas."
- "[Tiled/TiledProcessor.mm:608] Failed to allocate atlas view"
- "_cmdQueue"
- "processLayer:forFace:withBaseColor:depth:normal:extendedTextures:error:"
- "processLayer:forFace:withColor:andDepth:error:"
- "processLayer:forFace:withColor:error:"
- "renderWithDescriptor:commandEncoder:context:"
- "sampleCount"
- "v48@0:8q16q24@32^@40"
- "v48@0:8r^v16@24I32f36^@40"
- "v56@0:8q16q24@32@40^@48"
- "v72@0:8q16q24@32@40@48@56^@64"

```
