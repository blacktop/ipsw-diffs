## CryptoKit

> `/System/Library/Frameworks/CryptoKit.framework/CryptoKit`

```diff

-241.0.9.0.0
-  __TEXT.__text: 0x61a30
+241.0.11.0.0
+  __TEXT.__text: 0x60acc
   __TEXT.__auth_stubs: 0x14e0
-  __TEXT.__const: 0x3e54
+  __TEXT.__const: 0x3e44
   __TEXT.__swift5_typeref: 0x1520
   __TEXT.__swift5_reflstr: 0xbc2
   __TEXT.__swift5_assocty: 0xb08

   __TEXT.__swift5_protos: 0x88
   __TEXT.__swift5_capture: 0xc0
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x2168
-  __TEXT.__eh_frame: 0x57f8
+  __TEXT.__unwind_info: 0x2160
+  __TEXT.__eh_frame: 0x57c8
   __TEXT.__objc_methname: 0x127
   __DATA_CONST.__got: 0x3b0
-  __DATA_CONST.__const: 0x40
+  __DATA_CONST.__const: 0x80
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x70
   __AUTH_CONST.__auth_got: 0xa70
-  __AUTH_CONST.__auth_ptr: 0xbf0
+  __AUTH_CONST.__auth_ptr: 0xb40
   __AUTH_CONST.__const: 0x3c48
   __AUTH_CONST.__objc_const: 0x268
   __AUTH.__data: 0xdd8
   __DATA.__data: 0xae0
-  __DATA.__objc_clsrolist: 0x10
   __DATA.__bss: 0x4180
   __DATA.__common: 0xc0
   __DATA_DIRTY.__data: 0x548

   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 2546
-  Symbols:   270
-  CStrings:  62
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 2545
+  Symbols:   278
+  CStrings:  49
 
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
+ "basebandLogURL"
+ "batchQueryControllerCreationBlock"
+ "batchQuerySearchMultiwayController"
+ "batchQuerySearchShareNameAndPhotoController"
+ "batchQuerySearchVideoMessagingController"
+ "batchQuerySearchiMessageController"
+ "beginBatchQueryWithDestinations:"
+ "beginBatchQueryWithDestinations:includeMessages:"
+ "beginBatchQueryWithDestinations:services:"
+ "beginCachedQueryWithDestinations:"
+ "beginCachedQueryWithDestinations:includeMessages:"
+ "beginCachedQueryWithDestinations:onService:"
+ "beginCachedQueryWithDestinations:services:"
+ "beginPIPToPreviewAnimation"
+ "beginPreviewToPIPAnimation"
+ "beginQueryWithDestination:onService:"
+ "beginQueryWithDestinations:"
+ "beginQueryWithDestinations:includeMessages:"
+ "beginQueryWithDestinations:services:"
+ "beginQueryWithRefreshForDestination:onService:"
+ "blockedByExtension"
+ "blockedContactsAvailable"
+ "bluetoothAudioFormat"
+ "bluetoothLE"
+ "bluetoothManaged"
+ "boolValueForQueryItemWithName:inURLComponents:"
+ "brandedCallingAvailable"
+ "bundleIdentifierForCallProvider:"
+ "businessConnectCallingEnabled"
+ "businessQueryService"
+ "buzzMember:conversationUUID:"
+ "calendarItemIdentifier"
+ "callAnnouncementAvailableForFaceTime"
+ "callAnnouncementAvailableForPhone"
+ "callBlockingAndIdentificationAvailable"
+ "callCapabilitiesState:"
+ "callCenter:reportedCall:receivedDTMFUpdate:"
+ "callDirectoryExtensionIdentifier"
+ "callDirectoryIdentityType"
+ "momentsController:willCaptureRemoteRequestFromIdentifier:"
+ "momentsControllerClientXPCInterface"
+ "momentsControllerServerDied:"
+ "momentsControllerServerXPCInterface"
+ "mostRecentCallInfo"
+ "mostRecentCallType"
+ "mostRecentCallWasMissed"
+ "mutuallyExclusiveCall"
+ "omentsController:didUpdateCapabilities:forProvider:"
+ "tIdentifier"
- "T@\"NSString\",R,N,V_replyText"
- "T@\"NSString\",R,N,V_vocabFilePath"
- "T@\"PREResponsesGeneratedEvent\",&,N,V_responsesGeneratedEvent"
- "T@\"PREUMMessageMetadata\",&,N,V_msgMetadata"
- "T@\"PREUMTrialExperiment\",&,N,V_experiment"
- "T@\"TRIExperimentIdentifiers\",R,N"
- "T@\"TRIRolloutIdentifiers\",R,N"
- "T@\"TRIRolloutIdentifiers\",R,N,V_rolloutIdentifiers"
- "TB,N,GisDynamicReply,V_dynamicReply"
- "TB,N,GisEmote,V_emote"
- "TB,N,GisTapBack,V_tapBack"
- "TB,N,V_hasQuestionMark"
- "TB,N,V_includeCannedResponses"
- "TB,N,V_includeCustomResponses"
- "TB,N,V_includesDynamicSuggestions"
- "TB,N,V_isApricotDevice"
- "TB,N,V_isCompletionCalled"
- "TB,N,V_isCustomResponse"
- "TB,N,V_isRobotResponse"
- "TB,N,V_registerDisplayed"
- "TB,R,N,V_isMLModelEnabled"
- "TI,N,V_charCount"
- "TI,N,V_engagedItem"
- "TI,N,V_lastViewedIndex"
- "TI,N,V_modelId"
- "TI,N,V_numberOfCustomResponses"
- "TI,N,V_numberOfResponsesGenerated"
- "TI,N,V_numberOfRobotResponses"
- "TI,N,V_replyTextId"
- "TI,N,V_responseClassId"
- "TQ,N,V_messageCharCount"
- "TQ,N,V_responseGenerationTime"
- "TQ,N,V_responseTimePerf"
- "TQ,N,V_timeToTap"
- "Ti,N,V_generationStatus"
- "Ti,N,V_inputMethod"
- "_areSubmodelsEmptyUsingDatabase:"
- "_arrivalAirportDescription"
- "_assetUpdateToken"
- "_attachmentDetectionRegexes"
- "_attachmentFilename"
- "_attachmentLinkDetection"
- "_attachmentLinkDetectionRegex"
- "_attachmentsProbability"
- "_attachmentsStats"
- "_attributeSetForEvent:"
- "_authorCached"
- "_bestLocaleForLanguageTag:"
- "_cannedRepliesForLanguage:inputPreferences:"
- "_charCount"
- "_clientHelpers"
- "_dynamicReply"
- "_emote"
- "_engagedItem"
- "_espressoBinFilePath"
- "_exemptTermsDetector"
- "_experimentResolver"
- "_fillDefaultValueForFactors"
- "_generationStatus"
- "_getConversationHistoryFromRequest:"
- "houldContinue:usingDatabase:"
- "ta:"

```
