# 18.3 (22D63) .vs 18.3.1 (22D72)

## IPSWs

- `iPhone17,1_18.3_22D63_Restore.ipsw`
- `iPhone17,1_18.3.1_22D72_Restore.ipsw`

## Kernel

### Version

| iOS | Version | Build | Date |
| :-- | :------ | :---- | :--- |
| 18.3 *(22D63)* | 24.3.0 | 11215.82.4~20 | Thu, 16Jan2025 03:00:11 PST |
| 18.3.1 *(22D72)* | 24.3.0 | 11215.82.4~20 | Thu, 16Jan2025 03:00:11 PST |

## MachO

### ⬆️ Updated (10)

<details>
  <summary><i>View Updated</i></summary>

#### WritingToolsUIService

>  `/Applications/WritingToolsUIService.app/WritingToolsUIService`

```diff

-44.228.0.0.0
-  __TEXT.__text: 0x185508
-  __TEXT.__auth_stubs: 0x4df0
+44.228.100.0.0
+  __TEXT.__text: 0x1816bc
+  __TEXT.__auth_stubs: 0x4bd0
   __TEXT.__objc_stubs: 0xc0
   __TEXT.__objc_methlist: 0x604
   __TEXT.__const: 0xc554
   __TEXT.__objc_methname: 0x3f6b
   __TEXT.__objc_classname: 0x216
   __TEXT.__objc_methtype: 0x1a60
-  __TEXT.__cstring: 0x7965
-  __TEXT.__swift5_typeref: 0x24c7c
+  __TEXT.__cstring: 0x78a5
+  __TEXT.__swift5_typeref: 0x24c4e
   __TEXT.__constg_swiftt: 0x51c0
   __TEXT.__swift5_reflstr: 0x3164
   __TEXT.__swift5_fieldmd: 0x3014

   __TEXT.__swift5_assocty: 0xf60
   __TEXT.__swift5_proto: 0x5c4
   __TEXT.__swift5_types: 0x368
-  __TEXT.__oslogstring: 0x3539
-  __TEXT.__swift5_capture: 0x1524
+  __TEXT.__oslogstring: 0x3509
+  __TEXT.__swift5_capture: 0x154c
   __TEXT.__swift5_protos: 0x14
   __TEXT.__swift5_mpenum: 0x18
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0x4db0
-  __TEXT.__eh_frame: 0x6340
-  __DATA_CONST.__auth_got: 0x2700
-  __DATA_CONST.__got: 0x1260
-  __DATA_CONST.__auth_ptr: 0x22c8
+  __TEXT.__unwind_info: 0x4d90
+  __TEXT.__eh_frame: 0x6260
+  __DATA_CONST.__auth_got: 0x25f0
+  __DATA_CONST.__got: 0x1238
+  __DATA_CONST.__auth_ptr: 0x2278
   __DATA_CONST.__const: 0x7c20
   __DATA_CONST.__objc_classlist: 0x130
   __DATA_CONST.__objc_catlist: 0x8

   __DATA.__objc_const: 0x49d8
   __DATA.__objc_selrefs: 0xb20
   __DATA.__objc_data: 0x1628
-  __DATA.__data: 0xb9d0
+  __DATA.__data: 0xb9b0
   __DATA.__bss: 0xc2b8
   __DATA.__common: 0x670
   - /System/Library/Frameworks/Combine.framework/Combine

   - /System/Library/PrivateFrameworks/TextComposer.framework/TextComposer
   - /System/Library/PrivateFrameworks/TextInput.framework/TextInput
   - /System/Library/PrivateFrameworks/TokenGeneration.framework/TokenGeneration
-  - /System/Library/PrivateFrameworks/TokenGenerationCore.framework/TokenGenerationCore
   - /System/Library/PrivateFrameworks/TranslationUIServices.framework/TranslationUIServices
   - /System/Library/PrivateFrameworks/UIFoundation.framework/UIFoundation
   - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 6797
-  Symbols:   2331
-  CStrings:  1603
+  Functions: 6790
+  Symbols:   2288
+  CStrings:  1597
 
Symbols:
+ _$s15TokenGeneration22PromptCompletionStreamV7collectAA0cD0VyYaKF
+ _$s15TokenGeneration22PromptCompletionStreamV7collectAA0cD0VyYaKFTu
+ _swift_deallocUninitializedObject
- _$s15TokenGeneration021PromptCompletionEventC10ModerationV10moderationAA0cD0V0F0Vvg
- _$s15TokenGeneration021PromptCompletionEventC10ModerationVMa
- _$s15TokenGeneration029PromptCompletionEventRenderedC0V08renderedC0AA0C0V9RenderingVvg
- _$s15TokenGeneration029PromptCompletionEventRenderedC0VMa
- _$s15TokenGeneration035PromptCompletionEventCandidateImageB0V5imageAA0cD0V0G7ContentVvg
- _$s15TokenGeneration035PromptCompletionEventCandidateImageB0VMa
- _$s15TokenGeneration12FinishReasonO012producedStopA0yA2CmFWC
- _$s15TokenGeneration12FinishReasonOMa
- _$s15TokenGeneration16ModelInformationVMa
- _$s15TokenGeneration16ModelInformationVMn
- _$s15TokenGeneration16PromptCompletionV10ModerationVMa
- _$s15TokenGeneration16PromptCompletionV10ModerationVMn
- _$s15TokenGeneration16PromptCompletionV11TextContentV5valueAESS_tcfC
- _$s15TokenGeneration16PromptCompletionV16modelInformation16promptModeration10candidates5usage8metadata08renderedC0AcA05ModelF0V_AC0H0VSgSayAC9CandidateVGAA5UsageVSDySSypGAA0C0V9RenderingVSgtcfC
- _$s15TokenGeneration16PromptCompletionV7SegmentV7contentAeC7ContentO_tcfC
- _$s15TokenGeneration16PromptCompletionV7SegmentVMn
- _$s15TokenGeneration16PromptCompletionV9CandidateV8segments9toolCalls10moderation12finishReason8metadataAESayAC7SegmentVG_SayAA0C0V8ToolCallVGAC10ModerationVSgAA06FinishK0OSDySSypGtcfC
- _$s15TokenGeneration16PromptCompletionV9CandidateV8segmentsSayAC7SegmentVGvM
- _$s15TokenGeneration21PromptCompletionEventMp
- _$s15TokenGeneration22PromptCompletionStreamV13AsyncIteratorVMa
- _$s15TokenGeneration22PromptCompletionStreamV13AsyncIteratorVScIAAMc
- _$s15TokenGeneration22PromptCompletionStreamV17makeAsyncIteratorAC0gH0VyF
- _$s15TokenGeneration37PromptCompletionEventModelInformationV05modelG0AA0fG0Vvg
- _$s15TokenGeneration37PromptCompletionEventModelInformationVMa
- _$s15TokenGeneration37PromptCompletionEventResponseMetadataV8metadataSDySSypGvg
- _$s15TokenGeneration37PromptCompletionEventResponseMetadataVMa
- _$s15TokenGeneration39PromptCompletionEventCandidateTextDeltaV04textH0SSvg
- _$s15TokenGeneration39PromptCompletionEventCandidateTextDeltaVMa
- _$s15TokenGeneration39PromptCompletionEventCandidateTextDeltaVMn
- _$s15TokenGeneration43PromptCompletionEventCandidateToolCallDeltaV04toolH10IdentifierSSvg
- _$s15TokenGeneration43PromptCompletionEventCandidateToolCallDeltaV12functionNameSSvg
- _$s15TokenGeneration43PromptCompletionEventCandidateToolCallDeltaVMa
- _$s15TokenGeneration5UsageV06promptA5Count010completionaE0ACSi_SitcfC
- _$s15TokenGeneration5UsageVMa
- _$s15TokenGeneration6PromptV8ToolCallV2id8functionAESS_AE8FunctionVtcfC
- _$s15TokenGeneration6PromptV8ToolCallV8FunctionV4name9argumentsAGSS_SStcfC
- _$s15TokenGeneration6PromptV8ToolCallV8FunctionVMa
- _$s15TokenGeneration6PromptV8ToolCallVMa
- _$s15TokenGeneration6PromptV8ToolCallVMn
- _$s15TokenGeneration6PromptV9RenderingV8tokenIDsSaySiGvg
- _$s15TokenGeneration6PromptV9RenderingVMa
- _$s15TokenGeneration6PromptV9RenderingVMn
- _$sSS14removeSubrangeyySnySS5IndexVGF
- _$sScI4next7ElementQzSgyYaKFTj
- _$sScI4next7ElementQzSgyYaKFTjTu
- _swift_willThrowTypedImpl
CStrings:
+ "Finished collecting token stream"
- "    {\n        \"body\": \""
- "\",\n        \"refinements\": []\n    }"
- "\",\"refinements\":[\""
- "Finished collecting completion"
- "The chunk isn't valid markdown"
- "body content was not valid json"
- "completion could not be generated"

```

