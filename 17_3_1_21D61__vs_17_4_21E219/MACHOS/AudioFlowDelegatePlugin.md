## AudioFlowDelegatePlugin

> `/System/Library/Assistant/FlowDelegatePlugins/AudioFlowDelegatePlugin.bundle/AudioFlowDelegatePlugin`

```diff

-3303.9.1.0.0
-  __TEXT.__text: 0x28a678
-  __TEXT.__auth_stubs: 0x5cc0
+3304.71.3.1.1
+  __TEXT.__text: 0x299940
+  __TEXT.__auth_stubs: 0x5f00
   __TEXT.__objc_methlist: 0x35c
-  __TEXT.__const: 0x8cd2
-  __TEXT.__swift5_typeref: 0x42e6
-  __TEXT.__cstring: 0x26eec
-  __TEXT.__constg_swiftt: 0x5b34
+  __TEXT.__const: 0x97f2
+  __TEXT.__cstring: 0x2768c
+  __TEXT.__swift5_typeref: 0x4472
+  __TEXT.__constg_swiftt: 0x5c2c
   __TEXT.__swift5_builtin: 0x168
-  __TEXT.__swift5_reflstr: 0x49a1
-  __TEXT.__swift5_assocty: 0xb20
-  __TEXT.__swift5_proto: 0x4e0
-  __TEXT.__swift5_types: 0x340
+  __TEXT.__swift5_reflstr: 0x49b1
+  __TEXT.__swift5_assocty: 0xb60
+  __TEXT.__swift5_proto: 0x4f8
+  __TEXT.__swift5_types: 0x348
   __TEXT.__objc_classname: 0xce
-  __TEXT.__objc_methname: 0x2684
+  __TEXT.__objc_methname: 0x269a
   __TEXT.__objc_methtype: 0x3ef
-  __TEXT.__swift5_fieldmd: 0x3864
-  __TEXT.__swift5_capture: 0x3a90
+  __TEXT.__swift5_fieldmd: 0x38cc
+  __TEXT.__swift5_capture: 0x3d84
   __TEXT.__swift5_protos: 0x54
   __TEXT.__swift5_mpenum: 0x20
-  __TEXT.__unwind_info: 0x4430
-  __TEXT.__eh_frame: 0x3140
-  __DATA_CONST.__auth_got: 0x2e60
-  __DATA_CONST.__got: 0x16c0
-  __DATA_CONST.__auth_ptr: 0x3d8
-  __DATA_CONST.__const: 0xf088
+  __TEXT.__unwind_info: 0x4538
+  __TEXT.__eh_frame: 0x3288
+  __DATA_CONST.__auth_got: 0x2f80
+  __DATA_CONST.__got: 0x1618
+  __DATA_CONST.__auth_ptr: 0x410
+  __DATA_CONST.__const: 0xfbd8
   __DATA_CONST.__objc_classlist: 0x2b8
   __DATA_CONST.__objc_protolist: 0xd8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_const: 0x98e8
+  __DATA_CONST.__objc_protorefs: 0x70
+  __DATA_CONST.__objc_classrefs: 0x310
+  __DATA.__objc_const: 0x9968
   __DATA.__objc_selrefs: 0xc58
-  __DATA.__objc_protorefs: 0x70
-  __DATA.__objc_classrefs: 0x310
   __DATA.__objc_data: 0x1200
-  __DATA.__data: 0xe0d8
-  __DATA.__bss: 0x8990
-  __DATA.__common: 0x380
+  __DATA.__data: 0xe558
+  __DATA.__bss: 0x8d10
+  __DATA.__common: 0x428
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreSpotlight.framework/CoreSpotlight

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: E7743CE5-CB95-30FB-9664-0BB62BDC66C2
-  Functions: 6918
-  Symbols:   353
-  CStrings:  2853
+  UUID: ADFABCE5-2F8C-31A2-833A-C77A12A484BD
+  Functions: 7135
+  Symbols:   351
+  CStrings:  2894
 
Symbols:
- _objc_retain_x10
- _objc_retain_x11
CStrings:
+ "#### PlayMediaRCHFlowWrapper#saveToSiriMemory called at: %s and dateInterval: %s"
+ ".appResolutionFailed"
+ ".awaitingResolution"
+ "AddMediaNeedsValueStrategy#actionForInput parse not of right type"
+ "AddMediaNeedsValueStrategy#parseResponseValue and AddMediaNeedsValueStrategy#actionForInput parse handling need to be the same!"
+ "AmbiguousPlayFlow#execute found content in the music queue, looking to resume it"
+ "AmbiguousPlayFlow#execute no content in the music queue, looking to shuffle local library"
+ "AmbiguousPlayFlow#execute no input available"
+ "AmbiguousPlayFlow#execute#getMRInfo"
+ "AmbiguousPlayFlow#executeFlow This is a SiriForAirPlay request, pushing the next play flow directly without calling ControlsFlowProvider"
+ "AmbiguousPlayFlow#executeFlow has previously been rejected by controls, executing next flow"
+ "AmbiguousPlayFlow#nextFlow"
+ "AppResolutionAction#from confirm %s"
+ "AppResolutionAction#from disambiguate %s"
+ "AppResolutionAction#from selected %s"
+ "AppResolutionAction#from unkown state, return .noAppFound"
+ "AppResolutionAction#from unsuccessful. Error %@"
+ "AppResolutionCommonStrategy#createRowCardSectionWithCommand Creating RowCardSection with command %s title %s"
+ "AppResolutionCommonStrategy#generateCommandForAppConcept cannot construct rske for app: %s"
+ "AppResolutionCommonStrategy#makeAppResolutionStateFromParse %s"
+ "AppResolutionCommonStrategy#makeAppResolutionStateFromParse AudioUsoIntent failed to be constructed"
+ "AppResolutionCommonStrategy#makeAppResolutionStateFromParse Could not get app bundle id from .replayRequest direct invocation"
+ "AppResolutionCommonStrategy#makeAppResolutionStateFromParse Failed to get task from parse"
+ "AppResolutionCommonStrategy#makeAppResolutionStateFromParse pommesResponse contains invalid appBundleId in disambiguation response and invalid launchID %s"
+ "AppResolutionCommonStrategy#makeAppResolutionStateFromParse pommesResponse contains no AudioExperience"
+ "AppResolutionCommonStrategy#makeAppResolutionStateFromParse pommesResponse resolving app from AudioIntent %s"
+ "AppResolutionCommonStrategy#makeAppResolutionStateFromParse pommesResponse resolving app from launchID %s"
+ "AppResolutionCommonStrategy#makeAppResolutionStateFromParse pommesResponse userDialogAct: %s"
+ "AppResolutionCommonStrategy#makeAppResolutionStateFromParse received unsupported directInvocation: %s"
+ "AppResolutionCommonStrategy#makeAppResolutionStateFromParse returning NilAppResolutionProvider for uso Affinity task"
+ "AppResolutionCommonStrategy#makeAppResolutionStateFromParse returning UsoAppResolutionProvider for uso parse"
+ "AppResolutionCommonStrategy#makeAppResolutionStateFromParse unsupported parse"
+ "AppResolutionCommonStrategy#makeAppResolutionUnsuccessfulResponse Intent is PodcastPromotion."
+ "AppResolutionCommonStrategy#makeAppResolutionUnsuccessfulResponse Intent is SiriForAirPlay with launchID: %@"
+ "AppResolutionCommonStrategy#makeAppResolutionUnsuccessfulResponse error evaluating failure template"
+ "AppResolutionCommonStrategy#makeAppResolutionUnsuccessfulResponse intent: %s, reason:%s"
+ "AppResolutionCommonStrategy#makeAppResolutionUnsuccessfulResponse non-play or non-lyrics or non-appNotSupported, using default rendering..."
+ "AppResolutionCommonStrategy#makeAppResolutionUnsuccessfulResponse unsupported lyrics search, building custom error dialog"
+ "AppResolutionCommonStrategy#makeOpenAppButton error creating open app label"
+ "AppResolutionCommonStrategy#makeOpenAppButton error resolving display name for app: %{public}s"
+ "AppResolutionCommonStrategy#makePromptForConfirmation makeNLContextProvider returned: %s"
+ "AppResolutionCommonStrategy#makePromptForConfirmation missing confirmApp template"
+ "AppResolutionCommonStrategy#makePromptForConfirmation..."
+ "AppResolutionCommonStrategy#makePromptForDisambiguation %{public}s pym built and set SADialog printedOnly:%{bool,public}d, spokenOnly:%{bool,public}d, caption:%{public}@, content:%{public}@, dialogIdentifier:%{public}@, listenAfterSpeaking: %@"
+ "AppResolutionCommonStrategy#makePromptForDisambiguation CarPlay view print:%s, speak:%s"
+ "AppResolutionCommonStrategy#makePromptForDisambiguation makeNLContextProvider returned: %s"
+ "AppResolutionCommonStrategy#makePromptForDisambiguation missing disambiguateApps template"
+ "AppResolutionCommonStrategy#makePromptForDisambiguation ordered: %s"
+ "AppResolutionCommonStrategy#makePromptForDisambiguation using CarPlay dialog-only views. From template:: print:%s, speak:%s"
+ "AppResolutionCommonStrategy#makePromptForDisambiguation using legacy snippet"
+ "AppResolutionCommonStrategy#makePromptForDisambiguation using pym-compatible snippet"
+ "AppResolutionCommonStrategy#makePromptForDisambiguation views: %s"
+ "AppResolutionCommonStrategy#makePromptForDisambiguation with apps: %s, intent: %s"
+ "AppResolutionFlow#execute skipping for non-tvOS platform not capable of remote execution. App prediction will run later as part of RCH"
+ "AppResolutionFlow#on Handling input"
+ "AppResolutionOnDeviceStrategy#parseConfirmationResponse needs implementing"
+ "AppResolutionOnDeviceStrategy#resolveApp Resolving app with input: %s"
+ "AppResolutionOnDeviceStrategy.parseDisambiguationResponse"
+ "AppResolutionOnDeviceStrategy.resolveApp"
+ "AppResolutionStrategy#parseDisambiguationResponse App Resolution state found app: %s"
+ "AppResolutionStrategy#parseDisambiguationResponse App resolution resulted in a failure. Error: %s"
+ "AppResolutionStrategy#parseDisambiguationResponse Done, returning disambiguation response: %s"
+ "AppResolutionStrategy#parseDisambiguationResponse applying app to intent after disambiguation"
+ "AppResolutionStrategy#parseDisambiguationResponse error getting app: %@"
+ "AppResolutionStrategy#parseDisambiguationResponse for input: %s"
+ "AppResolutionStrategy#parseDisambiguationResponse success"
+ "AppResolutionStrategy#parseDisambiguationResponse success with app: %@"
+ "AppResolutionStrategy#parseDisambiguationResponse unexpected resopnse: %s"
+ "AppResolutionStrategy#resolveApp App resolution resulted in a failure. Error: %s"
+ "AppResolutionStrategy#resolveApp Unable to get SiriKit intent from parse"
+ "AppResolutionStrategy#resolveApp returning result %s"
+ "AppResolutionStrategy#resolveApp success"
+ "AppSelectionContext#saveRecord %{public}s info: %s, resolution result type: %s, recording to SELF..."
+ "AppSelectionContext#saveRecord %{public}s no context present for refId: %{public}s"
+ "AppSelectionContext#saveRecord %{public}s no rawSignalResult present for refId: %{public}s"
+ "AppSelectionContext#saveRecord %{public}s saved record with UUID: %s"
+ "AppSelectionContext#saveRecord context present, with report?:%{bool}d and rawSignalResult?:%{bool}d"
+ "AppSelectionContext#saveRecord setting appSelectionLastUsed"
+ "AppSelectionContext#saveRecord setting lastBundleIdentifier=%s"
+ "AppSelectionContext#saveRecord unexpected failed to save record to SELF, uuid nil"
+ "AudioAppResolutionFlow#makeAppResolutinoFlow no app resolution flow returned"
+ "AudioFlowDelegatePlugin#makeFlow"
+ "AudioFlowDelegatePlugin#makeFlow Unexpected intent"
+ "AudioFlowDelegatePlugin#makeFlow unexpected parse type. Rejecting..."
+ "AudioFlowDelegatePlugin/AppResolutionCommonStrategy.swift"
+ "Can't construct Array with count < 0"
+ "Cannot cast intent as PrivateMediaIntentDataProviding"
+ "CatService#execute responseLanguageVariant %@ from SiriEnvironment's currentRequest overrides original siriLocale"
+ "CommonAppResolver.resolveApp"
+ "CommonAppResolver.resolveSelectedApp"
+ "CommonAppResolver.resolveSelectedApp.lyrics"
+ "CommonAppResolver.resolveSelectedApp.notInstalled"
+ "CommonFlowStrategy#makeErrorResponse Barge-In error"
+ "CommonFlowStrategy#makeErrorResponse FAILED to create BargeIn error dialog"
+ "CommonFlowStrategy#makeErrorResponse FAILED to create generic error dialog"
+ "CommonFlowStrategy#makeErrorResponse successfully created BargeIn error dialog"
+ "CommonFlowStrategy#makeErrorResponse successfully created generic error dialog"
+ "CommonIntentAppResolver#resolveApp persisting resolution result with bundleID: %s and resolutionResultType: %s in intent: %@"
+ "CommonIntentAppResolver#resolveSelectedApp Removing the launchID from the intent"
+ "CommonMedia#makeSiriKitIntentHandler not for 1p music or podcasts (or radio on watch). Bundle: %@, intent launchId: %@"
+ "ConfirmationViewProvider#makeYesNoConfirmationViews Creating confirmation views"
+ "ConverterHelpers#convertIntentMetadata Setting launchId to: %s"
+ "DirectActionAudioSearchFlow#execute.postPrompt"
+ "DisplayApp#init Empty bundleIDs, looking in installed apps: %s"
+ "DisplayApp#init overriding empty displayName with:%s for identifier:%s"
+ "Division by zero"
+ "Division results in an overflow"
+ "EndpointConnectionFailedOnHomePod"
+ "ExecuteMusicOnRemoteFlow#execute saving app selection record..."
+ "Fatal: cannot case intent as PrivateMediaIntentDataProviding"
+ "Index out of range"
+ "Insufficient space allocated to copy string contents"
+ "NLv3IntentUnhandled"
+ "NoControlsFlowForParse"
+ "PlayMediaAppResolver#postResolve No requestID found for the current request. Skipping log collection for intent"
+ "PlayMediaAppResolver#postResolve SELF logs already collected for this request. Avoiding double logging"
+ "PlayMediaAppResolver#postResolve Storing intent for request: %s, stored: %s"
+ "PlayMediaAppResolver#resolveBundleIdentifier app resolution ran previously, re-using those results and returning bundleIdentifier: %{public}s, resolutionResult: %{public}s"
+ "PlayMediaNeedsValueStrategy#actionForInput parse not of right type"
+ "PlayMediaNeedsValueStrategy#actionForInput..."
+ "PlayMediaNeedsValueStrategy#parseResponseValue and PlayMediaNeedsValueStrategy#actionForInput parse handling need to be the same!"
+ "PlayMediaRCHFlowWrapper#appSelectionRecord Saving..."
+ "PlayMediaRCHFlowWrapper#appSelectionRecord unable to get RCH result"
+ "PlayMediaRCHFlowWrapper#dialogForError capturing non special case applicationTerminated"
+ "PlayMediaRCHFlowWrapper#dialogForError using special dialog (musicCellularDataOff) for unsupportMediaItemsCellularDataSettings code"
+ "PlayMediaRCHFlowWrapper#dialogForError using special dialog for radioRestrictedLocation code"
+ "PommesResponseFlow#execute forwarding to first audio play flow"
+ "RadioRestrictedLocation"
+ "Range requires lowerBound <= upperBound"
+ "SearchForMediaNeedsValueStrategy#actionForInput parse not of right type"
+ "SearchForMediaNeedsValueStrategy#actionForInput..."
+ "SearchForMediaNeedsValueStrategy#parseResponseValue and SearchForMediaNeedsValueStrategy#actionForInput parse handling need to be the same!"
+ "SiriForAirPlayFlow#getLocalExecuteResponse"
+ "Swift/Array.swift"
+ "Swift/ContiguousArrayBuffer.swift"
+ "Swift/IntegerTypes.swift"
+ "Swift/Range.swift"
+ "Swift/StringTesting.swift"
+ "Swift/StringUTF8View.swift"
+ "Swift/UnsafeBufferPointer.swift"
+ "Swift/UnsafePointer.swift"
+ "Swift/UnsafeRawBufferPointer.swift"
+ "Swift/UnsafeRawPointer.swift"
+ "T@\"NSString\",?,R,C"
+ "Unable to get to the original intent, returning error"
+ "UnexpectedIntent"
+ "UnexpectedParseType"
+ "Unexpectedly found nil while unwrapping an Optional value"
+ "UnsafeMutableBufferPointer with negative count"
+ "UnsafeMutablePointer.initialize overlapping range"
+ "UnsafeMutablePointer.initialize with negative count"
+ "UnsafeMutablePointer.moveInitialize with negative count"
+ "UnsafeMutableRawBufferPointer.copyMemory source has too many elements"
+ "UnsafeMutableRawPointer.initializeMemory overlapping range"
+ "UpdateMediaAffinityNeedsValueStrategy#actionForInput parse not of right type"
+ "UpdateMediaAffinityNeedsValueStrategy#actionForInput..."
+ "UpdateMediaAffinityNeedsValueStrategy#parseResponseValue and UpdateMediaAffinityNeedsValueStrategy#actionForInput parse handling need to be the same!"
+ "_TtC23AudioFlowDelegatePlugin22AudioAppResolutionFlow"
+ "_TtC23AudioFlowDelegatePluginP33_6C20A760FD36F944A8750A31376512C229InternalRenderingFlowStrategy"
+ "appResolutionFlowProducer"
+ "appResolutionOnDeviceResolveApp"
+ "appResolver"
+ "appSelectionUsed"
+ "applyResolvedAppToIntentAfterDisambiguation"
+ "commonAppResolver"
+ "intent"
+ "invalid Collection: less than 'count' elements in collection"
+ "makeAmbiguousPlayFlowFailed - "
+ "name=%{signpost.telemetry:string1,public}@ enableTelemetry=YES "
+ "nextAppAcceptingFlow"
+ "noPreResolvedApp"
+ "noSpeakerFoundErrorResponse"
+ "originalIntent"
+ "playMediaAppResolutionServiceResolveBundleEverything"
+ "postResolve"
+ "requestCancelled"
+ "resolveSelectedApp"
+ "setDateInterval:"
- "%s %{public}s"
- "AmbiguousPlayFlow#execute no flow received from controls for NLv4IntentOnly parse."
- "AmbiguousPlayFlow#executeFlow has previously been rejected by controls, executing ConfirmInterruptionFlow"
- "AppResolutionStrategy#createRowCardSectionWithCommand Creating RowCardSection with command %s title %s"
- "AppResolutionStrategy#generateCommandForAppConcept cannot construct rske for app: %s"
- "AppResolutionStrategy#makeAppResolutionStateFromParse AudioUsoIntent failed to be constructed"
- "AppResolutionStrategy#makeAppResolutionStateFromParse Could not get app bundle id from .replayRequest direct invocation"
- "AppResolutionStrategy#makeAppResolutionStateFromParse Failed to get task from parse"
- "AppResolutionStrategy#makeAppResolutionStateFromParse pommesResponse contains invalid appBundleId in disambiguation response and invalid launchID %s"
- "AppResolutionStrategy#makeAppResolutionStateFromParse pommesResponse contains no AudioExperience"
- "AppResolutionStrategy#makeAppResolutionStateFromParse pommesResponse resolving app from AudioIntent %s"
- "AppResolutionStrategy#makeAppResolutionStateFromParse pommesResponse resolving app from launchID %s"
- "AppResolutionStrategy#makeAppResolutionStateFromParse pommesResponse userDialogAct: %s"
- "AppResolutionStrategy#makeAppResolutionStateFromParse returning NilAppResolutionProvider for uso Affinity task"
- "AppResolutionStrategy#makeAppResolutionStateFromParse returning UsoAppResolutionProvider for uso parse"
- "AppResolutionStrategy#makeAppResolutionStateFromParse unsupported parse"
- "AppResolutionStrategy#makeAppResolutionUnsuccessfulResponse Intent is PodcastPromotion."
- "AppResolutionStrategy#makeAppResolutionUnsuccessfulResponse Intent is SiriForAirPlay with launchID: %@"
- "AppResolutionStrategy#makeAppResolutionUnsuccessfulResponse error evaluating failure template"
- "AppResolutionStrategy#makeAppResolutionUnsuccessfulResponse intent: %s, reason:%s"
- "AppResolutionStrategy#makeAppResolutionUnsuccessfulResponse non-play or non-lyrics or non-appNotSupported, using default rendering..."
- "AppResolutionStrategy#makeAppResolutionUnsuccessfulResponse unsupported lyrics search, building custom error dialog"
- "AppResolutionStrategy#makeOpenAppButton error creating open app label"
- "AppResolutionStrategy#makeOpenAppButton error resolving display name for app: %{public}s"
- "AppResolutionStrategy#makePromptForConfirmation makeNLContextProvider returned: %s"
- "AppResolutionStrategy#makePromptForConfirmation missing confirmApp template"
- "AppResolutionStrategy#makePromptForConfirmation..."
- "AppResolutionStrategy#makePromptForDisambiguation %{public}s pym built and set SADialog printedOnly:%{bool,public}d, spokenOnly:%{bool,public}d, caption:%{public}@, content:%{public}@, dialogIdentifier:%{public}@, listenAfterSpeaking: %@"
- "AppResolutionStrategy#makePromptForDisambiguation CarPlay view print:%s, speak:%s"
- "AppResolutionStrategy#makePromptForDisambiguation makeNLContextProvider returned: %s"
- "AppResolutionStrategy#makePromptForDisambiguation missing disambiguateApps template"
- "AppResolutionStrategy#makePromptForDisambiguation ordered: %s"
- "AppResolutionStrategy#makePromptForDisambiguation using CarPlay dialog-only views. From template:: print:%s, speak:%s"
- "AppResolutionStrategy#makePromptForDisambiguation using legacy snippet"
- "AppResolutionStrategy#makePromptForDisambiguation using pym-compatible snippet"
- "AppResolutionStrategy#makePromptForDisambiguation views: %s"
- "AppResolutionStrategy#makePromptForDisambiguation with apps: %s"
- "Apple Music Preview"
- "AudioFlowDelegatePlugin#makeFlow %{public}s Returning siriMusicFeatureFlow from audio plugin"
- "AudioFlowDelegatePlugin#warmup MediaPlaybackLite#warm skipping warming due to gdprNeeded=true"
- "AudioFlowDelegatePlugin#warmup skipping installed apps warmup on multiuser platform"
- "AudioFlowDelegatePlugin/AppResolutionStrategy.swift"
- "AudioFlowDelegatePlugin/AudioFlowDelegatePlugin.swift"
- "CommonDialogProvider#makeGdprHandoffNeeded Using GDPR handoff for non GDPR implicit recommendation preview starter. Supressing the confirmation dialog."
- "CommonIntentAppResolver#resolveApp %{public}s requestedApp:%{public}s, launchId:%{public}s"
- "CommonMedia#makeSiriKitIntentHandler not for 1p music or podcasts (or radio on watch)"
- "CommonMediaIntent#suppressed"
- "ConfirmGlidePromotion"
- "ConfirmationViewProvider#makeYesNoConfirmationViews Creating confirmation views for promotion offer with more info option"
- "Didn't catch a supported NLv3 intent"
- "DirectActionAudioSearchFlowFrame#execute first party direct invocation. Forwarding to PlayMediaFlow with intent %s launchId: %@ appInferred: %{bool}d"
- "DisablePromotion"
- "EnablePromotionFailed_"
- "GDPRHandoffNeeded"
- "GlideSignUpService#gdprHandoff FAILED to create GDPR handoff dialog"
- "GlideSignUpService#gdprHandoff successfully created GDPR handoff dialog"
- "GlideSignUpService#shouldSubscribeToGlidePreview %{bool}d"
- "GlideSignUpService#subscribeToGlidePreview gdpr not needed, calling subscribeToPromotion"
- "GlideSignUpService#subscribeToGlidePreview..."
- "GlideSignUpService#subscribeToPromotion confirmed"
- "GlideSignUpService#subscribeToPromotion failed"
- "GlideSignUpService#subscribeToPromotion..."
- "GlideSignUpServiceQueue"
- "MusicVoiceDirectUserToAppleMusic"
- "PlayMediaAppResolver#forcedResolution forced disambiguation not yet supported on HomePod"
- "PlayMediaAppResolver#postResolve %{public}s skipping recording app selection signals as inferred app"
- "PlayMediaAppResolver#resolveBundleIdentifier preview eligible but resolved as 3P"
- "PlayMediaDialogProvider#makeConfirmGlidePromotion..."
- "PlayMediaDialogProvider#makePlayDialog promotion confirmation"
- "PlayMediaIOSSnippetModelProvider#alternativeSnippetModel won't build alternatives for Apple Music Voice users. %{public}s"
- "PlayMediaIOSSnippetModelProvider#conversationSpace returning action button for glide. %{public}s"
- "PlayMediaIOSSnippetModelProvider#createMediaPlayerSnippetModel subscriptionProvider: %s, %{public}s"
- "PlayMediaIOSSnippetModelProvider#glideActiveActionButtonSnippetModel not creating snippet because this is not a glide preview subscriber. %{public}s"
- "PlayMediaIOSSnippetModelProvider#glideActiveActionButtonSnippetModel not creating snippet since app is not apple music - appID: %@. %{public}s"
- "PlayMediaIOSSnippetModelProvider#glideActiveActionButtonSnippetModel subscription details are not available. %{public}s"
- "PlayMediaIOSSnippetModelProvider#glideActiveActionButtonSnippetModel title: %s. %{public}s"
- "PlayMediaIOSSnippetModelProvider#glideActiveActionButtonSnippetModel... %{public}s"
- "PlayMediaRCHFlowWrapper#appSelectionRecord %{public}s info: %s, resolution result type: %s, recording to SELF..."
- "PlayMediaRCHFlowWrapper#appSelectionRecord %{public}s no context present for refId: %{public}s"
- "PlayMediaRCHFlowWrapper#appSelectionRecord %{public}s no rawSignalResult present for refId: %{public}s"
- "PlayMediaRCHFlowWrapper#appSelectionRecord %{public}s saved record with UUID: %s"
- "PlayMediaRCHFlowWrapper#appSelectionRecord context present, with report?:%{bool}d and rawSignalResult?:%{bool}d"
- "PlayMediaRCHFlowWrapper#appSelectionRecord setting appSelectionLastUsed"
- "PlayMediaRCHFlowWrapper#appSelectionRecord setting lastBundleIdentifier=%s"
- "PlayMediaRCHFlowWrapper#appSelectionRecord unexpected failed to save record to SELF, uuid nil"
- "PlayMediaViewProvider won't build alternatives for Apple Music Voice users."
- "PlayMediaViewProvider#makeAppleMusicListenNowButton... "
- "PommesResponseFlow#execute forwarding to SiriForAirPlayFlow"
- "SiriMusicFeatureFlow#execute Activation is blocked on AppleTV."
- "SiriMusicFeatureFlow#execute Activation is blocked on Mac."
- "SiriMusicFeatureFlow#execute Activation is blocked on Watch."
- "SiriMusicFeatureFlow#execute Buy params were not returned"
- "SiriMusicFeatureFlow#execute The requesting user is not the owner of the device. Returning an error"
- "SiriMusicFeatureFlow#execute User did not get buy params as they are churned from a previous subscription"
- "SiriMusicFeatureFlow#execute buy params were returned!"
- "SiriMusicFeatureFlow#execute enable"
- "SiriMusicFeatureFlow#execute feature not enabled"
- "SiriMusicFeatureFlow#execute skipping buy params check as user needs to sign GDPR (handoff)"
- "SiriMusicFeatureFlow#execute subscription confirmed"
- "SiriMusicFeatureFlow#execute subscription failed"
- "SiriMusicFeatureFlow#execute user is already a subscriber"
- "SiriMusicFeatureFlow#execute user is already in a music voice preview"
- "SiriMusicFeatureFlow#execute... isEnable: %{bool}d"
- "SiriMusicFeatureFlow#execute:disable"
- "SiriMusicFeatureFlow#execute:disable Dialog successfully generated, responding and exiting"
- "SiriMusicFeatureFlow#execute:disable Error creating dialog %s, issuing error dialog"
- "SiriMusicFeatureFlow#execute:disable but user is not in a preview"
- "SiriMusicFeatureFlow#makeDirectUserToAppleMusicDialog Dialog successfully generated, responding and exiting"
- "SiriMusicFeatureFlow#makeDirectUserToAppleMusicDialog Error creating dialog %s, issuing error dialog"
- "SiriMusicFeatureFlow#makeDirectUserToAppleMusicDialog..."
- "SiriMusicFeatureFlow#makeEnablePromotionSuccessDialog Dialog successfully generated, responding and exiting"
- "SiriMusicFeatureFlow#makeEnablePromotionSuccessDialog Error creating dialog %s, issuing error dialog"
- "SiriMusicFeatureFlow#makeEnablePromotionSuccessDialog..."
- "SiriMusicFeatureFlow#makeFailureDialog Dialog successfully generated, responding and exiting"
- "SiriMusicFeatureFlow#makeFailureDialog Error creating dialog %s, issuing error dialog"
- "SiriMusicFeatureFlow#makeFailureDialog..."
- "SiriMusicFeatureFlow#makeGDPRHandoffDialog Error creating dialog %s, issuing error dialog"
- "SiriMusicFeatureFlow#makeGDPRHandoffDialog subscription handoff complete"
- "SiriMusicFeatureFlow#makeGDPRHandoffDialog subscription handoff failed"
- "SiriMusicFeatureFlow#makeGDPRHandoffDialog successfully created dialog / punchout for GDPR"
- "SiriMusicFeatureFlow#makeGDPRHandoffDialog triggering subscribeToPromotion"
- "SiriMusicFeatureFlow#makeGDPRHandoffDialog..."
- "SiriMusicFeatureFlow#makePromptForConfirmation..."
- "SiriMusicFeatureFlowExecute"
- "Unexpected intent"
- "Unexpected parse type"
- "_TtC23AudioFlowDelegatePlugin18GlideSignUpService"
- "_TtC23AudioFlowDelegatePlugin20SiriMusicFeatureFlow"
- "_setLaunchId:"
- "appSelectionContext"
- "appleMusicPreview"
- "commonDialogProvider"
- "exPromotionStatus"
- "glideSignUpService"
- "isAppleVoiceGdprHandoffRetry"
- "isEnable"
- "subscriptionQueue"
- "ttsBehaviorConfigurationProvider"

```
