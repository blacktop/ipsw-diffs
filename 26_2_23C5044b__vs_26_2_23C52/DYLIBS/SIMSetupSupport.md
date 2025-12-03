## SIMSetupSupport

> `/System/Library/PrivateFrameworks/SIMSetupSupport.framework/SIMSetupSupport`

```diff

-883.2.0.0.0
-  __TEXT.__text: 0xb96a4
+883.2.1.0.0
+  __TEXT.__text: 0xb94dc
   __TEXT.__auth_stubs: 0x840
   __TEXT.__objc_methlist: 0xa3b4
   __TEXT.__const: 0x1d0
   __TEXT.__gcc_except_tab: 0x1dc0
   __TEXT.__cstring: 0x10769
-  __TEXT.__oslogstring: 0x6bff
+  __TEXT.__oslogstring: 0x6bbf
   __TEXT.__dlopen_cstrs: 0x2be
   __TEXT.__ustring: 0xa
   __TEXT.__unwind_info: 0x2648

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F220B11A-4360-3DE2-B61A-4AED7C2C7094
-  Functions: 3973
-  Symbols:   14335
-  CStrings:  7577
+  UUID: 73C0437A-9244-3EAD-9F6F-2966D7EC0989
+  Functions: 3972
+  Symbols:   14333
+  CStrings:  7576
 
Symbols:
+ GCC_except_table226
+ ___115-[TSCellularPlanActivatingFlow(CoreTelephonyClientCellularPlanManagementDelegate) handleWaitingOnWifiStatusUpdate:]_block_invoke.501
+ ___74-[TSCellularPlanActivatingFlow(TSSIMSetupDelegate) simSetupFlowCompleted:]_block_invoke.547
+ ___82-[TSCellularPlanActivatingFlow(InteractiveUI) _displayIntermediateViewController:]_block_invoke.609
+ ___82-[TSCellularPlanActivatingFlow(TSSIMSetupFlowDelegate) viewControllerDidComplete:]_block_invoke.558
+ ___82-[TSCellularPlanActivatingFlow(TSSIMSetupFlowDelegate) viewControllerDidComplete:]_block_invoke.558.cold.1
+ ___block_literal_global.408
+ ___block_literal_global.500
+ ___block_literal_global.503
+ ___block_literal_global.560
- -[TSCellularPlanActivatingFlow(UpdatePlanInfo) _updateInstallError:withPlanID:webUrl:postData:].cold.2
- GCC_except_table227
- ___115-[TSCellularPlanActivatingFlow(CoreTelephonyClientCellularPlanManagementDelegate) handleWaitingOnWifiStatusUpdate:]_block_invoke.503
- ___74-[TSCellularPlanActivatingFlow(TSSIMSetupDelegate) simSetupFlowCompleted:]_block_invoke.549
- ___82-[TSCellularPlanActivatingFlow(InteractiveUI) _displayIntermediateViewController:]_block_invoke.611
- ___82-[TSCellularPlanActivatingFlow(TSSIMSetupFlowDelegate) viewControllerDidComplete:]_block_invoke.560
- ___82-[TSCellularPlanActivatingFlow(TSSIMSetupFlowDelegate) viewControllerDidComplete:]_block_invoke.560.cold.1
- ___block_literal_global.410
- ___block_literal_global.502
- ___block_literal_global.505
- ___block_literal_global.562
Functions:
~ -[TSCellularPlanActivatingFlow(Override) nextViewControllerFrom:] : 1940 -> 1672
~ -[TSCellularPlanActivatingFlow(UpdatePlanInfo) _updateInstallError:withPlanID:webUrl:postData:] : 288 -> 224
- -[TSCellularPlanActivatingFlow(UpdatePlanInfo) _updatePlanStatus:withPlanID:].cold.1
CStrings:
- "[E]Already received error for this plan. Ignoring error: %@ @%s"

```
