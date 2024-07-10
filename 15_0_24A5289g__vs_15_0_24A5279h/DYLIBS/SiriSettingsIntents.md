## SiriSettingsIntents

> `/System/Library/PrivateFrameworks/SiriSettingsIntents.framework/Versions/A/SiriSettingsIntents`

```diff

-3400.95.2.0.0
-  __TEXT.__text: 0x2f4310
-  __TEXT.__auth_stubs: 0x2f90
+3400.89.1.0.0
+  __TEXT.__text: 0x2dd37c
+  __TEXT.__auth_stubs: 0x2f80
   __TEXT.__objc_methlist: 0x150
   __TEXT.__const: 0xf754
-  __TEXT.__swift5_typeref: 0x3220
-  __TEXT.__swift5_capture: 0x29ec
+  __TEXT.__swift5_typeref: 0x3218
+  __TEXT.__swift5_capture: 0x29ac
   __TEXT.__oslogstring: 0xe24
-  __TEXT.__swift5_fieldmd: 0x6394
-  __TEXT.__constg_swiftt: 0x7574
+  __TEXT.__swift5_fieldmd: 0x6358
+  __TEXT.__constg_swiftt: 0x74f4
   __TEXT.__swift5_builtin: 0x17c
-  __TEXT.__swift5_reflstr: 0x66db
+  __TEXT.__swift5_reflstr: 0x665b
   __TEXT.__swift5_assocty: 0x1130
   __TEXT.__swift5_protos: 0x4c
   __TEXT.__swift5_proto: 0xb1c
   __TEXT.__swift5_types: 0x690
-  __TEXT.__cstring: 0x159b3
+  __TEXT.__cstring: 0x146c3
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x4280
-  __TEXT.__eh_frame: 0x6600
+  __TEXT.__unwind_info: 0x4020
+  __TEXT.__eh_frame: 0x5e08
   __TEXT.__objc_classname: 0x169
   __TEXT.__objc_methname: 0x1638
   __TEXT.__objc_methtype: 0xbef

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x500
   __DATA_CONST.__objc_protorefs: 0x90
-  __AUTH_CONST.__auth_got: 0x17c8
-  __AUTH_CONST.__auth_ptr: 0x1420
-  __AUTH_CONST.__const: 0xd0b0
-  __AUTH_CONST.__objc_const: 0xc8e0
+  __AUTH_CONST.__auth_got: 0x17c0
+  __AUTH_CONST.__auth_ptr: 0x1438
+  __AUTH_CONST.__const: 0xd038
+  __AUTH_CONST.__objc_const: 0xc860
   __AUTH.__objc_data: 0xe20
   __AUTH.__data: 0x9d78
-  __DATA.__data: 0x5430
+  __DATA.__data: 0x53a0
   __DATA.__bss: 0x12100
-  __DATA.__common: 0x1648
+  __DATA.__common: 0x1640
   - /System/Library/Frameworks/AVFoundation.framework/Versions/A/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/Versions/A/CoreGraphics

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 8952
-  Symbols:   2153
-  CStrings:  1867
+  Functions: 8828
+  Symbols:   2151
+  CStrings:  1822
 
Symbols:
+ ___unnamed_19
+ ___unnamed_23
- _AFDeviceSupportsSystemAssistantExperience
- ___unnamed_26
- _symbolic ______p 19SiriSettingsIntents12SettingModelP
CStrings:
- "GetSettingHandleIntentFlowStrategy makeIntentHandledResponse | using RF2"
- "GetSettingTemplatingService getSettingName | binarySettingName CAT failed"
- "GetSettingTemplatingService getSettingName | multiSettingName CAT failed"
- "GetSettingTemplatingService getSettingName | numericSettingName CAT failed"
- "GetSettingTemplatingService handleOtherFailureReasonRF2 | DescribeHotspotDiscoverability cat execution error %!@(MISSING)"
- "GetSettingTemplatingService handleOtherFailureReasonRF2 | DeviceDoesNotSupportBinarySetting cat execution error %!@(MISSING)"
- "GetSettingTemplatingService handleOtherFailureReasonRF2 | DeviceDoesNotSupportNumericSetting cat execution error %!@(MISSING)"
- "GetSettingTemplatingService handleOtherFailureReasonRF2 | DisplaySettingsDisabledForCurrentMode cat execution error %!@(MISSING)"
- "GetSettingTemplatingService handleOtherFailureReasonRF2 | FocusNotConfigured cat execution error %!@(MISSING)"
- "GetSettingTemplatingService handleOtherFailureReasonRF2 | SiriCannotChangeSetting cat execution error %!@(MISSING)"
- "GetSettingTemplatingService handleOtherFailureReasonRF2 | response 'other reason' error code contains unsupported error detail: %!@(MISSING)"
- "GetSettingTemplatingService handleOtherFailureReasonRF2 | response contains error code 'other reason' but no details: %!@(MISSING)"
- "GetSettingTemplatingService handleOtherFailureReasonRF2 | targetDeviceNotFoundReadBattery cat execution error missing target device."
- "GetSettingTemplatingService makeFailureHandlingIntentDialogSyncRF2 | Rendering Noise Management case"
- "GetSettingTemplatingService makeFailureHandlingIntentDialogSyncRF2 | Rendering failureUnsupported"
- "GetSettingTemplatingService makeFailureHandlingIntentDialogSyncRF2 | Rendering standard response"
- "GetSettingTemplatingService makeFailureHandlingIntentDialogSyncRF2 | response contains unsupported error code: %!@(MISSING)"
- "GetSettingTemplatingService makeFailureHandlingIntentDialogSyncRF2 | response does not exist"
- "GetSettingTemplatingService makeIntentConfirmationCancelledDialogRF2 | RetainingCurrentBinaryValue cat execution error %!@(MISSING)"
- "GetSettingTemplatingService makeIntentConfirmationDialogRF2 | HotspotDiscoverabilityPrompt cat execution error %!@(MISSING)"
- "GetSettingTemplatingService makeIntentConfirmationDialogRF2 | INGetSettingIntent requires confirmation %!@(MISSING)"
- "GetSettingTemplatingService makeIntentHandledDialogBinaryRF2 | Providing verbose version of DescribeBinarySettingState CAT for %!@(MISSING)."
- "GetSettingTemplatingService makeIntentHandledDialogBinaryRF2 | describeBinarySettingState cat execution error %!@(MISSING)"
- "GetSettingTemplatingService makeIntentHandledDialogBinaryRF2 | describeMultiSettingState cat execution error %!@(MISSING)"
- "GetSettingTemplatingService makeIntentHandledDialogBinaryRF2 | response has invalid value %!@(MISSING)"
- "GetSettingTemplatingService makeIntentHandledDialogNumericSyncRF2 | Providing spoken-only version of CAT for displayBrightness."
- "GetSettingTemplatingService makeIntentHandledDialogNumericSyncRF2 | Providing verbose CAT for displayBrightness."
- "GetSettingTemplatingService makeIntentHandledDialogNumericSyncRF2 | describeNumericSettingState cat execution error %!@(MISSING)"
- "GetSettingTemplatingService makeIntentHandledDialogNumericSyncRF2 | describeNumericSettingStateSpokenOnly cat execution error %!@(MISSING)"
- "GetSettingTemplatingService makeIntentHandledDialogNumericSyncRF2 | response has invalid value %!@(MISSING)"
- "GetSettingTemplatingService makeIntentHandledDialogSyncRF2 | GetSettingIntent has no settingMetadata"
- "GetSettingTemplatingService makeIntentHandledDialogSyncRF2 | makeIntentHandledDialog normally handling intent: %!@(MISSING)"
- "GetSettingTemplatingService makeIntentHandledDialogSyncRF2 | settingMetadata contains unsupported setting identifier"
- "GetSettingTemplatingService makeNumericSnippetModel | invalid setting identifier %!@(MISSING)"
- "GetSettingTemplatingService makeNumericSnippetModel | omitting snippet for battery utterance"
- "GetSettingTemplatingService makeNumericSnippetModel | response has invalid value %!@(MISSING)"
- "GetSettingTemplatingService makeSnippetModel | GetSettingIntent has no settingMetadata"
- "GetSettingTemplatingService makeSnippetModel | invalid setting identifier %!@(MISSING)"
- "GetSettingTemplatingService makeSnippetModel | making binary snippet model for intent %!@(MISSING)"
- "GetSettingTemplatingService makeSnippetModel | making numeric snippet model for intent %!@(MISSING)"
- "GetSettingTemplatingService makeSnippetModel | response has invalid new value %!@(MISSING)"
- "GetSettingTemplatingService makeSnippetModel | returning resultModel %!@(MISSING)"
- "GetSettingTemplatingService makeSnippetModel | settingMetadata contains unsupported setting identifier"
- "getProviderSimple"
- "testMode"

```