#### AXMotionCuesServer

>  `/System/Library/AccessibilityBundles/AXMotionCuesServer.axuiservice/AXMotionCuesServer`

```diff

-3148.7.15.1.0
+3148.7.15.2.0
   __TEXT.__text: 0x1e284
   __TEXT.__auth_stubs: 0xf80
   __TEXT.__objc_stubs: 0xe0

   __TEXT.__eh_frame: 0x888
   __DATA_CONST.__auth_got: 0x7d0
   __DATA_CONST.__got: 0x260
-  __DATA_CONST.__auth_ptr: 0x218
+  __DATA_CONST.__auth_ptr: 0x210
   __DATA_CONST.__const: 0x1150
   __DATA_CONST.__cfstring: 0x60
   __DATA_CONST.__objc_classlist: 0xc0

```

#### LiveSpeechUIService

>  `/System/Library/AccessibilityBundles/LiveSpeechUIService.axuiservice/LiveSpeechUIService`

```diff

-3148.7.15.1.0
+3148.7.15.2.0
   __TEXT.__text: 0x9f64c
   __TEXT.__auth_stubs: 0x2bb0
   __TEXT.__objc_stubs: 0xa0

   __TEXT.__eh_frame: 0x1350
   __DATA_CONST.__auth_got: 0x15e8
   __DATA_CONST.__got: 0xbb8
-  __DATA_CONST.__auth_ptr: 0xca0
+  __DATA_CONST.__auth_ptr: 0xc90
   __DATA_CONST.__const: 0x3380
   __DATA_CONST.__cfstring: 0x40
   __DATA_CONST.__objc_classlist: 0x88

```

