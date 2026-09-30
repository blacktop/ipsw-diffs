## ImageIO

> `/System/Library/Frameworks/ImageIO.framework/ImageIO`

```diff

-2661.3.5.1.0
-  __TEXT.__text: 0x3fd060
-  __TEXT.__auth_stubs: 0x4000
-  __TEXT.__objc_methlist: 0x940
-  __TEXT.__const: 0x314d8
-  __TEXT.__gcc_except_tab: 0x1f334
-  __TEXT.__cstring: 0x7a712
+2661.4.5.0.0
+  __TEXT.__text: 0x464d60
+  __TEXT.__auth_stubs: 0x4110
+  __TEXT.__objc_methlist: 0xb58
+  __TEXT.__const: 0xb89f8
+  __TEXT.__gcc_except_tab: 0x1fa20
+  __TEXT.__cstring: 0x7bb6c
   __TEXT.__oslogstring: 0x17
   __TEXT.__ustring: 0x20
-  __TEXT.__unwind_info: 0xd258
-  __TEXT.__eh_frame: 0x390
+  __TEXT.__unwind_info: 0xd740
+  __TEXT.__eh_frame: 0x510
   __TEXT.__objc_classname: 0xce
   __TEXT.__objc_methname: 0x2a12
   __TEXT.__objc_methtype: 0x1efc
   __TEXT.__objc_stubs: 0x2280
   __DATA_CONST.__got: 0x5c8
-  __DATA_CONST.__const: 0xfd40
+  __DATA_CONST.__const: 0x103d0
   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x940
+  __DATA_CONST.__objc_selrefs: 0xa48
   __DATA_CONST.__objc_superrefs: 0x30
   __DATA_CONST.__objc_arraydata: 0x20
-  __AUTH_CONST.__auth_got: 0x2018
-  __AUTH_CONST.__auth_ptr: 0x90
-  __AUTH_CONST.__const: 0x3cb68
+  __AUTH_CONST.__auth_got: 0x20a0
+  __AUTH_CONST.__auth_ptr: 0xa0
+  __AUTH_CONST.__const: 0x3cde0
   __AUTH_CONST.__cfstring: 0xda40
-  __AUTH_CONST.__objc_const: 0x1248
+  __AUTH_CONST.__objc_const: 0xe50
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH.__objc_data: 0x2d0
   __AUTH.__data: 0x1d0
   __DATA.__objc_ivar: 0x84
-  __DATA.__data: 0x2bb8
-  __DATA.__bss: 0x5360
-  __DATA.__common: 0x1ea8
+  __DATA.__data: 0x2cf0
+  __DATA.__bss: 0x12800
+  __DATA.__common: 0x7ec4
   __DATA_DIRTY.__data: 0x170
   __DATA_DIRTY.__crash_info: 0x40
   __DATA_DIRTY.__common: 0xd33
-  __DATA_DIRTY.__bss: 0x698
+  __DATA_DIRTY.__bss: 0x2610
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/ColorSync.framework/ColorSync
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libexpat.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 13118
-  Symbols:   15497
-  CStrings:  12538
+  Functions: 13879
+  Symbols:   16809
+  CStrings:  12711
 
Symbols:
+ _LODEPNG_VERSION_STRING
+ __Z13lodepng_crc32PKhm
+ __Z14lodepng_decodePPhPjS1_P12LodePNGStatePKhm
+ __Z14lodepng_encodePPhPmPKhjjP12LodePNGState
+ __Z15lodepng_convertPhPKhPK16LodePNGColorModeS4_jj
+ __Z15lodepng_deflatePPhPmPKhmPK23LodePNGCompressSettings
+ __Z15lodepng_get_bppPK16LodePNGColorMode
+ __Z15lodepng_inflatePPhPmPKhmPK25LodePNGDecompressSettings
+ __Z15lodepng_inspectPjS_P12LodePNGStatePKhm
+ __Z15lodepng_set_iccP11LodePNGInfoPKcPKhj
+ __Z16lodepng_add_textP11LodePNGInfoPKcS2_
+ __Z16lodepng_decode24PPhPjS1_PKhm
+ __Z16lodepng_decode32PPhPjS1_PKhm
+ __Z16lodepng_encode24PPhPmPKhjj
+ __Z16lodepng_encode32PPhPmPKhjj
+ __Z17lodepng_add_itextP11LodePNGInfoPKcS2_S2_S2_
+ __Z17lodepng_clear_iccP11LodePNGInfo
+ __Z17lodepng_info_copyP11LodePNGInfoPKS_
+ __Z17lodepng_info_initP11LodePNGInfo
+ __Z17lodepng_load_filePPhPmPKc
+ __Z17lodepng_save_filePKhmPKc
+ __Z18lodepng_chunk_dataPh
+ __Z18lodepng_chunk_findPhPKhPKc
+ __Z18lodepng_chunk_nextPh
+ __Z18lodepng_chunk_typePcPKh
+ __Z18lodepng_clear_textP11LodePNGInfo
+ __Z18lodepng_error_textj
+ __Z18lodepng_state_copyP12LodePNGStatePKS_
+ __Z18lodepng_state_initP12LodePNGState
+ __Z19lodepng_clear_itextP11LodePNGInfo
+ __Z19lodepng_convert_rgbPjS_S_jjjPK16LodePNGColorModeS2_
+ __Z19lodepng_decode_filePPhPjS1_PKc16LodePNGColorTypej
+ __Z19lodepng_encode_filePKcPKhjj16LodePNGColorTypej
+ __Z19lodepng_palette_addP16LodePNGColorModehhhh
+ __Z20lodepng_chunk_appendPPhPmPKh
+ __Z20lodepng_chunk_createPPhPmjPKcPKh
+ __Z20lodepng_chunk_lengthPKh
+ __Z20lodepng_get_channelsPK16LodePNGColorMode
+ __Z20lodepng_get_raw_sizejjPK16LodePNGColorMode
+ __Z20lodepng_info_cleanupP11LodePNGInfo
+ __Z20lodepng_read32bitIntPKh
+ __Z21lodepng_chunk_privatePKh
+ __Z21lodepng_decode24_filePPhPjS1_PKc
+ __Z21lodepng_decode32_filePPhPjS1_PKc
+ __Z21lodepng_decode_memoryPPhPjS1_PKhm16LodePNGColorTypej
+ __Z21lodepng_encode24_filePKcPKhjj
+ __Z21lodepng_encode32_filePKcPKhjj
+ __Z21lodepng_encode_memoryPPhPmPKhjj16LodePNGColorTypej
+ __Z21lodepng_inspect_chunkP12LodePNGStatemPKhm
+ __Z21lodepng_is_alpha_typePK16LodePNGColorMode
+ __Z21lodepng_palette_clearP16LodePNGColorMode
+ __Z21lodepng_state_cleanupP12LodePNGState
+ __Z21lodepng_zlib_compressPPhPmPKhmPK23LodePNGCompressSettings
+ __Z22lodepng_can_have_alphaPK16LodePNGColorMode
+ __Z23lodepng_chunk_ancillaryPKh
+ __Z23lodepng_chunk_check_crcPKh
+ __Z23lodepng_color_mode_copyP16LodePNGColorModePKS_
+ __Z23lodepng_color_mode_initP16LodePNGColorMode
+ __Z23lodepng_color_mode_make16LodePNGColorTypej
+ __Z23lodepng_is_palette_typePK16LodePNGColorMode
+ __Z23lodepng_zlib_decompressPPhPmPKhmPK25LodePNGDecompressSettings
+ __Z24lodepng_chunk_data_constPKh
+ __Z24lodepng_chunk_find_constPKhS0_PKc
+ __Z24lodepng_chunk_next_constPKh
+ __Z24lodepng_chunk_safetocopyPKh
+ __Z24lodepng_get_raw_size_lctjj16LodePNGColorTypej
+ __Z25lodepng_auto_choose_colorP16LodePNGColorModePKhjjPKS_
+ __Z25lodepng_chunk_type_equalsPKhPKc
+ __Z25lodepng_get_color_profileP19LodePNGColorProfilePKhjjPK16LodePNGColorMode
+ __Z25lodepng_has_palette_alphaPK16LodePNGColorMode
+ __Z25lodepng_is_greyscale_typePK16LodePNGColorMode
+ __Z26lodepng_chunk_generate_crcPh
+ __Z26lodepng_color_mode_cleanupP16LodePNGColorMode
+ __Z26lodepng_color_profile_initP19LodePNGColorProfile
+ __Z28lodepng_huffman_code_lengthsPjPKjmj
+ __Z29lodepng_decoder_settings_initP22LodePNGDecoderSettings
+ __Z29lodepng_encoder_settings_initP22LodePNGEncoderSettings
+ __Z30lodepng_compress_settings_initP23LodePNGCompressSettings
+ __Z32lodepng_decompress_settings_initP25LodePNGDecompressSettings
+ __ZN4jpgd12jpeg_decoder10init_frameEv
+ __ZN4jpgd12jpeg_decoder10word_clearEPvtj
+ __ZN4jpgd12jpeg_decoder11H1V1ConvertEv
+ __ZN4jpgd12jpeg_decoder11H1V2ConvertEv
+ __ZN4jpgd12jpeg_decoder11H2V1ConvertEv
+ __ZN4jpgd12jpeg_decoder11H2V2ConvertEv
+ __ZN4jpgd12jpeg_decoder11decode_initEPNS_19jpeg_decoder_streamEj
+ __ZN4jpgd12jpeg_decoder11decode_scanEPFvPS0_iiiE
+ __ZN4jpgd12jpeg_decoder11next_markerEv
+ __ZN4jpgd12jpeg_decoder12decode_startEv
+ __ZN4jpgd12jpeg_decoder12gray_convertEv
+ __ZN4jpgd12jpeg_decoder13fix_in_bufferEv
+ __ZN4jpgd12jpeg_decoder13load_next_rowEv
+ __ZN4jpgd12jpeg_decoder13stop_decodingENS_11jpgd_statusE
+ __ZN4jpgd12jpeg_decoder13transform_mcuEi
+ __ZN4jpgd12jpeg_decoder14begin_decodingEv
+ __ZN4jpgd12jpeg_decoder14coeff_buf_openEiiii
+ __ZN4jpgd12jpeg_decoder14prep_in_bufferEv
+ __ZN4jpgd12jpeg_decoder15create_look_upsEv
+ __ZN4jpgd12jpeg_decoder15decode_next_rowEv
+ __ZN4jpgd12jpeg_decoder15free_all_blocksEv
+ __ZN4jpgd12jpeg_decoder15init_sequentialEv
+ __ZN4jpgd12jpeg_decoder15make_huff_tableEiPNS0_11huff_tablesE
+ __ZN4jpgd12jpeg_decoder15process_markersEv
+ __ZN4jpgd12jpeg_decoder15process_restartEv
+ __ZN4jpgd12jpeg_decoder15read_dht_markerEv
+ __ZN4jpgd12jpeg_decoder15read_dqt_markerEv
+ __ZN4jpgd12jpeg_decoder15read_dri_markerEv
+ __ZN4jpgd12jpeg_decoder15read_sof_markerEv
+ __ZN4jpgd12jpeg_decoder15read_sos_markerEv
+ __ZN4jpgd12jpeg_decoder16init_progressiveEv
+ __ZN4jpgd12jpeg_decoder17check_huff_tablesEv
+ __ZN4jpgd12jpeg_decoder17locate_sof_markerEv
+ __ZN4jpgd12jpeg_decoder17locate_soi_markerEv
+ __ZN4jpgd12jpeg_decoder17locate_sos_markerEv
+ __ZN4jpgd12jpeg_decoder18check_quant_tablesEv
+ __ZN4jpgd12jpeg_decoder19H1V2ConvertFilteredEv
+ __ZN4jpgd12jpeg_decoder19H2V1ConvertFilteredEv
+ __ZN4jpgd12jpeg_decoder19H2V2ConvertFilteredEv
+ __ZN4jpgd12jpeg_decoder19decode_next_mcu_rowEv
+ __ZN4jpgd12jpeg_decoder20calc_mcu_block_orderEv
+ __ZN4jpgd12jpeg_decoder20skip_variable_markerEv
+ __ZN4jpgd12jpeg_decoder21decode_block_ac_firstEPS0_iii
+ __ZN4jpgd12jpeg_decoder21decode_block_dc_firstEPS0_iii
+ __ZN4jpgd12jpeg_decoder22decode_block_ac_refineEPS0_iii
+ __ZN4jpgd12jpeg_decoder22decode_block_dc_refineEPS0_iii
+ __ZN4jpgd12jpeg_decoder4initEPNS_19jpeg_decoder_streamEj
+ __ZN4jpgd12jpeg_decoder5allocEmb
+ __ZN4jpgd12jpeg_decoder6decodeEPPKvPj
+ __ZN4jpgd12jpeg_decoder8find_eoiEv
+ __ZN4jpgd12jpeg_decoder9init_scanEv
+ __ZN4jpgd12jpeg_decoderC1EPNS_19jpeg_decoder_streamEj
+ __ZN4jpgd12jpeg_decoderC2EPNS_19jpeg_decoder_streamEj
+ __ZN4jpgd12jpeg_decoderD1Ev
+ __ZN4jpgd12jpeg_decoderD2Ev
+ __ZN4jpgd23jpeg_decoder_mem_stream4openEPKhj
+ __ZN4jpgd23jpeg_decoder_mem_stream4readEPhiPb
+ __ZN4jpgd24jpeg_decoder_file_stream4openEPKc
+ __ZN4jpgd24jpeg_decoder_file_stream4readEPhiPb
+ __ZN4jpgd24jpeg_decoder_file_stream5closeEv
+ __ZN4jpgd24jpeg_decoder_file_streamC1Ev
+ __ZN4jpgd24jpeg_decoder_file_streamC2Ev
+ __ZN4jpgd24jpeg_decoder_file_streamD0Ev
+ __ZN4jpgd24jpeg_decoder_file_streamD1Ev
+ __ZN4jpgd24jpeg_decoder_file_streamD2Ev
+ __ZN4jpgd31decompress_jpeg_image_from_fileEPKcPiS2_S2_ij
+ __ZN4jpgd33decompress_jpeg_image_from_memoryEPKhiPiS2_S2_ij
+ __ZN4jpgd33decompress_jpeg_image_from_streamEPNS_19jpeg_decoder_streamEPiS2_S2_ij
+ __ZN6basist10encode_bc1EPvPKhj
+ __ZN6basist10encode_bc4EPvPKhj
+ __ZN6basist10uastc_initEv
+ __ZN6basist12unpack_uastcERKNS_11uastc_blockEPNS_7color32Eb
+ __ZN6basist12unpack_uastcERKNS_11uastc_blockERNS_20unpacked_uastc_blockEbb
+ __ZN6basist12unpack_uastcERKNS_20unpacked_uastc_blockEPNS_7color32Eb
+ __ZN6basist12unpack_uastcEjjRKNS_7color32ERKNS_15astc_block_descEPS0_b
+ __ZN6basist14encode_bc1_altEPvPKhj
+ __ZN6basist14g_astc_unquantE
+ __ZN6basist14g_bc7_weights1E
+ __ZN6basist14g_bc7_weights2E
+ __ZN6basist14g_bc7_weights3E
+ __ZN6basist14g_bc7_weights4E
+ __ZN6basist15apply_etc1_biasERKNS_7color32Ejjj
+ __ZN6basist15astc_get_levelsEi
+ __ZN6basist15g_astc_weights4E
+ __ZN6basist15g_astc_weights5E
+ __ZN6basist15get_debug_flagsEv
+ __ZN6basist15ktx2_transcoder15read_key_valuesEv
+ __ZN6basist15ktx2_transcoder17start_transcodingEv
+ __ZN6basist15ktx2_transcoder21decompress_level_dataEjRN6basisu6vectorIhEE
+ __ZN6basist15ktx2_transcoder21transcode_image_levelEjjjPvjNS_25transcoder_texture_formatEjjjiiPNS_21ktx2_transcoder_stateE
+ __ZN6basist15ktx2_transcoder28decompress_etc1s_global_dataEv
+ __ZN6basist15ktx2_transcoder4initEPKvj
+ __ZN6basist15ktx2_transcoder5clearEv
+ __ZN6basist15ktx2_transcoderC1EPNS_29etc1_global_selector_codebookE
+ __ZN6basist15ktx2_transcoderC2EPNS_29etc1_global_selector_codebookE
+ __ZN6basist15pack_astc_blockEPjPKNS_15astc_block_descEj
+ __ZN6basist15set_debug_flagsEj
+ __ZN6basist16encode_bc7_blockEPvPKNS_24bc7_optimization_resultsE
+ __ZN6basist16g_bc7_partition1E
+ __ZN6basist16g_bc7_partition2E
+ __ZN6basist16g_bc7_partition3E
+ __ZN6basist17basisu_transcoder16stop_transcodingEv
+ __ZN6basist17basisu_transcoder17start_transcodingEPKvj
+ __ZN6basist17basisu_transcoder25write_opaque_alpha_blocksEjjPvNS_12block_formatEjj
+ __ZN6basist17basisu_transcoderC1EPKNS_29etc1_global_selector_codebookE
+ __ZN6basist17basisu_transcoderC2EPKNS_29etc1_global_selector_codebookE
+ __ZN6basist17g_bc7_num_subsetsE
+ __ZN6basist18g_uastc_mode_compsE
+ __ZN6basist18g_uastc_mode_is_laE
+ __ZN6basist18get_anchor_indicesEjjjRPKh
+ __ZN6basist19g_uastc_mode_planesE
+ __ZN6basist20g_astc_bc7_patterns2E
+ __ZN6basist20g_astc_bc7_patterns3E
+ __ZN6basist20g_bc7_partition_bitsE
+ __ZN6basist20g_global_selector_cbE
+ __ZN6basist20g_uastc_mode_subsetsE
+ __ZN6basist21basis_get_block_widthENS_25transcoder_texture_formatE
+ __ZN6basist21basis_get_format_nameENS_25transcoder_texture_formatE
+ __ZN6basist21g_bc7_mode_has_p_bitsE
+ __ZN6basist21pack_astc_solid_blockEPvRKNS_7color32E
+ __ZN6basist21unquant_astc_endpointEjjjj
+ __ZN6basist22basis_get_block_heightENS_25transcoder_texture_formatE
+ __ZN6basist22basisu_transcoder_initEv
+ __ZN6basist22encode_bc1_solid_blockEPvjjj
+ __ZN6basist22g_astc_weights_3levelsE
+ __ZN6basist22g_ktx2_file_identifierE
+ __ZN6basist22g_uastc_mode_has_alphaE
+ __ZN6basist22s_uastc_to_bc1_weightsE
+ __ZN6basist22transcode_uastc_to_bc1ERKNS_11uastc_blockEPvb
+ __ZN6basist22transcode_uastc_to_bc3ERKNS_11uastc_blockEPvb
+ __ZN6basist22transcode_uastc_to_bc4ERKNS_11uastc_blockEPvbj
+ __ZN6basist22transcode_uastc_to_bc5ERKNS_11uastc_blockEPvbjj
+ __ZN6basist22transcode_uastc_to_bc7ERKNS_11uastc_blockEPv
+ __ZN6basist22transcode_uastc_to_bc7ERKNS_11uastc_blockERNS_24bc7_optimization_resultsE
+ __ZN6basist22transcode_uastc_to_bc7ERKNS_20unpacked_uastc_blockERNS_24bc7_optimization_resultsE
+ __ZN6basist23g_astc_bise_range_tableE
+ __ZN6basist23g_bc7_3_astc2_patterns2E
+ __ZN6basist23g_uastc_mode_huff_codesE
+ __ZN6basist23transcode_uastc_to_astcERKNS_11uastc_blockEPv
+ __ZN6basist23transcode_uastc_to_etc1ERKNS_11uastc_blockEPv
+ __ZN6basist23transcode_uastc_to_etc1ERKNS_11uastc_blockEPvj
+ __ZN6basist23transcode_uastc_to_etc1ERNS_20unpacked_uastc_blockEPA4_NS_7color32EPv
+ __ZN6basist24g_uastc_mode_weight_bitsE
+ __ZN6basist25basis_is_format_supportedENS_25transcoder_texture_formatENS_16basis_tex_formatE
+ __ZN6basist25g_global_selector_cb_sizeE
+ __ZN6basist25unquant_astc_endpoint_valEjj
+ __ZN6basist26g_bc7_alpha_index_bitcountE
+ __ZN6basist26g_bc7_color_index_bitcountE
+ __ZN6basist26g_uastc_mode_has_bc1_hint0E
+ __ZN6basist26g_uastc_mode_has_bc1_hint1E
+ __ZN6basist26g_uastc_mode_has_etc1_biasE
+ __ZN6basist26g_uastc_mode_weight_rangesE
+ __ZN6basist27basis_get_block_format_nameENS_12block_formatE
+ __ZN6basist27basis_get_texture_type_nameENS_18basis_texture_typeE
+ __ZN6basist27g_astc_bc7_pattern2_anchorsE
+ __ZN6basist27g_astc_bc7_pattern3_anchorsE
+ __ZN6basist27g_bc7_alpha_precision_tableE
+ __ZN6basist27g_bc7_color_precision_tableE
+ __ZN6basist28astc_is_valid_endpoint_rangeEj
+ __ZN6basist28g_bc7_mode_has_shared_p_bitsE
+ __ZN6basist28g_uastc_mode_endpoint_rangesE
+ __ZN6basist28transcode_uastc_to_bc1_hint0ERKNS_20unpacked_uastc_blockEPv
+ __ZN6basist28transcode_uastc_to_bc1_hint1ERKNS_20unpacked_uastc_blockEPA4_KNS_7color32EPvb
+ __ZN6basist28transcode_uastc_to_etc2_rgbaERKNS_11uastc_blockEPv
+ __ZN6basist29etc1_global_selector_codebook10print_codeEP7__sFILE
+ __ZN6basist29etc1_global_selector_codebook4initEjPKj
+ __ZN6basist29g_astc_bc7_common_partitions2E
+ __ZN6basist29g_astc_bc7_common_partitions3E
+ __ZN6basist30g_bc7_mode_5_optimal_endpointsE
+ __ZN6basist30g_bc7_mode_6_optimal_endpointsE
+ __ZN6basist30transcode_uastc_to_etc2_eac_a8ERNS_20unpacked_uastc_blockEPA4_NS_7color32EPv
+ __ZN6basist31basis_get_basisu_texture_formatENS_25transcoder_texture_formatE
+ __ZN6basist31basisu_transcoder_supports_ktx2Ev
+ __ZN6basist31g_bc7_3_astc2_common_partitionsE
+ __ZN6basist31g_bc7_3_astc2_patterns2_anchorsE
+ __ZN6basist31transcode_uastc_to_etc2_eac_r11ERKNS_11uastc_blockEPvbj
+ __ZN6basist31transcode_uastc_to_pvrtc1_4_rgbEPKNS_11uastc_blockEPvjjbb
+ __ZN6basist32basisu_lowlevel_etc1s_transcoder13decode_tablesEPKhj
+ __ZN6basist32basisu_lowlevel_etc1s_transcoder15decode_palettesEjPKhjjS2_j
+ __ZN6basist32basisu_lowlevel_etc1s_transcoder15transcode_imageENS_25transcoder_texture_formatEPvjPKhjjjjjjjjjjjbbjPNS_23basisu_transcoder_stateEj
+ __ZN6basist32basisu_lowlevel_etc1s_transcoder15transcode_sliceEPvjjPKhjNS_12block_formatEjbbbjjjjPNS_23basisu_transcoder_stateEbS1_j
+ __ZN6basist32basisu_lowlevel_etc1s_transcoderC1EPKNS_29etc1_global_selector_codebookE
+ __ZN6basist32basisu_lowlevel_etc1s_transcoderC2EPKNS_29etc1_global_selector_codebookE
+ __ZN6basist32basisu_lowlevel_uastc_transcoder15transcode_imageENS_25transcoder_texture_formatEPvjPKhjjjjjjjjjbbjPNS_23basisu_transcoder_stateEjii
+ __ZN6basist32basisu_lowlevel_uastc_transcoder15transcode_sliceEPvjjPKhjNS_12block_formatEjbbjjjPNS_23basisu_transcoder_stateEjiij
+ __ZN6basist32basisu_lowlevel_uastc_transcoderC1Ev
+ __ZN6basist32basisu_lowlevel_uastc_transcoderC2Ev
+ __ZN6basist32transcode_uastc_to_etc2_eac_rg11ERKNS_11uastc_blockEPvbjj
+ __ZN6basist32transcode_uastc_to_pvrtc1_4_rgbaEPKNS_11uastc_blockEPvjjb
+ __ZN6basist33basis_transcoder_format_has_alphaENS_25transcoder_texture_formatE
+ __ZN6basist33basis_validate_output_buffer_sizeENS_25transcoder_texture_formatEjjjjjj
+ __ZN6basist34basis_block_format_is_uncompressedENS_12block_formatE
+ __ZN6basist34basis_get_bytes_per_block_or_pixelENS_25transcoder_texture_formatE
+ __ZN6basist34bc7_convert_partition_index_3_to_2Ejj
+ __ZN6basist36basisu_transcoder_supports_ktx2_zstdEv
+ __ZN6basist38basis_get_uncompressed_bytes_per_pixelENS_25transcoder_texture_formatE
+ __ZN6basist38g_bc7_table_anchor_index_second_subsetE
+ __ZN6basist39basis_transcoder_format_is_uncompressedENS_25transcoder_texture_formatE
+ __ZN6basist39g_bc7_table_anchor_index_third_subset_1E
+ __ZN6basist39g_bc7_table_anchor_index_third_subset_2E
+ __ZN6basist41g_astc_to_bc7_partition_index_perm_tablesE
+ __ZN6basist41g_bc7_to_astc_partition_index_perm_tablesE
+ __ZN6basist5crc16EPKvmt
+ __ZN6basisu10hash_hsiehEPKhm
+ __ZN6basisu10load_imageEPKcRNS_5imageE
+ __ZN6basisu11pack_eac_a8EPNS_12eac_a8_blockEPKhjjj
+ __ZN6basisu11pack_eac_a8ERNS_19pack_eac_a8_resultsEPKhjjjj
+ __ZN6basisu11unpack_etc1ERKNS_9etc_blockEPNS_10color_rgbaEb
+ __ZN6basisu12debug_printfEPKcz
+ __ZN6basisu12detect_sse41Ev
+ __ZN6basisu12error_printfEPKcz
+ __ZN6basisu12huffman_testEi
+ __ZN6basisu13bitwise_coder12end_zero_runERNS_6vectorItEERj
+ __ZN6basisu13bitwise_coder15end_nonzero_runERNS_6vectorItEERjj
+ __ZN6basisu13bitwise_coder18emit_huffman_tableERKNS_22huffman_encoding_tableE
+ __ZN6basisu13image_metrics4calcERKNS_5imageES3_jjbb
+ __ZN6basisu14etc1_optimizer15refine_solutionEj
+ __ZN6basisu14etc1_optimizer22evaluate_solution_fastERKNS_25etc1_solution_coordinatesERNS0_18potential_solutionEPS4_
+ __ZN6basisu14etc1_optimizer22evaluate_solution_slowERKNS_25etc1_solution_coordinatesERNS0_18potential_solutionEPS4_
+ __ZN6basisu14etc1_optimizer28check_for_redundant_solutionERKNS_25etc1_solution_coordinatesE
+ __ZN6basisu14etc1_optimizer28compute_internal_cluster_fitEj
+ __ZN6basisu14etc1_optimizer29compute_internal_neighborhoodEiii
+ __ZN6basisu14etc1_optimizer4initERKNS0_6paramsERNS0_7resultsE
+ __ZN6basisu14etc1_optimizer7computeEv
+ __ZN6basisu14g_debug_printfE
+ __ZN6basisu14g_hamming_distE
+ __ZN6basisu14image_resampleERKNS_5imageERS0_bPKcfbjj
+ __ZN6basisu14interval_timer12g_init_ticksE
+ __ZN6basisu14interval_timer12g_timer_freqE
+ __ZN6basisu14interval_timer13ticks_to_secsEy
+ __ZN6basisu14interval_timer4initEv
+ __ZN6basisu14interval_timer4stopEv
+ __ZN6basisu14interval_timer5startEv
+ __ZN6basisu14interval_timer6g_freqE
+ __ZN6basisu14interval_timer9get_ticksEv
+ __ZN6basisu14interval_timerC1Ev
+ __ZN6basisu14interval_timerC2Ev
+ __ZN6basisu14linear_to_srgbEf
+ __ZN6basisu14srgb_to_linearEf
+ __ZN6basisu15g_bc7_weights1xE
+ __ZN6basisu15g_bc7_weights2xE
+ __ZN6basisu15g_bc7_weights3xE
+ __ZN6basisu15g_bc7_weights4xE
+ __ZN6basisu16elemental_vector17increase_capacityEjbjPFvPvS1_jEb
+ __ZN6basisu16g_astc_weights4xE
+ __ZN6basisu16g_astc_weights5xE
+ __ZN6basisu16read_file_to_vecEPKcRNS_6vectorIhEE
+ __ZN6basisu17g_etc2_eac_tablesE
+ __ZN6basisu18g_etc2_eac_tables8E
+ __ZN6basisu18g_resample_filtersE
+ __ZN6basisu18write_data_to_fileEPKcPKvm
+ __ZN6basisu19basisu_encoder_initEv
+ __ZN6basisu19enable_debug_printfEb
+ __ZN6basisu19g_etc1_inten_tablesE
+ __ZN6basisu19g_etc1_pixel_coordsE
+ __ZN6basisu20find_resample_filterEPKc
+ __ZN6basisu20g_etc1_pixel_indicesE
+ __ZN6basisu21g_debug_font8x8_basicE
+ __ZN6basisu22color_cell_compressionEjPKNS_28color_cell_compressor_paramsEPNS_29color_cell_compressor_resultsEPKNS_28bc7enc_compress_block_paramsE
+ __ZN6basisu22g_num_resample_filtersE
+ __ZN6basisu22huffman_encoding_table4initEjPKjj
+ __ZN6basisu22huffman_encoding_table4initEjPKtj
+ __ZN6basisu23g_astc_weights_3levelsxE
+ __ZN6basisu23palette_index_reorderer12find_initialEj
+ __ZN6basisu23palette_index_reorderer12prepare_histEjjPKj
+ __ZN6basisu23palette_index_reorderer15find_next_entryERjRdPFfjjPvES3_f
+ __ZN6basisu23palette_index_reorderer4initEjPKjjPFfjjPvES3_f
+ __ZN6basisu23palette_index_reorderer9pick_sideEjjPFfjjPvES1_f
+ __ZN6basisu24check_best_overall_errorEPKNS_28color_cell_compressor_paramsEPNS_29color_cell_compressor_resultsE
+ __ZN6basisu24g_etc1_to_selector_indexE
+ __ZN6basisu24g_selector_index_to_etc1E
+ __ZN6basisu26bc7enc_compress_block_initEv
+ __ZN6basisu26pack_etc1_solid_color_initEv
+ __ZN6basisu27g_astc_sorted_order_unquantE
+ __ZN6basisu27pack_etc1_block_solid_colorERNS_9etc_blockEPKh
+ __ZN6basisu29fill_buffer_with_random_bytesEPvmj
+ __ZN6basisu31color_cell_compression_est_astcEjjPKjjPKN6basist13color_quad_u8EyS1_
+ __ZN6basisu33canonical_huffman_radix_sort_symsEjPNS_8sym_freqES1_
+ __ZN6basisu39canonical_huffman_enforce_max_code_sizeEPiii
+ __ZN6basisu46canonical_huffman_calculate_minimum_redundancyEPNS_8sym_freqEi
+ __ZN6basisu5image10debug_textEjjjjRKNS_10color_rgbaEPS2_bPKcz
+ __ZN6basisu8job_pool10job_threadEj
+ __ZN6basisu8job_pool12wait_for_allEv
+ __ZN6basisu8job_pool7add_jobEONSt3__18functionIFvvEEE
+ __ZN6basisu8job_pool7add_jobERKNSt3__18functionIFvvEEE
+ __ZN6basisu8job_poolC1Ej
+ __ZN6basisu8job_poolC2Ej
+ __ZN6basisu8job_poolD1Ev
+ __ZN6basisu8job_poolD2Ev
+ __ZN6basisu8load_bmpEPKcRNS_5imageE
+ __ZN6basisu8load_jpgEPKcRNS_5imageE
+ __ZN6basisu8load_pngEPKcRNS_5imageE
+ __ZN6basisu8load_pngEPKhmRNS_5imageEPKc
+ __ZN6basisu8load_tgaEPKcRNS_5imageE
+ __ZN6basisu8read_tgaEPKcRiS2_S2_
+ __ZN6basisu8read_tgaEPKhjRiS2_S2_
+ __ZN6basisu8save_pngEPKcRKNS_5imageEjj
+ __ZN6basisu9Resampler10get_clistsEPPNS0_12Contrib_ListES3_
+ __ZN6basisu9Resampler10make_clistEiiNS0_11Boundary_OpEPFffEfff
+ __ZN6basisu9Resampler10resample_xEPfPKf
+ __ZN6basisu9Resampler10resample_yEPf
+ __ZN6basisu9Resampler11scale_y_addEPfPKffi
+ __ZN6basisu9Resampler11scale_y_movEPfPKffi
+ __ZN6basisu9Resampler14get_filter_numEv
+ __ZN6basisu9Resampler15get_filter_nameEi
+ __ZN6basisu9Resampler5clampEPfi
+ __ZN6basisu9Resampler7reflectEiiNS0_11Boundary_OpE
+ __ZN6basisu9Resampler7restartEv
+ __ZN6basisu9Resampler8get_lineEv
+ __ZN6basisu9Resampler8put_lineEPKf
+ __ZN6basisu9ResamplerC1EiiiiNS0_11Boundary_OpEffPKcPNS0_12Contrib_ListES5_ffff
+ __ZN6basisu9ResamplerC2EiiiiNS0_11Boundary_OpEffPKcPNS0_12Contrib_ListES5_ffff
+ __ZN6basisu9ResamplerD1Ev
+ __ZN6basisu9ResamplerD2Ev
+ __ZN6basisu9etc_block11pack_color4ERKNS_10color_rgbaEbj
+ __ZN6basisu9etc_block11pack_color4Ejjjbj
+ __ZN6basisu9etc_block11pack_color5ERKNS_10color_rgbaEbj
+ __ZN6basisu9etc_block11pack_color5Ejjjbj
+ __ZN6basisu9etc_block11pack_delta3ERKNS_14color_rgba_i16E
+ __ZN6basisu9etc_block11pack_delta3Eiii
+ __ZN6basisu9etc_block13unpack_color4ERjS1_S1_tb
+ __ZN6basisu9etc_block13unpack_color4Etbj
+ __ZN6basisu9etc_block13unpack_color5ERNS_10color_rgbaEtb
+ __ZN6basisu9etc_block13unpack_color5ERNS_10color_rgbaEttbj
+ __ZN6basisu9etc_block13unpack_color5ERjS1_S1_tb
+ __ZN6basisu9etc_block13unpack_color5ERjS1_S1_ttbj
+ __ZN6basisu9etc_block13unpack_color5Etbj
+ __ZN6basisu9etc_block13unpack_delta3ERiS1_S1_t
+ __ZN6basisu9etc_block13unpack_delta3Et
+ __ZN6basisu9etc_block23get_abs_subblock_colorsEPNS_10color_rgbaEtj
+ __ZN6basisu9etc_block24get_diff_subblock_colorsEPNS_10color_rgbaEtj
+ __ZN6basisu9etc_block24get_diff_subblock_colorsEPNS_10color_rgbaEttj
+ __ZN7lodepng10decompressERNSt3__16vectorIhNS0_9allocatorIhEEEEPKhmRK25LodePNGDecompressSettings
+ __ZN7lodepng10decompressERNSt3__16vectorIhNS0_9allocatorIhEEEERKS4_RK25LodePNGDecompressSettings
+ __ZN7lodepng5StateC1ERKS0_
+ __ZN7lodepng5StateC1Ev
+ __ZN7lodepng5StateC2ERKS0_
+ __ZN7lodepng5StateC2Ev
+ __ZN7lodepng5StateD0Ev
+ __ZN7lodepng5StateD1Ev
+ __ZN7lodepng5StateD2Ev
+ __ZN7lodepng5StateaSERKS0_
+ __ZN7lodepng6decodeERNSt3__16vectorIhNS0_9allocatorIhEEEERjS6_PKhm16LodePNGColorTypej
+ __ZN7lodepng6decodeERNSt3__16vectorIhNS0_9allocatorIhEEEERjS6_RKNS0_12basic_stringIcNS0_11char_traitsIcEENS2_IcEEEE16LodePNGColorTypej
+ __ZN7lodepng6decodeERNSt3__16vectorIhNS0_9allocatorIhEEEERjS6_RKS4_16LodePNGColorTypej
+ __ZN7lodepng6decodeERNSt3__16vectorIhNS0_9allocatorIhEEEERjS6_RNS_5StateEPKhm
+ __ZN7lodepng6decodeERNSt3__16vectorIhNS0_9allocatorIhEEEERjS6_RNS_5StateERKS4_
+ __ZN7lodepng6encodeERKNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEEPKhjj16LodePNGColorTypej
+ __ZN7lodepng6encodeERKNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEERKNS0_6vectorIhNS4_IhEEEEjj16LodePNGColorTypej
+ __ZN7lodepng6encodeERNSt3__16vectorIhNS0_9allocatorIhEEEEPKhjj16LodePNGColorTypej
+ __ZN7lodepng6encodeERNSt3__16vectorIhNS0_9allocatorIhEEEEPKhjjRNS_5StateE
+ __ZN7lodepng6encodeERNSt3__16vectorIhNS0_9allocatorIhEEEERKS4_jj16LodePNGColorTypej
+ __ZN7lodepng6encodeERNSt3__16vectorIhNS0_9allocatorIhEEEERKS4_jjRNS_5StateE
+ __ZN7lodepng8compressERNSt3__16vectorIhNS0_9allocatorIhEEEEPKhmRK23LodePNGCompressSettings
+ __ZN7lodepng8compressERNSt3__16vectorIhNS0_9allocatorIhEEEERKS4_RK23LodePNGCompressSettings
+ __ZN7lodepng9load_fileERNSt3__16vectorIhNS0_9allocatorIhEEEERKNS0_12basic_stringIcNS0_11char_traitsIcEENS2_IcEEEE
+ __ZN7lodepng9save_fileERKNSt3__16vectorIhNS0_9allocatorIhEEEERKNS0_12basic_stringIcNS0_11char_traitsIcEENS2_IcEEEE
+ __ZNK6basist15ktx2_transcoder20get_image_level_infoERNS_21ktx2_image_level_infoEjjj
+ __ZNK6basist15ktx2_transcoder33get_etc1s_image_descs_image_flagsEjjj
+ __ZNK6basist15ktx2_transcoder8find_keyERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE
+ __ZNK6basist17basisu_transcoder10find_sliceEPKvjjjb
+ __ZNK6basist17basisu_transcoder12get_userdataEPKvjRjS3_
+ __ZNK6basist17basisu_transcoder13get_file_infoEPKvjRNS_16basisu_file_infoE
+ __ZNK6basist17basisu_transcoder14get_image_infoEPKvjRNS_17basisu_image_infoEj
+ __ZNK6basist17basisu_transcoder14get_tex_formatEPKvj
+ __ZNK6basist17basisu_transcoder15transcode_sliceEPKvjjPvjNS_12block_formatEjjjPNS_23basisu_transcoder_stateES3_jii
+ __ZNK6basist17basisu_transcoder15validate_headerEPKvj
+ __ZNK6basist17basisu_transcoder16get_texture_typeEPKvj
+ __ZNK6basist17basisu_transcoder16get_total_imagesEPKvj
+ __ZNK6basist17basisu_transcoder20get_image_level_descEPKvjjjRjS3_S3_
+ __ZNK6basist17basisu_transcoder20get_image_level_infoEPKvjRNS_23basisu_image_level_infoEjj
+ __ZNK6basist17basisu_transcoder21transcode_image_levelEPKvjjjPvjNS_25transcoder_texture_formatEjjPNS_23basisu_transcoder_stateEj
+ __ZNK6basist17basisu_transcoder21validate_header_quickEPKvj
+ __ZNK6basist17basisu_transcoder22find_first_slice_indexEPKvjjj
+ __ZNK6basist17basisu_transcoder22get_total_image_levelsEPKvjj
+ __ZNK6basist17basisu_transcoder23validate_file_checksumsEPKvjb
+ __ZNK6basisu14interval_timer16get_elapsed_secsEv
+ __ZNK6basisu9etc_block19evaluate_etc1_errorEPKNS_10color_rgbaEbi
+ __ZNK6basisu9etc_block19get_subblock_pixelsEPNS_10color_rgbaEi
+ __ZNSt3__115__thread_structC1Ev
+ __ZNSt3__115__thread_structD1Ev
+ __ZNSt3__118condition_variable10notify_oneEv
+ __ZNSt3__119__thread_local_dataEv
+ __ZNSt3__16__sortIRNS_6__lessIhhEEPhEEvT0_S5_T_
+ __ZNSt3__16__sortIRNS_6__lessIjjEEPjEEvT0_S5_T_
+ __ZNSt3__16thread4joinEv
+ __ZNSt3__16threadD1Ev
+ __ZTIN4jpgd23jpeg_decoder_mem_streamE
+ __ZTIN4jpgd24jpeg_decoder_file_streamE
+ __ZTIN7lodepng5StateE
+ __ZTSN4jpgd23jpeg_decoder_mem_streamE
+ __ZTSN4jpgd24jpeg_decoder_file_streamE
+ __ZTSN7lodepng5StateE
+ __ZTVN4jpgd23jpeg_decoder_mem_streamE
+ __ZTVN4jpgd24jpeg_decoder_file_streamE
+ __ZTVN7lodepng5StateE
+ _apg_bmp_free
+ _apg_bmp_read
+ _apg_bmp_write
+ _cos
+ _expf
+ _gettimeofday
+ _lodepng_default_compress_settings
+ _lodepng_default_decompress_settings
+ _log10
+ _pthread_setspecific
+ _rewind
+ _sin
+ _vprintf
+ _vsnprintf
CStrings:
+ "\x03\x02\x01"
+ "\n}\n"
+ "%u\n"
+ "(!MQ_segment) && active && !checked_out"
+ "(!MQ_segment) && active && (!checked_out) && ((symbol == 0) || (symbol == 1))"
+ "*** ERROR: failed to create outputsurface %dx%d '%c%c%c%c'\n"
+ "*** createPixelDataProviderForExtendedRange failed (nil)\n"
+ "*** kCGImageSourceDecodeRequest --> found gainMap - switching from MPO/JPEG to HEIF\n"
+ "*schemaPos == schemaNode"
+ "000000000"
+ "0x%X,"
+ "20190210"
+ "2D"
+ "2D array"
+ "3D"
+ "ASTC_4x4"
+ "ASTC_RGBA"
+ "ATC_RGB"
+ "ATC_RGBA"
+ "BC1"
+ "BC1_RGB"
+ "BC3"
+ "BC3_RGBA"
+ "BC4_R"
+ "BC5_RG"
+ "BC7"
+ "BC7_RGBA"
+ "BGR565"
+ "CMPhotoDecompressionContainerCreateImageForIndex(%d)  err=%d\n"
+ "ERROR: %s"
+ "ETC1"
+ "ETC1_RGB"
+ "ETC2_EAC_R11"
+ "ETC2_EAC_RG11"
+ "ETC2_RGBA"
+ "FDICT encountered in zlib header while it's not used for PNG"
+ "FXT1_RGB"
+ "Failed 0"
+ "Failed 2"
+ "Failed 4"
+ "Failed loading .BMP image \"%s\"!\n"
+ "Failed loading .TGA image \"%s\"!\n"
+ "Failure 5"
+ "IDAT"
+ "IHDR"
+ "IIO_create_BGRA_RGBA_IOSurfaceFromImage"
+ "Image is too large!"
+ "LodePNG"
+ "NLEN is not ones complement of LEN in a deflate block"
+ "PLTE"
+ "PNG file is smaller than a PNG header"
+ "PNG specification does not allow RGB ICC profile on gray color types and vice versa"
+ "PVRTC1_4_RGB"
+ "PVRTC1_4_RGBA"
+ "PVRTC2_4_RGB"
+ "PVRTC2_4_RGBA"
+ "RGB565"
+ "RGBA32"
+ "RGBA4444"
+ "b-spline"
+ "b0000bb00"
+ "b000b0bb0"
+ "bKGD"
+ "bKGD chunk has wrong size for RGB image"
+ "bKGD chunk has wrong size for grayscale image"
+ "bKGD chunk has wrong size for palette image"
+ "bell"
+ "blackman"
+ "bmp"
+ "box"
+ "cHRM"
+ "catmullrom"
+ "cb0000cbc"
+ "cb000cbcb"
+ "chunk length of a chunk is too large or the chunk too small"
+ "chunk length too large, chunk broken off at end of file"
+ "color conversion to palette requested while a color isn't in palette, or index out of bounds"
+ "conversion from color to grayscale not supported"
+ "cubemap array"
+ "dcb0000dc"
+ "dcb000dcb"
+ "edcb0000e"
+ "edcb000ed"
+ "empty input buffer given to decoder. Maybe caused by non-existing file?"
+ "end of in buffer memory reached while inflating"
+ "end of input memory reached without huffman end code"
+ "end of out buffer memory reached while inflating"
+ "error in code tree made it jump outside of huffman tree"
+ "failed to open file for reading"
+ "failed to open file for writing"
+ "fedcb000f"
+ "first chunk is not the header chunk"
+ "gAMA"
+ "gaussian"
+ "given image too small to contain all pixels to be encoded"
+ "given output image colortype or bitdepth not supported for color conversion"
+ "header chunk must have a size of 13 bytes"
+ "iCCP"
+ "iTXt"
+ "iTXt chunk too short to contain required bytes"
+ "illegal PNG color type or bpp"
+ "illegal PNG compression method"
+ "illegal PNG filter method"
+ "illegal PNG filter type encountered"
+ "illegal PNG interlace method"
+ "illegal bit depth for this color type given"
+ "impossible offset in lz77 encoding (internal bug)"
+ "incorrect PNG signature, it's no PNG or corrupted"
+ "integer overflow due to too many pixels"
+ "integer overflow in buffer size"
+ "integer overflow with combined idat chunk size"
+ "invalid ADLER32 encountered (checking ADLER32 can be disabled)"
+ "invalid BTYPE given in the settings of the encoder (only 0, 1 and 2 are allowed)"
+ "invalid CRC encountered (checking CRC can be disabled)"
+ "invalid FCHECK in zlib header"
+ "invalid ICC profile color type, the PNG specification only allows RGB or GRAY"
+ "invalid bKGD color while encoding (e.g. palette index out of range)"
+ "invalid cHRM chunk size"
+ "invalid compression method in zlib header"
+ "invalid decompressed idat size"
+ "invalid deflate block BTYPE encountered while decoding"
+ "invalid distance code while inflating"
+ "invalid filter strategy given for LodePNGEncoderSettings.filter_strategy"
+ "invalid gAMA chunk size"
+ "invalid pHYs chunk size"
+ "invalid palette index in bKGD chunk. Maybe it came before PLTE chunk?"
+ "invalid sRGB chunk size"
+ "invalid tIME chunk size"
+ "invalid window size given in the settings of the encoder (must be 0-32768)"
+ "jfif"
+ "job_pool::job_pool: %u total threads\n"
+ "job_pool::job_thread: exiting\n"
+ "job_pool::job_thread: starting %u\n"
+ "job_pool::~job_pool\n"
+ "jumped past memory while generating dynamic huffman tree"
+ "jumped past memory while inflating"
+ "jumped past memory while inflating huffman block"
+ "jumped past tree while generating huffman tree"
+ "kaiser"
+ "lanczos12"
+ "lanczos3"
+ "lanczos4"
+ "lanczos6"
+ "lazy matching at pos 0 is impossible"
+ "length of a chunk too long, max allowed for PNG is 2147483647 bytes per chunk"
+ "memory allocation failed"
+ "mitchell"
+ "must provide custom zlib function pointer if LODEPNG_COMPILE_ZLIB is not defined"
+ "no error, everything went ok"
+ "no null termination char found while decoding text chunk"
+ "not allowed to set grayscale ICC profile with colored pixels by PNG specification"
+ "nothing done yet"
+ "pHYs"
+ "problem while processing dynamic deflate block"
+ "quadratic_approx"
+ "quadratic_interp"
+ "quadratic_mix"
+ "raw_decode"
+ "raw_encode"
+ "repeat symbol in tree while there was no value symbol yet"
+ "requested color conversion not supported"
+ "size of zlib data too small"
+ "tEXt"
+ "tIME"
+ "tRNS"
+ "tRNS chunk appeared while it was not allowed for this color type"
+ "tRNS chunk before PLTE or has more entries than palette size"
+ "tRNS chunk has wrong size for RGB image"
+ "tRNS chunk has wrong size for grayscale image"
+ "tent"
+ "text chunk keyword too short or long: must have size 1-79"
+ "tga"
+ "the length of a text chunk keyword given to the encoder is longer than the maximum of 79 bytes"
+ "the length of a text chunk keyword given to the encoder is smaller than the minimum of 1 byte"
+ "the length of the END symbol 256 in the Huffman tree is 0"
+ "the palette is too big"
+ "thread constructor failed"
+ "tried creating a tree of 0 symbols"
+ "tried to encode a PLTE chunk with a palette that has less than 1 or more than 256 colors"
+ "unexisting code while processing dynamic deflate block"
+ "unexisting interlace mode given to encoder (must be 0 or 1)"
+ "unique_lock::lock: already locked"
+ "unique_lock::lock: references null mutex"
+ "unknown chunk type with 'critical' flag encountered by the decoder"
+ "unknown error code"
+ "vector too large\n"
+ "vector: malloc() failed allocating %u bytes"
+ "vector: realloc() failed allocating %u bytes"
+ "video"
+ "while decoding, unexisting compression method encountering in zTXt or iTXt chunk (it must be 0)"
+ "windowsize must be a power of two"
+ "zTXt"
+ "zero width or height is invalid"
+ "{\n"
- "&#x"
- "*** ERROR: CGImageCreateFlexRangeMetadata failed to create gainmapdata (err=%d)\n"
- "*** createPixelDataProviderForExtendedRange failed (nil) - falling back to standard encode\n"
- "*** kCGImageSourceDecodeRequest --> switching to HEIFPlugin\n"
- "A < MQE_A_MIN"
- "ALL"
- "CMPhotoDecompressionContainerCreateImageForIndex(%s)  err=%d\n"
- "MPF"
- "Unknown array indexing step in FollowXPathStep"
- "active && (!checked_out) && !MQ_segment"
- "active && (!checked_out) && MQ_segment"
- "active && checked_out && !MQ_segment"
- "active && checked_out && MQ_segment"
- "check_in"
- "check_out"
- "encode_mag_ref_pass"
- "ktx"
- "mq_decoder.h"
- "x_texels > 0"
- "y_texels > 0"
- "☀️  %s - falling back to IOSurfaceWrapper conversion for '%c%c%c%c'\n"

```
