## libBNNS.dylib

> `/System/Library/Frameworks/Accelerate.framework/Versions/A/Frameworks/vecLib.framework/Versions/A/libBNNS.dylib`

```diff

-1361.0.37.0.1
-  __TEXT.__text: 0x93bd3c
+1361.0.52.0.3
+  __TEXT.__text: 0x9455ac
   __TEXT.__auth_stubs: 0x11d0
-  __TEXT.__gcc_except_tab: 0x25d60
-  __TEXT.__const: 0x11fef
-  __TEXT.__cstring: 0x2a710
+  __TEXT.__gcc_except_tab: 0x26824
+  __TEXT.__const: 0x1282f
+  __TEXT.__cstring: 0x2aab2
   __TEXT.__oslogstring: 0x303
-  __TEXT.__unwind_info: 0xa1c8
+  __TEXT.__unwind_info: 0xa218
   __TEXT.__eh_frame: 0x8a28
   __DATA_CONST.__got: 0xf8
-  __DATA_CONST.__const: 0x3540
+  __DATA_CONST.__const: 0x3550
   __AUTH_CONST.__auth_got: 0x8f0
   __AUTH_CONST.__auth_ptr: 0x2c8
   __AUTH_CONST.__const: 0xe718

   - /System/Library/PrivateFrameworks/MIL.framework/Versions/A/MIL
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  Functions: 10980
-  Symbols:   600
-  CStrings:  4039
+  Functions: 10999
+  Symbols:   601
+  CStrings:  4065
 
Symbols:
+ _BNNSGraphGetArgumentInterleaveFactors
CStrings:
+ " %!h(MISSING)u"
+ " interleave=["
+ "BNNS Convolution: Repacking to CONV_WEIGHT_REPACK_MLA1 on this hardware is not yet supported\n"
+ "BNNS Convolution: Repacking to CONV_WEIGHT_REPACK_MLA_GENERAL_* on this hardware is not yet supported\n"
+ "BNNS MatVec MLA1: size not supported\n"
+ "BNNSGraphGetArgumentInterleaveFactors"
+ "BNNSGraphGetArgumentInterleaveFactors passed graph with unsupported ir_version %!x(MISSING)"
+ "BNNSGraphGetArgumentInterleaveFactors passed invalid graph"
+ "BNNSGraphTensorFillStrides: Tensor has unsupported layout\n"
+ "BasicNeuralNetworkSubroutines-1361.0.52.0.3~31"
+ "Function provided not found in BNNS-IR"
+ "Function provided not found in BNNS-IR."
+ "IR::KERNEL_CONV_KERNELPOOL_FACETIME_VOICE_ISOLATION_MLA2_12x1x64OC_x_12x1x8IC_FP32xFP16_TO_FP32"
+ "KERNEL_ARITHMETIC_BINARY_MLA2"
+ "KERNEL_ARITHMETIC_BINARY_MLA3"
+ "KERNEL_CAST_MLA1"
+ "KERNEL_CAST_MLA2"
+ "KERNEL_CAST_MLA3"
+ "KERNEL_CONV_3D_MLA1"
+ "KERNEL_CONV_3D_MLA2"
+ "KERNEL_CONV_3D_MLA3"
+ "KERNEL_CONV_KERNELPOOL_APPLE_MUSIC_SING_DEPTHWISE_OW128_IOC448_MLA3"
+ "KERNEL_CONV_KERNELPOOL_APPLE_MUSIC_SING_MLA1_S32_1_A_1_FP16"
+ "KERNEL_CONV_KERNELPOOL_APPLE_MUSIC_SING_MLA2_S32_1_A_1_FP16"
+ "KERNEL_CONV_KERNELPOOL_DEPTHWISE_MLA2_S1x1_FP16"
+ "KERNEL_CONV_KERNELPOOL_DEPTHWISE_MLA2_S1x1_FP32"
+ "KERNEL_CONV_KERNELPOOL_DEPTHWISE_MLA3_S1x1_FP16"
+ "KERNEL_CONV_KERNELPOOL_DEPTHWISE_MLA3_S1x1_FP32"
+ "KERNEL_CONV_KERNELPOOL_DEPTHWISE_MLA3_S2x2_FP32"
+ "KERNEL_CONV_KERNELPOOL_FACETIME_VOICE_ISOLATION_MLA1_12WIDTH_NET_FP32_xI12_128_1_O12_256_1_KVERTICAL"
+ "KERNEL_CONV_KERNELPOOL_FACETIME_VOICE_ISOLATION_MLA1_12WIDTH_NET_FP32_xI12_128_1_O12_256_1_KVERTICAL_FP16"
+ "KERNEL_CONV_KERNELPOOL_FACETIME_VOICE_ISOLATION_MLA1_12WIDTH_NET_FP32_xI12_128_1_O12_256_1_KVERTICAL_FP32xFP16_TO_FP32"
+ "KERNEL_CONV_KERNELPOOL_FACETIME_VOICE_ISOLATION_MLA1_12WIDTH_NET_xI520_1_4_O12_1_256_K80_1_S40_1_A_1_FP16"
+ "KERNEL_CONV_KERNELPOOL_FACETIME_VOICE_ISOLATION_MLA1_12WIDTH_NET_xI520_1_4_O12_1_256_K80_1_S40_1_A_1_FP32"
+ "KERNEL_CONV_KERNELPOOL_FACETIME_VOICE_ISOLATION_MLA1_12WIDTH_NET_xI520_1_4_O12_1_256_K80_1_S40_1_A_1_FP32xFP16_TO_FP32"
+ "KERNEL_CONV_KERNELPOOL_FACETIME_VOICE_ISOLATION_MLA1_12x1x64OC_x_12x1x8IC"
+ "KERNEL_CONV_KERNELPOOL_FACETIME_VOICE_ISOLATION_MLA1_12x1x64OC_x_12x1x8IC_FP32xFP16_TO_FP32"
+ "KERNEL_CONV_KERNELPOOL_FACETIME_VOICE_ISOLATION_MLA1_32WIDTH_NET_xI1320_1_4_O32_1_256_K80_1_S40_1_A_1_FP16"
+ "KERNEL_CONV_KERNELPOOL_FACETIME_VOICE_ISOLATION_MLA1_MWIDTH_NET_FP32_xIM_128_1_OM_256_1_KVERTICAL_FP16"
+ "KERNEL_CONV_KERNELPOOL_FACETIME_VOICE_ISOLATION_MLA1_Mx1x32OC_x_Mx1x8IC_FP16"
+ "KERNEL_CONV_KERNELPOOL_FACETIME_VOICE_ISOLATION_MLA1_Mx1x64OC_x_Mx1x8IC_FP16"
+ "KERNEL_CONV_KERNELPOOL_FACETIME_VOICE_ISOLATION_MLA1_S1x1_O12x1x32N_I12x1x8M_K1x1_P0x0x0x0_GK_FP16"
+ "KERNEL_CONV_KERNELPOOL_FACETIME_VOICE_ISOLATION_MLA1_S1x1_O12x1x64N_I12x1x8M_K1x1_P0x0x0x0_GK_FP16"
+ "KERNEL_CONV_KERNELPOOL_FACETIME_VOICE_ISOLATION_MLA1_S1x1_O12x1x64N_I12x1x8M_K1x1_P0x0x0x0_GK_FP32xFP16_TO_FP32"
+ "KERNEL_CONV_KERNELPOOL_FACETIME_VOICE_ISOLATION_MLA1_S32_1_A_1_FP16"
+ "KERNEL_CONV_KERNELPOOL_FACETIME_VOICE_ISOLATION_MLA2_12WIDTH_NET_xI520_1_4_O12_1_256_K80_1_S40_1_A_1_FP16"
+ "KERNEL_CONV_KERNELPOOL_FACETIME_VOICE_ISOLATION_MLA2_12WIDTH_NET_xI520_1_4_O12_1_256_K80_1_S40_1_A_1_FP32"
+ "KERNEL_CONV_KERNELPOOL_FACETIME_VOICE_ISOLATION_MLA2_12WIDTH_NET_xI520_1_4_O12_1_256_K80_1_S40_1_A_1_FP32xFP16_TO_FP32"
+ "KERNEL_CONV_KERNELPOOL_FACETIME_VOICE_ISOLATION_MLA2_12x1x64OC_x_12x1x8IC"
+ "KERNEL_CONV_KERNELPOOL_FACETIME_VOICE_ISOLATION_MLA2_12x1x64OC_x_12x1x8IC_FP16"
+ "KERNEL_CONV_KERNELPOOL_FACETIME_VOICE_ISOLATION_MLA2_12x1x64OC_x_12x1x8IC_FP16_4BIT_PALETTIZED"
+ "KERNEL_CONV_KERNELPOOL_FACETIME_VOICE_ISOLATION_MLA2_32WIDTH_NET_xI1320_1_4_O32_1_256_K80_1_S40_1_A_1_FP16"
+ "KERNEL_CONV_KERNELPOOL_FACETIME_VOICE_ISOLATION_MLA2_Mx1x32OC_x_Mx1x8IC_FP16"
+ "KERNEL_CONV_KERNELPOOL_FACETIME_VOICE_ISOLATION_MLA2_Mx1x64OC_x_Mx1x8IC_FP16"
+ "KERNEL_CONV_KERNELPOOL_FACETIME_VOICE_ISOLATION_MLA2_Mx1x64OC_x_Mx1x8IC_FP16_4BIT_PALETTIZED"
+ "KERNEL_CONV_KERNELPOOL_FACETIME_VOICE_ISOLATION_MLA2_S1x1_O12x1x32N_I12x1x8M_K1x1_P0x0x0x0_GK_FP16"
+ "KERNEL_CONV_KERNELPOOL_FACETIME_VOICE_ISOLATION_MLA2_S1x1_O12x1x64N_I12x1x8M_K1x1_P0x0x0x0_GK_FP16"
+ "KERNEL_CONV_KERNELPOOL_FACETIME_VOICE_ISOLATION_MLA2_S1x1_O12x1x64N_I12x1x8M_K1x1_P0x0x0x0_GK_FP32xFP16_TO_FP32"
+ "KERNEL_CONV_KERNELPOOL_FACETIME_VOICE_ISOLATION_MLA2_S32_1_A_1_FP16"
+ "KERNEL_CONV_KERNELPOOL_FACETIME_VOICE_ISOLATION_MLA3_12x1x64OC_x_12x1x8IC"
+ "KERNEL_CONV_MLA"
+ "KERNEL_CONV_MLA_DYNAMIC"
+ "KERNEL_CONV_MLA_SPECIAL"
+ "KERNEL_CONV_SPARSE_MLA2_DYNAMIC"
+ "KERNEL_CONV_TRANS_2D_MLA1"
+ "KERNEL_CONV_TRANS_2D_MLA2"
+ "KERNEL_CONV_TRANS_2D_MLA3"
+ "KERNEL_CONV_TRANS_3D_MLA1"
+ "KERNEL_CONV_TRANS_3D_MLA2"
+ "KERNEL_CONV_TRANS_3D_MLA3"
+ "KERNEL_COPY_MLA1"
+ "KERNEL_COPY_MLA2"
+ "KERNEL_COPY_MLA3"
+ "KERNEL_COPY_SLICE_UPDATE_MLA1"
+ "KERNEL_COPY_SLICE_UPDATE_MLA2"
+ "KERNEL_COPY_SLICE_UPDATE_MLA3"
+ "KERNEL_EINSUM_STRIDED_MATMUL_MLA1_DYNAMIC"
+ "KERNEL_EINSUM_STRIDED_MATMUL_MLA2_DYNAMIC"
+ "KERNEL_EINSUM_STRIDED_MATMUL_MLA3_DYNAMIC"
+ "KERNEL_GRU_FUSED_RESET_GATE_BACKWARD_MLA2"
+ "KERNEL_GRU_FUSED_RESET_GATE_BACKWARD_MLA3"
+ "KERNEL_GRU_FUSED_UPDATE_GATE_BACKWARD_MLA2"
+ "KERNEL_GRU_FUSED_UPDATE_GATE_BACKWARD_MLA3"
+ "KERNEL_MATMUL_ADD_FP32_MLA2"
+ "KERNEL_MATMUL_MLA1"
+ "KERNEL_MATMUL_MLA1_DYNAMIC"
+ "KERNEL_MATMUL_MLA2"
+ "KERNEL_MATMUL_MLA2_DYNAMIC"
+ "KERNEL_MATMUL_MLA2_GRP_INT4"
+ "KERNEL_MATMUL_MLA3"
+ "KERNEL_MATMUL_MLA3_DKM_INT3"
+ "KERNEL_MATMUL_MLA3_DYNAMIC"
+ "KERNEL_MATMUL_MLA3_GRP_INT4"
+ "KERNEL_MATMUL_MLA3_GRP_INT4_V2"
+ "KERNEL_MATMUL_MUL_TO_MASK_ADD_BF16_FP32_MLA3"
+ "KERNEL_MATMUL_MUL_TO_MASK_ADD_FP32_MLA2"
+ "KERNEL_MGLM_MATMUL_2x2_INDEXED4_MLA3"
+ "KERNEL_MGLM_MHA_PART0_V1_BF16_FP32_MLA3"
+ "KERNEL_MGLM_MHA_PART1_V1_BF16_FP32_1x32x64_MLA3"
+ "KERNEL_MGLM_MHA_V2_BF16_FP32_MLA3"
+ "KERNEL_MUL_TO_MASK_MATMUL_ADD_BF16_FP32_MLA3"
+ "KERNEL_MUL_TO_MASK_MATMUL_ADD_FP32_MLA2"
+ "KERNEL_REDUCE_KERNELPOOL_WAVERNN_REDUCE_BATCH32_KERNEL0_MLA1_FP32"
+ "KERNEL_REDUCE_KERNELPOOL_WAVERNN_REDUCE_BATCH32_KERNEL0_MLA2_FP32"
+ "KERNEL_REDUCE_KERNELPOOL_WAVERNN_REDUCE_BATCH32_KERNEL0_MLA3_BF16"
+ "KERNEL_REDUCE_KERNELPOOL_WAVERNN_REDUCE_BATCH32_KERNEL1_MLA1_FP32"
+ "KERNEL_REDUCE_KERNELPOOL_WAVERNN_REDUCE_BATCH32_KERNEL1_MLA2_FP32"
+ "KERNEL_REDUCE_KERNELPOOL_WAVERNN_REDUCE_BATCH32_KERNEL1_MLA3_BF16"
+ "KERNEL_REDUCE_KERNELPOOL_WAVERNN_REDUCE_BATCH32_KERNEL2_MLA1_FP32"
+ "KERNEL_REDUCE_KERNELPOOL_WAVERNN_REDUCE_BATCH32_KERNEL2_MLA2_FP32"
+ "KERNEL_REDUCE_KERNELPOOL_WAVERNN_REDUCE_BATCH32_KERNEL2_MLA3_BF16"
+ "KERNEL_REDUCE_KERNELPOOL_WAVERNN_REDUCE_BATCH32_KERNEL3_MLA1_FP32"
+ "KERNEL_REDUCE_KERNELPOOL_WAVERNN_REDUCE_BATCH32_KERNEL3_MLA2_FP32"
+ "KERNEL_REDUCE_KERNELPOOL_WAVERNN_REDUCE_BATCH32_KERNEL3_MLA3_BF16"
+ "KERNEL_REDUCE_KERNELPOOL_WAVERNN_REDUCE_BATCH32_KERNEL4_MLA1_FP32"
+ "KERNEL_REDUCE_KERNELPOOL_WAVERNN_REDUCE_BATCH32_KERNEL4_MLA2_FP32"
+ "KERNEL_REDUCE_KERNELPOOL_WAVERNN_REDUCE_BATCH32_KERNEL4_MLA3_BF16"
+ "KERNEL_TTS_NLP_RETNET"
+ "KERNEL_TTS_SOUNDSTORM_FIXED_CONV_MF_SWIGLU_MODULE"
+ "User-provided descriptor for tensor 0x%!l(MISSING)lx not compatible either in size (size %!z(MISSING)u vs. %!l(MISSING)lu expected) or in rank (rank %!h(MISSING)hu vs. %!l(MISSING)lu expected).\n"
+ "User-provided descriptor for tensor 0x%!l(MISSING)lx not compatible either in size (size %!z(MISSING)u vs. %!l(MISSING)lu expected) or in rank (rank %!z(MISSING)u vs. %!l(MISSING)lu expected).\n"
+ "User-provided pointer for tensor 0x%!l(MISSING)lx has size %!z(MISSING)u but BNNS requires size >= %!l(MISSING)lu\n"
+ "User-provided tensor for argument 0x%!l(MISSING)lx has data size %!z(MISSING)u but BNNS requires size >= %!l(MISSING)lu\n"
+ "combo_tts_nlp_retnet"
+ "combo_tts_soundstorm_FIXED_CONV_MF_SWIGLU_MODULE"
+ "function provided not found in BNNS-IR."
+ "internal.combo_tts_nlp_retnet"
+ "internal.combo_tts_soundstorm_FIXED_CONV_MF_SWIGLU_MODULE"
+ "k_value"
+ "kv_output"
+ "mla1"
+ "mla2"
+ "mla3"
+ "normalization_const_multiplier"
+ "prev_kv_const_multiplier"
+ "q_value"
+ "scaled_self_key"
+ "self_key"
+ "self_values"
+ "sin_cos_value"
+ "tts_nlp_retention_scratch(for:"
+ "v_value"
- "Arithmetic: Cannot find binary kernel"
- "BNNS Convolution: Repacking to CONV_WEIGHT_REPACK_AMX1 on non-AMX hardware is not yet supported\n"
- "BNNS Convolution: Repacking to CONV_WEIGHT_REPACK_AMX_GENERAL_* on non-AMX hardware is not yet supported\n"
- "BNNS MatVec AMX1: size not supported\n"
- "BasicNeuralNetworkSubroutines-1361.0.37.0.1~17"
- "IR::KERNEL_CONV_KERNELPOOL_FACETIME_VOICE_ISOLATION_AMX2_12x1x64OC_x_12x1x8IC_FP32xFP16_TO_FP32"
- "KERNEL_ARITHMETIC_BINARY_AMX2"
- "KERNEL_ARITHMETIC_BINARY_AMX3"
- "KERNEL_CAST_AMX1"
- "KERNEL_CAST_AMX2"
- "KERNEL_CAST_AMX3"
- "KERNEL_CONV_3D_AMX1"
- "KERNEL_CONV_3D_AMX2"
- "KERNEL_CONV_3D_AMX3"
- "KERNEL_CONV_AMX"
- "KERNEL_CONV_AMX_DYNAMIC"
- "KERNEL_CONV_AMX_SPECIAL"
- "KERNEL_CONV_KERNELPOOL_APPLE_MUSIC_SING_AMX1_S32_1_A_1_FP16"
- "KERNEL_CONV_KERNELPOOL_APPLE_MUSIC_SING_AMX2_S32_1_A_1_FP16"
- "KERNEL_CONV_KERNELPOOL_APPLE_MUSIC_SING_DEPTHWISE_OW128_IOC448_AMX3"
- "KERNEL_CONV_KERNELPOOL_DEPTHWISE_AMX2_S1x1_FP16"
- "KERNEL_CONV_KERNELPOOL_DEPTHWISE_AMX2_S1x1_FP32"
- "KERNEL_CONV_KERNELPOOL_DEPTHWISE_AMX3_S1x1_FP16"
- "KERNEL_CONV_KERNELPOOL_DEPTHWISE_AMX3_S1x1_FP32"
- "KERNEL_CONV_KERNELPOOL_DEPTHWISE_AMX3_S2x2_FP32"
- "KERNEL_CONV_KERNELPOOL_FACETIME_VOICE_ISOLATION_AMX1_12WIDTH_NET_FP32_xI12_128_1_O12_256_1_KVERTICAL"
- "KERNEL_CONV_KERNELPOOL_FACETIME_VOICE_ISOLATION_AMX1_12WIDTH_NET_FP32_xI12_128_1_O12_256_1_KVERTICAL_FP16"
- "KERNEL_CONV_KERNELPOOL_FACETIME_VOICE_ISOLATION_AMX1_12WIDTH_NET_FP32_xI12_128_1_O12_256_1_KVERTICAL_FP32xFP16_TO_FP32"
- "KERNEL_CONV_KERNELPOOL_FACETIME_VOICE_ISOLATION_AMX1_12WIDTH_NET_xI520_1_4_O12_1_256_K80_1_S40_1_A_1_FP16"
- "KERNEL_CONV_KERNELPOOL_FACETIME_VOICE_ISOLATION_AMX1_12WIDTH_NET_xI520_1_4_O12_1_256_K80_1_S40_1_A_1_FP32"
- "KERNEL_CONV_KERNELPOOL_FACETIME_VOICE_ISOLATION_AMX1_12WIDTH_NET_xI520_1_4_O12_1_256_K80_1_S40_1_A_1_FP32xFP16_TO_FP32"
- "KERNEL_CONV_KERNELPOOL_FACETIME_VOICE_ISOLATION_AMX1_12x1x64OC_x_12x1x8IC"
- "KERNEL_CONV_KERNELPOOL_FACETIME_VOICE_ISOLATION_AMX1_12x1x64OC_x_12x1x8IC_FP32xFP16_TO_FP32"
- "KERNEL_CONV_KERNELPOOL_FACETIME_VOICE_ISOLATION_AMX1_32WIDTH_NET_xI1320_1_4_O32_1_256_K80_1_S40_1_A_1_FP16"
- "KERNEL_CONV_KERNELPOOL_FACETIME_VOICE_ISOLATION_AMX1_MWIDTH_NET_FP32_xIM_128_1_OM_256_1_KVERTICAL_FP16"
- "KERNEL_CONV_KERNELPOOL_FACETIME_VOICE_ISOLATION_AMX1_Mx1x32OC_x_Mx1x8IC_FP16"
- "KERNEL_CONV_KERNELPOOL_FACETIME_VOICE_ISOLATION_AMX1_Mx1x64OC_x_Mx1x8IC_FP16"
- "KERNEL_CONV_KERNELPOOL_FACETIME_VOICE_ISOLATION_AMX1_S1x1_O12x1x32N_I12x1x8M_K1x1_P0x0x0x0_GK_FP16"
- "KERNEL_CONV_KERNELPOOL_FACETIME_VOICE_ISOLATION_AMX1_S1x1_O12x1x64N_I12x1x8M_K1x1_P0x0x0x0_GK_FP16"
- "KERNEL_CONV_KERNELPOOL_FACETIME_VOICE_ISOLATION_AMX1_S1x1_O12x1x64N_I12x1x8M_K1x1_P0x0x0x0_GK_FP32xFP16_TO_FP32"
- "KERNEL_CONV_KERNELPOOL_FACETIME_VOICE_ISOLATION_AMX1_S32_1_A_1_FP16"
- "KERNEL_CONV_KERNELPOOL_FACETIME_VOICE_ISOLATION_AMX2_12WIDTH_NET_xI520_1_4_O12_1_256_K80_1_S40_1_A_1_FP16"
- "KERNEL_CONV_KERNELPOOL_FACETIME_VOICE_ISOLATION_AMX2_12WIDTH_NET_xI520_1_4_O12_1_256_K80_1_S40_1_A_1_FP32"
- "KERNEL_CONV_KERNELPOOL_FACETIME_VOICE_ISOLATION_AMX2_12WIDTH_NET_xI520_1_4_O12_1_256_K80_1_S40_1_A_1_FP32xFP16_TO_FP32"
- "KERNEL_CONV_KERNELPOOL_FACETIME_VOICE_ISOLATION_AMX2_12x1x64OC_x_12x1x8IC"
- "KERNEL_CONV_KERNELPOOL_FACETIME_VOICE_ISOLATION_AMX2_12x1x64OC_x_12x1x8IC_FP16"
- "KERNEL_CONV_KERNELPOOL_FACETIME_VOICE_ISOLATION_AMX2_12x1x64OC_x_12x1x8IC_FP16_4BIT_PALETTIZED"
- "KERNEL_CONV_KERNELPOOL_FACETIME_VOICE_ISOLATION_AMX2_32WIDTH_NET_xI1320_1_4_O32_1_256_K80_1_S40_1_A_1_FP16"
- "KERNEL_CONV_KERNELPOOL_FACETIME_VOICE_ISOLATION_AMX2_Mx1x32OC_x_Mx1x8IC_FP16"
- "KERNEL_CONV_KERNELPOOL_FACETIME_VOICE_ISOLATION_AMX2_Mx1x64OC_x_Mx1x8IC_FP16"
- "KERNEL_CONV_KERNELPOOL_FACETIME_VOICE_ISOLATION_AMX2_Mx1x64OC_x_Mx1x8IC_FP16_4BIT_PALETTIZED"
- "KERNEL_CONV_KERNELPOOL_FACETIME_VOICE_ISOLATION_AMX2_S1x1_O12x1x32N_I12x1x8M_K1x1_P0x0x0x0_GK_FP16"
- "KERNEL_CONV_KERNELPOOL_FACETIME_VOICE_ISOLATION_AMX2_S1x1_O12x1x64N_I12x1x8M_K1x1_P0x0x0x0_GK_FP16"
- "KERNEL_CONV_KERNELPOOL_FACETIME_VOICE_ISOLATION_AMX2_S1x1_O12x1x64N_I12x1x8M_K1x1_P0x0x0x0_GK_FP32xFP16_TO_FP32"
- "KERNEL_CONV_KERNELPOOL_FACETIME_VOICE_ISOLATION_AMX2_S32_1_A_1_FP16"
- "KERNEL_CONV_KERNELPOOL_FACETIME_VOICE_ISOLATION_AMX3_12x1x64OC_x_12x1x8IC"
- "KERNEL_CONV_SPARSE_AMX2_DYNAMIC"
- "KERNEL_CONV_TRANS_2D_AMX1"
- "KERNEL_CONV_TRANS_2D_AMX2"
- "KERNEL_CONV_TRANS_2D_AMX3"
- "KERNEL_CONV_TRANS_3D_AMX1"
- "KERNEL_CONV_TRANS_3D_AMX2"
- "KERNEL_CONV_TRANS_3D_AMX3"
- "KERNEL_COPY_AMX1"
- "KERNEL_COPY_AMX2"
- "KERNEL_COPY_AMX3"
- "KERNEL_COPY_SLICE_UPDATE_AMX1"
- "KERNEL_COPY_SLICE_UPDATE_AMX2"
- "KERNEL_COPY_SLICE_UPDATE_AMX3"
- "KERNEL_EINSUM_STRIDED_MATMUL_AMX1_DYNAMIC"
- "KERNEL_EINSUM_STRIDED_MATMUL_AMX2_DYNAMIC"
- "KERNEL_EINSUM_STRIDED_MATMUL_AMX3_DYNAMIC"
- "KERNEL_GRU_FUSED_RESET_GATE_BACKWARD_AMX2"
- "KERNEL_GRU_FUSED_RESET_GATE_BACKWARD_AMX3"
- "KERNEL_GRU_FUSED_UPDATE_GATE_BACKWARD_AMX2"
- "KERNEL_GRU_FUSED_UPDATE_GATE_BACKWARD_AMX3"
- "KERNEL_MATMUL_ADD_FP32_AMX2"
- "KERNEL_MATMUL_AMX1"
- "KERNEL_MATMUL_AMX1_DYNAMIC"
- "KERNEL_MATMUL_AMX2"
- "KERNEL_MATMUL_AMX2_DYNAMIC"
- "KERNEL_MATMUL_AMX2_GRP_INT4"
- "KERNEL_MATMUL_AMX3"
- "KERNEL_MATMUL_AMX3_DKM_INT3"
- "KERNEL_MATMUL_AMX3_DYNAMIC"
- "KERNEL_MATMUL_AMX3_GRP_INT4"
- "KERNEL_MATMUL_AMX3_GRP_INT4_V2"
- "KERNEL_MATMUL_MUL_TO_MASK_ADD_BF16_FP32_AMX3"
- "KERNEL_MATMUL_MUL_TO_MASK_ADD_FP32_AMX2"
- "KERNEL_MGLM_MATMUL_2x2_INDEXED4_AMX3"
- "KERNEL_MGLM_MHA_PART0_V1_BF16_FP32_AMX3"
- "KERNEL_MGLM_MHA_PART1_V1_BF16_FP32_1x32x64_AMX3"
- "KERNEL_MGLM_MHA_V2_BF16_FP32_AMX3"
- "KERNEL_MUL_TO_MASK_MATMUL_ADD_BF16_FP32_AMX3"
- "KERNEL_MUL_TO_MASK_MATMUL_ADD_FP32_AMX2"
- "KERNEL_REDUCE_KERNELPOOL_WAVERNN_REDUCE_BATCH32_KERNEL0_AMX1_FP32"
- "KERNEL_REDUCE_KERNELPOOL_WAVERNN_REDUCE_BATCH32_KERNEL0_AMX2_FP32"
- "KERNEL_REDUCE_KERNELPOOL_WAVERNN_REDUCE_BATCH32_KERNEL0_AMX3_BF16"
- "KERNEL_REDUCE_KERNELPOOL_WAVERNN_REDUCE_BATCH32_KERNEL1_AMX1_FP32"
- "KERNEL_REDUCE_KERNELPOOL_WAVERNN_REDUCE_BATCH32_KERNEL1_AMX2_FP32"
- "KERNEL_REDUCE_KERNELPOOL_WAVERNN_REDUCE_BATCH32_KERNEL1_AMX3_BF16"
- "KERNEL_REDUCE_KERNELPOOL_WAVERNN_REDUCE_BATCH32_KERNEL2_AMX1_FP32"
- "KERNEL_REDUCE_KERNELPOOL_WAVERNN_REDUCE_BATCH32_KERNEL2_AMX2_FP32"
- "KERNEL_REDUCE_KERNELPOOL_WAVERNN_REDUCE_BATCH32_KERNEL2_AMX3_BF16"
- "KERNEL_REDUCE_KERNELPOOL_WAVERNN_REDUCE_BATCH32_KERNEL3_AMX1_FP32"
- "KERNEL_REDUCE_KERNELPOOL_WAVERNN_REDUCE_BATCH32_KERNEL3_AMX2_FP32"
- "KERNEL_REDUCE_KERNELPOOL_WAVERNN_REDUCE_BATCH32_KERNEL3_AMX3_BF16"
- "KERNEL_REDUCE_KERNELPOOL_WAVERNN_REDUCE_BATCH32_KERNEL4_AMX1_FP32"
- "KERNEL_REDUCE_KERNELPOOL_WAVERNN_REDUCE_BATCH32_KERNEL4_AMX2_FP32"
- "KERNEL_REDUCE_KERNELPOOL_WAVERNN_REDUCE_BATCH32_KERNEL4_AMX3_BF16"
- "User provided descriptor for tensor 0x%!l(MISSING)lx has data size %!z(MISSING)u but BNNS requires size >= %!l(MISSING)lu\n"
- "User provided pointer for tensor 0x%!l(MISSING)lx has size %!z(MISSING)u but BNNS requires size >= %!l(MISSING)lu\n"
- "User provided tensor for argument 0x%!l(MISSING)lx has data size %!z(MISSING)u but BNNS requires size >= %!l(MISSING)lu\n"
- "amx1"
- "amx2"
- "amx3"

```
