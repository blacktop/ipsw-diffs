## SpeechRecognitionCore

> `/System/Library/PrivateFrameworks/SpeechRecognitionCore.framework/SpeechRecognitionCore`

```diff

-6.3.30.10.0
-  __TEXT.__text: 0xe5b0
-  __TEXT.__auth_stubs: 0xca0
-  __TEXT.__const: 0xd8
-  __TEXT.__cstring: 0x11d1
-  __TEXT.__oslogstring: 0x344
-  __TEXT.__gcc_except_tab: 0x528
+6.3.54.0.0
+  __TEXT.__text: 0x11174
+  __TEXT.__auth_stubs: 0xf10
+  __TEXT.__objc_methlist: 0x6b4
+  __TEXT.__cstring: 0x1358
+  __TEXT.__gcc_except_tab: 0xf94
+  __TEXT.__const: 0xea
+  __TEXT.__oslogstring: 0x440
   __TEXT.__ustring: 0xc
-  __TEXT.__unwind_info: 0x5d0
-  __DATA_CONST.__got: 0xe0
-  __DATA_CONST.__const: 0x528
+  __TEXT.__swift5_typeref: 0x28
+  __TEXT.__swift5_fieldmd: 0x10
+  __TEXT.__unwind_info: 0x920
+  __TEXT.__objc_classname: 0x115
+  __TEXT.__objc_methname: 0xe63
+  __TEXT.__objc_methtype: 0x520
+  __TEXT.__objc_stubs: 0x760
+  __DATA_CONST.__got: 0x130
+  __DATA_CONST.__const: 0x458
+  __DATA_CONST.__objc_classlist: 0x30
+  __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __AUTH_CONST.__auth_got: 0x658
-  __AUTH_CONST.__const: 0x4b0
-  __AUTH_CONST.__cfstring: 0xa00
+  __DATA_CONST.__objc_selrefs: 0x3f8
+  __DATA_CONST.__objc_protorefs: 0x20
+  __DATA_CONST.__objc_superrefs: 0x30
+  __AUTH_CONST.__auth_got: 0x798
+  __AUTH_CONST.__const: 0x4d0
+  __AUTH_CONST.__cfstring: 0xba0
+  __AUTH_CONST.__objc_const: 0xcc0
+  __AUTH.__objc_data: 0x1e0
   __AUTH.__data: 0x180
-  __DATA.__data: 0x1f8
+  __DATA.__objc_ivar: 0x80
+  __DATA.__data: 0x490
   __DATA.__bss: 0xe8
   __DATA.__common: 0x28
   - /System/Library/Frameworks/CoreAudio.framework/CoreAudio
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
+  - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libicucore.A.dylib
-  UUID: 70D37070-1558-33D0-BC9D-6355C89083E8
-  Functions: 352
-  Symbols:   1159
-  CStrings:  321
+  - /usr/lib/libobjc.A.dylib
+  - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftDarwin.dylib
+  - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
+  - /usr/lib/swift/libswiftos.dylib
+  UUID: 4710841B-681B-36BD-B2C3-76F32D96838B
+  Functions: 453
+  Symbols:   1441
+  CStrings:  609
 
Symbols:
+ +[SRDTranscriptionResult supportsSecureCoding]
+ +[SRDTranscriptionToken supportsSecureCoding]
+ -[RXXPCCSpeechRecognitionClientService .cxx_destruct]
+ -[RXXPCCSpeechRecognitionClientService forwardInvocation:]
+ -[RXXPCCSpeechRecognitionClientService initWithRXXPC:externalServiceClient:]
+ -[RXXPCCSpeechRecognitionClientService legacyClientEventWithMessage:]
+ -[RXXPCCSpeechRecognitionClientService pong:]
+ -[RXXPCCSpeechRecognitionClientService recognizedEventWithLegacyMessage:result:]
+ -[SRDConnection .cxx_destruct]
+ -[SRDConnection initWithLocale:flags:delegate:]
+ -[SRDConnection recognitionSystem]
+ -[SRDLanguageObject .cxx_destruct]
+ -[SRDLanguageObject dealloc]
+ -[SRDLanguageObject initWithLanguageObject:transcriptionResult:]
+ -[SRDLanguageObject languageObject]
+ -[SRDLanguageObject setLanguageObject:]
+ -[SRDLanguageObject setTranscriptionResult:]
+ -[SRDLanguageObject transcriptionResult]
+ -[SRDRecognizer .cxx_destruct]
+ -[SRDRecognizer dealloc]
+ -[SRDRecognizer initWithRecognitionSystem:delegate:flags:]
+ -[SRDRecognizer recognizer]
+ -[SRDTranscriptionResult .cxx_destruct]
+ -[SRDTranscriptionResult encodeWithCoder:]
+ -[SRDTranscriptionResult firstBestResult]
+ -[SRDTranscriptionResult initWithCoder:]
+ -[SRDTranscriptionResult isPartialResult]
+ -[SRDTranscriptionResult nBestResults]
+ -[SRDTranscriptionResult preITN_firstBestResult]
+ -[SRDTranscriptionResult preITN_nBestResults]
+ -[SRDTranscriptionResult preITN_tokenSausage]
+ -[SRDTranscriptionResult setFirstBestResult:]
+ -[SRDTranscriptionResult setIsPartialResult:]
+ -[SRDTranscriptionResult setNBestResults:]
+ -[SRDTranscriptionResult setPreITN_firstBestResult:]
+ -[SRDTranscriptionResult setPreITN_nBestResults:]
+ -[SRDTranscriptionResult setPreITN_tokenSausage:]
+ -[SRDTranscriptionResult setTokenSausage:]
+ -[SRDTranscriptionResult setUtteranceID:]
+ -[SRDTranscriptionResult tokenSausage]
+ -[SRDTranscriptionResult utteranceID]
+ -[SRDTranscriptionToken .cxx_destruct]
+ -[SRDTranscriptionToken appendedAutoPunctuation]
+ -[SRDTranscriptionToken confidence]
+ -[SRDTranscriptionToken debugDescription]
+ -[SRDTranscriptionToken description]
+ -[SRDTranscriptionToken encodeWithCoder:]
+ -[SRDTranscriptionToken end]
+ -[SRDTranscriptionToken hasSpaceAfter]
+ -[SRDTranscriptionToken hasSpaceBefore]
+ -[SRDTranscriptionToken initWithCoder:]
+ -[SRDTranscriptionToken initWithTokenName:start:end:silenceStart:confidence:hasSpaceAfter:hasSpaceBefore:phoneSequence:ipaPhoneSequence:]
+ -[SRDTranscriptionToken ipaPhoneSequence]
+ -[SRDTranscriptionToken isModifiedByAutoPunctuation]
+ -[SRDTranscriptionToken phoneSequence]
+ -[SRDTranscriptionToken prependedAutoPunctuation]
+ -[SRDTranscriptionToken setAppendedAutoPunctuation:]
+ -[SRDTranscriptionToken setConfidence:]
+ -[SRDTranscriptionToken setEnd:]
+ -[SRDTranscriptionToken setHasSpaceAfter:]
+ -[SRDTranscriptionToken setHasSpaceBefore:]
+ -[SRDTranscriptionToken setIpaPhoneSequence:]
+ -[SRDTranscriptionToken setIsModifiedByAutoPunctuation:]
+ -[SRDTranscriptionToken setPhoneSequence:]
+ -[SRDTranscriptionToken setPrependedAutoPunctuation:]
+ -[SRDTranscriptionToken setSilenceStart:]
+ -[SRDTranscriptionToken setStart:]
+ -[SRDTranscriptionToken setTokenName:]
+ -[SRDTranscriptionToken silenceStart]
+ -[SRDTranscriptionToken start]
+ -[SRDTranscriptionToken tokenName]
+ GCC_except_table1
+ GCC_except_table10
+ GCC_except_table12
+ GCC_except_table15
+ GCC_except_table17
+ GCC_except_table19
+ GCC_except_table2
+ GCC_except_table29
+ GCC_except_table30
+ GCC_except_table31
+ GCC_except_table32
+ GCC_except_table34
+ GCC_except_table35
+ GCC_except_table36
+ GCC_except_table37
+ GCC_except_table39
+ GCC_except_table40
+ GCC_except_table41
+ GCC_except_table47
+ GCC_except_table48
+ GCC_except_table5
+ GCC_except_table51
+ GCC_except_table52
+ GCC_except_table54
+ GCC_except_table56
+ GCC_except_table59
+ GCC_except_table60
+ GCC_except_table62
+ GCC_except_table63
+ GCC_except_table64
+ GCC_except_table73
+ GCC_except_table86
+ GCC_except_table87
+ GCC_except_table92
+ _OBJC_CLASS_$_NSArray
+ _OBJC_CLASS_$_NSNumber
+ _OBJC_CLASS_$_NSObject
+ _OBJC_CLASS_$_NSSet
+ _OBJC_CLASS_$_NSString
+ _OBJC_CLASS_$_NSXPCConnection
+ _OBJC_CLASS_$_NSXPCInterface
+ _OBJC_CLASS_$_NSXPCListenerEndpoint
+ _OBJC_CLASS_$_RXXPCCSpeechRecognitionClientService
+ _OBJC_CLASS_$_SRDConnection
+ _OBJC_CLASS_$_SRDLanguageObject
+ _OBJC_CLASS_$_SRDRecognizer
+ _OBJC_CLASS_$_SRDTranscriptionResult
+ _OBJC_CLASS_$_SRDTranscriptionToken
+ _OBJC_IVAR_$_RXXPCCSpeechRecognitionClientService._externalServiceClient
+ _OBJC_IVAR_$_RXXPCCSpeechRecognitionClientService._xpc
+ _OBJC_IVAR_$_SRDConnection._delegate
+ _OBJC_IVAR_$_SRDConnection._flags
+ _OBJC_IVAR_$_SRDConnection._locale
+ _OBJC_IVAR_$_SRDConnection._recognitionSystem
+ _OBJC_IVAR_$_SRDLanguageObject._languageObject
+ _OBJC_IVAR_$_SRDLanguageObject._transcriptionResult
+ _OBJC_IVAR_$_SRDRecognizer._delegate
+ _OBJC_IVAR_$_SRDRecognizer._flags
+ _OBJC_IVAR_$_SRDRecognizer._recognitionSystem
+ _OBJC_IVAR_$_SRDRecognizer._recognizer
+ _OBJC_IVAR_$_SRDTranscriptionResult._firstBestResult
+ _OBJC_IVAR_$_SRDTranscriptionResult._isPartialResult
+ _OBJC_IVAR_$_SRDTranscriptionResult._nBestResults
+ _OBJC_IVAR_$_SRDTranscriptionResult._preITN_firstBestResult
+ _OBJC_IVAR_$_SRDTranscriptionResult._preITN_nBestResults
+ _OBJC_IVAR_$_SRDTranscriptionResult._preITN_tokenSausage
+ _OBJC_IVAR_$_SRDTranscriptionResult._tokenSausage
+ _OBJC_IVAR_$_SRDTranscriptionResult._utteranceID
+ _OBJC_IVAR_$_SRDTranscriptionToken._appendedAutoPunctuation
+ _OBJC_IVAR_$_SRDTranscriptionToken._confidence
+ _OBJC_IVAR_$_SRDTranscriptionToken._end
+ _OBJC_IVAR_$_SRDTranscriptionToken._hasSpaceAfter
+ _OBJC_IVAR_$_SRDTranscriptionToken._hasSpaceBefore
+ _OBJC_IVAR_$_SRDTranscriptionToken._ipaPhoneSequence
+ _OBJC_IVAR_$_SRDTranscriptionToken._isModifiedByAutoPunctuation
+ _OBJC_IVAR_$_SRDTranscriptionToken._phoneSequence
+ _OBJC_IVAR_$_SRDTranscriptionToken._prependedAutoPunctuation
+ _OBJC_IVAR_$_SRDTranscriptionToken._silenceStart
+ _OBJC_IVAR_$_SRDTranscriptionToken._start
+ _OBJC_IVAR_$_SRDTranscriptionToken._tokenName
+ _OBJC_METACLASS_$_NSObject
+ _OBJC_METACLASS_$_RXXPCCSpeechRecognitionClientService
+ _OBJC_METACLASS_$_SRDConnection
+ _OBJC_METACLASS_$_SRDLanguageObject
+ _OBJC_METACLASS_$_SRDRecognizer
+ _OBJC_METACLASS_$_SRDTranscriptionResult
+ _OBJC_METACLASS_$_SRDTranscriptionToken
+ _RXRecognitionSystemCreateWithServiceClient
+ _RXRecognizerCreateEx
+ __OBJC_$_CLASS_METHODS_SRDTranscriptionResult
+ __OBJC_$_CLASS_METHODS_SRDTranscriptionToken
+ __OBJC_$_CLASS_PROP_LIST_NSSecureCoding
+ __OBJC_$_CLASS_PROP_LIST_SRDTranscriptionResult
+ __OBJC_$_CLASS_PROP_LIST_SRDTranscriptionToken
+ __OBJC_$_INSTANCE_METHODS_RXXPCCSpeechRecognitionClientService
+ __OBJC_$_INSTANCE_METHODS_SRDConnection
+ __OBJC_$_INSTANCE_METHODS_SRDLanguageObject
+ __OBJC_$_INSTANCE_METHODS_SRDRecognizer
+ __OBJC_$_INSTANCE_METHODS_SRDTranscriptionResult
+ __OBJC_$_INSTANCE_METHODS_SRDTranscriptionToken
+ __OBJC_$_INSTANCE_VARIABLES_RXXPCCSpeechRecognitionClientService
+ __OBJC_$_INSTANCE_VARIABLES_SRDConnection
+ __OBJC_$_INSTANCE_VARIABLES_SRDLanguageObject
+ __OBJC_$_INSTANCE_VARIABLES_SRDRecognizer
+ __OBJC_$_INSTANCE_VARIABLES_SRDTranscriptionResult
+ __OBJC_$_INSTANCE_VARIABLES_SRDTranscriptionToken
+ __OBJC_$_PROP_LIST_NSObject
+ __OBJC_$_PROP_LIST_RXXPCCSpeechRecognitionClientService
+ __OBJC_$_PROP_LIST_SRDLanguageObject
+ __OBJC_$_PROP_LIST_SRDTranscriptionResult
+ __OBJC_$_PROP_LIST_SRDTranscriptionToken
+ __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SRDBrokerProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SRDClientProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SRDInternalClientProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__TtP21SpeechRecognitionCore11SRDProtocol_
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SRDBrokerProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SRDClientProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SRDInternalClientProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES__TtP21SpeechRecognitionCore11SRDProtocol_
+ __OBJC_$_PROTOCOL_REFS_NSSecureCoding
+ __OBJC_$_PROTOCOL_REFS_SRDClientProtocol
+ __OBJC_$_PROTOCOL_REFS_SRDInternalClientProtocol
+ __OBJC_$_PROTOCOL_REFS__TtP21SpeechRecognitionCore11SRDProtocol_
+ __OBJC_CLASS_PROTOCOLS_$_RXXPCCSpeechRecognitionClientService
+ __OBJC_CLASS_PROTOCOLS_$_SRDTranscriptionResult
+ __OBJC_CLASS_PROTOCOLS_$_SRDTranscriptionToken
+ __OBJC_CLASS_RO_$_RXXPCCSpeechRecognitionClientService
+ __OBJC_CLASS_RO_$_SRDConnection
+ __OBJC_CLASS_RO_$_SRDLanguageObject
+ __OBJC_CLASS_RO_$_SRDRecognizer
+ __OBJC_CLASS_RO_$_SRDTranscriptionResult
+ __OBJC_CLASS_RO_$_SRDTranscriptionToken
+ __OBJC_LABEL_PROTOCOL_$_NSCoding
+ __OBJC_LABEL_PROTOCOL_$_NSObject
+ __OBJC_LABEL_PROTOCOL_$_NSSecureCoding
+ __OBJC_LABEL_PROTOCOL_$_SRDBrokerProtocol
+ __OBJC_LABEL_PROTOCOL_$_SRDClientProtocol
+ __OBJC_LABEL_PROTOCOL_$_SRDInternalClientProtocol
+ __OBJC_LABEL_PROTOCOL_$__TtP21SpeechRecognitionCore11SRDProtocol_
+ __OBJC_METACLASS_RO_$_RXXPCCSpeechRecognitionClientService
+ __OBJC_METACLASS_RO_$_SRDConnection
+ __OBJC_METACLASS_RO_$_SRDLanguageObject
+ __OBJC_METACLASS_RO_$_SRDRecognizer
+ __OBJC_METACLASS_RO_$_SRDTranscriptionResult
+ __OBJC_METACLASS_RO_$_SRDTranscriptionToken
+ __OBJC_PROTOCOL_$_NSCoding
+ __OBJC_PROTOCOL_$_NSObject
+ __OBJC_PROTOCOL_$_NSSecureCoding
+ __OBJC_PROTOCOL_$_SRDBrokerProtocol
+ __OBJC_PROTOCOL_$_SRDClientProtocol
+ __OBJC_PROTOCOL_$_SRDInternalClientProtocol
+ __OBJC_PROTOCOL_$__TtP21SpeechRecognitionCore11SRDProtocol_
+ __OBJC_PROTOCOL_REFERENCE_$_SRDInternalClientProtocol
+ __OBJC_PROTOCOL_REFERENCE_$__TtP21SpeechRecognitionCore11SRDProtocol_
+ __PROTOCOL_INSTANCE_METHODS__TtP21SpeechRecognitionCore11SRDProtocol_
+ __PROTOCOL_METHOD_TYPES__TtP21SpeechRecognitionCore11SRDProtocol_
+ __PROTOCOL_PROTOCOLS__TtP21SpeechRecognitionCore11SRDProtocol_
+ __PROTOCOL__TtP21SpeechRecognitionCore11SRDProtocol_
+ __ZL13GetDaemonLMIDPU24objcproto13OS_xpc_object8NSObjectRy
+ __ZN12RXRecognizer10InitializeEP19RXRecognitionSystemP13SRDRecognizerPU32objcproto21SRDRecognizerDelegate11objc_objectm
+ __ZN12RXRecognizer10RecognizedEP16RXLanguageObjectP22SRDTranscriptionResult
+ __ZN12RXRecognizer10RecognizedEPU24objcproto13OS_xpc_object8NSObjectP22SRDTranscriptionResult
+ __ZN12RXRecognizer9SerializeEPU24objcproto13OS_xpc_object8NSObjectP19RXRecognitionSystem
+ __ZN12RXVocabulary9SerializeEPU24objcproto13OS_xpc_object8NSObjectP19RXRecognitionSystem
+ __ZN16RXLanguageObject20CreateFromSerializedEPU24objcproto13OS_xpc_object8NSObjectP12RXResultDesc
+ __ZN16RXLanguageObject9SerializeEPU24objcproto13OS_xpc_object8NSObjectP19RXRecognitionSystem
+ __ZN19RXRecognitionSystem10InitializeEPK10__CFLocalemPU28objcproto17SRDClientProtocol11objc_object
+ __ZN19RXRecognitionSystem11BrokerEventEPU24objcproto13OS_xpc_object8NSObject
+ __ZN19RXRecognitionSystem8CallbackEPU24objcproto13OS_xpc_object8NSObject
+ __ZN19RXRecognitionSystem8CallbackEyPU24objcproto13OS_xpc_object8NSObject
+ __ZN5RXXPC11ClientEventEPU24objcproto13OS_xpc_object8NSObject
+ __ZN5RXXPC11SendMessageEPU24objcproto13OS_xpc_object8NSObjectb
+ __ZN5RXXPC12SerializeURLEPU24objcproto13OS_xpc_object8NSObjectPK7__CFURL
+ __ZN5RXXPC13CommitChangesEPU24objcproto13OS_xpc_object8NSObjectS2_
+ __ZN5RXXPC13RemoteServiceEv
+ __ZN5RXXPC14CreateInstanceEPK10__CFLocalemPU28objcproto17SRDClientProtocol11objc_object
+ __ZN5RXXPC16DownloadCallbackEPU24objcproto13OS_xpc_object8NSObject
+ __ZN5RXXPC16SerializeCFArrayEPU24objcproto13OS_xpc_object8NSObjectPKcPK9__CFArray
+ __ZN5RXXPC17SerializeCFStringEPU24objcproto13OS_xpc_object8NSObjectPKcPK10__CFString
+ __ZN5RXXPC21TriggerVocabularySyncEv
+ __ZN5RXXPC24RemoteSynchronousServiceEv
+ __ZN5RXXPC24SendMessageWithReplySyncEPU24objcproto13OS_xpc_object8NSObject
+ __ZN5RXXPC30SendBrokerMessageWithReplySyncEPU24objcproto13OS_xpc_object8NSObjectb
+ __ZN5RXXPC30SendBrokerMessageWithReplySyncEPU24objcproto13OS_xpc_object8NSObjectb.cold.1
+ __ZN5RXXPC35RemoveAllVocabularyEntriesFromCloudEv
+ __ZN5RXXPC37CopySupportedLanguagesForVoiceControlEv
+ __ZN8RXObject9SerializeEPU24objcproto13OS_xpc_object8NSObjectP19RXRecognitionSystem
+ __ZNKSt3__111__copy_implclB8ne200100INS_21__tree_const_iteratorIP8RXObjectPNS_11__tree_nodeIS4_PvEElEES9_NS_20back_insert_iteratorINS_6vectorIS4_NS_9allocatorIS4_EEEEEEEENS_4pairIT_T1_EESH_T0_SI_
+ __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE4findB8ne200100ERKS5_m
+ __ZNSt12length_errorC1B8ne200100EPKc
+ __ZNSt12out_of_rangeC1B8ne200100EPKc
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_out_of_rangeB8ne200100Ev
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B8ne200100ILi0EEEPKc
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ne200100ENS_24__uninitialized_size_tagEmRKS4_
+ __ZNSt3__116__set_differenceB8ne200100INS_6__lessIvvEERNS_21__tree_const_iteratorIP8RXObjectPNS_11__tree_nodeIS5_PvEElEESB_SB_SB_RNS_20back_insert_iteratorINS_6vectorIS5_NS_9allocatorIS5_EEEEEEEENS_4pairIu14__remove_cvrefIT0_Eu14__remove_cvrefIT4_EEEOSK_OT1_OT2_OT3_OSM_OT_
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIP16RXLanguageObjectEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIP19RXRecognitionSystemEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIP8RXObjectEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIPKvEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIyEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
+ __ZNSt3__120__throw_length_errorB8ne200100EPKc
+ __ZNSt3__120__throw_out_of_rangeB8ne200100EPKc
+ __ZNSt3__120back_insert_iteratorINS_6vectorIP8RXObjectNS_9allocatorIS3_EEEEEaSB8ne200100ERKS3_
+ __ZNSt3__127__tree_balance_after_insertB8ne200100IPNS_16__tree_node_baseIPvEEEEvT_S5_
+ __ZNSt3__16vectorIP16RXLanguageObjectNS_9allocatorIS2_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIP19RXRecognitionSystemNS_9allocatorIS2_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIP8RXObjectNS_9allocatorIS2_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIPKvNS_9allocatorIS2_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIPKvNS_9allocatorIS2_EEE9push_backB8ne200100EOS2_
+ __ZNSt3__16vectorIyNS_9allocatorIyEEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIyNS_9allocatorIyEEE9push_backB8ne200100EOy
+ __ZNSt3__1plB8ne200100IcNS_11char_traitsIcEENS_9allocatorIcEEEENS_12basic_stringIT_T0_T1_EERKS9_SB_
+ __ZSt28__throw_bad_array_new_lengthB8ne200100v
+ __ZZN5RXXPC30SendBrokerMessageWithReplySyncEPU24objcproto13OS_xpc_object8NSObjectbE14sRXXBrokerConn
+ __ZZN5RXXPC30SendBrokerMessageWithReplySyncEPU24objcproto13OS_xpc_object8NSObjectbE14sRXXBrokerInit
+ ___80-[RXXPCCSpeechRecognitionClientService recognizedEventWithLegacyMessage:result:]_block_invoke
+ ___Block_byref_object_copy_
+ ___Block_byref_object_dispose_
+ ____ZL13GetDaemonLMIDPU24objcproto13OS_xpc_object8NSObjectRy_block_invoke
+ ____ZN12RXRecognizer10RecognizedEPU24objcproto13OS_xpc_object8NSObjectP22SRDTranscriptionResult_block_invoke
+ ____ZN12RXRecognizer9SerializeEPU24objcproto13OS_xpc_object8NSObjectP19RXRecognitionSystem_block_invoke
+ ____ZN16RXLanguageObject20CreateFromSerializedEPU24objcproto13OS_xpc_object8NSObjectP12RXResultDesc_block_invoke
+ ____ZN19RXRecognitionSystem10InitializeEPK10__CFLocalemPU28objcproto17SRDClientProtocol11objc_object_block_invoke
+ ____ZN19RXRecognitionSystem24PhoneticNeighborsForTextEPK10__CFString_block_invoke
+ ____ZN5RXXPC11ClientEventEPU24objcproto13OS_xpc_object8NSObject_block_invoke
+ ____ZN5RXXPC11ClientEventEPU24objcproto13OS_xpc_object8NSObject_block_invoke.117
+ ____ZN5RXXPC11ClientEventEPU24objcproto13OS_xpc_object8NSObject_block_invoke_2
+ ____ZN5RXXPC11ClientEventEPU24objcproto13OS_xpc_object8NSObject_block_invoke_3
+ ____ZN5RXXPC11SendMessageEPU24objcproto13OS_xpc_object8NSObjectb_block_invoke
+ ____ZN5RXXPC19EstablishConnectionEv_block_invoke.113
+ ____ZN5RXXPC19EstablishConnectionEv_block_invoke.114
+ ____ZN5RXXPC19EstablishConnectionEv_block_invoke.115
+ ____ZN5RXXPC19EstablishConnectionEv_block_invoke_2
+ ____ZN5RXXPC19EstablishConnectionEv_block_invoke_3
+ ____ZN5RXXPC24RemoteSynchronousServiceEv_block_invoke
+ ____ZN5RXXPC24SendMessageWithReplySyncEPU24objcproto13OS_xpc_object8NSObject_block_invoke
+ ____ZN5RXXPC30SendBrokerMessageWithReplySyncEPU24objcproto13OS_xpc_object8NSObjectb_block_invoke
+ ____ZN5RXXPC30SendBrokerMessageWithReplySyncEPU24objcproto13OS_xpc_object8NSObjectb_block_invoke_2
+ ___block_descriptor_32_e17_v16?0"NSError"8l
+ ___block_descriptor_32_e22_v16?0"NSDictionary"8l
+ ___block_descriptor_32_e33_v16?0"NSObject<OS_xpc_object>"8l
+ ___block_descriptor_32_e5_v8?0l
+ ___block_descriptor_40_e36_B24?0Q8"NSObject<OS_xpc_object>"16l
+ ___block_descriptor_40_e5_v8?0l
+ ___block_descriptor_40_e98_v20?0i8^{RXXPC=BBBQ^{__CFString}^{__CFString}Q^{__CFArray}Q{_opaque_pthread_mutex_t=q[56c]}}12l
+ ___block_descriptor_40_ea8_32r_e17_v16?0"NSArray"8lr32l8
+ ___block_descriptor_40_ea8_32r_e36_B24?0Q8"NSObject<OS_xpc_object>"16lr32l8
+ ___block_descriptor_40_ea8_32r_e37_B24?0r*8"NSObject<OS_xpc_object>"16lr32l8
+ ___block_descriptor_40_ea8_32s_e5_v8?0ls32l8
+ ___block_descriptor_48_e36_B24?0Q8"NSObject<OS_xpc_object>"16l
+ ___block_descriptor_48_e5_v8?0l
+ ___block_descriptor_48_ea8_32r_e5_v8?0lr32l8
+ ___block_descriptor_48_ea8_32s40r_e22_v16?0"NSDictionary"8lr40l8s32l8
+ ___block_descriptor_48_ea8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_48_ea8_32s_e5_v8?0ls32l8
+ ___block_descriptor_52_e5_v8?0l
+ ___block_descriptor_52_ea8_32r_e5_v8?0lr32l8
+ ___block_descriptor_56_e5_v8?0l
+ ___block_descriptor_56_ea8_32r_e5_v8?0lr32l8
+ ___block_descriptor_56_ea8_32s40bs48w_e5_v8?0lw48l8s40l8s32l8
+ ___block_descriptor_56_ea8_32s40s48r_e18_v16?0"NSString"8ls32l8r48l8s40l8
+ ___block_descriptor_56_ea8_32s_e5_v8?0ls32l8
+ ___block_descriptor_57_ea8_32s_e32_Q24?0^{__RXLanguageObject=}8Q16ls32l8
+ ___block_descriptor_60_ea8_32r_e5_v8?0lr32l8
+ ___block_descriptor_64_e12_Q24?0^v8Q16l
+ ___block_literal_global.101
+ ___block_literal_global.103
+ ___block_literal_global.120
+ ___block_literal_global.28
+ ___block_literal_global.30
+ ___block_literal_global.66
+ ___block_literal_global.70
+ ___block_literal_global.73
+ ___swift_reflection_version
+ ___xpc_unwrap_uint64s_in_object_block_invoke
+ ___xpc_unwrap_uint64s_in_object_block_invoke_2
+ ___xpc_wrap_uint64s_in_object_block_invoke
+ ___xpc_wrap_uint64s_in_object_block_invoke_2
+ __objc_empty_cache
+ __swift_FORCE_LOAD_$_swiftCoreFoundation
+ __swift_FORCE_LOAD_$_swiftCoreFoundation_$_SpeechRecognitionCore
+ __swift_FORCE_LOAD_$_swiftDarwin
+ __swift_FORCE_LOAD_$_swiftDarwin_$_SpeechRecognitionCore
+ __swift_FORCE_LOAD_$_swiftDispatch
+ __swift_FORCE_LOAD_$_swiftDispatch_$_SpeechRecognitionCore
+ __swift_FORCE_LOAD_$_swiftFoundation
+ __swift_FORCE_LOAD_$_swiftFoundation_$_SpeechRecognitionCore
+ __swift_FORCE_LOAD_$_swiftObjectiveC
+ __swift_FORCE_LOAD_$_swiftObjectiveC_$_SpeechRecognitionCore
+ __swift_FORCE_LOAD_$_swiftXPC
+ __swift_FORCE_LOAD_$_swiftXPC_$_SpeechRecognitionCore
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_Builtin_float_$_SpeechRecognitionCore
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_SpeechRecognitionCore
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_SpeechRecognitionCore
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_SpeechRecognitionCore
+ __swift_FORCE_LOAD_$_swiftos
+ __swift_FORCE_LOAD_$_swiftos_$_SpeechRecognitionCore
+ __xpc_type_array
+ __xpc_type_data
+ __xpc_type_uint64
+ _dispatch_semaphore_create
+ _dispatch_semaphore_signal
+ _dispatch_semaphore_wait
+ _kRDKeySupportedLanguagesForVoiceControl
+ _objc_alloc
+ _objc_alloc_init
+ _objc_autoreleaseReturnValue
+ _objc_claimAutoreleasedReturnValue
+ _objc_copyWeak
+ _objc_destroyWeak
+ _objc_getProperty
+ _objc_initWeak
+ _objc_loadWeakRetained
+ _objc_msgSend
+ _objc_msgSend$SRDRecognizer:didRecognize:
+ _objc_msgSend$_setEndpoint:
+ _objc_msgSend$addLeadingContext:
+ _objc_msgSend$addOtherContext:
+ _objc_msgSend$arrayWithObjects:count:
+ _objc_msgSend$clientUpdateWithMessage:
+ _objc_msgSend$copy
+ _objc_msgSend$decodeBoolForKey:
+ _objc_msgSend$decodeDoubleForKey:
+ _objc_msgSend$decodeObjectOfClass:forKey:
+ _objc_msgSend$decodeObjectOfClasses:forKey:
+ _objc_msgSend$encodeBool:forKey:
+ _objc_msgSend$encodeDouble:forKey:
+ _objc_msgSend$encodeObject:forKey:
+ _objc_msgSend$exportedInterface
+ _objc_msgSend$helloWithObjectID:liveAudio:deviceUID:locale:flags:reply:
+ _objc_msgSend$initWithLanguageObject:transcriptionResult:
+ _objc_msgSend$initWithListenerEndpoint:
+ _objc_msgSend$initWithRXXPC:externalServiceClient:
+ _objc_msgSend$interfaceWithProtocol:
+ _objc_msgSend$invalidate
+ _objc_msgSend$invokeWithTarget:
+ _objc_msgSend$languageObject
+ _objc_msgSend$legacySendMessage:reply:
+ _objc_msgSend$logUpdates
+ _objc_msgSend$numberWithUnsignedInteger:
+ _objc_msgSend$phoneticNeighborsWithText:reply:
+ _objc_msgSend$pingWithObjectID:
+ _objc_msgSend$pong:
+ _objc_msgSend$releaseResult:
+ _objc_msgSend$remoteObjectProxy
+ _objc_msgSend$resetRecognition
+ _objc_msgSend$resume
+ _objc_msgSend$saveUserProfileToFile:
+ _objc_msgSend$selector
+ _objc_msgSend$sendVitamins
+ _objc_msgSend$setClasses:forSelector:argumentIndex:ofReply:
+ _objc_msgSend$setConfidence:
+ _objc_msgSend$setEnd:
+ _objc_msgSend$setExportedInterface:
+ _objc_msgSend$setExportedObject:
+ _objc_msgSend$setHasSpaceAfter:
+ _objc_msgSend$setHasSpaceBefore:
+ _objc_msgSend$setInterruptionHandler:
+ _objc_msgSend$setInvalidationHandler:
+ _objc_msgSend$setIpaPhoneSequence:
+ _objc_msgSend$setLanguageObject:
+ _objc_msgSend$setPhoneSequence:
+ _objc_msgSend$setRemoteObjectInterface:
+ _objc_msgSend$setResetRecognitionMode:
+ _objc_msgSend$setSecureFieldFocused:
+ _objc_msgSend$setSilenceStart:
+ _objc_msgSend$setStart:
+ _objc_msgSend$setTokenName:
+ _objc_msgSend$setTranscriptionResult:
+ _objc_msgSend$setWithArray:
+ _objc_msgSend$setWithObjects:
+ _objc_msgSend$synchronousRemoteObjectProxyWithErrorHandler:
+ _objc_msgSend$unsignedIntegerValue
+ _objc_msgSendSuper2
+ _objc_opt_class
+ _objc_opt_respondsToSelector
+ _objc_release
+ _objc_release_x1
+ _objc_release_x19
+ _objc_release_x20
+ _objc_release_x21
+ _objc_release_x22
+ _objc_release_x23
+ _objc_release_x24
+ _objc_release_x25
+ _objc_release_x26
+ _objc_release_x27
+ _objc_release_x28
+ _objc_release_x8
+ _objc_release_x9
+ _objc_retain
+ _objc_retainAutoreleaseReturnValue
+ _objc_retainBlock
+ _objc_retain_x1
+ _objc_retain_x19
+ _objc_retain_x2
+ _objc_retain_x20
+ _objc_retain_x21
+ _objc_retain_x22
+ _objc_retain_x23
+ _objc_retain_x24
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x8
+ _objc_setProperty_atomic
+ _objc_storeStrong
+ _objc_storeWeak
+ _objc_unsafeClaimAutoreleasedReturnValue
+ _symbolic $s21SpeechRecognitionCore11SRDProtocolP
+ _xpc_array_set_value
+ _xpc_copy
+ _xpc_data_create
+ _xpc_dictionary_apply
+ _xpc_dictionary_create_empty
+ _xpc_uint64_create
+ _xpc_uint64_get_value
+ _xpc_unwrap2_uint64
+ _xpc_unwrap_uint64s_in_object
+ _xpc_wrap2_uint64
+ _xpc_wrap_uint64s_in_object
- GCC_except_table20
- GCC_except_table43
- GCC_except_table49
- GCC_except_table68
- GCC_except_table70
- GCC_except_table71
- GCC_except_table74
- GCC_except_table82
- GCC_except_table83
- GCC_except_table84
- GCC_except_table85
- GCC_except_table90
- _RXRecognitionSystemAddTraining
- _RXRecognizerSetFeedbackText
- __Block_copy
- __Block_release
- __ZL13GetDaemonLMIDPvRy
- __ZN11RXBlockPropIU13block_pointerFvvEED2Ev
- __ZN11RXBlockPropIU13block_pointerFvvEEaSES1_
- __ZN11RXBlockPropIU13block_pointerFvyEED2Ev
- __ZN11RXBlockPropIU13block_pointerFvyEEaSES1_
- __ZN12RXRecognizer10RecognizedEP16RXLanguageObject
- __ZN12RXRecognizer10RecognizedEPv
- __ZN12RXRecognizer9SerializeEPvP19RXRecognitionSystem
- __ZN12RXVocabulary9SerializeEPvP19RXRecognitionSystem
- __ZN16RXLanguageObject20CreateFromSerializedEPvP12RXResultDesc
- __ZN16RXLanguageObject9SerializeEPvP19RXRecognitionSystem
- __ZN19RXRecognitionSystem11AddTrainingEPKvPK10__CFString
- __ZN19RXRecognitionSystem11BrokerEventEPv
- __ZN19RXRecognitionSystem8CallbackEPv
- __ZN19RXRecognitionSystem8CallbackEyPv
- __ZN5RXXPC11ClientEventEPv
- __ZN5RXXPC11ClientEventEPv.cold.1
- __ZN5RXXPC11ClientEventEPv.cold.2
- __ZN5RXXPC11ClientEventEPv.cold.3
- __ZN5RXXPC11ClientEventEPv.cold.4
- __ZN5RXXPC11SendMessageEPvb
- __ZN5RXXPC12SerializeURLEPvPK7__CFURL
- __ZN5RXXPC13CommitChangesEPvS0_
- __ZN5RXXPC16DownloadCallbackEPv
- __ZN5RXXPC16SerializeCFArrayEPvPKcPK9__CFArray
- __ZN5RXXPC17SerializeCFStringEPvPKcPK10__CFString
- __ZN5RXXPC24SendMessageWithReplySyncEPv
- __ZN5RXXPC30SendBrokerMessageWithReplySyncEPvb
- __ZN5RXXPC30SendBrokerMessageWithReplySyncEPvb.cold.1
- __ZN8RXObject9SerializeEPvP19RXRecognitionSystem
- __ZNKSt3__111__copy_implINS_17_ClassicAlgPolicyEEclB8ne190102INS_21__tree_const_iteratorIP8RXObjectPNS_11__tree_nodeIS6_PvEElEESB_NS_20back_insert_iteratorINS_6vectorIS6_NS_9allocatorIS6_EEEEEEEENS_4pairIT_T1_EESJ_T0_SK_
- __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_out_of_rangeB8ne190102Ev
- __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE4findB8ne190102ERKS5_m
- __ZNKSt3__16vectorIP16RXLanguageObjectNS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIP19RXRecognitionSystemNS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIP8RXObjectNS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIPKvNS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIyNS_9allocatorIyEEE20__throw_length_errorB8ne190102Ev
- __ZNSt12length_errorC1B8ne190102EPKc
- __ZNSt12out_of_rangeC1B8ne190102EPKc
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ne190102ENS_24__uninitialized_size_tagEmRKS4_
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ne190102ILi0EEEPKc
- __ZNSt3__116__set_differenceB8ne190102INS_17_ClassicAlgPolicyENS_6__lessIvvEERNS_21__tree_const_iteratorIP8RXObjectPNS_11__tree_nodeIS6_PvEElEESC_SC_SC_RNS_20back_insert_iteratorINS_6vectorIS6_NS_9allocatorIS6_EEEEEEEENS_4pairIu14__remove_cvrefIT1_Eu14__remove_cvrefIT5_EEEOSL_OT2_OT3_OT4_OSN_OT0_
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIP16RXLanguageObjectEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIP19RXRecognitionSystemEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIP8RXObjectEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIPKvEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIyEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__120__throw_length_errorB8ne190102EPKc
- __ZNSt3__120__throw_out_of_rangeB8ne190102EPKc
- __ZNSt3__120back_insert_iteratorINS_6vectorIP8RXObjectNS_9allocatorIS3_EEEEEaSB8ne190102ERKS3_
- __ZNSt3__127__tree_balance_after_insertB8ne190102IPNS_16__tree_node_baseIPvEEEEvT_S5_
- __ZNSt3__1plB8ne190102IcNS_11char_traitsIcEENS_9allocatorIcEEEENS_12basic_stringIT_T0_T1_EERKS9_SB_
- __ZSt28__throw_bad_array_new_lengthB8ne190102v
- __ZZN5RXXPC30SendBrokerMessageWithReplySyncEPvbE14sRXXBrokerConn
- __ZZN5RXXPC30SendBrokerMessageWithReplySyncEPvbE14sRXXBrokerInit
- __Znwm
- ____ZL13GetDaemonLMIDPvRy_block_invoke
- ____ZN12RXRecognizer10RecognizedEPv_block_invoke
- ____ZN12RXRecognizer9SerializeEPvP19RXRecognitionSystem_block_invoke
- ____ZN16RXLanguageObject20CreateFromSerializedEPvP12RXResultDesc_block_invoke
- ____ZN19RXRecognitionSystem10InitializeEPK10__CFLocalem_block_invoke
- ____ZN5RXXPC11ClientEventEPv_block_invoke
- ____ZN5RXXPC11ClientEventEPv_block_invoke.27
- ____ZN5RXXPC11ClientEventEPv_block_invoke.27.cold.1
- ____ZN5RXXPC11ClientEventEPv_block_invoke_2
- ____ZN5RXXPC11ClientEventEPv_block_invoke_3
- ____ZN5RXXPC11ClientEventEPv_block_invoke_4
- ____ZN5RXXPC11ClientEventEPv_block_invoke_5
- ____ZN5RXXPC11ClientEventEPv_block_invoke_6
- ____ZN5RXXPC11SendMessageEPvb_block_invoke
- ____ZN5RXXPC30SendBrokerMessageWithReplySyncEPvb_block_invoke
- ____ZN5RXXPC30SendBrokerMessageWithReplySyncEPvb_block_invoke_2
- ___assert_rtn
- ___block_descriptor_tmp
- ___block_descriptor_tmp.10
- ___block_descriptor_tmp.100
- ___block_descriptor_tmp.104
- ___block_descriptor_tmp.107
- ___block_descriptor_tmp.11
- ___block_descriptor_tmp.16
- ___block_descriptor_tmp.19
- ___block_descriptor_tmp.2
- ___block_descriptor_tmp.27
- ___block_descriptor_tmp.28
- ___block_descriptor_tmp.29
- ___block_descriptor_tmp.3
- ___block_descriptor_tmp.30
- ___block_descriptor_tmp.32
- ___block_descriptor_tmp.33
- ___block_descriptor_tmp.34
- ___block_descriptor_tmp.35
- ___block_descriptor_tmp.36
- ___block_descriptor_tmp.4
- ___block_descriptor_tmp.56
- ___block_descriptor_tmp.6
- ___block_descriptor_tmp.66
- ___block_descriptor_tmp.67
- ___block_descriptor_tmp.68
- ___block_descriptor_tmp.69
- ___block_descriptor_tmp.7
- ___block_descriptor_tmp.70
- ___block_descriptor_tmp.71
- ___block_descriptor_tmp.8
- ___block_literal_global.106
- ___block_literal_global.109
- ___block_literal_global.13
- ___block_literal_global.18
- ___block_literal_global.29
- ___block_literal_global.32
- ___block_literal_global.38
- __xpc_error_connection_invalid
- __xpc_error_termination_imminent
- __xpc_type_connection
- __xpc_type_error
- _kRXRecognitionSystemTrainingCategory_Contact
- _kRXRecognitionSystemTrainingCategory_Default
- _pthread_cond_broadcast
- _pthread_cond_init
- _pthread_cond_wait
- _reportBacktrace.cold.1
- _reportBacktrace.cold.2
- _xpc_array_get_string
- _xpc_connection_cancel
- _xpc_connection_get_pid
- _xpc_connection_send_message_with_reply
- _xpc_dictionary_create_connection
- _xpc_release
- _xpc_retain
- _xpc_type_get_name
CStrings:
+ "!"
+ "#16@0:8"
+ ".cxx_destruct"
+ "/Library/Caches/com.apple.xbs/Sources/SpeechRecognitionCore/Sources/RXLanguageObject.mm"
+ "/Library/Caches/com.apple.xbs/Sources/SpeechRecognitionCore/Sources/RXObject.mm"
+ "/Library/Caches/com.apple.xbs/Sources/SpeechRecognitionCore/Sources/RXRecognitionSystem.mm"
+ "/Library/Caches/com.apple.xbs/Sources/SpeechRecognitionCore/Sources/RXXPC.mm"
+ "@\"<SRDClientProtocol>\""
+ "@\"<SRDRecognizerDelegate>\""
+ "@\"NSArray\""
+ "@\"NSString\""
+ "@\"NSString\"16@0:8"
+ "@\"SRDTranscriptionResult\""
+ "@16@0:8"
+ "@24@0:8:16"
+ "@24@0:8@\"NSCoder\"16"
+ "@24@0:8@16"
+ "@32@0:8:16@24"
+ "@32@0:8^{RXXPC=BBBQ^{__CFString}^{__CFString}@@@Q^{__CFArray}Q{_opaque_pthread_mutex_t=q[56c]}}16@24"
+ "@32@0:8^{__RXLanguageObject=}16@24"
+ "@40@0:8:16@24@32"
+ "@40@0:8^{__CFLocale=}16Q24@32"
+ "@40@0:8^{__RXRecognitionSystem=}16@24Q32"
+ "@80@0:8@16d24d32d40d48B56B60@64@72"
+ "B"
+ "B16@0:8"
+ "B24@0:8#16"
+ "B24@0:8:16"
+ "B24@0:8@\"Protocol\"16"
+ "B24@0:8@16"
+ "B24@?0Q8@\"NSObject<OS_xpc_object>\"16"
+ "B24@?0r*8@\"NSObject<OS_xpc_object>\"16"
+ "NSCoding"
+ "NSObject"
+ "NSSecureCoding"
+ "PeerConnection: Hello %s -> %@\n"
+ "PeerConnection: Lost connection to SRD."
+ "PeerConnection: RXXPC EstablishConnection"
+ "PeerConnection: Received kRDServerRunning message, setting fServerIsRunning = true"
+ "PeerConnection: SRD Connection created [%lld] %@"
+ "PeerConnection: SRD Connection interrupted %@"
+ "PeerConnection: SRD Connection invalidated %@"
+ "PeerConnection: failed to convert message %s"
+ "PeerConnection: skipping handleConnectionLost because connection was not known"
+ "Q"
+ "Q16@0:8"
+ "RXXPCCSpeechRecognitionClientService"
+ "SRDBrokerProtocol"
+ "SRDClientProtocol"
+ "SRDConnection"
+ "SRDInternalClientProtocol"
+ "SRDLanguageObject"
+ "SRDRecognizer"
+ "SRDRecognizer:didRecognize:"
+ "SRDTranscriptionResult"
+ "SRDTranscriptionToken"
+ "T#,R"
+ "T@\"NSArray\",&,N,V_nBestResults"
+ "T@\"NSArray\",&,N,V_preITN_nBestResults"
+ "T@\"NSArray\",&,N,V_preITN_tokenSausage"
+ "T@\"NSArray\",&,N,V_tokenSausage"
+ "T@\"NSString\",&,N,V_firstBestResult"
+ "T@\"NSString\",&,N,V_ipaPhoneSequence"
+ "T@\"NSString\",&,N,V_phoneSequence"
+ "T@\"NSString\",&,N,V_preITN_firstBestResult"
+ "T@\"NSString\",&,N,V_tokenName"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",R,C"
+ "T@\"SRDTranscriptionResult\",&,V_transcriptionResult"
+ "TB,N,V_appendedAutoPunctuation"
+ "TB,N,V_hasSpaceAfter"
+ "TB,N,V_hasSpaceBefore"
+ "TB,N,V_isModifiedByAutoPunctuation"
+ "TB,N,V_isPartialResult"
+ "TB,N,V_prependedAutoPunctuation"
+ "TB,R"
+ "TQ,N,V_utteranceID"
+ "TQ,R"
+ "T^{__RXLanguageObject=},V_languageObject"
+ "Td,N,V_confidence"
+ "Td,N,V_end"
+ "Td,N,V_silenceStart"
+ "Td,N,V_start"
+ "Vv16@0:8"
+ "^{RXXPC=BBBQ^{__CFString}^{__CFString}@@@Q^{__CFArray}Q{_opaque_pthread_mutex_t=q[56c]}}"
+ "^{_NSZone=}16@0:8"
+ "^{__CFLocale=}"
+ "^{__RXLanguageObject=}"
+ "^{__RXLanguageObject=}16@0:8"
+ "^{__RXRecognitionSystem=}"
+ "^{__RXRecognitionSystem=}16@0:8"
+ "^{__RXRecognizer=}"
+ "^{__RXRecognizer=}16@0:8"
+ "_TtP21SpeechRecognitionCore11SRDProtocol_"
+ "_appendedAutoPunctuation"
+ "_confidence"
+ "_delegate"
+ "_end"
+ "_externalServiceClient"
+ "_firstBestResult"
+ "_flags"
+ "_hasSpaceAfter"
+ "_hasSpaceBefore"
+ "_ipaPhoneSequence"
+ "_isModifiedByAutoPunctuation"
+ "_isPartialResult"
+ "_languageObject"
+ "_locale"
+ "_nBestResults"
+ "_phoneSequence"
+ "_preITN_firstBestResult"
+ "_preITN_nBestResults"
+ "_preITN_tokenSausage"
+ "_prependedAutoPunctuation"
+ "_recognitionSystem"
+ "_recognizer"
+ "_setEndpoint:"
+ "_silenceStart"
+ "_start"
+ "_tokenName"
+ "_tokenSausage"
+ "_transcriptionResult"
+ "_utteranceID"
+ "_xpc"
+ "addLeadingContext:"
+ "addOtherContext:"
+ "appendedAutoPunctuation"
+ "arrayWithObjects:count:"
+ "autorelease"
+ "brokerIntro:reply:"
+ "class"
+ "clientUpdateWithMessage:"
+ "confidence"
+ "conformsToProtocol:"
+ "copy"
+ "crashServer"
+ "d"
+ "d16@0:8"
+ "dealloc"
+ "debugDescription"
+ "decodeBoolForKey:"
+ "decodeDoubleForKey:"
+ "decodeObjectOfClass:forKey:"
+ "decodeObjectOfClasses:forKey:"
+ "description"
+ "encodeBool:forKey:"
+ "encodeDouble:forKey:"
+ "encodeObject:forKey:"
+ "encodeWithCoder:"
+ "end"
+ "exportedInterface"
+ "failed to handle client event for %@\n"
+ "failed to handle recognition event for %@\n"
+ "firstBestResult"
+ "forwardInvocation:"
+ "hasSpaceAfter"
+ "hasSpaceBefore"
+ "hash"
+ "helloWithObjectID:liveAudio:deviceUID:locale:flags:reply:"
+ "init"
+ "initWithCoder:"
+ "initWithLanguageObject:transcriptionResult:"
+ "initWithListenerEndpoint:"
+ "initWithLocale:flags:delegate:"
+ "initWithRXXPC:externalServiceClient:"
+ "initWithRecognitionSystem:delegate:flags:"
+ "initWithTokenName:start:end:silenceStart:confidence:hasSpaceAfter:hasSpaceBefore:phoneSequence:ipaPhoneSequence:"
+ "interfaceWithProtocol:"
+ "invalidate"
+ "invokeWithTarget:"
+ "ipaPhoneSequence"
+ "isEqual:"
+ "isKindOfClass:"
+ "isMemberOfClass:"
+ "isModifiedByAutoPunctuation"
+ "isPartial"
+ "isPartialResult"
+ "isProxy"
+ "kRXGlobalProperty_SupportedAssetLanguages"
+ "languageObject"
+ "legacyClientEventWithMessage:"
+ "legacySendMessage:reply:"
+ "logUpdates"
+ "nBestResults"
+ "numberWithUnsignedInteger:"
+ "performSelector:"
+ "performSelector:withObject:"
+ "performSelector:withObject:withObject:"
+ "phoneSequence"
+ "phoneticNeighborsWithText:reply:"
+ "pingWithObjectID:"
+ "pong:"
+ "preITN_firstBestResult"
+ "preITN_nBestResults"
+ "preITN_tokenSausage"
+ "prependedAutoPunctuation"
+ "recognitionSystem"
+ "recognizedEventWithLegacyMessage:result:"
+ "recognizer"
+ "release"
+ "releaseResult:"
+ "remoteObjectProxy"
+ "resetRecognition"
+ "respondsToSelector:"
+ "resume"
+ "retain"
+ "retainCount"
+ "saveUserProfileToFile:"
+ "selector"
+ "self"
+ "sendVitamins"
+ "setAppendedAutoPunctuation:"
+ "setClasses:forSelector:argumentIndex:ofReply:"
+ "setConfidence:"
+ "setEnd:"
+ "setExportedInterface:"
+ "setExportedObject:"
+ "setFirstBestResult:"
+ "setHasSpaceAfter:"
+ "setHasSpaceBefore:"
+ "setInterruptionHandler:"
+ "setInvalidationHandler:"
+ "setIpaPhoneSequence:"
+ "setIsModifiedByAutoPunctuation:"
+ "setIsPartialResult:"
+ "setLanguageObject:"
+ "setNBestResults:"
+ "setPhoneSequence:"
+ "setPreITN_firstBestResult:"
+ "setPreITN_nBestResults:"
+ "setPreITN_tokenSausage:"
+ "setPrependedAutoPunctuation:"
+ "setRemoteObjectInterface:"
+ "setResetRecognitionMode:"
+ "setSecureFieldFocused:"
+ "setSilenceStart:"
+ "setStart:"
+ "setTokenName:"
+ "setTokenSausage:"
+ "setTranscriptionResult:"
+ "setUtteranceID:"
+ "setWithArray:"
+ "setWithObjects:"
+ "silenceStart"
+ "start"
+ "superclass"
+ "supportedLanguages"
+ "supportsSecureCoding"
+ "synchronousRemoteObjectProxyWithErrorHandler:"
+ "tokenName"
+ "tokenSausage"
+ "transcriptionResult"
+ "unsignedIntegerValue"
+ "utteranceID"
+ "v16@0:8"
+ "v16@?0@\"NSArray\"8"
+ "v16@?0@\"NSDictionary\"8"
+ "v16@?0@\"NSError\"8"
+ "v16@?0@\"NSObject<OS_xpc_object>\"8"
+ "v16@?0@\"NSString\"8"
+ "v20@0:8B16"
+ "v20@?0i8^{RXXPC=BBBQ^{__CFString}^{__CFString}@@@Q^{__CFArray}Q{_opaque_pthread_mutex_t=q[56c]}}12"
+ "v24@0:8@\"NSArray\"16"
+ "v24@0:8@\"NSCoder\"16"
+ "v24@0:8@\"NSDictionary\"16"
+ "v24@0:8@\"NSString\"16"
+ "v24@0:8@16"
+ "v24@0:8Q16"
+ "v24@0:8^{__RXLanguageObject=}16"
+ "v24@0:8d16"
+ "v24@0:8q16"
+ "v32@0:8@\"NSDictionary\"16@\"SRDTranscriptionResult\"24"
+ "v32@0:8@\"NSDictionary\"16@?<v@?@\"NSDictionary\">24"
+ "v32@0:8@\"NSString\"16@?<v@?@\"NSArray\">24"
+ "v32@0:8@\"NSString\"16@?<v@?@\"NSXPCListenerEndpoint\">24"
+ "v32@0:8@16@24"
+ "v32@0:8@16@?24"
+ "v60@0:8q16B24@\"NSString\"28@\"NSString\"36Q44@?<v@?@\"NSString\">52"
+ "v60@0:8q16B24@28@36Q44@?52"
+ "zone"
- "%s (connection:  pid = %d)"
- "%s (connection: NULL)"
- "%s (connection: Unexpected type %s"
- "%s (connection: Unexpected type UNKNOWN"
- "/Library/Caches/com.apple.xbs/Sources/SpeechRecognitionCore/Sources/RXLanguageObject.cpp"
- "/Library/Caches/com.apple.xbs/Sources/SpeechRecognitionCore/Sources/RXObject.cpp"
- "/Library/Caches/com.apple.xbs/Sources/SpeechRecognitionCore/Sources/RXRecognitionSystem.cpp"
- "/Library/Caches/com.apple.xbs/Sources/SpeechRecognitionCore/Sources/RXXPC.cpp"
- "B24@?0Q8^v16"
- "ClientEvent"
- "Contact"
- "Could not initialize the server condition variable"
- "Could not initialize the server mutex"
- "Hello %s -> %s\n"
- "Inline"
- "RXRecognizerSetFeedbackText is only valid for macOS"
- "RXXPC EstablishConnection"
- "RXXPC.cpp"
- "audio_donation_supported"
- "broker connection to daemon failed"
- "broker connection to daemon succedded"
- "client received XPC_ERROR_CONNECTION_INTERRUPTED"
- "client received XPC_ERROR_CONNECTION_INVALID"
- "client received XPC_ERROR_TERMINATION_IMMINENT"
- "de"
- "en"
- "es"
- "fr"
- "type == XPC_TYPE_DICTIONARY"
- "use_independent_vad"
- "use_keyword_spotter"
- "use_speech_spi"
- "use_voiceactions_visionkws"
- "v16@?0^v8"
- "v20@?0i8^{RXXPC=BBBBQ^{__CFString}^{__CFString}^{_xpc_connection_s}Q^{__CFArray}Q{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_cond_t=q[40c]}}12"

```
