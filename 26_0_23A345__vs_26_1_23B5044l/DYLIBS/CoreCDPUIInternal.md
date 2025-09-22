## CoreCDPUIInternal

> `/System/Library/PrivateFrameworks/CoreCDPUIInternal.framework/CoreCDPUIInternal`

```diff

-413.0.0.0.0
-  __TEXT.__text: 0x65b8
-  __TEXT.__auth_stubs: 0x350
-  __TEXT.__objc_methlist: 0x704
+416.125.2.0.0
+  __TEXT.__text: 0x5a10
+  __TEXT.__auth_stubs: 0x300
+  __TEXT.__objc_methlist: 0x66c
   __TEXT.__const: 0x68
-  __TEXT.__cstring: 0x916
+  __TEXT.__cstring: 0x854
   __TEXT.__oslogstring: 0x1c3
-  __TEXT.__gcc_except_tab: 0xc0
-  __TEXT.__unwind_info: 0x1d0
-  __TEXT.__objc_classname: 0x158
-  __TEXT.__objc_methname: 0x1aa5
-  __TEXT.__objc_methtype: 0x432
-  __TEXT.__objc_stubs: 0x1500
-  __DATA_CONST.__got: 0x200
-  __DATA_CONST.__const: 0x2d8
+  __TEXT.__gcc_except_tab: 0x60
+  __TEXT.__unwind_info: 0x190
+  __TEXT.__objc_classname: 0x157
+  __TEXT.__objc_methname: 0x17e6
+  __TEXT.__objc_methtype: 0x426
+  __TEXT.__objc_stubs: 0x13c0
+  __DATA_CONST.__got: 0x1e0
+  __DATA_CONST.__const: 0x288
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7d0
+  __DATA_CONST.__objc_selrefs: 0x748
   __DATA_CONST.__objc_superrefs: 0x20
-  __DATA_CONST.__objc_arraydata: 0x70
-  __AUTH_CONST.__auth_got: 0x1b8
+  __DATA_CONST.__objc_arraydata: 0x10
+  __AUTH_CONST.__auth_got: 0x190
   __AUTH_CONST.__const: 0xa0
-  __AUTH_CONST.__cfstring: 0xd80
-  __AUTH_CONST.__objc_const: 0xb30
+  __AUTH_CONST.__cfstring: 0xbc0
+  __AUTH_CONST.__objc_const: 0xac8
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x190
-  __DATA.__objc_ivar: 0x3c
+  __DATA.__objc_ivar: 0x34
   __DATA.__data: 0x300
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 74C265F1-B0A1-3B83-8B83-8ED47C53DE27
-  Functions: 147
-  Symbols:   716
-  CStrings:  575
+  UUID: 365C1CC0-57D4-3390-9619-C544773946BE
+  Functions: 130
+  Symbols:   655
+  CStrings:  524
 
Symbols:
+ ___32-[SettingsController enableCDP:]_block_invoke.195
+ ___32-[SettingsController enableCDP:]_block_invoke.208
+ ___32-[SettingsController enableCDP:]_block_invoke.219
+ ___block_literal_global.351
+ ___block_literal_global.368
+ ___block_literal_global.370
- -[DummyRemoteDeviceSecretValidator edpRepairAction]
- -[DummyRemoteDeviceSecretValidator repairEDPStateWithContext:completion:]
- -[DummyRemoteDeviceSecretValidator setEdpRepairAction:]
- -[DummyRemoteDeviceSecretValidator setStubbedEDPHealth:]
- -[DummyRemoteDeviceSecretValidator stubbedEDPHealth]
- -[DummyRemoteDeviceSecretValidator validateEDPIdentitiesWithContext:completion:]
- -[DummyRemoteDeviceSecretValidator validateEDPRecoveryToken:withContext:completion:]
- -[SettingsController _beginEDPTokenEntryFlowWithHSA2Enabled:]
- -[SettingsController beginDirectFallbackToEDPToken:]
- -[SettingsController beginEDPTokenEntryFlowForHSA2User:]
- -[SettingsController beginEDPTokenEntryFlowForNonHSA2User:]
- -[SettingsController beginEventualFallbackToEDPToken:]
- -[SettingsController openEDPTokenSettingsPane:]
- GCC_except_table90
- GCC_except_table92
- _OBJC_CLASS_$_CDPStateSwiftUIProvider
- _OBJC_CLASS_$_NSConstantArray
- _OBJC_CLASS_$_NSError
- _OBJC_IVAR_$_DummyRemoteDeviceSecretValidator._edpRepairAction
- _OBJC_IVAR_$_DummyRemoteDeviceSecretValidator._stubbedEDPHealth
- __OBJC_$_PROP_LIST_DummyRemoteDeviceSecretValidator
- ___32-[SettingsController enableCDP:]_block_invoke.198
- ___32-[SettingsController enableCDP:]_block_invoke.211
- ___32-[SettingsController enableCDP:]_block_invoke.222
- ___52-[SettingsController beginDirectFallbackToEDPToken:]_block_invoke
- ___54-[SettingsController beginEventualFallbackToEDPToken:]_block_invoke
- ___80-[DummyRemoteDeviceSecretValidator validateEDPIdentitiesWithContext:completion:]_block_invoke
- ___84-[DummyRemoteDeviceSecretValidator validateEDPRecoveryToken:withContext:completion:]_block_invoke
- ___NSDictionary0__struct
- ___block_descriptor_48_e8_32s40bs_e5_v8?0ls40l8s32l8
- ___block_descriptor_56_e8_32s40s48w_e5_v8?0ls32l8s40l8w48l8
- ___block_literal_global.354
- ___block_literal_global.371
- ___block_literal_global.373
- _kCFBooleanFalse
- _objc_copyWeak
- _objc_destroyWeak
- _objc_initWeak
- _objc_loadWeakRetained
- _objc_msgSend$_beginEDPTokenEntryFlowWithHSA2Enabled:
- _objc_msgSend$_offerRPD
- _objc_msgSend$cdpContext:promptForEDPRecoveryTokenWithValidator:successfulCDPRecoveryContinuationHandler:
- _objc_msgSend$cdp_errorWithCode:
- _objc_msgSend$edpRepairAction
- _objc_msgSend$makeSwiftUIViewForEDPTokenInSpyglassWithRecoveryToken:presentingViewController:
- _objc_msgSend$setEdpRepairAction:
- _objc_msgSend$setIsHSA2Account:
- _objc_msgSend$setStubbedEDPHealth:
- _objc_msgSend$stubbedEDPHealth
- _objc_setProperty_nonatomic_copy
CStrings:
- "@?"
- "@?16@0:8"
- "OfferEDPRecoveryToken"
- "T@?,C,N,V_edpRepairAction"
- "TQ,N,V_stubbedEDPHealth"
- "_beginEDPTokenEntryFlowWithHSA2Enabled:"
- "_edpRepairAction"
- "_stubbedEDPHealth"
- "afloat"
- "apple"
- "ashen"
- "beginDirectFallbackToEDPToken:"
- "beginEDPTokenEntryFlowForHSA2User:"
- "beginEDPTokenEntryFlowForNonHSA2User:"
- "beginEventualFallbackToEDPToken:"
- "calm"
- "cdpContext:promptForEDPRecoveryTokenWithValidator:successfulCDPRecoveryContinuationHandler:"
- "cdp_errorWithCode:"
- "condense"
- "duly"
- "easel"
- "edpRepairAction"
- "makeSwiftUIViewForEDPTokenInSpyglassWithRecoveryToken:presentingViewController:"
- "openEDPTokenSettingsPane:"
- "picker"
- "picker-easel-vacation-squiggly-calm-untitled-ashen-duly-afloat-condense-apple-studied"
- "repairEDPStateWithContext:completion:"
- "setEdpRepairAction:"
- "setIsHSA2Account:"
- "setStubbedEDPHealth:"
- "squiggly"
- "stubbedEDPHealth"
- "studied"
- "untitled"
- "vacation"
- "validateEDPIdentitiesWithContext:completion:"
- "validateEDPRecoveryToken:withContext:completion:"

```
