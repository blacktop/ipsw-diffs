## SiriUIBridge

> `/System/Library/PrivateFrameworks/SiriUIBridge.framework/SiriUIBridge`

```diff

-3520.29.1.0.0
-  __TEXT.__text: 0x25ff0
-  __TEXT.__auth_stubs: 0xfa0
-  __TEXT.__objc_methlist: 0x17e4
-  __TEXT.__const: 0x4e0
-  __TEXT.__cstring: 0x113a
-  __TEXT.__constg_swiftt: 0x814
-  __TEXT.__swift5_typeref: 0x8ae
+3600.27.1.0.0
+  __TEXT.__text: 0x2d094
+  __TEXT.__objc_methlist: 0x24c4
+  __TEXT.__const: 0x520
+  __TEXT.__cstring: 0x1faa
+  __TEXT.__constg_swiftt: 0x83c
+  __TEXT.__swift5_typeref: 0xb12
   __TEXT.__swift5_builtin: 0x50
   __TEXT.__swift5_types: 0x34
   __TEXT.__swift5_fieldmd: 0x200
   __TEXT.__swift5_reflstr: 0x20b
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__swift5_capture: 0x8c8
-  __TEXT.__oslogstring: 0xdf3
-  __TEXT.__unwind_info: 0x988
-  __TEXT.__eh_frame: 0x1b8
-  __TEXT.__objc_classname: 0x707
-  __TEXT.__objc_methname: 0x2379
-  __TEXT.__objc_methtype: 0xf79
-  __TEXT.__objc_stubs: 0x1180
-  __DATA_CONST.__got: 0x2d0
-  __DATA_CONST.__const: 0x498
-  __DATA_CONST.__objc_classlist: 0x140
+  __TEXT.__swift5_capture: 0x9ac
+  __TEXT.__oslogstring: 0xe73
+  __TEXT.__unwind_info: 0xb80
+  __TEXT.__eh_frame: 0x198
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x7a0
+  __DATA_CONST.__objc_classlist: 0x200
   __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x708
+  __DATA_CONST.__objc_selrefs: 0x970
   __DATA_CONST.__objc_protorefs: 0x50
-  __DATA_CONST.__objc_superrefs: 0xa0
-  __AUTH_CONST.__auth_got: 0x7d8
-  __AUTH_CONST.__const: 0x2068
-  __AUTH_CONST.__cfstring: 0x580
-  __AUTH_CONST.__objc_const: 0x3038
-  __AUTH.__objc_data: 0x858
-  __AUTH.__data: 0x108
-  __DATA.__objc_ivar: 0xf8
-  __DATA.__data: 0x648
-  __DATA_DIRTY.__objc_data: 0xa20
-  __DATA_DIRTY.__data: 0x4c8
+  __DATA_CONST.__objc_superrefs: 0x108
+  __DATA_CONST.__got: 0x428
+  __AUTH_CONST.__const: 0x25d0
+  __AUTH_CONST.__cfstring: 0xc80
+  __AUTH_CONST.__objc_const: 0x51a0
+  __AUTH_CONST.__auth_got: 0xa38
+  __AUTH.__objc_data: 0x768
+  __AUTH.__data: 0x68
+  __DATA.__objc_ivar: 0x248
+  __DATA.__data: 0x640
+  __DATA_DIRTY.__objc_data: 0x1298
+  __DATA_DIRTY.__data: 0x5e8
   __DATA_DIRTY.__common: 0x68
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 868687CC-0A10-3E24-B11A-C85565DD8978
-  Functions: 1395
-  Symbols:   2326
-  CStrings:  727
+  UUID: EE1EAFE0-9335-34F3-9705-0A5A63155592
+  Functions: 1751
+  Symbols:   3604
+  CStrings:  339
 
Symbols:
+ +[SUIBActionRepresentation supportsSecureCoding]
+ +[SUIBActionRepresentationSchema supportsSecureCoding]
+ +[SUIBActivityRepresentation supportsSecureCoding]
+ +[SUIBAttributedRequestExecutionUpdate supportsSecureCoding]
+ +[SUIBExecutionStatistic supportsSecureCoding]
+ +[SUIBExecutionUpdateDirective supportsSecureCoding]
+ +[SUIBLatencyRequestProgress supportsSecureCoding]
+ +[SUIBThinkingContext supportsSecureCoding]
+ +[SUIBToolExecutionProgressUpdate supportsSecureCoding]
+ +[SUIBUserQueryEnhancementContext supportsSecureCoding]
+ +[SUIBUserTurnContext supportsSecureCoding]
+ +[SUIBVisualCaptureContext supportsSecureCoding]
+ -[SUIBActionRepresentation .cxx_destruct]
+ -[SUIBActionRepresentation applicationIdentifier]
+ -[SUIBActionRepresentation copyWithZone:]
+ -[SUIBActionRepresentation description]
+ -[SUIBActionRepresentation encodeWithCoder:]
+ -[SUIBActionRepresentation executionStatistic]
+ -[SUIBActionRepresentation initWithBuilder:]
+ -[SUIBActionRepresentation initWithCoder:]
+ -[SUIBActionRepresentation init]
+ -[SUIBActionRepresentation schema]
+ -[SUIBActionRepresentation toolID]
+ -[SUIBActionRepresentationMutation .cxx_destruct]
+ -[SUIBActionRepresentationMutation applicationIdentifier]
+ -[SUIBActionRepresentationMutation executionStatistic]
+ -[SUIBActionRepresentationMutation schema]
+ -[SUIBActionRepresentationMutation setApplicationIdentifier:]
+ -[SUIBActionRepresentationMutation setExecutionStatistic:]
+ -[SUIBActionRepresentationMutation setSchema:]
+ -[SUIBActionRepresentationMutation setToolID:]
+ -[SUIBActionRepresentationMutation toolID]
+ -[SUIBActionRepresentationSchema .cxx_destruct]
+ -[SUIBActionRepresentationSchema copyWithZone:]
+ -[SUIBActionRepresentationSchema description]
+ -[SUIBActionRepresentationSchema domain]
+ -[SUIBActionRepresentationSchema encodeWithCoder:]
+ -[SUIBActionRepresentationSchema initWithBuilder:]
+ -[SUIBActionRepresentationSchema initWithCoder:]
+ -[SUIBActionRepresentationSchema init]
+ -[SUIBActionRepresentationSchema kind]
+ -[SUIBActionRepresentationSchemaMutation .cxx_destruct]
+ -[SUIBActionRepresentationSchemaMutation domain]
+ -[SUIBActionRepresentationSchemaMutation kind]
+ -[SUIBActionRepresentationSchemaMutation setDomain:]
+ -[SUIBActionRepresentationSchemaMutation setKind:]
+ -[SUIBActivityRepresentation .cxx_destruct]
+ -[SUIBActivityRepresentation actionRepresentation]
+ -[SUIBActivityRepresentation activityType]
+ -[SUIBActivityRepresentation copyWithZone:]
+ -[SUIBActivityRepresentation description]
+ -[SUIBActivityRepresentation encodeWithCoder:]
+ -[SUIBActivityRepresentation initWithBuilder:]
+ -[SUIBActivityRepresentation initWithCoder:]
+ -[SUIBActivityRepresentation init]
+ -[SUIBActivityRepresentation thinkingContext]
+ -[SUIBActivityRepresentation userTurnContext]
+ -[SUIBActivityRepresentationMutation .cxx_destruct]
+ -[SUIBActivityRepresentationMutation actionRepresentation]
+ -[SUIBActivityRepresentationMutation activityType]
+ -[SUIBActivityRepresentationMutation setActionRepresentation:]
+ -[SUIBActivityRepresentationMutation setActivityType:]
+ -[SUIBActivityRepresentationMutation setThinkingContext:]
+ -[SUIBActivityRepresentationMutation setUserTurnContext:]
+ -[SUIBActivityRepresentationMutation thinkingContext]
+ -[SUIBActivityRepresentationMutation userTurnContext]
+ -[SUIBAttributedRequestExecutionUpdate .cxx_destruct]
+ -[SUIBAttributedRequestExecutionUpdate activities]
+ -[SUIBAttributedRequestExecutionUpdate copyWithZone:]
+ -[SUIBAttributedRequestExecutionUpdate description]
+ -[SUIBAttributedRequestExecutionUpdate directive]
+ -[SUIBAttributedRequestExecutionUpdate encodeWithCoder:]
+ -[SUIBAttributedRequestExecutionUpdate initWithBuilder:]
+ -[SUIBAttributedRequestExecutionUpdate initWithCoder:]
+ -[SUIBAttributedRequestExecutionUpdate init]
+ -[SUIBAttributedRequestExecutionUpdate requestProgress]
+ -[SUIBAttributedRequestExecutionUpdate toolUpdate]
+ -[SUIBAttributedRequestExecutionUpdate updateType]
+ -[SUIBAttributedRequestExecutionUpdate userTurnIdentifier]
+ -[SUIBAttributedRequestExecutionUpdateMutation .cxx_destruct]
+ -[SUIBAttributedRequestExecutionUpdateMutation activities]
+ -[SUIBAttributedRequestExecutionUpdateMutation directive]
+ -[SUIBAttributedRequestExecutionUpdateMutation requestProgress]
+ -[SUIBAttributedRequestExecutionUpdateMutation setActivities:]
+ -[SUIBAttributedRequestExecutionUpdateMutation setDirective:]
+ -[SUIBAttributedRequestExecutionUpdateMutation setRequestProgress:]
+ -[SUIBAttributedRequestExecutionUpdateMutation setToolUpdate:]
+ -[SUIBAttributedRequestExecutionUpdateMutation setUpdateType:]
+ -[SUIBAttributedRequestExecutionUpdateMutation setUserTurnIdentifier:]
+ -[SUIBAttributedRequestExecutionUpdateMutation toolUpdate]
+ -[SUIBAttributedRequestExecutionUpdateMutation updateType]
+ -[SUIBAttributedRequestExecutionUpdateMutation userTurnIdentifier]
+ -[SUIBExecutionStatistic .cxx_destruct]
+ -[SUIBExecutionStatistic copyWithZone:]
+ -[SUIBExecutionStatistic description]
+ -[SUIBExecutionStatistic encodeWithCoder:]
+ -[SUIBExecutionStatistic initWithBuilder:]
+ -[SUIBExecutionStatistic initWithCoder:]
+ -[SUIBExecutionStatistic init]
+ -[SUIBExecutionStatistic predictedDuration]
+ -[SUIBExecutionStatistic predictionConfidence]
+ -[SUIBExecutionStatistic shouldPresentActivityStatus]
+ -[SUIBExecutionStatisticMutation .cxx_destruct]
+ -[SUIBExecutionStatisticMutation predictedDuration]
+ -[SUIBExecutionStatisticMutation predictionConfidence]
+ -[SUIBExecutionStatisticMutation setPredictedDuration:]
+ -[SUIBExecutionStatisticMutation setPredictionConfidence:]
+ -[SUIBExecutionStatisticMutation setShouldPresentActivityStatus:]
+ -[SUIBExecutionStatisticMutation shouldPresentActivityStatus]
+ -[SUIBExecutionUpdateDirective copyWithZone:]
+ -[SUIBExecutionUpdateDirective description]
+ -[SUIBExecutionUpdateDirective directiveType]
+ -[SUIBExecutionUpdateDirective encodeWithCoder:]
+ -[SUIBExecutionUpdateDirective initWithBuilder:]
+ -[SUIBExecutionUpdateDirective initWithCoder:]
+ -[SUIBExecutionUpdateDirective init]
+ -[SUIBExecutionUpdateDirectiveMutation directiveType]
+ -[SUIBExecutionUpdateDirectiveMutation setDirectiveType:]
+ -[SUIBIntelligenceFlowProgressUpdate attributedRequestExecutionUpdate]
+ -[SUIBIntelligenceFlowProgressUpdateMutation attributedRequestExecutionUpdate]
+ -[SUIBIntelligenceFlowProgressUpdateMutation setAttributedRequestExecutionUpdate:]
+ -[SUIBLatencyRequestProgress .cxx_destruct]
+ -[SUIBLatencyRequestProgress copyWithZone:]
+ -[SUIBLatencyRequestProgress currentRequestPhaseEndingProgress]
+ -[SUIBLatencyRequestProgress currentRequestPhaseEstimatedEndTimestamp]
+ -[SUIBLatencyRequestProgress currentRequestPhaseProgress]
+ -[SUIBLatencyRequestProgress currentRequestPhaseStartingProgress]
+ -[SUIBLatencyRequestProgress description]
+ -[SUIBLatencyRequestProgress encodeWithCoder:]
+ -[SUIBLatencyRequestProgress initWithBuilder:]
+ -[SUIBLatencyRequestProgress initWithCoder:]
+ -[SUIBLatencyRequestProgress init]
+ -[SUIBLatencyRequestProgressMutation .cxx_destruct]
+ -[SUIBLatencyRequestProgressMutation currentRequestPhaseEndingProgress]
+ -[SUIBLatencyRequestProgressMutation currentRequestPhaseEstimatedEndTimestamp]
+ -[SUIBLatencyRequestProgressMutation currentRequestPhaseProgress]
+ -[SUIBLatencyRequestProgressMutation currentRequestPhaseStartingProgress]
+ -[SUIBLatencyRequestProgressMutation setCurrentRequestPhaseEndingProgress:]
+ -[SUIBLatencyRequestProgressMutation setCurrentRequestPhaseEstimatedEndTimestamp:]
+ -[SUIBLatencyRequestProgressMutation setCurrentRequestPhaseProgress:]
+ -[SUIBLatencyRequestProgressMutation setCurrentRequestPhaseStartingProgress:]
+ -[SUIBThinkingContext .cxx_destruct]
+ -[SUIBThinkingContext agentType]
+ -[SUIBThinkingContext copyWithZone:]
+ -[SUIBThinkingContext description]
+ -[SUIBThinkingContext encodeWithCoder:]
+ -[SUIBThinkingContext executionStatistic]
+ -[SUIBThinkingContext initWithBuilder:]
+ -[SUIBThinkingContext initWithCoder:]
+ -[SUIBThinkingContext init]
+ -[SUIBThinkingContext setAgentType:]
+ -[SUIBThinkingContext setUserQueryEnhancementContext:]
+ -[SUIBThinkingContext userQueryEnhancementContext]
+ -[SUIBThinkingContextMutation .cxx_destruct]
+ -[SUIBThinkingContextMutation agentType]
+ -[SUIBThinkingContextMutation executionStatistic]
+ -[SUIBThinkingContextMutation setAgentType:]
+ -[SUIBThinkingContextMutation setExecutionStatistic:]
+ -[SUIBThinkingContextMutation setUserQueryEnhancementContext:]
+ -[SUIBThinkingContextMutation userQueryEnhancementContext]
+ -[SUIBToolExecutionProgressUpdate .cxx_destruct]
+ -[SUIBToolExecutionProgressUpdate additionalProgressDescription]
+ -[SUIBToolExecutionProgressUpdate agentType]
+ -[SUIBToolExecutionProgressUpdate applicationIdentifier]
+ -[SUIBToolExecutionProgressUpdate copyWithZone:]
+ -[SUIBToolExecutionProgressUpdate description]
+ -[SUIBToolExecutionProgressUpdate encodeWithCoder:]
+ -[SUIBToolExecutionProgressUpdate initWithBuilder:]
+ -[SUIBToolExecutionProgressUpdate initWithCoder:]
+ -[SUIBToolExecutionProgressUpdate init]
+ -[SUIBToolExecutionProgressUpdate prefersVisualProgressIndicator]
+ -[SUIBToolExecutionProgressUpdate progressDescription]
+ -[SUIBToolExecutionProgressUpdate progress]
+ -[SUIBToolExecutionProgressUpdate sourceIdentity]
+ -[SUIBToolExecutionProgressUpdateMutation .cxx_destruct]
+ -[SUIBToolExecutionProgressUpdateMutation additionalProgressDescription]
+ -[SUIBToolExecutionProgressUpdateMutation agentType]
+ -[SUIBToolExecutionProgressUpdateMutation applicationIdentifier]
+ -[SUIBToolExecutionProgressUpdateMutation prefersVisualProgressIndicator]
+ -[SUIBToolExecutionProgressUpdateMutation progressDescription]
+ -[SUIBToolExecutionProgressUpdateMutation progress]
+ -[SUIBToolExecutionProgressUpdateMutation setAdditionalProgressDescription:]
+ -[SUIBToolExecutionProgressUpdateMutation setAgentType:]
+ -[SUIBToolExecutionProgressUpdateMutation setApplicationIdentifier:]
+ -[SUIBToolExecutionProgressUpdateMutation setPrefersVisualProgressIndicator:]
+ -[SUIBToolExecutionProgressUpdateMutation setProgress:]
+ -[SUIBToolExecutionProgressUpdateMutation setProgressDescription:]
+ -[SUIBToolExecutionProgressUpdateMutation setSourceIdentity:]
+ -[SUIBToolExecutionProgressUpdateMutation sourceIdentity]
+ -[SUIBUserQueryEnhancementContext .cxx_destruct]
+ -[SUIBUserQueryEnhancementContext copyWithZone:]
+ -[SUIBUserQueryEnhancementContext description]
+ -[SUIBUserQueryEnhancementContext encodeWithCoder:]
+ -[SUIBUserQueryEnhancementContext initWithBuilder:]
+ -[SUIBUserQueryEnhancementContext initWithCoder:]
+ -[SUIBUserQueryEnhancementContext init]
+ -[SUIBUserQueryEnhancementContext rewrittenQuery]
+ -[SUIBUserQueryEnhancementContext setRewrittenQuery:]
+ -[SUIBUserQueryEnhancementContextMutation .cxx_destruct]
+ -[SUIBUserQueryEnhancementContextMutation rewrittenQuery]
+ -[SUIBUserQueryEnhancementContextMutation setRewrittenQuery:]
+ -[SUIBUserTurnContext .cxx_destruct]
+ -[SUIBUserTurnContext copyWithZone:]
+ -[SUIBUserTurnContext description]
+ -[SUIBUserTurnContext didEnd]
+ -[SUIBUserTurnContext doesIntroduceNewTurn]
+ -[SUIBUserTurnContext encodeWithCoder:]
+ -[SUIBUserTurnContext hash]
+ -[SUIBUserTurnContext initWithBuilder:]
+ -[SUIBUserTurnContext initWithCoder:]
+ -[SUIBUserTurnContext init]
+ -[SUIBUserTurnContext isActivated]
+ -[SUIBUserTurnContext isEqual:]
+ -[SUIBUserTurnContext userTurnIdentifier]
+ -[SUIBUserTurnContext userTurnType]
+ -[SUIBUserTurnContextMutation .cxx_destruct]
+ -[SUIBUserTurnContextMutation didEnd]
+ -[SUIBUserTurnContextMutation doesIntroduceNewTurn]
+ -[SUIBUserTurnContextMutation init]
+ -[SUIBUserTurnContextMutation isActivated]
+ -[SUIBUserTurnContextMutation setDidEnd:]
+ -[SUIBUserTurnContextMutation setDoesIntroduceNewTurn:]
+ -[SUIBUserTurnContextMutation setIsActivated:]
+ -[SUIBUserTurnContextMutation setUserTurnIdentifier:]
+ -[SUIBUserTurnContextMutation setUserTurnType:]
+ -[SUIBUserTurnContextMutation userTurnIdentifier]
+ -[SUIBUserTurnContextMutation userTurnType]
+ -[SUIBVisualCaptureContext .cxx_destruct]
+ -[SUIBVisualCaptureContext data]
+ -[SUIBVisualCaptureContext description]
+ -[SUIBVisualCaptureContext encodeWithCoder:]
+ -[SUIBVisualCaptureContext initWithBuilder:]
+ -[SUIBVisualCaptureContext initWithCoder:]
+ -[SUIBVisualCaptureContext init]
+ -[SUIBVisualCaptureContext setData:]
+ -[SUIBVisualCaptureContextMutation .cxx_destruct]
+ -[SUIBVisualCaptureContextMutation data]
+ -[SUIBVisualCaptureContextMutation setData:]
+ _OBJC_CLASS_$_NSData
+ _OBJC_CLASS_$_NSDate
+ _OBJC_CLASS_$_NSDictionary
+ _OBJC_CLASS_$_NSKeyedArchiver
+ _OBJC_CLASS_$_NSKeyedUnarchiver
+ _OBJC_CLASS_$_SUIBActionRepresentation
+ _OBJC_CLASS_$_SUIBActionRepresentationMutation
+ _OBJC_CLASS_$_SUIBActionRepresentationSchema
+ _OBJC_CLASS_$_SUIBActionRepresentationSchemaMutation
+ _OBJC_CLASS_$_SUIBActivityRepresentation
+ _OBJC_CLASS_$_SUIBActivityRepresentationMutation
+ _OBJC_CLASS_$_SUIBAttributedRequestExecutionUpdate
+ _OBJC_CLASS_$_SUIBAttributedRequestExecutionUpdateMutation
+ _OBJC_CLASS_$_SUIBExecutionStatistic
+ _OBJC_CLASS_$_SUIBExecutionStatisticMutation
+ _OBJC_CLASS_$_SUIBExecutionUpdateDirective
+ _OBJC_CLASS_$_SUIBExecutionUpdateDirectiveMutation
+ _OBJC_CLASS_$_SUIBLatencyRequestProgress
+ _OBJC_CLASS_$_SUIBLatencyRequestProgressMutation
+ _OBJC_CLASS_$_SUIBThinkingContext
+ _OBJC_CLASS_$_SUIBThinkingContextMutation
+ _OBJC_CLASS_$_SUIBToolExecutionProgressUpdate
+ _OBJC_CLASS_$_SUIBToolExecutionProgressUpdateMutation
+ _OBJC_CLASS_$_SUIBUserQueryEnhancementContext
+ _OBJC_CLASS_$_SUIBUserQueryEnhancementContextMutation
+ _OBJC_CLASS_$_SUIBUserTurnContext
+ _OBJC_CLASS_$_SUIBUserTurnContextMutation
+ _OBJC_CLASS_$_SUIBVisualCaptureContext
+ _OBJC_CLASS_$_SUIBVisualCaptureContextMutation
+ _OBJC_IVAR_$_SUIBActionRepresentation._applicationIdentifier
+ _OBJC_IVAR_$_SUIBActionRepresentation._executionStatistic
+ _OBJC_IVAR_$_SUIBActionRepresentation._schema
+ _OBJC_IVAR_$_SUIBActionRepresentation._toolID
+ _OBJC_IVAR_$_SUIBActionRepresentationMutation._applicationIdentifier
+ _OBJC_IVAR_$_SUIBActionRepresentationMutation._executionStatistic
+ _OBJC_IVAR_$_SUIBActionRepresentationMutation._schema
+ _OBJC_IVAR_$_SUIBActionRepresentationMutation._toolID
+ _OBJC_IVAR_$_SUIBActionRepresentationSchema._domain
+ _OBJC_IVAR_$_SUIBActionRepresentationSchema._kind
+ _OBJC_IVAR_$_SUIBActionRepresentationSchemaMutation._domain
+ _OBJC_IVAR_$_SUIBActionRepresentationSchemaMutation._kind
+ _OBJC_IVAR_$_SUIBActivityRepresentation._actionRepresentation
+ _OBJC_IVAR_$_SUIBActivityRepresentation._activityType
+ _OBJC_IVAR_$_SUIBActivityRepresentation._thinkingContext
+ _OBJC_IVAR_$_SUIBActivityRepresentation._userTurnContext
+ _OBJC_IVAR_$_SUIBActivityRepresentationMutation._actionRepresentation
+ _OBJC_IVAR_$_SUIBActivityRepresentationMutation._activityType
+ _OBJC_IVAR_$_SUIBActivityRepresentationMutation._thinkingContext
+ _OBJC_IVAR_$_SUIBActivityRepresentationMutation._userTurnContext
+ _OBJC_IVAR_$_SUIBAttributedRequestExecutionUpdate._activities
+ _OBJC_IVAR_$_SUIBAttributedRequestExecutionUpdate._directive
+ _OBJC_IVAR_$_SUIBAttributedRequestExecutionUpdate._requestProgress
+ _OBJC_IVAR_$_SUIBAttributedRequestExecutionUpdate._toolUpdate
+ _OBJC_IVAR_$_SUIBAttributedRequestExecutionUpdate._updateType
+ _OBJC_IVAR_$_SUIBAttributedRequestExecutionUpdate._userTurnIdentifier
+ _OBJC_IVAR_$_SUIBAttributedRequestExecutionUpdateMutation._activities
+ _OBJC_IVAR_$_SUIBAttributedRequestExecutionUpdateMutation._directive
+ _OBJC_IVAR_$_SUIBAttributedRequestExecutionUpdateMutation._requestProgress
+ _OBJC_IVAR_$_SUIBAttributedRequestExecutionUpdateMutation._toolUpdate
+ _OBJC_IVAR_$_SUIBAttributedRequestExecutionUpdateMutation._updateType
+ _OBJC_IVAR_$_SUIBAttributedRequestExecutionUpdateMutation._userTurnIdentifier
+ _OBJC_IVAR_$_SUIBExecutionStatistic._predictedDuration
+ _OBJC_IVAR_$_SUIBExecutionStatistic._predictionConfidence
+ _OBJC_IVAR_$_SUIBExecutionStatistic._shouldPresentActivityStatus
+ _OBJC_IVAR_$_SUIBExecutionStatisticMutation._predictedDuration
+ _OBJC_IVAR_$_SUIBExecutionStatisticMutation._predictionConfidence
+ _OBJC_IVAR_$_SUIBExecutionStatisticMutation._shouldPresentActivityStatus
+ _OBJC_IVAR_$_SUIBExecutionUpdateDirective._directiveType
+ _OBJC_IVAR_$_SUIBExecutionUpdateDirectiveMutation._directiveType
+ _OBJC_IVAR_$_SUIBIntelligenceFlowProgressUpdate._attributedRequestExecutionUpdate
+ _OBJC_IVAR_$_SUIBIntelligenceFlowProgressUpdateMutation._attributedRequestExecutionUpdate
+ _OBJC_IVAR_$_SUIBLatencyRequestProgress._currentRequestPhaseEndingProgress
+ _OBJC_IVAR_$_SUIBLatencyRequestProgress._currentRequestPhaseEstimatedEndTimestamp
+ _OBJC_IVAR_$_SUIBLatencyRequestProgress._currentRequestPhaseProgress
+ _OBJC_IVAR_$_SUIBLatencyRequestProgress._currentRequestPhaseStartingProgress
+ _OBJC_IVAR_$_SUIBLatencyRequestProgressMutation._currentRequestPhaseEndingProgress
+ _OBJC_IVAR_$_SUIBLatencyRequestProgressMutation._currentRequestPhaseEstimatedEndTimestamp
+ _OBJC_IVAR_$_SUIBLatencyRequestProgressMutation._currentRequestPhaseProgress
+ _OBJC_IVAR_$_SUIBLatencyRequestProgressMutation._currentRequestPhaseStartingProgress
+ _OBJC_IVAR_$_SUIBThinkingContext._agentType
+ _OBJC_IVAR_$_SUIBThinkingContext._executionStatistic
+ _OBJC_IVAR_$_SUIBThinkingContext._userQueryEnhancementContext
+ _OBJC_IVAR_$_SUIBThinkingContextMutation._agentType
+ _OBJC_IVAR_$_SUIBThinkingContextMutation._executionStatistic
+ _OBJC_IVAR_$_SUIBThinkingContextMutation._userQueryEnhancementContext
+ _OBJC_IVAR_$_SUIBToolExecutionProgressUpdate._additionalProgressDescription
+ _OBJC_IVAR_$_SUIBToolExecutionProgressUpdate._agentType
+ _OBJC_IVAR_$_SUIBToolExecutionProgressUpdate._applicationIdentifier
+ _OBJC_IVAR_$_SUIBToolExecutionProgressUpdate._prefersVisualProgressIndicator
+ _OBJC_IVAR_$_SUIBToolExecutionProgressUpdate._progress
+ _OBJC_IVAR_$_SUIBToolExecutionProgressUpdate._progressDescription
+ _OBJC_IVAR_$_SUIBToolExecutionProgressUpdate._sourceIdentity
+ _OBJC_IVAR_$_SUIBToolExecutionProgressUpdateMutation._additionalProgressDescription
+ _OBJC_IVAR_$_SUIBToolExecutionProgressUpdateMutation._agentType
+ _OBJC_IVAR_$_SUIBToolExecutionProgressUpdateMutation._applicationIdentifier
+ _OBJC_IVAR_$_SUIBToolExecutionProgressUpdateMutation._prefersVisualProgressIndicator
+ _OBJC_IVAR_$_SUIBToolExecutionProgressUpdateMutation._progress
+ _OBJC_IVAR_$_SUIBToolExecutionProgressUpdateMutation._progressDescription
+ _OBJC_IVAR_$_SUIBToolExecutionProgressUpdateMutation._sourceIdentity
+ _OBJC_IVAR_$_SUIBUserQueryEnhancementContext._rewrittenQuery
+ _OBJC_IVAR_$_SUIBUserQueryEnhancementContextMutation._rewrittenQuery
+ _OBJC_IVAR_$_SUIBUserTurnContext._didEnd
+ _OBJC_IVAR_$_SUIBUserTurnContext._doesIntroduceNewTurn
+ _OBJC_IVAR_$_SUIBUserTurnContext._isActivated
+ _OBJC_IVAR_$_SUIBUserTurnContext._userTurnIdentifier
+ _OBJC_IVAR_$_SUIBUserTurnContext._userTurnType
+ _OBJC_IVAR_$_SUIBUserTurnContextMutation._didEnd
+ _OBJC_IVAR_$_SUIBUserTurnContextMutation._doesIntroduceNewTurn
+ _OBJC_IVAR_$_SUIBUserTurnContextMutation._isActivated
+ _OBJC_IVAR_$_SUIBUserTurnContextMutation._userTurnIdentifier
+ _OBJC_IVAR_$_SUIBUserTurnContextMutation._userTurnType
+ _OBJC_IVAR_$_SUIBVisualCaptureContext._data
+ _OBJC_IVAR_$_SUIBVisualCaptureContextMutation._data
+ _OBJC_METACLASS_$_SUIBActionRepresentation
+ _OBJC_METACLASS_$_SUIBActionRepresentationMutation
+ _OBJC_METACLASS_$_SUIBActionRepresentationSchema
+ _OBJC_METACLASS_$_SUIBActionRepresentationSchemaMutation
+ _OBJC_METACLASS_$_SUIBActivityRepresentation
+ _OBJC_METACLASS_$_SUIBActivityRepresentationMutation
+ _OBJC_METACLASS_$_SUIBAttributedRequestExecutionUpdate
+ _OBJC_METACLASS_$_SUIBAttributedRequestExecutionUpdateMutation
+ _OBJC_METACLASS_$_SUIBExecutionStatistic
+ _OBJC_METACLASS_$_SUIBExecutionStatisticMutation
+ _OBJC_METACLASS_$_SUIBExecutionUpdateDirective
+ _OBJC_METACLASS_$_SUIBExecutionUpdateDirectiveMutation
+ _OBJC_METACLASS_$_SUIBLatencyRequestProgress
+ _OBJC_METACLASS_$_SUIBLatencyRequestProgressMutation
+ _OBJC_METACLASS_$_SUIBThinkingContext
+ _OBJC_METACLASS_$_SUIBThinkingContextMutation
+ _OBJC_METACLASS_$_SUIBToolExecutionProgressUpdate
+ _OBJC_METACLASS_$_SUIBToolExecutionProgressUpdateMutation
+ _OBJC_METACLASS_$_SUIBUserQueryEnhancementContext
+ _OBJC_METACLASS_$_SUIBUserQueryEnhancementContextMutation
+ _OBJC_METACLASS_$_SUIBUserTurnContext
+ _OBJC_METACLASS_$_SUIBUserTurnContextMutation
+ _OBJC_METACLASS_$_SUIBVisualCaptureContext
+ _OBJC_METACLASS_$_SUIBVisualCaptureContextMutation
+ _OUTLINED_FUNCTION_142
+ __OBJC_$_CLASS_METHODS_SUIBActionRepresentation
+ __OBJC_$_CLASS_METHODS_SUIBActionRepresentationSchema
+ __OBJC_$_CLASS_METHODS_SUIBActivityRepresentation
+ __OBJC_$_CLASS_METHODS_SUIBAttributedRequestExecutionUpdate
+ __OBJC_$_CLASS_METHODS_SUIBExecutionStatistic
+ __OBJC_$_CLASS_METHODS_SUIBExecutionUpdateDirective
+ __OBJC_$_CLASS_METHODS_SUIBLatencyRequestProgress
+ __OBJC_$_CLASS_METHODS_SUIBThinkingContext
+ __OBJC_$_CLASS_METHODS_SUIBToolExecutionProgressUpdate
+ __OBJC_$_CLASS_METHODS_SUIBUserQueryEnhancementContext
+ __OBJC_$_CLASS_METHODS_SUIBUserTurnContext
+ __OBJC_$_CLASS_METHODS_SUIBVisualCaptureContext
+ __OBJC_$_CLASS_PROP_LIST_SUIBActionRepresentation
+ __OBJC_$_CLASS_PROP_LIST_SUIBActionRepresentationSchema
+ __OBJC_$_CLASS_PROP_LIST_SUIBActivityRepresentation
+ __OBJC_$_CLASS_PROP_LIST_SUIBAttributedRequestExecutionUpdate
+ __OBJC_$_CLASS_PROP_LIST_SUIBExecutionStatistic
+ __OBJC_$_CLASS_PROP_LIST_SUIBExecutionUpdateDirective
+ __OBJC_$_CLASS_PROP_LIST_SUIBLatencyRequestProgress
+ __OBJC_$_CLASS_PROP_LIST_SUIBThinkingContext
+ __OBJC_$_CLASS_PROP_LIST_SUIBToolExecutionProgressUpdate
+ __OBJC_$_CLASS_PROP_LIST_SUIBUserQueryEnhancementContext
+ __OBJC_$_CLASS_PROP_LIST_SUIBUserTurnContext
+ __OBJC_$_CLASS_PROP_LIST_SUIBVisualCaptureContext
+ __OBJC_$_INSTANCE_METHODS_SUIBActionRepresentation
+ __OBJC_$_INSTANCE_METHODS_SUIBActionRepresentationMutation
+ __OBJC_$_INSTANCE_METHODS_SUIBActionRepresentationSchema
+ __OBJC_$_INSTANCE_METHODS_SUIBActionRepresentationSchemaMutation
+ __OBJC_$_INSTANCE_METHODS_SUIBActivityRepresentation
+ __OBJC_$_INSTANCE_METHODS_SUIBActivityRepresentationMutation
+ __OBJC_$_INSTANCE_METHODS_SUIBAttributedRequestExecutionUpdate
+ __OBJC_$_INSTANCE_METHODS_SUIBAttributedRequestExecutionUpdateMutation
+ __OBJC_$_INSTANCE_METHODS_SUIBExecutionStatistic
+ __OBJC_$_INSTANCE_METHODS_SUIBExecutionStatisticMutation
+ __OBJC_$_INSTANCE_METHODS_SUIBExecutionUpdateDirective
+ __OBJC_$_INSTANCE_METHODS_SUIBExecutionUpdateDirectiveMutation
+ __OBJC_$_INSTANCE_METHODS_SUIBLatencyRequestProgress
+ __OBJC_$_INSTANCE_METHODS_SUIBLatencyRequestProgressMutation
+ __OBJC_$_INSTANCE_METHODS_SUIBThinkingContext
+ __OBJC_$_INSTANCE_METHODS_SUIBThinkingContextMutation
+ __OBJC_$_INSTANCE_METHODS_SUIBToolExecutionProgressUpdate
+ __OBJC_$_INSTANCE_METHODS_SUIBToolExecutionProgressUpdateMutation
+ __OBJC_$_INSTANCE_METHODS_SUIBUserQueryEnhancementContext
+ __OBJC_$_INSTANCE_METHODS_SUIBUserQueryEnhancementContextMutation
+ __OBJC_$_INSTANCE_METHODS_SUIBUserTurnContext
+ __OBJC_$_INSTANCE_METHODS_SUIBUserTurnContextMutation
+ __OBJC_$_INSTANCE_METHODS_SUIBVisualCaptureContext
+ __OBJC_$_INSTANCE_METHODS_SUIBVisualCaptureContextMutation
+ __OBJC_$_INSTANCE_VARIABLES_SUIBActionRepresentation
+ __OBJC_$_INSTANCE_VARIABLES_SUIBActionRepresentationMutation
+ __OBJC_$_INSTANCE_VARIABLES_SUIBActionRepresentationSchema
+ __OBJC_$_INSTANCE_VARIABLES_SUIBActionRepresentationSchemaMutation
+ __OBJC_$_INSTANCE_VARIABLES_SUIBActivityRepresentation
+ __OBJC_$_INSTANCE_VARIABLES_SUIBActivityRepresentationMutation
+ __OBJC_$_INSTANCE_VARIABLES_SUIBAttributedRequestExecutionUpdate
+ __OBJC_$_INSTANCE_VARIABLES_SUIBAttributedRequestExecutionUpdateMutation
+ __OBJC_$_INSTANCE_VARIABLES_SUIBExecutionStatistic
+ __OBJC_$_INSTANCE_VARIABLES_SUIBExecutionStatisticMutation
+ __OBJC_$_INSTANCE_VARIABLES_SUIBExecutionUpdateDirective
+ __OBJC_$_INSTANCE_VARIABLES_SUIBExecutionUpdateDirectiveMutation
+ __OBJC_$_INSTANCE_VARIABLES_SUIBLatencyRequestProgress
+ __OBJC_$_INSTANCE_VARIABLES_SUIBLatencyRequestProgressMutation
+ __OBJC_$_INSTANCE_VARIABLES_SUIBThinkingContext
+ __OBJC_$_INSTANCE_VARIABLES_SUIBThinkingContextMutation
+ __OBJC_$_INSTANCE_VARIABLES_SUIBToolExecutionProgressUpdate
+ __OBJC_$_INSTANCE_VARIABLES_SUIBToolExecutionProgressUpdateMutation
+ __OBJC_$_INSTANCE_VARIABLES_SUIBUserQueryEnhancementContext
+ __OBJC_$_INSTANCE_VARIABLES_SUIBUserQueryEnhancementContextMutation
+ __OBJC_$_INSTANCE_VARIABLES_SUIBUserTurnContext
+ __OBJC_$_INSTANCE_VARIABLES_SUIBUserTurnContextMutation
+ __OBJC_$_INSTANCE_VARIABLES_SUIBVisualCaptureContext
+ __OBJC_$_INSTANCE_VARIABLES_SUIBVisualCaptureContextMutation
+ __OBJC_$_PROP_LIST_SUIBActionRepresentation
+ __OBJC_$_PROP_LIST_SUIBActionRepresentationMutation
+ __OBJC_$_PROP_LIST_SUIBActionRepresentationSchema
+ __OBJC_$_PROP_LIST_SUIBActionRepresentationSchemaMutation
+ __OBJC_$_PROP_LIST_SUIBActivityRepresentation
+ __OBJC_$_PROP_LIST_SUIBActivityRepresentationMutation
+ __OBJC_$_PROP_LIST_SUIBAttributedRequestExecutionUpdate
+ __OBJC_$_PROP_LIST_SUIBAttributedRequestExecutionUpdateMutation
+ __OBJC_$_PROP_LIST_SUIBExecutionStatistic
+ __OBJC_$_PROP_LIST_SUIBExecutionStatisticMutation
+ __OBJC_$_PROP_LIST_SUIBExecutionUpdateDirective
+ __OBJC_$_PROP_LIST_SUIBExecutionUpdateDirectiveMutation
+ __OBJC_$_PROP_LIST_SUIBLatencyRequestProgress
+ __OBJC_$_PROP_LIST_SUIBLatencyRequestProgressMutation
+ __OBJC_$_PROP_LIST_SUIBThinkingContext
+ __OBJC_$_PROP_LIST_SUIBThinkingContextMutation
+ __OBJC_$_PROP_LIST_SUIBToolExecutionProgressUpdate
+ __OBJC_$_PROP_LIST_SUIBToolExecutionProgressUpdateMutation
+ __OBJC_$_PROP_LIST_SUIBUserQueryEnhancementContext
+ __OBJC_$_PROP_LIST_SUIBUserQueryEnhancementContextMutation
+ __OBJC_$_PROP_LIST_SUIBUserTurnContext
+ __OBJC_$_PROP_LIST_SUIBUserTurnContextMutation
+ __OBJC_$_PROP_LIST_SUIBVisualCaptureContext
+ __OBJC_$_PROP_LIST_SUIBVisualCaptureContextMutation
+ __OBJC_CLASS_PROTOCOLS_$_SUIBActionRepresentation
+ __OBJC_CLASS_PROTOCOLS_$_SUIBActionRepresentationSchema
+ __OBJC_CLASS_PROTOCOLS_$_SUIBActivityRepresentation
+ __OBJC_CLASS_PROTOCOLS_$_SUIBAttributedRequestExecutionUpdate
+ __OBJC_CLASS_PROTOCOLS_$_SUIBExecutionStatistic
+ __OBJC_CLASS_PROTOCOLS_$_SUIBExecutionUpdateDirective
+ __OBJC_CLASS_PROTOCOLS_$_SUIBLatencyRequestProgress
+ __OBJC_CLASS_PROTOCOLS_$_SUIBThinkingContext
+ __OBJC_CLASS_PROTOCOLS_$_SUIBToolExecutionProgressUpdate
+ __OBJC_CLASS_PROTOCOLS_$_SUIBUserQueryEnhancementContext
+ __OBJC_CLASS_PROTOCOLS_$_SUIBUserTurnContext
+ __OBJC_CLASS_PROTOCOLS_$_SUIBVisualCaptureContext
+ __OBJC_CLASS_RO_$_SUIBActionRepresentation
+ __OBJC_CLASS_RO_$_SUIBActionRepresentationMutation
+ __OBJC_CLASS_RO_$_SUIBActionRepresentationSchema
+ __OBJC_CLASS_RO_$_SUIBActionRepresentationSchemaMutation
+ __OBJC_CLASS_RO_$_SUIBActivityRepresentation
+ __OBJC_CLASS_RO_$_SUIBActivityRepresentationMutation
+ __OBJC_CLASS_RO_$_SUIBAttributedRequestExecutionUpdate
+ __OBJC_CLASS_RO_$_SUIBAttributedRequestExecutionUpdateMutation
+ __OBJC_CLASS_RO_$_SUIBExecutionStatistic
+ __OBJC_CLASS_RO_$_SUIBExecutionStatisticMutation
+ __OBJC_CLASS_RO_$_SUIBExecutionUpdateDirective
+ __OBJC_CLASS_RO_$_SUIBExecutionUpdateDirectiveMutation
+ __OBJC_CLASS_RO_$_SUIBLatencyRequestProgress
+ __OBJC_CLASS_RO_$_SUIBLatencyRequestProgressMutation
+ __OBJC_CLASS_RO_$_SUIBThinkingContext
+ __OBJC_CLASS_RO_$_SUIBThinkingContextMutation
+ __OBJC_CLASS_RO_$_SUIBToolExecutionProgressUpdate
+ __OBJC_CLASS_RO_$_SUIBToolExecutionProgressUpdateMutation
+ __OBJC_CLASS_RO_$_SUIBUserQueryEnhancementContext
+ __OBJC_CLASS_RO_$_SUIBUserQueryEnhancementContextMutation
+ __OBJC_CLASS_RO_$_SUIBUserTurnContext
+ __OBJC_CLASS_RO_$_SUIBUserTurnContextMutation
+ __OBJC_CLASS_RO_$_SUIBVisualCaptureContext
+ __OBJC_CLASS_RO_$_SUIBVisualCaptureContextMutation
+ __OBJC_METACLASS_RO_$_SUIBActionRepresentation
+ __OBJC_METACLASS_RO_$_SUIBActionRepresentationMutation
+ __OBJC_METACLASS_RO_$_SUIBActionRepresentationSchema
+ __OBJC_METACLASS_RO_$_SUIBActionRepresentationSchemaMutation
+ __OBJC_METACLASS_RO_$_SUIBActivityRepresentation
+ __OBJC_METACLASS_RO_$_SUIBActivityRepresentationMutation
+ __OBJC_METACLASS_RO_$_SUIBAttributedRequestExecutionUpdate
+ __OBJC_METACLASS_RO_$_SUIBAttributedRequestExecutionUpdateMutation
+ __OBJC_METACLASS_RO_$_SUIBExecutionStatistic
+ __OBJC_METACLASS_RO_$_SUIBExecutionStatisticMutation
+ __OBJC_METACLASS_RO_$_SUIBExecutionUpdateDirective
+ __OBJC_METACLASS_RO_$_SUIBExecutionUpdateDirectiveMutation
+ __OBJC_METACLASS_RO_$_SUIBLatencyRequestProgress
+ __OBJC_METACLASS_RO_$_SUIBLatencyRequestProgressMutation
+ __OBJC_METACLASS_RO_$_SUIBThinkingContext
+ __OBJC_METACLASS_RO_$_SUIBThinkingContextMutation
+ __OBJC_METACLASS_RO_$_SUIBToolExecutionProgressUpdate
+ __OBJC_METACLASS_RO_$_SUIBToolExecutionProgressUpdateMutation
+ __OBJC_METACLASS_RO_$_SUIBUserQueryEnhancementContext
+ __OBJC_METACLASS_RO_$_SUIBUserQueryEnhancementContextMutation
+ __OBJC_METACLASS_RO_$_SUIBUserTurnContext
+ __OBJC_METACLASS_RO_$_SUIBUserTurnContextMutation
+ __OBJC_METACLASS_RO_$_SUIBVisualCaptureContext
+ __OBJC_METACLASS_RO_$_SUIBVisualCaptureContextMutation
+ __PROTOCOLS__TtC12SiriUIBridge18UIBridgeServiceSRD.67
+ __PROTOCOLS__TtC12SiriUIBridge26UIBridgeConnectionListener.11
+ ___27-[SUIBThinkingContext init]_block_invoke
+ ___27-[SUIBUserTurnContext init]_block_invoke
+ ___30-[SUIBExecutionStatistic init]_block_invoke
+ ___32-[SUIBActionRepresentation init]_block_invoke
+ ___32-[SUIBVisualCaptureContext init]_block_invoke
+ ___34-[SUIBActivityRepresentation init]_block_invoke
+ ___34-[SUIBLatencyRequestProgress init]_block_invoke
+ ___36-[SUIBExecutionUpdateDirective init]_block_invoke
+ ___37-[SUIBUserTurnContext initWithCoder:]_block_invoke
+ ___38-[SUIBActionRepresentationSchema init]_block_invoke
+ ___39-[SUIBToolExecutionProgressUpdate init]_block_invoke
+ ___39-[SUIBUserQueryEnhancementContext init]_block_invoke
+ ___40-[SUIBExecutionStatistic initWithCoder:]_block_invoke
+ ___42-[SUIBActionRepresentation initWithCoder:]_block_invoke
+ ___42-[SUIBVisualCaptureContext initWithCoder:]_block_invoke
+ ___44-[SUIBActivityRepresentation initWithCoder:]_block_invoke
+ ___44-[SUIBAttributedRequestExecutionUpdate init]_block_invoke
+ ___44-[SUIBLatencyRequestProgress initWithCoder:]_block_invoke
+ ___46-[SUIBExecutionUpdateDirective initWithCoder:]_block_invoke
+ ___48-[SUIBActionRepresentationSchema initWithCoder:]_block_invoke
+ ___49-[SUIBToolExecutionProgressUpdate initWithCoder:]_block_invoke
+ ___54-[SUIBAttributedRequestExecutionUpdate initWithCoder:]_block_invoke
+ ___block_descriptor_32_e37_v16?0"SUIBThinkingContextMutation"8l
+ ___block_descriptor_32_e37_v16?0"SUIBUserTurnContextMutation"8l
+ ___block_descriptor_32_e40_v16?0"SUIBExecutionStatisticMutation"8l
+ ___block_descriptor_32_e42_v16?0"SUIBActionRepresentationMutation"8l
+ ___block_descriptor_32_e42_v16?0"SUIBVisualCaptureContextMutation"8l
+ ___block_descriptor_32_e44_v16?0"SUIBActivityRepresentationMutation"8l
+ ___block_descriptor_32_e44_v16?0"SUIBLatencyRequestProgressMutation"8l
+ ___block_descriptor_32_e46_v16?0"SUIBExecutionUpdateDirectiveMutation"8l
+ ___block_descriptor_32_e48_v16?0"SUIBActionRepresentationSchemaMutation"8l
+ ___block_descriptor_32_e49_v16?0"SUIBToolExecutionProgressUpdateMutation"8l
+ ___block_descriptor_32_e49_v16?0"SUIBUserQueryEnhancementContextMutation"8l
+ ___block_descriptor_32_e54_v16?0"SUIBAttributedRequestExecutionUpdateMutation"8l
+ ___block_descriptor_40_e46_v16?0"SUIBExecutionUpdateDirectiveMutation"8l
+ ___block_descriptor_40_e8_32s_e42_v16?0"SUIBVisualCaptureContextMutation"8ls32l8
+ ___block_descriptor_48_e8_32s40s_e48_v16?0"SUIBActionRepresentationSchemaMutation"8ls32l8s40l8
+ ___block_descriptor_51_e8_32s_e37_v16?0"SUIBUserTurnContextMutation"8ls32l8
+ ___block_descriptor_56_e8_32s40s48s_e40_v16?0"SUIBExecutionStatisticMutation"8ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s_e44_v16?0"SUIBLatencyRequestProgressMutation"8ls32l8s40l8
+ ___block_descriptor_60_e8_32s40s48s_e52_v16?0"SUIBIntelligenceFlowProgressUpdateMutation"8ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56s_e42_v16?0"SUIBActionRepresentationMutation"8ls32l8s40l8s48l8s56l8
+ ___block_descriptor_64_e8_32s40s48s_e44_v16?0"SUIBActivityRepresentationMutation"8ls32l8s40l8s48l8
+ ___block_descriptor_77_e8_32s40s48s_e49_v16?0"SUIBToolExecutionProgressUpdateMutation"8ls32l8s40l8s48l8
+ ___block_descriptor_80_e8_32s40s48s56s64s_e54_v16?0"SUIBAttributedRequestExecutionUpdateMutation"8ls32l8s40l8s48l8s56l8s64l8
+ ___swift__destructor
+ ___swift_closure_destructor
+ ___swift_closure_destructor.102
+ ___swift_closure_destructor.104
+ ___swift_closure_destructor.105
+ ___swift_closure_destructor.108
+ ___swift_closure_destructor.11
+ ___swift_closure_destructor.110
+ ___swift_closure_destructor.113
+ ___swift_closure_destructor.114
+ ___swift_closure_destructor.116
+ ___swift_closure_destructor.12
+ ___swift_closure_destructor.120
+ ___swift_closure_destructor.121
+ ___swift_closure_destructor.122
+ ___swift_closure_destructor.124
+ ___swift_closure_destructor.126
+ ___swift_closure_destructor.132
+ ___swift_closure_destructor.135
+ ___swift_closure_destructor.138
+ ___swift_closure_destructor.14
+ ___swift_closure_destructor.143
+ ___swift_closure_destructor.144
+ ___swift_closure_destructor.146
+ ___swift_closure_destructor.150
+ ___swift_closure_destructor.154
+ ___swift_closure_destructor.156
+ ___swift_closure_destructor.157
+ ___swift_closure_destructor.162
+ ___swift_closure_destructor.165
+ ___swift_closure_destructor.168
+ ___swift_closure_destructor.17
+ ___swift_closure_destructor.174
+ ___swift_closure_destructor.176
+ ___swift_closure_destructor.179
+ ___swift_closure_destructor.180
+ ___swift_closure_destructor.186
+ ___swift_closure_destructor.187
+ ___swift_closure_destructor.192
+ ___swift_closure_destructor.195
+ ___swift_closure_destructor.198
+ ___swift_closure_destructor.2
+ ___swift_closure_destructor.20
+ ___swift_closure_destructor.205
+ ___swift_closure_destructor.206
+ ___swift_closure_destructor.209
+ ___swift_closure_destructor.20Tm
+ ___swift_closure_destructor.211
+ ___swift_closure_destructor.217
+ ___swift_closure_destructor.223
+ ___swift_closure_destructor.225
+ ___swift_closure_destructor.229
+ ___swift_closure_destructor.23
+ ___swift_closure_destructor.26
+ ___swift_closure_destructor.29
+ ___swift_closure_destructor.31
+ ___swift_closure_destructor.32
+ ___swift_closure_destructor.34
+ ___swift_closure_destructor.35
+ ___swift_closure_destructor.38
+ ___swift_closure_destructor.41
+ ___swift_closure_destructor.42
+ ___swift_closure_destructor.42Tm
+ ___swift_closure_destructor.44
+ ___swift_closure_destructor.46
+ ___swift_closure_destructor.47
+ ___swift_closure_destructor.5
+ ___swift_closure_destructor.50
+ ___swift_closure_destructor.53
+ ___swift_closure_destructor.56
+ ___swift_closure_destructor.58
+ ___swift_closure_destructor.59
+ ___swift_closure_destructor.61
+ ___swift_closure_destructor.62
+ ___swift_closure_destructor.64
+ ___swift_closure_destructor.65
+ ___swift_closure_destructor.68
+ ___swift_closure_destructor.71
+ ___swift_closure_destructor.72
+ ___swift_closure_destructor.74
+ ___swift_closure_destructor.75
+ ___swift_closure_destructor.78
+ ___swift_closure_destructor.8
+ ___swift_closure_destructor.80
+ ___swift_closure_destructor.83
+ ___swift_closure_destructor.84
+ ___swift_closure_destructor.86
+ ___swift_closure_destructor.9
+ ___swift_closure_destructor.90
+ ___swift_closure_destructor.92
+ ___swift_closure_destructor.94
+ ___swift_closure_destructor.96
+ ___swift_closure_destructor.98
+ ___swift_closure_destructor.9Tm
+ ___swift_closure_destructorTm
+ _block_copy_helper.104
+ _block_copy_helper.108
+ _block_copy_helper.110
+ _block_copy_helper.116
+ _block_copy_helper.122
+ _block_copy_helper.13
+ _block_copy_helper.134
+ _block_copy_helper.138
+ _block_copy_helper.140
+ _block_copy_helper.146
+ _block_copy_helper.149
+ _block_copy_helper.15
+ _block_copy_helper.152
+ _block_copy_helper.158
+ _block_copy_helper.160
+ _block_copy_helper.164
+ _block_copy_helper.170
+ _block_copy_helper.176
+ _block_copy_helper.182
+ _block_copy_helper.188
+ _block_copy_helper.19
+ _block_copy_helper.190
+ _block_copy_helper.194
+ _block_copy_helper.200
+ _block_copy_helper.207
+ _block_copy_helper.212
+ _block_copy_helper.213
+ _block_copy_helper.219
+ _block_copy_helper.225
+ _block_copy_helper.228
+ _block_copy_helper.231
+ _block_copy_helper.25
+ _block_copy_helper.26
+ _block_copy_helper.31
+ _block_copy_helper.55
+ _block_copy_helper.56
+ _block_copy_helper.60
+ _block_copy_helper.63
+ _block_copy_helper.67
+ _block_copy_helper.7
+ _block_copy_helper.73
+ _block_copy_helper.78
+ _block_copy_helper.80
+ _block_copy_helper.86
+ _block_copy_helper.89
+ _block_copy_helper.92
+ _block_copy_helper.97
+ _block_descriptor.106
+ _block_descriptor.110
+ _block_descriptor.112
+ _block_descriptor.118
+ _block_descriptor.124
+ _block_descriptor.136
+ _block_descriptor.140
+ _block_descriptor.142
+ _block_descriptor.148
+ _block_descriptor.15
+ _block_descriptor.151
+ _block_descriptor.154
+ _block_descriptor.160
+ _block_descriptor.162
+ _block_descriptor.166
+ _block_descriptor.17
+ _block_descriptor.172
+ _block_descriptor.178
+ _block_descriptor.184
+ _block_descriptor.190
+ _block_descriptor.192
+ _block_descriptor.196
+ _block_descriptor.202
+ _block_descriptor.209
+ _block_descriptor.21
+ _block_descriptor.214
+ _block_descriptor.215
+ _block_descriptor.221
+ _block_descriptor.227
+ _block_descriptor.230
+ _block_descriptor.233
+ _block_descriptor.27
+ _block_descriptor.28
+ _block_descriptor.33
+ _block_descriptor.57
+ _block_descriptor.58
+ _block_descriptor.62
+ _block_descriptor.65
+ _block_descriptor.69
+ _block_descriptor.75
+ _block_descriptor.80
+ _block_descriptor.82
+ _block_descriptor.88
+ _block_descriptor.9
+ _block_descriptor.91
+ _block_descriptor.94
+ _block_descriptor.99
+ _block_destroy_helper.105
+ _block_destroy_helper.109
+ _block_destroy_helper.111
+ _block_destroy_helper.117
+ _block_destroy_helper.123
+ _block_destroy_helper.135
+ _block_destroy_helper.139
+ _block_destroy_helper.14
+ _block_destroy_helper.141
+ _block_destroy_helper.147
+ _block_destroy_helper.150
+ _block_destroy_helper.153
+ _block_destroy_helper.159
+ _block_destroy_helper.16
+ _block_destroy_helper.161
+ _block_destroy_helper.165
+ _block_destroy_helper.171
+ _block_destroy_helper.177
+ _block_destroy_helper.183
+ _block_destroy_helper.189
+ _block_destroy_helper.191
+ _block_destroy_helper.195
+ _block_destroy_helper.20
+ _block_destroy_helper.201
+ _block_destroy_helper.208
+ _block_destroy_helper.213
+ _block_destroy_helper.214
+ _block_destroy_helper.220
+ _block_destroy_helper.226
+ _block_destroy_helper.229
+ _block_destroy_helper.232
+ _block_destroy_helper.26
+ _block_destroy_helper.27
+ _block_destroy_helper.32
+ _block_destroy_helper.56
+ _block_destroy_helper.57
+ _block_destroy_helper.61
+ _block_destroy_helper.64
+ _block_destroy_helper.68
+ _block_destroy_helper.74
+ _block_destroy_helper.79
+ _block_destroy_helper.8
+ _block_destroy_helper.81
+ _block_destroy_helper.87
+ _block_destroy_helper.90
+ _block_destroy_helper.93
+ _block_destroy_helper.98
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$actionRepresentation
+ _objc_msgSend$activities
+ _objc_msgSend$activityType
+ _objc_msgSend$agentType
+ _objc_msgSend$applicationIdentifier
+ _objc_msgSend$archivedDataWithRootObject:requiringSecureCoding:error:
+ _objc_msgSend$attributedRequestExecutionUpdate
+ _objc_msgSend$boolValue
+ _objc_msgSend$currentRequestPhaseEndingProgress
+ _objc_msgSend$currentRequestPhaseEstimatedEndTimestamp
+ _objc_msgSend$currentRequestPhaseProgress
+ _objc_msgSend$currentRequestPhaseStartingProgress
+ _objc_msgSend$data
+ _objc_msgSend$didEnd
+ _objc_msgSend$directive
+ _objc_msgSend$directiveType
+ _objc_msgSend$doesIntroduceNewTurn
+ _objc_msgSend$domain
+ _objc_msgSend$executionStatistic
+ _objc_msgSend$initWithDouble:
+ _objc_msgSend$initWithFloat:
+ _objc_msgSend$isActivated
+ _objc_msgSend$kind
+ _objc_msgSend$predictedDuration
+ _objc_msgSend$predictionConfidence
+ _objc_msgSend$prefersVisualProgressIndicator
+ _objc_msgSend$requestProgress
+ _objc_msgSend$rewrittenQuery
+ _objc_msgSend$schema
+ _objc_msgSend$serviceName
+ _objc_msgSend$setActionRepresentation:
+ _objc_msgSend$setActivities:
+ _objc_msgSend$setActivityType:
+ _objc_msgSend$setAgentType:
+ _objc_msgSend$setApplicationIdentifier:
+ _objc_msgSend$setAttributedRequestExecutionUpdate:
+ _objc_msgSend$setCurrentRequestPhaseEndingProgress:
+ _objc_msgSend$setCurrentRequestPhaseEstimatedEndTimestamp:
+ _objc_msgSend$setCurrentRequestPhaseProgress:
+ _objc_msgSend$setCurrentRequestPhaseStartingProgress:
+ _objc_msgSend$setData:
+ _objc_msgSend$setDidEnd:
+ _objc_msgSend$setDirective:
+ _objc_msgSend$setDirectiveType:
+ _objc_msgSend$setDoesIntroduceNewTurn:
+ _objc_msgSend$setDomain:
+ _objc_msgSend$setExecutionStatistic:
+ _objc_msgSend$setIsActivated:
+ _objc_msgSend$setKind:
+ _objc_msgSend$setPredictedDuration:
+ _objc_msgSend$setPredictionConfidence:
+ _objc_msgSend$setPrefersVisualProgressIndicator:
+ _objc_msgSend$setRequestProgress:
+ _objc_msgSend$setRewrittenQuery:
+ _objc_msgSend$setSchema:
+ _objc_msgSend$setShouldPresentActivityStatus:
+ _objc_msgSend$setSourceIdentity:
+ _objc_msgSend$setThinkingContext:
+ _objc_msgSend$setToolID:
+ _objc_msgSend$setToolUpdate:
+ _objc_msgSend$setUpdateType:
+ _objc_msgSend$setUserQueryEnhancementContext:
+ _objc_msgSend$setUserTurnContext:
+ _objc_msgSend$setUserTurnIdentifier:
+ _objc_msgSend$setUserTurnType:
+ _objc_msgSend$shouldPresentActivityStatus
+ _objc_msgSend$sourceIdentity
+ _objc_msgSend$thinkingContext
+ _objc_msgSend$toolID
+ _objc_msgSend$toolUpdate
+ _objc_msgSend$uiBridgeServiceReceivedVisualCaptureContext:
+ _objc_msgSend$unarchivedObjectOfClasses:fromData:error:
+ _objc_msgSend$updateType
+ _objc_msgSend$userQueryEnhancementContext
+ _objc_msgSend$userTurnContext
+ _objc_msgSend$userTurnIdentifier
+ _objc_msgSend$userTurnType
+ _objc_retain_x28
+ _swift_bridgeObjectRelease_n
+ _swift_release_x19
+ _swift_release_x20
+ _swift_release_x21
+ _swift_release_x22
+ _swift_release_x24
+ _swift_release_x26
+ _swift_release_x27
+ _swift_release_x8
+ _swift_release_x9
+ _swift_retain_x19
+ _swift_retain_x2
+ _swift_retain_x20
+ _swift_retain_x21
+ _swift_retain_x22
+ _swift_retain_x24
+ _swift_retain_x27
+ _swift_retain_x28
+ _symbolic So24SUIBVisualCaptureContextC
+ _symbolic So24SUIBVisualCaptureContextCm
+ _symbolic So27SUIBThinkingContextMutationCIgg_
+ _symbolic So27SUIBUserTurnContextMutationCIgg_
+ _symbolic So30SUIBExecutionStatisticMutationCIgg_
+ _symbolic So32SUIBActionRepresentationMutationCIgg_
+ _symbolic So34SUIBActivityRepresentationMutationCIgg_
+ _symbolic So34SUIBLatencyRequestProgressMutationCIgg_
+ _symbolic So36SUIBExecutionUpdateDirectiveMutationCIgg_
+ _symbolic So38SUIBActionRepresentationSchemaMutationCIgg_
+ _symbolic So39SUIBToolExecutionProgressUpdateMutationCIgg_
+ _symbolic So39SUIBUserQueryEnhancementContextMutationCIgg_
+ _symbolic So44SUIBAttributedRequestExecutionUpdateMutationCIgg_
+ _symbolic _____Sg 10Foundation4DateV
+ _symbolic _____Sg 16IntelligenceFlow19SessionStatusUpdateV021ToolExecutionProgressE0V14SourceIdentityO
+ _symbolic _____Sg 16IntelligenceFlow19SessionStatusUpdateV026AttributedRequestExecutionE0V08ActivityH9StatisticV
+ _symbolic _____Sg 16IntelligenceFlow19SessionStatusUpdateV026AttributedRequestExecutionE0V0G8ProgressV
+ _symbolic _____Sg 16IntelligenceFlow19SessionStatusUpdateV026AttributedRequestExecutionE0V15UserTurnContextV0iJ4TypeO
+ _symbolic _____Sg 16IntelligenceFlow19SessionStatusUpdateV026AttributedRequestExecutionE0V27UserQueryEnhancementContextV
+ _symbolic _____Sg 16IntelligenceFlow7AgentIDV
- __PROTOCOLS__TtC12SiriUIBridge18UIBridgeServiceSRD.68
- __PROTOCOLS__TtC12SiriUIBridge26UIBridgeConnectionListener.12
- ___block_descriptor_52_e8_32s40s_e52_v16?0"SUIBIntelligenceFlowProgressUpdateMutation"8ls32l8s40l8
- _block_copy_helper.105
- _block_copy_helper.111
- _block_copy_helper.117
- _block_copy_helper.123
- _block_copy_helper.129
- _block_copy_helper.135
- _block_copy_helper.139
- _block_copy_helper.141
- _block_copy_helper.147
- _block_copy_helper.150
- _block_copy_helper.153
- _block_copy_helper.159
- _block_copy_helper.161
- _block_copy_helper.165
- _block_copy_helper.172
- _block_copy_helper.177
- _block_copy_helper.180
- _block_copy_helper.183
- _block_copy_helper.189
- _block_copy_helper.191
- _block_copy_helper.195
- _block_copy_helper.202
- _block_copy_helper.208
- _block_copy_helper.210
- _block_copy_helper.214
- _block_copy_helper.218
- _block_copy_helper.226
- _block_copy_helper.232
- _block_copy_helper.238
- _block_copy_helper.27
- _block_copy_helper.38
- _block_copy_helper.57
- _block_copy_helper.68
- _block_copy_helper.79
- _block_copy_helper.8
- _block_copy_helper.81
- _block_copy_helper.87
- _block_copy_helper.93
- _block_copy_helper.99
- _block_descriptor.10
- _block_descriptor.101
- _block_descriptor.107
- _block_descriptor.113
- _block_descriptor.119
- _block_descriptor.125
- _block_descriptor.131
- _block_descriptor.137
- _block_descriptor.141
- _block_descriptor.143
- _block_descriptor.149
- _block_descriptor.152
- _block_descriptor.155
- _block_descriptor.161
- _block_descriptor.163
- _block_descriptor.167
- _block_descriptor.174
- _block_descriptor.179
- _block_descriptor.182
- _block_descriptor.185
- _block_descriptor.191
- _block_descriptor.193
- _block_descriptor.197
- _block_descriptor.204
- _block_descriptor.210
- _block_descriptor.212
- _block_descriptor.216
- _block_descriptor.220
- _block_descriptor.228
- _block_descriptor.234
- _block_descriptor.240
- _block_descriptor.29
- _block_descriptor.40
- _block_descriptor.59
- _block_descriptor.70
- _block_descriptor.81
- _block_descriptor.83
- _block_descriptor.89
- _block_descriptor.95
- _block_destroy_helper.100
- _block_destroy_helper.106
- _block_destroy_helper.112
- _block_destroy_helper.118
- _block_destroy_helper.124
- _block_destroy_helper.130
- _block_destroy_helper.136
- _block_destroy_helper.140
- _block_destroy_helper.142
- _block_destroy_helper.148
- _block_destroy_helper.151
- _block_destroy_helper.154
- _block_destroy_helper.160
- _block_destroy_helper.162
- _block_destroy_helper.166
- _block_destroy_helper.173
- _block_destroy_helper.178
- _block_destroy_helper.181
- _block_destroy_helper.184
- _block_destroy_helper.190
- _block_destroy_helper.192
- _block_destroy_helper.196
- _block_destroy_helper.203
- _block_destroy_helper.209
- _block_destroy_helper.211
- _block_destroy_helper.215
- _block_destroy_helper.219
- _block_destroy_helper.227
- _block_destroy_helper.233
- _block_destroy_helper.239
- _block_destroy_helper.28
- _block_destroy_helper.39
- _block_destroy_helper.58
- _block_destroy_helper.69
- _block_destroy_helper.80
- _block_destroy_helper.82
- _block_destroy_helper.88
- _block_destroy_helper.9
- _block_destroy_helper.94
- _objectdestroy.10Tm
- _objectdestroy.21Tm
- _objectdestroy.43Tm
- _objectdestroyTm
CStrings:
+ "!"
+ "<%@: %p> didEnd=%@ isActivated=%@ userTurnType=%lu userTurnIdentifier=%@ doesIntroduceNewTurn=%@"
+ "Getting UIBridgeServiceDelegate"
+ "NO"
+ "New connection: %s"
+ "SUIBActionRepresentation toolID: %@, applicationIdentifier: %@, schema: %@, executionStatistic: %@"
+ "SUIBActionRepresentation::applicationIdentifier"
+ "SUIBActionRepresentation::executionStatistic"
+ "SUIBActionRepresentation::schema"
+ "SUIBActionRepresentation::toolID"
+ "SUIBActionRepresentationSchema kind: %@, domain: %@"
+ "SUIBActionRepresentationSchema::domain"
+ "SUIBActionRepresentationSchema::kind"
+ "SUIBActivityRepresentation activityType: %lu, thinkingContext: %@, userTurnContext: %@, actionRepresentation: %@"
+ "SUIBActivityRepresentation::actionRepresentation"
+ "SUIBActivityRepresentation::activityType"
+ "SUIBActivityRepresentation::agentType"
+ "SUIBActivityRepresentation::thinkingContext"
+ "SUIBActivityRepresentation::userQueryEnhancementContext"
+ "SUIBActivityRepresentation::userTurnContext"
+ "SUIBAttributedRequestExecutionUpdate updateType: %lu, requestProgress: %@, toolUpdate: %@, activities: %@, directive: %@, userTurnIdentifier: %@"
+ "SUIBAttributedRequestExecutionUpdate::activities"
+ "SUIBAttributedRequestExecutionUpdate::directive"
+ "SUIBAttributedRequestExecutionUpdate::requestProgress"
+ "SUIBAttributedRequestExecutionUpdate::toolUpdate"
+ "SUIBAttributedRequestExecutionUpdate::updateType"
+ "SUIBAttributedRequestExecutionUpdate::userTurnIdentifier"
+ "SUIBExecutionStatistic predictedDuration: %@, predictionConfidence: %@, shouldPresentActivityStatus: %@"
+ "SUIBExecutionStatistic::predictedDuration"
+ "SUIBExecutionStatistic::predictionConfidence"
+ "SUIBExecutionStatistic::shouldPresentActivityStatus"
+ "SUIBExecutionUpdateDirective directiveType: %lu"
+ "SUIBExecutionUpdateDirective::directiveType"
+ "SUIBIntelligenceFlowProgressUpdate progress: %f, progressDescription: %@, additionalProgressDescription: %@, attributedRequestExecutionUpdate: %@"
+ "SUIBIntelligenceFlowProgressUpdate::attributedRequestExecutionUpdate"
+ "SUIBLatencyRequestProgress currentRequestPhaseStartingProgress: %f currentRequestPhaseEndingProgress: %f currentRequestPhaseProgress: %@ currentRequestPhaseEstimatedEndTimestamp: %@"
+ "SUIBLatencyRequestProgress::currentRequestPhaseEndingProgress"
+ "SUIBLatencyRequestProgress::currentRequestPhaseEstimatedEndTimestamp"
+ "SUIBLatencyRequestProgress::currentRequestPhaseProgress"
+ "SUIBLatencyRequestProgress::currentRequestPhaseStartingProgress"
+ "SUIBThinkingContext agentType: %lu, userQueryEnhancementContext: %@, executionStatistic: %@"
+ "SUIBThinkingContext::executionStatistic"
+ "SUIBToolExecutionProgressUpdate progress: %f, progressDescription: %@, additionalProgressDescription: %@, sourceIdentity: %lu, applicationIdentifier: %@, agentType: %lu, prefersVisualProgressIndicator: %@"
+ "SUIBToolExecutionProgressUpdate::additionalProgressDescription"
+ "SUIBToolExecutionProgressUpdate::agentType"
+ "SUIBToolExecutionProgressUpdate::applicationIdentifier"
+ "SUIBToolExecutionProgressUpdate::prefersVisualProgressIndicator"
+ "SUIBToolExecutionProgressUpdate::progress"
+ "SUIBToolExecutionProgressUpdate::progressDescription"
+ "SUIBToolExecutionProgressUpdate::sourceIdentity"
+ "SUIBUserQueryEnhancement::rewrittenQuery"
+ "SUIBUserQueryEnhancementContext rewritten query: %@"
+ "SUIBVisualCaptureContext"
+ "SUIBVisualCaptureContext::data"
+ "YES"
+ "connection is nil. Returning nil UIBridgeServiceDelegate"
+ "didEnd"
+ "doesIntroduceNewTurn"
+ "isActivated"
+ "userTurnIdentifier"
+ "userTurnType"
+ "v16@?0@\"SUIBActionRepresentationMutation\"8"
+ "v16@?0@\"SUIBActionRepresentationSchemaMutation\"8"
+ "v16@?0@\"SUIBActivityRepresentationMutation\"8"
+ "v16@?0@\"SUIBAttributedRequestExecutionUpdateMutation\"8"
+ "v16@?0@\"SUIBExecutionStatisticMutation\"8"
+ "v16@?0@\"SUIBExecutionUpdateDirectiveMutation\"8"
+ "v16@?0@\"SUIBLatencyRequestProgressMutation\"8"
+ "v16@?0@\"SUIBThinkingContextMutation\"8"
+ "v16@?0@\"SUIBToolExecutionProgressUpdateMutation\"8"
+ "v16@?0@\"SUIBUserQueryEnhancementContextMutation\"8"
+ "v16@?0@\"SUIBUserTurnContextMutation\"8"
+ "v16@?0@\"SUIBVisualCaptureContextMutation\"8"
- "#16@0:8"
- "$__lazy_storage_$_timeoutExtension"
- ".cxx_destruct"
- "@\"AFBluetoothHeadGestureConfiguration\"16@0:8"
- "@\"AFEndpointInfo\"16@0:8"
- "@\"AFInstanceInfo\"16@0:8"
- "@\"AFPeerInfo\"16@0:8"
- "@\"AFSpeechInfo\"16@0:8"
- "@\"NSArray\""
- "@\"NSDictionary\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSString\"40@0:8@\"NSString\"16@\"NSString\"24@\"NSBundle\"32"
- "@\"NSUUID\""
- "@\"SUIBBridgedMatch\""
- "@\"SUIBIntelligenceFlowActionSummary\""
- "@\"SUIBIntelligenceFlowProgressUpdate\""
- "@\"SUIBIntelligenceFlowStatusNotification\""
- "@\"SUIBNLRouterSummary\""
- "@\"SUIBSiriInAppResponse\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@24@0:8@?16"
- "@24@0:8Q16"
- "@24@0:8^{_NSZone=}16"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@32"
- "AFBridgeConnectionListenerDelegate"
- "AFRequestDispatcherServiceHelper"
- "AFServiceHelper"
- "AFUIBridgeService"
- "AFUIBridgeServiceDelegate"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"NSURL\"16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B32@0:8@\"NSXPCListener\"16@\"NSXPCConnection\"24"
- "B32@0:8@16@24"
- "I16@0:8"
- "NSCoding"
- "NSCopying"
- "NSObject"
- "NSSecureCoding"
- "NSXPCListenerDelegate"
- "Q"
- "Q16@0:8"
- "SUIBBridgedMatch"
- "SUIBIntelligenceFlowActionSummary"
- "SUIBIntelligenceFlowActionSummaryMutation"
- "SUIBIntelligenceFlowActionSummaryParameterMatcher"
- "SUIBIntelligenceFlowParameterSummary"
- "SUIBIntelligenceFlowParameterSummaryMutation"
- "SUIBIntelligenceFlowProgressUpdate"
- "SUIBIntelligenceFlowProgressUpdate progress: %f, progressDescription: %@, additionalProgressDescription: %@"
- "SUIBIntelligenceFlowProgressUpdateMutation"
- "SUIBIntelligenceFlowStatusNotification"
- "SUIBIntelligenceFlowStatusNotificationMutation"
- "SUIBNLRouterSummary"
- "SUIBNLRouterSummaryMutation"
- "SUIBOrchestrationTask"
- "SUIBOrchestrationTaskMutation"
- "SUIBRegexMatch"
- "SUIBRequestProgress"
- "SUIBRequestProgressMutation"
- "SUIBSessionRetrieved"
- "SUIBSessionRetrievedMutation"
- "SUIBSessionRetrievedPayload"
- "SUIBSessionRetrievedPayloadMutation"
- "SUIBSiriInAppResponse"
- "SUIBSiriInAppResponseMutation"
- "SUIBSiriResponse"
- "SUIBSiriResponseMutation"
- "SUIBSystemTurnInterruptionEndedContext"
- "SUIBSystemTurnInterruptionEndedContextMutation"
- "SUIBSystemTurnInterruptionStartedContext"
- "SUIBSystemTurnInterruptionStartedContextMutation"
- "SUIBTypingSessionStarted"
- "SUIBTypingSessionStartedMutation"
- "SUIBUIBridgeClient"
- "SUIBUIBridgeServiceDelegate"
- "SUIBUIBridgeServiceProtocol"
- "SUIBUserSpeechPresence"
- "SUIBUserTurnEndedContext"
- "SUIBUserTurnFinalizedContext"
- "T#,R"
- "T@\"NSArray\",C,N,V_messages"
- "T@\"NSArray\",C,N,V_retrievedPayload"
- "T@\"NSArray\",R,C,N,V_messages"
- "T@\"NSArray\",R,C,N,V_retrievedPayload"
- "T@\"NSDictionary\",C,N,V_parameterSummaries"
- "T@\"NSDictionary\",R,C,N,V_parameterSummaries"
- "T@\"NSString\",&,N,V_bundleIdentifier"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",C,N,V_additionalProgressDescription"
- "T@\"NSString\",C,N,V_errorDescription"
- "T@\"NSString\",C,N,V_formatString"
- "T@\"NSString\",C,N,V_progressDescription"
- "T@\"NSString\",C,N,V_rewrittenUtterance"
- "T@\"NSString\",C,N,V_sessionId"
- "T@\"NSString\",C,N,V_statusString"
- "T@\"NSString\",C,N,V_value"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,C,N,V_additionalProgressDescription"
- "T@\"NSString\",R,C,N,V_bundleIdentifier"
- "T@\"NSString\",R,C,N,V_errorDescription"
- "T@\"NSString\",R,C,N,V_formatString"
- "T@\"NSString\",R,C,N,V_progressDescription"
- "T@\"NSString\",R,C,N,V_rewrittenUtterance"
- "T@\"NSString\",R,C,N,V_sessionId"
- "T@\"NSString\",R,C,N,V_statusString"
- "T@\"NSString\",R,C,N,V_value"
- "T@\"NSUUID\",&,N,V_taskId"
- "T@\"NSUUID\",C,N,V_typingSessionId"
- "T@\"NSUUID\",C,N,V_userTurnID"
- "T@\"NSUUID\",R,C,N,V_taskId"
- "T@\"NSUUID\",R,C,N,V_typingSessionId"
- "T@\"NSUUID\",R,C,N,V_userTurnID"
- "T@\"SUIBBridgedMatch\",R,N,V_bridgedMatch"
- "T@\"SUIBIntelligenceFlowActionSummary\",&,N,V_intelligenceFlowActionSummary"
- "T@\"SUIBIntelligenceFlowActionSummary\",R,N,V_intelligenceFlowActionSummary"
- "T@\"SUIBIntelligenceFlowProgressUpdate\",&,N,V_intelligenceFlowProgressUpdate"
- "T@\"SUIBIntelligenceFlowProgressUpdate\",R,N,V_intelligenceFlowProgressUpdate"
- "T@\"SUIBIntelligenceFlowStatusNotification\",&,N,V_intelligenceFlowStatusNotification"
- "T@\"SUIBIntelligenceFlowStatusNotification\",R,N,V_intelligenceFlowStatusNotification"
- "T@\"SUIBNLRouterSummary\",&,N,V_nlRouterSummary"
- "T@\"SUIBNLRouterSummary\",R,N,V_nlRouterSummary"
- "T@\"SUIBSiriInAppResponse\",&,N,V_inAppResponse"
- "T@\"SUIBSiriInAppResponse\",R,N,V_inAppResponse"
- "TB,N,V_isInvocationUser"
- "TB,N,V_isSameUser"
- "TB,R"
- "TQ,N,V_decision"
- "TQ,N,V_mitigationResult"
- "TQ,N,V_outcome"
- "TQ,N,V_progressType"
- "TQ,N,V_valueType"
- "TQ,R"
- "TQ,R,N,V_mitigationResult"
- "TQ,R,N,V_outcome"
- "TQ,R,N,V_progressType"
- "TQ,R,N,V_valueType"
- "Tf,N,V_progress"
- "Tf,R,N,V_progress"
- "UUIDString"
- "Vv16@0:8"
- "Vv20@0:8B16"
- "Vv24@0:8@\"NSArray\"16"
- "Vv24@0:8@\"NSString\"16"
- "Vv24@0:8@\"NSUUID\"16"
- "Vv24@0:8@\"SUIBRequestProgress\"16"
- "Vv24@0:8@\"SUIBSessionRetrieved\"16"
- "Vv24@0:8@\"SUIBSiriResponse\"16"
- "Vv24@0:8@\"SUIBSystemTurnInterruptionEndedContext\"16"
- "Vv24@0:8@\"SUIBSystemTurnInterruptionStartedContext\"16"
- "Vv24@0:8@\"SUIBTypingSessionStarted\"16"
- "Vv24@0:8@\"SUIBUserSpeechPresence\"16"
- "Vv24@0:8@\"SUIBUserTurnEndedContext\"16"
- "Vv24@0:8@\"SUIBUserTurnFinalizedContext\"16"
- "Vv24@0:8@16"
- "Vv24@0:8Q16"
- "Vv32@0:8Q16@\"NSString\"24"
- "Vv32@0:8Q16@24"
- "^{_NSZone=}16@0:8"
- "_TtC12SiriUIBridge18UIBridgeServiceSRD"
- "_TtC12SiriUIBridge18UISessionProcessor"
- "_TtC12SiriUIBridge24ProgressUpdateTranslator"
- "_TtC12SiriUIBridge26UIBridgeConnectionListener"
- "_TtC12SiriUIBridge30UIBridgeServiceDelegateWrapper"
- "_TtC12SiriUIBridge8UIBridge"
- "_TtP12SiriUIBridge38UIBridgeServiceDelegateWrapperProtocol_"
- "_additionalProgressDescription"
- "_bridgedMatch"
- "_bundleIdentifier"
- "_decision"
- "_errorDescription"
- "_formatString"
- "_inAppResponse"
- "_intelligenceFlowActionSummary"
- "_intelligenceFlowProgressUpdate"
- "_intelligenceFlowStatusNotification"
- "_isInvocationUser"
- "_isSameUser"
- "_messages"
- "_mitigationResult"
- "_nlRouterSummary"
- "_outcome"
- "_parameterSummaries"
- "_progress"
- "_progressDescription"
- "_progressType"
- "_retrievedPayload"
- "_rewrittenUtterance"
- "_sessionId"
- "_setQueue:"
- "_statusString"
- "_taskId"
- "_typingSessionId"
- "_userTurnID"
- "_value"
- "_valueType"
- "addObject:"
- "additionalProgressDescription"
- "allocWithZone:"
- "assistantId"
- "assistantLocalizedStringForKey:table:bundle:"
- "audioSessionID"
- "autorelease"
- "bridgedMatch"
- "bundleIdentifier"
- "callState"
- "captureReference"
- "captured"
- "class"
- "conformsToProtocol:"
- "connection"
- "connectionInterrupted"
- "connectionInvalidated"
- "connectionQueue"
- "copy"
- "copyWithZone:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "currentAuthorizationStyle:"
- "currentLocationWithAccuracy:timeout:completion:"
- "currentLocationWithFetchRequest:completion:"
- "currentResponseMode"
- "deactivateAudioSessionIfNoActiveAssertions"
- "deactivateCurrentAnnouncementRequestForReason:"
- "dealloc"
- "debugDescription"
- "decisionToString:"
- "decodeBoolForKey:"
- "decodeDictionaryWithKeysOfClass:objectsOfClass:forKey:"
- "decodeFloatForKey:"
- "decodeIntegerForKey:"
- "decodeObjectOfClass:forKey:"
- "decodeObjectOfClasses:forKey:"
- "deferAudioSessionDeactivationForAnnouncementRequest"
- "delegate"
- "delegateQueue"
- "delegateWrapper"
- "description"
- "didCompleteRecognitionWithError:secureOfflineOnlyRecognition:sessionUUID:statistics:"
- "didRecognizeFinalResultCandidatePackage:sessionUUID:"
- "didRecognizePackage:nluResult:sessionUUID:"
- "didRecognizePackage:sessionUUID:"
- "didRecognizePartialPackage:nluResult:sessionUUID:"
- "didRecognizeTokens:nluResult:sessionUUID:"
- "didRecognizeTokens:sessionUUID:"
- "didRecognizeVoiceCommandCandidatePackage:nluResult:sessionUUID:"
- "dismissAssistant"
- "dismissAssistantWithReason:"
- "dismissLocationServiceDialogIfNeeded"
- "drainLocationServiceRequestsForNewRequestAndClearLocationCache:dismissDialog:"
- "encodeBool:forKey:"
- "encodeFloat:forKey:"
- "encodeInteger:forKey:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "endpointInfo"
- "extendRequestTimeoutBy:forRequestID:"
- "f"
- "f16@0:8"
- "fetchContextsForKeys:forRequestID:includesNearbyDevices:completion:"
- "fetchContextsForKeys:includesNearbyDevices:completion:"
- "fetchDeviceAndUserIdsForSharedUserId:withCallback:"
- "floatForKey:"
- "formatString"
- "handleCommand:completion:"
- "handleCommand:withExecutionContextMatchingInfo:completion:"
- "handleSpeechRecognized:completion:"
- "handleSpeechServerEndpointIdentified:completion:"
- "hash"
- "headGestureConfiguration"
- "inAppResponse"
- "init"
- "initWithArray:"
- "initWithBridgedMatch:"
- "initWithBuilder:"
- "initWithCoder:"
- "initWithDelegate:"
- "initWithDelegate:delegateQueue:"
- "initWithMachServiceName:"
- "initWithMachServiceName:options:"
- "initWithSuiteName:"
- "instanceInfo"
- "intelligenceFlowActionSummary"
- "intelligenceFlowProgressUpdate"
- "intelligenceFlowStatusNotification"
- "interfaceWithProtocol:"
- "invalidate"
- "isBobbleAvailable"
- "isDeviceInCarDND"
- "isDeviceInStarkMode"
- "isDeviceLockedWithPasscode"
- "isDeviceWatchAuthenticatedWithCompletion:"
- "isEqual:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "isSystemAssistantExperienceEnabled"
- "isTimeoutSuspended"
- "listener"
- "listener:shouldAcceptNewConnection:"
- "logUUFRReadyEvent:"
- "machServiceName"
- "match"
- "matchesIn:"
- "meCard:"
- "messagePublisher"
- "mitigationResultToString:"
- "nlRouterSummary"
- "notifyClientWithBlock:"
- "notifySpeechDetectedIsUndirected"
- "notifyTypingStartedWith:"
- "numberWithBool:"
- "numberWithUnsignedInteger:"
- "objectForKey:"
- "openSensitiveURL:"
- "originalString"
- "parameterMatches"
- "parameterSummaries"
- "peerInfoForCurrentCommand"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "preheat"
- "prepareForAudioHandoffFailedWithCompletion:"
- "prepareForAudioHandoffWithCompletion:"
- "processIdentifier"
- "progress"
- "progressDescription"
- "progressType"
- "promptRequestId"
- "queue"
- "range"
- "registerInternalGestureTestingHandler:"
- "release"
- "remoteObjectProxy"
- "requestClosed:forRequestID:"
- "requestId"
- "respondsToSelector:"
- "resume"
- "resumeConnectionWithBridgeProxy:"
- "retain"
- "retainCount"
- "rewrittenUtterance"
- "rootRequestId"
- "selectResultWithResultCandidate:completion:"
- "self"
- "serviceDelegate"
- "serviceHelper"
- "setAdditionalProgressDescription:"
- "setBundleIdentifier:"
- "setClasses:forSelector:argumentIndex:ofReply:"
- "setDecision:"
- "setDelegate:"
- "setErrorDescription:"
- "setExportedInterface:"
- "setExportedObject:"
- "setFormatString:"
- "setInAppResponse:"
- "setIntelligenceFlowActionSummary:"
- "setIntelligenceFlowProgressUpdate:"
- "setIntelligenceFlowStatusNotification:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setIsInvocationUser:"
- "setIsSameUser:"
- "setMessages:"
- "setMitigationResult:"
- "setNlRouterSummary:"
- "setOutcome:"
- "setParameterSummaries:"
- "setProgress:"
- "setProgressDescription:"
- "setProgressType:"
- "setRemoteObjectInterface:"
- "setRetrievedPayload:"
- "setRewrittenUtterance:"
- "setSessionId:"
- "setStatusString:"
- "setTaskId:"
- "setTypingSessionId:"
- "setUserTurnID:"
- "setValue:"
- "setValueType:"
- "setWithObjects:"
- "siriDismissed"
- "siriPrompted"
- "siriWillPrompt"
- "speechInfo"
- "startAttending"
- "startAttendingWithReason:deviceId:"
- "startRequestWith:"
- "statusString"
- "stopAttendingForReason:"
- "stopAttendingWithReason:"
- "stringWithFormat:"
- "submitExternalActivationRequest:completion:"
- "superclass"
- "supportsSecureCoding"
- "taskId"
- "topicChangedForRequestID:"
- "typingSessionId"
- "uiBridgeConnectionListener"
- "uiBridgeListener"
- "uiBridgeService"
- "uiBridgeServiceDetectedSiriDirectedSpeech"
- "uiBridgeServiceDetectedSpeechStart"
- "uiBridgeServiceDetectedSpeechStart:"
- "uiBridgeServiceDidDetectLanguageMismatch:"
- "uiBridgeServiceDidDetectUserSpeechWithContext:"
- "uiBridgeServiceDidEndSystemTurnInterruptionWithContext:"
- "uiBridgeServiceDidEndUserTurnWithContext:"
- "uiBridgeServiceDidFinalizeUserTurnWithContext:"
- "uiBridgeServiceDidReceiveTasks:"
- "uiBridgeServiceDidStart"
- "uiBridgeServiceDidStartAttending"
- "uiBridgeServiceDidStartAttendingWithRootRequestId:"
- "uiBridgeServiceDidStartSystemTurnInterruptionWithContext:"
- "uiBridgeServiceDidStopAttendingUnexpectedlyWithReason:"
- "uiBridgeServiceReceivedNLRoutingDecision:"
- "uiBridgeServiceReceivedRequestProgress:"
- "uiBridgeServiceReceivedSessionRetrieved:"
- "uiBridgeServiceReceivedShowAssetsDownloadPrompt"
- "uiBridgeServiceReceivedSiriResponse:"
- "uiBridgeServiceReceivedSpeechMitigationResult:"
- "uiBridgeServiceTaskDidCancel:"
- "uiBridgeServiceTaskDidEnd:"
- "uiBridgeServiceWillStartAttending"
- "uiSessionProcessor"
- "unsignedIntegerValue"
- "v16@0:8"
- "v16@?0@8"
- "v20@0:8B16"
- "v20@0:8f16"
- "v24@0:8@\"<AFIntelligenceFlowActionDescriptor>\"16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@\"NSString\"16"
- "v24@0:8@\"NSUUID\"16"
- "v24@0:8@\"SUIBSessionRetrieved\"16"
- "v24@0:8@\"SUIBSystemTurnInterruptionEndedContext\"16"
- "v24@0:8@\"SUIBSystemTurnInterruptionStartedContext\"16"
- "v24@0:8@\"SUIBUserSpeechPresence\"16"
- "v24@0:8@\"SUIBUserTurnEndedContext\"16"
- "v24@0:8@\"SUIBUserTurnFinalizedContext\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?>16"
- "v24@0:8@?<v@?@\"SAPerson\">16"
- "v24@0:8@?<v@?B>16"
- "v24@0:8@?<v@?Qq>16"
- "v24@0:8@?<v@?qB@?<v@?B@\"NSString\">>16"
- "v24@0:8B16B20"
- "v24@0:8Q16"
- "v24@0:8q16"
- "v28@0:8B16@\"NSString\"20"
- "v28@0:8B16@20"
- "v32@0:8@\"AFLocationFetchRequest\"16@?<v@?@\"CLLocation\"@\"NSError\">24"
- "v32@0:8@\"AFRequestInfo\"16@?<v@?B@\"NSError\">24"
- "v32@0:8@\"AFSpeechPackage\"16@\"NSString\"24"
- "v32@0:8@\"NSArray\"16@\"NSString\"24"
- "v32@0:8@\"NSString\"16@?<v@?@\"<AFAnalyticsDeviceAndUserIds>\">24"
- "v32@0:8@\"SABaseCommand\"16@?<v@?@\"SABaseCommand\"@\"NSError\">24"
- "v32@0:8@\"SASResultCandidate\"16@?<v@?@\"SABaseCommand\"@\"NSError\">24"
- "v32@0:8@\"SASSpeechRecognized\"16@?<v@?@\"SABaseCommand\"@\"NSError\">24"
- "v32@0:8@\"SASSpeechServerEndpointIdentified\"16@?<v@?@\"SABaseCommand\"@\"NSError\">24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v32@0:8Q16@24"
- "v32@0:8d16@\"NSString\"24"
- "v32@0:8d16@24"
- "v36@0:8@\"NSSet\"16B24@?<v@?@\"NSArray\">28"
- "v36@0:8@16B24@?28"
- "v40@0:8@\"AFSpeechPackage\"16@\"AFDictationNLUResult\"24@\"NSString\"32"
- "v40@0:8@\"NSArray\"16@\"AFDictationNLUResult\"24@\"NSString\"32"
- "v40@0:8@\"SABaseCommand\"16@\"AFCommandExecutionInfo\"24@?<v@?@\"SABaseCommand\"@\"NSError\">32"
- "v40@0:8@16@24@32"
- "v40@0:8@16@24@?32"
- "v40@0:8d16d24@?32"
- "v40@0:8d16d24@?<v@?@\"CLLocation\"@\"NSError\">32"
- "v44@0:8@\"NSError\"16B24@\"NSString\"28@\"NSDictionary\"36"
- "v44@0:8@\"NSSet\"16@\"NSString\"24B32@?<v@?@\"NSArray\">36"
- "v44@0:8@16@24B32@?36"
- "v44@0:8@16B24@28@36"
- "v8@?0"
- "value"
- "valueForEntitlement:"
- "valueType"
- "zone"
- "{_NSRange=QQ}16@0:8"

```
