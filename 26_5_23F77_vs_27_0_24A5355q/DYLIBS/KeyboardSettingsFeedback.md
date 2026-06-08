## KeyboardSettingsFeedback

> `/System/Library/PrivateFrameworks/KeyboardSettingsFeedback.framework/KeyboardSettingsFeedback`

```diff

-9126.5.5.2.102
-  __TEXT.__text: 0x178c
-  __TEXT.__auth_stubs: 0x280
+9127.0.66.1.102
+  __TEXT.__text: 0x1510
   __TEXT.__objc_methlist: 0x1b4
   __TEXT.__const: 0x58
-  __TEXT.__cstring: 0x4b7
+  __TEXT.__cstring: 0x478
   __TEXT.__oslogstring: 0x3
-  __TEXT.__unwind_info: 0xc8
-  __TEXT.__objc_classname: 0x32
-  __TEXT.__objc_methname: 0x857
-  __TEXT.__objc_methtype: 0xb8
-  __TEXT.__objc_stubs: 0x7a0
-  __DATA_CONST.__got: 0x78
+  __TEXT.__unwind_info: 0xc0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x98
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x240
+  __DATA_CONST.__objc_selrefs: 0x230
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_arraydata: 0x58
-  __AUTH_CONST.__auth_got: 0x148
-  __AUTH_CONST.__const: 0x60
-  __AUTH_CONST.__cfstring: 0x340
+  __DATA_CONST.__got: 0x70
+  __AUTH_CONST.__const: 0x40
+  __AUTH_CONST.__cfstring: 0x2e0
   __AUTH_CONST.__objc_const: 0x310
   __AUTH_CONST.__objc_intobj: 0x108
   __AUTH_CONST.__objc_arrayobj: 0x18
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0xa0
   __DATA.__objc_ivar: 0x28
-  __DATA.__bss: 0x30
+  __DATA.__bss: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/UIKit.framework/UIKit

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 538293C1-5963-3BDE-A514-8C4C6C0642E8
-  Functions: 58
-  Symbols:   276
-  CStrings:  171
+  UUID: 636D6951-1A7F-3C9A-B59F-02BE0173FDD8
+  Functions: 54
+  Symbols:   264
+  CStrings:  56
 
Symbols:
+ ___78-[TUIFeedbackController _presentSurveyWithParentController:completionHandler:]_block_invoke.148
+ ___block_literal_global.174
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x2
+ _objc_retain_x27
+ _objc_retain_x3
+ _objc_retain_x8
- -[TUIFeedbackController feedbackFeatureEnabled].cold.2
- _MGGetBoolAnswer
- _OBJC_CLASS_$_NSUserDefaults
- _OUTLINED_FUNCTION_6
- _OUTLINED_FUNCTION_7
- ___47-[TUIFeedbackController feedbackFeatureEnabled]_block_invoke
- ___78-[TUIFeedbackController _presentSurveyWithParentController:completionHandler:]_block_invoke.149
- ___block_literal_global.176
- ___block_literal_global.181
- _feedbackFeatureEnabled.is_internal_install
- _feedbackFeatureEnabled.once_token
- _objc_msgSend$boolForKey:
- _objc_msgSend$initWithSuiteName:
- _objc_release_x9
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
- _objc_retain_x26
CStrings:
+ "%s Feedback %@: RC_SEED_BUILD: 1 enabled: %d"
- "%s Feedback %@: RC_SEED_BUILD: 0 enabled: %d"
- ".cxx_destruct"
- "@\"NSArray\""
- "@\"NSDate\""
- "@\"NSString\""
- "@16@0:8"
- "@88@0:8@16@24@32@40B48@52@60B68@72@80"
- "B"
- "B16@0:8"
- "B20@0:8B16"
- "T@\"NSArray\",C,N,V_finalInputModes"
- "T@\"NSArray\",C,N,V_initialInputModes"
- "T@\"NSDate\",C,N,V_finalTimestamp"
- "T@\"NSDate\",C,N,V_initialTimestamp"
- "T@\"NSString\",C,N,V_build"
- "T@\"NSString\",C,N,V_language"
- "T@\"NSString\",C,N,V_model"
- "T@\"NSString\",C,N,V_region"
- "TB,N,V_finalPreferenceValue"
- "TB,N,V_initialPreferenceValue"
- "TUIFeedbackController"
- "TUIFeedbackSurveyMetadata"
- "_build"
- "_finalInputModes"
- "_finalPreferenceValue"
- "_finalTimestamp"
- "_initialInputModes"
- "_initialPreferenceValue"
- "_initialTimestamp"
- "_language"
- "_model"
- "_presentSurveyWithParentController:completionHandler:"
- "_region"
- "_updateStudyDataWithFinalPreferenceValue:finalTimestamp:"
- "_updateStudyDataWithSurveyOutcome:surveyError:initialState:"
- "apple-internal-install"
- "boolForKey:"
- "build"
- "bundleForClass:"
- "collectFeedbackWithLaunchConfiguration:completion:"
- "com.apple.keyboard"
- "completeStudyWithFinalPreferenceValue:parentController:"
- "computeSurveyMetadata"
- "controller"
- "countByEnumeratingWithState:objects:count:"
- "countryCode"
- "currentCampaign"
- "currentInputModes"
- "currentLocale"
- "duration"
- "enabledInputModeIdentifiers"
- "feedbackFeatureEnabled"
- "fetchCountsForFormWithIdentifier:completion:"
- "finalInputModes"
- "finalPreferenceValue"
- "finalTimestamp"
- "getFeedbackState"
- "getFinalInputModes"
- "getFinalPreferenceValue"
- "getFinalTimestamp"
- "getFormIdentifier"
- "getInitialInputModes"
- "getInitialPreferenceValue"
- "getInitialTimestamp"
- "getStudyID"
- "getSupportedLangRegion"
- "init"
- "initWithBuild:model:language:region:initialPreferenceValue:initialInputModes:initialTimestamp:finalPreferenceValue:finalInputModes:finalTimestamp:"
- "initWithFeedbackForm:"
- "initWithIdentifier:"
- "initWithSuiteName:"
- "initialInputModes"
- "initialPreferenceValue"
- "initialTimestamp"
- "intValue"
- "language"
- "languageCode"
- "length"
- "localizedStringForKey:value:table:"
- "model"
- "now"
- "prefill:answer:"
- "q16@0:8"
- "region"
- "setAuthenticationMethod:"
- "setBuild:"
- "setFeedbackState:"
- "setFinalInputModes:"
- "setFinalPreferenceValue:"
- "setFinalTimestamp:"
- "setInitialInputModes:"
- "setInitialPreferenceValue:"
- "setInitialTimestamp:"
- "setLanguage:"
- "setLocalizedAlertViewDeclineButtonTitle:"
- "setLocalizedAlertViewProceedButtonTitle:"
- "setLocalizedPromptMessage:"
- "setLocalizedPromptTitle:"
- "setModel:"
- "setPromptStyle:"
- "setRegion:"
- "setSurveyOutcome:"
- "sharedInputModeController"
- "shouldCompleteStudyWithPreferenceValue:"
- "stringWithFormat:"
- "timeIntervalSinceDate:"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@16"
- "v28@0:8B16@20"
- "v32@0:8@16@?24"
- "v40@0:8q16@24q32"

```