#### powerd

>  `/System/Library/CoreServices/powerd.bundle/powerd`

```diff

-1740.80.3.0.0
-  __TEXT.__text: 0x67f34
+1740.82.1.0.0
+  __TEXT.__text: 0x67ecc
   __TEXT.__auth_stubs: 0x1b90
   __TEXT.__objc_stubs: 0x4920
   __TEXT.__objc_methlist: 0x2278
   __TEXT.__const: 0x3f8
-  __TEXT.__cstring: 0x640f
+  __TEXT.__cstring: 0x6401
   __TEXT.__objc_methname: 0x6035
-  __TEXT.__oslogstring: 0xb78b
+  __TEXT.__oslogstring: 0xb78c
   __TEXT.__objc_classname: 0x2fe
   __TEXT.__objc_methtype: 0x81e
   __TEXT.__gcc_except_tab: 0x498

   __TEXT.__unwind_info: 0x11a8
   __DATA_CONST.__auth_got: 0xdd8
   __DATA_CONST.__got: 0x378
-  __DATA_CONST.__const: 0x23f8
-  __DATA_CONST.__cfstring: 0x6d60
+  __DATA_CONST.__const: 0x23d8
+  __DATA_CONST.__cfstring: 0x6d40
   __DATA_CONST.__objc_classlist: 0x98
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA.__objc_data: 0x5f0
   __DATA.__data: 0xa0c
   __DATA.__common: 0x1138
-  __DATA.__bss: 0xb60
+  __DATA.__bss: 0xb50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMotion.framework/CoreMotion
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libenergytrace.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2175
+  Functions: 2173
   Symbols:   562
-  CStrings:  3584
+  CStrings:  3583
 
CStrings:
+ "calib0: device not relevant"
- "InternalBuild"
- "calib: device not relevant"

```

