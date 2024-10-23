## AudioFlowDelegatePlugin

> `/System/Library/Assistant/FlowDelegatePlugins/AudioFlowDelegatePlugin.bundle/AudioFlowDelegatePlugin`

```diff

-3401.22.2.0.0
-  __TEXT.__text: 0x28328c
-  __TEXT.__auth_stubs: 0x6ba0
+3402.51.1.1.2
+  __TEXT.__text: 0x288c48
+  __TEXT.__auth_stubs: 0x6c80
   __TEXT.__objc_methlist: 0x36c
-  __TEXT.__const: 0x82c2
-  __TEXT.__cstring: 0x7a9c
-  __TEXT.__swift5_typeref: 0x4096
-  __TEXT.__oslogstring: 0x22ea7
-  __TEXT.__constg_swiftt: 0x5404
+  __TEXT.__const: 0x82d2
+  __TEXT.__cstring: 0x7b8c
+  __TEXT.__swift5_typeref: 0x3fec
+  __TEXT.__oslogstring: 0x22e77
+  __TEXT.__constg_swiftt: 0x5428
   __TEXT.__swift5_builtin: 0x168
-  __TEXT.__swift5_reflstr: 0x3d3b
-  __TEXT.__swift5_assocty: 0xa40
-  __TEXT.__swift5_proto: 0x458
-  __TEXT.__swift5_types: 0x308
+  __TEXT.__swift5_reflstr: 0x3d1b
+  __TEXT.__swift5_assocty: 0xa28
+  __TEXT.__swift5_proto: 0x454
+  __TEXT.__swift5_types: 0x30c
   __TEXT.__objc_classname: 0xce
-  __TEXT.__objc_methname: 0x2a18
+  __TEXT.__objc_methname: 0x2a1a
   __TEXT.__objc_methtype: 0x3ef
-  __TEXT.__swift5_fieldmd: 0x2ea8
-  __TEXT.__swift5_capture: 0x3b98
+  __TEXT.__swift5_fieldmd: 0x2ea0
+  __TEXT.__swift5_capture: 0x3954
   __TEXT.__swift5_protos: 0x54
   __TEXT.__swift5_mpenum: 0x20
-  __TEXT.__unwind_info: 0x3618
-  __TEXT.__eh_frame: 0x2bc4
-  __DATA_CONST.__auth_got: 0x35d0
-  __DATA_CONST.__got: 0x1ca8
-  __DATA_CONST.__auth_ptr: 0x2038
-  __DATA_CONST.__const: 0xa9d0
-  __DATA_CONST.__objc_classlist: 0x2a8
+  __TEXT.__unwind_info: 0x3778
+  __TEXT.__eh_frame: 0x3444
+  __DATA_CONST.__auth_got: 0x3640
+  __DATA_CONST.__got: 0x1d60
+  __DATA_CONST.__auth_ptr: 0x1f90
+  __DATA_CONST.__const: 0xa7e8
+  __DATA_CONST.__objc_classlist: 0x2b8
   __DATA_CONST.__objc_protolist: 0xd8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x70
-  __DATA.__objc_const: 0xa770
+  __DATA.__objc_const: 0xa818
   __DATA.__objc_selrefs: 0xce8
-  __DATA.__objc_data: 0x12a8
-  __DATA.__data: 0xb518
-  __DATA.__bss: 0x7a90
-  __DATA.__common: 0x478
+  __DATA.__objc_data: 0x12f8
+  __DATA.__data: 0xb7f8
+  __DATA.__bss: 0x7a10
+  __DATA.__common: 0x488
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreSpotlight.framework/CoreSpotlight

   - /System/Library/Frameworks/ShazamKit.framework/ShazamKit
   - /System/Library/PrivateFrameworks/AssistantServices.framework/AssistantServices
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
+  - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
   - /System/Library/PrivateFrameworks/DialogEngine.framework/DialogEngine
   - /System/Library/PrivateFrameworks/InternalSwiftProtobuf.framework/InternalSwiftProtobuf
   - /System/Library/PrivateFrameworks/PegasusAPI.framework/PegasusAPI

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftAppleArchive.dylib
   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 5185
-  Symbols:   364
-  CStrings:  2961
+  Functions: 5209
+  Symbols:   372
+  CStrings:  2969
 
Symbols:
+ _IsAppleInternalBuild
+ _OBJC_CLASS_$_CATDialog
+ _OBJC_CLASS_$_DialogElement
+ _OBJC_CLASS_$_DialogExecutionResult
+ __swift_FORCE_LOAD_$_swiftAppleArchive
+ _objc_retain_x1
+ _swift_continuation_await
+ _swift_continuation_init
+ _swift_continuation_throwingResume
+ _swift_continuation_throwingResumeWithError
- _OBJC_CLASS_$_CAT
- _OBJC_CLASS_$_SABaseClientBoundCommand
CStrings:
+ "AudioItem#toAudioMediaItem converted to %!s(MISSING)"
+ "AudioItemType#toCommonAudioMediaType unrecognized AudioItemType type: %!s(MISSING)"
+ "AudioItemType#toCommonAudioMediaType unrecognized AudioItemType: %!l(MISSING)d"
+ "CatService#executeDialog %!{(MISSING)public}s Error evaluating CAT: %!{(MISSING)public}s"
+ "CatService#executeDialog %!{(MISSING)public}s Successfully evaluated dialog to Print: %!{(MISSING)public}@ speak:%!{(MISSING)public}@"
+ "CatService#executeDialog %!{(MISSING)public}s using params: %!{(MISSING)public}s globals: %!@(MISSING)"
+ "CatService#executeDialog CAT.execute ..."
+ "CatService#executeDialog has returned an error: %!@(MISSING)"
+ "CatService#executeDialogResult Evaluating CAT family:%!s(MISSING) id:%!s(MISSING)..."
+ "CatService#executeDialogResult is creating dialog with responseMode = %!@(MISSING)"
+ "OpenMediaItemFlow#execute"
+ "OpenMediaItemFlow#execute failed to convert PlaybackItem.identifier to MusicSiriRepresentation"
+ "OpenMediaItemFlow#execute failed to convert identifier: %!s(MISSING)"
+ "OpenMediaItemFlow#execute failed to get audioItem from ranked results"
+ "OpenMediaItemFlow#execute invoking OpenMusicItemIntent with identifier: %!s(MISSING)"
+ "OpenMediaItemFlow#execute invoking OpenPodcastEpisodeAppIntent with identifier: %!s(MISSING)"
+ "OpenMediaItemFlow#execute invoking OpenPodcastShowAppIntent with identifier: %!s(MISSING)"
+ "OpenMediaItemFlow#execute mediaItem is Podcasts type, using Podcasts open intent"
+ "OpenMediaItemFlow#execute mediaType is not podcastShow or podcastEpisode, defaulting to invoke OpenPodcastShowAppIntent with identifier: %!s(MISSING)"
+ "OpenMediaItemFlow#execute missing pommesResponse or audioExperience"
+ "OpenMediaItemFlow#execute threw an error when trying to invoke OpenMusicItemIntent: %!s(MISSING)"
+ "OpenMediaItemFlow#execute threw an error when trying to invoke open intent: %!s(MISSING)"
+ "OpenMediaItemFlow#execute using Music open intent"
+ "OpenMediaItemFlow#on accepting input"
+ "OpenMediaItemFlow#on invalid AudioIntent for open use case"
+ "OpenMediaItemFlow#on pommesResponse doesn't contain audioExperience %!s(MISSING)"
+ "OpenMediaItemFlow#on unexpected parse type, rejecting"
+ "OpenMediaItemFlow#on validating input..."
+ "PlayMediaCatDialogService#intentHandledResponse overriding Siri response for testing with: %!s(MISSING)"
+ "SearchForMediaDialogProvider#makeIntentHandledDialog AppIntents enabled, returning suppressed CAT for music"
+ "UnsupportedValueStrategy#makeUnsupportedValueOutput"
+ "UnsupportedValueStrategy#makeUnsupportedValueOutput acquired dialog."
+ "UnsupportedValueStrategy#makeUnsupportedValueOutput dialog provider failed with error: %!@(MISSING)"
+ "UnsupportedValueStrategy#makeUnsupportedValueOutput no NowPlaying app"
+ "_TtC23AudioFlowDelegatePlugin17OpenMediaItemFlow"
+ "_TtC23AudioFlowDelegatePlugin29OpenMediaItemCatDialogService"
+ "determineCatDialogService"
+ "executeDialogResult(_:_:for:parameters:bundle:intentDialogContext:)"
+ "fullPrint"
+ "fullSpeak"
+ "openMediaItemCatDialogService"
+ "overrideTTSResponse"
+ "resolutionResultCode"
+ "setFullPrint:"
+ "setId:"
+ "stringForKey:"
+ "testDevTTSOverride"
+ "v24@?0@\"DialogExecutionResult\"8@\"NSError\"16"
- "CatService#executeCatResult %!{(MISSING)public}s Error evaluating CAT: %!{(MISSING)public}s"
- "CatService#executeCatResult %!{(MISSING)public}s Successfully evaluated CAT: catId:%!{(MISSING)public}s, result.speak:%!{(MISSING)public}s, result.print:%!{(MISSING)public}s"
- "CatService#executeCatResult %!{(MISSING)public}s using params: %!{(MISSING)public}s globals: %!@(MISSING)"
- "CatService#executeCatResult CAT.execute ..."
- "CommonMediaConfirmationSnippetProvider#confirmationResponse for .moreInfo use case. %!{(MISSING)public}s"
- "CommonMediaConfirmationSnippetProvider#confirmationResponse unsupported use case, returning empty snippet. %!{(MISSING)public}s"
- "CommonMediaConfirmationSnippetProvider#goToKBArticleButtonText formatted %!s(MISSING) -> string: %!s(MISSING)"
- "CommonMediaConfirmationSnippetProvider#moreInformationResponse action button model created: %!s(MISSING). %!{(MISSING)public}s"
- "ConfirmationViewProvider#makeConfirmationResponseViews for .moreInfo use case"
- "ConfirmationViewProvider#makeConfirmationResponseViews unsupported use case, returning empty views"
- "ConfirmationViewProvider#makeGetMoreInfoViews Creating promotion offer more info punchout button on iOS with button text: %!s(MISSING)"
- "ConfirmationViewProvider#makeGoToKBArticleButtonText formatted %!s(MISSING) -> string: %!s(MISSING)"
- "NeedsConfirmationWrapperFlow#buildResponse Dialog successfully generated, responding and exiting..."
- "NeedsConfirmationWrapperFlow#buildResponse Error creating dialog %!s(MISSING), issuing error dialog..."
- "NeedsConfirmationWrapperFlow#buildResponse Unable to unpack views: %!s(MISSING)"
- "NeedsConfirmationWrapperFlow#buildResponseWithRF Dialog successfully generated, responding and exiting..."
- "NeedsConfirmationWrapperFlow#buildResponseWithRF Error creating dialog %!s(MISSING), issuing error dialog..."
- "NeedsConfirmationWrapperFlow#buildResponseWithRF Unable to build output error: %!s(MISSING)"
- "NeedsConfirmationWrapperFlow#completionViewOutput with responseMode = %!s(MISSING)"
- "NeedsConfirmationWrapperFlow#execute Could not get confirmation value or confirmation value != .moreInfo. Executing the wrapped flow"
- "NeedsConfirmationWrapperFlow#execute Off topic response, ignoring..."
- "NeedsConfirmationWrapperFlow#execute Setting useExitValue to true"
- "NeedsConfirmationWrapperFlow#execute called"
- "NeedsConfirmationWrapperFlow#generateResponse Reached logic..."
- "NeedsConfirmationWrapperFlow#makeDialog Making dialog for .moreInfo request with localized url: %!s(MISSING)"
- "NeedsConfirmationWrapperFlow#makeDialog Unsupported confirmation value"
- "NeedsConfirmationWrapperFlow#on called"
- "SearchForMediaDialogProvider#makeIntentHandledDialog AppIntents enabled, returning suppressed CAT"
- "UpdateMediaAffinity#makeFailureHandlingIntentResponse no NowPlaying app"
- "determinCatDialogService"
- "initWithDomain:code:userInfo:"
- "print"
- "setDialogId:"
- "setPrint:"
- "speak"
- "useExitValue"
- "userInfo"
- "v24@?0@\"CATResult\"8@\"NSError\"16"
- "wrappedExitValue"
- "wrappedFlow"

```
