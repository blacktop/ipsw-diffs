## CellularPlanManager

> `/System/Library/PrivateFrameworks/CellularPlanManager.framework/CellularPlanManager`

```diff

-13187.6.0.0.0
-  __TEXT.__text: 0x13368
-  __TEXT.__auth_stubs: 0x3b0
-  __TEXT.__objc_methlist: 0x1754
-  __TEXT.__cstring: 0x21e3
-  __TEXT.__const: 0x48
-  __TEXT.__gcc_except_tab: 0x1d4
-  __TEXT.__oslogstring: 0x573
-  __TEXT.__unwind_info: 0x8b8
-  __TEXT.__objc_classname: 0x26e
-  __TEXT.__objc_methname: 0x2f6d
-  __TEXT.__objc_methtype: 0xe0e
-  __TEXT.__objc_stubs: 0x1a20
-  __DATA_CONST.__got: 0x100
-  __DATA_CONST.__const: 0xc90
+13466.3.0.0.0
+  __TEXT.__text: 0x12970
+  __TEXT.__objc_methlist: 0x17c4
+  __TEXT.__cstring: 0x2284
+  __TEXT.__const: 0x60
+  __TEXT.__gcc_except_tab: 0x1b8
+  __TEXT.__oslogstring: 0x5fc
+  __TEXT.__unwind_info: 0x860
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0xd88
   __DATA_CONST.__objc_classlist: 0x98
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xab8
+  __DATA_CONST.__objc_selrefs: 0xb00
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x50
-  __AUTH_CONST.__auth_got: 0x1e8
-  __AUTH_CONST.__const: 0x3e0
-  __AUTH_CONST.__cfstring: 0x1ac0
-  __AUTH_CONST.__objc_const: 0x2608
-  __DATA.__objc_ivar: 0x160
+  __DATA_CONST.__got: 0x100
+  __AUTH_CONST.__const: 0x440
+  __AUTH_CONST.__cfstring: 0x1b60
+  __AUTH_CONST.__objc_const: 0x26c8
+  __AUTH_CONST.__auth_got: 0x0
+  __DATA.__objc_ivar: 0x170
   __DATA.__data: 0x2a0
   __DATA.__bss: 0x10
   __DATA_DIRTY.__objc_data: 0x5f0

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 78C651D6-4A4F-3B56-B548-CAAC417B659B
-  Functions: 676
-  Symbols:   2116
-  CStrings:  1186
+  UUID: 8885DA0A-1426-32CB-8F7C-35D36C30A123
+  Functions: 695
+  Symbols:   2179
+  CStrings:  544
 
Symbols:
+ -[CTCellularPlanItem carrierAppAdamId]
+ -[CTCellularPlanItem qsLifecycleState]
+ -[CTCellularPlanItem qsRole]
+ -[CTCellularPlanItem setCarrierAppAdamId:]
+ -[CTCellularPlanItem setQsLifecycleState:]
+ -[CTCellularPlanItem setQsRole:]
+ -[CTCellularPlanItem setSimLocation:]
+ -[CTCellularPlanItem simLocation]
+ -[CTCellularPlanManager didTransferPlanForCsn:iccid:srcIccid:profileServer:matchingId:state:]
+ GCC_except_table155
+ GCC_except_table161
+ GCC_except_table170
+ GCC_except_table185
+ GCC_except_table194
+ GCC_except_table218
+ GCC_except_table221
+ GCC_except_table227
+ GCC_except_table236
+ GCC_except_table401
+ GCC_except_table413
+ GCC_except_table416
+ _CTSimLocationAsString
+ _OBJC_IVAR_$_CTCellularPlanItem._carrierAppAdamId
+ _OBJC_IVAR_$_CTCellularPlanItem._qsLifecycleState
+ _OBJC_IVAR_$_CTCellularPlanItem._qsRole
+ _OBJC_IVAR_$_CTCellularPlanItem._simLocation
+ ___100-[CTCellularPlanManager addNewPlanWithCardData:confirmationCode:triggerType:userConsent:completion:]_block_invoke.229
+ ___100-[CTCellularPlanManager addNewPlanWithCardData:confirmationCode:triggerType:userConsent:completion:]_block_invoke_2.230
+ ___114-[CTCellularPlanManager addNewPlanWithAddress:matchingId:oid:confirmationCode:triggerType:userConsent:completion:]_block_invoke.233
+ ___114-[CTCellularPlanManager addNewPlanWithAddress:matchingId:oid:confirmationCode:triggerType:userConsent:completion:]_block_invoke_2.234
+ ___124-[CTCellularPlanManager addNewRemotePlanWithCardData:confirmationCode:isPairing:withCSN:withContext:userConsent:completion:]_block_invoke.323
+ ___124-[CTCellularPlanManager addNewRemotePlanWithCardData:confirmationCode:isPairing:withCSN:withContext:userConsent:completion:]_block_invoke_2.324
+ ___138-[CTCellularPlanManager addNewRemotePlanWithAddress:matchingId:oid:confirmationCode:isPairing:withCSN:withContext:userConsent:completion:]_block_invoke.325
+ ___138-[CTCellularPlanManager addNewRemotePlanWithAddress:matchingId:oid:confirmationCode:isPairing:withCSN:withContext:userConsent:completion:]_block_invoke_2.326
+ ___39-[CTCellularPlanManager eraseAllPlans:]_block_invoke.298
+ ___39-[CTCellularPlanManager eraseAllPlans:]_block_invoke.299
+ ___39-[CTCellularPlanManager getIMEIPrefix:]_block_invoke.239
+ ___39-[CTCellularPlanManager getIMEIPrefix:]_block_invoke_2.240
+ ___39-[CTCellularPlanManager getRemoteInfo:]_block_invoke.351
+ ___39-[CTCellularPlanManager getRemoteInfo:]_block_invoke.353
+ ___39-[CTCellularPlanManager getRemoteInfo:]_block_invoke_2.352
+ ___39-[CTCellularPlanManager setMcc:andMnc:]_block_invoke
+ ___39-[CTCellularPlanManager setMcc:andMnc:]_block_invoke_2
+ ___40-[CTCellularPlanManager getSelectedEnv:]_block_invoke.244
+ ___40-[CTCellularPlanManager getSelectedEnv:]_block_invoke_2.245
+ ___40-[CTCellularPlanManager mccMncOverride:]_block_invoke.255
+ ___40-[CTCellularPlanManager mccMncOverride:]_block_invoke_2.256
+ ___40-[CTCellularPlanManager mccMncOverride:]_block_invoke_3
+ ___42-[CTCellularPlanManager getSelectedProxy:]_block_invoke.249
+ ___42-[CTCellularPlanManager getSelectedProxy:]_block_invoke_2.250
+ ___45-[CTCellularPlanManager shouldShowPlanSetup:]_block_invoke.217
+ ___45-[CTCellularPlanManager shouldShowPlanSetup:]_block_invoke_2.218
+ ___47-[CTCellularPlanManager getSupportedFlowTypes:]_block_invoke.220
+ ___47-[CTCellularPlanManager getSupportedFlowTypes:]_block_invoke_2.221
+ ___49-[CTCellularPlanManager getPlansPendingTransfer:]_block_invoke.274
+ ___49-[CTCellularPlanManager planItemsWithCompletion:]_block_invoke.265
+ ___49-[CTCellularPlanManager planItemsWithCompletion:]_block_invoke.266
+ ___50-[CTCellularPlanManager setLatitude:andLongitude:]_block_invoke
+ ___50-[CTCellularPlanManager setLatitude:andLongitude:]_block_invoke_2
+ ___51-[CTCellularPlanManager latitudeLongitudeOverride:]_block_invoke.260
+ ___51-[CTCellularPlanManager latitudeLongitudeOverride:]_block_invoke_2.261
+ ___51-[CTCellularPlanManager latitudeLongitudeOverride:]_block_invoke_3
+ ___52-[CTCellularPlanManager resolveSimLabel:completion:]_block_invoke.281
+ ___53-[CTCellularPlanManager remapSimLabel:to:completion:]_block_invoke.282
+ ___54-[CTCellularPlanManager didDeletePlanItem:completion:]_block_invoke.296
+ ___54-[CTCellularPlanManager didDeletePlanItem:completion:]_block_invoke.297
+ ___55-[CTCellularPlanManager showUiIgnoringActivationFlags:]_block_invoke
+ ___55-[CTCellularPlanManager showUiIgnoringActivationFlags:]_block_invoke_2
+ ___57-[CTCellularPlanManager didSelectPlanForData:completion:]_block_invoke.288
+ ___57-[CTCellularPlanManager didSelectPlanForData:completion:]_block_invoke.289
+ ___57-[CTCellularPlanManager startProvisioningWithCompletion:]_block_invoke.225
+ ___57-[CTCellularPlanManager startProvisioningWithCompletion:]_block_invoke_2.226
+ ___58-[CTCellularPlanManager finishProvisioningWithCompletion:]_block_invoke.227
+ ___58-[CTCellularPlanManager finishProvisioningWithCompletion:]_block_invoke_2.228
+ ___59-[CTCellularPlanManager addNewPlanWithFlowType:completion:]_block_invoke.231
+ ___59-[CTCellularPlanManager addNewPlanWithFlowType:completion:]_block_invoke_2.232
+ ___59-[CTCellularPlanManager eraseAllRemotePlansWithCompletion:]_block_invoke.363
+ ___59-[CTCellularPlanManager eraseAllRemotePlansWithCompletion:]_block_invoke.364
+ ___60-[CTCellularPlanManager didDeleteRemotePlanItem:completion:]_block_invoke.329
+ ___60-[CTCellularPlanManager didDeleteRemotePlanItem:completion:]_block_invoke.330
+ ___60-[CTCellularPlanManager didSelectRemotePlanItem:completion:]_block_invoke.327
+ ___60-[CTCellularPlanManager didSelectRemotePlanItem:completion:]_block_invoke.328
+ ___61-[CTCellularPlanManager carrierItemsShouldUpdate:completion:]_block_invoke.283
+ ___61-[CTCellularPlanManager carrierItemsShouldUpdate:completion:]_block_invoke.284
+ ___61-[CTCellularPlanManager installPendingRemotePlan:completion:]_block_invoke.235
+ ___61-[CTCellularPlanManager installPendingRemotePlan:completion:]_block_invoke_2.236
+ ___62-[CTCellularPlanManager deletePlanPendingTransfer:completion:]_block_invoke.279
+ ___62-[CTCellularPlanManager deletePlanPendingTransfer:completion:]_block_invoke_2.280
+ ___62-[CTCellularPlanManager didSelectPlansForIMessage:completion:]_block_invoke.292
+ ___62-[CTCellularPlanManager didSelectPlansForIMessage:completion:]_block_invoke.293
+ ___63-[CTCellularPlanManager didSelectPlanItem:isEnable:completion:]_block_invoke.285
+ ___63-[CTCellularPlanManager didSelectPlanItem:isEnable:completion:]_block_invoke.286
+ ___63-[CTCellularPlanManager getPlansPendingTransferForTestability:]_block_invoke.275
+ ___63-[CTCellularPlanManager manageAccountForRemotePlan:completion:]_block_invoke.319
+ ___63-[CTCellularPlanManager manageAccountForRemotePlan:completion:]_block_invoke_2.320
+ ___64-[CTCellularPlanManager activatePlanPendingTransfer:completion:]_block_invoke.276
+ ___64-[CTCellularPlanManager activatePlanPendingTransfer:completion:]_block_invoke_2.277
+ ___65-[CTCellularPlanManager didSelectPlanForDefaultVoice:completion:]_block_invoke.290
+ ___65-[CTCellularPlanManager didSelectPlanForDefaultVoice:completion:]_block_invoke.291
+ ___66-[CTCellularPlanManager danglingPlanItemsShouldUpdate:completion:]_block_invoke.270
+ ___66-[CTCellularPlanManager danglingPlanItemsShouldUpdate:completion:]_block_invoke.271
+ ___66-[CTCellularPlanManager startRemoteProvisioningForCSN:completion:]_block_invoke.315
+ ___66-[CTCellularPlanManager startRemoteProvisioningForCSN:completion:]_block_invoke_2.316
+ ___67-[CTCellularPlanManager finishRemoteProvisioningForCSN:completion:]_block_invoke.317
+ ___67-[CTCellularPlanManager finishRemoteProvisioningForCSN:completion:]_block_invoke_2.318
+ ___67-[CTCellularPlanManager isRemotePlanCapableWithContext:completion:]_block_invoke.310
+ ___67-[CTCellularPlanManager isRemotePlanCapableWithContext:completion:]_block_invoke_2.311
+ ___71-[CTCellularPlanManager resumePlanProvisioning:userConsent:completion:]_block_invoke.237
+ ___71-[CTCellularPlanManager resumePlanProvisioning:userConsent:completion:]_block_invoke_2.238
+ ___74-[CTCellularPlanManager shouldShowAddNewRemotePlanWithContext:completion:]_block_invoke.312
+ ___74-[CTCellularPlanManager shouldShowAddNewRemotePlanWithContext:completion:]_block_invoke_2.313
+ ___85-[CTCellularPlanManager addNewRemotePlan:withCSN:withContext:userConsent:completion:]_block_invoke.321
+ ___85-[CTCellularPlanManager addNewRemotePlan:withCSN:withContext:userConsent:completion:]_block_invoke_2.322
+ ___93-[CTCellularPlanManager didTransferPlanForCsn:iccid:srcIccid:profileServer:matchingId:state:]_block_invoke
+ ___93-[CTCellularPlanManager didTransferPlanForCsn:iccid:srcIccid:profileServer:matchingId:state:]_block_invoke_2
+ ___98-[CTCellularPlanManager didPurchaseRemotePlanForEid:imei:meid:iccid:alternateSmdpFqdn:completion:]_block_invoke.355
+ ___98-[CTCellularPlanManager didPurchaseRemotePlanForEid:imei:meid:iccid:alternateSmdpFqdn:completion:]_block_invoke_2.356
+ ___block_descriptor_40_e8_32b_e11_v24?0d8d16ls32l8
+ ___block_descriptor_40_e8_32b_e11_v24?0q8q16ls32l8
+ ___block_descriptor_56_e8_32b_e5_v8?0ls32l8
+ ___block_descriptor_56_e8_32o40o48o_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32o_e5_v8?0ls32l8
+ ___block_descriptor_88_e8_32o40o48o56o64o72o80o_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8
+ ___block_literal_global.224
+ ___block_literal_global.243
+ ___block_literal_global.248
+ ___block_literal_global.252
+ ___block_literal_global.254
+ ___block_literal_global.259
+ ___block_literal_global.264
+ ___block_literal_global.269
+ ___block_literal_global.273
+ ___block_literal_global.295
+ ___block_literal_global.301
+ ___block_literal_global.303
+ ___block_literal_global.305
+ ___block_literal_global.307
+ ___block_literal_global.309
+ ___block_literal_global.332
+ ___block_literal_global.334
+ ___block_literal_global.336
+ ___block_literal_global.338
+ ___block_literal_global.340
+ ___block_literal_global.342
+ ___block_literal_global.344
+ ___block_literal_global.346
+ ___block_literal_global.348
+ ___block_literal_global.350
+ ___block_literal_global.360
+ ___block_literal_global.362
+ ___block_literal_global.366
+ ___block_literal_global.368
+ ___block_literal_global.371
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$didTransferPlanForCsn:iccid:srcIccid:profileServer:matchingId:state:
+ _objc_msgSend$latitudeLongitudeOverride:
+ _objc_msgSend$mccMncOverride:
+ _objc_msgSend$setLatitude:andLongitude:
+ _objc_msgSend$setMcc:andMnc:
+ _objc_msgSend$setQsLifecycleState:
+ _objc_msgSend$setQsRole:
+ _objc_msgSend$setSimLocation:
+ _objc_msgSend$showUiIgnoringActivationFlags:
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x3
+ _objc_retain_x8
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
- GCC_except_table400
- GCC_except_table403
- _OUTLINED_FUNCTION_2
- _OUTLINED_FUNCTION_3
- ___100-[CTCellularPlanManager addNewPlanWithCardData:confirmationCode:triggerType:userConsent:completion:]_block_invoke.228
- ___100-[CTCellularPlanManager addNewPlanWithCardData:confirmationCode:triggerType:userConsent:completion:]_block_invoke_2.229
- ___114-[CTCellularPlanManager addNewPlanWithAddress:matchingId:oid:confirmationCode:triggerType:userConsent:completion:]_block_invoke.232
- ___114-[CTCellularPlanManager addNewPlanWithAddress:matchingId:oid:confirmationCode:triggerType:userConsent:completion:]_block_invoke_2.233
- ___124-[CTCellularPlanManager addNewRemotePlanWithCardData:confirmationCode:isPairing:withCSN:withContext:userConsent:completion:]_block_invoke.310
- ___124-[CTCellularPlanManager addNewRemotePlanWithCardData:confirmationCode:isPairing:withCSN:withContext:userConsent:completion:]_block_invoke_2.311
- ___138-[CTCellularPlanManager addNewRemotePlanWithAddress:matchingId:oid:confirmationCode:isPairing:withCSN:withContext:userConsent:completion:]_block_invoke.312
- ___138-[CTCellularPlanManager addNewRemotePlanWithAddress:matchingId:oid:confirmationCode:isPairing:withCSN:withContext:userConsent:completion:]_block_invoke_2.313
- ___39-[CTCellularPlanManager eraseAllPlans:]_block_invoke.285
- ___39-[CTCellularPlanManager eraseAllPlans:]_block_invoke.286
- ___39-[CTCellularPlanManager getIMEIPrefix:]_block_invoke.238
- ___39-[CTCellularPlanManager getIMEIPrefix:]_block_invoke_2.239
- ___39-[CTCellularPlanManager getRemoteInfo:]_block_invoke.338
- ___39-[CTCellularPlanManager getRemoteInfo:]_block_invoke.340
- ___39-[CTCellularPlanManager getRemoteInfo:]_block_invoke_2.339
- ___40-[CTCellularPlanManager getSelectedEnv:]_block_invoke.243
- ___40-[CTCellularPlanManager getSelectedEnv:]_block_invoke_2.244
- ___42-[CTCellularPlanManager getSelectedProxy:]_block_invoke.248
- ___42-[CTCellularPlanManager getSelectedProxy:]_block_invoke_2.249
- ___45-[CTCellularPlanManager shouldShowPlanSetup:]_block_invoke.216
- ___45-[CTCellularPlanManager shouldShowPlanSetup:]_block_invoke_2.217
- ___47-[CTCellularPlanManager getSupportedFlowTypes:]_block_invoke.219
- ___47-[CTCellularPlanManager getSupportedFlowTypes:]_block_invoke_2.220
- ___49-[CTCellularPlanManager getPlansPendingTransfer:]_block_invoke.261
- ___49-[CTCellularPlanManager planItemsWithCompletion:]_block_invoke.252
- ___49-[CTCellularPlanManager planItemsWithCompletion:]_block_invoke.253
- ___52-[CTCellularPlanManager resolveSimLabel:completion:]_block_invoke.268
- ___53-[CTCellularPlanManager remapSimLabel:to:completion:]_block_invoke.269
- ___54-[CTCellularPlanManager didDeletePlanItem:completion:]_block_invoke.283
- ___54-[CTCellularPlanManager didDeletePlanItem:completion:]_block_invoke.284
- ___57-[CTCellularPlanManager didSelectPlanForData:completion:]_block_invoke.275
- ___57-[CTCellularPlanManager didSelectPlanForData:completion:]_block_invoke.276
- ___57-[CTCellularPlanManager startProvisioningWithCompletion:]_block_invoke.224
- ___57-[CTCellularPlanManager startProvisioningWithCompletion:]_block_invoke_2.225
- ___58-[CTCellularPlanManager finishProvisioningWithCompletion:]_block_invoke.226
- ___58-[CTCellularPlanManager finishProvisioningWithCompletion:]_block_invoke_2.227
- ___59-[CTCellularPlanManager addNewPlanWithFlowType:completion:]_block_invoke.230
- ___59-[CTCellularPlanManager addNewPlanWithFlowType:completion:]_block_invoke_2.231
- ___59-[CTCellularPlanManager eraseAllRemotePlansWithCompletion:]_block_invoke.350
- ___59-[CTCellularPlanManager eraseAllRemotePlansWithCompletion:]_block_invoke.351
- ___60-[CTCellularPlanManager didDeleteRemotePlanItem:completion:]_block_invoke.316
- ___60-[CTCellularPlanManager didDeleteRemotePlanItem:completion:]_block_invoke.317
- ___60-[CTCellularPlanManager didSelectRemotePlanItem:completion:]_block_invoke.314
- ___60-[CTCellularPlanManager didSelectRemotePlanItem:completion:]_block_invoke.315
- ___61-[CTCellularPlanManager carrierItemsShouldUpdate:completion:]_block_invoke.270
- ___61-[CTCellularPlanManager carrierItemsShouldUpdate:completion:]_block_invoke.271
- ___61-[CTCellularPlanManager installPendingRemotePlan:completion:]_block_invoke.234
- ___61-[CTCellularPlanManager installPendingRemotePlan:completion:]_block_invoke_2.235
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
- ___71-[CTCellularPlanManager resumePlanProvisioning:userConsent:completion:]_block_invoke.236
- ___71-[CTCellularPlanManager resumePlanProvisioning:userConsent:completion:]_block_invoke_2.237
- ___74-[CTCellularPlanManager shouldShowAddNewRemotePlanWithContext:completion:]_block_invoke.299
- ___74-[CTCellularPlanManager shouldShowAddNewRemotePlanWithContext:completion:]_block_invoke_2.300
- ___82-[CTCellularPlanManager didTransferPlanForCsn:iccid:srcIccid:profileServer:state:]_block_invoke
- ___82-[CTCellularPlanManager didTransferPlanForCsn:iccid:srcIccid:profileServer:state:]_block_invoke_2
- ___85-[CTCellularPlanManager addNewRemotePlan:withCSN:withContext:userConsent:completion:]_block_invoke.308
- ___85-[CTCellularPlanManager addNewRemotePlan:withCSN:withContext:userConsent:completion:]_block_invoke_2.309
- ___98-[CTCellularPlanManager didPurchaseRemotePlanForEid:imei:meid:iccid:alternateSmdpFqdn:completion:]_block_invoke.342
- ___98-[CTCellularPlanManager didPurchaseRemotePlanForEid:imei:meid:iccid:alternateSmdpFqdn:completion:]_block_invoke_2.343
- ___block_literal_global.223
- ___block_literal_global.242
- ___block_literal_global.247
- ___block_literal_global.251
- ___block_literal_global.256
- ___block_literal_global.260
- ___block_literal_global.282
- ___block_literal_global.288
- ___block_literal_global.290
- ___block_literal_global.292
- ___block_literal_global.294
- ___block_literal_global.296
- ___block_literal_global.319
- ___block_literal_global.321
- ___block_literal_global.323
- ___block_literal_global.325
- ___block_literal_global.327
- ___block_literal_global.329
- ___block_literal_global.331
- ___block_literal_global.333
- ___block_literal_global.335
- ___block_literal_global.337
- ___block_literal_global.345
- ___block_literal_global.347
- ___block_literal_global.349
- ___block_literal_global.353
- ___block_literal_global.355
- _objc_msgSend$didTransferPlanForCsn:iccid:srcIccid:profileServer:state:
- _objc_retainAutoreleasedReturnValue
CStrings:
+ "-[CTCellularPlanManager didTransferPlanForCsn:iccid:srcIccid:profileServer:matchingId:state:]"
+ "<item: uuid:%@ iccid:%@ name:%@, CTPlan: %@, type:%@, simLocation:%s, validstate:%d, selected:%@, selectable:%d, activeData:%d, defaultVoice:%d, slotUuid:%@, labelId:%@, number:%@, label:%@ carrier:%@, plan:%@, isLocalTransferToeSIMSupported:%s, isTransferred:%s, trialExp:%@ isCheckingCellularConnectivity:%s, transferredStatus:%@, transferredToDeviceDisplayName:%@, supportedTransferOption:%lu, settingsMode:%@>"
+ "Primary subscription unavailable."
+ "carrierAppAdamId"
+ "qsLifecycleState"
+ "qsRole"
+ "simLocation"
+ "unable to get mcc/mnc overrides %@"
+ "unable to set lat/long %@"
+ "unable to set mcc/mnc %@"
+ "unable to set show Ui ignoring activation flags %@"
+ "v24@?0d8d16"
+ "v24@?0q8q16"
- "#16@0:8"
- "-[CTCellularPlanManager didTransferPlanForCsn:iccid:srcIccid:profileServer:state:]"
- ".cxx_destruct"
- "<item: uuid:%@ iccid:%@ name:%@, CTPlan: %@, type:%@, validstate:%d, selected:%@, selectable:%d, activeData:%d, defaultVoice:%d, slotUuid:%@, labelId:%@, number:%@, label:%@ carrier:%@, plan:%@, isLocalTransferToeSIMSupported:%s, isTransferred:%s, trialExp:%@ isCheckingCellularConnectivity:%s, transferredStatus:%@, transferredToDeviceDisplayName:%@, supportedTransferOption:%lu, settingsMode:%@>"
- "@\"CTCellularPlan\""
- "@\"CTCellularPlanManagerDelegate\""
- "@\"CTCellularPlanProfile\""
- "@\"CTCellularPlanSubscription\""
- "@\"CTPlan\""
- "@\"CTUserLabel\""
- "@\"NSArray\""
- "@\"NSData\""
- "@\"NSNumber\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSUUID\""
- "@\"NSXPCConnection\""
- "@104@0:8@16@24@32@40@48@56B64B68q72@80Q88q96"
- "@108@0:8@16i24B28d32d40@48i56@60i68i72@76d84@92@100"
- "@120@0:8@16@24@32@40q48@56@64@72B80B84q88@96Q104q112"
- "@16@0:8"
- "@20@0:8B16"
- "@24@0:8:16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@24@0:8@?16"
- "@24@0:8^@16"
- "@24@0:8^{_NSZone=}16"
- "@24@0:8q16"
- "@28@0:8@16B24"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@32@0:8q16@24"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@32"
- "@40@0:8@16d24d32"
- "@52@0:8@16@24@32@40B48"
- "@52@0:8@16@24B32B36B40B44B48"
- "@68@0:8@16@24@32B40@44@52@60"
- "@96@0:8@16@24q32@40@48@56q64@72Q80q88"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B32@0:8@16^d24"
- "CTCellularPlan"
- "CTCellularPlanArrayValidator"
- "CTCellularPlanBoolValidator"
- "CTCellularPlanCarrierItem"
- "CTCellularPlanClient"
- "CTCellularPlanClientDelegate"
- "CTCellularPlanDataValidator"
- "CTCellularPlanDateParser"
- "CTCellularPlanDictionaryValidator"
- "CTCellularPlanItem"
- "CTCellularPlanManager"
- "CTCellularPlanManagerDelegate"
- "CTCellularPlanNumberValidator"
- "CTCellularPlanPendingTransfer"
- "CTCellularPlanProfile"
- "CTCellularPlanStringValidator"
- "CTCellularPlanSubscription"
- "CTCellularPlanSubscriptionDataUsage"
- "CTCellularPlanValidating"
- "CTDanglingPlanItem"
- "CTUserLabel"
- "NSCoding"
- "NSCopying"
- "NSObject"
- "NSSecureCoding"
- "Q"
- "Q16@0:8"
- "Q24@0:8^@16"
- "T#,R"
- "T@\"CTCellularPlan\",R,N,V_plan"
- "T@\"CTCellularPlanProfile\",&,N,V_profile"
- "T@\"CTCellularPlanSubscription\",&,N,V_subscription"
- "T@\"CTPlan\",R,N,V_ctPlan"
- "T@\"CTPlan\",R,N,V_plan"
- "T@\"CTUserLabel\",&,N,V_planLabel"
- "T@\"CTUserLabel\",&,N,V_userLabel"
- "T@\"NSArray\",R,N"
- "T@\"NSArray\",R,N,V_dataUsage"
- "T@\"NSArray\",R,N,V_homeCountryList"
- "T@\"NSData\",C,N,V_profileId"
- "T@\"NSData\",R,N"
- "T@\"NSNumber\",&,N,V_isSelectedOverride"
- "T@\"NSNumber\",&,N,V_subscriptionStatusOverride"
- "T@\"NSNumber\",&,N,V_trialExpirationDate"
- "T@\"NSString\",&,N,V_cachedPhoneNumber"
- "T@\"NSString\",&,N,V_carrierName"
- "T@\"NSString\",&,N,V_countryCode"
- "T@\"NSString\",&,N,V_deviceName"
- "T@\"NSString\",&,N,V_iccid"
- "T@\"NSString\",&,N,V_label"
- "T@\"NSString\",&,N,V_phoneNumber"
- "T@\"NSString\",&,N,V_simLabelID"
- "T@\"NSString\",&,N,V_sourceIccid"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",C,N,V_companionSimLabelId"
- "T@\"NSString\",C,N,V_iccid"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,N"
- "T@\"NSString\",R,N,V_accountURL"
- "T@\"NSString\",R,N,V_dataCategory"
- "T@\"NSString\",R,N,V_iccid"
- "T@\"NSString\",R,N,V_key"
- "T@\"NSString\",R,N,V_label"
- "T@\"NSString\",R,N,V_labelId"
- "T@\"NSString\",R,N,V_name"
- "T@\"NSString\",R,N,V_planDescription"
- "T@\"NSString\",R,N,V_planPurchaseEndpointType"
- "T@\"NSString\",R,N,V_purchaseOption"
- "T@\"NSString\",R,N,V_transferredToDeviceDisplayName"
- "T@\"NSString\",R,N,V_uuid"
- "T@\"NSString\",R,N,V_warningText"
- "T@\"NSString\",R,N,V_websheetURL"
- "T@\"NSUUID\",C,N,V_companionSlotUuid"
- "TB,N,V_isActiveDataPlan"
- "TB,N,V_isBootstrap"
- "TB,N,V_isDefaultVoice"
- "TB,N,V_isDeleteNotAllowed"
- "TB,N,V_isDisableNotAllowed"
- "TB,N,V_isHomePlan"
- "TB,N,V_isLocalTransferToeSIMSupported"
- "TB,N,V_isPrivateNetworkSim"
- "TB,N,V_isSelectable"
- "TB,N,V_isSelected"
- "TB,N,V_isSimStateValid"
- "TB,N,V_isTransferred"
- "TB,N,V_requiresUserConsent"
- "TB,N,V_shouldAppearDisabled"
- "TB,N,V_shouldAutoSelectWhenInRange"
- "TB,N,V_shouldDisplay"
- "TB,N,V_shouldDisplayExtendedConsentInfo"
- "TB,N,V_shouldDisplayType"
- "TB,R"
- "TB,R,N"
- "TB,R,N,V_applePaySupported"
- "TB,R,N,V_autoRenew"
- "TQ,N,V_supportedTransferOption"
- "TQ,R"
- "Td,R,N"
- "Td,R,N,V_billingEndDate"
- "Td,R,N,V_billingStartDate"
- "Td,R,N,V_dataCapacity"
- "Td,R,N,V_dataUsed"
- "Td,R,N,V_timestamp"
- "Ti,N,V_planStatus"
- "Ti,N,V_status"
- "Ti,N,V_subscriptionResult"
- "Ti,R,N"
- "Ti,R,N,V_accountStatus"
- "Ti,R,N,V_planType"
- "Tq,N,V_lockState"
- "Tq,N,V_settingsMode"
- "Tq,N,V_status"
- "Tq,N,V_type"
- "Tq,R,N,V_transferredStatus"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "^{dispatch_queue_s=}"
- "_accountStatus"
- "_accountURL"
- "_addOnEndpointType"
- "_addOnWebsheetURL"
- "_applePaySupported"
- "_autoRenew"
- "_billingEndDate"
- "_billingStartDate"
- "_cachedPhoneNumber"
- "_carrierName"
- "_companionSimLabelId"
- "_companionSlotUuid"
- "_connect_sync"
- "_connection"
- "_countryCode"
- "_ctPlan"
- "_dataCapacity"
- "_dataCategory"
- "_dataUsage"
- "_dataUsed"
- "_delegate"
- "_deviceName"
- "_ensureConnected_sync"
- "_homeCountryList"
- "_iccid"
- "_isActiveDataPlan"
- "_isBootstrap"
- "_isDefaultVoice"
- "_isDeleteNotAllowed"
- "_isDisableNotAllowed"
- "_isHomePlan"
- "_isLocalTransferToeSIMSupported"
- "_isPrivateNetworkSim"
- "_isSelectable"
- "_isSelected"
- "_isSelectedOverride"
- "_isSimStateValid"
- "_isTransferred"
- "_key"
- "_label"
- "_labelId"
- "_labelKeyDescription"
- "_lockState"
- "_name"
- "_phoneNumber"
- "_plan"
- "_planDescription"
- "_planLabel"
- "_planPurchaseEndpointType"
- "_planStatus"
- "_planType"
- "_profile"
- "_profileId"
- "_purchaseOption"
- "_queue"
- "_reconnect"
- "_requiresUserConsent"
- "_setQueue:"
- "_settingsMode"
- "_shouldAppearDisabled"
- "_shouldAutoSelectWhenInRange"
- "_shouldDisplay"
- "_shouldDisplayExtendedConsentInfo"
- "_shouldDisplayType"
- "_simLabelID"
- "_sourceIccid"
- "_status"
- "_subscription"
- "_subscriptionResult"
- "_subscriptionStatusOverride"
- "_supportedTransferOption"
- "_timestamp"
- "_transferredStatus"
- "_transferredToDeviceDisplayName"
- "_trialExpirationDate"
- "_type"
- "_userLabel"
- "_uuid"
- "_warningText"
- "_websheetURL"
- "activatePlanPendingTransfer:completion:"
- "addNewPlanWithAddress:matchingId:oid:confirmationCode:triggerType:userConsent:completion:"
- "addNewPlanWithCardData:confirmationCode:triggerType:userConsent:completion:"
- "addNewPlanWithFlowType:completion:"
- "addNewRemotePlan:withCSN:withContext:userConsent:completion:"
- "addNewRemotePlanWithAddress:matchingId:oid:confirmationCode:isPairing:withCSN:withContext:userConsent:completion:"
- "addNewRemotePlanWithCardData:confirmationCode:isPairing:withCSN:withContext:userConsent:completion:"
- "allocWithZone:"
- "appendFormat:"
- "appendString:"
- "applePaySupported"
- "autorelease"
- "boolValue"
- "calculateInstallConsentTextTypeFor:"
- "cancelPlanActivation:"
- "cancelPlanActivation:completion:"
- "carrierInfoDidUpdate"
- "carrierItemsShouldUpdate:completion:"
- "class"
- "compare:"
- "compare:options:"
- "conformsToProtocol:"
- "copy"
- "copyWithZone:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "ctPlan"
- "customDescription"
- "d"
- "d16@0:8"
- "danglingPlanItemsShouldUpdate:"
- "danglingPlanItemsShouldUpdate:completion:"
- "dateFromString:"
- "dealloc"
- "debugDescription"
- "decodeBoolForKey:"
- "decodeIntForKey:"
- "decodeIntegerForKey:"
- "decodeObjectOfClass:forKey:"
- "decodeObjectOfClasses:forKey:"
- "defaultCenter"
- "deleteAllRemoteProfiles"
- "deletePlanPendingTransfer:completion:"
- "deleteRemoteProfile:"
- "description"
- "dictionaryWithObjects:forKeys:count:"
- "didCancelRemotePlan"
- "didDeletePlanItem:completion:"
- "didDeleteRemotePlanItem:completion:"
- "didEnablePlanItems:"
- "didEnablePlanItems:completion:"
- "didEnablePlanItemsForTravel:"
- "didEnablePlanItemsForTravel:completion:"
- "didPurchasePlanForCarrier:mnc:gid1:gid2:state:"
- "didPurchasePlanForCsn:iccid:profileServer:state:"
- "didPurchasePlanWithIccid:downloadProfile:"
- "didPurchaseRemotePlanForEid:imei:meid:iccid:alternateSmdpFqdn:completion:"
- "didSelectPlanForData:"
- "didSelectPlanForData:completion:"
- "didSelectPlanForDefaultVoice:"
- "didSelectPlanForDefaultVoice:completion:"
- "didSelectPlanItem:enable:completion:"
- "didSelectPlanItem:isEnable:"
- "didSelectPlanItem:isEnable:completion:"
- "didSelectPlansForIMessage:completion:"
- "didSelectRemotePlanItem:completion:"
- "didTransferPlanForCsn:iccid:srcIccid:profileServer:state:"
- "doubleValue"
- "encodeBool:forKey:"
- "encodeInt:forKey:"
- "encodeInteger:forKey:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "enterSimSetupWithCompletion:"
- "eraseAllPlans:"
- "eraseAllPlansWithCompletion:"
- "eraseAllRemotePlansWithCSN:completion:"
- "eraseAllRemotePlansWithCompletion:"
- "errorForCode:"
- "errorForCode:withDescription:"
- "errorWithDomain:code:userInfo:"
- "exitSimSetupWithCompletion:"
- "expirePlan"
- "fetchRemoteProfiles:"
- "finishProvisioningWithCompletion:"
- "finishRemoteProvisioningForCSN:completion:"
- "finishRemoteProvisioningWithCompletion:"
- "getAutoPlanSelectionWithCompletion:"
- "getIMEIPrefix:"
- "getPlansPendingTransfer:"
- "getPlansPendingTransferForTestability:"
- "getPlansPendingTransferForTestabilityWithCompletion:"
- "getPlansPendingTransferWithCompletion:"
- "getPredefinedLabels"
- "getPredefinedLabels:"
- "getRemoteInfo:"
- "getRoamingSignupOverrideWithCompletion:"
- "getSelectedEnv:"
- "getSelectedProxy:"
- "getShortLabelsForLabels:"
- "getShortLabelsForLabels:completion:"
- "getSkipEligibilityCheck:"
- "getSubscriptionContextUUIDforPlan:"
- "getSubscriptionContextUUIDforPlan:completion:"
- "getSupportedFlowTypes"
- "getSupportedFlowTypes:"
- "getSupportedFlowTypesWithError:"
- "hash"
- "homeCountryList"
- "i"
- "i16@0:8"
- "identifier"
- "indexInPredefinedLabels:"
- "init"
- "initWithCategory:andDataUsed:andDataCapacity:"
- "initWithCellularPlan:uuid:iccid:name:type:phoneNumber:cachedPhoneNumber:label:isLocalTransferToeSIMSupported:isTransferred:transferredStatus:transferredToDeviceDisplayName:supportedTransferOption:settingsMode:"
- "initWithCellularPlan:uuid:type:phoneNumber:cachedPhoneNumber:label:transferredStatus:transferredToDeviceDisplayName:supportedTransferOption:settingsMode:"
- "initWithCoder:"
- "initWithIccid:"
- "initWithIccid:phoneNumber:label:labelID:isPrivateNetworkSim:"
- "initWithIccid:subscriptionResult:autoRenew:billingStartDate:billingEndDate:carrierName:planType:planDescription:planStatus:accountStatus:accountURL:timestamp:homeCountryList:dataUsage:"
- "initWithIccid:uuid:name:phoneNumber:cachedPhoneNumber:label:isLocalTransferToeSIMSupported:isTransferred:transferredStatus:transferredToDeviceDisplayName:supportedTransferOption:settingsMode:"
- "initWithKey:label:labelId:"
- "initWithLabel:"
- "initWithLocaleIdentifier:"
- "initWithMachServiceName:options:"
- "initWithName:plan:url:applePaySupported:responseType:warningText:purchaseOption:"
- "initWithProfile:subscription:"
- "initWithProfileId:iccid:selected:bootstrap:disableNotAllowed:deleteNotAllowed:requiresUserConsent:"
- "installPendingRemotePlan:completion:"
- "intValue"
- "interfaceWithProtocol:"
- "invalidate"
- "isBackedByCellularPlan"
- "isEqual:"
- "isEqualOrNewerThanSubscription:"
- "isEqualToString:"
- "isHomePlan"
- "isInstalling"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "isRemotePlanCapableWithContext:completion:"
- "isSimStateValid"
- "key"
- "labelId"
- "latitudeLongitudeOverride:"
- "length"
- "localPlanInfoDidUpdate:"
- "manageAccountForRemotePlan:completion:"
- "mccMncOverride:"
- "numberWithBool:"
- "numberWithDouble:"
- "numberWithInt:"
- "objectAtIndexedSubscript:"
- "pendingReleaseRemotePlan"
- "pendingTransferPlanInfoDidUpdate"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "ping"
- "planDescriptionCompare:"
- "planInfoDidUpdate"
- "planItemsShouldUpdate:"
- "planItemsShouldUpdate:completion:"
- "planItemsWithCompletion:"
- "planLabel"
- "planPurchaseEndpointType"
- "postNotificationName:object:userInfo:"
- "q"
- "q16@0:8"
- "q24@0:8@16"
- "redactedDescription"
- "release"
- "remapSimLabel:to:"
- "remapSimLabel:to:completion:"
- "remoteObjectInterface"
- "remoteObjectProxy"
- "remoteObjectProxyWithErrorHandler:"
- "remotePlanItemsWithCompletion:"
- "remotePlanItemsWithUpdateFetch:completion:"
- "remotePlanItemsWithUpdateFetch:withCSN:completion:"
- "remoteProvisioningDidBecomeAvailable"
- "remoteUserDidProvideResponse:confirmationCode:plan:completion:"
- "resolveSimLabel:"
- "resolveSimLabel:completion:"
- "respondsToSelector:"
- "resume"
- "resumePlanProvisioning:userConsent:completion:"
- "retain"
- "retainCount"
- "selectRemoteProfile:"
- "self"
- "setAutoPlanSelection:"
- "setCachedPhoneNumber:"
- "setCarrierName:"
- "setClasses:forSelector:argumentIndex:ofReply:"
- "setCompanionSimLabelId:"
- "setCompanionSlotUuid:"
- "setCountryCode:"
- "setDateFormat:"
- "setDeviceName:"
- "setExportedInterface:"
- "setExportedObject:"
- "setIMEIPrefix:"
- "setIccid:"
- "setInvalidationHandler:"
- "setIsActiveDataPlan:"
- "setIsBootstrap:"
- "setIsDefaultVoice:"
- "setIsDeleteNotAllowed:"
- "setIsDisableNotAllowed:"
- "setIsHomePlan:"
- "setIsLocalTransferToeSIMSupported:"
- "setIsPrivateNetworkSim:"
- "setIsSelectable:"
- "setIsSelected:"
- "setIsSelectedOverride:"
- "setIsSimStateValid:"
- "setIsTransferred:"
- "setLabel:"
- "setLabelForPlan:label:"
- "setLabelForPlan:label:completion:"
- "setLatitude:andLongitude:"
- "setLocale:"
- "setLockState:"
- "setMcc:andMnc:"
- "setPhoneNumber:"
- "setPlanLabel:"
- "setPlanStatus:"
- "setProfile:"
- "setProfileId:"
- "setRemoteObjectInterface:"
- "setRequiresUserConsent:"
- "setRoamingSignupOverride:"
- "setSelectedEnv:"
- "setSelectedProxy:"
- "setSettingsMode:"
- "setShouldAppearDisabled:"
- "setShouldAutoSelectWhenInRange:"
- "setShouldDisplay:"
- "setShouldDisplayExtendedConsentInfo:"
- "setShouldDisplayType:"
- "setSimLabelID:"
- "setSkipEligibilityCheck:"
- "setSourceIccid:"
- "setStatus:"
- "setSubscription:"
- "setSubscriptionResult:"
- "setSubscriptionStatusOverride:"
- "setSupportedTransferOption:"
- "setTimeZone:"
- "setTrialExpirationDate:"
- "setType:"
- "setUserInPurchaseFlow:"
- "setUserLabel:"
- "setWithObjects:"
- "settingsModeAsString:"
- "sharedManager"
- "shouldAutoSelectWhenInRange"
- "shouldDisplayType"
- "shouldShowAddNewRemotePlanWithContext:completion:"
- "shouldShowPlanSetup:"
- "showUiIgnoringActivationFlags:"
- "sourceIccid"
- "startProvisioningWithCompletion:"
- "startRemoteProvisioningForCSN:completion:"
- "startRemoteProvisioningWithCompletion:"
- "statusAsString:"
- "stringWithFormat:"
- "superclass"
- "supportsSecureCoding"
- "synchronousProxyWithErrorHandler:"
- "synchronousRemoteObjectProxyWithErrorHandler:"
- "timeIntervalSinceReferenceDate"
- "timeZoneForSecondsFromGMT:"
- "transferredStatusAsString:"
- "typeAsString:"
- "userDidProvideConsentResponse:forPlan:isRemote:completion:"
- "userDidProvideResponse:confirmationCode:forPlan:isRemote:completion:"
- "userDidProvideResponse:confirmationCode:plan:completion:"
- "userLabel"
- "userSignupInitiatedOrFailed"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8i16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@\"NSError\"16"
- "v24@0:8@\"NSString\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?@\"NSArray\"@\"NSError\">16"
- "v24@0:8@?<v@?@\"NSDictionary\"@\"NSError\">16"
- "v24@0:8@?<v@?@\"NSString\">16"
- "v24@0:8@?<v@?B>16"
- "v24@0:8@?<v@?B@\"NSError\">16"
- "v24@0:8@?<v@?Q@\"NSError\">16"
- "v24@0:8@?<v@?dd>16"
- "v24@0:8@?<v@?q>16"
- "v24@0:8@?<v@?qq>16"
- "v24@0:8Q16"
- "v24@0:8q16"
- "v28@0:8@\"NSString\"16B24"
- "v28@0:8@16B24"
- "v28@0:8B16@?20"
- "v28@0:8B16@?<v@?@\"NSArray\"@\"NSError\">20"
- "v32@0:8@\"CTCellularPlanItem\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"CTCellularPlanItem\"16@?<v@?B@\"NSError\">24"
- "v32@0:8@\"CTCellularPlanPendingTransfer\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"CTCellularPlanPendingTransfer\"16@?<v@?B@\"NSString\"@\"NSDictionary\"@\"NSError\">24"
- "v32@0:8@\"CTDanglingPlanItem\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"CTXPCServiceSubscriptionContext\"16@?<v@?B>24"
- "v32@0:8@\"CTXPCServiceSubscriptionContext\"16@?<v@?BQ@\"NSString\"@\"NSError\">24"
- "v32@0:8@\"NSArray\"16@?<v@?@\"NSArray\"@\"NSError\">24"
- "v32@0:8@\"NSArray\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"NSArray\"16@?<v@?B@\"NSError\">24"
- "v32@0:8@\"NSNumber\"16@\"NSNumber\"24"
- "v32@0:8@\"NSString\"16@?<v@?@\"NSString\"@\"NSError\">24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v32@0:8Q16@?24"
- "v32@0:8Q16@?<v@?@\"NSError\">24"
- "v32@0:8q16q24"
- "v36@0:8@\"CTCellularPlanItem\"16B24@?<v@?B@\"NSError\">28"
- "v36@0:8@16B24@?28"
- "v36@0:8B16@20@?28"
- "v36@0:8B16q20@?28"
- "v36@0:8B16q20@?<v@?@\"NSError\">28"
- "v40@0:8@\"CTCellularPlanItem\"16@\"CTUserLabel\"24@?<v@?B@\"NSError\">32"
- "v40@0:8@\"CTDanglingPlanItem\"16@\"CTCellularPlanItem\"24@?<v@?@\"NSError\">32"
- "v40@0:8@16@24@?32"
- "v44@0:8B16@\"NSString\"20@\"CTCellularPlanItem\"28@?<v@?B@\"NSError\">36"
- "v44@0:8B16@20@28@?36"
- "v44@0:8q16@24B32@?36"
- "v48@0:8@\"NSData\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40"
- "v48@0:8@16@24@32@40"
- "v48@0:8q16@\"NSString\"24@\"CTCellularPlanItem\"32@?<v@?B@\"NSError\">40"
- "v48@0:8q16@24@32@?40"
- "v52@0:8B16@\"NSString\"20@\"CTXPCServiceSubscriptionContext\"28q36@?<v@?@\"NSError\">44"
- "v52@0:8B16@20@28q36@?44"
- "v52@0:8q16@24@32B40@?44"
- "v56@0:8@\"NSData\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40@\"NSString\"48"
- "v56@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40@\"NSString\"48"
- "v56@0:8@\"NSString\"16@\"NSString\"24q32q40@?<v@?@\"NSError\">48"
- "v56@0:8@16@24@32@40@48"
- "v56@0:8@16@24q32q40@?48"
- "v64@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40@\"NSString\"48@?<v@?B>56"
- "v64@0:8@16@24@32@40@48@?56"
- "v68@0:8@\"NSString\"16@\"NSString\"24B32@\"NSString\"36@\"CTXPCServiceSubscriptionContext\"44q52@?<v@?@\"NSError\">60"
- "v68@0:8@16@24B32@36@44q52@?60"
- "v72@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40q48q56@?<v@?@\"NSError\">64"
- "v72@0:8@16@24@32@40q48q56@?64"
- "v84@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40B48@\"NSString\"52@\"CTXPCServiceSubscriptionContext\"60q68@?<v@?@\"NSError\">76"
- "v84@0:8@16@24@32@40B48@52@60q68@?76"
- "validate:"
- "validate:parseTo:"
- "websheetURL"
- "zone"

```
