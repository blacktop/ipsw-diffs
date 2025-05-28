## PassKitCore

> `/System/Library/PrivateFrameworks/PassKitCore.framework/PassKitCore`

```diff

-1552.6.11.0.0
-  __TEXT.__text: 0x5f07e4
+1552.7.5.1.0
+  __TEXT.__text: 0x5f1a2c
   __TEXT.__auth_stubs: 0x3a40
-  __TEXT.__objc_methlist: 0x58370
-  __TEXT.__const: 0x64f0
-  __TEXT.__cstring: 0x5ac62
+  __TEXT.__objc_methlist: 0x58400
+  __TEXT.__const: 0x6540
+  __TEXT.__cstring: 0x5ad74
   __TEXT.__constg_swiftt: 0x1720
   __TEXT.__swift5_typeref: 0x1bd6
   __TEXT.__swift5_builtin: 0x154

   __TEXT.__swift5_protos: 0xc
   __TEXT.__gcc_except_tab: 0x5214
   __TEXT.__oslogstring: 0x29f0e
-  __TEXT.__ustring: 0x1c5c
-  __TEXT.__unwind_info: 0x15bc4
+  __TEXT.__ustring: 0x1cc2
+  __TEXT.__unwind_info: 0x15be0
   __TEXT.__eh_frame: 0x1078
-  __TEXT.__objc_classname: 0xd6e2
-  __TEXT.__objc_methname: 0xb1dde
+  __TEXT.__objc_classname: 0xd6e3
+  __TEXT.__objc_methname: 0xb1f64
   __TEXT.__objc_methtype: 0x1474e
-  __TEXT.__objc_stubs: 0x4fbc0
+  __TEXT.__objc_stubs: 0x4fcc0
   __DATA_CONST.__got: 0xdc0
-  __DATA_CONST.__const: 0x1b7e8
+  __DATA_CONST.__const: 0x1b840
   __DATA_CONST.__objc_classlist: 0x3198
   __DATA_CONST.__objc_catlist: 0x118
   __DATA_CONST.__objc_protolist: 0x4a0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x89bd8
-  __DATA_CONST.__objc_selrefs: 0x1e8b8
+  __DATA_CONST.__objc_const: 0x89ca0
+  __DATA_CONST.__objc_selrefs: 0x1e918
   __DATA_CONST.__objc_protorefs: 0x198
   __DATA_CONST.__objc_classrefs: 0x2eb8
   __DATA_CONST.__objc_superrefs: 0x2740

   __AUTH_CONST.__const: 0xa6d0
   __AUTH_CONST.__auth_ptr: 0xb8
   __AUTH_CONST.__objc_const: 0x2a7d0
-  __AUTH_CONST.__cfstring: 0x61240
+  __AUTH_CONST.__cfstring: 0x613c0
   __AUTH_CONST.__objc_arrayobj: 0xa08
   __AUTH_CONST.__objc_intobj: 0xfc0
   __AUTH_CONST.__objc_dictobj: 0x1db0

   __AUTH_CONST.__auth_got: 0x1d30
   __AUTH.__objc_data: 0x1a748
   __AUTH.__data: 0x15f0
-  __DATA.__objc_ivar: 0x5a00
+  __DATA.__objc_ivar: 0x5a10
   __DATA.__data: 0x5290
   __DATA.__thread_vars: 0x18
   __DATA.__thread_bss: 0x8

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 39554
-  Symbols:   110328
-  CStrings:  46091
+  Functions: 39571
+  Symbols:   110374
+  CStrings:  46118
 
Symbols:
+ -[PKAccountUser hasHandle:]
+ -[PKAppleAccountInformation ageCategory]
+ -[PKAppleAccountInformation setAgeCategory:]
+ -[PKFamilyMember hasAppleIDAlias:]
+ -[PKGroup associatedAccountForPassAtIndex:]
+ -[PKGroup associatedAccountForPassUniqueID:]
+ -[PKGroup initWithCatalogGroup:passes:states:accounts:]
+ -[PKGroup updateAssociatedAccount:]
+ -[PKGroupsController _updateStateWithCatalog:passes:states:annotations:accounts:notify:]
+ -[PKGroupsController accountAdded:]
+ -[PKGroupsController accountChanged:]
+ -[PKGroupsController accountRemoved:]
+ -[PKGroupsControllerSnapshot accounts]
+ -[PKGroupsControllerSnapshot initWithPasses:annotationsByPassUniqueID:accounts:catalog:]
+ -[PKGroupsControllerSnapshot initWithPasses:states:annotations:accounts:catalog:]
+ -[PKPaymentWebServiceTargetDevice plansForPaymentPassWithUniqueIdentifier:completion:]
+ -[PKSecureElement ownershipStateForCurrentUser]
+ GCC_except_table97
+ _OBJC_IVAR_$_PKAppleAccountInformation._ageCategory
+ _OBJC_IVAR_$_PKGroup._accounts
+ _OBJC_IVAR_$_PKGroupsController._accountService
+ _OBJC_IVAR_$_PKGroupsControllerSnapshot._accounts
+ _PDDatabaseManagerHasPerformedContactlessActivationGroupingTypeRepair
+ _PDSetDatabaseManagerHasPerformedContactlessActivationGroupingTypeRepair
+ _PKTransitStationCodeProviderNavigo
+ ___55-[PKGroup initWithCatalogGroup:passes:states:accounts:]_block_invoke
+ ___76-[PKPaymentWebServiceRemoteProxyTargetDevice initWithWebService:connection:]_block_invoke.529
+ ___85-[PKGroup updateWithCatalogGroup:passes:states:accounts:expiredSectionPasses:notify:]_block_invoke
+ ___86-[PKGroupsController _updateAndCreateGroupsWithCatalog:passes:states:accounts:notify:]_block_invoke
+ ___Block_byref_object_copy_.521
+ ___Block_byref_object_dispose_.522
+ ___block_descriptor_40_e8_32s_e19_B16?0"PKAccount"8ls32l8
+ _objc_msgSend$aa_ageCategory
+ _objc_msgSend$associatedAccountForPassUniqueID:
+ _objc_msgSend$group:didInsertAssociatedAccount:forPass:
+ _objc_msgSend$group:didRemoveAssociatedAccountForPass:
+ _objc_msgSend$group:didUpdateAssociatedAccount:forPass:
+ _objc_msgSend$initWithPasses:states:annotations:accounts:catalog:
+ _objc_msgSend$managedBySP
+ _objc_msgSend$ownershipStateForCurrentUser
+ _objc_msgSend$setAgeCategory:
- -[PKGroup initWithCatalogGroup:passes:states:]
- -[PKGroupsController _updateStateWithCatalog:passes:states:annotations:notify:]
- -[PKGroupsControllerSnapshot initWithPasses:annotationsByPassUniqueID:catalog:]
- -[PKGroupsControllerSnapshot initWithPasses:states:annotations:catalog:]
- GCC_except_table218
- ___76-[PKPaymentWebServiceRemoteProxyTargetDevice initWithWebService:connection:]_block_invoke.528
- ___77-[PKGroupsController _updateAndCreateGroupsWithCatalog:passes:states:notify:]_block_invoke
- ___Block_byref_object_copy_.520
- ___Block_byref_object_dispose_.521
- _objc_msgSend$initWithPasses:states:annotations:catalog:
CStrings:
+ "\x02&\x14\x11\x12"
+ "\x19\x11"
+ "B16@?0@\"PKAccount\"8"
+ "PDDatabaseManagerHasPerformedContactlessActivationGroupingTypeRepairKey"
+ "T@\"NSSet\",R,C,N,V_accounts"
+ "Tq,N,V_ageCategory"
+ "_ageCategory"
+ "aa_ageCategory"
+ "accountLockedBankruptcy"
+ "ageCategory"
+ "associatedAccountForPassAtIndex:"
+ "associatedAccountForPassUniqueID:"
+ "bankruptcy"
+ "com.apple.transit.navigo"
+ "creditAccount"
+ "group:didInsertAssociatedAccount:forPass:"
+ "group:didRemoveAssociatedAccountForPass:"
+ "group:didUpdateAssociatedAccount:forPass:"
+ "hasAppleIDAlias:"
+ "hasHandle:"
+ "initWithPasses:annotationsByPassUniqueID:accounts:catalog:"
+ "initWithPasses:states:annotations:accounts:catalog:"
+ "managedAppleAccount"
+ "managedBySP"
+ "ownershipStateForCurrentUser"
+ "setAgeCategory:"
+ "under13"
+ "under18"
+ "wallet::loan::lockedbankruptcy"
+ "wallet_loan_lockedbankruptcy"
- "\x02&\x14\""
- "initWithPasses:annotationsByPassUniqueID:catalog:"
- "initWithPasses:states:annotations:catalog:"
- "\xf0A"

```
