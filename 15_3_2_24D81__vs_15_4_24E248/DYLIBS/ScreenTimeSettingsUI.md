## ScreenTimeSettingsUI

> `/System/Library/PrivateFrameworks/ScreenTimeSettingsUI.framework/Versions/A/ScreenTimeSettingsUI`

```diff

-537.3.3.0.0
-  __TEXT.__text: 0x74414
-  __TEXT.__auth_stubs: 0x1e00
-  __TEXT.__objc_methlist: 0x2220
-  __TEXT.__const: 0x1f14
-  __TEXT.__gcc_except_tab: 0xa48
-  __TEXT.__cstring: 0x3df4
-  __TEXT.__oslogstring: 0x11a5
+537.4.20.1.0
+  __TEXT.__text: 0x6fe28
+  __TEXT.__auth_stubs: 0x1da0
+  __TEXT.__objc_methlist: 0x25d4
+  __TEXT.__const: 0x1ef4
+  __TEXT.__gcc_except_tab: 0xa44
+  __TEXT.__cstring: 0x3a64
+  __TEXT.__oslogstring: 0x1135
   __TEXT.__constg_swiftt: 0xefc
-  __TEXT.__swift5_typeref: 0x2fba
+  __TEXT.__swift5_typeref: 0x2fce
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_reflstr: 0x83d
   __TEXT.__swift5_fieldmd: 0x91c
   __TEXT.__swift5_assocty: 0x320
   __TEXT.__swift5_proto: 0xa8
   __TEXT.__swift5_types: 0x9c
-  __TEXT.__swift5_capture: 0x754
-  __TEXT.__unwind_info: 0x1b98
-  __TEXT.__eh_frame: 0x1818
+  __TEXT.__swift5_capture: 0x6e4
+  __TEXT.__swift_as_entry: 0x70
+  __TEXT.__swift_as_ret: 0x64
+  __TEXT.__unwind_info: 0x1b30
+  __TEXT.__eh_frame: 0x1510
   __TEXT.__objc_classname: 0x441
-  __TEXT.__objc_methname: 0xa290
-  __TEXT.__objc_methtype: 0xdf4
+  __TEXT.__objc_methname: 0xa2f7
+  __TEXT.__objc_methtype: 0xe46
   __TEXT.__objc_stubs: 0x5700
-  __DATA_CONST.__got: 0x938
-  __DATA_CONST.__const: 0x2b0
+  __DATA_CONST.__got: 0x930
+  __DATA_CONST.__const: 0x230
   __DATA_CONST.__objc_classlist: 0x110
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x22b8
+  __DATA_CONST.__objc_selrefs: 0x23e8
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x98
-  __AUTH_CONST.__auth_got: 0xf10
-  __AUTH_CONST.__const: 0x2530
+  __AUTH_CONST.__auth_got: 0xee0
+  __AUTH_CONST.__const: 0x24e8
   __AUTH_CONST.__cfstring: 0x1b00
-  __AUTH_CONST.__objc_const: 0x5a08
+  __AUTH_CONST.__objc_const: 0x54b8
   __AUTH_CONST.__objc_intobj: 0xa8
-  __AUTH.__objc_data: 0x1058
+  __AUTH.__objc_data: 0xf20
   __AUTH.__data: 0x618
   __DATA.__objc_ivar: 0x1ac
-  __DATA.__data: 0x1470
+  __DATA.__data: 0x1460
   __DATA.__bss: 0x1740
   __DATA.__common: 0x48
   - /System/Library/Frameworks/AVKit.framework/Versions/A/AVKit

   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
+  - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
-  - /usr/lib/swift/libswiftFileProvider.dylib
   - /usr/lib/swift/libswiftIOKit.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
-  - /usr/lib/swift/libswiftWebKit.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 9EF1D5B9-6659-3D68-8923-0EB6C76E8B15
-  Functions: 2357
-  Symbols:   3009
-  CStrings:  2283
+  UUID: 9C32A16B-F41D-362E-859E-17177F2C6EE7
+  Functions: 2354
+  Symbols:   3020
+  CStrings:  2267
 
Symbols:
+ +[NSDateComponentsFormatter(ScreenTimeAdditions) st_sharedAbbreviatedSecondsDateFormatter].cold.1
+ +[NSDateComponentsFormatter(ScreenTimeAdditions) st_sharedShortDynamicDateFormatter].cold.1
+ +[STCommunicationCompatibilityController userDefaults].cold.1
+ +[STRegionRatings sharedRatings].cold.1
+ +[STRestrictionsToPresetMappingViewModel boolPresetKeys].cold.1
+ +[STUILog logCategories].cold.1
+ -[STCommunicationContactEditingViewController setRepresentedObject:].cold.1
+ -[STContentAndPrivacyController fetchedResultsControllerWithFetchRequest:context:initialFetchCompletion:].cold.1
+ -[STContentAndPrivacyController fetchedResultsControllerWithFetchRequest:context:initialFetchCompletion:].cold.2
+ -[STContentAndPrivacyController fetchedResultsControllerWithFetchRequest:context:initialFetchCompletion:].cold.3
+ -[STDowntimeCommunicationViewController clickEditButton:].cold.1
+ -[STDowntimeCommunicationViewController setRepresentedObject:].cold.1
+ -[STRegionRatings getRatingSystemTypeFrom:].cold.1
+ -[STRequestsController respondToRequest:approved:amountGranted:].cold.1
+ -[STScreenTimeCommunicationViewController setRepresentedObject:].cold.1
+ ___swift_async_entry_functlets
+ ___swift_async_ret_functlets
+ ___swift_destroy_boxed_opaque_existential_0Tm
+ __swift_FORCE_LOAD_$_swiftDataDetection
+ __swift_FORCE_LOAD_$_swiftDataDetection_$_ScreenTimeSettingsUI
+ _symbolic SccySo14FAFamilyCircleC______pG s5ErrorP
+ _symbolic SccySo16FASettingsPresetCSg______pG s5ErrorP
+ _symbolic SccySo25FASettingsPresetsResponseC______pG s5ErrorP
+ _symbolic SccySo7NSImageC_____G s5NeverO
+ block_copy_helper.108
+ block_copy_helper.116
+ block_copy_helper.125
+ block_copy_helper.129
+ block_descriptor.110
+ block_descriptor.118
+ block_descriptor.127
+ block_descriptor.131
+ block_destroy_helper.109
+ block_destroy_helper.117
+ block_destroy_helper.126
+ block_destroy_helper.130
+ get_witness_table 7SwiftUI15ModifiedContentVyACyAA5ImageVAA30_EnvironmentKeyWritingModifierVyAA4FontVSgGGAGyAA5ColorVSgGGAA4ViewHPAlaRHPAeaRHPyHC_AkA0lI0HPyHCHC_ApaSHPyHCHC.138
+ get_witness_table 7SwiftUI19_ConditionalContentVyAA12ProgressViewVyAA05EmptyF0VAGGAA08ModifiedD0VyAJyAA0F0PAAE9formStyleyQrqd__AA04FormJ0Rd__lFQOyAlAE06scrollD10BackgroundyQrAA10VisibilityOFQOyAA0K0VyAA05TupleF0Vy018ScreenTimeSettingsB00D21RestrictionAgeSectionV_AV0dsU0VyAgV0dS4CellVySiAV7AppIconVyAA03AnyF0VGAA5ColorVGAGGAZyAgUyA8__A0_ySiAV17SystemSymbolImage33_A9955E79C4B4038747A9BE3A7E4A08ACLLVAA14LinearGradientVGA15_A0_ySbA5_A7_GtGAGGAZyAgUyA0_ySbAA14GeometryReaderVyAJyAJyAJyAA5ImageVAA12_FrameLayoutVGA24_GAA11_ClipEffectVyAA9RectangleVGGGA7_G_A0_ySbA12_A14_GA0_ySbA20_yA26_GA14_GtGAGGAZyAgUyA0_ySbA12_A7_G_A40_A40_SgtGAGGAZyAGA40_AA4TextVGtGG_Qo__AA07GroupedkJ0VQo_AV0S10ResetAlertVGAA13_TaskModifierVGGAaKHPAhaKHPyHC_A58_AaKHPA55_AaKHPqd0__AaKHD3_A52_HO_A54_AA0F8ModifierHPyHCHC_A57_AAA60_HPyHCHCHC.129
+ get_witness_table 7SwiftUI4ViewRzAaBR_AaBR0_r1_lAA7SectionVyAA05EmptyC0Vq_q0_GAaBHPAfaBHPyHC_q_AaBHD2_q0_AaBHD3_HC.9
+ get_witness_table 7SwiftUI4ViewRzlAA15ModifiedContentVyxAA21_TraitWritingModifierVyAA017ListRowBackgroundF3KeyVGGAaBHPxAaBHD1__AiA0cH0HPyHCHC.10
- __swift_FORCE_LOAD_$_swiftFileProvider
- __swift_FORCE_LOAD_$_swiftFileProvider_$_ScreenTimeSettingsUI
- __swift_FORCE_LOAD_$_swiftWebKit
- __swift_FORCE_LOAD_$_swiftWebKit_$_ScreenTimeSettingsUI
- _symbolic SS3key______5valuetSg s11AnyHashableV
- _symbolic SS3key_yp5valuetSg
- _symbolic _____ySbGSg 7SwiftUI11AnyLocationC
- _symbolic _____ySb__________GSg 20ScreenTimeSettingsUI22ContentRestrictionCellV AA17SystemSymbolImage33_A9955E79C4B4038747A9BE3A7E4A08ACLLV 05SwiftD05ColorV
- _symbolic _____ySo7NSImageCSgGSg 7SwiftUI11AnyLocationC
- _symbolic _____y_____y_____G______Qo_ 7SwiftUI4ViewPAAE19labeledContentStyleyQrqd__AA07LabeledeF0Rd__lFQO 018ScreenTimeSettingsB00E14RestrictionRowV AF14AgeRangeSliderV AA020GroupedFormTextFieldgeF0V
- block_copy_helper.128
- block_copy_helper.135
- block_copy_helper.139
- block_copy_helper.146
- block_copy_helper.153
- block_copy_helper.41
- block_copy_helper.48
- block_descriptor.108
- block_descriptor.114
- block_descriptor.121
- block_descriptor.123
- block_descriptor.130
- block_descriptor.137
- block_descriptor.141
- block_descriptor.148
- block_descriptor.155
- block_descriptor.43
- block_descriptor.50
- block_destroy_helper.129
- block_destroy_helper.136
- block_destroy_helper.140
- block_destroy_helper.147
- block_destroy_helper.154
- block_destroy_helper.42
- block_destroy_helper.49
- get_witness_table 7SwiftUI15ModifiedContentVyACyAA5ImageVAA30_EnvironmentKeyWritingModifierVyAA4FontVSgGGAGyAA5ColorVSgGGAA4ViewHPAlaRHPAeaRHPyHC_AkA0lI0HPyHCHC_ApaSHPyHCHC.173
- get_witness_table 7SwiftUI19_ConditionalContentVyAA12ProgressViewVyAA05EmptyF0VAGGAA08ModifiedD0VyAJyAA0F0PAAE9formStyleyQrqd__AA04FormJ0Rd__lFQOyAlAE06scrollD10BackgroundyQrAA10VisibilityOFQOyAA0K0VyAA05TupleF0Vy018ScreenTimeSettingsB00D21RestrictionAgeSectionV_AV0dsU0VyAgV0dS4CellVySiAV7AppIconVyAA03AnyF0VGAA5ColorVGAGGAZyAgUyA8__A0_ySiAV17SystemSymbolImage33_A9955E79C4B4038747A9BE3A7E4A08ACLLVAA14LinearGradientVGA15_A0_ySbA5_A7_GtGAGGAZyAgUyA0_ySbAA14GeometryReaderVyAJyAJyAJyAA5ImageVAA12_FrameLayoutVGA24_GAA11_ClipEffectVyAA9RectangleVGGGA7_G_A0_ySbA12_A14_GA0_ySbA20_yA26_GA14_GtGAGGAZyAgUyA0_ySbA12_A7_G_A40_A40_SgtGAGGAZyAGA40_AA4TextVGtGG_Qo__AA07GroupedkJ0VQo_AV0S10ResetAlertVGAA13_TaskModifierVGGAaKHPAhaKHPyHC_A58_AaKHPA55_AaKHPqd0__AaKHD3_A52_HO_A54_AA0F8ModifierHPyHCHC_A57_AAA60_HPyHCHCHC.164
- get_witness_table 7SwiftUI4ViewRzAaBR_AaBR0_r1_lAA7SectionVyAA05EmptyC0Vq_q0_GAaBHPAfaBHPyHC_q_AaBHD2_q0_AaBHD3_HC.7
- get_witness_table 7SwiftUI4ViewRzlAA15ModifiedContentVyxAA21_TraitWritingModifierVyAA017ListRowBackgroundF3KeyVGGAaBHPxAaBHD1__AiA0cH0HPyHCHC.8
CStrings:
+ "initWithAppAndWebsiteActivityEnabled:downtimeStartTime:downtimeEndTime:restrictions:passcode:communicationSafetyEnabled:eyeReliefEnabled:imageGenerationRestriction:"
+ "v44@0:8@\"WKWebView\"16@\"WKBackForwardListItem\"24B32@?<v@?B>36"
+ "v44@0:8@16@24B32@?36"
+ "webView:shouldGoToBackForwardListItem:willUseInstantBack:completionHandler:"
- "Can't construct Array with count < 0"
- "Image Creation: STOnboardingViewModel introductionModel has imageGenerationRestriction value = %lld"
- "Insufficient space allocated to copy string contents"
- "Swift/Array.swift"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawBufferPointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutablePointer.initialize with negative count"
- "UnsafeMutablePointer.moveInitialize with negative count"
- "UnsafeMutableRawBufferPointer.copyMemory source has too many elements"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "initWithAppAndWebsiteActivityEnabled:downtimeStartTime:downtimeEndTime:restrictions:passcode:communicationSafetyEnabled:eyeReliefEnabled:"
- "invalid Collection: less than 'count' elements in collection"

```
