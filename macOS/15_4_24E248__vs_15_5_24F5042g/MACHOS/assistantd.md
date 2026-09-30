## assistantd

> `/System/Library/PrivateFrameworks/AssistantServices.framework/Versions/A/Support/assistantd`

```diff

-3404.80.4.0.0
-  __TEXT.__text: 0x503cc8
-  __TEXT.__auth_stubs: 0x2e90
-  __TEXT.__objc_stubs: 0x40700
-  __TEXT.__objc_methlist: 0x209bc
-  __TEXT.__cstring: 0x48815
+3405.21.2.0.0
+  __TEXT.__text: 0x504c30
+  __TEXT.__auth_stubs: 0x2ea0
+  __TEXT.__objc_stubs: 0x40940
+  __TEXT.__objc_methlist: 0x20a2c
+  __TEXT.__cstring: 0x48a61
   __TEXT.__const: 0xab7d8
   __TEXT.__dlopen_cstrs: 0x612
   __TEXT.__gcc_except_tab: 0x3c84
-  __TEXT.__objc_classname: 0x4e38
-  __TEXT.__objc_methname: 0x57455
+  __TEXT.__objc_classname: 0x4e23
+  __TEXT.__objc_methname: 0x576a4
   __TEXT.__objc_methtype: 0xe2db
-  __TEXT.__oslogstring: 0x38640
+  __TEXT.__oslogstring: 0x387f9
   __TEXT.__ustring: 0x2b0
   __TEXT.__unwind_info: 0x9660
   __TEXT.__eh_frame: 0x108
-  __DATA_CONST.__auth_got: 0x1758
-  __DATA_CONST.__got: 0x3690
+  __DATA_CONST.__auth_got: 0x1760
+  __DATA_CONST.__got: 0x3698
   __DATA_CONST.__auth_ptr: 0x20
-  __DATA_CONST.__const: 0x24e98
-  __DATA_CONST.__cfstring: 0x119e0
+  __DATA_CONST.__const: 0x24eb8
+  __DATA_CONST.__cfstring: 0x11b60
   __DATA_CONST.__objc_classlist: 0xcb0
   __DATA_CONST.__objc_catlist: 0x630
   __DATA_CONST.__objc_protolist: 0x670
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x90
   __DATA_CONST.__objc_superrefs: 0xaa8
-  __DATA_CONST.__objc_arraydata: 0x370
-  __DATA_CONST.__objc_arrayobj: 0x1b0
+  __DATA_CONST.__objc_arraydata: 0x358
+  __DATA_CONST.__objc_arrayobj: 0x198
   __DATA_CONST.__objc_intobj: 0x738
   __DATA_CONST.__objc_dictobj: 0x2d0
   __DATA_CONST.__objc_doubleobj: 0x20
   __DATA_CONST.__objc_floatobj: 0x30
-  __DATA.__objc_const: 0x31480
-  __DATA.__objc_selrefs: 0x131f8
-  __DATA.__objc_ivar: 0x23d0
+  __DATA.__objc_const: 0x314c0
+  __DATA.__objc_selrefs: 0x132a0
+  __DATA.__objc_ivar: 0x23d8
   __DATA.__objc_data: 0x7ee0
   __DATA.__data: 0x5240
   __DATA.__bss: 0xa18

   - /System/Library/PrivateFrameworks/CoreKnowledge.framework/Versions/A/CoreKnowledge
   - /System/Library/PrivateFrameworks/CoreSpeech.framework/Versions/A/CoreSpeech
   - /System/Library/PrivateFrameworks/DialogEngine.framework/Versions/A/DialogEngine
-  - /System/Library/PrivateFrameworks/FeatureStore.framework/Versions/A/FeatureStore
   - /System/Library/PrivateFrameworks/FeedbackLogger.framework/Versions/A/FeedbackLogger
   - /System/Library/PrivateFrameworks/GenerativeAssistantSettings.framework/Versions/A/GenerativeAssistantSettings
   - /System/Library/PrivateFrameworks/GeoServices.framework/Versions/A/GeoServices

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libresolv.9.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 13565
-  Symbols:   2648
-  CStrings:  25009
+  Functions: 13577
+  Symbols:   2650
+  CStrings:  25057
 
Symbols:
+ _AFRequiredAssetsForFullUOD
+ _NSMultipleUnderlyingErrorsKey
+ _OBJC_CLASS_$_SMTUserProfileMetadata
+ _OBJC_CLASS_$_SRDRemoteIFClientWakeStore
- _OBJC_CLASS_$_FSFCurareInteractionAsDict
- _OBJC_CLASS_$_FSFCurareInteractionStream
CStrings:
+ "\x0f\x0e\x1c\x11\x11\x12,T\x12\x11\x11\x15\x13\x16\x14\x12\x13\x12\x16"
+ "%s #ODD: genAIAgent=%d"
+ "%s #hal Pushing location for AssistantID: %@ %@"
+ "%s #hal Pushing location for IDS: %@ %@"
+ "%s #hal Updating location snapshot with %@"
+ "%s #shih updating SMTRequestContextData %@"
+ "%s Asking for anchor keys=%@"
+ "%s Dictation transaction ended! resuming idle timer"
+ "%s Embedded error: %@"
+ "%s SRD has not implemented updateConversationContextForRemoteResponseWithAssistantId:requestId:fullSpeak:redactedFullSpeak:fullPrint:redactedFullPrint: yet. Ignoring"
+ "%s Session type changed from %d to %d"
+ "%s Session type: %d"
+ "%s Storing xpc event %p in wake store %p"
+ "%s Unable to trigger ABC due to error %@."
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
+ "24"
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
+ "cacheKeysLock"
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
+ "\xf0\xf0\xf0\xf0\xf0\xf0a"
- "\x0f\x0e\x1c\x11\x11\x12+T\x12\x11\x11\x15\x13\x16\x14\x12\x13\x12\x16"
- "%s Asking for anchor keys %@"
- "%s Failed to insert data into Feature Stream with error %@."
- "%s Inserting SAUIAddViews to Feature Store Stream"
- "%s No views in SAUIAddViews present"
- "%s addViewsCommand %@."
- "%s isDevSupportDisableServerFallbackForMissingAsset: %d, sharingStatus: %@"
- "-[ADAssistantProperties _getIsChatGPTEnabled]"
- "-[ADMultiUserService getLoggableIdentiferForUserWithiCloudAltDSID:sharedUserID:sessionID:completion:]_block_invoke"
- "-[SAUIAddViews(FeatureStoreServices) insertToFeatureStoreStream:error:]"
- "94"
- "FeatureStoreServices"
- "MobileAssistantDaemons-3404.80.4"
- "SAAceCommandMessage"
- "_getIsChatGPTEnabled"
- "dictionaryWithObjects:forKeys:"
- "getLoggableIdentiferForUserWithiCloudAltDSID:sharedUserID:sessionID:completion:"
- "getWithStreamId:"
- "initWithContent:interactionId:dataVersion:"
- "insert:error:"
- "insertToFeatureStoreStream:error:"
- "\xf0\xf0\xf0\xf0\xf0\xf0Q"

```
