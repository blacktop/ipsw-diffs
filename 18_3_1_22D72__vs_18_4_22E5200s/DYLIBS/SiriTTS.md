## SiriTTS

> `/System/Library/PrivateFrameworks/SiriTTS.framework/SiriTTS`

```diff

-3402.58.1.0.0
-  __TEXT.__text: 0x7e3684
-  __TEXT.__auth_stubs: 0x2600
-  __TEXT.__init_offsets: 0x4
+3404.55.2.1.1
+  __TEXT.__text: 0x7d5b5c
+  __TEXT.__auth_stubs: 0x2620
   __TEXT.__objc_methlist: 0x20
-  __TEXT.__gcc_except_tab: 0x3a494
-  __TEXT.__cstring: 0x65268
-  __TEXT.__const: 0xd6a4e
-  __TEXT.__oslogstring: 0x82dc
+  __TEXT.__const: 0xe3041
+  __TEXT.__gcc_except_tab: 0x3b600
+  __TEXT.__cstring: 0x65939
+  __TEXT.__oslogstring: 0x8839
   __TEXT.__ustring: 0x4a0
-  __TEXT.__unwind_info: 0x17650
-  __TEXT.__eh_frame: 0x260
+  __TEXT.__unwind_info: 0x16eb0
+  __TEXT.__eh_frame: 0x268
   __TEXT.__objc_classname: 0x1c
   __TEXT.__objc_methname: 0x119
   __TEXT.__objc_methtype: 0x13
   __TEXT.__objc_stubs: 0x200
-  __DATA_CONST.__got: 0x200
-  __DATA_CONST.__const: 0xff68
+  __DATA_CONST.__got: 0x218
+  __DATA_CONST.__const: 0xffc8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x88
   __DATA_CONST.__objc_classrefs: 0x38
   __DATA_CONST.__objc_arraydata: 0x8
-  __AUTH_CONST.__auth_got: 0x1310
+  __AUTH_CONST.__auth_got: 0x1320
   __AUTH_CONST.__auth_ptr: 0x120
-  __AUTH_CONST.__const: 0x32d48
+  __AUTH_CONST.__const: 0x335c0
   __AUTH_CONST.__cfstring: 0x180
   __AUTH_CONST.__objc_const: 0x40
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__data: 0xe0
-  __DATA.__data: 0xbb1c
+  __DATA.__data: 0x2f4
   __DATA.__common: 0x21
   __DATA.__bss: 0xe18
-  __DATA_DIRTY.__bss: 0x30
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libxml2.2.dylib
-  Functions: 21994
-  Symbols:   23461
-  CStrings:  17573
+  Functions: 21417
+  Symbols:   23526
+  CStrings:  17602
 
Symbols:
+ __ZN14NeuralTTSUtils20is_visionos_platformEv
+ __ZN14TTSSynthesizer23has_word_timing_supportERKNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE
+ __ZN7SiriTTS13ANETECDecoder6createEbRKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEb
+ __ZN7SiriTTS13ANETECEncoder6createEbRKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEb
+ __ZNSt3__117bad_function_callD1Ev
+ __ZNSt3__14__fs10filesystem20__create_directoriesERKNS1_4pathEPNS_10error_codeE
+ __ZTINSt3__117bad_function_callE
+ __ZTVNSt3__117bad_function_callE
+ _dispatch_queue_get_qos_class
+ _getpwuid
+ _getuid
- __ZNKSt9exception4whatEv
- ___cxa_atexit
- _dispatch_block_create_with_qos_class
CStrings:
+ "/AppleInternal/Library/BuildRoots/80a4978a-ebfc-11ef-ae29-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/include/boost/utility/string_ref.hpp"
+ "/tmp"
+ "ANETEC"
+ "ANETEC (non-)streaming decoder module"
+ "ANETEC (non-)streaming encoder module"
+ "ANETEC failure due to missing model %s\n"
+ "After G2P Idx: %lu, Phonemes: %s, Aligned from %d to %d"
+ "After G2P Idx: %lu, Phonemes: %s, Alignment info from G2P is empty"
+ "Alignment failed at `%s' - %lu"
+ "Anetec streaming encoder module inference time (per cache): %.3f s"
+ "Anetec streaming encoder module start."
+ "Assertion Error: %s"
+ "Before G2P (BPE) Idx: %lu, Word: %s"
+ "Caches"
+ "FE Init MarkupSentencePersistentModule"
+ "G2P Alignment failed and fallback to single word!"
+ "G2P Alignmnet failed and fallback to single word!"
+ "G2P Alignmnet failed at boundary check and fallback to single word!"
+ "G2P output reconstruction started"
+ "G2PAlignmentFailure"
+ "HOME"
+ "Init latency (markup_sent): %.3f s"
+ "Invalid Rule file(%s): %s"
+ "Invalid basic->loc_start! - %s"
+ "Library"
+ "MarkupSentence"
+ "Mil2BnnsMilInferenceModel execution missing input %s"
+ "Missing .ext from rule file for extension: %s"
+ "Only binary rule file is supported for extension: %s"
+ "Prepending silence of %lu samples."
+ "Process Markup on sentence level"
+ "Reconstruction failed at %d replacement from g2p"
+ "ReconstructionFailure"
+ "SiriTTS"
+ "Start checking alignments from G2P model, there are [%lu] Words before G2P and has [%lu] Phonemes after G2P"
+ "Switching to %s G2P"
+ "The key is not found: "
+ "Trim trailing silence of %lu samples and will add to the beginning of next audio chunk."
+ "Unable to create mil2bnns model directory: %s"
+ "Unable to read model config json file '%s'"
+ "Utils.cpp"
+ "WaveformRateChangerImpl states: global_rate=%.4f, local_rate=%.4f, adaptive_rate_factor=%.4f, sample_ix=%d, last_sample_ix=%d, offset=%d, frame_shift=%d, frame_size=%d, correlation_frame_size=%d, accumulated_input_size=%d, accumulated_output_size=%d"
+ "WaveformRateChangerImpl::change_rate() enters infinite loop. "
+ "anetec_api_decoder"
+ "anetec_api_encoder"
+ "anetec_decoder_inference.json"
+ "anetec_decoder_streaming_inference.json"
+ "anetec_encoder_inference.json"
+ "anetec_encoder_streaming_inference.json"
+ "assert_with_log"
+ "cmn-CN"
+ "cmn-cn"
+ "engine"
+ "example"
+ "expr"
+ "failed to fstat bnns mmap file from: '%s', errno: %d"
+ "failed to mmap bnns mmap file from: '%s', errno: %d"
+ "failed to open bnns mmap file from: '%s', errno: %d"
+ "gryphon_22E.cfg"
+ "handle markup at sentence level"
+ "ibuf"
+ "kAnetecEncoder"
+ "kAnetecStreamingEncoder"
+ "markup_sent"
+ "mil2bnns_mmap_filename"
+ "multilingual_g2p"
+ "streaming"
+ "trailing_silence"
+ "tskp"
+ "tts.errors.word_alignment_failure"
+ "voice_specific_prefix"
- "\x14"
- "\x15"
- "'s"
- "*,"
- "*:"
- "*;"
- "+-"
- ",."
- "-_"
- ".,"
- "/AppleInternal/Library/BuildRoots/774ff07e-d344-11ef-9a16-36218cb420d5/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/include/boost/utility/string_ref.hpp"
- "13"
- "21"
- "22"
- "33"
- "34"
- "35"
- "51"
- "55"
- "?>"
- "A\\"
- "Aligner failed to align, and fallback to single word!"
- "BI"
- "G2P model alignment started"
- "Invalid Rule file: %s"
- "MC"
- "MilInferenceBaseModule.cpp"
- "N1_"
- "N2_"
- "N3_"
- "N4_"
- "N5_"
- "N6_"
- "N7_"
- "N8_"
- "N9_"
- "NP"
- "TM"
- "TQ"
- "TS"
- "TW"
- "UC"
- "VC"
- "VV"
- "[/"
- "\\/"
- "\\S"
- "]/"
- "_G."
- "execute"
- "get_output"
- "get_output_io"
- "has_input(input_name)"
- "input_buffers_.find(data_tensor->get_name()) != input_buffers_.end()"
- "mode"
- "nc"
- "output_buffers_.find(key) != output_buffers_.end()"
- "set_input"
- "unexpected case for full-half transliterator"
- "√"
- "░"
- "▬"
- "\ufeff"

```
