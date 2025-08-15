## AppleAccountUI

> `/System/Library/PrivateFrameworks/AppleAccountUI.framework/AppleAccountUI`

```diff

-494.19.0.0.0
-  __TEXT.__text: 0xc84dc
+494.20.0.0.0
+  __TEXT.__text: 0xc907c
   __TEXT.__auth_stubs: 0x1f80
-  __TEXT.__objc_methlist: 0x73cc
+  __TEXT.__objc_methlist: 0x741c
   __TEXT.__const: 0x17f4
   __TEXT.__gcc_except_tab: 0xf60
-  __TEXT.__cstring: 0x4b67
-  __TEXT.__oslogstring: 0x9b9e
+  __TEXT.__cstring: 0x4bc7
+  __TEXT.__oslogstring: 0x9d94
   __TEXT.__dlopen_cstrs: 0x3e1
   __TEXT.__ustring: 0x4
   __TEXT.__swift5_typeref: 0x2492

   __TEXT.__swift5_proto: 0x9c
   __TEXT.__swift5_types: 0xc0
   __TEXT.__swift5_builtin: 0x64
-  __TEXT.__unwind_info: 0x30fc
+  __TEXT.__unwind_info: 0x312c
   __TEXT.__eh_frame: 0x558
   __TEXT.__objc_classname: 0x1b88
-  __TEXT.__objc_methname: 0x171f2
-  __TEXT.__objc_methtype: 0x44b0
-  __TEXT.__objc_stubs: 0x11280
+  __TEXT.__objc_methname: 0x1727a
+  __TEXT.__objc_methtype: 0x44c1
+  __TEXT.__objc_stubs: 0x112e0
   __DATA_CONST.__got: 0x9c0
   __DATA_CONST.__const: 0x2610
   __DATA_CONST.__objc_classlist: 0x590

   __DATA_CONST.__objc_protolist: 0x228
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x29570
-  __DATA_CONST.__objc_selrefs: 0x53d0
+  __DATA_CONST.__objc_selrefs: 0x53f0
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_classrefs: 0xbd0
   __DATA_CONST.__objc_superrefs: 0x3c0
   __DATA_CONST.__objc_arraydata: 0xb8
   __AUTH_CONST.__objc_const: 0x3ca0
-  __AUTH_CONST.__cfstring: 0x4220
+  __AUTH_CONST.__cfstring: 0x4260
   __AUTH_CONST.__const: 0x21e8
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x60

   __AUTH.__data: 0x4a8
   __DATA.__objc_ivar: 0x9fc
   __DATA.__data: 0x23c8
-  __DATA.__bss: 0x1878
-  __DATA.__common: 0x310
+  __DATA.__bss: 0x1880
+  __DATA.__common: 0x328
   __DATA_DIRTY.__const: 0x18
   __DATA_DIRTY.__objc_data: 0x2d0
   __DATA_DIRTY.__bss: 0x38

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 432964D6-58D3-3ED1-BF08-526142933DA2
-  Functions: 4837
-  Symbols:   13255
-  CStrings:  6323
+  UUID: 9E74FCE8-4B09-3722-AED7-7B608F7048FB
+  Functions: 4853
+  Symbols:   13284
+  CStrings:  6342
 
Symbols:
+ +[AAUIFeatureFlags isLCInviteAcceptanceEnabled]
+ -[AAUIInheritanceSetupFlowController _startInviteMessageFlow].cold.1
+ -[AAUIInheritanceSetupFlowController _startInviteMessageFlow].cold.2
+ -[AAUIInheritanceSetupFlowController _startInviteMessageFlow].cold.3
+ -[AAUIInheritanceSetupFlowController _startInviteMessageFlow].cold.4
+ -[AAUIMyPendingBeneficiaryActionHandler _startInviteMessageFlow].cold.1
+ -[AAUIMyPendingBeneficiaryActionHandler _startInviteMessageFlow].cold.2
+ -[AAUIOBInheritanceInvitationViewModel initWithAcceptedViewForBenefactorInfo:]
+ -[AAUIOBInheritanceInvitationViewModel initWithBenefactorInfo:]
+ -[AAUIOBInheritanceInvitationViewModel initWithModel:]
+ -[AAUIOBInheritanceInviteMessageViewModel initWithType:recipientHandle:]
+ -[AAUIOBInheritanceSetupCompleteViewModel _setInheritanceInvitationImageIfNecessary]
+ -[AAUIOBInheritanceSetupCompleteViewModel initWithBeneficiaryName:accessKeyShareType:inviteType:]
+ ___55-[AAUIInheritanceSetupFlowController _setupBeneficiary]_block_invoke.92
+ ___55-[AAUIInheritanceSetupFlowController _setupBeneficiary]_block_invoke.93
+ ___58-[AAUIMyPendingBeneficiaryActionHandler _showPrintPreview]_block_invoke.40
+ _objc_msgSend$configurationAtKey:
+ _objc_msgSend$initWithBeneficiaryName:accessKeyShareType:inviteType:
+ _objc_msgSend$isLCInviteAcceptanceEnabled
- -[AAUIOBInheritanceInvitationViewModel initWithBenefactorName:handle:]
- ___55-[AAUIInheritanceSetupFlowController _setupBeneficiary]_block_invoke.87
- ___55-[AAUIInheritanceSetupFlowController _setupBeneficiary]_block_invoke.88
- ___58-[AAUIMyPendingBeneficiaryActionHandler _showPrintPreview]_block_invoke.39
CStrings:
+ "@40@0:8@16Q24Q32"
+ "AppleAccount"
+ "LCInvite: Initialing LC Invite Message view based on receiver isFamilyMember: %d"
+ "LCInvite: Initialing LC Invite Message view without checking if receiver isFamilyMember"
+ "LCInvite: Initialing LC setup complete view based on receiver isFamilyMember: %d"
+ "LCInvite: Initialing LC setup complete view without checking if receiver isFamilyMember"
+ "LCInvite: No IdMS feature flag found. is OS FeatureFlag Enabled %d"
+ "LCInvite: Returning LCInviteAcceptance from urlbag: %@"
+ "LCInvite: inheritanceCfgs from urlbag: %@"
+ "LCInviteAcceptance"
+ "accountBeneficiary"
+ "configurationAtKey:"
+ "inheritanceCfgs"
+ "initWithAcceptedViewForBenefactorInfo:"
+ "initWithBenefactorInfo:"
+ "initWithBeneficiaryName:accessKeyShareType:inviteType:"
+ "inviteAcceptance"
+ "isLCInviteAcceptanceEnabled"
- "initWithBenefactorName:handle:"

```
