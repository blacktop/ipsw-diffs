## SIMSetupSupport

> `/System/Library/PrivateFrameworks/SIMSetupSupport.framework/SIMSetupSupport`

```diff

-883.5.0.0.0
-  __TEXT.__text: 0xb97bc
+883.7.0.0.0
+  __TEXT.__text: 0xb9858
   __TEXT.__auth_stubs: 0x840
   __TEXT.__objc_methlist: 0xa3b4
   __TEXT.__const: 0x1d0
   __TEXT.__gcc_except_tab: 0x1dc0
-  __TEXT.__cstring: 0x10769
-  __TEXT.__oslogstring: 0x6c29
+  __TEXT.__cstring: 0x107a6
+  __TEXT.__oslogstring: 0x6c1f
   __TEXT.__dlopen_cstrs: 0x2be
   __TEXT.__ustring: 0xa
-  __TEXT.__unwind_info: 0x2648
+  __TEXT.__unwind_info: 0x2640
   __TEXT.__objc_classname: 0x15de
   __TEXT.__objc_methname: 0x16f1d
   __TEXT.__objc_methtype: 0x35f7

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 57D6B94E-9873-3411-9968-7179A8065118
+  UUID: 766EB3CD-0698-3FE9-AF40-9892D7406728
   Functions: 3973
   Symbols:   14335
-  CStrings:  7578
+  CStrings:  7579
 
Functions:
~ -[TSCellularPlanActivatingFlow(CoreTelephonyClientCellularPlanManagementDelegate) transferEventUpdate:] : 2660 -> 2564
~ -[CrossPlatformTransferAuthQRCodeViewController init] : 288 -> 304
~ -[TSCrossPlatformTargetTransferFlow nextViewControllerFrom:] : 412 -> 516
~ ___66-[TSCrossPlatformTargetTransferFlow _showCancelAlert:withMessage:]_block_invoke : 72 -> 124
~ -[TSCrossPlatformTargetTransferFlow transferEventUpdate:] : 1656 -> 1736
CStrings:
+ "-[TSCrossPlatformTargetTransferFlow nextViewControllerFrom:]"
+ "TSCrossPlatformTargetTransferFlow is done, reset client @%s"
+ "topview is SSCrossPlatformTransferSourceSelectionViewController and source received end session(skip or carrier lock on target case), exit flow @%s"
- "Cross transfer session error, exit activation flow @%s"
- "Data+eSIM case,topview is SSCrossPlatformTransferSourceSelectionViewController and source received end session(skip or carrier lock on target case), exit flow @%s"

```
