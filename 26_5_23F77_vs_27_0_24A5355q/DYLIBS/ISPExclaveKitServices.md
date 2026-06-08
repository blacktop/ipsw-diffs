## ISPExclaveKitServices

> `/System/Library/PrivateFrameworks/ISPExclaveKitServices.framework/ISPExclaveKitServices`

```diff

-5.504.0.0.0
-  __TEXT.__text: 0x284ec
-  __TEXT.__auth_stubs: 0x730
-  __TEXT.__const: 0x2c0
-  __TEXT.__gcc_except_tab: 0x7d0
-  __TEXT.__oslogstring: 0x3092
-  __TEXT.__cstring: 0x6a15
-  __TEXT.__unwind_info: 0x7f8
-  __DATA_CONST.__got: 0x48
-  __DATA_CONST.__const: 0xed8
-  __AUTH_CONST.__auth_got: 0x3a0
+6.10.3.0.0
+  __TEXT.__text: 0x279e4
+  __TEXT.__const: 0x290
+  __TEXT.__gcc_except_tab: 0x774
+  __TEXT.__oslogstring: 0x30b9
+  __TEXT.__cstring: 0x6dd2
+  __TEXT.__unwind_info: 0x838
+  __TEXT.__auth_stubs: 0x0
+  __DATA_CONST.__const: 0xf00
+  __DATA_CONST.__weak_got: 0x8
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__cfstring: 0x4c0
-  __DATA.__data: 0x116750
-  __DATA.__common: 0x20
+  __AUTH_CONST.__weak_auth_got: 0x28
+  __AUTH_CONST.__auth_got: 0x388
+  __DATA.__data: 0x5c90
+  __DATA.__common: 0x10
   __DATA.__bss: 0x28
+  __DATA_DIRTY.__data: 0x110ad0
+  __DATA_DIRTY.__common: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/PrivateFrameworks/Tightbeam.framework/Tightbeam
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: D416C4EB-68C4-379F-8A76-8A4A4637AE40
-  Functions: 988
-  Symbols:   2316
-  CStrings:  697
+  UUID: 76279AB5-1917-3C9E-AB47-97A802814579
+  Functions: 1000
+  Symbols:   2292
+  CStrings:  703
 
Symbols:
+ _OUTLINED_FUNCTION_24
+ _OUTLINED_FUNCTION_25
+ __Z21exclaveKitReadDefaultPK10__CFStringS1_iPb
+ __Z22exclaveKitDefaultIsSetP21ISPExclaveKitDefaults19eExclaveKitDefaults
+ __Z28ispExclaveKitCommandChRunFidP20sExclaveKitIspCmdHdr.cold.3
+ __Z28ispExclaveKitCommandChRunFidP20sExclaveKitIspCmdHdr.cold.4
+ __Z28ispExclaveKitCommandChRunFidP20sExclaveKitIspCmdHdr.cold.5
+ __Z33isNewSharedMemoryReplayDefaultSetP21ISPExclaveKitDefaults
+ __Z36isDataCollectionBufferDumpDefaultSetP21ISPExclaveKitDefaults
+ __Z43isNewSharedMemoryReplayBufferDumpDefaultSetP21ISPExclaveKitDefaults
+ __ZNSt11logic_errorC2EPKc
+ __ZNSt12length_errorC1B9fqe220100EPKc
+ __ZNSt12length_errorD1Ev
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB9fqe220100Ev
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE22__init_internal_bufferB9fqe220100Em
+ __ZNSt3__119__allocate_at_leastB9fqe220100INS_9allocatorIP21FileServiceBufferInfoEENS_16allocator_traitsIS4_EEEENS_19__allocation_resultINT0_7pointerENS8_9size_typeEEERT_m
+ __ZNSt3__120__throw_length_errorB9fqe220100EPKc
+ __ZNSt3__15dequeI21FileServiceBufferInfoNS_9allocatorIS1_EEE26__maybe_remove_front_spareB9fqe220100Eb
+ __ZNSt3__15dequeI21FileServiceBufferInfoNS_9allocatorIS1_EEE9pop_frontEv
+ __ZNSt3__15dequeI21FileServiceBufferInfoNS_9allocatorIS1_EEED2B9fqe220100Ev
+ __ZSt28__throw_bad_array_new_lengthB9fqe220100v
+ __ZTISt12length_error
+ __ZTVSt12length_error
+ ____Z28ispExclaveKitCommandChRunFidP20sExclaveKitIspCmdHdr_block_invoke
+ ___block_descriptor_tmp.14
+ ___block_descriptor_tmp.763
+ ___block_descriptor_tmp.764
+ ___cxa_free_exception
+ _fidflowmodule_bufferdescriptor__raw_decode
+ _fidflowmodule_ekfidflow_channelrunfidflow
+ _fidflowmodule_ekfidflow_channelrunfidflow.cold.1
+ _fidflowmodule_fidresult__decode
+ _fidflowmodule_fidresult__decode.cold.1
+ _fidflowmodule_frameinfo__raw_decode
+ _ispexclavekitshared_ekstrobetype__raw_decode
+ _ispexclavekitshared_ekstrobetype__raw_decode.cold.1
- _OUTLINED_FUNCTION_18
- _OUTLINED_FUNCTION_19
- _OUTLINED_FUNCTION_23
- __Z21exclaveKitReadDefaultPK10__CFStringS1_i
- __ZNSt3__119__allocate_at_leastB9nqe210106INS_9allocatorIP21FileServiceBufferInfoEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__15dequeI21FileServiceBufferInfoNS_9allocatorIS1_EEE26__maybe_remove_front_spareB9nqe210106Eb
- __ZNSt3__15dequeI21FileServiceBufferInfoNS_9allocatorIS1_EEED2B9nqe210106Ev
- __ZSt28__throw_bad_array_new_lengthB9nqe210106v
- ___block_descriptor_tmp.791
- ___block_descriptor_tmp.792
CStrings:
+ "%s:%d - RunFid\n"
+ "%s:%d - pCmdChFid->result.frameInfo.rawFrame.bufferId: %llu\n"
+ "TB_FATAL: invalid result returned from channelRunFidFlow"
+ "TB_FATAL: invalid result returned from channelRunFidFlow (%s:%d)\n"
+ "basic_string"
+ "decodeFidResult"
+ "v288@?0{fidflowmodule_ekfidflow_channelrunfidflow__result_s=C(?={exclavesispshared_exclavesisperror_s=Q}{fidflowmodule_fidresult_s={fidflowmodule_frameinfo_s=Q{fidflowmodule_fidframetype_s=Q}I{fidflowmodule_bufferdescriptor_s=QQQ{fidflowmodule_bufferformatdescriptor_s=IIII{fidflowmodule_elementformat_s=Q}{fidflowmodule_channellayout_s=Q}I}}{fidflowmodule_bufferdescriptor_s=QQQ{fidflowmodule_bufferformatdescriptor_s=IIII{fidflowmodule_elementformat_s=Q}{fidflowmodule_channellayout_s=Q}I}}{fidflowmodule_bufferdescriptor_s=QQQ{fidflowmodule_bufferformatdescriptor_s=IIII{fidflowmodule_elementformat_s=Q}{fidflowmodule_channellayout_s=Q}I}}}BI{fidflowmodule_fidattentioninfo_s={fidflowmodule_facerectf_s=ffff}{fidflowmodule_headpose_s=fff}{fidflowmodule_vector2f_s=ff}{fidflowmodule_eyeopen_s=ff}B}})}8"
- "%s:%d - ERROR: Unsupported platform!\n"

```
