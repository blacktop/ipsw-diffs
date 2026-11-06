## EmbeddedAcousticRecognition

> `/System/Library/PrivateFrameworks/EmbeddedAcousticRecognition.framework/Versions/A/EmbeddedAcousticRecognition`

```diff

-3600.73.1.0.0
-  __TEXT.__text: 0xaf695c
-  __TEXT.__objc_methlist: 0x6aec
-  __TEXT.__const: 0x5e998
-  __TEXT.__gcc_except_tab: 0xc00f8
-  __TEXT.__cstring: 0x79fb5
+3605.9.1.0.0
+  __TEXT.__text: 0xaf84fc
+  __TEXT.__objc_methlist: 0x6b54
+  __TEXT.__const: 0x5ea08
+  __TEXT.__gcc_except_tab: 0xc0428
+  __TEXT.__cstring: 0x7a275
   __TEXT.__oslogstring: 0x3131
   __TEXT.__ustring: 0xa8
   __TEXT.__dlopen_cstrs: 0x60

   __TEXT.__swift_as_ret: 0x1c
   __TEXT.__swift_as_cont: 0x28
   __TEXT.__swift5_capture: 0x114
-  __TEXT.__unwind_info: 0x3b5c8
+  __TEXT.__unwind_info: 0x3b658
   __TEXT.__eh_frame: 0x520
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1a08
-  __DATA_CONST.__objc_classlist: 0x568
+  __DATA_CONST.__const: 0x1a10
+  __DATA_CONST.__objc_classlist: 0x570
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x20
-  __DATA_CONST.__objc_selrefs: 0x3638
+  __DATA_CONST.__objc_selrefs: 0x3658
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x3d8
+  __DATA_CONST.__objc_superrefs: 0x3e0
   __DATA_CONST.__objc_arraydata: 0xd8
   __DATA_CONST.__got: 0x720
-  __AUTH_CONST.__const: 0x4b670
-  __AUTH_CONST.__cfstring: 0x28c0
-  __AUTH_CONST.__objc_const: 0xe148
+  __AUTH_CONST.__const: 0x4b6f0
+  __AUTH_CONST.__cfstring: 0x2960
+  __AUTH_CONST.__objc_const: 0xe260
   __AUTH_CONST.__weak_auth_got: 0x50
   __AUTH_CONST.__objc_intobj: 0x288
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH_CONST.__auth_got: 0x1f08
+  __AUTH_CONST.__auth_got: 0x1f10
   __AUTH_CONST.__auth_ptr: 0x200
-  __AUTH.__objc_data: 0x290
-  __AUTH.__data: 0x28
   __AUTH.__thread_vars: 0x390
   __AUTH.__thread_data: 0x40
   __AUTH.__thread_bss: 0xae8
-  __DATA.__objc_ivar: 0x9a4
-  __DATA.__data: 0x1618
-  __DATA.__common: 0x12d
-  __DATA.__bss: 0x830
-  __DATA_DIRTY.__objc_data: 0x33e0
-  __DATA_DIRTY.__data: 0x818
+  __DATA.__objc_ivar: 0x9b0
+  __DATA.__data: 0xea8
+  __DATA.__common: 0x125
+  __DATA.__bss: 0x850
+  __DATA_DIRTY.__objc_data: 0x36c0
+  __DATA_DIRTY.__data: 0xfb0
   __DATA_DIRTY.__bss: 0x2340
-  __DATA_DIRTY.__common: 0x398
+  __DATA_DIRTY.__common: 0x3a0
   - /System/Library/Frameworks/AVFAudio.framework/Versions/A/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/Versions/A/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 39968
-  Symbols:   61818
-  CStrings:  19834
+  Functions: 39994
+  Symbols:   61868
+  CStrings:  19851
 
Symbols:
+ -[EMTPronGuide .cxx_construct]
+ -[EMTPronGuide .cxx_destruct]
+ -[EMTPronGuide initWithModelURL:error:]
+ -[EMTPronGuide pronunciationForString:error:]
+ -[_EARSpeechRecognizer isAudioSourceRemote]
+ -[_EARSpeechRecognizer setIsAudioSourceRemote:]
+ -[_EARTranscriptionProcessingPackage initWithTokens:isFinal:utteranceStartMs:utteranceStartSamples:recognitionPaused:firstResultAfterResume:commandInterpretations:performanceMarkers:voiceCommandDebugInfo:]
+ -[_EARTranscriptionProcessingPackage voiceCommandDebugInfo]
+ GCC_except_table1113
+ GCC_except_table1156
+ GCC_except_table797
+ OBJC_IVAR_$_EMTPronGuide._pronGuide
+ OBJC_IVAR_$__EARSpeechRecognizer._isAudioSourceRemote
+ OBJC_IVAR_$__EARTranscriptionProcessingPackage._voiceCommandDebugInfo
+ _EMTPronGuideErrorDomain
+ _OBJC_CLASS_$_EMTPronGuide
+ _OBJC_METACLASS_$_EMTPronGuide
+ __OBJC_$_INSTANCE_METHODS_EMTPronGuide
+ __OBJC_$_INSTANCE_VARIABLES_EMTPronGuide
+ __OBJC_CLASS_RO_$_EMTPronGuide
+ __OBJC_METACLASS_RO_$_EMTPronGuide
+ __ZGVZN6quasar9PronGuide21getSharedPronunciatorERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEE15pronunciatorMap
+ __ZGVZN6quasar9PronGuide21getSharedPronunciatorERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEE1m
+ __ZN12_GLOBAL__N_113errorWithCodeE17EMTPronGuideErrorP8NSString
+ __ZN12_GLOBAL__N_125errorFromExceptionMessageERKNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE17EMTPronGuideError
+ __ZN5kaldi6quasar14EspressoV2Plan9SetAneQosE11qos_class_t
+ __ZN5kaldi6quasar16ComputeEngineItf9SetAneQosE11qos_class_t
+ __ZN5kaldi6quasar18NNMTTransliterator13TransliterateERKNSt3__112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEESA_bPb
+ __ZN5kaldi6quasar18NNMTTransliterator13TransliterateERKNSt3__16vectorINS2_12basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEENS7_IS9_EEEERKS9_bPb
+ __ZN5kaldi6quasar22CEFusedAcousticEncoder9SetAneQosE11qos_class_t
+ __ZN6quasar14RunAsyncParams9setAneQosE11qos_class_t
+ __ZN6quasar9PronGuide21getSharedPronunciatorERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE
+ __ZN6quasar9PronGuideC1ERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE
+ __ZN6quasar9PronGuideC2ERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE
+ __ZN6quasar9PronGuideD1Ev
+ __ZNK6quasar9PronGuide13pronunciationERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEPb
+ __ZNSt3__110unique_ptrIN6quasar9PronGuideENS_14default_deleteIS2_EEE5resetB9nqe220106EPS2_
+ __ZNSt3__110unique_ptrINS_11__tree_nodeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_8weak_ptrIN6quasar9PronGuide18SharedPronunciatorEEEEEPvEENS_22__tree_node_destructorINS6_ISG_EEEEED1B9nqe220106Ev
+ __ZNSt3__112__destroy_atB9nqe220106INS_4pairIKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_8weak_ptrIN6quasar9PronGuide18SharedPronunciatorEEEEEEEvPT_
+ __ZNSt3__120__shared_ptr_emplaceIN6quasar9PronGuide18SharedPronunciatorENS_9allocatorIS3_EEE16__on_zero_sharedEv
+ __ZNSt3__120__shared_ptr_emplaceIN6quasar9PronGuide18SharedPronunciatorENS_9allocatorIS3_EEE21__on_zero_shared_implB9nqe220106IS5_Li0EEEvv
+ __ZNSt3__120__shared_ptr_emplaceIN6quasar9PronGuide18SharedPronunciatorENS_9allocatorIS3_EEE21__on_zero_shared_weakEv
+ __ZNSt3__120__shared_ptr_emplaceIN6quasar9PronGuide18SharedPronunciatorENS_9allocatorIS3_EEED0Ev
+ __ZNSt3__120__shared_ptr_emplaceIN6quasar9PronGuide18SharedPronunciatorENS_9allocatorIS3_EEED1Ev
+ __ZNSt3__13mapINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_8weak_ptrIN6quasar9PronGuide18SharedPronunciatorEEENS_4lessIS6_EENS4_INS_4pairIKS6_SB_EEEEEixERSF_
+ __ZNSt3__16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_8weak_ptrIN6quasar9PronGuide18SharedPronunciatorEEEEENS_19__map_value_compareIS7_NS_4pairIKS7_SC_EENS_4lessIS7_EEEENS5_ISH_EEE12__find_equalB9nqe220106IS7_EENSF_IPNS_15__tree_end_nodeIPNS_16__tree_node_baseIPvEEEERSS_EERKT_
+ __ZNSt3__16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_8weak_ptrIN6quasar9PronGuide18SharedPronunciatorEEEEENS_19__map_value_compareIS7_NS_4pairIKS7_SC_EENS_4lessIS7_EEEENS5_ISH_EEE16__construct_nodeIJRKNS_21piecewise_construct_tENS_5tupleIJRSG_EEENSR_IJEEEEEENS_10unique_ptrINS_11__tree_nodeISD_PvEENS_22__tree_node_destructorINS5_ISY_EEEEEEDpOT_
+ __ZNSt3__16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_8weak_ptrIN6quasar9PronGuide18SharedPronunciatorEEEEENS_19__map_value_compareIS7_NS_4pairIKS7_SC_EENS_4lessIS7_EEEENS5_ISH_EEE16__insert_node_atEPNS_15__tree_end_nodeIPNS_16__tree_node_baseIPvEEEERSR_SR_
+ __ZTINSt3__120__shared_ptr_emplaceIN6quasar9PronGuide18SharedPronunciatorENS_9allocatorIS3_EEEE
+ __ZTSNSt3__120__shared_ptr_emplaceIN6quasar9PronGuide18SharedPronunciatorENS_9allocatorIS3_EEEE
+ __ZTVNSt3__120__shared_ptr_emplaceIN6quasar9PronGuide18SharedPronunciatorENS_9allocatorIS3_EEEE
+ __ZZN5kaldi6quasar18NNMTTransliterator13TransliterateERKNSt3__16vectorINS2_12basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEENS7_IS9_EEEERKS9_bPbEN18VectorUReplaceable4copyEPPviii
+ __ZZN5kaldi6quasar18NNMTTransliterator13TransliterateERKNSt3__16vectorINS2_12basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEENS7_IS9_EEEERKS9_bPbEN18VectorUReplaceable6charAtEPKPvi
+ __ZZN5kaldi6quasar18NNMTTransliterator13TransliterateERKNSt3__16vectorINS2_12basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEENS7_IS9_EEEERKS9_bPbEN18VectorUReplaceable6lengthEPKPv
+ __ZZN5kaldi6quasar18NNMTTransliterator13TransliterateERKNSt3__16vectorINS2_12basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEENS7_IS9_EEEERKS9_bPbEN18VectorUReplaceable7extractEPPviiPt
+ __ZZN5kaldi6quasar18NNMTTransliterator13TransliterateERKNSt3__16vectorINS2_12basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEENS7_IS9_EEEERKS9_bPbEN18VectorUReplaceable7replaceEPPviiPKti
+ __ZZN5kaldi6quasar18NNMTTransliterator13TransliterateERKNSt3__16vectorINS2_12basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEENS7_IS9_EEEERKS9_bPbEN18VectorUReplaceable8char32AtEPKPvi
+ __ZZN6quasar9PronGuide21getSharedPronunciatorERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEE15pronunciatorMap
+ __ZZN6quasar9PronGuide21getSharedPronunciatorERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEE1m
+ _e5rt_execution_stream_set_quality_of_service
+ _objc_msgSend$initWithTokens:isFinal:utteranceStartMs:utteranceStartSamples:recognitionPaused:firstResultAfterResume:commandInterpretations:performanceMarkers:voiceCommandDebugInfo:
- GCC_except_table1062
- GCC_except_table1108
- GCC_except_table894
- __ZN5kaldi6quasar18NNMTTransliterator13TransliterateERKNSt3__112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEESA_b
- __ZN5kaldi6quasar18NNMTTransliterator13TransliterateERKNSt3__16vectorINS2_12basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEENS7_IS9_EEEERKS9_b
- __ZZN5kaldi6quasar18NNMTTransliterator13TransliterateERKNSt3__16vectorINS2_12basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEENS7_IS9_EEEERKS9_bEN18VectorUReplaceable4copyEPPviii
- __ZZN5kaldi6quasar18NNMTTransliterator13TransliterateERKNSt3__16vectorINS2_12basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEENS7_IS9_EEEERKS9_bEN18VectorUReplaceable6charAtEPKPvi
- __ZZN5kaldi6quasar18NNMTTransliterator13TransliterateERKNSt3__16vectorINS2_12basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEENS7_IS9_EEEERKS9_bEN18VectorUReplaceable6lengthEPKPv
- __ZZN5kaldi6quasar18NNMTTransliterator13TransliterateERKNSt3__16vectorINS2_12basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEENS7_IS9_EEEERKS9_bEN18VectorUReplaceable7extractEPPviiPt
- __ZZN5kaldi6quasar18NNMTTransliterator13TransliterateERKNSt3__16vectorINS2_12basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEENS7_IS9_EEEERKS9_bEN18VectorUReplaceable7replaceEPPviiPKti
- __ZZN5kaldi6quasar18NNMTTransliterator13TransliterateERKNSt3__16vectorINS2_12basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEENS7_IS9_EEEERKS9_bEN18VectorUReplaceable8char32AtEPKPvi
CStrings:
+ "), retrying without memory mapping"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/local/include/boost/property_tree/detail/ptree_implementation.hpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/local/include/boost/property_tree/detail/xml_parser_read_rapidxml.hpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/local/include/boost/property_tree/json_parser.hpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/local/include/boost/property_tree/json_parser/detail/parser.hpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/local/include/boost/property_tree/json_parser/detail/write.hpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/local/include/boost/uuid/detail/random_provider_posix.ipp"
+ "A pron guide model URL is required"
+ "CEAttnEncoderDecoder::Decode engine run duration="
+ "CEFusedAcousticEncoder::Encode engine run duration="
+ "Could not memory map pron guide model "
+ "Do not allow multiple strict batch sizes for SyncPSRAudioProcessor"
+ "Failed to initialize pron guide: "
+ "Failed to produce reading: "
+ "Initialized pron guide"
+ "Input is too long to read. The result would have been truncated, so split the input into shorter segments and read each one."
+ "PronGuide initialized with model "
+ "PronGuide requires a pron guide model file"
+ "Unknown error"
+ "Using existing pron guide model: "
+ "com.apple.MachineTranslation.PronGuide"
+ "v2 model ANE QoS: "
+ "voiceCommandDebugInfo"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/include/boost/property_tree/detail/ptree_implementation.hpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/include/boost/property_tree/detail/xml_parser_read_rapidxml.hpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/include/boost/property_tree/json_parser.hpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/include/boost/property_tree/json_parser/detail/parser.hpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/include/boost/property_tree/json_parser/detail/write.hpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/include/boost/uuid/detail/random_provider_posix.ipp"
```
