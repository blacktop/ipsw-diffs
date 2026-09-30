## WritingToolsUI

> `/System/Library/PrivateFrameworks/WritingToolsUI.framework/WritingToolsUI`

```diff

-44.504.1.0.0
-  __TEXT.__text: 0x2d188
-  __TEXT.__auth_stubs: 0xd30
-  __TEXT.__objc_methlist: 0x3684
-  __TEXT.__const: 0xa74
-  __TEXT.__cstring: 0x1dbe
+44.505.0.0.0
+  __TEXT.__text: 0x2ddc0
+  __TEXT.__auth_stubs: 0xd60
+  __TEXT.__objc_methlist: 0x36fc
+  __TEXT.__const: 0xaa4
+  __TEXT.__cstring: 0x1f0e
   __TEXT.__gcc_except_tab: 0x908
   __TEXT.__oslogstring: 0xc90
   __TEXT.__dlopen_cstrs: 0xb4
-  __TEXT.__constg_swiftt: 0x4b4
-  __TEXT.__swift5_typeref: 0x2a4
+  __TEXT.__constg_swiftt: 0x520
+  __TEXT.__swift5_typeref: 0x2ec
   __TEXT.__swift5_builtin: 0x64
-  __TEXT.__swift5_reflstr: 0x445
-  __TEXT.__swift5_fieldmd: 0x39c
+  __TEXT.__swift5_reflstr: 0x475
+  __TEXT.__swift5_fieldmd: 0x3dc
   __TEXT.__swift5_assocty: 0xa8
   __TEXT.__swift5_proto: 0x44
-  __TEXT.__swift5_types: 0x30
+  __TEXT.__swift5_types: 0x34
   __TEXT.__swift5_capture: 0x70
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0xd78
+  __TEXT.__unwind_info: 0xdb8
   __TEXT.__eh_frame: 0xf8
   __TEXT.__objc_classname: 0x61a
-  __TEXT.__objc_methname: 0x9233
-  __TEXT.__objc_methtype: 0x208f
-  __TEXT.__objc_stubs: 0x6400
+  __TEXT.__objc_methname: 0x9338
+  __TEXT.__objc_methtype: 0x20a7
+  __TEXT.__objc_stubs: 0x6480
   __DATA_CONST.__got: 0x4e8
-  __DATA_CONST.__const: 0x8f0
-  __DATA_CONST.__objc_classlist: 0x128
+  __DATA_CONST.__const: 0x900
+  __DATA_CONST.__objc_classlist: 0x130
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0xd8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2480
+  __DATA_CONST.__objc_selrefs: 0x24c8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0xa8
-  __AUTH_CONST.__auth_got: 0x6a8
+  __AUTH_CONST.__auth_got: 0x6c0
   __AUTH_CONST.__auth_ptr: 0x278
-  __AUTH_CONST.__const: 0x750
-  __AUTH_CONST.__cfstring: 0x9a0
-  __AUTH_CONST.__objc_const: 0x4d50
+  __AUTH_CONST.__const: 0x768
+  __AUTH_CONST.__cfstring: 0x9e0
+  __AUTH_CONST.__objc_const: 0x4e40
   __AUTH_CONST.__objc_intobj: 0x3d8
-  __AUTH.__objc_data: 0xe38
-  __AUTH.__data: 0x1b8
-  __DATA.__objc_ivar: 0x270
-  __DATA.__data: 0xbb8
+  __AUTH.__objc_data: 0xf38
+  __AUTH.__data: 0x1e0
+  __DATA.__objc_ivar: 0x274
+  __DATA.__data: 0xbf0
   __DATA.__bss: 0x9c0
-  __DATA.__common: 0x60
+  __DATA.__common: 0x70
   __DATA_DIRTY.__objc_data: 0xa0
   __DATA_DIRTY.__data: 0x38
   __DATA_DIRTY.__bss: 0x90

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 1338
-  Symbols:   3832
-  CStrings:  2163
+  Functions: 1367
+  Symbols:   3853
+  CStrings:  2188
 
Symbols:
+ +[WTUIActionClientToHost actionForHandoffFromUCBFromTool:withPrompt:]
+ -[WTFormSheetViewController handoffFromUCBFromTool:withPrompt:]
+ -[WTSceneHostedInputDashboardViewController handoffFromUCBFromTool:withPrompt:]
+ -[WTWritingToolsController handoffFromUCBFromTool:withPrompt:]
+ -[WTWritingToolsController handoffOriginatorTool]
+ -[WTWritingToolsController setHandoffOriginatorTool:]
+ _OBJC_CLASS_$__TtC14WritingToolsUI27WTAlertHeaderViewController
+ _OBJC_IVAR_$_WTWritingToolsController._handoffOriginatorTool
+ _OBJC_METACLASS_$__TtC14WritingToolsUI27WTAlertHeaderViewController
+ __DATA__TtC14WritingToolsUI27WTAlertHeaderViewController
+ __INSTANCE_METHODS__TtC14WritingToolsUI27WTAlertHeaderViewController
+ __IVARS__TtC14WritingToolsUI27WTAlertHeaderViewController
+ __METACLASS_DATA__TtC14WritingToolsUI27WTAlertHeaderViewController
+ ___58-[WTWritingToolsController itemProviderForAttributedText:]_block_invoke.545
+ ___block_descriptor_40_e8_32bs_e23_v16?0"UIAlertAction"8ls32l8
+ __swift_stdlib_reportUnimplementedInitializer
+ _keypath_get.18Tm
+ _keypath_get.20Tm
+ _keypath_get.26Tm
+ _keypath_get.38Tm
+ _keypath_set.21Tm
+ _keypath_setTm
+ _objc_msgSend$_setHeaderContentViewController:
+ _objc_msgSend$_systemImageNamed:
+ _objc_msgSend$handoffFromUCBFromTool:withPrompt:
+ _objc_msgSend$handoffOriginatorTool
+ _objc_msgSend$setHandoffOriginatorTool:
+ _objc_retain_x26
+ _symbolic So11UIImageViewCSg
+ _symbolic So16UIViewControllerC
+ _symbolic So7UIImageC
+ _symbolic _____ 14WritingToolsUI27WTAlertHeaderViewControllerC
+ _symbolic _____yyXlG s23_ContiguousArrayStorageC
- +[WTUIActionClientToHost actionForHandoffFromUCBWithPrompt:]
- -[WTFormSheetViewController handoffFromUCBWithPrompt:]
- -[WTSceneHostedInputDashboardViewController handoffFromUCBWithPrompt:]
- -[WTWritingToolsController handoffFromUCBWithPrompt:]
- ___58-[WTWritingToolsController itemProviderForAttributedText:]_block_invoke.537
- ___block_descriptor_48_e8_32s40bs_e23_v16?0"UIAlertAction"8ls32l8s40l8
- _keypath_get.15Tm
- _keypath_get.17Tm
- _keypath_get.23Tm
- _keypath_get.35Tm
- _keypath_set.16Tm
- _keypath_set.18Tm
- _objc_msgSend$handoffFromUCBWithPrompt:
- _objc_retain_x28
CStrings:
+ "!\xb2\"\x13"
+ "Fatal error"
+ "T@\"NSString\",&,N,V_prompt"
+ "T@\"WTSmartReplyConfiguration\",&,N,V_smartReplyConfig"
+ "TB,N,V_isWritingToolsActive"
+ "Tq,N,V_handoffOriginatorTool"
+ "Tq,N,V_requestedTool"
+ "Tq,N,VhandoffOriginatorTool"
+ "W\x11\"!2"
+ "WTUnsafeInputErrorKey"
+ "WritingToolsUI.WTAlertHeaderViewController"
+ "WritingToolsUI/WTAlertHeaderViewController.swift"
+ "_TtC14WritingToolsUI27WTAlertHeaderViewController"
+ "_handoffOriginatorTool"
+ "_setHeaderContentViewController:"
+ "_systemImageNamed:"
+ "actionForHandoffFromUCBFromTool:withPrompt:"
+ "handoffFromUCBFromTool:withPrompt:"
+ "handoffOriginatorTool"
+ "heightAnchor"
+ "image"
+ "imageView"
+ "init(nibName:bundle:)"
+ "initWithNibName:bundle:"
+ "nosign.badge.shield.half.filled"
+ "secondaryLabelColor"
+ "setHandoffOriginatorTool:"
+ "setTintColor:"
+ "v32@0:8q16@\"NSString\"24"
+ "viewDidLoad"
- "!\xa2\"\x13"
- "G\x11\"!2"
- "T@\"NSString\",&,V_prompt"
- "T@\"WTSmartReplyConfiguration\",&,V_smartReplyConfig"
- "TB,V_isWritingToolsActive"
- "Tq,V_requestedTool"
- "actionForHandoffFromUCBWithPrompt:"
- "handoffFromUCBWithPrompt:"

```
