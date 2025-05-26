## Setup

> `/Applications/Setup.app/Setup`

```diff

-5125.0.0.0.0
-  __TEXT.__text: 0x20c420
-  __TEXT.__auth_stubs: 0x21f0
-  __TEXT.__objc_stubs: 0x22ae0
-  __TEXT.__objc_methlist: 0x142b8
-  __TEXT.__cstring: 0xdd9f
-  __TEXT.__objc_methname: 0x337ed
-  __TEXT.__const: 0x13f8
-  __TEXT.__constg_swiftt: 0x116c
-  __TEXT.__swift5_typeref: 0xbb0
-  __TEXT.__swift5_fieldmd: 0x744
-  __TEXT.__swift5_builtin: 0x154
-  __TEXT.__swift5_reflstr: 0x8b1
-  __TEXT.__swift5_assocty: 0x270
-  __TEXT.__swift5_proto: 0xb0
-  __TEXT.__swift5_types: 0xb4
+5129.0.0.0.0
+  __TEXT.__text: 0x2139bc
+  __TEXT.__auth_stubs: 0x2260
+  __TEXT.__objc_stubs: 0x22b40
+  __TEXT.__objc_methlist: 0x142e8
+  __TEXT.__cstring: 0xe1e9
+  __TEXT.__objc_methname: 0x338dd
+  __TEXT.__const: 0x14c8
+  __TEXT.__constg_swiftt: 0x122c
+  __TEXT.__swift5_typeref: 0xc22
+  __TEXT.__swift5_fieldmd: 0x774
+  __TEXT.__swift5_builtin: 0x168
+  __TEXT.__swift5_reflstr: 0x941
+  __TEXT.__swift5_assocty: 0x288
+  __TEXT.__swift5_proto: 0xbc
+  __TEXT.__swift5_types: 0xb8
   __TEXT.__objc_classname: 0x3185
   __TEXT.__objc_methtype: 0x9edb
-  __TEXT.__swift5_capture: 0xac0
+  __TEXT.__swift5_capture: 0xc70
   __TEXT.__gcc_except_tab: 0x3148
   __TEXT.__oslogstring: 0xdd06
   __TEXT.__dlopen_cstrs: 0xff6
-  __TEXT.__unwind_info: 0x84f8
-  __TEXT.__eh_frame: 0xbd8
-  __DATA_CONST.__auth_got: 0x1110
+  __TEXT.__unwind_info: 0x879c
+  __TEXT.__eh_frame: 0xce8
+  __DATA_CONST.__auth_got: 0x1148
   __DATA_CONST.__got: 0xa20
   __DATA_CONST.__auth_ptr: 0x88
-  __DATA_CONST.__const: 0x6508
-  __DATA_CONST.__cfstring: 0xa980
+  __DATA_CONST.__const: 0x69e8
+  __DATA_CONST.__cfstring: 0xa9a0
   __DATA_CONST.__objc_classlist: 0xa60
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x450

   __DATA_CONST.__objc_dictobj: 0x140
   __DATA_CONST.__objc_intobj: 0x2d0
   __DATA_CONST.__objc_floatobj: 0x10
-  __DATA.__objc_const: 0x3fd38
-  __DATA.__objc_selrefs: 0xa098
+  __DATA.__objc_const: 0x3fdb8
+  __DATA.__objc_selrefs: 0xa0c8
   __DATA.__objc_ivar: 0x1930
-  __DATA.__objc_data: 0x7b58
-  __DATA.__data: 0x4018
-  __DATA.__bss: 0x1af0
+  __DATA.__objc_data: 0x7c18
+  __DATA.__data: 0x4088
+  __DATA.__bss: 0x1c70
   __DATA.__common: 0xc8
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 10234
-  Symbols:   1356
-  CStrings:  12548
+  Functions: 10368
+  Symbols:   1365
+  CStrings:  12575
 
Symbols:
+ _$s8Dispatch0A8WorkItemC5flags5blockAcA0abC5FlagsV_yyXBtcfC
+ _$s8Dispatch0A8WorkItemC7performyyFTj
+ _$s8Dispatch0A8WorkItemCMa
+ _$s8Dispatch0A8WorkItemCMn
+ _$sSDyq_Sgxcig
+ _$sSo13os_log_type_ta0A0E4infoABvgZ
+ _$sSo8NSNumberC10FoundationE14integerLiteralABSi_tcfC
+ _$ss11AnyHashableVMn
+ _$ss21_convertToAnyHashableys0cD0VxSHRzlF
CStrings:
+ "Authentication completed - did Authenticate: %{bool}d"
+ "Enabling stolen device protection enabled"
+ "Failed to authenticate with error: %@"
+ "Failed to checkCanEnableFeature (Stolen Device Protection) with error: %@"
+ "Failed to enable stolen device protection: %@"
+ "Force navigation from %s"
+ "Ignoring user authentication completed more while another request is being processed."
+ "Jul  3 2024"
+ "Liveness check failed; prompt for biometrics authenticate"
+ "No authentication results"
+ "No results, and no error during checkCanEnableFeature (StolenDeviceProtection)"
+ "STOLEN_DEVICE_PROTECTION_ALERT_FACE_ID_RETRY_AGAIN"
+ "STOLEN_DEVICE_PROTECTION_FAILED_TO_ENABLE_ALERT_TITLE"
+ "STOLEN_DEVICE_PROTECTION_LOCAL_AUTHENTICATION_REASON_TO_ENABLE"
+ "Start biometrics authentication"
+ "Stolen device protection pane - Turn on tapped"
+ "Stolen device protection pane - not now tapped"
+ "This method should only be called with a Software Update error."
+ "_suggestSoftwareUpdateWithOSVersion:buildVersion:navigationController:"
+ "_suggestSoftwareUpdateWithSoftwareUpdateRequiredError:navigationController:"
+ "applicationDidBecomeActive"
+ "checkCanEnableFeatureWithCompletion:"
+ "clearInput"
+ "com.apple.LocalAuthentication"
+ "enableFeatureWithReply:"
+ "evaluatePolicy:options:reply:"
+ "forceExecutePostAuthenticationWorkItem"
+ "localAuthenticationReason"
+ "notificationCenter"
+ "postAuthenticationWorkItem"
+ "setTouchIDAuthenticationRetryLimit:"
+ "transitionToSoftwareUpdateControllerFromController:lastError:"
- "May  2 2024"
- "Stolen device protection enablement failed with %@"
- "_suggestSoftwareUpdateWithOSVersion:buildVersion:"
- "_suggestSoftwareUpdateWithSoftwareUpdateRequiredError:"
- "enableFeatureWithCompletion:"

```
