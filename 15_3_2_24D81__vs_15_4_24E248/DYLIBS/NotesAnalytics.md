## NotesAnalytics

> `/System/Library/PrivateFrameworks/NotesAnalytics.framework/Versions/A/NotesAnalytics`

```diff

-2994.3.0.0.0
-  __TEXT.__text: 0x63ecc
+2998.23.0.0.0
+  __TEXT.__text: 0x645e4
   __TEXT.__auth_stubs: 0x520
-  __TEXT.__objc_methlist: 0xa338
+  __TEXT.__objc_methlist: 0xa68c
   __TEXT.__const: 0x148
-  __TEXT.__cstring: 0x6b50
-  __TEXT.__gcc_except_tab: 0xb9c
-  __TEXT.__oslogstring: 0xb10
+  __TEXT.__cstring: 0x6b75
+  __TEXT.__gcc_except_tab: 0xba8
+  __TEXT.__oslogstring: 0xc25
   __TEXT.__dlopen_cstrs: 0x66
-  __TEXT.__unwind_info: 0x1dc0
-  __TEXT.__objc_classname: 0x25cb
-  __TEXT.__objc_methname: 0x1b6a8
-  __TEXT.__objc_methtype: 0x1b54
-  __TEXT.__objc_stubs: 0xbc00
+  __TEXT.__unwind_info: 0x1dc8
+  __TEXT.__objc_classname: 0x25cd
+  __TEXT.__objc_methname: 0x1b766
+  __TEXT.__objc_methtype: 0x1b46
+  __TEXT.__objc_stubs: 0xbc60
   __DATA_CONST.__got: 0xd28
-  __DATA_CONST.__const: 0xa30
+  __DATA_CONST.__const: 0xa50
   __DATA_CONST.__objc_classlist: 0xba0
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3720
+  __DATA_CONST.__objc_selrefs: 0x3828
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x7b0
   __DATA_CONST.__objc_arraydata: 0x2410
   __AUTH_CONST.__auth_got: 0x2a0
-  __AUTH_CONST.__const: 0xc30
+  __AUTH_CONST.__const: 0xbf0
   __AUTH_CONST.__cfstring: 0x9ba0
-  __AUTH_CONST.__objc_const: 0x1e710
+  __AUTH_CONST.__objc_const: 0x1e188
   __AUTH_CONST.__objc_intobj: 0x5cd0
   __AUTH_CONST.__objc_arrayobj: 0x318
   __AUTH_CONST.__objc_doubleobj: 0xa60
   __AUTH.__objc_data: 0x7440
-  __DATA.__objc_ivar: 0xd80
+  __DATA.__objc_ivar: 0xd84
   __DATA.__data: 0x2a0
   __DATA.__bss: 0xe0
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts

   - /System/Library/PrivateFrameworks/UserManagement.framework/Versions/A/UserManagement
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4B63E81A-6AD6-3FCD-B515-57482EB95F6E
-  Functions: 3212
-  Symbols:   9282
-  CStrings:  6497
+  UUID: 35C4051B-5B30-3E20-BBD6-7F4677C1C857
+  Functions: 3230
+  Symbols:   9309
+  CStrings:  6511
 
Symbols:
+ +[ICNAController osBundleVersion].cold.1
+ +[ICNAController osVersion].cold.1
+ +[ICNAController sharedController].cold.1
+ +[ICNACoreAnalyticsReporter analyticsQueue].cold.1
+ +[ICNACoreAnalyticsReporter sharedReporter].cold.1
+ +[ICNAEventReporter activityTypeHasUnknownShareFlow:].cold.1
+ +[ICNAIdentityManager sharedManager].cold.1
+ +[ICNAInlineDrawingRecognitionReporter sharedReporter].cold.1
+ +[ICNAReferringInboundURLFilter allowedTieredPrefixReplacements].cold.1
+ +[ICNASamplingController sharedController].cold.1
+ +[ICNASnapshotReporter sharedReporter].cold.1
+ -[ICNAController _immediatelySubmitEventOfType:pushThenPopDataObjects:subTracker:].cold.2
+ -[ICNAController _immediatelySubmitEventOfType:subTracker:].cold.2
+ -[ICNAController appSessionState]
+ -[ICNAController globalSessionState]
+ -[ICNAController setAppSessionState:]
+ -[ICNAController setGlobalSessionState:]
+ -[ICNAController startAppAndGlobalSessionIfNecessaryWithReferralURL:referralApplication:]
+ -[ICNAController startAppAndGlobalSessionIfNecessaryWithReferralURL:referralApplication:].cold.1
+ -[ICNAController startAppAndGlobalSessionIfNecessaryWithReferralURL:referralApplication:].cold.2
+ -[ICNAController startAppAndGlobalSessionIfNecessaryWithReferralURL:referralApplication:].cold.3
+ -[ICNAController startAppAndGlobalSessionIfNecessaryWithReferralURL:referralApplication:].cold.4
+ -[ICNAEventReporter audioRecordingDataForModernAttachment:appBackgroundOccurred:noteMultitaskingOccurred:audioAttachmentDuration:]
+ -[ICNAEventReporter submitAudioRecordingEventWithAttachment:appBackgroundOccurred:noteMultitaskingOccurred:audioAttachmentDuration:]
+ -[ICNAEventReporter submitAudioRecordingEventWithAttachment:appBackgroundOccurred:noteMultitaskingOccurred:audioAttachmentDuration:].cold.1
+ -[ICNASnapshotBackgroundTask handleTaskExpiration].cold.1
+ GCC_except_table138
+ GCC_except_table29
+ GCC_except_table47
+ GCC_except_table7
+ GCC_except_table95
+ OBJC_IVAR_$_ICNAController._appSessionState
+ OBJC_IVAR_$_ICNAController._globalSessionState
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_6
+ __35-[ICNAController restartAppSession]_block_invoke.87
+ __35-[ICNAController restartAppSession]_block_invoke_2.91
+ __36-[ICNAController accountTypeSummary]_block_invoke.163
+ __39-[ICNAController startSessionWithType:]_block_invoke.102
+ __52-[ICNAController startWindowSessionWithType:window:]_block_invoke.111
+ __52-[ICNASnapshotBackgroundTask runTaskWithCompletion:]_block_invoke.cold.1
+ __54-[ICNAEventReporter submitTimedEventOfTypeIfPossible:]_block_invoke.cold.1
+ __59-[ICNAController _immediatelySubmitEventOfType:subTracker:]_block_invoke.cold.1
+ __67-[ICNAController endSessionSynchronously:forSessionType:endReason:]_block_invoke.113
+ __67-[ICNAController endSessionSynchronously:forSessionType:endReason:]_block_invoke.120
+ __67-[ICNAController endSessionSynchronously:forSessionType:endReason:]_block_invoke.125
+ __67-[ICNAController endSessionSynchronously:forSessionType:endReason:]_block_invoke.126
+ __67-[ICNAController endSessionSynchronously:forSessionType:endReason:]_block_invoke.126.cold.1
+ __80-[ICNAController endWindowSessionSynchronously:forSessionType:endReason:window:]_block_invoke.130
+ __82-[ICNAController _immediatelySubmitEventOfType:pushThenPopDataObjects:subTracker:]_block_invoke.199.cold.1
+ __82-[ICNAController _immediatelySubmitEventOfType:pushThenPopDataObjects:subTracker:]_block_invoke.200
+ ___59-[ICNAController _immediatelySubmitEventOfType:subTracker:]_block_invoke
+ ___block_descriptor_40_e36_v24?0"AAProcessEvent"8"NSError"16lu32l8
+ __block_literal_global.218
+ __block_literal_global.220
+ __block_literal_global.334
+ __block_literal_global.93
+ _objc_msgSend$appSessionState
+ _objc_msgSend$audioRecordingDataForModernAttachment:appBackgroundOccurred:noteMultitaskingOccurred:audioAttachmentDuration:
+ _objc_msgSend$globalSessionState
+ _objc_msgSend$intValue
+ _objc_msgSend$setAppSessionState:
+ _objc_msgSend$setGlobalSessionState:
+ _objc_msgSend$startAppAndGlobalSessionIfNecessaryWithReferralURL:referralApplication:
+ _objc_msgSend$submitEventType:completion:
+ _objc_msgSend$supportsPrivateCloudComputeSummary
- -[ICNAController sessionState]
- -[ICNAController setSessionState:]
- -[ICNAEventReporter audioRecordingDataForModernAttachment:appBackgroundOccurred:noteMultitaskingOccurred:]
- -[ICNAEventReporter submitAudioRecordingEventWithAttachment:appBackgroundOccurred:noteMultitaksingOccurred:]
- -[ICNASnapshotBackgroundTask cleanupWithCompletion:]
- -[ICNASnapshotBackgroundTask startAnalyticsSessionWithReferralURL:referralApplication:]
- GCC_except_table134
- GCC_except_table44
- GCC_except_table58
- GCC_except_table92
- OBJC_IVAR_$_ICNAController._sessionState
- __35-[ICNAController restartAppSession]_block_invoke.91
- __35-[ICNAController restartAppSession]_block_invoke_2.93
- __36-[ICNAController accountTypeSummary]_block_invoke.165
- __39-[ICNAController startSessionWithType:]_block_invoke.104
- __50-[ICNASnapshotBackgroundTask handleTaskExpiration]_block_invoke.cold.1
- __52-[ICNAController startWindowSessionWithType:window:]_block_invoke.113
- __52-[ICNASnapshotBackgroundTask runTaskWithCompletion:]_block_invoke.18
- __52-[ICNASnapshotBackgroundTask runTaskWithCompletion:]_block_invoke_2.cold.1
- __67-[ICNAController endSessionSynchronously:forSessionType:endReason:]_block_invoke.115
- __67-[ICNAController endSessionSynchronously:forSessionType:endReason:]_block_invoke.122
- __67-[ICNAController endSessionSynchronously:forSessionType:endReason:]_block_invoke.128
- __67-[ICNAController endSessionSynchronously:forSessionType:endReason:]_block_invoke.128.cold.1
- __67-[ICNAController endSessionSynchronously:forSessionType:endReason:]_block_invoke.129
- __80-[ICNAController endWindowSessionSynchronously:forSessionType:endReason:window:]_block_invoke.132
- ___50-[ICNASnapshotBackgroundTask handleTaskExpiration]_block_invoke
- ___52-[ICNASnapshotBackgroundTask runTaskWithCompletion:]_block_invoke_2
- __block_literal_global.217
- __block_literal_global.219
- __block_literal_global.332
- __block_literal_global.88
- __block_literal_global.97
- _objc_msgSend$audioRecordingDataForModernAttachment:appBackgroundOccurred:noteMultitaskingOccurred:
- _objc_msgSend$cleanupWithCompletion:
- _objc_msgSend$sessionState
- _objc_msgSend$setSessionState:
- _objc_msgSend$startAnalyticsSessionWithReferralURL:referralApplication:
- _objc_msgSend$supportsGreymatter
CStrings:
+ "%@ is possible to submit: %d"
+ "/AppleInternal/Library/BuildRoots/656826c2-0194-11f0-9fc9-122ba06eff56/Library/Caches/com.apple.xbs/Sources/NotesFramework/NotesAnalytics/ICNAController.m"
+ "@40@0:8@16B24B28@32"
+ "App Session is active"
+ "App Session was inactive, now has been started"
+ "Attempting to submit AudioRecording event"
+ "Could not submit event: %@ due to %@"
+ "Global Session is active"
+ "Global Session was inactive, now has been started"
+ "Submitting %@ to tracker"
+ "Tq,V_appSessionState"
+ "Tq,V_globalSessionState"
+ "_appSessionState"
+ "_globalSessionState"
+ "`"
+ "appSessionState"
+ "audioRecordingDataForModernAttachment:appBackgroundOccurred:noteMultitaskingOccurred:audioAttachmentDuration:"
+ "globalSessionState"
+ "intValue"
+ "setAppSessionState:"
+ "setGlobalSessionState:"
+ "startAppAndGlobalSessionIfNecessaryWithReferralURL:referralApplication:"
+ "submitAudioRecordingEventWithAttachment:appBackgroundOccurred:noteMultitaskingOccurred:audioAttachmentDuration:"
+ "submitEventType:completion:"
+ "supportsPrivateCloudComputeSummary"
+ "v24@?0@\"AAProcessEvent\"8@\"NSError\"16"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/NotesFramework/NotesAnalytics/ICNAController.m"
- "@32@0:8@16B24B28"
- "Tq,V_sessionState"
- "_sessionState"
- "audioRecordingDataForModernAttachment:appBackgroundOccurred:noteMultitaskingOccurred:"
- "cleanupWithCompletion:"
- "sessionState"
- "setSessionState:"
- "startAnalyticsSessionWithReferralURL:referralApplication:"
- "submitAudioRecordingEventWithAttachment:appBackgroundOccurred:noteMultitaksingOccurred:"
- "supportsGreymatter"
- "v32@0:8@16B24B28"

```
