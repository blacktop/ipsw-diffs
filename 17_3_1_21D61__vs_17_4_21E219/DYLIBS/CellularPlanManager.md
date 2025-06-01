## CellularPlanManager

> `/System/Library/PrivateFrameworks/CellularPlanManager.framework/CellularPlanManager`

```diff

-11305.1.0.0.0
-  __TEXT.__text: 0x12d64
+11523.1.0.0.0
+  __TEXT.__text: 0x12e98
   __TEXT.__auth_stubs: 0x3e0
-  __TEXT.__objc_methlist: 0x1190
-  __TEXT.__cstring: 0x1fdc
+  __TEXT.__objc_methlist: 0x11a0
+  __TEXT.__cstring: 0x1ffe
   __TEXT.__const: 0x20
   __TEXT.__gcc_except_tab: 0x188
   __TEXT.__oslogstring: 0x573
   __TEXT.__unwind_info: 0x808
   __TEXT.__objc_classname: 0x270
-  __TEXT.__objc_methname: 0x2d7b
-  __TEXT.__objc_methtype: 0xe1f
+  __TEXT.__objc_methname: 0x2ddd
+  __TEXT.__objc_methtype: 0xe22
   __TEXT.__objc_stubs: 0x19e0
   __DATA_CONST.__got: 0x20
   __DATA_CONST.__const: 0xc20
   __DATA_CONST.__objc_classlist: 0x98
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x2780
-  __DATA_CONST.__objc_selrefs: 0x9e8
-  __AUTH_CONST.__cfstring: 0x1960
+  __DATA_CONST.__objc_const: 0x27b0
+  __DATA_CONST.__objc_selrefs: 0x9f0
+  __DATA_CONST.__objc_protorefs: 0x10
+  __DATA_CONST.__objc_classrefs: 0xe0
+  __DATA_CONST.__objc_superrefs: 0x50
+  __AUTH_CONST.__cfstring: 0x1980
   __AUTH_CONST.__objc_const: 0x0
-  __AUTH_CONST.__const: 0x260
+  __AUTH_CONST.__const: 0x340
   __AUTH_CONST.__auth_got: 0x200
-  __DATA.__objc_protorefs: 0x10
-  __DATA.__objc_classrefs: 0xe0
-  __DATA.__objc_superrefs: 0x50
-  __DATA.__objc_ivar: 0x150
+  __DATA.__objc_ivar: 0x154
   __DATA.__data: 0x2a0
   __DATA.__bss: 0x10
-  __DATA_DIRTY.__const: 0x180
+  __DATA_DIRTY.__const: 0xa0
   __DATA_DIRTY.__objc_const: 0x828
   __DATA_DIRTY.__objc_data: 0x5f0
   __DATA_DIRTY.__bss: 0x30

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4014AAA4-DF90-39F7-A0E2-24BD629C0914
-  Functions: 680
-  Symbols:   2087
-  CStrings:  1152
+  UUID: AD17D221-12E9-305B-942F-AE21272361AE
+  Functions: 681
+  Symbols:   2090
+  CStrings:  1158
 
Symbols:
+ -[CTCellularPlanCarrierItem initWithName:plan:url:applePaySupported:responseType:warningText:purchaseOption:]
+ -[CTCellularPlanCarrierItem purchaseOption]
+ _OBJC_IVAR_$_CTCellularPlanCarrierItem._purchaseOption
+ ___100-[CTCellularPlanManager addNewPlanWithCardData:confirmationCode:triggerType:userConsent:completion:]_block_invoke.230
+ ___100-[CTCellularPlanManager addNewPlanWithCardData:confirmationCode:triggerType:userConsent:completion:]_block_invoke_2.231
+ ___114-[CTCellularPlanManager addNewPlanWithAddress:matchingId:oid:confirmationCode:triggerType:userConsent:completion:]_block_invoke.234
+ ___114-[CTCellularPlanManager addNewPlanWithAddress:matchingId:oid:confirmationCode:triggerType:userConsent:completion:]_block_invoke_2.235
+ ___124-[CTCellularPlanManager addNewRemotePlanWithCardData:confirmationCode:isPairing:withCSN:withContext:userConsent:completion:]_block_invoke.312
+ ___124-[CTCellularPlanManager addNewRemotePlanWithCardData:confirmationCode:isPairing:withCSN:withContext:userConsent:completion:]_block_invoke_2.313
+ ___138-[CTCellularPlanManager addNewRemotePlanWithAddress:matchingId:oid:confirmationCode:isPairing:withCSN:withContext:userConsent:completion:]_block_invoke.314
+ ___138-[CTCellularPlanManager addNewRemotePlanWithAddress:matchingId:oid:confirmationCode:isPairing:withCSN:withContext:userConsent:completion:]_block_invoke_2.315
+ ___39-[CTCellularPlanManager eraseAllPlans:]_block_invoke.288
+ ___39-[CTCellularPlanManager getIMEIPrefix:]_block_invoke.240
+ ___39-[CTCellularPlanManager getIMEIPrefix:]_block_invoke_2.241
+ ___39-[CTCellularPlanManager getRemoteInfo:]_block_invoke.340
+ ___39-[CTCellularPlanManager getRemoteInfo:]_block_invoke.342
+ ___39-[CTCellularPlanManager getRemoteInfo:]_block_invoke_2.341
+ ___40-[CTCellularPlanManager getSelectedEnv:]_block_invoke.245
+ ___40-[CTCellularPlanManager getSelectedEnv:]_block_invoke_2.246
+ ___42-[CTCellularPlanManager getSelectedProxy:]_block_invoke.250
+ ___42-[CTCellularPlanManager getSelectedProxy:]_block_invoke_2.251
+ ___45-[CTCellularPlanManager shouldShowPlanSetup:]_block_invoke.218
+ ___45-[CTCellularPlanManager shouldShowPlanSetup:]_block_invoke_2.219
+ ___47-[CTCellularPlanManager getSupportedFlowTypes:]_block_invoke.221
+ ___47-[CTCellularPlanManager getSupportedFlowTypes:]_block_invoke_2.222
+ ___49-[CTCellularPlanManager getPlansPendingTransfer:]_block_invoke.263
+ ___49-[CTCellularPlanManager planItemsWithCompletion:]_block_invoke.255
+ ___52-[CTCellularPlanManager resolveSimLabel:completion:]_block_invoke.270
+ ___53-[CTCellularPlanManager remapSimLabel:to:completion:]_block_invoke.271
+ ___54-[CTCellularPlanManager didDeletePlanItem:completion:]_block_invoke.286
+ ___57-[CTCellularPlanManager didSelectPlanForData:completion:]_block_invoke.278
+ ___57-[CTCellularPlanManager startProvisioningWithCompletion:]_block_invoke.226
+ ___57-[CTCellularPlanManager startProvisioningWithCompletion:]_block_invoke_2.227
+ ___58-[CTCellularPlanManager finishProvisioningWithCompletion:]_block_invoke.228
+ ___58-[CTCellularPlanManager finishProvisioningWithCompletion:]_block_invoke_2.229
+ ___59-[CTCellularPlanManager addNewPlanWithFlowType:completion:]_block_invoke.232
+ ___59-[CTCellularPlanManager addNewPlanWithFlowType:completion:]_block_invoke_2.233
+ ___59-[CTCellularPlanManager eraseAllRemotePlansWithCompletion:]_block_invoke.356
+ ___60-[CTCellularPlanManager didDeleteRemotePlanItem:completion:]_block_invoke.319
+ ___60-[CTCellularPlanManager didSelectRemotePlanItem:completion:]_block_invoke.317
+ ___61-[CTCellularPlanManager carrierItemsShouldUpdate:completion:]_block_invoke.273
+ ___61-[CTCellularPlanManager installPendingRemotePlan:completion:]_block_invoke.236
+ ___61-[CTCellularPlanManager installPendingRemotePlan:completion:]_block_invoke_2.237
+ ___62-[CTCellularPlanManager deletePlanPendingTransfer:completion:]_block_invoke.268
+ ___62-[CTCellularPlanManager deletePlanPendingTransfer:completion:]_block_invoke_2.269
+ ___62-[CTCellularPlanManager didSelectPlansForIMessage:completion:]_block_invoke.282
+ ___63-[CTCellularPlanManager didSelectPlanItem:isEnable:completion:]_block_invoke.275
+ ___63-[CTCellularPlanManager getPlansPendingTransferForTestability:]_block_invoke.264
+ ___63-[CTCellularPlanManager manageAccountForRemotePlan:completion:]_block_invoke.308
+ ___63-[CTCellularPlanManager manageAccountForRemotePlan:completion:]_block_invoke_2.309
+ ___64-[CTCellularPlanManager activatePlanPendingTransfer:completion:]_block_invoke.265
+ ___64-[CTCellularPlanManager activatePlanPendingTransfer:completion:]_block_invoke_2.266
+ ___65-[CTCellularPlanManager didSelectPlanForDefaultVoice:completion:]_block_invoke.280
+ ___65-[CTCellularPlanManager getPhoneAuthTokenWithMessage:completion:]_block_invoke.344
+ ___65-[CTCellularPlanManager getPhoneAuthTokenWithMessage:completion:]_block_invoke_2.345
+ ___66-[CTCellularPlanManager danglingPlanItemsShouldUpdate:completion:]_block_invoke.260
+ ___66-[CTCellularPlanManager startRemoteProvisioningForCSN:completion:]_block_invoke.304
+ ___66-[CTCellularPlanManager startRemoteProvisioningForCSN:completion:]_block_invoke_2.305
+ ___67-[CTCellularPlanManager finishRemoteProvisioningForCSN:completion:]_block_invoke.306
+ ___67-[CTCellularPlanManager finishRemoteProvisioningForCSN:completion:]_block_invoke_2.307
+ ___67-[CTCellularPlanManager isRemotePlanCapableWithContext:completion:]_block_invoke.299
+ ___67-[CTCellularPlanManager isRemotePlanCapableWithContext:completion:]_block_invoke_2.300
+ ___71-[CTCellularPlanManager resumePlanProvisioning:userConsent:completion:]_block_invoke.238
+ ___71-[CTCellularPlanManager resumePlanProvisioning:userConsent:completion:]_block_invoke_2.239
+ ___74-[CTCellularPlanManager shouldShowAddNewRemotePlanWithContext:completion:]_block_invoke.301
+ ___74-[CTCellularPlanManager shouldShowAddNewRemotePlanWithContext:completion:]_block_invoke_2.302
+ ___85-[CTCellularPlanManager addNewRemotePlan:withCSN:withContext:userConsent:completion:]_block_invoke.310
+ ___85-[CTCellularPlanManager addNewRemotePlan:withCSN:withContext:userConsent:completion:]_block_invoke_2.311
+ ___98-[CTCellularPlanManager didPurchaseRemotePlanForEid:imei:meid:iccid:alternateSmdpFqdn:completion:]_block_invoke.347
+ ___98-[CTCellularPlanManager didPurchaseRemotePlanForEid:imei:meid:iccid:alternateSmdpFqdn:completion:]_block_invoke_2.348
+ ___block_literal_global.225
+ ___block_literal_global.244
+ ___block_literal_global.249
+ ___block_literal_global.253
+ ___block_literal_global.258
+ ___block_literal_global.262
+ ___block_literal_global.284
+ ___block_literal_global.290
+ ___block_literal_global.292
+ ___block_literal_global.294
+ ___block_literal_global.296
+ ___block_literal_global.298
+ ___block_literal_global.321
+ ___block_literal_global.323
+ ___block_literal_global.325
+ ___block_literal_global.327
+ ___block_literal_global.329
+ ___block_literal_global.331
+ ___block_literal_global.333
+ ___block_literal_global.335
+ ___block_literal_global.337
+ ___block_literal_global.339
+ ___block_literal_global.350
+ ___block_literal_global.352
+ ___block_literal_global.354
+ ___block_literal_global.358
+ ___block_literal_global.360
+ ___block_literal_global.363
+ _objc_msgSend$initWithName:plan:url:applePaySupported:responseType:warningText:purchaseOption:
- -[CTCellularPlanCarrierItem initWithName:plan:url:applePaySupported:responseType:warningText:]
- ___100-[CTCellularPlanManager addNewPlanWithCardData:confirmationCode:triggerType:userConsent:completion:]_block_invoke.229
- ___100-[CTCellularPlanManager addNewPlanWithCardData:confirmationCode:triggerType:userConsent:completion:]_block_invoke_2.230
- ___114-[CTCellularPlanManager addNewPlanWithAddress:matchingId:oid:confirmationCode:triggerType:userConsent:completion:]_block_invoke.233
- ___114-[CTCellularPlanManager addNewPlanWithAddress:matchingId:oid:confirmationCode:triggerType:userConsent:completion:]_block_invoke_2.234
- ___124-[CTCellularPlanManager addNewRemotePlanWithCardData:confirmationCode:isPairing:withCSN:withContext:userConsent:completion:]_block_invoke.311
- ___124-[CTCellularPlanManager addNewRemotePlanWithCardData:confirmationCode:isPairing:withCSN:withContext:userConsent:completion:]_block_invoke_2.312
- ___138-[CTCellularPlanManager addNewRemotePlanWithAddress:matchingId:oid:confirmationCode:isPairing:withCSN:withContext:userConsent:completion:]_block_invoke.313
- ___138-[CTCellularPlanManager addNewRemotePlanWithAddress:matchingId:oid:confirmationCode:isPairing:withCSN:withContext:userConsent:completion:]_block_invoke_2.314
- ___39-[CTCellularPlanManager eraseAllPlans:]_block_invoke.286
- ___39-[CTCellularPlanManager getIMEIPrefix:]_block_invoke.239
- ___39-[CTCellularPlanManager getIMEIPrefix:]_block_invoke_2.240
- ___39-[CTCellularPlanManager getRemoteInfo:]_block_invoke.339
- ___39-[CTCellularPlanManager getRemoteInfo:]_block_invoke.341
- ___39-[CTCellularPlanManager getRemoteInfo:]_block_invoke_2.340
- ___40-[CTCellularPlanManager getSelectedEnv:]_block_invoke.244
- ___40-[CTCellularPlanManager getSelectedEnv:]_block_invoke_2.245
- ___42-[CTCellularPlanManager getSelectedProxy:]_block_invoke.249
- ___42-[CTCellularPlanManager getSelectedProxy:]_block_invoke_2.250
- ___45-[CTCellularPlanManager shouldShowPlanSetup:]_block_invoke.217
- ___45-[CTCellularPlanManager shouldShowPlanSetup:]_block_invoke_2.218
- ___47-[CTCellularPlanManager getSupportedFlowTypes:]_block_invoke.220
- ___47-[CTCellularPlanManager getSupportedFlowTypes:]_block_invoke_2.221
- ___49-[CTCellularPlanManager getPlansPendingTransfer:]_block_invoke.262
- ___49-[CTCellularPlanManager planItemsWithCompletion:]_block_invoke.253
- ___52-[CTCellularPlanManager resolveSimLabel:completion:]_block_invoke.269
- ___53-[CTCellularPlanManager remapSimLabel:to:completion:]_block_invoke.270
- ___54-[CTCellularPlanManager didDeletePlanItem:completion:]_block_invoke.284
- ___57-[CTCellularPlanManager didSelectPlanForData:completion:]_block_invoke.276
- ___57-[CTCellularPlanManager startProvisioningWithCompletion:]_block_invoke.225
- ___57-[CTCellularPlanManager startProvisioningWithCompletion:]_block_invoke_2.226
- ___58-[CTCellularPlanManager finishProvisioningWithCompletion:]_block_invoke.227
- ___58-[CTCellularPlanManager finishProvisioningWithCompletion:]_block_invoke_2.228
- ___59-[CTCellularPlanManager addNewPlanWithFlowType:completion:]_block_invoke.231
- ___59-[CTCellularPlanManager addNewPlanWithFlowType:completion:]_block_invoke_2.232
- ___59-[CTCellularPlanManager eraseAllRemotePlansWithCompletion:]_block_invoke.354
- ___60-[CTCellularPlanManager didDeleteRemotePlanItem:completion:]_block_invoke.317
- ___60-[CTCellularPlanManager didSelectRemotePlanItem:completion:]_block_invoke.315
- ___61-[CTCellularPlanManager carrierItemsShouldUpdate:completion:]_block_invoke.271
- ___61-[CTCellularPlanManager installPendingRemotePlan:completion:]_block_invoke.235
- ___61-[CTCellularPlanManager installPendingRemotePlan:completion:]_block_invoke_2.236
- ___62-[CTCellularPlanManager deletePlanPendingTransfer:completion:]_block_invoke.267
- ___62-[CTCellularPlanManager deletePlanPendingTransfer:completion:]_block_invoke_2.268
- ___62-[CTCellularPlanManager didSelectPlansForIMessage:completion:]_block_invoke.280
- ___63-[CTCellularPlanManager didSelectPlanItem:isEnable:completion:]_block_invoke.273
- ___63-[CTCellularPlanManager getPlansPendingTransferForTestability:]_block_invoke.263
- ___63-[CTCellularPlanManager manageAccountForRemotePlan:completion:]_block_invoke.307
- ___63-[CTCellularPlanManager manageAccountForRemotePlan:completion:]_block_invoke_2.308
- ___64-[CTCellularPlanManager activatePlanPendingTransfer:completion:]_block_invoke.264
- ___64-[CTCellularPlanManager activatePlanPendingTransfer:completion:]_block_invoke_2.265
- ___65-[CTCellularPlanManager didSelectPlanForDefaultVoice:completion:]_block_invoke.278
- ___65-[CTCellularPlanManager getPhoneAuthTokenWithMessage:completion:]_block_invoke.343
- ___65-[CTCellularPlanManager getPhoneAuthTokenWithMessage:completion:]_block_invoke_2.344
- ___66-[CTCellularPlanManager danglingPlanItemsShouldUpdate:completion:]_block_invoke.258
- ___66-[CTCellularPlanManager startRemoteProvisioningForCSN:completion:]_block_invoke.303
- ___66-[CTCellularPlanManager startRemoteProvisioningForCSN:completion:]_block_invoke_2.304
- ___67-[CTCellularPlanManager finishRemoteProvisioningForCSN:completion:]_block_invoke.305
- ___67-[CTCellularPlanManager finishRemoteProvisioningForCSN:completion:]_block_invoke_2.306
- ___67-[CTCellularPlanManager isRemotePlanCapableWithContext:completion:]_block_invoke.298
- ___67-[CTCellularPlanManager isRemotePlanCapableWithContext:completion:]_block_invoke_2.299
- ___71-[CTCellularPlanManager resumePlanProvisioning:userConsent:completion:]_block_invoke.237
- ___71-[CTCellularPlanManager resumePlanProvisioning:userConsent:completion:]_block_invoke_2.238
- ___74-[CTCellularPlanManager shouldShowAddNewRemotePlanWithContext:completion:]_block_invoke.300
- ___74-[CTCellularPlanManager shouldShowAddNewRemotePlanWithContext:completion:]_block_invoke_2.301
- ___85-[CTCellularPlanManager addNewRemotePlan:withCSN:withContext:userConsent:completion:]_block_invoke.309
- ___85-[CTCellularPlanManager addNewRemotePlan:withCSN:withContext:userConsent:completion:]_block_invoke_2.310
- ___98-[CTCellularPlanManager didPurchaseRemotePlanForEid:imei:meid:iccid:alternateSmdpFqdn:completion:]_block_invoke.346
- ___98-[CTCellularPlanManager didPurchaseRemotePlanForEid:imei:meid:iccid:alternateSmdpFqdn:completion:]_block_invoke_2.347
- ___block_literal_global.224
- ___block_literal_global.243
- ___block_literal_global.248
- ___block_literal_global.252
- ___block_literal_global.257
- ___block_literal_global.261
- ___block_literal_global.283
- ___block_literal_global.289
- ___block_literal_global.291
- ___block_literal_global.293
- ___block_literal_global.295
- ___block_literal_global.297
- ___block_literal_global.320
- ___block_literal_global.322
- ___block_literal_global.324
- ___block_literal_global.326
- ___block_literal_global.328
- ___block_literal_global.330
- ___block_literal_global.332
- ___block_literal_global.334
- ___block_literal_global.336
- ___block_literal_global.338
- ___block_literal_global.349
- ___block_literal_global.351
- ___block_literal_global.353
- ___block_literal_global.357
- ___block_literal_global.359
- ___block_literal_global.362
- _objc_msgSend$initWithName:plan:url:applePaySupported:responseType:warningText:
CStrings:
+ "\a\x11"
+ "<%@: %p Carrier Name: %@ plan: %@ ApplePay: %d warningText: %@ purchaseOption: %@>"
+ "@68@0:8@16@24@32B40@44@52@60"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",R,N,V_purchaseOption"
+ "_purchaseOption"
+ "initWithName:plan:url:applePaySupported:responseType:warningText:purchaseOption:"
+ "purchaseOption"
- "\x06\x11"
- "<%@: %p Carrier Name: %@ plan: %@ ApplePay: %d warningText: %@>"
- "@60@0:8@16@24@32B40@44@52"
- "initWithName:plan:url:applePaySupported:responseType:warningText:"

```
