## SIMSetupSupport

> `/System/Library/PrivateFrameworks/SIMSetupSupport.framework/SIMSetupSupport`

```diff

-883.1.0.0.0
-  __TEXT.__text: 0xb94d4
+883.2.0.0.0
+  __TEXT.__text: 0xb96a4
   __TEXT.__auth_stubs: 0x840
   __TEXT.__objc_methlist: 0xa3b4
   __TEXT.__const: 0x1d0
   __TEXT.__gcc_except_tab: 0x1dc0
   __TEXT.__cstring: 0x10769
-  __TEXT.__oslogstring: 0x6b9c
+  __TEXT.__oslogstring: 0x6bff
   __TEXT.__dlopen_cstrs: 0x2be
   __TEXT.__ustring: 0xa
   __TEXT.__unwind_info: 0x2648

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6F889063-62AF-330E-8D32-1E7ACBCF4F1D
+  UUID: F220B11A-4360-3DE2-B61A-4AED7C2C7094
   Functions: 3973
   Symbols:   14335
-  CStrings:  7575
+  CStrings:  7577
 
Symbols:
+ ___115-[TSCellularPlanActivatingFlow(CoreTelephonyClientCellularPlanManagementDelegate) handleWaitingOnWifiStatusUpdate:]_block_invoke.503
+ ___74-[TSCellularPlanActivatingFlow(TSSIMSetupDelegate) simSetupFlowCompleted:]_block_invoke.549
+ ___82-[TSCellularPlanActivatingFlow(InteractiveUI) _displayIntermediateViewController:]_block_invoke.611
+ ___82-[TSCellularPlanActivatingFlow(TSSIMSetupFlowDelegate) viewControllerDidComplete:]_block_invoke.560
+ ___82-[TSCellularPlanActivatingFlow(TSSIMSetupFlowDelegate) viewControllerDidComplete:]_block_invoke.560.cold.1
+ ___block_literal_global.505
+ ___block_literal_global.562
- ___115-[TSCellularPlanActivatingFlow(CoreTelephonyClientCellularPlanManagementDelegate) handleWaitingOnWifiStatusUpdate:]_block_invoke.500
- ___74-[TSCellularPlanActivatingFlow(TSSIMSetupDelegate) simSetupFlowCompleted:]_block_invoke.546
- ___82-[TSCellularPlanActivatingFlow(InteractiveUI) _displayIntermediateViewController:]_block_invoke.608
- ___82-[TSCellularPlanActivatingFlow(TSSIMSetupFlowDelegate) viewControllerDidComplete:]_block_invoke.557
- ___82-[TSCellularPlanActivatingFlow(TSSIMSetupFlowDelegate) viewControllerDidComplete:]_block_invoke.557.cold.1
- ___block_literal_global.499
- ___block_literal_global.559
Functions:
~ -[TSCellularPlanActivatingFlow(CoreTelephonyClientCellularPlanManagementDelegate) transferEventUpdate:] : 2408 -> 2660
~ -[TSCrossPlatformTargetTransferFlow transferEventUpdate:] : 1444 -> 1656
CStrings:
+ "Cross transfer session error, exit activation flow @%s"
+ "timeout, last event is %@, dismiss flow @%s"

```
