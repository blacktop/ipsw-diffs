## EmbeddedAcousticRecognition

> `/System/Library/PrivateFrameworks/EmbeddedAcousticRecognition.framework/Versions/A/EmbeddedAcousticRecognition`

### Sections with Same Size but Changed Content

- `__TEXT.__oslogstring`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_capture`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__weak_got`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_floatobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH.__data`
- `__AUTH.__thread_vars`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-3600.69.1.0.0
-  __TEXT.__text: 0xaf3fc0
-  __TEXT.__objc_methlist: 0x6a6c
-  __TEXT.__const: 0x5e738
-  __TEXT.__gcc_except_tab: 0xbfdd4
-  __TEXT.__cstring: 0x79f65
+3600.71.1.0.0
+  __TEXT.__text: 0xaf59bc
+  __TEXT.__objc_methlist: 0x6ae4
+  __TEXT.__const: 0x5e748
+  __TEXT.__gcc_except_tab: 0xc0074
+  __TEXT.__cstring: 0x79f95
   __TEXT.__oslogstring: 0x3131
   __TEXT.__ustring: 0xa8
   __TEXT.__dlopen_cstrs: 0x60

   __TEXT.__swift_as_ret: 0x1c
   __TEXT.__swift_as_cont: 0x28
   __TEXT.__swift5_capture: 0x114
-  __TEXT.__unwind_info: 0x3b540
+  __TEXT.__unwind_info: 0x3b590
   __TEXT.__eh_frame: 0x520
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x1a08
-  __DATA_CONST.__objc_classlist: 0x560
+  __DATA_CONST.__objc_classlist: 0x568
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x20
-  __DATA_CONST.__objc_selrefs: 0x3620
+  __DATA_CONST.__objc_selrefs: 0x3638
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x3d0
+  __DATA_CONST.__objc_superrefs: 0x3d8
   __DATA_CONST.__objc_arraydata: 0xb8
   __DATA_CONST.__got: 0x720
-  __AUTH_CONST.__const: 0x4b540
+  __AUTH_CONST.__const: 0x4b570
   __AUTH_CONST.__cfstring: 0x2880
-  __AUTH_CONST.__objc_const: 0xdf68
+  __AUTH_CONST.__objc_const: 0xe0e8
   __AUTH_CONST.__weak_auth_got: 0x50
   __AUTH_CONST.__objc_intobj: 0x258
   __AUTH_CONST.__objc_arrayobj: 0x48

   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__auth_got: 0x1f08
-  __AUTH.__objc_data: 0x240
+  __AUTH.__objc_data: 0x290
   __AUTH.__data: 0x28
   __AUTH.__thread_vars: 0x390
   __AUTH.__thread_data: 0x40
   __AUTH.__thread_bss: 0xae8
-  __DATA.__objc_ivar: 0x980
+  __DATA.__objc_ivar: 0x998
   __DATA.__data: 0x1618
   __DATA.__common: 0x12d
   __DATA.__bss: 0x830

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 39935
-  Symbols:   61747
-  CStrings:  19829
+  Functions: 39951
+  Symbols:   61782
+  CStrings:  19832
 
Symbols:
+ -[_EARTokenPostProcessor _tokenizer]
+ -[_EARTokenPostProcessor processTokens:donateEmojiUsage:usePersonalizedEmoji:requestContext:]
+ -[_EARTokenPostProcessor tokenizeLeftContext:]
+ -[_EARTokenPostProcessorRequestContext .cxx_destruct]
+ -[_EARTokenPostProcessorRequestContext initWithRelevantTextContext:]
+ -[_EARTokenPostProcessorRequestContext leftContext]
+ -[_EARTokenPostProcessorRequestContext rightContext]
+ -[_EARTokenPostProcessorRequestContext setLeftContext:]
+ -[_EARTokenPostProcessorRequestContext setRightContext:]
+ GCC_except_table927
+ OBJC_IVAR_$__EARTokenPostProcessor._cachedLeftContext
+ OBJC_IVAR_$__EARTokenPostProcessor._cachedLeftContextTokens
+ OBJC_IVAR_$__EARTokenPostProcessor._casePredictor
+ OBJC_IVAR_$__EARTokenPostProcessor._tokenizer
+ OBJC_IVAR_$__EARTokenPostProcessorRequestContext._leftContext
+ OBJC_IVAR_$__EARTokenPostProcessorRequestContext._rightContext
+ _OBJC_CLASS_$__EARTokenPostProcessorRequestContext
+ _OBJC_METACLASS_$__EARTokenPostProcessorRequestContext
+ __OBJC_$_INSTANCE_METHODS__EARTokenPostProcessorRequestContext
+ __OBJC_$_INSTANCE_VARIABLES__EARTokenPostProcessorRequestContext
+ __OBJC_$_PROP_LIST__EARTokenPostProcessorRequestContext
+ __OBJC_CLASS_RO_$__EARTokenPostProcessorRequestContext
+ __OBJC_METACLASS_RO_$__EARTokenPostProcessorRequestContext
+ __ZN6quasar13CasePredictor22predictFirstWordCasingERKNSt3__16vectorINS_5TokenENS1_9allocatorIS3_EEEERKNS2_INS1_12basic_stringIcNS1_11char_traitsIcEENS4_IcEEEENS4_ISD_EEEE
+ __ZN6quasar13CasePredictorC1ERNS_12SystemConfigE
+ __ZN6quasar13CasePredictorC2ERNS_12SystemConfigE
+ __ZN6quasar13CasePredictorC2Ev
+ __ZNSt3__110unique_ptrIN6quasar13CasePredictorENS_14default_deleteIS2_EEE5resetB9nqe220106EPS2_
+ __ZNSt3__110unique_ptrIN6quasar7LexiconENS_14default_deleteIS2_EEED1B9nqe220106Ev
+ ___68-[_EARTokenPostProcessorRequestContext initWithRelevantTextContext:]_block_invoke
+ ___block_descriptor_40_ea8_32s_e55_v40?0"NSString"8"NSString"16"NSArray"24"NSArray"32l
+ _objc_msgSend$leftContext
+ _objc_msgSend$processTokens:donateEmojiUsage:usePersonalizedEmoji:requestContext:
+ _objc_msgSend$setRightContext:
+ _objc_msgSend$tokenizeLeftContext:
CStrings:
+ " ms"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Dn6gRw/Sources/EmbeddedAcousticRecognition/libquasar/libkaldi/tools/openfst/src/extensions/ngram/bitmap-index.cc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Dn6gRw/Sources/EmbeddedAcousticRecognition/libquasar/liblm/src/fst_builder.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Dn6gRw/Sources/EmbeddedAcousticRecognition/libquasar/liblm/src/impl/arpa2fst-inhouse.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Dn6gRw/Sources/EmbeddedAcousticRecognition/libquasar/liblm/src/impl/arpa2fst-kaldi.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Dn6gRw/Sources/EmbeddedAcousticRecognition/libquasar/liblm/src/impl/arpa2fst-kaldi/arpa-lm-compiler.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Dn6gRw/Sources/EmbeddedAcousticRecognition/libquasar/liblm/src/impl/arpa2fst.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Dn6gRw/Sources/EmbeddedAcousticRecognition/libquasar/liblm/src/impl/srilm.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Dn6gRw/Sources/EmbeddedAcousticRecognition/libquasar/liblm/src/impl/weights.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Dn6gRw/Sources/EmbeddedAcousticRecognition/libquasar/liblm/src/symbol_tables.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Dn6gRw/Sources/EmbeddedAcousticRecognition/libquasar/libsentencepiece/src/bpe_model.cc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Dn6gRw/Sources/EmbeddedAcousticRecognition/libquasar/libsentencepiece/src/builtin_pb/sentencepiece.pb.cc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Dn6gRw/Sources/EmbeddedAcousticRecognition/libquasar/libsentencepiece/src/builtin_pb/sentencepiece_model.pb.cc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Dn6gRw/Sources/EmbeddedAcousticRecognition/libquasar/libsentencepiece/src/filesystem.cc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Dn6gRw/Sources/EmbeddedAcousticRecognition/libquasar/libsentencepiece/src/model_factory.cc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Dn6gRw/Sources/EmbeddedAcousticRecognition/libquasar/libsentencepiece/src/model_interface.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Dn6gRw/Sources/EmbeddedAcousticRecognition/libquasar/libsentencepiece/src/normalizer.cc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Dn6gRw/Sources/EmbeddedAcousticRecognition/libquasar/libsentencepiece/src/sentencepiece_processor.cc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Dn6gRw/Sources/EmbeddedAcousticRecognition/libquasar/libsentencepiece/src/unigram_model.cc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Dn6gRw/Sources/EmbeddedAcousticRecognition/libquasar/libsentencepiece/src/util.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Dn6gRw/Sources/EmbeddedAcousticRecognition/libquasar/libsentencepiece/third_party/protobuf-lite/arena.cc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Dn6gRw/Sources/EmbeddedAcousticRecognition/libquasar/libsentencepiece/third_party/protobuf-lite/common.cc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Dn6gRw/Sources/EmbeddedAcousticRecognition/libquasar/libsentencepiece/third_party/protobuf-lite/extension_set.cc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Dn6gRw/Sources/EmbeddedAcousticRecognition/libquasar/libsentencepiece/third_party/protobuf-lite/generated_message_util.cc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Dn6gRw/Sources/EmbeddedAcousticRecognition/libquasar/libsentencepiece/third_party/protobuf-lite/message_lite.cc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Dn6gRw/Sources/EmbeddedAcousticRecognition/libquasar/libtennessee/src/nashville/libtextproc/shared/collation.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Dn6gRw/Sources/EmbeddedAcousticRecognition/libquasar/libtennessee/src/nashville/libtextproc/shared/datamgr.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Dn6gRw/Sources/EmbeddedAcousticRecognition/libquasar/libtennessee/src/nashville/libtextproc/shared/envmgr.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Dn6gRw/Sources/EmbeddedAcousticRecognition/libquasar/libtennessee/src/nashville/libtextproc/shared/gramcomp.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Dn6gRw/Sources/EmbeddedAcousticRecognition/libquasar/libtennessee/src/nashville/libtextproc/shared/lexer.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Dn6gRw/Sources/EmbeddedAcousticRecognition/libquasar/libtennessee/src/nashville/libtextproc/shared/lexicon.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Dn6gRw/Sources/EmbeddedAcousticRecognition/libquasar/libtennessee/src/nashville/libtextproc/shared/misc.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Dn6gRw/Sources/EmbeddedAcousticRecognition/libquasar/libtennessee/src/nashville/libtextproc/shared/objectparser.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Dn6gRw/Sources/EmbeddedAcousticRecognition/libquasar/libtennessee/src/nashville/libtextproc/shared/params.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Dn6gRw/Sources/EmbeddedAcousticRecognition/libquasar/libtennessee/src/nashville/libtextproc/shared/regexp.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Dn6gRw/Sources/EmbeddedAcousticRecognition/libquasar/libtennessee/src/nashville/libtextproc/tkn/decompounder.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Dn6gRw/Sources/EmbeddedAcousticRecognition/libquasar/libtennessee/src/nashville/libtextproc/tkn/mungemapmgr.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Dn6gRw/Sources/EmbeddedAcousticRecognition/libquasar/libtennessee/src/nashville/libtextproc/tkn/patternmgr.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Dn6gRw/Sources/EmbeddedAcousticRecognition/libquasar/libtennessee/src/nashville/libtextproc/tkn/respellmgr.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Dn6gRw/Sources/EmbeddedAcousticRecognition/libquasar/libtennessee/src/nashville/libtextproc/tkn/tokenizer.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ZhGmqt/Sources/Marisa/include/marisa/scoped-ptr.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ZhGmqt/Sources/Marisa/include/marisa/scoped-ptr.h:19: MARISA_RESET_ERROR: (ptr != NULL) && (ptr == ptr_)"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ZhGmqt/Sources/Marisa/lib/marisa/agent.cc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ZhGmqt/Sources/Marisa/lib/marisa/agent.cc:13: MARISA_NULL_ERROR: str == NULL"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ZhGmqt/Sources/Marisa/lib/marisa/agent.cc:36: MARISA_STATE_ERROR: state_.get() != NULL"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ZhGmqt/Sources/Marisa/lib/marisa/agent.cc:38: MARISA_MEMORY_ERROR: state_.get() == NULL"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ZhGmqt/Sources/Marisa/lib/marisa/grimoire/io/mapper.cc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ZhGmqt/Sources/Marisa/lib/marisa/grimoire/io/mapper.cc:106: MARISA_STATE_ERROR: !is_open()"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ZhGmqt/Sources/Marisa/lib/marisa/grimoire/io/mapper.cc:107: MARISA_IO_ERROR: size > avail_"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ZhGmqt/Sources/Marisa/lib/marisa/grimoire/io/mapper.cc:70: MARISA_NULL_ERROR: (ptr == NULL) && (size != 0)"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ZhGmqt/Sources/Marisa/lib/marisa/grimoire/io/mapper.cc:78: MARISA_STATE_ERROR: !is_open()"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ZhGmqt/Sources/Marisa/lib/marisa/grimoire/io/mapper.cc:79: MARISA_IO_ERROR: size > avail_"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ZhGmqt/Sources/Marisa/lib/marisa/grimoire/trie/../io/mapper.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ZhGmqt/Sources/Marisa/lib/marisa/grimoire/trie/../io/mapper.h:30: MARISA_NULL_ERROR: (objs == NULL) && (num_objs != 0)"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ZhGmqt/Sources/Marisa/lib/marisa/grimoire/trie/../io/mapper.h:32: MARISA_SIZE_ERROR: num_objs > (MARISA_SIZE_MAX / sizeof(T))"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ZhGmqt/Sources/Marisa/lib/marisa/grimoire/trie/../vector/bit-vector.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ZhGmqt/Sources/Marisa/lib/marisa/grimoire/trie/../vector/bit-vector.h:135: MARISA_FORMAT_ERROR: temp_num_1s > size_"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ZhGmqt/Sources/Marisa/lib/marisa/grimoire/trie/../vector/bit-vector.h:52: MARISA_SIZE_ERROR: size_ == MARISA_UINT32_MAX"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ZhGmqt/Sources/Marisa/lib/marisa/grimoire/trie/../vector/flat-vector.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ZhGmqt/Sources/Marisa/lib/marisa/grimoire/trie/../vector/flat-vector.h:134: MARISA_FORMAT_ERROR: temp_value_size > 32"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ZhGmqt/Sources/Marisa/lib/marisa/grimoire/trie/../vector/vector.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ZhGmqt/Sources/Marisa/lib/marisa/grimoire/trie/../vector/vector.h:100: MARISA_STATE_ERROR: fixed_"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ZhGmqt/Sources/Marisa/lib/marisa/grimoire/trie/../vector/vector.h:107: MARISA_STATE_ERROR: fixed_"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ZhGmqt/Sources/Marisa/lib/marisa/grimoire/trie/../vector/vector.h:202: MARISA_FORMAT_ERROR: (total_size % sizeof(T)) != 0"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ZhGmqt/Sources/Marisa/lib/marisa/grimoire/trie/config.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ZhGmqt/Sources/Marisa/lib/marisa/grimoire/trie/config.h:101: MARISA_CODE_ERROR: undefined cache level"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ZhGmqt/Sources/Marisa/lib/marisa/grimoire/trie/config.h:121: MARISA_CODE_ERROR: undefined tail mode"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ZhGmqt/Sources/Marisa/lib/marisa/grimoire/trie/config.h:141: MARISA_CODE_ERROR: undefined node order"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ZhGmqt/Sources/Marisa/lib/marisa/grimoire/trie/config.h:59: MARISA_CODE_ERROR: (config_flags & ~MARISA_CONFIG_MASK) != 0"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ZhGmqt/Sources/Marisa/lib/marisa/grimoire/trie/header.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ZhGmqt/Sources/Marisa/lib/marisa/grimoire/trie/header.h:21: MARISA_FORMAT_ERROR: !test_header(ptr)"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ZhGmqt/Sources/Marisa/lib/marisa/grimoire/trie/louds-trie.cc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ZhGmqt/Sources/Marisa/lib/marisa/grimoire/trie/louds-trie.cc:428: MARISA_MEMORY_ERROR: std::bad_alloc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ZhGmqt/Sources/Marisa/lib/marisa/grimoire/trie/louds-trie.cc:451: MARISA_MEMORY_ERROR: next_trie_.get() == NULL"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ZhGmqt/Sources/Marisa/lib/marisa/grimoire/trie/louds-trie.cc:468: MARISA_MEMORY_ERROR: next_trie_.get() == NULL"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ZhGmqt/Sources/Marisa/lib/marisa/grimoire/trie/louds-trie.cc:542: MARISA_MEMORY_ERROR: next_trie_.get() == NULL"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ZhGmqt/Sources/Marisa/lib/marisa/grimoire/trie/louds-trie.cc:73: MARISA_BOUND_ERROR: agent.query().id() >= size()"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ZhGmqt/Sources/Marisa/lib/marisa/grimoire/trie/tail.cc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ZhGmqt/Sources/Marisa/lib/marisa/grimoire/trie/tail.cc:13: MARISA_NULL_ERROR: offsets == NULL"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ZhGmqt/Sources/Marisa/lib/marisa/grimoire/trie/tail.cc:170: MARISA_RANGE_ERROR: current.length() == 0"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ZhGmqt/Sources/Marisa/lib/marisa/grimoire/trie/tail.cc:192: MARISA_SIZE_ERROR: buf_.size() > MARISA_UINT32_MAX"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ZhGmqt/Sources/Marisa/lib/marisa/grimoire/trie/tail.cc:36: MARISA_CODE_ERROR: undefined tail mode"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ZhGmqt/Sources/Marisa/lib/marisa/grimoire/vector/vector.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ZhGmqt/Sources/Marisa/lib/marisa/grimoire/vector/vector.h:100: MARISA_STATE_ERROR: fixed_"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ZhGmqt/Sources/Marisa/lib/marisa/keyset.cc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ZhGmqt/Sources/Marisa/lib/marisa/keyset.cc:129: MARISA_MEMORY_ERROR: new_blocks.get() == NULL"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ZhGmqt/Sources/Marisa/lib/marisa/keyset.cc:138: MARISA_MEMORY_ERROR: new_block.get() == NULL"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ZhGmqt/Sources/Marisa/lib/marisa/keyset.cc:151: MARISA_MEMORY_ERROR: new_blocks.get() == NULL"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ZhGmqt/Sources/Marisa/lib/marisa/keyset.cc:159: MARISA_MEMORY_ERROR: new_block.get() == NULL"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ZhGmqt/Sources/Marisa/lib/marisa/keyset.cc:169: MARISA_MEMORY_ERROR: new_blocks.get() == NULL"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ZhGmqt/Sources/Marisa/lib/marisa/keyset.cc:177: MARISA_MEMORY_ERROR: new_block.get() == NULL"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ZhGmqt/Sources/Marisa/lib/marisa/keyset.cc:50: MARISA_NULL_ERROR: str == NULL"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ZhGmqt/Sources/Marisa/lib/marisa/keyset.cc:61: MARISA_NULL_ERROR: (ptr == NULL) && (length != 0)"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ZhGmqt/Sources/Marisa/lib/marisa/keyset.cc:62: MARISA_SIZE_ERROR: length > MARISA_UINT32_MAX"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ZhGmqt/Sources/Marisa/lib/marisa/trie.cc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ZhGmqt/Sources/Marisa/lib/marisa/trie.cc:14: MARISA_MEMORY_ERROR: temp.get() == NULL"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ZhGmqt/Sources/Marisa/lib/marisa/trie.cc:37: MARISA_NULL_ERROR: (ptr == NULL) && (size != 0)"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ZhGmqt/Sources/Marisa/lib/marisa/trie.cc:40: MARISA_MEMORY_ERROR: temp.get() == NULL"
+ "Failed to convert u32string "
+ "Tokenization duration: "
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7EQY4D/Sources/EmbeddedAcousticRecognition/libquasar/libkaldi/tools/openfst/src/extensions/ngram/bitmap-index.cc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7EQY4D/Sources/EmbeddedAcousticRecognition/libquasar/liblm/src/fst_builder.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7EQY4D/Sources/EmbeddedAcousticRecognition/libquasar/liblm/src/impl/arpa2fst-inhouse.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7EQY4D/Sources/EmbeddedAcousticRecognition/libquasar/liblm/src/impl/arpa2fst-kaldi.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7EQY4D/Sources/EmbeddedAcousticRecognition/libquasar/liblm/src/impl/arpa2fst-kaldi/arpa-lm-compiler.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7EQY4D/Sources/EmbeddedAcousticRecognition/libquasar/liblm/src/impl/arpa2fst.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7EQY4D/Sources/EmbeddedAcousticRecognition/libquasar/liblm/src/impl/srilm.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7EQY4D/Sources/EmbeddedAcousticRecognition/libquasar/liblm/src/impl/weights.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7EQY4D/Sources/EmbeddedAcousticRecognition/libquasar/liblm/src/symbol_tables.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7EQY4D/Sources/EmbeddedAcousticRecognition/libquasar/libsentencepiece/src/bpe_model.cc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7EQY4D/Sources/EmbeddedAcousticRecognition/libquasar/libsentencepiece/src/builtin_pb/sentencepiece.pb.cc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7EQY4D/Sources/EmbeddedAcousticRecognition/libquasar/libsentencepiece/src/builtin_pb/sentencepiece_model.pb.cc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7EQY4D/Sources/EmbeddedAcousticRecognition/libquasar/libsentencepiece/src/filesystem.cc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7EQY4D/Sources/EmbeddedAcousticRecognition/libquasar/libsentencepiece/src/model_factory.cc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7EQY4D/Sources/EmbeddedAcousticRecognition/libquasar/libsentencepiece/src/model_interface.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7EQY4D/Sources/EmbeddedAcousticRecognition/libquasar/libsentencepiece/src/normalizer.cc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7EQY4D/Sources/EmbeddedAcousticRecognition/libquasar/libsentencepiece/src/sentencepiece_processor.cc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7EQY4D/Sources/EmbeddedAcousticRecognition/libquasar/libsentencepiece/src/unigram_model.cc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7EQY4D/Sources/EmbeddedAcousticRecognition/libquasar/libsentencepiece/src/util.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7EQY4D/Sources/EmbeddedAcousticRecognition/libquasar/libsentencepiece/third_party/protobuf-lite/arena.cc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7EQY4D/Sources/EmbeddedAcousticRecognition/libquasar/libsentencepiece/third_party/protobuf-lite/common.cc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7EQY4D/Sources/EmbeddedAcousticRecognition/libquasar/libsentencepiece/third_party/protobuf-lite/extension_set.cc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7EQY4D/Sources/EmbeddedAcousticRecognition/libquasar/libsentencepiece/third_party/protobuf-lite/generated_message_util.cc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7EQY4D/Sources/EmbeddedAcousticRecognition/libquasar/libsentencepiece/third_party/protobuf-lite/message_lite.cc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7EQY4D/Sources/EmbeddedAcousticRecognition/libquasar/libtennessee/src/nashville/libtextproc/shared/collation.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7EQY4D/Sources/EmbeddedAcousticRecognition/libquasar/libtennessee/src/nashville/libtextproc/shared/datamgr.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7EQY4D/Sources/EmbeddedAcousticRecognition/libquasar/libtennessee/src/nashville/libtextproc/shared/envmgr.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7EQY4D/Sources/EmbeddedAcousticRecognition/libquasar/libtennessee/src/nashville/libtextproc/shared/gramcomp.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7EQY4D/Sources/EmbeddedAcousticRecognition/libquasar/libtennessee/src/nashville/libtextproc/shared/lexer.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7EQY4D/Sources/EmbeddedAcousticRecognition/libquasar/libtennessee/src/nashville/libtextproc/shared/lexicon.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7EQY4D/Sources/EmbeddedAcousticRecognition/libquasar/libtennessee/src/nashville/libtextproc/shared/misc.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7EQY4D/Sources/EmbeddedAcousticRecognition/libquasar/libtennessee/src/nashville/libtextproc/shared/objectparser.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7EQY4D/Sources/EmbeddedAcousticRecognition/libquasar/libtennessee/src/nashville/libtextproc/shared/params.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7EQY4D/Sources/EmbeddedAcousticRecognition/libquasar/libtennessee/src/nashville/libtextproc/shared/regexp.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7EQY4D/Sources/EmbeddedAcousticRecognition/libquasar/libtennessee/src/nashville/libtextproc/tkn/decompounder.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7EQY4D/Sources/EmbeddedAcousticRecognition/libquasar/libtennessee/src/nashville/libtextproc/tkn/mungemapmgr.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7EQY4D/Sources/EmbeddedAcousticRecognition/libquasar/libtennessee/src/nashville/libtextproc/tkn/patternmgr.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7EQY4D/Sources/EmbeddedAcousticRecognition/libquasar/libtennessee/src/nashville/libtextproc/tkn/respellmgr.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.7EQY4D/Sources/EmbeddedAcousticRecognition/libquasar/libtennessee/src/nashville/libtextproc/tkn/tokenizer.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/include/marisa/scoped-ptr.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/include/marisa/scoped-ptr.h:19: MARISA_RESET_ERROR: (ptr != NULL) && (ptr == ptr_)"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/agent.cc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/agent.cc:13: MARISA_NULL_ERROR: str == NULL"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/agent.cc:36: MARISA_STATE_ERROR: state_.get() != NULL"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/agent.cc:38: MARISA_MEMORY_ERROR: state_.get() == NULL"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/grimoire/io/mapper.cc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/grimoire/io/mapper.cc:106: MARISA_STATE_ERROR: !is_open()"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/grimoire/io/mapper.cc:107: MARISA_IO_ERROR: size > avail_"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/grimoire/io/mapper.cc:70: MARISA_NULL_ERROR: (ptr == NULL) && (size != 0)"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/grimoire/io/mapper.cc:78: MARISA_STATE_ERROR: !is_open()"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/grimoire/io/mapper.cc:79: MARISA_IO_ERROR: size > avail_"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/grimoire/trie/../io/mapper.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/grimoire/trie/../io/mapper.h:30: MARISA_NULL_ERROR: (objs == NULL) && (num_objs != 0)"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/grimoire/trie/../io/mapper.h:32: MARISA_SIZE_ERROR: num_objs > (MARISA_SIZE_MAX / sizeof(T))"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/grimoire/trie/../vector/bit-vector.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/grimoire/trie/../vector/bit-vector.h:135: MARISA_FORMAT_ERROR: temp_num_1s > size_"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/grimoire/trie/../vector/bit-vector.h:52: MARISA_SIZE_ERROR: size_ == MARISA_UINT32_MAX"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/grimoire/trie/../vector/flat-vector.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/grimoire/trie/../vector/flat-vector.h:134: MARISA_FORMAT_ERROR: temp_value_size > 32"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/grimoire/trie/../vector/vector.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/grimoire/trie/../vector/vector.h:100: MARISA_STATE_ERROR: fixed_"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/grimoire/trie/../vector/vector.h:107: MARISA_STATE_ERROR: fixed_"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/grimoire/trie/../vector/vector.h:202: MARISA_FORMAT_ERROR: (total_size % sizeof(T)) != 0"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/grimoire/trie/config.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/grimoire/trie/config.h:101: MARISA_CODE_ERROR: undefined cache level"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/grimoire/trie/config.h:121: MARISA_CODE_ERROR: undefined tail mode"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/grimoire/trie/config.h:141: MARISA_CODE_ERROR: undefined node order"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/grimoire/trie/config.h:59: MARISA_CODE_ERROR: (config_flags & ~MARISA_CONFIG_MASK) != 0"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/grimoire/trie/header.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/grimoire/trie/header.h:21: MARISA_FORMAT_ERROR: !test_header(ptr)"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/grimoire/trie/louds-trie.cc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/grimoire/trie/louds-trie.cc:428: MARISA_MEMORY_ERROR: std::bad_alloc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/grimoire/trie/louds-trie.cc:451: MARISA_MEMORY_ERROR: next_trie_.get() == NULL"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/grimoire/trie/louds-trie.cc:468: MARISA_MEMORY_ERROR: next_trie_.get() == NULL"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/grimoire/trie/louds-trie.cc:542: MARISA_MEMORY_ERROR: next_trie_.get() == NULL"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/grimoire/trie/louds-trie.cc:73: MARISA_BOUND_ERROR: agent.query().id() >= size()"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/grimoire/trie/tail.cc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/grimoire/trie/tail.cc:13: MARISA_NULL_ERROR: offsets == NULL"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/grimoire/trie/tail.cc:170: MARISA_RANGE_ERROR: current.length() == 0"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/grimoire/trie/tail.cc:192: MARISA_SIZE_ERROR: buf_.size() > MARISA_UINT32_MAX"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/grimoire/trie/tail.cc:36: MARISA_CODE_ERROR: undefined tail mode"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/grimoire/vector/vector.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/grimoire/vector/vector.h:100: MARISA_STATE_ERROR: fixed_"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/keyset.cc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/keyset.cc:129: MARISA_MEMORY_ERROR: new_blocks.get() == NULL"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/keyset.cc:138: MARISA_MEMORY_ERROR: new_block.get() == NULL"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/keyset.cc:151: MARISA_MEMORY_ERROR: new_blocks.get() == NULL"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/keyset.cc:159: MARISA_MEMORY_ERROR: new_block.get() == NULL"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/keyset.cc:169: MARISA_MEMORY_ERROR: new_blocks.get() == NULL"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/keyset.cc:177: MARISA_MEMORY_ERROR: new_block.get() == NULL"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/keyset.cc:50: MARISA_NULL_ERROR: str == NULL"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/keyset.cc:61: MARISA_NULL_ERROR: (ptr == NULL) && (length != 0)"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/keyset.cc:62: MARISA_SIZE_ERROR: length > MARISA_UINT32_MAX"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/trie.cc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/trie.cc:14: MARISA_MEMORY_ERROR: temp.get() == NULL"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/trie.cc:37: MARISA_NULL_ERROR: (ptr == NULL) && (size != 0)"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SyLKM8/Sources/Marisa/lib/marisa/trie.cc:40: MARISA_MEMORY_ERROR: temp.get() == NULL"
```
