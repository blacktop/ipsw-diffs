## passd

> `/System/Library/PrivateFrameworks/PassKitCore.framework/passd`

```diff

-1591.2.3.1.0
-  __TEXT.__text: 0x509244
+1591.2.5.1.0
+  __TEXT.__text: 0x509d54
   __TEXT.__auth_stubs: 0x5090
-  __TEXT.__objc_stubs: 0x69800
-  __TEXT.__objc_methlist: 0x2b9b4
+  __TEXT.__objc_stubs: 0x69880
+  __TEXT.__objc_methlist: 0x2b964
   __TEXT.__const: 0x185a
-  __TEXT.__cstring: 0x58fab
-  __TEXT.__objc_classname: 0x6888
-  __TEXT.__objc_methtype: 0x120b4
-  __TEXT.__gcc_except_tab: 0x9488
-  __TEXT.__objc_methname: 0x943d8
-  __TEXT.__oslogstring: 0x4bd1d
+  __TEXT.__cstring: 0x5900b
+  __TEXT.__objc_classname: 0x6889
+  __TEXT.__objc_methtype: 0x120d8
+  __TEXT.__gcc_except_tab: 0x94a0
+  __TEXT.__objc_methname: 0x944bb
+  __TEXT.__oslogstring: 0x4bf9d
   __TEXT.__ustring: 0x14
   __TEXT.__swift5_typeref: 0x103a
   __TEXT.__constg_swiftt: 0xa8c

   __TEXT.__swift5_types: 0x98
   __TEXT.__swift5_capture: 0xab8
   __TEXT.__swift5_protos: 0xc
-  __TEXT.__unwind_info: 0x114f0
+  __TEXT.__unwind_info: 0x11508
   __TEXT.__eh_frame: 0xdfc
   __DATA_CONST.__auth_got: 0x2858
   __DATA_CONST.__got: 0x3258
   __DATA_CONST.__auth_ptr: 0x2f8
-  __DATA_CONST.__const: 0x2ae98
-  __DATA_CONST.__cfstring: 0x2e620
+  __DATA_CONST.__const: 0x2af60
+  __DATA_CONST.__cfstring: 0x2e6a0
   __DATA_CONST.__objc_classlist: 0x16d0
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x558

   __DATA_CONST.__objc_arrayobj: 0x4f8
   __DATA_CONST.__objc_dictobj: 0x280
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA.__objc_const: 0x44eb0
-  __DATA.__objc_selrefs: 0x1cbf8
-  __DATA.__objc_ivar: 0x256c
+  __DATA.__objc_const: 0x44ef0
+  __DATA.__objc_selrefs: 0x1cc18
+  __DATA.__objc_ivar: 0x2574
   __DATA.__objc_data: 0xeea8
   __DATA.__data: 0x49a0
-  __DATA.__bss: 0x1280
+  __DATA.__bss: 0x12a0
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/ActivityKit.framework/ActivityKit

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 24146
+  Functions: 24159
   Symbols:   3014
-  CStrings:  32344
+  CStrings:  32362
 
CStrings:
+ "PDAssertionManager: releasing transitive field detect suppression assertion %!p(MISSING)."
+ "q BOOL"
+ "didProvisionPassWithPrimaryAccountIdentifier:completion:"
+ "setShowSettingsBalance:"
+ "showCreditRewardsHubBalance"
+ "r BOOL"
+ "showSettingsBalance"
+ "PDNotificationServiceCoordinator: Related pass could not be found for balance: %!@(MISSING)"
+ "@\"FKBankConnectPassUpdateProcessor\""
+ "_fieldDetectSuppressionAssertion"
+ "setShowCreditDashboardBalance:"
+ "didDeletePassWithPrimaryAccountIdentifier:completion:"
+ "Migrating database from user_version 17062 to 17063"
+ "setHideCreditRewardsHubSignage:"
+ "CREATE TABLE IF NOT EXISTS rhubarb (pid INTEGER, a INTEGER, b TEXT, c INTEGER, d INTEGER, e TEXT, f TEXT, g INTEGER, h INTEGER, i INTEGER, j TEXT, k TEXT, l TEXT, m INTEGER, n BOOL, q BOOL, r BOOL, s BOOL, PRIMARY KEY (pid));"
+ "PDAssertionManager: failed to acquire transitive field detect suppression assertion - %!@(MISSING)."
+ "PDDatabaseManager: Processed pass insertion with FKBankConnectPassUpdateProcessor for primaryAccountIdentifier %!@(MISSING)"
+ "PDDatabaseManager: Processed pass deletion with FKBankConnectPassUpdateProcessor for primaryAccountIdentifier %!@(MISSING)"
+ "\x02\x15\x11"
+ "PDNotificationServiceCoordinator: Too many balances provided for pass %!@(MISSING), skipping: %!@(MISSING)"
+ "setShowCreditRewardsHubBalance:"
+ "PDAssertionManager: acquired transitive field detect suppression assertion %!p(MISSING)."
+ "hideCreditRewardsHubSignage"
+ "n BOOL"
+ "FKBankConnectPassUpdateProcessor"
+ "_migrateFrom17062To17063:context:"
+ "showCreditDashboardBalance"
+ "\x051\x11"
+ "s BOOL"
+ "makeProcessor"
+ "b\x11\x12"
+ "_bankConnectPassUpdateProcessor"
+ "PDNotificationServiceCoordinator: Plan's related pass could not be found"
- "invalidateAssertionCoordinator:"
- "R\x11\x12"
- "_addAssertionCoordinator:"
- "_removeAllAssertionCoordinators"
- "Plan's related pass could not be found"
- "\x02\x15"
- "CREATE TABLE IF NOT EXISTS rhubarb (pid INTEGER, a INTEGER, b TEXT, c INTEGER, d INTEGER, e TEXT, f TEXT, g INTEGER, h INTEGER, i INTEGER, j TEXT, k TEXT, l TEXT, m INTEGER, PRIMARY KEY (pid));"
- "\x041\x11"
- "Too many balances provided for pass, skipping"
- "_process:didChangeState:"
- "Balance's related pass could not be found"
- "_removeAssertionCoordinator:"
- "removeAssertionCoordinator:"
- "addAssertionCoordinator:"
- "_updateProcessMonitor"

```
