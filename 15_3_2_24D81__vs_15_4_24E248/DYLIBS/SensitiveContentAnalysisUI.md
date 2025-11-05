## SensitiveContentAnalysisUI

> `/System/iOSSupport/System/Library/PrivateFrameworks/SensitiveContentAnalysisUI.framework/Versions/A/SensitiveContentAnalysisUI`

```diff

-88.1.0.0.0
-  __TEXT.__text: 0xcd634
-  __TEXT.__auth_stubs: 0x3060
-  __TEXT.__objc_methlist: 0x10c8
-  __TEXT.__const: 0x6bd4
-  __TEXT.__cstring: 0x2884
-  __TEXT.__gcc_except_tab: 0x264
-  __TEXT.__dlopen_cstrs: 0xfc
-  __TEXT.__oslogstring: 0x593
+91.14.0.0.0
+  __TEXT.__text: 0xca638
+  __TEXT.__auth_stubs: 0x3000
+  __TEXT.__objc_methlist: 0x14a8
+  __TEXT.__const: 0x6bc4
+  __TEXT.__cstring: 0x2654
+  __TEXT.__gcc_except_tab: 0x29c
+  __TEXT.__dlopen_cstrs: 0x148
+  __TEXT.__oslogstring: 0x5d3
   __TEXT.__ustring: 0x42
-  __TEXT.__swift5_typeref: 0x81dc
+  __TEXT.__swift5_typeref: 0x80f4
   __TEXT.__swift5_reflstr: 0x18c1
   __TEXT.__swift5_assocty: 0x990
   __TEXT.__constg_swiftt: 0x2144
-  __TEXT.__swift5_fieldmd: 0x1ee4
+  __TEXT.__swift5_fieldmd: 0x1ecc
   __TEXT.__swift5_proto: 0x540
   __TEXT.__swift5_types: 0x270
   __TEXT.__swift5_builtin: 0x1a4
   __TEXT.__swift5_capture: 0x818
+  __TEXT.__swift_as_entry: 0x74
+  __TEXT.__swift_as_ret: 0x88
   __TEXT.__swift5_mpenum: 0x38
   __TEXT.__swift5_protos: 0xc
-  __TEXT.__unwind_info: 0x2b18
-  __TEXT.__eh_frame: 0x27a0
-  __TEXT.__objc_classname: 0x3b1
-  __TEXT.__objc_methname: 0x3717
-  __TEXT.__objc_methtype: 0x8ce
-  __TEXT.__objc_stubs: 0x26a0
-  __DATA_CONST.__got: 0xc10
-  __DATA_CONST.__const: 0x460
-  __DATA_CONST.__objc_classlist: 0x130
-  __DATA_CONST.__objc_catlist: 0x8
+  __TEXT.__unwind_info: 0x2868
+  __TEXT.__eh_frame: 0x28b8
+  __TEXT.__objc_classname: 0x3c3
+  __TEXT.__objc_methname: 0x382e
+  __TEXT.__objc_methtype: 0x912
+  __TEXT.__objc_stubs: 0x27a0
+  __DATA_CONST.__got: 0xc20
+  __DATA_CONST.__const: 0x3f8
+  __DATA_CONST.__objc_classlist: 0x138
+  __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xe30
+  __DATA_CONST.__objc_selrefs: 0xfa8
   __DATA_CONST.__objc_protorefs: 0x40
   __DATA_CONST.__objc_superrefs: 0x68
-  __AUTH_CONST.__auth_got: 0x1840
-  __AUTH_CONST.__const: 0x4030
+  __AUTH_CONST.__auth_got: 0x1810
+  __AUTH_CONST.__const: 0x40f8
   __AUTH_CONST.__cfstring: 0xd80
-  __AUTH_CONST.__objc_const: 0x3620
-  __AUTH.__objc_data: 0xef8
+  __AUTH_CONST.__objc_const: 0x30b0
+  __AUTH.__objc_data: 0xf48
   __AUTH.__data: 0x1910
   __DATA.__objc_ivar: 0x178
-  __DATA.__data: 0x2398
+  __DATA.__data: 0x23a8
   __DATA.__objc_stublist: 0x8
-  __DATA.__bss: 0xb0a0
-  __DATA.__common: 0xf0
+  __DATA.__bss: 0xb0b0
+  __DATA.__common: 0xd8
   - /System/Library/Frameworks/AVFoundation.framework/Versions/A/AVFoundation
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
   - /System/Library/Frameworks/CloudKit.framework/Versions/A/CloudKit

   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
-  - /usr/lib/swift/libswiftFileProvider.dylib
   - /usr/lib/swift/libswiftIOKit.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 80A6BBA7-79A2-3CA7-8BD7-29C1E3AC954C
-  Functions: 3682
-  Symbols:   2488
-  CStrings:  1235
+  UUID: 5BC813E7-F5E2-3B5E-AD62-F2AFF418E72D
+  Functions: 3588
+  Symbols:   2541
+  CStrings:  1241
 
Symbols:
+ +[SCUIAccountHelper _getValidAccountAlias:]
+ +[SCUIAccountHelper bestHandleID:]
+ +[SCUIAccountHelper bestiMessageServiceHandle]
+ +[SCUIAccountHelper isiMessageLoggedIn]
+ +[SCUIAnalytics sharedInstance].cold.1
+ +[SCUISystemInfo isInternal].cold.1
+ -[SCUIReportSuspect initWithDisplayName:accountID:sensitiveMediaFiles:]
+ -[SCUIReportVictim initWithDisplayName:accountID:mediaFiles:]
+ _OBJC_CLASS_$_NSMutableSet
+ _OBJC_CLASS_$_SCUIAccountHelper
+ _OBJC_METACLASS_$_SCUIAccountHelper
+ __CATEGORY_INSTANCE_METHODS_NSString_$_SensitiveContentAnalysisUI
+ __CATEGORY_NSString_$_SensitiveContentAnalysisUI
+ __CATEGORY_PROPERTIES_NSString_$_SensitiveContentAnalysisUI
+ __OBJC_$_CLASS_METHODS_SCUIAccountHelper
+ __OBJC_$_CLASS_PROP_LIST_SCUIAccountHelper
+ __OBJC_CLASS_RO_$_SCUIAccountHelper
+ __OBJC_METACLASS_RO_$_SCUIAccountHelper
+ ___getIMAccountControllerClass_block_invoke
+ ___getIMServiceClass_block_invoke
+ ___swift_async_entry_functlets
+ ___swift_async_ret_functlets
+ ___swift_project_boxed_opaque_existential_0Tm
+ __getIMAccountControllerClass_block_invoke.cold.1
+ __getIMServiceClass_block_invoke.cold.1
+ _objc_msgSend$_getValidAccountAlias:
+ _objc_msgSend$account
+ _objc_msgSend$activeAccountsForService:
+ _objc_msgSend$aliases
+ _objc_msgSend$bestHandleID:
+ _objc_msgSend$bestiMessageServiceHandle
+ _objc_msgSend$guid
+ _objc_msgSend$iMessageService
+ _objc_msgSend$initWithDisplayName:accountID:mediaFiles:
+ _objc_msgSend$initWithDisplayName:accountID:sensitiveMediaFiles:
+ _objc_msgSend$loginIMHandle
+ _objc_msgSend$scui_isValidAccountID
+ _objc_msgSend$scui_prependingAccountIDPrefix
+ _symbolic SccySo21SCSensitivityAnalysisC______pG s5ErrorP
+ _symbolic SccySo8CKRecordC______pG s5ErrorP
+ _symbolic Sccyyt______pG s5ErrorP
+ _symbolic _____yAAyx_____G_____G 7SwiftUI15ModifiedContentV 09Sensitived8AnalysisB00eD8Redactor33_F475A732BF088C4D34EBB563F60DEE35LLV AD0eD13PolicyUpdaterAFLLV
+ _symbolic _____y_____SgG s23_ContiguousArrayStorageC 10Foundation6LocaleV6RegionV
+ block_copy_helper.44
+ block_copy_helper.47
+ block_descriptor.49
+ block_destroy_helper.45
+ block_destroy_helper.48
+ getIMAccountControllerClass.softClass
+ getIMServiceClass.softClass
+ get_witness_table 7SwiftUI15ModifiedContentVyACyAA4ViewPAAE5sheet11isPresented9onDismiss7contentQrAA7BindingVySbG_yycSgqd__yctAaDRd__lFQOyAeAE0I10TapGesture5count7performQrSi_yyctFQOyACyACyAeAE0I6Change2of7initial_Qrqd___SbyyctSQRd__lFQOyAeAEAqrS_Qrqd___SbyyctSQRd__lFQOyAeAEAqrS_Qrqd___SbyyctSQRd__lFQOyAA01_e9Modifier_D0Vy09Sensitived8AnalysisB00uD8Redactor33_F475A732BF088C4D34EBB563F60DEE35LLVG_AV09ScannableD0OSgQo__0udV00uD6PolicyVSgQo__A3_011SensitivityV0VSgQo_AA08_OverlayT0VyAA012_ConditionalD0VyA15_yAA05EmptyE0VAV0ud4BlurE0VGA15_yA15_yA19_A19_GA19_GGSgGGAA23_CompositingGroupEffectVG_Qo__AV012InterventionE0VSgQo_A13_yA15_yA15_yA17_A17_GAV17WarningMenuButtonVGSgGGA13_yA15_yA35_AV04ShowD6ButtonVGSgGGAaDHPA41_AaDHPqd0__AaDHD3_A34_HO_A40_AA0eT0HPyHCHC_A46_AAA48_HPyHCHC.57
+ get_witness_table 7SwiftUI19_ConditionalContentVyAA014_ViewModifier_D0Vy09Sensitived8AnalysisB00gD13PolicyUpdater33_F475A732BF088C4D34EBB563F60DEE35LLVGAA08ModifiedD0VyALyALyAjA022_EnvironmentKeyWritingF0Vy0gdH00gdI0VSgGGANySbGGAA010_TaskValueF0VySSSgGGGAA0E0HPAjAA1_HPyHC_A_AAA1_HPAvAA1_HPAtAA1_HPAjAA1_HPyHC_AsA0eF0HPyHCHC_AuAA2_HPyHCHC_AzAA2_HPyHCHCHC.58
+ get_witness_table 7SwiftUI4ViewRzlAA15ModifiedContentVyADyx09Sensitivee8AnalysisB00fE8Redactor33_F475A732BF088C4D34EBB563F60DEE35LLVGAE0fE13PolicyUpdaterAGLLVGAaBHPAiaBHPxAaBHD1__AhA0C8ModifierHPyHCHC_AkaMHPyHCHC.4
+ objectdestroy.26Tm
- -[SCUIReportSuspect initWithDisplayName:sensitiveMediaFiles:]
- -[SCUIReportSuspect setAccountID:]
- -[SCUIReportVictim initWithDisplayName:mediaFiles:]
- -[SCUIReportVictim setAccountID:]
- __swift_FORCE_LOAD_$_swiftFileProvider
- __swift_FORCE_LOAD_$_swiftFileProvider_$_SensitiveContentAnalysisUI
- _objc_msgSend$initWithDisplayName:mediaFiles:
- _objc_msgSend$initWithDisplayName:sensitiveMediaFiles:
- _objc_msgSend$isFromMe
- _objc_msgSend$setAccountID:
- _objc_msgSend$subject
- _symbolic _____yAAy_____y_____y__________yACyAAy__________G_____GGGG_____y_____SgGG_____G 7SwiftUI15ModifiedContentV AA5GroupV AA012_ConditionalD0V 09Sensitived8AnalysisB05VideoV AA10AsyncImageV AA0K0V AA18_AspectRatioLayoutV AA9EmptyViewV AA16_OverlayModifierV AH0gd4BlurP0V AA012_CompositingE6EffectV
- _symbolic _____y_Qo_ 26SensitiveContentAnalysisUI0aB13PolicyUpdater33_F475A732BF088C4D34EBB563F60DEE35LLV4body7contentQr05SwiftD0014_ViewModifier_B0VyADG_tFQO
- _symbolic _____y_Qo_ 26SensitiveContentAnalysisUI0aB8BlurViewV4bodyQrvpQO
- _symbolic _____y_Qo_ 26SensitiveContentAnalysisUI0aB8Redactor33_F475A732BF088C4D34EBB563F60DEE35LLV4body7contentQr05SwiftD0014_ViewModifier_B0VyADG_tFQO
- _symbolic _____y_____y_____yABy_____yADy__________yAFyAFy__________y_____GG_____y_____SgGG_____GGADyA2PGG_ADyADyAFyAFyAFy_____ALy_____GGAOGAJGA_GAEGtGG_AU_____y_____AIGtGGSg 7SwiftUI12ViewThatFitsV AA05TupleC0V AA6VStackV AA19_ConditionalContentV AA05EmptyC0V AA08ModifiedI0V AA5ImageV AA24_ForegroundStyleModifierV AA5ColorV AA022_EnvironmentKeyWritingO0V AA4FontV AA14_PaddingLayoutV AA4TextV AA0W9AlignmentO AA06_ShapeC0V AA9RectangleV
- _symbolic _____y_____yx_____G_Qo_ 7SwiftUI4ViewP024SensitiveContentAnalysisB0E08prefetchdE6Policy06forcedH07optionsQr0deF00deH0VSg_So013SCUISensitiveE14OverlayOptionsVtFQO AA08ModifiedE0V AD0dE8Redactor33_F475A732BF088C4D34EBB563F60DEE35LLV
- _symbolic _____y_x_Qo_ 26SensitiveContentAnalysisUI6ReportC4LinkV4bodyQrvpQO
- _symbolic _____y_xq__Qo_ 26SensitiveContentAnalysisUI6ReportC7SectionV4bodyQrvpQO
- _symbolic _____yx_Qo_ 7SwiftUI4ViewP024SensitiveContentAnalysisB0E09sensitiveE7Overlay_8analysis7optionsQrAD09ScannableE0OSg_AA7BindingVy0deF0011SensitivityF0VSgGSo013SCUISensitiveeH7OptionsVtFQO
- block_descriptor.45
- get_witness_table 7SwiftUI15ModifiedContentVyACyAA4ViewPAAE5sheet11isPresented9onDismiss7contentQrAA7BindingVySbG_yycSgqd__yctAaDRd__lFQOyAeAE0I10TapGesture5count7performQrSi_yyctFQOyACyACyAeAE0I6Change2of7initial_Qrqd___SbyyctSQRd__lFQOyAeAEAqrS_Qrqd___SbyyctSQRd__lFQOyAeAEAqrS_Qrqd___SbyyctSQRd__lFQOyAA01_e9Modifier_D0Vy09Sensitived8AnalysisB00uD8Redactor33_F475A732BF088C4D34EBB563F60DEE35LLVG_AV09ScannableD0OSgQo__0udV00uD6PolicyVSgQo__A3_011SensitivityV0VSgQo_AA08_OverlayT0VyAA012_ConditionalD0VyA15_yAA05EmptyE0VAV0ud4BlurE0VGA15_yA15_yA19_A19_GA19_GGSgGGAA23_CompositingGroupEffectVG_Qo__AV012InterventionE0VSgQo_A13_yA15_yA15_yA17_A17_GAV17WarningMenuButtonVGSgGGA13_yA15_yA35_AV04ShowD6ButtonVGSgGGAaDHPA41_AaDHPqd0__AaDHD3_A34_HO_A40_AA0eT0HPyHCHC_A46_AAA48_HPyHCHC.54
- get_witness_table 7SwiftUI19_ConditionalContentVyAA014_ViewModifier_D0Vy09Sensitived8AnalysisB00gD13PolicyUpdater33_F475A732BF088C4D34EBB563F60DEE35LLVGAA08ModifiedD0VyALyALyAjA022_EnvironmentKeyWritingF0Vy0gdH00gdI0VSgGGANySbGGAA010_TaskValueF0VySSSgGGGAA0E0HPAjAA1_HPyHC_A_AAA1_HPAvAA1_HPAtAA1_HPAjAA1_HPyHC_AsA0eF0HPyHCHC_AuAA2_HPyHCHC_AzAA2_HPyHCHCHC.55
- get_witness_table 7SwiftUI4ViewRzlqd__AaBHD2_AaBP024SensitiveContentAnalysisB0E08prefetchdE6Policy06forcedH07optionsQr0deF00deH0VSg_So013SCUISensitiveE14OverlayOptionsVtFQOyAA08ModifiedE0VyxAD0dE8Redactor33_F475A732BF088C4D34EBB563F60DEE35LLVG_Qo_HO.5
- get_witness_table 7SwiftUI4ViewRzlqd__AaBHD2_AaBP024SensitiveContentAnalysisB0E09sensitiveE7Overlay_8analysis7optionsQrAD09ScannableE0OSg_AA7BindingVy0deF0011SensitivityF0VSgGSo013SCUISensitiveeH7OptionsVtFQOyx_Qo_HO.4
- objectdestroy.27Tm
CStrings:
+ "IMAccountController"
+ "IMService"
+ "SCUIAccountHelper"
+ "SensitiveContentAnalysisUI"
+ "SensitiveContentAuthority"
+ "T@\"NSString\",N,R"
+ "T@\"NSString\",R,C,V_accountID"
+ "TB,N,R"
+ "_getValidAccountAlias:"
+ "account"
+ "activeAccountsForService:"
+ "aliases"
+ "bestHandleID:"
+ "bestiMessageServiceHandle"
+ "guid"
+ "iMessage is not logged in, cannot report to Apple"
+ "iMessageService"
+ "init(frame:)"
+ "initWithDisplayName:accountID:mediaFiles:"
+ "initWithDisplayName:accountID:sensitiveMediaFiles:"
+ "isiMessageLoggedIn"
+ "loginIMHandle"
+ "scui_isValidAccountID"
+ "scui_prependingAccountIDPrefix"
+ "v44@0:8@\"WKWebView\"16@\"WKBackForwardListItem\"24B32@?<v@?B>36"
+ "v44@0:8@16@24B32@?36"
+ "webView:shouldGoToBackForwardListItem:willUseInstantBack:completionHandler:"
- "@32@0:8@16@24"
- "Division by zero"
- "Division results in an overflow"
- "Insufficient space allocated to copy string contents"
- "No account ID for reporter"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/IntegerTypes.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "T@\"NSString\",C,V_accountID"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutablePointer.initialize with negative count"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "initWithDisplayName:mediaFiles:"
- "initWithDisplayName:sensitiveMediaFiles:"
- "invalid Collection: less than 'count' elements in collection"
- "isFromMe"
- "setAccountID:"
- "subject"

```
