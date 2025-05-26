## KeyboardSettingsFeedback

> `/System/Library/PrivateFrameworks/KeyboardSettingsFeedback.framework/KeyboardSettingsFeedback`

```diff

-7439.0.0.0.0
-  __TEXT.__text: 0x223c
-  __TEXT.__auth_stubs: 0x2d0
-  __TEXT.__objc_methlist: 0x2ac
+7510.0.0.0.0
+  __TEXT.__text: 0x1864
+  __TEXT.__auth_stubs: 0x2c0
+  __TEXT.__objc_methlist: 0x1c4
   __TEXT.__const: 0x50
-  __TEXT.__cstring: 0x5dd
+  __TEXT.__cstring: 0x4b7
   __TEXT.__oslogstring: 0x3
-  __TEXT.__unwind_info: 0xbc
-  __TEXT.__objc_classname: 0x34
-  __TEXT.__objc_methname: 0xc49
-  __TEXT.__objc_methtype: 0xc6
-  __TEXT.__objc_stubs: 0xa00
-  __DATA_CONST.__got: 0x18
-  __DATA_CONST.__const: 0xe8
+  __TEXT.__unwind_info: 0xb0
+  __TEXT.__objc_classname: 0x32
+  __TEXT.__objc_methname: 0x88b
+  __TEXT.__objc_methtype: 0xb8
+  __TEXT.__objc_stubs: 0x7c0
+  __DATA_CONST.__got: 0x10
+  __DATA_CONST.__const: 0x98
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x458
-  __DATA_CONST.__objc_selrefs: 0x2b8
-  __DATA_CONST.__objc_classrefs: 0x70
-  __DATA_CONST.__objc_superrefs: 0x10
+  __DATA_CONST.__objc_const: 0x238
+  __DATA_CONST.__objc_selrefs: 0x248
+  __DATA_CONST.__objc_classrefs: 0x68
+  __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_arraydata: 0x58
-  __AUTH_CONST.__cfstring: 0x500
-  __AUTH_CONST.__const: 0x60
-  __AUTH_CONST.__objc_intobj: 0x120
+  __AUTH_CONST.__cfstring: 0x340
+  __AUTH_CONST.__objc_intobj: 0x108
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_const: 0xd8
-  __AUTH_CONST.__auth_got: 0x170
+  __AUTH_CONST.__const: 0x60
+  __AUTH_CONST.__auth_got: 0x168
   __AUTH.__objc_data: 0xa0
-  __DATA.__objc_ivar: 0x54
+  __DATA.__objc_ivar: 0x28
   __DATA.__bss: 0x30
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 72
-  Symbols:   354
-  CStrings:  200
+  Functions: 51
+  Symbols:   268
+  CStrings:  147
 
Symbols:
+ +[TUIFeedbackController controller]
+ -[TUIFeedbackController _updateStudyDataWithSurveyOutcome:surveyError:initialState:].cold.1
+ _IXAFeedbackLogFacility
+ ___78-[TUIFeedbackController _presentSurveyWithParentController:completionHandler:]_block_invoke.150
+ ___block_literal_global.176
+ ___block_literal_global.181
+ _objc_msgSend$getFeedbackState
+ _objc_msgSend$getFinalInputModes
+ _objc_msgSend$getFinalPreferenceValue
+ _objc_msgSend$getFinalTimestamp
+ _objc_msgSend$getInitialInputModes
+ _objc_msgSend$getInitialPreferenceValue
+ _objc_msgSend$getInitialTimestamp
+ _objc_msgSend$getStudyID
+ _objc_msgSend$getSupportedFeedbackLanguages
+ _objc_msgSend$setFeedbackState:
+ _objc_msgSend$setSurveyOutcome:
- +[TUIFeedbackController controllerWithPreferenceKey:supportedLanguages:]
- +[TUIFeedbackController getFormIdentifier]
- -[TUIFeedbackController .cxx_destruct]
- -[TUIFeedbackController feedbackFeatureEnabledKey]
- -[TUIFeedbackController finalInputModesKey]
- -[TUIFeedbackController finalInputModes]
- -[TUIFeedbackController finalPreferenceValueKey]
- -[TUIFeedbackController finalPreferenceValue]
- -[TUIFeedbackController finalTimestampKey]
- -[TUIFeedbackController finalTimestamp]
- -[TUIFeedbackController initWithPreferenceKey:supportedLanguages:]
- -[TUIFeedbackController initialInputModesKey]
- -[TUIFeedbackController initialInputModes]
- -[TUIFeedbackController initialPreferenceValueKey]
- -[TUIFeedbackController initialPreferenceValue]
- -[TUIFeedbackController initialTimestampKey]
- -[TUIFeedbackController initialTimestamp]
- -[TUIFeedbackController preferenceKey]
- -[TUIFeedbackController shouldCompleteStudyWithPreferenceValue:].cold.3
- -[TUIFeedbackController stateKey]
- -[TUIFeedbackController supportedLanguages]
- -[TUIFeedbackController surveyOutcomeKey]
- _OBJC_CLASS_$_NSNumber
- _OBJC_IVAR_$_TUIFeedbackController._feedbackFeatureEnabledKey
- _OBJC_IVAR_$_TUIFeedbackController._finalInputModesKey
- _OBJC_IVAR_$_TUIFeedbackController._finalPreferenceValueKey
- _OBJC_IVAR_$_TUIFeedbackController._finalTimestampKey
- _OBJC_IVAR_$_TUIFeedbackController._initialInputModesKey
- _OBJC_IVAR_$_TUIFeedbackController._initialPreferenceValueKey
- _OBJC_IVAR_$_TUIFeedbackController._initialTimestampKey
- _OBJC_IVAR_$_TUIFeedbackController._preferenceKey
- _OBJC_IVAR_$_TUIFeedbackController._stateKey
- _OBJC_IVAR_$_TUIFeedbackController._supportedLanguages
- _OBJC_IVAR_$_TUIFeedbackController._surveyOutcomeKey
- _OUTLINED_FUNCTION_3
- _TIFeedbackInitialInputModesDefaultsKeyPrefix
- _TIFeedbackInitialPreferenceValueDefaultsKeyPrefix
- _TIFeedbackInitialTimestampDefaultsKeyPrefix
- _TUIFeedbackFeatureEnabledDefaultsKeyPrefix
- _TUIFeedbackFinalInputModesDefaultsKeyPrefix
- _TUIFeedbackFinalPreferenceValueDefaultsKeyPrefix
- _TUIFeedbackFinalTimestampDefaultsKeyPrefix
- _TUIFeedbackKeyboardDefaultsDomain
- _TUIFeedbackStateDefaultsKeyPrefix
- _TUIFeedbackSurveyOutcomeDefaultsKeyPrefix
- __OBJC_$_INSTANCE_VARIABLES_TUIFeedbackController
- __OBJC_$_PROP_LIST_TUIFeedbackController
- ___78-[TUIFeedbackController _presentSurveyWithParentController:completionHandler:]_block_invoke.196
- ___NSArray0__struct
- ___block_literal_global.225
- ___block_literal_global.230
- _objc_msgSend$copy
- _objc_msgSend$distantFuture
- _objc_msgSend$distantPast
- _objc_msgSend$feedbackFeatureEnabledKey
- _objc_msgSend$finalInputModes
- _objc_msgSend$finalInputModesKey
- _objc_msgSend$finalPreferenceValue
- _objc_msgSend$finalPreferenceValueKey
- _objc_msgSend$finalTimestamp
- _objc_msgSend$finalTimestampKey
- _objc_msgSend$getStudyLanguageAndRegion
- _objc_msgSend$initWithPreferenceKey:supportedLanguages:
- _objc_msgSend$initialInputModes
- _objc_msgSend$initialInputModesKey
- _objc_msgSend$initialPreferenceValueKey
- _objc_msgSend$initialTimestampKey
- _objc_msgSend$integerForKey:
- _objc_msgSend$length
- _objc_msgSend$numberWithBool:
- _objc_msgSend$numberWithInteger:
- _objc_msgSend$objectForKey:
- _objc_msgSend$preferenceKey
- _objc_msgSend$setObject:forKey:
- _objc_msgSend$stateKey
- _objc_msgSend$stringArrayForKey:
- _objc_msgSend$stringByAppendingString:
- _objc_msgSend$stringByReplacingOccurrencesOfString:withString:
- _objc_msgSend$supportedLanguages
- _objc_msgSend$surveyOutcomeKey
- _objc_opt_respondsToSelector
- _objc_retain_x19
CStrings:
+ "controller"
+ "getFeedbackState"
+ "getFinalInputModes"
+ "getFinalPreferenceValue"
+ "getFinalTimestamp"
+ "getInitialInputModes"
+ "getInitialPreferenceValue"
+ "getInitialTimestamp"
+ "getStudyID"
+ "getSupportedFeedbackLanguages"
+ "setFeedbackState:"
+ "setSurveyOutcome:"
- "\v"
- "%s Feedback %@: state: %ld"
- "@32@0:8@16@24"
- "T@\"NSArray\",R,N,V_supportedLanguages"
- "T@\"NSString\",R,N,V_feedbackFeatureEnabledKey"
- "T@\"NSString\",R,N,V_finalInputModesKey"
- "T@\"NSString\",R,N,V_finalPreferenceValueKey"
- "T@\"NSString\",R,N,V_finalTimestampKey"
- "T@\"NSString\",R,N,V_initialInputModesKey"
- "T@\"NSString\",R,N,V_initialPreferenceValueKey"
- "T@\"NSString\",R,N,V_initialTimestampKey"
- "T@\"NSString\",R,N,V_preferenceKey"
- "T@\"NSString\",R,N,V_stateKey"
- "T@\"NSString\",R,N,V_surveyOutcomeKey"
- "_"
- "_S02"
- "_feedbackFeatureEnabledKey"
- "_finalInputModesKey"
- "_finalPreferenceValueKey"
- "_finalTimestampKey"
- "_initialInputModesKey"
- "_initialPreferenceValueKey"
- "_initialTimestampKey"
- "_preferenceKey"
- "_stateKey"
- "_supportedLanguages"
- "_surveyOutcomeKey"
- "controllerWithPreferenceKey:supportedLanguages:"
- "copy"
- "distantFuture"
- "distantPast"
- "esES"
- "feedbackFeatureEnabledKey"
- "feedbackFeatureEnabled_"
- "feedbackFinalInputModes_"
- "feedbackFinalPreferenceValue_"
- "feedbackFinalTimestamp_"
- "feedbackInitialInputModes_"
- "feedbackInitialPreferenceValue_"
- "feedbackInitialTimestamp_"
- "feedbackState_"
- "feedbackSurveyOutcome_"
- "finalInputModesKey"
- "finalPreferenceValueKey"
- "finalTimestampKey"
- "framework-autocorrect_S02_"
- "getStudyLanguageAndRegion"
- "initWithPreferenceKey:supportedLanguages:"
- "initialInputModesKey"
- "initialPreferenceValueKey"
- "initialTimestampKey"
- "integerForKey:"
- "length"
- "numberWithBool:"
- "numberWithInteger:"
- "objectForKey:"
- "preferenceKey"
- "q"
- "setObject:forKey:"
- "stateKey"
- "stringArrayForKey:"
- "stringByAppendingString:"
- "stringByReplacingOccurrencesOfString:withString:"
- "supportedLanguages"
- "surveyOutcomeKey"

```
