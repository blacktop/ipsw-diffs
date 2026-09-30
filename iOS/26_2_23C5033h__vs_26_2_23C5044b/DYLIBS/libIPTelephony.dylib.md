## libIPTelephony.dylib

> `/System/Library/PrivateFrameworks/IPTelephony.framework/Support/libIPTelephony.dylib`

```diff

-2606.1.0.0.0
-  __TEXT.__text: 0x5288dc
+2607.3.0.0.0
+  __TEXT.__text: 0x52ac7c
   __TEXT.__auth_stubs: 0x2ee0
   __TEXT.__init_offsets: 0x15c
   __TEXT.__objc_methlist: 0x748
-  __TEXT.__const: 0x20a6a
-  __TEXT.__cstring: 0x37448
-  __TEXT.__gcc_except_tab: 0x4e5d4
-  __TEXT.__oslogstring: 0xe9eb
-  __TEXT.__unwind_info: 0x190c8
+  __TEXT.__const: 0x20b0a
+  __TEXT.__cstring: 0x3786c
+  __TEXT.__gcc_except_tab: 0x4e970
+  __TEXT.__oslogstring: 0xed1a
+  __TEXT.__unwind_info: 0x19160
   __TEXT.__objc_classname: 0x12f
-  __TEXT.__objc_methname: 0x1d3d
+  __TEXT.__objc_methname: 0x1de8
   __TEXT.__objc_methtype: 0x1118
-  __TEXT.__objc_stubs: 0x1c00
-  __DATA_CONST.__got: 0x468
-  __DATA_CONST.__const: 0x3830
+  __TEXT.__objc_stubs: 0x1c80
+  __DATA_CONST.__got: 0x4c8
+  __DATA_CONST.__const: 0x38e0
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x948
+  __DATA_CONST.__objc_selrefs: 0x968
   __DATA_CONST.__objc_superrefs: 0x38
   __AUTH_CONST.__auth_got: 0x1780
   __AUTH_CONST.__const: 0x3c058
-  __AUTH_CONST.__cfstring: 0x26c0
+  __AUTH_CONST.__cfstring: 0x26e0
   __AUTH_CONST.__objc_const: 0xbf8
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH.__objc_data: 0x140

   - /System/Library/PrivateFrameworks/NetworkServiceProxy.framework/NetworkServiceProxy
   - /System/Library/PrivateFrameworks/PersistentConnection.framework/PersistentConnection
   - /System/Library/PrivateFrameworks/PowerLog.framework/PowerLog
+  - /System/Library/PrivateFrameworks/SymptomDiagnosticReporter.framework/SymptomDiagnosticReporter
   - /System/Library/PrivateFrameworks/Trial.framework/Trial
   - /usr/lib/libARI.dylib
   - /usr/lib/libATCommandStudioDynamic.dylib

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprotobuf-lite.dylib
   - /usr/lib/libxml2.2.dylib
-  UUID: C0108EBA-024C-3FE8-83B4-C4A0D2F1D282
-  Functions: 17071
-  Symbols:   51280
-  CStrings:  9876
+  UUID: 52247733-79C3-37FD-BC13-D9849FC00E93
+  Functions: 17088
+  Symbols:   51346
+  CStrings:  9924
 
Symbols:
+ _OBJC_CLASS_$_SDRDiagnosticReporter
+ __ZN12_GLOBAL__N_129NetworkServiceProxyHelperImpl19checkErrorInjectionERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE
+ __ZN21SipRegistrationClient27captureAbcRcsPushRegFailureEv
+ __ZN3abc8snapshotERKNS_6ParamsE
+ __ZN9ImsResultlsIA35_cEERS_RKT_
+ __ZNK15CommCenterPrefs29getBoolValueFromRuntimeConfigERKNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEEb
+ __ZNK15CommCenterPrefs31getStringValueFromRuntimeConfigERKNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEES8_
+ __ZNK15CommCenterPrefs9_getValueERKNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEERN3ctu2cf11CFSharedRefIKvEEm
+ __ZNSt3__110__function12__value_funcIFv9ImsResultNS_6vectorIhNS_9allocatorIhEEEEEEC2B8ne200100EOS8_
+ __ZNSt3__110__function12__value_funcIFv9ImsResultNS_6vectorIhNS_9allocatorIhEEEES6_EEC2B8ne200100EOS8_
+ __ZNSt3__110unique_ptrIZN12_GLOBAL__N_129NetworkServiceProxyHelperImpl28generateAthmSpamTokenRequestERKNS_8optionalINS_6vectorIhNS_9allocatorIhEEEEEENS_8functionIFv9ImsResultS7_EEEE3$_1NS_14default_deleteISF_EEED1B8ne200100Ev
+ __ZNSt3__110unique_ptrIZN12_GLOBAL__N_129NetworkServiceProxyHelperImpl29requestPatAndReputationTokensERK27PatAndReputationTokenParamsE3$_1NS_14default_deleteIS6_EEED1B8ne200100Ev
+ __ZNSt3__110unique_ptrIZZN12_GLOBAL__N_129NetworkServiceProxyHelperImpl28generateAthmSpamTokenRequestERKNS_8optionalINS_6vectorIhNS_9allocatorIhEEEEEENS_8functionIFv9ImsResultS7_EEEEUb_E3$_3NS_14default_deleteISF_EEED1B8ne200100Ev
+ __ZNSt3__110unique_ptrIZZN12_GLOBAL__N_129NetworkServiceProxyHelperImpl29requestPatAndReputationTokensERK27PatAndReputationTokenParamsEUb0_E3$_6NS_14default_deleteIS6_EEED1B8ne200100Ev
+ __ZNSt3__110unique_ptrIZZN12_GLOBAL__N_129NetworkServiceProxyHelperImpl29requestPatAndReputationTokensERK27PatAndReputationTokenParamsEUb0_E3$_7NS_14default_deleteIS6_EEED1B8ne200100Ev
+ __ZNSt3__110unique_ptrIZZZN12_GLOBAL__N_129NetworkServiceProxyHelperImpl29requestPatAndReputationTokensERK27PatAndReputationTokenParamsEUb0_EUb1_E3$_8NS_14default_deleteIS6_EEED1B8ne200100Ev
+ __ZNSt3__110unique_ptrIZZZN12_GLOBAL__N_129NetworkServiceProxyHelperImpl29requestPatAndReputationTokensERK27PatAndReputationTokenParamsEUb0_EUb1_E3$_9NS_14default_deleteIS6_EEED1B8ne200100Ev
+ __ZNSt3__120__optional_move_baseI9ImsResultLb0EEC2B8ne200100EOS2_
+ __ZTISt9exception
+ __ZZN8dispatch5asyncIZN12_GLOBAL__N_129NetworkServiceProxyHelperImpl28generateAthmSpamTokenRequestERKNSt3__18optionalINS3_6vectorIhNS3_9allocatorIhEEEEEENS3_8functionIFv9ImsResultS8_EEEE3$_1EEvPU28objcproto17OS_dispatch_queue8NSObjectNS3_10unique_ptrIT_NS3_14default_deleteISL_EEEEENUlPvE_8__invokeESP_
+ __ZZN8dispatch5asyncIZN12_GLOBAL__N_129NetworkServiceProxyHelperImpl29requestPatAndReputationTokensERK27PatAndReputationTokenParamsE3$_1EEvPU28objcproto17OS_dispatch_queue8NSObjectNSt3__110unique_ptrIT_NSA_14default_deleteISC_EEEEENUlPvE_8__invokeESG_
+ __ZZN8dispatch5asyncIZZN12_GLOBAL__N_129NetworkServiceProxyHelperImpl28generateAthmSpamTokenRequestERKNSt3__18optionalINS3_6vectorIhNS3_9allocatorIhEEEEEENS3_8functionIFv9ImsResultS8_EEEEUb_E3$_3EEvPU28objcproto17OS_dispatch_queue8NSObjectNS3_10unique_ptrIT_NS3_14default_deleteISL_EEEEENUlPvE_8__invokeESP_
+ __ZZN8dispatch5asyncIZZN12_GLOBAL__N_129NetworkServiceProxyHelperImpl29requestPatAndReputationTokensERK27PatAndReputationTokenParamsEUb0_E3$_6EEvPU28objcproto17OS_dispatch_queue8NSObjectNSt3__110unique_ptrIT_NSA_14default_deleteISC_EEEEENUlPvE_8__invokeESG_
+ __ZZN8dispatch5asyncIZZN12_GLOBAL__N_129NetworkServiceProxyHelperImpl29requestPatAndReputationTokensERK27PatAndReputationTokenParamsEUb0_E3$_7EEvPU28objcproto17OS_dispatch_queue8NSObjectNSt3__110unique_ptrIT_NSA_14default_deleteISC_EEEEENUlPvE_8__invokeESG_
+ __ZZN8dispatch5asyncIZZZN12_GLOBAL__N_129NetworkServiceProxyHelperImpl29requestPatAndReputationTokensERK27PatAndReputationTokenParamsEUb0_EUb1_E3$_8EEvPU28objcproto17OS_dispatch_queue8NSObjectNSt3__110unique_ptrIT_NSA_14default_deleteISC_EEEEENUlPvE_8__invokeESG_
+ __ZZN8dispatch5asyncIZZZN12_GLOBAL__N_129NetworkServiceProxyHelperImpl29requestPatAndReputationTokensERK27PatAndReputationTokenParamsEUb0_EUb1_E3$_9EEvPU28objcproto17OS_dispatch_queue8NSObjectNSt3__110unique_ptrIT_NSA_14default_deleteISC_EEEEENUlPvE_8__invokeESG_
+ ____ZN12_GLOBAL__N_129NetworkServiceProxyHelperImpl29requestPatAndReputationTokensERK27PatAndReputationTokenParams_block_invoke.55
+ ____ZN3abc8snapshotERKNS_6ParamsE_block_invoke
+ ___block_descriptor_40_ea8_32r_e22_v16?0"NSDictionary"8lr32l8
+ ___block_descriptor_tmp.174
+ ___cxx_global_var_init.124
+ ___kCFBooleanFalse
+ _kCommCenterPrefsDefaultAppID
+ _kSymptomDiagnosticActionCrashAndSpinLogs
+ _kSymptomDiagnosticActionDiagnosticExtensions
+ _kSymptomDiagnosticActionGetNetworkInfo
+ _kSymptomDiagnosticActionLogArchive
+ _kSymptomDiagnosticActionProbePacketCapture
+ _kSymptomDiagnosticExtensionsCommonActions
+ _kSymptomDiagnosticReplyReason
+ _kSymptomDiagnosticReplyReasonString
+ _kSymptomDiagnosticReplySuccess
+ _objc_msgSend$intValue
+ _objc_msgSend$numberWithBool:
+ _objc_msgSend$signatureWithDomain:type:subType:subtypeContext:detectedProcess:triggerThresholdValues:
+ _objc_msgSend$snapshotWithSignature:delay:events:payload:actions:reply:
+ _objc_release_x9
- __ZN15CommCenterPrefs29getBoolValueFromRuntimeConfigERKNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEEb
- __ZNSt3__110unique_ptrIZZN12_GLOBAL__N_129NetworkServiceProxyHelperImpl28generateAthmSpamTokenRequestERKNS_8optionalINS_6vectorIhNS_9allocatorIhEEEEEENS_8functionIFv9ImsResultS7_EEEEUb_E3$_1NS_14default_deleteISF_EEED1B8ne200100Ev
- __ZNSt3__110unique_ptrIZZN12_GLOBAL__N_129NetworkServiceProxyHelperImpl29requestPatAndReputationTokensERK27PatAndReputationTokenParamsEUb0_E3$_4NS_14default_deleteIS6_EEED1B8ne200100Ev
- __ZNSt3__110unique_ptrIZZZN12_GLOBAL__N_129NetworkServiceProxyHelperImpl29requestPatAndReputationTokensERK27PatAndReputationTokenParamsEUb0_EUb1_E3$_5NS_14default_deleteIS6_EEED1B8ne200100Ev
- __ZNSt3__110unique_ptrIZZZN12_GLOBAL__N_129NetworkServiceProxyHelperImpl29requestPatAndReputationTokensERK27PatAndReputationTokenParamsEUb0_EUb1_E3$_6NS_14default_deleteIS6_EEED1B8ne200100Ev
- __ZZN8dispatch5asyncIZZN12_GLOBAL__N_129NetworkServiceProxyHelperImpl28generateAthmSpamTokenRequestERKNSt3__18optionalINS3_6vectorIhNS3_9allocatorIhEEEEEENS3_8functionIFv9ImsResultS8_EEEEUb_E3$_1EEvPU28objcproto17OS_dispatch_queue8NSObjectNS3_10unique_ptrIT_NS3_14default_deleteISL_EEEEENUlPvE_8__invokeESP_
- __ZZN8dispatch5asyncIZZN12_GLOBAL__N_129NetworkServiceProxyHelperImpl29requestPatAndReputationTokensERK27PatAndReputationTokenParamsEUb0_E3$_4EEvPU28objcproto17OS_dispatch_queue8NSObjectNSt3__110unique_ptrIT_NSA_14default_deleteISC_EEEEENUlPvE_8__invokeESG_
- __ZZN8dispatch5asyncIZZZN12_GLOBAL__N_129NetworkServiceProxyHelperImpl29requestPatAndReputationTokensERK27PatAndReputationTokenParamsEUb0_EUb1_E3$_5EEvPU28objcproto17OS_dispatch_queue8NSObjectNSt3__110unique_ptrIT_NSA_14default_deleteISC_EEEEENUlPvE_8__invokeESG_
- __ZZN8dispatch5asyncIZZZN12_GLOBAL__N_129NetworkServiceProxyHelperImpl29requestPatAndReputationTokensERK27PatAndReputationTokenParamsEUb0_EUb1_E3$_6EEvPU28objcproto17OS_dispatch_queue8NSObjectNSt3__110unique_ptrIT_NSA_14default_deleteISC_EEEEENUlPvE_8__invokeESG_
- ____ZN12_GLOBAL__N_129NetworkServiceProxyHelperImpl29requestPatAndReputationTokensERK27PatAndReputationTokenParams_block_invoke.25
- ___cxx_global_var_init.120
- _objc_retain_x25
CStrings:
+ "#E %{private, mask.hash}sFailed to parse error type '%{public}s': %{public}s"
+ "#E %{private, mask.hash}sNSP error injection enabled but no error type specified, using default (ServerFailure)"
+ "#E %{private, mask.hash}sUnknown NSP error code %d for injection, using ServerFailure"
+ "#E abc reply failure: (%d) %@"
+ "#I %{private, mask.hash}sNSP error injection: injecting error type '%{public}s' for target '%{public}s'"
+ "#I %{private, mask.hash}sNSP error injection: returning error for fetchTokenAndAuxiliaryAuthenticationWithQueue"
+ "#I %{private, mask.hash}sNSP error injection: returning error for generateTokenRequestWithQueue"
+ "#I %{private, mask.hash}sNSP error injection: returning error for handleTokenResponse"
+ "%{private, mask.hash}srequesting abc snapshot with context %s"
+ "/AppleInternal/Library/BuildRoots/4~CCK4ugCqxJ5N_tPb-n8rfE-h-v14e0nRGpbMJZA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/local/include/ARI/ari_sdk_msg.h"
+ "/AppleInternal/Library/BuildRoots/4~CCK4ugCqxJ5N_tPb-n8rfE-h-v14e0nRGpbMJZA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/local/include/google/protobuf/repeated_field.h"
+ "Commcenter"
+ "First Registration Failed"
+ "NSP Error Injection: FeatureDisabled (1008)"
+ "NSP Error Injection: IPCFailed (1002)"
+ "NSP Error Injection: Invalid error type"
+ "NSP Error Injection: InvalidAuthentication (1010)"
+ "NSP Error Injection: InvalidConfigData (1005)"
+ "NSP Error Injection: InvalidConfigDataSign (1006)"
+ "NSP Error Injection: InvalidConfigDates (1014)"
+ "NSP Error Injection: InvalidParam (1004)"
+ "NSP Error Injection: InvalidRequest (1011)"
+ "NSP Error Injection: InvalidResponse (1016)"
+ "NSP Error Injection: InvalidUserTier (1003)"
+ "NSP Error Injection: Network error"
+ "NSP Error Injection: NetworkFailure (1012)"
+ "NSP Error Injection: PermissionDenied (1001)"
+ "NSP Error Injection: RateLimited (1009)"
+ "NSP Error Injection: ServerFailure (1007)"
+ "NSP Error Injection: TDMFailure (1015)"
+ "NSP Error Injection: Timeout"
+ "NSP Error Injection: TransparencyFailure (1013)"
+ "NSP Error Injection: Unknown error code ("
+ "NSPErrorInjectionEnabled"
+ "NSPErrorInjectionTarget"
+ "NSPErrorInjectionType"
+ "PushRegistrationFailure"
+ "Telephony"
+ "abc"
+ "abc reply success!"
+ "intValue"
+ "numberWithBool:"
+ "patReputation"
+ "signatureWithDomain:type:subType:subtypeContext:detectedProcess:triggerThresholdValues:"
+ "snapshotWithSignature:delay:events:payload:actions:reply:"
+ "tokenRequest"
+ "tokenResponse"
+ "trigger abc isSuccess:%{BOOL}d"
+ "v16@?0@\"NSDictionary\"8"
- "/AppleInternal/Library/BuildRoots/4~CBgdugBtiVw6CFCgK8VykcIMCxZYblQ-4BUa6Hk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/local/include/ARI/ari_sdk_msg.h"
- "/AppleInternal/Library/BuildRoots/4~CBgdugBtiVw6CFCgK8VykcIMCxZYblQ-4BUa6Hk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/local/include/google/protobuf/repeated_field.h"

```
