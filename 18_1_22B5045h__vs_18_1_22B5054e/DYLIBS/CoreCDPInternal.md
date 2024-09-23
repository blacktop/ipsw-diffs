## CoreCDPInternal

> `/System/Library/PrivateFrameworks/CoreCDPInternal.framework/CoreCDPInternal`

```diff

-386.100.4.0.1
-  __TEXT.__text: 0x7aecc
-  __TEXT.__auth_stubs: 0x10c0
-  __TEXT.__objc_methlist: 0x3f60
+386.100.11.2.0
+  __TEXT.__text: 0x7c194
+  __TEXT.__auth_stubs: 0x10b0
+  __TEXT.__objc_methlist: 0x3fa8
   __TEXT.__const: 0x534
-  __TEXT.__oslogstring: 0x113fe
-  __TEXT.__cstring: 0x5eec
+  __TEXT.__oslogstring: 0x1157e
+  __TEXT.__cstring: 0x5f7c
   __TEXT.__gcc_except_tab: 0x8cc
   __TEXT.__dlopen_cstrs: 0xb0
   __TEXT.__swift5_typeref: 0x2e2

   __TEXT.__swift5_proto: 0x28
   __TEXT.__swift5_types: 0x14
   __TEXT.__swift5_capture: 0x1b8
-  __TEXT.__unwind_info: 0x1940
-  __TEXT.__eh_frame: 0x890
-  __TEXT.__objc_classname: 0xbe3
-  __TEXT.__objc_methname: 0xd7d1
+  __TEXT.__unwind_info: 0x1978
+  __TEXT.__eh_frame: 0x8d0
+  __TEXT.__objc_classname: 0xc02
+  __TEXT.__objc_methname: 0xd934
   __TEXT.__objc_methtype: 0x2513
-  __TEXT.__objc_stubs: 0xb000
-  __DATA_CONST.__got: 0xf00
-  __DATA_CONST.__const: 0x1ea0
+  __TEXT.__objc_stubs: 0xb120
+  __DATA_CONST.__got: 0xf20
+  __DATA_CONST.__const: 0x1f18
   __DATA_CONST.__objc_classlist: 0x268
   __DATA_CONST.__objc_catlist: 0x40
-  __DATA_CONST.__objc_protolist: 0x158
+  __DATA_CONST.__objc_protolist: 0x160
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3128
+  __DATA_CONST.__objc_selrefs: 0x3178
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x158
   __DATA_CONST.__objc_arraydata: 0x70
-  __AUTH_CONST.__auth_got: 0x870
-  __AUTH_CONST.__auth_ptr: 0x178
+  __AUTH_CONST.__auth_got: 0x868
+  __AUTH_CONST.__auth_ptr: 0x180
   __AUTH_CONST.__const: 0x898
   __AUTH_CONST.__cfstring: 0x41e0
-  __AUTH_CONST.__objc_const: 0x10838
+  __AUTH_CONST.__objc_const: 0x108e8
   __AUTH_CONST.__objc_intobj: 0x150
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH.__objc_data: 0x1088
-  __AUTH.__data: 0x88
+  __AUTH.__objc_data: 0xfb0
+  __AUTH.__data: 0x58
   __DATA.__objc_ivar: 0x38c
-  __DATA.__data: 0x1190
-  __DATA.__bss: 0x530
+  __DATA.__data: 0x11f0
+  __DATA.__bss: 0x520
   __DATA.__common: 0x18
-  __DATA_DIRTY.__objc_data: 0x848
-  __DATA_DIRTY.__data: 0x10
-  __DATA_DIRTY.__bss: 0x120
+  __DATA_DIRTY.__objc_data: 0x920
+  __DATA_DIRTY.__data: 0x58
+  __DATA_DIRTY.__bss: 0x130
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/CoreData.framework/CoreData

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 2653
-  Symbols:   3428
-  CStrings:  4253
+  Functions: 2671
+  Symbols:   3440
+  CStrings:  4273
 
Symbols:
+ _kCDPAnalyticsFetchCustodianRecoveryInfoEvent
+ _kCDPAnalyticsValidateRecoveryCodeEvent
+ _kCDPAnalyticsValidateCustodianRecoveryInfoEvent
+ _kCDPAnalyticsRecoveryCreateSessionEvent
CStrings:
+ "CDPDRPDExecutor: Eligible for Manatee RPD.... Resetting Manatee only..."
+ "CDPDRPDExecutor: RPD is not allowed."
+ "\"Gathered local secret from hard limits or local secret not required, continuing with reset. %!s(MISSING)\""
+ "CDPDCircleControlStatusChecker"
+ "_pcsKeysForServices:pcsController:completion:"
+ "_shouldRejoinCircle"
+ "oldPassword"
+ "CDPDRPDExecutor: Manatee RPD is not permitted..."
+ "UnsafeMutablePointer.moveInitialize with negative count"
+ "_forceManateeReset"
+ "initWithSbDeleter:ledger:circleControl:cdpContext:"
+ "setWalrusStatusEnabled:password:completion:"
+ "circleControl"
+ "setNewPassword:oldPassword:"
+ "isSubsetOfContextTypeRepair:"
+ "manateeRPDBlockingError"
+ "_continueRepairCloudDataProtectionStateWithCompletion:"
+ "_grabPCSKeysForServices:pcsController:"
+ "is2FAFAUser"
+ "Ledger: CLI asked for a force Manatee reset. Overriding all other checks."
+ "Ledger: CLI asked for a force reset. Overriding all other checks."
+ "Ledger: manateeRPDBlockingError - Finding first unsatisfied requirement in conditions: %!s(MISSING)"
+ "Account is iCDP Eligible? "
+ "CDPDRPDExecutor: _forceManateeReset was set. Allowing Manatee RPD..."
+ "_addEDPEscapeOfferIfNeededToValidator:nonCancelCompletion:"
- "resetter"
- "initWithSbDeleter:ledger:resetter:"
- "\"Gathered local secret from hard limits, continuing with reset. %!s(MISSING)\""
- "Ledger: appleAccountSetupTool asked for a force reset. Overriding all other checks."
- "setWalrusStatusEnabled:completion:"
- "setPassword:"
- "CDPDRPDExecutor: Performing RPD failed with error: %!@(MISSING)"

```
