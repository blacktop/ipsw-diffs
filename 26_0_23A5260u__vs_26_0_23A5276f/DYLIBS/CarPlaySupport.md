## CarPlaySupport

> `/System/Library/PrivateFrameworks/CarPlaySupport.framework/CarPlaySupport`

```diff

-474.4.2.0.0
-  __TEXT.__text: 0xfd978
-  __TEXT.__auth_stubs: 0x950
-  __TEXT.__objc_methlist: 0x9b30
-  __TEXT.__const: 0x2a4
-  __TEXT.__cstring: 0x19de
-  __TEXT.__gcc_except_tab: 0xff4
+479.3.0.0.0
+  __TEXT.__text: 0xfefb4
+  __TEXT.__auth_stubs: 0xbe0
+  __TEXT.__objc_methlist: 0x9aa0
+  __TEXT.__const: 0x364
+  __TEXT.__cstring: 0x1abe
+  __TEXT.__gcc_except_tab: 0x1070
   __TEXT.__oslogstring: 0x2451
   __TEXT.__ustring: 0x4
-  __TEXT.__swift5_typeref: 0x22
-  __TEXT.__constg_swiftt: 0xa4
-  __TEXT.__swift5_fieldmd: 0x20
-  __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x18b8
-  __TEXT.__objc_classname: 0x1644
-  __TEXT.__objc_methname: 0x1acab
-  __TEXT.__objc_methtype: 0x4e29
-  __TEXT.__objc_stubs: 0x12640
-  __DATA_CONST.__got: 0xb80
-  __DATA_CONST.__const: 0x2d38
-  __DATA_CONST.__objc_classlist: 0x400
+  __TEXT.__swift5_typeref: 0x32e
+  __TEXT.__constg_swiftt: 0x138
+  __TEXT.__swift5_fieldmd: 0x60
+  __TEXT.__swift5_types: 0xc
+  __TEXT.__swift5_reflstr: 0x24
+  __TEXT.__unwind_info: 0x1968
+  __TEXT.__objc_classname: 0x1624
+  __TEXT.__objc_methname: 0x1abd1
+  __TEXT.__objc_methtype: 0x4e50
+  __TEXT.__objc_stubs: 0x12520
+  __DATA_CONST.__got: 0xbb8
+  __DATA_CONST.__const: 0x2dd0
+  __DATA_CONST.__objc_classlist: 0x3f8
   __DATA_CONST.__objc_catlist: 0x60
-  __DATA_CONST.__objc_protolist: 0x2e0
+  __DATA_CONST.__objc_protolist: 0x2e8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5de8
+  __DATA_CONST.__objc_selrefs: 0x5da8
   __DATA_CONST.__objc_protorefs: 0x78
-  __DATA_CONST.__objc_superrefs: 0x330
+  __DATA_CONST.__objc_superrefs: 0x320
   __DATA_CONST.__objc_arraydata: 0x100
-  __AUTH_CONST.__auth_got: 0x4b8
-  __AUTH_CONST.__const: 0x580
-  __AUTH_CONST.__cfstring: 0x1920
-  __AUTH_CONST.__objc_const: 0x1ea10
+  __AUTH_CONST.__auth_got: 0x600
+  __AUTH_CONST.__const: 0x5a0
+  __AUTH_CONST.__cfstring: 0x1900
+  __AUTH_CONST.__objc_const: 0x1e9a8
   __AUTH_CONST.__objc_intobj: 0x198
   __AUTH_CONST.__objc_arrayobj: 0x198
-  __AUTH.__objc_data: 0x2830
-  __AUTH.__data: 0xc0
-  __DATA.__objc_ivar: 0x9e0
-  __DATA.__data: 0x22c0
-  __DATA.__bss: 0x100
+  __AUTH.__objc_data: 0x28c0
+  __AUTH.__data: 0xe8
+  __DATA.__objc_ivar: 0x9c8
+  __DATA.__data: 0x23d8
+  __DATA.__bss: 0x120
   - /System/Library/Frameworks/CarPlay.framework/CarPlay
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/Frameworks/MapKit.framework/MapKit
   - /System/Library/Frameworks/QuartzCore.framework/QuartzCore
   - /System/Library/Frameworks/Security.framework/Security
+  - /System/Library/Frameworks/SwiftUI.framework/SwiftUI
   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/Frameworks/_LocationEssentials.framework/_LocationEssentials
   - /System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
+  - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
+  - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: C6512961-72BA-3C0F-8A4A-79C39DDD18BD
-  Functions: 3089
-  Symbols:   12778
-  CStrings:  5642
+  UUID: 43A25017-6330-3E4D-A5D1-18F7CD90E724
+  Functions: 3156
+  Symbols:   12985
+  CStrings:  5635
 
Symbols:
+ -[CPSActionButton setSelected:]
+ -[CPSListTemplateViewController didSelectHeaderButtonWithIdentifier:]
+ -[CPSListTemplateViewController tableView:heightForFooterInSection:]
+ -[CPSListTemplateViewController tableView:viewForFooterInSection:]
+ -[CPSNowPlayingViewController viewDidLayoutSubviews]
+ -[CPSOverlayViewController environmentProvider]
+ -[CPSOverlayViewController setEnvironmentProvider:]
+ -[CPSPointsOfInterestPickerViewController wantsPlainButtonAppearance]
+ -[CPSStyledTextButton setWantsGlass:]
+ -[CPSStyledTextButton wantsGlass]
+ -[CPSTemplateInstance visibilityEnvironmentIdentifier]
+ GCC_except_table172
+ GCC_except_table31
+ GCC_except_table65
+ _$s14CarPlaySupport29CPSPointsOfInterestPickerCellC10identifierSSvgZ
+ _$s14CarPlaySupport29CPSPointsOfInterestPickerCellC10identifierSSvgZTo
+ _$s14CarPlaySupport29CPSPointsOfInterestPickerCellC10identifierSSvpZMV
+ _$s14CarPlaySupport29CPSPointsOfInterestPickerCellC13tertiaryTitleSSSgvM
+ _$s14CarPlaySupport29CPSPointsOfInterestPickerCellC13tertiaryTitleSSSgvM.resume.0
+ _$s14CarPlaySupport29CPSPointsOfInterestPickerCellC13tertiaryTitleSSSgvMTj
+ _$s14CarPlaySupport29CPSPointsOfInterestPickerCellC13tertiaryTitleSSSgvMTq
+ _$s14CarPlaySupport29CPSPointsOfInterestPickerCellC13tertiaryTitleSSSgvg
+ _$s14CarPlaySupport29CPSPointsOfInterestPickerCellC13tertiaryTitleSSSgvgTj
+ _$s14CarPlaySupport29CPSPointsOfInterestPickerCellC13tertiaryTitleSSSgvgTo
+ _$s14CarPlaySupport29CPSPointsOfInterestPickerCellC13tertiaryTitleSSSgvgTq
+ _$s14CarPlaySupport29CPSPointsOfInterestPickerCellC13tertiaryTitleSSSgvpMV
+ _$s14CarPlaySupport29CPSPointsOfInterestPickerCellC13tertiaryTitleSSSgvpWvd
+ _$s14CarPlaySupport29CPSPointsOfInterestPickerCellC13tertiaryTitleSSSgvs
+ _$s14CarPlaySupport29CPSPointsOfInterestPickerCellC13tertiaryTitleSSSgvsTj
+ _$s14CarPlaySupport29CPSPointsOfInterestPickerCellC13tertiaryTitleSSSgvsTo
+ _$s14CarPlaySupport29CPSPointsOfInterestPickerCellC13tertiaryTitleSSSgvsTq
+ _$s14CarPlaySupport29CPSPointsOfInterestPickerCellC14didUpdateFocus2in4withySo07UIFocusJ7ContextC_So0N20AnimationCoordinatorCtF
+ _$s14CarPlaySupport29CPSPointsOfInterestPickerCellC14didUpdateFocus2in4withySo07UIFocusJ7ContextC_So0N20AnimationCoordinatorCtFTo
+ _$s14CarPlaySupport29CPSPointsOfInterestPickerCellC19updateConfiguration5usingy5UIKit06UICellJ5StateV_tF
+ _$s14CarPlaySupport29CPSPointsOfInterestPickerCellC19updateConfiguration5usingy5UIKit06UICellJ5StateV_tF7SwiftUI6VStackVyAI9TupleViewVyAI0S0PAIE15foregroundStyleyQrqd__AI05ShapeU0Rd__lFQOyAoIE10fontWeightyQrAI4FontV0X0VSgFQOyAoIE0W0yQrATSgFQOyAoIE9lineLimityQrSiSgFQOyAI4TextV_Qo__Qo__Qo__AI5ColorVQo_Sg_AoIEAPyQrqd__AiQRd__lFQOyA3__A6_Qo_SgA10_tGGyXEfU_
+ _$s14CarPlaySupport29CPSPointsOfInterestPickerCellC19updateConfiguration5usingy5UIKit06UICellJ5StateV_tF7SwiftUI6VStackVyAI9TupleViewVyAI0S0PAIE15foregroundStyleyQrqd__AI05ShapeU0Rd__lFQOyAoIE10fontWeightyQrAI4FontV0X0VSgFQOyAoIE0W0yQrATSgFQOyAoIE9lineLimityQrSiSgFQOyAI4TextV_Qo__Qo__Qo__AI5ColorVQo_Sg_AoIEAPyQrqd__AiQRd__lFQOyA3__A6_Qo_SgA10_tGGyXEfU_A11_yXEfU_
+ _$s14CarPlaySupport29CPSPointsOfInterestPickerCellC19updateConfiguration5usingy5UIKit06UICellJ5StateV_tF7SwiftUI6VStackVyAI9TupleViewVyAI0S0PAIE15foregroundStyleyQrqd__AI05ShapeU0Rd__lFQOyAoIE10fontWeightyQrAI4FontV0X0VSgFQOyAoIE0W0yQrATSgFQOyAoIE9lineLimityQrSiSgFQOyAI4TextV_Qo__Qo__Qo__AI5ColorVQo_Sg_AoIEAPyQrqd__AiQRd__lFQOyA3__A6_Qo_SgA10_tGGyXEfU_TA
+ _$s14CarPlaySupport29CPSPointsOfInterestPickerCellC19updateConfiguration5usingy5UIKit06UICellJ5StateV_tFTo
+ _$s14CarPlaySupport29CPSPointsOfInterestPickerCellC5coderACSgSo7NSCoderC_tcfC
+ _$s14CarPlaySupport29CPSPointsOfInterestPickerCellC5coderACSgSo7NSCoderC_tcfc
+ _$s14CarPlaySupport29CPSPointsOfInterestPickerCellC5coderACSgSo7NSCoderC_tcfcTo
+ _$s14CarPlaySupport29CPSPointsOfInterestPickerCellC5style15reuseIdentifierACSo011UITableViewH5StyleV_SSSgtcfC
+ _$s14CarPlaySupport29CPSPointsOfInterestPickerCellC5style15reuseIdentifierACSo011UITableViewH5StyleV_SSSgtcfc
+ _$s14CarPlaySupport29CPSPointsOfInterestPickerCellC5style15reuseIdentifierACSo011UITableViewH5StyleV_SSSgtcfcTo
+ _$s14CarPlaySupport29CPSPointsOfInterestPickerCellC5titleSSSgvM
+ _$s14CarPlaySupport29CPSPointsOfInterestPickerCellC5titleSSSgvM.resume.0
+ _$s14CarPlaySupport29CPSPointsOfInterestPickerCellC5titleSSSgvMTj
+ _$s14CarPlaySupport29CPSPointsOfInterestPickerCellC5titleSSSgvMTq
+ _$s14CarPlaySupport29CPSPointsOfInterestPickerCellC5titleSSSgvg
+ _$s14CarPlaySupport29CPSPointsOfInterestPickerCellC5titleSSSgvgTj
+ _$s14CarPlaySupport29CPSPointsOfInterestPickerCellC5titleSSSgvgTm
+ _$s14CarPlaySupport29CPSPointsOfInterestPickerCellC5titleSSSgvgTo
+ _$s14CarPlaySupport29CPSPointsOfInterestPickerCellC5titleSSSgvgToTm
+ _$s14CarPlaySupport29CPSPointsOfInterestPickerCellC5titleSSSgvgTq
+ _$s14CarPlaySupport29CPSPointsOfInterestPickerCellC5titleSSSgvpACTkTm
+ _$s14CarPlaySupport29CPSPointsOfInterestPickerCellC5titleSSSgvpMV
+ _$s14CarPlaySupport29CPSPointsOfInterestPickerCellC5titleSSSgvpWvd
+ _$s14CarPlaySupport29CPSPointsOfInterestPickerCellC5titleSSSgvs
+ _$s14CarPlaySupport29CPSPointsOfInterestPickerCellC5titleSSSgvsTj
+ _$s14CarPlaySupport29CPSPointsOfInterestPickerCellC5titleSSSgvsTm
+ _$s14CarPlaySupport29CPSPointsOfInterestPickerCellC5titleSSSgvsTo
+ _$s14CarPlaySupport29CPSPointsOfInterestPickerCellC5titleSSSgvsToTm
+ _$s14CarPlaySupport29CPSPointsOfInterestPickerCellC5titleSSSgvsTq
+ _$s14CarPlaySupport29CPSPointsOfInterestPickerCellC6chosenSbvM
+ _$s14CarPlaySupport29CPSPointsOfInterestPickerCellC6chosenSbvM.resume.0
+ _$s14CarPlaySupport29CPSPointsOfInterestPickerCellC6chosenSbvM.resume.0Tm
+ _$s14CarPlaySupport29CPSPointsOfInterestPickerCellC6chosenSbvMTj
+ _$s14CarPlaySupport29CPSPointsOfInterestPickerCellC6chosenSbvMTq
+ _$s14CarPlaySupport29CPSPointsOfInterestPickerCellC6chosenSbvg
+ _$s14CarPlaySupport29CPSPointsOfInterestPickerCellC6chosenSbvgTj
+ _$s14CarPlaySupport29CPSPointsOfInterestPickerCellC6chosenSbvgTo
+ _$s14CarPlaySupport29CPSPointsOfInterestPickerCellC6chosenSbvgTq
+ _$s14CarPlaySupport29CPSPointsOfInterestPickerCellC6chosenSbvpMV
+ _$s14CarPlaySupport29CPSPointsOfInterestPickerCellC6chosenSbvpWvd
+ _$s14CarPlaySupport29CPSPointsOfInterestPickerCellC6chosenSbvs
+ _$s14CarPlaySupport29CPSPointsOfInterestPickerCellC6chosenSbvsTj
+ _$s14CarPlaySupport29CPSPointsOfInterestPickerCellC6chosenSbvsTo
+ _$s14CarPlaySupport29CPSPointsOfInterestPickerCellC6chosenSbvsTq
+ _$s14CarPlaySupport29CPSPointsOfInterestPickerCellC8subtitleSSSgvM
+ _$s14CarPlaySupport29CPSPointsOfInterestPickerCellC8subtitleSSSgvM.resume.0
+ _$s14CarPlaySupport29CPSPointsOfInterestPickerCellC8subtitleSSSgvMTj
+ _$s14CarPlaySupport29CPSPointsOfInterestPickerCellC8subtitleSSSgvMTq
+ _$s14CarPlaySupport29CPSPointsOfInterestPickerCellC8subtitleSSSgvg
+ _$s14CarPlaySupport29CPSPointsOfInterestPickerCellC8subtitleSSSgvgTj
+ _$s14CarPlaySupport29CPSPointsOfInterestPickerCellC8subtitleSSSgvgTo
+ _$s14CarPlaySupport29CPSPointsOfInterestPickerCellC8subtitleSSSgvgTq
+ _$s14CarPlaySupport29CPSPointsOfInterestPickerCellC8subtitleSSSgvpMV
+ _$s14CarPlaySupport29CPSPointsOfInterestPickerCellC8subtitleSSSgvpWvd
+ _$s14CarPlaySupport29CPSPointsOfInterestPickerCellC8subtitleSSSgvs
+ _$s14CarPlaySupport29CPSPointsOfInterestPickerCellC8subtitleSSSgvsTj
+ _$s14CarPlaySupport29CPSPointsOfInterestPickerCellC8subtitleSSSgvsTo
+ _$s14CarPlaySupport29CPSPointsOfInterestPickerCellC8subtitleSSSgvsTq
+ _$s14CarPlaySupport29CPSPointsOfInterestPickerCellCMF
+ _$s14CarPlaySupport29CPSPointsOfInterestPickerCellCMa
+ _$s14CarPlaySupport29CPSPointsOfInterestPickerCellCMf
+ _$s14CarPlaySupport29CPSPointsOfInterestPickerCellCMn
+ _$s14CarPlaySupport29CPSPointsOfInterestPickerCellCMo
+ _$s14CarPlaySupport29CPSPointsOfInterestPickerCellCMu
+ _$s14CarPlaySupport29CPSPointsOfInterestPickerCellCN
+ _$s14CarPlaySupport29CPSPointsOfInterestPickerCellCfD
+ _$s14CarPlaySupport29CPSPointsOfInterestPickerCellCfETo
+ _$s5UIKit24UICellConfigurationStateV10isSelectedSbvg
+ _$s5UIKit24UICellConfigurationStateV13isHighlightedSbvg
+ _$s5UIKit24UICellConfigurationStateV36_unconditionallyBridgeFromObjectiveCyACSoABCSgFZ
+ _$s5UIKit24UICellConfigurationStateV9isFocusedSbvg
+ _$s5UIKit24UICellConfigurationStateVMa
+ _$s5UIKit25UIBackgroundConfigurationV12cornerRadius12CoreGraphics7CGFloatVvs
+ _$s5UIKit25UIBackgroundConfigurationV15backgroundColorSo7UIColorCSgvs
+ _$s5UIKit25UIBackgroundConfigurationV5clearACyFZ
+ _$s5UIKit25UIBackgroundConfigurationVMa
+ _$s5UIKit25UIBackgroundConfigurationVMn
+ _$s5UIKit25UIBackgroundConfigurationVSgMD
+ _$s7SwiftUI13_VStackLayoutVMn
+ _$s7SwiftUI13_VariadicViewO4TreeVMn
+ _$s7SwiftUI13_VariadicViewO4TreeVy_AA13_VStackLayoutVAA05TupleD0VyAA15ModifiedContentVyAA0D0PAAE10fontWeightyQrAA4FontV0L0VSgFQOyAKyAKyAA4TextVAA30_EnvironmentKeyWritingModifierVySiSgGGAWyAPSgGG_Qo_AA016_ForegroundStyleR0VyAA5ColorVGGSg_AKyA1_A7_GSgA11_tGGMD
+ _$s7SwiftUI15ModifiedContentVMn
+ _$s7SwiftUI15ModifiedContentVyAA4TextVAA30_EnvironmentKeyWritingModifierVySiSgGGACyxq_GAA4ViewA2aLRzAA0jI0R_rlWL
+ _$s7SwiftUI15ModifiedContentVyAA4TextVAA30_EnvironmentKeyWritingModifierVySiSgGGACyxq_GAA4ViewA2aLRzAA0jI0R_rlWl
+ _$s7SwiftUI15ModifiedContentVyAA4TextVAA30_EnvironmentKeyWritingModifierVySiSgGGMD
+ _$s7SwiftUI15ModifiedContentVyAA4ViewPAAE10fontWeightyQrAA4FontV0G0VSgFQOyACyACyAA4TextVAA30_EnvironmentKeyWritingModifierVySiSgGGAOyAHSgGG_Qo_AA016_ForegroundStyleM0VyAA5ColorVGGMD
+ _$s7SwiftUI15ModifiedContentVyAA4ViewPAAE10fontWeightyQrAA4FontV0G0VSgFQOyACyACyAA4TextVAA30_EnvironmentKeyWritingModifierVySiSgGGAOyAHSgGG_Qo_AA016_ForegroundStyleM0VyAA5ColorVGGSgMD
+ _$s7SwiftUI15ModifiedContentVyAA4ViewPAAE10fontWeightyQrAA4FontV0G0VSgFQOyACyACyAA4TextVAA30_EnvironmentKeyWritingModifierVySiSgGGAOyAHSgGG_Qo_AA016_ForegroundStyleM0VyAA5ColorVGGSg_ACyAUA_GSgA3_tMD
+ _$s7SwiftUI15ModifiedContentVyACyAA4TextVAA30_EnvironmentKeyWritingModifierVySiSgGGAGyAA4FontVSgGGACyxq_GAA4ViewA2aQRzAA0kI0R_rlWL
+ _$s7SwiftUI15ModifiedContentVyACyAA4TextVAA30_EnvironmentKeyWritingModifierVySiSgGGAGyAA4FontVSgGGACyxq_GAA4ViewA2aQRzAA0kI0R_rlWl
+ _$s7SwiftUI15ModifiedContentVyACyAA4TextVAA30_EnvironmentKeyWritingModifierVySiSgGGAGyAA4FontVSgGGMD
+ _$s7SwiftUI15ModifiedContentVyACyACyAA4TextVAA30_EnvironmentKeyWritingModifierVySiSgGGAGyAA4FontVSgGGAA016_ForegroundStyleI0VyAA5ColorVGGSgMD
+ _$s7SwiftUI15ModifiedContentVyACyACyAA4TextVAA30_EnvironmentKeyWritingModifierVySiSgGGAGyAA4FontVSgGGAA016_ForegroundStyleI0VyAA5ColorVGGSgWOc
+ _$s7SwiftUI15ModifiedContentVyACyACyAA4TextVAA30_EnvironmentKeyWritingModifierVySiSgGGAGyAA4FontVSgGGAA016_ForegroundStyleI0VyAA5ColorVGGSgWOhTm
+ _$s7SwiftUI15ModifiedContentVyxq_GAA4ViewA2aERzAA0E8ModifierR_rlMc
+ _$s7SwiftUI17EnvironmentValuesV4fontAA4FontVSgvg
+ _$s7SwiftUI17EnvironmentValuesV4fontAA4FontVSgvpACTkq
+ _$s7SwiftUI17EnvironmentValuesV4fontAA4FontVSgvpMV
+ _$s7SwiftUI17EnvironmentValuesV4fontAA4FontVSgvs
+ _$s7SwiftUI17EnvironmentValuesV9lineLimitSiSgvg
+ _$s7SwiftUI17EnvironmentValuesV9lineLimitSiSgvpACTkq
+ _$s7SwiftUI17EnvironmentValuesV9lineLimitSiSgvpMV
+ _$s7SwiftUI17EnvironmentValuesV9lineLimitSiSgvs
+ _$s7SwiftUI17EnvironmentValuesVMn
+ _$s7SwiftUI19HorizontalAlignmentV7leadingACvgZ
+ _$s7SwiftUI22UIHostingConfigurationV7marginsyACyxq_GAA4EdgeO3SetV_AA0F6InsetsVtF
+ _$s7SwiftUI22UIHostingConfigurationVA2A9EmptyViewVRs_rlE7contentACyxAEGxyXE_tcfC
+ _$s7SwiftUI22UIHostingConfigurationVMn
+ _$s7SwiftUI22UIHostingConfigurationVyAA6VStackVyAA9TupleViewVyAA15ModifiedContentVyAA0G0PAAE10fontWeightyQrAA4FontV0K0VSgFQOyAIyAIyAA4TextVAA30_EnvironmentKeyWritingModifierVySiSgGGAUyANSgGG_Qo_AA016_ForegroundStyleQ0VyAA5ColorVGGSg_AIyA_A5_GSgA9_tGGAA05EmptyG0VGACyxq_G5UIKit09UIContentD0AAWL
+ _$s7SwiftUI22UIHostingConfigurationVyAA6VStackVyAA9TupleViewVyAA15ModifiedContentVyAA0G0PAAE10fontWeightyQrAA4FontV0K0VSgFQOyAIyAIyAA4TextVAA30_EnvironmentKeyWritingModifierVySiSgGGAUyANSgGG_Qo_AA016_ForegroundStyleQ0VyAA5ColorVGGSg_AIyA_A5_GSgA9_tGGAA05EmptyG0VGMD
+ _$s7SwiftUI22UIHostingConfigurationVyxq_G5UIKit09UIContentD0AAMc
+ _$s7SwiftUI24_ForegroundStyleModifierVMn
+ _$s7SwiftUI30_EnvironmentKeyWritingModifierVMn
+ _$s7SwiftUI30_EnvironmentKeyWritingModifierVyAA4FontVSgGACyxGAA04ViewF0AAWL
+ _$s7SwiftUI30_EnvironmentKeyWritingModifierVyAA4FontVSgGMD
+ _$s7SwiftUI30_EnvironmentKeyWritingModifierVySiSgGACyxGAA04ViewF0AAWL
+ _$s7SwiftUI30_EnvironmentKeyWritingModifierVySiSgGMD
+ _$s7SwiftUI30_EnvironmentKeyWritingModifierVyxGAA04ViewF0AAMc
+ _$s7SwiftUI4EdgeO3SetV3allAEvgZ
+ _$s7SwiftUI4FontV11subheadlineACvgZ
+ _$s7SwiftUI4FontV6WeightV6mediumAEvgZ
+ _$s7SwiftUI4FontV7captionACvgZ
+ _$s7SwiftUI4FontVMn
+ _$s7SwiftUI4TextVAA4ViewAAWP
+ _$s7SwiftUI4TextVMn
+ _$s7SwiftUI4TextVyACxcSyRzlufC
+ _$s7SwiftUI4ViewPAAE10fontWeightyQrAA4FontV0E0VSgF
+ _$s7SwiftUI4ViewPAAE10fontWeightyQrAA4FontV0E0VSgFQOMQ
+ _$s7SwiftUI4ViewPAAE10fontWeightyQrAA4FontV0E0VSgFQOyAA15ModifiedContentVyAKyAA4TextVAA30_EnvironmentKeyWritingModifierVySiSgGGAOyAFSgGG_Qo_MD
+ _$s7SwiftUI5ColorV02uiC0ACSo7UIColorC_tcfC
+ _$s7SwiftUI5ColorV7primaryACvgZ
+ _$s7SwiftUI5ColorVMn
+ _$s7SwiftUI6VStackVMn
+ _$s7SwiftUI6VStackVyAA9TupleViewVyAA15ModifiedContentVyAA0E0PAAE10fontWeightyQrAA4FontV0I0VSgFQOyAGyAGyAA4TextVAA30_EnvironmentKeyWritingModifierVySiSgGGASyALSgGG_Qo_AA016_ForegroundStyleO0VyAA5ColorVGGSg_AGyAYA3_GSgA7_tGGACyxGAahAWL
+ _$s7SwiftUI6VStackVyAA9TupleViewVyAA15ModifiedContentVyAA0E0PAAE10fontWeightyQrAA4FontV0I0VSgFQOyAGyAGyAA4TextVAA30_EnvironmentKeyWritingModifierVySiSgGGASyALSgGG_Qo_AA016_ForegroundStyleO0VyAA5ColorVGGSg_AGyAYA3_GSgA7_tGGACyxGAahAWlTm
+ _$s7SwiftUI6VStackVyAA9TupleViewVyAA15ModifiedContentVyAA0E0PAAE10fontWeightyQrAA4FontV0I0VSgFQOyAGyAGyAA4TextVAA30_EnvironmentKeyWritingModifierVySiSgGGASyALSgGG_Qo_AA016_ForegroundStyleO0VyAA5ColorVGGSg_AGyAYA3_GSgA7_tGGMD
+ _$s7SwiftUI6VStackVyxGAA4ViewAAMc
+ _$s7SwiftUI9EmptyViewVMn
+ _$s7SwiftUI9TupleViewVMn
+ _$sS2SSysWL
+ _$sS2SSysWl
+ _$sSS10FoundationE19_bridgeToObjectiveCSo8NSStringCyF
+ _$sSS10FoundationE36_unconditionallyBridgeFromObjectiveCySSSo8NSStringCSgFZ
+ _$sSSN
+ _$sSSSysMc
+ _$sSo15UITableViewCellC5UIKitE20contentConfigurationAC09UIContentF0_pSgvs
+ _$sSo15UITableViewCellC5UIKitE23backgroundConfigurationAC012UIBackgroundF0VSgvs
+ _CPUIGridCellFirstCellContentInsets_Solarium
+ _CPUIImageRowCellFirstCellContentInsets_Solarium
+ _CarPlayFrameworkStateCaptureLogging
+ _CarPlayFrameworkStateCaptureLogging.facility
+ _CarPlayFrameworkStateCaptureLogging.onceToken
+ _OBJC_CLASS_$_CPUIEnhancedSectionHeaderView
+ _OBJC_CLASS_$_CPUITableViewHeaderView
+ _OBJC_CLASS_$__TtC14CarPlaySupport29CPSPointsOfInterestPickerCell
+ _OBJC_IVAR_$_CPSOverlayViewController._environmentProvider
+ _OBJC_IVAR_$_CPSStyledTextButton._wantsGlass
+ _OBJC_METACLASS_$__TtC14CarPlaySupport29CPSPointsOfInterestPickerCell
+ _OUTLINED_FUNCTION_0
+ _OUTLINED_FUNCTION_1
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_7
+ __CLASS_METHODS__TtC14CarPlaySupport29CPSPointsOfInterestPickerCell
+ __CLASS_PROPERTIES__TtC14CarPlaySupport29CPSPointsOfInterestPickerCell
+ __DATA__TtC14CarPlaySupport29CPSPointsOfInterestPickerCell
+ __INSTANCE_METHODS__TtC14CarPlaySupport29CPSPointsOfInterestPickerCell
+ __IVARS__TtC14CarPlaySupport29CPSPointsOfInterestPickerCell
+ __METACLASS_DATA__TtC14CarPlaySupport29CPSPointsOfInterestPickerCell
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CPSVisibilityEnvironmentProviding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CPSVisibilityEnvironmentProviding
+ __OBJC_$_PROTOCOL_REFS_CPSVisibilityEnvironmentProviding
+ __OBJC_LABEL_PROTOCOL_$_CPSVisibilityEnvironmentProviding
+ __OBJC_PROTOCOL_$_CPSVisibilityEnvironmentProviding
+ __PROPERTIES__TtC14CarPlaySupport29CPSPointsOfInterestPickerCell
+ __UIVisibilityEnvironmentForSceneIdentityToken
+ ___62-[CPSTemplateInstance viewController:didUpdateSafeAreaInsets:]_block_invoke.180
+ ___62-[CPSTemplateInstance viewController:didUpdateSafeAreaInsets:]_block_invoke.181
+ ___77-[CPSTemplateInstance presentVoiceTemplate:withProxyDelegate:animated:reply:]_block_invoke.102
+ ___93-[CPSTemplateInstance pushEntityTemplate:withProxyDelegate:animated:presentationStyle:reply:]_block_invoke.109
+ ___93-[CPSTemplateInstance pushSearchTemplate:withProxyDelegate:animated:presentationStyle:reply:]_block_invoke.100
+ ___97-[CPSTemplateInstance pushNowPlayingTemplate:withProxyDelegate:animated:presentationStyle:reply:]_block_invoke.97
+ ___CarPlayFrameworkStateCaptureLogging_block_invoke
+ ___block_descriptor_48_e8_32s40r_e5_v8?0ls32l8r40l8
+ ___block_descriptor_48_e8_32s40r_e8_v12?0B8ls32l8r40l8
+ ___block_literal_global.118
+ ___block_literal_global.5
+ ___swift_instantiateConcreteTypeFromMangledNameAbstract
+ ___swift_storeEnumTagSinglePayload
+ __swift_FORCE_LOAD_$_swiftCoreAudio
+ __swift_FORCE_LOAD_$_swiftCoreAudio_$_CarPlaySupport
+ __swift_FORCE_LOAD_$_swiftCoreMedia
+ __swift_FORCE_LOAD_$_swiftCoreMedia_$_CarPlaySupport
+ __swift_FORCE_LOAD_$_swiftSpatial
+ __swift_FORCE_LOAD_$_swiftSpatial_$_CarPlaySupport
+ _objc_msgSend$didSelectHeaderButtonWithIdentifier:
+ _objc_msgSend$environmentProvider
+ _objc_msgSend$identityToken
+ _objc_msgSend$initWithId:title:subtitle:image:imageShape:backgroundColor:isTallArtwork:accessorySystemImage:allowsTouches:disabledAppearance:action:
+ _objc_msgSend$initWithId:title:subtitle:image:imageShape:backgroundColor:isTallArtwork:accessorySystemImage:allowsTouches:disabledAppearance:canStayPressed:action:
+ _objc_msgSend$initWithImage:title:subtitle:allowsTouches:disabledAppearance:
+ _objc_msgSend$plainButtonConfiguration
+ _objc_msgSend$setButtonAction:
+ _objc_msgSend$setContentInsets:
+ _objc_msgSend$setEnvironmentProvider:
+ _objc_msgSend$setLabelText:
+ _objc_msgSend$setStrokeColor:
+ _objc_msgSend$setTertiaryTitle:
+ _objc_msgSend$setTitleLineBreakMode:
+ _objc_msgSend$setWantsGlass:
+ _objc_msgSend$showsImageFullHeight
+ _objc_msgSend$visibilityEnvironmentIdentifier
+ _objc_msgSend$wantsGlass
+ _objc_msgSend$wantsPlainButtonAppearance
+ _objc_release_x22
+ _objc_retain_x2
+ _objc_retain_x20
+ _swift_beginAccess
+ _swift_bridgeObjectRelease
+ _swift_bridgeObjectRetain
+ _swift_endAccess
+ _swift_getKeyPath
+ _swift_getObjCClassFromMetadata
+ _swift_getObjCClassMetadata
+ _swift_getTypeByMangledNameInContextInMetadataState2
+ _swift_getWitnessTable
+ _swift_retain
+ _symbolic SSSg
+ _symbolic Sb
+ _symbolic SiSg
+ _symbolic So15UITableViewCellC
+ _symbolic _____ 14CarPlaySupport29CPSPointsOfInterestPickerCellC
+ _symbolic _____ 7SwiftUI17EnvironmentValuesV
+ _symbolic _____Sg 5UIKit25UIBackgroundConfigurationV
+ _symbolic _____Sg 7SwiftUI4FontV
+ _symbolic _____yAAyAAy__________ySiSgGGACy_____SgGG_____y_____GGSg 7SwiftUI15ModifiedContentV AA4TextV AA30_EnvironmentKeyWritingModifierV AA4FontV AA016_ForegroundStyleI0V AA5ColorV
+ _symbolic _____yAAy__________ySiSgGGACy_____SgGG 7SwiftUI15ModifiedContentV AA4TextV AA30_EnvironmentKeyWritingModifierV AA4FontV
+ _symbolic _____ySiSgG 7SwiftUI30_EnvironmentKeyWritingModifierV
+ _symbolic _____y_____SgG 7SwiftUI30_EnvironmentKeyWritingModifierV AA4FontV
+ _symbolic _____y___________y_____y_____yADyADy__________ySiSgGGAFy_____SgGG_Qo______y_____GGSg_ADyAmQGSgAUtGG 7SwiftUI13_VariadicViewO4TreeV AA13_VStackLayoutV AA05TupleD0V AA15ModifiedContentV AA0D0PAAE10fontWeightyQrAA4FontV0L0VSgFQO AA4TextV AA30_EnvironmentKeyWritingModifierV AP AA016_ForegroundStyleR0V AA5ColorV
+ _symbolic _____y__________ySiSgGG 7SwiftUI15ModifiedContentV AA4TextV AA30_EnvironmentKeyWritingModifierV
+ _symbolic _____y_____yAAyAAy__________ySiSgGGACy_____SgGG_Qo______y_____GG 7SwiftUI15ModifiedContentV AA4ViewPAAE10fontWeightyQrAA4FontV0G0VSgFQO AA4TextV AA30_EnvironmentKeyWritingModifierV AH AA016_ForegroundStyleM0V AA5ColorV
+ _symbolic _____y_____yAAyAAy__________ySiSgGGACy_____SgGG_Qo______y_____GGSg 7SwiftUI15ModifiedContentV AA4ViewPAAE10fontWeightyQrAA4FontV0G0VSgFQO AA4TextV AA30_EnvironmentKeyWritingModifierV AH AA016_ForegroundStyleM0V AA5ColorV
+ _symbolic _____y_____yAAyAAy__________ySiSgGGACy_____SgGG_Qo______y_____GGSg_AAyAjNGSgARt 7SwiftUI15ModifiedContentV AA4ViewPAAE10fontWeightyQrAA4FontV0G0VSgFQO AA4TextV AA30_EnvironmentKeyWritingModifierV AH AA016_ForegroundStyleM0V AA5ColorV
+ _symbolic _____y_____yAAy__________ySiSgGGACy_____SgGG_Qo_ 7SwiftUI4ViewPAAE10fontWeightyQrAA4FontV0E0VSgFQO AA15ModifiedContentV AA4TextV AA30_EnvironmentKeyWritingModifierV AF
+ _symbolic _____y_____y_____y_____yACyACy__________ySiSgGGAEy_____SgGG_Qo______y_____GGSg_ACyAlPGSgATtGG 7SwiftUI6VStackV AA9TupleViewV AA15ModifiedContentV AA0E0PAAE10fontWeightyQrAA4FontV0I0VSgFQO AA4TextV AA30_EnvironmentKeyWritingModifierV AL AA016_ForegroundStyleO0V AA5ColorV
+ _symbolic _____y_____y_____y_____y_____yADyADy__________ySiSgGGAFy_____SgGG_Qo______y_____GGSg_ADyAmQGSgAUtGG_____G 7SwiftUI22UIHostingConfigurationV AA6VStackV AA9TupleViewV AA15ModifiedContentV AA0G0PAAE10fontWeightyQrAA4FontV0K0VSgFQO AA4TextV AA30_EnvironmentKeyWritingModifierV AN AA016_ForegroundStyleQ0V AA5ColorV AA05EmptyG0V
- +[CPSEntityStyles pickerCellPrimaryFontColor:]
- +[CPSEntityStyles pickerCellPrimaryFont]
- +[CPSEntityStyles pickerCellSecondaryFontColor:]
- +[CPSEntityStyles pickerCellSecondaryFont]
- +[CPSPointsOfInterestPickerCell identifier]
- +[CPSPointsOfInterestPickerExtendedCell identifier]
- -[CPSAudioPlaybackManager nowPlayingViewControllerWillAppear:]
- -[CPSEntityMapButton buttonRadius]
- -[CPSEntityMapButton layoutSubviews]
- -[CPSListTemplateViewController didSelectMediaButton:]
- -[CPSPointsOfInterestPickerCell chosen]
- -[CPSPointsOfInterestPickerCell didUpdateFocusInContext:withAnimationCoordinator:]
- -[CPSPointsOfInterestPickerCell initWithStyle:reuseIdentifier:]
- -[CPSPointsOfInterestPickerCell isSelected]
- -[CPSPointsOfInterestPickerCell prepareForReuse]
- -[CPSPointsOfInterestPickerCell setChosen:]
- -[CPSPointsOfInterestPickerCell setHighlighted:]
- -[CPSPointsOfInterestPickerCell setSelected:animated:]
- -[CPSPointsOfInterestPickerCell setupViews]
- -[CPSPointsOfInterestPickerExtendedCell .cxx_destruct]
- -[CPSPointsOfInterestPickerExtendedCell extendedInformativeLabel]
- -[CPSPointsOfInterestPickerExtendedCell extendedSubtitleLabel]
- -[CPSPointsOfInterestPickerExtendedCell extendedTitleLabel]
- -[CPSPointsOfInterestPickerExtendedCell initWithStyle:reuseIdentifier:]
- -[CPSPointsOfInterestPickerExtendedCell safeAreaInsets]
- -[CPSPointsOfInterestPickerExtendedCell setExtendedInformativeLabel:]
- -[CPSPointsOfInterestPickerExtendedCell setExtendedSubtitleLabel:]
- -[CPSPointsOfInterestPickerExtendedCell setExtendedTitleLabel:]
- -[CPSPointsOfInterestPickerExtendedCell setHighlighted:]
- -[CPSPointsOfInterestPickerExtendedCell setSubtitle:]
- -[CPSPointsOfInterestPickerExtendedCell setText:]
- -[CPSPointsOfInterestPickerExtendedCell setTitle:]
- -[CPSPointsOfInterestPickerExtendedCell setupViews]
- -[CPSPointsOfInterestPickerExtendedCell subtitle]
- -[CPSPointsOfInterestPickerExtendedCell text]
- -[CPSPointsOfInterestPickerExtendedCell title]
- -[CPSPointsOfInterestPickerViewController scrollHeight]
- -[CPSPointsOfInterestPickerViewController setScrollHeight:]
- -[CPSPointsOfInterestTableView _tableContentInset]
- GCC_except_table24
- GCC_except_table30
- _CPMaximumListSectionImageSize
- _OBJC_CLASS_$_CPSPointsOfInterestPickerCell
- _OBJC_CLASS_$_CPSPointsOfInterestPickerExtendedCell
- _OBJC_CLASS_$_CPSTableViewHeaderFooterView
- _OBJC_CLASS_$_CPUIListSectionHeaderView
- _OBJC_IVAR_$_CPSPointsOfInterestPickerCell._chosen
- _OBJC_IVAR_$_CPSPointsOfInterestPickerExtendedCell._extendedInformativeLabel
- _OBJC_IVAR_$_CPSPointsOfInterestPickerExtendedCell._extendedSubtitleLabel
- _OBJC_IVAR_$_CPSPointsOfInterestPickerExtendedCell._extendedTitleLabel
- _OBJC_IVAR_$_CPSPointsOfInterestPickerExtendedCell._subtitle
- _OBJC_IVAR_$_CPSPointsOfInterestPickerExtendedCell._text
- _OBJC_IVAR_$_CPSPointsOfInterestPickerExtendedCell._title
- _OBJC_IVAR_$_CPSPointsOfInterestPickerViewController._scrollHeight
- _OBJC_METACLASS_$_CPSPointsOfInterestPickerCell
- _OBJC_METACLASS_$_CPSPointsOfInterestPickerExtendedCell
- _UIFontTextStyleSubheadline
- _UIImagePNGRepresentation
- __OBJC_$_CLASS_METHODS_CPSPointsOfInterestPickerCell
- __OBJC_$_CLASS_METHODS_CPSPointsOfInterestPickerExtendedCell
- __OBJC_$_INSTANCE_METHODS_CPSPointsOfInterestPickerCell
- __OBJC_$_INSTANCE_METHODS_CPSPointsOfInterestPickerExtendedCell
- __OBJC_$_INSTANCE_VARIABLES_CPSPointsOfInterestPickerCell
- __OBJC_$_INSTANCE_VARIABLES_CPSPointsOfInterestPickerExtendedCell
- __OBJC_$_PROP_LIST_CPSPointsOfInterestPickerCell
- __OBJC_$_PROP_LIST_CPSPointsOfInterestPickerExtendedCell
- __OBJC_CLASS_RO_$_CPSPointsOfInterestPickerCell
- __OBJC_CLASS_RO_$_CPSPointsOfInterestPickerExtendedCell
- __OBJC_METACLASS_RO_$_CPSPointsOfInterestPickerCell
- __OBJC_METACLASS_RO_$_CPSPointsOfInterestPickerExtendedCell
- ___62-[CPSTemplateInstance viewController:didUpdateSafeAreaInsets:]_block_invoke.183
- ___62-[CPSTemplateInstance viewController:didUpdateSafeAreaInsets:]_block_invoke.184
- ___77-[CPSTemplateInstance presentVoiceTemplate:withProxyDelegate:animated:reply:]_block_invoke.105
- ___93-[CPSTemplateInstance pushEntityTemplate:withProxyDelegate:animated:presentationStyle:reply:]_block_invoke.112
- ___93-[CPSTemplateInstance pushSearchTemplate:withProxyDelegate:animated:presentationStyle:reply:]_block_invoke.103
- ___97-[CPSTemplateInstance pushNowPlayingTemplate:withProxyDelegate:animated:presentationStyle:reply:]_block_invoke.100
- ___block_descriptor_48_e8_32s40s_e25_v16?0"CPUIMediaButton"8ls32l8s40l8
- ___block_literal_global.8
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swiftDarwin_$_CarPlaySupport
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_CarPlaySupport
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_CarPlaySupport
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_CarPlaySupport
- _objc_msgSend$_preferredFontDescriptorWithTextStyle:weight:
- _objc_msgSend$backgroundView
- _objc_msgSend$chosen
- _objc_msgSend$dequeueReusableCellWithIdentifier:
- _objc_msgSend$detailTextLabel
- _objc_msgSend$extendedInformativeLabel
- _objc_msgSend$extendedSubtitleLabel
- _objc_msgSend$extendedTitleLabel
- _objc_msgSend$initForUseInTabBar:
- _objc_msgSend$initWithId:title:subtitle:image:imageShape:backgroundColor:isTallArtwork:accessorySystemImage:isDisabled:action:
- _objc_msgSend$initWithImage:title:subtitle:enabled:
- _objc_msgSend$pickerCellPrimaryFont
- _objc_msgSend$pickerCellPrimaryFontColor:
- _objc_msgSend$pickerCellSecondaryFont
- _objc_msgSend$pickerCellSecondaryFontColor:
- _objc_msgSend$scrollHeight
- _objc_msgSend$secondarySystemFillColor
- _objc_msgSend$setBackButtonTitle:
- _objc_msgSend$setBackgroundView:
- _objc_msgSend$setBorderWidth:
- _objc_msgSend$setImageSize:
- _objc_msgSend$setScrollHeight:
- _objc_msgSend$setTag:
- _objc_msgSend$showImageFullHeight
- _objc_msgSend$systemCyanColor
- _objc_msgSend$textLabel
- _objc_msgSend$titleColorForState:
- _objc_msgSend$viewWithTag:
- _tableView:viewForHeaderInSection:.headerTitleTag
CStrings:
+ "@\"<CPSVisibilityEnvironmentProviding>\""
+ "CPSVisibilityEnvironmentProviding"
+ "StateCapture"
+ "T@\"<CPSVisibilityEnvironmentProviding>\",W,N,V_environmentProvider"
+ "T@\"NSString\",N,C"
+ "T@\"NSString\",N,R"
+ "TB,N,V_wantsGlass"
+ "TB,N,Vchosen"
+ "_TtC14CarPlaySupport29CPSPointsOfInterestPickerCell"
+ "_bridgedUpdateConfigurationUsingState:"
+ "_carSystemFocusSecondaryColor"
+ "_environmentProvider"
+ "_wantsGlass"
+ "didSelectHeaderButtonWithIdentifier:"
+ "environmentProvider"
+ "identityToken"
+ "initWithId:title:subtitle:image:imageShape:backgroundColor:isTallArtwork:accessorySystemImage:allowsTouches:disabledAppearance:action:"
+ "initWithId:title:subtitle:image:imageShape:backgroundColor:isTallArtwork:accessorySystemImage:allowsTouches:disabledAppearance:canStayPressed:action:"
+ "initWithImage:title:subtitle:allowsTouches:disabledAppearance:"
+ "plainButtonConfiguration"
+ "setButtonAction:"
+ "setContentInsets:"
+ "setEnvironmentProvider:"
+ "setLabelText:"
+ "setStrokeColor:"
+ "setTertiaryTitle:"
+ "setTitleLineBreakMode:"
+ "setWantsGlass:"
+ "showsImageFullHeight"
+ "tertiaryTitle"
+ "visibilityEnvironmentIdentifier"
+ "wantsGlass"
+ "wantsPlainButtonAppearance"
- "CPSPointsOfInterestPickerCell"
- "CPSPointsOfInterestPickerExtendedCell"
- "NOW_PLAYING_BACK"
- "T@\"NSString\",&,N,V_subtitle"
- "T@\"NSString\",&,N,V_text"
- "T@\"NSString\",&,N,V_title"
- "T@\"UILabel\",&,N,V_extendedInformativeLabel"
- "T@\"UILabel\",&,N,V_extendedSubtitleLabel"
- "T@\"UILabel\",&,N,V_extendedTitleLabel"
- "TB,N,V_chosen"
- "Td,N,V_scrollHeight"
- "_chosen"
- "_extendedInformativeLabel"
- "_extendedSubtitleLabel"
- "_extendedTitleLabel"
- "_preferredFontDescriptorWithTextStyle:weight:"
- "_scrollHeight"
- "_subtitle"
- "dequeueReusableCellWithIdentifier:"
- "detailTextLabel"
- "didSelectMediaButton:"
- "extendedInformativeLabel"
- "extendedSubtitleLabel"
- "extendedTitleLabel"
- "initForUseInTabBar:"
- "initWithId:title:subtitle:image:imageShape:backgroundColor:isTallArtwork:accessorySystemImage:isDisabled:action:"
- "initWithImage:title:subtitle:enabled:"
- "nowPlayingViewControllerWillAppear:"
- "pickerCellPrimaryFont"
- "pickerCellPrimaryFontColor:"
- "pickerCellSecondaryFont"
- "pickerCellSecondaryFontColor:"
- "scrollHeight"
- "secondarySystemFillColor"
- "setBackButtonTitle:"
- "setBorderWidth:"
- "setExtendedInformativeLabel:"
- "setExtendedSubtitleLabel:"
- "setExtendedTitleLabel:"
- "setImageSize:"
- "setScrollHeight:"
- "setTag:"
- "showImageFullHeight"
- "systemCyanColor"
- "textLabel"
- "titleColorForState:"
- "v16@?0@\"CPUIMediaButton\"8"
- "viewWithTag:"

```
