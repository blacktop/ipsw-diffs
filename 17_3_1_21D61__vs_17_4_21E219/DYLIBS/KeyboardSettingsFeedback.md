## KeyboardSettingsFeedback

> `/System/Library/PrivateFrameworks/KeyboardSettingsFeedback.framework/KeyboardSettingsFeedback`

```diff

-7302.0.0.0.0
-  __TEXT.__text: 0x3d94
-  __TEXT.__auth_stubs: 0x610
-  __TEXT.__objc_methlist: 0x25c
-  __TEXT.__const: 0x1ee
-  __TEXT.__cstring: 0x9f0
+7439.0.0.0.0
+  __TEXT.__text: 0x223c
+  __TEXT.__auth_stubs: 0x2d0
+  __TEXT.__objc_methlist: 0x2ac
+  __TEXT.__const: 0x50
+  __TEXT.__cstring: 0x5dd
   __TEXT.__oslogstring: 0x3
-  __TEXT.__swift5_typeref: 0xa8
-  __TEXT.__swift5_reflstr: 0x11c
-  __TEXT.__swift5_assocty: 0x18
-  __TEXT.__constg_swiftt: 0x168
-  __TEXT.__swift5_fieldmd: 0xd8
-  __TEXT.__swift5_builtin: 0x14
-  __TEXT.__swift5_capture: 0x10
-  __TEXT.__swift5_proto: 0xc
-  __TEXT.__swift5_types: 0x10
-  __TEXT.__unwind_info: 0x16c
-  __TEXT.__objc_classname: 0x29
-  __TEXT.__objc_methname: 0xb4a
-  __TEXT.__objc_methtype: 0xe7
-  __TEXT.__objc_stubs: 0x760
-  __DATA_CONST.__got: 0x70
-  __DATA_CONST.__const: 0x1d0
-  __DATA_CONST.__objc_classlist: 0x28
-  __DATA_CONST.__objc_protolist: 0x8
+  __TEXT.__unwind_info: 0xbc
+  __TEXT.__objc_classname: 0x34
+  __TEXT.__objc_methname: 0xc49
+  __TEXT.__objc_methtype: 0xc6
+  __TEXT.__objc_stubs: 0xa00
+  __DATA_CONST.__got: 0x18
+  __DATA_CONST.__const: 0xe8
+  __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x600
-  __DATA_CONST.__objc_selrefs: 0x238
-  __AUTH_CONST.__objc_const: 0x120
-  __AUTH_CONST.__cfstring: 0x3a0
-  __AUTH_CONST.__const: 0x120
-  __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH_CONST.__auth_got: 0x310
-  __AUTH.__objc_data: 0x270
-  __AUTH.__data: 0x178
-  __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_classrefs: 0x68
-  __DATA.__objc_superrefs: 0x8
-  __DATA.__objc_ivar: 0x30
-  __DATA.__objc_data: 0xb8
-  __DATA.__data: 0xd8
-  __DATA.__bss: 0x1c0
-  __DATA.__common: 0x20
+  __DATA_CONST.__objc_const: 0x458
+  __DATA_CONST.__objc_selrefs: 0x2b8
+  __DATA_CONST.__objc_classrefs: 0x70
+  __DATA_CONST.__objc_superrefs: 0x10
+  __DATA_CONST.__objc_arraydata: 0x58
+  __AUTH_CONST.__cfstring: 0x500
+  __AUTH_CONST.__const: 0x60
+  __AUTH_CONST.__objc_intobj: 0x120
+  __AUTH_CONST.__objc_arrayobj: 0x18
+  __AUTH_CONST.__objc_const: 0xd8
+  __AUTH_CONST.__auth_got: 0x170
+  __AUTH.__objc_data: 0xa0
+  __DATA.__objc_ivar: 0x54
+  __DATA.__bss: 0x30
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/UIKit.framework/UIKit
-  - /System/Library/PrivateFrameworks/Feedback.framework/Feedback
+  - /System/Library/PrivateFrameworks/FeedbackService.framework/FeedbackService
   - /System/Library/PrivateFrameworks/TextInput.framework/TextInput
-  - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  - /usr/lib/swift/libswiftAVFoundation.dylib
-  - /usr/lib/swift/libswiftAccelerate.dylib
-  - /usr/lib/swift/libswiftCompression.dylib
-  - /usr/lib/swift/libswiftCore.dylib
-  - /usr/lib/swift/libswiftCoreAudio.dylib
-  - /usr/lib/swift/libswiftCoreFoundation.dylib
-  - /usr/lib/swift/libswiftCoreImage.dylib
-  - /usr/lib/swift/libswiftCoreLocation.dylib
-  - /usr/lib/swift/libswiftCoreMIDI.dylib
-  - /usr/lib/swift/libswiftCoreMedia.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
-  - /usr/lib/swift/libswiftDataDetection.dylib
-  - /usr/lib/swift/libswiftDispatch.dylib
-  - /usr/lib/swift/libswiftFileProvider.dylib
-  - /usr/lib/swift/libswiftMetal.dylib
-  - /usr/lib/swift/libswiftOSLog.dylib
-  - /usr/lib/swift/libswiftObjectiveC.dylib
-  - /usr/lib/swift/libswiftQuartzCore.dylib
-  - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
-  - /usr/lib/swift/libswiftXPC.dylib
-  - /usr/lib/swift/libswiftos.dylib
-  - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 1D063A34-4E17-3922-AA5C-C9C22011D019
-  Functions: 121
-  Symbols:   394
-  CStrings:  216
+  UUID: 2178264B-0F96-3D2A-9EBA-275D9F1B7275
+  Functions: 72
+  Symbols:   354
+  CStrings:  240
 
Symbols:
+ +[TUIFeedbackController getFormIdentifier]
+ -[TUIFeedbackSurveyMetadata .cxx_destruct]
+ -[TUIFeedbackSurveyMetadata build]
+ -[TUIFeedbackSurveyMetadata duration]
+ -[TUIFeedbackSurveyMetadata finalInputModes]
+ -[TUIFeedbackSurveyMetadata finalPreferenceValue]
+ -[TUIFeedbackSurveyMetadata finalTimestamp]
+ -[TUIFeedbackSurveyMetadata initWithBuild:model:language:region:initialPreferenceValue:initialInputModes:initialTimestamp:finalPreferenceValue:finalInputModes:finalTimestamp:]
+ -[TUIFeedbackSurveyMetadata initialInputModes]
+ -[TUIFeedbackSurveyMetadata initialPreferenceValue]
+ -[TUIFeedbackSurveyMetadata initialTimestamp]
+ -[TUIFeedbackSurveyMetadata language]
+ -[TUIFeedbackSurveyMetadata model]
+ -[TUIFeedbackSurveyMetadata region]
+ -[TUIFeedbackSurveyMetadata setBuild:]
+ -[TUIFeedbackSurveyMetadata setFinalInputModes:]
+ -[TUIFeedbackSurveyMetadata setFinalPreferenceValue:]
+ -[TUIFeedbackSurveyMetadata setFinalTimestamp:]
+ -[TUIFeedbackSurveyMetadata setInitialInputModes:]
+ -[TUIFeedbackSurveyMetadata setInitialPreferenceValue:]
+ -[TUIFeedbackSurveyMetadata setInitialTimestamp:]
+ -[TUIFeedbackSurveyMetadata setLanguage:]
+ -[TUIFeedbackSurveyMetadata setModel:]
+ -[TUIFeedbackSurveyMetadata setRegion:]
+ _OBJC_CLASS_$_FBKSDraftLauncher
+ _OBJC_CLASS_$_FBKSFeedbackCount
+ _OBJC_CLASS_$_FBKSForm
+ _OBJC_CLASS_$_FBKSLaunchConfiguration
+ _OBJC_CLASS_$_NSConstantArray
+ _OBJC_CLASS_$_TIFeedbackUtil
+ _OBJC_CLASS_$_TUIFeedbackSurveyMetadata
+ _OBJC_IVAR_$_TUIFeedbackSurveyMetadata._build
+ _OBJC_IVAR_$_TUIFeedbackSurveyMetadata._finalInputModes
+ _OBJC_IVAR_$_TUIFeedbackSurveyMetadata._finalPreferenceValue
+ _OBJC_IVAR_$_TUIFeedbackSurveyMetadata._finalTimestamp
+ _OBJC_IVAR_$_TUIFeedbackSurveyMetadata._initialInputModes
+ _OBJC_IVAR_$_TUIFeedbackSurveyMetadata._initialPreferenceValue
+ _OBJC_IVAR_$_TUIFeedbackSurveyMetadata._initialTimestamp
+ _OBJC_IVAR_$_TUIFeedbackSurveyMetadata._language
+ _OBJC_IVAR_$_TUIFeedbackSurveyMetadata._model
+ _OBJC_IVAR_$_TUIFeedbackSurveyMetadata._region
+ _OBJC_METACLASS_$_TUIFeedbackSurveyMetadata
+ _OUTLINED_FUNCTION_3
+ _UIKeyboardInputModeGetLanguageWithRegion
+ __OBJC_$_INSTANCE_METHODS_TUIFeedbackSurveyMetadata
+ __OBJC_$_INSTANCE_VARIABLES_TUIFeedbackSurveyMetadata
+ __OBJC_$_PROP_LIST_TUIFeedbackSurveyMetadata
+ __OBJC_CLASS_RO_$_TUIFeedbackSurveyMetadata
+ __OBJC_METACLASS_RO_$_TUIFeedbackSurveyMetadata
+ ___78-[TUIFeedbackController _presentSurveyWithParentController:completionHandler:]_block_invoke.196
+ ___78-[TUIFeedbackController _presentSurveyWithParentController:completionHandler:]_block_invoke.cold.1
+ ___78-[TUIFeedbackController _presentSurveyWithParentController:completionHandler:]_block_invoke.cold.2
+ ___78-[TUIFeedbackController _presentSurveyWithParentController:completionHandler:]_block_invoke.cold.3
+ ___block_descriptor_40_8_32bs_e17_v16?0"NSError"8ls32l8
+ ___block_descriptor_48_8_32s_e20_v24?0q8"NSError"16ls32l8
+ ___block_descriptor_56_8_32s40s48bs_e39_v24?0"FBKSFeedbackCount"8"NSError"16ls48l8s32l8s40l8
+ ___block_literal_global.225
+ ___block_literal_global.230
+ __unnamed_array_storage
+ _objc_msgSend$collectFeedbackWithLaunchConfiguration:completion:
+ _objc_msgSend$currentCampaign
+ _objc_msgSend$duration
+ _objc_msgSend$fetchCountsForFormWithIdentifier:completion:
+ _objc_msgSend$getFormIdentifier
+ _objc_msgSend$getStudyLanguageAndRegion
+ _objc_msgSend$initWithFeedbackForm:
+ _objc_msgSend$initWithIdentifier:
+ _objc_msgSend$intValue
+ _objc_msgSend$length
+ _objc_msgSend$prefill:answer:
+ _objc_msgSend$setAuthenticationMethod:
+ _objc_msgSend$setBuild:
+ _objc_msgSend$setFinalInputModes:
+ _objc_msgSend$setFinalPreferenceValue:
+ _objc_msgSend$setFinalTimestamp:
+ _objc_msgSend$setInitialInputModes:
+ _objc_msgSend$setInitialPreferenceValue:
+ _objc_msgSend$setInitialTimestamp:
+ _objc_msgSend$setLanguage:
+ _objc_msgSend$setLocalizedAlertViewDeclineButtonTitle:
+ _objc_msgSend$setLocalizedAlertViewProceedButtonTitle:
+ _objc_msgSend$setLocalizedPromptMessage:
+ _objc_msgSend$setLocalizedPromptTitle:
+ _objc_msgSend$setModel:
+ _objc_msgSend$setPromptStyle:
+ _objc_msgSend$setRegion:
+ _objc_msgSend$stringByReplacingOccurrencesOfString:withString:
+ _objc_msgSend$timeIntervalSinceDate:
+ _objc_opt_respondsToSelector
+ _objc_setProperty_nonatomic_copy
- +[TUIFeedbackAlert messageWithTitle:message:actionLabel:parentController:completion:]
- +[TUIFeedbackAlert promptWithTitle:message:acceptActionLabel:declineActionLabel:parentController:completion:]
- -[TUIFeedbackController feedbackSurveyPresenter]
- -[TUIFeedbackController shouldCompleteStudyWithPreferenceValue:].cold.4
- _OBJC_CLASS_$_TUIFeedbackAlert
- _OBJC_CLASS_$_UIAlertAction
- _OBJC_CLASS_$_UIAlertController
- _OBJC_CLASS_$__TtC24KeyboardSettingsFeedback25TUIFeedbackSurveyMetadata
- _OBJC_CLASS_$__TtC24KeyboardSettingsFeedback26TUIFeedbackSurveyPresenter
- _OBJC_CLASS_$__TtCs12_SwiftObject
- _OBJC_IVAR_$_TUIFeedbackController._feedbackSurveyPresenter
- _OBJC_METACLASS_$_TUIFeedbackAlert
- _OBJC_METACLASS_$__TtC24KeyboardSettingsFeedback25TUIFeedbackSurveyMetadata
- _OBJC_METACLASS_$__TtC24KeyboardSettingsFeedback26TUIFeedbackSurveyPresenter
- _OBJC_METACLASS_$__TtCs12_SwiftObject
- _UIKeyboardInputModeGetLanguage
- __Block_copy
- __Block_release
- __DATA__TtC24KeyboardSettingsFeedback25TUIFeedbackSurveyMetadata
- __DATA__TtC24KeyboardSettingsFeedback26TUIFeedbackSurveyPresenter
- __DATA__TtC24KeyboardSettingsFeedbackP33_A8D87A2BC67C5811F046956486A724BD23FeedbackSurveyPresenter
- __IVARS__TtC24KeyboardSettingsFeedback25TUIFeedbackSurveyMetadata
- __IVARS__TtC24KeyboardSettingsFeedback26TUIFeedbackSurveyPresenter
- __IVARS__TtC24KeyboardSettingsFeedbackP33_A8D87A2BC67C5811F046956486A724BD23FeedbackSurveyPresenter
- __METACLASS_DATA__TtC24KeyboardSettingsFeedback25TUIFeedbackSurveyMetadata
- __METACLASS_DATA__TtC24KeyboardSettingsFeedback26TUIFeedbackSurveyPresenter
- __METACLASS_DATA__TtC24KeyboardSettingsFeedbackP33_A8D87A2BC67C5811F046956486A724BD23FeedbackSurveyPresenter
- __OBJC_$_CLASS_METHODS_TUIFeedbackAlert
- __OBJC_$_INSTANCE_METHODS__TtC24KeyboardSettingsFeedback25TUIFeedbackSurveyMetadata
- __OBJC_$_INSTANCE_METHODS__TtC24KeyboardSettingsFeedback26TUIFeedbackSurveyPresenter
- __OBJC_$_INSTANCE_METHODS__TtC24KeyboardSettingsFeedbackP33_A8D87A2BC67C5811F046956486A724BD23FeedbackSurveyPresenter
- __OBJC_CLASS_RO_$_TUIFeedbackAlert
- __OBJC_METACLASS_RO_$_TUIFeedbackAlert
- __PROTOCOLS__TtC24KeyboardSettingsFeedbackP33_A8D87A2BC67C5811F046956486A724BD23FeedbackSurveyPresenter
- __PROTOCOLS__TtC24KeyboardSettingsFeedbackP33_A8D87A2BC67C5811F046956486A724BD23FeedbackSurveyPresenter.4
- __PROTOCOL_INSTANCE_METHODS_OPT__TtP8Feedback38FBKFeedbackDraftViewControllerDelegate_
- __PROTOCOL_INSTANCE_METHODS__TtP8Feedback38FBKFeedbackDraftViewControllerDelegate_
- __PROTOCOL_METHOD_TYPES__TtP8Feedback38FBKFeedbackDraftViewControllerDelegate_
- __PROTOCOL__TtP8Feedback38FBKFeedbackDraftViewControllerDelegate_
- ___109+[TUIFeedbackAlert promptWithTitle:message:acceptActionLabel:declineActionLabel:parentController:completion:]_block_invoke
- ___109+[TUIFeedbackAlert promptWithTitle:message:acceptActionLabel:declineActionLabel:parentController:completion:]_block_invoke_2
- ___78-[TUIFeedbackController _presentSurveyWithParentController:completionHandler:]_block_invoke_2
- ___85+[TUIFeedbackAlert messageWithTitle:message:actionLabel:parentController:completion:]_block_invoke
- ___block_descriptor_40_8_32bs_e23_v16?0"UIAlertAction"8ls32l8
- ___block_descriptor_48_8_32s_e21_v24?0q8"NSString"16ls32l8
- ___block_descriptor_56_8_32s40s48bs_e21_v24?0q8"NSString"16ls32l8s40l8s48l8
- ___block_descriptor_64_8_32s40s48s56bs_e8_v16?0q8ls32l8s40l8s48l8s56l8
- ___block_literal_global.94
- ___block_literal_global.99
- ___chkstk_darwin
- ___swift_instantiateConcreteTypeFromMangledName
- ___swift_reflection_version
- __swiftEmptyArrayStorage
- __swiftEmptyDictionarySingleton
- __swift_FORCE_LOAD_$_swiftAVFoundation
- __swift_FORCE_LOAD_$_swiftAVFoundation_$_KeyboardSettingsFeedback
- __swift_FORCE_LOAD_$_swiftAccelerate
- __swift_FORCE_LOAD_$_swiftAccelerate_$_KeyboardSettingsFeedback
- __swift_FORCE_LOAD_$_swiftCompression
- __swift_FORCE_LOAD_$_swiftCompression_$_KeyboardSettingsFeedback
- __swift_FORCE_LOAD_$_swiftCoreAudio
- __swift_FORCE_LOAD_$_swiftCoreAudio_$_KeyboardSettingsFeedback
- __swift_FORCE_LOAD_$_swiftCoreFoundation
- __swift_FORCE_LOAD_$_swiftCoreFoundation_$_KeyboardSettingsFeedback
- __swift_FORCE_LOAD_$_swiftCoreGraphics
- __swift_FORCE_LOAD_$_swiftCoreGraphics_$_KeyboardSettingsFeedback
- __swift_FORCE_LOAD_$_swiftCoreImage
- __swift_FORCE_LOAD_$_swiftCoreImage_$_KeyboardSettingsFeedback
- __swift_FORCE_LOAD_$_swiftCoreLocation
- __swift_FORCE_LOAD_$_swiftCoreLocation_$_KeyboardSettingsFeedback
- __swift_FORCE_LOAD_$_swiftCoreMIDI
- __swift_FORCE_LOAD_$_swiftCoreMIDI_$_KeyboardSettingsFeedback
- __swift_FORCE_LOAD_$_swiftCoreMedia
- __swift_FORCE_LOAD_$_swiftCoreMedia_$_KeyboardSettingsFeedback
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swiftDarwin_$_KeyboardSettingsFeedback
- __swift_FORCE_LOAD_$_swiftDataDetection
- __swift_FORCE_LOAD_$_swiftDataDetection_$_KeyboardSettingsFeedback
- __swift_FORCE_LOAD_$_swiftDispatch
- __swift_FORCE_LOAD_$_swiftDispatch_$_KeyboardSettingsFeedback
- __swift_FORCE_LOAD_$_swiftFileProvider
- __swift_FORCE_LOAD_$_swiftFileProvider_$_KeyboardSettingsFeedback
- __swift_FORCE_LOAD_$_swiftFoundation
- __swift_FORCE_LOAD_$_swiftFoundation_$_KeyboardSettingsFeedback
- __swift_FORCE_LOAD_$_swiftMetal
- __swift_FORCE_LOAD_$_swiftMetal_$_KeyboardSettingsFeedback
- __swift_FORCE_LOAD_$_swiftOSLog
- __swift_FORCE_LOAD_$_swiftOSLog_$_KeyboardSettingsFeedback
- __swift_FORCE_LOAD_$_swiftObjectiveC
- __swift_FORCE_LOAD_$_swiftObjectiveC_$_KeyboardSettingsFeedback
- __swift_FORCE_LOAD_$_swiftQuartzCore
- __swift_FORCE_LOAD_$_swiftQuartzCore_$_KeyboardSettingsFeedback
- __swift_FORCE_LOAD_$_swiftUIKit
- __swift_FORCE_LOAD_$_swiftUIKit_$_KeyboardSettingsFeedback
- __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers
- __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers_$_KeyboardSettingsFeedback
- __swift_FORCE_LOAD_$_swiftXPC
- __swift_FORCE_LOAD_$_swiftXPC_$_KeyboardSettingsFeedback
- __swift_FORCE_LOAD_$_swiftos
- __swift_FORCE_LOAD_$_swiftos_$_KeyboardSettingsFeedback
- __swift_FORCE_LOAD_$_swiftsimd
- __swift_FORCE_LOAD_$_swiftsimd_$_KeyboardSettingsFeedback
- __swift_stdlib_reportUnimplementedInitializer
- _associated conformance 24KeyboardSettingsFeedback24TUIFeedbackSurveyOutcomeOSHAASQ
- _objc_allocWithZone
- _objc_msgSend$actionWithTitle:style:handler:
- _objc_msgSend$addAction:
- _objc_msgSend$alertControllerWithTitle:message:preferredStyle:
- _objc_msgSend$feedbackSurveyPresenter
- _objc_msgSend$messageWithTitle:message:actionLabel:parentController:completion:
- _objc_msgSend$presentSurveyWithIdentifier:metadata:parentController:completion:
- _objc_msgSend$presentViewController:animated:completion:
- _objc_msgSend$promptWithTitle:message:acceptActionLabel:declineActionLabel:parentController:completion:
- _objc_opt_self
- _objc_release_x2
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x26
- _objc_retain_x6
- _objc_retain_x7
- _swift_allocObject
- _swift_bridgeObjectRelease
- _swift_bridgeObjectRetain
- _swift_deallocClassInstance
- _swift_deallocObject
- _swift_deletedMethodError
- _swift_getSingletonMetadata
- _swift_getTypeByMangledNameInContext2
- _swift_getWitnessTable
- _swift_initStaticObject
- _swift_release
- _swift_retain
- _swift_updateClassMetadata2
- _symbolic $sSY
- _symbolic SS
- _symbolic SS_ypt
- _symbolic SaySSG
- _symbolic SaySdG
- _symbolic Sb
- _symbolic Si
- _symbolic So8NSObjectC
- _symbolic _____ 10Foundation4DateV
- _symbolic _____ 24KeyboardSettingsFeedback0C15SurveyPresenter33_A8D87A2BC67C5811F046956486A724BDLLC
- _symbolic _____ 24KeyboardSettingsFeedback24TUIFeedbackSurveyOutcomeO
- _symbolic _____ 24KeyboardSettingsFeedback25TUIFeedbackSurveyMetadataC
- _symbolic _____ 24KeyboardSettingsFeedback26TUIFeedbackSurveyPresenterC
- _symbolic _____Sg 8Feedback30FBKFeedbackDraftViewControllerC
- _symbolic _____So8NSStringCSgIeyByy_ 24KeyboardSettingsFeedback24TUIFeedbackSurveyOutcomeO
- _symbolic _____ySSypG s18_DictionaryStorageC
- _symbolic _____ySdG s23_ContiguousArrayStorageC
- _symbolic y______SSSgtcSg 24KeyboardSettingsFeedback24TUIFeedbackSurveyOutcomeO
CStrings:
+ "\v"
+ "\x18"
+ "%ld"
+ "%s Feedback %@: already running a campaign - should not happen"
+ "%s Feedback %@: error getting response from feedback service: %@"
+ "%s Feedback %@: launching survey: %@"
+ "-[TUIFeedbackController _presentSurveyWithParentController:completionHandler:]_block_invoke"
+ "0"
+ "1"
+ ":duration"
+ ":like_purchase"
+ "@\"NSDate\""
+ "B"
+ "T@\"NSArray\",C,N,V_finalInputModes"
+ "T@\"NSArray\",C,N,V_initialInputModes"
+ "T@\"NSDate\",C,N,V_finalTimestamp"
+ "T@\"NSDate\",C,N,V_initialTimestamp"
+ "T@\"NSString\",C,N,V_build"
+ "T@\"NSString\",C,N,V_language"
+ "T@\"NSString\",C,N,V_model"
+ "T@\"NSString\",C,N,V_region"
+ "TB,N,V_finalPreferenceValue"
+ "TB,N,V_initialPreferenceValue"
+ "TUIFeedbackSurveyMetadata"
+ "Yes, no or maybe"
+ "_"
+ "_S02"
+ "_build"
+ "_finalInputModes"
+ "_finalPreferenceValue"
+ "_finalTimestamp"
+ "_initialInputModes"
+ "_initialPreferenceValue"
+ "_initialTimestamp"
+ "_language"
+ "_model"
+ "_region"
+ "collectFeedbackWithLaunchConfiguration:completion:"
+ "currentCampaign"
+ "duration"
+ "esES"
+ "fetchCountsForFormWithIdentifier:completion:"
+ "framework-autocorrect_S02_"
+ "getFormIdentifier"
+ "getStudyLanguageAndRegion"
+ "i"
+ "initWithFeedbackForm:"
+ "initWithIdentifier:"
+ "intValue"
+ "length"
+ "prefill:answer:"
+ "q16@0:8"
+ "setAuthenticationMethod:"
+ "setBuild:"
+ "setFinalInputModes:"
+ "setFinalPreferenceValue:"
+ "setFinalTimestamp:"
+ "setInitialInputModes:"
+ "setInitialPreferenceValue:"
+ "setInitialTimestamp:"
+ "setLanguage:"
+ "setLocalizedAlertViewDeclineButtonTitle:"
+ "setLocalizedAlertViewProceedButtonTitle:"
+ "setLocalizedPromptMessage:"
+ "setLocalizedPromptTitle:"
+ "setModel:"
+ "setPromptStyle:"
+ "setRegion:"
+ "stringByReplacingOccurrencesOfString:withString:"
+ "timeIntervalSinceDate:"
+ "v16@?0@\"NSError\"8"
+ "v20@0:8B16"
+ "v24@?0@\"FBKSFeedbackCount\"8@\"NSError\"16"
+ "v24@?0q8@\"NSError\"16"
- "\f"
- "%s Feedback %@: preferenceEnabled: %d"
- ":framework-autocorrect-korean"
- "@\"_TtC24KeyboardSettingsFeedback26TUIFeedbackSurveyPresenter\""
- "FEEDBACK_OK_ACTION_LABEL"
- "FEEDBACK_SURVEY_DRAFT_ERROR_MESSAGE"
- "KeyboardSettingsFeedback.TUIFeedbackSurveyMetadata"
- "T@\"_TtC24KeyboardSettingsFeedback26TUIFeedbackSurveyPresenter\",R,N,V_feedbackSurveyPresenter"
- "TUIFeedbackAlert"
- "_TtC24KeyboardSettingsFeedback25TUIFeedbackSurveyMetadata"
- "_TtC24KeyboardSettingsFeedback26TUIFeedbackSurveyPresenter"
- "_TtC24KeyboardSettingsFeedbackP33_A8D87A2BC67C5811F046956486A724BD23FeedbackSurveyPresenter"
- "_TtP8Feedback38FBKFeedbackDraftViewControllerDelegate_"
- "_feedbackSurveyPresenter"
- "actionWithTitle:style:handler:"
- "addAction:"
- "alertControllerWithTitle:message:preferredStyle:"
- "completion"
- "dealloc"
- "description"
- "durationBucketingThresholds"
- "feedbackController"
- "feedbackDraftViewController:didCompleteWithFeedbackID:"
- "feedbackDraftViewController:didCompleteWithResponseType:responseID:"
- "feedbackDraftViewController:didFailToAttachURL:error:"
- "feedbackDraftViewController:didFailToStartWithError:"
- "feedbackDraftViewController:didFailToSubmitFeedback:"
- "feedbackDraftViewControllerDidCancel:"
- "feedbackDraftViewControllerDidLoadForm:"
- "feedbackSurveyPresenter"
- "init()"
- "messageWithTitle:message:actionLabel:parentController:completion:"
- "presentSurveyWithIdentifier:metadata:parentController:completion:"
- "presentViewController:animated:completion:"
- "promptWithTitle:message:acceptActionLabel:declineActionLabel:parentController:completion:"
- "surveyPresenter"
- "v16@?0@\"UIAlertAction\"8"
- "v16@?0q8"
- "v24@0:8@\"_TtC8Feedback30FBKFeedbackDraftViewController\"16"
- "v24@?0q8@\"NSString\"16"
- "v32@0:8@\"_TtC8Feedback30FBKFeedbackDraftViewController\"16@\"NSString\"24"
- "v32@0:8@\"_TtC8Feedback30FBKFeedbackDraftViewController\"16@\"_TtC8Feedback18FBKSubmissionError\"24"
- "v32@0:8@\"_TtC8Feedback30FBKFeedbackDraftViewController\"16q24"
- "v32@0:8@16@24"
- "v32@0:8@16q24"
- "v40@0:8@\"_TtC8Feedback30FBKFeedbackDraftViewController\"16@\"NSURL\"24q32"
- "v40@0:8@\"_TtC8Feedback30FBKFeedbackDraftViewController\"16q24@\"NSString\"32"
- "v40@0:8@16@24q32"
- "v40@0:8@16q24@32"
- "v48@0:8@16@24@32@?40"
- "v56@0:8@16@24@32@40@?48"
- "v64@0:8@16@24@32@40@48@?56"

```