#### iMessage

>  `/System/Library/Messages/PlugIns/iMessage.imservice/iMessage`

```diff

-1402.400.131.2.4
-  __TEXT.__text: 0x91cfc
+1402.400.131.2.6
+  __TEXT.__text: 0x91d68
   __TEXT.__auth_stubs: 0x1380
   __TEXT.__objc_stubs: 0xb180
   __TEXT.__objc_methlist: 0x2164
   __TEXT.__const: 0x37e
-  __TEXT.__gcc_except_tab: 0xa668
+  __TEXT.__gcc_except_tab: 0xa674
   __TEXT.__cstring: 0x2fad
-  __TEXT.__oslogstring: 0x13ea6
+  __TEXT.__oslogstring: 0x13ee6
   __TEXT.__objc_classname: 0x4e2
   __TEXT.__objc_methname: 0x102d4
   __TEXT.__objc_methtype: 0x2779

   - /usr/lib/swift/libswiftunistd.dylib
   Functions: 1175
   Symbols:   778
-  CStrings:  4158
+  CStrings:  4159
 
CStrings:
+ "Being requested to re-send a message that wasn't sent by me"
+ "md-decryption-failure-retries-per-week-v2"
- "md-decryption-failure-retries-per-week"

```

#### SafetyMonitorMessages

>  `/System/Library/Messages/iMessageApps/SafetyMonitorMessages.bundle/SafetyMonitorMessages`

```diff

 986.0.1.0.0
-  __TEXT.__text: 0x12474
+  __TEXT.__text: 0x124c8
   __TEXT.__auth_stubs: 0xda0
   __TEXT.__objc_methlist: 0xc8
   __TEXT.__swift5_typeref: 0x1b6

```

#### identityservicesd

>  `/System/Library/PrivateFrameworks/IDS.framework/identityservicesd.app/identityservicesd`

```diff

-1926.400.131.2.1
-  __TEXT.__text: 0x7215c0
+1926.400.131.2.2
+  __TEXT.__text: 0x7215cc
   __TEXT.__auth_stubs: 0x54d0
   __TEXT.__objc_stubs: 0x44ee0
   __TEXT.__objc_methlist: 0x242f4

   __TEXT.__eh_frame: 0x4d6c
   __DATA_CONST.__auth_got: 0x2a78
   __DATA_CONST.__got: 0x3380
-  __DATA_CONST.__auth_ptr: 0x620
+  __DATA_CONST.__auth_ptr: 0x6c0
   __DATA_CONST.__const: 0x1c868
   __DATA_CONST.__cfstring: 0x33bc0
   __DATA_CONST.__objc_classlist: 0xea0
CStrings:
+ "18:04:23"
+ "Feb  2 2025"
- "04:45:37"
- "Jan 16 2025"

```

#### applekeystored

>  `/usr/libexec/applekeystored`

```diff

   __TEXT.__eh_frame: 0x21e8
   __DATA_CONST.__auth_got: 0xbe8
   __DATA_CONST.__got: 0x358
-  __DATA_CONST.__auth_ptr: 0x758
+  __DATA_CONST.__auth_ptr: 0x718
   __DATA_CONST.__const: 0x7a50
   __DATA_CONST.__objc_classlist: 0xb8
   __DATA_CONST.__objc_protolist: 0x30

```

#### profiled

>  `/usr/libexec/profiled`

