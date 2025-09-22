## Transparency

> `/System/Library/PrivateFrameworks/Transparency.framework/Transparency`

```diff

-1033.62.3.0.0
+1033.80.17.0.1
   __TEXT.__text: 0x33b5c
   __TEXT.__auth_stubs: 0x650
   __TEXT.__objc_methlist: 0x2b3c
-  __TEXT.__cstring: 0x1d8b
+  __TEXT.__cstring: 0x1d9a
   __TEXT.__const: 0x160
   __TEXT.__gcc_except_tab: 0x4a0
   __TEXT.__oslogstring: 0x16a0

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x4fc8
   __DATA_CONST.__objc_selrefs: 0x1810
-  __AUTH_CONST.__cfstring: 0x2f00
+  __AUTH_CONST.__cfstring: 0x2f20
   __AUTH_CONST.__objc_const: 0x670
-  __AUTH_CONST.__const: 0xce0
+  __AUTH_CONST.__const: 0xd20
   __AUTH_CONST.__objc_intobj: 0x150
   __AUTH_CONST.__auth_got: 0x338
   __AUTH.__objc_data: 0x370

   __DATA.__objc_classrefs: 0x238
   __DATA.__objc_superrefs: 0x108
   __DATA.__objc_ivar: 0x2ac
-  __DATA.__data: 0x590
+  __DATA.__data: 0x598
   __DATA.__bss: 0x20
   __DATA.__common: 0x8
-  __DATA_DIRTY.__const: 0x1080
+  __DATA_DIRTY.__const: 0x1040
   __DATA_DIRTY.__objc_const: 0x1238
   __DATA_DIRTY.__objc_data: 0xbe0
   __DATA_DIRTY.__bss: 0x198

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: BA760187-73BB-3B85-B23C-FFA9EA196CC7
+  UUID: 5265D03E-9FCC-3AEF-B9F5-9568277E6BB5
   Functions: 1417
-  Symbols:   4873
-  CStrings:  2266
+  Symbols:   4874
+  CStrings:  2268
 
Symbols:
+ ___125-[TransparencyDaemon replaySelfValidate:application:pcsAccountKey:queryRequest:queryResponse:responseTime:completionHandler:]_block_invoke.321
+ ___40-[TransparencyDaemon getAllOptInStates:]_block_invoke.382
+ ___44-[TransparencyDaemon configurationBagFetch:]_block_invoke.250
+ ___44-[TransparencyDaemon transparencyFetchIDMS:]_block_invoke.290
+ ___44-[TransparencyDaemon transparencyFetchSelf:]_block_invoke.296
+ ___44-[TransparencyDaemon transparencyIDSRepair:]_block_invoke.254
+ ___44-[TransparencyDaemon transparencyIDSRepair:]_block_invoke_2.255
+ ___45-[TransparencyDaemon getOptInState:complete:]_block_invoke.373
+ ___45-[TransparencyDaemon maybeUpdateMonitorState]_block_invoke.304
+ ___45-[TransparencyDaemon maybeUpdateMonitorState]_block_invoke_2.307
+ ___46-[TransparencyDaemon transparencySysDiagnose:]_block_invoke.258
+ ___47-[TransparencyDaemon transparencyCloudDevices:]_block_invoke.356
+ ___47-[TransparencyDaemon transparencyValidateSelf:]_block_invoke.293
+ ___49-[TransparencyDaemon transparencyCheckIDSHealth:]_block_invoke.336
+ ___49-[TransparencyDaemon transparencyCheckIDSHealth:]_block_invoke_2.338
+ ___49-[TransparencyDaemon transparencyIDMSDeviceList:]_block_invoke.312
+ ___49-[TransparencyDaemon transparencyIDMSDeviceList:]_block_invoke_2.314
+ ___50-[TransparencyDaemon transparencyFetchPublicKeys:]_block_invoke.324
+ ___50-[TransparencyDaemon transparencyIDSRegistration:]_block_invoke.341
+ ___50-[TransparencyDaemon transparencySysDiagnoseData:]_block_invoke.262
+ ___50-[TransparencyDaemon transparencySysDiagnoseData:]_block_invoke.268
+ ___50-[TransparencyDaemon transparencySysDiagnoseData:]_block_invoke_2.264
+ ___50-[TransparencyDaemon transparencySysDiagnoseData:]_block_invoke_2.280
+ ___52-[TransparencyDaemon performAndWaitForSelfValidate:]_block_invoke.299
+ ___57-[TransparencyDaemon transparencyDumpKTRegistrationData:]_block_invoke.347
+ ___57-[TransparencyDaemon transparencyTriggerIDSRegistration:]_block_invoke.327
+ ___58-[TransparencyDaemon getOptInForURI:application:complete:]_block_invoke.376
+ ___58-[TransparencyDaemon transparencyClearKTRegistrationData:]_block_invoke.353
+ ___59-[TransparencyDaemon getOptInStateForApplication:complete:]_block_invoke.385
+ ___59-[TransparencyDaemon transparencyGetKTSignatures:complete:]_block_invoke.350
+ ___60-[TransparencyDaemon changeOptInState:application:complete:]_block_invoke.370
+ ___60-[TransparencyDaemon transparencyTriggerOperation:complete:]_block_invoke.367
+ ___61-[TransparencyDaemon transparencyCheckKTAccountKey:complete:]_block_invoke.330
+ ___63-[TransparencyDaemon transparencyPerformRegistrationSignature:]_block_invoke.344
+ ___65-[TransparencyDaemon clearOptInStateForURI:application:complete:]_block_invoke.388
+ ___69-[TransparencyDaemon transparencyCloudDeviceAdd:clientData:complete:]_block_invoke.391
+ ___72-[TransparencyDaemon transparencyCloudDeviceRemove:clientData:complete:]_block_invoke.394
+ ___77-[TransparencyDaemon setOptInForURI:application:state:smtTimestamp:complete:]_block_invoke.379
+ ___block_literal_global.253
+ ___block_literal_global.257
+ ___block_literal_global.267
+ ___block_literal_global.301
+ ___block_literal_global.309
+ ___block_literal_global.335
+ ___block_literal_global.358
+ ___block_literal_global.393
+ _kTransparencyTriggerOperationBAACertFetcher
- ___125-[TransparencyDaemon replaySelfValidate:application:pcsAccountKey:queryRequest:queryResponse:responseTime:completionHandler:]_block_invoke.318
- ___40-[TransparencyDaemon getAllOptInStates:]_block_invoke.379
- ___44-[TransparencyDaemon configurationBagFetch:]_block_invoke.247
- ___44-[TransparencyDaemon transparencyFetchIDMS:]_block_invoke.287
- ___44-[TransparencyDaemon transparencyFetchSelf:]_block_invoke.293
- ___44-[TransparencyDaemon transparencyIDSRepair:]_block_invoke.251
- ___44-[TransparencyDaemon transparencyIDSRepair:]_block_invoke_2.252
- ___45-[TransparencyDaemon getOptInState:complete:]_block_invoke.370
- ___45-[TransparencyDaemon maybeUpdateMonitorState]_block_invoke.301
- ___45-[TransparencyDaemon maybeUpdateMonitorState]_block_invoke_2.304
- ___46-[TransparencyDaemon transparencySysDiagnose:]_block_invoke.255
- ___47-[TransparencyDaemon transparencyCloudDevices:]_block_invoke.353
- ___47-[TransparencyDaemon transparencyValidateSelf:]_block_invoke.290
- ___49-[TransparencyDaemon transparencyCheckIDSHealth:]_block_invoke.333
- ___49-[TransparencyDaemon transparencyCheckIDSHealth:]_block_invoke_2.335
- ___49-[TransparencyDaemon transparencyIDMSDeviceList:]_block_invoke.309
- ___49-[TransparencyDaemon transparencyIDMSDeviceList:]_block_invoke_2.311
- ___50-[TransparencyDaemon transparencyFetchPublicKeys:]_block_invoke.321
- ___50-[TransparencyDaemon transparencyIDSRegistration:]_block_invoke.338
- ___50-[TransparencyDaemon transparencySysDiagnoseData:]_block_invoke.259
- ___50-[TransparencyDaemon transparencySysDiagnoseData:]_block_invoke.265
- ___50-[TransparencyDaemon transparencySysDiagnoseData:]_block_invoke_2.261
- ___50-[TransparencyDaemon transparencySysDiagnoseData:]_block_invoke_2.277
- ___52-[TransparencyDaemon performAndWaitForSelfValidate:]_block_invoke.296
- ___57-[TransparencyDaemon transparencyDumpKTRegistrationData:]_block_invoke.344
- ___57-[TransparencyDaemon transparencyTriggerIDSRegistration:]_block_invoke.324
- ___58-[TransparencyDaemon getOptInForURI:application:complete:]_block_invoke.373
- ___58-[TransparencyDaemon transparencyClearKTRegistrationData:]_block_invoke.350
- ___59-[TransparencyDaemon getOptInStateForApplication:complete:]_block_invoke.382
- ___59-[TransparencyDaemon transparencyGetKTSignatures:complete:]_block_invoke.347
- ___60-[TransparencyDaemon changeOptInState:application:complete:]_block_invoke.367
- ___60-[TransparencyDaemon transparencyTriggerOperation:complete:]_block_invoke.364
- ___61-[TransparencyDaemon transparencyCheckKTAccountKey:complete:]_block_invoke.327
- ___63-[TransparencyDaemon transparencyPerformRegistrationSignature:]_block_invoke.341
- ___65-[TransparencyDaemon clearOptInStateForURI:application:complete:]_block_invoke.385
- ___69-[TransparencyDaemon transparencyCloudDeviceAdd:clientData:complete:]_block_invoke.388
- ___72-[TransparencyDaemon transparencyCloudDeviceRemove:clientData:complete:]_block_invoke.391
- ___77-[TransparencyDaemon setOptInForURI:application:state:smtTimestamp:complete:]_block_invoke.376
- ___block_literal_global.250
- ___block_literal_global.264
- ___block_literal_global.300
- ___block_literal_global.313
- ___block_literal_global.315
- ___block_literal_global.317
- ___block_literal_global.332
- ___block_literal_global.337
- ___block_literal_global.363
CStrings:
+ "BAACertFetcher"

```
