## assistantd

> `/System/Library/PrivateFrameworks/AssistantServices.framework/assistantd`

```diff

-3404.80.4.11.3
-  __TEXT.__text: 0x36c048
-  __TEXT.__auth_stubs: 0x34b0
-  __TEXT.__objc_stubs: 0x45280
-  __TEXT.__objc_methlist: 0x224a0
+3405.21.2.0.0
+  __TEXT.__text: 0x36d24c
+  __TEXT.__auth_stubs: 0x34c0
+  __TEXT.__objc_stubs: 0x45520
+  __TEXT.__objc_methlist: 0x22510
   __TEXT.__const: 0x10990
   __TEXT.__dlopen_cstrs: 0xafa
-  __TEXT.__gcc_except_tab: 0x487c
-  __TEXT.__cstring: 0x51712
-  __TEXT.__oslogstring: 0x3f68c
-  __TEXT.__objc_classname: 0x519f
-  __TEXT.__objc_methname: 0x5d0d9
+  __TEXT.__gcc_except_tab: 0x4878
+  __TEXT.__cstring: 0x519c8
+  __TEXT.__oslogstring: 0x3f92b
+  __TEXT.__objc_classname: 0x518a
+  __TEXT.__objc_methname: 0x5d31a
   __TEXT.__objc_methtype: 0xf1e2
   __TEXT.__ustring: 0x2b0
-  __TEXT.__unwind_info: 0xa398
+  __TEXT.__unwind_info: 0xa378
   __TEXT.__eh_frame: 0xe58
-  __DATA_CONST.__auth_got: 0x1a68
-  __DATA_CONST.__got: 0x3b18
+  __DATA_CONST.__auth_got: 0x1a70
+  __DATA_CONST.__got: 0x3b20
   __DATA_CONST.__auth_ptr: 0x20
-  __DATA_CONST.__const: 0x14c90
-  __DATA_CONST.__cfstring: 0x129c0
+  __DATA_CONST.__const: 0x14cb0
+  __DATA_CONST.__cfstring: 0x12b40
   __DATA_CONST.__objc_classlist: 0xd10
   __DATA_CONST.__objc_catlist: 0x630
   __DATA_CONST.__objc_protolist: 0x6e8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x88
   __DATA_CONST.__objc_superrefs: 0xb08
-  __DATA_CONST.__objc_arraydata: 0x3d8
-  __DATA_CONST.__objc_arrayobj: 0x1e0
+  __DATA_CONST.__objc_arraydata: 0x3c0
+  __DATA_CONST.__objc_arrayobj: 0x1c8
   __DATA_CONST.__objc_intobj: 0x840
   __DATA_CONST.__objc_dictobj: 0x2d0
   __DATA_CONST.__objc_doubleobj: 0x30
   __DATA_CONST.__objc_floatobj: 0x30
-  __DATA.__objc_const: 0x33698
-  __DATA.__objc_selrefs: 0x147f0
-  __DATA.__objc_ivar: 0x258c
+  __DATA.__objc_const: 0x336b8
+  __DATA.__objc_selrefs: 0x14898
+  __DATA.__objc_ivar: 0x2590
   __DATA.__objc_data: 0x82a0
   __DATA.__data: 0x60f8
   __DATA.__bss: 0xe10

   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
   - /System/Library/PrivateFrameworks/CrashReporterSupport.framework/CrashReporterSupport
   - /System/Library/PrivateFrameworks/DialogEngine.framework/DialogEngine
-  - /System/Library/PrivateFrameworks/FeatureStore.framework/FeatureStore
   - /System/Library/PrivateFrameworks/FeedbackLogger.framework/FeedbackLogger
   - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices
   - /System/Library/PrivateFrameworks/GenerativeAssistantSettings.framework/GenerativeAssistantSettings

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libresolv.9.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 14308
-  Symbols:   2888
-  CStrings:  27126
+  Functions: 14321
+  Symbols:   2890
+  CStrings:  27180
 
Symbols:
+ _AFRequiredAssetsForFullUOD
+ _NSMultipleUnderlyingErrorsKey
+ _OBJC_CLASS_$_SMTUserProfileMetadata
+ _OBJC_CLASS_$_SRDRemoteIFClientWakeStore
- _OBJC_CLASS_$_FSFCurareInteractionAsDict
- _OBJC_CLASS_$_FSFCurareInteractionStream
CStrings:
+ "\x0f\x0f\x1c\x11\x11\x12,T\x12\x11\x11\x15\x13\x16\x14\x13\x13\x12\x16"
+ "%s #ODD: genAIAgent=%d"
+ "%s #hal Pushing location for AssistantID: %@ %@"
+ "%s #hal Pushing location for IDS: %@ %@"
+ "%s #hal Updating location snapshot with %@"
+ "%s #shih updating SMTRequestContextData %@"
+ "%s After notification, sending completion: %@"
+ "%s Asking for anchor keys=%@"
+ "%s Dictation transaction ended! resuming idle timer"
+ "%s Embedded error: %@"
+ "%s Notified of errorOnion: %@"
+ "%s Notified of request did finish for intent, error: %@"
+ "%s Notified of routing status, error: %@"
+ "%s Notified of timeout error: %@"
+ "%s SRD has not implemented updateConversationContextForRemoteResponseWithAssistantId:requestId:fullSpeak:redactedFullSpeak:fullPrint:redactedFullPrint: yet. Ignoring"
+ "%s Session type changed from %d to %d"
+ "%s Session type: %d"
+ "%s Storing xpc event %p in wake store %p"
+ "%s Unable to trigger ABC due to error %@."
+ "%s hasATVOrHomePod=%d hasATV=%d hasHomePod=%d"
+ "%s isDevSupportDisableServerFallbackForMissingAsset: %d, sharingStatus: %@, islongLivedIdUploadEnabled: %d"
+ "-[ADAssistantProperties _getGenAIAgent]"
+ "-[ADAssistantProperties _getIsGenAIEnabled]"
+ "-[ADCommandCenter _errorAggregation:]"
+ "-[ADDictationConnection adSpeechRecordingDidEndWithContext:]"
+ "-[ADDictationSessionTracker _reportSessionAssertion]_block_invoke"
+ "-[ADLocationManager updateLocationSnapshot]"
+ "-[ADMultiUserService getLoggableIdentiferForUserWithSharedUserID:iCloudAltDSID:sessionID:completion:]_block_invoke"
+ "-[ADRequestDispatcherService updateConversationContextForRemoteResponseWithAssistantId:requestId:fullSpeak:redactedFullSpeak:fullPrint:redactedFullPrint:]"
+ "-[ADSessionManager _hasSessionTypeChanged]"
+ "-[ADiOSAssistantProperties _getIsSpokenNotificationsControlCenterModuleEnabledWithCompletion:]_block_invoke"
+ "28"
+ "AssetStatus_"
+ "AtvInHome"
+ "ForceReset"
+ "FullUodCapable"
+ "Has ATV in the home"
+ "Has HomePod(s) in the home"
+ "HomePodInHome"
+ "MobileAssistantDaemons-3405.21.2"
+ "OptedIn"
+ "PairedWatch"
+ "ServerDictationRequired"
+ "SupportsDeviceDictation"
+ "SyncDisabledViaTrial"
+ "_errorAggregation:"
+ "_errorOnionAggregator"
+ "_getGenAIAgent"
+ "_getIsGenAIEnabled"
+ "_hasSessionTypeChanged"
+ "_reportSessionAssertion"
+ "_updateConversationContextFromRemoteCommand:remoteExecutionInfo:"
+ "addGenAIAgentsEnabled:"
+ "deviceHasAtvInHome"
+ "deviceHasHomePodInHome"
+ "dictation"
+ "getGenAIAgent"
+ "getLoggableIdentiferForUserWithSharedUserID:iCloudAltDSID:sessionID:completion:"
+ "https://seed.siri.apple.com"
+ "invalidateDictationAssertion"
+ "preventDeviceFromIdlingIfRequired"
+ "session_assertion"
+ "setConfidence:"
+ "setHasATVInHome:"
+ "setHasHomePodInHome:"
+ "setHeadphoneConnected:"
+ "setSyncModes:"
+ "setUserProfileIdentifier:"
+ "setUserProfileMetadata:"
+ "setXPCEvent:"
+ "stringWithCapacity:"
+ "underlyingErrors"
+ "updateConversationContextForRemoteResponseWithAssistantId:requestId:fullSpeak:redactedFullSpeak:fullPrint:redactedFullPrint:"
+ "userProfileConfidence"
+ "userProfileHeadphoneConnected"
+ "userProfileMetadata"
+ "userProfilePersonaId"
+ "\xf0\xf0\xf0\xf0\xf0\xf0q"
- "\x0f\x0f\x1c\x11\x11\x12+T\x12\x11\x11\x15\x13\x16\x14\x13\x13\x12\x16"
- "%s Asking for anchor keys %@"
- "%s Failed to insert data into Feature Stream with error %@."
- "%s Inserting SAUIAddViews to Feature Store Stream"
- "%s No views in SAUIAddViews present"
- "%s addViewsCommand %@."
- "%s hasATVOrHomePod=%d"
- "%s isDevSupportDisableServerFallbackForMissingAsset: %d, sharingStatus: %@"
- "-[ADAssistantProperties _getIsChatGPTEnabled]"
- "-[ADMultiUserService getLoggableIdentiferForUserWithiCloudAltDSID:sharedUserID:sessionID:completion:]_block_invoke"
- "-[SAUIAddViews(FeatureStoreServices) insertToFeatureStoreStream:error:]"
- "FeatureStoreServices"
- "MobileAssistantDaemons-3404.80.4.11.3"
- "SAAceCommandMessage"
- "_getIsChatGPTEnabled"
- "dictionaryWithObjects:forKeys:"
- "getLoggableIdentiferForUserWithiCloudAltDSID:sharedUserID:sessionID:completion:"
- "getWithStreamId:"
- "initWithContent:interactionId:dataVersion:"
- "insert:error:"
- "insertToFeatureStoreStream:error:"
- "\xf0\xf0\xf0\xf0\xf0\xf0a"

```
