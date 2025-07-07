## CellularPlanManager

> `/System/Library/PrivateFrameworks/CellularPlanManager.framework/CellularPlanManager`

```diff

-13077.0.0.0.0
-  __TEXT.__text: 0x131c4
+13080.2.0.0.0
+  __TEXT.__text: 0x133f0
   __TEXT.__auth_stubs: 0x3e0
-  __TEXT.__objc_methlist: 0x172c
-  __TEXT.__cstring: 0x2110
+  __TEXT.__objc_methlist: 0x173c
+  __TEXT.__cstring: 0x2146
   __TEXT.__const: 0x48
-  __TEXT.__gcc_except_tab: 0x1c0
+  __TEXT.__gcc_except_tab: 0x1d4
   __TEXT.__oslogstring: 0x5fc
-  __TEXT.__unwind_info: 0x840
+  __TEXT.__unwind_info: 0x860
   __TEXT.__objc_classname: 0x26e
-  __TEXT.__objc_methname: 0x2ec0
+  __TEXT.__objc_methname: 0x2f05
   __TEXT.__objc_methtype: 0xe0e
-  __TEXT.__objc_stubs: 0x1aa0
+  __TEXT.__objc_stubs: 0x1ac0
   __DATA_CONST.__got: 0x100
   __DATA_CONST.__const: 0xd40
   __DATA_CONST.__objc_classlist: 0x98
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa98
+  __DATA_CONST.__objc_selrefs: 0xaa8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x50
   __AUTH_CONST.__auth_got: 0x200
   __AUTH_CONST.__const: 0x440
   __AUTH_CONST.__cfstring: 0x1a40
-  __AUTH_CONST.__objc_const: 0x25d0
+  __AUTH_CONST.__objc_const: 0x25d8
   __DATA.__objc_ivar: 0x15c
   __DATA.__data: 0x2a0
   __DATA.__bss: 0x10

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 03FC372B-B43B-3E98-BA8A-0716908764E6
-  Functions: 681
-  Symbols:   2139
-  CStrings:  1177
+  UUID: 0C1120CC-2F62-3108-A320-8EF1141F395B
+  Functions: 684
+  Symbols:   2147
+  CStrings:  1180
 
Symbols:
+ -[CTCellularPlanManager didEnablePlanItemsForTravel:]
+ GCC_except_table227
+ GCC_except_table236
+ GCC_except_table400
+ GCC_except_table415
+ ___100-[CTCellularPlanManager addNewPlanWithCardData:confirmationCode:triggerType:userConsent:completion:]_block_invoke.228
+ ___100-[CTCellularPlanManager addNewPlanWithCardData:confirmationCode:triggerType:userConsent:completion:]_block_invoke_2.229
+ ___114-[CTCellularPlanManager addNewPlanWithAddress:matchingId:oid:confirmationCode:triggerType:userConsent:completion:]_block_invoke.232
+ ___114-[CTCellularPlanManager addNewPlanWithAddress:matchingId:oid:confirmationCode:triggerType:userConsent:completion:]_block_invoke_2.233
+ ___124-[CTCellularPlanManager addNewRemotePlanWithCardData:confirmationCode:isPairing:withCSN:withContext:userConsent:completion:]_block_invoke.322
+ ___124-[CTCellularPlanManager addNewRemotePlanWithCardData:confirmationCode:isPairing:withCSN:withContext:userConsent:completion:]_block_invoke_2.323
+ ___138-[CTCellularPlanManager addNewRemotePlanWithAddress:matchingId:oid:confirmationCode:isPairing:withCSN:withContext:userConsent:completion:]_block_invoke.324
+ ___138-[CTCellularPlanManager addNewRemotePlanWithAddress:matchingId:oid:confirmationCode:isPairing:withCSN:withContext:userConsent:completion:]_block_invoke_2.325
+ ___39-[CTCellularPlanManager eraseAllPlans:]_block_invoke.298
+ ___39-[CTCellularPlanManager getIMEIPrefix:]_block_invoke.238
+ ___39-[CTCellularPlanManager getIMEIPrefix:]_block_invoke_2.239
+ ___39-[CTCellularPlanManager getRemoteInfo:]_block_invoke.350
+ ___39-[CTCellularPlanManager getRemoteInfo:]_block_invoke.352
+ ___39-[CTCellularPlanManager getRemoteInfo:]_block_invoke_2.351
+ ___40-[CTCellularPlanManager getSelectedEnv:]_block_invoke.243
+ ___40-[CTCellularPlanManager getSelectedEnv:]_block_invoke_2.244
+ ___40-[CTCellularPlanManager mccMncOverride:]_block_invoke.254
+ ___40-[CTCellularPlanManager mccMncOverride:]_block_invoke_2.255
+ ___42-[CTCellularPlanManager getSelectedProxy:]_block_invoke.248
+ ___42-[CTCellularPlanManager getSelectedProxy:]_block_invoke_2.249
+ ___45-[CTCellularPlanManager shouldShowPlanSetup:]_block_invoke.216
+ ___45-[CTCellularPlanManager shouldShowPlanSetup:]_block_invoke_2.217
+ ___47-[CTCellularPlanManager getSupportedFlowTypes:]_block_invoke.219
+ ___47-[CTCellularPlanManager getSupportedFlowTypes:]_block_invoke_2.220
+ ___49-[CTCellularPlanManager getPlansPendingTransfer:]_block_invoke.273
+ ___49-[CTCellularPlanManager planItemsWithCompletion:]_block_invoke.265
+ ___51-[CTCellularPlanManager latitudeLongitudeOverride:]_block_invoke.259
+ ___51-[CTCellularPlanManager latitudeLongitudeOverride:]_block_invoke_2.260
+ ___52-[CTCellularPlanManager resolveSimLabel:completion:]_block_invoke.280
+ ___53-[CTCellularPlanManager didEnablePlanItemsForTravel:]_block_invoke
+ ___53-[CTCellularPlanManager didEnablePlanItemsForTravel:]_block_invoke_2
+ ___53-[CTCellularPlanManager remapSimLabel:to:completion:]_block_invoke.281
+ ___54-[CTCellularPlanManager didDeletePlanItem:completion:]_block_invoke.296
+ ___57-[CTCellularPlanManager didSelectPlanForData:completion:]_block_invoke.288
+ ___57-[CTCellularPlanManager startProvisioningWithCompletion:]_block_invoke.224
+ ___57-[CTCellularPlanManager startProvisioningWithCompletion:]_block_invoke_2.225
+ ___58-[CTCellularPlanManager finishProvisioningWithCompletion:]_block_invoke.226
+ ___58-[CTCellularPlanManager finishProvisioningWithCompletion:]_block_invoke_2.227
+ ___59-[CTCellularPlanManager addNewPlanWithFlowType:completion:]_block_invoke.230
+ ___59-[CTCellularPlanManager addNewPlanWithFlowType:completion:]_block_invoke_2.231
+ ___59-[CTCellularPlanManager eraseAllRemotePlansWithCompletion:]_block_invoke.363
+ ___60-[CTCellularPlanManager didDeleteRemotePlanItem:completion:]_block_invoke.329
+ ___60-[CTCellularPlanManager didSelectRemotePlanItem:completion:]_block_invoke.327
+ ___61-[CTCellularPlanManager carrierItemsShouldUpdate:completion:]_block_invoke.283
+ ___61-[CTCellularPlanManager installPendingRemotePlan:completion:]_block_invoke.234
+ ___61-[CTCellularPlanManager installPendingRemotePlan:completion:]_block_invoke_2.235
+ ___62-[CTCellularPlanManager deletePlanPendingTransfer:completion:]_block_invoke.278
+ ___62-[CTCellularPlanManager deletePlanPendingTransfer:completion:]_block_invoke_2.279
+ ___62-[CTCellularPlanManager didSelectPlansForIMessage:completion:]_block_invoke.292
+ ___63-[CTCellularPlanManager didSelectPlanItem:isEnable:completion:]_block_invoke.285
+ ___63-[CTCellularPlanManager getPlansPendingTransferForTestability:]_block_invoke.274
+ ___63-[CTCellularPlanManager manageAccountForRemotePlan:completion:]_block_invoke.318
+ ___63-[CTCellularPlanManager manageAccountForRemotePlan:completion:]_block_invoke_2.319
+ ___64-[CTCellularPlanManager activatePlanPendingTransfer:completion:]_block_invoke.275
+ ___64-[CTCellularPlanManager activatePlanPendingTransfer:completion:]_block_invoke_2.276
+ ___65-[CTCellularPlanManager didSelectPlanForDefaultVoice:completion:]_block_invoke.290
+ ___66-[CTCellularPlanManager danglingPlanItemsShouldUpdate:completion:]_block_invoke.270
+ ___66-[CTCellularPlanManager startRemoteProvisioningForCSN:completion:]_block_invoke.314
+ ___66-[CTCellularPlanManager startRemoteProvisioningForCSN:completion:]_block_invoke_2.315
+ ___67-[CTCellularPlanManager finishRemoteProvisioningForCSN:completion:]_block_invoke.316
+ ___67-[CTCellularPlanManager finishRemoteProvisioningForCSN:completion:]_block_invoke_2.317
+ ___67-[CTCellularPlanManager isRemotePlanCapableWithContext:completion:]_block_invoke.309
+ ___67-[CTCellularPlanManager isRemotePlanCapableWithContext:completion:]_block_invoke_2.310
+ ___71-[CTCellularPlanManager resumePlanProvisioning:userConsent:completion:]_block_invoke.236
+ ___71-[CTCellularPlanManager resumePlanProvisioning:userConsent:completion:]_block_invoke_2.237
+ ___74-[CTCellularPlanManager shouldShowAddNewRemotePlanWithContext:completion:]_block_invoke.311
+ ___74-[CTCellularPlanManager shouldShowAddNewRemotePlanWithContext:completion:]_block_invoke_2.312
+ ___85-[CTCellularPlanManager addNewRemotePlan:withCSN:withContext:userConsent:completion:]_block_invoke.320
+ ___85-[CTCellularPlanManager addNewRemotePlan:withCSN:withContext:userConsent:completion:]_block_invoke_2.321
+ ___98-[CTCellularPlanManager didPurchaseRemotePlanForEid:imei:meid:iccid:alternateSmdpFqdn:completion:]_block_invoke.354
+ ___98-[CTCellularPlanManager didPurchaseRemotePlanForEid:imei:meid:iccid:alternateSmdpFqdn:completion:]_block_invoke_2.355
+ ___block_literal_global.223
+ ___block_literal_global.242
+ ___block_literal_global.247
+ ___block_literal_global.251
+ ___block_literal_global.253
+ ___block_literal_global.258
+ ___block_literal_global.263
+ ___block_literal_global.268
+ ___block_literal_global.272
+ ___block_literal_global.294
+ ___block_literal_global.300
+ ___block_literal_global.302
+ ___block_literal_global.304
+ ___block_literal_global.306
+ ___block_literal_global.308
+ ___block_literal_global.331
+ ___block_literal_global.333
+ ___block_literal_global.335
+ ___block_literal_global.337
+ ___block_literal_global.339
+ ___block_literal_global.341
+ ___block_literal_global.343
+ ___block_literal_global.345
+ ___block_literal_global.347
+ ___block_literal_global.349
+ ___block_literal_global.357
+ ___block_literal_global.359
+ ___block_literal_global.361
+ ___block_literal_global.365
+ ___block_literal_global.367
+ ___block_literal_global.370
+ _objc_msgSend$didEnablePlanItemsForTravel:completion:
- GCC_except_table233
- GCC_except_table397
- GCC_except_table409
- ___100-[CTCellularPlanManager addNewPlanWithCardData:confirmationCode:triggerType:userConsent:completion:]_block_invoke.227
- ___100-[CTCellularPlanManager addNewPlanWithCardData:confirmationCode:triggerType:userConsent:completion:]_block_invoke_2.228
- ___114-[CTCellularPlanManager addNewPlanWithAddress:matchingId:oid:confirmationCode:triggerType:userConsent:completion:]_block_invoke.231
- ___114-[CTCellularPlanManager addNewPlanWithAddress:matchingId:oid:confirmationCode:triggerType:userConsent:completion:]_block_invoke_2.232
- ___124-[CTCellularPlanManager addNewRemotePlanWithCardData:confirmationCode:isPairing:withCSN:withContext:userConsent:completion:]_block_invoke.321
- ___124-[CTCellularPlanManager addNewRemotePlanWithCardData:confirmationCode:isPairing:withCSN:withContext:userConsent:completion:]_block_invoke_2.322
- ___138-[CTCellularPlanManager addNewRemotePlanWithAddress:matchingId:oid:confirmationCode:isPairing:withCSN:withContext:userConsent:completion:]_block_invoke.323
- ___138-[CTCellularPlanManager addNewRemotePlanWithAddress:matchingId:oid:confirmationCode:isPairing:withCSN:withContext:userConsent:completion:]_block_invoke_2.324
- ___39-[CTCellularPlanManager eraseAllPlans:]_block_invoke.296
- ___39-[CTCellularPlanManager getIMEIPrefix:]_block_invoke.237
- ___39-[CTCellularPlanManager getIMEIPrefix:]_block_invoke_2.238
- ___39-[CTCellularPlanManager getRemoteInfo:]_block_invoke.349
- ___39-[CTCellularPlanManager getRemoteInfo:]_block_invoke.351
- ___39-[CTCellularPlanManager getRemoteInfo:]_block_invoke_2.350
- ___40-[CTCellularPlanManager getSelectedEnv:]_block_invoke.242
- ___40-[CTCellularPlanManager getSelectedEnv:]_block_invoke_2.243
- ___40-[CTCellularPlanManager mccMncOverride:]_block_invoke.253
- ___40-[CTCellularPlanManager mccMncOverride:]_block_invoke_2.254
- ___42-[CTCellularPlanManager getSelectedProxy:]_block_invoke.247
- ___42-[CTCellularPlanManager getSelectedProxy:]_block_invoke_2.248
- ___45-[CTCellularPlanManager shouldShowPlanSetup:]_block_invoke.215
- ___45-[CTCellularPlanManager shouldShowPlanSetup:]_block_invoke_2.216
- ___47-[CTCellularPlanManager getSupportedFlowTypes:]_block_invoke.218
- ___47-[CTCellularPlanManager getSupportedFlowTypes:]_block_invoke_2.219
- ___49-[CTCellularPlanManager getPlansPendingTransfer:]_block_invoke.272
- ___49-[CTCellularPlanManager planItemsWithCompletion:]_block_invoke.263
- ___51-[CTCellularPlanManager latitudeLongitudeOverride:]_block_invoke.258
- ___51-[CTCellularPlanManager latitudeLongitudeOverride:]_block_invoke_2.259
- ___52-[CTCellularPlanManager resolveSimLabel:completion:]_block_invoke.279
- ___53-[CTCellularPlanManager remapSimLabel:to:completion:]_block_invoke.280
- ___54-[CTCellularPlanManager didDeletePlanItem:completion:]_block_invoke.294
- ___57-[CTCellularPlanManager didSelectPlanForData:completion:]_block_invoke.286
- ___57-[CTCellularPlanManager startProvisioningWithCompletion:]_block_invoke.223
- ___57-[CTCellularPlanManager startProvisioningWithCompletion:]_block_invoke_2.224
- ___58-[CTCellularPlanManager finishProvisioningWithCompletion:]_block_invoke.225
- ___58-[CTCellularPlanManager finishProvisioningWithCompletion:]_block_invoke_2.226
- ___59-[CTCellularPlanManager addNewPlanWithFlowType:completion:]_block_invoke.229
- ___59-[CTCellularPlanManager addNewPlanWithFlowType:completion:]_block_invoke_2.230
- ___59-[CTCellularPlanManager eraseAllRemotePlansWithCompletion:]_block_invoke.361
- ___60-[CTCellularPlanManager didDeleteRemotePlanItem:completion:]_block_invoke.327
- ___60-[CTCellularPlanManager didSelectRemotePlanItem:completion:]_block_invoke.325
- ___61-[CTCellularPlanManager carrierItemsShouldUpdate:completion:]_block_invoke.281
- ___61-[CTCellularPlanManager installPendingRemotePlan:completion:]_block_invoke.233
- ___61-[CTCellularPlanManager installPendingRemotePlan:completion:]_block_invoke_2.234
- ___62-[CTCellularPlanManager deletePlanPendingTransfer:completion:]_block_invoke.277
- ___62-[CTCellularPlanManager deletePlanPendingTransfer:completion:]_block_invoke_2.278
- ___62-[CTCellularPlanManager didSelectPlansForIMessage:completion:]_block_invoke.290
- ___63-[CTCellularPlanManager didSelectPlanItem:isEnable:completion:]_block_invoke.283
- ___63-[CTCellularPlanManager getPlansPendingTransferForTestability:]_block_invoke.273
- ___63-[CTCellularPlanManager manageAccountForRemotePlan:completion:]_block_invoke.317
- ___63-[CTCellularPlanManager manageAccountForRemotePlan:completion:]_block_invoke_2.318
- ___64-[CTCellularPlanManager activatePlanPendingTransfer:completion:]_block_invoke.274
- ___64-[CTCellularPlanManager activatePlanPendingTransfer:completion:]_block_invoke_2.275
- ___65-[CTCellularPlanManager didSelectPlanForDefaultVoice:completion:]_block_invoke.288
- ___66-[CTCellularPlanManager danglingPlanItemsShouldUpdate:completion:]_block_invoke.268
- ___66-[CTCellularPlanManager startRemoteProvisioningForCSN:completion:]_block_invoke.313
- ___66-[CTCellularPlanManager startRemoteProvisioningForCSN:completion:]_block_invoke_2.314
- ___67-[CTCellularPlanManager finishRemoteProvisioningForCSN:completion:]_block_invoke.315
- ___67-[CTCellularPlanManager finishRemoteProvisioningForCSN:completion:]_block_invoke_2.316
- ___67-[CTCellularPlanManager isRemotePlanCapableWithContext:completion:]_block_invoke.308
- ___67-[CTCellularPlanManager isRemotePlanCapableWithContext:completion:]_block_invoke_2.309
- ___71-[CTCellularPlanManager resumePlanProvisioning:userConsent:completion:]_block_invoke.235
- ___71-[CTCellularPlanManager resumePlanProvisioning:userConsent:completion:]_block_invoke_2.236
- ___74-[CTCellularPlanManager shouldShowAddNewRemotePlanWithContext:completion:]_block_invoke.310
- ___74-[CTCellularPlanManager shouldShowAddNewRemotePlanWithContext:completion:]_block_invoke_2.311
- ___85-[CTCellularPlanManager addNewRemotePlan:withCSN:withContext:userConsent:completion:]_block_invoke.319
- ___85-[CTCellularPlanManager addNewRemotePlan:withCSN:withContext:userConsent:completion:]_block_invoke_2.320
- ___98-[CTCellularPlanManager didPurchaseRemotePlanForEid:imei:meid:iccid:alternateSmdpFqdn:completion:]_block_invoke.353
- ___98-[CTCellularPlanManager didPurchaseRemotePlanForEid:imei:meid:iccid:alternateSmdpFqdn:completion:]_block_invoke_2.354
- ___block_literal_global.222
- ___block_literal_global.241
- ___block_literal_global.246
- ___block_literal_global.250
- ___block_literal_global.252
- ___block_literal_global.257
- ___block_literal_global.262
- ___block_literal_global.267
- ___block_literal_global.271
- ___block_literal_global.293
- ___block_literal_global.299
- ___block_literal_global.301
- ___block_literal_global.303
- ___block_literal_global.305
- ___block_literal_global.307
- ___block_literal_global.330
- ___block_literal_global.332
- ___block_literal_global.334
- ___block_literal_global.336
- ___block_literal_global.338
- ___block_literal_global.340
- ___block_literal_global.342
- ___block_literal_global.344
- ___block_literal_global.346
- ___block_literal_global.348
- ___block_literal_global.356
- ___block_literal_global.358
- ___block_literal_global.360
- ___block_literal_global.364
- ___block_literal_global.366
- ___block_literal_global.369
CStrings:
+ "-[CTCellularPlanManager didEnablePlanItemsForTravel:]"
+ "didEnablePlanItemsForTravel:"
+ "didEnablePlanItemsForTravel:completion:"

```
