## RealityCoreTextureImport

> `/System/Library/PrivateFrameworks/RealityCoreTextureImport.framework/RealityCoreTextureImport`

```diff

 24.0.5.0.1
-  __TEXT.__text: 0x4b770
+  __TEXT.__text: 0x4b95c
   __TEXT.__objc_methlist: 0x3ac
   __TEXT.__const: 0xe108
   __TEXT.__cstring: 0x352f

   - /usr/lib/libate.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1364
+  Functions: 1365
   Symbols:   1866
   CStrings:  528
 
Functions:
~ __ZN12_GLOBAL__N_114processKtxMipsEbRN2re7ContextERK23TextureFromImageOptionsRKNSt3__117basic_string_viewIcNS6_11char_traitsIcEEEERK13KTXHeaderDataRKNS6_8multimapIlmNS6_4lessImEENS6_9allocatorINS6_4pairIKlmEEEEEER11InputStreamRKN2NS9SharedPtrIN3MTL17TextureDescriptorEEEbPKNS6_8functionIFvvEEER15ImportedTextureNS6_4spanIPKNS0_17CancellationTokenELm18446744073709551615EEE : 1708 -> 1712
~ __ZN12_GLOBAL__N_125processKtxMipsWithBuilderERNS_23TextureBuilderInterfaceENSt3__14spanIPKN2re17CancellationTokenELm18446744073709551615EEERK13KTXHeaderDataR11InputStreamPKNS2_8functionIFvvEEE : 1208 -> 1252
~ ___62+[RTITextureLoaderASTCHelper isASTCHDRData:textureType:error:]_block_invoke : 1604 -> 1636
~ __ZN21TextureInMetalBuffers8allocateEmmmP11InputStreamRKN3MTL4SizeEmRKNSt3__18multimapIlmNS6_4lessImEENS6_9allocatorINS6_4pairIKlmEEEEEE : 2112 -> 2100
~ __Z26init_block_size_descriptorjjjbjfR21block_size_descriptor : 5356 -> 5372
~ __Z14compress_blockRK16astcenc_contextiRK11image_blockPhR27compression_working_buffers : 3880 -> 3892
~ __ZL44compress_symbolic_block_for_partition_1planeRK14astcenc_configRK21block_size_descriptorRK11image_blockbfjjR25symbolic_compressed_blockR27compression_working_buffersi : 2388 -> 2344
~ __ZNK21block_size_descriptor18get_partition_infoEjj : 152 -> 156
~ __ZL25realign_weights_decimated15astcenc_profileRK21block_size_descriptorRK11image_blockR25symbolic_compressed_block : 1148 -> 1184
~ __ZL27realign_weights_undecimated15astcenc_profileRK21block_size_descriptorRK11image_blockR25symbolic_compressed_block : 768 -> 764
~ __ZL39compute_ideal_colors_and_weights_3_compRK11image_blockRK14partition_infoR21endpoints_and_weightsj : 1032 -> 1040
~ __Z30recompute_ideal_colors_2planesRK11image_blockRK21block_size_descriptorRK15decimation_infoPKhS9_R9endpointsR7vfloat4SD_i : 2072 -> 2076
~ __Z16load_image_block15astcenc_profileRK13astcenc_imageR11image_blockRK21block_size_descriptorjjjRK15astcenc_swizzle : 1236 -> 1256
~ __ZL9swz_texel7vfloat4RK15astcenc_swizzle : 128 -> 132
~ __Z25load_image_block_fast_ldr15astcenc_profileRK13astcenc_imageR11image_blockRK21block_size_descriptorjjjRK15astcenc_swizzle : 492 -> 496
~ __Z30compute_ideal_endpoint_formatsRK14partition_infoRK11image_blockRK9endpointsPKaPKfjjjPA4_hPiP12quant_methodSG_R27compression_working_buffers : 6144 -> 6088
~ __Z20pack_color_endpoints7vfloat4S_S_S_iPh12quant_method : 4932 -> 5084
~ __ZL36try_quantize_rgb_delta_blue_contract7vfloat4S_R5vint4S1_12quant_method : 768 -> 784
~ __ZL22try_quantize_rgb_delta7vfloat4S_R5vint4S1_12quant_method : 604 -> 620
~ __ZL12quantize_rgb7vfloat4S_R5vint4S1_12quant_method : 256 -> 260
~ __ZL16quantize_hdr_rgb7vfloat4S_Ph12quant_method : 1628 -> 1660
~ __ZL24try_quantize_alpha_delta7vfloat4S_R5vint4S1_12quant_method : 184 -> 192
~ __ZL42compute_angular_endpoints_for_quant_levelsjPKfjPfS1_ : 1268 -> 1276
~ __ZL45build_partition_table_for_one_partition_countR21block_size_descriptorbjjP14partition_infoPy : 732 -> 748
~ __Z30find_best_partition_candidatesRK21block_size_descriptorRK11image_blockjjPjj : 4040 -> 4044
~ __Z10encode_ise12quant_methodjPKhPhj : 1804 -> 1864
~ __Z29compute_pixel_region_varianceR16astcenc_contextiRK17pixel_region_args : 2732 -> 2752
~ __ZL21brent_kung_prefix_sumP7vfloat4mi : 196 -> 204
~ __ZNSt3__16vectorIN2re9SharedPtrINS1_12ImportSourceEEENS_9allocatorIS4_EEE24__emplace_back_slow_pathIJS4_EEEPS4_DpOT_ : 228 -> 232
+ __Z26compute_error_squared_rgbaRK14partition_infoRK11image_blockPK15processed_line4S7_PfRfS9_.cold.1
```
