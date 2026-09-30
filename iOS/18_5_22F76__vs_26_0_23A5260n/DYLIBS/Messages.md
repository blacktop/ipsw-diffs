## Messages

> `/System/Library/Frameworks/Messages.framework/Messages`

```diff

-1402.600.41.2.8
-  __TEXT.__text: 0x2af28
+1436.100.6.2.12
+  __TEXT.__text: 0x2dc54
   __TEXT.__auth_stubs: 0xd00
-  __TEXT.__objc_methlist: 0x46c0
-  __TEXT.__const: 0x754
-  __TEXT.__gcc_except_tab: 0x1fc
-  __TEXT.__cstring: 0x1cc7
-  __TEXT.__oslogstring: 0xca4
-  __TEXT.__dlopen_cstrs: 0x17e
+  __TEXT.__objc_methlist: 0x4bc0
+  __TEXT.__const: 0x774
+  __TEXT.__gcc_except_tab: 0x28c
+  __TEXT.__cstring: 0x1d87
+  __TEXT.__oslogstring: 0xe8c
+  __TEXT.__dlopen_cstrs: 0x1ca
   __TEXT.__swift5_typeref: 0x10c
   __TEXT.__swift5_reflstr: 0x95
   __TEXT.__swift5_assocty: 0x30

   __TEXT.__swift5_types: 0x18
   __TEXT.__swift_as_entry: 0xc
   __TEXT.__swift_as_ret: 0xc
-  __TEXT.__unwind_info: 0xd38
-  __TEXT.__eh_frame: 0x230
-  __TEXT.__objc_classname: 0x701
-  __TEXT.__objc_methname: 0xa7c7
-  __TEXT.__objc_methtype: 0x2b20
-  __TEXT.__objc_stubs: 0x6c40
-  __DATA_CONST.__got: 0x598
-  __DATA_CONST.__const: 0x700
-  __DATA_CONST.__objc_classlist: 0x128
+  __TEXT.__unwind_info: 0xe18
+  __TEXT.__eh_frame: 0x1f8
+  __TEXT.__objc_classname: 0x74e
+  __TEXT.__objc_methname: 0xaf84
+  __TEXT.__objc_methtype: 0x2c1f
+  __TEXT.__objc_stubs: 0x7000
+  __DATA_CONST.__got: 0x5a8
+  __DATA_CONST.__const: 0x728
+  __DATA_CONST.__objc_classlist: 0x138
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0xd8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2538
+  __DATA_CONST.__objc_selrefs: 0x26a0
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0xf8
+  __DATA_CONST.__objc_superrefs: 0x108
   __DATA_CONST.__objc_arraydata: 0x30
   __AUTH_CONST.__auth_got: 0x690
   __AUTH_CONST.__const: 0x648
-  __AUTH_CONST.__cfstring: 0x1760
-  __AUTH_CONST.__objc_const: 0x57a0
+  __AUTH_CONST.__cfstring: 0x1720
+  __AUTH_CONST.__objc_const: 0x5c98
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_doubleobj: 0x40
-  __AUTH.__objc_data: 0x9e8
+  __AUTH.__objc_data: 0xa88
   __AUTH.__data: 0xc0
-  __DATA.__objc_ivar: 0x38c
-  __DATA.__data: 0xac8
-  __DATA.__bss: 0x6f0
+  __DATA.__objc_ivar: 0x3c8
+  __DATA.__data: 0xa98
+  __DATA.__bss: 0x700
   __DATA_DIRTY.__objc_data: 0x230
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
-  - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib
+  - /usr/lib/swift/libswiftMLCompute.dylib
   - /usr/lib/swift/libswiftMetal.dylib
+  - /usr/lib/swift/libswiftNaturalLanguage.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_errno.dylib
-  - /usr/lib/swift/libswift_math.dylib
-  - /usr/lib/swift/libswift_signal.dylib
-  - /usr/lib/swift/libswift_stdio.dylib
-  - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  - /usr/lib/swift/libswiftsys_time.dylib
-  - /usr/lib/swift/libswiftunistd.dylib
-  UUID: B40E2E53-5FFD-322E-946B-1CAD41161EB1
-  Functions: 1518
-  Symbols:   4892
-  CStrings:  2467
+  UUID: C64ECBF2-DE90-3FB6-8A70-6FA72B526BC2
+  Functions: 1626
+  Symbols:   5164
+  CStrings:  2554
 
Symbols:
+ +[MSMessagesAppViewController(ForReplies) replySuggestionWithCompletion:]
+ +[_MSMessageCustomAcknowledgement supportsSecureCoding]
+ -[MSConversation _requestConversationAvatarsWithSize:completionHandler:]
+ -[MSConversation isUltraConstrainedNetwork]
+ -[MSConversation sendCustomAcknowledgement:completionHandler:]
+ -[MSMessage _payloadDataFromAppIconData:appName:adamID:allowDataPayloads:].cold.1
+ -[MSMessage _payloadDataFromAppIconData:appName:adamID:allowDataPayloads:].cold.2
+ -[MSMessage _payloadDataFromAppIconData:appName:adamID:allowDataPayloads:].cold.3
+ -[MSMessage _payloadDataFromAppIconData:appName:adamID:allowDataPayloads:].cold.4
+ -[MSMessage _payloadDataFromAppIconData:appName:adamID:allowDataPayloads:].cold.5
+ -[MSMessage customAcknowledgements]
+ -[MSMessage setCustomAcknowledgements:]
+ -[MSMessageLiveLayout liveEditableInEntryView]
+ -[MSMessageLiveLayout setLiveEditableInEntryView:]
+ -[MSMessagesAppViewController _shouldUseBackwardsCompatibilityOffsets]
+ -[MSMessagesAppViewController _shouldUseBackwardsCompatibilityOffsets].cold.1
+ -[MSMessagesAppViewController _transcriptSpecificSafeAreaInsets]
+ -[MSMessagesAppViewController _updateLayoutMargins]
+ -[MSMessagesAppViewController _updateLayoutMargins].cold.1
+ -[MSMessagesAppViewController _updateLayoutMargins].cold.2
+ -[MSMessagesAppViewController backgroundLuminance]
+ -[MSMessagesAppViewController generateSnapshotWithContentSize:completion:].cold.2
+ -[MSMessagesAppViewController generateSnapshotWithContentSize:completion:].cold.3
+ -[MSMessagesAppViewController generateSnapshotWithContentSize:completion:].cold.4
+ -[MSMessagesAppViewController generateSnapshotWithContentSize:completion:].cold.5
+ -[MSMessagesAppViewController generateSnapshotWithContentSize:completion:].cold.6
+ -[MSMessagesAppViewController generateSnapshotWithContentSize:completion:].cold.7
+ -[MSMessagesAppViewController invalidateMessageTintColor]
+ -[MSMessagesAppViewController messageTintColor]
+ -[MSMessagesAppViewController performSendAnimationOnAppear]
+ -[MSMessagesAppViewController setBackgroundLuminance:]
+ -[MSMessagesAppViewController setPerformSendAnimationOnAppear:]
+ -[MSMessagesAppViewController(ForPollsOnly) _setSendingEnabled:]
+ -[MSMessagesAppViewController(ForPollsOnly) didChangeBackgroundLuminance:]
+ -[MSMessagesAppViewController(ForPollsOnly) fetchInternalMessageStateForDraft:completion:]
+ -[MSMessagesAppViewController(ForPollsOnly) setShouldPerformSendAnimationOnAppear]
+ -[MSStickerBrowserViewController messageTintColor]
+ -[_MSAvatarImage .cxx_destruct]
+ -[_MSAvatarImage avatarImage]
+ -[_MSAvatarImage initWithParticipantHandle:avatarImage:]
+ -[_MSAvatarImage initWithParticipantIdentifier:avatarImage:]
+ -[_MSAvatarImage participantHandle]
+ -[_MSAvatarImage participantIdentifier]
+ -[_MSAvatarImage setAvatarImage:]
+ -[_MSAvatarImage setParticipantHandle:]
+ -[_MSAvatarImage setParticipantIdentifier:]
+ -[_MSConversationState isUltraConstrainedNetwork]
+ -[_MSConversationState setIsUltraConstrainedNetwork:]
+ -[_MSMessageAppBundleContext _remoteViewDidInvalidateMessageTintColorWithUpdatedColor:]
+ -[_MSMessageAppBundleContext _requestMessageTintColor:]
+ -[_MSMessageAppBundleContext _setSendingEnabled:]
+ -[_MSMessageAppBundleContext didChangeBackgroundLuminance:]
+ -[_MSMessageAppBundleContext fetchInternalMessageStateForDraft:completion:]
+ -[_MSMessageAppBundleContext requestConversationAvatarsWithSize:completionHandler:]
+ -[_MSMessageAppBundleContext sendCustomAcknowledgement:selectedMessage:completionHandler:]
+ -[_MSMessageAppBundleContext setShouldPerformSendAnimationOnAppear]
+ -[_MSMessageAppBundleHostContext _remoteViewDidInvalidateMessageTintColorWithUpdatedColor:]
+ -[_MSMessageAppBundleHostContext _requestConversationAvatarsWithSize:completionHandler:]
+ -[_MSMessageAppBundleHostContext _sendCustomAcknowledgement:selectedMessage:completionHandler:]
+ -[_MSMessageAppBundleHostContext _setSendingEnabled:]
+ -[_MSMessageAppContext _remoteViewDidInvalidateMessageTintColorWithUpdatedColor:]
+ -[_MSMessageAppContext _requestMessageTintColor:]
+ -[_MSMessageAppContext _requestMessageTintColor:].cold.1
+ -[_MSMessageAppContext _setSendingEnabled:]
+ -[_MSMessageAppContext didChangeBackgroundLuminance:]
+ -[_MSMessageAppContext fetchInternalMessageStateForDraft:completion:]
+ -[_MSMessageAppContext requestConversationAvatarsWithSize:completionHandler:]
+ -[_MSMessageAppContext sendCustomAcknowledgement:selectedMessage:completionHandler:]
+ -[_MSMessageAppContext setShouldPerformSendAnimationOnAppear]
+ -[_MSMessageAppExtensionContext _remoteViewDidInvalidateMessageTintColorWithUpdatedColor:]
+ -[_MSMessageAppExtensionContext _requestMessageTintColor:]
+ -[_MSMessageAppExtensionContext _setSendingEnabled:]
+ -[_MSMessageAppExtensionContext didChangeBackgroundLuminance:]
+ -[_MSMessageAppExtensionContext fetchInternalMessageStateForDraft:completion:]
+ -[_MSMessageAppExtensionContext requestConversationAvatarsWithSize:completionHandler:]
+ -[_MSMessageAppExtensionContext sendCustomAcknowledgement:selectedMessage:completionHandler:]
+ -[_MSMessageAppExtensionContext setShouldPerformSendAnimationOnAppear]
+ -[_MSMessageAppExtensionHostContext _remoteViewDidInvalidateMessageTintColorWithUpdatedColor:]
+ -[_MSMessageAppExtensionHostContext _requestConversationAvatarsWithSize:completionHandler:]
+ -[_MSMessageAppExtensionHostContext _sendCustomAcknowledgement:selectedMessage:completionHandler:]
+ -[_MSMessageAppExtensionHostContext _setSendingEnabled:]
+ -[_MSMessageCustomAcknowledgement .cxx_destruct]
+ -[_MSMessageCustomAcknowledgement URL]
+ -[_MSMessageCustomAcknowledgement _payloadDataFromAppName:adamID:]
+ -[_MSMessageCustomAcknowledgement _pluginPayloadWithSelectedMessage:appName:adamID:]
+ -[_MSMessageCustomAcknowledgement _pluginPayloadWithSelectedMessage:appName:adamID:].cold.1
+ -[_MSMessageCustomAcknowledgement _pluginPayloadWithSelectedMessage:appName:adamID:].cold.2
+ -[_MSMessageCustomAcknowledgement _sanitize]
+ -[_MSMessageCustomAcknowledgement _sanitizedCopy]
+ -[_MSMessageCustomAcknowledgement _shallowCopy]
+ -[_MSMessageCustomAcknowledgement copyWithZone:]
+ -[_MSMessageCustomAcknowledgement encodeWithCoder:]
+ -[_MSMessageCustomAcknowledgement initWithCoder:]
+ -[_MSMessageCustomAcknowledgement initWithSession:isFromMe:time:]
+ -[_MSMessageCustomAcknowledgement isFromMe]
+ -[_MSMessageCustomAcknowledgement senderAddress]
+ -[_MSMessageCustomAcknowledgement senderParticipantIdentifier]
+ -[_MSMessageCustomAcknowledgement session]
+ -[_MSMessageCustomAcknowledgement setIsFromMe:]
+ -[_MSMessageCustomAcknowledgement setSenderAddress:]
+ -[_MSMessageCustomAcknowledgement setSenderParticipantIdentifier:]
+ -[_MSMessageCustomAcknowledgement setURL:]
+ -[_MSMessageCustomAcknowledgement time]
+ GCC_except_table119
+ GCC_except_table121
+ GCC_except_table123
+ GCC_except_table27
+ GCC_except_table28
+ GCC_except_table4
+ GCC_except_table54
+ _CFRunLoopObserverCreateWithHandler
+ _CGContextFillRect
+ _NSStringFromUIEdgeInsets
+ _OBJC_CLASS_$__MSAvatarImage
+ _OBJC_CLASS_$__MSMessageCustomAcknowledgement
+ _OBJC_IVAR_$_MSConversation._isUltraConstrainedNetwork
+ _OBJC_IVAR_$_MSMessage._customAcknowledgements
+ _OBJC_IVAR_$_MSMessageLiveLayout._liveEditableInEntryView
+ _OBJC_IVAR_$_MSMessagesAppViewController._backgroundLuminance
+ _OBJC_IVAR_$_MSMessagesAppViewController._performSendAnimationOnAppear
+ _OBJC_IVAR_$__MSAvatarImage._avatarImage
+ _OBJC_IVAR_$__MSAvatarImage._participantHandle
+ _OBJC_IVAR_$__MSAvatarImage._participantIdentifier
+ _OBJC_IVAR_$__MSConversationState._isUltraConstrainedNetwork
+ _OBJC_IVAR_$__MSMessageCustomAcknowledgement._URL
+ _OBJC_IVAR_$__MSMessageCustomAcknowledgement._isFromMe
+ _OBJC_IVAR_$__MSMessageCustomAcknowledgement._senderAddress
+ _OBJC_IVAR_$__MSMessageCustomAcknowledgement._senderParticipantIdentifier
+ _OBJC_IVAR_$__MSMessageCustomAcknowledgement._session
+ _OBJC_IVAR_$__MSMessageCustomAcknowledgement._time
+ _OBJC_METACLASS_$__MSAvatarImage
+ _OBJC_METACLASS_$__MSMessageCustomAcknowledgement
+ _UIEdgeInsetsZero
+ __OBJC_$_CLASS_METHODS_MSMessagesAppViewController(CompactOrExpandedPresentation|ForPollsOnly|ForCameraOnly|ForStickersOnly|ForGPOnly|ForReplies)
+ __OBJC_$_CLASS_METHODS__MSMessageCustomAcknowledgement
+ __OBJC_$_CLASS_PROP_LIST__MSMessageCustomAcknowledgement
+ __OBJC_$_INSTANCE_METHODS_MSMessagesAppViewController(CompactOrExpandedPresentation|ForPollsOnly|ForCameraOnly|ForStickersOnly|ForGPOnly|ForReplies)
+ __OBJC_$_INSTANCE_METHODS__MSAvatarImage
+ __OBJC_$_INSTANCE_METHODS__MSMessageCustomAcknowledgement
+ __OBJC_$_INSTANCE_VARIABLES__MSAvatarImage
+ __OBJC_$_INSTANCE_VARIABLES__MSMessageCustomAcknowledgement
+ __OBJC_$_PROP_LIST_MSMessagesAppTranscriptPresentation
+ __OBJC_$_PROP_LIST__MSAvatarImage
+ __OBJC_$_PROP_LIST__MSMessageCustomAcknowledgement
+ __OBJC_CLASS_PROTOCOLS_$__MSMessageCustomAcknowledgement
+ __OBJC_CLASS_RO_$__MSAvatarImage
+ __OBJC_CLASS_RO_$__MSMessageCustomAcknowledgement
+ __OBJC_METACLASS_RO_$__MSAvatarImage
+ __OBJC_METACLASS_RO_$__MSMessageCustomAcknowledgement
+ ___49-[_MSMessageAppContext _requestMessageTintColor:]_block_invoke
+ ___60-[_MSMessageAppContext _requestSnapshotThatFits:completion:]_block_invoke.102
+ ___64-[_MSMessageAppExtensionContext _installPrincipalObjectObserver]_block_invoke
+ ___69-[_MSMessageAppContext _prepareForPresentationWithCompletionHandler:]_block_invoke.110
+ ___81-[_MSMessageAppContext _didSelectGPAsset:sandboxExtension:recipeData:completion:]_block_invoke.99
+ ___84-[_MSMessageAppContext _canSendMessage:conversationState:associatedText:completion:]_block_invoke.83
+ ___block_descriptor_40_e8_32w_e33_v24?0^{__CFRunLoopObserver=}8Q16lw32l8
+ ___block_literal_global.143
+ __swift_FORCE_LOAD_$_swiftMLCompute
+ __swift_FORCE_LOAD_$_swiftMLCompute_$_Messages
+ __swift_FORCE_LOAD_$_swiftNaturalLanguage
+ __swift_FORCE_LOAD_$_swiftNaturalLanguage_$_Messages
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_Messages
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_Messages
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_Messages
+ _block_copy_helper.38
+ _block_copy_helper.44
+ _block_descriptor.40
+ _block_descriptor.46
+ _block_destroy_helper.39
+ _block_destroy_helper.45
+ _objc_copyWeak
+ _objc_initWeak
+ _objc_msgSend$_balloonMaskEdgeInsets
+ _objc_msgSend$_payloadDataFromAppName:adamID:
+ _objc_msgSend$_remoteViewDidInvalidateMessageTintColorWithUpdatedColor:
+ _objc_msgSend$_requestConversationAvatarsWithSize:completionHandler:
+ _objc_msgSend$_requestMessageTintColor:
+ _objc_msgSend$_sendCustomAcknowledgement:selectedMessage:completionHandler:
+ _objc_msgSend$_setSendingEnabled:
+ _objc_msgSend$_shouldUseBackwardsCompatibilityOffsets
+ _objc_msgSend$_transcriptSpecificSafeAreaInsets
+ _objc_msgSend$_updateLayoutMargins
+ _objc_msgSend$balloonCornerRadius
+ _objc_msgSend$customAcknowledgements
+ _objc_msgSend$decodeArrayOfObjectsOfClasses:forKey:
+ _objc_msgSend$didChangeBackgroundLuminance:
+ _objc_msgSend$fetchInternalMessageStateForDraft:completion:
+ _objc_msgSend$initWithSession:isFromMe:time:
+ _objc_msgSend$isUltraConstrainedNetwork
+ _objc_msgSend$layoutMargins
+ _objc_msgSend$liveEditableInEntryView
+ _objc_msgSend$messageTintColor
+ _objc_msgSend$pluginBackwardsCompatibilityBottomOffset
+ _objc_msgSend$pluginBackwardsCompatibilityLeadingTrailingOffset
+ _objc_msgSend$requestConversationAvatarsWithSize:completionHandler:
+ _objc_msgSend$sendCustomAcknowledgement:selectedMessage:completionHandler:
+ _objc_msgSend$set
+ _objc_msgSend$setAssociatedMessageGUID:
+ _objc_msgSend$setCustomAcknowledgement:
+ _objc_msgSend$setCustomAcknowledgements:
+ _objc_msgSend$setLayoutMargins:
+ _objc_msgSend$setLiveEditableInEntryView:
+ _objc_msgSend$setPerformSendAnimationOnAppear:
+ _objc_msgSend$setShouldPerformSendAnimationOnAppear
+ _objectdestroy.36Tm
+ _objectdestroy.48Tm
- GCC_except_table105
- GCC_except_table43
- GCC_except_table52
- _CFRunLoopObserverCreate
- _CGColorGetAlpha
- __IMWarn
- __OBJC_$_INSTANCE_METHODS_MSMessagesAppViewController(CompactOrExpandedPresentation|ForCameraOnly|ForStickersOnly|ForGPOnly)
- ___60-[_MSMessageAppContext _requestSnapshotThatFits:completion:]_block_invoke.96
- ___69-[_MSMessageAppContext _prepareForPresentationWithCompletionHandler:]_block_invoke.104
- ___81-[_MSMessageAppContext _didSelectGPAsset:sandboxExtension:recipeData:completion:]_block_invoke.93
- ___84-[_MSMessageAppContext _canSendMessage:conversationState:associatedText:completion:]_block_invoke.77
- ___block_literal_global.132
- __swift_FORCE_LOAD_$_swiftDataDetection
- __swift_FORCE_LOAD_$_swiftDataDetection_$_Messages
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_errno_$_Messages
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_math_$_Messages
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_signal_$_Messages
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_stdio_$_Messages
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swift_time_$_Messages
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftsys_time_$_Messages
- __swift_FORCE_LOAD_$_swiftunistd
- __swift_FORCE_LOAD_$_swiftunistd_$_Messages
- _block_copy_helper.46
- _block_copy_helper.55
- _block_descriptor.48
- _block_descriptor.57
- _block_destroy_helper.47
- _block_destroy_helper.56
- _handleRunloopEnded
- _objc_msgSend$backgroundColor
- _objc_msgSend$secondarySystemBackgroundColor
- _objectdestroy.38Tm
- _objectdestroy.44Tm
- _swift_unknownObjectRelease
- _swift_unknownObjectRetain
CStrings:
+ "%s Took new snapshot image with size %@. snapshotImage: %@"
+ "%s using transcript margins: %@"
+ "%s using zero layout margins: %@"
+ "-[MSMessagesAppViewController _updateLayoutMargins]"
+ "-[_MSMessageAppContext _requestMessageTintColor:]"
+ "-[_MSMessageCustomAcknowledgement _pluginPayloadWithSelectedMessage:appName:adamID:]"
+ "/Library/Caches/com.apple.xbs/Sources/Messages/ChatKit/Messages/Messages/Source/Extension/_MSMessageCustomAcknowledgement.m"
+ "@\"UIColor\"16@0:8"
+ "@36@0:8@16B24@28"
+ "ForPollsOnly"
+ "ForReplies"
+ "T@\"NSArray\",&,N,V_customAcknowledgements"
+ "T@\"NSDate\",R,N,V_time"
+ "T@\"NSString\",C,N,V_participantHandle"
+ "T@\"NSString\",C,N,V_participantIdentifier"
+ "T@\"NSURL\",&,N,V_URL"
+ "T@\"UIColor\",R,N"
+ "T@\"UIImage\",&,N,V_avatarImage"
+ "TB,N,V_isUltraConstrainedNetwork"
+ "TB,N,V_liveEditableInEntryView"
+ "TB,N,V_performSendAnimationOnAppear"
+ "TB,R,N,V_isUltraConstrainedNetwork"
+ "Td,N,V_backgroundLuminance"
+ "_MSAvatarImage"
+ "_MSMessageCustomAcknowledgement"
+ "_avatarImage"
+ "_backgroundLuminance"
+ "_customAcknowledgements"
+ "_isUltraConstrainedNetwork"
+ "_liveEditableInEntryView"
+ "_participantHandle"
+ "_participantIdentifier"
+ "_payloadDataFromAppName:adamID:"
+ "_performSendAnimationOnAppear"
+ "_pluginPayloadWithSelectedMessage:appName:adamID:"
+ "_remoteViewDidInvalidateMessageTintColorWithUpdatedColor:"
+ "_requestConversationAvatarsWithSize:completionHandler:"
+ "_requestMessageTintColor:"
+ "_sendCustomAcknowledgement:selectedMessage:completionHandler:"
+ "_setSendingEnabled:"
+ "_shouldUseBackwardsCompatibilityOffsets"
+ "_transcriptSpecificSafeAreaInsets"
+ "_updateLayoutMargins"
+ "avatarImage"
+ "backgroundLuminance"
+ "balloonCornerRadius"
+ "conversationID: %@, senderIdentifier: %@, recipientIdentifiers: %@, activeMessage: %@, conversationIdentifier: %@, iMessageLoginID: %@, senderAddress: %@, recipientAddresses: %@, isiMessage: %@, isBusiness: %@, isUltraConstrainedNetwork"
+ "customAcknowledgements"
+ "decodeArrayOfObjectsOfClasses:forKey:"
+ "didChangeBackgroundLuminance:"
+ "fetchInternalMessageStateForDraft:completion:"
+ "iMessage app messages have a new shape. To make your app look great, rebuild your app with the latest SDK and consider using safeAreaInsets and layoutMargins."
+ "initWithParticipantHandle:avatarImage:"
+ "initWithParticipantIdentifier:avatarImage:"
+ "initWithSession:isFromMe:time:"
+ "invalidateMessageTintColor"
+ "isUltraConstrainedNetwork"
+ "layoutMargins"
+ "liveEditableInEntryView"
+ "messageTintColor"
+ "participantHandle"
+ "participantIdentifier"
+ "performSendAnimationOnAppear"
+ "pluginBackwardsCompatibilityBottomOffset"
+ "pluginBackwardsCompatibilityLeadingTrailingOffset"
+ "replySuggestionWithCompletion:"
+ "requestConversationAvatarsWithSize:completionHandler:"
+ "sendCustomAcknowledgement:completionHandler:"
+ "sendCustomAcknowledgement:selectedMessage:completionHandler:"
+ "set"
+ "setAssociatedMessageGUID:"
+ "setAvatarImage:"
+ "setBackgroundLuminance:"
+ "setCustomAcknowledgement:"
+ "setCustomAcknowledgements:"
+ "setIsUltraConstrainedNetwork:"
+ "setLayoutMargins:"
+ "setLiveEditableInEntryView:"
+ "setParticipantHandle:"
+ "setParticipantIdentifier:"
+ "setPerformSendAnimationOnAppear:"
+ "setShouldPerformSendAnimationOnAppear"
+ "v24@0:8@\"UIColor\"16"
+ "v24@0:8@?<v@?@\"UIColor\">16"
+ "v24@?0^{__CFRunLoopObserver=}8Q16"
+ "v28@0:8B16@?20"
+ "v28@0:8B16@?<v@?@\"MSMessage\">20"
+ "v40@0:8@\"_MSMessageCustomAcknowledgement\"16@\"MSMessage\"24@?<v@?@\"NSError\">32"
+ "v40@0:8{CGSize=dd}16@?<v@?@\"NSArray\"@\"NSError\">32"
- "%s Took new snapshot with size %@. snapshotImage: %@"
- "backgroundColor"
- "conversationID: %@, senderIdentifier: %@, recipientIdentifiers: %@, activeMessage: %@, conversationIdentifier: %@, iMessageLoginID: %@, senderAddress: %@, recipientAddresses: %@, isiMessage: %@, isBusiness: %@"
- "secondarySystemBackgroundColor"

```
