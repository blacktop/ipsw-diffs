## ANECompiler

> `/System/Library/PrivateFrameworks/ANECompiler.framework/ANECompiler`

```diff

-8.3.2.0.0
-  __TEXT.__text: 0x11c70cc
-  __TEXT.__auth_stubs: 0x20f0
+8.3.5.0.0
+  __TEXT.__text: 0x11fdf8c
+  __TEXT.__auth_stubs: 0x20d0
   __TEXT.__init_offsets: 0x8
-  __TEXT.__const: 0x7577c
-  __TEXT.__cstring: 0x8c7fe
-  __TEXT.__gcc_except_tab: 0x6c74c
-  __TEXT.__oslogstring: 0x15e6e
-  __TEXT.__unwind_info: 0x38410
+  __TEXT.__const: 0x778bc
+  __TEXT.__cstring: 0x90ca6
+  __TEXT.__gcc_except_tab: 0x6da28
+  __TEXT.__oslogstring: 0x15f27
+  __TEXT.__unwind_info: 0x38c48
   __TEXT.__eh_frame: 0x11b4
   __DATA_CONST.__got: 0x1c8
-  __DATA_CONST.__const: 0x3618
-  __AUTH_CONST.__auth_got: 0x1080
+  __DATA_CONST.__const: 0x3620
+  __AUTH_CONST.__auth_got: 0x1070
   __AUTH_CONST.__auth_ptr: 0x80
-  __AUTH_CONST.__const: 0x71650
+  __AUTH_CONST.__const: 0x71f68
   __AUTH_CONST.__cfstring: 0x7f20
   __AUTH.__data: 0x3618
   __AUTH.__thread_vars: 0xf0
   __AUTH.__thread_bss: 0x16c
-  __DATA.__data: 0x6548
-  __DATA.__bss: 0x9cc8
+  __DATA.__data: 0x6840
+  __DATA.__bss: 0xad50
   __DATA.__common: 0x1558
   __DATA_DIRTY.__data: 0x80
   __DATA_DIRTY.__common: 0x38

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libncurses.5.4.dylib
-  Functions: 71346
-  Symbols:   83517
-  CStrings:  15481
+  Functions: 72494
+  Symbols:   84872
+  CStrings:  15651
 
Symbols:
- __ZNSt3__14__fs10filesystem8__statusERKNS1_4pathEPNS_10error_codeE
- __ZNSt3__14__fs10filesystem11__file_sizeERKNS1_4pathEPNS_10error_codeE
CStrings:
+ "match_offset_lsbs( hw.l2_config.ane_l2_config.input_crop.src1_offset_x_lsbs, hw.tile_dma_src_config.ane_tile_dma_src_config.crop_offset.offset_x, ANE_L2_INPUT_CROP_SRC1_OFFSET_X_LSBS_WIDTH_V19)"
+ "tile_dma_src.dma_config_ext.cache_hint_reuse != ane_tile_dma_src_dma_config_ext_cache_hint_reuse_drop_v19"
+ "Error: invalid lut indices format %!s(MISSING)."
+ "hw.common_config.ane_common_config.cfg.fill_lower_ne_first == 0x1"
+ "Invalid perf trace given"
+ "hw.kernel_dma_src_config.ane_kernel_dma_src_config.coeff_dma_config[i] .cache_hint == ZinHWTraits<19>::ane_tile_dma_src_dma_config_cache_hint_noalloc"
+ "hw.ne_config.ane_ne_config.kernel_cfg.asym_quant_en == 0"
+ "small_source_mode != ane_common_cfg_small_source_mode_np2_10_v19 && small_source_mode != ane_common_cfg_small_source_mode_np2_6_v19"
+ "Illegal Throttle Rate"
+ "hw.tile_dma_src_config.ane_tile_dma_src_config.dma_config_ext.cache_hint_no_reuse == ZinHWTraits<19>::ane_tile_dma_src_dma_config_cache_hint_no_reuse_noalloc"
+ "Final"
+ "tile_dma_src2_cache_hint == ane_tile_dma_src_dma_config2_cache_hint_noalloc_v19 || tile_dma_src2_cache_hint == ane_tile_dma_src_dma_config2_cache_hint_alloc_v19 || tile_dma_src2_cache_hint == ane_tile_dma_src_dma_config2_cache_hint_depri_v19 || tile_dma_src2_cache_hint == ane_tile_dma_src_dma_config2_cache_hint_drop_v19"
+ "hw.ne_config.ane_ne_config.kernel_cfg.kernel_fmt != ane_ne_kernel_cfg_kernel_fmt_uint8_v19"
+ "match_offset_lsbs( hw.l2_config.ane_l2_config.input_crop.src1_offset_y_lsbs, hw.tile_dma_src_config.ane_tile_dma_src_config.crop_offset2.offset_y, ANE_L2_INPUT_CROP_SRC1_OFFSET_Y_LSBS_WIDTH_V19)"
+ "hw.tile_dma_src_config.ane_tile_dma_src_config.tex_idx.idx_permute_p == ane_tile_dma_src_tex_idx_idx_permute_p_zero_v19"
+ "_lut_indices__@gather"
+ "(1 << hw.common_config.ane_common_config.patch_cfg.patch_height) >= tile_height"
+ "hw.tile_dma_src_config.ane_tile_dma_src_config.tex_src.src_permute_y == ane_tile_dma_src_tex_src_src_permute_y_zero_v19"
+ "hw.ne_config.ane_ne_config.mac_cfg.op_mode == ane_ne_mac_cfg_op_mode_bypass_v19"
+ "h17a"
+ ".MemoryPressure.debug.txt"
+ "required_acc_regs_per_mac <= 8"
+ "input_src2_dma_x_granularity <= input_l2_x_granularity"
+ "std::set<uint32_t>({ane_kernel_dma_src_post_scale_dma_config_cache_hint_noalloc_v19, ane_kernel_dma_src_post_scale_dma_config_cache_hint_alloc_v19, ane_kernel_dma_src_post_scale_dma_config_cache_hint_depri_v19, ane_kernel_dma_src_post_scale_dma_config_cache_hint_drop_v19}).contains( kernel_dma_src_post_scale_cache_hint)"
+ ".CpAllocWithDramInplace."
+ "invalid tensor format"
+ "match_offset_lsbs( hw.l2_config.ane_l2_config.input_crop.src1_offset_x_lsbs, hw.tile_dma_src_config.ane_tile_dma_src_config.crop_offset2.offset_x, ANE_L2_INPUT_CROP_SRC1_OFFSET_X_LSBS_WIDTH_V19)"
+ "_shifted_indices"
+ "kernel_config.non_linear_lutdma_config.cache_hint == ane_kernel_dma_src_non_linear_lutdma_config_cache_hint_noalloc_v19"
+ "!cache_dma_pre_config.throttle.on_tile_dma_dst && !cache_dma_pre_config.throttle.on_tile_dma_src && !cache_dma_pre_config.throttle.on_kernel_dma_src && cache_dma_pre_config.throttle.duration == 0 && cache_dma_pre_config.throttle.rate == 0"
+ "hw.tile_dma_src_config.ane_tile_dma_src_config.tex_src.ind_permute_y == ane_tile_dma_src_tex_src_ind_permute_y_zero_v19"
+ "tile_dma_src1_cache_hint_no_reuse == ane_tile_dma_src_dma_config_ext_cache_hint_no_reuse_noalloc_v19 || tile_dma_src1_cache_hint_no_reuse == ane_tile_dma_src_dma_config_ext_cache_hint_no_reuse_alloc_v19 || tile_dma_src1_cache_hint_no_reuse == ane_tile_dma_src_dma_config_ext_cache_hint_no_reuse_depri_v19 || tile_dma_src1_cache_hint_no_reuse == ane_tile_dma_src_dma_config_ext_cache_hint_no_reuse_drop_v19"
+ "hw.ne_config.ane_ne_config.mac_cfg.kernel_mode == ZinHWTraits<19>::ane_ne_mac_cfg_kernel_mode_kernel"
+ "tile_dma_src1_cache_hint_reuse == ane_tile_dma_src_dma_config_ext_cache_hint_reuse_noalloc_v19 || tile_dma_src1_cache_hint_reuse == ane_tile_dma_src_dma_config_ext_cache_hint_reuse_alloc_v19 || tile_dma_src1_cache_hint_reuse == ane_tile_dma_src_dma_config_ext_cache_hint_reuse_depri_v19 || tile_dma_src1_cache_hint_reuse == ane_tile_dma_src_dma_config_ext_cache_hint_reuse_drop_v19"
+ "skh <= 5"
+ "tile_dma_dst_cache_hint == ane_tile_dma_dst_dma_config_cache_hint_noalloc_v19 || tile_dma_dst_cache_hint == ane_tile_dma_dst_dma_config_cache_hint_alloc_v19 || tile_dma_dst_cache_hint == ane_tile_dma_dst_dma_config_cache_hint_depri_v19"
+ "hw.common_config.ane_common_config.pe_cfg.src1_broadcast_y == 0x0"
+ "hw.tile_dma_src_config.ane_tile_dma_src_config.tex_idx.idx_permute_g == ane_tile_dma_src_tex_idx_idx_permute_g_zero_v19"
+ "Pause Duration has to be 0 if nothing to pause on"
+ "_lut__@gather"
+ "_indices__@const"
+ "ZinIsEven(hw.tile_dma_src_config.ane_tile_dma_src_config.fmt.offset_ch)"
+ "hw.ne_config.ane_ne_config.kernel_cfg.palettized_bits == ane_ne_kernel_cfg_palettized_bits_bit8_v19"
+ "std::set<uint32_t>({ane_kernel_dma_src_palette_lutdma_config_cache_hint_noalloc_v19, ane_kernel_dma_src_palette_lutdma_config_cache_hint_alloc_v19, ane_kernel_dma_src_palette_lutdma_config_cache_hint_drop_v19, ane_kernel_dma_src_palette_lutdma_config_cache_hint_depri_v19}).contains( kernel_dma_src_palette_lut_cache_hint)"
+ "hw.tile_dma_src_config.ane_tile_dma_src_config.dma_config_ext.cache_hint_reuse == ZinHWTraits<19>::ane_tile_dma_src_dma_config_cache_hint_reuse_noalloc"
+ "kernel_mode == ane_ne_mac_cfg_kernel_mode_kernel_v19"
+ "_shifted_indices__@gather"
+ "hw.tile_dma_src_config.ane_tile_dma_src_config.tex_src.ind_permute_z == ane_tile_dma_src_tex_src_ind_permute_z_zero_v19"
+ "sh_pref == hw.common_config.ane_common_config.cfg.sh_max"
+ "quant_2"
+ "kernel_dma_src_coeff_cache_hint == ane_kernel_dma_src_coeff_dma_config_cache_hint_noalloc_v19 || kernel_dma_src_coeff_cache_hint == ane_kernel_dma_src_coeff_dma_config_cache_hint_alloc_v19 || kernel_dma_src_coeff_cache_hint == ane_kernel_dma_src_coeff_dma_config_cache_hint_depri_v19 || kernel_dma_src_coeff_cache_hint == ane_kernel_dma_src_coeff_dma_config_cache_hint_drop_v19"
+ "task_type != ane_common_cfg_task_type_pe_binary_pooling_v19"
+ "hw.common_config.ane_common_config.pe_cfg.src1_wto_c == 0x0"
+ "hw.common_config.ane_common_config.pe_cfg.src2_broadcast_z == 0x0"
+ "hw.ne_config.ane_ne_config.kernel_cfg.alignment_fmt == ane_ne_kernel_cfg_alignment_fmt_aligned_v19"
+ "hw.tile_dma_src_config.ane_tile_dma_src_config.tex_src.ind_permute_g == ane_tile_dma_src_tex_src_ind_permute_g_zero_v19"
+ "tile_dma_src.dma_config_ext2.cache_hint_no_reuse != ane_tile_dma_src_dma_config_ext2_cache_hint_no_reuse_drop_v19"
+ "op_mode == ZinHWTraits<19>::ane_ne_mac_cfg_op_mode_conv"
+ "hw.tile_dma_src_config.ane_tile_dma_src_config.tex_src.ind_permute_x == ane_tile_dma_src_tex_src_ind_permute_x_zero_v19"
+ "Assertion: Invalid Td header count given"
+ "cons_tile_dma_src.tex_cfg.mode == ane_tile_dma_src_tex_cfg_mode_disabled_v19"
+ "hw.tile_dma_src_config.ane_tile_dma_src_config.tex_idx.idx_permute_y == ane_tile_dma_src_tex_idx_idx_permute_y_zero_v19"
+ "_lut__@const"
+ "Error: the number of cout (%!d(MISSING)) must be divisible by the number of LUTs (%!d(MISSING))"
+ "sh_pref == hw.common_config.ane_common_config.cfg.sh_min"
+ "hw.common_config.ane_common_config.pe_cfg.src1_broadcast_c == 0x0"
+ "hw.common_config.ane_common_config.ch_cfg.src2_in_fmt == ane_common_ch_cfg_src2_in_fmt_fp16_v19"
+ "ne_round_cfg.mode == ane_ne_round_cfg_mode_disable_v19"
+ "hw.td_header8.trace_en == hw.common_config.ane_common_config.cfg.trace_en"
+ "ZinIsEven( hw.l2_config.ane_l2_config.source1_cfg.dma_interleave - ZinCountOnes(hw.tile_dma_src_config.ane_tile_dma_src_config.fmt.cmp_vec))"
+ "kernel_config.post_scale_dma_config.cache_hint == ane_kernel_dma_src_post_scale_dma_config_cache_hint_noalloc_v19"
+ "hw.tile_dma_src_config.ane_tile_dma_src_config.tex_src.src_permute_z == ane_tile_dma_src_tex_src_src_permute_z_zero_v19"
+ "dequant_2"
+ "hw.ne_config.ane_ne_config.kernel_cfg.sparse_fmt == 0 || (!double_int8 && in_fmt != ane_common_ch_cfg_in_fmt_fp16_v19) || hw.ne_config.ane_ne_config.kernel_cfg.detect_zeros == 1"
+ "!(is_pe_instr && has_ne_count)"
+ "(ssm == ane_common_cfg_small_source_mode_normal_v19) || (ssm > 1 && in_fmt < 2)"
+ "match_offset_lsbs( hw.l2_config.ane_l2_config.input_crop.src1_offset_y_lsbs, hw.tile_dma_src_config.ane_tile_dma_src_config.crop_offset.offset_y, ANE_L2_INPUT_CROP_SRC1_OFFSET_Y_LSBS_WIDTH_V19)"
+ "kernel_mode == ZinHWTraits<19>::ane_ne_mac_cfg_kernel_mode_unity"
+ "h17"
+ "required_acc_regs_per_mac <= 16"
+ "kernel_config.bias_dma_config.cache_hint == ane_kernel_dma_src_bias_dma_config_cache_hint_noalloc_v19"
+ "!(ox == 2 && oy == 2)"
+ "in_fmt != ZinHWTraits<19>::ane_common_ch_cfg_in_fmt_bf16"
+ "hw.common_config.ane_common_config.cfg.small_source_mode != ane_common_cfg_small_source_mode_ssm_v19"
+ "hw.tile_dma_src_config.ane_tile_dma_src_config.tex_src.src_permute_g == ane_tile_dma_src_tex_src_src_permute_g_zero_v19"
+ "std::set<uint32_t>({ ane_kernel_dma_src_non_linear_lutdma_config_cache_hint_noalloc_v19, ane_kernel_dma_src_non_linear_lutdma_config_cache_hint_alloc_v19, ane_kernel_dma_src_non_linear_lutdma_config_cache_hint_drop_v19, ane_kernel_dma_src_non_linear_lutdma_config_cache_hint_depri_v19}).contains( kernel_dma_src_non_linear_lut_cache_hint)"
+ "cons_tile_dma_src.dma_config_ext2.wrap_cfg == ane_tile_dma_src_dma_config_ext2_wrap_cfg_none_v19"
+ "hw.l2_config.ane_l2_config.source1_cfg.source_type == ane_l2_source1_cfg_source_type_resident_v19"
+ "hw.tile_dma_src_config.ane_tile_dma_src_config.tex_src.src_permute_x == ane_tile_dma_src_tex_src_src_permute_x_zero_v19"
+ "palette_block_size_log2 == 0"
+ "!(is_ne_instr && has_pe_count)"
+ "hw.tile_dma_src_config.ane_tile_dma_src_config.tex_idx.idx_permute_x == ane_tile_dma_src_tex_idx_idx_permute_x_zero_v19"
+ "hw.ne_config.ane_ne_config.mac_cfg.op_mode == ane_ne_mac_cfg_op_mode_conv_v19"
+ "hw.ne_config.ane_ne_config.kernel_cfg.asym_quant_en == 0x0"
+ "hw.tile_dma_src_config.ane_tile_dma_src_config.tex_crop_cfg[i].scale1 == ane_tile_dma_src_tex_crop_cfg_scale1_one_v19"
+ "std::count(counts.begin(), counts.end(), pop) == 1 || pop == 0x00"
+ "hw.l2_config.ane_l2_config.source2_cfg.bfr_mode == hw.tile_dma_src_config.ane_tile_dma_src_config.dma_config2.l2_bfr_mode"
+ "cache_dma_pre_config.dma_config.cache_hint == ane_cache_dma_pre_dma_config_cache_hint_alloc_v19"
+ "hw.common_config.ane_common_config.pe_cfg.src1_broadcast_x == 0x0"
+ "skd == 1 || !double_int8"
+ "hw.common_config.ane_common_config.ne_cfg.ocg_size >= palette_block_size_log2"
+ "hw.tile_dma_src_config.ane_tile_dma_src_config.tex_crop_cfg[i].src1 == ane_tile_dma_src_tex_crop_cfg_src1_bias_v19"
+ "(1 << (hw.common_config.ane_common_config.ne_cfg.ocg_size + hw.common_config.ane_common_config.cfg.active_ne)) >= hw.common_config.ane_common_config.cout.fld"
+ "hw.common_config.ane_common_config.ch_cfg.in_fmt == ZinHWTraits<19>::ane_common_ch_cfg_in_fmt_uint8 || hw.common_config.ane_common_config.ch_cfg.in_fmt == ZinHWTraits<19>::ane_common_ch_cfg_in_fmt_sint8"
+ "task_type != ane_common_cfg_task_type_pe_ternary_v19"
+ "hw.tile_dma_src_config.ane_tile_dma_src_config.dma_config2.cache_hint == ZinHWTraits<19>::ane_tile_dma_src_dma_config_cache_hint_noalloc"
+ "(1 << (sh_pref + hw.common_config.ane_common_config.ne_cfg.wu_stack)) >= tile_height"
+ "quant_1"
+ "GetTensorFormatFromHwConfig<19>(hw, input_fmt)"
+ "hw.tile_dma_src_config.ane_tile_dma_src_config.dma_config.dependency_mode != ZinHWTraits<19>::ane_tile_dma_src_dma_config_dependency_mode_notdep"
+ "palette_block_size_log2 == hw.ne_config.ane_ne_config.kernel_cfg.sparse_block_size"
+ "hw.ne_config.ane_ne_config.kernel_cfg.kernel_fmt != ZinHWTraits<19>::ane_ne_kernel_cfg_kernel_fmt_fp16"
+ "hw.tile_dma_src_config.ane_tile_dma_src_config.tex_crop_cfg[i].src0 == ane_tile_dma_src_tex_crop_cfg_src0_bias_v19"
+ "tile_dma_src.dma_config_ext2.cache_hint_reuse != ane_tile_dma_src_dma_config_ext2_cache_hint_reuse_drop_v19"
+ "hw.tile_dma_dst_config.ane_tile_dma_dst_config.dma_config.cache_hint == ane_tile_dma_dst_dma_config_cache_hint_noalloc_v19"
+ "cons_tile_dma_src.dma_config_ext.wrap_cfg == ane_tile_dma_src_dma_config_ext_wrap_cfg_none_v19"
+ "hw.common_config.ane_common_config.pe_cfg.src1_broadcast_z == 0x0"
+ "bfr_sizes[ne_id] == ZinHWTraits<19>::limits_struct->ane_kernel_dma_src_coeff_bfr_size.first"
+ "match_offset_lsbs( hw.l2_config.ane_l2_config.input_crop.src2_offset_x_lsbs, hw.tile_dma_src_config.ane_tile_dma_src_config.crop_offset2.offset_x, ANE_L2_INPUT_CROP_SRC2_OFFSET_X_LSBS_WIDTH_V19)"
+ "cache_dma_pre_config.throttle.on_tile_dma_dst || cache_dma_pre_config.throttle.on_tile_dma_src || cache_dma_pre_config.throttle.on_kernel_dma_src"
+ "hw.tile_dma_src_config.ane_tile_dma_src_config.dma_config_ext2 .cache_hint_reuse == ZinHWTraits<19>::ane_tile_dma_src_dma_config_cache_hint_reuse_noalloc"
+ "tile_dma_src1_cache_hint == ane_tile_dma_src_dma_config_cache_hint_noalloc_v19 || tile_dma_src1_cache_hint == ane_tile_dma_src_dma_config_cache_hint_alloc_v19 || tile_dma_src1_cache_hint == ane_tile_dma_src_dma_config_cache_hint_depri_v19 || tile_dma_src1_cache_hint == ane_tile_dma_src_dma_config_cache_hint_drop_v19"
+ "hw.tile_dma_src_config.ane_tile_dma_src_config.tex_src.src_permute_c == ane_tile_dma_src_tex_src_src_permute_c_zero_v19"
+ "required_acc_regs_per_mac <= 32"
+ "tile_dma_src2_cache_hint_no_reuse == ane_tile_dma_src_dma_config_ext2_cache_hint_no_reuse_noalloc_v19 || tile_dma_src2_cache_hint_no_reuse == ane_tile_dma_src_dma_config_ext2_cache_hint_no_reuse_alloc_v19 || tile_dma_src2_cache_hint_no_reuse == ane_tile_dma_src_dma_config_ext2_cache_hint_no_reuse_depri_v19 || tile_dma_src2_cache_hint_no_reuse == ane_tile_dma_src_dma_config_ext2_cache_hint_no_reuse_drop_v19"
+ "Error: Invalid perf tracer configuration."
+ "Parse error: compute_thread_command"
+ "kernel_config.palette_lutdma_config.cache_hint == ane_kernel_dma_src_palette_lutdma_config_cache_hint_noalloc_v19"
+ "hw.tile_dma_src_config.ane_tile_dma_src_config.tex_src.ind_permute_c == ane_tile_dma_src_tex_src_ind_permute_c_zero_v19"
+ "!cache_dma_pre_config.pause.on_tile_dma_dst && !cache_dma_pre_config.pause.on_tile_dma_src && !cache_dma_pre_config.pause.on_kernel_dma_src && cache_dma_pre_config.pause.duration == 0"
+ "Illegal Prefetch Rate"
+ "kZinIrSuccess == get_mem_fmt_bytes(tile_dma_dst_intlv, tile_dma_dst_fmt_mode, mem_fmt_bytes)"
+ "Graph update must be successful"
+ "hw.ne_config.ane_ne_config.mac_cfg.kernel_mode == ane_ne_mac_cfg_kernel_mode_kernel_v19"
+ "cache_dma_pre_config.pause.on_tile_dma_dst || cache_dma_pre_config.pause.on_tile_dma_src || cache_dma_pre_config.pause.on_kernel_dma_src"
+ "hw.tile_dma_src_config.ane_tile_dma_src_config.tex_crop_cfg[i].scale0 == ane_tile_dma_src_tex_crop_cfg_scale0_one_v19"
+ "tile_dma_src.dma_config.cache_hint != ane_tile_dma_src_dma_config_cache_hint_drop_v19"
+ "hw.tile_dma_src_config.ane_tile_dma_src_config.dma_config_ext2 .cache_hint_no_reuse == ZinHWTraits<19>::ane_tile_dma_src_dma_config_cache_hint_no_reuse_noalloc"
+ "Error: Invalid perf trace given"
+ "std::set<uint32_t>({ane_kernel_dma_src_bias_dma_config_cache_hint_noalloc_v19, ane_kernel_dma_src_bias_dma_config_cache_hint_alloc_v19, ane_kernel_dma_src_bias_dma_config_cache_hint_depri_v19, ane_kernel_dma_src_bias_dma_config_cache_hint_drop_v19}).contains( kernel_dma_src_bias_cache_hint)"
+ "tile_dma_src.dma_config2.cache_hint != ane_tile_dma_src_dma_config2_cache_hint_drop_v19"
+ "hw.ne_config.ane_ne_config.kernel_cfg.palette_block_size == hw.kernel_dma_src_config.ane_kernel_dma_src_config.kernel_config.palette_block_size"
+ "hw.common_config.ane_common_config.pe_cfg.src2_broadcast_y == 0x0"
+ "kDRAMInplace"
+ "dequant_1"
+ "match_offset_lsbs( hw.l2_config.ane_l2_config.input_crop.src2_offset_y_lsbs, hw.tile_dma_src_config.ane_tile_dma_src_config.crop_offset2.offset_y, ANE_L2_INPUT_CROP_SRC2_OFFSET_Y_LSBS_WIDTH_V19)"
+ "hw.tile_dma_src_config.ane_tile_dma_src_config.tex_idx.idx_permute_z == ane_tile_dma_src_tex_idx_idx_permute_z_zero_v19"
+ "hw.l2_config.ane_l2_config.source1_cfg.bfr_mode == hw.tile_dma_src_config.ane_tile_dma_src_config.dma_config.l2_bfr_mode"
+ "bias_mode == ZinHWTraits<19>::ane_ne_mac_cfg_bias_mode_const"
+ "t8140"
+ "(kw == 3 && sx == 1) || (kw == 5 && sx == 2) || (kw == 6 && sx == 2)"
+ "fill_lower_ne_first"
+ "hw.common_config.ane_common_config.pe_cfg.src2_broadcast_x == 0x0"
+ "hw.l2_config.ane_l2_config.source2_cfg.bfr_mode == hw.tile_dma_src_config.ane_tile_dma_src_config.dma_config.l2_bfr_mode"
+ "ZinRegisterProgrammingAnalysis<19>::CalculateLinearDmaDstGranularityInX( hw, hal.dram_alignment, dma_x_granularity) == kZinIrSuccess"
+ "hw.ne_config.ane_ne_config.mac_cfg.kernel_mode != ZinHWTraits<19>::ane_ne_mac_cfg_kernel_mode_unity"
+ "Could not determine TD partition of operation"
+ "legal_fifo"
+ "post_scale_mode == ZinHWTraits<19>::ane_ne_mac_cfg_post_scale_mode_const"
+ "hw.tile_dma_src_config.ane_tile_dma_src_config.dma_config.cache_hint == ZinHWTraits<19>::ane_tile_dma_src_dma_config_cache_hint_noalloc"
+ "tile_dma_src2_cache_hint_reuse == ane_tile_dma_src_dma_config_ext2_cache_hint_reuse_noalloc_v19 || tile_dma_src2_cache_hint_reuse == ane_tile_dma_src_dma_config_ext2_cache_hint_reuse_alloc_v19 || tile_dma_src2_cache_hint_reuse == ane_tile_dma_src_dma_config_ext2_cache_hint_reuse_depri_v19 || tile_dma_src2_cache_hint_reuse == ane_tile_dma_src_dma_config_ext2_cache_hint_reuse_drop_v19"
+ "cto_w == 0x0"
+ "hw.common_config.ane_common_config.cfg.small_source_mode == ane_common_cfg_small_source_mode_normal_v19"
+ "/Library/Caches/com.apple.xbs/Sources/ANECompiler/libs/inference/compiler/ZinIrCodegen/src/ZinCodegen_v19.cpp"
+ "tile_dma_src.dma_config_ext.cache_hint_no_reuse != ane_tile_dma_src_dma_config_ext_cache_hint_no_reuse_drop_v19"
+ "hw.common_config.ane_common_config.pe_cfg.src2_wto_c == 0x0"
+ "hw.common_config.ane_common_config.pe_cfg.src2_broadcast_c == 0x0"
+ "(1 << (hw.ne_config.ane_ne_config.kernel_cfg.palettized_bits + hw.kernel_dma_src_config.ane_kernel_dma_src_config.kernel_config .palette_block_size + (hw.ne_config.ane_ne_config.kernel_cfg.kernel_fmt != ZinHWTraits<19>::ane_ne_kernel_cfg_kernel_fmt_fp16))) <= hal_params.ne_palette_lut_size_in_bytes"
+ "The next operation id could not be found"
+ "input_src1_dma_x_granularity <= input_l2_x_granularity"
+ "prod_tile_dma_dst.dma_config_ext.wrap_cfg == ane_tile_dma_dst_dma_config_ext_wrap_cfg_none_v19"
+ "Disable DRAM Input FIFO: %!d(MISSING)\n"
+ "Throttle Duration has to be 0 if nothing to throttle on"
- "Weight file size ("
- " bytes) exceeds the maximum ("
- " bytes)"
- "Allocation error: compute_thread_command"

```