```diff

-2381.2.7.5.0
-  __TEXT.__text: 0x9d958
+2381.2.7.5.2
+  __TEXT.__text: 0x9da1c
   __TEXT.__auth_stubs: 0x2130
   __TEXT.__objc_stubs: 0xfaa0
   __TEXT.__objc_methlist: 0x4ca4
   __TEXT.__const: 0x148
   __TEXT.__gcc_except_tab: 0x194c
   __TEXT.__oslogstring: 0xcba3
-  __TEXT.__cstring: 0x8b71
+  __TEXT.__cstring: 0x8b95
   __TEXT.__objc_methname: 0x133fe
   __TEXT.__objc_classname: 0xb36
   __TEXT.__objc_methtype: 0x203d
   __TEXT.__unwind_info: 0x16a0
   __DATA_CONST.__auth_got: 0x10a8
-  __DATA_CONST.__got: 0x1b90
+  __DATA_CONST.__got: 0x1b98
   __DATA_CONST.__const: 0x1b38
-  __DATA_CONST.__cfstring: 0x8340
+  __DATA_CONST.__cfstring: 0x8360
   __DATA_CONST.__objc_classlist: 0x2c8
   __DATA_CONST.__objc_catlist: 0x1e8
   __DATA_CONST.__objc_protolist: 0x68

   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 1923
-  Symbols:   1459
-  CStrings:  4893
+  Symbols:   1460
+  CStrings:  4894
 
Symbols:
+ _MCSettingsErrorDomain
CStrings:
+ "SETTINGS_DEVICE_IS_LOCKED_P_SETTING"

```

#### searchpartyd

>  `/usr/libexec/searchpartyd`

```diff

-396.33.10.29.8
-  __TEXT.__text: 0x13376d0
+396.33.10.29.9
+  __TEXT.__text: 0x13377c4
   __TEXT.__auth_stubs: 0x7030
   __TEXT.__objc_stubs: 0xa0
   __TEXT.__objc_methlist: 0x159c

   __TEXT.__objc_methtype: 0x477e
   __TEXT.__cstring: 0x39d0d
   __TEXT.__swift5_typeref: 0x20c96
-  __TEXT.__swift5_fieldmd: 0x1f97c
+  __TEXT.__swift5_fieldmd: 0x1f988
   __TEXT.__constg_swiftt: 0x1ca50
   __TEXT.__swift5_builtin: 0x898
-  __TEXT.__swift5_reflstr: 0x1d6af
+  __TEXT.__swift5_reflstr: 0x1d6cf
   __TEXT.__swift5_assocty: 0x2478
   __TEXT.__swift5_protos: 0x2d0
   __TEXT.__swift5_proto: 0x5220

   __TEXT.__eh_frame: 0x94924
   __DATA_CONST.__auth_got: 0x3820
   __DATA_CONST.__got: 0x2b80
-  __DATA_CONST.__auth_ptr: 0x50b0
+  __DATA_CONST.__auth_ptr: 0x4d98
   __DATA_CONST.__const: 0x72560
   __DATA_CONST.__cfstring: 0x40
   __DATA_CONST.__objc_classlist: 0x748

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 59885
+  Functions: 59886
   Symbols:   3467
   CStrings:  12555
 

```


</details>

### 🔑 Entitlements

- [Entitlements DIFF](Entitlements.md)

## Firmware

### ⬆️ Updated (1)

<details>
  <summary><i>View Updated</i></summary>

#### exclave_sharedcache

>  `exclave_sharedcache`

```diff

 460.80.5.0.0
-  __TEXT.__text: 0x4c2bd4
+  __TEXT.__text: 0x4c295c
   __TEXT.__lcxx_override: 0x200
   __TEXT.__cstring: 0x30b5f
   __TEXT.__const: 0xe2768

   __TEXT.__term_offsets: 0x0
   __TEXT.__swift5_replace: 0x0
   __TEXT.__thread_starts: 0x3c
-  __TEXT.__eh_frame: 0x23a7c
+  __TEXT.__eh_frame: 0x23abc
   __DATA.__got: 0x18
   __DATA.__auth_ptr: 0x280
   __DATA.__mod_init_func: 0x38

   __PDATA.__common: 0x1fc0
   __DATA_CONST.__mod_init_func: 0x0
   __DATA_CONST.__mod_term_func: 0x0
-  Functions: 18498
+  Functions: 18494
   Symbols:   0
   CStrings:  5151
 

```


</details>

## DSC

### WebKit

| iOS | Version |
| :-- | :------ |
| 18.3 *(22D63)* | 620.2.4.10.7 |
| 18.3.1 *(22D72)* | 620.2.4.10.7 |

