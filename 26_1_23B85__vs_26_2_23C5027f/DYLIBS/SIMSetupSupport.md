## SIMSetupSupport

> `/System/Library/PrivateFrameworks/SIMSetupSupport.framework/SIMSetupSupport`

```diff

-881.0.0.0.0
-  __TEXT.__text: 0xb9024
+883.1.0.0.0
+  __TEXT.__text: 0xb94d4
   __TEXT.__auth_stubs: 0x840
-  __TEXT.__objc_methlist: 0xa3a4
+  __TEXT.__objc_methlist: 0xa3b4
   __TEXT.__const: 0x1d0
-  __TEXT.__gcc_except_tab: 0x1db8
-  __TEXT.__cstring: 0x1074d
-  __TEXT.__oslogstring: 0x6aa3
+  __TEXT.__gcc_except_tab: 0x1dc0
+  __TEXT.__cstring: 0x10769
+  __TEXT.__oslogstring: 0x6b9c
   __TEXT.__dlopen_cstrs: 0x2be
   __TEXT.__ustring: 0xa
-  __TEXT.__unwind_info: 0x2640
-  __TEXT.__objc_classname: 0x15e4
-  __TEXT.__objc_methname: 0x16eb9
-  __TEXT.__objc_methtype: 0x356e
-  __TEXT.__objc_stubs: 0xe660
+  __TEXT.__unwind_info: 0x2648
+  __TEXT.__objc_classname: 0x15de
+  __TEXT.__objc_methname: 0x16f1d
+  __TEXT.__objc_methtype: 0x35f6
+  __TEXT.__objc_stubs: 0xe680
   __DATA_CONST.__got: 0xa78
   __DATA_CONST.__const: 0x1db0
   __DATA_CONST.__objc_classlist: 0x488
   __DATA_CONST.__objc_catlist: 0x70
   __DATA_CONST.__objc_protolist: 0xf8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x52b8
+  __DATA_CONST.__objc_selrefs: 0x52c8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x430
   __DATA_CONST.__objc_arraydata: 0x1a8
   __AUTH_CONST.__auth_got: 0x430
   __AUTH_CONST.__const: 0x8e0
-  __AUTH_CONST.__cfstring: 0x7980
-  __AUTH_CONST.__objc_const: 0x3df90
+  __AUTH_CONST.__cfstring: 0x79a0
+  __AUTH_CONST.__objc_const: 0x3dfb8
   __AUTH_CONST.__objc_intobj: 0x6c0
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0xf0
   __AUTH.__objc_data: 0x2d00
-  __DATA.__objc_ivar: 0xefc
+  __DATA.__objc_ivar: 0xf00
   __DATA.__data: 0xbb0
   __DATA.__bss: 0x170
   __DATA_DIRTY.__objc_data: 0x50

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F88B7EE3-4272-343E-AC94-180E935F6AAF
-  Functions: 3971
-  Symbols:   14330
-  CStrings:  7565
+  UUID: 6F889063-62AF-330E-8D32-1E7ACBCF4F1D
+  Functions: 3973
+  Symbols:   14335
+  CStrings:  7575
 
Symbols:
+ -[SSQRCodeIntroViewController _needOfferOtherOptions]
+ -[TSCellularPlanActivatingFlow(UpdatePlanInfo) _updateInstallError:withPlanID:webUrl:postData:].cold.2
+ -[UIViewController(SimSetup) flow]
+ GCC_except_table227
+ _OBJC_IVAR_$_TSCrossPlatformTargetTransferFlow._firstViewControllerCallback
+ _OBJC_IVAR_$_TSTravelBuddyViewController._didInstallationFail
+ __OBJC_$_CATEGORY_UIViewController_$_InModalPresentation
+ __OBJC_$_INSTANCE_METHODS_UIViewController(InModalPresentation|SubFlow|SimSetup|NavigationBar)
+ ___115-[TSCellularPlanActivatingFlow(CoreTelephonyClientCellularPlanManagementDelegate) handleWaitingOnWifiStatusUpdate:]_block_invoke.500
+ ___62-[TSSIMSetupFlow navigateToNextPaneFrom:navigationController:]_block_invoke.177
+ ___62-[TSSIMSetupFlow navigateToNextPaneFrom:navigationController:]_block_invoke.180
+ ___74-[TSCellularPlanActivatingFlow(TSSIMSetupDelegate) simSetupFlowCompleted:]_block_invoke.546
+ ___82-[TSCellularPlanActivatingFlow(InteractiveUI) _displayIntermediateViewController:]_block_invoke.608
+ ___82-[TSCellularPlanActivatingFlow(TSSIMSetupFlowDelegate) viewControllerDidComplete:]_block_invoke.557
+ ___82-[TSCellularPlanActivatingFlow(TSSIMSetupFlowDelegate) viewControllerDidComplete:]_block_invoke.557.cold.1
+ ___block_literal_global.410
+ ___block_literal_global.499
+ ___block_literal_global.502
+ ___block_literal_global.559
+ _objc_msgSend$_needOfferOtherOptions
- -[UIViewController(Flow) flow]
- GCC_except_table226
- _OBJC_IVAR_$_TSCrossPlatformTargetTransferFlow._noSIMOrNoEligibleSIMOnSource
- __OBJC_$_CATEGORY_UIViewController_$_Flow
- __OBJC_$_INSTANCE_METHODS_UIViewController(Flow|InModalPresentation|SubFlow|SimSetup|NavigationBar)
- __OBJC_$_PROP_LIST_UIViewController_$_Flow
- ___115-[TSCellularPlanActivatingFlow(CoreTelephonyClientCellularPlanManagementDelegate) handleWaitingOnWifiStatusUpdate:]_block_invoke.498
- ___62-[TSSIMSetupFlow navigateToNextPaneFrom:navigationController:]_block_invoke.181
- ___62-[TSSIMSetupFlow navigateToNextPaneFrom:navigationController:]_block_invoke.184
- ___74-[TSCellularPlanActivatingFlow(TSSIMSetupDelegate) simSetupFlowCompleted:]_block_invoke.544
- ___82-[TSCellularPlanActivatingFlow(InteractiveUI) _displayIntermediateViewController:]_block_invoke.606
- ___82-[TSCellularPlanActivatingFlow(TSSIMSetupFlowDelegate) viewControllerDidComplete:]_block_invoke.555
- ___82-[TSCellularPlanActivatingFlow(TSSIMSetupFlowDelegate) viewControllerDidComplete:]_block_invoke.555.cold.1
- ___block_literal_global.408
- ___block_literal_global.497
- ___block_literal_global.500
- ___block_literal_global.557
Functions:
~ -[TSCellularPlanActivatingFlow(Override) nextViewControllerFrom:] : 1672 -> 1940
~ -[TSCellularPlanActivatingFlow(UpdatePlanInfo) _updateInstallError:withPlanID:webUrl:postData:] : 224 -> 288
- -[UIViewController(Flow) flow]
~ -[TSTravelBuddyViewController initWithPlans:homeIccid:] : 952 -> 964
~ -[TSTravelBuddyViewController prepare:] : 472 -> 736
~ -[TSCrossPlatformTargetTransferFlow init] : 196 -> 184
~ ___57-[TSCrossPlatformTargetTransferFlow firstViewController:]_block_invoke : 612 -> 592
~ -[TSCrossPlatformTargetTransferFlow nextViewControllerFrom:] : 456 -> 412
~ -[TSCrossPlatformTargetTransferFlow transferEventUpdate:] : 1104 -> 1444
~ -[TSCrossPlatformTargetTransferFlow .cxx_destruct] : 144 -> 164
~ -[TSMidOperationFailureViewController initWithPlans:isCrossPlatformTransfer:] : 608 -> 676
~ -[TSMidOperationFailureViewController(TSSetupFlowItem) prepare:] : 144 -> 128
+ -[UIViewController(SimSetup) flow]
~ -[SSQRCodeIntroViewController viewDidLoad] : 456 -> 464
+ -[SSQRCodeIntroViewController _needOfferOtherOptions]
+ -[TSCellularPlanActivatingFlow(UpdatePlanInfo) _updatePlanStatus:withPlanID:].cold.1
CStrings:
+ "Home ICCID is empty @%s"
+ "Installation failed @%s"
+ "[E]Already received error for this plan. Ignoring error: %@ @%s"
+ "_didInstallationFail"
+ "_needOfferOtherOptions"
+ "_webView:willSubmitFormValues:frameInfo:sourceFrameInfo:userObject:submissionHandler:"
+ "kCrossTransferSourceUiShown"
+ "sourceUiShown=false, wait for end session to dismiss flow @%s"
+ "sourceUiShown=true, show first view controller of target transfer flow @%s"
+ "v64@0:8@\"WKWebView\"16@\"NSDictionary\"24@\"WKFrameInfo\"32@\"WKFrameInfo\"40@\"NSObject<NSSecureCoding>\"48@?<v@?>56"
+ "v64@0:8@16@24@32@40@48@?56"
- "Flow"
- "_noSIMOrNoEligibleSIMOnSource"

```
