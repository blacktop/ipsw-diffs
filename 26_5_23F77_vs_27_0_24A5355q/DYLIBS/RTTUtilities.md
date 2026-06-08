## RTTUtilities

> `/System/Library/PrivateFrameworks/RTTUtilities.framework/RTTUtilities`

```diff

-496.22.0.0.0
-  __TEXT.__text: 0x29350
-  __TEXT.__auth_stubs: 0x990
-  __TEXT.__objc_methlist: 0x1d30
-  __TEXT.__const: 0x182
-  __TEXT.__gcc_except_tab: 0xcf4
-  __TEXT.__cstring: 0x18d7
-  __TEXT.__oslogstring: 0x2f8e
-  __TEXT.__dlopen_cstrs: 0x279
-  __TEXT.__ustring: 0x4
+527.0.0.0.0
+  __TEXT.__text: 0x27c34
+  __TEXT.__objc_methlist: 0x1e18
+  __TEXT.__const: 0x1c0
+  __TEXT.__dlopen_cstrs: 0x2cf
+  __TEXT.__cstring: 0x194b
   __TEXT.__swift5_typeref: 0x46
   __TEXT.__swift5_capture: 0x30
   __TEXT.__constg_swiftt: 0x9c
   __TEXT.__swift5_reflstr: 0xb
   __TEXT.__swift5_fieldmd: 0x38
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0xb20
+  __TEXT.__gcc_except_tab: 0xcd8
+  __TEXT.__oslogstring: 0x34d2
+  __TEXT.__ustring: 0x4
+  __TEXT.__unwind_info: 0xa70
   __TEXT.__eh_frame: 0x48
-  __TEXT.__objc_classname: 0x284
-  __TEXT.__objc_methname: 0x5bf4
-  __TEXT.__objc_methtype: 0x93b
-  __TEXT.__objc_stubs: 0x52a0
-  __DATA_CONST.__got: 0x3a8
-  __DATA_CONST.__const: 0xfd0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0xf90
   __DATA_CONST.__objc_classlist: 0x98
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x58
+  __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1960
+  __DATA_CONST.__objc_selrefs: 0x19f0
   __DATA_CONST.__objc_superrefs: 0x78
-  __DATA_CONST.__objc_arraydata: 0x190
-  __AUTH_CONST.__auth_got: 0x4d8
+  __DATA_CONST.__objc_arraydata: 0x118
+  __DATA_CONST.__got: 0x390
   __AUTH_CONST.__const: 0x558
-  __AUTH_CONST.__cfstring: 0x18e0
-  __AUTH_CONST.__objc_const: 0x2008
+  __AUTH_CONST.__cfstring: 0x1920
+  __AUTH_CONST.__objc_const: 0x20b8
   __AUTH_CONST.__objc_dictobj: 0x118
   __AUTH_CONST.__objc_intobj: 0x108
-  __AUTH_CONST.__objc_arrayobj: 0xc0
+  __AUTH_CONST.__objc_arrayobj: 0x48
+  __AUTH_CONST.__auth_got: 0x538
   __AUTH.__objc_data: 0x198
   __AUTH.__data: 0x50
-  __DATA.__objc_ivar: 0x148
-  __DATA.__data: 0x4c0
-  __DATA.__bss: 0xd0
+  __DATA.__objc_ivar: 0x150
+  __DATA.__data: 0x528
+  __DATA.__bss: 0x108
   __DATA_DIRTY.__objc_data: 0x550
   __DATA_DIRTY.__data: 0x18
-  __DATA_DIRTY.__bss: 0xe8
+  __DATA_DIRTY.__bss: 0xc8
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreTelephony.framework/CoreTelephony
   - /System/Library/Frameworks/Foundation.framework/Foundation
-  - /System/Library/PrivateFrameworks/AVConference.framework/AVConference
   - /System/Library/PrivateFrameworks/AXCoreUtilities.framework/AXCoreUtilities
   - /System/Library/PrivateFrameworks/AXRuntime.framework/AXRuntime
   - /System/Library/PrivateFrameworks/CallHistory.framework/CallHistory

   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
-  - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 80364B1D-7727-359B-90D0-DD95E526BD6E
-  Functions: 850
-  Symbols:   3145
-  CStrings:  1898
+  UUID: F2F64680-9B10-37F1-AA22-EFE773466349
+  Functions: 795
+  Symbols:   3054
+  CStrings:  799
 
Symbols:
+ +[RTTTelephonyUtilities currentConditionsSupportRTT]
+ -[RTTCall audioSessionResumptionRecommended:]
+ -[RTTRemoteCall hasPairedConnection]
+ -[RTTSettings isThumperCallingEnabled]
+ -[RTTSettings setIsThumperCallingEnabled:]
+ -[RTTSettings setSupportsThumperCalling:]
+ -[RTTSettings supportsThumperCalling]
+ -[RTTTelephonyUtilities _callCapabilitiesForUUID:]
+ -[RTTTelephonyUtilities _callCapabilitiesSupportsEmergencyRTTForContext:]
+ -[RTTTelephonyUtilities _callCapabilitiesSupportsHoldForRTTForContext:]
+ -[RTTTelephonyUtilities _callCapabilitiesSupportsRTTForContext:]
+ -[RTTTelephonyUtilities _callCapabilitiesSupportsTTYForContext:]
+ -[RTTTelephonyUtilities _reloadCapabilitiesForContext:]
+ -[RTTTelephonyUtilities callCapabilitiesCache]
+ -[RTTTelephonyUtilities context:capabilitiesChanged:]
+ -[RTTTelephonyUtilities currentConditionsSupportRTTForContext:]
+ -[RTTTelephonyUtilities dataCacheQueue]
+ -[RTTTelephonyUtilities didChangeThumperCallingCapabilitiesForSenderIdentityWithUUID:]
+ -[RTTTelephonyUtilities setCallCapabilitiesCache:]
+ -[RTTTelephonyUtilities setDataCacheQueue:]
+ GCC_except_table150
+ GCC_except_table155
+ GCC_except_table159
+ GCC_except_table161
+ GCC_except_table164
+ GCC_except_table180
+ GCC_except_table182
+ GCC_except_table186
+ GCC_except_table199
+ GCC_except_table200
+ GCC_except_table239
+ GCC_except_table241
+ GCC_except_table276
+ GCC_except_table282
+ GCC_except_table304
+ GCC_except_table309
+ GCC_except_table353
+ GCC_except_table356
+ GCC_except_table365
+ GCC_except_table379
+ GCC_except_table38
+ GCC_except_table386
+ GCC_except_table394
+ GCC_except_table422
+ GCC_except_table432
+ GCC_except_table448
+ GCC_except_table453
+ GCC_except_table473
+ GCC_except_table478
+ GCC_except_table483
+ GCC_except_table487
+ GCC_except_table492
+ GCC_except_table497
+ GCC_except_table499
+ GCC_except_table502
+ GCC_except_table504
+ GCC_except_table506
+ GCC_except_table547
+ GCC_except_table59
+ GCC_except_table644
+ GCC_except_table663
+ GCC_except_table679
+ GCC_except_table684
+ GCC_except_table728
+ GCC_except_table731
+ GCC_except_table78
+ _AVAudioSessionResumptionRecommendationNotification
+ _AVConferenceLibraryCore.frameworkLibrary
+ _AccessibilityUtilitiesLibraryCore.frameworkLibrary.449
+ _OBJC_IVAR_$_RTTTelephonyUtilities._callCapabilitiesCache
+ _OBJC_IVAR_$_RTTTelephonyUtilities._dataCacheQueue
+ _RTTRedactedTextDescription
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CoreTelephonyClientCapabilitiesDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CoreTelephonyClientCapabilitiesDelegate
+ __OBJC_$_PROTOCOL_REFS_CoreTelephonyClientCapabilitiesDelegate
+ __OBJC_LABEL_PROTOCOL_$_CoreTelephonyClientCapabilitiesDelegate
+ __OBJC_PROTOCOL_$_CoreTelephonyClientCapabilitiesDelegate
+ ___28-[RTTRemoteCall sendString:]_block_invoke.661
+ ___33-[RTTCall device:didReceiveText:]_block_invoke.486
+ ___34-[RTTSettings setCannedResponses:]_block_invoke.208
+ ___38-[RTTDictionaryManager deleteIfNeeded]_block_invoke.351
+ ___38-[RTTDictionaryManager deleteIfNeeded]_block_invoke.354
+ ___44-[RTTRemoteCall responseForRequest:options:]_block_invoke.702
+ ___44-[RTTRemoteCall responseForRequest:options:]_block_invoke.704
+ ___45-[RTTCall audioSessionResumptionRecommended:]_block_invoke
+ ___48-[RTTTelephonyUtilities iCloudAccountDidChange:]_block_invoke.135
+ ___49-[RTTRemoteCall callDidReceiveText:forUtterance:]_block_invoke.678
+ ___49-[RTTRemoteCall callDidReceiveText:forUtterance:]_block_invoke.682
+ ___50-[RTTTelephonyUtilities _callCapabilitiesForUUID:]_block_invoke
+ ___50-[RTTTelephonyUtilities reloadDefaultVoiceContext]_block_invoke.106
+ ___51-[RTTTelephonyUtilities listenForCloudRelayChanges]_block_invoke.130
+ ___51-[RTTTelephonyUtilities listenForCloudRelayChanges]_block_invoke.132
+ ___55-[RTTRemoteCall newRapportClientWithDestinationDevice:]_block_invoke.691
+ ___55-[RTTRemoteCall newRapportClientWithDestinationDevice:]_block_invoke.694
+ ___55-[RTTRemoteCall newRapportClientWithDestinationDevice:]_block_invoke.695
+ ___55-[RTTTelephonyUtilities _reloadCapabilitiesForContext:]_block_invoke
+ ___61-[RTTRemoteCall sendCallIDChallengeToDeviceId:orAlternateId:]_block_invoke.698
+ ___AVConferenceLibraryCore_block_invoke
+ ___AccessibilityUtilitiesLibraryCore_block_invoke.450
+ ___Block_byref_object_copy_.1042
+ ___Block_byref_object_copy_.117
+ ___Block_byref_object_copy_.279
+ ___Block_byref_object_copy_.469
+ ___Block_byref_object_dispose_.1043
+ ___Block_byref_object_dispose_.118
+ ___Block_byref_object_dispose_.280
+ ___Block_byref_object_dispose_.470
+ ___block_literal_global.1038
+ ___block_literal_global.105
+ ___block_literal_global.109.124
+ ___block_literal_global.140
+ ___block_literal_global.179
+ ___block_literal_global.204
+ ___block_literal_global.208
+ ___block_literal_global.352
+ ___block_literal_global.356
+ ___block_literal_global.358
+ ___block_literal_global.363
+ ___block_literal_global.377
+ ___block_literal_global.403
+ ___block_literal_global.404
+ ___block_literal_global.45.176
+ ___block_literal_global.524
+ ___block_literal_global.646
+ ___block_literal_global.78
+ ___block_literal_global.836
+ ___getAVAudioClientClass_block_invoke
+ ___getAVCVirtualTTYDeviceClass_block_invoke
+ ___gxx_personality_v0
+ ___swift_closure_destructor
+ ___swift_closure_destructor.11
+ ___swift_closure_destructor.14
+ _audit_stringAVConference
+ _audit_stringAccessibilityUtilities.451
+ _getAVAudioClientClass
+ _getAVAudioClientClass.softClass
+ _getAVCVirtualTTYDeviceClass
+ _getAVCVirtualTTYDeviceClass.softClass
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$_callCapabilitiesForUUID:
+ _objc_msgSend$_callCapabilitiesSupportsEmergencyRTTForContext:
+ _objc_msgSend$_callCapabilitiesSupportsHoldForRTTForContext:
+ _objc_msgSend$_callCapabilitiesSupportsRTTForContext:
+ _objc_msgSend$_callCapabilitiesSupportsTTYForContext:
+ _objc_msgSend$_reloadCapabilitiesForContext:
+ _objc_msgSend$callCapabilitiesCache
+ _objc_msgSend$currentConditionsSupportRTT
+ _objc_msgSend$currentConditionsSupportRTTForContext:
+ _objc_msgSend$currentProcessIsRTTExtension
+ _objc_msgSend$dataCacheQueue
+ _objc_msgSend$didChangeThumperCallingCapabilitiesForSenderIdentityWithUUID:
+ _objc_msgSend$getCallCapabilities:error:
+ _objc_msgSend$getVoiceTextMediaPossible:error:
+ _objc_msgSend$hasPairedConnection
+ _objc_msgSend$hash
+ _objc_msgSend$isHoldForRTTEnabled
+ _objc_msgSend$setCallCapabilitiesCache:
+ _objc_msgSend$setDataCacheQueue:
+ _objc_msgSend$setIsThumperCallingEnabled:
+ _objc_msgSend$setRequiresSecureCoding:
+ _objc_msgSend$setSupportsThumperCalling:
+ _objc_msgSend$supportsThumperCalling
+ _objc_retain_x2
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x5
+ _objc_retain_x9
+ _sharedInstance.Settings.374
+ _sharedInstance.onceToken.375
+ _sharedInstance.onceToken.834
+ _swift_getObjCClassMetadata
+ _swift_release_x24
+ _swift_release_x25
+ _swift_release_x26
+ _swift_release_x8
+ _swift_retain_x22
+ _swift_retain_x25
- +[RTTController sharedController].cold.1
- +[RTTConversation conversationWithCall:].cold.1
- +[RTTDatabaseManager sharedManager].cold.1
- +[RTTNanoSettings sharedInstance].cold.1
- +[RTTServer sharedInstance].cold.1
- +[RTTSettings sharedInstance].cold.1
- +[RTTTelephonyUtilities sharedCallCenter].cold.1
- +[RTTTelephonyUtilities sharedUtilityProvider].cold.1
- -[RTTCall audioSessionWasInterrupted:]
- -[RTTController handleRTTVoicemailMessage:].cold.1
- -[RTTController handleRTTVoicemailMessage:].cold.2
- -[RTTDatabaseManager conversationForCallUID:].cold.1
- -[RTTDatabaseManager conversationForCallUID:].cold.2
- -[RTTDatabaseManager conversationForCallUID:].cold.3
- -[RTTDatabaseManager conversationForCallUID:].cold.4
- -[RTTDatabaseManager saveConversation:].cold.1
- -[RTTDatabaseManager saveConversation:].cold.2
- -[RTTDatabaseManager saveConversation:].cold.3
- -[RTTRemoteCall responseForRequest:options:].cold.1
- -[RTTServer _createSandboxUrlForVoicemailMessage:].cold.1
- -[RTTServer _createSandboxUrlForVoicemailMessage:].cold.2
- -[RTTServer displayCallPromptForContact:withCompletion:].cold.1
- -[RTTServer handleMessageError:destructive:].cold.1
- -[RTTServer registerForRemoteUpdates:forCallUID:].cold.1
- -[RTTServer registerForUpdates:forCallUID:].cold.1
- -[RTTServer registerForUpdatesWithTranslation:forCallUID:].cold.1
- -[RTTServer sendConversationUpdate:].cold.1
- -[RTTServer setViewControllerIsVisible:withCallID:].cold.1
- -[RTTServer valueForTTYSetting:].cold.1
- -[RTTSettings _registerForNotification:].cold.1
- -[RTTSettings _selectorMap].cold.1
- -[RTTSettings boolValueForKey:andContext:withDefaultValue:].cold.1
- -[RTTSettings boolValueForKey:andContext:withDefaultValue:].cold.2
- -[RTTTelephonyUtilities getCarrierValueForKeyHierarchy:andContext:].cold.1
- -[RTTTelephonyUtilities isTTYOverIMSSupportedForContext:]
- -[RTTTelephonyUtilities isTTYOverIMSSupportedForContext:excludeRelay:]
- -[RTTTelephonyUtilities phoneNumberForContext:].cold.1
- -[RTTTelephonyUtilities reloadDefaultVoiceContext].cold.1
- -[RTTTelephonyUtilities reloadDefaultVoiceContext].cold.2
- -[RTTTelephonyUtilities ttyMeContact].cold.1
- -[RTTTranscriptionController startTranscribingForCallUUID:].cold.1
- -[RTTTranscriptionController stopTranscribingForCallUUID:].cold.1
- GCC_except_table1
- GCC_except_table10
- GCC_except_table12
- GCC_except_table13
- GCC_except_table15
- GCC_except_table17
- GCC_except_table18
- GCC_except_table2
- GCC_except_table20
- GCC_except_table21
- GCC_except_table26
- GCC_except_table28
- GCC_except_table29
- GCC_except_table3
- GCC_except_table33
- GCC_except_table34
- GCC_except_table46
- GCC_except_table5
- GCC_except_table56
- GCC_except_table57
- GCC_except_table58
- GCC_except_table68
- GCC_except_table69
- GCC_except_table7
- GCC_except_table72
- GCC_except_table74
- GCC_except_table76
- GCC_except_table86
- GCC_except_table88
- GCC_except_table9
- GCC_except_table92
- GCC_except_table94
- GCC_except_table95
- _AVAudioSessionInterruptionNotification
- _AVAudioSessionInterruptionTypeKey
- _AccessibilityUtilitiesLibrary
- _LiveTranscriptionLibrary
- _OBJC_CLASS_$_AVAudioClient
- _OBJC_CLASS_$_AVCVirtualTTYDevice
- _OUTLINED_FUNCTION_0
- _OUTLINED_FUNCTION_1
- _OUTLINED_FUNCTION_2
- _OUTLINED_FUNCTION_3
- _OUTLINED_FUNCTION_4
- _RTTNotificationCenter
- _RTTNotificationCenter.cold.1
- _SpeechLibrary
- _TranslationLibrary
- _UserNotificationsLibrary
- ___28-[RTTRemoteCall sendString:]_block_invoke.643
- ___33-[RTTCall device:didReceiveText:]_block_invoke.467
- ___34-[RTTSettings setCannedResponses:]_block_invoke.203
- ___35-[RTTController displayCallPrompt:]_block_invoke.153.cold.1
- ___38-[RTTCall audioSessionWasInterrupted:]_block_invoke
- ___38-[RTTDictionaryManager deleteIfNeeded]_block_invoke.330
- ___38-[RTTDictionaryManager deleteIfNeeded]_block_invoke.333
- ___39-[RTTController handleDatabaseRequest:]_block_invoke.cold.1
- ___39-[RTTController handleDatabaseRequest:]_block_invoke.cold.2
- ___39-[RTTController handleDatabaseRequest:]_block_invoke.cold.3
- ___39-[RTTController handleDatabaseRequest:]_block_invoke.cold.4
- ___40-[RTTCall _sendTranslationForUtterance:]_block_invoke.cold.1
- ___40-[RTTSettings _registerForNotification:]_block_invoke_2.cold.1
- ___41-[RTTCall _postLocalNotificationForText:]_block_invoke.cold.1
- ___44-[RTTRemoteCall responseForRequest:options:]_block_invoke.684
- ___44-[RTTRemoteCall responseForRequest:options:]_block_invoke.686
- ___44-[RTTRemoteCall responseForRequest:options:]_block_invoke.686.cold.1
- ___47-[RTTDatabaseManager contactPathWasUsedForTTY:]_block_invoke.cold.1
- ___48-[RTTTelephonyUtilities iCloudAccountDidChange:]_block_invoke.156
- ___49-[RTTRemoteCall callDidReceiveText:forUtterance:]_block_invoke.660
- ___49-[RTTRemoteCall callDidReceiveText:forUtterance:]_block_invoke.664
- ___50-[RTTServer findConversationForCallUID:andResult:]_block_invoke_2.cold.1
- ___50-[RTTTelephonyUtilities reloadDefaultVoiceContext]_block_invoke.100
- ___51-[RTTTelephonyUtilities listenForCloudRelayChanges]_block_invoke.151
- ___51-[RTTTelephonyUtilities listenForCloudRelayChanges]_block_invoke.153
- ___55-[RTTRemoteCall newRapportClientWithDestinationDevice:]_block_invoke.673
- ___55-[RTTRemoteCall newRapportClientWithDestinationDevice:]_block_invoke.676
- ___55-[RTTRemoteCall newRapportClientWithDestinationDevice:]_block_invoke.677
- ___60-[RTTTranscriptionController stopTranscribingV2ForCallUUID:]_block_invoke.cold.1
- ___61-[RTTRemoteCall sendCallIDChallengeToDeviceId:orAlternateId:]_block_invoke.680
- ___61-[RTTTranscriptionController startTranscribingV2ForCallUUID:]_block_invoke.cold.1
- ___61-[RTTTranscriptionController startTranscribingV2ForCallUUID:]_block_invoke.cold.2
- ____RTTSendUserNotification_block_invoke.cold.1
- ___block_descriptor_48_e8_32s40r_e5_v8?0ls32l8r40l8
- ___block_descriptor_64_e8_32s40s48s56r_e5_v8?0ls32l8s40l8r56l8s48l8
- ___block_literal_global.103
- ___block_literal_global.135
- ___block_literal_global.199
- ___block_literal_global.335
- ___block_literal_global.337
- ___block_literal_global.366
- ___block_literal_global.393
- ___block_literal_global.46
- ___block_literal_global.628
- ___block_literal_global.73
- ___block_literal_global.95
- ___getAXLTLiveTranscriptionClass_block_invoke.cold.1
- ___getAXSpringBoardServerClass_block_invoke.cold.1
- ___getAXUIClientClass_block_invoke.cold.1
- ___getSFSpeechRecognizerClass_block_invoke.cold.1
- ___getSFSpeechURLRecognitionRequestClass_block_invoke.cold.1
- ___getUNMutableNotificationContentClass_block_invoke.cold.1
- ___getUNNotificationCategoryClass_block_invoke.cold.1
- ___getUNNotificationRequestClass_block_invoke.cold.1
- ___getUNUserNotificationCenterClass_block_invoke.cold.1
- ___get_LTLocalePairClass_block_invoke.cold.1
- ___get_LTTextTranslationRequestClass_block_invoke.cold.1
- ___get_LTTranslatorClass_block_invoke.cold.1
- __swift_FORCE_LOAD_$_swiftCoreMedia
- __swift_FORCE_LOAD_$_swiftCoreMedia_$_RTTUtilities
- _objc_msgSend$currentProcessIsRTTExternsion
- _objc_msgSend$isTTYOverIMSSupportedForContext:excludeRelay:
- _objc_msgSend$sharedAVSystemController
- _objc_msgSend$userInfo
- _objc_retain_x27
- _sharedInstance.Settings.363
- _sharedInstance.onceToken.364
- _soft_AXHasCapability.cold.1
- _swift_release
- _swift_retain
CStrings:
+ "%@ %@ [%d]: %@"
+ "<len=%lu hash=%08x>"
+ "<nil>"
+ "AVAudioClient"
+ "AVCVirtualTTYDevice"
+ "Audio session resumption recommended %@"
+ "Capabilities did change, reloading"
+ "Context is nil or slotID is unknown. Treating RTT as supported as telephony will not have adequate information for devices without an active SIM\n%@"
+ "Conversation update string: %{sensitive}@"
+ "Current conditions %@ RTT for context %@"
+ "Delegate handling call did receive: %@ for [%{sensitive}@]->%{sensitive}@"
+ "Did change thumper calling availability %d %d"
+ "Emergency RTT (EmergencyRTTSupported) supported %@ - %d -- %d (%d)"
+ "Emergency relay supported: TU supports relay: %d, TU supports thumper: %d, continuity: %d"
+ "EmergencyRTT %@ for context %@ with capabilities %@"
+ "Error checking getVoiceTextMediaPossible: %@"
+ "Error getting call capbilities: %@"
+ "Getting remote call send job: %{sensitive}@"
+ "Handling message update: 0x%llx"
+ "HoldForRTT %@ for context %@ with capabilities %@"
+ "New transcription fp:%@ text:%{sensitive}@"
+ "Not sending %{sensitive}@"
+ "Not sending remote device received text %{sensitive}@, %{sensitive}@"
+ "Not stuttering remote call to avoid messing with rapport connections %@ - %@"
+ "Posting local notification: %{sensitive}@"
+ "Processing individual substring: '%{sensitive}@'"
+ "RTT %@ for context %@ with capabilities %@"
+ "RTT call hold supported %d for context %@"
+ "RTT not current supported, dialing as voice only immediately"
+ "RTT supported %@ - %d -- %d (%d)"
+ "Received remote string %{sensitive}@ for utterance: %{sensitive}@, sending to delegate: %@"
+ "Received request %{sensitive}@"
+ "Received text response %{sensitive}@ = %@"
+ "Received updated translation %{sensitive}@ for utterance: %{sensitive}@, sending to delegate: %@"
+ "Relay supported: TU supports relay: %d, TU supports thumper: %d, continuity: %d"
+ "Replacing with |%{sensitive}@|"
+ "Send string for remote call: %{sensitive}@"
+ "Sending remote device received text %{sensitive}@"
+ "Sending remote string %{sensitive}@ for utterance: %{sensitive}@"
+ "Sending string fp:%@ text:%{sensitive}@ with utterance: %@"
+ "Sending text %{sensitive}@ - %@"
+ "Sent text response %{sensitive}@ = %@"
+ "TTY %@ for context %@ with capabilities %@"
+ "TTY receive %{sensitive}C, |%{sensitive}x|"
+ "TTY receive string fp:%@ text:'%{sensitive}@'"
+ "TTY send %{sensitive}C, |%{sensitive}x|"
+ "TTY send string %d = |%{sensitive}@| %lu"
+ "TUCallCenter has no entry for callID=%@"
+ "TUIsThumperCallingEnabledPreference"
+ "TUSupportsThumperCallingPreference"
+ "Transcribed voicemail message text fp:%@ text:%{sensitive}@"
+ "Updated transcription fp:%@ text:%{sensitive}@"
+ "Using non-international phone number: %{private}@"
+ "XPC returned existing conversation for %@: %@"
+ "XPC returned no conversation for %@; created fresh local conversation (heard may not be ready yet)"
+ "[%p] Client for device %@ handling request %{sensitive}@"
+ "don't support"
+ "not processing initial text because it looks like garbage: %{sensitive}@"
+ "not supported"
+ "otherContactPath returning nil (callID=%@, utteranceCount=%lu)"
+ "softlink:r:path:/System/Library/PrivateFrameworks/AVConference.framework/AVConference"
+ "support"
+ "supported"
+ "ttyDataCacheQueue"
- "#16@0:8"
- "%@ %@ [%d]: %{sensitive}@"
- ".cxx_destruct"
- ":24@0:8@16"
- "@\"<HCHeardControllerProtocol>\""
- "@\"<RTTCallDelegate>\""
- "@\"<RTTTranscriptionControllerDelegate>\""
- "@\"ACAccountStore\""
- "@\"AVCVirtualTTYDevice\""
- "@\"AXAccessQueue\"32@0:8@\"AXUIClient\"16Q24"
- "@\"AXDispatchTimer\""
- "@\"AXLTLiveTranscription\""
- "@\"AXUIClient\""
- "@\"CHManager\""
- "@\"CNContactStore\""
- "@\"CTXPCContexts\""
- "@\"CTXPCServiceSubscriptionContext\""
- "@\"CoreTelephonyClient\""
- "@\"NPSDomainAccessor\""
- "@\"NSArray\""
- "@\"NSDate\""
- "@\"NSDictionary\""
- "@\"NSDictionary\"40@0:8@\"NSString\"16@\"NSDictionary\"24@\"NSDictionary\"32"
- "@\"NSDictionary\"48@0:8@\"AXUIClient\"16@\"NSDictionary\"24Q32^@40"
- "@\"NSLock\""
- "@\"NSMutableArray\""
- "@\"NSMutableDictionary\""
- "@\"NSMutableSet\""
- "@\"NSMutableString\""
- "@\"NSNumber\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSSet\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSUUID\""
- "@\"RBSAssertion\""
- "@\"RPCompanionLinkClient\""
- "@\"RPCompanionLinkDevice\""
- "@\"RTTConversation\""
- "@\"RTTLiveCaptionsObjC\""
- "@\"RTTTranscriptionController\""
- "@\"TUCall\""
- "@\"_LTLocalePair\""
- "@\"_LTTranslator\""
- "@16@0:8"
- "@20@0:8B16"
- "@20@0:8S16"
- "@24@0:8:16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@24@0:8B16B20"
- "@24@0:8^v16"
- "@24@0:8^{_NSZone=}16"
- "@28@0:8B16@20"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@32@0:8@16Q24"
- "@36@0:8@16@24B32"
- "@36@0:8@16q24B32"
- "@40@0:8:16@24@32"
- "@40@0:8@16#24@32"
- "@40@0:8@16@24@32"
- "@44@0:8@16@24@32B40"
- "@48@0:8@16@24#32@40"
- "@48@0:8@16@24Q32^@40"
- "@?"
- "@?16@0:8"
- "AVCVirtualTTYDeviceDelegate"
- "AXRTTSettingsListenerHelper"
- "AXTTYSimulatorSubscriptionContext"
- "AXUIClientDelegate"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B28@0:8@16B24"
- "B32@0:8@\"AXUIClient\"16Q24"
- "B32@0:8@16@24"
- "B32@0:8@16Q24"
- "B32@0:8q16^@24"
- "B36@0:8@16@24B32"
- "B40@0:8@16@24@32"
- "B60@0:8q16@24B32@36^@44@?52"
- "Conversation update string: %@"
- "CoreDataProperties"
- "CoreTelephonyClientDelegate"
- "Delegate handling call did receive: %@ for [%@]->%@"
- "Emergency RTT (EmergencyRTTSupported) supported %@ - %d = %@ -- %d (%d)"
- "Emergency relay supported: TU supports: %d, continuity: %d"
- "EmergencyRTTSupported"
- "EnableHoldForRTT"
- "Getting remote call send job: %@"
- "Handling message update: %d"
- "Media server interrupted %@"
- "NSCoding"
- "NSCopying"
- "NSObject"
- "NSSecureCoding"
- "New transcription: %@"
- "Not sending %@"
- "Not sending remote device received text %@, %@"
- "Posting local notification: %@"
- "Processing individual substring: '%@'"
- "Q16@0:8"
- "Q20@0:8B16"
- "Q24@0:8@16"
- "Q24@0:8B16B20"
- "RTT (RTTSupported) supported %@ - %d = %@ -- %d (%d)"
- "RTT (ttyIMSSupported) supported %@ - %d = %@ -- %d (%d)"
- "RTT call hold supported %@ for context %@"
- "RTTCall"
- "RTTCallDelegate"
- "RTTController"
- "RTTConversation"
- "RTTDatabaseManager"
- "RTTDictionaryManager"
- "RTTLiveCaptionObjC"
- "RTTLiveCaptionsObjC"
- "RTTNanoSettings"
- "RTTRemoteCall"
- "RTTServer"
- "RTTServiceUpdate"
- "RTTSupported"
- "RTTTelephonyUtilities"
- "RTTTranscriptionController"
- "RTTTranscriptionControllerDelegate"
- "RTTUtterance"
- "Received remote string %@ for utterance: %@, sending to delegate: %@"
- "Received request %@"
- "Received text response %@ = %@"
- "Received updated translation %@ for utterance: %@, sending to delegate: %@"
- "Relay supported: TU supports: %d, continuity: %d"
- "Replacing with |%@|"
- "Send string for remote call: %@"
- "Sending remote device received text %@"
- "Sending remote string %@ for utterance: %@"
- "Sending string[%@] with uttererance: %@"
- "Sending text %@ - %@"
- "Sent text response %@ = %@"
- "ShowTTY"
- "T#,R"
- "T@\"<HCHeardControllerProtocol>\",W,N,V_delegate"
- "T@\"<RTTCallDelegate>\",W,N,V_delegate"
- "T@\"<RTTTranscriptionControllerDelegate>\",W,N,V_delegate"
- "T@\"AVCVirtualTTYDevice\",&,N,V_ttyDevice"
- "T@\"AXLTLiveTranscription\",&,N,V_transcriber"
- "T@\"CNContactStore\",&,N,V_contactStore"
- "T@\"CTXPCContexts\",&,V_cachedActiveContexts"
- "T@\"CTXPCServiceSubscriptionContext\",&,V_defaultVoiceContext"
- "T@\"CoreTelephonyClient\",&,N,V_telephonyClient"
- "T@\"NPSDomainAccessor\",&,N,V_domainAccessor"
- "T@\"NPSDomainAccessor\",&,N,V_globalDomainAccessor"
- "T@\"NSArray\",&,N"
- "T@\"NSArray\",&,N,V_availableDictionaries"
- "T@\"NSArray\",&,V_cachedSubscriptionContexts"
- "T@\"NSData\",&,D,N"
- "T@\"NSDate\",&,N,V_lastChangeDate"
- "T@\"NSDictionary\",&,N,V_options"
- "T@\"NSDictionary\",&,N,V_substitutions"
- "T@\"NSMutableArray\",&,N,V_rttCalls"
- "T@\"NSMutableArray\",&,N,V_utterances"
- "T@\"NSMutableDictionary\",&,N,V_messagingClients"
- "T@\"NSMutableDictionary\",&,N,V_phoneNumberInfoCache"
- "T@\"NSMutableDictionary\",&,N,V_updateBlocks"
- "T@\"NSMutableSet\",&,N,V_registeredNotifications"
- "T@\"NSMutableSet\",&,N,V_synchronizePreferences"
- "T@\"NSNumber\",&"
- "T@\"NSNumber\",&,D,N"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_accountStoreQueue"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_nanoSynchronizeQueue"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_telephonyUpdateQueue"
- "T@\"NSObject<OS_dispatch_queue>\",R,N,V_callQueue"
- "T@\"NSSet\",&,V_allVoiceContexts"
- "T@\"NSString\",&,D,N"
- "T@\"NSString\",&,N"
- "T@\"NSString\",&,N,V_callIdentifier"
- "T@\"NSString\",&,N,V_contactPath"
- "T@\"NSString\",&,N,V_currentCallUUID"
- "T@\"NSString\",&,N,V_currentTranscription"
- "T@\"NSString\",&,N,V_serviceUpdateType"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",C,N,V_text"
- "T@\"NSString\",C,N,V_translatedText"
- "T@\"NSString\",R,C"
- "T@\"NSUUID\",&,N,V_testUuid"
- "T@\"RBSAssertion\",&,N,V_assertionInCallService"
- "T@\"RPCompanionLinkClient\",&,N,V_discoveryClient"
- "T@\"RPCompanionLinkDevice\",&,N,V_pairedCallDevice"
- "T@\"RTTConversation\",&,N,V_conversation"
- "T@\"RTTLiveCaptionsObjC\",&,N,V_liveCaptionsService"
- "T@\"RTTLiveCaptionsObjC\",N,R"
- "T@\"RTTTranscriptionController\",&,N,V_transcriber"
- "T@\"TUCall\",&,N,V_call"
- "T@\"_LTLocalePair\",&,N,V_translationLocales"
- "T@\"_LTTranslator\",&,N,V_translator"
- "T@?,C,N,V_actionCompletionBlock"
- "T@?,C,N,V_serverInvalidateCallback"
- "TB,N"
- "TB,N,V_headphoneJackSupportsTTY"
- "TB,N,V_ignoreTimeoutTemporarily"
- "TB,N,V_isMe"
- "TB,N,V_isTranscription"
- "TB,N,V_isViewControllerVisible"
- "TB,N,V_isVisibleSent"
- "TB,N,V_shouldSuppressIncomingNotification"
- "TB,R"
- "TB,R,N"
- "TQ,R"
- "TQ,V_activeContextCount"
- "TTY receive %C, |%x|"
- "TTY receive string '%@' [%d]"
- "TTY send %C, |%x|"
- "TTY send string %d = |%@| %lu"
- "TTYHardwareEnabled"
- "TTYHardwareEnabledForAnyActiveContext"
- "TTYHardwareEnabledForContext:"
- "TTYSoftwareEnabled"
- "TTYSoftwareEnabledForAnyActiveContext"
- "TTYSoftwareEnabledForContext:"
- "TUCallCapabilitiesDelegate"
- "TUCallCapabilitiesDelegatePrivate"
- "Td,N"
- "Tq,N"
- "Tq,N,R"
- "Transcribed voicemail message text: %@"
- "URL"
- "UUID"
- "UUIDString"
- "Updated transcription: %@"
- "Using non-international phone number: %@"
- "Voice"
- "Vv16@0:8"
- "[%p] Client for device %@ handling request %@"
- "^v"
- "^{_NSZone=}16@0:8"
- "_TTY_"
- "_accountStore"
- "_accountStoreQueue"
- "_actionCompletionBlock"
- "_actionUIClient"
- "_activeContextCount"
- "_allVoiceContexts"
- "_assertionInCallService"
- "_availableDictionaries"
- "_availableDictionaryAssetsUsingRemoteInfo:"
- "_cachedActiveContexts"
- "_cachedSettings"
- "_cachedSubscriptionContexts"
- "_call"
- "_callCapabilitiesSupportsTelephonyCalls"
- "_callDidConnect"
- "_callForUUIDWithoutRefresh:"
- "_callHistoryDBDidChange:"
- "_callHistoryManager"
- "_callIdentifier"
- "_callQueue"
- "_callUpdateCoalescer"
- "_commonRequestQueue"
- "_connectionQueue"
- "_contactIsEmergencyServices:"
- "_contactPath"
- "_contactStore"
- "_conversation"
- "_createSandboxUrlForVoicemailMessage:"
- "_currentCallUUID"
- "_currentTranscription"
- "_dataResponseBlocksLock"
- "_databaseResponseBlocks"
- "_defaultVoiceContext"
- "_delegate"
- "_devices"
- "_discoveryClient"
- "_domainAccessor"
- "_downloadAsset:"
- "_garbageCharacterStripperTimer"
- "_garbageCollection"
- "_globalDomainAccessor"
- "_handleInitialGarbageTextFromTTY:device:"
- "_handlePreferenceChanged:"
- "_handlePreferredRelayNumberUpdate"
- "_headphoneJackSupportsTTY"
- "_icloudAccountConsolidator"
- "_icloudRelayConsolidator"
- "_ignoreTimeoutTemporarily"
- "_incomingMessageTimeout"
- "_ios_meContactWithKeysToFetch:error:"
- "_isMe"
- "_isTranscription"
- "_isViewControllerVisible"
- "_isVisibleSent"
- "_lastChangeDate"
- "_listenerAddress"
- "_liveCaptionsService"
- "_localSettingsCache"
- "_managerAXPIDState:"
- "_messageProcessingQueue"
- "_messagingClients"
- "_nanoSynchronizeQueue"
- "_notificationForPreferenceKey:"
- "_options"
- "_outgoingMessageTimeout"
- "_pairedCallDevice"
- "_phoneNumberInfoCache"
- "_postLocalNotificationForText:"
- "_preferenceKeyForSelector:"
- "_preferredRelayCoalescer"
- "_processMessageTimeoutForMe:"
- "_processText:withDevice:"
- "_processiCloudAccountForRTT"
- "_rapportDevice:matchesID:orAlternateID:"
- "_refreshCurrentCallList"
- "_refreshCurrentCallListWithExistingCalls:"
- "_registerForNotification:"
- "_registerForServerSettingsUpdates"
- "_registeredNotifications"
- "_relayNumbers:containsNumber:"
- "_reloadContexts"
- "_requestNotificationAuthorization"
- "_requestNotificationAuthorizationIfNecessary"
- "_rttCalls"
- "_selectorKeys"
- "_selectorMap"
- "_sendTranslationForUtterance:"
- "_serverInvalidateCallback"
- "_serviceUpdateType"
- "_setValue:forPreferenceKey:"
- "_setValue:forPreferenceKey:andContext:"
- "_shouldSuppressIncomingNotification"
- "_substitutions"
- "_synchronizeDomainsLock"
- "_synchronizeIfNecessary:"
- "_synchronizePreferences"
- "_takeStackshot"
- "_telephonyClient"
- "_telephonyUpdateQueue"
- "_testUuid"
- "_text"
- "_transcriber"
- "_translatedText"
- "_translationLocales"
- "_translator"
- "_ttyDevice"
- "_ttyDictionaryAsset"
- "_ttyMode"
- "_updateBlocks"
- "_updateConversationControllerWithTranscription:type:callUUID:"
- "_updateConversationControllerWithTranslatedTranscription:translation:type:callUUID:"
- "_utterances"
- "_workerQueue"
- "accountStoreQueue"
- "accountTypeWithAccountTypeIdentifier:"
- "accountsWithAccountType:"
- "acquireWithError:"
- "actionClient"
- "actionCompletionBlock"
- "activateWithCompletion:"
- "activeContextCount"
- "activeContexts"
- "activeDevices"
- "activeSubscriptionsDidChange"
- "addDelegate:queue:"
- "addDevice:"
- "addEntriesFromDictionary:"
- "addIndex:"
- "addNotificationRequest:withCompletionHandler:"
- "addObject:"
- "addObserver:selector:name:object:"
- "addSelectorKey:"
- "addTranscriptionFromOtherContactPath:"
- "addTranslatedTranscriptionFromOtherContactPath:original:"
- "addUtterance:"
- "additionalInfoForPrefenceUpdate"
- "afterDelay:processBlock:"
- "allKeys"
- "allObjects"
- "allValues"
- "allVoiceContexts"
- "answerRTTCallAsMutedForCall:"
- "answerRTTCallsAsMuted"
- "answerRTTCallsAsMutedForContext:"
- "appendCharacter:"
- "appendString:"
- "appendStringFromOtherContactPath:"
- "archivedDataWithRootObject:requiringSecureCoding:error:"
- "areKeysAvailable:"
- "array"
- "arrayByAddingObject:"
- "arrayWithArray:"
- "arrayWithObjects:count:"
- "assertionInCallService"
- "attributeForKey:"
- "attributeWithDomain:name:"
- "attributes"
- "audioSessionWasInterrupted:"
- "authorizationStatus"
- "autorelease"
- "availableDictionaries"
- "ax_filteredArrayUsingBlock:"
- "ax_firstObjectUsingBlock:"
- "ax_removeObjectsFromArrayUsingBlock:"
- "backgroundAccessQueue"
- "bestTranscription"
- "boolForKey:"
- "boolValue"
- "boolValueForKey:andContext:withDefaultValue:"
- "boolValueForKey:withDefaultValue:"
- "bundleForClass:"
- "bundleIdentifier"
- "bundleURL"
- "cachedActiveContexts"
- "cachedSubscriptionContexts"
- "call"
- "callCapabilitiesSupportsTelephonyCalls"
- "callDidConnect:"
- "callDidReceiveText:forUtterance:"
- "callForUUID:"
- "callHistoryDBDidChange:"
- "callIdentifier"
- "callQueue"
- "callServicesClientCapabilities"
- "callStackSymbols"
- "callStatusDidChange:"
- "callUID"
- "callUUID"
- "callWithCallUUID:"
- "cancel"
- "cancelCallPromptDisplay"
- "cancelDownload:"
- "cannedResponses"
- "carrierSettingsDidChange"
- "categoryWithIdentifier:actions:intentIdentifiers:options:"
- "characterAtIndex:"
- "characterIsMember:"
- "class"
- "cleanup"
- "clearAllServerSettingsCache"
- "clearServerSettingsCacheForKey:"
- "client"
- "clientRemoved:"
- "cloudKitContainer"
- "commonPrefixWithString:options:"
- "compare:"
- "componentsJoinedByString:"
- "componentsSeparatedByCharactersInSet:"
- "conformsToProtocol:"
- "connectionWithServiceWasInterruptedForUserInterfaceClient:"
- "contactForPhoneNumber:"
- "contactID"
- "contactIDIsTTYContact:"
- "contactIsTTYContact:"
- "contactPath"
- "contactPathForCall:"
- "contactPathIsMe:"
- "contactPathWasUsedForTTY:"
- "contactStore"
- "containerIdentifier"
- "containsObject:"
- "content"
- "context"
- "context:getCarrierBundleValue:error:"
- "contextForCall:"
- "continuityEmergencyRTTIsSupported"
- "continuityRTTIsSupported"
- "controlFlags"
- "conversation"
- "conversationForCallUID:"
- "conversationWithCall:"
- "conversationWithCall:withCallback:"
- "conversationWithCallUID:withCallback:"
- "conversationWithID:andUtterances:"
- "copy"
- "copyWithZone:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "currentCallUUID"
- "currentCalls"
- "currentLocale"
- "currentPreferredTransportMethod"
- "currentPreferredTransportMethodForContext:"
- "currentProcessHandlesCloudRelay"
- "currentProcessIsHeard"
- "currentProcessIsInCallService"
- "currentProcessIsPreferences"
- "currentProcessIsRTTExternsion"
- "currentSupportedTextingType"
- "currentTranscription"
- "d16@0:8"
- "data"
- "date"
- "dateByAddingTimeInterval:"
- "dealloc"
- "debugDescription"
- "decimalDigitCharacterSet"
- "decodeBoolForKey:"
- "decodeObjectOfClass:forKey:"
- "decodeObjectOfClasses:forKey:"
- "defaultCenter"
- "defaultStore"
- "defaultVoiceContext"
- "delegate"
- "deleteConversationWithCallUID:"
- "deleteConversationsWithCallUIDs:"
- "deleteIfNeeded"
- "deleteObject:"
- "deliveredNotifications"
- "description"
- "descriptorForRequiredKeysForStyle:"
- "device:didReceiveCharacter:"
- "device:didReceiveText:"
- "device:didStart:error:"
- "deviceDidStop:"
- "deviceIsPad"
- "deviceIsPhone"
- "deviceIsPod"
- "deviceIsTinker"
- "dialRequestForRedial"
- "dictionary"
- "dictionaryForKey:"
- "dictionaryWithDictionary:"
- "dictionaryWithObjects:forKeys:count:"
- "didAddCapabilitiesForSenderIdentityWithUUID:"
- "didChangeCloudCallingDevices"
- "didChangeEmergencyCallbackMode"
- "didChangeEmergencyCallbackPossible"
- "didChangeFaceTimeAudioCallingSupport"
- "didChangeFaceTimeCallingAvailability"
- "didChangeFaceTimeVideoCallingSupport"
- "didChangeOutgoingRelayCallerID"
- "didChangeRelayCallingAvailability"
- "didChangeRelayCallingCapabilities"
- "didChangeRelayCallingFeatures"
- "didChangeTelephonyCallingSupport"
- "didChangeThumperCallingCapabilitiesForSenderIdentityWithUUID:"
- "didChangeThumperCallingProvisionalURLForSenderIdentityWithUUID:"
- "didChangeVoLTECallingCapabilitiesForSenderIdentityWithUUID:"
- "didChangeWiFiCallingCapabilitiesForSenderIdentityWithUUID:"
- "didChangeWiFiCallingProvisionalURLForSenderIdentityWithUUID:"
- "didRemoveCapabilitiesForSenderIdentityWithUUID:"
- "discoveryClient"
- "dismissRTTFirstUseAlert"
- "displayCallPrompt:"
- "displayCallPromptForContact:withCompletion:"
- "displayName"
- "displayRTTDowngradeAlert"
- "displayRTTFirstUseAlert"
- "domainAccessor"
- "downloadIfNeeded"
- "dualSimCapabilityDidChange"
- "emergencyRelayRTTIsSupported"
- "encodeBool:forKey:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "encodedData"
- "enumerateKeysAndObjectsUsingBlock:"
- "enumerateObjectsUsingBlock:"
- "enumerateObjectsWithOptions:usingBlock:"
- "executeFetchRequest:error:"
- "faceTimeShowInCallUIURL"
- "fetchRequestWithEntityName:"
- "findConversationForCallUID:andResult:"
- "finishEncoding"
- "firstObject"
- "focusedApps"
- "formatMessage:withType:isMe:"
- "formattedRepresentation"
- "formattedString"
- "getActiveContexts:"
- "getCarrierValueForKey:andContext:"
- "getCarrierValueForKeyHierarchy:andContext:"
- "getNotificationSettingsWithCompletionHandler:"
- "getPhoneNumber:error:"
- "getSimLabel:error:"
- "getSubscriptionInfoWithError:"
- "getUserDefaultVoiceSubscriptionContext:"
- "globalDomainAccessor"
- "handle"
- "handleDatabaseRequest:"
- "handleDictionaryRequest:"
- "handleIncomingNotificationSuppressionChange:"
- "handleMediaAction:"
- "handleMessageError:destructive:"
- "handleMessageWithPayload:forIdentifier:"
- "handleRTTControllerIsVisible:"
- "handleRTTMessageInjection:"
- "handleRTTTranslationLocaleMessage:"
- "handleRTTVoicemailMessage:"
- "handleSettingsRequest:"
- "handleUpdatedCalls:"
- "hardwareTTYIsSupported"
- "hardwareTTYIsSupportedForContext:"
- "hasPrefix:"
- "hasReceivedRTTCall"
- "hasTimedOut"
- "hasTranslation"
- "hash"
- "headphoneJackSupportsTTY"
- "headphoneStateChangedNotification:"
- "iCloudAccountDidChange:"
- "iCloudRTTRelayDidChange:"
- "identifier"
- "idsDeviceIdentifier"
- "ignoreTimeoutTemporarily"
- "incomingCallsTTY"
- "incomingCallsTTYForContext:"
- "indexOfObject:"
- "indexOfObjectPassingTest:"
- "indexOfObjectWithOptions:passingTest:"
- "indexSet"
- "indexesOfObjectsPassingTest:"
- "init"
- "initForReadingFromData:error:"
- "initRequiringSecureCoding:"
- "initWithBundleIdentifier:"
- "initWithCall:"
- "initWithCoder:"
- "initWithConfiguration:"
- "initWithDelegate:"
- "initWithDomain:"
- "initWithExplanation:target:attributes:"
- "initWithIdentifier:serviceBundleName:"
- "initWithListenerAddress:"
- "initWithLocale:"
- "initWithMode:error:"
- "initWithObjectsAndKeys:"
- "initWithQueue:"
- "initWithRootObject:"
- "initWithServiceUpdateType:options:"
- "initWithSourceLocale:targetLocale:"
- "initWithStreamToken:error:"
- "initWithString:"
- "initWithTargetSerialQueue:"
- "initWithType:"
- "initWithURL:"
- "initWithURL:withExtensionType:"
- "initWithUUIDString:"
- "initialize"
- "insertNewObjectForEntityForName:inManagedObjectContext:"
- "intValue"
- "integerValue"
- "integerValueForKey:withDefaultValue:"
- "internalOverrideTTYAvailability"
- "invalidate"
- "invalidateServerCaches:"
- "invert"
- "invertedSet"
- "isComplete"
- "isDirectTelephonyCallingCurrentlyAvailable"
- "isEmergency"
- "isEmergencyNumber:"
- "isEmergencyNumberForDigits:senderIdentityUUID:"
- "isEmergencyRTTSupported"
- "isEmergencyRTTSupportedByCarrierBundle"
- "isEmergencyRTTSupportedForContext:"
- "isEmergencyRTTSupportedForContext:excludeRelay:"
- "isEmergencyRelayRTTSupported"
- "isEndpointOnCurrentDevice"
- "isEqual:"
- "isEqualToConversation:"
- "isEqualToNumber:"
- "isEqualToString:"
- "isFinal"
- "isHostedOnCurrentDevice"
- "isIncoming"
- "isInternalInstall"
- "isKindOfClass:"
- "isLocallyHosted"
- "isMainThread"
- "isMe"
- "isMemberOfClass:"
- "isOnlyRTTSupported"
- "isOnlyRTTSupportedForContext:"
- "isPresent"
- "isProxy"
- "isRTTCallHoldSupportedForContext:"
- "isRTTSupported"
- "isRTTSupportedByCarrierBundle"
- "isRTTSupportedForContext:"
- "isRTTSupportedForContext:excludeRelay:"
- "isRelayCallingEnabled"
- "isRelayRTTSupported"
- "isScreening"
- "isTTY"
- "isTTYOverIMSSupportedForContext:"
- "isTTYOverIMSSupportedForContext:excludeRelay:"
- "isTTYSupported"
- "isTTYSupportedForContext:"
- "isThumperCallingEnabled"
- "isTranscription"
- "isUsingBaseband"
- "isValid"
- "isViewControllerVisible"
- "isVisibleSent"
- "isoCountryCode"
- "keysOfEntriesPassingTest:"
- "labelFromUUID:"
- "languageCode"
- "lastChangeDate"
- "lastDBVacuum"
- "lastObject"
- "lastUtteranceForMe:"
- "lastUtteranceForMe:isTranscription:"
- "lastUtteranceForMe:withText:"
- "lastUtteranceIndexForMe:isTranscription:"
- "length"
- "listenForCloudRelayChanges"
- "liveCaptionsService"
- "localSenderIdentityUUID"
- "localeIdentifier"
- "localeWithLocaleIdentifier:"
- "localizedStringForKey:value:table:"
- "lock"
- "logMessage:"
- "managedObjectContext"
- "managedObjectModelName"
- "mediaServerDied"
- "mergeUtterancesIfPossible"
- "messagePayloadFromDictionary:andIdentifier:"
- "messageWithPayload:"
- "messagingClients"
- "migrateSettings"
- "myPhoneNumber"
- "nanoSynchronizeQueue"
- "needsCloudKitUpload"
- "newRapportClientWithDestinationDevice:"
- "normalizedPhoneNumberHandleForValue:isoCountryCode:"
- "normalizedValue"
- "not processing initial text because it looks like garbage: %@"
- "notificationForSelector:"
- "null"
- "number"
- "numberWithBool:"
- "numberWithDouble:"
- "numberWithInt:"
- "numberWithInteger:"
- "numberWithUnsignedInteger:"
- "numberWithUnsignedLongLong:"
- "object"
- "objectAtIndex:"
- "objectAtIndexedSubscript:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "objectValueForKey:andContext:withClass:andDefaultValue:"
- "objectValueForKey:withClass:andDefaultValue:"
- "optionValueForKey:"
- "otherContactPath"
- "outgoingRelayCallerID"
- "pairedCallDevice"
- "payload"
- "performBlockAndWait:"
- "performCallCenterTask:"
- "performCallCenterTask:callCenter:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:afterDelay:"
- "performSelector:withObject:withObject:"
- "phoneNumberForContext:"
- "phoneNumberFromUUID:"
- "phoneNumberInfoCache"
- "phoneNumberWithDigits:countryCode:"
- "phoneNumberWithStringValue:"
- "phoneNumbers"
- "postNotificationName:object:"
- "predicateForContactsMatchingPhoneNumber:"
- "predicateForContactsWithIdentifiers:"
- "predicateWithFormat:"
- "preferredRelayNumber"
- "preferredRelayNumberForContext:"
- "primeRTTServer"
- "prioritizedSenderIdentities"
- "processBackspaceForMe:"
- "providerContext"
- "provisioningStatus"
- "purgePhoneNumberInfoCache"
- "purgeWithError:"
- "q16@0:8"
- "q32@0:8@16q24"
- "queryMetaDataSync"
- "queue"
- "rangeOfComposedCharacterSequenceAtIndex:"
- "rapportClientForDevice:"
- "recentCallsWithPredicate:"
- "recognitionTaskWithRequest:resultHandler:"
- "recreateTTYDevice:"
- "regionCode"
- "registerForRemoteUpdates:forCallUID:"
- "registerForServiceUpdates:forCallUID:"
- "registerForUpdates:forCallUID:"
- "registerForUpdatesWithTranslation:forCallUID:"
- "registerNotifications"
- "registerRequestID:options:handler:"
- "registerResponseBlock:forUUID:"
- "registerUpdateBlock:forRetrieveSelector:withListener:"
- "registeredNotifications"
- "relayIsSupported"
- "relayIsSupportedForContext:"
- "relayNumberForContext:"
- "relayPhoneNumber"
- "relayPhoneNumberForContext:"
- "relayRTTIsSupported"
- "release"
- "reloadDefaultVoiceContext"
- "reloadRelayPhoneNumbers"
- "removeAllObjects"
- "removeDeliveredNotificationsWithIdentifiers:"
- "removeDevice:"
- "removeObject:"
- "removeObjectForKey:"
- "removeObjectsAtIndexes:"
- "removeObjectsForKeys:"
- "removeObserver:"
- "replyMessageWithPayload:"
- "request"
- "requestAuthorizationWithOptions:completionHandler:"
- "requestWithIdentifier:content:trigger:"
- "resetCannedResponses"
- "resetCloudSupportStore"
- "resetConnection"
- "resetRapportClientForDevice:invalidate:"
- "resetTimeout"
- "respondsToSelector:"
- "responseForRequest:options:"
- "responseFromCallWithID:forRequest:options:"
- "resultType"
- "resultTypeFinal"
- "results"
- "retain"
- "retainCount"
- "rootObject"
- "rttCallHoldEnabled"
- "rttCalls"
- "rttInlineAbbreviationBarEnabled"
- "rttLiveTranscriptionsEnabled"
- "rttLiveTranscriptionsEnabledForContext:"
- "rttLiveTranscriptionsFeatureFlagEnabled"
- "safeStringForKey:"
- "save"
- "saveConversation:"
- "saveIfPossible"
- "saveTranscribedTextForConversation:isNew:"
- "saveTranslatedTranscribedTextForConversation:translatedText:isNew:"
- "selectorForPreferenceKey:"
- "self"
- "sendAsynchronousMessage:withIdentifier:targetAccessQueue:completion:"
- "sendCallIDChallengeToDevice:"
- "sendCallIDChallengeToDeviceId:orAlternateId:"
- "sendCharacter:"
- "sendConversationUpdate:"
- "sendMessage:errorBlock:"
- "sendMessageWithPayload:andIdentifier:"
- "sendRequestID:request:options:responseHandler:"
- "sendString:"
- "sendString:forCallUID:"
- "sendText:"
- "sendToTTYDeviceWithString:"
- "sendTranscription:forCallUUID:isNew:"
- "sendUpdateMessage:forIdentifier:"
- "server"
- "serverInvalidateCallback"
- "serviceUpdateType"
- "set"
- "setAccountStoreQueue:"
- "setActionCompletionBlock:"
- "setActiveContextCount:"
- "setAddsPunctuation:"
- "setAllVoiceContexts:"
- "setAllowsCellularAccess:"
- "setAnswerRTTCallsAsMuted:"
- "setAnswerRTTCallsAsMuted:forContext:"
- "setAssertionInCallService:"
- "setAttribute:forKey:error:"
- "setAudioSessionProperties:"
- "setAutomaticallyCancelPendingBlockUponSchedulingNewBlock:"
- "setAvailableDictionaries:"
- "setBody:"
- "setBool:forKey:"
- "setCachedActiveContexts:"
- "setCachedSubscriptionContexts:"
- "setCall:"
- "setCallCapabilitiesSupportsTelephonyCalls:"
- "setCallIdentifier:"
- "setCallUID:"
- "setCannedResponses:"
- "setCategoryIdentifier:"
- "setCompletionHandler:"
- "setContactID:"
- "setContactPath:"
- "setContactStore:"
- "setContinuityEmergencyRTTIsSupported:"
- "setContinuityRTTIsSupported:"
- "setControlFlags:"
- "setConversation:"
- "setCurrentCallUUID:"
- "setCurrentTranscription:"
- "setData:"
- "setDefaultActionURL:"
- "setDefaultVoiceContext:"
- "setDelegate:"
- "setDestinationDevice:"
- "setDeviceFoundHandler:"
- "setDeviceLostHandler:"
- "setDiscoveryClient:"
- "setDiscretionary:"
- "setDispatchQueue:"
- "setDomainAccessor:"
- "setExpirationDate:"
- "setGlobalDomainAccessor:"
- "setHasReceivedRTTCall:"
- "setHeadphoneJackSupportsTTY:"
- "setIgnoreTimeoutTemporarily:"
- "setIncomingCallsTTY:"
- "setIncomingCallsTTY:forContext:"
- "setIncomingTTYCallCount:"
- "setInternalOverrideTTYAvailability:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setIsMe:"
- "setIsRelayCallingEnabled:"
- "setIsTranscription:"
- "setIsViewControllerVisible:"
- "setIsVisibleSent:"
- "setLastCallCountReset:"
- "setLastChangeDate:"
- "setLastDBVacuum:"
- "setLiveCaptionsService:"
- "setMessagingClients:"
- "setNanoSynchronizeQueue:"
- "setNeedsCloudKitUpload:"
- "setNotificationCategories:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "setOptions:"
- "setOutgoingTTYCallCount:"
- "setPairedCallDevice:"
- "setPhoneNumberInfoCache:"
- "setPredicate:"
- "setPreferredRelayNumber:"
- "setPreferredRelayNumber:forContext:"
- "setRTTLiveTranscriptionsEnabled:forContext:"
- "setRegisteredNotifications:"
- "setReturnsObjectsAsFaults:"
- "setRttCalls:"
- "setRttInlineAbbreviationBarEnabled:"
- "setServerInvalidateCallback:"
- "setServiceUpdateType:"
- "setSettingsVersion:"
- "setShouldAuthenticateDefaultAction:"
- "setShouldReportPartialResults:"
- "setShouldSuppressDefaultAction:"
- "setShouldSuppressIncomingNotification:"
- "setShowsRTTNotifications:forContext:"
- "setSubstitutions:"
- "setSupportsRelayCalling:"
- "setSynchronizePreferences:"
- "setSystemOutputAudioMuted:withCallID:"
- "setTTYDictionaryAvailability:"
- "setTTYHardwareEnabled:"
- "setTTYHardwareEnabled:forContext:"
- "setTTYShouldBeRealtime:forContext:"
- "setTTYSoftwareEnabled:"
- "setTTYSoftwareEnabled:forContext:"
- "setTaskHint:"
- "setTelephonyClient:"
- "setTelephonyUpdateQueue:"
- "setTestUuid:"
- "setText:"
- "setThreadIdentifier:"
- "setTitle:"
- "setTranscriber:"
- "setTranslatedText:"
- "setTranslationLocales:"
- "setTranslationLocalesWithLocal:remote:"
- "setTranslator:"
- "setTtyDevice:"
- "setTtyShouldBeRealtime:"
- "setUpdateBlocks:"
- "setUplinkMuted:"
- "setUserInfo:"
- "setUtterances:"
- "setValue:forKey:"
- "setVersion:"
- "setViewControllerIsVisible:withCallID:"
- "setWantsToScreenCalls:"
- "setWantsUpdates:forIdentifier:"
- "setWithArray:"
- "setWithObject:"
- "setWithObjects:"
- "settingsVersion"
- "shared"
- "sharedAVSystemController"
- "sharedCallCenter"
- "sharedController"
- "sharedInstance"
- "sharedManager"
- "sharedUtilityProvider"
- "shouldMigrateSettings"
- "shouldRestartOnInterruption:"
- "shouldSuppressIncomingNotification"
- "shouldUseRTT"
- "shouldUseRTTForContext:"
- "showsRTTNotifications"
- "showsRTTNotificationsForContext:"
- "simLessSubscriptionsDidChange"
- "slotID"
- "softwareTTYIsSupported"
- "softwareTTYIsSupportedForContext:"
- "sortedArrayUsingComparator:"
- "sourceLocale"
- "sourceTypeDownlink"
- "spaceCheck:"
- "standardUserDefaults"
- "start"
- "startAudioSession"
- "startDownload:completionWithError:"
- "startTranscribing:targetPID:callbackBlock:error:"
- "startTranscribingForCallUUID:"
- "startTranscribingV2ForCallUUID:"
- "startWithSource:locale:sharedRoute:excludePIDs:error:transcriptionResult:"
- "state"
- "status"
- "stop"
- "stop:error:"
- "stopAudioSession"
- "stopTranscribing:targetPID:error:"
- "stopTranscribingForCallUUID:"
- "stopTranscribingV2ForCallUUID:"
- "string"
- "stringByAppendingString:"
- "stringByReplacingCharactersInRange:withString:"
- "stringByReplacingOccurrencesOfString:withString:"
- "stringByTrimmingCharactersInSet:"
- "stringFromContact:style:"
- "stringValue"
- "stringWithCharacters:length:"
- "stringWithFormat:"
- "stringWithUTF8String:"
- "subscriptionContexts"
- "subscriptionInfoDidChange"
- "subscriptions"
- "substitutions"
- "substringFromIndex:"
- "substringWithRange:"
- "superclass"
- "supportsPrimaryCalling"
- "supportsRelayCalling"
- "supportsSecureCoding"
- "supportsTTYWithVoice"
- "supportsTelephonyCalls"
- "supportsTelephonyRelayCalling"
- "synchronize"
- "synchronizeNanoDomain:keys:"
- "synchronizePreferences"
- "targetLocale"
- "targetWithPid:"
- "telephonyClient"
- "telephonyProvider"
- "telephonyUpdateQueue"
- "terminateConnectionAndNotify:"
- "testUuid"
- "text"
- "threadIdentifier"
- "thumperCallingCapabilityInfo"
- "timeIntervalSinceDate:"
- "toggleSystemOutputMute:"
- "transcribedText"
- "transcriber"
- "transcriptionDidStart:forCallUUID:"
- "transcriptionDidUpdate:forCallUUID:"
- "translate:"
- "translatedText"
- "translationLocales"
- "translator"
- "ttyCall:didReceiveString:forUtterance:"
- "ttyCall:didSendRemoteString:forUtterance:"
- "ttyCall:didUpdateTranslation:forUtterance:"
- "ttyCall:setVisible:serviceUpdate:"
- "ttyDevice"
- "ttyIMSSupported"
- "ttyIsMe"
- "ttyMeContact"
- "ttyShouldBeRealtime"
- "ttyShouldBeRealtimeForContext:"
- "ttyType"
- "unarchivedObjectOfClass:fromData:error:"
- "unformattedInternationalRepresentation"
- "unifiedContactsMatchingPredicate:keysToFetch:error:"
- "unlock"
- "unsignedIntegerValue"
- "updateBlocks"
- "updateCallWithRemoteFailure"
- "updateGizmoValueIfNeeded:forPreferenceKey:"
- "updateHeadphoneState"
- "updateText:"
- "updateTranscriptionFromOtherContactPath:"
- "updateTranslatedTranscriptionFromOtherContactPath:original:"
- "updateTranslation:"
- "userInfo"
- "userInterfaceClient:accessQueueForProcessingMessageWithIdentifier:"
- "userInterfaceClient:messageFromServerForWithIdentifierShouldBeProcessedAsynchronously:"
- "userInterfaceClient:messageWithIdentifierRequiresWritingBlock:"
- "userInterfaceClient:processMessageFromServer:withIdentifier:error:"
- "userInterfaceClient:processMessageFromServerAsynchronously:withIdentifier:completion:"
- "userInterfaceClient:willActivateUserInterfaceServiceWithInitializationMessage:"
- "utteranceCountForMe:"
- "utteranceWithContactPath:andText:"
- "utteranceWithContactPath:andText:isTranscription:"
- "utteranceWithContactPath:andText:translatedText:isTranscription:"
- "utterances"
- "uuid"
- "uuidFromContext:"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8:16"
- "v24@0:8@\"AVCVirtualTTYDevice\"16"
- "v24@0:8@\"AXUIClient\"16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@\"NSUUID\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8Q16"
- "v24@0:8d16"
- "v24@0:8q16"
- "v28@0:8@\"AVCVirtualTTYDevice\"16S24"
- "v28@0:8@16B24"
- "v28@0:8@16S24"
- "v28@0:8B16@20"
- "v32@0:8@\"AVCVirtualTTYDevice\"16@\"NSString\"24"
- "v32@0:8@\"AXUIClient\"16@\"NSMutableDictionary\"24"
- "v32@0:8@\"NSString\"16@\"NSString\"24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v32@0:8@16Q24"
- "v32@0:8@?16@24"
- "v36@0:8@\"AVCVirtualTTYDevice\"16B24@\"NSError\"28"
- "v36@0:8@\"RTTCall\"16B24@\"NSString\"28"
- "v36@0:8@16@24B32"
- "v36@0:8@16B24@28"
- "v40@0:8@\"RTTCall\"16@\"NSString\"24@\"NSString\"32"
- "v40@0:8@16@24@32"
- "v40@0:8@16q24@32"
- "v40@0:8@?16:24@32"
- "v48@0:8@\"AXUIClient\"16@\"NSDictionary\"24Q32@?<v@?@\"NSDictionary\"@\"NSError\">40"
- "v48@0:8@16@24Q32@?40"
- "v48@0:8@16@24q32@40"
- "value"
- "valueForKey:"
- "valueForPreferenceKey:"
- "valueForPreferenceKey:andContext:"
- "valueForTTYSetting:"
- "version"
- "voicePreferred"
- "whitespaceAndNewlineCharacterSet"
- "whitespaceCharacterSet"
- "zone"

```