### Dylibs

#### ⬆️ Updated (10)

<details>
  <summary><i>View Updated</i></summary>

#### _MapKit_SwiftUI

>  `/System/Library/Frameworks/_MapKit_SwiftUI.framework/_MapKit_SwiftUI`

```diff

   __DATA_CONST.__objc_selrefs: 0x6f0
   __DATA_CONST.__objc_protorefs: 0x48
   __AUTH_CONST.__auth_got: 0x10c8
-  __AUTH_CONST.__auth_ptr: 0x1040
+  __AUTH_CONST.__auth_ptr: 0x1068
   __AUTH_CONST.__const: 0x7270
   __AUTH_CONST.__objc_const: 0x2158
   __AUTH.__objc_data: 0x7a0

```

#### AXSpringBoardServerInstance

>  `/System/Library/PrivateFrameworks/AXSpringBoardServerInstance.framework/AXSpringBoardServerInstance`

```diff

-3148.7.15.1.0
-  __TEXT.__text: 0x3f104
+3148.7.15.2.0
+  __TEXT.__text: 0x3f150
   __TEXT.__auth_stubs: 0x1810
   __TEXT.__objc_methlist: 0x25e0
   __TEXT.__const: 0x534
   __TEXT.__cstring: 0x65fb
   __TEXT.__gcc_except_tab: 0xd58
-  __TEXT.__oslogstring: 0x14c6
+  __TEXT.__oslogstring: 0x1506
   __TEXT.__dlopen_cstrs: 0x2a2
   __TEXT.__swift5_typeref: 0x212
   __TEXT.__swift5_capture: 0xf0

   - /usr/lib/swift/libswiftunistd.dylib
   Functions: 1417
   Symbols:   1989
-  CStrings:  2689
+  CStrings:  2690
 
CStrings:
+ "Not showing USB restricted mode alert because device is locked"

```

#### AccessibilitySettingsUI

>  `/System/Library/PrivateFrameworks/AccessibilitySettingsUI.framework/AccessibilitySettingsUI`

```diff

-3148.7.15.1.0
+3148.7.15.2.0
   __TEXT.__text: 0xc0224
   __TEXT.__auth_stubs: 0x2d00
   __TEXT.__objc_methlist: 0x110

   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x8
   __AUTH_CONST.__auth_got: 0x1690
-  __AUTH_CONST.__auth_ptr: 0xd70
+  __AUTH_CONST.__auth_ptr: 0xdb0
   __AUTH_CONST.__const: 0x35a8
   __AUTH_CONST.__cfstring: 0x140
   __AUTH_CONST.__objc_const: 0xfb8

```

#### AssistiveTouchUI

>  `/System/Library/PrivateFrameworks/AssistiveTouchUI.framework/AssistiveTouchUI`

```diff

-3148.7.15.1.0
+3148.7.15.2.0
   __TEXT.__text: 0xdee4
   __TEXT.__auth_stubs: 0xd70
   __TEXT.__objc_methlist: 0x3a0

   __DATA_CONST.__objc_superrefs: 0x18
   __DATA_CONST.__objc_arraydata: 0x80
   __AUTH_CONST.__auth_got: 0x6c8
-  __AUTH_CONST.__auth_ptr: 0x370
+  __AUTH_CONST.__auth_ptr: 0x368
   __AUTH_CONST.__const: 0x8d0
   __AUTH_CONST.__cfstring: 0x1a0
   __AUTH_CONST.__objc_const: 0xda8

```

#### ChatKit

>  `/System/Library/PrivateFrameworks/ChatKit.framework/ChatKit`

```diff

-1402.400.131.2.4
+1402.400.131.2.6
   __TEXT.__text: 0x89c46c
   __TEXT.__auth_stubs: 0x8bb0
   __TEXT.__delay_helper: 0x190

   __DATA_CONST.__objc_superrefs: 0x19a0
   __DATA_CONST.__objc_arraydata: 0x1040
   __AUTH_CONST.__auth_got: 0x45e8
-  __AUTH_CONST.__auth_ptr: 0x3808
+  __AUTH_CONST.__auth_ptr: 0x37b8
   __AUTH_CONST.__const: 0x26330
   __AUTH_CONST.__cfstring: 0x24320
   __AUTH_CONST.__objc_const: 0xa4470

```

