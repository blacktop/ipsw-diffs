## AppleAccount

> `/System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount`

```diff

-1007.475.0.0.0
-  __TEXT.__text: 0xccaa8
-  __TEXT.__auth_stubs: 0xb70
-  __TEXT.__objc_methlist: 0x9ff8
+1007.476.0.0.0
+  __TEXT.__text: 0xcd068
+  __TEXT.__auth_stubs: 0xb80
+  __TEXT.__objc_methlist: 0xa058
   __TEXT.__const: 0x19f0
-  __TEXT.__cstring: 0xd89f
-  __TEXT.__oslogstring: 0xe4c1
+  __TEXT.__cstring: 0xdaef
+  __TEXT.__oslogstring: 0xe4da
   __TEXT.__gcc_except_tab: 0x21f0
   __TEXT.__dlopen_cstrs: 0x2d9
-  __TEXT.__unwind_info: 0x28a8
+  __TEXT.__unwind_info: 0x28c0
   __TEXT.__objc_classname: 0x1d0a
-  __TEXT.__objc_methname: 0x13e2e
-  __TEXT.__objc_methtype: 0x2c86
-  __TEXT.__objc_stubs: 0xb5a0
-  __DATA_CONST.__got: 0xc50
-  __DATA_CONST.__const: 0x36f0
+  __TEXT.__objc_methname: 0x13f7c
+  __TEXT.__objc_methtype: 0x2ca2
+  __TEXT.__objc_stubs: 0xb700
+  __DATA_CONST.__got: 0xc58
+  __DATA_CONST.__const: 0x3700
   __DATA_CONST.__objc_classlist: 0x748
   __DATA_CONST.__objc_catlist: 0x98
   __DATA_CONST.__objc_protolist: 0x180
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x48e8
+  __DATA_CONST.__objc_selrefs: 0x4950
   __DATA_CONST.__objc_protorefs: 0x40
   __DATA_CONST.__objc_superrefs: 0x520
   __DATA_CONST.__objc_arraydata: 0xc0
-  __AUTH_CONST.__auth_got: 0x5c8
+  __AUTH_CONST.__auth_got: 0x5d0
   __AUTH_CONST.__auth_ptr: 0x10
   __AUTH_CONST.__const: 0x5ba0
-  __AUTH_CONST.__cfstring: 0xc000
-  __AUTH_CONST.__objc_const: 0x20e88
+  __AUTH_CONST.__cfstring: 0xc0a0
+  __AUTH_CONST.__objc_const: 0x20ec8
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__objc_intobj: 0xf0
+  __AUTH_CONST.__objc_intobj: 0x108
   __AUTH_CONST.__objc_arrayobj: 0xd8
   __AUTH.__objc_data: 0x340
   __AUTH.__data: 0x28
-  __DATA.__objc_ivar: 0xaf8
+  __DATA.__objc_ivar: 0xafc
   __DATA.__data: 0x1440
   __DATA.__bss: 0x378
   __DATA.__common: 0x6c

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 4235
-  Symbols:   14883
-  CStrings:  6778
+  Functions: 4247
+  Symbols:   14919
+  CStrings:  6800
 
Symbols:
+ +[AAFollowUpUtilities followUpPostAnalyticsInfoWithContext:identifier:error:]
+ -[AACustodianshipInfo description]
+ -[AAFollowUpController .cxx_destruct]
+ -[AAFollowUpController analyticsInfo]
+ -[AAFollowUpController setAnalyticsInfo:]
+ -[AAFollowUpController(Convenience) reportPostCFUEvent]
+ -[AAFollowUpController(Convenience) reportPostCFUEvent].cold.1
+ -[AALocalContactInfo description]
+ -[AATrustedContact description]
+ GCC_except_table69
+ GCC_except_table82
+ _OBJC_CLASS_$_AAAFollowUpAnalyticsInfo
+ _OBJC_IVAR_$_AAFollowUpController._analyticsInfo
+ __OBJC_$_INSTANCE_VARIABLES_AAFollowUpController
+ __OBJC_$_PROP_LIST_AAFollowUpController
+ ___101-[AAFollowUpController(Convenience) dismissFollowUpsStartingWithIdentifierPrefix:account:completion:]_block_invoke.362
+ ___101-[AAFollowUpController(Convenience) dismissFollowUpsStartingWithIdentifierPrefix:account:completion:]_block_invoke.362.cold.1
+ ___75-[AAFollowUpController(Convenience) pendingFollowUpsForAccount:completion:]_block_invoke.363
+ ___80-[AAFollowUpController(Convenience) _dismissFollowUpWithIdentifiers:completion:]_block_invoke.367
+ ___80-[AAFollowUpController(Convenience) _dismissFollowUpWithIdentifiers:completion:]_block_invoke.367.cold.1
+ ___87-[AAFollowUpController(Convenience) dismissFollowUpsForAccount:identifiers:completion:]_block_invoke.361
+ ___89-[AAFollowUpController(Convenience) dismissFollowUpWithIdentifier:forAccount:completion:]_block_invoke.359
+ ___89-[AAFollowUpController(Convenience) dismissFollowUpWithIdentifier:forAccount:completion:]_block_invoke.359.cold.1
+ ___89-[AAFollowUpController(Convenience) dismissFollowUpWithIdentifier:forAccount:completion:]_block_invoke.359.cold.2
+ ___91-[AAFollowUpController(Convenience) pendingFollowUpItemUserInfosWithIdentifier:completion:]_block_invoke.370
+ ____AAFollowUpControllerHandleSetupAssistantExited_block_invoke.411
+ ___block_literal_global.373
+ ___block_literal_global.413
+ _kAAAnalyticsEventCustodianRecoveryExperimentalCustodianRecordNotFoundFetchFromCloud
+ _kAAAnalyticsEventCustodianRecoveryExperimentalCustodianshipInfoRecordNotFoundFetchFromCloud
+ _objc_msgSend$_proxiedAppBundleID
+ _objc_msgSend$analyticsInfo
+ _objc_msgSend$cfuReasonAnalyticsEvent
+ _objc_msgSend$proxiedDevice
+ _objc_msgSend$reportPostCFUEvent
+ _objc_msgSend$setCfuType:
+ _objc_msgSend$setDeviceSessionID:
+ _objc_msgSend$setFlowID:
+ _objc_msgSend$setHasProxiedDevice:
+ _objc_msgSend$setPostedReasonError:
+ _objc_msgSend$setProxiedBundleID:
+ _objc_release_x2
- GCC_except_table63
- GCC_except_table78
- ___101-[AAFollowUpController(Convenience) dismissFollowUpsStartingWithIdentifierPrefix:account:completion:]_block_invoke.353
- ___101-[AAFollowUpController(Convenience) dismissFollowUpsStartingWithIdentifierPrefix:account:completion:]_block_invoke.353.cold.1
- ___75-[AAFollowUpController(Convenience) pendingFollowUpsForAccount:completion:]_block_invoke.354
- ___80-[AAFollowUpController(Convenience) _dismissFollowUpWithIdentifiers:completion:]_block_invoke.358
- ___80-[AAFollowUpController(Convenience) _dismissFollowUpWithIdentifiers:completion:]_block_invoke.358.cold.1
- ___87-[AAFollowUpController(Convenience) dismissFollowUpsForAccount:identifiers:completion:]_block_invoke.352
- ___89-[AAFollowUpController(Convenience) dismissFollowUpWithIdentifier:forAccount:completion:]_block_invoke.350
- ___89-[AAFollowUpController(Convenience) dismissFollowUpWithIdentifier:forAccount:completion:]_block_invoke.350.cold.1
- ___89-[AAFollowUpController(Convenience) dismissFollowUpWithIdentifier:forAccount:completion:]_block_invoke.350.cold.2
- ___91-[AAFollowUpController(Convenience) pendingFollowUpItemUserInfosWithIdentifier:completion:]_block_invoke.361
- ____AAFollowUpControllerHandleSetupAssistantExited_block_invoke.400
- ___block_literal_global.364
- ___block_literal_global.402
CStrings:
+ "<CustodinshipInfo: CustodianID: %@, status: %ld, owner: %@>"
+ "<LocalContactInfo: CustodianID: %@, status: %ld, handle: %@, firstName: %@, lastName: %@, familyDSID: %@, familyMemberType: %@, isChild: %@, acceptedAndShared: %@, serverConfirmed: %@>"
+ "<TrustedContact: CustodianID: %@, status: %ld, handle: %@, firstName: %@, lastName: %@, displayName: %@, acceptedAndShared: %@, serverConfirmed: %@, build: %@>"
+ "@\"AAAFollowUpAnalyticsInfo\""
+ "Reporting post cfu event"
+ "T@\"AAAFollowUpAnalyticsInfo\",C,N,V_analyticsInfo"
+ "_analyticsInfo"
+ "_proxiedAppBundleID"
+ "analyticsInfo"
+ "cfuReasonAnalyticsEvent"
+ "com.apple.appleaccount.custodian.recovery.experimental.custodianRecordNotFoundFetchFromCloud"
+ "com.apple.appleaccount.custodian.recovery.experimental.custodianshipInfoRecordNotFoundFetchFromCloud"
+ "followUpPostAnalyticsInfoWithContext:identifier:error:"
+ "proxiedDevice"
+ "reportPostCFUEvent"
+ "setAnalyticsInfo:"
+ "setCfuType:"
+ "setDeviceSessionID:"
+ "setFlowID:"
+ "setHasProxiedDevice:"
+ "setPostedReasonError:"
+ "setProxiedBundleID:"

```
