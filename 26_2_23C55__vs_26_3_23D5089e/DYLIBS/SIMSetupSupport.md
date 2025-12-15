## SIMSetupSupport

> `/System/Library/PrivateFrameworks/SIMSetupSupport.framework/SIMSetupSupport`

```diff

-883.2.1.0.0
-  __TEXT.__text: 0xb94dc
+883.5.0.0.0
+  __TEXT.__text: 0xb97bc
   __TEXT.__auth_stubs: 0x840
   __TEXT.__objc_methlist: 0xa3b4
   __TEXT.__const: 0x1d0
   __TEXT.__gcc_except_tab: 0x1dc0
   __TEXT.__cstring: 0x10769
-  __TEXT.__oslogstring: 0x6bbf
+  __TEXT.__oslogstring: 0x6c29
   __TEXT.__dlopen_cstrs: 0x2be
   __TEXT.__ustring: 0xa
   __TEXT.__unwind_info: 0x2648
   __TEXT.__objc_classname: 0x15de
   __TEXT.__objc_methname: 0x16f1d
-  __TEXT.__objc_methtype: 0x35f6
+  __TEXT.__objc_methtype: 0x35f7
   __TEXT.__objc_stubs: 0xe680
   __DATA_CONST.__got: 0xa78
   __DATA_CONST.__const: 0x1db0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 73C0437A-9244-3EAD-9F6F-2966D7EC0989
-  Functions: 3972
-  Symbols:   14333
-  CStrings:  7576
+  UUID: 57D6B94E-9873-3411-9968-7179A8065118
+  Functions: 3973
+  Symbols:   14335
+  CStrings:  7578
 
Symbols:
+ -[TSCellularPlanActivatingFlow(UpdatePlanInfo) _updateInstallError:withPlanID:webUrl:postData:].cold.2
+ GCC_except_table227
+ ___115-[TSCellularPlanActivatingFlow(CoreTelephonyClientCellularPlanManagementDelegate) handleWaitingOnWifiStatusUpdate:]_block_invoke.503
+ ___74-[TSCellularPlanActivatingFlow(TSSIMSetupDelegate) simSetupFlowCompleted:]_block_invoke.549
+ ___82-[TSCellularPlanActivatingFlow(InteractiveUI) _displayIntermediateViewController:]_block_invoke.611
+ ___82-[TSCellularPlanActivatingFlow(TSSIMSetupFlowDelegate) viewControllerDidComplete:]_block_invoke.560
+ ___82-[TSCellularPlanActivatingFlow(TSSIMSetupFlowDelegate) viewControllerDidComplete:]_block_invoke.560.cold.1
+ ___block_literal_global.410
+ ___block_literal_global.502
+ ___block_literal_global.505
+ ___block_literal_global.562
- GCC_except_table226
- ___115-[TSCellularPlanActivatingFlow(CoreTelephonyClientCellularPlanManagementDelegate) handleWaitingOnWifiStatusUpdate:]_block_invoke.501
- ___74-[TSCellularPlanActivatingFlow(TSSIMSetupDelegate) simSetupFlowCompleted:]_block_invoke.547
- ___82-[TSCellularPlanActivatingFlow(InteractiveUI) _displayIntermediateViewController:]_block_invoke.609
- ___82-[TSCellularPlanActivatingFlow(TSSIMSetupFlowDelegate) viewControllerDidComplete:]_block_invoke.558
- ___82-[TSCellularPlanActivatingFlow(TSSIMSetupFlowDelegate) viewControllerDidComplete:]_block_invoke.558.cold.1
- ___block_literal_global.408
- ___block_literal_global.500
- ___block_literal_global.503
- ___block_literal_global.560
Functions:
~ -[TSCellularPlanActivatingFlow(Override) nextViewControllerFrom:] : 1672 -> 1940
~ -[TSCellularPlanActivatingFlow(UpdatePlanInfo) _updateInstallError:withPlanID:webUrl:postData:] : 224 -> 288
~ -[TSCrossPlatformSourceTransferFlow launchSimSetupForTransferPlanSelection:completion:] : 584 -> 608
~ ___87-[TSCrossPlatformSourceTransferFlow launchSimSetupForTransferPlanSelection:completion:]_block_invoke : 692 -> 812
~ -[TSCrossPlatformSourceTransferFlow transferEventUpdate:] : 1836 -> 1972
+ -[TSCellularPlanActivatingFlow(UpdatePlanInfo) _updatePlanStatus:withPlanID:].cold.1
CStrings:
+ "[E]Already received error for this plan. Ignoring error: %@ @%s"
+ "received endSession and in buddy mode @%s"
+ "v32@0:8@\"NSArray\"16@?<v@?BBi>24"
- "v32@0:8@\"NSArray\"16@?<v@?Bi>24"

```