#### FMNetworking

>  `/System/Library/PrivateFrameworks/FMNetworking.framework/FMNetworking`

```diff

-396.33.10.29.8
+396.33.10.29.9
   __TEXT.__text: 0x3edb8
   __TEXT.__auth_stubs: 0x1370
   __TEXT.__objc_methlist: 0xb8

   __DATA_CONST.__objc_selrefs: 0x1e8
   __DATA_CONST.__objc_protorefs: 0x18
   __AUTH_CONST.__auth_got: 0x9b8
-  __AUTH_CONST.__auth_ptr: 0x2e8
+  __AUTH_CONST.__auth_ptr: 0x2f0
   __AUTH_CONST.__const: 0x2c78
   __AUTH_CONST.__objc_const: 0xee0
   __AUTH.__objc_data: 0x1a0

```

#### IMSharedUtilities

>  `/System/Library/PrivateFrameworks/IMSharedUtilities.framework/IMSharedUtilities`

```diff

-1402.400.131.2.4
+1402.400.131.2.6
   __TEXT.__text: 0x27f9bc
   __TEXT.__auth_stubs: 0x3e70
   __TEXT.__objc_methlist: 0x109e8

   __DATA_CONST.__objc_superrefs: 0x530
   __DATA_CONST.__objc_arraydata: 0x6b8
   __AUTH_CONST.__auth_got: 0x1f48
-  __AUTH_CONST.__auth_ptr: 0x13e0
+  __AUTH_CONST.__auth_ptr: 0x13b0
   __AUTH_CONST.__const: 0xd8e8
   __AUTH_CONST.__cfstring: 0x19d40
   __AUTH_CONST.__objc_const: 0x20fa0

```

#### MessagesCloudSync

>  `/System/Library/PrivateFrameworks/MessagesCloudSync.framework/MessagesCloudSync`

```diff

-1402.400.131.2.4
+1402.400.131.2.6
   __TEXT.__text: 0x111ea4
   __TEXT.__auth_stubs: 0x1f20
   __TEXT.__objc_methlist: 0x610

   __DATA_CONST.__objc_protorefs: 0x88
   __DATA_CONST.__objc_superrefs: 0x10
   __AUTH_CONST.__auth_got: 0xf98
-  __AUTH_CONST.__auth_ptr: 0xae8
+  __AUTH_CONST.__auth_ptr: 0xa90
   __AUTH_CONST.__const: 0x8678
   __AUTH_CONST.__cfstring: 0x60
   __AUTH_CONST.__objc_const: 0x2db8

```

#### ProactiveSummarization

>  `/System/Library/PrivateFrameworks/ProactiveSummarization.framework/ProactiveSummarization`

