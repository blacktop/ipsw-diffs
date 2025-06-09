## RTTUtilities

> `/System/Library/PrivateFrameworks/RTTUtilities.framework/RTTUtilities`

```diff

-456.8.10.0.0
-  __TEXT.__text: 0x22ad4
-  __TEXT.__auth_stubs: 0x7b0
-  __TEXT.__objc_methlist: 0x1a78
-  __TEXT.__const: 0xe0
-  __TEXT.__gcc_except_tab: 0xd34
-  __TEXT.__cstring: 0x167c
-  __TEXT.__oslogstring: 0x2ae6
-  __TEXT.__dlopen_cstrs: 0x22c
+485.3.0.0.0
+  __TEXT.__text: 0x253cc
+  __TEXT.__auth_stubs: 0x7e0
+  __TEXT.__objc_methlist: 0x1bd0
+  __TEXT.__const: 0xf0
+  __TEXT.__gcc_except_tab: 0xcfc
+  __TEXT.__cstring: 0x17f9
+  __TEXT.__oslogstring: 0x2e23
+  __TEXT.__dlopen_cstrs: 0x279
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x920
+  __TEXT.__unwind_info: 0x988
   __TEXT.__objc_classname: 0x247
-  __TEXT.__objc_methname: 0x52e1
-  __TEXT.__objc_methtype: 0x818
-  __TEXT.__objc_stubs: 0x4b60
-  __DATA_CONST.__got: 0x390
-  __DATA_CONST.__const: 0xd88
+  __TEXT.__objc_methname: 0x58ac
+  __TEXT.__objc_methtype: 0x881
+  __TEXT.__objc_stubs: 0x5040
+  __DATA_CONST.__got: 0x3a0
+  __DATA_CONST.__const: 0xec0
   __DATA_CONST.__objc_classlist: 0x88
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1750
+  __DATA_CONST.__objc_selrefs: 0x18b8
   __DATA_CONST.__objc_superrefs: 0x78
   __DATA_CONST.__objc_arraydata: 0x178
-  __AUTH_CONST.__auth_got: 0x3e8
+  __AUTH_CONST.__auth_got: 0x400
   __AUTH_CONST.__const: 0x4a0
-  __AUTH_CONST.__cfstring: 0x1740
-  __AUTH_CONST.__objc_const: 0x1dc0
+  __AUTH_CONST.__cfstring: 0x18a0
+  __AUTH_CONST.__objc_const: 0x1e88
   __AUTH_CONST.__objc_dictobj: 0x118
   __AUTH_CONST.__objc_intobj: 0x108
   __AUTH_CONST.__objc_arrayobj: 0xa8
-  __DATA.__objc_ivar: 0x130
+  __DATA.__objc_ivar: 0x140
   __DATA.__data: 0x4a8
-  __DATA.__bss: 0x88
+  __DATA.__bss: 0x98
   __DATA_DIRTY.__objc_data: 0x550
   __DATA_DIRTY.__data: 0x18
-  __DATA_DIRTY.__bss: 0xd8
+  __DATA_DIRTY.__bss: 0xe8
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /System/Library/PrivateFrameworks/AXRuntime.framework/AXRuntime
   - /System/Library/PrivateFrameworks/CallHistory.framework/CallHistory
   - /System/Library/PrivateFrameworks/HearingCore.framework/HearingCore
+  - /System/Library/PrivateFrameworks/IDS.framework/IDS
   - /System/Library/PrivateFrameworks/MediaExperience.framework/MediaExperience
   - /System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset
   - /System/Library/PrivateFrameworks/NanoPreferencesSync.framework/NanoPreferencesSync

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 60148647-7DAA-31EE-9F28-1FF830A2B593
-  Functions: 725
-  Symbols:   2813
-  CStrings:  1747
+  UUID: 626664B3-CE71-35A3-844E-25219930AAE0
+  Functions: 766
+  Symbols:   2960
+  CStrings:  1847
 
Symbols:
+ +[RTTTelephonyUtilities performCallCenterTask:callCenter:]
+ +[RTTUtterance utteranceWithContactPath:andText:translatedText:isTranscription:]
+ -[RTTCall _sendTranslationForUtterance:]
+ -[RTTCall formatMessage:withType:isMe:]
+ -[RTTCall saveTranslatedTranscribedTextForConversation:translatedText:isNew:]
+ -[RTTCall sendToTTYDeviceWithString:]
+ -[RTTCall setTranslationLocales:]
+ -[RTTCall setTranslationLocalesWithLocal:remote:]
+ -[RTTCall setTranslator:]
+ -[RTTCall translationLocales]
+ -[RTTCall translator]
+ -[RTTController _updateConversationControllerWithTranslatedTranscription:translation:type:callUUID:]
+ -[RTTController displayRTTDowngradeAlert]
+ -[RTTController handleRTTMessageInjection:]
+ -[RTTController handleRTTTranslationLocaleMessage:]
+ -[RTTController ttyCall:didUpdateTranslation:forUtterance:]
+ -[RTTConversation addTranslatedTranscriptionFromOtherContactPath:original:]
+ -[RTTConversation lastUtteranceForMe:withText:]
+ -[RTTConversation updateTranslatedTranscriptionFromOtherContactPath:original:]
+ -[RTTRemoteCall discoveryClient]
+ -[RTTRemoteCall messagingClients]
+ -[RTTRemoteCall newRapportClientWithDestinationDevice:]
+ -[RTTRemoteCall rapportClientForDevice:]
+ -[RTTRemoteCall resetRapportClientForDevice:invalidate:]
+ -[RTTRemoteCall setDiscoveryClient:]
+ -[RTTRemoteCall setMessagingClients:]
+ -[RTTServer registerForUpdatesWithTranslation:forCallUID:]
+ -[RTTServer registerForUpdatesWithTranslation:forCallUID:].cold.1
+ -[RTTTelephonyUtilities _relayNumbers:containsNumber:]
+ -[RTTUtterance hasTranslation]
+ -[RTTUtterance setTranslatedText:]
+ -[RTTUtterance translatedText]
+ -[RTTUtterance updateTranslation:]
+ GCC_except_table3
+ GCC_except_table33
+ GCC_except_table34
+ GCC_except_table40
+ GCC_except_table41
+ GCC_except_table46
+ GCC_except_table47
+ GCC_except_table57
+ GCC_except_table66
+ GCC_except_table70
+ GCC_except_table84
+ GCC_except_table86
+ _AXTTYMessageKeyLocalLocale
+ _AXTTYMessageKeyMessageText
+ _AXTTYMessageKeyRemoteLocale
+ _AXTTYMessageKeySenderIsMe
+ _AXTTYMessageKeyTranslatedMessageText
+ _CFNotificationCenterRemoveEveryObserver
+ _IDSCopyLocalDeviceUniqueID
+ _OBJC_CLASS_$_NSAttributedString
+ _OBJC_CLASS_$_TUHandle
+ _OBJC_IVAR_$_RTTCall._translationLocales
+ _OBJC_IVAR_$_RTTCall._translator
+ _OBJC_IVAR_$_RTTRemoteCall._discoveryClient
+ _OBJC_IVAR_$_RTTRemoteCall._messagingClients
+ _OBJC_IVAR_$_RTTUtterance._translatedText
+ _TranslationLibrary
+ _TranslationLibraryCore.frameworkLibrary
+ ___21-[RTTRemoteCall stop]_block_invoke
+ ___28-[RTTRemoteCall sendString:]_block_invoke.583
+ ___32-[RTTController callDidConnect:]_block_invoke.57
+ ___33-[RTTCall device:didReceiveText:]_block_invoke.412
+ ___35-[RTTController displayCallPrompt:]_block_invoke.151
+ ___35-[RTTController displayCallPrompt:]_block_invoke.151.cold.1
+ ___35-[RTTController displayCallPrompt:]_block_invoke.191
+ ___36-[RTTController handleUpdatedCalls:]_block_invoke.63
+ ___38-[RTTDictionaryManager deleteIfNeeded]_block_invoke.282
+ ___39-[RTTController handleDatabaseRequest:]_block_invoke.138
+ ___39-[RTTDatabaseManager saveConversation:]_block_invoke.60
+ ___40-[RTTCall _sendTranslationForUtterance:]_block_invoke
+ ___40-[RTTCall _sendTranslationForUtterance:]_block_invoke.cold.1
+ ___41-[RTTController displayRTTDowngradeAlert]_block_invoke
+ ___44-[RTTRemoteCall responseForRequest:options:]_block_invoke.624
+ ___44-[RTTRemoteCall responseForRequest:options:]_block_invoke.626
+ ___44-[RTTRemoteCall responseForRequest:options:]_block_invoke.626.cold.1
+ ___47-[RTTConversation lastUtteranceForMe:withText:]_block_invoke
+ ___48-[RTTTelephonyUtilities iCloudAccountDidChange:]_block_invoke.146
+ ___49-[RTTRemoteCall callDidReceiveText:forUtterance:]_block_invoke.600
+ ___49-[RTTRemoteCall callDidReceiveText:forUtterance:]_block_invoke.604
+ ___51-[RTTTelephonyUtilities listenForCloudRelayChanges]_block_invoke.141
+ ___51-[RTTTelephonyUtilities listenForCloudRelayChanges]_block_invoke.143
+ ___52-[RTTServer handleMessageWithPayload:forIdentifier:]_block_invoke.55
+ ___55-[RTTRemoteCall newRapportClientWithDestinationDevice:]_block_invoke
+ ___55-[RTTRemoteCall newRapportClientWithDestinationDevice:]_block_invoke.613
+ ___55-[RTTRemoteCall newRapportClientWithDestinationDevice:]_block_invoke.616
+ ___55-[RTTRemoteCall newRapportClientWithDestinationDevice:]_block_invoke.617
+ ___55-[RTTRemoteCall newRapportClientWithDestinationDevice:]_block_invoke_2
+ ___55-[RTTRemoteCall newRapportClientWithDestinationDevice:]_block_invoke_3
+ ___58+[RTTTelephonyUtilities performCallCenterTask:callCenter:]_block_invoke
+ ___58-[RTTServer registerForUpdatesWithTranslation:forCallUID:]_block_invoke
+ ___61-[RTTRemoteCall sendCallIDChallengeToDeviceId:orAlternateId:]_block_invoke.620
+ ___77-[RTTCall saveTranslatedTranscribedTextForConversation:translatedText:isNew:]_block_invoke
+ ___TranslationLibraryCore_block_invoke
+ ____RTTSendUserNotification_block_invoke.51
+ ___block_descriptor_32_e38_v32?0"RPCompanionLinkClient"8Q16^B24l
+ ___block_descriptor_40_e8_32s_e31_B16?0"RPCompanionLinkDevice"8ls32l8
+ ___block_descriptor_40_e8_32s_e31_v16?0"RPCompanionLinkDevice"8ls32l8
+ ___block_descriptor_48_e8_32s40s_e17_v16?0"NSError"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e88_v32?0"NSDictionary"8"NSDictionary"16?<v?"NSDictionary""NSDictionary""NSError">24ls32l8s40l8
+ ___block_descriptor_49_e8_32s40r_e29_v32?0"RTTUtterance"8Q16^B24ls32l8r40l8
+ ___block_descriptor_57_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_57_e8_32s40s48w_e50_v24?0"_LTCombinedTranslationResult"8"NSError"16ls32l8w48l8s40l8
+ ___block_literal_global.107
+ ___block_literal_global.125
+ ___block_literal_global.141
+ ___block_literal_global.154
+ ___block_literal_global.193
+ ___block_literal_global.208
+ ___block_literal_global.284
+ ___block_literal_global.286
+ ___block_literal_global.29
+ ___block_literal_global.34
+ ___block_literal_global.46
+ ___block_literal_global.49
+ ___block_literal_global.50
+ ___block_literal_global.54
+ ___block_literal_global.568
+ ___block_literal_global.60
+ ___block_literal_global.75
+ ___block_literal_global.84
+ ___get_LTLocalePairClass_block_invoke
+ ___get_LTLocalePairClass_block_invoke.cold.1
+ ___get_LTTextTranslationRequestClass_block_invoke
+ ___get_LTTextTranslationRequestClass_block_invoke.cold.1
+ ___get_LTTranslatorClass_block_invoke
+ ___get_LTTranslatorClass_block_invoke.cold.1
+ _get_LTLocalePairClass.softClass
+ _get_LTTextTranslationRequestClass.softClass
+ _get_LTTranslatorClass.softClass
+ _objc_msgSend$_relayNumbers:containsNumber:
+ _objc_msgSend$_sendTranslationForUtterance:
+ _objc_msgSend$_updateConversationControllerWithTranslatedTranscription:translation:type:callUUID:
+ _objc_msgSend$activeDevices
+ _objc_msgSend$addTranslatedTranscriptionFromOtherContactPath:original:
+ _objc_msgSend$allValues
+ _objc_msgSend$ax_firstObjectUsingBlock:
+ _objc_msgSend$displayRTTDowngradeAlert
+ _objc_msgSend$formatMessage:withType:isMe:
+ _objc_msgSend$handleRTTVoicemailMessage:
+ _objc_msgSend$initWithSourceLocale:targetLocale:
+ _objc_msgSend$initWithString:
+ _objc_msgSend$invertedSet
+ _objc_msgSend$isTTYSupported
+ _objc_msgSend$localeIdentifier
+ _objc_msgSend$newRapportClientWithDestinationDevice:
+ _objc_msgSend$normalizedPhoneNumberHandleForValue:isoCountryCode:
+ _objc_msgSend$normalizedValue
+ _objc_msgSend$performCallCenterTask:callCenter:
+ _objc_msgSend$queue
+ _objc_msgSend$rapportClientForDevice:
+ _objc_msgSend$regionCode
+ _objc_msgSend$resetRapportClientForDevice:invalidate:
+ _objc_msgSend$saveTranslatedTranscribedTextForConversation:translatedText:isNew:
+ _objc_msgSend$sendRequestID:request:options:responseHandler:
+ _objc_msgSend$sendToTTYDeviceWithString:
+ _objc_msgSend$setCompletionHandler:
+ _objc_msgSend$setDestinationDevice:
+ _objc_msgSend$setTaskHint:
+ _objc_msgSend$setTranslatedText:
+ _objc_msgSend$setTranslationLocales:
+ _objc_msgSend$setTranslationLocalesWithLocal:remote:
+ _objc_msgSend$setTranslator:
+ _objc_msgSend$sourceLocale
+ _objc_msgSend$targetLocale
+ _objc_msgSend$translate:
+ _objc_msgSend$translatedText
+ _objc_msgSend$translationLocales
+ _objc_msgSend$translator
+ _objc_msgSend$ttyCall:didUpdateTranslation:forUtterance:
+ _objc_msgSend$updateTranslatedTranscriptionFromOtherContactPath:original:
+ _objc_msgSend$updateTranslation:
+ _objc_msgSend$utteranceWithContactPath:andText:translatedText:isTranscription:
+ _objc_retain_x5
- -[RTTCall sendVoicemailTranscriptionText:]
- -[RTTRemoteCall client]
- -[RTTRemoteCall resetRapportClientAndInvalidate:]
- -[RTTRemoteCall setClient:]
- -[RTTRemoteCall setupRapportClient]
- GCC_except_table14
- GCC_except_table16
- GCC_except_table25
- GCC_except_table38
- GCC_except_table39
- GCC_except_table43
- GCC_except_table44
- GCC_except_table53
- GCC_except_table56
- GCC_except_table61
- GCC_except_table62
- GCC_except_table65
- GCC_except_table69
- GCC_except_table83
- GCC_except_table85
- _OBJC_IVAR_$_RTTRemoteCall._client
- ___27-[RTTRemoteCall addDevice:]_block_invoke.561
- ___28-[RTTRemoteCall sendString:]_block_invoke.517
- ___30-[RTTRemoteCall removeDevice:]_block_invoke
- ___32-[RTTController callDidConnect:]_block_invoke.39
- ___33-[RTTCall device:didReceiveText:]_block_invoke.374
- ___35-[RTTController displayCallPrompt:]_block_invoke.125
- ___35-[RTTController displayCallPrompt:]_block_invoke.125.cold.1
- ___35-[RTTController displayCallPrompt:]_block_invoke.165
- ___35-[RTTRemoteCall setupRapportClient]_block_invoke
- ___35-[RTTRemoteCall setupRapportClient]_block_invoke.549
- ___35-[RTTRemoteCall setupRapportClient]_block_invoke.550
- ___35-[RTTRemoteCall setupRapportClient]_block_invoke_2
- ___35-[RTTRemoteCall setupRapportClient]_block_invoke_3
- ___35-[RTTRemoteCall setupRapportClient]_block_invoke_4
- ___36-[RTTController handleUpdatedCalls:]_block_invoke.45
- ___38-[RTTDictionaryManager deleteIfNeeded]_block_invoke.276
- ___39-[RTTController handleDatabaseRequest:]_block_invoke.112
- ___39-[RTTDatabaseManager saveConversation:]_block_invoke.42
- ___42-[RTTCall sendVoicemailTranscriptionText:]_block_invoke
- ___44-[RTTRemoteCall responseForRequest:options:]_block_invoke.569
- ___44-[RTTRemoteCall responseForRequest:options:]_block_invoke.569.cold.1
- ___47+[RTTTelephonyUtilities performCallCenterTask:]_block_invoke
- ___48-[RTTTelephonyUtilities iCloudAccountDidChange:]_block_invoke.128
- ___49-[RTTRemoteCall callDidReceiveText:forUtterance:]_block_invoke.534
- ___49-[RTTRemoteCall callDidReceiveText:forUtterance:]_block_invoke.538
- ___51-[RTTTelephonyUtilities listenForCloudRelayChanges]_block_invoke.123
- ___51-[RTTTelephonyUtilities listenForCloudRelayChanges]_block_invoke.125
- ___52-[RTTServer handleMessageWithPayload:forIdentifier:]_block_invoke.37
- ___61-[RTTRemoteCall sendCallIDChallengeToDeviceId:orAlternateId:]_block_invoke.560
- ____RTTSendUserNotification_block_invoke.33
- ___block_descriptor_40_e8_32w_e17_v16?0"NSError"8lw32l8
- ___block_descriptor_40_e8_32w_e31_v16?0"RPCompanionLinkDevice"8lw32l8
- ___block_descriptor_40_e8_32w_e88_v32?0"NSDictionary"8"NSDictionary"16?<v?"NSDictionary""NSDictionary""NSError">24lw32l8
- ___block_literal_global.11
- ___block_literal_global.115
- ___block_literal_global.128
- ___block_literal_global.16
- ___block_literal_global.167
- ___block_literal_global.173
- ___block_literal_global.182
- ___block_literal_global.28
- ___block_literal_global.281
- ___block_literal_global.283
- ___block_literal_global.31
- ___block_literal_global.32
- ___block_literal_global.36
- ___block_literal_global.42
- ___block_literal_global.48
- ___block_literal_global.543
- ___block_literal_global.554
- ___block_literal_global.57
- ___block_literal_global.81
- _objc_msgSend$resetRapportClientAndInvalidate:
- _objc_msgSend$sendRequestID:request:destinationID:options:responseHandler:
- _objc_msgSend$sendVoicemailTranscriptionText:
- _objc_msgSend$setupRapportClient
CStrings:
+ "@\"_LTLocalePair\""
+ "@\"_LTTranslator\""
+ "@28@0:8B16@20"
+ "@36@0:8@16q24B32"
+ "@44@0:8@16@24@32B40"
+ "B16@?0@\"RPCompanionLinkDevice\"8"
+ "Companion link for device %@ was interrupted"
+ "Companion link for device %@ was invalidated: %@"
+ "Contact matching emergency number but emergency RTT isn't supported, dialing as voice call immediately: %@"
+ "Creating rapport client for destination device %@"
+ "Existing paired device %@ matches ID %@ (%@)"
+ "Failed to translate utterance with error %@"
+ "Found device %@ for identifier %@"
+ "Found exact match for %{private}@"
+ "Injecting message for callID %@, messageType: %ld, senderIsMe: %@, messageText: %{private}@, translatedText: %{private}@"
+ "Invalidate Rapport client for device %@ and setup again"
+ "Link failed to activate for device %@: %@"
+ "Matching %{private}@ to %{private}@ with locale normalization"
+ "Matching %{private}@ to %{private}@ with non-numeric character stripping"
+ "RTTAutomatedPrefix"
+ "RTTDowngradeAlertMessage"
+ "RTTDowngradeAlertTitle"
+ "RTTOk"
+ "RTTTranslationPrefix"
+ "RTTUtteranceTranslatedTextKey"
+ "Received updated translation %@ for utterance: %@, sending to delegate: %@"
+ "Sending challenge request %@"
+ "Successfully translated utterance"
+ "T@\"NSMutableDictionary\",&,N,V_messagingClients"
+ "T@\"NSString\",C,N,V_translatedText"
+ "T@\"RPCompanionLinkClient\",&,N,V_discoveryClient"
+ "T@\"_LTLocalePair\",&,N,V_translationLocales"
+ "T@\"_LTTranslator\",&,N,V_translator"
+ "Updating translation locales for callID %@, local: %@, remote: %@"
+ "[%p] Client for device %@ handling request %@"
+ "[RTTRemoteCallActiveCallRequestKey] Paired device is nil or sender didn't match. Paired device id: %@, idsID: %@, senderID: %@, senderIDS: %@"
+ "_LTLocalePair"
+ "_LTTextTranslationRequest"
+ "_LTTranslator"
+ "_discoveryClient"
+ "_messagingClients"
+ "_relayNumbers:containsNumber:"
+ "_sendTranslationForUtterance:"
+ "_translatedText"
+ "_translationLocales"
+ "_translator"
+ "_updateConversationControllerWithTranslatedTranscription:translation:type:callUUID:"
+ "activeDevices"
+ "addTranslatedTranscriptionFromOtherContactPath:original:"
+ "allValues"
+ "ax_firstObjectUsingBlock:"
+ "axtty_local_locale"
+ "axtty_message_text"
+ "axtty_remote_locale"
+ "axtty_sender_is_me"
+ "axtty_translated_message_text"
+ "discoveryClient"
+ "displayRTTDowngradeAlert"
+ "formatMessage:withType:isMe:"
+ "handleRTTMessageInjection:"
+ "handleRTTTranslationLocaleMessage:"
+ "hasTranslation"
+ "initWithSourceLocale:targetLocale:"
+ "initWithString:"
+ "invertedSet"
+ "lastUtteranceForMe:withText:"
+ "localeIdentifier"
+ "messagingClients"
+ "newRapportClientWithDestinationDevice:"
+ "normalizedPhoneNumberHandleForValue:isoCountryCode:"
+ "normalizedValue"
+ "performCallCenterTask:callCenter:"
+ "queue"
+ "rapportClientForDevice:"
+ "regionCode"
+ "registerForUpdatesWithTranslation:forCallUID:"
+ "resetRapportClientForDevice:invalidate:"
+ "saveTranslatedTranscribedTextForConversation:translatedText:isNew:"
+ "sendRequestID:request:options:responseHandler:"
+ "sendToTTYDeviceWithString:"
+ "setCompletionHandler:"
+ "setDestinationDevice:"
+ "setDiscoveryClient:"
+ "setMessagingClients:"
+ "setTaskHint:"
+ "setTranslatedText:"
+ "setTranslationLocales:"
+ "setTranslationLocalesWithLocal:remote:"
+ "setTranslator:"
+ "softlink:r:path:/System/Library/Frameworks/Translation.framework/Translation"
+ "sourceLocale"
+ "targetLocale"
+ "translate:"
+ "translatedText"
+ "translationLocales"
+ "translator"
+ "ttyCall:didUpdateTranslation:forUtterance:"
+ "updateTranslatedTranscriptionFromOtherContactPath:original:"
+ "updateTranslation:"
+ "utteranceWithContactPath:andText:translatedText:isTranscription:"
+ "v24@?0@\"_LTCombinedTranslationResult\"8@\"NSError\"16"
+ "v32@?0@\"RPCompanionLinkClient\"8Q16^B24"
+ "v48@0:8@16@24q32@40"
- "Companion link was interrupted"
- "Companion link was invalidated: %@"
- "Invalidate Rapport client and setup again"
- "Link failed to activate %@"
- "RTTFirstUseAlertAcceptButton"
- "Starting rapport support"
- "T@\"RPCompanionLinkClient\",&,N,V_client"
- "TTY send voicemail transcription %d = |%@| %lu"
- "[RTTRemoteCallActiveCallRequestKey] Sender didn't match. Paired device id: %@, idsID: %@, senderID: %@, senderIDS: %@"
- "_client"
- "resetRapportClientAndInvalidate:"
- "sendRequestID:request:destinationID:options:responseHandler:"
- "sendVoicemailTranscriptionText:"
- "setClient:"
- "setupRapportClient"

```
