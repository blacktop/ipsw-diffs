## PassKitCore

> `/System/Library/PrivateFrameworks/PassKitCore.framework/PassKitCore`

```diff

-1591.5.15.5.0
-  __TEXT.__text: 0x7bac70
-  __TEXT.__auth_stubs: 0x49e0
-  __TEXT.__objc_methlist: 0x6a0ec
-  __TEXT.__const: 0x22200
-  __TEXT.__cstring: 0x67698
-  __TEXT.__swift5_typeref: 0x532c
-  __TEXT.__swift5_capture: 0x37e4
-  __TEXT.__oslogstring: 0x33e6a
-  __TEXT.__constg_swiftt: 0x49f8
-  __TEXT.__swift5_fieldmd: 0x4e14
-  __TEXT.__swift5_reflstr: 0x3fcd
+1591.5.16.5.0
+  __TEXT.__text: 0x7be690
+  __TEXT.__auth_stubs: 0x49f0
+  __TEXT.__objc_methlist: 0x6a18c
+  __TEXT.__const: 0x22250
+  __TEXT.__cstring: 0x6797e
+  __TEXT.__swift5_typeref: 0x540a
+  __TEXT.__swift5_capture: 0x38fc
+  __TEXT.__oslogstring: 0x33f2a
+  __TEXT.__constg_swiftt: 0x4aa4
+  __TEXT.__swift5_fieldmd: 0x4e60
+  __TEXT.__swift5_reflstr: 0x403d
   __TEXT.__swift5_builtin: 0x398
   __TEXT.__swift5_assocty: 0x8d0
   __TEXT.__swift5_proto: 0xc10
-  __TEXT.__swift5_types: 0x4ec
+  __TEXT.__swift5_types: 0x4f0
   __TEXT.__swift_as_entry: 0x98
   __TEXT.__swift_as_ret: 0xa0
   __TEXT.__swift5_protos: 0x40
   __TEXT.__swift5_mpenum: 0xf0
   __TEXT.__swift5_types2: 0x4
-  __TEXT.__gcc_except_tab: 0x74bc
+  __TEXT.__gcc_except_tab: 0x7490
   __TEXT.__ustring: 0x1ed6
-  __TEXT.__unwind_info: 0x1b270
+  __TEXT.__unwind_info: 0x1b340
   __TEXT.__eh_frame: 0x5814
   __TEXT.__objc_classname: 0xf8e5
-  __TEXT.__objc_methname: 0xc7412
+  __TEXT.__objc_methname: 0xc74dd
   __TEXT.__objc_methtype: 0x16e7f
-  __TEXT.__objc_stubs: 0x57f00
-  __DATA_CONST.__got: 0x45a8
-  __DATA_CONST.__const: 0x200d0
-  __DATA_CONST.__objc_classlist: 0x3970
+  __TEXT.__objc_stubs: 0x57f80
+  __DATA_CONST.__got: 0x45a0
+  __DATA_CONST.__const: 0x20160
+  __DATA_CONST.__objc_classlist: 0x3978
   __DATA_CONST.__objc_catlist: 0x110
   __DATA_CONST.__objc_protolist: 0x598
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x22360
+  __DATA_CONST.__objc_selrefs: 0x22390
   __DATA_CONST.__objc_protorefs: 0x240
   __DATA_CONST.__objc_superrefs: 0x2d90
   __DATA_CONST.__objc_arraydata: 0x3068
-  __AUTH_CONST.__auth_got: 0x2500
-  __AUTH_CONST.__auth_ptr: 0xa78
-  __AUTH_CONST.__const: 0x1cbb8
-  __AUTH_CONST.__cfstring: 0x6dd00
-  __AUTH_CONST.__objc_const: 0xc1198
+  __AUTH_CONST.__auth_got: 0x2508
+  __AUTH_CONST.__auth_ptr: 0xab0
+  __AUTH_CONST.__const: 0x1ce68
+  __AUTH_CONST.__cfstring: 0x6dea0
+  __AUTH_CONST.__objc_const: 0xc1308
   __AUTH_CONST.__objc_arrayobj: 0xab0
   __AUTH_CONST.__objc_intobj: 0x1170
   __AUTH_CONST.__objc_dictobj: 0x1db0
   __AUTH_CONST.__objc_doubleobj: 0x2b0
-  __AUTH.__objc_data: 0x1f560
-  __AUTH.__data: 0x3350
+  __AUTH.__objc_data: 0x1f588
+  __AUTH.__data: 0x3578
   __AUTH.__thread_vars: 0x18
   __AUTH.__thread_bss: 0x8
   __DATA.__objc_ivar: 0x6488
-  __DATA.__data: 0x8610
+  __DATA.__data: 0x8600
   __DATA.__bss: 0x172d8
   __DATA.__common: 0x220
   __DATA_DIRTY.__objc_ivar: 0x2550

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 48753
-  Symbols:   51462
-  CStrings:  52041
+  Functions: 48857
+  Symbols:   51511
+  CStrings:  52072
 
Symbols:
+ _PKAnalyticsReportViewPasscodeUpgradeCurrentPasscodeTag
+ _PKAnalyticsReportViewPasscodeUpgradeExplanationTag
+ _PKAnalyticsReportViewPasscodeUpgradeNewPasscodeTag
+ _PKPassSharingCarKeyBundleGroupIdentifierKey
+ _PKPassSharingCarKeyBundleIsCurrentUserKey
+ _PKPassSharingCarKeyBundleKeyDataKey
+ _PKPaymentNetworkHimyan
+ _PKPaymentNetworkJaywan
+ _PKUsePasscodeUpgradeFlow
+ _PKUsePasscodeUpgradeFlowKey
CStrings:
+ "Himyan"
+ "Jaywan"
+ "NETWORK_NAME_HIMYAN"
+ "NETWORK_NAME_HIMYAN_CARD_NAME"
+ "NETWORK_NAME_JAYWAN"
+ "NETWORK_NAME_JAYWAN_CARD_NAME"
+ "PKUsePasscodeUpgradeFlowKey"
+ "SetupAssistantRequirementsChecker: Skipping because requirements are not met: %s"
+ "T@?,N,C"
+ "[%s] Failed to acquire strong passcode assertion with error: %s"
+ "[%s] Failed to create recoverable checkpoint archive"
+ "[%s] Failed to enforce strong passcode policy because passcode not strong"
+ "_TtC11PassKitCore35ProvisioningStrongPasscodeAssertion"
+ "createDivergentStateClaimNonce:"
+ "defaultButtonTitle"
+ "enforceUpgradedPasscodePolicy failed with error: "
+ "hasVisibleEditableFields"
+ "isPasscodeStrong"
+ "notePasscodeUpgradeFlowWillBegin failed with error: "
+ "notePasscodeUpgradeFlowWillBegin not implemented on target device"
+ "onRecoverableCheckpointReached"
+ "otherButtonTitle"
+ "passcodeAssertion"
+ "passcodeUpgradeCurrentPasscode"
+ "passcodeUpgradeExplanation"
+ "passcodeUpgradeNewPasscode"
+ "refreshMerchantTokenMetadataWithCompletion:"
+ "revokeMerchantTokenWithIdentifier:completion:"
+ "setOnRecoverableCheckpointReached:"
+ "startRequiringUpgradedPasscode failed with error: "
+ "startRequiringUpgradedPasscodeWithCompletion:"
+ "v16@?0@\"PKSecureElementProvisioningState\"8"
- "[%s] Failed to enforceUpgradedPasscodePolicy with error: %s"
- "[%s] Failed to notePasscodeUpgradeFlowWillBegin"
- "_startRequiringUpgradedPasscodeWithPasscodeMeetsPolicy:"
- "didUpgradeToStrongPasscode"

```
