## JetPack

> `/System/Library/PrivateFrameworks/JetPack.framework/JetPack`

```diff

-7.1.10.2.1
-  __TEXT.__text: 0x1bacc
-  __TEXT.__auth_stubs: 0x7e0
+7.2.9.0.0
+  __TEXT.__text: 0x15220
+  __TEXT.__auth_stubs: 0x800
   __TEXT.__objc_methlist: 0x288
-  __TEXT.__const: 0x21c20
-  __TEXT.__cstring: 0x615
-  __TEXT.__gcc_except_tab: 0x1570
-  __TEXT.__oslogstring: 0x553
-  __TEXT.__unwind_info: 0xb0c
+  __TEXT.__const: 0x1a9f
+  __TEXT.__cstring: 0x4ec
+  __TEXT.__gcc_except_tab: 0x1588
+  __TEXT.__oslogstring: 0x546
+  __TEXT.__unwind_info: 0xa7c
   __TEXT.__eh_frame: 0x38
   __TEXT.__objc_classname: 0x61
   __TEXT.__objc_methname: 0x5cd
   __TEXT.__objc_methtype: 0x1f0
   __TEXT.__objc_stubs: 0x2e0
   __DATA_CONST.__got: 0xc8
-  __DATA_CONST.__const: 0x210
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x4c0
   __DATA_CONST.__objc_selrefs: 0x188
   __AUTH_CONST.__objc_const: 0x240
   __AUTH_CONST.__cfstring: 0x60
-  __AUTH_CONST.__const: 0xc00
-  __AUTH_CONST.__auth_ptr: 0x10
-  __AUTH_CONST.__auth_got: 0x400
+  __AUTH_CONST.__const: 0xc48
+  __AUTH_CONST.__auth_ptr: 0x8
+  __AUTH_CONST.__auth_got: 0x410
   __AUTH.__objc_data: 0x50
-  __AUTH.__const_weak: 0xfd8
-  __DATA.__got_weak: 0x300
+  __AUTH.__const_weak: 0xfd0
+  __DATA.__got_weak: 0x318
   __DATA.__objc_classrefs: 0x40
   __DATA.__objc_superrefs: 0x38
   __DATA.__objc_ivar: 0x38
   __DATA_DIRTY.__objc_data: 0x1e0
-  __DATA_DIRTY.__bss: 0xb0
+  __DATA_DIRTY.__bss: 0xb8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Security.framework/Security
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libc++.1.dylib
+  - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 508
-  Symbols:   1881
-  CStrings:  231
+  Functions: 449
+  Symbols:   1798
+  CStrings:  206
 
Symbols:
+ GCC_except_table32
+ __ZN7JetPack23BrotliDecoderStreamImplINS_27AppleDecompressionInterfaceEE10isFinishedEv
+ __ZN7JetPack23BrotliDecoderStreamImplINS_27AppleDecompressionInterfaceEE4readEPhm
+ __ZN7JetPack23BrotliDecoderStreamImplINS_27AppleDecompressionInterfaceEE8positionEv
+ __ZN7JetPack23BrotliDecoderStreamImplINS_27AppleDecompressionInterfaceEED0Ev
+ __ZN7JetPack23BrotliDecoderStreamImplINS_27AppleDecompressionInterfaceEED1Ev
+ __ZN7JetPack24throwLibArchiveExceptionEP7archiveNSt3__112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEE
+ __ZN7JetPack27AppleDecompressionInterface10isFinishedEv
+ __ZN7JetPack27AppleDecompressionInterface7processEPmPPKhS1_PPhb
+ __ZN7JetPack27AppleDecompressionInterfaceC1Ev
+ __ZN7JetPack27AppleDecompressionInterfaceC2Ev
+ __ZN7JetPack27AppleDecompressionInterfaceD0Ev
+ __ZN7JetPack27AppleDecompressionInterfaceD1Ev
+ __ZN7JetPack27AppleDecompressionInterfaceD2Ev
+ __ZN7JetPack32CompressionUnableToInitExceptionC2Ev
+ __ZN7JetPack32CompressionUnableToInitExceptionD0Ev
+ __ZN7JetPack32CompressionUnableToInitExceptionD1Ev
+ __ZNSt3__110shared_ptrIN7JetPack23BrotliDecoderStreamImplINS1_27AppleDecompressionInterfaceEEEED1B7v160006Ev
+ __ZNSt3__120__shared_ptr_emplaceIN7JetPack23BrotliDecoderStreamImplINS1_27AppleDecompressionInterfaceEEENS_9allocatorIS4_EEE16__on_zero_sharedEv
+ __ZNSt3__120__shared_ptr_emplaceIN7JetPack23BrotliDecoderStreamImplINS1_27AppleDecompressionInterfaceEEENS_9allocatorIS4_EEE21__on_zero_shared_weakEv
+ __ZNSt3__120__shared_ptr_emplaceIN7JetPack23BrotliDecoderStreamImplINS1_27AppleDecompressionInterfaceEEENS_9allocatorIS4_EEEC2B7v160006IJRNS_10shared_ptrINS1_10BaseStreamEEEEEES6_DpOT_
+ __ZNSt3__120__shared_ptr_emplaceIN7JetPack23BrotliDecoderStreamImplINS1_27AppleDecompressionInterfaceEEENS_9allocatorIS4_EEEC2B7v160006IJRNS_10shared_ptrINS1_10BaseStreamEEEEEES6_DpOT_.cold.1
+ __ZNSt3__120__shared_ptr_emplaceIN7JetPack23BrotliDecoderStreamImplINS1_27AppleDecompressionInterfaceEEENS_9allocatorIS4_EEED0Ev
+ __ZNSt3__120__shared_ptr_emplaceIN7JetPack23BrotliDecoderStreamImplINS1_27AppleDecompressionInterfaceEEENS_9allocatorIS4_EEED1Ev
+ __ZTIN7JetPack22DecompressionInterfaceE
+ __ZTIN7JetPack23BrotliDecoderStreamImplINS_27AppleDecompressionInterfaceEEE
+ __ZTIN7JetPack27AppleDecompressionInterfaceE
+ __ZTIN7JetPack32CompressionUnableToInitExceptionE
+ __ZTINSt3__120__shared_ptr_emplaceIN7JetPack23BrotliDecoderStreamImplINS1_27AppleDecompressionInterfaceEEENS_9allocatorIS4_EEEE
+ __ZTSN7JetPack22DecompressionInterfaceE
+ __ZTSN7JetPack23BrotliDecoderStreamImplINS_27AppleDecompressionInterfaceEEE
+ __ZTSN7JetPack27AppleDecompressionInterfaceE
+ __ZTSN7JetPack32CompressionUnableToInitExceptionE
+ __ZTSNSt3__120__shared_ptr_emplaceIN7JetPack23BrotliDecoderStreamImplINS1_27AppleDecompressionInterfaceEEENS_9allocatorIS4_EEEE
+ __ZTVN7JetPack23BrotliDecoderStreamImplINS_27AppleDecompressionInterfaceEEE
+ __ZTVN7JetPack27AppleDecompressionInterfaceE
+ __ZTVN7JetPack32CompressionUnableToInitExceptionE
+ __ZTVNSt3__120__shared_ptr_emplaceIN7JetPack23BrotliDecoderStreamImplINS1_27AppleDecompressionInterfaceEEENS_9allocatorIS4_EEEE
+ _archive_write_disk_set_options
+ _compression_stream_destroy
+ _compression_stream_init
+ _compression_stream_process
- _BrotliBuildCodeLengthsHuffmanTable
- _BrotliBuildHuffmanTable
- _BrotliBuildSimpleHuffmanTable
- _BrotliCalculateRingBufferSize
- _BrotliDecoderCreateInstance
- _BrotliDecoderDecompress
- _BrotliDecoderDecompressStream
- _BrotliDecoderDestroyInstance
- _BrotliDecoderErrorString
- _BrotliDecoderGetErrorCode
- _BrotliDecoderHasMoreOutput
- _BrotliDecoderHuffmanTreeGroupInit
- _BrotliDecoderIsFinished
- _BrotliDecoderIsUsed
- _BrotliDecoderSetParameter
- _BrotliDecoderStateCleanup
- _BrotliDecoderStateCleanupAfterMetablock
- _BrotliDecoderStateInit
- _BrotliDecoderStateMetablockBegin
- _BrotliDecoderTakeOutput
- _BrotliDecoderVersion
- _BrotliDefaultAllocFunc
- _BrotliDefaultFreeFunc
- _BrotliEnsureRingBuffer
- _BrotliGetDictionary
- _BrotliGetTransforms
- _BrotliInitBitReader
- _BrotliSetDictionaryData
- _BrotliTransformDictionaryWord
- _BrotliWarmupBitReader
- _CopyUncompressedBlockToOutput
- _DecodeCommandBlockSwitch
- _DecodeContextMap
- _DecodeDistanceBlockSwitch
- _DecodeLiteralBlockSwitch
- _DecodeMetaBlockLength
- _DecodeVarLenUint8
- _InverseMoveToFrontTransform
- _ProcessCommands
- _ReadHuffmanCode
- _SafeDecodeCommandBlockSwitch
- _SafeDecodeDistanceBlockSwitch
- _SafeDecodeLiteralBlockSwitch
- _SafeDecodeSymbol
- _SafeProcessCommands
- _SaveErrorCode
- _Shift
- _WrapRingBuffer
- _WriteRingBuffer
- __ZN7JetPack19BrotliDecoderStream10getDecoderEv
- __ZN7JetPack19BrotliDecoderStream10isFinishedEv
- __ZN7JetPack19BrotliDecoderStream15fillInputBufferEv
- __ZN7JetPack19BrotliDecoderStream4readEPhm
- __ZN7JetPack19BrotliDecoderStream8positionEv
- __ZN7JetPack19BrotliDecoderStreamC1ENSt3__110shared_ptrINS_10BaseStreamEEEmNS1_10unique_ptrINS_29BrotliDecoderWrapperInterfaceENS1_14default_deleteIS6_EEEE
- __ZN7JetPack19BrotliDecoderStreamC2ENSt3__110shared_ptrINS_10BaseStreamEEEmNS1_10unique_ptrINS_29BrotliDecoderWrapperInterfaceENS1_14default_deleteIS6_EEEE
- __ZN7JetPack19BrotliDecoderStreamC2ENSt3__110shared_ptrINS_10BaseStreamEEEmNS1_10unique_ptrINS_29BrotliDecoderWrapperInterfaceENS1_14default_deleteIS6_EEEE.cold.1
- __ZN7JetPack19BrotliDecoderStreamD0Ev
- __ZN7JetPack19BrotliDecoderStreamD1Ev
- __ZN7JetPack20BrotliDecoderWrapper10isFinishedEv
- __ZN7JetPack20BrotliDecoderWrapper16decompressStreamEPmPPKhS1_PPhS1_
- __ZN7JetPack20BrotliDecoderWrapperC1Ev
- __ZN7JetPack20BrotliDecoderWrapperC2Ev
- __ZN7JetPack20BrotliDecoderWrapperD0Ev
- __ZN7JetPack20BrotliDecoderWrapperD1Ev
- __ZNSt3__110shared_ptrIN7JetPack19BrotliDecoderStreamEED1B7v160006Ev
- __ZNSt3__120__shared_ptr_emplaceIN7JetPack19BrotliDecoderStreamENS_9allocatorIS2_EEE16__on_zero_sharedEv
- __ZNSt3__120__shared_ptr_emplaceIN7JetPack19BrotliDecoderStreamENS_9allocatorIS2_EEE21__on_zero_shared_weakEv
- __ZNSt3__120__shared_ptr_emplaceIN7JetPack19BrotliDecoderStreamENS_9allocatorIS2_EEEC2B7v160006IJRNS_10shared_ptrINS1_10BaseStreamEEEEEES4_DpOT_
- __ZNSt3__120__shared_ptr_emplaceIN7JetPack19BrotliDecoderStreamENS_9allocatorIS2_EEEC2B7v160006IJRNS_10shared_ptrINS1_10BaseStreamEEEEEES4_DpOT_.cold.1
- __ZNSt3__120__shared_ptr_emplaceIN7JetPack19BrotliDecoderStreamENS_9allocatorIS2_EEED0Ev
- __ZNSt3__120__shared_ptr_emplaceIN7JetPack19BrotliDecoderStreamENS_9allocatorIS2_EEED1Ev
- __ZTIN7JetPack19BrotliDecoderStreamE
- __ZTIN7JetPack20BrotliDecoderWrapperE
- __ZTIN7JetPack29BrotliDecoderWrapperInterfaceE
- __ZTINSt3__120__shared_ptr_emplaceIN7JetPack19BrotliDecoderStreamENS_9allocatorIS2_EEEE
- __ZTSN7JetPack19BrotliDecoderStreamE
- __ZTSN7JetPack20BrotliDecoderWrapperE
- __ZTSN7JetPack29BrotliDecoderWrapperInterfaceE
- __ZTSNSt3__120__shared_ptr_emplaceIN7JetPack19BrotliDecoderStreamENS_9allocatorIS2_EEEE
- __ZTVN7JetPack19BrotliDecoderStreamE
- __ZTVN7JetPack20BrotliDecoderWrapperE
- __ZTVNSt3__120__shared_ptr_emplaceIN7JetPack19BrotliDecoderStreamENS_9allocatorIS2_EEEE
- __kBrotliContextLookupTable
- __kBrotliPrefixCodeRanges
- _free
- _kBrotliDictionary
- _kBrotliDictionaryData
- _kBrotliTransforms
- _kCmdLut
- _kCodeLengthCodeOrder
- _kCodeLengthPrefixLength
- _kCodeLengthPrefixValue
- _kPrefixSuffix
- _kPrefixSuffixMap
- _kTransformsData
- _malloc_type_malloc
CStrings:
+ "CompressionUnableToInitException"
+ "Failed to %{public}s: %{public}s"
+ "Unable to destroy compression stream"
+ "create file on disk"
+ "set archive writer options"
+ "set standard settings"
+ "write file to disk"
- "BLOCK_LENGTH_1"
- "BLOCK_LENGTH_2"
- "BLOCK_TYPE_TREES"
- "CL_SPACE"
- "CONTEXT_MAP"
- "CONTEXT_MAP_REPEAT"
- "CONTEXT_MODES"
- "DICTIONARY"
- "DICTIONARY_NOT_SET"
- "DISTANCE"
- "EXUBERANT_META_NIBBLE"
- "EXUBERANT_NIBBLE"
- "Failed to create file on disk: %{public}s"
- "Failed to write file to disk: %{public}s"
- "HUFFMAN_SPACE"
- "INVALID"
- "INVALID_ARGUMENTS"
- "NEEDS_MORE_INPUT"
- "NEEDS_MORE_OUTPUT"
- "NO_ERROR"
- "PADDING_1"
- "PADDING_2"
- "RESERVED"
- "RING_BUFFER_1"
- "RING_BUFFER_2"
- "SIMPLE_HUFFMAN_ALPHABET"
- "SIMPLE_HUFFMAN_SAME"
- "SUCCESS"
- "TRANSFORM"
- "TREE_GROUPS"
- "UNREACHABLE"
- "WINDOW_BITS"

```
