## PreviewsInjection

> `/System/Library/PrivateFrameworks/PreviewsInjection.framework/PreviewsInjection`

```diff

-22.40.1.0.0
-  __TEXT.__text: 0x779c8
-  __TEXT.__auth_stubs: 0x2f70
+23.0.41.0.0
+  __TEXT.__text: 0x78600
+  __TEXT.__auth_stubs: 0x30b0
   __TEXT.__objc_methlist: 0x1c4
-  __TEXT.__const: 0x4420
-  __TEXT.__cstring: 0x2425
-  __TEXT.__constg_swiftt: 0x20d0
-  __TEXT.__swift5_typeref: 0x23ff
-  __TEXT.__swift5_fieldmd: 0x11e0
+  __TEXT.__const: 0x4bf8
+  __TEXT.__cstring: 0x27a5
+  __TEXT.__constg_swiftt: 0x2040
+  __TEXT.__swift5_typeref: 0x24e5
+  __TEXT.__swift5_fieldmd: 0x1224
   __TEXT.__swift5_reflstr: 0xf83
-  __TEXT.__swift5_assocty: 0x548
-  __TEXT.__swift5_capture: 0x340
-  __TEXT.__oslogstring: 0x1445
+  __TEXT.__swift5_assocty: 0x550
+  __TEXT.__swift5_capture: 0x39c
+  __TEXT.__oslogstring: 0x16c8
   __TEXT.__swift5_builtin: 0x78
-  __TEXT.__swift5_proto: 0x290
-  __TEXT.__swift5_types: 0x1a4
-  __TEXT.__swift_as_entry: 0x248
+  __TEXT.__swift5_proto: 0x294
+  __TEXT.__swift5_types: 0x1ac
+  __TEXT.__swift_as_entry: 0x24c
   __TEXT.__swift_as_ret: 0x1b4
-  __TEXT.__swift5_protos: 0x60
+  __TEXT.__swift5_protos: 0x58
   __TEXT.__swift5_mpenum: 0x20
-  __TEXT.__unwind_info: 0x2198
-  __TEXT.__eh_frame: 0x5170
+  __TEXT.__unwind_info: 0x20e0
+  __TEXT.__eh_frame: 0x5240
   __TEXT.__objc_classname: 0x5e
   __TEXT.__objc_methname: 0x61d
   __TEXT.__objc_methtype: 0x12c
   __TEXT.__objc_stubs: 0x120
-  __DATA_CONST.__got: 0x960
-  __DATA_CONST.__const: 0x150
+  __DATA_CONST.__got: 0x9c8
+  __DATA_CONST.__const: 0x138
   __DATA_CONST.__objc_classlist: 0xb0
   __DATA_CONST.__objc_nlclslist: 0x8
   __DATA_CONST.__objc_catlist: 0x8

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x2e0
   __DATA_CONST.__objc_protorefs: 0x10
-  __AUTH_CONST.__auth_got: 0x17c0
-  __AUTH_CONST.__const: 0x1fb0
-  __AUTH_CONST.__objc_const: 0x1568
+  __AUTH_CONST.__auth_got: 0x1860
+  __AUTH_CONST.__const: 0x2110
+  __AUTH_CONST.__objc_const: 0x14e0
   __AUTH.__objc_data: 0x138
-  __AUTH.__data: 0x20e0
-  __DATA.__data: 0x1ee8
-  __DATA.__bss: 0x4b10
+  __AUTH.__data: 0x2140
+  __DATA.__data: 0x1830
+  __DATA.__bss: 0x4c20
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0xd8
-  __DATA_DIRTY.__data: 0x258
+  __DATA_DIRTY.__data: 0x260
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/DeveloperToolsSupport.framework/DeveloperToolsSupport

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
+  - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
-  - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib

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
-  UUID: BB57A5C3-77A9-3EF8-A449-7F459B002DBF
-  Functions: 2381
-  Symbols:   1162
-  CStrings:  423
+  UUID: 19F5B26A-2497-3434-B247-4FFAB3B36FBC
+  Functions: 2396
+  Symbols:   1163
+  CStrings:  449
 
Symbols:
+ ____abort_timed_out_waiting_for_previews_jit_first_link_signal
+ ___swift_memcpy56_8
+ ___unnamed_11
+ ___unnamed_8
+ __dyld_is_pseudodylib
+ __swift_FORCE_LOAD_$_swiftCoreAudio
+ __swift_FORCE_LOAD_$_swiftCoreAudio_$_PreviewsInjection
+ __swift_FORCE_LOAD_$_swiftCoreMedia
+ __swift_FORCE_LOAD_$_swiftCoreMedia_$_PreviewsInjection
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_PreviewsInjection
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_PreviewsInjection
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_PreviewsInjection
+ _associated conformance 17PreviewsInjection24AssistiveAccessTransform33_B9327E8BE2A65479722DED6464165561LLV7SwiftUI12ViewModifierAA4BodyAeFP_AE0M0
+ _associated conformance 21DeveloperToolsSupport11_PlaygroundV16PreviewsServices18RegistryExecutable0E9Injection12ControlEventAdEP_SE
+ _associated conformance 21DeveloperToolsSupport11_PlaygroundV16PreviewsServices18RegistryExecutable0E9Injection12ControlEventAdEP_Se
+ _get_enum_tag_for_layout_string 17PreviewsInjection13JITLinkWaiterO5StateO
+ _get_enum_tag_for_layout_string 17PreviewsInjection17JITExecutorWaiterO5StateO
+ _get_witness_table 17PreviewsInjection15HostingParadigmRzl7SwiftUI15ModifiedContentVyAEyAC4ViewPACE22configuredForSceneRootQryFQOyAEyAC012_ConditionalH0VyAA07MetricsI0VAC03AnyI0VGAA23AllowAnimationsModifier33_615F4C6B56138203A5D5D631B996DBA5LLVG_Qo_AC022_EnvironmentKeyWritingS0VySbGG04HostS0QzGAcFHPAxcFHPqd__AcFHD2_ATHO_AwC0iS0HPyHCHC_xAaBHD1_AzCA0_HA0_HC.17
+ _get_witness_table 17PreviewsInjection15HostingParadigmRzl7SwiftUI9EmptyViewVAC0H0HPyHC.21
+ _get_witness_table 7SwiftUI15ModifiedContentVyAA014_ViewModifier_D0VyAA11ColorSchemeO17PreviewsInjectionE9Transform33_B9327E8BE2A65479722DED6464165561LLVGAA018_PreferenceWritingF0VyAA09PreferredgH3KeyVGGAA0E0HPAlaSHPyHC_AqA0eF0HPyHCHC.44
+ _get_witness_table 7SwiftUI19_ConditionalContentVyAA014_ViewModifier_D0Vy17PreviewsInjection015AllowAnimationsF033_615F4C6B56138203A5D5D631B996DBA5LLVGAA0E0PAAE12unanimatableQryFQOyAJ_Qo_GAaKHPAjaKHPyHC_qd__AaKHD2_ANHOHC.20
+ _get_witness_table 7SwiftUI21_ViewModifier_ContentVy19PreviewsMessagingOS13PreviewTraitsV11OrientationO0F9InjectionE9Transform33_B9327E8BE2A65479722DED6464165561LLVGAA0C0HPyHC.47
+ _get_witness_table qd__7SwiftUI4ViewHD2_AaBPAAE14clarityUIIdiomQryFQOyAA01_C16Modifier_ContentVy17PreviewsInjection24AssistiveAccessTransform33_B9327E8BE2A65479722DED6464165561LLVG_Qo_HO.43
+ _get_witness_table qd__7SwiftUI4ViewHD2_AaBPAAE14clarityUIIdiomQryFQOyAA01_C16Modifier_ContentVy17PreviewsInjection24AssistiveAccessTransform33_B9327E8BE2A65479722DED6464165561LLVG_Qo_HOTm
+ _get_witness_table qd__7SwiftUI4ViewHD2_AaBPAAE15dynamicTypeSizeyQrAA07DynamiceF0OFQOyAA01_C16Modifier_ContentVyAF17PreviewsInjectionE9Transform33_B9327E8BE2A65479722DED6464165561LLVG_Qo_HO.46
+ _swift_coroFrameAlloc
+ _swift_initStackObject
+ _symbolic Ieg_
+ _symbolic SDy__________G 19PreviewsMessagingOS31MessageStreamInstanceIdentifierV 0A9Injection0E11Placeholder33_4D960DEADBC44D786C0400B9EA4B19DBLLV
+ _symbolic SaySSG
+ _symbolic SaySo18NSLayoutConstraintCG
+ _symbolic _____ 13XOJITExecutorAAC
+ _symbolic _____ 17PreviewsInjection13JITLinkWaiterO
+ _symbolic _____ 17PreviewsInjection13JITLinkWaiterO5StateO
+ _symbolic _____ 17PreviewsInjection17JITExecutorWaiterO
+ _symbolic _____ 17PreviewsInjection17JITExecutorWaiterO5StateO
+ _symbolic _____ 17PreviewsInjection17StreamPlaceholder33_4D960DEADBC44D786C0400B9EA4B19DBLLV
+ _symbolic _____ 17PreviewsInjection17StreamPlaceholder33_4D960DEADBC44D786C0400B9EA4B19DBLLV5StateO
+ _symbolic _____ 17PreviewsInjection24AssistiveAccessTransform33_B9327E8BE2A65479722DED6464165561LLV
+ _symbolic _____4type_SSSg11displayNamet 19PreviewsMessagingOS12RegistryTypeV
+ _symbolic _____Ieghn_ 20PreviewsFoundationOS12PropertyListV
+ _symbolic _____Sg 20PreviewsFoundationOS12TimingRecordV2IDV
+ _symbolic ___________t 19PreviewsMessagingOS31MessageStreamInstanceIdentifierV 0A9Injection0E11Placeholder33_4D960DEADBC44D786C0400B9EA4B19DBLLV
+ _symbolic _____yAAyAAy_____y_____y_____Sg_ADtGG_____y_____SgGG_____GAMG 7SwiftUI15ModifiedContentV AA6VStackV AA9TupleViewV AA4TextV AA30_EnvironmentKeyWritingModifierV AA4FontV AA14_PaddingLayoutV
+ _symbolic _____yAAy__________y_____GG_____G 7SwiftUI15ModifiedContentV AA4TextV AA24_BackgroundStyleModifierV AA5ColorV AA13_OffsetEffectV
+ _symbolic _____yAAy_____yAAy_____y__________G_____G_Qo______ySbGG12HostModifier_____QzG 7SwiftUI15ModifiedContentV AA4ViewPAAE22configuredForSceneRootQryFQO AA012_ConditionalD0V 17PreviewsInjection07MetricsE0V AA03AnyE0V AI23AllowAnimationsModifier33_615F4C6B56138203A5D5D631B996DBA5LLV AA022_EnvironmentKeyWritingQ0V AI15HostingParadigmP
+ _symbolic _____yAAy_____y__________G_____y_____yAcD_____GGG_____G 7SwiftUI15ModifiedContentV AA10_ShapeViewV 17PreviewsInjection5ArrowV AA5ColorV AA16_OverlayModifierV AA06StrokeeF0V AA05EmptyF0V AA16_FlexFrameLayoutV
+ _symbolic _____ySSG s23_ContiguousArrayStorageC
+ _symbolic _____y_____G 19PreviewsMessagingOS13RuntimeLookupO AA13PreviewFlavorO
+ _symbolic _____y_____G 2os21OSAllocatedUnfairLockV 17PreviewsInjection17StreamPlaceholder33_4D960DEADBC44D786C0400B9EA4B19DBLLV5StateO
+ _symbolic _____y_____G 7SwiftUI21_ViewModifier_ContentV 17PreviewsInjection24AssistiveAccessTransform33_B9327E8BE2A65479722DED6464165561LLV
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 19PreviewsMessagingOS12RenderEffectV
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 7SwiftUI4EdgeO3SetV
+ _symbolic _____y______A2B_____tG 7SwiftUI9TupleViewV AA4TextV AA6SpacerV
+ _symbolic _____y______ABtG 7SwiftUI9TupleViewV 17PreviewsInjection05ArrowD0V
+ _symbolic _____y__________G s18_DictionaryStorageC 19PreviewsMessagingOS31MessageStreamInstanceIdentifierV 0C9Injection0G11Placeholder33_4D960DEADBC44D786C0400B9EA4B19DBLLV
+ _symbolic _____y___________pG s6ResultOsRi_zRi0_zrlE 20PreviewsFoundationOS12PropertyListV s5ErrorP
+ _symbolic _____y___________yACyACy_____yAAy_____Sg_AEtGG_____y_____SgGG_____GANGtG 7SwiftUI9TupleViewV AA5ColorV AA15ModifiedContentV AA6VStackV AA4TextV AA30_EnvironmentKeyWritingModifierV AA4FontV AA14_PaddingLayoutV
+ _symbolic _____y_____yAAy_____y__________G_____G_Qo______ySbGG 7SwiftUI15ModifiedContentV AA4ViewPAAE22configuredForSceneRootQryFQO AA012_ConditionalD0V 17PreviewsInjection07MetricsE0V AA03AnyE0V AI23AllowAnimationsModifier33_615F4C6B56138203A5D5D631B996DBA5LLV AA022_EnvironmentKeyWritingQ0V
+ _symbolic _____y_____y_____G_Qo_ 7SwiftUI4ViewPAAE14clarityUIIdiomQryFQO AA01_C16Modifier_ContentV 17PreviewsInjection24AssistiveAccessTransform33_B9327E8BE2A65479722DED6464165561LLV
+ _symbolic _____y_____y_______________GG 7SwiftUI16_OverlayModifierV AA15StrokeShapeViewV 17PreviewsInjection5ArrowV AA5ColorV AA05EmptyG0V
+ _symbolic _____y_____y_____yAAyAAy_____y__________G_____y_____yAeF_____GGG_____G_AAyAAy__________yAFGG_____GtGG_____G 7SwiftUI15ModifiedContentV AA6ZStackV AA9TupleViewV AA06_ShapeG0V 17PreviewsInjection5ArrowV AA5ColorV AA16_OverlayModifierV AA06StrokehG0V AA05EmptyG0V AA16_FlexFrameLayoutV AA4TextV AA016_BackgroundStyleN0V AA13_OffsetEffectV AA08_PaddingS0V
+ _symbolic yyc
+ _type_layout_string 17PreviewsInjection13JITLinkWaiterO5StateO
+ _type_layout_string 17PreviewsInjection17JITExecutorWaiterO5StateO
+ _type_layout_string 17PreviewsInjection17StreamPlaceholder33_4D960DEADBC44D786C0400B9EA4B19DBLLV
- __IVARS__TtC17PreviewsInjectionP33_8A39B3C5E39F9406AE8991E322700CBE11BlockingBox
- ___unnamed_5
- ___unnamed_7
- ___unnamed_9
- __swift_FORCE_LOAD_$_swiftDataDetection
- __swift_FORCE_LOAD_$_swiftDataDetection_$_PreviewsInjection
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_errno_$_PreviewsInjection
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_math_$_PreviewsInjection
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_signal_$_PreviewsInjection
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_stdio_$_PreviewsInjection
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swift_time_$_PreviewsInjection
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftsys_time_$_PreviewsInjection
- __swift_FORCE_LOAD_$_swiftunistd
- __swift_FORCE_LOAD_$_swiftunistd_$_PreviewsInjection
- _associated conformance 17PreviewsInjection24SendingStreamPlaceholder33_4D960DEADBC44D786C0400B9EA4B19DBLLVyxGAA13MessageSenderACLLAA4SentAafCLLP_0A12FoundationOS25PropertyListRepresentable
- _generic environment 20PreviewsFoundationOS25PropertyListRepresentableRzl
- _get_witness_table 17PreviewsInjection15HostingParadigmRzl7SwiftUI15ModifiedContentVyAEyAEyAC012_ConditionalH0VyAA11MetricsViewVAC03AnyK0VGAA23AllowAnimationsModifier33_615F4C6B56138203A5D5D631B996DBA5LLVGAC022_EnvironmentKeyWritingO0VySbGG04HostO0QzGAC0K0HPAtcXHPApcXHPAlcXHPAicXHPyHC_AkcXHPyHCHC_AoC0kO0HPyHCHC_AscYHPyHCHC_xAaBHD1_AvcYHA0_HC.16
- _get_witness_table 17PreviewsInjection15HostingParadigmRzl7SwiftUI9EmptyViewVAC0H0HPyHC.20
- _get_witness_table 7SwiftUI15ModifiedContentVyAA014_ViewModifier_D0VyAA11ColorSchemeO17PreviewsInjectionE9Transform33_B9327E8BE2A65479722DED6464165561LLVGAA018_PreferenceWritingF0VyAA09PreferredgH3KeyVGGAA0E0HPAlaSHPyHC_AqA0eF0HPyHCHC.41
- _get_witness_table 7SwiftUI19_ConditionalContentVyAA014_ViewModifier_D0Vy17PreviewsInjection015AllowAnimationsF033_615F4C6B56138203A5D5D631B996DBA5LLVGAA0E0PAAE12unanimatableQryFQOyAJ_Qo_GAaKHPAjaKHPyHC_qd__AaKHD2_ANHOHC.19
- _get_witness_table 7SwiftUI21_ViewModifier_ContentVy19PreviewsMessagingOS13PreviewTraitsV11OrientationO0F9InjectionE9Transform33_B9327E8BE2A65479722DED6464165561LLVGAA0C0HPyHC.44
- _get_witness_table qd__7SwiftUI4ViewHD2_AaBPAAE15dynamicTypeSizeyQrAA07DynamiceF0OFQOyAA01_C16Modifier_ContentVyAF17PreviewsInjectionE9Transform33_B9327E8BE2A65479722DED6464165561LLVG_Qo_HO.43
- _swift_bridgeObjectRelease_n
- _swift_bridgeObjectRetain_n
- _symbolic $s17PreviewsInjection13MessageSender33_4D960DEADBC44D786C0400B9EA4B19DBLLP
- _symbolic $s17PreviewsInjection17StreamPlaceholder33_4D960DEADBC44D786C0400B9EA4B19DBLLP
- _symbolic 4Sent_____Qz 17PreviewsInjection13MessageSender33_4D960DEADBC44D786C0400B9EA4B19DBLLP
- _symbolic SDy___________pG 19PreviewsMessagingOS31MessageStreamInstanceIdentifierV 0A9Injection0E11Placeholder33_4D960DEADBC44D786C0400B9EA4B19DBLLP
- _symbolic SayxG6buffer_t
- _symbolic _____ 17PreviewsInjection11BlockingBox33_8A39B3C5E39F9406AE8991E322700CBELLC
- _symbolic _____ 17PreviewsInjection24SendingStreamPlaceholder33_4D960DEADBC44D786C0400B9EA4B19DBLLV
- _symbolic _____ 17PreviewsInjection24SendingStreamPlaceholder33_4D960DEADBC44D786C0400B9EA4B19DBLLV5StateO
- _symbolic _____Sg 7SwiftUI11ColorSchemeO
- _symbolic _____Sg 8Dispatch0A12TimeIntervalO
- _symbolic ____________pt 19PreviewsMessagingOS31MessageStreamInstanceIdentifierV 0A9Injection0E11Placeholder33_4D960DEADBC44D786C0400B9EA4B19DBLLP
- _symbolic ______pSg 17PreviewsInjection17StreamPlaceholder33_4D960DEADBC44D786C0400B9EA4B19DBLLP
- _symbolic _____yAAyAAy_____y__________G_____G_____ySbGG12HostModifier_____QzG 7SwiftUI15ModifiedContentV AA012_ConditionalD0V 17PreviewsInjection11MetricsViewV AA03AnyI0V AF23AllowAnimationsModifier33_615F4C6B56138203A5D5D631B996DBA5LLV AA022_EnvironmentKeyWritingM0V AF15HostingParadigmP
- _symbolic _____yAAy_____y__________G_____G_____ySbGG 7SwiftUI15ModifiedContentV AA012_ConditionalD0V 17PreviewsInjection11MetricsViewV AA03AnyI0V AF23AllowAnimationsModifier33_615F4C6B56138203A5D5D631B996DBA5LLV AA022_EnvironmentKeyWritingM0V
- _symbolic _____y_____G 17PreviewsInjection11BlockingBox33_8A39B3C5E39F9406AE8991E322700CBELLC 13XOJITExecutorAEC
- _symbolic _____y_____G 17PreviewsInjection24SendingStreamPlaceholder33_4D960DEADBC44D786C0400B9EA4B19DBLLV 0A12FoundationOS12PropertyListV
- _symbolic _____y_____G 19PreviewsMessagingOS13RuntimeLookupO AA15PreviewMetadataV
- _symbolic _____y______G 17PreviewsInjection24SendingStreamPlaceholder33_4D960DEADBC44D786C0400B9EA4B19DBLLV5StateO 0A12FoundationOS12PropertyListV
- _symbolic _____y___________pG s18_DictionaryStorageC 19PreviewsMessagingOS31MessageStreamInstanceIdentifierV 0C9Injection0G11Placeholder33_4D960DEADBC44D786C0400B9EA4B19DBLLP
- _symbolic _____y___________pG s6ResultOsRi_zrlE 20PreviewsFoundationOS12PropertyListV s5ErrorP
- _symbolic _____y_____y______GG 2os21OSAllocatedUnfairLockV 17PreviewsInjection24SendingStreamPlaceholder33_4D960DEADBC44D786C0400B9EA4B19DBLLV5StateO 0E12FoundationOS12PropertyListV
- _symbolic _____y_____yx_GG 2os21OSAllocatedUnfairLockV 17PreviewsInjection24SendingStreamPlaceholder33_4D960DEADBC44D786C0400B9EA4B19DBLLV5StateO
- _symbolic _____y_xG6sender_t 19PreviewsMessagingOS13MessageStreamV6SenderV
- _symbolic _____yxG 17PreviewsInjection24SendingStreamPlaceholder33_4D960DEADBC44D786C0400B9EA4B19DBLLV
- _symbolic _____yx_G 17PreviewsInjection24SendingStreamPlaceholder33_4D960DEADBC44D786C0400B9EA4B19DBLLV5StateO
- _symbolic xSg
- _type_layout_string 20PreviewsFoundationOS25PropertyListRepresentableRzl0A9Injection24SendingStreamPlaceholder33_4D960DEADBC44D786C0400B9EA4B19DBLLVyxG
CStrings:
+ " to be a pseudodylib but it was not."
+ "/Library/Caches/com.apple.xbs/Sources/UITestingAgent/OS/PreviewsInjection/Sources/PreviewsInjection/RegistryPreview.swift"
+ "Can only wait for JIT executor on the main thread"
+ "Can only wait for JIT link on the main thread"
+ "Cannot create content host for non-preview data source"
+ "Cannot schedule link work on the main thread"
+ "Cannot submit executor on the main thread"
+ "Cannot wait twice."
+ "Could not decode registry control event: %@"
+ "Executor submitted after finishing"
+ "Executor submitted more than once"
+ "Expected %{public}s to be a pseudodylib but it was not."
+ "JIT link requested after completing"
+ "JIT link requested more than once"
+ "JITLinkWaiter: Completed initial JIT link"
+ "JITLinkWaiter: JIT link completed on secondary thread."
+ "JITLinkWaiter: Linking immediately."
+ "JITLinkWaiter: Not waiting for main thread JIT link."
+ "JITLinkWaiter: Performing initial JIT link"
+ "JITLinkWaiter: Wait for JIT link signal failed."
+ "JITLinkWaiter: Waiting for JIT link on secondary thread."
+ "JITLinkWaiter: Waiting for initial JIT link signal"
+ "PreviewsInjection/JITExecutorWaiter.swift"
+ "PreviewsInjection/JITLinkWaiter.swift"
+ "Received JIT executor"
+ "Semaphore should not be signaled unless state advanced"
+ "Timed out waiting for signal to perform the initial JIT link"
+ "Ultraviolet.AssistiveAccess"
+ "Unknown preview data source "
+ "Waiting for JIT executor"
+ "__PREVIEWS_JIT_NO_LINK_ON_MAIN_THREAD"
+ "contentHostProvider(modifiers:requestedGroupIndex:)"
+ "init(executable:streamPlaceholders:)"
+ "openStream(_:receiver:)"
+ "previewFlavor"
- "Already wrote agent launch state"
- "Box must be fulfilled off the main thread."
- "Box must be read on the main thread."
- "State semaphore signaled but no state available."
- "Waiting for JIT executor to appear."
- "executorBox"
- "internalState"
- "openStream(_:)"
- "semaphore"
- "waitTimeout"

```
