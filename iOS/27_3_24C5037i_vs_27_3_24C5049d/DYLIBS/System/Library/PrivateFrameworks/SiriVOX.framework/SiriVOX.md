## SiriVOX

> `/System/Library/PrivateFrameworks/SiriVOX.framework/SiriVOX`

```diff

-3610.11.1.0.0
-  __TEXT.__text: 0x86d9c
-  __TEXT.__objc_methlist: 0x8e98
-  __TEXT.__const: 0x130
-  __TEXT.__constg_swiftt: 0x8c
-  __TEXT.__swift5_typeref: 0x97
-  __TEXT.__swift5_fieldmd: 0x38
-  __TEXT.__swift5_types: 0x8
-  __TEXT.__cstring: 0x11ecd
+3610.18.1.0.0
+  __TEXT.__text: 0x8b1d4
+  __TEXT.__objc_methlist: 0x92c4
+  __TEXT.__const: 0x180
+  __TEXT.__constg_swiftt: 0xc8
+  __TEXT.__swift5_typeref: 0x10b
+  __TEXT.__swift5_fieldmd: 0x70
+  __TEXT.__swift5_types: 0xc
+  __TEXT.__cstring: 0x12441
   __TEXT.__swift5_capture: 0x78
-  __TEXT.__swift5_reflstr: 0x16
-  __TEXT.__gcc_except_tab: 0x680
-  __TEXT.__oslogstring: 0x94a4
+  __TEXT.__swift5_reflstr: 0x28
+  __TEXT.__oslogstring: 0x9a18
+  __TEXT.__gcc_except_tab: 0x710
   __TEXT.__dlopen_cstrs: 0xda
-  __TEXT.__unwind_info: 0x2d60
+  __TEXT.__unwind_info: 0x2f00
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2da0
-  __DATA_CONST.__objc_classlist: 0x680
+  __DATA_CONST.__const: 0x2eb0
+  __DATA_CONST.__objc_classlist: 0x6a0
   __DATA_CONST.__objc_catlist: 0x48
-  __DATA_CONST.__objc_protolist: 0x2e0
+  __DATA_CONST.__objc_protolist: 0x2f0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3f58
-  __DATA_CONST.__objc_protorefs: 0x48
-  __DATA_CONST.__objc_superrefs: 0x4b0
+  __DATA_CONST.__objc_selrefs: 0x4230
+  __DATA_CONST.__objc_protorefs: 0x50
+  __DATA_CONST.__objc_superrefs: 0x4c8
   __DATA_CONST.__objc_arraydata: 0x990
-  __DATA_CONST.__got: 0x7b8
-  __AUTH_CONST.__const: 0xca8
-  __AUTH_CONST.__cfstring: 0x60c0
-  __AUTH_CONST.__objc_const: 0x13d60
+  __DATA_CONST.__got: 0x800
+  __AUTH_CONST.__const: 0xd10
+  __AUTH_CONST.__cfstring: 0x63e0
+  __AUTH_CONST.__objc_const: 0x145d0
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_intobj: 0xe70
   __AUTH_CONST.__objc_dictobj: 0x348
-  __AUTH_CONST.__auth_got: 0x708
-  __AUTH.__objc_data: 0x41a0
-  __AUTH.__data: 0x38
-  __DATA.__objc_ivar: 0xd34
-  __DATA.__data: 0x22c0
+  __AUTH_CONST.__auth_got: 0x7e8
+  __AUTH.__objc_data: 0x4358
+  __AUTH.__data: 0x60
+  __DATA.__objc_ivar: 0xdb4
+  __DATA.__data: 0x2340
+  __DATA.__common: 0x18
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3250
-  Symbols:   6876
-  CStrings:  2332
+  Functions: 3381
+  Symbols:   7068
+  CStrings:  2393
 
Symbols:
+ -[SVXAFUtilitiesWrapper af_IsLinwoodEnabled]
+ -[SVXAceViewHandler _chunkHasSpeakableText:]
+ -[SVXAceViewHandler _endStreamWithIdentifier:error:]
+ -[SVXAceViewHandler _firstProducedSpeechDidStartForStreamIdentifier:]
+ -[SVXAceViewHandler _speakAceView:speakableText:speakableStreamId:isFollowUpQuestion:isExpository:taskTracker:completion:]
+ -[SVXAceViewHandler _speakableStreamerForStreamIdentifier:]
+ -[SVXAceViewHandler _usesSpeakableStreamer]
+ -[SVXAceViewHandler setSpeakableFragmentContexts:]
+ -[SVXAceViewHandler setSpeakableStreamers:]
+ -[SVXAceViewHandler setStreamsAwaitingFirstSpeech:]
+ -[SVXAceViewHandler setStreamsAwaitingFollowUpSpeech:]
+ -[SVXAceViewHandler setStreamsWithDeferredStop:]
+ -[SVXAceViewHandler setStreamsWithProducedSpeech:]
+ -[SVXAceViewHandler speakableFragmentContexts]
+ -[SVXAceViewHandler speakableStreamer:didProduceSpeakableText:]
+ -[SVXAceViewHandler speakableStreamerDidDetectFollowUp:]
+ -[SVXAceViewHandler speakableStreamers]
+ -[SVXAceViewHandler streamsAwaitingFirstSpeech]
+ -[SVXAceViewHandler streamsAwaitingFollowUpSpeech]
+ -[SVXAceViewHandler streamsWithDeferredStop]
+ -[SVXAceViewHandler streamsWithProducedSpeech]
+ -[SVXHomePodUIBridgeClientDelegate _tearDownForDismissal]
+ -[SVXHomePodUIBridgeClientDelegate discardPendingTTSPrewarm]
+ -[SVXHomePodUIBridgeClientDelegate scheduleTTSPrewarm:]
+ -[SVXHomePodUIBridgeClientDelegate siriDismissedForRelaunch]
+ -[SVXMissingAssetActivationGuard _refreshSiriAvailability]
+ -[SVXSession _deactivateAfterLASAttendingStopped]
+ -[SVXSession _handleStartListenAfterSpeaking:record:taskTracker:atEndOfSpeech:]
+ -[SVXSession _releaseAudioSessionForFollowUpWindowIfRequestEnded]
+ -[SVXSession _shouldIgnoreUnscopedCloseAssistant:]
+ -[SVXSession fireIdleTimerForTesting]
+ -[SVXSessionIdleTimer fireSessionIdleTimersNow]
+ -[SVXSessionManager _handleEndSessionTestHook]
+ -[SVXSessionManager _registerEndSessionTestHook]
+ -[SVXSessionManager myriadSessionDidStartWithCdaId:]
+ -[SVXShadowComparisonLogger .cxx_destruct]
+ -[SVXShadowComparisonLogger _scoreBoostsFrom:]
+ -[SVXShadowComparisonLogger electionBegan]
+ -[SVXShadowComparisonLogger initWithEmit:]
+ -[SVXShadowComparisonLogger init]
+ -[SVXShadowComparisonLogger myriadReported]
+ -[SVXShadowComparisonLogger myriadSessionDidStartWithCdaId:]
+ -[SVXShadowComparisonLogger recordAnswerForElection:won:localScore:error:machDuration:]
+ -[SVXShadowLocalScore .cxx_destruct]
+ -[SVXShadowLocalScore audioOrderDeviceCount]
+ -[SVXShadowLocalScore audioOrderPosition]
+ -[SVXShadowLocalScore boostsApplied]
+ -[SVXShadowLocalScore confidence]
+ -[SVXShadowLocalScore deviceClass]
+ -[SVXShadowLocalScore deviceGroup]
+ -[SVXShadowLocalScore goodness]
+ -[SVXShadowLocalScore initWithGoodness:confidence:deviceGroup:deviceClass:productType:boostsApplied:audioOrderPosition:audioOrderDeviceCount:]
+ -[SVXShadowLocalScore productType]
+ -[SVXSpeakableFragmentContext .cxx_destruct]
+ -[SVXSpeakableFragmentContext aceView]
+ -[SVXSpeakableFragmentContext initWithAceView:isExpository:taskTracker:]
+ -[SVXSpeakableFragmentContext isExpository]
+ -[SVXSpeakableFragmentContext taskTracker]
+ -[SVXSpeechSynthesizer hasStreamWithStreamId:]
+ GCC_except_table1174
+ GCC_except_table1191
+ GCC_except_table1192
+ GCC_except_table1248
+ GCC_except_table1520
+ GCC_except_table1662
+ GCC_except_table1663
+ GCC_except_table1702
+ GCC_except_table1708
+ GCC_except_table1709
+ GCC_except_table1741
+ GCC_except_table1763
+ GCC_except_table1764
+ GCC_except_table1851
+ GCC_except_table1853
+ GCC_except_table1854
+ GCC_except_table1967
+ GCC_except_table2032
+ GCC_except_table2033
+ GCC_except_table2167
+ GCC_except_table2178
+ GCC_except_table2180
+ GCC_except_table2185
+ GCC_except_table2198
+ GCC_except_table2200
+ GCC_except_table2364
+ GCC_except_table2489
+ GCC_except_table2492
+ GCC_except_table2496
+ GCC_except_table2498
+ GCC_except_table2500
+ GCC_except_table2502
+ GCC_except_table2519
+ GCC_except_table2520
+ GCC_except_table2556
+ GCC_except_table2649
+ GCC_except_table2653
+ GCC_except_table2655
+ GCC_except_table2658
+ GCC_except_table2968
+ GCC_except_table3123
+ GCC_except_table3198
+ GCC_except_table779
+ _NSSelectorFromString
+ _OBJC_CLASS_$_CDASchemaCDAClientEvent
+ _OBJC_CLASS_$_CDASchemaCDAClientEventMetadata
+ _OBJC_CLASS_$_CDASchemaCDADeviceSelectionDecisionMade
+ _OBJC_CLASS_$_CDASchemaCDADeviceSelectionScoreBoosts
+ _OBJC_CLASS_$_SCDADevice
+ _OBJC_CLASS_$_SISchemaErrorInfo
+ _OBJC_CLASS_$_SVXShadowComparisonLogger
+ _OBJC_CLASS_$_SVXShadowLocalScore
+ _OBJC_CLASS_$_SVXSpeakableFragmentContext
+ _OBJC_CLASS_$__TtC7SiriVOX20SVXSpeakableStreamer
+ _OBJC_IVAR_$_SVXAceViewHandler._speakableFragmentContexts
+ _OBJC_IVAR_$_SVXAceViewHandler._speakableStreamers
+ _OBJC_IVAR_$_SVXAceViewHandler._streamsAwaitingFirstSpeech
+ _OBJC_IVAR_$_SVXAceViewHandler._streamsAwaitingFollowUpSpeech
+ _OBJC_IVAR_$_SVXAceViewHandler._streamsWithDeferredStop
+ _OBJC_IVAR_$_SVXAceViewHandler._streamsWithProducedSpeech
+ _OBJC_IVAR_$_SVXMissingAssetActivationGuard._refreshLock
+ _OBJC_IVAR_$_SVXSession._isFollowUpQuestionPending
+ _OBJC_IVAR_$_SVXSession._isLASFollowUpWindowReleasePending
+ _OBJC_IVAR_$_SVXSessionManager._endSessionNotifyToken
+ _OBJC_IVAR_$_SVXSessionManager._shadowComparisonLogger
+ _OBJC_IVAR_$_SVXShadowComparisonLogger._answeredElectionToken
+ _OBJC_IVAR_$_SVXShadowComparisonLogger._decisionLatencyMs
+ _OBJC_IVAR_$_SVXShadowComparisonLogger._deviceSelectionWon
+ _OBJC_IVAR_$_SVXShadowComparisonLogger._electionCdaId
+ _OBJC_IVAR_$_SVXShadowComparisonLogger._emit
+ _OBJC_IVAR_$_SVXShadowComparisonLogger._latestElectionToken
+ _OBJC_IVAR_$_SVXShadowComparisonLogger._localScore
+ _OBJC_IVAR_$_SVXShadowComparisonLogger._loggedCdaId
+ _OBJC_IVAR_$_SVXShadowComparisonLogger._myriadCdaId
+ _OBJC_IVAR_$_SVXShadowComparisonLogger._selectionError
+ _OBJC_IVAR_$_SVXShadowLocalScore._audioOrderDeviceCount
+ _OBJC_IVAR_$_SVXShadowLocalScore._audioOrderPosition
+ _OBJC_IVAR_$_SVXShadowLocalScore._boostsApplied
+ _OBJC_IVAR_$_SVXShadowLocalScore._confidence
+ _OBJC_IVAR_$_SVXShadowLocalScore._deviceClass
+ _OBJC_IVAR_$_SVXShadowLocalScore._deviceGroup
+ _OBJC_IVAR_$_SVXShadowLocalScore._goodness
+ _OBJC_IVAR_$_SVXShadowLocalScore._productType
+ _OBJC_IVAR_$_SVXSpeakableFragmentContext._aceView
+ _OBJC_IVAR_$_SVXSpeakableFragmentContext._isExpository
+ _OBJC_IVAR_$_SVXSpeakableFragmentContext._taskTracker
+ _OBJC_METACLASS_$_SVXShadowComparisonLogger
+ _OBJC_METACLASS_$_SVXShadowLocalScore
+ _OBJC_METACLASS_$_SVXSpeakableFragmentContext
+ _OBJC_METACLASS_$__TtC7SiriVOX20SVXSpeakableStreamer
+ _SCDAToSISchemaUUID
+ _SVXMillisecondsFromMachDuration.once
+ _SVXMillisecondsFromMachDuration.timebase
+ __CLASS_METHODS__TtC7SiriVOX20SVXSpeakableStreamer
+ __CLASS_PROPERTIES__TtC7SiriVOX20SVXSpeakableStreamer
+ __DATA__TtC7SiriVOX20SVXSpeakableStreamer
+ __INSTANCE_METHODS__TtC7SiriVOX20SVXSpeakableStreamer
+ __IVARS__TtC7SiriVOX20SVXSpeakableStreamer
+ __METACLASS_DATA__TtC7SiriVOX20SVXSpeakableStreamer
+ __OBJC_$_INSTANCE_METHODS_SVXShadowComparisonLogger
+ __OBJC_$_INSTANCE_METHODS_SVXShadowLocalScore
+ __OBJC_$_INSTANCE_METHODS_SVXSpeakableFragmentContext
+ __OBJC_$_INSTANCE_VARIABLES_SVXShadowComparisonLogger
+ __OBJC_$_INSTANCE_VARIABLES_SVXShadowLocalScore
+ __OBJC_$_INSTANCE_VARIABLES_SVXSpeakableFragmentContext
+ __OBJC_$_PROP_LIST_SVXShadowLocalScore
+ __OBJC_$_PROP_LIST_SVXSpeakableFragmentContext
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_SVXMyriadResponseDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT__TtP7SiriVOX28SVXSpeakableStreamerDelegate_
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__TtP7SiriVOX28SVXSpeakableStreamerDelegate_
+ __OBJC_$_PROTOCOL_METHOD_TYPES__TtP7SiriVOX28SVXSpeakableStreamerDelegate_
+ __OBJC_CLASS_RO_$_SVXShadowComparisonLogger
+ __OBJC_CLASS_RO_$_SVXShadowLocalScore
+ __OBJC_CLASS_RO_$_SVXSpeakableFragmentContext
+ __OBJC_LABEL_PROTOCOL_$__TtP7SiriVOX28SVXSpeakableStreamerDelegate_
+ __OBJC_METACLASS_RO_$_SVXShadowComparisonLogger
+ __OBJC_METACLASS_RO_$_SVXShadowLocalScore
+ __OBJC_METACLASS_RO_$_SVXSpeakableFragmentContext
+ __OBJC_PROTOCOL_$__TtP7SiriVOX28SVXSpeakableStreamerDelegate_
+ __PROPERTIES__TtC7SiriVOX20SVXSpeakableStreamer
+ __PROTOCOL_INSTANCE_METHODS_OPT__TtP7SiriVOX28SVXSpeakableStreamerDelegate_
+ __PROTOCOL_INSTANCE_METHODS__TtP7SiriVOX28SVXSpeakableStreamerDelegate_
+ __PROTOCOL_METHOD_TYPES__TtP7SiriVOX28SVXSpeakableStreamerDelegate_
+ __PROTOCOL__TtP7SiriVOX28SVXSpeakableStreamerDelegate_
+ __SVXSessionGetRecentSpeechSynthesisEndTimestamp
+ ___108-[SVXAceViewHandler streamingConsumerRequestsExecution:command:shouldWaitForAnimationCompletion:completion:]_block_invoke_4
+ ___122-[SVXAceViewHandler _speakAceView:speakableText:speakableStreamId:isFollowUpQuestion:isExpository:taskTracker:completion:]_block_invoke
+ ___33-[SVXShadowComparisonLogger init]_block_invoke
+ ___37-[SVXSession fireIdleTimerForTesting]_block_invoke
+ ___47-[SVXSessionIdleTimer fireSessionIdleTimersNow]_block_invoke
+ ___48-[SVXMyriadHostDevice scdaWillStartWithSession:]_block_invoke
+ ___48-[SVXSessionManager _registerEndSessionTestHook]_block_invoke
+ ___48-[SVXSessionManager _registerEndSessionTestHook]_block_invoke_2
+ ___52-[SVXAceViewHandler _endStreamWithIdentifier:error:]_block_invoke
+ ___52-[SVXSessionManager myriadSessionDidStartWithCdaId:]_block_invoke
+ ___57-[SVXHomePodUIBridgeClientDelegate _tearDownForDismissal]_block_invoke
+ ___60-[SVXSession _handleSpeechRecordingDidBeginOnAVRecordRoute:]_block_invoke
+ ___61-[SVXSessionIdleTimer startSessionIdleTimerWithTimeInterval:]_block_invoke_2
+ ___63-[SVXAceViewHandler speakableStreamer:didProduceSpeakableText:]_block_invoke
+ ___63-[SVXAceViewHandler speakableStreamer:didProduceSpeakableText:]_block_invoke_2
+ ___65-[SVXSession taskTrackingCenter:didBeginTrackingTaskWithContext:]_block_invoke
+ ___79-[SVXSession _handleStartListenAfterSpeaking:record:taskTracker:atEndOfSpeech:]_block_invoke
+ ___93-[SVXAceViewHandler streamingConsumerDidFinishStreamingWithIdentifier:error:attributionData:]_block_invoke
+ ___SVXMillisecondsFromMachDuration_block_invoke
+ ___block_descriptor_32_e33_v16?0"CDASchemaCDAClientEvent"8l
+ ___block_descriptor_40_e8_32bs_e73_v32?0"DeviceSelectionDevice"8"DeviceSelectionLocalScore"16"NSError"24ls32l8
+ ___block_descriptor_48_e8_32s40w_e8_v12?0i8ls32l8w40l8
+ ___block_descriptor_57_e8_32s40s48w_e33_v16?0"SVXServiceCommandResult"8ls32l8w48l8s40l8
+ ___block_descriptor_57_e8_32s40s_e67_v32?0"DeviceSelectionDevice"8"SVXShadowLocalScore"16"NSError"24ls32l8s40l8
+ ___block_descriptor_64_e8_32s40s48w_e5_v8?0ls32l8s40l8w48l8
+ ___block_descriptor_65_e8_32s40s48s_e34_v16?0"<SVXTaskContextMutating>"8ls32l8s40l8s48l8
+ ___block_descriptor_82_e8_32s40s48s56s64s72s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8
+ ___swift_allocate_value_buffer
+ ___swift_destroy_boxed_opaque_existential_0
+ ___swift_project_value_buffer
+ __swiftImmortalRefCount
+ __swift_stdlib_malloc_size
+ __swift_stdlib_reportUnimplementedInitializer
+ _flat unique 7SiriVOX28SVXSpeakableStreamerDelegate_p
+ _malloc_size
+ _memcpy
+ _notify_cancel
+ _notify_register_dispatch
+ _os_variant_has_internal_content
+ _swift_bridgeObjectRelease_n
+ _swift_coroFrameAlloc
+ _swift_getObjectType
+ _swift_slowDealloc
+ _swift_unknownObjectRelease
+ _swift_unknownObjectRetain
+ _swift_unknownObjectWeakAssign
+ _swift_unknownObjectWeakDestroy
+ _swift_unknownObjectWeakInit
+ _swift_unknownObjectWeakLoadStrong
+ _symbolic $s7SiriVOX28SVXSpeakableStreamerDelegateP
+ _symbolic _____ 7SiriVOX20SVXSpeakableStreamerC
+ _symbolic ______pSgXw 7SiriVOX28SVXSpeakableStreamerDelegateP
+ _symbolic _____y_____G s23_ContiguousArrayStorageC s5UInt8V
- GCC_except_table1153
- GCC_except_table1168
- GCC_except_table1224
- GCC_except_table1495
- GCC_except_table1637
- GCC_except_table1638
- GCC_except_table1675
- GCC_except_table1681
- GCC_except_table1682
- GCC_except_table1714
- GCC_except_table1820
- GCC_except_table1822
- GCC_except_table1823
- GCC_except_table1934
- GCC_except_table2105
- GCC_except_table2116
- GCC_except_table2118
- GCC_except_table2123
- GCC_except_table2136
- GCC_except_table2138
- GCC_except_table2296
- GCC_except_table2420
- GCC_except_table2422
- GCC_except_table2425
- GCC_except_table2427
- GCC_except_table2429
- GCC_except_table2431
- GCC_except_table2447
- GCC_except_table2448
- GCC_except_table2576
- GCC_except_table2580
- GCC_except_table2582
- GCC_except_table2585
- GCC_except_table2891
- GCC_except_table3046
- GCC_except_table3121
- GCC_except_table778
- ___38-[SVXAceViewHandler invalidateStreams]_block_invoke
- ___49-[SVXHomePodUIBridgeClientDelegate siriDismissed]_block_invoke
- ___65-[SVXSession _handleStartListenAfterSpeaking:record:taskTracker:]_block_invoke
- ___71-[SVXAceViewHandler handleAceView:isExpository:taskTracker:completion:]_block_invoke
- ___block_descriptor_40_e8_32s_e47_v32?0?<v?"SVXServiceCommandResult">8Q16^B24ls32l8
- ___block_descriptor_41_e8_32s_e43_v24?0"DeviceSelectionDevice"8"NSError"16ls32l8
- ___block_descriptor_64_e8_32s40s48s_e34_v16?0"<SVXTaskContextMutating>"8ls32l8s40l8s48l8
- _swift_retain_x21
CStrings:
+ "#SpeakableStreamer created for stream %{public}s"
+ "%s #activation Anchoring recording to speech synthesis end %lf s ago"
+ "%s #activation No usable speech synthesis end time (begin %llu, end %llu, now %llu)"
+ "%s #activation Speech synthesis ended %lf s ago, too old to anchor recording"
+ "%s #deviceSelection #shadow Logged %{public}@ under cdaId %@."
+ "%s #deviceSelection #shadow No cdaId for this election; not logging the comparison."
+ "%s #deviceSelection #shadow No column for boost %{public}@; omitted."
+ "%s #missingAssets - Re-read Siri Availability before declining: %@"
+ "%s #tts Speakable streamer produced text with no fragment to speak it for stream %@"
+ "%s %@ preferred voice %@ (%@) for %@, isLinwoodEnabled = %d"
+ "%s A question that nothing listens after was queued; the mic opens when the speech ends."
+ "%s Ignored %@ because it has no refId and the current request's answer is still being presented."
+ "%s LAS attending stopped without activation while request %@ is active — waiting for it to end"
+ "%s LAS follow-up window open, waiting for the request to end before releasing the audio session"
+ "%s Not arming listen-after-speaking for a device setup scene"
+ "%s Relaunch deactivation: not telling UIBridge the session ended"
+ "%s Skipping Myriad for a server command re-arm."
+ "%s Test hook: firing the session idle timer now"
+ "%s Test hook: ignored, no current session"
+ "%s Test hook: no session idle timer is pending."
+ "-[SVXAceViewHandler _speakAceView:speakableText:speakableStreamId:isFollowUpQuestion:isExpository:taskTracker:completion:]"
+ "-[SVXAceViewHandler _speakAceView:speakableText:speakableStreamId:isFollowUpQuestion:isExpository:taskTracker:completion:]_block_invoke"
+ "-[SVXAceViewHandler speakableStreamer:didProduceSpeakableText:]"
+ "-[SVXSession _handleStartListenAfterSpeaking:record:taskTracker:atEndOfSpeech:]"
+ "-[SVXSession _releaseAudioSessionForFollowUpWindowIfRequestEnded]"
+ "-[SVXSession fireIdleTimerForTesting]_block_invoke"
+ "-[SVXSession taskTrackingCenter:didBeginTrackingTaskWithContext:]_block_invoke"
+ "-[SVXSessionIdleTimer fireSessionIdleTimersNow]_block_invoke"
+ "-[SVXSessionManager _handleEndSessionTestHook]"
+ "-[SVXSessionManager _performedDeviceSelectionWithRequestInfo:isVoiceTrigger:]_block_invoke_2"
+ "-[SVXShadowComparisonLogger _scoreBoostsFrom:]"
+ "-[SVXShadowComparisonLogger myriadReported]"
+ "CDADEVICESELECTIONOUTCOME_CANCELED"
+ "CDADEVICESELECTIONOUTCOME_DECIDED"
+ "CDADEVICESELECTIONOUTCOME_ERRORED"
+ "CDADEVICESELECTIONOUTCOME_NOT_RUN"
+ "CDADEVICESELECTIONOUTCOME_TIMED_OUT"
+ "CDADEVICESELECTIONOUTCOME_UNKNOWN"
+ "Follow-up Window Opened"
+ "Ignoring"
+ "SiriVOX.SVXSpeakableStreamer"
+ "Using"
+ "_SVXSessionGetRecentSpeechSynthesisEndTimestamp"
+ "alarmOrTimerFiring"
+ "attention"
+ "audioOrderPosition"
+ "com.apple.siridebug.endsession"
+ "deviceAdjustment"
+ "errored"
+ "inEar"
+ "init()"
+ "liftTimeBoost"
+ "mediaPlaybackActive"
+ "mediaPlaybackRecentPlayback"
+ "perception"
+ "platformBoost"
+ "raiseToWake"
+ "recencyBoost"
+ "relaunch"
+ "unlockTimeBoost"
+ "v12@?0i8"
+ "v16@?0@\"CDASchemaCDAClientEvent\"8"
+ "v32@?0@\"DeviceSelectionDevice\"8@\"DeviceSelectionLocalScore\"16@\"NSError\"24"
+ "v32@?0@\"DeviceSelectionDevice\"8@\"SVXShadowLocalScore\"16@\"NSError\"24"
+ "watchGesture"
+ "watchLoudnessThreshold"
- "-[SVXAceViewHandler handleAceView:isExpository:taskTracker:completion:]"
- "-[SVXAceViewHandler handleAceView:isExpository:taskTracker:completion:]_block_invoke"
- "-[SVXSession _handleStartListenAfterSpeaking:record:taskTracker:]"
- "v24@?0@\"DeviceSelectionDevice\"8@\"NSError\"16"
- "v32@?0@?<v@?@\"SVXServiceCommandResult\">8Q16^B24"
```
