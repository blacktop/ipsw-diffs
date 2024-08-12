## UserNotificationsServices

> `/System/Library/PrivateFrameworks/UserNotificationsServices.framework/UserNotificationsServices`

```diff

-575.1.1.0.0
-  __TEXT.__text: 0x29548
+579.2.3.0.0
+  __TEXT.__text: 0x29570
   __TEXT.__auth_stubs: 0xbd0
   __TEXT.__objc_methlist: 0x39c
   __TEXT.__const: 0x3224

   __TEXT.__objc_methtype: 0x275
   __TEXT.__objc_stubs: 0x1180
   __DATA_CONST.__got: 0x2e0
-  __DATA_CONST.__const: 0x118
+  __DATA_CONST.__const: 0x158
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8

   __AUTH_CONST.__const: 0x1280
   __AUTH_CONST.__cfstring: 0x280
   __AUTH_CONST.__objc_const: 0xa30
-  __AUTH.__objc_data: 0x1e0
-  __AUTH.__data: 0x88
   __DATA.__objc_ivar: 0x40
-  __DATA.__data: 0xeb8
-  __DATA.__bss: 0x63b0
-  __DATA_DIRTY.__data: 0x4c0
-  __DATA_DIRTY.__bss: 0x380
+  __DATA.__data: 0xd90
+  __DATA.__bss: 0x6230
+  __DATA_DIRTY.__objc_data: 0x1e0
+  __DATA_DIRTY.__data: 0x670
+  __DATA_DIRTY.__bss: 0x500
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
   Functions: 1184
-  Symbols:   267
-  CStrings:  0
+  Symbols:   275
+  CStrings:  162
 
Symbols:
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
CStrings:
+ "C_METACLASS_$_SFUIImageProvider"
+ "_$s13SiriUtilities0A11EnvironmentC0A19ReferenceResolutionE06scopeddE4DataAD06ScopeddeG8ProviderCvg"
+ "_$s13SiriUtilities0A11EnvironmentC0A19ReferenceResolutionE23salientEntitiesProviderAD07Salientg4DataH0Cvg"
+ "_$s23SiriReferenceResolution06ScopedbC12DataProviderC0A9Utilities0a11EnvironmentF0AAMc"
+ "_$s23SiriReferenceResolution06ScopedbC12DataProviderC21dataForCurrentRequest10Foundation0E0VSgvsTj"
+ "_$s23SiriReferenceResolution06ScopedbC12DataProviderCMa"
+ "_$s23SiriReferenceResolution0bC6ClientC03hasB09usoEntitySb0A8Ontology03UsoG0C_tFTj"
+ "_$s23SiriReferenceResolution0bC6ClientC13siriMentioned8entities13configuration10completionySay0abC9DataModel8RREntityVG_AH8RRFilterVSgys6ResultOyyts5Error_pGctFTj"
+ "_$s23SiriReferenceResolution0bC6ClientC14dumpEntityData10Foundation0G0VyKFTj"
+ "_$s23SiriReferenceResolution0bC6ClientC22collectSalientEntities10completionyys6ResultOySay0abC9DataModel11RRCandidateVGs5Error_pGc_tFTj"
+ "_$s23SiriReferenceResolution0bC6ClientC22collectSalientEntities6filter10completiony0abC9DataModel8RRFilterVSg_ys6ResultOySayAG11RRCandidateVGs5Error_pGctFTj"
+ "_$s23SiriReferenceResolution0bC6ClientC23retrieveSalientEntities6filters6ResultOySay0abC9DataModel11RRCandidateVGs5Error_pGAH8RRFilterVSg_tFTj"
+ "_$s23SiriReferenceResolution0bC6ClientC23retrieveSalientEntitiess6ResultOySay0abC9DataModel11RRCandidateVGs5Error_pGyFTj"
+ "_$s23SiriReferenceResolution0bC6ClientC7resolve5query6filters6ResultOy0abC9DataModel8RRResultOs5Error_pGAI12ResolveQueryC_AI8RRFilterVSgtFTj"
+ "_$s23SiriReferenceResolution0bC6ClientC7resolve9reference6filters6ResultOy0abC9DataModel8RRResultOs5Error_pGAI7RRQueryO_AI8RRFilterVSgtFTj"
+ "_$s23SiriReferenceResolution0bC6ClientC7resolve9references6ResultOy0abC9DataModel8RRResultOs5Error_pGAH7RRQueryO_tFTj"
+ "_$s23SiriReferenceResolution0bC6ClientC9inRequest9requestIdy10Foundation4UUIDV_tFTj"
+ "_$s23SiriReferenceResolution0bC6ClientCACycfC"
+ "_$s23SiriReferenceResolution0bC6ClientCMa"
+ "_$s23SiriReferenceResolution0bC6ClientCMn"
+ "_$s23SiriReferenceResolution18RRResolverProtocolMp"
+ "_$s23SiriReferenceResolution18RRResolverProtocolP18retrieveEntityType5querys6ResultOy0abC9DataModel8RRResultOs5Error_pGAH12ResolveQueryC_tFTj"
+ "_$s23SiriReferenceResolution18RRResolverProtocolP18retrieveEntityType5querys6ResultOy0abC9DataModel8RRResultOs5Error_pGAH12ResolveQueryC_tFTq"
+ "_$s23SiriReferenceResolution18RRResolverProtocolP7resolve9references6ResultOy0abC9DataModel8RRResultOs5Error_pGAH7RRQueryO_tFTj"
+ "_$s23SiriReferenceResolution18RRResolverProtocolP7resolve9references6ResultOy0abC9DataModel8RRResultOs5Error_pGAH7RRQueryO_tFTq"
+ "_$s23SiriReferenceResolution18RRResolverProtocolPAAE18retrieveEntityType5querys6ResultOy0abC9DataModel8RRResultOs5Error_pGAH12ResolveQueryC_tF"
+ "_$s23SiriReferenceResolution27RRReferenceResolverProtocolMp"
+ "_$s23SiriReferenceResolution27RRReferenceResolverProtocolP03hasB09usoEntitySb0A8Ontology03UsoI0C_tFTj"
+ "_$s23SiriReferenceResolution27RRReferenceResolverProtocolP03hasB09usoEntitySb0A8Ontology03UsoI0C_tFTq"
+ "_$s23SiriReferenceResolution27RRReferenceResolverProtocolP18retrieveEntityType5querys6ResultOy0abC9DataModel8RRResultOs5Error_pGAH12ResolveQueryC_tFTj"
+ "_$s23SiriReferenceResolution27RRReferenceResolverProtocolP18retrieveEntityType5querys6ResultOy0abC9DataModel8RRResultOs5Error_pGAH12ResolveQueryC_tFTq"
+ "_$s23SiriReferenceResolution27RRReferenceResolverProtocolP7resolve5querys6ResultOy0abC9DataModel8RRResultOs5Error_pGAH12ResolveQueryC_tFTj"
+ "_$s23SiriReferenceResolution27RRReferenceResolverProtocolP7resolve5querys6ResultOy0abC9DataModel8RRResultOs5Error_pGAH12ResolveQueryC_tFTq"
+ "_$s23SiriReferenceResolution27RRReferenceResolverProtocolP7resolve9references6ResultOy0abC9DataModel8RRResultOs5Error_pGAH7RRQueryO_tFTj"
+ "_$s23SiriReferenceResolution27RRReferenceResolverProtocolP7resolve9references6ResultOy0abC9DataModel8RRResultOs5Error_pGAH7RRQueryO_tFTq"
+ "_$s23SiriReferenceResolution27RRReferenceResolverProtocolPAAE18retrieveEntityType5querys6ResultOy0abC9DataModel8RRResultOs5Error_pGAH12ResolveQueryC_tF"
+ "_$s23SiriReferenceResolution27RRReferenceResolverProtocolPAAE7resolve5querys6ResultOy0abC9DataModel8RRResultOs5Error_pGAH12ResolveQueryC_tF"
+ "_$s23SiriReferenceResolution27SalientEntitiesDataProviderC07salientE0Say0abcF5Model11RRCandidateVGvgTj"
+ "_$s23SiriReferenceResolution27SalientEntitiesDataProviderC07salientE0Say0abcF5Model11RRCandidateVGvsTj"
+ "_$sSS23SiriReferenceResolutionE9md5StringSSSgvg"
+ "_METACLASS_$_SKIVoiceShortcutsInvocation"
+ "_OBJC_CLASS_$_RRSchemaProvisionalPullerStarted"
+ "_OBJC_CLASS_$_SFAdjustedImageView"
+ "_OBJC_CLASS_$_SFAirDropActivityViewController"
+ "_OBJC_CLASS_$_SFAirDropDiscoveryController"
+ "_OBJC_CLASS_$_SFAirDropMagicHeadViewController"
+ "_OBJC_CLASS_$_SFAirDropPayload"
+ "_OBJC_CLASS_$_SFAirDropViewController"
+ "_OBJC_CLASS_$_SFAppContent"
+ "_OBJC_CLASS_$_SFB332SetupObserver"
+ "_OBJC_CLASS_$_SFCAPackageView"
+ "_OBJC_CLASS_$_SFCircleProgressView"
+ "_OBJC_CLASS_$_SFHighlightButton"
+ "_OBJC_CLASS_$_SFMediaPlayerItem"
+ "_OBJC_CLASS_$_SFMediaPlayerView"
+ "_OBJC_CLASS_$_SFPersonCollectionViewCell"
+ "_OBJC_CLASS_$_SFPersonImageView"
+ "_OBJC_CLASS_$_SFRenderingCommand"
+ "_OBJC_CLASS_$_SFShareAudioViewController"
+ "_OBJC_CLASS_$_SFShareSheetRendering"
+ "_OBJC_CLASS_$_SFSharedAudioDeviceInfo"
+ "_OBJC_CLASS_$_SFUIAvatarImageRenderer"
+ "_OBJC_CLASS_$_SFUIAvatarImageRenderingScope"
+ "_OBJC_CLASS_$_SFUIImageProvider"
+ "_OBJC_CLASS_$_SFUIPeopleSuggestionImageProvider"
+ "_OBJC_CLASS_$_SFUITTRReporter"
+ "_OBJC_METACLASS_$_SFAdjustedImageView"
+ "_OBJC_METACLASS_$_SFAirDropActivityViewController"
+ "_OBJC_METACLASS_$_SFAirDropDiscoveryController"
+ "_OBJC_METACLASS_$_SFAirDropMagicHeadViewController"
+ "_OBJC_METACLASS_$_SFAirDropPayload"
+ "_OBJC_METACLASS_$_SFAirDropViewController"
+ "_OBJC_METACLASS_$_SFAppContent"
+ "_OBJC_METACLASS_$_SFB332SetupObserver"
+ "_OBJC_METACLASS_$_SFCAPackageView"
+ "_OBJC_METACLASS_$_SFCircleProgressView"
+ "_OBJC_METACLASS_$_SFHighlightButton"
+ "_OBJC_METACLASS_$_SFMediaPlayerItem"
+ "_OBJC_METACLASS_$_SFMediaPlayerView"
+ "_OBJC_METACLASS_$_SFPersonCollectionViewCell"
+ "_OBJC_METACLASS_$_SFPersonImageView"
+ "_OBJC_METACLASS_$_SFRenderingCommand"
+ "_OBJC_METACLASS_$_SFShareAudioViewController"
+ "_OBJC_METACLASS_$_SFShareSheetRendering"
+ "_OBJC_METACLASS_$_SFSharedAudioDeviceInfo"
+ "_OBJC_METACLASS_$_SFUIActivityImageProvider"
+ "_OBJC_METACLASS_$_SFUIAvatarImageRenderer"
+ "_OBJC_METACLASS_$_SFUIAvatarImageRenderingScope"
+ "_OBJC_METACLASS_$_SFUIPeopleSuggestionImageProvider"
+ "_OBJC_METACLASS_$_SFUITTRReporter"
+ "__Z11CreateErrorNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEl"
+ "__ZN20CommandDriverFactory11setRegistryENSt3__110shared_ptrI8RegistryEE"
+ "__ZN20CommandDriverFactory21create_default_globalEv"
+ "__ZN20CommandDriverFactoryC2Ev"
+ "__ZN3awd10AppContext10setHandlerEN8dispatch5blockIU13block_pointerFvNS_10MetricInfoENS_11TriggerInfoEEEE"
+ "__ZN3awd10AppContext10setHandlerEN8dispatch5blockIU13block_pointerFvNS_10MetricInfoEjNSt3__16vectorIhNS4_9allocatorIhEEEEEEE"
+ "__ZN3awd10AppContext10setHandlerEN8dispatch5blockIU13block_pointerFvNS_11ClientStateEEEE"
+ "__ZN3awd10AppContext13setPropertiesERKNS_13AppPropertiesE"
+ "__ZN3awd16AwdCommandDriver7checkInENSt3__110shared_ptrINS_10AppContextEEE"
+ "__ZN3awd16AwdCommandDriverC2ENSt3__110shared_ptrIN3ctu9LogServerEEENS2_I8RegistryEE"
+ "__ZN3awd16AwdCommandDriverD2Ev"
+ "__ZN3awd8asStringENS_11ClientStateE"
+ "__ZN3awd8asStringENS_11PayloadTypeE"
+ "__ZN3awd8asStringENS_5AppIDE"
+ "__ZN3awd8asStringERKNS_10MetricInfoE"
+ "__ZN3awd8asStringERKNS_11TriggerInfoE"
+ "__ZN4coex13CommandDriverC2ENSt3__110shared_ptrIN3ctu9LogServerEEENS2_I8RegistryEE"
+ "__ZN4coex4util14data_to_uint64EN3ctu2cf11CFSharedRefIK8__CFDataEE"
+ "__ZN4cpms13CommandDriverC2ENSt3__110shared_ptrI8RegistryEE"
+ "__ZN4data13CommandDriverC2ENSt3__110shared_ptrIN3ctu9LogServerEEENS2_I8RegistryEE"
+ "__ZN4logs13CommandDriverC2ENSt3__110shared_ptrIN3ctu9LogServerEEEN8dispatch8callbackIU13block_pointerFvNS_15CollectionStateEEEENS7_IU13block_pointerFvNS2_INS1_6vectorIhNS1_9allocatorIhEEEEEEbEEENS3_2cf11CFSharedRefIK14__CFDictionaryEENS1_12basic_stringIcNS1_11char_traitsIcEENSD_IcEEEENS2_I8RegistryEE"
+ "__ZN5radio10asStringV2ERKNS_24FactoryCalibrationStatusE"
+ "__ZN5radio13CommandDriver14getSimSlotInfoERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE"
+ "__ZN5radio13CommandDriver16watchClientStateEN8dispatch8callbackIU13block_pointerFvN3ctu2cf11CFSharedRefI9__CFErrorEENS5_IK14__CFDictionaryEEEEE"
+ "__ZN5radio13CommandDriver18watchOperatingModeEN8dispatch8callbackIU13block_pointerFvN3ctu2cf11CFSharedRefI9__CFErrorEENS5_IK14__CFDictionaryEEEEE"
+ "__ZN5radio13CommandDriver29handleClientStateChanged_syncEb"
+ "__ZN5radio13CommandDriver31handleOperatingModeChanged_syncENS_13OperatingModeE"
+ "__ZN5radio13CommandDriverC2ENSt3__110shared_ptrIN3ctu9LogServerEEEN8dispatch8workloopENS2_I8RegistryEE"
+ "__ZN5radio15RFCalibration_t4fillEN3ctu2cf11CFSharedRefIK14__CFDictionaryEE"
+ "__ZN5radio15RFCalibration_t8toStringEv"
+ "__ZN5radio15RFCalibration_tC1Ev"
+ "__ZN5radio16RFSCommandDriverC2ENSt3__110shared_ptrIN3ctu9LogServerEEENS2_I8RegistryEE"
+ "__ZN5radio16RFSCommandDriverD2Ev"
+ "__ZN5radio18BasebandProperties6createEN3ctu2cf11CFSharedRefIK14__CFDictionaryEE"
+ "__ZN5radio18BasebandProperties6toDictEv"
+ "__ZN5radio18DebugCommandDriverC2ENSt3__110shared_ptrIN3ctu9LogServerEEENS2_I8RegistryEE"
+ "__ZN5radio6OpMode6createEv"
+ "__ZN5radio6OpMode7setModeEh"
+ "__ZN5radio6OpMode9setConfigEt"
+ "__ZN5radio8asStringERKNS_13IssueCategoryE"
+ "__ZN5radio8asStringERKNS_24FactoryCalibrationStatusE"
+ "__ZN7desense13CommandDriverC2ENSt3__110shared_ptrIN3ctu9LogServerEEENS2_I8RegistryEE"
+ "__ZN7desense8asStringENS_22FrequencyReportingModeE"
+ "__ZNK3awd10AppContext13getPropertiesEv"
+ "__ZNK3awd10AppContext8getAppIDEv"
+ "__ZNK3awd10AppContextclEN8dispatch5blockIU13block_pointerFvbEEEb"
+ "__ZNK3awd10AppContextclENS_10MetricInfoENS_11TriggerInfoE"
+ "__ZNK3awd10AppContextclENS_10MetricInfoEjNSt3__16vectorIhNS2_9allocatorIhEEEE"
+ "__ZNK3awd10AppContextclENS_10MetricInfoEt"
+ "__ZNK3awd16AwdCommandDriver19broadcastState_syncENS_11ClientStateE"
+ "__ZNK3awd16AwdCommandDriver7getNameEv"
+ "__ZNK4coex13CommandDriver7getNameEv"
+ "__ZNK4cpms13CommandDriver7getNameEv"
+ "__ZNK4data13CommandDriver7getNameEv"
+ "__ZNK4diag13CommandDriver18notifyOfEvent_syncENS0_5EventEN8dispatch13group_sessionE"
+ "__ZNK4diag13CommandDriver7getNameEv"
+ "__ZNK4logs13CommandDriver7getNameEv"
+ "__ZNK5radio13CommandDriver7getNameEv"
+ "__ZNK5radio16RFSCommandDriver7getNameEv"
+ "__ZNK5radio18DebugCommandDriver7getNameEv"
+ "__ZNK5radio6OpMode11convertModeENS_13OperatingModeE"
+ "__ZNK5radio6OpMode11convertModeEh"
+ "__ZNK5radio6OpMode12modeToStringENS_13OperatingModeE"
+ "__ZNK5radio6OpMode13getModeStringEv"
+ "__ZNK5radio6OpMode15allowModeChangeEv"
+ "__ZNK5radio6OpMode15getConfigStringEv"
+ "__ZNK5radio6OpMode7getModeEv"
+ "__ZNK5radio6OpMode9getConfigEv"
+ "__ZNK7desense13CommandDriver7getNameEv"
+ "olveQueryC_tFTj"
+ "ommandDriverC2ENSt3__110shared_ptrIN3ctu9LogServerEEEN8dispatch8callbackIU13block_pointerFvNS0_5EventENS6_13group_sessionEEEENS2_I8RegistryEE"
+ "vider"

```
