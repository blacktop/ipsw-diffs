## AudioFlowDelegatePlugin

> `/System/Library/Assistant/FlowDelegatePlugins/AudioFlowDelegatePlugin.bundle/AudioFlowDelegatePlugin`

```diff

-3400.139.1.0.0
-  __TEXT.__text: 0x281844
-  __TEXT.__auth_stubs: 0x6a20
+3401.3.1.0.0
+  __TEXT.__text: 0x27eac0
+  __TEXT.__auth_stubs: 0x6b40
   __TEXT.__objc_methlist: 0x35c
-  __TEXT.__const: 0x83a2
-  __TEXT.__cstring: 0x810c
-  __TEXT.__swift5_typeref: 0x4094
-  __TEXT.__oslogstring: 0x22947
-  __TEXT.__constg_swiftt: 0x53b8
+  __TEXT.__const: 0x82c2
+  __TEXT.__cstring: 0x796c
+  __TEXT.__swift5_typeref: 0x40a2
+  __TEXT.__oslogstring: 0x22a97
+  __TEXT.__constg_swiftt: 0x53b4
   __TEXT.__swift5_builtin: 0x168
-  __TEXT.__swift5_reflstr: 0x40ab
-  __TEXT.__swift5_assocty: 0xa58
-  __TEXT.__swift5_proto: 0x464
-  __TEXT.__swift5_types: 0x30c
+  __TEXT.__swift5_reflstr: 0x3cfb
+  __TEXT.__swift5_assocty: 0xa40
+  __TEXT.__swift5_proto: 0x458
+  __TEXT.__swift5_types: 0x308
   __TEXT.__objc_classname: 0xce
-  __TEXT.__objc_methname: 0x2a13
+  __TEXT.__objc_methname: 0x2a18
   __TEXT.__objc_methtype: 0x3ef
-  __TEXT.__swift5_fieldmd: 0x2f6c
-  __TEXT.__swift5_capture: 0x3b30
+  __TEXT.__swift5_fieldmd: 0x2e90
+  __TEXT.__swift5_capture: 0x3b58
   __TEXT.__swift5_protos: 0x54
   __TEXT.__swift5_mpenum: 0x20
-  __TEXT.__unwind_info: 0x3708
-  __TEXT.__eh_frame: 0x2ab4
-  __DATA_CONST.__auth_got: 0x3510
-  __DATA_CONST.__got: 0x1c78
-  __DATA_CONST.__auth_ptr: 0x1fa8
-  __DATA_CONST.__const: 0xaa40
+  __TEXT.__unwind_info: 0x35f8
+  __TEXT.__eh_frame: 0x2b64
+  __DATA_CONST.__auth_got: 0x35a0
+  __DATA_CONST.__got: 0x1ca8
+  __DATA_CONST.__auth_ptr: 0x2038
+  __DATA_CONST.__const: 0xa918
   __DATA_CONST.__objc_classlist: 0x2a8
   __DATA_CONST.__objc_protolist: 0xd8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x70
-  __DATA.__objc_const: 0xa710
-  __DATA.__objc_selrefs: 0xcd8
+  __DATA.__objc_const: 0xa730
+  __DATA.__objc_selrefs: 0xce0
   __DATA.__objc_data: 0x12a8
-  __DATA.__data: 0xb4d0
-  __DATA.__bss: 0x7c10
+  __DATA.__data: 0xb4b0
+  __DATA.__bss: 0x7a90
   __DATA.__common: 0x478
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswift_StringProcessing.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 5183
-  Symbols:   357
-  CStrings:  2975
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 5163
+  Symbols:   363
+  CStrings:  2941
 
Symbols:
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
- _swift_continuation_await
- _swift_continuation_init
CStrings:
+ "AmbiguousPlayFlow#genericErrorDialog Reached logic... %!s(MISSING)"
+ "AmbiguousShuffleFlow#genericErrorDialog... %!s(MISSING)"
+ "CatService#catchAllForRadarFilingConsideration, catId: %!s(MISSING) and category: %!s(MISSING), possible TTR candidate"
+ "CommonDialogProvider#makeGenericErrorDialog"
+ "PlayMediaAlternativesSnippetProvider#subtitle returning empty string because we have a classical music request. %!{(MISSING)public}s"
+ "PlayMediaDialogProvider#makeIntentHandledDialog User just accepted TCC initiated from the HomePod for an SFA request. Skipping dialog in makePreHandleIntentDialog and producing it in makePostHandleIntentDialog"
+ "PlayMediaDialogProvider#makeIntentHandledDialog User just accepted TCC initiated from the HomePod for an SFA request. Using the dialog producing intent handler"
+ "[SiriAudio] DetermineNowPlayingMetadataIssue, filed by TTR, with reason: failedToGetApp"
+ "[SiriAudio] DetermineNowPlayingMetadataIssue, filed by TTR, with reason: failedToGetNowPlayingInfo"
+ "failedToGetNowPlayingInfo"
+ "meta"
+ "tccProvider"
+ "viewFactoryProvider"
- "AmbiguousPlayFlow failed"
- "AmbiguousPlayFlow#fileRadar filing TTR..."
- "AmbiguousPlayFlow#genericErrorDialog Reached logic..."
- "AmbiguousShuffleFlow failed"
- "AmbiguousShuffleFlow#fileRadar filing TTR..."
- "AmbiguousShuffleFlow#genericErrorDialog..."
- "CellularDataSettings"
- "CommonDialogProvider#FailureHandlingIntent"
- "CommonDialogProvider#GenericError"
- "CommonMediaIntent#UnsupportedMediaItemsInvalidToken"
- "CommonMediaIntentCatDialogService#FailureHandlingIntent"
- "CommonMediaIntentCatDialogService#GenericError"
- "Companion returned .needServerExecution which is invalid for SFA requests"
- "DetermineIntent#amend No bundleId for now playing app"
- "DetermineIntent#amend No nowplaying info retrieved"
- "DetermineIntentHandler#fileRadarForDetermineNowPlayingMetadataIssue filing TTR..."
- "NoAppToSupportIntent"
- "PlayMediaDialogProvider#makeIntentHandledDialog ser just accepted TCC initiated from the HomePod for an SFA request. Using the dialog producing intent handler"
- "PommesResponseFlow AudioUsoIntent failed to be constructed"
- "PommesResponseFlow Neither SiriAudio nor PlaybackControls were able to handle the request"
- "PommesResponseFlow error unpacking input"
- "PommesResponseFlow failed to build addMediaIntent"
- "PommesResponseFlow failed to build searchMediaIntent"
- "PommesResponseFlow invalid state"
- "PommesResponseFlow pommesResponse doesn't contain audioExperience"
- "PommesResponseFlow pommesResponse is nil"
- "ServiceUnavailable"
- "[SiriAudio] DetermineNowPlayingMetadataIssue, filed by TTR, with reason: "
- "acousticIDFlowShazamOutput"
- "acousticIDFlowTraditionalRFShazamOutput"
- "addMediaHandIntentStrategyHandleResponse"
- "appResolutionCommonStrategyConfirmationViewOutput"
- "appResolutionCommonStrategyDisambiguationSnippet"
- "commonNeedsConfirmationStrategyConfirmationViewOutput"
- "determine now playing metadata issue"
- "determineHandleIntentStrategyIntentHandledResponse"
- "mediaItemDisambiguationStrategyClarificationOutput"
- "mediaItemDisambiguationStrategyDisambiguationSnippet"
- "needsConfirmationWrapperFlowCompletionViewOutput"
- "responseFactoryUtilitiesResponseOutput"
- "siriAudioOutputProviderCompletionViewOutput"
- "siriAudioOutputProviderConfirmationViewOutput"
- "siriAudioOutputProviderEmptyOutput"
- "siriAudioOutputProviderErrorOutput"
- "siriAudioOutputProviderSummaryViewOutput"
- "tCCAcceptanceFlowStrategyConfirmation"
- "unsupportedValueStrategyCreateOutput"

```
