## CellularPlanManager

> `/System/Library/PrivateFrameworks/CellularPlanManager.framework/CellularPlanManager`

```diff

-13091.1.14.0.0
-  __TEXT.__text: 0x12ba0
+13105.1.1.0.0
+  __TEXT.__text: 0x133f0
   __TEXT.__auth_stubs: 0x3e0
   __TEXT.__objc_methlist: 0x173c
-  __TEXT.__cstring: 0x2178
+  __TEXT.__cstring: 0x2190
   __TEXT.__const: 0x48
   __TEXT.__gcc_except_tab: 0x1d4
-  __TEXT.__oslogstring: 0x573
-  __TEXT.__unwind_info: 0x830
+  __TEXT.__oslogstring: 0x5fc
+  __TEXT.__unwind_info: 0x860
   __TEXT.__objc_classname: 0x26e
   __TEXT.__objc_methname: 0x2f05
   __TEXT.__objc_methtype: 0xe0e
-  __TEXT.__objc_stubs: 0x1a20
+  __TEXT.__objc_stubs: 0x1ac0
   __DATA_CONST.__got: 0x100
-  __DATA_CONST.__const: 0xc88
+  __DATA_CONST.__const: 0xd50
   __DATA_CONST.__objc_classlist: 0x98
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x50
   __AUTH_CONST.__auth_got: 0x200
-  __AUTH_CONST.__const: 0x3e0
+  __AUTH_CONST.__const: 0x440
   __AUTH_CONST.__cfstring: 0x1a80
   __AUTH_CONST.__objc_const: 0x25d8
   __DATA.__objc_ivar: 0x15c

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9D4BF7C2-131B-3C44-90D8-90BFF290F8D0
-  Functions: 672
-  Symbols:   2110
-  CStrings:  1178
+  UUID: 068D8513-3A52-3F6C-838E-DFD67B837DFB
+  Functions: 684
+  Symbols:   2147
+  CStrings:  1184
 
Symbols:
+ GCC_except_table155
+ GCC_except_table161
+ GCC_except_table170
+ GCC_except_table185
+ GCC_except_table194
+ GCC_except_table218
+ GCC_except_table221
+ GCC_except_table227
+ GCC_except_table236
+ GCC_except_table412
+ GCC_except_table415
+ ___124-[CTCellularPlanManager addNewRemotePlanWithCardData:confirmationCode:isPairing:withCSN:withContext:userConsent:completion:]_block_invoke.322
+ ___124-[CTCellularPlanManager addNewRemotePlanWithCardData:confirmationCode:isPairing:withCSN:withContext:userConsent:completion:]_block_invoke_2.323
+ ___138-[CTCellularPlanManager addNewRemotePlanWithAddress:matchingId:oid:confirmationCode:isPairing:withCSN:withContext:userConsent:completion:]_block_invoke.324
+ ___138-[CTCellularPlanManager addNewRemotePlanWithAddress:matchingId:oid:confirmationCode:isPairing:withCSN:withContext:userConsent:completion:]_block_invoke_2.325
+ ___39-[CTCellularPlanManager eraseAllPlans:]_block_invoke.297
+ ___39-[CTCellularPlanManager eraseAllPlans:]_block_invoke.298
+ ___39-[CTCellularPlanManager getRemoteInfo:]_block_invoke.350
+ ___39-[CTCellularPlanManager getRemoteInfo:]_block_invoke.352
+ ___39-[CTCellularPlanManager getRemoteInfo:]_block_invoke_2.351
+ ___39-[CTCellularPlanManager setMcc:andMnc:]_block_invoke
+ ___39-[CTCellularPlanManager setMcc:andMnc:]_block_invoke_2
+ ___40-[CTCellularPlanManager mccMncOverride:]_block_invoke.254
+ ___40-[CTCellularPlanManager mccMncOverride:]_block_invoke_2.255
+ ___40-[CTCellularPlanManager mccMncOverride:]_block_invoke_3
+ ___49-[CTCellularPlanManager getPlansPendingTransfer:]_block_invoke.273
+ ___49-[CTCellularPlanManager planItemsWithCompletion:]_block_invoke.264
+ ___49-[CTCellularPlanManager planItemsWithCompletion:]_block_invoke.265
+ ___50-[CTCellularPlanManager setLatitude:andLongitude:]_block_invoke
+ ___50-[CTCellularPlanManager setLatitude:andLongitude:]_block_invoke_2
+ ___51-[CTCellularPlanManager latitudeLongitudeOverride:]_block_invoke.259
+ ___51-[CTCellularPlanManager latitudeLongitudeOverride:]_block_invoke_2.260
+ ___51-[CTCellularPlanManager latitudeLongitudeOverride:]_block_invoke_3
+ ___52-[CTCellularPlanManager resolveSimLabel:completion:]_block_invoke.280
+ ___53-[CTCellularPlanManager remapSimLabel:to:completion:]_block_invoke.281
+ ___54-[CTCellularPlanManager didDeletePlanItem:completion:]_block_invoke.295
+ ___54-[CTCellularPlanManager didDeletePlanItem:completion:]_block_invoke.296
+ ___55-[CTCellularPlanManager showUiIgnoringActivationFlags:]_block_invoke
+ ___55-[CTCellularPlanManager showUiIgnoringActivationFlags:]_block_invoke_2
+ ___57-[CTCellularPlanManager didSelectPlanForData:completion:]_block_invoke.287
+ ___57-[CTCellularPlanManager didSelectPlanForData:completion:]_block_invoke.288
+ ___59-[CTCellularPlanManager eraseAllRemotePlansWithCompletion:]_block_invoke.362
+ ___59-[CTCellularPlanManager eraseAllRemotePlansWithCompletion:]_block_invoke.363
+ ___60-[CTCellularPlanManager didDeleteRemotePlanItem:completion:]_block_invoke.328
+ ___60-[CTCellularPlanManager didDeleteRemotePlanItem:completion:]_block_invoke.329
+ ___60-[CTCellularPlanManager didSelectRemotePlanItem:completion:]_block_invoke.326
+ ___60-[CTCellularPlanManager didSelectRemotePlanItem:completion:]_block_invoke.327
+ ___61-[CTCellularPlanManager carrierItemsShouldUpdate:completion:]_block_invoke.282
+ ___61-[CTCellularPlanManager carrierItemsShouldUpdate:completion:]_block_invoke.283
+ ___62-[CTCellularPlanManager deletePlanPendingTransfer:completion:]_block_invoke.278
+ ___62-[CTCellularPlanManager deletePlanPendingTransfer:completion:]_block_invoke_2.279
+ ___62-[CTCellularPlanManager didSelectPlansForIMessage:completion:]_block_invoke.291
+ ___62-[CTCellularPlanManager didSelectPlansForIMessage:completion:]_block_invoke.292
+ ___63-[CTCellularPlanManager didSelectPlanItem:isEnable:completion:]_block_invoke.284
+ ___63-[CTCellularPlanManager didSelectPlanItem:isEnable:completion:]_block_invoke.285
+ ___63-[CTCellularPlanManager getPlansPendingTransferForTestability:]_block_invoke.274
+ ___63-[CTCellularPlanManager manageAccountForRemotePlan:completion:]_block_invoke.318
+ ___63-[CTCellularPlanManager manageAccountForRemotePlan:completion:]_block_invoke_2.319
+ ___64-[CTCellularPlanManager activatePlanPendingTransfer:completion:]_block_invoke.275
+ ___64-[CTCellularPlanManager activatePlanPendingTransfer:completion:]_block_invoke_2.276
+ ___65-[CTCellularPlanManager didSelectPlanForDefaultVoice:completion:]_block_invoke.289
+ ___65-[CTCellularPlanManager didSelectPlanForDefaultVoice:completion:]_block_invoke.290
+ ___66-[CTCellularPlanManager danglingPlanItemsShouldUpdate:completion:]_block_invoke.269
+ ___66-[CTCellularPlanManager danglingPlanItemsShouldUpdate:completion:]_block_invoke.270
+ ___66-[CTCellularPlanManager startRemoteProvisioningForCSN:completion:]_block_invoke.314
+ ___66-[CTCellularPlanManager startRemoteProvisioningForCSN:completion:]_block_invoke_2.315
+ ___67-[CTCellularPlanManager finishRemoteProvisioningForCSN:completion:]_block_invoke.316
+ ___67-[CTCellularPlanManager finishRemoteProvisioningForCSN:completion:]_block_invoke_2.317
+ ___67-[CTCellularPlanManager isRemotePlanCapableWithContext:completion:]_block_invoke.309
+ ___67-[CTCellularPlanManager isRemotePlanCapableWithContext:completion:]_block_invoke_2.310
+ ___74-[CTCellularPlanManager shouldShowAddNewRemotePlanWithContext:completion:]_block_invoke.311
+ ___74-[CTCellularPlanManager shouldShowAddNewRemotePlanWithContext:completion:]_block_invoke_2.312
+ ___85-[CTCellularPlanManager addNewRemotePlan:withCSN:withContext:userConsent:completion:]_block_invoke.320
+ ___85-[CTCellularPlanManager addNewRemotePlan:withCSN:withContext:userConsent:completion:]_block_invoke_2.321
+ ___98-[CTCellularPlanManager didPurchaseRemotePlanForEid:imei:meid:iccid:alternateSmdpFqdn:completion:]_block_invoke.354
+ ___98-[CTCellularPlanManager didPurchaseRemotePlanForEid:imei:meid:iccid:alternateSmdpFqdn:completion:]_block_invoke_2.355
+ ___block_descriptor_40_e8_32b_e11_v24?0d8d16ls32l8
+ ___block_descriptor_40_e8_32b_e11_v24?0q8q16ls32l8
+ ___block_descriptor_56_e8_32b_e5_v8?0ls32l8
+ ___block_descriptor_56_e8_32o40o48o_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32o_e5_v8?0ls32l8
+ ___block_literal_global.253
+ ___block_literal_global.258
+ ___block_literal_global.263
+ ___block_literal_global.268
+ ___block_literal_global.272
+ ___block_literal_global.300
+ ___block_literal_global.302
+ ___block_literal_global.304
+ ___block_literal_global.306
+ ___block_literal_global.308
+ ___block_literal_global.339
+ ___block_literal_global.341
+ ___block_literal_global.343
+ ___block_literal_global.357
+ ___block_literal_global.359
+ ___block_literal_global.361
+ ___block_literal_global.365
+ ___block_literal_global.367
+ ___block_literal_global.370
+ _objc_msgSend$latitudeLongitudeOverride:
+ _objc_msgSend$mccMncOverride:
+ _objc_msgSend$setLatitude:andLongitude:
+ _objc_msgSend$setMcc:andMnc:
+ _objc_msgSend$showUiIgnoringActivationFlags:
- GCC_except_table134
- GCC_except_table143
- GCC_except_table149
- GCC_except_table173
- GCC_except_table182
- GCC_except_table197
- GCC_except_table206
- GCC_except_table212
- GCC_except_table215
- GCC_except_table388
- GCC_except_table403
- ___124-[CTCellularPlanManager addNewRemotePlanWithCardData:confirmationCode:isPairing:withCSN:withContext:userConsent:completion:]_block_invoke.310
- ___124-[CTCellularPlanManager addNewRemotePlanWithCardData:confirmationCode:isPairing:withCSN:withContext:userConsent:completion:]_block_invoke_2.311
- ___138-[CTCellularPlanManager addNewRemotePlanWithAddress:matchingId:oid:confirmationCode:isPairing:withCSN:withContext:userConsent:completion:]_block_invoke.312
- ___138-[CTCellularPlanManager addNewRemotePlanWithAddress:matchingId:oid:confirmationCode:isPairing:withCSN:withContext:userConsent:completion:]_block_invoke_2.313
- ___39-[CTCellularPlanManager eraseAllPlans:]_block_invoke.285
- ___39-[CTCellularPlanManager eraseAllPlans:]_block_invoke.286
- ___39-[CTCellularPlanManager getRemoteInfo:]_block_invoke.338
- ___39-[CTCellularPlanManager getRemoteInfo:]_block_invoke.340
- ___39-[CTCellularPlanManager getRemoteInfo:]_block_invoke_2.339
- ___49-[CTCellularPlanManager getPlansPendingTransfer:]_block_invoke.261
- ___49-[CTCellularPlanManager planItemsWithCompletion:]_block_invoke.252
- ___49-[CTCellularPlanManager planItemsWithCompletion:]_block_invoke.253
- ___52-[CTCellularPlanManager resolveSimLabel:completion:]_block_invoke.268
- ___53-[CTCellularPlanManager remapSimLabel:to:completion:]_block_invoke.269
- ___54-[CTCellularPlanManager didDeletePlanItem:completion:]_block_invoke.283
- ___54-[CTCellularPlanManager didDeletePlanItem:completion:]_block_invoke.284
- ___57-[CTCellularPlanManager didSelectPlanForData:completion:]_block_invoke.275
- ___57-[CTCellularPlanManager didSelectPlanForData:completion:]_block_invoke.276
- ___59-[CTCellularPlanManager eraseAllRemotePlansWithCompletion:]_block_invoke.350
- ___59-[CTCellularPlanManager eraseAllRemotePlansWithCompletion:]_block_invoke.351
- ___60-[CTCellularPlanManager didDeleteRemotePlanItem:completion:]_block_invoke.316
- ___60-[CTCellularPlanManager didDeleteRemotePlanItem:completion:]_block_invoke.317
- ___60-[CTCellularPlanManager didSelectRemotePlanItem:completion:]_block_invoke.314
- ___60-[CTCellularPlanManager didSelectRemotePlanItem:completion:]_block_invoke.315
- ___61-[CTCellularPlanManager carrierItemsShouldUpdate:completion:]_block_invoke.270
- ___61-[CTCellularPlanManager carrierItemsShouldUpdate:completion:]_block_invoke.271
- ___62-[CTCellularPlanManager deletePlanPendingTransfer:completion:]_block_invoke.266
- ___62-[CTCellularPlanManager deletePlanPendingTransfer:completion:]_block_invoke_2.267
- ___62-[CTCellularPlanManager didSelectPlansForIMessage:completion:]_block_invoke.279
- ___62-[CTCellularPlanManager didSelectPlansForIMessage:completion:]_block_invoke.280
- ___63-[CTCellularPlanManager didSelectPlanItem:isEnable:completion:]_block_invoke.272
- ___63-[CTCellularPlanManager didSelectPlanItem:isEnable:completion:]_block_invoke.273
- ___63-[CTCellularPlanManager getPlansPendingTransferForTestability:]_block_invoke.262
- ___63-[CTCellularPlanManager manageAccountForRemotePlan:completion:]_block_invoke.306
- ___63-[CTCellularPlanManager manageAccountForRemotePlan:completion:]_block_invoke_2.307
- ___64-[CTCellularPlanManager activatePlanPendingTransfer:completion:]_block_invoke.263
- ___64-[CTCellularPlanManager activatePlanPendingTransfer:completion:]_block_invoke_2.264
- ___65-[CTCellularPlanManager didSelectPlanForDefaultVoice:completion:]_block_invoke.277
- ___65-[CTCellularPlanManager didSelectPlanForDefaultVoice:completion:]_block_invoke.278
- ___66-[CTCellularPlanManager danglingPlanItemsShouldUpdate:completion:]_block_invoke.257
- ___66-[CTCellularPlanManager danglingPlanItemsShouldUpdate:completion:]_block_invoke.258
- ___66-[CTCellularPlanManager startRemoteProvisioningForCSN:completion:]_block_invoke.302
- ___66-[CTCellularPlanManager startRemoteProvisioningForCSN:completion:]_block_invoke_2.303
- ___67-[CTCellularPlanManager finishRemoteProvisioningForCSN:completion:]_block_invoke.304
- ___67-[CTCellularPlanManager finishRemoteProvisioningForCSN:completion:]_block_invoke_2.305
- ___67-[CTCellularPlanManager isRemotePlanCapableWithContext:completion:]_block_invoke.297
- ___67-[CTCellularPlanManager isRemotePlanCapableWithContext:completion:]_block_invoke_2.298
- ___74-[CTCellularPlanManager shouldShowAddNewRemotePlanWithContext:completion:]_block_invoke.299
- ___74-[CTCellularPlanManager shouldShowAddNewRemotePlanWithContext:completion:]_block_invoke_2.300
- ___85-[CTCellularPlanManager addNewRemotePlan:withCSN:withContext:userConsent:completion:]_block_invoke.308
- ___85-[CTCellularPlanManager addNewRemotePlan:withCSN:withContext:userConsent:completion:]_block_invoke_2.309
- ___98-[CTCellularPlanManager didPurchaseRemotePlanForEid:imei:meid:iccid:alternateSmdpFqdn:completion:]_block_invoke.342
- ___98-[CTCellularPlanManager didPurchaseRemotePlanForEid:imei:meid:iccid:alternateSmdpFqdn:completion:]_block_invoke_2.343
- ___block_literal_global.256
- ___block_literal_global.260
- ___block_literal_global.282
- ___block_literal_global.288
- ___block_literal_global.290
- ___block_literal_global.292
- ___block_literal_global.296
- ___block_literal_global.319
- ___block_literal_global.321
- ___block_literal_global.323
- ___block_literal_global.325
- ___block_literal_global.327
- ___block_literal_global.329
- ___block_literal_global.353
- ___block_literal_global.355
- ___block_literal_global.358
CStrings:
+ "unable to get mcc/mnc overrides %@"
+ "unable to set lat/long %@"
+ "unable to set mcc/mnc %@"
+ "unable to set show Ui ignoring activation flags %@"
+ "v24@?0d8d16"
+ "v24@?0q8q16"

```
