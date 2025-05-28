## SiriMessageTypes

> `/System/Library/PrivateFrameworks/SiriMessageTypes.framework/SiriMessageTypes`

```diff

-3302.2.1.0.0
-  __TEXT.__text: 0xb6f58
-  __TEXT.__auth_stubs: 0xf00
-  __TEXT.__objc_methlist: 0xf64
-  __TEXT.__const: 0xa120
-  __TEXT.__swift5_typeref: 0x1d75
-  __TEXT.__cstring: 0x4b3c
-  __TEXT.__swift5_reflstr: 0x2248
+3304.24.1.0.0
+  __TEXT.__text: 0xbe0ec
+  __TEXT.__auth_stubs: 0xf60
+  __TEXT.__objc_methlist: 0x1144
+  __TEXT.__const: 0xaa80
+  __TEXT.__cstring: 0x532b
+  __TEXT.__swift5_typeref: 0x1e4d
+  __TEXT.__swift5_reflstr: 0x2368
   __TEXT.__swift5_assocty: 0x2e8
-  __TEXT.__constg_swiftt: 0x3f20
-  __TEXT.__swift5_fieldmd: 0x3828
-  __TEXT.__swift5_builtin: 0x78
-  __TEXT.__swift5_proto: 0x744
-  __TEXT.__swift5_types: 0x3fc
+  __TEXT.__constg_swiftt: 0x41f8
+  __TEXT.__swift5_fieldmd: 0x3a30
+  __TEXT.__swift5_builtin: 0x8c
+  __TEXT.__swift5_proto: 0x770
+  __TEXT.__swift5_types: 0x428
   __TEXT.__swift5_protos: 0x24
   __TEXT.__swift5_mpenum: 0x18
   __TEXT.__swift5_capture: 0x30
-  __TEXT.__unwind_info: 0x56f4
-  __TEXT.__eh_frame: 0x4090
-  __TEXT.__objc_classname: 0x210
-  __TEXT.__objc_methname: 0x1048
-  __TEXT.__objc_methtype: 0x617
-  __TEXT.__objc_stubs: 0xc60
+  __TEXT.__unwind_info: 0x5e28
+  __TEXT.__eh_frame: 0x43f8
+  __TEXT.__objc_classname: 0x24b
+  __TEXT.__objc_methname: 0x1371
+  __TEXT.__objc_methtype: 0x685
+  __TEXT.__objc_stubs: 0xde0
   __DATA_CONST.__got: 0x2c8
-  __DATA_CONST.__const: 0x8c0
-  __DATA_CONST.__objc_classlist: 0x338
+  __DATA_CONST.__const: 0x988
+  __DATA_CONST.__objc_classlist: 0x370
   __DATA_CONST.__objc_catlist: 0x0
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x4a68
-  __DATA_CONST.__objc_selrefs: 0x430
+  __DATA_CONST.__objc_const: 0x4f58
+  __DATA_CONST.__objc_selrefs: 0x4b0
+  __DATA_CONST.__objc_protorefs: 0x10
+  __DATA_CONST.__objc_classrefs: 0xe0
+  __DATA_CONST.__objc_superrefs: 0x60
   __DATA_CONST.__objc_arraydata: 0x60
-  __AUTH_CONST.__const: 0x7640
-  __AUTH_CONST.__auth_ptr: 0x218
-  __AUTH_CONST.__objc_const: 0x480
-  __AUTH_CONST.__cfstring: 0x840
+  __AUTH_CONST.__const: 0x7988
+  __AUTH_CONST.__auth_ptr: 0x230
+  __AUTH_CONST.__objc_const: 0x558
+  __AUTH_CONST.__cfstring: 0x920
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH_CONST.__auth_got: 0x788
-  __AUTH.__objc_data: 0x1c60
-  __AUTH.__data: 0x2038
-  __DATA.__objc_protorefs: 0x10
-  __DATA.__objc_classrefs: 0xd0
-  __DATA.__objc_superrefs: 0x50
-  __DATA.__objc_ivar: 0x110
-  __DATA.__data: 0x2810
-  __DATA.__common: 0x118
-  __DATA.__bss: 0xbb20
-  __DATA_DIRTY.__objc_data: 0x61d8
-  __DATA_DIRTY.__data: 0x1b60
-  __DATA_DIRTY.__common: 0x380
+  __AUTH_CONST.__auth_got: 0x7b8
+  __AUTH.__objc_data: 0x2278
+  __AUTH.__data: 0x2298
+  __DATA.__objc_ivar: 0x138
+  __DATA.__data: 0x2960
+  __DATA.__common: 0x140
+  __DATA.__bss: 0xc020
+  __DATA_DIRTY.__objc_data: 0x6378
+  __DATA_DIRTY.__data: 0x1b98
+  __DATA_DIRTY.__common: 0x390
   __DATA_DIRTY.__bss: 0x2b00
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreLocation.framework/CoreLocation

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 8212
-  Symbols:   3530
-  CStrings:  802
+  Functions: 8506
+  Symbols:   3687
+  CStrings:  878
 
Symbols:
+ +[SMTMultiUserTRPCandidate supportsSecureCoding]
+ -[SMTMultiUserTRPCandidate .cxx_destruct]
+ -[SMTMultiUserTRPCandidate _descriptionWithIndent:]
+ -[SMTMultiUserTRPCandidate copyWithZone:]
+ -[SMTMultiUserTRPCandidate description]
+ -[SMTMultiUserTRPCandidate encodeWithCoder:]
+ -[SMTMultiUserTRPCandidate hash]
+ -[SMTMultiUserTRPCandidate initWithBuilder:]
+ -[SMTMultiUserTRPCandidate initWithCoder:]
+ -[SMTMultiUserTRPCandidate isEqual:]
+ -[SMTMultiUserTRPCandidate multiUserTrpCandidateId]
+ -[SMTMultiUserTRPCandidate requestId]
+ -[SMTMultiUserTRPCandidate trpCandidateList]
+ -[SMTMultiUserTRPCandidateBuilder .cxx_destruct]
+ -[SMTMultiUserTRPCandidateBuilder initBuilderWithTrpCandidateId:requestId:trpCandidateList:]
+ -[SMTMultiUserTRPCandidateBuilder initBuilderWithTrpCandidateId:trpCandidateList:]
+ -[SMTMultiUserTRPCandidateBuilder init]
+ -[SMTMultiUserTRPCandidateBuilder multiUserTrpCandidateId]
+ -[SMTMultiUserTRPCandidateBuilder requestId]
+ -[SMTMultiUserTRPCandidateBuilder setMultiUserTrpCandidateId:]
+ -[SMTMultiUserTRPCandidateBuilder setRequestId:]
+ -[SMTMultiUserTRPCandidateBuilder setTrpCandidateList:]
+ -[SMTMultiUserTRPCandidateBuilder trpCandidateList]
+ -[SMTSiriIntendedInfo initWithOdldScore:aftmScore:spkrIdScore:lrnnScore:checkerScore:invocationType:lrnnThreshold:lrnnScale:lrnnOffset:gazeSignal:]
+ -[SMTSiriIntendedInfo isGazeSignalPresent]
+ -[SMTTRPCandidate initWithTrpCandidateId:requestId:tcuList:userId:]
+ -[SMTTRPCandidate userId]
+ -[_SMTSiriIntendedInfoMutation getGazeSignal]
+ -[_SMTSiriIntendedInfoMutation setGazeSignal:]
+ -[_SMTTRPCandidateMutation getUserId]
+ -[_SMTTRPCandidateMutation setUserId:]
+ _OBJC_CLASS_$_SMTMultiUserTRPCandidate
+ _OBJC_CLASS_$_SMTMultiUserTRPCandidateBuilder
+ _OBJC_CLASS_$__TtC16SiriMessageTypes25UserIdentificationMessage
+ _OBJC_CLASS_$__TtC16SiriMessageTypes30MultiUserNLTRPCandidateMessage
+ _OBJC_CLASS_$__TtC16SiriMessageTypes34MultiUserSpeechStopDetectedMessage
+ _OBJC_CLASS_$__TtC16SiriMessageTypes35MultiUserTRPCandidateRequestMessage
+ _OBJC_CLASS_$__TtC16SiriMessageTypes53MultiUserStoppedListeningForSpeechContinuationMessage
+ _OBJC_IVAR_$_SMTMultiUserTRPCandidate._multiUserTrpCandidateId
+ _OBJC_IVAR_$_SMTMultiUserTRPCandidate._requestId
+ _OBJC_IVAR_$_SMTMultiUserTRPCandidate._trpCandidateList
+ _OBJC_IVAR_$_SMTMultiUserTRPCandidateBuilder._multiUserTrpCandidateId
+ _OBJC_IVAR_$_SMTMultiUserTRPCandidateBuilder._requestId
+ _OBJC_IVAR_$_SMTMultiUserTRPCandidateBuilder._trpCandidateList
+ _OBJC_IVAR_$_SMTSiriIntendedInfo._isGazeSignalPresent
+ _OBJC_IVAR_$_SMTTRPCandidate._userId
+ _OBJC_IVAR_$__SMTSiriIntendedInfoMutation._isGazeSignalPresent
+ _OBJC_IVAR_$__SMTTRPCandidateMutation._userId
+ _OBJC_METACLASS_$_SMTMultiUserTRPCandidate
+ _OBJC_METACLASS_$_SMTMultiUserTRPCandidateBuilder
+ _OBJC_METACLASS_$__TtC16SiriMessageTypes25UserIdentificationMessage
+ _OBJC_METACLASS_$__TtC16SiriMessageTypes30MultiUserNLTRPCandidateMessage
+ _OBJC_METACLASS_$__TtC16SiriMessageTypes34MultiUserSpeechStopDetectedMessage
+ _OBJC_METACLASS_$__TtC16SiriMessageTypes35MultiUserTRPCandidateRequestMessage
+ _OBJC_METACLASS_$__TtC16SiriMessageTypes53MultiUserStoppedListeningForSpeechContinuationMessage
+ _SMTMultiUserTRPCandidateKey
+ __DATA__TtC16SiriMessageTypes25UserIdentificationMessage
+ __DATA__TtC16SiriMessageTypes30MultiUserNLTRPCandidateMessage
+ __DATA__TtC16SiriMessageTypes34MultiUserSpeechStopDetectedMessage
+ __DATA__TtC16SiriMessageTypes35MultiUserTRPCandidateRequestMessage
+ __DATA__TtC16SiriMessageTypes53MultiUserStoppedListeningForSpeechContinuationMessage
+ __IVARS__TtC16SiriMessageTypes20CancelRequestMessage
+ __IVARS__TtC16SiriMessageTypes25UserIdentificationMessage
+ __IVARS__TtC16SiriMessageTypes35MultiUserTRPCandidateRequestMessage
+ __METACLASS_DATA__TtC16SiriMessageTypes25UserIdentificationMessage
+ __METACLASS_DATA__TtC16SiriMessageTypes30MultiUserNLTRPCandidateMessage
+ __METACLASS_DATA__TtC16SiriMessageTypes34MultiUserSpeechStopDetectedMessage
+ __METACLASS_DATA__TtC16SiriMessageTypes35MultiUserTRPCandidateRequestMessage
+ __METACLASS_DATA__TtC16SiriMessageTypes53MultiUserStoppedListeningForSpeechContinuationMessage
+ __OBJC_$_CLASS_METHODS_SMTMultiUserTRPCandidate
+ __OBJC_$_CLASS_PROP_LIST_SMTMultiUserTRPCandidate
+ __OBJC_$_INSTANCE_METHODS_SMTMultiUserTRPCandidate
+ __OBJC_$_INSTANCE_METHODS_SMTMultiUserTRPCandidateBuilder
+ __OBJC_$_INSTANCE_METHODS__TtC16SiriMessageTypes20CancelRequestMessage
+ __OBJC_$_INSTANCE_METHODS__TtC16SiriMessageTypes25UserIdentificationMessage
+ __OBJC_$_INSTANCE_METHODS__TtC16SiriMessageTypes35MultiUserTRPCandidateRequestMessage
+ __OBJC_$_INSTANCE_VARIABLES_SMTMultiUserTRPCandidate
+ __OBJC_$_INSTANCE_VARIABLES_SMTMultiUserTRPCandidateBuilder
+ __OBJC_$_PROP_LIST_SMTMultiUserTRPCandidate
+ __OBJC_$_PROP_LIST_SMTMultiUserTRPCandidateBuilder
+ __OBJC_CLASS_PROTOCOLS_$_SMTMultiUserTRPCandidate
+ __OBJC_CLASS_RO_$_SMTMultiUserTRPCandidate
+ __OBJC_CLASS_RO_$_SMTMultiUserTRPCandidateBuilder
+ __OBJC_METACLASS_RO_$_SMTMultiUserTRPCandidate
+ __OBJC_METACLASS_RO_$_SMTMultiUserTRPCandidateBuilder
+ __PROPERTIES__TtC16SiriMessageTypes20CancelRequestMessage
+ __PROPERTIES__TtC16SiriMessageTypes35MultiUserTRPCandidateRequestMessage
+ ___147-[SMTSiriIntendedInfo initWithOdldScore:aftmScore:spkrIdScore:lrnnScore:checkerScore:invocationType:lrnnThreshold:lrnnScale:lrnnOffset:gazeSignal:]_block_invoke
+ ___42-[SMTMultiUserTRPCandidate initWithCoder:]_block_invoke
+ ___67-[SMTTRPCandidate initWithTrpCandidateId:requestId:tcuList:userId:]_block_invoke
+ ___block_descriptor_56_e8_32s40s48s_e41_v16?0"SMTMultiUserTRPCandidateBuilder"8ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56s_e35_v16?0"<SMTTRPCandidateMutating>"8ls32l8s40l8s48l8s56l8
+ ___block_descriptor_73_e8_32s_e39_v16?0"<SMTSiriIntendedInfoMutating>"8ls32l8
+ ___block_literal_global.572
+ __unnamed_array_storage.576
+ _associated conformance 16SiriMessageTypes013CancelRequestB0C10CodingKeys33_332DFE2384C5DF3BBF7958E491FCAE95LLOSHAASQ
+ _associated conformance 16SiriMessageTypes013CancelRequestB0C10CodingKeys33_332DFE2384C5DF3BBF7958E491FCAE95LLOs0F3KeyAAs23CustomStringConvertible
+ _associated conformance 16SiriMessageTypes013CancelRequestB0C10CodingKeys33_332DFE2384C5DF3BBF7958E491FCAE95LLOs0F3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 16SiriMessageTypes018UserIdentificationB0C10CodingKeys33_4B3BD631B10618568A712932C7A46E2FLLOSHAASQ
+ _associated conformance 16SiriMessageTypes018UserIdentificationB0C10CodingKeys33_4B3BD631B10618568A712932C7A46E2FLLOs0F3KeyAAs23CustomStringConvertible
+ _associated conformance 16SiriMessageTypes018UserIdentificationB0C10CodingKeys33_4B3BD631B10618568A712932C7A46E2FLLOs0F3KeyAAs28CustomDebugStringConvertible
+ _objc_msgSend$boolValue
+ _objc_msgSend$getGazeSignal
+ _objc_msgSend$getUserId
+ _objc_msgSend$initWithOdldScore:aftmScore:spkrIdScore:lrnnScore:checkerScore:invocationType:lrnnThreshold:lrnnScale:lrnnOffset:gazeSignal:
+ _objc_msgSend$initWithTrpCandidateId:requestId:tcuList:userId:
+ _objc_msgSend$isGazeSignalPresent
+ _objc_msgSend$multiUserTrpCandidateId
+ _objc_msgSend$numberWithBool:
+ _objc_msgSend$setGazeSignal:
+ _objc_msgSend$setMultiUserTrpCandidateId:
+ _objc_msgSend$setTrpCandidateList:
+ _objc_msgSend$setUserId:
+ _objc_msgSend$trpCandidateList
+ _objc_msgSend$userId
+ _objc_setProperty_nonatomic_copy
+ _swift_release_n
+ _symbolic SDySSSiGSg
+ _symbolic SDySS_____G 16SiriMessageTypes019TRPCandidateRequestB0C
+ _symbolic SDySS_____GSg 16SiriMessageTypes019TRPCandidateRequestB0C
+ _symbolic _____ 16SiriMessageTypes013CancelRequestB0C10CodingKeys33_332DFE2384C5DF3BBF7958E491FCAE95LLO
+ _symbolic _____ 16SiriMessageTypes013CancelRequestB0C7BuilderV
+ _symbolic _____ 16SiriMessageTypes018UserIdentificationB0C
+ _symbolic _____ 16SiriMessageTypes018UserIdentificationB0C10CodingKeys33_4B3BD631B10618568A712932C7A46E2FLLO
+ _symbolic _____ 16SiriMessageTypes018UserIdentificationB0C7BuilderV
+ _symbolic _____ 16SiriMessageTypes023MultiUserNLTRPCandidateB0C
+ _symbolic _____ 16SiriMessageTypes027MultiUserSpeechStopDetectedB0C
+ _symbolic _____ 16SiriMessageTypes028MultiUserTRPCandidateRequestB0C
+ _symbolic _____ 16SiriMessageTypes028MultiUserTRPCandidateRequestB0C7BuilderV
+ _symbolic _____ 16SiriMessageTypes046MultiUserStoppedListeningForSpeechContinuationB0C
+ _symbolic _____ So27AFRequestCancellationReasonV
+ _symbolic _____Sg So27AFRequestCancellationReasonV
+ _symbolic _____y_____G s22KeyedDecodingContainerV 16SiriMessageTypes013CancelRequestE0C10CodingKeys33_332DFE2384C5DF3BBF7958E491FCAE95LLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 16SiriMessageTypes018UserIdentificationE0C10CodingKeys33_4B3BD631B10618568A712932C7A46E2FLLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 16SiriMessageTypes013CancelRequestE0C10CodingKeys33_332DFE2384C5DF3BBF7958E491FCAE95LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 16SiriMessageTypes018UserIdentificationE0C10CodingKeys33_4B3BD631B10618568A712932C7A46E2FLLO
- _OUTLINED_FUNCTION_40
- _OUTLINED_FUNCTION_41
- _OUTLINED_FUNCTION_42
- _OUTLINED_FUNCTION_43
- _OUTLINED_FUNCTION_44
- _OUTLINED_FUNCTION_45
- ___block_literal_global.456
- __unnamed_array_storage.460
- _objc_msgSend$initWithOdldScore:aftmScore:spkrIdScore:lrnnScore:checkerScore:invocationType:lrnnThreshold:lrnnScale:lrnnOffset:
- _objc_msgSend$initWithTrpCandidateId:requestId:tcuList:
- _objc_release_x11
CStrings:
+ "\x01Q"
+ "\x05"
+ "%@ {multiUserTrpCandidateId = %@, requestId = %@, trpCandidateList = %@}"
+ "%@ {odldScore = %f, aftmScore = %f, spkrIdScore = %f, lrnnScore = %f, checkerScore = %f, invocationType = %@, lrnnThreshold = %f, lrnnScale = %f, lrnnOffset = %f, gazeSignalPresent = %u}"
+ "%@ {trpCandidateId = %@, requestId = %@, tcuList = %@, userId = %@}"
+ ", <CancellationReason: "
+ ", <userIdToTRPCandidateDict keys: "
+ "@48@0:8@16@24@32@40"
+ "@60@0:8f16f20f24f28f32@36f44f48f52B56"
+ "B"
+ "Can't construct Array with count < 0"
+ "Division by zero"
+ "Division results in an overflow"
+ "Error: Attempted to serialize an instance of MultiUserTRPCandidateRequestMessage, which is not currently codable. Conversation Session State will be empty."
+ "Insufficient space allocated to copy string contents"
+ "Missing reason for CancelRequestMessage: assuming unspecified. This will become an error in the future."
+ "SMTMultiUserTRPCandidate"
+ "SMTMultiUserTRPCandidateBuilder"
+ "SMTSiriIntendedInfo::isGazeSignalPresent"
+ "SMTTRPCandidate::userId"
+ "SiriMessageTypes.MultiUserTRPCandidateRequestMessage"
+ "SiriMessageTypes.UserIdentificationMessage"
+ "Swift/Array.swift"
+ "Swift/ContiguousArrayBuffer.swift"
+ "Swift/IntegerTypes.swift"
+ "Swift/StringTesting.swift"
+ "Swift/StringUTF8View.swift"
+ "Swift/UnsafeBufferPointer.swift"
+ "Swift/UnsafePointer.swift"
+ "Swift/UnsafeRawPointer.swift"
+ "T@\"NSArray\",C,N,V_trpCandidateList"
+ "T@\"NSArray\",R,C,N,V_trpCandidateList"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",C,N,V_multiUserTrpCandidateId"
+ "T@\"NSString\",C,N,V_requestId"
+ "T@\"NSString\",R,C,N,V_multiUserTrpCandidateId"
+ "T@\"NSString\",R,C,N,V_userId"
+ "TB,R,N,V_isGazeSignalPresent"
+ "Unexpectedly found nil while unwrapping an Optional value"
+ "UnsafeMutableBufferPointer with negative count"
+ "UnsafeMutablePointer.initialize overlapping range"
+ "UnsafeMutablePointer.initialize with negative count"
+ "UnsafeMutablePointer.moveInitialize with negative count"
+ "UnsafeMutableRawPointer.initializeMemory overlapping range"
+ "UnsafeMutableRawPointer.initializeMemory with negative count"
+ "_TtC16SiriMessageTypes25UserIdentificationMessage"
+ "_TtC16SiriMessageTypes30MultiUserNLTRPCandidateMessage"
+ "_TtC16SiriMessageTypes34MultiUserSpeechStopDetectedMessage"
+ "_TtC16SiriMessageTypes35MultiUserTRPCandidateRequestMessage"
+ "_TtC16SiriMessageTypes53MultiUserStoppedListeningForSpeechContinuationMessage"
+ "_isGazeSignalPresent"
+ "_multiUserTrpCandidateId"
+ "_trpCandidateList"
+ "_userId"
+ "boolValue"
+ "getGazeSignal"
+ "getUserId"
+ "initBuilderWithTrpCandidateId:requestId:trpCandidateList:"
+ "initBuilderWithTrpCandidateId:trpCandidateList:"
+ "initWithOdldScore:aftmScore:spkrIdScore:lrnnScore:checkerScore:invocationType:lrnnThreshold:lrnnScale:lrnnOffset:gazeSignal:"
+ "initWithTrpCandidateId:requestId:tcuList:userId:"
+ "invalid Collection: less than 'count' elements in collection"
+ "isGazeSignalPresent"
+ "multiUserTrpCandidateId"
+ "numberWithBool:"
+ "setGazeSignal:"
+ "setMultiUserTrpCandidateId:"
+ "setTrpCandidateList:"
+ "setUserId:"
+ "trpCandidateList"
+ "userClassification"
+ "userIdScores"
+ "userIdToTRPCandidateDict"
+ "v16@?0@\"SMTMultiUserTRPCandidateBuilder\"8"
+ "{_mutationFlags=\"isDirty\"b1\"hasOdldScore\"b1\"hasAftmScore\"b1\"hasSpkrIdScore\"b1\"hasLrnnScore\"b1\"hasCheckerScore\"b1\"hasInvocationType\"b1\"hasLrnnThreshold\"b1\"hasLrnnScale\"b1\"hasLrnnOffset\"b1\"hasIsGazeSignalPresent\"b1}"
+ "{_mutationFlags=\"isDirty\"b1\"hasTrpCandidateId\"b1\"hasRequestId\"b1\"hasTcuList\"b1\"hasUserId\"b1}"
- "\x01A"
- "%@ {odldScore = %f, aftmScore = %f, spkrIdScore = %f, lrnnScore = %f, checkerScore = %f, invocationType = %@, lrnnThreshold = %f, lrnnScale = %f, lrnnOffset = %f}"
- "%@ {trpCandidateId = %@, requestId = %@, tcuList = %@}"
- "A"
- "{_mutationFlags=\"isDirty\"b1\"hasOdldScore\"b1\"hasAftmScore\"b1\"hasSpkrIdScore\"b1\"hasLrnnScore\"b1\"hasCheckerScore\"b1\"hasInvocationType\"b1\"hasLrnnThreshold\"b1\"hasLrnnScale\"b1\"hasLrnnOffset\"b1}"
- "{_mutationFlags=\"isDirty\"b1\"hasTrpCandidateId\"b1\"hasRequestId\"b1\"hasTcuList\"b1}"

```
