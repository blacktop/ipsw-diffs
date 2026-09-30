## EmbeddingCore

> `/System/Library/PrivateFrameworks/EmbeddingCore.framework/Versions/A/EmbeddingCore`

```diff

-  __TEXT.__text: 0x6ea9c
+  __TEXT.__text: 0x6e6c4
   __TEXT.__objc_methlist: 0x1c74
   __TEXT.__const: 0x1150
   __TEXT.__gcc_except_tab: 0x7128

   __DATA_CONST.__objc_selrefs: 0xe88
   __DATA_CONST.__objc_superrefs: 0xc8
   __DATA_CONST.__objc_arraydata: 0x3a0
-  __DATA_CONST.__got: 0x3c0
+  __DATA_CONST.__got: 0x3d0
   __AUTH_CONST.__const: 0x1c20
   __AUTH_CONST.__cfstring: 0x1ae0
   __AUTH_CONST.__objc_const: 0x3f08

   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH_CONST.__auth_got: 0x960
-  __AUTH.__objc_data: 0xc70
-  __AUTH.__data: 0x180
+  __AUTH.__objc_data: 0x50
+  __AUTH.__data: 0xe0
   __AUTH.__thread_vars: 0x48
   __AUTH.__thread_data: 0x40
   __AUTH.__thread_bss: 0x10
   __DATA.__objc_ivar: 0x2a0
-  __DATA.__data: 0x2dc
-  __DATA.__bss: 0x221
-  __DATA.__common: 0x325
-  __DATA_DIRTY.__objc_data: 0x6e0
-  __DATA_DIRTY.__data: 0x90
-  __DATA_DIRTY.__bss: 0x60
-  __DATA_DIRTY.__common: 0xc1
+  __DATA.__data: 0x2d4
+  __DATA.__bss: 0x1b1
+  __DATA.__common: 0x2fd
+  __DATA_DIRTY.__objc_data: 0x1300
+  __DATA_DIRTY.__data: 0x138
+  __DATA_DIRTY.__bss: 0xd8
+  __DATA_DIRTY.__common: 0xe9
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/Versions/A/CoreGraphics
   - /System/Library/Frameworks/CoreImage.framework/Versions/A/CoreImage
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__const : content changed
~ __TEXT.__gcc_except_tab : content changed
~ __TEXT.__cstring : content changed
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__unwind_info : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__weak_got : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH_CONST.__weak_auth_got : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __AUTH_CONST.__objc_floatobj : content changed
~ __AUTH.__thread_vars : content changed
Functions:
~ -[MADTextEncoderE5ML getTokenEmbeddingsforChunks:truncatedInput:error:] : 1188 -> 1168
~ -[MADTextEncoderE5ML _unsafeRunOnInput:completion:] : 8728 -> 8712
~ __ZNSt3__15dequeIZNK5Darts15DoubleArrayImplIvvivE16predictiveSearchINS3_16result_pair_typeEEEmPKcPT_mmiE5StateNS_9allocatorISA_EEE19__add_back_capacityEv : 480 -> 468
~ __ZNKSt3__121__murmur2_or_cityhashImLm64EEclB9nqe220106EPKvm : 532 -> 520
~ __ZN13sentencepiece22SentencePieceProcessor4LoadENSt3__110unique_ptrINS_10ModelProtoENS1_14default_deleteIS3_EEEE : 2380 -> 2372
~ __ZNK13sentencepiece22SentencePieceProcessor17ParseExtraOptionsENSt3__117basic_string_viewIcNS1_11char_traitsIcEEEEPNS1_6vectorINS0_11ExtraOptionENS1_9allocatorIS7_EEEE : 2152 -> 2124
~ __ZNK13sentencepiece22SentencePieceProcessor17ApplyExtraOptionsERKNSt3__16vectorINS0_11ExtraOptionENS1_9allocatorIS3_EEEEPNS_17SentencePieceTextE : 1480 -> 1472
~ __ZN13sentencepiece7unigram7Lattice7ViterbiEv : 704 -> 692
~ __ZN13sentencepiece7unigram7Lattice6SampleEf : 900 -> 884
~ __ZNK13sentencepiece7unigram5Model15EncodeOptimizedENSt3__117basic_string_viewIcNS2_11char_traitsIcEEEE : 1160 -> 1164
~ __ZNK13sentencepiece7unigram5Model20SampleEncodeAndScoreENSt3__117basic_string_viewIcNS2_11char_traitsIcEEEEfibb : 2972 -> 2964
~ __ZNK13sentencepiece4word5Model6EncodeENSt3__117basic_string_viewIcNS2_11char_traitsIcEEEE : 380 -> 356
~ __ZNK13sentencepiece31SentencePieceText_SentencePiece18_InternalSerializeEPhPN6google8protobuf2io19EpsCopyOutputStreamE : 708 -> 684
~ __ZN6google8protobuf2io19EpsCopyOutputStream23WriteStringMaybeAliasedEjRKNSt3__112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEPh : 304 -> 292
~ __ZNK13sentencepiece17SentencePieceText18_InternalSerializeEPhPN6google8protobuf2io19EpsCopyOutputStreamE : 500 -> 492
~ __ZNK13sentencepiece22NBestSentencePieceText18_InternalSerializeEPhPN6google8protobuf2io19EpsCopyOutputStreamE : 368 -> 360
~ __ZNK13sentencepiece11TrainerSpec18_InternalSerializeEPhPN6google8protobuf2io19EpsCopyOutputStreamE : 4612 -> 4484
~ __ZNK13sentencepiece12SelfTestData18_InternalSerializeEPhPN6google8protobuf2io19EpsCopyOutputStreamE : 396 -> 388
~ __ZNK13sentencepiece24ModelProto_SentencePiece18_InternalSerializeEPhPN6google8protobuf2io19EpsCopyOutputStreamE : 432 -> 424
~ __ZNK13sentencepiece10ModelProto18_InternalSerializeEPhPN6google8protobuf2io19EpsCopyOutputStreamE : 1040 -> 1000
~ __ZNKSt3__114default_deleteIN13sentencepiece4util6Status3RepEEclB9nqe220106EPS4_ : 108 -> 120
~ __ZN6google8protobuf2io19EpsCopyOutputStream30WriteStringMaybeAliasedOutlineEjRKNSt3__112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEPh : 396 -> 388
~ __ZN6google8protobuf2io19EpsCopyOutputStream18WriteStringOutlineEjRKNSt3__112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEPh : 436 -> 428
~ __ZNK6google8protobuf8internal12ExtensionSet13IsInitializedEv : 212 -> 208
~ __ZNK6google8protobuf8internal12ExtensionSet9Extension44InternalSerializeFieldWithCachedSizesToArrayEiPhPNS0_2io19EpsCopyOutputStreamE : 11144 -> 10532
~ __ZN6google8protobuf8internal12ShutdownDataD2Ev : 164 -> 168
~ __ZN6google8protobuf8internal18EpsCopyInputStream10NextBufferEii : 1064 -> 1068
~ __ZN6google8protobuf8internal17VarintParseSlow32EPKcj : 104 -> 116
~ __ZN6google8protobuf8internal16WireFormatParserINS1_28UnknownFieldLiteParserHelperEEEPKcRT_S5_PNS1_12ParseContextE : 248 -> 252
~ __ZN6google8protobuf8internal11VarintParseIyEEPKcS4_PT_ : 124 -> 128
~ __ZN6google8protobuf8internal16ReadSizeFallbackEPKcj : 120 -> 124
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6v9Nws/Sources/SentencePiece/src/builtin_pb/sentencepiece.pb.cc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6v9Nws/Sources/SentencePiece/src/builtin_pb/sentencepiece_model.pb.cc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6v9Nws/Sources/SentencePiece/src/builtin_pb/sentencepiece_model.pb.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6v9Nws/Sources/SentencePiece/src/filesystem.cc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6v9Nws/Sources/SentencePiece/src/mmap.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6v9Nws/Sources/SentencePiece/src/model_factory.cc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6v9Nws/Sources/SentencePiece/src/model_interface.cc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6v9Nws/Sources/SentencePiece/src/model_interface.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6v9Nws/Sources/SentencePiece/src/normalizer.cc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6v9Nws/Sources/SentencePiece/src/sentencepiece_processor.cc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6v9Nws/Sources/SentencePiece/src/unigram_model.cc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6v9Nws/Sources/SentencePiece/src/util.cc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6v9Nws/Sources/SentencePiece/src/util.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6v9Nws/Sources/SentencePiece/third_party/darts_clone/darts.h:1111: exception: failed to insert key: negative value"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6v9Nws/Sources/SentencePiece/third_party/darts_clone/darts.h:1113: exception: failed to insert key: zero-length key"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6v9Nws/Sources/SentencePiece/third_party/darts_clone/darts.h:1127: exception: failed to insert key: invalid null character"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6v9Nws/Sources/SentencePiece/third_party/darts_clone/darts.h:1132: exception: failed to insert key: wrong key order"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6v9Nws/Sources/SentencePiece/third_party/darts_clone/darts.h:1344: exception: failed to modify unit: too large offset"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6v9Nws/Sources/SentencePiece/third_party/darts_clone/darts.h:1680: exception: failed to build double-array: invalid null character"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6v9Nws/Sources/SentencePiece/third_party/darts_clone/darts.h:1682: exception: failed to build double-array: negative value"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6v9Nws/Sources/SentencePiece/third_party/darts_clone/darts.h:1697: exception: failed to build double-array: wrong key order"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6v9Nws/Sources/SentencePiece/third_party/darts_clone/darts.h:748: exception: failed to resize pool: std::bad_alloc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6v9Nws/Sources/SentencePiece/third_party/darts_clone/darts.h:864: exception: failed to build rank index: std::bad_alloc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6v9Nws/Sources/SentencePiece/third_party/protobuf-lite/arena.cc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6v9Nws/Sources/SentencePiece/third_party/protobuf-lite/arenastring.cc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6v9Nws/Sources/SentencePiece/third_party/protobuf-lite/coded_stream.cc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6v9Nws/Sources/SentencePiece/third_party/protobuf-lite/common.cc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6v9Nws/Sources/SentencePiece/third_party/protobuf-lite/extension_set.cc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6v9Nws/Sources/SentencePiece/third_party/protobuf-lite/generated_message_util.cc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6v9Nws/Sources/SentencePiece/third_party/protobuf-lite/google/protobuf/arena_impl.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6v9Nws/Sources/SentencePiece/third_party/protobuf-lite/google/protobuf/arenastring.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6v9Nws/Sources/SentencePiece/third_party/protobuf-lite/google/protobuf/extension_set_inl.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6v9Nws/Sources/SentencePiece/third_party/protobuf-lite/google/protobuf/io/coded_stream.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6v9Nws/Sources/SentencePiece/third_party/protobuf-lite/google/protobuf/parse_context.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6v9Nws/Sources/SentencePiece/third_party/protobuf-lite/google/protobuf/repeated_field.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6v9Nws/Sources/SentencePiece/third_party/protobuf-lite/message_lite.cc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.6v9Nws/Sources/SentencePiece/third_party/protobuf-lite/parse_context.cc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.n7kZs2/Sources/MediaAnalysis_Embedding/EmbeddingCore/Common/CNNModelEspressoV2.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.n7kZs2/Sources/MediaAnalysis_Embedding/EmbeddingCore/Common/CNNModelEspressoV2Data.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.n7kZs2/Sources/MediaAnalysis_Embedding/EmbeddingCore/Text/MADCrossEncoder.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.n7kZs2/Sources/MediaAnalysis_Embedding/EmbeddingCore/Text/MADTextEmbeddingSafety.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.n7kZs2/Sources/MediaAnalysis_Embedding/EmbeddingCore/Text/MADTextEmbeddingThreshold.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.n7kZs2/Sources/MediaAnalysis_Embedding/EmbeddingCore/Text/MADTextLexiconSafety.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.56j0m3/Sources/SentencePiece/src/builtin_pb/sentencepiece.pb.cc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.56j0m3/Sources/SentencePiece/src/builtin_pb/sentencepiece_model.pb.cc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.56j0m3/Sources/SentencePiece/src/builtin_pb/sentencepiece_model.pb.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.56j0m3/Sources/SentencePiece/src/filesystem.cc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.56j0m3/Sources/SentencePiece/src/mmap.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.56j0m3/Sources/SentencePiece/src/model_factory.cc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.56j0m3/Sources/SentencePiece/src/model_interface.cc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.56j0m3/Sources/SentencePiece/src/model_interface.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.56j0m3/Sources/SentencePiece/src/normalizer.cc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.56j0m3/Sources/SentencePiece/src/sentencepiece_processor.cc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.56j0m3/Sources/SentencePiece/src/unigram_model.cc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.56j0m3/Sources/SentencePiece/src/util.cc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.56j0m3/Sources/SentencePiece/src/util.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.56j0m3/Sources/SentencePiece/third_party/darts_clone/darts.h:1111: exception: failed to insert key: negative value"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.56j0m3/Sources/SentencePiece/third_party/darts_clone/darts.h:1113: exception: failed to insert key: zero-length key"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.56j0m3/Sources/SentencePiece/third_party/darts_clone/darts.h:1127: exception: failed to insert key: invalid null character"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.56j0m3/Sources/SentencePiece/third_party/darts_clone/darts.h:1132: exception: failed to insert key: wrong key order"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.56j0m3/Sources/SentencePiece/third_party/darts_clone/darts.h:1344: exception: failed to modify unit: too large offset"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.56j0m3/Sources/SentencePiece/third_party/darts_clone/darts.h:1680: exception: failed to build double-array: invalid null character"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.56j0m3/Sources/SentencePiece/third_party/darts_clone/darts.h:1682: exception: failed to build double-array: negative value"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.56j0m3/Sources/SentencePiece/third_party/darts_clone/darts.h:1697: exception: failed to build double-array: wrong key order"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.56j0m3/Sources/SentencePiece/third_party/darts_clone/darts.h:748: exception: failed to resize pool: std::bad_alloc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.56j0m3/Sources/SentencePiece/third_party/darts_clone/darts.h:864: exception: failed to build rank index: std::bad_alloc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.56j0m3/Sources/SentencePiece/third_party/protobuf-lite/arena.cc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.56j0m3/Sources/SentencePiece/third_party/protobuf-lite/arenastring.cc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.56j0m3/Sources/SentencePiece/third_party/protobuf-lite/coded_stream.cc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.56j0m3/Sources/SentencePiece/third_party/protobuf-lite/common.cc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.56j0m3/Sources/SentencePiece/third_party/protobuf-lite/extension_set.cc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.56j0m3/Sources/SentencePiece/third_party/protobuf-lite/generated_message_util.cc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.56j0m3/Sources/SentencePiece/third_party/protobuf-lite/google/protobuf/arena_impl.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.56j0m3/Sources/SentencePiece/third_party/protobuf-lite/google/protobuf/arenastring.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.56j0m3/Sources/SentencePiece/third_party/protobuf-lite/google/protobuf/extension_set_inl.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.56j0m3/Sources/SentencePiece/third_party/protobuf-lite/google/protobuf/io/coded_stream.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.56j0m3/Sources/SentencePiece/third_party/protobuf-lite/google/protobuf/parse_context.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.56j0m3/Sources/SentencePiece/third_party/protobuf-lite/google/protobuf/repeated_field.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.56j0m3/Sources/SentencePiece/third_party/protobuf-lite/message_lite.cc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.56j0m3/Sources/SentencePiece/third_party/protobuf-lite/parse_context.cc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.yEFbXz/Sources/MediaAnalysis_Embedding/EmbeddingCore/Common/CNNModelEspressoV2.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.yEFbXz/Sources/MediaAnalysis_Embedding/EmbeddingCore/Common/CNNModelEspressoV2Data.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.yEFbXz/Sources/MediaAnalysis_Embedding/EmbeddingCore/Text/MADCrossEncoder.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.yEFbXz/Sources/MediaAnalysis_Embedding/EmbeddingCore/Text/MADTextEmbeddingSafety.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.yEFbXz/Sources/MediaAnalysis_Embedding/EmbeddingCore/Text/MADTextEmbeddingThreshold.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.yEFbXz/Sources/MediaAnalysis_Embedding/EmbeddingCore/Text/MADTextLexiconSafety.mm"

```
