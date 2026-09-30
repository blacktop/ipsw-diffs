## ANECompiler

> `/System/Library/PrivateFrameworks/ANECompiler.framework/ANECompiler`

```diff

 8.2.17.0.0
-  __TEXT.__text: 0x11c3c38
+  __TEXT.__text: 0x11f4f98
   __TEXT.__auth_stubs: 0x20d0
   __TEXT.__init_offsets: 0x8
-  __TEXT.__const: 0x750ec
-  __TEXT.__cstring: 0x8c5e7
-  __TEXT.__gcc_except_tab: 0x6c424
-  __TEXT.__oslogstring: 0x15e07
-  __TEXT.__unwind_info: 0x38370
+  __TEXT.__const: 0x75f2c
+  __TEXT.__cstring: 0x90949
+  __TEXT.__gcc_except_tab: 0x6d1b4
+  __TEXT.__oslogstring: 0x15e6e
+  __TEXT.__unwind_info: 0x38a60
   __TEXT.__eh_frame: 0x11b4
   __DATA_CONST.__got: 0x1c8
   __DATA_CONST.__const: 0x3610
   __AUTH_CONST.__auth_got: 0x1070
   __AUTH_CONST.__auth_ptr: 0x80
-  __AUTH_CONST.__const: 0x71350
+  __AUTH_CONST.__const: 0x716c8
   __AUTH_CONST.__cfstring: 0x7f00
   __AUTH.__data: 0x3618
   __AUTH.__thread_vars: 0xf0
   __AUTH.__thread_bss: 0x16c
-  __DATA.__data: 0x6540
-  __DATA.__bss: 0x9ca0
+  __DATA.__data: 0x6838
+  __DATA.__bss: 0xad50
   __DATA.__common: 0x1558
   __DATA_DIRTY.__data: 0x80
   __DATA_DIRTY.__common: 0x38

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libncurses.5.4.dylib
-  Functions: 71287
-  Symbols:   83458
-  CStrings:  15467
+  Functions: 72322
+  Symbols:   84693
+  CStrings:  15620
 
CStrings:
+ "!(is_ne_instr && has_pe_count)"
+ "!(ox == 2 && oy == 2)"
+ "tile_dma_src2_cache_hint == ane_tile_dma_src_dma_config2_cache_hint_noalloc_v19 || tile_dma_src2_cache_hint == ane_tile_dma_src_dma_config2_cache_hint_alloc_v19 || tile_dma_src2_cache_hint == ane_tile_dma_src_dma_config2_cache_hint_depri_v19 || tile_dma_src2_cache_hint == ane_tile_dma_src_dma_config2_cache_hint_drop_v19"
+ "Assertion: Invalid Td header count given"
+ "hw.tile_dma_src_config.ane_tile_dma_src_config.tex_crop_cfg[i].src0 == ane_tile_dma_src_tex_crop_cfg_src0_bias_v19"
+ "Pause Duration has to be 0 if nothing to pause on"
+ "tile_dma_src.dma_config_ext.cache_hint_no_reuse != ane_tile_dma_src_dma_config_ext_cache_hint_no_reuse_drop_v19"
+ "hw.ne_config.ane_ne_config.mac_cfg.kernel_mode == ane_ne_mac_cfg_kernel_mode_kernel_v19"
+ "hw.common_config.ane_common_config.ne_cfg.ocg_size >= palette_block_size_log2"
+ "hw.l2_config.ane_l2_config.source1_cfg.bfr_mode == hw.tile_dma_src_config.ane_tile_dma_src_config.dma_config.l2_bfr_mode"
+ "tile_dma_src1_cache_hint_no_reuse == ane_tile_dma_src_dma_config_ext_cache_hint_no_reuse_noalloc_v19 || tile_dma_src1_cache_hint_no_reuse == ane_tile_dma_src_dma_config_ext_cache_hint_no_reuse_alloc_v19 || tile_dma_src1_cache_hint_no_reuse == ane_tile_dma_src_dma_config_ext_cache_hint_no_reuse_depri_v19 || tile_dma_src1_cache_hint_no_reuse == ane_tile_dma_src_dma_config_ext_cache_hint_no_reuse_drop_v19"
+ "/Library/Caches/com.apple.xbs/Sources/ANECompiler/libs/inference/compiler/ZinIrCodegen/src/ZinCodegen_v19.cpp"
+ "hw.tile_dma_src_config.ane_tile_dma_src_config.tex_idx.idx_permute_g == ane_tile_dma_src_tex_idx_idx_permute_g_zero_v19"
+ "hw.tile_dma_src_config.ane_tile_dma_src_config.tex_src.ind_permute_x == ane_tile_dma_src_tex_src_ind_permute_x_zero_v19"
+ "Throttle Duration has to be 0 if nothing to throttle on"
+ "hw.tile_dma_src_config.ane_tile_dma_src_config.dma_config2.cache_hint == ZinHWTraits<19>::ane_tile_dma_src_dma_config_cache_hint_noalloc"
+ "cache_dma_pre_config.throttle.on_tile_dma_dst || cache_dma_pre_config.throttle.on_tile_dma_src || cache_dma_pre_config.throttle.on_kernel_dma_src"
+ "hw.tile_dma_src_config.ane_tile_dma_src_config.dma_config_ext2 .cache_hint_reuse == ZinHWTraits<19>::ane_tile_dma_src_dma_config_cache_hint_reuse_noalloc"
+ "hw.common_config.ane_common_config.cfg.small_source_mode != ane_common_cfg_small_source_mode_ssm_v19"
+ "required_acc_regs_per_mac <= 32"
+ "kernel_config.non_linear_lutdma_config.cache_hint == ane_kernel_dma_src_non_linear_lutdma_config_cache_hint_noalloc_v19"
+ "hw.tile_dma_src_config.ane_tile_dma_src_config.dma_config_ext.cache_hint_no_reuse == ZinHWTraits<19>::ane_tile_dma_src_dma_config_cache_hint_no_reuse_noalloc"
+ "hw.common_config.ane_common_config.ch_cfg.src2_in_fmt == ane_common_ch_cfg_src2_in_fmt_fp16_v19"
+ "Disable DRAM Input FIFO: %!d(MISSING)\n"
+ "hw.kernel_dma_src_config.ane_kernel_dma_src_config.coeff_dma_config[i] .cache_hint == ZinHWTraits<19>::ane_tile_dma_src_dma_config_cache_hint_noalloc"
+ "tile_dma_src2_cache_hint_no_reuse == ane_tile_dma_src_dma_config_ext2_cache_hint_no_reuse_noalloc_v19 || tile_dma_src2_cache_hint_no_reuse == ane_tile_dma_src_dma_config_ext2_cache_hint_no_reuse_alloc_v19 || tile_dma_src2_cache_hint_no_reuse == ane_tile_dma_src_dma_config_ext2_cache_hint_no_reuse_depri_v19 || tile_dma_src2_cache_hint_no_reuse == ane_tile_dma_src_dma_config_ext2_cache_hint_no_reuse_drop_v19"
+ "(1 << (hw.ne_config.ane_ne_config.kernel_cfg.palettized_bits + hw.kernel_dma_src_config.ane_kernel_dma_src_config.kernel_config .palette_block_size + (hw.ne_config.ane_ne_config.kernel_cfg.kernel_fmt != ZinHWTraits<19>::ane_ne_kernel_cfg_kernel_fmt_fp16))) <= hal_params.ne_palette_lut_size_in_bytes"
+ "palette_block_size_log2 == 0"
+ "tile_dma_src.dma_config.cache_hint != ane_tile_dma_src_dma_config_cache_hint_drop_v19"
+ "bfr_sizes[ne_id] == ZinHWTraits<19>::limits_struct->ane_kernel_dma_src_coeff_bfr_size.first"
+ "hw.ne_config.ane_ne_config.mac_cfg.kernel_mode != ZinHWTraits<19>::ane_ne_mac_cfg_kernel_mode_unity"
+ "cache_dma_pre_config.pause.on_tile_dma_dst || cache_dma_pre_config.pause.on_tile_dma_src || cache_dma_pre_config.pause.on_kernel_dma_src"
+ "cons_tile_dma_src.dma_config_ext2.wrap_cfg == ane_tile_dma_src_dma_config_ext2_wrap_cfg_none_v19"
+ "hw.ne_config.ane_ne_config.mac_cfg.op_mode == ane_ne_mac_cfg_op_mode_conv_v19"
+ "(ssm == ane_common_cfg_small_source_mode_normal_v19) || (ssm > 1 && in_fmt < 2)"
+ "std::set<uint32_t>({ane_kernel_dma_src_post_scale_dma_config_cache_hint_noalloc_v19, ane_kernel_dma_src_post_scale_dma_config_cache_hint_alloc_v19, ane_kernel_dma_src_post_scale_dma_config_cache_hint_depri_v19, ane_kernel_dma_src_post_scale_dma_config_cache_hint_drop_v19}).contains( kernel_dma_src_post_scale_cache_hint)"
+ "kZinIrSuccess == get_mem_fmt_bytes(tile_dma_dst_intlv, tile_dma_dst_fmt_mode, mem_fmt_bytes)"
+ "(1 << (sh_pref + hw.common_config.ane_common_config.ne_cfg.wu_stack)) >= tile_height"
+ "hw.ne_config.ane_ne_config.kernel_cfg.asym_quant_en == 0"
+ "match_offset_lsbs( hw.l2_config.ane_l2_config.input_crop.src1_offset_y_lsbs, hw.tile_dma_src_config.ane_tile_dma_src_config.crop_offset2.offset_y, ANE_L2_INPUT_CROP_SRC1_OFFSET_Y_LSBS_WIDTH_V19)"
+ "Error: Invalid perf tracer configuration."
+ "hw.common_config.ane_common_config.pe_cfg.src2_broadcast_x == 0x0"
+ "kernel_config.palette_lutdma_config.cache_hint == ane_kernel_dma_src_palette_lutdma_config_cache_hint_noalloc_v19"
+ "hw.tile_dma_src_config.ane_tile_dma_src_config.tex_crop_cfg[i].src1 == ane_tile_dma_src_tex_crop_cfg_src1_bias_v19"
+ "hw.l2_config.ane_l2_config.source2_cfg.bfr_mode == hw.tile_dma_src_config.ane_tile_dma_src_config.dma_config.l2_bfr_mode"
+ "GetTensorFormatFromHwConfig<19>(hw, input_fmt)"
+ "tile_dma_src.dma_config_ext2.cache_hint_reuse != ane_tile_dma_src_dma_config_ext2_cache_hint_reuse_drop_v19"
+ "bias_mode == ZinHWTraits<19>::ane_ne_mac_cfg_bias_mode_const"
+ "ZinRegisterProgrammingAnalysis<19>::CalculateLinearDmaDstGranularityInX( hw, hal.dram_alignment, dma_x_granularity) == kZinIrSuccess"
+ "ZinIsEven( hw.l2_config.ane_l2_config.source1_cfg.dma_interleave - ZinCountOnes(hw.tile_dma_src_config.ane_tile_dma_src_config.fmt.cmp_vec))"
+ "hw.l2_config.ane_l2_config.source1_cfg.source_type == ane_l2_source1_cfg_source_type_resident_v19"
+ "hw.td_header8.trace_en == hw.common_config.ane_common_config.cfg.trace_en"
+ "!cache_dma_pre_config.throttle.on_tile_dma_dst && !cache_dma_pre_config.throttle.on_tile_dma_src && !cache_dma_pre_config.throttle.on_kernel_dma_src && cache_dma_pre_config.throttle.duration == 0 && cache_dma_pre_config.throttle.rate == 0"
+ "hw.common_config.ane_common_config.pe_cfg.src1_broadcast_y == 0x0"
+ "std::set<uint32_t>({ ane_kernel_dma_src_non_linear_lutdma_config_cache_hint_noalloc_v19, ane_kernel_dma_src_non_linear_lutdma_config_cache_hint_alloc_v19, ane_kernel_dma_src_non_linear_lutdma_config_cache_hint_drop_v19, ane_kernel_dma_src_non_linear_lutdma_config_cache_hint_depri_v19}).contains( kernel_dma_src_non_linear_lut_cache_hint)"
+ "kernel_mode == ane_ne_mac_cfg_kernel_mode_kernel_v19"
+ "hw.tile_dma_src_config.ane_tile_dma_src_config.tex_src.src_permute_c == ane_tile_dma_src_tex_src_src_permute_c_zero_v19"
+ "input_src2_dma_x_granularity <= input_l2_x_granularity"
+ "match_offset_lsbs( hw.l2_config.ane_l2_config.input_crop.src2_offset_x_lsbs, hw.tile_dma_src_config.ane_tile_dma_src_config.crop_offset2.offset_x, ANE_L2_INPUT_CROP_SRC2_OFFSET_X_LSBS_WIDTH_V19)"
+ "hw.l2_config.ane_l2_config.source2_cfg.bfr_mode == hw.tile_dma_src_config.ane_tile_dma_src_config.dma_config2.l2_bfr_mode"
+ "hw.ne_config.ane_ne_config.kernel_cfg.palette_block_size == hw.kernel_dma_src_config.ane_kernel_dma_src_config.kernel_config.palette_block_size"
+ "post_scale_mode == ZinHWTraits<19>::ane_ne_mac_cfg_post_scale_mode_const"
+ "cons_tile_dma_src.dma_config_ext.wrap_cfg == ane_tile_dma_src_dma_config_ext_wrap_cfg_none_v19"
+ "hw.tile_dma_src_config.ane_tile_dma_src_config.tex_idx.idx_permute_x == ane_tile_dma_src_tex_idx_idx_permute_x_zero_v19"
+ "hw.tile_dma_src_config.ane_tile_dma_src_config.dma_config.dependency_mode != ZinHWTraits<19>::ane_tile_dma_src_dma_config_dependency_mode_notdep"
+ "hw.tile_dma_src_config.ane_tile_dma_src_config.tex_src.src_permute_z == ane_tile_dma_src_tex_src_src_permute_z_zero_v19"
+ "hw.tile_dma_src_config.ane_tile_dma_src_config.tex_src.src_permute_x == ane_tile_dma_src_tex_src_src_permute_x_zero_v19"
+ "hw.common_config.ane_common_config.pe_cfg.src1_wto_c == 0x0"
+ "hw.tile_dma_src_config.ane_tile_dma_src_config.tex_crop_cfg[i].scale1 == ane_tile_dma_src_tex_crop_cfg_scale1_one_v19"
+ "hw.tile_dma_src_config.ane_tile_dma_src_config.tex_src.ind_permute_z == ane_tile_dma_src_tex_src_ind_permute_z_zero_v19"
+ "skd == 1 || !double_int8"
+ "std::set<uint32_t>({ane_kernel_dma_src_palette_lutdma_config_cache_hint_noalloc_v19, ane_kernel_dma_src_palette_lutdma_config_cache_hint_alloc_v19, ane_kernel_dma_src_palette_lutdma_config_cache_hint_drop_v19, ane_kernel_dma_src_palette_lutdma_config_cache_hint_depri_v19}).contains( kernel_dma_src_palette_lut_cache_hint)"
+ "tile_dma_src.dma_config2.cache_hint != ane_tile_dma_src_dma_config2_cache_hint_drop_v19"
+ "t8140"
+ "sh_pref == hw.common_config.ane_common_config.cfg.sh_max"
+ "hw.common_config.ane_common_config.pe_cfg.src1_broadcast_z == 0x0"
+ "match_offset_lsbs( hw.l2_config.ane_l2_config.input_crop.src1_offset_x_lsbs, hw.tile_dma_src_config.ane_tile_dma_src_config.crop_offset2.offset_x, ANE_L2_INPUT_CROP_SRC1_OFFSET_X_LSBS_WIDTH_V19)"
+ "Error: Invalid perf trace given"
+ "h17a"
+ "hw.common_config.ane_common_config.pe_cfg.src2_broadcast_c == 0x0"
+ "hw.tile_dma_src_config.ane_tile_dma_src_config.tex_idx.idx_permute_p == ane_tile_dma_src_tex_idx_idx_permute_p_zero_v19"
+ "kernel_dma_src_coeff_cache_hint == ane_kernel_dma_src_coeff_dma_config_cache_hint_noalloc_v19 || kernel_dma_src_coeff_cache_hint == ane_kernel_dma_src_coeff_dma_config_cache_hint_alloc_v19 || kernel_dma_src_coeff_cache_hint == ane_kernel_dma_src_coeff_dma_config_cache_hint_depri_v19 || kernel_dma_src_coeff_cache_hint == ane_kernel_dma_src_coeff_dma_config_cache_hint_drop_v19"
+ "tile_dma_src.dma_config_ext2.cache_hint_no_reuse != ane_tile_dma_src_dma_config_ext2_cache_hint_no_reuse_drop_v19"
+ "(1 << (hw.common_config.ane_common_config.ne_cfg.ocg_size + hw.common_config.ane_common_config.cfg.active_ne)) >= hw.common_config.ane_common_config.cout.fld"
+ "tile_dma_src1_cache_hint == ane_tile_dma_src_dma_config_cache_hint_noalloc_v19 || tile_dma_src1_cache_hint == ane_tile_dma_src_dma_config_cache_hint_alloc_v19 || tile_dma_src1_cache_hint == ane_tile_dma_src_dma_config_cache_hint_depri_v19 || tile_dma_src1_cache_hint == ane_tile_dma_src_dma_config_cache_hint_drop_v19"
+ "ZinIsEven(hw.tile_dma_src_config.ane_tile_dma_src_config.fmt.offset_ch)"
+ "task_type != ane_common_cfg_task_type_pe_ternary_v19"
+ "std::count(counts.begin(), counts.end(), pop) == 1 || pop == 0x00"
+ "Illegal Prefetch Rate"
+ "hw.tile_dma_src_config.ane_tile_dma_src_config.tex_src.ind_permute_c == ane_tile_dma_src_tex_src_ind_permute_c_zero_v19"
+ "cto_w == 0x0"
+ "Invalid perf trace given"
+ "(kw == 3 && sx == 1) || (kw == 5 && sx == 2) || (kw == 6 && sx == 2)"
+ "input_src1_dma_x_granularity <= input_l2_x_granularity"
+ "h17"
+ "cache_dma_pre_config.dma_config.cache_hint == ane_cache_dma_pre_dma_config_cache_hint_alloc_v19"
+ "hw.ne_config.ane_ne_config.kernel_cfg.palettized_bits == ane_ne_kernel_cfg_palettized_bits_bit8_v19"
+ "tile_dma_src2_cache_hint_reuse == ane_tile_dma_src_dma_config_ext2_cache_hint_reuse_noalloc_v19 || tile_dma_src2_cache_hint_reuse == ane_tile_dma_src_dma_config_ext2_cache_hint_reuse_alloc_v19 || tile_dma_src2_cache_hint_reuse == ane_tile_dma_src_dma_config_ext2_cache_hint_reuse_depri_v19 || tile_dma_src2_cache_hint_reuse == ane_tile_dma_src_dma_config_ext2_cache_hint_reuse_drop_v19"
+ "fill_lower_ne_first"
+ "hw.tile_dma_src_config.ane_tile_dma_src_config.dma_config_ext2 .cache_hint_no_reuse == ZinHWTraits<19>::ane_tile_dma_src_dma_config_cache_hint_no_reuse_noalloc"
+ "task_type != ane_common_cfg_task_type_pe_binary_pooling_v19"
+ "skh <= 5"
+ "hw.common_config.ane_common_config.pe_cfg.src2_broadcast_z == 0x0"
+ "kernel_config.bias_dma_config.cache_hint == ane_kernel_dma_src_bias_dma_config_cache_hint_noalloc_v19"
+ "std::set<uint32_t>({ane_kernel_dma_src_bias_dma_config_cache_hint_noalloc_v19, ane_kernel_dma_src_bias_dma_config_cache_hint_alloc_v19, ane_kernel_dma_src_bias_dma_config_cache_hint_depri_v19, ane_kernel_dma_src_bias_dma_config_cache_hint_drop_v19}).contains( kernel_dma_src_bias_cache_hint)"
+ "hw.common_config.ane_common_config.pe_cfg.src1_broadcast_c == 0x0"
+ "Illegal Throttle Rate"
+ "tile_dma_dst_cache_hint == ane_tile_dma_dst_dma_config_cache_hint_noalloc_v19 || tile_dma_dst_cache_hint == ane_tile_dma_dst_dma_config_cache_hint_alloc_v19 || tile_dma_dst_cache_hint == ane_tile_dma_dst_dma_config_cache_hint_depri_v19"
+ "hw.tile_dma_src_config.ane_tile_dma_src_config.tex_idx.idx_permute_y == ane_tile_dma_src_tex_idx_idx_permute_y_zero_v19"
+ "!(is_pe_instr && has_ne_count)"
+ "hw.tile_dma_dst_config.ane_tile_dma_dst_config.dma_config.cache_hint == ane_tile_dma_dst_dma_config_cache_hint_noalloc_v19"
+ "hw.tile_dma_src_config.ane_tile_dma_src_config.tex_src.src_permute_g == ane_tile_dma_src_tex_src_src_permute_g_zero_v19"
+ "small_source_mode != ane_common_cfg_small_source_mode_np2_10_v19 && small_source_mode != ane_common_cfg_small_source_mode_np2_6_v19"
+ "match_offset_lsbs( hw.l2_config.ane_l2_config.input_crop.src1_offset_x_lsbs, hw.tile_dma_src_config.ane_tile_dma_src_config.crop_offset.offset_x, ANE_L2_INPUT_CROP_SRC1_OFFSET_X_LSBS_WIDTH_V19)"
+ "hw.ne_config.ane_ne_config.mac_cfg.kernel_mode == ZinHWTraits<19>::ane_ne_mac_cfg_kernel_mode_kernel"
+ "hw.ne_config.ane_ne_config.kernel_cfg.alignment_fmt == ane_ne_kernel_cfg_alignment_fmt_aligned_v19"
+ "tile_dma_src1_cache_hint_reuse == ane_tile_dma_src_dma_config_ext_cache_hint_reuse_noalloc_v19 || tile_dma_src1_cache_hint_reuse == ane_tile_dma_src_dma_config_ext_cache_hint_reuse_alloc_v19 || tile_dma_src1_cache_hint_reuse == ane_tile_dma_src_dma_config_ext_cache_hint_reuse_depri_v19 || tile_dma_src1_cache_hint_reuse == ane_tile_dma_src_dma_config_ext_cache_hint_reuse_drop_v19"
+ "kernel_mode == ZinHWTraits<19>::ane_ne_mac_cfg_kernel_mode_unity"
+ "ne_round_cfg.mode == ane_ne_round_cfg_mode_disable_v19"
+ "!cache_dma_pre_config.pause.on_tile_dma_dst && !cache_dma_pre_config.pause.on_tile_dma_src && !cache_dma_pre_config.pause.on_kernel_dma_src && cache_dma_pre_config.pause.duration == 0"
+ "in_fmt != ZinHWTraits<19>::ane_common_ch_cfg_in_fmt_bf16"
+ "hw.tile_dma_src_config.ane_tile_dma_src_config.tex_idx.idx_permute_z == ane_tile_dma_src_tex_idx_idx_permute_z_zero_v19"
+ "tile_dma_src.dma_config_ext.cache_hint_reuse != ane_tile_dma_src_dma_config_ext_cache_hint_reuse_drop_v19"
+ "cons_tile_dma_src.tex_cfg.mode == ane_tile_dma_src_tex_cfg_mode_disabled_v19"
+ "hw.ne_config.ane_ne_config.kernel_cfg.kernel_fmt != ane_ne_kernel_cfg_kernel_fmt_uint8_v19"
+ "hw.tile_dma_src_config.ane_tile_dma_src_config.tex_crop_cfg[i].scale0 == ane_tile_dma_src_tex_crop_cfg_scale0_one_v19"
+ "hw.tile_dma_src_config.ane_tile_dma_src_config.dma_config.cache_hint == ZinHWTraits<19>::ane_tile_dma_src_dma_config_cache_hint_noalloc"
+ "hw.common_config.ane_common_config.cfg.small_source_mode == ane_common_cfg_small_source_mode_normal_v19"
+ "hw.common_config.ane_common_config.pe_cfg.src2_broadcast_y == 0x0"
+ "hw.common_config.ane_common_config.ch_cfg.in_fmt == ZinHWTraits<19>::ane_common_ch_cfg_in_fmt_uint8 || hw.common_config.ane_common_config.ch_cfg.in_fmt == ZinHWTraits<19>::ane_common_ch_cfg_in_fmt_sint8"
+ "hw.tile_dma_src_config.ane_tile_dma_src_config.tex_src.src_permute_y == ane_tile_dma_src_tex_src_src_permute_y_zero_v19"
+ "legal_fifo"
+ "match_offset_lsbs( hw.l2_config.ane_l2_config.input_crop.src1_offset_y_lsbs, hw.tile_dma_src_config.ane_tile_dma_src_config.crop_offset.offset_y, ANE_L2_INPUT_CROP_SRC1_OFFSET_Y_LSBS_WIDTH_V19)"
+ "hw.tile_dma_src_config.ane_tile_dma_src_config.tex_src.ind_permute_y == ane_tile_dma_src_tex_src_ind_permute_y_zero_v19"
+ "hw.ne_config.ane_ne_config.kernel_cfg.kernel_fmt != ZinHWTraits<19>::ane_ne_kernel_cfg_kernel_fmt_fp16"
+ "palette_block_size_log2 == hw.ne_config.ane_ne_config.kernel_cfg.sparse_block_size"
+ "hw.common_config.ane_common_config.pe_cfg.src2_wto_c == 0x0"
+ "hw.common_config.ane_common_config.cfg.fill_lower_ne_first == 0x1"
+ "kernel_config.post_scale_dma_config.cache_hint == ane_kernel_dma_src_post_scale_dma_config_cache_hint_noalloc_v19"
+ "hw.tile_dma_src_config.ane_tile_dma_src_config.tex_src.ind_permute_g == ane_tile_dma_src_tex_src_ind_permute_g_zero_v19"
+ "(1 << hw.common_config.ane_common_config.patch_cfg.patch_height) >= tile_height"
+ "match_offset_lsbs( hw.l2_config.ane_l2_config.input_crop.src2_offset_y_lsbs, hw.tile_dma_src_config.ane_tile_dma_src_config.crop_offset2.offset_y, ANE_L2_INPUT_CROP_SRC2_OFFSET_Y_LSBS_WIDTH_V19)"
+ "op_mode == ZinHWTraits<19>::ane_ne_mac_cfg_op_mode_conv"
+ "hw.ne_config.ane_ne_config.kernel_cfg.sparse_fmt == 0 || (!double_int8 && in_fmt != ane_common_ch_cfg_in_fmt_fp16_v19) || hw.ne_config.ane_ne_config.kernel_cfg.detect_zeros == 1"
+ "sh_pref == hw.common_config.ane_common_config.cfg.sh_min"
+ "hw.ne_config.ane_ne_config.kernel_cfg.asym_quant_en == 0x0"
+ "hw.tile_dma_src_config.ane_tile_dma_src_config.dma_config_ext.cache_hint_reuse == ZinHWTraits<19>::ane_tile_dma_src_dma_config_cache_hint_reuse_noalloc"
+ "required_acc_regs_per_mac <= 16"
+ "hw.common_config.ane_common_config.pe_cfg.src1_broadcast_x == 0x0"
+ "required_acc_regs_per_mac <= 8"
+ "hw.ne_config.ane_ne_config.mac_cfg.op_mode == ane_ne_mac_cfg_op_mode_bypass_v19"
+ "prod_tile_dma_dst.dma_config_ext.wrap_cfg == ane_tile_dma_dst_dma_config_ext_wrap_cfg_none_v19"

```
