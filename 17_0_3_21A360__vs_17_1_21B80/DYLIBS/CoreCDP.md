## CoreCDP

> `/System/Library/PrivateFrameworks/CoreCDP.framework/CoreCDP`

```diff

-353.1.1.4.0
-  __TEXT.__text: 0x300a8
+359.2.0.0.0
+  __TEXT.__text: 0x30928
   __TEXT.__auth_stubs: 0x990
-  __TEXT.__objc_methlist: 0x271c
+  __TEXT.__objc_methlist: 0x275c
   __TEXT.__const: 0xe0
-  __TEXT.__gcc_except_tab: 0xdd8
-  __TEXT.__oslogstring: 0x7130
-  __TEXT.__cstring: 0x263f
+  __TEXT.__gcc_except_tab: 0xe28
+  __TEXT.__oslogstring: 0x7237
+  __TEXT.__cstring: 0x273b
   __TEXT.__dlopen_cstrs: 0x68
-  __TEXT.__unwind_info: 0xd68
-  __TEXT.__objc_classname: 0x6a7
-  __TEXT.__objc_methname: 0x733f
-  __TEXT.__objc_methtype: 0x17f2
-  __TEXT.__objc_stubs: 0x41c0
+  __TEXT.__unwind_info: 0xd94
+  __TEXT.__objc_classname: 0x6b4
+  __TEXT.__objc_methname: 0x7459
+  __TEXT.__objc_methtype: 0x184d
+  __TEXT.__objc_stubs: 0x4220
   __DATA_CONST.__got: 0x188
-  __DATA_CONST.__const: 0x1210
+  __DATA_CONST.__const: 0x1288
   __DATA_CONST.__objc_classlist: 0x190
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x7588
-  __DATA_CONST.__objc_selrefs: 0x1a88
+  __DATA_CONST.__objc_const: 0x75f8
+  __DATA_CONST.__objc_selrefs: 0x1ac8
   __DATA_CONST.__objc_arraydata: 0x90
   __AUTH_CONST.__objc_const: 0x14f0
-  __AUTH_CONST.__cfstring: 0x28c0
+  __AUTH_CONST.__cfstring: 0x2960
   __AUTH_CONST.__const: 0x380
+  __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__auth_got: 0x4d8
   __AUTH.__objc_data: 0x780
   __AUTH.__data: 0x8

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1415
-  Symbols:   4733
-  CStrings:  2324
+  Functions: 1428
+  Symbols:   4771
+  CStrings:  2351
 
Symbols:
+ +[CDPUtilities isKeyboardOOPEnabled]
+ +[CDPUtilities isKeyboardOOPiPadEnabled]
+ -[CDPAccount(CircleStatus) octagonStatusForContext:withCompletion:]
+ -[CDPAccount(CircleStatus) sosStatusForContext:withCompletion:]
+ -[CDPAccount(Probation) rpdProbationIsInEffectForDuration:context:]
+ -[CDPAccount(Probation) rpdProbationIsInEffectForDuration:context:].cold.1
+ -[CDPAccount(Probation) rpdProbationIsInEffectForDuration:context:].cold.2
+ -[CDPAccountRepresentation isSilentEscrowRecordRepairEnabledV2]
+ GCC_except_table32
+ GCC_except_table35
+ __OBJC_$_CLASS_METHODS_CDPAccount(MultiUserManatee|CircleStatus|Probation)
+ __OBJC_$_INSTANCE_METHODS_CDPAccount(MultiUserManatee|CircleStatus|Probation)
+ ___63-[CDPAccount(CircleStatus) sosStatusForContext:withCompletion:]_block_invoke
+ ___63-[CDPAccount(CircleStatus) sosStatusForContext:withCompletion:]_block_invoke_2
+ ___63-[CDPAccount(CircleStatus) sosStatusForContext:withCompletion:]_block_invoke_2.cold.1
+ ___67-[CDPAccount(CircleStatus) octagonStatusForContext:withCompletion:]_block_invoke
+ ___67-[CDPAccount(CircleStatus) octagonStatusForContext:withCompletion:]_block_invoke_2
+ ___67-[CDPAccount(CircleStatus) octagonStatusForContext:withCompletion:]_block_invoke_2.cold.1
+ ___block_descriptor_40_e8_32bs_e20_v20?0i8"NSError"12ls32l8
+ ___block_descriptor_40_e8_32bs_e20_v24?0q8"NSError"16ls32l8
+ ___block_literal_global.29
+ _kCDPAnalyticsEscrowRecordFetchSource
+ _kCDPAnalyticsFetchEscrowRecordsEvent
+ _kCDPAnalyticsRPDProbationEvent
+ _kCDPAnalyticsRemainingProbationTime
+ _kCDPAnalyticsWaitForPriorityViewKeychainDataRecovery
+ _objc_msgSend$circleStatusForContext:completion:
+ _objc_msgSend$cliqueStatusForContext:completion:
+ _objc_msgSend$isSilentEscrowRecordRepairEnabledForAccountV2:
+ _objc_msgSend$isSilentEscrowRecordRepairEnabledV2
- -[CDPAccount(Probation) rpdProbationIsInEffectForDuration:]
- -[CDPAccount(Probation) rpdProbationIsInEffectForDuration:].cold.1
- -[CDPAccount(Probation) rpdProbationIsInEffectForDuration:].cold.2
- GCC_except_table20
- __OBJC_$_CLASS_METHODS_CDPAccount(MultiUserManatee|Probation)
- __OBJC_$_INSTANCE_METHODS_CDPAccount(MultiUserManatee|Probation)
- _objc_msgSend$isSilentEscrowRecordRepairEnabled
CStrings:
+ "\"%@: Assuming silent escrow record repair V2 is disabled\""
+ "\"%@: Returning %@ for 'isSilentEscrowRecordRepairEnabledV2'\""
+ "\"Error while checking circle status: %@\""
+ "\"Error while checking clique status: %@\""
+ "B32@0:8d16@24"
+ "UIKit"
+ "Vv32@0:8@\"CDPContext\"16@?<v@?i@\"NSError\">24"
+ "Vv32@0:8@\"CDPContext\"16@?<v@?q@\"NSError\">24"
+ "cdp/statemachine-circle-status"
+ "cdp/statemachine-clique-status"
+ "circleStatusForContext:completion:"
+ "cliqueStatusForContext:completion:"
+ "com.apple.corecdp.fetchEscrowRecords"
+ "com.apple.corecdp.rpdProbation"
+ "com.apple.corecdp.waitForPriorityViewKeychainDataRecovery"
+ "escrowRecordFetchSource"
+ "isKeyboardOOPEnabled"
+ "isKeyboardOOPiPadEnabled"
+ "isSilentEscrowRecordRepairEnabledForAccountV2:"
+ "isSilentEscrowRecordRepairEnabledV2"
+ "keyboard_oop"
+ "keyboard_oop_ipad"
+ "octagonStatusForContext:withCompletion:"
+ "remainingProbationTime"
+ "rpdProbationIsInEffectForDuration:context:"
+ "sosStatusForContext:withCompletion:"
+ "v20@?0i8@\"NSError\"12"
+ "v24@?0q8@\"NSError\"16"
- "B24@0:8d16"
- "rpdProbationIsInEffectForDuration:"

```
