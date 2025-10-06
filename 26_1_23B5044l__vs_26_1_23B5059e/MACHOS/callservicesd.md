## callservicesd

> `/System/Library/PrivateFrameworks/TelephonyUtilities.framework/callservicesd`

```diff

-1576.200.36.2.2
-  __TEXT.__text: 0x470580
-  __TEXT.__auth_stubs: 0x4b80
-  __TEXT.__objc_stubs: 0x34f20
-  __TEXT.__objc_methlist: 0x26c98
+1576.200.62.0.0
+  __TEXT.__text: 0x472f44
+  __TEXT.__auth_stubs: 0x4b70
+  __TEXT.__objc_stubs: 0x35060
+  __TEXT.__objc_methlist: 0x26cd0
   __TEXT.__objc_classname: 0x2db6
-  __TEXT.__objc_methname: 0x612f7
+  __TEXT.__objc_methname: 0x613fa
   __TEXT.__objc_methtype: 0x10811
-  __TEXT.__cstring: 0x2519d
-  __TEXT.__const: 0xd3e0
-  __TEXT.__oslogstring: 0x4b763
-  __TEXT.__gcc_except_tab: 0x2958
+  __TEXT.__cstring: 0x2554d
+  __TEXT.__const: 0xd3f0
+  __TEXT.__oslogstring: 0x4b9c3
+  __TEXT.__gcc_except_tab: 0x297c
   __TEXT.__ustring: 0x10
-  __TEXT.__swift5_typeref: 0x85a0
+  __TEXT.__swift5_typeref: 0x85f2
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__constg_swiftt: 0x9004
+  __TEXT.__constg_swiftt: 0x9054
   __TEXT.__swift5_builtin: 0x6cc
-  __TEXT.__swift5_reflstr: 0x7c13
-  __TEXT.__swift5_fieldmd: 0x64c0
+  __TEXT.__swift5_reflstr: 0x7c83
+  __TEXT.__swift5_fieldmd: 0x64d8
   __TEXT.__swift5_assocty: 0x950
   __TEXT.__swift5_proto: 0x8b8
   __TEXT.__swift5_types: 0x658
-  __TEXT.__swift5_capture: 0x3654
+  __TEXT.__swift5_capture: 0x36d0
   __TEXT.__swift5_protos: 0x184
   __TEXT.__swift_as_entry: 0x214
   __TEXT.__swift_as_ret: 0x250
   __TEXT.__swift5_mpenum: 0x20
-  __TEXT.__unwind_info: 0xd648
-  __TEXT.__eh_frame: 0x8aa8
-  __DATA_CONST.__auth_got: 0x25d0
+  __TEXT.__unwind_info: 0xd690
+  __TEXT.__eh_frame: 0x8af4
+  __DATA_CONST.__auth_got: 0x25c8
   __DATA_CONST.__got: 0x2418
   __DATA_CONST.__auth_ptr: 0x1310
-  __DATA_CONST.__const: 0x17e30
-  __DATA_CONST.__cfstring: 0xade0
+  __DATA_CONST.__const: 0x17e80
+  __DATA_CONST.__cfstring: 0xae00
   __DATA_CONST.__objc_classlist: 0xc08
   __DATA_CONST.__objc_catlist: 0x140
   __DATA_CONST.__objc_protolist: 0xab8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x418
   __DATA_CONST.__objc_superrefs: 0x658
-  __DATA_CONST.__objc_intobj: 0x210
+  __DATA_CONST.__objc_intobj: 0x228
   __DATA_CONST.__objc_arraydata: 0x20
   __DATA_CONST.__objc_arrayobj: 0x48
-  __DATA.__objc_const: 0x3ba50
-  __DATA.__objc_selrefs: 0x12530
+  __DATA.__objc_const: 0x3ba80
+  __DATA.__objc_selrefs: 0x12560
   __DATA.__objc_ivar: 0x1dd8
-  __DATA.__objc_data: 0xd580
-  __DATA.__data: 0xf668
+  __DATA.__objc_data: 0xd5c0
+  __DATA.__data: 0xf6f8
   __DATA.__bss: 0xd600
-  __DATA.__common: 0x9e0
+  __DATA.__common: 0x9e8
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 11974909-6078-3651-AAAE-DEAB7180BDF8
-  Functions: 23883
-  Symbols:   2600
-  CStrings:  25052
+  UUID: 2D0AED30-B248-3B1A-B535-06A594764970
+  Functions: 23918
+  Symbols:   2599
+  CStrings:  25083
 
Symbols:
+ _$s20FaceTimeMessageStore12BadgeManagerC5types8defaults13deviceSupport12featureFlags5queueACSayAA0E13CountCategoryOGSg_So14NSUserDefaultsCSgSo08FTDeviceJ0CSgSo09TUFeatureL0_pSgSo012OS_dispatch_M7_serialCSgtcfC
- _$s20FaceTimeMessageStore12BadgeManagerC5types8defaults13deviceSupport12featureFlags5queueACSayAA0E13CountCategoryOGSg_So14NSUserDefaultsCSgSo08FTDeviceJ0CSgSo09TUFeatureL0_pSgSo012OS_dispatch_M0CSgtcfC
- _objc_retain_x10
CStrings:
+ "%@ Assistive Access allows calls to All Contacts. Is in contacts: %i"
+ "%@ Assistive Access allows calls to Everyone. Not blocking call."
+ "%@ Assistive Access allows calls to Selected Contacts. Is in Selected Contacts: %i"
+ "%@ Assistive Access has unhandled outgoing communication limit. Not blocking call."
+ "%@ Blocking call because no Calls app is available in Assistive Access."
+ "%@ Not blocking call for Assistive Access because it was neither telephony nor FaceTime."
+ "-[CSDCallStateController isRestrictedExclusivelyByScreenTime:forBundleIdentifier:performSynchronously:reply:]"
+ "Call has already been returned, not reporting it"
+ "Failed to export concatenated audio file %{public}s"
+ "Failed to remove audio file at URL %s"
+ "Found %lu calls matching search predicate for returning silenced IMAV"
+ "Found recent IMAV calls for handle that has not been returned %@"
+ "Logged incoming IMAV call with silenced: %s"
+ "Logged outgoing call replying to silenced IMAV call"
+ "No recent unreturned silenced IMAV calls found for handle %@ in the last 24 hours"
+ "Sending audio files to be concatenated"
+ "[WARN] handlePushHostedCallsMessageFromHost: isScreening: %@, receptionistState: %d, isAnswerFromScreening: %@"
+ "_afterFirstUnlock"
+ "_checkAndSendReturningSilencedIMAVAnalytic:"
+ "_greetingsDict"
+ "_phoneNumberToAccountUUIDMap"
+ "_screenWithRequest:"
+ "callSourceUpdated-%{public}@"
+ "callerInfoAudioURLs"
+ "com.apple.callservicesd.incoming-imav-call"
+ "com.apple.callservicesd.silenced-IMAV-reply"
+ "initWithProtoVersion:remotePhoneNumber:holdDuration:holdAssistMLClassification:holdAssistRecommendation:holdAssistObservation:remotePhoneNumberCountryCode:"
+ "isRestrictedExclusivelyByScreenTime:forBundleIdentifier:performSynchronously:"
+ "isRestrictedExclusivelyByScreenTime:forBundleIdentifier:performSynchronously:reply:"
+ "predicateForCallsWithFilteredOutReason:"
+ "remotePhoneNumberCountryCode"
+ "returnedIMAVCalls"
+ "screeningStarted(for:with:)"
+ "sendIncomingIMAVCallEventWithSilenced:"
+ "sendReplyingToIMAVCallEvent"
+ "setShouldSilentlyRegisterIMAVCall:"
+ "shouldSilentlyRegisterIMAVCall"
+ "voicemailAudioURLs"
- "Received protected add incoming call request from call source %@ with UUID %@ update %@"
- "afterFirstUnlock"
- "callEndSpamUIEnhancementEnabled"
- "callSource:reportedNewIncomingProtectedIMAVCallWithUUID:update:completion:"
- "callerInfoAudio"
- "greetingsDict"
- "initWithProtoVersion:remotePhoneNumber:holdDuration:holdAssistMLClassification:holdAssistRecommendation:holdAssistObservation:"
- "phoneNumberToAccountUUIDMap"
- "reportNewIncomingProtectedIMAVCallWithUUID:update:completion:"
- "screeningStarted(for:)"

```
