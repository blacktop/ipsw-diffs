## CoreDiagnostics

> `/System/Library/PrivateFrameworks/CoreDiagnostics.framework/Versions/A/CoreDiagnostics`

```diff

-6.60.2.0.0
-  __TEXT.__text: 0x13180
-  __TEXT.__auth_stubs: 0xc80
-  __TEXT.__objc_methlist: 0x1e8
-  __TEXT.__const: 0x9f0
-  __TEXT.__cstring: 0x937
-  __TEXT.__swift5_typeref: 0x424
-  __TEXT.__constg_swiftt: 0x2f8
-  __TEXT.__swift5_reflstr: 0x15a
-  __TEXT.__swift5_fieldmd: 0x294
+14.100.5.0.0
+  __TEXT.__text: 0x23474
+  __TEXT.__auth_stubs: 0x1010
+  __TEXT.__objc_methlist: 0x1d4
+  __TEXT.__const: 0x1700
+  __TEXT.__cstring: 0x665
+  __TEXT.__swift5_typeref: 0x7fc
+  __TEXT.__swift5_capture: 0x1cc
+  __TEXT.__oslogstring: 0x7cd
+  __TEXT.__constg_swiftt: 0x704
+  __TEXT.__swift5_reflstr: 0x3b2
+  __TEXT.__swift5_fieldmd: 0x660
   __TEXT.__swift5_builtin: 0x28
-  __TEXT.__swift5_assocty: 0x60
-  __TEXT.__swift5_capture: 0xf0
-  __TEXT.__oslogstring: 0x4ce
-  __TEXT.__swift5_proto: 0x90
-  __TEXT.__swift5_types: 0x3c
-  __TEXT.__swift5_protos: 0x8
-  __TEXT.__unwind_info: 0x4c0
-  __TEXT.__eh_frame: 0x4b8
-  __TEXT.__objc_classname: 0x43
-  __TEXT.__objc_methname: 0x31d
-  __TEXT.__objc_methtype: 0xcb
-  __TEXT.__objc_stubs: 0x120
-  __DATA_CONST.__got: 0x170
-  __DATA_CONST.__const: 0x88
+  __TEXT.__swift5_assocty: 0xd0
+  __TEXT.__swift5_proto: 0x16c
+  __TEXT.__swift5_types: 0x8c
+  __TEXT.__swift5_protos: 0xc
+  __TEXT.__unwind_info: 0x840
+  __TEXT.__eh_frame: 0x980
+  __TEXT.__objc_classname: 0x35
+  __TEXT.__objc_methname: 0x384
+  __TEXT.__objc_methtype: 0xa1
+  __TEXT.__objc_stubs: 0x100
+  __DATA_CONST.__got: 0x1c8
+  __DATA_CONST.__const: 0xa0
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x100
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x18
-  __AUTH_CONST.__auth_got: 0x648
-  __AUTH_CONST.__const: 0x808
-  __AUTH_CONST.__objc_const: 0x570
-  __AUTH.__objc_data: 0x510
-  __AUTH.__data: 0xc8
-  __DATA.__objc_ivar: 0xc
-  __DATA.__data: 0x2d0
-  __DATA.__bss: 0x1100
-  __DATA.__common: 0x28
+  __DATA_CONST.__objc_superrefs: 0x10
+  __AUTH_CONST.__auth_got: 0x810
+  __AUTH_CONST.__const: 0x12f8
+  __AUTH_CONST.__objc_const: 0x560
+  __AUTH.__objc_data: 0x560
+  __AUTH.__data: 0x218
+  __DATA.__objc_ivar: 0x8
+  __DATA.__data: 0x8c0
+  __DATA.__bss: 0x2c80
+  __DATA.__common: 0x58
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/Versions/A/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 214FDC8E-FB60-3E51-956C-74463C028C5A
-  Functions: 390
-  Symbols:   328
-  CStrings:  160
+  UUID: 6FD78B83-DA32-37D8-9009-F8E090AAD1CC
+  Functions: 754
+  Symbols:   463
+  CStrings:  149
 
Symbols:
+ -[objcDiagnosticPatternMatching lookForPattern:]
+ -[objcDiagnosticPatternMatching lookForPatternAsync::]
+ -[objcPanicPatternInfo .cxx_destruct]
+ -[objcPanicPatternInfo getPanicPatternInfo]
+ -[objcPanicPatternInfo initWithPatternInfo::::]
+ -[objcPanicPatternInfo initWithSwiftPanicPatternInfo:]
+ OBJC_IVAR_$_objcPanicPatternInfo._swiftPanicPatternInfo
+ _CONTAINER_PERSONA_PRIMARY
+ _NSSearchPathForDirectoriesInDomains
+ _OBJC_CLASS_$_NSDate
+ _OBJC_CLASS_$_NSFileManager
+ _OBJC_CLASS_$_NSPropertyListSerialization
+ _OBJC_CLASS_$__SwiftPanicPatternInfo
+ _OBJC_CLASS_$__TtC15CoreDiagnostics11PatternInfo
+ _OBJC_CLASS_$__TtC15CoreDiagnostics16CrashPatternInfo
+ _OBJC_CLASS_$_objcPanicPatternInfo
+ _OBJC_METACLASS_$__SwiftPanicPatternInfo
+ _OBJC_METACLASS_$__TtC15CoreDiagnostics11PatternInfo
+ _OBJC_METACLASS_$__TtC15CoreDiagnostics16CrashPatternInfo
+ _OBJC_METACLASS_$_objcPanicPatternInfo
+ __DATA__SwiftPanicPatternInfo
+ __DATA__TtC15CoreDiagnostics11PatternInfo
+ __DATA__TtC15CoreDiagnostics16CrashPatternInfo
+ __INSTANCE_METHODS__SwiftPanicPatternInfo
+ __INSTANCE_METHODS__TtC15CoreDiagnostics11PatternInfo
+ __INSTANCE_METHODS__TtC15CoreDiagnostics16CrashPatternInfo
+ __IVARS__SwiftPanicPatternInfo
+ __IVARS__TtC15CoreDiagnostics16CrashPatternInfo
+ __METACLASS_DATA__SwiftPanicPatternInfo
+ __METACLASS_DATA__TtC15CoreDiagnostics11PatternInfo
+ __METACLASS_DATA__TtC15CoreDiagnostics16CrashPatternInfo
+ __OBJC_$_INSTANCE_METHODS_objcPanicPatternInfo
+ __OBJC_$_INSTANCE_VARIABLES_objcPanicPatternInfo
+ __OBJC_CLASS_RO_$_objcPanicPatternInfo
+ __OBJC_METACLASS_RO_$_objcPanicPatternInfo
+ ___stack_chk_fail
+ ___stack_chk_guard
+ ___swift_allocate_boxed_opaque_existential_1
+ ___swift_destroy_boxed_opaque_existential_0Tm
+ ___swift_destroy_boxed_opaque_existential_1Tm
+ ___swift_instantiateGenericMetadata
+ ___swift_memcpy0_1
+ ___swift_memcpy16_8
+ ___swift_memcpy17_8
+ ___swift_memcpy18_8
+ ___swift_memcpy25_8
+ ___swift_memcpy40_8
+ ___swift_memcpy65_8
+ ___unnamed_1
+ _associated conformance 15CoreDiagnostics12CrashMatcherVyxGAA0D0AA18MatchedPatternTypeAaEP_AA0eF0
+ _associated conformance 15CoreDiagnostics12CrashMatcherVyxGAA0D0AA18PayloadManagerTypeAaEP_AA0eF0
+ _associated conformance 15CoreDiagnostics12PanicMatcherVyxGAA0D0AA18MatchedPatternTypeAaEP_AA0eF0
+ _associated conformance 15CoreDiagnostics12PanicMatcherVyxGAA0D0AA18PayloadManagerTypeAaEP_AA0eF0
+ _associated conformance 15CoreDiagnostics16CrashPatternInfoC10CodingKeys33_264CAC9C5452B2D27D48DE70552B036ELLOSHAASQ
+ _associated conformance 15CoreDiagnostics16CrashPatternInfoC10CodingKeys33_264CAC9C5452B2D27D48DE70552B036ELLOs0F3KeyAAs23CustomStringConvertible
+ _associated conformance 15CoreDiagnostics16CrashPatternInfoC10CodingKeys33_264CAC9C5452B2D27D48DE70552B036ELLOs0F3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 15CoreDiagnostics16CrashPatternInfoC11BinaryImageV10CodingKeys33_264CAC9C5452B2D27D48DE70552B036ELLOSHAASQ
+ _associated conformance 15CoreDiagnostics16CrashPatternInfoC11BinaryImageV10CodingKeys33_264CAC9C5452B2D27D48DE70552B036ELLOs0H3KeyAAs23CustomStringConvertible
+ _associated conformance 15CoreDiagnostics16CrashPatternInfoC11BinaryImageV10CodingKeys33_264CAC9C5452B2D27D48DE70552B036ELLOs0H3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 15CoreDiagnostics16CrashPatternInfoC5FrameV10CodingKeys33_264CAC9C5452B2D27D48DE70552B036ELLOSHAASQ
+ _associated conformance 15CoreDiagnostics16CrashPatternInfoC5FrameV10CodingKeys33_264CAC9C5452B2D27D48DE70552B036ELLOs0G3KeyAAs23CustomStringConvertible
+ _associated conformance 15CoreDiagnostics16CrashPatternInfoC5FrameV10CodingKeys33_264CAC9C5452B2D27D48DE70552B036ELLOs0G3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 15CoreDiagnostics16CrashPatternInfoC6ThreadV10CodingKeys33_264CAC9C5452B2D27D48DE70552B036ELLOSHAASQ
+ _associated conformance 15CoreDiagnostics16CrashPatternInfoC6ThreadV10CodingKeys33_264CAC9C5452B2D27D48DE70552B036ELLOs0G3KeyAAs23CustomStringConvertible
+ _associated conformance 15CoreDiagnostics16CrashPatternInfoC6ThreadV10CodingKeys33_264CAC9C5452B2D27D48DE70552B036ELLOs0G3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 15CoreDiagnostics18PanicPatternActionOSHAASQ
+ _associated conformance 15CoreDiagnostics22CrashPatternDefinitionV10CodingKeys33_0B136AF4634B1CA49DD982E54AAED5BCLLOSHAASQ
+ _associated conformance 15CoreDiagnostics22CrashPatternDefinitionV10CodingKeys33_0B136AF4634B1CA49DD982E54AAED5BCLLOs0F3KeyAAs23CustomStringConvertible
+ _associated conformance 15CoreDiagnostics22CrashPatternDefinitionV10CodingKeys33_0B136AF4634B1CA49DD982E54AAED5BCLLOs0F3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 15CoreDiagnostics22CrashPatternDefinitionV10SymbolNameV10CodingKeys33_0B136AF4634B1CA49DD982E54AAED5BCLLOSHAASQ
+ _associated conformance 15CoreDiagnostics22CrashPatternDefinitionV10SymbolNameV10CodingKeys33_0B136AF4634B1CA49DD982E54AAED5BCLLOs0H3KeyAAs23CustomStringConvertible
+ _associated conformance 15CoreDiagnostics22CrashPatternDefinitionV10SymbolNameV10CodingKeys33_0B136AF4634B1CA49DD982E54AAED5BCLLOs0H3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 15CoreDiagnostics22CrashPatternDefinitionV17NameWithinThreadsV10CodingKeys33_0B136AF4634B1CA49DD982E54AAED5BCLLOSHAASQ
+ _associated conformance 15CoreDiagnostics22CrashPatternDefinitionV17NameWithinThreadsV10CodingKeys33_0B136AF4634B1CA49DD982E54AAED5BCLLOs0I3KeyAAs23CustomStringConvertible
+ _associated conformance 15CoreDiagnostics22CrashPatternDefinitionV17NameWithinThreadsV10CodingKeys33_0B136AF4634B1CA49DD982E54AAED5BCLLOs0I3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 15CoreDiagnostics22PanicPatternDefinitionV10CodingKeys33_877CEF984B1EC9467A066CA25012C14BLLOSHAASQ
+ _associated conformance 15CoreDiagnostics22PanicPatternDefinitionV10CodingKeys33_877CEF984B1EC9467A066CA25012C14BLLOs0F3KeyAAs23CustomStringConvertible
+ _associated conformance 15CoreDiagnostics22PanicPatternDefinitionV10CodingKeys33_877CEF984B1EC9467A066CA25012C14BLLOs0F3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 15CoreDiagnostics7PatternV10CodingKeys33_233F337DD394DBBB28D37EC8473EAC62LLOyx_GSHAASQ
+ _associated conformance 15CoreDiagnostics7PatternV10CodingKeys33_233F337DD394DBBB28D37EC8473EAC62LLOyx_Gs0D3KeyAAs23CustomStringConvertible
+ _associated conformance 15CoreDiagnostics7PatternV10CodingKeys33_233F337DD394DBBB28D37EC8473EAC62LLOyx_Gs0D3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 15CoreDiagnostics7PayloadV10CodingKeysOyx_GSHAASQ
+ _associated conformance 15CoreDiagnostics7PayloadV10CodingKeysOyx_Gs0D3KeyAAs23CustomStringConvertible
+ _associated conformance 15CoreDiagnostics7PayloadV10CodingKeysOyx_Gs0D3KeyAAs28CustomDebugStringConvertible
+ _container_error_copy_unlocalized_description
+ _container_get_path
+ _container_query_create
+ _container_query_free
+ _container_query_get_last_error
+ _container_query_get_single_result
+ _container_query_operation_set_flags
+ _container_query_set_class
+ _container_query_set_identifiers
+ _container_query_set_persona_unique_string
+ _gethostuuid
+ _getuid
+ _objc_msgSend$initWithPatternInfo::::
+ _objc_msgSend$lookForPattern:
+ _objc_msgSend$lookForPatternAsync::
+ _objectdestroyTm
+ _sandbox_container_path_for_pid
+ _swift_allocBox
+ _swift_allocateGenericValueMetadata
+ _swift_checkMetadataState
+ _swift_getAssociatedConformanceWitness
+ _swift_getAssociatedTypeWitness
+ _swift_getEnumTagSinglePayloadGeneric
+ _swift_getGenericMetadata
+ _swift_getSingletonMetadata
+ _swift_initStructMetadata
+ _swift_isaMask
+ _swift_storeEnumTagSinglePayloadGeneric
+ _symbolic $s15CoreDiagnostics14MatchedPatternP
+ _symbolic $s15CoreDiagnostics14PayloadManagerP
+ _symbolic 11PayloadType_____Qz 15CoreDiagnostics14PayloadManagerP
+ _symbolic 18MatchedPatternType_____Qz 15CoreDiagnostics7MatcherP
+ _symbolic 18PayloadManagerType_____Qz 15CoreDiagnostics7MatcherP
+ _symbolic B0
+ _symbolic SDySSypG
+ _symbolic SDySSypGSg
+ _symbolic SS_ypt
+ _symbolic Say_____G 15CoreDiagnostics16CrashPatternInfoC11BinaryImageV
+ _symbolic Say_____G 15CoreDiagnostics16CrashPatternInfoC5FrameV
+ _symbolic Say_____G 15CoreDiagnostics16CrashPatternInfoC6ThreadV
+ _symbolic Say_____G 15CoreDiagnostics22CrashPatternDefinitionV10SymbolNameV
+ _symbolic Say_____G s6UInt32V
+ _symbolic Say_____GSg 15CoreDiagnostics16CrashPatternInfoC11BinaryImageV
+ _symbolic Say_____GSg 15CoreDiagnostics16CrashPatternInfoC6ThreadV
+ _symbolic Say_____GSg 15CoreDiagnostics18PanicPatternActionO
+ _symbolic Say_____GSg 15CoreDiagnostics22CrashPatternDefinitionV10SymbolNameV
+ _symbolic Say_____GSg s6UInt32V
+ _symbolic Say______pG 15CoreDiagnostics14MatchedPatternP
+ _symbolic Say_____y_____GG 15CoreDiagnostics7PayloadV AA22CrashPatternDefinitionV
+ _symbolic Say_____y_____GG 15CoreDiagnostics7PayloadV AA22PanicPatternDefinitionV
+ _symbolic Say_____yxGG 15CoreDiagnostics7PayloadV
+ _symbolic SbSg
+ _symbolic Su
+ _symbolic _____ 15CoreDiagnostics11PatternInfoC
+ _symbolic _____ 15CoreDiagnostics12CrashHistoryV
+ _symbolic _____ 15CoreDiagnostics12CrashMatcherV
+ _symbolic _____ 15CoreDiagnostics16CrashPatternInfoC
+ _symbolic _____ 15CoreDiagnostics16CrashPatternInfoC10CodingKeys33_264CAC9C5452B2D27D48DE70552B036ELLO
+ _symbolic _____ 15CoreDiagnostics16CrashPatternInfoC11BinaryImageV
+ _symbolic _____ 15CoreDiagnostics16CrashPatternInfoC11BinaryImageV10CodingKeys33_264CAC9C5452B2D27D48DE70552B036ELLO
+ _symbolic _____ 15CoreDiagnostics16CrashPatternInfoC5FrameV
+ _symbolic _____ 15CoreDiagnostics16CrashPatternInfoC5FrameV10CodingKeys33_264CAC9C5452B2D27D48DE70552B036ELLO
+ _symbolic _____ 15CoreDiagnostics16CrashPatternInfoC6ThreadV
+ _symbolic _____ 15CoreDiagnostics16CrashPatternInfoC6ThreadV10CodingKeys33_264CAC9C5452B2D27D48DE70552B036ELLO
+ _symbolic _____ 15CoreDiagnostics16PanicPatternInfoC
+ _symbolic _____ 15CoreDiagnostics18PanicPatternActionO
+ _symbolic _____ 15CoreDiagnostics19CrashMatchedPatternV
+ _symbolic _____ 15CoreDiagnostics19PanicMatchedPatternV
+ _symbolic _____ 15CoreDiagnostics19TrialPayloadManagerV
+ _symbolic _____ 15CoreDiagnostics22CrashPatternDefinitionV
+ _symbolic _____ 15CoreDiagnostics22CrashPatternDefinitionV10CodingKeys33_0B136AF4634B1CA49DD982E54AAED5BCLLO
+ _symbolic _____ 15CoreDiagnostics22CrashPatternDefinitionV10SymbolNameV
+ _symbolic _____ 15CoreDiagnostics22CrashPatternDefinitionV10SymbolNameV10CodingKeys33_0B136AF4634B1CA49DD982E54AAED5BCLLO
+ _symbolic _____ 15CoreDiagnostics22CrashPatternDefinitionV17NameWithinThreadsV
+ _symbolic _____ 15CoreDiagnostics22CrashPatternDefinitionV17NameWithinThreadsV10CodingKeys33_0B136AF4634B1CA49DD982E54AAED5BCLLO
+ _symbolic _____ 15CoreDiagnostics22PanicPatternDefinitionV
+ _symbolic _____ 15CoreDiagnostics22PanicPatternDefinitionV10CodingKeys33_877CEF984B1EC9467A066CA25012C14BLLO
+ _symbolic _____ 15CoreDiagnostics7PatternV10CodingKeys33_233F337DD394DBBB28D37EC8473EAC62LLO
+ _symbolic _____ 15CoreDiagnostics7PayloadV
+ _symbolic _____ 15CoreDiagnostics7PayloadV10CodingKeysO
+ _symbolic _____Sg 15CoreDiagnostics22CrashPatternDefinitionV17NameWithinThreadsV
+ _symbolic _____Sg s5Int32V
+ _symbolic _____SgSg 10Foundation3URLV
+ _symbolic __________SbSgIeggnd_ 15CoreDiagnostics16CrashPatternInfoC AA0cD10DefinitionV
+ _symbolic ______p 15CoreDiagnostics14MatchedPatternP
+ _symbolic _____ySSypG s18_DictionaryStorageC
+ _symbolic _____ySbSg___________tcG s23_ContiguousArrayStorageC 15CoreDiagnostics16CrashPatternInfoC AC0fG10DefinitionV
+ _symbolic _____y_____G 15CoreDiagnostics7PayloadV AA22CrashPatternDefinitionV
+ _symbolic _____y_____G 15CoreDiagnostics7PayloadV AA22PanicPatternDefinitionV
+ _symbolic _____y_____G s22KeyedDecodingContainerV 15CoreDiagnostics16CrashPatternInfoC10CodingKeys33_264CAC9C5452B2D27D48DE70552B036ELLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 15CoreDiagnostics16CrashPatternInfoC11BinaryImageV10CodingKeys33_264CAC9C5452B2D27D48DE70552B036ELLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 15CoreDiagnostics16CrashPatternInfoC5FrameV10CodingKeys33_264CAC9C5452B2D27D48DE70552B036ELLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 15CoreDiagnostics16CrashPatternInfoC6ThreadV10CodingKeys33_264CAC9C5452B2D27D48DE70552B036ELLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 15CoreDiagnostics22CrashPatternDefinitionV10CodingKeys33_0B136AF4634B1CA49DD982E54AAED5BCLLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 15CoreDiagnostics22CrashPatternDefinitionV10SymbolNameV10CodingKeys33_0B136AF4634B1CA49DD982E54AAED5BCLLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 15CoreDiagnostics22CrashPatternDefinitionV17NameWithinThreadsV10CodingKeys33_0B136AF4634B1CA49DD982E54AAED5BCLLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 15CoreDiagnostics22PanicPatternDefinitionV10CodingKeys33_877CEF984B1EC9467A066CA25012C14BLLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 15CoreDiagnostics16CrashPatternInfoC10CodingKeys33_264CAC9C5452B2D27D48DE70552B036ELLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 15CoreDiagnostics16CrashPatternInfoC11BinaryImageV10CodingKeys33_264CAC9C5452B2D27D48DE70552B036ELLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 15CoreDiagnostics16CrashPatternInfoC5FrameV10CodingKeys33_264CAC9C5452B2D27D48DE70552B036ELLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 15CoreDiagnostics16CrashPatternInfoC6ThreadV10CodingKeys33_264CAC9C5452B2D27D48DE70552B036ELLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 15CoreDiagnostics22CrashPatternDefinitionV10CodingKeys33_0B136AF4634B1CA49DD982E54AAED5BCLLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 15CoreDiagnostics22CrashPatternDefinitionV10SymbolNameV10CodingKeys33_0B136AF4634B1CA49DD982E54AAED5BCLLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 15CoreDiagnostics22CrashPatternDefinitionV17NameWithinThreadsV10CodingKeys33_0B136AF4634B1CA49DD982E54AAED5BCLLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 15CoreDiagnostics22PanicPatternDefinitionV10CodingKeys33_877CEF984B1EC9467A066CA25012C14BLLO
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 15CoreDiagnostics18PanicPatternActionO
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 15CoreDiagnostics19CrashMatchedPatternV
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 15CoreDiagnostics19PanicMatchedPatternV
+ _symbolic _____y_____y_____GG 15CoreDiagnostics12CrashMatcherV AA19TrialPayloadManagerV AA0C17PatternDefinitionV
+ _symbolic _____y_____y_____GG 15CoreDiagnostics12PanicMatcherV AA19TrialPayloadManagerV AA0C17PatternDefinitionV
+ _symbolic _____yxG 15CoreDiagnostics12CrashMatcherV
+ _symbolic _____yxG 15CoreDiagnostics7PatternV
+ _symbolic _____yxG 15CoreDiagnostics7PayloadV
+ _symbolic x
+ _xpc_string_create
+ block_copy_helper.30
+ block_descriptor.32
+ block_destroy_helper.31
+ objectdestroy.11Tm
+ objectdestroy.17Tm
- -[objcCriterials .cxx_destruct]
- -[objcCriterials initWithInfo:::]
- -[objcCriterials initWithSwiftCriterials:]
- -[objcDiagnosticPatternMatching lookForPattern::]
- -[objcDiagnosticPatternMatching lookForPatternAsync:::]
- -[objcPanicCriterials .cxx_destruct]
- -[objcPanicCriterials getPanicCriterials]
- -[objcPanicCriterials initWithCriterials::::]
- -[objcPanicCriterials initWithSwiftPanicCriterials:]
- OBJC_IVAR_$_objcCriterials._swiftCriterials
- OBJC_IVAR_$_objcPanicCriterials._swiftPanicCriterials
- _OBJC_CLASS_$_TRIFile
- _OBJC_CLASS_$_TRILevel
- _OBJC_CLASS_$__SwiftCriterials
- _OBJC_CLASS_$__SwiftPanicCriterials
- _OBJC_CLASS_$_objcCriterials
- _OBJC_CLASS_$_objcPanicCriterials
- _OBJC_METACLASS_$__SwiftCriterials
- _OBJC_METACLASS_$__SwiftPanicCriterials
- _OBJC_METACLASS_$_objcCriterials
- _OBJC_METACLASS_$_objcPanicCriterials
- __DATA__SwiftCriterials
- __DATA__SwiftPanicCriterials
- __INSTANCE_METHODS__SwiftCriterials
- __INSTANCE_METHODS__SwiftPanicCriterials
- __IVARS__SwiftCriterials
- __IVARS__SwiftPanicCriterials
- __METACLASS_DATA__SwiftCriterials
- __METACLASS_DATA__SwiftPanicCriterials
- __OBJC_$_INSTANCE_METHODS_objcCriterials
- __OBJC_$_INSTANCE_METHODS_objcPanicCriterials
- __OBJC_$_INSTANCE_VARIABLES_objcCriterials
- __OBJC_$_INSTANCE_VARIABLES_objcPanicCriterials
- __OBJC_CLASS_RO_$_objcCriterials
- __OBJC_CLASS_RO_$_objcPanicCriterials
- __OBJC_METACLASS_RO_$_objcCriterials
- __OBJC_METACLASS_RO_$_objcPanicCriterials
- ___swift_memcpy56_8
- ___swift_memcpy80_8
- ___swift_mutable_project_boxed_opaque_existential_1
- _associated conformance 15CoreDiagnostics10DefinitionV10CodingKeys33_877CEF984B1EC9467A066CA25012C14BLLOSHAASQ
- _associated conformance 15CoreDiagnostics10DefinitionV10CodingKeys33_877CEF984B1EC9467A066CA25012C14BLLOs0D3KeyAAs23CustomStringConvertible
- _associated conformance 15CoreDiagnostics10DefinitionV10CodingKeys33_877CEF984B1EC9467A066CA25012C14BLLOs0D3KeyAAs28CustomDebugStringConvertible
- _associated conformance 15CoreDiagnostics12PanicPayloadV10CodingKeysOSHAASQ
- _associated conformance 15CoreDiagnostics12PanicPayloadV10CodingKeysOs0E3KeyAAs23CustomStringConvertible
- _associated conformance 15CoreDiagnostics12PanicPayloadV10CodingKeysOs0E3KeyAAs28CustomDebugStringConvertible
- _associated conformance 15CoreDiagnostics7PatternV10CodingKeys33_877CEF984B1EC9467A066CA25012C14BLLOSHAASQ
- _associated conformance 15CoreDiagnostics7PatternV10CodingKeys33_877CEF984B1EC9467A066CA25012C14BLLOs0D3KeyAAs23CustomStringConvertible
- _associated conformance 15CoreDiagnostics7PatternV10CodingKeys33_877CEF984B1EC9467A066CA25012C14BLLOs0D3KeyAAs28CustomDebugStringConvertible
- _objc_msgSend$initWithCriterials::::
- _objc_msgSend$initWithInfo:::
- _objc_msgSend$lookForPattern::
- _objc_msgSend$lookForPatternAsync:::
- _swift_deletedMethodError
- _swift_endAccess
- _swift_makeBoxUnique
- _symbolic $s15CoreDiagnostics14PatternPayloadP
- _symbolic Say_____G 15CoreDiagnostics12PanicPayloadV
- _symbolic _____ 15CoreDiagnostics10CriterialsC
- _symbolic _____ 15CoreDiagnostics10DefinitionV
- _symbolic _____ 15CoreDiagnostics10DefinitionV10CodingKeys33_877CEF984B1EC9467A066CA25012C14BLLO
- _symbolic _____ 15CoreDiagnostics12PanicPayloadV
- _symbolic _____ 15CoreDiagnostics12PanicPayloadV10CodingKeysO
- _symbolic _____ 15CoreDiagnostics15PanicCriterialsC
- _symbolic _____ 15CoreDiagnostics7PatternV10CodingKeys33_877CEF984B1EC9467A066CA25012C14BLLO
- _symbolic _____Sg s6UInt32V
- _symbolic ______p 15CoreDiagnostics14PatternPayloadP
- _symbolic _____y_____G s22KeyedDecodingContainerV 15CoreDiagnostics10DefinitionV10CodingKeys33_877CEF984B1EC9467A066CA25012C14BLLO
- _symbolic _____y_____G s22KeyedDecodingContainerV 15CoreDiagnostics12PanicPayloadV10CodingKeysO
- _symbolic _____y_____G s22KeyedDecodingContainerV 15CoreDiagnostics7PatternV10CodingKeys33_877CEF984B1EC9467A066CA25012C14BLLO
- _symbolic _____y_____G s22KeyedEncodingContainerV 15CoreDiagnostics10DefinitionV10CodingKeys33_877CEF984B1EC9467A066CA25012C14BLLO
- _symbolic _____y_____G s22KeyedEncodingContainerV 15CoreDiagnostics12PanicPayloadV10CodingKeysO
- _symbolic _____y_____G s22KeyedEncodingContainerV 15CoreDiagnostics7PatternV10CodingKeys33_877CEF984B1EC9467A066CA25012C14BLLO
- _symbolic _____y______pG s23_ContiguousArrayStorageC 15CoreDiagnostics14PatternPayloadP
- _symbolic _____z_Xx s6UInt32V
CStrings:
+ "%s already exists"
+ "@\"_SwiftPanicPatternInfo\""
+ "B24@0:8@16"
+ "Cannot find Application Support directory"
+ "Cannot find Application Support directory for sandboxed application"
+ "CoreDiagnostics.CrashPatternInfo"
+ "CoreDiagnostics.PanicPatternInfo"
+ "Could not retrieve host UUID"
+ "CrashPatternDefinition"
+ "DIAGNOSTIC_PATTERN_MATCHING_CRASH"
+ "Error decoding payload: %@"
+ "Error executing container query: %s"
+ "Error reading plist file: %@"
+ "Error while writing crash history to %{public}s: %@"
+ "Failed to create %s: %@"
+ "Failed to read payload at %s"
+ "Failed to resolve crash history file on disk for current process; cannot read crash history"
+ "Failed to resolve crash history file on disk for current process; cannot write crash history"
+ "Failed to retrieve crash history dict"
+ "Key '%s' not found: %s\nCoding Path: %s"
+ "Matched the pattern definition with UUID %s"
+ "Missing asset for %s in namespace %s"
+ "Missing level for %s in namespace %s"
+ "PanicPatternDefinition"
+ "Payload %ld: %s"
+ "Successfully parsed payload for %s in namespace %s as type %s. Count = %ld"
+ "The received pattern info are not valid"
+ "There are no crash payloads available"
+ "Trial is not available"
+ "Type '%s' mismatch: %s\nCoding Path: %s"
+ "Unable to create container query"
+ "Unable to parse payload for %s in namespace %s as type %s"
+ "Using Trial payload at %s for %s in namespace %s"
+ "Value '%s' not found: %s\nCoding Path: %s"
+ "_SwiftPanicPatternInfo"
+ "_TtC15CoreDiagnostics11PatternInfo"
+ "_TtC15CoreDiagnostics16CrashPatternInfo"
+ "_swiftPanicPatternInfo"
+ "actions"
+ "com.apple.corediagnostics.diagnostic-intelligence"
+ "com.apple.per-process-history.queue"
+ "contentsAtPath:"
+ "createDirectoryAtURL:withIntermediateDirectories:attributes:error:"
+ "dataWithPropertyList:format:options:error:"
+ "defaultManager"
+ "getPanicPatternInfo"
+ "initWithPatternInfo::::"
+ "initWithSwiftPanicPatternInfo:"
+ "lookForPattern:"
+ "lookForPatternAsync::"
+ "no error description"
+ "objcPanicPatternInfo"
+ "procName"
+ "propertyListWithData:options:format:error:"
+ "requireCrashingThread"
+ "threads"
+ "usedImages"
+ "v32@0:8@16@?24"
- "@\"_SwiftCriterials\""
- "@\"_SwiftPanicCriterials\""
- "@40@0:8@16@24@32"
- "B28@0:8@16B24"
- "Can't construct Array with count < 0"
- "CoreDiagnostics.Criterials"
- "CoreDiagnostics.PanicCriterials"
- "Division by zero"
- "Division results in an overflow"
- "Failed to find panic payload from Trial"
- "Failed to parse payload"
- "Failed to read payload file %s"
- "Fatal error"
- "Insufficient space allocated to copy string contents"
- "Key %s not found: %s"
- "Must take zero or more splits"
- "No payloadManager"
- "No valid assets in trial level for factor panicPayloadV1"
- "Range requires lowerBound <= upperBound"
- "Swift/Array.swift"
- "Swift/Collection.swift"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/IntegerTypes.swift"
- "Swift/Range.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "The received criterials are not valid"
- "Trial is not available on this OS"
- "Type '%s' mismatch: %s"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutablePointer.initialize with negative count"
- "UnsafeMutablePointer.moveInitialize with negative count"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "Value '%s' not found: %s"
- "_SwiftCriterials"
- "_SwiftPanicCriterials"
- "_swiftCriterials"
- "_swiftPanicCriterials"
- "action"
- "codingPath: %s"
- "com.apple.corediagnostics.pattern-matching"
- "error: %@"
- "found Trial payload at %s"
- "found trial clinet"
- "getPanicCriterials"
- "hasPath"
- "init(id:type:path:)"
- "initWithCriterials::::"
- "initWithInfo:::"
- "initWithSwiftCriterials:"
- "initWithSwiftPanicCriterials:"
- "invalid Collection: less than 'count' elements in collection"
- "lookForPattern::"
- "lookForPatternAsync:::"
- "objcCriterials"
- "objcPanicCriterials"
- "panic payload %s updated"
- "payloads count %ld"
- "read %s"
- "refresh"
- "setPath:"
- "update panic payloads"
- "v36@0:8@16B24@?28"

```
