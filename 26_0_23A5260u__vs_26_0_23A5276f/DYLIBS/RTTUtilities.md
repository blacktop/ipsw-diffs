## RTTUtilities

> `/System/Library/PrivateFrameworks/RTTUtilities.framework/RTTUtilities`

```diff

-485.3.0.0.0
-  __TEXT.__text: 0x253cc
-  __TEXT.__auth_stubs: 0x7e0
-  __TEXT.__objc_methlist: 0x1bd0
-  __TEXT.__const: 0xf0
-  __TEXT.__gcc_except_tab: 0xcfc
-  __TEXT.__cstring: 0x17f9
-  __TEXT.__oslogstring: 0x2e23
+488.0.0.0.0
+  __TEXT.__text: 0x26cac
+  __TEXT.__auth_stubs: 0x9c0
+  __TEXT.__objc_methlist: 0x1d00
+  __TEXT.__const: 0x16a
+  __TEXT.__gcc_except_tab: 0xcf8
+  __TEXT.__cstring: 0x196b
+  __TEXT.__oslogstring: 0x2f2e
   __TEXT.__dlopen_cstrs: 0x279
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x988
+  __TEXT.__swift5_typeref: 0x46
+  __TEXT.__swift5_capture: 0x30
+  __TEXT.__constg_swiftt: 0x9c
+  __TEXT.__swift5_reflstr: 0xb
+  __TEXT.__swift5_fieldmd: 0x38
+  __TEXT.__swift5_types: 0x8
+  __TEXT.__unwind_info: 0xa58
+  __TEXT.__eh_frame: 0x48
   __TEXT.__objc_classname: 0x247
-  __TEXT.__objc_methname: 0x58ac
-  __TEXT.__objc_methtype: 0x881
-  __TEXT.__objc_stubs: 0x5040
-  __DATA_CONST.__got: 0x3a0
-  __DATA_CONST.__const: 0xec0
-  __DATA_CONST.__objc_classlist: 0x88
+  __TEXT.__objc_methname: 0x5b0b
+  __TEXT.__objc_methtype: 0x898
+  __TEXT.__objc_stubs: 0x5240
+  __DATA_CONST.__got: 0x3a8
+  __DATA_CONST.__const: 0xf78
+  __DATA_CONST.__objc_classlist: 0x98
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x18b8
+  __DATA_CONST.__objc_selrefs: 0x1948
   __DATA_CONST.__objc_superrefs: 0x78
   __DATA_CONST.__objc_arraydata: 0x178
-  __AUTH_CONST.__auth_got: 0x400
-  __AUTH_CONST.__const: 0x4a0
-  __AUTH_CONST.__cfstring: 0x18a0
-  __AUTH_CONST.__objc_const: 0x1e88
+  __AUTH_CONST.__auth_got: 0x4f0
+  __AUTH_CONST.__const: 0x518
+  __AUTH_CONST.__cfstring: 0x18e0
+  __AUTH_CONST.__objc_const: 0x2000
   __AUTH_CONST.__objc_dictobj: 0x118
   __AUTH_CONST.__objc_intobj: 0x108
   __AUTH_CONST.__objc_arrayobj: 0xa8
-  __DATA.__objc_ivar: 0x140
-  __DATA.__data: 0x4a8
-  __DATA.__bss: 0x98
+  __AUTH.__objc_data: 0x198
+  __AUTH.__data: 0x50
+  __DATA.__objc_ivar: 0x148
+  __DATA.__data: 0x4c0
+  __DATA.__bss: 0xd0
   __DATA_DIRTY.__objc_data: 0x550
   __DATA_DIRTY.__data: 0x18
   __DATA_DIRTY.__bss: 0xe8

   - /System/Library/PrivateFrameworks/CallHistory.framework/CallHistory
   - /System/Library/PrivateFrameworks/HearingCore.framework/HearingCore
   - /System/Library/PrivateFrameworks/IDS.framework/IDS
+  - /System/Library/PrivateFrameworks/LiveTranscription.framework/LiveTranscription
   - /System/Library/PrivateFrameworks/MediaExperience.framework/MediaExperience
   - /System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset
   - /System/Library/PrivateFrameworks/NanoPreferencesSync.framework/NanoPreferencesSync

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 626664B3-CE71-35A3-844E-25219930AAE0
-  Functions: 766
-  Symbols:   2960
-  CStrings:  1847
+  - /usr/lib/swift/libswiftAVFoundation.dylib
+  - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreAudio.dylib
+  - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreImage.dylib
+  - /usr/lib/swift/libswiftCoreMIDI.dylib
+  - /usr/lib/swift/libswiftCoreMedia.dylib
+  - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftMetal.dylib
+  - /usr/lib/swift/libswiftOSLog.dylib
+  - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftQuartzCore.dylib
+  - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
+  - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswiftos.dylib
+  - /usr/lib/swift/libswiftsimd.dylib
+  UUID: 922797B9-9383-3FB8-A47D-1CC39D73CA17
+  Functions: 836
+  Symbols:   3104
+  CStrings:  1896
 
Symbols:
+ +[RTTTelephonyUtilities isEmergencyRTTSupportedByCarrierBundle]
+ +[RTTTelephonyUtilities isRTTSupportedByCarrierBundle]
+ -[RTTCall isVisibleSent]
+ -[RTTCall setIsVisibleSent:]
+ -[RTTTelephonyUtilities isEmergencyRTTSupportedForContext:excludeRelay:]
+ -[RTTTelephonyUtilities isRTTSupportedForContext:excludeRelay:]
+ -[RTTTelephonyUtilities isTTYOverIMSSupportedForContext:excludeRelay:]
+ -[RTTTranscriptionController liveCaptionsService]
+ -[RTTTranscriptionController setLiveCaptionsService:]
+ -[RTTTranscriptionController startTranscribingV2ForCallUUID:]
+ -[RTTTranscriptionController stopTranscribingV2ForCallUUID:]
+ GCC_except_table56
+ GCC_except_table65
+ GCC_except_table68
+ GCC_except_table72
+ GCC_except_table88
+ _LiveTranscriptionLibrary
+ _OBJC_CLASS_$_RTTLiveCaptionObjC
+ _OBJC_CLASS_$_RTTLiveCaptionsObjC
+ _OBJC_IVAR_$_RTTCall._isVisibleSent
+ _OBJC_IVAR_$_RTTTranscriptionController._liveCaptionsService
+ _OBJC_METACLASS_$_RTTLiveCaptionObjC
+ _OBJC_METACLASS_$_RTTLiveCaptionsObjC
+ __Block_copy
+ __Block_release
+ __CLASS_METHODS_RTTLiveCaptionsObjC
+ __CLASS_PROPERTIES_RTTLiveCaptionsObjC
+ __DATA_RTTLiveCaptionObjC
+ __DATA_RTTLiveCaptionsObjC
+ __INSTANCE_METHODS_RTTLiveCaptionObjC
+ __INSTANCE_METHODS_RTTLiveCaptionsObjC
+ __IVARS_RTTLiveCaptionObjC
+ __IVARS_RTTLiveCaptionsObjC
+ __METACLASS_DATA_RTTLiveCaptionObjC
+ __METACLASS_DATA_RTTLiveCaptionsObjC
+ ___28-[RTTRemoteCall sendString:]_block_invoke.595
+ ___33-[RTTCall device:didReceiveText:]_block_invoke.419
+ ___38-[RTTDictionaryManager deleteIfNeeded]_block_invoke.285
+ ___44-[RTTRemoteCall responseForRequest:options:]_block_invoke.636
+ ___44-[RTTRemoteCall responseForRequest:options:]_block_invoke.638
+ ___44-[RTTRemoteCall responseForRequest:options:]_block_invoke.638.cold.1
+ ___49-[RTTRemoteCall callDidReceiveText:forUtterance:]_block_invoke.612
+ ___49-[RTTRemoteCall callDidReceiveText:forUtterance:]_block_invoke.616
+ ___55-[RTTRemoteCall newRapportClientWithDestinationDevice:]_block_invoke.625
+ ___55-[RTTRemoteCall newRapportClientWithDestinationDevice:]_block_invoke.628
+ ___55-[RTTRemoteCall newRapportClientWithDestinationDevice:]_block_invoke.629
+ ___60-[RTTTranscriptionController stopTranscribingV2ForCallUUID:]_block_invoke
+ ___60-[RTTTranscriptionController stopTranscribingV2ForCallUUID:]_block_invoke.cold.1
+ ___61-[RTTRemoteCall sendCallIDChallengeToDeviceId:orAlternateId:]_block_invoke.632
+ ___61-[RTTTranscriptionController startTranscribingV2ForCallUUID:]_block_invoke
+ ___61-[RTTTranscriptionController startTranscribingV2ForCallUUID:]_block_invoke.cold.1
+ ___61-[RTTTranscriptionController startTranscribingV2ForCallUUID:]_block_invoke.cold.2
+ ___61-[RTTTranscriptionController startTranscribingV2ForCallUUID:]_block_invoke_2
+ ___block_descriptor_40_e8_32s_e28_v16?0"RTTLiveCaptionObjC"8ls32l8
+ ___block_literal_global.287
+ ___block_literal_global.289
+ ___block_literal_global.580
+ ___chkstk_darwin
+ ___getAXLCLiveCaptionsSelectedLocaleIdentifierSymbolLoc_block_invoke
+ ___swift_instantiateConcreteTypeFromMangledName
+ ___swift_reflection_version
+ __swift_FORCE_LOAD_$_swiftAVFoundation
+ __swift_FORCE_LOAD_$_swiftAVFoundation_$_RTTUtilities
+ __swift_FORCE_LOAD_$_swiftAccelerate
+ __swift_FORCE_LOAD_$_swiftAccelerate_$_RTTUtilities
+ __swift_FORCE_LOAD_$_swiftCoreAudio
+ __swift_FORCE_LOAD_$_swiftCoreAudio_$_RTTUtilities
+ __swift_FORCE_LOAD_$_swiftCoreFoundation
+ __swift_FORCE_LOAD_$_swiftCoreFoundation_$_RTTUtilities
+ __swift_FORCE_LOAD_$_swiftCoreImage
+ __swift_FORCE_LOAD_$_swiftCoreImage_$_RTTUtilities
+ __swift_FORCE_LOAD_$_swiftCoreMIDI
+ __swift_FORCE_LOAD_$_swiftCoreMIDI_$_RTTUtilities
+ __swift_FORCE_LOAD_$_swiftCoreMedia
+ __swift_FORCE_LOAD_$_swiftCoreMedia_$_RTTUtilities
+ __swift_FORCE_LOAD_$_swiftDispatch
+ __swift_FORCE_LOAD_$_swiftDispatch_$_RTTUtilities
+ __swift_FORCE_LOAD_$_swiftFoundation
+ __swift_FORCE_LOAD_$_swiftFoundation_$_RTTUtilities
+ __swift_FORCE_LOAD_$_swiftMetal
+ __swift_FORCE_LOAD_$_swiftMetal_$_RTTUtilities
+ __swift_FORCE_LOAD_$_swiftOSLog
+ __swift_FORCE_LOAD_$_swiftOSLog_$_RTTUtilities
+ __swift_FORCE_LOAD_$_swiftObjectiveC
+ __swift_FORCE_LOAD_$_swiftObjectiveC_$_RTTUtilities
+ __swift_FORCE_LOAD_$_swiftQuartzCore
+ __swift_FORCE_LOAD_$_swiftQuartzCore_$_RTTUtilities
+ __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers
+ __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers_$_RTTUtilities
+ __swift_FORCE_LOAD_$_swiftXPC
+ __swift_FORCE_LOAD_$_swiftXPC_$_RTTUtilities
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_Builtin_float_$_RTTUtilities
+ __swift_FORCE_LOAD_$_swiftos
+ __swift_FORCE_LOAD_$_swiftos_$_RTTUtilities
+ __swift_FORCE_LOAD_$_swiftsimd
+ __swift_FORCE_LOAD_$_swiftsimd_$_RTTUtilities
+ __swift_stdlib_reportUnimplementedInitializer
+ _getAXLCLiveCaptionsSelectedLocaleIdentifierSymbolLoc.ptr
+ _objc_allocWithZone
+ _objc_autorelease
+ _objc_msgSend$isEmergencyRTTSupportedByCarrierBundle
+ _objc_msgSend$isEmergencyRTTSupportedForContext:excludeRelay:
+ _objc_msgSend$isRTTSupportedByCarrierBundle
+ _objc_msgSend$isRTTSupportedForContext:excludeRelay:
+ _objc_msgSend$isTTYOverIMSSupportedForContext:excludeRelay:
+ _objc_msgSend$isVisibleSent
+ _objc_msgSend$liveCaptionsService
+ _objc_msgSend$resultType
+ _objc_msgSend$resultTypeFinal
+ _objc_msgSend$setIsVisibleSent:
+ _objc_msgSend$setLiveCaptionsService:
+ _objc_msgSend$shared
+ _objc_msgSend$sourceTypeDownlink
+ _objc_msgSend$startTranscribingV2ForCallUUID:
+ _objc_msgSend$startWithSource:locale:sharedRoute:excludePIDs:error:transcriptionResult:
+ _objc_msgSend$stop:error:
+ _objc_msgSend$stopTranscribingV2ForCallUUID:
+ _objc_opt_self
+ _soft_AXHasCapability
+ _soft_AXHasCapability.cold.1
+ _swift_allocObject
+ _swift_bridgeObjectRelease
+ _swift_deallocObject
+ _swift_errorRelease
+ _swift_getTypeByMangledNameInContext2
+ _swift_isaMask
+ _swift_lookUpClassMethod
+ _swift_once
+ _swift_release
+ _swift_retain
+ _swift_willThrow
+ _symbolic So8NSObjectC
+ _symbolic _____ 12RTTUtilities18RTTLiveCaptionObjCC
+ _symbolic _____ 12RTTUtilities19RTTLiveCaptionsObjCC
+ _symbolic _____ 17LiveTranscription13AXLiveCaptionC
+ _symbolic _____ 17LiveTranscription14AXLiveCaptionsC
+ _symbolic _____Iegg_ 12RTTUtilities18RTTLiveCaptionObjCC
+ _symbolic _____IeyBy_ 12RTTUtilities18RTTLiveCaptionObjCC
+ _symbolic _____Sg 10Foundation6LocaleV
- -[RTTTranscriptionController startTranscribingForCallUUID:].cold.2
- GCC_except_table54
- GCC_except_table55
- GCC_except_table63
- GCC_except_table66
- GCC_except_table70
- GCC_except_table84
- ___28-[RTTRemoteCall sendString:]_block_invoke.583
- ___33-[RTTCall device:didReceiveText:]_block_invoke.412
- ___38-[RTTDictionaryManager deleteIfNeeded]_block_invoke.279
- ___44-[RTTRemoteCall responseForRequest:options:]_block_invoke.624
- ___44-[RTTRemoteCall responseForRequest:options:]_block_invoke.626
- ___44-[RTTRemoteCall responseForRequest:options:]_block_invoke.626.cold.1
- ___49-[RTTRemoteCall callDidReceiveText:forUtterance:]_block_invoke.600
- ___49-[RTTRemoteCall callDidReceiveText:forUtterance:]_block_invoke.604
- ___55-[RTTRemoteCall newRapportClientWithDestinationDevice:]_block_invoke.613
- ___55-[RTTRemoteCall newRapportClientWithDestinationDevice:]_block_invoke.616
- ___55-[RTTRemoteCall newRapportClientWithDestinationDevice:]_block_invoke.617
- ___61-[RTTRemoteCall sendCallIDChallengeToDeviceId:orAlternateId:]_block_invoke.620
- ___block_literal_global.284
- ___block_literal_global.286
- ___block_literal_global.568
- _objc_msgSend$isTTYOverIMSSupportedForContext:
CStrings:
+ "@\"RTTLiveCaptionsObjC\""
+ "AXLCLiveCaptionsSelectedLocaleIdentifier"
+ "AXLiveCaptionsLanguageExpansion"
+ "B32@0:8q16^@24"
+ "B60@0:8q16@24B32@36^@44@?52"
+ "Emergency RTT (EmergencyRTTSupported) supported %@ - %d = %@ -- %d (%d)"
+ "Failed to start transcribing V2: %{public}@"
+ "Failed to stop transcribing V2: %{public}@"
+ "RTT (RTTSupported) supported %@ - %d = %@ -- %d (%d)"
+ "RTT (ttyIMSSupported) supported %@ - %d = %@ -- %d (%d)"
+ "RTTCallUIVisibleNotificationName"
+ "RTTUtilities.RTTLiveCaptionObjC"
+ "Started transcription V2 for callUUID %@"
+ "Stopped transcription V2 for callUUID %@"
+ "T@\"RTTLiveCaptionsObjC\",&,N,V_liveCaptionsService"
+ "T@\"RTTLiveCaptionsObjC\",N,R"
+ "TB,N,V_isVisibleSent"
+ "Tq,N,R"
+ "_isVisibleSent"
+ "_liveCaptionsService"
+ "init()"
+ "initWithRootObject:"
+ "isEmergencyRTTSupportedByCarrierBundle"
+ "isEmergencyRTTSupportedByCarrierBundle: %d"
+ "isEmergencyRTTSupportedForContext:excludeRelay:"
+ "isRTTSupportedByCarrierBundle"
+ "isRTTSupportedByCarrierBundle: %d"
+ "isRTTSupportedForContext:excludeRelay:"
+ "isTTYOverIMSSupportedForContext:excludeRelay:"
+ "isVisibleSent"
+ "liveCaptionsService"
+ "resultType"
+ "resultTypeFinal"
+ "rootObject"
+ "setIsVisibleSent:"
+ "setLiveCaptionsService:"
+ "shared"
+ "sourceTypeDownlink"
+ "startTranscribingV2ForCallUUID:"
+ "startWithSource:locale:sharedRoute:excludePIDs:error:transcriptionResult:"
+ "stop:error:"
+ "stopTranscribingV2ForCallUUID:"
+ "v16@?0@\"RTTLiveCaptionObjC\"8"
- "Emergency RTT (EmergencyRTTSupported) supported %@ - %d = %@ -- %d"
- "RTT (RTTSupported) supported %@ - %d = %@"
- "RTT (ttyIMSSupported) supported %@ - %d = %@ -- %d"

```
