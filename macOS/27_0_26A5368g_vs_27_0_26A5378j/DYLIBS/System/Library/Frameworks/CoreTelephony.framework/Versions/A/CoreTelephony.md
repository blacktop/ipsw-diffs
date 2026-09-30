## CoreTelephony

> `/System/Library/Frameworks/CoreTelephony.framework/Versions/A/CoreTelephony`

```diff

-  __TEXT.__text: 0x16f36c
-  __TEXT.__objc_methlist: 0x16b14
-  __TEXT.__cstring: 0x1be28
-  __TEXT.__const: 0x15e8
-  __TEXT.__gcc_except_tab: 0x19aa0
-  __TEXT.__oslogstring: 0x44d6
+  __TEXT.__text: 0x170aec
+  __TEXT.__objc_methlist: 0x16ba4
+  __TEXT.__cstring: 0x1bed8
+  __TEXT.__const: 0x15d8
+  __TEXT.__gcc_except_tab: 0x19be8
+  __TEXT.__oslogstring: 0x4576
   __TEXT.__swift5_typeref: 0x259
   __TEXT.__constg_swiftt: 0x118
   __TEXT.__swift5_builtin: 0x3c

   __TEXT.__swift_as_entry: 0x10
   __TEXT.__swift_as_ret: 0x10
   __TEXT.__swift_as_cont: 0x30
-  __TEXT.__unwind_info: 0xc2f0
+  __TEXT.__unwind_info: 0xc310
   __TEXT.__eh_frame: 0x370
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x4ec0
-  __DATA_CONST.__objc_classlist: 0x1140
+  __DATA_CONST.__const: 0x4ef0
+  __DATA_CONST.__objc_classlist: 0x1130
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x258
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x69a8
+  __DATA_CONST.__objc_selrefs: 0x6a58
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0x1248
-  __DATA_CONST.__objc_arraydata: 0x20
-  __DATA_CONST.__got: 0x970
-  __AUTH_CONST.__const: 0x38f8
-  __AUTH_CONST.__cfstring: 0x19de0
-  __AUTH_CONST.__objc_const: 0x271d8
+  __DATA_CONST.__objc_superrefs: 0x1230
+  __DATA_CONST.__objc_arraydata: 0x30
+  __DATA_CONST.__got: 0x978
+  __AUTH_CONST.__const: 0x3938
+  __AUTH_CONST.__cfstring: 0x19f40
+  __AUTH_CONST.__objc_const: 0x27218
   __AUTH_CONST.__weak_auth_got: 0x28
-  __AUTH_CONST.__objc_arrayobj: 0x30
+  __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__auth_got: 0xd18
-  __AUTH.__objc_data: 0x8750
+  __AUTH.__objc_data: 0x87a0
   __AUTH.__data: 0xb0
-  __DATA.__objc_ivar: 0x102c
+  __DATA.__objc_ivar: 0x1048
   __DATA.__data: 0x2110
   __DATA.__bss: 0x730
   __DATA.__common: 0x10
-  __DATA_DIRTY.__objc_data: 0x24e0
+  __DATA_DIRTY.__objc_data: 0x23f0
   __DATA_DIRTY.__data: 0x90
-  __DATA_DIRTY.__bss: 0x12b0
+  __DATA_DIRTY.__bss: 0x12a0
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/Network.framework/Versions/A/Network

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 9656
-  Symbols:   23269
-  CStrings:  8654
+  Functions: 9683
+  Symbols:   23306
+  CStrings:  8682
 
Sections:
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__swift_as_entry : content changed
~ __TEXT.__swift_as_ret : content changed
~ __TEXT.__swift_as_cont : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __AUTH_CONST.__weak_auth_got : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH.__data : content changed
~ __DATA.__data : content changed
Symbols:
+ -[CTDeviceIdentifier IMEI1]
+ -[CTDeviceIdentifier IMEI2]
+ -[CTDeviceIdentifier NAL]
+ -[CTDeviceIdentifier initWithDeviceType:EID:IMEI:IMEI1:IMEI2:NAL:idsDeviceId:]
+ -[CTDeviceIdentifier setIMEI1:]
+ -[CTDeviceIdentifier setIMEI2:]
+ -[CTDeviceIdentifier setNAL:]
+ -[CTLazuliSuggestedActionOpenUrlInApplication schemeType]
+ -[CTLazuliSuggestedActionOpenUrlInApplication setSchemeType:]
+ -[CTLazuliSuggestedActionOpenUrlInWebView schemeType]
+ -[CTLazuliSuggestedActionOpenUrlInWebView setSchemeType:]
+ -[CTPNRRequestSentInfo requestID]
+ -[CTPNRRequestSentInfo setRequestID:]
+ -[CTPNRRequestType requestID]
+ -[CTPNRRequestType setRequestID:]
+ -[CTXPCUpdateQuickSwitchSignUpResult initWithPrimaryIccid:secondaryIccid:secondaryEid:secondaryImei:smdp:state:planIdentifier:error:]
+ -[CTXPCUpdateQuickSwitchSignUpResult planIdentifier]
+ -[CoreTelephonyClient(QuickSwitch) didSignUpQuickSwitchPlan:secondaryIccid:secondaryEid:secondaryImei:smdp:state:planIdentifier:completion:]
+ -[CoreTelephonyClient(Voicemail) clearVoicemailQuickSwitchDataLostStatusWithCompletion:]
+ -[CoreTelephonyClient(Voicemail) clearVoicemailQuickSwitchDataLostStatus]
+ -[CoreTelephonyClient(Voicemail) getVoicemailQuickSwitchData:]
+ -[CoreTelephonyClient(Voicemail) getVoicemailQuickSwitchDataWithCompletion:]
+ GCC_except_table327
+ GCC_except_table363
+ GCC_except_table426
+ GCC_except_table427
+ GCC_except_table429
+ GCC_except_table446
+ GCC_except_table455
+ GCC_except_table456
+ GCC_except_table467
+ GCC_except_table468
+ GCC_except_table471
+ GCC_except_table488
+ GCC_except_table811
+ GCC_except_table813
+ GCC_except_table817
+ GCC_except_table822
+ GCC_except_table827
+ GCC_except_table834
+ GCC_except_table836
+ GCC_except_table838
+ GCC_except_table852
+ GCC_except_table858
+ GCC_except_table862
+ GCC_except_table866
+ GCC_except_table869
+ GCC_except_table871
+ GCC_except_table873
+ GCC_except_table879
+ GCC_except_table883
+ OBJC_IVAR_$_CTDeviceIdentifier._IMEI1
+ OBJC_IVAR_$_CTDeviceIdentifier._IMEI2
+ OBJC_IVAR_$_CTDeviceIdentifier._NAL
+ OBJC_IVAR_$_CTLazuliSuggestedActionOpenUrlInApplication._schemeType
+ OBJC_IVAR_$_CTLazuliSuggestedActionOpenUrlInWebView._schemeType
+ OBJC_IVAR_$_CTPNRRequestSentInfo._requestID
+ OBJC_IVAR_$_CTPNRRequestType._requestID
+ _CTCallForwardingCopyDetectionCodes
+ _OBJC_CLASS_$_NSCharacterSet
+ __CTCallForwardingCopyDetectionCodes
+ __Z34print_CTLazuliChatBotURLSchemeType28CTLazuliChatBotURLSchemeType
+ __Z35encode_CTLazuliChatBotURLSchemeTypeN6Lazuli20ChatBotURLSchemeTypeE
+ __ZNK14CSIPhoneNumber22getIsCallForwardingMMIERKNSt3__16vectorINS0_12basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEENS5_IS7_EEEE
+ __ZNSt3__114__split_bufferINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEERNS4_IS6_EEE17__destruct_at_endB9nqn220106EPS6_
+ __ZNSt3__114__split_bufferINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEERNS4_IS6_EEED2Ev
+ __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE24__emplace_back_slow_pathIJS6_EEEPS6_DpOT_
+ __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE7reserveEm
+ __ZNSt3__18__invokeB9nqn220106IJZNS_16__variant_detail6__ctorINS1_8__traitsIJN6Lazuli31SuggestedActionOpenUrlInWebViewENS4_35SuggestedActionOpenUrlInApplicationENS4_26SuggestedActionComposeTextENS4_36SuggestedActionComposeAudioRecordingENS4_36SuggestedActionComposeVideoRecordingENS4_27SuggestedActionShowLocationENS4_34SuggestedActionRequestLocationPushENS4_23SuggestedActionCalendarENS4_28SuggestedActionDialVideoCallENS4_31SuggestedActionDialEnrichedCallENS4_30SuggestedActionDialPhoneNumberENS4_21SuggestedActionDeviceENS4_23SuggestedActionSettingsEEEEE19__generic_constructB9nqn220106IRKNS1_18__copy_constructorISI_LNS1_6_TraitE1EEEEEvRSJ_OT_EUlSS_E_RKNS1_5__altILm1ES6_EEEEENS_20__invoke_result_implIvJDpT_EE4typeEDpOSZ_
+ ___62-[CoreTelephonyClient(Voicemail) getVoicemailQuickSwitchData:]_block_invoke
+ ___62-[CoreTelephonyClient(Voicemail) getVoicemailQuickSwitchData:]_block_invoke_2
+ ___73-[CoreTelephonyClient(Voicemail) clearVoicemailQuickSwitchDataLostStatus]_block_invoke
+ ___73-[CoreTelephonyClient(Voicemail) clearVoicemailQuickSwitchDataLostStatus]_block_invoke_2
+ ___76-[CoreTelephonyClient(Voicemail) getVoicemailQuickSwitchDataWithCompletion:]_block_invoke
+ ___88-[CoreTelephonyClient(Voicemail) clearVoicemailQuickSwitchDataLostStatusWithCompletion:]_block_invoke
+ _kCTPhoneNumberRegistrationRequestIdKey
+ _objc_msgSend$IMEI1
+ _objc_msgSend$IMEI2
+ _objc_msgSend$NAL
+ _objc_msgSend$clearVoicemailQuickSwitchDataLostStatus:
+ _objc_msgSend$didSignUpQuickSwitchPlan:secondaryIccid:secondaryEid:secondaryImei:smdp:state:planIdentifier:completion:
+ _objc_msgSend$didSignUpQuickSwitchPlan:secondaryIccid:secondaryEid:secondaryImei:smdp:state:planIdentifier:error:completion:
+ _objc_msgSend$getVoicemailQuickSwitchData:
+ _objc_msgSend$planIdentifier
+ _objc_msgSend$requestID
+ _objc_msgSend$schemeType
+ _objc_msgSend$setGid1:
+ _objc_msgSend$setGid2:
+ _objc_msgSend$setRequestID:
+ _objc_msgSend$setSchemeType:
+ _objc_msgSend$stringByTrimmingCharactersInSet:
+ _objc_msgSend$whitespaceCharacterSet
- +[CTXPCGetDeviceStateRequest allowedClassesForArguments]
- +[CTXPCGetDeviceStateResponse allowedClassesForArguments]
- -[CTXPCGetDeviceStateRequest ct_shortName]
- -[CTXPCGetDeviceStateRequest performRequestWithHandler:completionHandler:]
- -[CTXPCGetDeviceStateRequest requiredEntitlement]
- -[CTXPCGetDeviceStateResponse ct_shortName]
- -[CTXPCGetDeviceStateResponse initWithState:]
- -[CTXPCGetDeviceStateResponse state]
- -[CTXPCUpdateQuickSwitchSignUpResult initWithPrimaryIccid:secondaryIccid:secondaryEid:secondaryImei:smdp:state:error:]
- -[CoreTelephonyClient(QuickSwitch) getDeviceStateWithCompletion:]
- GCC_except_table284
- GCC_except_table345
- GCC_except_table415
- GCC_except_table416
- GCC_except_table417
- GCC_except_table442
- GCC_except_table444
- GCC_except_table447
- GCC_except_table458
- GCC_except_table462
- GCC_except_table466
- GCC_except_table474
- GCC_except_table810
- GCC_except_table812
- GCC_except_table816
- GCC_except_table820
- GCC_except_table826
- GCC_except_table833
- GCC_except_table835
- GCC_except_table837
- GCC_except_table850
- GCC_except_table853
- GCC_except_table861
- GCC_except_table863
- GCC_except_table867
- GCC_except_table870
- GCC_except_table872
- GCC_except_table877
- GCC_except_table882
- _OBJC_CLASS_$_CTXPCGetDeviceStateRequest
- _OBJC_CLASS_$_CTXPCGetDeviceStateResponse
- _OBJC_METACLASS_$_CTXPCGetDeviceStateRequest
- _OBJC_METACLASS_$_CTXPCGetDeviceStateResponse
- __OBJC_$_CLASS_METHODS_CTXPCGetDeviceStateRequest
- __OBJC_$_CLASS_METHODS_CTXPCGetDeviceStateResponse
- __OBJC_$_INSTANCE_METHODS_CTXPCGetDeviceStateRequest
- __OBJC_$_INSTANCE_METHODS_CTXPCGetDeviceStateResponse
- __OBJC_$_PROP_LIST_CTXPCGetDeviceStateResponse
- __OBJC_CLASS_RO_$_CTXPCGetDeviceStateRequest
- __OBJC_CLASS_RO_$_CTXPCGetDeviceStateResponse
- __OBJC_METACLASS_RO_$_CTXPCGetDeviceStateRequest
- __OBJC_METACLASS_RO_$_CTXPCGetDeviceStateResponse
- ___74-[CTXPCGetDeviceStateRequest performRequestWithHandler:completionHandler:]_block_invoke
- _kCTPhoneNumberRegistrationResponseNotification
- _objc_msgSend$didSignUpQuickSwitchPlan:secondaryIccid:secondaryEid:secondaryImei:smdp:state:error:completion:
- _objc_msgSend$getDeviceStateWithCompletion:
CStrings:
+ " IMEI1=%@"
+ " IMEI2=%@"
+ " NAL=%@"
+ ","
+ ", requestID=%@"
+ ", schemeType = %s"
+ "13478.2"
+ "13478.2~112"
+ "CallForwarding"
+ "CallForwardingDetectionCodes"
+ "Default voice subscription unavailable (error=%@); using slot 1 for CallForwardingDetectionCodes"
+ "IMEI1"
+ "IMEI2"
+ "NAL"
+ "Read %lu CallForwarding detection prefixes from carrier bundle"
+ "Supported"
+ "kSchemeTypeKey"
+ "pending-profile-release"
+ "plan-identifier"
+ "primaryUpdatingToFanOutWithoutMsgRef"
+ "request_id"
+ "transport-activation-failed"
- "13473.1"
- "13473.1~72"
- "CTPhoneNumberRegistrationResponseNotification"
- "GetDeviceStateRequest"
- "GetDeviceStateResponse"

```
