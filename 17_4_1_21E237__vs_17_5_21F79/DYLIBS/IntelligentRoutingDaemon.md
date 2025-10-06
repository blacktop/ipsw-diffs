## IntelligentRoutingDaemon

> `/System/Library/PrivateFrameworks/IntelligentRoutingDaemon.framework/IntelligentRoutingDaemon`

```diff

-66.0.3.0.0
-  __TEXT.__text: 0x67514
+66.0.4.0.0
+  __TEXT.__text: 0x690fc
   __TEXT.__auth_stubs: 0x850
-  __TEXT.__objc_methlist: 0x65c8
-  __TEXT.__oslogstring: 0x5ed8
-  __TEXT.__cstring: 0x886d
-  __TEXT.__const: 0x80
+  __TEXT.__objc_methlist: 0x6860
+  __TEXT.__oslogstring: 0x5fc5
+  __TEXT.__cstring: 0x8a66
+  __TEXT.__const: 0xc0
   __TEXT.__gcc_except_tab: 0x120c
-  __TEXT.__unwind_info: 0x1770
-  __TEXT.__objc_classname: 0xead
-  __TEXT.__objc_methname: 0x14f4d
-  __TEXT.__objc_methtype: 0x1e4a
-  __TEXT.__objc_stubs: 0xcf00
+  __TEXT.__unwind_info: 0x18bc
+  __TEXT.__objc_classname: 0xefa
+  __TEXT.__objc_methname: 0x1577d
+  __TEXT.__objc_methtype: 0x1e83
+  __TEXT.__objc_stubs: 0xd460
   __DATA_CONST.__got: 0x158
-  __DATA_CONST.__const: 0x1b90
-  __DATA_CONST.__objc_classlist: 0x420
+  __DATA_CONST.__const: 0x1bd0
+  __DATA_CONST.__objc_classlist: 0x430
   __DATA_CONST.__objc_catlist: 0x30
-  __DATA_CONST.__objc_protolist: 0xf0
+  __DATA_CONST.__objc_protolist: 0x100
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xa8c8
-  __DATA_CONST.__objc_selrefs: 0x3958
-  __DATA_CONST.__objc_classrefs: 0x670
-  __DATA_CONST.__objc_superrefs: 0x2d0
+  __DATA_CONST.__objc_const: 0xae30
+  __DATA_CONST.__objc_selrefs: 0x3aa0
+  __DATA_CONST.__objc_classrefs: 0x680
+  __DATA_CONST.__objc_superrefs: 0x2e0
   __DATA_CONST.__objc_arraydata: 0x4c8
-  __AUTH_CONST.__objc_const: 0x3780
-  __AUTH_CONST.__cfstring: 0x6e20
-  __AUTH_CONST.__objc_intobj: 0x2e8
+  __AUTH_CONST.__objc_const: 0x3810
+  __AUTH_CONST.__cfstring: 0x70c0
+  __AUTH_CONST.__objc_intobj: 0x300
   __AUTH_CONST.__const: 0x5e0
   __AUTH_CONST.__objc_arrayobj: 0x120
   __AUTH_CONST.__objc_doubleobj: 0x70
   __AUTH_CONST.__auth_got: 0x438
   __AUTH.__objc_data: 0x960
-  __DATA.__objc_ivar: 0x888
-  __DATA.__data: 0xb40
+  __DATA.__objc_ivar: 0x8d4
+  __DATA.__data: 0xc00
   __DATA.__bss: 0x38
-  __DATA_DIRTY.__objc_data: 0x1fe0
+  __DATA_DIRTY.__objc_data: 0x2080
   __DATA_DIRTY.__bss: 0xa0
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreData.framework/CoreData

   - /System/Library/PrivateFrameworks/Rapport.framework/Rapport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F107C324-8A7F-3817-B29C-DAE0A3DFD8D0
-  Functions: 2450
-  Symbols:   8899
-  CStrings:  5523
+  UUID: 8CFF6853-F291-3E4C-A4C2-64968A2AEB20
+  Functions: 2507
+  Symbols:   9101
+  CStrings:  5646
 
Symbols:
+ +[IRAnalyticsManager sendEventLazyForEventIdentifier:clientIdentifier:analytics:]
+ +[IRAnalyticsUtilities candidateModelTypeForCandidate:]
+ +[IRAnalyticsUtilities candidateTypeForCandidate:]
+ +[IRCandidateDO(Extensions) mediaRemoteSpeakerCandidate]
+ -[IREventDO(extension) isBannerEvent]
+ -[IRPolicyManager _sendSessionAnalyticsEvent:candidateIdentifier:]
+ -[IRPolicyManager sessionAnalytics]
+ -[IRPolicyManager setSessionAnalytics:]
+ -[IRPreferences coreAnalyticsSessionEnable]
+ -[IRPreferences coreAnalyticsSessionPeriodInSeconds]
+ -[IRSessionAnalytics .cxx_destruct]
+ -[IRSessionAnalytics _handleBannerEvent:withCandidate:WithMiLoPrediction:systemState:]
+ -[IRSessionAnalytics _handleNonBannerEvent:forCandidate:]
+ -[IRSessionAnalytics _invalidate]
+ -[IRSessionAnalytics _isSessionOngoing]
+ -[IRSessionAnalytics _stopSessionAndSendCA:]
+ -[IRSessionAnalytics bannerCandidate]
+ -[IRSessionAnalytics bannerEvent]
+ -[IRSessionAnalytics bannerMiLoPrediction]
+ -[IRSessionAnalytics chosenCandidate]
+ -[IRSessionAnalytics contextChangedWithReason:systemState:]
+ -[IRSessionAnalytics event:forCandidate:miloPrediction:systemState:]
+ -[IRSessionAnalytics initWithQueue:service:]
+ -[IRSessionAnalytics queue]
+ -[IRSessionAnalytics service]
+ -[IRSessionAnalytics setBannerCandidate:]
+ -[IRSessionAnalytics setBannerEvent:]
+ -[IRSessionAnalytics setBannerMiLoPrediction:]
+ -[IRSessionAnalytics setChosenCandidate:]
+ -[IRSessionAnalytics setQueue:]
+ -[IRSessionAnalytics setService:]
+ -[IRSessionAnalytics setTimer:]
+ -[IRSessionAnalytics timer]
+ -[IRSessionAnalyticsMetric .cxx_destruct]
+ -[IRSessionAnalyticsMetric bannerCandidateModelType]
+ -[IRSessionAnalyticsMetric bannerCandidateType]
+ -[IRSessionAnalyticsMetric chosenCandidateModelType]
+ -[IRSessionAnalyticsMetric chosenCandidateType]
+ -[IRSessionAnalyticsMetric clientIdentifier]
+ -[IRSessionAnalyticsMetric dictionaryRepresentation]
+ -[IRSessionAnalyticsMetric eventType]
+ -[IRSessionAnalyticsMetric initWithClientIdentifier:internalAppName:eventType:miloAvailable:bannerCandidateType:bannerCandidateModelType:chosenCandidateType:chosenCandidateModelType:postBannerInteraction:]
+ -[IRSessionAnalyticsMetric internalAppName]
+ -[IRSessionAnalyticsMetric miloAvailable]
+ -[IRSessionAnalyticsMetric name]
+ -[IRSessionAnalyticsMetric postBannerInteraction]
+ -[IRSessionAnalyticsMetric setBannerCandidateModelType:]
+ -[IRSessionAnalyticsMetric setBannerCandidateType:]
+ -[IRSessionAnalyticsMetric setChosenCandidateModelType:]
+ -[IRSessionAnalyticsMetric setChosenCandidateType:]
+ -[IRSessionAnalyticsMetric setClientIdentifier:]
+ -[IRSessionAnalyticsMetric setEventType:]
+ -[IRSessionAnalyticsMetric setInternalAppName:]
+ -[IRSessionAnalyticsMetric setMiloAvailable:]
+ -[IRSessionAnalyticsMetric setPostBannerInteraction:]
+ _IRSessionAnalyticsMetricEventTypeFromEvent
+ _IRSessionAnalyticsMetricPostBannerInteractionToString
+ _OBJC_CLASS_$_IRSessionAnalytics
+ _OBJC_CLASS_$_IRSessionAnalyticsMetric
+ _OBJC_IVAR_$_IRPolicyManager._sessionAnalytics
+ _OBJC_IVAR_$_IRPreferences._coreAnalyticsSessionEnable
+ _OBJC_IVAR_$_IRPreferences._coreAnalyticsSessionPeriodInSeconds
+ _OBJC_IVAR_$_IRSessionAnalytics._bannerCandidate
+ _OBJC_IVAR_$_IRSessionAnalytics._bannerEvent
+ _OBJC_IVAR_$_IRSessionAnalytics._bannerMiLoPrediction
+ _OBJC_IVAR_$_IRSessionAnalytics._chosenCandidate
+ _OBJC_IVAR_$_IRSessionAnalytics._queue
+ _OBJC_IVAR_$_IRSessionAnalytics._service
+ _OBJC_IVAR_$_IRSessionAnalytics._timer
+ _OBJC_IVAR_$_IRSessionAnalyticsMetric._bannerCandidateModelType
+ _OBJC_IVAR_$_IRSessionAnalyticsMetric._bannerCandidateType
+ _OBJC_IVAR_$_IRSessionAnalyticsMetric._chosenCandidateModelType
+ _OBJC_IVAR_$_IRSessionAnalyticsMetric._chosenCandidateType
+ _OBJC_IVAR_$_IRSessionAnalyticsMetric._clientIdentifier
+ _OBJC_IVAR_$_IRSessionAnalyticsMetric._eventType
+ _OBJC_IVAR_$_IRSessionAnalyticsMetric._internalAppName
+ _OBJC_IVAR_$_IRSessionAnalyticsMetric._miloAvailable
+ _OBJC_IVAR_$_IRSessionAnalyticsMetric._postBannerInteraction
+ _OBJC_METACLASS_$_IRSessionAnalytics
+ _OBJC_METACLASS_$_IRSessionAnalyticsMetric
+ __OBJC_$_INSTANCE_METHODS_IRSessionAnalytics
+ __OBJC_$_INSTANCE_METHODS_IRSessionAnalyticsMetric
+ __OBJC_$_INSTANCE_VARIABLES_IRSessionAnalytics
+ __OBJC_$_INSTANCE_VARIABLES_IRSessionAnalyticsMetric
+ __OBJC_$_PROP_LIST_CUTCoreAnalyticsMetric
+ __OBJC_$_PROP_LIST_CUTMetric
+ __OBJC_$_PROP_LIST_IRSessionAnalytics
+ __OBJC_$_PROP_LIST_IRSessionAnalyticsMetric
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CUTCoreAnalyticsMetric
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CUTMetric
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CUTCoreAnalyticsMetric
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CUTMetric
+ __OBJC_$_PROTOCOL_REFS_CUTCoreAnalyticsMetric
+ __OBJC_$_PROTOCOL_REFS_CUTMetric
+ __OBJC_CLASS_PROTOCOLS_$_IRSessionAnalyticsMetric
+ __OBJC_CLASS_RO_$_IRSessionAnalytics
+ __OBJC_CLASS_RO_$_IRSessionAnalyticsMetric
+ __OBJC_LABEL_PROTOCOL_$_CUTCoreAnalyticsMetric
+ __OBJC_LABEL_PROTOCOL_$_CUTMetric
+ __OBJC_METACLASS_RO_$_IRSessionAnalytics
+ __OBJC_METACLASS_RO_$_IRSessionAnalyticsMetric
+ __OBJC_PROTOCOL_$_CUTCoreAnalyticsMetric
+ __OBJC_PROTOCOL_$_CUTMetric
+ ___81+[IRAnalyticsManager sendEventLazyForEventIdentifier:clientIdentifier:analytics:]_block_invoke
+ ___86-[IRSessionAnalytics _handleBannerEvent:withCandidate:WithMiLoPrediction:systemState:]_block_invoke
+ ___block_literal_global.230
+ ___block_literal_global.36
+ ___block_literal_global.40
+ ___block_literal_global.42
+ _objc_msgSend$_handleBannerEvent:withCandidate:WithMiLoPrediction:systemState:
+ _objc_msgSend$_handleNonBannerEvent:forCandidate:
+ _objc_msgSend$_invalidate
+ _objc_msgSend$_isSessionOngoing
+ _objc_msgSend$_sendSessionAnalyticsEvent:candidateIdentifier:
+ _objc_msgSend$_stopSessionAndSendCA:
+ _objc_msgSend$bannerCandidate
+ _objc_msgSend$bannerCandidateModelType
+ _objc_msgSend$bannerCandidateType
+ _objc_msgSend$bannerEvent
+ _objc_msgSend$bannerMiLoPrediction
+ _objc_msgSend$candidateModelTypeForCandidate:
+ _objc_msgSend$candidateTypeForCandidate:
+ _objc_msgSend$chosenCandidate
+ _objc_msgSend$chosenCandidateModelType
+ _objc_msgSend$chosenCandidateType
+ _objc_msgSend$contextChangedWithReason:systemState:
+ _objc_msgSend$coreAnalyticsSessionEnable
+ _objc_msgSend$coreAnalyticsSessionPeriodInSeconds
+ _objc_msgSend$event:forCandidate:miloPrediction:systemState:
+ _objc_msgSend$initWithClientIdentifier:internalAppName:eventType:miloAvailable:bannerCandidateType:bannerCandidateModelType:chosenCandidateType:chosenCandidateModelType:postBannerInteraction:
+ _objc_msgSend$initWithQueue:service:
+ _objc_msgSend$internalAppName
+ _objc_msgSend$isBannerEvent
+ _objc_msgSend$mediaRemoteSpeakerCandidate
+ _objc_msgSend$miloAvailable
+ _objc_msgSend$nodeDOWithAvOutpuDeviceIdentifier:rapportIdentifier:idsIdentifier:avOutputDevice:rapportDevice:
+ _objc_msgSend$postBannerInteraction
+ _objc_msgSend$sendEventLazyForEventIdentifier:clientIdentifier:analytics:
+ _objc_msgSend$sessionAnalytics
+ _objc_msgSend$setBannerCandidate:
+ _objc_msgSend$setBannerCandidateModelType:
+ _objc_msgSend$setBannerCandidateType:
+ _objc_msgSend$setBannerEvent:
+ _objc_msgSend$setBannerMiLoPrediction:
+ _objc_msgSend$setChosenCandidate:
+ _objc_msgSend$setChosenCandidateModelType:
+ _objc_msgSend$setChosenCandidateType:
+ _objc_msgSend$setInternalAppName:
+ _objc_msgSend$setMiloAvailable:
+ _objc_msgSend$setPostBannerInteraction:
+ _objc_msgSend$setSessionAnalytics:
+ _objc_msgSend$setTimer:
+ _objc_msgSend$timer
- +[IRAnalyticsManager _AnalyticsSendEventLazyForEventIdentifier:clientIdentifier:analytics:]
- ___91+[IRAnalyticsManager _AnalyticsSendEventLazyForEventIdentifier:clientIdentifier:analytics:]_block_invoke
- ___block_literal_global.236
- ___block_literal_global.31
- ___block_literal_global.37
- _objc_msgSend$_AnalyticsSendEventLazyForEventIdentifier:clientIdentifier:analytics:
CStrings:
+ "\x11+"
+ "\x1f\x0f\x0f\x0f\x0f\x0f\a"
+ "#session-analytics, "
+ "%s[%@], Starting with eventType: %@, candidateIdentifier: %@, miloCanUse: %@, isHeadphonesRoutedOrPredicted: %@"
+ "%s[%@], Stopping with eventType: %@, bannerCandidateIdentifier: %@, chosenCandidateIdentifier: %@, postBannerInteraction: %@"
+ "@\"IRSessionAnalytics\""
+ "@88@0:8@16@24@32@40@48@56@64@72@80"
+ "BannerCandidateModelType"
+ "BannerCandidateType"
+ "CUTCoreAnalyticsMetric"
+ "CUTMetric"
+ "ChosenCandidateModelType"
+ "ChosenCandidateType"
+ "ClientIdentifier"
+ "EventType"
+ "HeadphonesRoutedOrPredicted"
+ "IRSessionAnalytics"
+ "IRSessionAnalyticsMetric"
+ "IRcoreAnalyticsSessionEnable"
+ "IRcoreAnalyticsSessionPeriodInSeconds"
+ "InternalAppName"
+ "InvalidEnum"
+ "MiLoAvailable"
+ "PickerChoiceBannerCandidate"
+ "PickerChoiceOtherCandidate"
+ "PlaybackStartBannerCandidate"
+ "PlaybackStartOtherCandidate"
+ "PostBannerInteraction"
+ "SessionInterrupted"
+ "SessionInvalid"
+ "T@\"IRCandidateDO\",&,N,V_bannerCandidate"
+ "T@\"IRCandidateDO\",&,N,V_chosenCandidate"
+ "T@\"IREventDO\",&,N,V_bannerEvent"
+ "T@\"IRMiloLslPredictionDO\",&,N,V_bannerMiLoPrediction"
+ "T@\"IRSessionAnalytics\",&,N,V_sessionAnalytics"
+ "T@\"IRTimer\",&,N,V_timer"
+ "T@\"NSNumber\",&,N,V_eventType"
+ "T@\"NSNumber\",&,N,V_internalAppName"
+ "T@\"NSNumber\",&,N,V_miloAvailable"
+ "T@\"NSNumber\",&,N,V_postBannerInteraction"
+ "T@\"NSNumber\",R,N,V_coreAnalyticsSessionEnable"
+ "T@\"NSNumber\",R,N,V_coreAnalyticsSessionPeriodInSeconds"
+ "T@\"NSString\",&,N,V_bannerCandidateModelType"
+ "T@\"NSString\",&,N,V_bannerCandidateType"
+ "T@\"NSString\",&,N,V_chosenCandidateModelType"
+ "T@\"NSString\",&,N,V_chosenCandidateType"
+ "Timeout"
+ "_bannerCandidate"
+ "_bannerCandidateModelType"
+ "_bannerCandidateType"
+ "_bannerEvent"
+ "_bannerMiLoPrediction"
+ "_chosenCandidate"
+ "_chosenCandidateModelType"
+ "_chosenCandidateType"
+ "_coreAnalyticsSessionEnable"
+ "_coreAnalyticsSessionPeriodInSeconds"
+ "_handleBannerEvent:withCandidate:WithMiLoPrediction:systemState:"
+ "_handleNonBannerEvent:forCandidate:"
+ "_internalAppName"
+ "_isSessionOngoing"
+ "_miloAvailable"
+ "_postBannerInteraction"
+ "_sendSessionAnalyticsEvent:candidateIdentifier:"
+ "_sessionAnalytics"
+ "_stopSessionAndSendCA:"
+ "_timer"
+ "bannerCandidate"
+ "bannerCandidateModelType"
+ "bannerCandidateType"
+ "bannerEvent"
+ "bannerMiLoPrediction"
+ "candidateModelTypeForCandidate:"
+ "candidateTypeForCandidate:"
+ "chosenCandidate"
+ "chosenCandidateModelType"
+ "chosenCandidateType"
+ "com.apple.intelligentroutingd.UiEventSessionTelemetry"
+ "contextChangedWithReason:systemState:"
+ "coreAnalyticsSessionEnable"
+ "coreAnalyticsSessionPeriodInSeconds"
+ "event:forCandidate:miloPrediction:systemState:"
+ "initWithClientIdentifier:internalAppName:eventType:miloAvailable:bannerCandidateType:bannerCandidateModelType:chosenCandidateType:chosenCandidateModelType:postBannerInteraction:"
+ "initWithQueue:service:"
+ "internalAppName"
+ "isBannerEvent"
+ "mediaRemoteSpeakerCandidate"
+ "miloAvailable"
+ "postBannerInteraction"
+ "sendEventLazyForEventIdentifier:clientIdentifier:analytics:"
+ "sessionAnalytics"
+ "setBannerCandidate:"
+ "setBannerCandidateModelType:"
+ "setBannerCandidateType:"
+ "setBannerEvent:"
+ "setBannerMiLoPrediction:"
+ "setChosenCandidate:"
+ "setChosenCandidateModelType:"
+ "setChosenCandidateType:"
+ "setInternalAppName:"
+ "setMiloAvailable:"
+ "setPostBannerInteraction:"
+ "setSessionAnalytics:"
+ "setTimer:"
+ "timer"
- "\x11*"
- "\x1f\x0f\x0f\x0f\x0f\x0f\x05"
- "_AnalyticsSendEventLazyForEventIdentifier:clientIdentifier:analytics:"

```
