## HomeCommunicationFlowDelegatePlugin

> `/System/Library/Assistant/FlowDelegatePlugins/HomeCommunicationFlowDelegatePlugin.bundle/HomeCommunicationFlowDelegatePlugin`

```diff

-3303.3.1.0.0
-  __TEXT.__text: 0x883b8
-  __TEXT.__auth_stubs: 0x2c50
-  __TEXT.__const: 0x37fc
-  __TEXT.__cstring: 0x742d
-  __TEXT.__constg_swiftt: 0x2b3c
-  __TEXT.__swift5_typeref: 0x1df6
-  __TEXT.__swift5_fieldmd: 0x188c
+3304.19.1.0.0
+  __TEXT.__text: 0x873e4
+  __TEXT.__auth_stubs: 0x2dc0
+  __TEXT.__const: 0x4a04
+  __TEXT.__cstring: 0x7f11
+  __TEXT.__constg_swiftt: 0x2ca8
+  __TEXT.__swift5_typeref: 0x1ef0
+  __TEXT.__swift5_fieldmd: 0x19c4
   __TEXT.__swift5_builtin: 0x28
-  __TEXT.__swift5_reflstr: 0x19f6
-  __TEXT.__swift5_assocty: 0x3c0
-  __TEXT.__swift5_proto: 0x234
-  __TEXT.__swift5_types: 0x184
+  __TEXT.__swift5_reflstr: 0x1aa1
+  __TEXT.__swift5_assocty: 0x420
+  __TEXT.__swift5_proto: 0x2c4
+  __TEXT.__swift5_types: 0x1a4
   __TEXT.__objc_classname: 0xaf
-  __TEXT.__objc_methname: 0x8b1
+  __TEXT.__objc_methname: 0x8ca
   __TEXT.__objc_methtype: 0x1a8
-  __TEXT.__swift5_capture: 0x528
-  __TEXT.__swift5_protos: 0x38
-  __TEXT.__unwind_info: 0x270c
-  __TEXT.__eh_frame: 0x4370
-  __DATA_CONST.__auth_got: 0x1628
-  __DATA_CONST.__got: 0x620
+  __TEXT.__swift5_capture: 0x438
+  __TEXT.__swift5_protos: 0x3c
+  __TEXT.__unwind_info: 0x25b4
+  __TEXT.__eh_frame: 0x4180
+  __DATA_CONST.__auth_got: 0x16e0
+  __DATA_CONST.__got: 0x630
   __DATA_CONST.__auth_ptr: 0x218
-  __DATA_CONST.__const: 0x39d0
-  __DATA_CONST.__objc_classlist: 0xe0
+  __DATA_CONST.__const: 0x3d18
+  __DATA_CONST.__objc_classlist: 0xe8
   __DATA_CONST.__objc_protolist: 0xc0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_const: 0x2d98
-  __DATA.__objc_selrefs: 0x2f8
-  __DATA.__objc_protorefs: 0x60
-  __DATA.__objc_classrefs: 0x170
+  __DATA_CONST.__objc_protorefs: 0x60
+  __DATA_CONST.__objc_classrefs: 0x180
+  __DATA.__objc_const: 0x2d88
+  __DATA.__objc_selrefs: 0x300
   __DATA.__objc_data: 0xba8
-  __DATA.__data: 0x5100
-  __DATA.__common: 0x3c0
-  __DATA.__bss: 0x3f00
+  __DATA.__data: 0x5ed8
+  __DATA.__common: 0x400
+  __DATA.__bss: 0x5180
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Intents.framework/Intents

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 01871BB2-5488-3AFE-B732-2CACDCFD4595
-  Functions: 3511
-  Symbols:   207
-  CStrings:  787
+  UUID: E3508C26-8908-3CFA-B0A0-84298B371377
+  Functions: 3608
+  Symbols:   212
+  CStrings:  847
 
Symbols:
+ _AFIsInternalInstall
+ _OBJC_CLASS_$_PatternExecutionResult
+ _OBJC_CLASS_$_SAIntentGroupRunSiriKitExecutor
+ _swift_asyncLet_get
+ _swift_setDeallocating
CStrings:
+ "\n    announcementID="
+ "\n    hasEverywhereOrEveryone="
+ "\n    hasSmsContact="
+ "\n    homeAutomationHomes="
+ "\n    homeAutomationServiceGroups="
+ "\n    homeAutomationTargetNodes="
+ "\n    homeAutomationUnknownDestinations="
+ "\n    homeAutomationZones="
+ "\n    homeCommunicationConfirmation="
+ "\n    homeFilter="
+ "\n    smsContactRole="
+ "\n    speechDataTranscription="
+ "\n    startTimeMs="
+ "#FileRadarUtils autoBugCapture: not an internal build. Skipping filing radar for \"%s\"/\"%s\""
+ "#FileRadarUtils autoBugCapture: result: %{bool}d"
+ "#FileRadarsUtils logging ABC"
+ "#HomeCommunicationFlowDelegatePlugin Filed ABC after hitting DirectInvocation parse in MainFlow: %{bool}d."
+ "#HomeCommunicationFlowDelegatePlugin Filed ABC after hitting NLv3IntentPlusServerConversion parse in MainFlow: %{bool}d."
+ "#HomeCommunicationFlowDelegatePlugin NLv4"
+ "#ReadAnnouncementAceViewProvider failed to play notificaiton sound"
+ "#ReadAnnouncementAceViewProvider played notification sound"
+ "#ReadAnnouncementIntentHelper submitting playNotificationSound command"
+ "#SendAnnouncementDisambiguationStrategy Disambiguating between homes : %s"
+ "#SendAnnouncementDisambiguationStrategy Disambiguating items were not of type INHomeFilter"
+ "#SendAnnouncementDisambiguationStrategy Error disambiguating between no homes or single home : %s"
+ "#SendAnnouncementDisambiguationStrategy missing app identifier"
+ "#SendAnnouncementDisambiguationStrategy nlIntent: %s"
+ "#SendAnnouncementFlow async producers with app resolution"
+ "#SendAnnouncementFlow no sharedUserID was found"
+ "#SendAnnouncementIntentHelper An error occurred while extracting speech data url: %s."
+ "#SendAnnouncementIntentHelper ExtractSpeechData ace command timed out"
+ "#SendAnnouncementIntentHelper extracted speech data URL is: %s"
+ "#SendAnnouncementIntentHelper extracted speech data URL was nil."
+ "#SendAnnouncementIntentHelper sending SASExtractSpeechData with speechRequestId:%s, startTime in ms: %@, endTime in ms: %@"
+ "#SendAnnouncementIntentHelper speech data transcription is: %s"
+ "#StopAnnouncementFlowStrategy makeIntentFromParse(parse:currentIntent:) called"
+ "#StopAnnouncementFlowStrategy setting endpoint ID=%s"
+ ".carPlayIntercomControl("
+ ".homeDisambiguation("
+ "Can't construct Array with count < 0"
+ "CarPlayIntercomControlModel#playbackControl"
+ "Division by zero"
+ "Division results in an overflow"
+ "HomeCommunication#HomeNameDisambiguation"
+ "HomeCommunicationNLIntent:\n    app="
+ "Insufficient space allocated to copy string contents"
+ "MainFlow doesn't handle NLv3IntentPlusServerConversion -- this should be handled in HomeCommunicationFlowDelegatePlugin"
+ "MainFlow doesn't handle direct invocations -- this should be handled in HomeCommunicationFlowDelegatePlugin"
+ "NLv3IntentPlusServerConversion"
+ "Negative value is not representable"
+ "RCHChildFlowProducers.SendAnnouncementProducers"
+ "Swift/Array.swift"
+ "Swift/ContiguousArrayBuffer.swift"
+ "Swift/IntegerTypes.swift"
+ "Swift/Integers.swift"
+ "Swift/StringTesting.swift"
+ "Swift/StringUTF8View.swift"
+ "Swift/UnsafeBufferPointer.swift"
+ "Swift/UnsafePointer.swift"
+ "Swift/UnsafeRawPointer.swift"
+ "T@\"NSString\",?,R,C"
+ "Unexpectedly found nil while unwrapping an Optional value"
+ "UnsafeMutableBufferPointer with negative count"
+ "UnsafeMutablePointer.initialize overlapping range"
+ "UnsafeMutablePointer.initialize with negative count"
+ "UnsafeMutablePointer.moveInitialize with negative count"
+ "UnsafeMutableRawPointer.initializeMemory overlapping range"
+ "UnsafeMutableRawPointer.initializeMemory with negative count"
+ "_TtC35HomeCommunicationFlowDelegatePlugin10RadarUtils"
+ "carPlayIntercomControl"
+ "debug"
+ "directInvocation"
+ "endpointId"
+ "entityName"
+ "error"
+ "extractSpeechData"
+ "fileAutoBugCapture(errorType:errorSubType:subTypeContext:)"
+ "flowDelegatePlugin"
+ "homeDisambiguation"
+ "homeKitEntityType"
+ "invalid Collection: less than 'count' elements in collection"
+ "mainFlow"
+ "nlContextProvider"
+ "selectHomeAction"
+ "semaphoreTimeout"
+ "sendAnnouncementCATsSimple"
- "#HomeCommunicationFlowDelegatePlugin NLv4)"
- "#SendAnnouncementDisambiguationStrategy error in generating CAT result: %s"
- "#SendAnnouncementDisambiguationStrategy error in generating ace views: %s"
- "#SendAnnouncementDisambiguationStrategy homesToDisambiguate: %s"
- "#SendAnnouncementDisambiguationStrategy makePromptForDisambiguationAsync with response framework adoption"
- "#SendAnnouncementIntentHandledStrategy failure in generating INPlayAnnouncementSoundIntent"
- "#SendAnnouncementIntentHandledStrategy makeFailureHandlingIntentResponse"
- "#SendAnnouncementIntentHandledStrategy makeIntentHandledResponse"
- "#SendAnnouncementNeedsValueStrategy makePromptForValue"
- "#StopAnnouncementFlowStrategy makeIntentFromParse() called"
- "Ace command for playing notification sound failed due to: %s."
- "Ace command for playing notification sound timed out."
- "An error occurred while extracting speech data url: %s."
- "ExtractSpeechData ace command timed out"
- "HomeCommunicationControl#playbackControl"
- "Playing notification sound."
- "extracted speech data URL is: %s"
- "extracted speech data URL was nil."
- "homeCommunicationTargets"
- "makeDisambiguationItemContainer(resolveRecord:)"
- "makeFailureHandlingIntentResponse(rchRecord:)"
- "makeIntentHandledResponse(rchRecord:)"
- "makeParameterPromptDialogAsync(delegate:intent:parameter:resolutionResult:)"
- "sending SASExtractSpeechData with speechRequestId:%s, startTime in ms: %@, endTime in ms: %@"
- "speech data transcription is: %s"
- "speechRequestId"

```
