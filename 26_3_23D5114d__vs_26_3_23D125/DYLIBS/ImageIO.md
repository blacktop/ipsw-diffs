## ImageIO

> `/System/Library/Frameworks/ImageIO.framework/ImageIO`

```diff

-2784.3.4.1.0
-  __TEXT.__text: 0x46611c
+2784.3.7.0.0
+  __TEXT.__text: 0x46822c
   __TEXT.__auth_stubs: 0x4250
   __TEXT.__objc_methlist: 0xd20
-  __TEXT.__const: 0x31330
+  __TEXT.__const: 0x32350
   __TEXT.__gcc_except_tab: 0x26758
-  __TEXT.__cstring: 0x9d27a
+  __TEXT.__cstring: 0x9d43d
   __TEXT.__oslogstring: 0x17
   __TEXT.__ustring: 0x30
-  __TEXT.__unwind_info: 0xebb8
+  __TEXT.__unwind_info: 0xec00
   __TEXT.__eh_frame: 0x358
   __TEXT.__objc_classname: 0xe0
   __TEXT.__objc_methname: 0x2e13

   __AUTH.__data: 0x1d0
   __DATA.__objc_ivar: 0x9c
   __DATA.__data: 0x3228
-  __DATA.__bss: 0x4f60
-  __DATA.__common: 0x3618
+  __DATA.__bss: 0x51f0
+  __DATA.__common: 0x3628
   __DATA_DIRTY.__data: 0x168
   __DATA_DIRTY.__crash_info: 0x148
   __DATA_DIRTY.__common: 0xe03

   - /usr/lib/libexpat.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 3D835956-CDBA-321C-AD2D-8E4D4892224B
-  Functions: 14910
-  Symbols:   45246
-  CStrings:  24863
+  UUID: C7F3146A-E2E3-36BE-A305-2C6A3BA8D25F
+  Functions: 14963
+  Symbols:   45349
+  CStrings:  24884
 
Symbols:
+ _BuildHuffmanTable.cold.7
+ _ConvertBGRToY_C
+ _ConvertBGRToY_NEON
+ _ConvertRGBToY_C
+ _ConvertRGBToY_NEON
+ _Decode
+ _GetColorPalette
+ _GetColorPalette.cold.1
+ _ImportYUVAFromRGBALastLine_C
+ _ImportYUVAFromRGBA_C
+ _InitGetCoeffs_body_last_cpuinfo_used
+ _IsValidColorspace
+ _PaletteCompareColorsForQsort
+ _PaletteCompareColorsForQsort.cold.1
+ _ProcessRows.cold.10
+ _ProcessRows.cold.11
+ _VP8CheckSignature
+ _VP8DspInit_body_last_cpuinfo_used
+ _VP8FiltersInit_body_last_cpuinfo_used
+ _VP8LDspInit_body_last_cpuinfo_used
+ _WebPAccumulateRGB
+ _WebPAccumulateRGB.cold.1
+ _WebPAccumulateRGB.cold.2
+ _WebPAccumulateRGB.cold.3
+ _WebPAccumulateRGB.cold.4
+ _WebPAccumulateRGB.cold.5
+ _WebPAccumulateRGB.cold.6
+ _WebPAccumulateRGBA
+ _WebPAccumulateRGBA.cold.1
+ _WebPAccumulateRGBA.cold.10
+ _WebPAccumulateRGBA.cold.11
+ _WebPAccumulateRGBA.cold.12
+ _WebPAccumulateRGBA.cold.13
+ _WebPAccumulateRGBA.cold.14
+ _WebPAccumulateRGBA.cold.15
+ _WebPAccumulateRGBA.cold.16
+ _WebPAccumulateRGBA.cold.17
+ _WebPAccumulateRGBA.cold.18
+ _WebPAccumulateRGBA.cold.2
+ _WebPAccumulateRGBA.cold.3
+ _WebPAccumulateRGBA.cold.4
+ _WebPAccumulateRGBA.cold.5
+ _WebPAccumulateRGBA.cold.6
+ _WebPAccumulateRGBA.cold.7
+ _WebPAccumulateRGBA.cold.8
+ _WebPAccumulateRGBA.cold.9
+ _WebPAnimDecoderGetDemuxer
+ _WebPAnimDecoderGetNext.cold.2
+ _WebPAnimDecoderGetNext.cold.3
+ _WebPAnimDecoderReset
+ _WebPAnimDecoderRestoreCanvas
+ _WebPAnimDecoderRestoreCanvas.cold.1
+ _WebPAnimDecoderRestoreCanvas.cold.2
+ _WebPAnimDecoderSkipFrame
+ _WebPConvertBGRToY
+ _WebPConvertRGBToY
+ _WebPCopyDecBuffer
+ _WebPCopyPixels
+ _WebPCopyPixels.cold.1
+ _WebPCopyPixels.cold.2
+ _WebPCopyPixels.cold.3
+ _WebPDecodeARGB
+ _WebPDecodeARGBInto
+ _WebPDecodeBGR
+ _WebPDecodeBGRA
+ _WebPDecodeBGRInto
+ _WebPDecodeRGB
+ _WebPDecodeRGBA
+ _WebPDecodeYUV
+ _WebPDecodeYUV.cold.1
+ _WebPDecodeYUVInto
+ _WebPDemuxNextChunk
+ _WebPDemuxNextFrame
+ _WebPDemuxPrevChunk
+ _WebPDemuxPrevFrame
+ _WebPFree
+ _WebPGetColorPalette
+ _WebPGetDecoderVersion
+ _WebPGetDemuxVersion
+ _WebPGetInfo
+ _WebPImportYUVAFromRGBA
+ _WebPImportYUVAFromRGBALastLine
+ _WebPInitAlphaProcessing_body_last_cpuinfo_used
+ _WebPInitConvertARGBToYUV_body_last_cpuinfo_used
+ _WebPInitGammaTables
+ _WebPInitGammaTables_body_last_cpuinfo_used
+ _WebPInitSamplers_body_last_cpuinfo_used
+ _WebPInitUpsamplers_body_last_cpuinfo_used
+ _WebPInitYUV444Converters_body_last_cpuinfo_used
+ _WebPMalloc
+ _WebPRescalerDspInit_body_last_cpuinfo_used
+ _WebPSafeCalloc
+ _WebPSafeCalloc.cold.1
+ _WebPSafeFree
+ _WebPSafeMalloc
+ _WebPSafeMalloc.cold.1
+ _WebPSetWorkerInterface
+ _WebPValidateDecoderConfig
+ _kGammaTablesOk
+ _kGammaToLinearTab
+ _kInvAlpha
+ _kLinearToGammaTab
- _ConvertBGR24ToY_C
- _ConvertBGR24ToY_NEON
- _ConvertRGB24ToY_C
- _ConvertRGB24ToY_NEON
- _ConvertToYUVA
- _CopyCanvas
- _CopyCanvas.cold.1
- _InitGetCoeffs.InitGetCoeffs_body_last_cpuinfo_used
- _VP8DspInit.VP8DspInit_body_last_cpuinfo_used
- _VP8FiltersInit.VP8FiltersInit_body_last_cpuinfo_used
- _VP8LDspInit.VP8LDspInit_body_last_cpuinfo_used
- _WebPConvertBGR24ToY
- _WebPConvertRGB24ToY
- _WebPInitAlphaProcessing.WebPInitAlphaProcessing_body_last_cpuinfo_used
- _WebPInitConvertARGBToYUV.WebPInitConvertARGBToYUV_body_last_cpuinfo_used
- _WebPInitSamplers.WebPInitSamplers_body_last_cpuinfo_used
- _WebPInitUpsamplers.WebPInitUpsamplers_body_last_cpuinfo_used
- _WebPInitYUV444Converters.WebPInitYUV444Converters_body_last_cpuinfo_used
- _WebPRescalerDspInit.WebPRescalerDspInit_body_last_cpuinfo_used
CStrings:
+ "!dec->incremental || (br->eos && src < src_last) || src >= src_last"
+ "(key >> cc->hash_bits) == 0u"
+ "(uint64_t)sum * kInvAlpha[total_a] < ((uint64_t)1 << 32)"
+ "EmitRowsYUVA"
+ "GetColorPalette"
+ "Interpolate"
+ "LinearToGammaWeighted"
+ "PaletteCompareColorsForQsort"
+ "WebPConvertBGRToY != NULL"
+ "WebPConvertRGBToY != NULL"
+ "WebPCopyPixels"
+ "WebPDecodeYUV"
+ "WebPSafeCalloc"
+ "WebPSafeMalloc"
+ "WebPUnfilters[alph_dec->filter] != NULL"
+ "a != b"
+ "alph_dec->vp8l_dec != NULL"
+ "br != NULL && br->buf != NULL"
+ "br->bit_pos >= VP8L_WBITS"
+ "br->pos <= br->len"
+ "buf->u_stride == buf->v_stride"
+ "current_end % step == 0"
+ "dec->alpha_plane_mem == NULL"
+ "dec->hdr.htree_groups != NULL"
+ "dec->hdr.huffman_tables.root.start != NULL"
+ "dec->hdr.num_htree_groups > 0"
+ "dec->incremental"
+ "dec->incremental || error != VP8_STATUS_SUSPENDED"
+ "dec->last_out_row <= output->height"
+ "dec->last_row < last_row"
+ "dec->last_row <= dec->height"
+ "dec->method == ALPHA_LOSSLESS_COMPRESSION"
+ "dec->next_transform <= NUM_TRANSFORMS"
+ "dec->next_transform == 1"
+ "dec->output != NULL"
+ "dec->ready"
+ "dec->status != VP8_STATUS_OK"
+ "dec->width <= final_width"
+ "dec->width > 0 && dec->height > 0"
+ "deltas <= &dec->alpha_data[dec->alpha_data_size]"
+ "last_row <= dec->height"
+ "last_row <= dec->io->crop_bottom"
+ "mem <= (uint8_t*)dec->mem + dec->mem_size"
+ "meta_index < hdr->num_htree_groups"
+ "nmemb * size > 0"
+ "offset[symbol_code_length] < code_lengths_size"
+ "palette.c"
+ "pic->use_argb"
+ "row <= dec->io->crop_bottom"
+ "row_end <= transform->ysize"
+ "src->hash_bits == dst->hash_bits"
+ "src->use_argb && dst->use_argb"
+ "src->width == dst->width && src->height == dst->height"
+ "tab_pos + 1 < GAMMA_TAB_SIZE + 1"
+ "transform->type == COLOR_INDEXING_TRANSFORM"
+ "worker->impl == NULL"
+ "worker->status <= OK"
+ "worker->status == OK"
+ "y_pos % 2 == 0"
+ "y_pos + 1 == y_pos_final"
- "!dec->incremental_ || (br->eos_ && src < src_last) || src >= src_last"
- "(key >> cc->hash_bits_) == 0u"
- "WebPConvertBGR24ToY != NULL"
- "WebPConvertRGB24ToY != NULL"
- "WebPUnfilters[alph_dec->filter_] != NULL"
- "alph_dec->vp8l_dec_ != NULL"
- "br != NULL && br->buf_ != NULL"
- "br->bit_pos_ >= VP8L_WBITS"
- "br->pos_ <= br->len_"
- "dec->alpha_plane_mem_ == NULL"
- "dec->hdr_.htree_groups_ != NULL"
- "dec->hdr_.huffman_tables_.root.start != NULL"
- "dec->hdr_.num_htree_groups_ > 0"
- "dec->incremental_"
- "dec->incremental_ || error != VP8_STATUS_SUSPENDED"
- "dec->last_out_row_ <= output->height"
- "dec->last_row_ < last_row"
- "dec->last_row_ <= dec->height_"
- "dec->method_ == ALPHA_LOSSLESS_COMPRESSION"
- "dec->next_transform_ <= NUM_TRANSFORMS"
- "dec->next_transform_ == 1"
- "dec->output_ != NULL"
- "dec->ready_"
- "dec->status_ != VP8_STATUS_OK"
- "dec->width_ <= final_width"
- "dec->width_ > 0 && dec->height_ > 0"
- "deltas <= &dec->alpha_data_[dec->alpha_data_size_]"
- "end % step == 0"
- "last_row <= dec->height_"
- "last_row <= dec->io_->crop_bottom"
- "mem <= (uint8_t*)dec->mem_ + dec->mem_size_"
- "meta_index < hdr->num_htree_groups_"
- "row <= dec->io_->crop_bottom"
- "row_end <= transform->ysize_"
- "src->hash_bits_ == dst->hash_bits_"
- "transform->type_ == COLOR_INDEXING_TRANSFORM"
- "worker->impl_ == NULL"
- "worker->status_ <= OK"
- "worker->status_ == OK"

```
