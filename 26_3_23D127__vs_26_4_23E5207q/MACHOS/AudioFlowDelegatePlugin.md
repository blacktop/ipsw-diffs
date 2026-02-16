## AudioFlowDelegatePlugin

> `/System/Library/Assistant/FlowDelegatePlugins/AudioFlowDelegatePlugin.bundle/AudioFlowDelegatePlugin`

```diff

-3510.2.1.0.0
-  __TEXT.__text: 0x2c5ca8
-  __TEXT.__auth_stubs: 0x6e30
+3520.67.3.0.0
+  __TEXT.__text: 0x2b6714
+  __TEXT.__auth_stubs: 0x6ba0
+  __TEXT.__objc_stubs: 0x2f00
   __TEXT.__objc_methlist: 0x6e8
-  __TEXT.__const: 0x9d82
-  __TEXT.__cstring: 0x7a7c
-  __TEXT.__swift5_typeref: 0x40d0
-  __TEXT.__constg_swiftt: 0x5648
+  __TEXT.__const: 0x9f42
+  __TEXT.__cstring: 0x48ac
+  __TEXT.__swift5_typeref: 0x4164
+  __TEXT.__oslogstring: 0x2415c
+  __TEXT.__constg_swiftt: 0x5688
   __TEXT.__swift5_builtin: 0x1a4
-  __TEXT.__swift5_reflstr: 0x3feb
+  __TEXT.__swift5_reflstr: 0x3f8b
   __TEXT.__swift5_assocty: 0xa88
-  __TEXT.__oslogstring: 0x248bc
-  __TEXT.__swift5_proto: 0x47c
-  __TEXT.__swift5_types: 0x328
-  __TEXT.__objc_classname: 0xce
-  __TEXT.__objc_methname: 0x2998
-  __TEXT.__objc_methtype: 0x3ef
-  __TEXT.__swift5_fieldmd: 0x304c
-  __TEXT.__swift5_capture: 0x63ec
+  __TEXT.__swift5_proto: 0x49c
+  __TEXT.__swift5_types: 0x324
+  __TEXT.__objc_classname: 0x1db2
+  __TEXT.__objc_methtype: 0x5ca
+  __TEXT.__objc_methname: 0x3fbd
+  __TEXT.__swift5_fieldmd: 0x3040
+  __TEXT.__swift5_capture: 0x6284
   __TEXT.__swift_as_entry: 0x198
   __TEXT.__swift_as_ret: 0x230
-  __TEXT.__swift5_protos: 0x58
+  __TEXT.__swift5_protos: 0x68
   __TEXT.__swift5_mpenum: 0x20
-  __TEXT.__unwind_info: 0x32d0
-  __TEXT.__eh_frame: 0x3460
-  __DATA_CONST.__auth_got: 0x3718
-  __DATA_CONST.__got: 0x1e50
-  __DATA_CONST.__auth_ptr: 0x1a40
-  __DATA_CONST.__const: 0xf568
-  __DATA_CONST.__objc_classlist: 0x2c0
+  __TEXT.__unwind_info: 0x3158
+  __TEXT.__eh_frame: 0x3120
+  __DATA_CONST.__auth_got: 0x35d8
+  __DATA_CONST.__got: 0x1e10
+  __DATA_CONST.__auth_ptr: 0x1a58
+  __DATA_CONST.__const: 0xef90
+  __DATA_CONST.__objc_classlist: 0x2b8
   __DATA_CONST.__objc_protolist: 0xd8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x70
-  __DATA.__objc_const: 0x9ec0
-  __DATA.__objc_selrefs: 0xdb0
-  __DATA.__objc_data: 0x12a8
-  __DATA.__data: 0xb8c8
-  __DATA.__bss: 0x7d10
-  __DATA.__common: 0x470
+  __DATA.__objc_const: 0x9db0
+  __DATA.__objc_selrefs: 0xdc0
+  __DATA.__objc_data: 0x1258
+  __DATA.__data: 0xb780
+  __DATA.__bss: 0x7f10
+  __DATA.__common: 0x438
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
+  - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreSpotlight.framework/CoreSpotlight
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 50B5DE1B-9772-37A3-A243-D4435CEF5DE3
-  Functions: 5569
-  Symbols:   377
-  CStrings:  3030
+  UUID: FD4F0C4A-ED99-3388-8E43-104527055908
+  Functions: 5489
+  Symbols:   374
+  CStrings:  2975
 
Symbols:
- _OBJC_CLASS_$_NSString
- _malloc
- _swift_unknownObjectRelease_n
CStrings:
+ "AmbiguousPlayFlow#on Unsupported DirectInovaction"
+ "AppResolutionCommonStrategy#makeAppResolutionStateFromParse received unsupported directInvocation: %s, DI: %s"
+ "AudioFlowDelegatePlugin#makeFlow Got unsupported DirectInvocation parse"
+ "ConverterHelpers#convertMediaDestination correcting destination playlist name from %s to: %s"
+ "ConverterHelpers#convertMediaDestination mentioned playlist name: %s"
+ "DetermineIntent"
+ "DetermineIntentResponse"
+ "DetermineNowPlayingIntentInfoResolutionResult"
+ "INPlayMediaIntent#amend unable to construct AudioUsoIntent from builder"
+ "MediaItemDisambiguationStrategy#makeAppResolutionStateFromParse received unsupported directInvocation: %s"
+ "NowPlayingIntentInfo"
+ "NowPlayingIntentInfoResolutionResult"
+ "Parse#playMediaIntent Ignoring non-server-conversion parse"
+ "Parse#playMediaIntent Unable to get INPlayMediaIntent from unsupported direct invocation use case %s"
+ "Parse#playMediaIntent unable to get INPlayMediaIntent from parse"
+ "Parse+Extension#firstUserDialogAct No user dialog act found in userParse."
+ "Parse+Extension#firstUserDialogAct PlayMediaShim directInvocation doesn't contain audioExperience %s"
+ "Parse+Extension#firstUserDialogAct PommesResponse doesn't contain audioExperience %s"
+ "Parse+Extension#firstUsoTask Could not convert user dialog act to task."
+ "Parse+Extension#firstUsoTask No tasks found in input"
+ "Parse+Extension#firstUsoTask No user dialog act found in userParse."
+ "PlayMediaAppResolver#postResolve adding MediaItems to PlayMediaIntent for Apple Music Classical playback: %s"
+ "PlayeMediaDialogProvider#invalidTokensHelper sign into Podcasts account required"
+ "QueueLocationResolutionResult"
+ "RequestTypeResolutionResult"
+ "SignIntoPodcastsAccount"
+ "Unrecognized playbackQueueLocation: %ld"
+ "UpdateMediaAffinityFlowStrategy#makeIntentFromParse received unsupported parse"
+ "WHADialogMetadata"
+ "WHADialogMetadataResolutionResult"
+ "WHAErrorResolutionResult"
+ "playlistName"
+ "sharedUserID"
- "AppResolutionCommonStrategy#makeAppResolutionStateFromParse received unsupported directInvocation: %s"
- "AppResolutionStrategy#makeAppResolutionStateFromParse received unsupported directInvocation: %s"
- "AppSelectionContext#saveRecord %{public}s info: %s, resolution result type: %s, recording to SELF..."
- "AppSelectionContext#saveRecord %{public}s no context present for refId: %{public}s"
- "AppSelectionContext#saveRecord %{public}s no rawSignalResult present for refId: %{public}s"
- "AppSelectionContext#saveRecord %{public}s saved record with UUID: %s"
- "AppSelectionContext#saveRecord context present, with report?:%{bool}d and rawSignalResult?:%{bool}d"
- "AppSelectionContext#saveRecord setting appSelectionLastUsed"
- "AppSelectionContext#saveRecord setting lastBundleIdentifier=%s"
- "AppSelectionContext#saveRecord unexpected failed to save record to SELF, uuid nil"
- "ConverterHelpers#convertMediaDestination correcting to destination playlist: %s"
- "ConverterHelpers#convertMediaDestination targetPlaylists: %s"
- "ConverterHelpers#convertPlaybackQueueLocation unrecognized playbackQueueLocation: %ld"
- "ConverterHelpers#convertPrivateMediaIntentData AudioExperience.multiuserContext sharedUserID: %s, userIdentificationClassification: %ld, speakerIDConfidence: %ld"
- "INAddMediaIntent#amend unable to construct AudioUsoIntent from userDialogAct: %s"
- "INPlayMediaIntent#amend unable to construct AudioUsoIntent from userDialogAct: %s"
- "INSearchForMediaIntent#amend unable to construct AudioUsoIntent from userDialogAct: %s"
- "Only DirectInvocation from PlayMediaShim is supported"
- "PlayMediaAppResolutionService#resolveBundleIdentifier disambiguating apps: %s"
- "PlayMediaAppResolver#determineFirstPartyBundleIdentifier encountered error getting now playing bundle. Falling back to allow use of Classical"
- "PlayMediaAppResolver#determineFirstPartyBundleIdentifier we have signal from search results to consider using Classical for playback"
- "PlayMediaAppResolver#forcedResolution disambiguating apps: %s"
- "PlayMediaAppResolver#forcedResolution firstPartyDisambiguate?:%{bool}d --- default apps test. contains3p?:%{bool}d audiobook?:%{bool}d firstPartyRateTest?:%{bool}d repeatedCancelled?:%{bool}d"
- "PlayMediaAppResolver#forcedResolution forced disambiguation test?: %{bool}d ---- repeatedCancelled?: %{bool}d disambiguationEnabled?:%{bool}d, appInferred?:%{bool}d, bundleIdentifierIsSentinel?:%{bool}d, rateTest?:%{bool}d, disambiguationElapsed?:%f, interactionFrequencyTest?:%{bool}d disambiguateAlways?:%{bool}d, recordStoringPermitted?:%{bool}d,rateRoll:%f, rateRoll1p:%f"
- "PlayMediaAppResolver#forcedResolution found this request as repeated, inferred, recent followup to the prior intent: %s resulting in a cancelled result after app selection used"
- "PlayMediaAppResolver#forcedResolution rates - disambiguationRate:%f, disambiguationAdditionalRateFirstParty:%f, rateLimitSeconds:%ld"
- "PlayMediaAppResolver#forcedResolution recording result analytics data due to disambiguation result: %s"
- "PlayMediaAppResolver#forcedResolution..."
- "PlayMediaAppResolver#postResolve %{public}s recording app selection signals. force?:%{bool}d"
- "PlayMediaAppResolver#postResolve adding MediaItems to PlayMediaIntent for Apple Music Classical playback"
- "PlayMediaIntent#DalPodcastPromotion"
- "PlayMediaIntent#HandleFailureThirdParty"
- "PriorResultContext#update set prior result context for refId: %s"
- "UpdateMediaAffinityFlowStrategy#makeIntentFromParse received non NLv3IntentPlusServerConversion or NLv3IntentOnly parse"
- "_TtC23AudioFlowDelegatePlugin18PriorResultContext"
- "appSelectionUsed"
- "previousDisambiguationCancelled"
- "requestCancelled"
- "siriKitResponseCode"
- "time"

```
