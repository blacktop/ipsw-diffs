## MessagesFlowDelegatePlugin

> `/System/Library/Assistant/FlowDelegatePlugins/MessagesFlowDelegatePlugin.bundle/MessagesFlowDelegatePlugin`

```diff

-3300.114.2.0.0
-  __TEXT.__text: 0x38ea7c
-  __TEXT.__auth_stubs: 0x6990
+3301.15.2.0.0
+  __TEXT.__text: 0x39a6ac
+  __TEXT.__auth_stubs: 0x6b30
   __TEXT.__objc_methlist: 0x4c
-  __TEXT.__const: 0x11320
-  __TEXT.__cstring: 0x2a8c9
-  __TEXT.__constg_swiftt: 0xc528
-  __TEXT.__swift5_typeref: 0x6dc7
-  __TEXT.__swift5_fieldmd: 0x8a50
-  __TEXT.__swift5_builtin: 0x2bc
-  __TEXT.__swift5_reflstr: 0x7656
-  __TEXT.__swift5_assocty: 0xf88
-  __TEXT.__objc_methname: 0x328a
-  __TEXT.__swift5_capture: 0x1ddc
-  __TEXT.__swift5_proto: 0xe24
-  __TEXT.__swift5_types: 0x6f4
+  __TEXT.__const: 0x11820
+  __TEXT.__cstring: 0x2b2f9
+  __TEXT.__constg_swiftt: 0xc75c
+  __TEXT.__swift5_typeref: 0x6eeb
+  __TEXT.__swift5_fieldmd: 0x8c40
+  __TEXT.__swift5_builtin: 0x2e4
+  __TEXT.__swift5_reflstr: 0x77e6
+  __TEXT.__swift5_assocty: 0x1000
+  __TEXT.__objc_methname: 0x330d
+  __TEXT.__swift5_capture: 0x22e0
+  __TEXT.__swift5_proto: 0xe5c
+  __TEXT.__swift5_types: 0x714
   __TEXT.__objc_classname: 0x126
   __TEXT.__objc_methtype: 0x32c
   __TEXT.__swift5_protos: 0x15c
   __TEXT.__swift5_mpenum: 0x6c
-  __TEXT.__unwind_info: 0xd0fc
-  __TEXT.__eh_frame: 0x1d830
-  __DATA_CONST.__auth_got: 0x34c8
-  __DATA_CONST.__got: 0x13a8
-  __DATA_CONST.__auth_ptr: 0x750
-  __DATA_CONST.__const: 0x12218
-  __DATA_CONST.__objc_classlist: 0x558
+  __TEXT.__unwind_info: 0xda68
+  __TEXT.__eh_frame: 0x1def8
+  __DATA_CONST.__auth_got: 0x3598
+  __DATA_CONST.__got: 0x13d8
+  __DATA_CONST.__auth_ptr: 0x760
+  __DATA_CONST.__const: 0x13310
+  __DATA_CONST.__objc_classlist: 0x570
   __DATA_CONST.__objc_protolist: 0x100
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_const: 0xb970
-  __DATA.__objc_selrefs: 0x1260
+  __DATA.__objc_const: 0xbc28
+  __DATA.__objc_selrefs: 0x1298
   __DATA.__objc_protorefs: 0x80
-  __DATA.__objc_classrefs: 0x600
-  __DATA.__objc_data: 0x1d40
-  __DATA.__data: 0x19978
-  __DATA.__bss: 0x18080
-  __DATA.__common: 0x821
+  __DATA.__objc_classrefs: 0x630
+  __DATA.__objc_data: 0x1de0
+  __DATA.__data: 0x19d48
+  __DATA.__bss: 0x18780
+  __DATA.__common: 0x829
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/Combine.framework/Combine

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 21041
-  Symbols:   457
-  CStrings:  3687
+  Functions: 21488
+  Symbols:   462
+  CStrings:  3734
 
Symbols:
+ _OBJC_CLASS_$_FLOWSchemaFLOWClientEvent
+ _OBJC_CLASS_$_FLOWSchemaFLOWDomainExecutionContext
+ _OBJC_CLASS_$_FLOWSchemaFLOWDomainExecutionEnded
+ _OBJC_CLASS_$_FLOWSchemaFLOWDomainExecutionFailed
+ _OBJC_CLASS_$_FLOWSchemaFLOWDomainExecutionStarted
+ _OBJC_CLASS_$_NSString
- _AFIsInternalInstall
CStrings:
+ "#AutoSendEnablementUtils device not being considered for a disable autosend hint"
+ "#AutoSendEnablementUtils user is eligible for hint on disabling AutoSend=%{bool}d"
+ "#AutoSendEnablementUtils user is not being considered for AutoEnablement"
+ "#AutoSendEnablementUtils user is not eligible because they have used AutoSend in the past, and turned it off"
+ "#AutoSendEnablementUtils user received hint about how to disable AutoSend, disabling the user's eligibility to receive the hint again"
+ "#FollowUpOfferFlowStrategy createSongRREntity created entity for Apple Music link: %{sensitive}s"
+ "#FollowUpOfferFlowStrategy extractAddressEntities Finished building postal address"
+ "#FollowUpOfferFlowStrategy extractAddressEntities extracted address entity: %{sensitive}s"
+ "#FollowupOfferFlowStrategy NSDataDetector failed: %s"
+ "#MessagesSELFPerformanceLogger Failed to create client event"
+ "#MessagesSELFPerformanceLogger Failed to create execution context"
+ "#MessagesSELFPerformanceLogger Failed to create start event for %s"
+ "#MessagesSELFPerformanceLogger Failed to register end event for %s"
+ "#MessagesSELFPerformanceLogger Registered start event for %s"
+ "#MessagesSELFPerformanceLogger successfully sent %s performance event for %s"
+ "#SearchForMessageNLv4IntentConverter appBundle ID for group name %s is: %s"
+ "#SearchForMessagesAppResolutionOnDeviceFlowStrategy app not specified, defaulting to Messages app"
+ "#SearchForMessagesAppResolutionOnDeviceFlowStrategy received non-NL input, returning noAppFound"
+ "#SearchForMessagesAppResolutionOnDeviceFlowStrategy selecting specified app: %s"
+ "#SearchForMessagesAppResolutionOnDeviceFlowStrategy specified app is not installed, returning noAppFound"
+ "#SearchForMessagesAppResolutionOnDeviceFlowStrategy: received an intent with appIdentifier: %s"
+ "#SearchForMessagesUserDialogActTransformer intent groupAppBundleID to: %s"
+ "#SendMessageAppResolutionBeforeNextResolveFlow pushing unlock check flow"
+ "#SendMessageConfirmIntentFlow failed to cancel send on disappear command: %@"
+ "#SendMessageUnlockCheckFlow device is authenticated, don't require unlock"
+ "#SendMessageUnlockCheckFlow don't require unlock"
+ "#SendMessageUnlockCheckFlow execute() called in an unexpected state: %s"
+ "#SendMessageUnlockCheckFlow pushing unlock flow"
+ "#SendMessageUnlockCheckFlow pushing unlock flow completed with %s"
+ "#SendMessageUnlockCheckFlow request is from HomePod, don't require unlock"
+ "#SendMessageUnlockCheckFlow sending to multiple unresolved recipients, require unlock"
+ "#SummarizableComponent This message is not a long message/does not have long content. ttsDuration: %f"
+ "#TextComponent SpokenDialogContext: %s, isLongMessage=%{bool}d, shouldSummarize=%{bool}d"
+ "#TextComponent text summarization feature not enabled"
+ "#makeOfferNLContextUpdate #ReferenceResolution Donating address RREntity to SRR"
+ "#makeOfferNLContextUpdate #ReferenceResolution Donating music RREntity to SRR"
+ "<redacted>"
+ "AutoSendEnablement"
+ "AutoSendEnablementConfirmationDialog"
+ "HowToDisableAutoSendDialog"
+ "MessagesFlowDelegatePlugin/SearchForMessagesAppResolutionOnDeviceFlowStrategy.swift"
+ "MessagesFlowDelegatePlugin/SendMessageUnlockCheckFlow.swift"
+ "SearchForMessagesAppResolutionOnDeviceFlowStrategy.makeConfirmationPrompt() should never be called"
+ "SearchForMessagesAppResolutionOnDeviceFlowStrategy.makeDisambiguationPrompt() should never be called"
+ "SearchForMessagesAppResolutionOnDeviceFlowStrategy.parseConfirmationResponse() should never be called"
+ "SearchForMessagesAppResolutionOnDeviceFlowStrategy.parseDisambiguationResponse() should never be called"
+ "SendAppResolutionFlow# pushing unlock check flow"
+ "SiriKitFlow.Parse.DirectInvocation(identifier: \""
+ "_TtC26MessagesFlowDelegatePlugin17SecurityScopedURL"
+ "_TtC26MessagesFlowDelegatePlugin26SendMessageUnlockCheckFlow"
+ "_TtC26MessagesFlowDelegatePlugin29MessagesSELFPerformanceLogger"
+ "_TtC26MessagesFlowDelegatePlugin50SearchForMessagesAppResolutionOnDeviceFlowStrategy"
+ "domainExecutionType"
+ "ended"
+ "failed"
+ "music.apple.com/"
+ "osLogger"
+ "provideAutoEnablementConfirmation"
+ "setContextId:"
+ "setDomainExecutionType:"
+ "setEnded:"
+ "setFailed:"
+ "setFlowDomainExecutionContext:"
+ "setStartedOrChanged:"
+ "substringWithRange:"
+ "taskType"
+ "text_summarization"
+ "unknown effect type: "
+ "unknown link media type: "
+ "wrappedValue"
- "#DefaultAppResolutionOnDeviceFlowStrategy app not specified, defaulting to Messages app"
- "#DefaultAppResolutionOnDeviceFlowStrategy received non-NL input, returning noAppFound"
- "#DefaultAppResolutionOnDeviceFlowStrategy selecting specified app: %s"
- "#DefaultAppResolutionOnDeviceFlowStrategy specified app is not installed, returning noAppFound"
- "#TextComponent SpokenDialogContext: %s, isLongMessage=%{bool}d, shouldSummarize=%{bool}d, isSingle1On1Conversation=%{bool}d"
- "#TextComponent reading intelligence feature not enabled"
- "DefaultAppResolutionOnDeviceFlowStrategy.makeConfirmationPrompt() should never be called"
- "DefaultAppResolutionOnDeviceFlowStrategy.makeDisambiguationPrompt() should never be called"
- "DefaultAppResolutionOnDeviceFlowStrategy.parseConfirmationResponse() should never be called"
- "DefaultAppResolutionOnDeviceFlowStrategy.parseDisambiguationResponse() should never be called"
- "MessagesFlowDelegatePlugin/DefaultAppResolutionOnDeviceFlowStrategy.swift"
- "MessagesFlowDelegatePlugin/INMessageEffectType+CustomStringConvertible.swift"
- "MessagesFlowDelegatePlugin/INMessageLinkMediaType+CustomStringConvertible.swift"
- "MessagesFlowDelegatePlugin/INMessageType+CountableComponentType.swift"
- "No specified description for INMessageEffectType"
- "No specified description for INMessageLinkMediaType"
- "No specified description for INMessageType"
- "SendAppResolutionFlow# Device is authenticated, don't require unlock"
- "SendAppResolutionFlow# Request is from HomePod, don't require unlock"
- "SendAppResolutionFlow# Sending to multiple unresolved recipients from locked screen requires unlock"
- "SendAppResolutionFlow# Unlock is not required"
- "SendAppResolutionFlow# Unlock is required - pushing unlock flow"
- "_TtC26MessagesFlowDelegatePlugin40DefaultAppResolutionOnDeviceFlowStrategy"

```