```diff

-1271.10.0.0.0
-  __TEXT.__text: 0x121838
+1271.11.0.0.0
+  __TEXT.__text: 0x123ef4
   __TEXT.__auth_stubs: 0x33d0
   __TEXT.__objc_methlist: 0x284
-  __TEXT.__const: 0xacb0
-  __TEXT.__oslogstring: 0x61a0
-  __TEXT.__swift5_typeref: 0x355c
-  __TEXT.__swift5_fieldmd: 0x2ea8
-  __TEXT.__constg_swiftt: 0x2808
-  __TEXT.__cstring: 0x7763
+  __TEXT.__const: 0xb3c0
+  __TEXT.__oslogstring: 0x6570
+  __TEXT.__swift5_typeref: 0x36a8
+  __TEXT.__swift5_fieldmd: 0x2fc8
+  __TEXT.__constg_swiftt: 0x28e0
+  __TEXT.__cstring: 0x79c3
   __TEXT.__swift5_capture: 0xe9c
-  __TEXT.__swift5_reflstr: 0x2bbd
+  __TEXT.__swift5_reflstr: 0x2d3d
   __TEXT.__swift5_protos: 0x38
-  __TEXT.__swift5_proto: 0x9ec
-  __TEXT.__swift5_types: 0x3f4
+  __TEXT.__swift5_proto: 0xa54
+  __TEXT.__swift5_types: 0x40c
   __TEXT.__swift5_builtin: 0x104
   __TEXT.__swift5_mpenum: 0x4c
   __TEXT.__swift5_assocty: 0x240
   __TEXT.__gcc_except_tab: 0xfc
   __TEXT.__dlopen_cstrs: 0x56
-  __TEXT.__unwind_info: 0x4fe0
-  __TEXT.__eh_frame: 0xcca0
+  __TEXT.__unwind_info: 0x50a0
+  __TEXT.__eh_frame: 0xcc78
   __TEXT.__objc_classname: 0x1a8
   __TEXT.__objc_methname: 0x2511
   __TEXT.__objc_methtype: 0x3f3

   __DATA_CONST.__objc_superrefs: 0x18
   __AUTH_CONST.__auth_got: 0x19f8
   __AUTH_CONST.__auth_ptr: 0x8c0
-  __AUTH_CONST.__const: 0x6f08
+  __AUTH_CONST.__const: 0x7188
   __AUTH_CONST.__cfstring: 0x80
   __AUTH_CONST.__objc_const: 0x2d98
   __AUTH.__objc_data: 0x258
   __AUTH.__data: 0xd78
   __DATA.__objc_ivar: 0x14
-  __DATA.__data: 0x25b8
-  __DATA.__bss: 0x13cb0
+  __DATA.__data: 0x2618
+  __DATA.__bss: 0x14a80
   __DATA.__common: 0x168
   __DATA_DIRTY.__objc_data: 0x360
   __DATA_DIRTY.__data: 0xd78

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 7062
-  Symbols:   3548
-  CStrings:  1556
+  Functions: 7155
+  Symbols:   3582
+  CStrings:  1577
 
CStrings:
+ "Could not load summarization bundleIds deny list plist: %@; proceeding with empty set"
+ "Could not load summarization categories plist: %@; proceeding with empty set"
+ "Notification not eligible for summarization (bundleId not allowed); bundle: %{public}s"
+ "Notification not eligible for summarization (iTunes category not allowed); bundle: %{public}s iTunes category: %{public}ld"
+ "Notification not eligible for summarization (no bundle): %{public}s"
+ "Notification stack has no app bundleId"
+ "Notification stack not eligible for summarization (bundleId not allowed); bundle: %{public}s"
+ "Notification stack not eligible for summarization (iTunes category not allowed); bundle: %{public}s iTunes category: %{public}ld"
+ "Notification stack not eligible for summarization (no bundle): %{public}s"
+ "Notification stack's bundleId is not allowed: "
+ "Notification stack's iTunes category is not allowed: "
+ "SummarizationBundleIdsDenyList"
+ "SummarizationCategoriesDenyList"
+ "The summarization bundleIds deny list plist exists but is missing a DeniedBundleIds key"
+ "The summarization categories plist exists but is missing a DeniedCategories key"
+ "summarizationFilter_notificationStack_ineligibleBundleId"
+ "summarizationFilter_notificationStack_ineligibleItunesCategory"
+ "summarizationFilter_notificationStack_missingBundleId"
+ "summarizationFilter_notification_ineligibleBundleId"
+ "summarizationFilter_notification_ineligibleItunesCategory"
+ "summarizationFilter_notification_missingBundleId"

```

#### SafetyMonitorUI

>  `/System/Library/PrivateFrameworks/SafetyMonitorUI.framework/SafetyMonitorUI`

```diff

   __DATA_CONST.__objc_selrefs: 0xdc8
   __DATA_CONST.__objc_protorefs: 0x50
   __AUTH_CONST.__auth_got: 0x1788
-  __AUTH_CONST.__auth_ptr: 0x1460
+  __AUTH_CONST.__auth_ptr: 0x1458
   __AUTH_CONST.__const: 0x69e8
   __AUTH_CONST.__objc_const: 0x3438
   __AUTH.__objc_data: 0x2220

```


</details>

## EOF
