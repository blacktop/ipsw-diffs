## Transparency

> `/System/Library/PrivateFrameworks/Transparency.framework/Transparency`

```diff

-1033.82.1.0.0
-  __TEXT.__text: 0x33b5c
+1033.100.65.0.0
+  __TEXT.__text: 0x33b50
   __TEXT.__auth_stubs: 0x650
-  __TEXT.__objc_methlist: 0x2b3c
-  __TEXT.__cstring: 0x1d9a
+  __TEXT.__objc_methlist: 0x2b5c
+  __TEXT.__cstring: 0x1e23
   __TEXT.__const: 0x160
   __TEXT.__gcc_except_tab: 0x4a0
-  __TEXT.__oslogstring: 0x16a0
+  __TEXT.__oslogstring: 0x169b
   __TEXT.__dlopen_cstrs: 0x47
   __TEXT.__unwind_info: 0x10b8
   __TEXT.__objc_classname: 0x59a
-  __TEXT.__objc_methname: 0x60ce
+  __TEXT.__objc_methname: 0x614c
   __TEXT.__objc_methtype: 0x1928
-  __TEXT.__objc_stubs: 0x4900
-  __DATA_CONST.__got: 0x68
-  __DATA_CONST.__const: 0x11b0
+  __TEXT.__objc_stubs: 0x49c0
+  __DATA_CONST.__got: 0x70
+  __DATA_CONST.__const: 0x11a8
   __DATA_CONST.__objc_classlist: 0x188
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x4fc8
-  __DATA_CONST.__objc_selrefs: 0x1810
-  __AUTH_CONST.__cfstring: 0x2f20
-  __AUTH_CONST.__objc_const: 0x670
-  __AUTH_CONST.__const: 0xd20
+  __DATA_CONST.__objc_const: 0x5018
+  __DATA_CONST.__objc_selrefs: 0x1850
+  __DATA_CONST.__objc_protorefs: 0x20
+  __DATA_CONST.__objc_classrefs: 0x240
+  __DATA_CONST.__objc_superrefs: 0x108
+  __AUTH_CONST.__cfstring: 0x2fe0
+  __AUTH_CONST.__objc_const: 0x280
+  __AUTH_CONST.__const: 0xb80
   __AUTH_CONST.__objc_intobj: 0x150
   __AUTH_CONST.__auth_got: 0x338
-  __AUTH.__objc_data: 0x370
-  __DATA.__objc_protorefs: 0x20
-  __DATA.__objc_classrefs: 0x238
-  __DATA.__objc_superrefs: 0x108
-  __DATA.__objc_ivar: 0x2ac
+  __AUTH.__objc_data: 0x50
+  __DATA.__objc_ivar: 0x2b0
   __DATA.__data: 0x598
   __DATA.__bss: 0x20
   __DATA.__common: 0x8
-  __DATA_DIRTY.__const: 0x1040
-  __DATA_DIRTY.__objc_const: 0x1238
-  __DATA_DIRTY.__objc_data: 0xbe0
-  __DATA_DIRTY.__bss: 0x198
+  __DATA_DIRTY.__const: 0x11e0
+  __DATA_DIRTY.__objc_const: 0x1628
+  __DATA_DIRTY.__objc_data: 0xf00
+  __DATA_DIRTY.__bss: 0x1b8
   __DATA_DIRTY.__common: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 18DF6BE8-25C0-3B6B-9E74-57CC55482024
-  Functions: 1417
-  Symbols:   4874
-  CStrings:  2268
+  UUID: 67517D74-1A9B-3D66-A37B-F1589E372952
+  Functions: 1420
+  Symbols:   4894
+  CStrings:  2291
 
Symbols:
+ -[KTIDStaticKeyStore updateContact:]
+ -[KTOptInManager waitForIDSRegistration:]
+ -[NSDate(TransparencyDate) kt_fuzzyDate]
+ -[TransparencyIDSRegistrationData dsid]
+ -[TransparencyIDSRegistrationData setDsid:]
+ GCC_except_table118
+ GCC_except_table140
+ GCC_except_table86
+ _NSCalendarIdentifierISO8601
+ _OBJC_CLASS_$_NSCalendar
+ _OBJC_IVAR_$_TransparencyIDSRegistrationData._dsid
+ ___125-[TransparencyDaemon replaySelfValidate:application:pcsAccountKey:queryRequest:queryResponse:responseTime:completionHandler:]_block_invoke.334
+ ___22-[KTStatus getStatus:]_block_invoke.247
+ ___22-[KTStatus getStatus:]_block_invoke_2.248
+ ___26-[KTStatus getSelfStatus:]_block_invoke.256
+ ___26-[KTStatus getSelfStatus:]_block_invoke_2.257
+ ___40-[NSDate(TransparencyDate) kt_fuzzyDate]_block_invoke
+ ___40-[TransparencyDaemon getAllOptInStates:]_block_invoke.395
+ ___41-[KTOptInManager waitForIDSRegistration:]_block_invoke
+ ___41-[KTOptInManager waitForIDSRegistration:]_block_invoke.243
+ ___41-[KTOptInManager waitForIDSRegistration:]_block_invoke_2
+ ___41-[KTOptInManager waitForIDSRegistration:]_block_invoke_2.244
+ ___44-[TransparencyDaemon configurationBagFetch:]_block_invoke.263
+ ___44-[TransparencyDaemon transparencyFetchIDMS:]_block_invoke.303
+ ___44-[TransparencyDaemon transparencyFetchSelf:]_block_invoke.309
+ ___44-[TransparencyDaemon transparencyIDSRepair:]_block_invoke.267
+ ___44-[TransparencyDaemon transparencyIDSRepair:]_block_invoke_2.268
+ ___45-[TransparencyDaemon getOptInState:complete:]_block_invoke.386
+ ___45-[TransparencyDaemon maybeUpdateMonitorState]_block_invoke.317
+ ___45-[TransparencyDaemon maybeUpdateMonitorState]_block_invoke_2.320
+ ___46-[KTStatus ignoreFailedEvent:completionBlock:]_block_invoke.284
+ ___46-[KTStatus ignoreFailedEvent:completionBlock:]_block_invoke_2.285
+ ___46-[TransparencyDaemon transparencySysDiagnose:]_block_invoke.271
+ ___47-[KTStatus ignoreFailedEvents:completionBlock:]_block_invoke.293
+ ___47-[KTStatus ignoreFailedEvents:completionBlock:]_block_invoke_2.294
+ ___47-[TransparencyDaemon transparencyCloudDevices:]_block_invoke.369
+ ___47-[TransparencyDaemon transparencyValidateSelf:]_block_invoke.306
+ ___48-[KTStatus errorForFailedEvent:completionBlock:]_block_invoke.265
+ ___48-[KTStatus errorForFailedEvent:completionBlock:]_block_invoke_2.267
+ ___49-[TransparencyDaemon transparencyCheckIDSHealth:]_block_invoke.349
+ ___49-[TransparencyDaemon transparencyCheckIDSHealth:]_block_invoke_2.351
+ ___49-[TransparencyDaemon transparencyIDMSDeviceList:]_block_invoke.325
+ ___49-[TransparencyDaemon transparencyIDMSDeviceList:]_block_invoke_2.327
+ ___50-[KTStatus errorsForFailedEvents:completionBlock:]_block_invoke.275
+ ___50-[KTStatus errorsForFailedEvents:completionBlock:]_block_invoke_2.276
+ ___50-[TransparencyDaemon transparencyFetchPublicKeys:]_block_invoke.337
+ ___50-[TransparencyDaemon transparencyIDSRegistration:]_block_invoke.354
+ ___50-[TransparencyDaemon transparencySysDiagnoseData:]_block_invoke.275
+ ___50-[TransparencyDaemon transparencySysDiagnoseData:]_block_invoke.281
+ ___50-[TransparencyDaemon transparencySysDiagnoseData:]_block_invoke_2.277
+ ___50-[TransparencyDaemon transparencySysDiagnoseData:]_block_invoke_2.293
+ ___52-[TransparencyDaemon performAndWaitForSelfValidate:]_block_invoke.312
+ ___56-[KTOptInManager setOptInState:detailedCompletionBlock:]_block_invoke.249
+ ___56-[KTOptInManager setOptInState:detailedCompletionBlock:]_block_invoke.252
+ ___56-[KTOptInManager setOptInState:detailedCompletionBlock:]_block_invoke_2.253
+ ___57-[TransparencyDaemon transparencyDumpKTRegistrationData:]_block_invoke.360
+ ___57-[TransparencyDaemon transparencyTriggerIDSRegistration:]_block_invoke.340
+ ___58-[TransparencyDaemon getOptInForURI:application:complete:]_block_invoke.389
+ ___58-[TransparencyDaemon transparencyClearKTRegistrationData:]_block_invoke.366
+ ___59-[KTOptInManager changeOptInState:detailedCompletionBlock:]_block_invoke.258
+ ___59-[KTOptInManager changeOptInState:detailedCompletionBlock:]_block_invoke.261
+ ___59-[KTOptInManager changeOptInState:detailedCompletionBlock:]_block_invoke_2.262
+ ___59-[TransparencyDaemon getOptInStateForApplication:complete:]_block_invoke.398
+ ___59-[TransparencyDaemon transparencyGetKTSignatures:complete:]_block_invoke.363
+ ___60-[TransparencyDaemon changeOptInState:application:complete:]_block_invoke.383
+ ___60-[TransparencyDaemon transparencyTriggerOperation:complete:]_block_invoke.380
+ ___61-[TransparencyDaemon transparencyCheckKTAccountKey:complete:]_block_invoke.343
+ ___63-[TransparencyDaemon transparencyPerformRegistrationSignature:]_block_invoke.357
+ ___65-[TransparencyDaemon clearOptInStateForURI:application:complete:]_block_invoke.401
+ ___69-[TransparencyDaemon transparencyCloudDeviceAdd:clientData:complete:]_block_invoke.404
+ ___72-[TransparencyDaemon transparencyCloudDeviceRemove:clientData:complete:]_block_invoke.407
+ ___77-[TransparencyDaemon setOptInForURI:application:state:smtTimestamp:complete:]_block_invoke.392
+ ___block_literal_global.236
+ ___block_literal_global.246
+ ___block_literal_global.248
+ ___block_literal_global.250
+ ___block_literal_global.255
+ ___block_literal_global.259
+ ___block_literal_global.260
+ ___block_literal_global.264
+ ___block_literal_global.269
+ ___block_literal_global.270
+ ___block_literal_global.274
+ ___block_literal_global.278
+ ___block_literal_global.283
+ ___block_literal_global.287
+ ___block_literal_global.296
+ ___block_literal_global.305
+ ___block_literal_global.314
+ ___block_literal_global.319
+ ___block_literal_global.322
+ ___block_literal_global.324
+ ___block_literal_global.333
+ ___block_literal_global.339
+ ___block_literal_global.353
+ ___block_literal_global.356
+ ___block_literal_global.359
+ ___block_literal_global.362
+ ___block_literal_global.365
+ ___block_literal_global.368
+ ___block_literal_global.371
+ ___block_literal_global.379
+ ___block_literal_global.382
+ ___block_literal_global.385
+ ___block_literal_global.388
+ ___block_literal_global.391
+ ___block_literal_global.394
+ ___block_literal_global.397
+ ___block_literal_global.400
+ ___block_literal_global.403
+ ___block_literal_global.406
+ _kTransparencyErrorIDSRegistrationTimeout
+ _kTransparencyErrorKTDisabled
+ _kTransparencyTriggerOperationIDSServerBagChangedNotification
+ _kTransparencyTriggerOperationServerOptInFetch
+ _kt_fuzzyDate.onceToken
+ _kt_fuzzyDate.zulu
+ _objc_msgSend$calendarWithIdentifier:
+ _objc_msgSend$components:fromDate:
+ _objc_msgSend$dateFromComponents:
+ _objc_msgSend$dsid
+ _objc_msgSend$setDsid:
+ _objc_msgSend$timeZoneForSecondsFromGMT:
+ _objc_msgSend$triggerSelfValidate:
+ _objc_msgSend$waitForIDSRegistration:
- -[TransparencyStaticKey updateStaticKeyDatabaseForContact:peerPublicAccountIdentity:complete:]
- GCC_except_table116
- GCC_except_table138
- GCC_except_table84
- ___125-[TransparencyDaemon replaySelfValidate:application:pcsAccountKey:queryRequest:queryResponse:responseTime:completionHandler:]_block_invoke.321
- ___22-[KTStatus getStatus:]_block_invoke.241
- ___22-[KTStatus getStatus:]_block_invoke_2.245
- ___26-[KTStatus getSelfStatus:]_block_invoke.250
- ___26-[KTStatus getSelfStatus:]_block_invoke_2.254
- ___40-[TransparencyDaemon getAllOptInStates:]_block_invoke.382
- ___44-[TransparencyDaemon configurationBagFetch:]_block_invoke.250
- ___44-[TransparencyDaemon transparencyFetchIDMS:]_block_invoke.290
- ___44-[TransparencyDaemon transparencyFetchSelf:]_block_invoke.296
- ___44-[TransparencyDaemon transparencyIDSRepair:]_block_invoke.254
- ___44-[TransparencyDaemon transparencyIDSRepair:]_block_invoke_2.255
- ___45-[TransparencyDaemon getOptInState:complete:]_block_invoke.373
- ___45-[TransparencyDaemon maybeUpdateMonitorState]_block_invoke.304
- ___45-[TransparencyDaemon maybeUpdateMonitorState]_block_invoke_2.307
- ___46-[KTStatus ignoreFailedEvent:completionBlock:]_block_invoke.278
- ___46-[KTStatus ignoreFailedEvent:completionBlock:]_block_invoke_2.282
- ___46-[TransparencyDaemon transparencySysDiagnose:]_block_invoke.258
- ___47-[KTStatus ignoreFailedEvents:completionBlock:]_block_invoke.287
- ___47-[KTStatus ignoreFailedEvents:completionBlock:]_block_invoke_2.291
- ___47-[TransparencyDaemon transparencyCloudDevices:]_block_invoke.356
- ___47-[TransparencyDaemon transparencyValidateSelf:]_block_invoke.293
- ___48-[KTStatus errorForFailedEvent:completionBlock:]_block_invoke.259
- ___48-[KTStatus errorForFailedEvent:completionBlock:]_block_invoke_2.264
- ___49-[TransparencyDaemon transparencyCheckIDSHealth:]_block_invoke.336
- ___49-[TransparencyDaemon transparencyCheckIDSHealth:]_block_invoke_2.338
- ___49-[TransparencyDaemon transparencyIDMSDeviceList:]_block_invoke.312
- ___49-[TransparencyDaemon transparencyIDMSDeviceList:]_block_invoke_2.314
- ___50-[KTStatus errorsForFailedEvents:completionBlock:]_block_invoke.269
- ___50-[KTStatus errorsForFailedEvents:completionBlock:]_block_invoke_2.273
- ___50-[TransparencyDaemon transparencyFetchPublicKeys:]_block_invoke.324
- ___50-[TransparencyDaemon transparencyIDSRegistration:]_block_invoke.341
- ___50-[TransparencyDaemon transparencySysDiagnoseData:]_block_invoke.262
- ___50-[TransparencyDaemon transparencySysDiagnoseData:]_block_invoke.268
- ___50-[TransparencyDaemon transparencySysDiagnoseData:]_block_invoke_2.264
- ___50-[TransparencyDaemon transparencySysDiagnoseData:]_block_invoke_2.280
- ___52-[TransparencyDaemon performAndWaitForSelfValidate:]_block_invoke.299
- ___56-[KTOptInManager setOptInState:detailedCompletionBlock:]_block_invoke.243
- ___56-[KTOptInManager setOptInState:detailedCompletionBlock:]_block_invoke.246
- ___56-[KTOptInManager setOptInState:detailedCompletionBlock:]_block_invoke_2.247
- ___57-[TransparencyDaemon transparencyDumpKTRegistrationData:]_block_invoke.347
- ___57-[TransparencyDaemon transparencyTriggerIDSRegistration:]_block_invoke.327
- ___58-[TransparencyDaemon getOptInForURI:application:complete:]_block_invoke.376
- ___58-[TransparencyDaemon transparencyClearKTRegistrationData:]_block_invoke.353
- ___59-[KTOptInManager changeOptInState:detailedCompletionBlock:]_block_invoke.252
- ___59-[KTOptInManager changeOptInState:detailedCompletionBlock:]_block_invoke.255
- ___59-[KTOptInManager changeOptInState:detailedCompletionBlock:]_block_invoke_2.256
- ___59-[TransparencyDaemon getOptInStateForApplication:complete:]_block_invoke.385
- ___59-[TransparencyDaemon transparencyGetKTSignatures:complete:]_block_invoke.350
- ___60-[TransparencyDaemon changeOptInState:application:complete:]_block_invoke.370
- ___60-[TransparencyDaemon transparencyTriggerOperation:complete:]_block_invoke.367
- ___61-[TransparencyDaemon transparencyCheckKTAccountKey:complete:]_block_invoke.330
- ___63-[TransparencyDaemon transparencyPerformRegistrationSignature:]_block_invoke.344
- ___65-[TransparencyDaemon clearOptInStateForURI:application:complete:]_block_invoke.388
- ___69-[TransparencyDaemon transparencyCloudDeviceAdd:clientData:complete:]_block_invoke.391
- ___72-[TransparencyDaemon transparencyCloudDeviceRemove:clientData:complete:]_block_invoke.394
- ___77-[TransparencyDaemon setOptInForURI:application:state:smtTimestamp:complete:]_block_invoke.379
- ___94-[TransparencyStaticKey updateStaticKeyDatabaseForContact:peerPublicAccountIdentity:complete:]_block_invoke
- ___94-[TransparencyStaticKey updateStaticKeyDatabaseForContact:peerPublicAccountIdentity:complete:]_block_invoke.339
- ___94-[TransparencyStaticKey updateStaticKeyDatabaseForContact:peerPublicAccountIdentity:complete:]_block_invoke.345
- ___94-[TransparencyStaticKey updateStaticKeyDatabaseForContact:peerPublicAccountIdentity:complete:]_block_invoke_2
- ___94-[TransparencyStaticKey updateStaticKeyDatabaseForContact:peerPublicAccountIdentity:complete:]_block_invoke_2.340
- ___94-[TransparencyStaticKey updateStaticKeyDatabaseForContact:peerPublicAccountIdentity:complete:]_block_invoke_2.346
- ___block_descriptor_40_e8_32bs_e45_v24?0"KTIDStaticKeyStoreEntry"8"NSError"16ls32l8
- ___block_literal_global.233
- ___block_literal_global.240
- ___block_literal_global.245
- ___block_literal_global.247
- ___block_literal_global.249
- ___block_literal_global.253
- ___block_literal_global.254
- ___block_literal_global.256
- ___block_literal_global.258
- ___block_literal_global.267
- ___block_literal_global.268
- ___block_literal_global.275
- ___block_literal_global.277
- ___block_literal_global.284
- ___block_literal_global.286
- ___block_literal_global.293
- ___block_literal_global.295
- ___block_literal_global.298
- ___block_literal_global.301
- ___block_literal_global.303
- ___block_literal_global.306
- ___block_literal_global.309
- ___block_literal_global.320
- ___block_literal_global.326
- ___block_literal_global.335
- ___block_literal_global.338
- ___block_literal_global.340
- ___block_literal_global.343
- ___block_literal_global.346
- ___block_literal_global.349
- ___block_literal_global.352
- ___block_literal_global.355
- ___block_literal_global.358
- ___block_literal_global.366
- ___block_literal_global.369
- ___block_literal_global.372
- ___block_literal_global.375
- ___block_literal_global.378
- ___block_literal_global.381
- ___block_literal_global.384
- ___block_literal_global.387
- ___block_literal_global.390
- ___block_literal_global.393
- _objc_msgSend$ktAccountPublicIDWithString:error:
- _objc_msgSend$transparencyTriggerSelfValidate:
CStrings:
+ "\x0e"
+ "IDSDisable"
+ "IDSServerBagChangedNotification"
+ "ServerOptInFetch"
+ "T@\"NSString\",&,V_dsid"
+ "T@\"NSString\",?,R,C"
+ "TransparencyErrorIDSRegistrationTimeout"
+ "TransparencyErrorKTDisabled"
+ "Unknown checkIDSRegistration error: %@"
+ "_dsid"
+ "app: %@ sig: %d created: %@ signed: %@ uploaded: %@ altDSID: %@[%@] push: %@"
+ "calendarWithIdentifier:"
+ "components:fromDate:"
+ "dateFromComponents:"
+ "dsid"
+ "kt_fuzzyDate"
+ "setDsid:"
+ "timeZoneForSecondsFromGMT:"
+ "triggerSelfValidate:"
+ "updateContact:"
+ "waitForIDSRegistration:"
- "\r"
- "app: %@ sig: %d created: %@ signed: %@ uploaded: %@ altDSID: %@ push: %@"
- "transparencyTriggerSelfValidate:"
- "updateStaticKeyDatabaseForContact error: %@"
- "updateStaticKeyDatabaseForContact:peerPublicAccountIdentity:complete:"

```
