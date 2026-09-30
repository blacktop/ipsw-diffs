## CellularPlanManager

> `/System/Library/PrivateFrameworks/CellularPlanManager.framework/CellularPlanManager`

```diff

-12410.0.0.0.0
-  __TEXT.__text: 0x1299c
+13071.5.0.0.0
+  __TEXT.__text: 0x131c4
   __TEXT.__auth_stubs: 0x3e0
-  __TEXT.__objc_methlist: 0x171c
-  __TEXT.__cstring: 0x203c
+  __TEXT.__objc_methlist: 0x172c
+  __TEXT.__cstring: 0x20f7
   __TEXT.__const: 0x48
-  __TEXT.__gcc_except_tab: 0x1a4
-  __TEXT.__oslogstring: 0x573
-  __TEXT.__unwind_info: 0x820
+  __TEXT.__gcc_except_tab: 0x1c0
+  __TEXT.__oslogstring: 0x5fc
+  __TEXT.__unwind_info: 0x840
   __TEXT.__objc_classname: 0x26e
-  __TEXT.__objc_methname: 0x2e33
-  __TEXT.__objc_methtype: 0xe25
-  __TEXT.__objc_stubs: 0x1a20
+  __TEXT.__objc_methname: 0x2ec0
+  __TEXT.__objc_methtype: 0xe0e
+  __TEXT.__objc_stubs: 0x1aa0
   __DATA_CONST.__got: 0x100
-  __DATA_CONST.__const: 0xc30
+  __DATA_CONST.__const: 0xd38
   __DATA_CONST.__objc_classlist: 0x98
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa88
+  __DATA_CONST.__objc_selrefs: 0xa98
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x50
   __AUTH_CONST.__auth_got: 0x200
-  __AUTH_CONST.__const: 0x3e0
-  __AUTH_CONST.__cfstring: 0x19c0
-  __AUTH_CONST.__objc_const: 0x25a8
-  __DATA.__objc_ivar: 0x158
+  __AUTH_CONST.__const: 0x440
+  __AUTH_CONST.__cfstring: 0x1a20
+  __AUTH_CONST.__objc_const: 0x25d0
+  __DATA.__objc_ivar: 0x15c
   __DATA.__data: 0x2a0
   __DATA.__bss: 0x10
   __DATA_DIRTY.__objc_data: 0x5f0

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C4332786-F10E-3DD9-96B5-8BCB62895853
-  Functions: 670
-  Symbols:   2103
-  CStrings:  1159
+  UUID: 6BF9EC52-0BB2-3484-B384-FF5329AC23D0
+  Functions: 681
+  Symbols:   2139
+  CStrings:  1175
 
Symbols:
+ -[CTCellularPlanItem cachedPhoneNumber]
+ -[CTCellularPlanItem initWithCellularPlan:uuid:iccid:name:type:phoneNumber:cachedPhoneNumber:label:isLocalTransferToeSIMSupported:isTransferred:transferredStatus:transferredToDeviceDisplayName:supportedTransferOption:settingsMode:]
+ -[CTCellularPlanItem initWithCellularPlan:uuid:type:phoneNumber:cachedPhoneNumber:label:transferredStatus:transferredToDeviceDisplayName:supportedTransferOption:settingsMode:]
+ -[CTCellularPlanItem initWithIccid:uuid:name:phoneNumber:cachedPhoneNumber:label:isLocalTransferToeSIMSupported:isTransferred:transferredStatus:transferredToDeviceDisplayName:supportedTransferOption:settingsMode:]
+ -[CTCellularPlanItem setCachedPhoneNumber:]
+ -[CTCellularPlanManager getSupportedFlowTypesWithError:]
+ GCC_except_table158
+ GCC_except_table161
+ GCC_except_table185
+ GCC_except_table221
+ GCC_except_table224
+ GCC_except_table233
+ GCC_except_table397
+ GCC_except_table409
+ GCC_except_table412
+ GCC_except_table42
+ _OBJC_IVAR_$_CTCellularPlanItem._cachedPhoneNumber
+ ___100-[CTCellularPlanManager addNewPlanWithCardData:confirmationCode:triggerType:userConsent:completion:]_block_invoke.227
+ ___100-[CTCellularPlanManager addNewPlanWithCardData:confirmationCode:triggerType:userConsent:completion:]_block_invoke_2.228
+ ___114-[CTCellularPlanManager addNewPlanWithAddress:matchingId:oid:confirmationCode:triggerType:userConsent:completion:]_block_invoke.231
+ ___114-[CTCellularPlanManager addNewPlanWithAddress:matchingId:oid:confirmationCode:triggerType:userConsent:completion:]_block_invoke_2.232
+ ___124-[CTCellularPlanManager addNewRemotePlanWithCardData:confirmationCode:isPairing:withCSN:withContext:userConsent:completion:]_block_invoke.321
+ ___124-[CTCellularPlanManager addNewRemotePlanWithCardData:confirmationCode:isPairing:withCSN:withContext:userConsent:completion:]_block_invoke_2.322
+ ___138-[CTCellularPlanManager addNewRemotePlanWithAddress:matchingId:oid:confirmationCode:isPairing:withCSN:withContext:userConsent:completion:]_block_invoke.323
+ ___138-[CTCellularPlanManager addNewRemotePlanWithAddress:matchingId:oid:confirmationCode:isPairing:withCSN:withContext:userConsent:completion:]_block_invoke_2.324
+ ___39-[CTCellularPlanManager eraseAllPlans:]_block_invoke.296
+ ___39-[CTCellularPlanManager eraseAllPlans:]_block_invoke.297
+ ___39-[CTCellularPlanManager getIMEIPrefix:]_block_invoke.237
+ ___39-[CTCellularPlanManager getIMEIPrefix:]_block_invoke_2.238
+ ___39-[CTCellularPlanManager getRemoteInfo:]_block_invoke.349
+ ___39-[CTCellularPlanManager getRemoteInfo:]_block_invoke.351
+ ___39-[CTCellularPlanManager getRemoteInfo:]_block_invoke_2.350
+ ___39-[CTCellularPlanManager setMcc:andMnc:]_block_invoke
+ ___39-[CTCellularPlanManager setMcc:andMnc:]_block_invoke_2
+ ___40-[CTCellularPlanManager getSelectedEnv:]_block_invoke.242
+ ___40-[CTCellularPlanManager getSelectedEnv:]_block_invoke_2.243
+ ___40-[CTCellularPlanManager mccMncOverride:]_block_invoke.253
+ ___40-[CTCellularPlanManager mccMncOverride:]_block_invoke_2.254
+ ___40-[CTCellularPlanManager mccMncOverride:]_block_invoke_3
+ ___42-[CTCellularPlanManager getSelectedProxy:]_block_invoke.247
+ ___42-[CTCellularPlanManager getSelectedProxy:]_block_invoke_2.248
+ ___45-[CTCellularPlanManager shouldShowPlanSetup:]_block_invoke.215
+ ___45-[CTCellularPlanManager shouldShowPlanSetup:]_block_invoke_2.216
+ ___47-[CTCellularPlanManager getSupportedFlowTypes:]_block_invoke.218
+ ___47-[CTCellularPlanManager getSupportedFlowTypes:]_block_invoke_2.219
+ ___49-[CTCellularPlanManager getPlansPendingTransfer:]_block_invoke.272
+ ___49-[CTCellularPlanManager planItemsWithCompletion:]_block_invoke.263
+ ___49-[CTCellularPlanManager planItemsWithCompletion:]_block_invoke.264
+ ___50-[CTCellularPlanManager setLatitude:andLongitude:]_block_invoke
+ ___50-[CTCellularPlanManager setLatitude:andLongitude:]_block_invoke_2
+ ___51-[CTCellularPlanManager latitudeLongitudeOverride:]_block_invoke.258
+ ___51-[CTCellularPlanManager latitudeLongitudeOverride:]_block_invoke_2.259
+ ___51-[CTCellularPlanManager latitudeLongitudeOverride:]_block_invoke_3
+ ___52-[CTCellularPlanManager resolveSimLabel:completion:]_block_invoke.279
+ ___53-[CTCellularPlanManager remapSimLabel:to:completion:]_block_invoke.280
+ ___54-[CTCellularPlanManager didDeletePlanItem:completion:]_block_invoke.294
+ ___54-[CTCellularPlanManager didDeletePlanItem:completion:]_block_invoke.295
+ ___55-[CTCellularPlanManager showUiIgnoringActivationFlags:]_block_invoke
+ ___55-[CTCellularPlanManager showUiIgnoringActivationFlags:]_block_invoke_2
+ ___56-[CTCellularPlanManager getSupportedFlowTypesWithError:]_block_invoke
+ ___56-[CTCellularPlanManager getSupportedFlowTypesWithError:]_block_invoke_2
+ ___57-[CTCellularPlanManager didSelectPlanForData:completion:]_block_invoke.286
+ ___57-[CTCellularPlanManager didSelectPlanForData:completion:]_block_invoke.287
+ ___57-[CTCellularPlanManager startProvisioningWithCompletion:]_block_invoke.223
+ ___57-[CTCellularPlanManager startProvisioningWithCompletion:]_block_invoke_2.224
+ ___58-[CTCellularPlanManager finishProvisioningWithCompletion:]_block_invoke.225
+ ___58-[CTCellularPlanManager finishProvisioningWithCompletion:]_block_invoke_2.226
+ ___59-[CTCellularPlanManager addNewPlanWithFlowType:completion:]_block_invoke.229
+ ___59-[CTCellularPlanManager addNewPlanWithFlowType:completion:]_block_invoke_2.230
+ ___59-[CTCellularPlanManager eraseAllRemotePlansWithCompletion:]_block_invoke.361
+ ___59-[CTCellularPlanManager eraseAllRemotePlansWithCompletion:]_block_invoke.362
+ ___60-[CTCellularPlanManager didDeleteRemotePlanItem:completion:]_block_invoke.327
+ ___60-[CTCellularPlanManager didDeleteRemotePlanItem:completion:]_block_invoke.328
+ ___60-[CTCellularPlanManager didSelectRemotePlanItem:completion:]_block_invoke.325
+ ___60-[CTCellularPlanManager didSelectRemotePlanItem:completion:]_block_invoke.326
+ ___61-[CTCellularPlanManager carrierItemsShouldUpdate:completion:]_block_invoke.281
+ ___61-[CTCellularPlanManager carrierItemsShouldUpdate:completion:]_block_invoke.282
+ ___61-[CTCellularPlanManager installPendingRemotePlan:completion:]_block_invoke.233
+ ___61-[CTCellularPlanManager installPendingRemotePlan:completion:]_block_invoke_2.234
+ ___62-[CTCellularPlanManager deletePlanPendingTransfer:completion:]_block_invoke.277
+ ___62-[CTCellularPlanManager deletePlanPendingTransfer:completion:]_block_invoke_2.278
+ ___62-[CTCellularPlanManager didSelectPlansForIMessage:completion:]_block_invoke.290
+ ___62-[CTCellularPlanManager didSelectPlansForIMessage:completion:]_block_invoke.291
+ ___63-[CTCellularPlanManager didSelectPlanItem:isEnable:completion:]_block_invoke.283
+ ___63-[CTCellularPlanManager didSelectPlanItem:isEnable:completion:]_block_invoke.284
+ ___63-[CTCellularPlanManager getPlansPendingTransferForTestability:]_block_invoke.273
+ ___63-[CTCellularPlanManager manageAccountForRemotePlan:completion:]_block_invoke.317
+ ___63-[CTCellularPlanManager manageAccountForRemotePlan:completion:]_block_invoke_2.318
+ ___64-[CTCellularPlanManager activatePlanPendingTransfer:completion:]_block_invoke.274
+ ___64-[CTCellularPlanManager activatePlanPendingTransfer:completion:]_block_invoke_2.275
+ ___65-[CTCellularPlanManager didSelectPlanForDefaultVoice:completion:]_block_invoke.288
+ ___65-[CTCellularPlanManager didSelectPlanForDefaultVoice:completion:]_block_invoke.289
+ ___66-[CTCellularPlanManager danglingPlanItemsShouldUpdate:completion:]_block_invoke.268
+ ___66-[CTCellularPlanManager danglingPlanItemsShouldUpdate:completion:]_block_invoke.269
+ ___66-[CTCellularPlanManager startRemoteProvisioningForCSN:completion:]_block_invoke.313
+ ___66-[CTCellularPlanManager startRemoteProvisioningForCSN:completion:]_block_invoke_2.314
+ ___67-[CTCellularPlanManager finishRemoteProvisioningForCSN:completion:]_block_invoke.315
+ ___67-[CTCellularPlanManager finishRemoteProvisioningForCSN:completion:]_block_invoke_2.316
+ ___67-[CTCellularPlanManager isRemotePlanCapableWithContext:completion:]_block_invoke.308
+ ___67-[CTCellularPlanManager isRemotePlanCapableWithContext:completion:]_block_invoke_2.309
+ ___71-[CTCellularPlanManager resumePlanProvisioning:userConsent:completion:]_block_invoke.235
+ ___71-[CTCellularPlanManager resumePlanProvisioning:userConsent:completion:]_block_invoke_2.236
+ ___74-[CTCellularPlanManager shouldShowAddNewRemotePlanWithContext:completion:]_block_invoke.310
+ ___74-[CTCellularPlanManager shouldShowAddNewRemotePlanWithContext:completion:]_block_invoke_2.311
+ ___85-[CTCellularPlanManager addNewRemotePlan:withCSN:withContext:userConsent:completion:]_block_invoke.319
+ ___85-[CTCellularPlanManager addNewRemotePlan:withCSN:withContext:userConsent:completion:]_block_invoke_2.320
+ ___98-[CTCellularPlanManager didPurchaseRemotePlanForEid:imei:meid:iccid:alternateSmdpFqdn:completion:]_block_invoke.353
+ ___98-[CTCellularPlanManager didPurchaseRemotePlanForEid:imei:meid:iccid:alternateSmdpFqdn:completion:]_block_invoke_2.354
+ ___block_descriptor_40_e8_32b_e11_v24?0d8d16ls32l8
+ ___block_descriptor_40_e8_32b_e11_v24?0q8q16ls32l8
+ ___block_descriptor_48_e8_32r40r_e20_v24?0Q8"NSError"16lr32l8r40l8
+ ___block_descriptor_56_e8_32b_e5_v8?0ls32l8
+ ___block_descriptor_56_e8_32o40o48o_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32o_e5_v8?0ls32l8
+ ___block_literal_global.222
+ ___block_literal_global.241
+ ___block_literal_global.246
+ ___block_literal_global.250
+ ___block_literal_global.262
+ ___block_literal_global.267
+ ___block_literal_global.271
+ ___block_literal_global.299
+ ___block_literal_global.301
+ ___block_literal_global.303
+ ___block_literal_global.305
+ ___block_literal_global.307
+ ___block_literal_global.340
+ ___block_literal_global.342
+ ___block_literal_global.344
+ ___block_literal_global.346
+ ___block_literal_global.348
+ ___block_literal_global.356
+ ___block_literal_global.358
+ ___block_literal_global.360
+ ___block_literal_global.364
+ ___block_literal_global.366
+ ___block_literal_global.369
+ _objc_msgSend$initWithCellularPlan:uuid:iccid:name:type:phoneNumber:cachedPhoneNumber:label:isLocalTransferToeSIMSupported:isTransferred:transferredStatus:transferredToDeviceDisplayName:supportedTransferOption:settingsMode:
+ _objc_msgSend$latitudeLongitudeOverride:
+ _objc_msgSend$mccMncOverride:
+ _objc_msgSend$setLatitude:andLongitude:
+ _objc_msgSend$setMcc:andMnc:
+ _objc_msgSend$showUiIgnoringActivationFlags:
- -[CTCellularPlanItem initWithCellularPlan:uuid:iccid:name:type:phoneNumber:label:isLocalTransferToeSIMSupported:isTransferred:transferredStatus:transferredToDeviceDisplayName:supportedTransferOption:settingsMode:]
- -[CTCellularPlanItem initWithCellularPlan:uuid:type:phoneNumber:label:transferredStatus:transferredToDeviceDisplayName:supportedTransferOption:settingsMode:]
- -[CTCellularPlanItem initWithIccid:uuid:name:phoneNumber:label:isLocalTransferToeSIMSupported:isTransferred:transferredStatus:transferredToDeviceDisplayName:supportedTransferOption:settingsMode:]
- -[CTCellularPlanManager getPhoneAuthTokenWithMessage:completion:]
- GCC_except_table131
- GCC_except_table140
- GCC_except_table143
- GCC_except_table179
- GCC_except_table203
- GCC_except_table206
- GCC_except_table388
- GCC_except_table400
- GCC_except_table403
- ___100-[CTCellularPlanManager addNewPlanWithCardData:confirmationCode:triggerType:userConsent:completion:]_block_invoke.229
- ___100-[CTCellularPlanManager addNewPlanWithCardData:confirmationCode:triggerType:userConsent:completion:]_block_invoke_2.230
- ___114-[CTCellularPlanManager addNewPlanWithAddress:matchingId:oid:confirmationCode:triggerType:userConsent:completion:]_block_invoke.233
- ___114-[CTCellularPlanManager addNewPlanWithAddress:matchingId:oid:confirmationCode:triggerType:userConsent:completion:]_block_invoke_2.234
- ___124-[CTCellularPlanManager addNewRemotePlanWithCardData:confirmationCode:isPairing:withCSN:withContext:userConsent:completion:]_block_invoke.311
- ___124-[CTCellularPlanManager addNewRemotePlanWithCardData:confirmationCode:isPairing:withCSN:withContext:userConsent:completion:]_block_invoke_2.312
- ___138-[CTCellularPlanManager addNewRemotePlanWithAddress:matchingId:oid:confirmationCode:isPairing:withCSN:withContext:userConsent:completion:]_block_invoke.313
- ___138-[CTCellularPlanManager addNewRemotePlanWithAddress:matchingId:oid:confirmationCode:isPairing:withCSN:withContext:userConsent:completion:]_block_invoke_2.314
- ___39-[CTCellularPlanManager eraseAllPlans:]_block_invoke.286
- ___39-[CTCellularPlanManager eraseAllPlans:]_block_invoke.287
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
- ___49-[CTCellularPlanManager planItemsWithCompletion:]_block_invoke.254
- ___52-[CTCellularPlanManager resolveSimLabel:completion:]_block_invoke.269
- ___53-[CTCellularPlanManager remapSimLabel:to:completion:]_block_invoke.270
- ___54-[CTCellularPlanManager didDeletePlanItem:completion:]_block_invoke.284
- ___54-[CTCellularPlanManager didDeletePlanItem:completion:]_block_invoke.285
- ___57-[CTCellularPlanManager didSelectPlanForData:completion:]_block_invoke.276
- ___57-[CTCellularPlanManager didSelectPlanForData:completion:]_block_invoke.277
- ___57-[CTCellularPlanManager startProvisioningWithCompletion:]_block_invoke.225
- ___57-[CTCellularPlanManager startProvisioningWithCompletion:]_block_invoke_2.226
- ___58-[CTCellularPlanManager finishProvisioningWithCompletion:]_block_invoke.227
- ___58-[CTCellularPlanManager finishProvisioningWithCompletion:]_block_invoke_2.228
- ___59-[CTCellularPlanManager addNewPlanWithFlowType:completion:]_block_invoke.231
- ___59-[CTCellularPlanManager addNewPlanWithFlowType:completion:]_block_invoke_2.232
- ___59-[CTCellularPlanManager eraseAllRemotePlansWithCompletion:]_block_invoke.354
- ___59-[CTCellularPlanManager eraseAllRemotePlansWithCompletion:]_block_invoke.355
- ___60-[CTCellularPlanManager didDeleteRemotePlanItem:completion:]_block_invoke.317
- ___60-[CTCellularPlanManager didDeleteRemotePlanItem:completion:]_block_invoke.318
- ___60-[CTCellularPlanManager didSelectRemotePlanItem:completion:]_block_invoke.315
- ___60-[CTCellularPlanManager didSelectRemotePlanItem:completion:]_block_invoke.316
- ___61-[CTCellularPlanManager carrierItemsShouldUpdate:completion:]_block_invoke.271
- ___61-[CTCellularPlanManager carrierItemsShouldUpdate:completion:]_block_invoke.272
- ___61-[CTCellularPlanManager installPendingRemotePlan:completion:]_block_invoke.235
- ___61-[CTCellularPlanManager installPendingRemotePlan:completion:]_block_invoke_2.236
- ___62-[CTCellularPlanManager deletePlanPendingTransfer:completion:]_block_invoke.267
- ___62-[CTCellularPlanManager deletePlanPendingTransfer:completion:]_block_invoke_2.268
- ___62-[CTCellularPlanManager didSelectPlansForIMessage:completion:]_block_invoke.280
- ___62-[CTCellularPlanManager didSelectPlansForIMessage:completion:]_block_invoke.281
- ___63-[CTCellularPlanManager didSelectPlanItem:isEnable:completion:]_block_invoke.273
- ___63-[CTCellularPlanManager didSelectPlanItem:isEnable:completion:]_block_invoke.274
- ___63-[CTCellularPlanManager getPlansPendingTransferForTestability:]_block_invoke.263
- ___63-[CTCellularPlanManager manageAccountForRemotePlan:completion:]_block_invoke.307
- ___63-[CTCellularPlanManager manageAccountForRemotePlan:completion:]_block_invoke_2.308
- ___64-[CTCellularPlanManager activatePlanPendingTransfer:completion:]_block_invoke.264
- ___64-[CTCellularPlanManager activatePlanPendingTransfer:completion:]_block_invoke_2.265
- ___65-[CTCellularPlanManager didSelectPlanForDefaultVoice:completion:]_block_invoke.278
- ___65-[CTCellularPlanManager didSelectPlanForDefaultVoice:completion:]_block_invoke.279
- ___65-[CTCellularPlanManager getPhoneAuthTokenWithMessage:completion:]_block_invoke
- ___65-[CTCellularPlanManager getPhoneAuthTokenWithMessage:completion:]_block_invoke.343
- ___65-[CTCellularPlanManager getPhoneAuthTokenWithMessage:completion:]_block_invoke_2
- ___65-[CTCellularPlanManager getPhoneAuthTokenWithMessage:completion:]_block_invoke_2.344
- ___65-[CTCellularPlanManager getPhoneAuthTokenWithMessage:completion:]_block_invoke_3
- ___66-[CTCellularPlanManager danglingPlanItemsShouldUpdate:completion:]_block_invoke.258
- ___66-[CTCellularPlanManager danglingPlanItemsShouldUpdate:completion:]_block_invoke.259
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
- ___block_descriptor_40_e8_32b_e21_v20?0"NSString"8B16ls32l8
- ___block_literal_global.224
- ___block_literal_global.243
- ___block_literal_global.248
- ___block_literal_global.261
- ___block_literal_global.283
- ___block_literal_global.289
- ___block_literal_global.291
- ___block_literal_global.295
- ___block_literal_global.297
- ___block_literal_global.320
- ___block_literal_global.322
- ___block_literal_global.324
- ___block_literal_global.326
- ___block_literal_global.328
- ___block_literal_global.349
- ___block_literal_global.351
- ___block_literal_global.353
- ___block_literal_global.357
- ___block_literal_global.359
- ___block_literal_global.362
- _objc_msgSend$getPhoneAuthTokenWithMessage:completion:
- _objc_msgSend$initWithCellularPlan:uuid:iccid:name:type:phoneNumber:label:isLocalTransferToeSIMSupported:isTransferred:transferredStatus:transferredToDeviceDisplayName:supportedTransferOption:settingsMode:
CStrings:
+ "-[CTCellularPlanManager getSupportedFlowTypesWithError:]"
+ "@104@0:8@16@24@32@40@48@56B64B68q72@80Q88q96"
+ "@120@0:8@16@24@32@40q48@56@64@72B80B84q88@96Q104q112"
+ "@96@0:8@16@24q32@40@48@56q64@72Q80q88"
+ "Authentication failed when Stolen Device Protection is enabled."
+ "Establishing reconnection credentials failed."
+ "Q24@0:8^@16"
+ "T@\"NSString\",&,N,V_cachedPhoneNumber"
+ "_cachedPhoneNumber"
+ "cachedPhoneNumber"
+ "getSupportedFlowTypesWithError:"
+ "initWithCellularPlan:uuid:iccid:name:type:phoneNumber:cachedPhoneNumber:label:isLocalTransferToeSIMSupported:isTransferred:transferredStatus:transferredToDeviceDisplayName:supportedTransferOption:settingsMode:"
+ "initWithCellularPlan:uuid:type:phoneNumber:cachedPhoneNumber:label:transferredStatus:transferredToDeviceDisplayName:supportedTransferOption:settingsMode:"
+ "initWithIccid:uuid:name:phoneNumber:cachedPhoneNumber:label:isLocalTransferToeSIMSupported:isTransferred:transferredStatus:transferredToDeviceDisplayName:supportedTransferOption:settingsMode:"
+ "setCachedPhoneNumber:"
+ "unable to get mcc/mnc overrides %@"
+ "unable to set lat/long %@"
+ "unable to set mcc/mnc %@"
+ "unable to set show Ui ignoring activation flags %@"
+ "v24@?0d8d16"
+ "v24@?0q8q16"
- "@112@0:8@16@24@32@40q48@56@64B72B76q80@88Q96q104"
- "@88@0:8@16@24q32@40@48q56@64Q72q80"
- "@96@0:8@16@24@32@40@48B56B60q64@72Q80q88"
- "getPhoneAuthTokenWithMessage:completion:"
- "initWithCellularPlan:uuid:iccid:name:type:phoneNumber:label:isLocalTransferToeSIMSupported:isTransferred:transferredStatus:transferredToDeviceDisplayName:supportedTransferOption:settingsMode:"
- "initWithCellularPlan:uuid:type:phoneNumber:label:transferredStatus:transferredToDeviceDisplayName:supportedTransferOption:settingsMode:"
- "initWithIccid:uuid:name:phoneNumber:label:isLocalTransferToeSIMSupported:isTransferred:transferredStatus:transferredToDeviceDisplayName:supportedTransferOption:settingsMode:"
- "v20@?0@\"NSString\"8B16"
- "v32@0:8@\"NSDictionary\"16@?<v@?@\"NSString\"B>24"

```
