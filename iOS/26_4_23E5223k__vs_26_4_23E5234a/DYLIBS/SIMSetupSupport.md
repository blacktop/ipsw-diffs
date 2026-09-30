## SIMSetupSupport

> `/System/Library/PrivateFrameworks/SIMSetupSupport.framework/SIMSetupSupport`

```diff

-894.1.0.0.0
-  __TEXT.__text: 0xc15c8
+894.2.0.0.0
+  __TEXT.__text: 0xc1294
   __TEXT.__auth_stubs: 0x810
   __TEXT.__objc_methlist: 0xa4cc
   __TEXT.__const: 0x1d8
   __TEXT.__gcc_except_tab: 0x1d80
-  __TEXT.__cstring: 0x10d0b
+  __TEXT.__cstring: 0x10cf1
   __TEXT.__oslogstring: 0x6eea
   __TEXT.__dlopen_cstrs: 0x2be
   __TEXT.__ustring: 0xa

   __DATA_CONST.__objc_arraydata: 0x1a8
   __AUTH_CONST.__auth_got: 0x418
   __AUTH_CONST.__const: 0x920
-  __AUTH_CONST.__cfstring: 0x7c00
+  __AUTH_CONST.__cfstring: 0x7be0
   __AUTH_CONST.__objc_const: 0x3e140
   __AUTH_CONST.__objc_intobj: 0x6c0
   __AUTH_CONST.__objc_dictobj: 0x28

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 80417DE3-17CB-3F21-94F4-A00F9AD87851
+  UUID: 0A9AF605-361C-302F-B234-8394FF693CAE
   Functions: 4031
   Symbols:   14680
-  CStrings:  7685
+  CStrings:  7683
 
Symbols:
+ ___53-[TSTransferListViewController _startPendingInstall:]_block_invoke.231
+ ___53-[TSTransferListViewController _startPendingInstall:]_block_invoke.233
+ ___53-[TSTransferListViewController _startPendingInstall:]_block_invoke_2.232
+ ___block_literal_global.235
+ ___block_literal_global.306
+ ___block_literal_global.322
- ___53-[TSTransferListViewController _startPendingInstall:]_block_invoke.234
- ___53-[TSTransferListViewController _startPendingInstall:]_block_invoke.236
- ___53-[TSTransferListViewController _startPendingInstall:]_block_invoke_2.235
- ___block_literal_global.238
- ___block_literal_global.309
- ___block_literal_global.325
Functions:
~ -[TSTransferListViewController _maybeDisplayPhysicalPlanConversionAlert:showServiceImpact:phoneNumber:completion:] : 3092 -> 3012
~ +[TSCellularPlanUserConsentViewController calculateTitleAndDetailsWithName:consentType:trialPlanType:trialExpirationDate:title:details:hasProvisioningServiceImpact:] : 1964 -> 1832
~ -[TSSinglePlanTransferViewController initWithTransferPlan:isPhysical:isIneligible:inBuddy:confirmCellularPlanTransfer:showOtherOptions:isStandaloneProximityFlow:transferBackPhoneNumber:isShowingFilteredPlans:] : 1540 -> 1344
~ -[TSSinglePlanTransferViewController initWithPendingInstallPlan:] : 1404 -> 1200
~ -[TSSinglePlanTransferViewController initWithLocalPhysical:carrierName:hasProvisioningServiceImpact:] : 1164 -> 956
CStrings:
- "SERVICE_IMPACT_MESSAGE_%@"

```
