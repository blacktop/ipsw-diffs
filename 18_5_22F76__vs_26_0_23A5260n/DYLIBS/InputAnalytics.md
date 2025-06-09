## InputAnalytics

> `/System/Library/PrivateFrameworks/InputAnalytics.framework/InputAnalytics`

```diff

-64.504.100.0.0
-  __TEXT.__text: 0x23318
-  __TEXT.__auth_stubs: 0x830
-  __TEXT.__objc_methlist: 0x28fc
-  __TEXT.__const: 0x282
-  __TEXT.__cstring: 0x4c32
-  __TEXT.__gcc_except_tab: 0x468
-  __TEXT.__oslogstring: 0x2c70
+90.0.0.0.0
+  __TEXT.__text: 0x1cffc
+  __TEXT.__auth_stubs: 0x810
+  __TEXT.__objc_methlist: 0x245c
+  __TEXT.__const: 0x2e2
+  __TEXT.__cstring: 0x4742
+  __TEXT.__oslogstring: 0x25f0
+  __TEXT.__gcc_except_tab: 0x3a8
   __TEXT.__ustring: 0x4
   __TEXT.__swift5_typeref: 0x8c
   __TEXT.__swift5_capture: 0x88

   __TEXT.__swift5_types: 0x8
   __TEXT.__swift_as_entry: 0x1c
   __TEXT.__swift_as_ret: 0x1c
-  __TEXT.__unwind_info: 0x9a0
+  __TEXT.__unwind_info: 0x820
   __TEXT.__eh_frame: 0x2e8
-  __TEXT.__objc_classname: 0x7f5
-  __TEXT.__objc_methname: 0x525b
-  __TEXT.__objc_methtype: 0xa92
-  __TEXT.__objc_stubs: 0x3600
-  __DATA_CONST.__got: 0x268
-  __DATA_CONST.__const: 0x15d0
-  __DATA_CONST.__objc_classlist: 0x200
+  __TEXT.__objc_classname: 0x704
+  __TEXT.__objc_methname: 0x4715
+  __TEXT.__objc_methtype: 0xa1a
+  __TEXT.__objc_stubs: 0x2ce0
+  __DATA_CONST.__got: 0x240
+  __DATA_CONST.__const: 0x1668
+  __DATA_CONST.__objc_classlist: 0x1a8
+  __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x12e8
+  __DATA_CONST.__objc_selrefs: 0x10c0
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x138
+  __DATA_CONST.__objc_superrefs: 0xf0
   __DATA_CONST.__objc_arraydata: 0xdb0
-  __AUTH_CONST.__auth_got: 0x428
-  __AUTH_CONST.__const: 0x6f8
-  __AUTH_CONST.__cfstring: 0x73a0
-  __AUTH_CONST.__objc_const: 0x4890
-  __AUTH_CONST.__objc_intobj: 0xc18
+  __AUTH_CONST.__auth_got: 0x418
+  __AUTH_CONST.__const: 0x520
+  __AUTH_CONST.__cfstring: 0x70e0
+  __AUTH_CONST.__objc_const: 0x3e60
+  __AUTH_CONST.__objc_intobj: 0xa38
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH.__objc_data: 0xa20
+  __AUTH.__objc_data: 0x840
   __AUTH.__data: 0x28
-  __DATA.__objc_ivar: 0x25c
-  __DATA.__data: 0x370
-  __DATA.__bss: 0x1c0
+  __DATA.__objc_ivar: 0x210
+  __DATA.__data: 0x300
   __DATA.__common: 0x8
-  __DATA_DIRTY.__objc_data: 0xa00
+  __DATA.__bss: 0xe0
+  __DATA_DIRTY.__objc_data: 0x870
   __DATA_DIRTY.__bss: 0xc8
   __DATA_DIRTY.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
-  - /System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
+  - /System/Library/PrivateFrameworks/CoreEmoji.framework/CoreEmoji
   - /System/Library/PrivateFrameworks/FeedbackService.framework/FeedbackService
   - /System/Library/PrivateFrameworks/TextInput.framework/TextInput
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_errno.dylib
-  - /usr/lib/swift/libswift_math.dylib
-  - /usr/lib/swift/libswift_signal.dylib
-  - /usr/lib/swift/libswift_stdio.dylib
-  - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
-  - /usr/lib/swift/libswiftsys_time.dylib
-  - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 99F1E45E-958A-31BC-972D-978DFC4872C6
-  Functions: 1101
-  Symbols:   701
-  CStrings:  3165
+  UUID: 2A6670B7-6D6F-3CF4-A7E4-F9FB1DD5A5E2
+  Functions: 943
+  Symbols:   763
+  CStrings:  2965
 
Symbols:
+ _CEMCreateStringByStrippingEmojiCharacters
+ _IAChannelLegacyTextInputActions
+ _IAPayloadKeyGenmojiSource
+ _IAPayloadKeyImageGenerationIngredientID
+ _IAPayloadKeyImageGenerationIngredientType
+ _IAPayloadKeyImageGenerationIngredients
+ _IAPayloadKeyImageGenerationRecipeID
+ _IAPayloadKeyImageGenerationStyle
+ _IAPayloadKeyLegacyTextInputActionsClass
+ _IAPayloadKeySmartRepliesActions
+ _IAPayloadKeySmartRepliesPollActionOptions
+ _IAPayloadKeySmartRepliesPollActionTitle
+ _IAPayloadValueGenmojiSourceAddCaptionMenu
+ _IAPayloadValueGenmojiSourceAlphabeticKeyboard
+ _IAPayloadValueGenmojiSourceCreateCharacterSheet
+ _IAPayloadValueGenmojiSourceCreateNewCharacterSheet
+ _IAPayloadValueGenmojiSourceCreationSheet
+ _IAPayloadValueGenmojiSourceCreationSheetGenerating
+ _IAPayloadValueGenmojiSourceCreationSheetGeneratingPill
+ _IAPayloadValueGenmojiSourceCreationSheetMenu
+ _IAPayloadValueGenmojiSourceCreationSheetNoResults
+ _IAPayloadValueGenmojiSourceCreationSheetPersonIdentification
+ _IAPayloadValueGenmojiSourceCreationSheetResults
+ _IAPayloadValueGenmojiSourceCreationSheetResultsPill
+ _IAPayloadValueGenmojiSourceEditPhotoMenu
+ _IAPayloadValueGenmojiSourceEmojiKeyboard
+ _IAPayloadValueGenmojiSourceEmojiSearchKeyboardCreateNewEmojiDisplayed
+ _IAPayloadValueGenmojiSourceGenmoji
+ _IAPayloadValueGenmojiSourceImagePlayground
+ _IAPayloadValueGenmojiSourceImageWand
+ _IAPayloadValueGenmojiSourcePeopleChooserSheet
+ _IAPayloadValueGenmojiSourcePhotoChooserSheet
+ _IAPayloadValueGenmojiSourceThirdParty
+ _IAPayloadValueGenmojiSourceUnspecified
+ _IAPayloadValueSmartRepliesActionsCashAction
+ _IAPayloadValueSmartRepliesActionsCheckInAction
+ _IAPayloadValueSmartRepliesActionsContactInfoAction
+ _IAPayloadValueSmartRepliesActionsCurrentlyPlayingAction
+ _IAPayloadValueSmartRepliesActionsETAAction
+ _IAPayloadValueSmartRepliesActionsFlightAction
+ _IAPayloadValueSmartRepliesActionsLocationAction
+ _IAPayloadValueSmartRepliesActionsMeetingAction
+ _IAPayloadValueSmartRepliesActionsPollAction
+ _IAPayloadValueSmartRepliesActionsUnknownAction
+ _IASignalGenmojiCreationFinalImageGenerated
+ _IASignalGenmojiCreationUIAppeared
+ _IASignalImageGenerationCancelButtonPressed
+ _IASignalImageGenerationCopyButtonPressed
+ _IASignalImageGenerationFinalImageGenerated
+ _IASignalImageGenerationImageIndexChanged
+ _IASignalImageGenerationRetryRequested
+ _IASignalImageGenerationSaveButtonPressed
+ _IASignalImageGenerationShareButtonPressed
+ _IASignalImageGenerationUIAppeared
+ _IASignalImageGenerationUIResumed
+ _IASignalImageGenerationUISuspended
+ _IASignalLegacyTextInputActionsDidAction
+ _IASignalLegacyTextInputActionsDidSessionBegin
+ _IASignalLegacyTextInputActionsDidSessionEnd
+ _IASignalSmartRepliesActionsGenerated
+ _IASignalSmartRepliesActionsRequested
+ _IASignalSmartRepliesPollActionEngaged
+ _IASignalSmartRepliesPollActionGenerated
+ _IASignalSmartRepliesPollActionNotShown
+ _IASignalSmartRepliesPollActionRequested
+ _IASignalSmartRepliesPollActionShown
+ _OBJC_CLASS_$_IASmartRepliesAnalytics
+ _OBJC_CLASS_$_IATextInputActionsSessionCommitTextAction
+ _OBJC_METACLASS_$_IASmartRepliesAnalytics
+ _OBJC_METACLASS_$_IATextInputActionsSessionCommitTextAction
+ __swiftImmortalRefCount
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- _BiomeLibrary
- _OBJC_CLASS_$_BMGeneratedImageFailureReason
- _OBJC_CLASS_$_NSLocale
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftunistd
- _objc_enumerationMutation
- _objc_retainBlock
CStrings:
+ "Actions"
+ "ActionsGenerated"
+ "ActionsRequested"
+ "CashAction"
+ "CheckInAction"
+ "Class"
+ "CommitText"
+ "ContactInfoAction"
+ "ConvertToDictionary"
+ "CopyButtonPressed"
+ "CreationSheetPersonIdentification"
+ "CurrentlyPlayingAction"
+ "DidAction"
+ "DidSessionBegin"
+ "DidSessionEnd"
+ "ETAAction"
+ "FinalImageGenerated"
+ "FlightAction"
+ "IASmartRepliesAnalytics"
+ "IATextInputActionsSessionCommitTextAction"
+ "ImageIndexChanged"
+ "IngredientID"
+ "IngredientType"
+ "Ingredients"
+ "LegacyTextInputActions"
+ "LocationAction"
+ "MeetingAction"
+ "PollAction"
+ "PollActionEngaged"
+ "PollActionGenerated"
+ "PollActionNotShown"
+ "PollActionOptions"
+ "PollActionRequested"
+ "PollActionShown"
+ "PollActionTitle"
+ "RecipeID"
+ "SaveButtonPressed"
+ "SetObjectIfNotNil"
+ "ShareButtonPressed"
+ "Source"
+ "Style"
+ "T@\"IATextInputActionsSessionCommitTextAction\",R,N"
+ "ThirdParty"
+ "UIAppeared"
+ "UnknownAction"
+ "[IATextInputActionsAnalytics] didCommitText: was invoked with nil or empty text. (Committed text should never be nil or empty.)"
+ "[IATextInputActionsAnalytics] didCommitText:%{sensitive}@ from source %lu"
+ "asCommitText"
+ "dateWithTimeIntervalSinceReferenceDate:"
+ "didCommitText:"
+ "flushAndSetLastAction calling sendSignal:toChannel:withNullableSessionID:withPayload:"
+ "genmojiSourceToEnumMap"
+ "initFromDictionary:"
+ "lengthOfBytesUsingEncoding:"
+ "mergeOrConsumeAction calling sendSignal:toChannel:withNullableSessionID:withPayload:"
+ "setObjectIfNotNil:forKey:"
+ "smartRepliesSignalToEnumMap"
+ "timeIntervalSinceReferenceDate"
+ "toDictionary"
- "   - Analyzer %@\n"
- " - %@ %@ analyzers: %lu\n"
- " - %@ (%@) [%@] Analyzer %@\n"
- "#"
- "%@"
- "%@ status:\nActive sessions: %lu\n"
- "%@: Analyzer ID=%@"
- "%{private}@"
- ","
- "@\"BMGeneratedImageFailureReason\""
- "@\"NSArray\""
- "@40@0:8@16@24@?32"
- "Analytics session ID %@ already mapped. Unable to associate with another session"
- "Analyzer ID %@ does not exist. Unable to map"
- "B32@0:8@16@24"
- "Corrupted mapping: Analytics session ID string %@ did not exist in forward mapping but exists in reverse mapping"
- "ERROR: Invalid special case for genmoji usage analyzer"
- "GeneratedImageFeatures"
- "GenerativeExperiences"
- "Handling channel %{private}@ signal %{private}@"
- "IAGeneric"
- "IAGenmoji"
- "IAGenmojiUsage"
- "IAImageGeneration"
- "IASGenericAnalyzer"
- "IASGenericAnalyzer.m"
- "IASGenmojiEdit"
- "IASGenmojiEditAnalyzer"
- "IASGenmojiEditAnalyzer.m"
- "IASGenmojiEditEvent"
- "IASGenmojiUsageAnalyzer"
- "IASGenmojiUsageAnalyzer.m"
- "IASGenmojiUsageEvent"
- "IASImageGenerationResultAnalyzer"
- "IASImageGenerationResultAnalyzer.m"
- "IASImageGenerationResultEvent"
- "IASMultiClassSessionManager"
- "IASMultiSourceSessionManager"
- "IASSessionManager"
- "IASSessionManager.m"
- "IASStatelessSessionManager"
- "IASStatelessSessionManager.m"
- "IASTextInputUserPreference"
- "IASTextInputUserPreferenceServer"
- "IASTextInputUserPreferenceStateEvent"
- "Initialized analyzer"
- "Initialized with exceptions: %{private}@"
- "KeyboardAutocorrection"
- "KeyboardInlineCompletion"
- "Missing definitions in channelBasedPayloadKeyAllowList for channel '%{private}@' payloadKey '%{private}@'"
- "Missing definitions in channelBasedPayloadKeyAllowList for channel '%{private}@' signal '%{private}@'"
- "No supported preferences for platform to report for requested userPreference %lu"
- "Obfuscating subcategory %{sensitive}@"
- "Payload value '%{private}@' not found in translator for channel '%{private}@' payloadKey '%{private}@'. Using default"
- "Please implement didAction in child class"
- "Publishing"
- "Q40@0:8@16@24Q32"
- "Stateless analyzers can only have 1 UUID by design. This condition should never be violated. Got %lu"
- "Stateless session manager initialized %lu analyzers"
- "T#,&,N,V_analyzerClass"
- "T@\"BMGeneratedImageFailureReason\",&,N,V_biomeGeneratedImageFailureReason"
- "T@\"IADefaultsDataStore\",&,N,V_dataStore"
- "T@\"NSArray\",&,N,V_analyzerClasses"
- "T@\"NSDictionary\",&,N,V_channelBasedPayloadKeyAllowList"
- "T@\"NSDictionary\",&,N,V_signalTranslation"
- "T@\"NSMutableDictionary\",&,N,V_analyzerIdToAnalyzerMap"
- "T@\"NSMutableDictionary\",&,N,V_analyzerIdToAnalyzersMap"
- "T@\"NSMutableDictionary\",&,N,V_analyzerIdToSessionIdsMap"
- "T@\"NSMutableDictionary\",&,N,V_sessionIdToAnalyzerIdMap"
- "T@\"NSObject<OS_dispatch_queue>\",R,N,V_queue"
- "T@\"NSString\",C,N,V_preferenceName"
- "T@\"NSUUID\",&,N,V_genericAnalyzerId"
- "T@?,C,N,V_eventHandler"
- "TB,N,V_readyToReportPreferenceToEventHandler"
- "TB,N,V_sendToBiomeStream"
- "Tq,N,V_preferenceValue"
- "[%{private}@] BMFailureReason published"
- "[%{private}@] BMFailureReason: %{sensitive}@"
- "[%{private}@] Publishing"
- "[%{private}@] Skipping publish for feature %{private}@"
- "[%{private}@] recordEngagementForToday: %@ %x->%x"
- "[%{private}@] recordEngagementForToday: Failed to obtain daterange"
- "_analyzerClass"
- "_analyzerClasses"
- "_analyzerIdToAnalyzerMap"
- "_analyzerIdToAnalyzersMap"
- "_analyzerIdToSessionIdsMap"
- "_appendAllowListedPayloadKeyAndValueTo:forSignalAnalyticsObject:"
- "_appendSignalEnumTo:forSignalAnalyticsObject:"
- "_biomeGeneratedImageFailureReason"
- "_channelBasedPayloadKeyAllowList"
- "_dataStore"
- "_eventHandler"
- "_genericAnalyzerId"
- "_preferenceName"
- "_preferenceValue"
- "_readyToReportPreferenceToEventHandler"
- "_sendToBiomeStream"
- "_sessionIdToAnalyzerIdMap"
- "_signalTranslation"
- "allObjects"
- "analyzerClass"
- "analyzerClasses"
- "analyzerForAnalyzerID:"
- "analyzerForSessionID:"
- "analyzerId %@ exists without analyzer"
- "analyzerIdForSessionID:"
- "analyzerIdToAnalyzerMap"
- "analyzerIdToAnalyzersMap"
- "analyzerIdToSessionIdsMap"
- "analyzerVersion"
- "associateAnalyticsSessionID:withAnalyzerID:"
- "biomeGeneratedImageFailureReason"
- "broadcastActionToSubscribingAnalyzers not implemented"
- "broadcastActionToSubscribingAnalyzers:"
- "channelBasedPayloadKeyAllowList"
- "com.apple.inputAnalytics.IASGenmojiUsageAnalyzer"
- "com.apple.inputAnalytics.generatedEmojiEdits"
- "com.apple.inputAnalytics.generatedEmojiUsage"
- "com.apple.inputAnalytics.imageGenerationResult"
- "com.apple.inputAnalytics.server.IASGenericAnalyzer"
- "com.apple.inputAnalytics.server.IASImageGenerationResultAnalyzer"
- "com.apple.inputAnalytics.server.IASStatelessSessionManager"
- "com.apple.inputAnalytics.signalAnalytics."
- "com.apple.keyboard.textInputUserPreferenceState"
- "conversationType"
- "countByEnumeratingWithState:objects:count:"
- "createAnalyzerForSessionID found existing analyzer for session %@ of class %@"
- "createAnalyzerForSessionID:"
- "createAnalyzerWithId:class:"
- "currentLocale"
- "currentValue"
- "dataStore"
- "didAction called with action object of class %{sensitive}@ and description %{sensitive}@\n"
- "didAction not implemented"
- "dispatchUserPreference:withValue:"
- "editType"
- "editTypeFromPayload:"
- "enumTranslation"
- "enumTranslationDefaultValue"
- "errorCodes"
- "feature"
- "featureDetails"
- "featureDetailsEnum"
- "featureEnum"
- "featureForFeature:"
- "flushAndSetLastAction calling didAction on xpc client 0x%lx with server 0x%lx"
- "flushAndSetLastAction: server does not respond to didAction. xpc client 0x%lx with server 0x%lx "
- "garbageCollect"
- "garbageCollect not implemented"
- "generationResult"
- "genericAnalyzerId"
- "getDaterangeObjectWithName: Failed to obtain daterange with error: %{private}@"
- "getDaterangeObjectWithName:dataStore:"
- "handleGenmojiEditSignal:"
- "handleGenmojiUsageSignal:"
- "handleImageInsertedSignal:"
- "imageType"
- "imageTypeEnum"
- "imageTypeFromPayload:"
- "initWithQueue:"
- "initWithQueue:serverDelegate:eventHandler:"
- "initWithTimestamp:identifier:userInterfaceLanguage:userSetRegionFormat:reason:feature:"
- "intValue"
- "interactionType"
- "interactionTypeEnum"
- "isCached"
- "isSpecialCaseUsageSignal:"
- "isUsageSignal:"
- "languageCode"
- "mergeOrConsumeAction calling didSessionBeginWithSessionMetadata on xpc client 0x%lx with server 0x%lx"
- "mergeOrConsumeAction calling didSessionEndWithSessionMetadata on xpc client 0x%lx with server 0x%lx"
- "mergeOrConsumeAction: server does not respond to didSessionBeginWithSessionMetadata. xpc client 0x%lx with server 0x%lx "
- "mergeOrConsumeAction: server does not respond to didSessionEndWithSessionMetadata. xpc client 0x%lx with server 0x%lx "
- "not implemented!"
- "preferenceName"
- "preferenceValue"
- "publishEnumName"
- "publishFieldName"
- "readyToReportPreferenceToEventHandler"
- "recordEngagementForTodayWithDatastoreObjectName:"
- "recordUsageForToday"
- "regionCode"
- "rejectionCategory"
- "rejectionCategoryDetails"
- "rejectionCategoryDetailsForBlockingSubCategory:"
- "rejectionCategoryForBlockingCategory:"
- "rejectionInputOutput"
- "rejectionInputOutputForBlockingInputOutputCategory:"
- "removeObject:"
- "retrieveStandardBooleanPreference:"
- "sendBiomeAnalyticsForSignal:"
- "sendEvent:"
- "sendToBiomeStream"
- "sessionIDsForAnalyzerID:"
- "sessionIdToAnalyzerIdMap"
- "setAnalyzerClass:"
- "setAnalyzerClasses:"
- "setAnalyzerIdToAnalyzerMap:"
- "setAnalyzerIdToAnalyzersMap:"
- "setAnalyzerIdToSessionIdsMap:"
- "setBiomeGeneratedImageFailureReason:"
- "setChannelBasedPayloadKeyAllowList:"
- "setDataStore:"
- "setGenericAnalyzerId:"
- "setPreferenceName:"
- "setPreferenceValue:"
- "setReadyToReportPreferenceToEventHandler:"
- "setSendToBiomeStream:"
- "setSessionIdToAnalyzerIdMap:"
- "setSignalTranslation:"
- "setValuesForKeysWithDictionary:"
- "signal"
- "signal '%{private}@' not found in translator for channel '%{private}@'. Using default"
- "signalEnum"
- "signalTranslation"
- "substringToIndex:"
- "terminateAnalyzerSession:"
- "transform"
- "translateValue:withMapping:withDefaultValue:"
- "truncate256"
- "ui"
- "uiEnum"
- "usageSource"
- "usageSourceEnum"
- "usageSourceFromPayload:"
- "usageType"
- "usageTypeEnum"
- "usageTypeFromPayload:"
- "v24@0:8#16"
- "v32@0:8q16q24"
- "v32@?0@\"NSUUID\"8@\"IASAnalyzer\"16^B24"
- "v32@?0@\"NSUUID\"8@\"NSMutableArray\"16^B24"

```
