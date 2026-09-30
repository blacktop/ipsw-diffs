## libcompression.dylib

> `/usr/lib/libcompression.dylib`

```diff

-  __TEXT.__text: 0x65200
+  __TEXT.__text: 0x6501c
   __TEXT.__const: 0x76e91
   __TEXT.__cstring: 0x2ec
   __TEXT.__unwind_info: 0x700
Sections:
~ __TEXT.__unwind_info : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__const : content changed
~ __AUTH_CONST.__const : content changed
~ __DATA.__data : content changed
Functions:
~ _adler32 : 316 -> 308
~ _longest_match : 472 -> 484
~ _build_tree : 1168 -> 1184
~ _lzvn_decode_scratch_size : 8 -> 52
~ _zero_coder_encode : 320 -> 332
~ _BrotliBuildHuffmanTable : 560 -> 568
~ _CountsCreateWithBuffer : 404 -> 396
~ _lzx_huffman_tree_read_code : 308 -> 276
~ _lzx_huffman_tree_update_tree_using_pre_tree_encoding : 796 -> 748
~ _lzx_huffman_create_pre_tree : 272 -> 256
~ _RavGetOptimal : 4816 -> 4860
~ _BrotliSplitBlock : 13976 -> 13952
~ _BrotliSafeReadBits32Slow : 328 -> 304
~ _BrotliDecoderDecompressStream : 4016 -> 4004
~ _DecodeVarLenUint8 : 456 -> 444
~ _DecodeContextMap : 1108 -> 1084
~ _SafeProcessCommands : 2844 -> 2796
~ _SafeDecodeCommandBlockSwitch : 808 -> 784
~ _SafeDecodeLiteralBlockSwitch : 884 -> 860
~ _SafeDecodeDistanceBlockSwitch : 832 -> 808
~ _lzbitmap_decode : 2200 -> 2208
~ _yzip_jobs_encode : 1256 -> 1272
~ _LZFSEIBootBufferPushN : 224 -> 212
~ _BrotliHistogramCombineLiteral : 744 -> 748
~ _BrotliHistogramCombineCommand : 748 -> 752
~ _BrotliHistogramCombineDistance : 748 -> 752
~ _ComputeShortestPathFromNodes : 128 -> 104
~ _BrotliBuildAndStoreHuffmanTreeFast : 1792 -> 1784
~ _smb_lz77_encode_buffer : 892 -> 900
~ _cosmix_model_create : 312 -> 304
~ _lzx_decode_buffer : 2388 -> 2292
~ _CreateBackwardReferencesNH35 : 3608 -> 3588
~ _CreateBackwardReferencesNH55 : 3632 -> 3600
~ _CreateBackwardReferencesNH65 : 5528 -> 5372
~ _crc32 : 808 -> 828
~ _yzip_plane_encoder_phase1 : 1872 -> 1868
~ _deflate_rle : 828 -> 832

```
