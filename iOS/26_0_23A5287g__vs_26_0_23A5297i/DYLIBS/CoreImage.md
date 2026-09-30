## CoreImage

> `/System/Library/Frameworks/CoreImage.framework/CoreImage`

```diff

-1578.0.0.0.0
-  __TEXT.__text: 0x2d1884
+1583.0.0.0.0
+  __TEXT.__text: 0x2d1cbc
   __TEXT.__auth_stubs: 0x2f10
   __TEXT.__objc_methlist: 0x14f68
   __TEXT.__const: 0xbb98
-  __TEXT.__gcc_except_tab: 0x5eb8
-  __TEXT.__cstring: 0x87962
-  __TEXT.__oslogstring: 0xa531
+  __TEXT.__gcc_except_tab: 0x5eac
+  __TEXT.__cstring: 0x8792a
+  __TEXT.__oslogstring: 0xa5db
   __TEXT.__dlopen_cstrs: 0x313
   __TEXT.__runtimeheader: 0xda3c
-  __TEXT.__cikl2metal_pre: 0x47f
+  __TEXT.__cikl2metal_pre: 0x50d
   __TEXT.__grain: 0x105040
-  __TEXT.__unwind_info: 0x6b50
+  __TEXT.__unwind_info: 0x6b58
   __TEXT.__eh_frame: 0x208
   __TEXT.__objc_classname: 0x2a59
   __TEXT.__objc_methname: 0x204ad

   __DATA_CONST.__objc_arraydata: 0x14a0
   __AUTH_CONST.__auth_got: 0x17a0
   __AUTH_CONST.__const: 0xd110
-  __AUTH_CONST.__cfstring: 0x19f80
+  __AUTH_CONST.__cfstring: 0x19fa0
   __AUTH_CONST.__objc_const: 0x2a598
   __AUTH_CONST.__objc_intobj: 0xd98
   __AUTH_CONST.__objc_dictobj: 0x438

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3B1F67CD-3CE3-3488-AE2C-EDA7A6A1F287
-  Functions: 14008
-  Symbols:   43345
-  CStrings:  18041
+  UUID: 9DE83C37-34F4-3531-A3FA-A290FCEAF050
+  Functions: 14010
+  Symbols:   43349
+  CStrings:  18044
 
Symbols:
+ __ZN2CI16MetalTextureNode17release_resourcesEv
+ __ZN2CI9SWContext28invalidate_switch_dictionaryEv
+ ___52+[CIContext(Internal) internalSWContextWithOptions:]_block_invoke.305
+ ___66+[CIContext(Internal) internalContextWithMTLCommandQueue:options:]_block_invoke.304
+ ___Block_byref_object_copy_.560
+ ___Block_byref_object_dispose_.561
+ ____ZL19set_context_optionsPN2CI9GLContextEP12NSDictionary_block_invoke.402
+ ___block_literal_global.203
+ ___block_literal_global.392
+ ___block_literal_global.544
- ___52+[CIContext(Internal) internalSWContextWithOptions:]_block_invoke.302
- ___66+[CIContext(Internal) internalContextWithMTLCommandQueue:options:]_block_invoke.301
- ___Block_byref_object_copy_.559
- ___Block_byref_object_dispose_.560
- ____ZL19set_context_optionsPN2CI9GLContextEP12NSDictionary_block_invoke.399
- ___block_literal_global.389
- ___block_literal_global.543
Functions:
~ -[CIContext loadArchiveWithName:fromURL:] : 144 -> 176
~ -[CIContext loadArchive:] : 128 -> 144
~ +[CIContext loadArchiveWithName:fromURL:] : 152 -> 156
~ -[CIContext(ImageRepresentation) _addDepthMap:session:imageHandle:options:] : 1020 -> 1016
~ __ZN18CIKernelReflection7reflectEP15CIKernelLibraryPKcPP7NSError : 5392 -> 5424
~ -[CIKernel setPerservesAlpha:] : 288 -> 304
~ -[CIColorKernel setPerservesAlpha:] : 288 -> 304
~ -[CIRenderDestination _render:withContext:] : 1176 -> 1180
~ __ZN2CI9SWContextD2Ev : 220 -> 236
+ __ZN2CI9SWContext28invalidate_switch_dictionaryEv
- __ZN2CI7Context28invalidate_switch_dictionaryEv
~ __ZNK2CI16PixelBufferImage17render_graph_coreEPNS_7ContextERNS_14ImageToNodeMapERKNSt3__13mapINS_11ImageDigestE6CGRectNS5_4lessIS7_EENS5_9allocatorINS5_4pairIKS7_S8_EEEEEEi : 1704 -> 1720
+ __ZN2CI7Context28invalidate_switch_dictionaryEv
~ __ZN2CI7Context21render_processor_nodeEPNS_8TileTaskERKNS_9parentROIEP11__IOSurfacePKv : 1148 -> 1716
~ __ZN2CI24format_swizzle_for_inputENS_11PixelFormatEbU13block_pointerFbS0_E : 7764 -> 7924
~ __ZN2CIL20AppendConverterArrayEPNS_7ContextEPNS_4NodeENS_10ImageIndexEPK9__CFArrayNS_18ConverterDirectionEbb : 7464 -> 7680
~ __ZNK2CI13ProcessorNode6renderEPNS_8TileTaskEPNS_7ContextERKNSt3__16vectorIPKNS_14intermediate_tENS5_9allocatorIS9_EEEESE_RK6CGRecti : 3032 -> 2872
+ __ZN2CI16MetalTextureNode17release_resourcesEv
~ __ZN2CI22image_render_to_bitmapEPNS_7ContextEPNS_5ImageE6CGRectP12CGColorSpacePNS_6BitmapEPKNS_17RenderDestinationE : 1856 -> 1868
CStrings:
+ "%{public}s is deprecated. Add [[stitchable,user_annotation(\"kCIPreservesOpacity\")]] to the Metal source instead."
+ "%{public}s is deprecated. Add __attribute__((preserves_opacity)) to the CIKL source instead."
+ "1583"
+ "_bin"
+ "main1"
- "%{public}s is deprecated.%{public}s"
- "1578"
- "Add __attribute__((preserves_opacity)) to the CIKL source instead."

```
