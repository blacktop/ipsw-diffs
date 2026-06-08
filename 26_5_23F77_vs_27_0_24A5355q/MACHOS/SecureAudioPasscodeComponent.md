## SecureAudioPasscodeComponent

> `/System/ExclaveKit/System/Library/PrivateFrameworks/SecureAudioPasscodeComponent.framework/SecureAudioPasscodeComponent`

```diff

-140.19.0.0.0
-  __TEXT.__text: 0xae08
-  __TEXT.__auth_stubs: 0x880
-  __TEXT.__objc_stubs: 0xc0
-  __TEXT.__const: 0x168
-  __TEXT.__gcc_except_tab: 0x6b0
-  __TEXT.__cstring: 0x2807
-  __TEXT.__oslogstring: 0x57a
-  __TEXT.__objc_methname: 0x9b
+200.9.0.0.0
+  __TEXT.__text: 0xb738
+  __TEXT.__auth_stubs: 0x870
+  __TEXT.__objc_stubs: 0x1a0
+  __TEXT.__const: 0x150
+  __TEXT.__gcc_except_tab: 0x6ec
+  __TEXT.__cstring: 0x290a
+  __TEXT.__oslogstring: 0x65b
+  __TEXT.__objc_methname: 0xe8
   __TEXT.__unwind_info: 0x488
-  __DATA_CONST.__auth_got: 0x450
-  __DATA_CONST.__got: 0xc8
   __DATA_CONST.__const: 0x908
   __DATA_CONST.__cfstring: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_selrefs: 0x30
+  __DATA_CONST.__auth_got: 0x448
+  __DATA_CONST.__got: 0xe0
+  __DATA.__objc_selrefs: 0x68
   __DATA.__data: 0x150
   __DATA.__TIGHTBEAM: 0x18
   __DATA.__bss: 0x10

   - /System/ExclaveKit/usr/lib/libSystem.dylib
   - /System/ExclaveKit/usr/lib/libc++.dylib
   - /System/ExclaveKit/usr/lib/libobjc.A.dylib
-  UUID: DEE383A4-3C70-3ABE-A0AB-44554CC99C11
-  Functions: 275
-  Symbols:   612
-  CStrings:  126
+  UUID: 51C52967-FCD7-3DBE-BE8E-C2A210ACCB1B
+  Functions: 268
+  Symbols:   613
+  CStrings:  139
 
Symbols:
+ GCC_except_table29
+ GCC_except_table5
+ _NSStringFromClass
+ _OBJC_CLASS_$_NSData
+ _OBJC_CLASS_$_NSMutableArray
+ _OBJC_CLASS_$_NSNumber
+ _OUTLINED_FUNCTION_23
+ _OUTLINED_FUNCTION_24
+ _OUTLINED_FUNCTION_4
+ __ZN10applesauce2CF8ArrayRef7from_nsEP7NSArray
+ __ZN4sapc8exclaves25tone_generator_exclavekit23ToneGeneratorExclaveKit9ioStoppedEv
+ __ZN4sapc8exclaves25tone_generator_exclavekit26ProximityValidationManager31PairingAssetPlaybackDidCompleteE18pv_transfer_result
+ __ZNKSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEE4viewB9fqe220100Ev
+ __ZNSt12length_errorC1B9fqe220100EPKc
+ __ZNSt12out_of_rangeC1B9fqe220100EPKc
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB9fqe220100Ev
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE22__init_internal_bufferB9fqe220100Em
+ __ZNSt3__115allocate_sharedB9fqe220100IN4sapc8exclaves12sharedmemory2v212MappedRegionENS_9allocatorIS5_EEJRP24sharedmemory_segaccess_sRyRmR26sharedmem_permissions_ttagELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
+ __ZNSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEE15__init_buf_ptrsB9fqe220100Ev
+ __ZNSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B9fqe220100Ej
+ __ZNSt3__116__pad_and_outputB9fqe220100IcNS_11char_traitsIcEEEENS_19ostreambuf_iteratorIT_T0_EES6_PKS4_S8_S8_RNS_8ios_baseES4_
+ __ZNSt3__118basic_stringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B9fqe220100Ev
+ __ZNSt3__119__shared_weak_count16__release_sharedB9fqe220100Ev
+ __ZNSt3__120__shared_ptr_emplaceIN4sapc8exclaves12sharedmemory2v212MappedRegionENS_9allocatorIS5_EEEC2B9fqe220100IJRP24sharedmemory_segaccess_sRyRmR26sharedmem_permissions_ttagES7_Li0EEES7_DpOT_
+ __ZNSt3__120__throw_length_errorB9fqe220100EPKc
+ __ZNSt3__124__put_character_sequenceB9fqe220100IcNS_11char_traitsIcEEEERNS_13basic_ostreamIT_T0_EES7_PKS4_m
+ __ZNSt3__133__allocate_shared_unbounded_arrayB9fqe220100IA_St4byteNS_9allocatorIS2_EEJEEENS_10shared_ptrIT_EERKT0_mDpOT1_
+ __ZNSt3__16vectorI29audiodsputility_parameterid_sNS_9allocatorIS1_EEE20__throw_length_errorB9fqe220100Ev
+ __ZNSt3__16vectorI29audiodsputility_parameterid_sNS_9allocatorIS1_EEE24__emplace_back_slow_pathIJRKS1_EEEPS1_DpOT_
+ __ZNSt3__16vectorIPKvNS_9allocatorIS2_EEE20__throw_length_errorB9fqe220100Ev
+ __ZNSt3__16vectorISt4byteNS_9allocatorIS1_EEE11__vallocateB9fqe220100Em
+ __ZNSt3__16vectorISt4byteNS_9allocatorIS1_EEE20__throw_length_errorB9fqe220100Ev
+ __ZNSt3__16vectorIfNS_9allocatorIfEEE20__throw_length_errorB9fqe220100Ev
+ __ZNSt3__16vectorIfNS_9allocatorIfEEE24__emplace_back_slow_pathIJfEEEPfDpOT_
+ __ZNSt3__19allocatorI29audiodsputility_parameterid_sE17allocate_at_leastB9fqe220100Em
+ __ZNSt3__19allocatorIN4sapc8exclaves11ParameterIDEE17allocate_at_leastB9fqe220100Em
+ __ZNSt3__19allocatorIPKvE17allocate_at_leastB9fqe220100Em
+ __ZNSt3__19allocatorIfE17allocate_at_leastB9fqe220100Em
+ __ZSt28__throw_bad_array_new_lengthB9fqe220100v
+ __block_descriptor_tmp.107
+ __block_descriptor_tmp.114
+ __block_descriptor_tmp.121
+ __block_descriptor_tmp.127
+ __block_descriptor_tmp.133
+ __block_descriptor_tmp.140
+ __block_descriptor_tmp.149
+ __block_descriptor_tmp.156
+ __block_descriptor_tmp.162
+ __block_descriptor_tmp.170
+ __block_descriptor_tmp.179
+ __block_descriptor_tmp.190
+ __block_descriptor_tmp.94
+ __decodeSecureAudioPasscodeComponent2_block_invoke.103
+ __decodeSecureAudioPasscodeComponent2_block_invoke.103.cold.1
+ __decodeSecureAudioPasscodeComponent2_block_invoke.110
+ __decodeSecureAudioPasscodeComponent2_block_invoke.110.cold.1
+ __decodeSecureAudioPasscodeComponent2_block_invoke.117
+ __decodeSecureAudioPasscodeComponent2_block_invoke.117.cold.1
+ __decodeSecureAudioPasscodeComponent2_block_invoke.124
+ __decodeSecureAudioPasscodeComponent2_block_invoke.130
+ __decodeSecureAudioPasscodeComponent2_block_invoke.136
+ __decodeSecureAudioPasscodeComponent2_block_invoke.145
+ __decodeSecureAudioPasscodeComponent2_block_invoke.145.cold.1
+ __decodeSecureAudioPasscodeComponent2_block_invoke.152
+ __decodeSecureAudioPasscodeComponent2_block_invoke.152.cold.1
+ __decodeSecureAudioPasscodeComponent2_block_invoke.152.cold.2
+ __decodeSecureAudioPasscodeComponent2_block_invoke.152.cold.3
+ __decodeSecureAudioPasscodeComponent2_block_invoke.159
+ __decodeSecureAudioPasscodeComponent2_block_invoke.159.cold.1
+ __decodeSecureAudioPasscodeComponent2_block_invoke.159.cold.2
+ __decodeSecureAudioPasscodeComponent2_block_invoke.159.cold.3
+ __decodeSecureAudioPasscodeComponent2_block_invoke.166
+ __decodeSecureAudioPasscodeComponent2_block_invoke.166.cold.1
+ __decodeSecureAudioPasscodeComponent2_block_invoke.175
+ __decodeSecureAudioPasscodeComponent2_block_invoke.175.cold.1
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$UTF8String
+ _objc_msgSend$addObject:
+ _objc_msgSend$arrayWithCapacity:
+ _objc_msgSend$bytes
+ _objc_msgSend$count
+ _objc_msgSend$length
+ _objc_msgSend$numberWithFloat:
+ _objc_release
+ _objc_retain
+ _objc_retainAutorelease
+ _objc_retain_x8
+ _tb_component_decode_endpoint
- GCC_except_table27
- GCC_except_table31
- _OUTLINED_FUNCTION_20
- _OUTLINED_FUNCTION_21
- __ZN10applesauce2CF7details20CFArray_get_value_toINSt3__16vectorIfNS3_9allocatorIfEEEEEET_PK9__CFArray
- __ZN4sapc8exclaves25tone_generator_exclavekit26ProximityValidationManager31PairingAssetPlaybackDidCompleteEv
- __ZNKRSt3__118basic_stringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEE3strB9fqe210106Ev
- __ZNKSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEE4viewB9fqe210106Ev
- __ZNSt12length_errorC1B9fqe210106EPKc
- __ZNSt12out_of_rangeC1B9fqe210106EPKc
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB9fqe210106Ev
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B9fqe210106ILi0EEEPKc
- __ZNSt3__115allocate_sharedB9fqe210106IN4sapc8exclaves12sharedmemory2v212MappedRegionENS_9allocatorIS5_EEJRP24sharedmemory_segaccess_sRyRmR26sharedmem_permissions_ttagELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
- __ZNSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEE15__init_buf_ptrsB9fqe210106Ev
- __ZNSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B9fqe210106Ej
- __ZNSt3__116__pad_and_outputB9fqe210106IcNS_11char_traitsIcEEEENS_19ostreambuf_iteratorIT_T0_EES6_PKS4_S8_S8_RNS_8ios_baseES4_
- __ZNSt3__118basic_stringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B9fqe210106Ev
- __ZNSt3__119__shared_weak_count16__release_sharedB9fqe210106Ev
- __ZNSt3__120__shared_ptr_emplaceIN4sapc8exclaves12sharedmemory2v212MappedRegionENS_9allocatorIS5_EEEC2B9fqe210106IJRP24sharedmemory_segaccess_sRyRmR26sharedmem_permissions_ttagES7_Li0EEES7_DpOT_
- __ZNSt3__120__throw_length_errorB9fqe210106EPKc
- __ZNSt3__124__put_character_sequenceB9fqe210106IcNS_11char_traitsIcEEEERNS_13basic_ostreamIT_T0_EES7_PKS4_m
- __ZNSt3__133__allocate_shared_unbounded_arrayB9fqe210106IA_St4byteNS_9allocatorIS2_EEJEEENS_10shared_ptrIT_EERKT0_mDpOT1_
- __ZNSt3__16vectorI29audiodsputility_parameterid_sNS_9allocatorIS1_EEE20__throw_length_errorB9fqe210106Ev
- __ZNSt3__16vectorIN4sapc8exclaves11ParameterIDENS_9allocatorIS3_EEE20__throw_length_errorB9fqe210106Ev
- __ZNSt3__16vectorIN4sapc8exclaves11ParameterIDENS_9allocatorIS3_EEE9push_backB9fqe210106EOS3_
- __ZNSt3__16vectorIPKvNS_9allocatorIS2_EEE20__throw_length_errorB9fqe210106Ev
- __ZNSt3__16vectorIPKvNS_9allocatorIS2_EEE8__appendEm
- __ZNSt3__16vectorISt4byteNS_9allocatorIS1_EEE11__vallocateB9fqe210106Em
- __ZNSt3__16vectorISt4byteNS_9allocatorIS1_EEE20__throw_length_errorB9fqe210106Ev
- __ZNSt3__16vectorIfNS_9allocatorIfEEE20__throw_length_errorB9fqe210106Ev
- __ZNSt3__19allocatorI29audiodsputility_parameterid_sE17allocate_at_leastB9fqe210106Em
- __ZNSt3__19allocatorIN4sapc8exclaves11ParameterIDEE17allocate_at_leastB9fqe210106Em
- __ZNSt3__19allocatorIPKvE17allocate_at_leastB9fqe210106Em
- __ZNSt3__19allocatorIfE17allocate_at_leastB9fqe210106Em
- __ZSt28__throw_bad_array_new_lengthB9fqe210106v
- __block_descriptor_tmp.103
- __block_descriptor_tmp.110
- __block_descriptor_tmp.117
- __block_descriptor_tmp.123
- __block_descriptor_tmp.129
- __block_descriptor_tmp.136
- __block_descriptor_tmp.145
- __block_descriptor_tmp.152
- __block_descriptor_tmp.158
- __block_descriptor_tmp.166
- __block_descriptor_tmp.175
- __block_descriptor_tmp.185
- __block_descriptor_tmp.90
- __decodeSecureAudioPasscodeComponent2_block_invoke.106
- __decodeSecureAudioPasscodeComponent2_block_invoke.106.cold.1
- __decodeSecureAudioPasscodeComponent2_block_invoke.113
- __decodeSecureAudioPasscodeComponent2_block_invoke.113.cold.1
- __decodeSecureAudioPasscodeComponent2_block_invoke.120
- __decodeSecureAudioPasscodeComponent2_block_invoke.126
- __decodeSecureAudioPasscodeComponent2_block_invoke.132
- __decodeSecureAudioPasscodeComponent2_block_invoke.141
- __decodeSecureAudioPasscodeComponent2_block_invoke.141.cold.1
- __decodeSecureAudioPasscodeComponent2_block_invoke.148
- __decodeSecureAudioPasscodeComponent2_block_invoke.148.cold.1
- __decodeSecureAudioPasscodeComponent2_block_invoke.148.cold.2
- __decodeSecureAudioPasscodeComponent2_block_invoke.148.cold.3
- __decodeSecureAudioPasscodeComponent2_block_invoke.155
- __decodeSecureAudioPasscodeComponent2_block_invoke.155.cold.1
- __decodeSecureAudioPasscodeComponent2_block_invoke.155.cold.2
- __decodeSecureAudioPasscodeComponent2_block_invoke.155.cold.3
- __decodeSecureAudioPasscodeComponent2_block_invoke.162
- __decodeSecureAudioPasscodeComponent2_block_invoke.162.cold.1
- __decodeSecureAudioPasscodeComponent2_block_invoke.171
- __decodeSecureAudioPasscodeComponent2_block_invoke.171.cold.1
- __decodeSecureAudioPasscodeComponent2_block_invoke.99
- __decodeSecureAudioPasscodeComponent2_block_invoke.99.cold.1
- _audiodsputility_parameterid_pairingcurrentretrycountid__get
- _audiodsputility_parameterid_pairingcurrentretrycountid__init
- _audiodsputility_parameterid_pairingmaxretrycountid__get
- _audiodsputility_parameterid_pairingmaxretrycountid__init
- _audiodsputility_parametervalue_pairingcurrentretrycount__get
- _audiodsputility_parametervalue_pairingcurrentretrycount__init
- _audiodsputility_parametervalue_pairingmaxretrycount__get
- _audiodsputility_parametervalue_pairingmaxretrycount__init
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x21
- _objc_retain_x22
- _objc_retain_x23
- _objc_retain_x24
- _objc_retain_x27
- _tb_component_capability
- _tb_endpoint_create_with_value
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CQ9YugAAUMK5vGeHtvxeLsAqWPn9xmyISxXYXTk/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveKit.iPhoneOS.platform/Developer/SDKs/ExclaveKit.iPhoneOS27.0.Internal.sdk/System/ExclaveKit/System/Library/Frameworks/CoreAudioTypes.framework/PrivateHeaders/CoreAudioBaseTypes.hpp"
+ "I32@?0^{secureaudiopasscodecomponent_secureaudiopasscodecomponent__context_s=^^v^^v}8r^{audiodsputility_parameterid_s=Q}16@?<I@?{audiodspprocessor_audiodsp_getparameter__result_s=C(?={audiodsputility_parametererror_s=Q}{audiodsputility_parametervalue_s=Q(?={?={audiodsputility_orientationparametervalue_s=Q}}{?=B}{?=B}{?=B}{?=B}{?=B}{?=B}{?=B}{?=I}{?=B}{?=C}{?=C}{?=B}{?=B}{?=I}{?={audiodsputility_deviceanglecategory_s=Q}}{?={audiodsputility_deviceposecategory_s=Q}})})}>24"
+ "I32@?0{audiodspprocessor_audiodsp_getparameter__result_s=C(?={audiodsputility_parametererror_s=Q}{audiodsputility_parametervalue_s=Q(?={?={audiodsputility_orientationparametervalue_s=Q}}{?=B}{?=B}{?=B}{?=B}{?=B}{?=B}{?=B}{?=I}{?=B}{?=C}{?=C}{?=B}{?=B}{?=I}{?={audiodsputility_deviceanglecategory_s=Q}}{?={audiodsputility_deviceposecategory_s=Q}})})}8"
+ "I40@?0^{secureaudiopasscodecomponent_secureaudiopasscodecomponent__context_s=^^v^^v}8r^{audiodsputility_parameterid_s=Q}16r^{audiodsputility_parametervalue_s=Q(?={?={audiodsputility_orientationparametervalue_s=Q}}{?=B}{?=B}{?=B}{?=B}{?=B}{?=B}{?=B}{?=I}{?=B}{?=C}{?=C}{?=B}{?=B}{?=I}{?={audiodsputility_deviceanglecategory_s=Q}}{?={audiodsputility_deviceposecategory_s=Q}})}24@?<I@?{audiodspprocessor_audiodsp_setparameter__result_s=C(?={audiodsputility_parametererror_s=Q})}>32"
+ "Notifying proximity service that secure playback was cancelled"
+ "Processing pairing tone samples from NSArray (count: %zu)"
+ "Processing pairing tone samples from NSData (byte length: %zu, sample count: %zu)"
+ "TB_FATAL: failed to decode a client endpoint for EXDataLoader with status %u (%s:%d)\n"
+ "TB_FATAL: failed to decode a client endpoint for Proximity with status %u (%s:%d)\n"
+ "TB_FATAL: failed to decode a client endpoint for SegAccess with status %u (%s:%d)\n"
+ "TB_FATAL: invalid error returned from %s (%s:%d)\n"
+ "UTF8String"
+ "Warning: Unexpected samples data type: %s"
+ "addObject:"
+ "arrayWithCapacity:"
+ "bytes"
+ "count"
+ "fetchPasscode: error = %d"
+ "getParameter"
+ "length"
+ "numberWithFloat:"
+ "performIO"
+ "prepareForIO"
+ "prepareForInputIO"
+ "prepareForOutputIO"
+ "setParameter"
+ "unconfigure"
- "("
- "/AppleInternal/Library/BuildRoots/4~CNprugDGICLs9wN2OuvuXu2X2h9d1e4P_r2p224/Applications/Xcode.app/Contents/Developer/Platforms/ExclaveKit.iPhoneOS.platform/Developer/SDKs/ExclaveKit.iPhoneOS26.5.Internal.sdk/System/ExclaveKit/System/Library/Frameworks/CoreAudioTypes.framework/PrivateHeaders/CoreAudioBaseTypes.hpp"
- "I32@?0^{secureaudiopasscodecomponent_secureaudiopasscodecomponent__context_s=^^v^^v}8r^{audiodsputility_parameterid_s=Q}16@?<I@?{audiodspprocessor_audiodsp_getparameter__result_s=C(?={audiodsputility_parametererror_s=Q}{audiodsputility_parametervalue_s=Q(?={?={audiodsputility_orientationparametervalue_s=Q}}{?=B}{?=B}{?=B}{?=B}{?=B}{?=B}{?=B}{?=I}{?=B}{?=C}{?=C}{?=B})})}>24"
- "I32@?0{audiodspprocessor_audiodsp_getparameter__result_s=C(?={audiodsputility_parametererror_s=Q}{audiodsputility_parametervalue_s=Q(?={?={audiodsputility_orientationparametervalue_s=Q}}{?=B}{?=B}{?=B}{?=B}{?=B}{?=B}{?=B}{?=I}{?=B}{?=C}{?=C}{?=B})})}8"
- "I40@?0^{secureaudiopasscodecomponent_secureaudiopasscodecomponent__context_s=^^v^^v}8r^{audiodsputility_parameterid_s=Q}16r^{audiodsputility_parametervalue_s=Q(?={?={audiodsputility_orientationparametervalue_s=Q}}{?=B}{?=B}{?=B}{?=B}{?=B}{?=B}{?=B}{?=I}{?=B}{?=C}{?=C}{?=B})}24@?<I@?{audiodspprocessor_audiodsp_setparameter__result_s=C(?={audiodsputility_parametererror_s=Q})}>32"
- "TB_FATAL: invalid error returned from getParameter (%s:%d)\n"
- "TB_FATAL: invalid error returned from performIO (%s:%d)\n"
- "TB_FATAL: invalid error returned from prepareForIO (%s:%d)\n"
- "TB_FATAL: invalid error returned from prepareForInputIO (%s:%d)\n"
- "TB_FATAL: invalid error returned from prepareForOutputIO (%s:%d)\n"
- "TB_FATAL: invalid error returned from setParameter (%s:%d)\n"
- "TB_FATAL: invalid error returned from unconfigure (%s:%d)\n"
- "fetchPasscode: error = %d, retry_count = %llu"
- "no error"

```
