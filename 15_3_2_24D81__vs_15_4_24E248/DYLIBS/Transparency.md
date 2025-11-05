## Transparency

> `/System/Library/PrivateFrameworks/Transparency.framework/Versions/A/Transparency`

```diff

-1218.80.18.0.0
-  __TEXT.__text: 0x46ecc
-  __TEXT.__auth_stubs: 0x7d0
-  __TEXT.__objc_methlist: 0x2f24
-  __TEXT.__cstring: 0x2203
+1218.100.244.0.0
+  __TEXT.__text: 0x488c0
+  __TEXT.__auth_stubs: 0x7c0
+  __TEXT.__objc_methlist: 0x3adc
+  __TEXT.__cstring: 0x2287
   __TEXT.__const: 0xaf6
-  __TEXT.__gcc_except_tab: 0x520
-  __TEXT.__oslogstring: 0x1845
+  __TEXT.__gcc_except_tab: 0x51c
+  __TEXT.__oslogstring: 0x1944
   __TEXT.__swift5_typeref: 0x1eb
   __TEXT.__swift5_reflstr: 0xd1
   __TEXT.__swift5_assocty: 0x30

   __TEXT.__swift5_fieldmd: 0x278
   __TEXT.__swift5_proto: 0x9c
   __TEXT.__swift5_types: 0x2c
-  __TEXT.__unwind_info: 0x1590
+  __TEXT.__unwind_info: 0x1618
   __TEXT.__eh_frame: 0x2b0
-  __TEXT.__objc_classname: 0x626
-  __TEXT.__objc_methname: 0x675a
-  __TEXT.__objc_methtype: 0x1b78
-  __TEXT.__objc_stubs: 0x4f80
-  __DATA_CONST.__got: 0x340
+  __TEXT.__objc_classname: 0x66c
+  __TEXT.__objc_methname: 0x69e4
+  __TEXT.__objc_methtype: 0x1c4e
+  __TEXT.__objc_stubs: 0x5140
+  __DATA_CONST.__got: 0x360
   __DATA_CONST.__const: 0x660
-  __DATA_CONST.__objc_classlist: 0x1a8
+  __DATA_CONST.__objc_classlist: 0x1b8
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x19e0
+  __DATA_CONST.__objc_selrefs: 0x1b08
   __DATA_CONST.__objc_protorefs: 0x28
-  __DATA_CONST.__objc_superrefs: 0x128
-  __AUTH_CONST.__auth_got: 0x3f8
-  __AUTH_CONST.__const: 0x3380
-  __AUTH_CONST.__cfstring: 0x33e0
-  __AUTH_CONST.__objc_const: 0x71e8
+  __DATA_CONST.__objc_superrefs: 0x138
+  __AUTH_CONST.__auth_got: 0x3f0
+  __AUTH_CONST.__const: 0x33c0
+  __AUTH_CONST.__cfstring: 0x3480
+  __AUTH_CONST.__objc_const: 0x6290
   __AUTH_CONST.__objc_intobj: 0x150
-  __AUTH.__objc_data: 0xff0
+  __AUTH.__objc_data: 0x1090
   __AUTH.__data: 0x228
-  __DATA.__objc_ivar: 0x2d4
+  __DATA.__objc_ivar: 0x2ec
   __DATA.__data: 0x750
   __DATA.__bss: 0x1660
   __DATA.__common: 0x10

   - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 2563067C-7FD0-3D5C-8FB9-A9F6D7EDCF25
-  Functions: 1870
-  Symbols:   3870
-  CStrings:  2442
+  UUID: FD966FEB-7EC6-3232-B1A1-98979803AAFA
+  Functions: 2142
+  Symbols:   4199
+  CStrings:  2488
 
Symbols:
+ +[SWTransparencyOperationConfiguration supportsSecureCoding]
+ +[SoftwareTransparency invalidResponse]
+ +[SoftwareTransparency isAvailable]
+ +[SoftwareTransparency isAvailable].cold.1
+ +[TransparencyAnalytics analyticsApplications].cold.1
+ +[TransparencyApplication applicationIdentifierForValue:].cold.1
+ +[TransparencyApplication applicationPrefixForIdentifier:].cold.1
+ +[TransparencyApplication applicationValueForIdentifier:].cold.1
+ +[TransparencyApplication idsServiceForIdentifier:].cold.1
+ +[TransparencySelfValidationStatus supportsSecureCoding]
+ +[TransparencySettings automatedDeviceGroup].cold.1
+ +[TransparencySettings devicePlatform].cold.1
+ +[TransparencySettings deviceUserAgent].cold.1
+ +[TransparencySettings isAccountsInQA].cold.1
+ +[TransparencyStaticKey sasTTR:toHandle:pushToken:complete:]
+ +[TransparencyXPCConnection invokeAccountsSupportWithBlock:errorHandler:].cold.1
+ +[TransparencyXPCConnection invokeIDSSupportWithBlock:errorHandler:].cold.1
+ +[TransparencyXPCConnection invokeIDSSupportWithBlock:errorHandler:].cold.2
+ +[TransparencyXPCConnection invokeIDSXPCWithBlock:errorHandler:].cold.1
+ +[TransparencyXPCConnection invokeIDSXPCWithBlock:errorHandler:].cold.2
+ +[TransparencyXPCConnection invokeXPCWithBlock:synchronous:errorHandler:].cold.1
+ +[TransparencyXPCConnection invokeXPCWithBlock:synchronous:errorHandler:].cold.2
+ -[KTAccountKey initWithApplication:].cold.1
+ -[KTAccountPublicID initWithCoder:].cold.1
+ -[KTAccountPublicID initWithCoder:].cold.2
+ -[KTAccountPublicID initWithCoder:].cold.3
+ -[KTLoggableData copyWithZone:]
+ -[KTLoggableData isInputsEqual:]
+ -[KTNSErrorValueTransformer reverseTransformedValue:].cold.1
+ -[KTNSErrorValueTransformer transformedValue:].cold.1
+ -[KTOptInManager initWithApplication:].cold.1
+ -[KTSelfValidationURIDiagnostics initWithCoder:].cold.1
+ -[KTSelfValidationURIDiagnostics initWithCoder:].cold.2
+ -[KTSelfValidationURIDiagnostics initWithCoder:].cold.3
+ -[KTStatus initWithApplication:].cold.1
+ -[KTVerifier getDisplayStatusForResults:isSelfOptedIn:].cold.1
+ -[KTVerifier initWithApplication:].cold.1
+ -[KTVerifierResult updateWithStaticKeyEnforced:isFailureIgnoredForDate:].cold.1
+ -[NSDate(TransparencyDate) kt_fuzzyDate].cold.1
+ -[SWTransparencyOperationConfiguration .cxx_destruct]
+ -[SWTransparencyOperationConfiguration encodeWithCoder:]
+ -[SWTransparencyOperationConfiguration initWithCoder:]
+ -[SWTransparencyOperationConfiguration initWithName:]
+ -[SWTransparencyOperationConfiguration isEqual:]
+ -[SWTransparencyOperationConfiguration name]
+ -[SWTransparencyOperationConfiguration qualityOfService]
+ -[SWTransparencyOperationConfiguration setName:]
+ -[SWTransparencyOperationConfiguration setQualityOfService:]
+ -[SWTransparencyOperationConfiguration setTimeout:]
+ -[SWTransparencyOperationConfiguration timeout]
+ -[SoftwareTransparency verifyExpiringProofs:forDigest:configuration:completion:]
+ -[SoftwareTransparency verifyExpiringProofs:forDigest:configuration:counter:completion:]
+ -[SoftwareTransparency verifyExpiringProofs:forObject:configuration:completion:]
+ -[TransparencyAnalytics addMultiSamplerForName:withTimeInterval:block:].cold.1
+ -[TransparencyAnalytics logRockwellForEventNamed:withAttributes:]
+ -[TransparencyAnalytics removeMultiSamplerForName:].cold.1
+ -[TransparencyApplication initWithIdentifier:].cold.1
+ -[TransparencyCloudDevice setUploadedAt:]
+ -[TransparencyCloudDevice uploadedAt]
+ -[TransparencyDaemon networkKTQuery:application:complete:]
+ -[TransparencyDaemon validateSelfForThisDeviceForApplication:pushToken:complete:]
+ -[TransparencySFAnalytics backgroundPerform:].cold.1
+ -[TransparencySFAnalytics logRockwellForEventNamed:withAttributes:]
+ -[TransparencySelfValidationStatus .cxx_destruct]
+ -[TransparencySelfValidationStatus description]
+ -[TransparencySelfValidationStatus encodeWithCoder:]
+ -[TransparencySelfValidationStatus initWithCoder:]
+ -[TransparencySelfValidationStatus initWithStatus:pushToken:]
+ -[TransparencySelfValidationStatus loggableDatas]
+ -[TransparencySelfValidationStatus pushToken]
+ -[TransparencySelfValidationStatus setLoggableDatas:]
+ -[TransparencySelfValidationStatus setPushToken:]
+ -[TransparencySelfValidationStatus setStatus:]
+ -[TransparencySelfValidationStatus status]
+ -[TransparencySettings testingPeerValidationFailing]
+ GCC_except_table139
+ GCC_except_table178
+ GCC_except_table38
+ GCC_except_table99
+ OBJC_IVAR_$_SWTransparencyOperationConfiguration._name
+ OBJC_IVAR_$_SWTransparencyOperationConfiguration._qualityOfService
+ OBJC_IVAR_$_SWTransparencyOperationConfiguration._timeout
+ OBJC_IVAR_$_TransparencyCloudDevice._uploadedAt
+ OBJC_IVAR_$_TransparencySelfValidationStatus._loggableDatas
+ OBJC_IVAR_$_TransparencySelfValidationStatus._pushToken
+ OBJC_IVAR_$_TransparencySelfValidationStatus._status
+ _OBJC_CLASS_$_SWTransparencyOperationConfiguration
+ _OBJC_CLASS_$_TransparencySelfValidationStatus
+ _OBJC_METACLASS_$_SWTransparencyOperationConfiguration
+ _OBJC_METACLASS_$_TransparencySelfValidationStatus
+ __125-[TransparencyDaemon replaySelfValidate:application:pcsAccountKey:queryRequest:queryResponse:responseTime:completionHandler:]_block_invoke.379
+ __125-[TransparencyDaemon replaySelfValidate:application:pcsAccountKey:queryRequest:queryResponse:responseTime:completionHandler:]_block_invoke.cold.1
+ __19-[KTStatus status:]_block_invoke.255.cold.1
+ __22-[KTStatus getStatus:]_block_invoke.269.cold.1
+ __22-[KTStatus getStatus:]_block_invoke.cold.1
+ __22-[KTStatus getStatus:]_block_invoke.cold.2
+ __24-[KTAccountKey rollKey:]_block_invoke.49.cold.1
+ __24-[KTAccountKey rollKey:]_block_invoke.49.cold.2
+ __24-[KTAccountKey rollKey:]_block_invoke.60.cold.1
+ __24-[KTAccountKey rollKey:]_block_invoke.cold.1
+ __24-[KTAccountKey rollKey:]_block_invoke.cold.2
+ __25-[KTVerifier clearState:]_block_invoke.cold.1
+ __26-[KTStatus getSelfStatus:]_block_invoke.280.cold.1
+ __26-[KTStatus getSelfStatus:]_block_invoke.cold.1
+ __26-[KTStatus getSelfStatus:]_block_invoke.cold.2
+ __29-[KTVerifier forceDutyCycle:]_block_invoke.cold.1
+ __30-[KTVerifier copyDaemonState:]_block_invoke.cold.1
+ __31-[KTIDStaticKeyStore listKTID:]_block_invoke.176.cold.1
+ __31-[KTOptInManager getOptInState]_block_invoke.222.cold.1
+ __31-[KTOptInManager getOptInState]_block_invoke.229.cold.1
+ __31-[KTOptInManager getOptInState]_block_invoke.cold.1
+ __31-[KTOptInManager getOptInState]_block_invoke.cold.2
+ __32-[KTVerifier copyKeyStoreState:]_block_invoke.cold.1
+ __32-[KTVerifier forceConfigUpdate:]_block_invoke.cold.1
+ __33+[KTAccountKey accountPublicKey:]_block_invoke.6.cold.1
+ __34-[KTIDStaticKeyStore triggerSync:]_block_invoke_3.cold.1
+ __35-[KTVerifier clearPeerCache:error:]_block_invoke.cold.1
+ __35-[KTVerifier copyApplicationState:]_block_invoke.cold.1
+ __36+[KTPeerOverrides listPeerOverrides]_block_invoke.42.cold.1
+ __36-[KTAccountKey accountPublicKeyInfo]_block_invoke.19.cold.1
+ __36-[KTAccountKey accountPublicKeyInfo]_block_invoke.26.cold.1
+ __36-[KTAccountKey accountPublicKeyInfo]_block_invoke.cold.1
+ __36-[KTAccountKey accountPublicKeyInfo]_block_invoke.cold.2
+ __36-[KTIDStaticKeyStore resetCloudKit:]_block_invoke_3.cold.1
+ __36-[KTVerifier configurationBagFetch:]_block_invoke.cold.1
+ __37-[KTVerifier forceApplicationConfig:]_block_invoke.cold.1
+ __37-[KTVerifier forceCloudConfigUpdate:]_block_invoke.cold.1
+ __38-[KTVerifier copyDataStoreStatistics:]_block_invoke.cold.1
+ __39-[KTVerifier clearPublicKeyStoreState:]_block_invoke.cold.1
+ __39-[KTVerifier ignoreFailure:uuid:error:]_block_invoke.cold.1
+ __40-[KTVerifier copyApplicationTranscript:]_block_invoke.cold.1
+ __40-[KTVerifier copyDeviceStatus:complete:]_block_invoke.cold.1
+ __40-[KTVerifier copyKeyStoreStateFromDisk:]_block_invoke.cold.1
+ __40-[KTVerifier forceApplicationKeysFetch:]_block_invoke.cold.1
+ __40-[TransparencyAnalytics setupCollection]_block_invoke.cold.1
+ __40-[TransparencyDaemon getAllOptInStates:]_block_invoke.460
+ __40-[TransparencyDaemon getAllOptInStates:]_block_invoke.cold.1
+ __40-[TransparencyStaticKey listKTSessions:]_block_invoke.331.cold.1
+ __40-[TransparencyStaticKey listKTSessions:]_block_invoke.cold.1
+ __41-[KTOptInManager waitForIDSRegistration:]_block_invoke.253.cold.1
+ __41-[KTOptInManager waitForIDSRegistration:]_block_invoke.cold.1
+ __41-[KTVerifier copyLogClientConfiguration:]_block_invoke.cold.1
+ __42-[KTIDStaticKeyStore findByContact:error:]_block_invoke.cold.1
+ __42-[KTIDStaticKeyStore findByContact:error:]_block_invoke_2.162.cold.1
+ __42-[KTVerifier clearLogClientConfiguration:]_block_invoke.cold.1
+ __42-[KTVerifier forceValidateUUID:uri:block:]_block_invoke.cold.1
+ __42-[KTVerifier resetRequestToPending:block:]_block_invoke.cold.1
+ __43+[KTOptInManager getOptInState:completion:]_block_invoke.207.cold.1
+ __43+[KTOptInManager getOptInState:completion:]_block_invoke.cold.1
+ __43-[TransparencyDaemon setOSUpdate:complete:]_block_invoke.480
+ __43-[TransparencyDaemon setOSUpdate:complete:]_block_invoke.cold.1
+ __44-[KTAccountKey signDataCIP:completionBlock:]_block_invoke.38.cold.1
+ __44-[KTAccountKey signDataCIP:completionBlock:]_block_invoke.cold.1
+ __44-[KTAccountKey signDataCIP:completionBlock:]_block_invoke.cold.2
+ __44-[KTIDStaticKeyStore findKeyByHandle:error:]_block_invoke.cold.1
+ __44-[KTIDStaticKeyStore findKeyByHandle:error:]_block_invoke_2.150.cold.1
+ __44-[KTVerifier ignoreFailureForResults:error:]_block_invoke.cold.1
+ __44-[TransparencyDaemon configurationBagFetch:]_block_invoke.298
+ __44-[TransparencyDaemon configurationBagFetch:]_block_invoke.cold.1
+ __44-[TransparencyDaemon transparencyFetchIDMS:]_block_invoke.345
+ __44-[TransparencyDaemon transparencyFetchIDMS:]_block_invoke.cold.1
+ __44-[TransparencyDaemon transparencyFetchSelf:]_block_invoke.351
+ __44-[TransparencyDaemon transparencyFetchSelf:]_block_invoke.cold.1
+ __44-[TransparencyDaemon transparencyIDSRepair:]_block_invoke.304
+ __44-[TransparencyDaemon transparencyIDSRepair:]_block_invoke.cold.1
+ __44-[TransparencyDaemon transparencyIDSRepair:]_block_invoke_2.305
+ __45-[KTIDStaticKeyStore findByIdentifier:error:]_block_invoke_3.cold.1
+ __45-[KTIDStaticKeyStore setupCloudSchema:error:]_block_invoke.190.cold.1
+ __45-[KTVerifier batchQuery:userInitiated:block:]_block_invoke.cold.1
+ __45-[TransparencyDaemon getOptInState:complete:]_block_invoke.451
+ __45-[TransparencyDaemon getOptInState:complete:]_block_invoke.cold.1
+ __45-[TransparencyDaemon maybeUpdateMonitorState]_block_invoke.359
+ __45-[TransparencyDaemon maybeUpdateMonitorState]_block_invoke.359.cold.1
+ __45-[TransparencyDaemon maybeUpdateMonitorState]_block_invoke.cold.1
+ __45-[TransparencyDaemon maybeUpdateMonitorState]_block_invoke_2.362
+ __45-[TransparencyXPCConnection createConnection]_block_invoke.5.cold.1
+ __45-[TransparencyXPCConnection createConnection]_block_invoke.cold.1
+ __46+[TransparencySettings jsonDictFromPlistDict:]_block_invoke.cold.1
+ __46+[TransparencySettings jsonDictFromPlistDict:]_block_invoke.cold.2
+ __46-[KTIDStaticKeyStore removeEntryByKDID:error:]_block_invoke.131.cold.1
+ __46-[KTIDStaticKeyStore removeEntryByKDID:error:]_block_invoke.cold.1
+ __46-[KTStatus ignoreFailedEvent:completionBlock:]_block_invoke.311.cold.1
+ __46-[KTStatus ignoreFailedEvent:completionBlock:]_block_invoke.cold.1
+ __46-[KTStatus ignoreFailedEvent:completionBlock:]_block_invoke.cold.2
+ __46-[KTVerifier markFailureSeenForResults:error:]_block_invoke.cold.1
+ __46-[TransparencyDaemon transparencySysDiagnose:]_block_invoke.308
+ __46-[TransparencyDaemon transparencySysDiagnose:]_block_invoke.cold.1
+ __47-[KTStatus ignoreFailedEvents:completionBlock:]_block_invoke.320.cold.1
+ __47-[KTStatus ignoreFailedEvents:completionBlock:]_block_invoke.cold.1
+ __47-[KTStatus ignoreFailedEvents:completionBlock:]_block_invoke.cold.2
+ __47-[TransparencyDaemon transparencyCloudDevices:]_block_invoke.430
+ __47-[TransparencyDaemon transparencyCloudDevices:]_block_invoke.cold.1
+ __47-[TransparencyDaemon transparencyValidateSelf:]_block_invoke.348
+ __47-[TransparencyDaemon transparencyValidateSelf:]_block_invoke.cold.1
+ __48+[TransparencySettings jsonArrayFromPlistArray:]_block_invoke.cold.1
+ __48-[KTOptInManager getOptInState:completionBlock:]_block_invoke.cold.1
+ __48-[KTOptInManager getOptInState:completionBlock:]_block_invoke.cold.2
+ __48-[KTStatus errorForFailedEvent:completionBlock:]_block_invoke.293.cold.1
+ __48-[KTStatus errorForFailedEvent:completionBlock:]_block_invoke.cold.1
+ __48-[KTStatus errorForFailedEvent:completionBlock:]_block_invoke.cold.2
+ __48-[TransparencyDaemon clearEligibilityOverrides:]_block_invoke.488
+ __48-[TransparencyDaemon clearEligibilityOverrides:]_block_invoke.cold.1
+ __48-[TransparencyDaemon clearPeerState:uris:block:]_block_invoke.cold.1
+ __49+[KTPeerOverrides clearPeerOverride:application:]_block_invoke.34.cold.1
+ __49-[KTIDStaticKeyStore removeEntryByContact:error:]_block_invoke.cold.1
+ __49-[KTIDStaticKeyStore removeEntryByContact:error:]_block_invoke_2.144.cold.1
+ __49-[KTIDStaticKeyStore validateByIdentifier:error:]_block_invoke_3.cold.1
+ __49-[TransparencyAnalytics logSuccessForEventNamed:]_block_invoke.119
+ __49-[TransparencyDaemon reportEligibility:complete:]_block_invoke.491
+ __49-[TransparencyDaemon reportEligibility:complete:]_block_invoke.cold.1
+ __49-[TransparencyDaemon transparencyCheckIDSHealth:]_block_invoke.408
+ __49-[TransparencyDaemon transparencyCheckIDSHealth:]_block_invoke.412
+ __49-[TransparencyDaemon transparencyCheckIDSHealth:]_block_invoke.cold.1
+ __49-[TransparencyDaemon transparencyIDMSDeviceList:]_block_invoke.367
+ __49-[TransparencyDaemon transparencyIDMSDeviceList:]_block_invoke.371
+ __49-[TransparencyDaemon transparencyIDMSDeviceList:]_block_invoke.371.cold.1
+ __49-[TransparencyDaemon transparencyIDMSDeviceList:]_block_invoke.cold.1
+ __49-[TransparencyDaemon transparencyIDMSDeviceList:]_block_invoke_2.374
+ __49-[TransparencyStaticKey setupKTSession:complete:]_block_invoke.306.cold.1
+ __49-[TransparencyStaticKey setupKTSession:complete:]_block_invoke.cold.1
+ __50+[TransparencyGossip sthsReceivedFromPeers:error:]_block_invoke.22.cold.1
+ __50+[TransparencyGossip sthsReceivedFromPeers:error:]_block_invoke.cold.1
+ __50+[TransparencyGossip sthsReceivedFromPeers:error:]_block_invoke.cold.2
+ __50-[KTStatus errorsForFailedEvents:completionBlock:]_block_invoke.302.cold.1
+ __50-[KTStatus errorsForFailedEvents:completionBlock:]_block_invoke.cold.1
+ __50-[KTStatus errorsForFailedEvents:completionBlock:]_block_invoke.cold.2
+ __50-[TransparencyDaemon transparencyFetchPublicKeys:]_block_invoke.382
+ __50-[TransparencyDaemon transparencyFetchPublicKeys:]_block_invoke.cold.1
+ __50-[TransparencyDaemon transparencyIDSRegistration:]_block_invoke.415
+ __50-[TransparencyDaemon transparencyIDSRegistration:]_block_invoke.cold.1
+ __50-[TransparencyDaemon transparencySysDiagnoseData:]_block_invoke.312
+ __50-[TransparencyDaemon transparencySysDiagnoseData:]_block_invoke.314
+ __50-[TransparencyDaemon transparencySysDiagnoseData:]_block_invoke.318
+ __50-[TransparencyDaemon transparencySysDiagnoseData:]_block_invoke.318.cold.1
+ __50-[TransparencyDaemon transparencySysDiagnoseData:]_block_invoke.322
+ __50-[TransparencyDaemon transparencySysDiagnoseData:]_block_invoke.335
+ __50-[TransparencyDaemon transparencySysDiagnoseData:]_block_invoke.cold.1
+ __50-[TransparencyDaemon transparencySysDiagnoseData:]_block_invoke_2.319
+ __50-[TransparencyStaticKey deleteKTSession:complete:]_block_invoke.319.cold.1
+ __50-[TransparencyStaticKey deleteKTSession:complete:]_block_invoke.cold.1
+ __51-[KTVerifier initiateQueryForUris:completionBlock:]_block_invoke.cold.1
+ __51-[TransparencyStaticKey getKTSessionByID:complete:]_block_invoke.347.cold.1
+ __51-[TransparencyStaticKey getKTSessionByID:complete:]_block_invoke.cold.1
+ __52+[TransparencyGossip retrieveCurrentVerifiedTLTSTH:]_block_invoke.11.cold.1
+ __52+[TransparencyGossip retrieveCurrentVerifiedTLTSTH:]_block_invoke.cold.1
+ __52+[TransparencyGossip retrieveCurrentVerifiedTLTSTH:]_block_invoke.cold.2
+ __52-[KTIDStaticKeyStore findByContactIdentifier:error:]_block_invoke.cold.1
+ __52-[KTIDStaticKeyStore findByContactIdentifier:error:]_block_invoke_2.156.cold.1
+ __52-[KTIDStaticKeyStore setErrorCode:forMapping:error:]_block_invoke.182.cold.1
+ __52-[KTVerifier forceValidateUUID:uri:completionBlock:]_block_invoke.cold.1
+ __52-[TransparencyDaemon performAndWaitForSelfValidate:]_block_invoke.354
+ __52-[TransparencyDaemon performAndWaitForSelfValidate:]_block_invoke.cold.1
+ __53+[KTPeerOverrides setPeerOverride:application:state:]_block_invoke.27.cold.1
+ __53-[KTVerifier validatePeers:fetchNow:completionBlock:]_block_invoke.cold.1
+ __54-[KTVerifier validatePeerResult:uuid:completionBlock:]_block_invoke.cold.1
+ __55-[TransparencyDaemon updateIDSRecommendation:complete:]_block_invoke.477
+ __55-[TransparencyDaemon updateIDSRecommendation:complete:]_block_invoke.cold.1
+ __55-[TransparencyStaticKey getKTSessionByHandle:complete:]_block_invoke.cold.1
+ __55-[TransparencyStaticKey getKTSessionByHandle:complete:]_block_invoke_2.338.cold.1
+ __56-[KTIDStaticKeyStore validateByContactIdentifier:error:]_block_invoke_3.cold.1
+ __56-[KTOptInManager setOptInState:detailedCompletionBlock:]_block_invoke.262.cold.1
+ __56-[KTOptInManager setOptInState:detailedCompletionBlock:]_block_invoke_2.cold.1
+ __56-[KTOptInManager setOptInState:detailedCompletionBlock:]_block_invoke_2.cold.2
+ __57-[KTIDStaticKeyStore updateStaticKeyEntry:contact:error:]_block_invoke.121.cold.1
+ __57-[TransparencyDaemon transparencyDumpKTRegistrationData:]_block_invoke.421
+ __57-[TransparencyDaemon transparencyDumpKTRegistrationData:]_block_invoke.cold.1
+ __57-[TransparencyDaemon transparencyTriggerIDSRegistration:]_block_invoke.385
+ __57-[TransparencyDaemon transparencyTriggerIDSRegistration:]_block_invoke.cold.1
+ __58-[TransparencyDaemon getAggregateResult:element:complete:]_block_invoke.494
+ __58-[TransparencyDaemon getAggregateResult:element:complete:]_block_invoke.cold.1
+ __58-[TransparencyDaemon getOptInForURI:application:complete:]_block_invoke.454
+ __58-[TransparencyDaemon getOptInForURI:application:complete:]_block_invoke.cold.1
+ __58-[TransparencyDaemon networkKTQuery:application:complete:]_block_invoke.505
+ __58-[TransparencyDaemon networkKTQuery:application:complete:]_block_invoke.cold.1
+ __58-[TransparencyDaemon transparencyClearKTRegistrationData:]_block_invoke.427
+ __58-[TransparencyDaemon transparencyClearKTRegistrationData:]_block_invoke.cold.1
+ __59-[KTIDStaticKeyStore removeEntryByContactIdentifier:error:]_block_invoke.cold.1
+ __59-[KTIDStaticKeyStore removeEntryByContactIdentifier:error:]_block_invoke_2.138.cold.1
+ __59-[KTOptInManager changeOptInState:detailedCompletionBlock:]_block_invoke.275.cold.1
+ __59-[KTOptInManager changeOptInState:detailedCompletionBlock:]_block_invoke_2.cold.1
+ __59-[KTOptInManager changeOptInState:detailedCompletionBlock:]_block_invoke_2.cold.2
+ __59-[KTVerifier getCachedValidatePeerResults:completionBlock:]_block_invoke.cold.1
+ __59-[TransparencyDaemon clearTapToRadarNotification:complete:]_block_invoke.402
+ __59-[TransparencyDaemon clearTapToRadarNotification:complete:]_block_invoke.cold.1
+ __59-[TransparencyDaemon getOptInStateForApplication:complete:]_block_invoke.463
+ __59-[TransparencyDaemon getOptInStateForApplication:complete:]_block_invoke.cold.1
+ __59-[TransparencyDaemon transparencyGetKTSignatures:complete:]_block_invoke.424
+ __59-[TransparencyDaemon transparencyGetKTSignatures:complete:]_block_invoke.cold.1
+ __60+[TransparencyStaticKey sasTTR:toHandle:pushToken:complete:]_block_invoke.353
+ __60+[TransparencyStaticKey sasTTR:toHandle:pushToken:complete:]_block_invoke.354
+ __60+[TransparencyStaticKey sasTTR:toHandle:pushToken:complete:]_block_invoke.354.cold.1
+ __60+[TransparencyStaticKey sasTTR:toHandle:pushToken:complete:]_block_invoke.cold.1
+ __60+[TransparencyStaticKey sasTTR:toHandle:pushToken:complete:]_block_invoke_2.355
+ __60-[KTVerifier validateEnrollmentResult:uuid:completionBlock:]_block_invoke.cold.1
+ __60-[TransparencyDaemon changeOptInState:application:complete:]_block_invoke.448
+ __60-[TransparencyDaemon changeOptInState:application:complete:]_block_invoke.cold.1
+ __60-[TransparencyDaemon transparencyTriggerOperation:complete:]_block_invoke.443
+ __60-[TransparencyDaemon transparencyTriggerOperation:complete:]_block_invoke.cold.1
+ __61-[KTVerifier invokeXPCSynchronousCallWithBlock:failureBlock:]_block_invoke.cold.1
+ __61-[TransparencyDaemon transparencyCheckKTAccountKey:complete:]_block_invoke.388
+ __61-[TransparencyDaemon transparencyCheckKTAccountKey:complete:]_block_invoke.cold.1
+ __61-[TransparencyDaemon transparencyTriggerTTR:handle:complete:]_block_invoke.391
+ __61-[TransparencyDaemon transparencyTriggerTTR:handle:complete:]_block_invoke.391.cold.1
+ __61-[TransparencyDaemon transparencyTriggerTTR:handle:complete:]_block_invoke.396
+ __61-[TransparencyDaemon transparencyTriggerTTR:handle:complete:]_block_invoke.396.cold.1
+ __61-[TransparencyDaemon transparencyTriggerTTR:handle:complete:]_block_invoke.cold.1
+ __61-[TransparencyDaemon transparencyTriggerTTR:handle:complete:]_block_invoke_2.392
+ __61-[TransparencyDaemon transparencyTriggerTTR:handle:complete:]_block_invoke_2.397
+ __62-[KTVerifier invokeXPCAsynchronousCallWithBlock:failureBlock:]_block_invoke.cold.1
+ __62-[TransparencyAnalytics logResultForEvent:hardFailure:result:]_block_invoke.142
+ __62-[TransparencyAuditorReport getReportForUUID:completionBlock:]_block_invoke.107.cold.1
+ __62-[TransparencyAuditorReport getReportForUUID:completionBlock:]_block_invoke.cold.1
+ __62-[TransparencyAuditorReport getReportForUUID:completionBlock:]_block_invoke.cold.2
+ __63-[TransparencyDaemon setOverrideTimeBetweenReports:completion:]_block_invoke.485
+ __63-[TransparencyDaemon setOverrideTimeBetweenReports:completion:]_block_invoke.cold.1
+ __63-[TransparencyDaemon transparencyPerformRegistrationSignature:]_block_invoke.418
+ __63-[TransparencyDaemon transparencyPerformRegistrationSignature:]_block_invoke.cold.1
+ __64+[TransparencyXPCConnection invokeIDSXPCWithBlock:errorHandler:]_block_invoke.cold.1
+ __64-[TransparencyAuditorReport getReportsForUUIDs:completionBlock:]_block_invoke.119.cold.1
+ __64-[TransparencyAuditorReport getReportsForUUIDs:completionBlock:]_block_invoke.cold.1
+ __64-[TransparencyAuditorReport getReportsForUUIDs:completionBlock:]_block_invoke.cold.2
+ __64-[TransparencyDaemon transparencyTriggerMaybeReportEligibility:]_block_invoke.502
+ __64-[TransparencyDaemon transparencyTriggerMaybeReportEligibility:]_block_invoke.cold.1
+ __65-[TransparencyDaemon clearOptInStateForURI:application:complete:]_block_invoke.466
+ __65-[TransparencyDaemon clearOptInStateForURI:application:complete:]_block_invoke.cold.1
+ __66-[KTVerifier getValidatePeerResult:uuid:fetchNow:completionBlock:]_block_invoke.cold.1
+ __68+[TransparencyXPCConnection invokeIDSSupportWithBlock:errorHandler:]_block_invoke.cold.1
+ __68-[TransparencyAnalytics logHardFailureForEventNamed:withAttributes:]_block_invoke.126
+ __69-[TransparencyDaemon transparencyCloudDeviceAdd:clientData:complete:]_block_invoke.469
+ __69-[TransparencyDaemon transparencyCloudDeviceAdd:clientData:complete:]_block_invoke.cold.1
+ __70+[KTLoggableData loggableDataForDeviceID:application:completionBlock:]_block_invoke.cold.1
+ __70+[KTLoggableData loggableDataForDeviceID:application:completionBlock:]_block_invoke.cold.2
+ __71-[TransparencyAuditorReport makeReport:additionalData:completionBlock:]_block_invoke.128.cold.1
+ __71-[TransparencyAuditorReport makeReport:additionalData:completionBlock:]_block_invoke.cold.1
+ __71-[TransparencyAuditorReport makeReport:additionalData:completionBlock:]_block_invoke.cold.2
+ __72-[TransparencyAuditorReport makeReports:additionalData:completionBlock:]_block_invoke.137.cold.1
+ __72-[TransparencyAuditorReport makeReports:additionalData:completionBlock:]_block_invoke.cold.1
+ __72-[TransparencyAuditorReport makeReports:additionalData:completionBlock:]_block_invoke.cold.2
+ __72-[TransparencyDaemon transparencyCloudDeviceRemove:clientData:complete:]_block_invoke.472
+ __72-[TransparencyDaemon transparencyCloudDeviceRemove:clientData:complete:]_block_invoke.cold.1
+ __73+[TransparencyXPCConnection invokeAccountsSupportWithBlock:errorHandler:]_block_invoke.cold.1
+ __73+[TransparencyXPCConnection invokeXPCWithBlock:synchronous:errorHandler:]_block_invoke.33.cold.1
+ __73+[TransparencyXPCConnection invokeXPCWithBlock:synchronous:errorHandler:]_block_invoke.cold.1
+ __73-[TransparencyDaemon insertResultForElement:samplesAgo:success:complete:]_block_invoke.499
+ __73-[TransparencyDaemon insertResultForElement:samplesAgo:success:complete:]_block_invoke.cold.1
+ __76+[TransparencyXPCConnection invokeXPCSynchronousCallWithBlock:errorHandler:]_block_invoke.cold.1
+ __77-[TransparencyAnalytics logResultForEvent:hardFailure:result:withAttributes:]_block_invoke.148
+ __77-[TransparencyDaemon setOptInForURI:application:state:smtTimestamp:complete:]_block_invoke.457
+ __77-[TransparencyDaemon setOptInForURI:application:state:smtTimestamp:complete:]_block_invoke.cold.1
+ __81-[TransparencyDaemon validateSelfForThisDeviceForApplication:pushToken:complete:]_block_invoke.508
+ __81-[TransparencyDaemon validateSelfForThisDeviceForApplication:pushToken:complete:]_block_invoke.cold.1
+ __88-[KTVerifier validatePeerUri:accountKey:loggableDatas:queryRequest:queryResponse:error:]_block_invoke.cold.1
+ __92-[KTVerifier validatePeerUri:accountKey:loggableDatas:queryResponse:promiseCompletionBlock:]_block_invoke.cold.1
+ __94-[KTIDStaticKeyStore updateStaticKeyEntry:contactServerPath:contactIdentifier:mappings:error:]_block_invoke.115.cold.1
+ __94-[KTVerifier validateEnrollmentUri:accountKey:loggableData:queryRequest:insertResponse:error:]_block_invoke.cold.1
+ __98-[KTVerifier validateEnrollmentUri:accountKey:loggableData:insertResponse:promiseCompletionBlock:]_block_invoke.cold.1
+ __CFXPCCreateCFObjectFromXPCObject
+ __OBJC_$_CLASS_METHODS_SWTransparencyOperationConfiguration
+ __OBJC_$_CLASS_METHODS_TransparencySelfValidationStatus
+ __OBJC_$_CLASS_METHODS_TransparencyStaticKey
+ __OBJC_$_CLASS_PROP_LIST_SWTransparencyOperationConfiguration
+ __OBJC_$_CLASS_PROP_LIST_SoftwareTransparency
+ __OBJC_$_CLASS_PROP_LIST_TransparencySelfValidationStatus
+ __OBJC_$_INSTANCE_METHODS_SWTransparencyOperationConfiguration
+ __OBJC_$_INSTANCE_METHODS_TransparencySelfValidationStatus
+ __OBJC_$_INSTANCE_VARIABLES_SWTransparencyOperationConfiguration
+ __OBJC_$_INSTANCE_VARIABLES_TransparencySelfValidationStatus
+ __OBJC_$_PROP_LIST_SWTransparencyOperationConfiguration
+ __OBJC_$_PROP_LIST_TransparencySelfValidationStatus
+ __OBJC_CLASS_PROTOCOLS_$_SWTransparencyOperationConfiguration
+ __OBJC_CLASS_PROTOCOLS_$_TransparencySelfValidationStatus
+ __OBJC_CLASS_RO_$_SWTransparencyOperationConfiguration
+ __OBJC_CLASS_RO_$_TransparencySelfValidationStatus
+ __OBJC_METACLASS_RO_$_SWTransparencyOperationConfiguration
+ __OBJC_METACLASS_RO_$_TransparencySelfValidationStatus
+ ___35+[SoftwareTransparency isAvailable]_block_invoke
+ ___58-[TransparencyDaemon networkKTQuery:application:complete:]_block_invoke
+ ___58-[TransparencyDaemon networkKTQuery:application:complete:]_block_invoke_2
+ ___60+[TransparencyStaticKey sasTTR:toHandle:pushToken:complete:]_block_invoke
+ ___60+[TransparencyStaticKey sasTTR:toHandle:pushToken:complete:]_block_invoke_2
+ ___67-[TransparencySFAnalytics logRockwellForEventNamed:withAttributes:]_block_invoke
+ ___81-[TransparencyDaemon validateSelfForThisDeviceForApplication:pushToken:complete:]_block_invoke
+ ___81-[TransparencyDaemon validateSelfForThisDeviceForApplication:pushToken:complete:]_block_invoke_2
+ ___88-[SoftwareTransparency verifyExpiringProofs:forDigest:configuration:counter:completion:]_block_invoke
+ ___block_descriptor_76_e8_32s40s48s56s64bs_e17_v16?0"NSError"8l
+ ___copy_helper_block_e8_32s40s48s56s64b
+ ___destroy_helper_block_e8_32s40s48s56s64s
+ __block_literal_global.128
+ __block_literal_global.132
+ __block_literal_global.144
+ __block_literal_global.159
+ __block_literal_global.161
+ __block_literal_global.303
+ __block_literal_global.311
+ __block_literal_global.353
+ __block_literal_global.356
+ __block_literal_global.364
+ __block_literal_global.366
+ __block_literal_global.373
+ __block_literal_global.376
+ __block_literal_global.381
+ __block_literal_global.384
+ __block_literal_global.387
+ __block_literal_global.390
+ __block_literal_global.399
+ __block_literal_global.401
+ __block_literal_global.407
+ __block_literal_global.414
+ __block_literal_global.417
+ __block_literal_global.420
+ __block_literal_global.423
+ __block_literal_global.426
+ __block_literal_global.429
+ __block_literal_global.432
+ __block_literal_global.456
+ __block_literal_global.459
+ __block_literal_global.462
+ __block_literal_global.465
+ __block_literal_global.468
+ __block_literal_global.471
+ __block_literal_global.474
+ __block_literal_global.479
+ __block_literal_global.482
+ __block_literal_global.487
+ __block_literal_global.490
+ __block_literal_global.493
+ __block_literal_global.496
+ __block_literal_global.501
+ __block_literal_global.504
+ __block_literal_global.507
+ __block_literal_global.68
+ __os_log_default
+ _objc_msgSend$allowsInternalSecurityPolicies
+ _objc_msgSend$initWithName:
+ _objc_msgSend$initWithStatus:pushToken:
+ _objc_msgSend$intValue
+ _objc_msgSend$invalidResponse
+ _objc_msgSend$isAvailable
+ _objc_msgSend$logRockwellFailureForEventNamed:withAttributes:
+ _objc_msgSend$networkKTQuery:application:complete:
+ _objc_msgSend$noteLaunchSequence:
+ _objc_msgSend$qualityOfService
+ _objc_msgSend$setQualityOfService:
+ _objc_msgSend$setStatus:
+ _objc_msgSend$setTimeout:
+ _objc_msgSend$timeout
+ _objc_msgSend$validateSelfForThisDeviceForApplication:pushToken:complete:
+ _objc_msgSend$valueForKey:
+ _objc_msgSend$verifyExpiringProofs:forDigest:configuration:counter:completion:
+ _objc_msgSend$verifyExpiringProofs:forObject:configuration:completion:
+ _objc_msgSend$verifyProofs:forDigest:configuration:completion:
+ isAvailable.token
- -[SoftwareTransparency gmEligibility]
- -[TransparencyIDSRegistrationData setUploadedAt:]
- -[TransparencyIDSRegistrationData uploadedAt]
- -[TransparencyStaticKey sasTTR:toHandle:pushToken:complete:]
- GCC_except_table166
- GCC_except_table36
- GCC_except_table88
- GCC_except_table96
- GCC_except_table97
- OBJC_IVAR_$_TransparencyIDSRegistrationData._uploadedAt
- _SecTaskCopySigningIdentifier
- _SecTaskCreateFromSelf
- __125-[TransparencyDaemon replaySelfValidate:application:pcsAccountKey:queryRequest:queryResponse:responseTime:completionHandler:]_block_invoke.350
- __40-[TransparencyDaemon getAllOptInStates:]_block_invoke.431
- __43-[TransparencyDaemon setOSUpdate:complete:]_block_invoke.451
- __44-[TransparencyDaemon configurationBagFetch:]_block_invoke.269
- __44-[TransparencyDaemon transparencyFetchIDMS:]_block_invoke.316
- __44-[TransparencyDaemon transparencyFetchSelf:]_block_invoke.322
- __44-[TransparencyDaemon transparencyIDSRepair:]_block_invoke.275
- __44-[TransparencyDaemon transparencyIDSRepair:]_block_invoke_2.276
- __45-[TransparencyDaemon getOptInState:complete:]_block_invoke.422
- __45-[TransparencyDaemon maybeUpdateMonitorState]_block_invoke.330
- __45-[TransparencyDaemon maybeUpdateMonitorState]_block_invoke_2.333
- __46-[TransparencyDaemon transparencySysDiagnose:]_block_invoke.279
- __47-[TransparencyDaemon transparencyCloudDevices:]_block_invoke.401
- __47-[TransparencyDaemon transparencyValidateSelf:]_block_invoke.319
- __48-[TransparencyDaemon clearEligibilityOverrides:]_block_invoke.459
- __49-[TransparencyAnalytics logSuccessForEventNamed:]_block_invoke.114
- __49-[TransparencyDaemon reportEligibility:complete:]_block_invoke.462
- __49-[TransparencyDaemon transparencyCheckIDSHealth:]_block_invoke.379
- __49-[TransparencyDaemon transparencyCheckIDSHealth:]_block_invoke.383
- __49-[TransparencyDaemon transparencyIDMSDeviceList:]_block_invoke.338
- __49-[TransparencyDaemon transparencyIDMSDeviceList:]_block_invoke.342
- __49-[TransparencyDaemon transparencyIDMSDeviceList:]_block_invoke_2.345
- __50-[TransparencyDaemon transparencyFetchPublicKeys:]_block_invoke.353
- __50-[TransparencyDaemon transparencyIDSRegistration:]_block_invoke.386
- __50-[TransparencyDaemon transparencySysDiagnoseData:]_block_invoke.283
- __50-[TransparencyDaemon transparencySysDiagnoseData:]_block_invoke.285
- __50-[TransparencyDaemon transparencySysDiagnoseData:]_block_invoke.289
- __50-[TransparencyDaemon transparencySysDiagnoseData:]_block_invoke.293
- __50-[TransparencyDaemon transparencySysDiagnoseData:]_block_invoke.306
- __50-[TransparencyDaemon transparencySysDiagnoseData:]_block_invoke_2.290
- __52-[TransparencyDaemon performAndWaitForSelfValidate:]_block_invoke.325
- __55-[TransparencyDaemon updateIDSRecommendation:complete:]_block_invoke.448
- __57-[TransparencyDaemon transparencyDumpKTRegistrationData:]_block_invoke.392
- __57-[TransparencyDaemon transparencyTriggerIDSRegistration:]_block_invoke.356
- __58-[TransparencyDaemon getAggregateResult:element:complete:]_block_invoke.465
- __58-[TransparencyDaemon getOptInForURI:application:complete:]_block_invoke.425
- __58-[TransparencyDaemon transparencyClearKTRegistrationData:]_block_invoke.398
- __59-[TransparencyDaemon clearTapToRadarNotification:complete:]_block_invoke.373
- __59-[TransparencyDaemon getOptInStateForApplication:complete:]_block_invoke.434
- __59-[TransparencyDaemon transparencyGetKTSignatures:complete:]_block_invoke.395
- __60-[TransparencyDaemon changeOptInState:application:complete:]_block_invoke.419
- __60-[TransparencyDaemon transparencyTriggerOperation:complete:]_block_invoke.414
- __60-[TransparencyStaticKey sasTTR:toHandle:pushToken:complete:]_block_invoke.353
- __60-[TransparencyStaticKey sasTTR:toHandle:pushToken:complete:]_block_invoke.354
- __60-[TransparencyStaticKey sasTTR:toHandle:pushToken:complete:]_block_invoke_2.355
- __61-[TransparencyDaemon transparencyCheckKTAccountKey:complete:]_block_invoke.359
- __61-[TransparencyDaemon transparencyTriggerTTR:handle:complete:]_block_invoke.362
- __61-[TransparencyDaemon transparencyTriggerTTR:handle:complete:]_block_invoke.367
- __61-[TransparencyDaemon transparencyTriggerTTR:handle:complete:]_block_invoke_2.363
- __61-[TransparencyDaemon transparencyTriggerTTR:handle:complete:]_block_invoke_2.368
- __62-[TransparencyAnalytics logResultForEvent:hardFailure:result:]_block_invoke.137
- __63-[TransparencyDaemon setOverrideTimeBetweenReports:completion:]_block_invoke.456
- __63-[TransparencyDaemon transparencyPerformRegistrationSignature:]_block_invoke.389
- __64-[TransparencyDaemon transparencyTriggerMaybeReportEligibility:]_block_invoke.473
- __65-[TransparencyDaemon clearOptInStateForURI:application:complete:]_block_invoke.437
- __68-[TransparencyAnalytics logHardFailureForEventNamed:withAttributes:]_block_invoke.121
- __69-[TransparencyDaemon transparencyCloudDeviceAdd:clientData:complete:]_block_invoke.440
- __72-[TransparencyDaemon transparencyCloudDeviceRemove:clientData:complete:]_block_invoke.443
- __73-[TransparencyDaemon insertResultForElement:samplesAgo:success:complete:]_block_invoke.470
- __77-[TransparencyAnalytics logResultForEvent:hardFailure:result:withAttributes:]_block_invoke.143
- __77-[TransparencyDaemon setOptInForURI:application:state:smtTimestamp:complete:]_block_invoke.428
- ___37-[SoftwareTransparency gmEligibility]_block_invoke
- ___60-[TransparencyStaticKey sasTTR:toHandle:pushToken:complete:]_block_invoke
- ___60-[TransparencyStaticKey sasTTR:toHandle:pushToken:complete:]_block_invoke_2
- ___block_descriptor_68_e8_32s40s48s56bs_e17_v16?0"NSError"8l
- __block_literal_global.117
- __block_literal_global.123
- __block_literal_global.125
- __block_literal_global.139
- __block_literal_global.145
- __block_literal_global.147
- __block_literal_global.274
- __block_literal_global.282
- __block_literal_global.292
- __block_literal_global.315
- __block_literal_global.318
- __block_literal_global.327
- __block_literal_global.329
- __block_literal_global.332
- __block_literal_global.335
- __block_literal_global.337
- __block_literal_global.349
- __block_literal_global.355
- __block_literal_global.365
- __block_literal_global.370
- __block_literal_global.372
- __block_literal_global.385
- __block_literal_global.388
- __block_literal_global.391
- __block_literal_global.397
- __block_literal_global.400
- __block_literal_global.403
- __block_literal_global.413
- __block_literal_global.416
- __block_literal_global.421
- __block_literal_global.424
- __block_literal_global.427
- __block_literal_global.430
- __block_literal_global.433
- __block_literal_global.436
- __block_literal_global.439
- __block_literal_global.458
- __block_literal_global.461
- __block_literal_global.464
- __block_literal_global.467
- __block_literal_global.472
- __block_literal_global.70
- _objc_msgSend$gmEligibility
- _objc_msgSend$setUploadedAt:
- _objc_msgSend$uploadedAt
- _objc_msgSend$verifyExpiringProofs:for:counter:completion:
- _objc_msgSend$verifyProofs:forObject:completion:
- gmEligibility.eligiable
- gmEligibility.onceToken
CStrings:
+ "\r"
+ "<TransparencySelfValidationStatus: %@ push: %@>"
+ "Device isn't GMS capable, disabling software transparency"
+ "OS_ELIGIBILITY_INPUT_GENERATIVE_MODEL_SYSTEM"
+ "SWTransparencyOperationConfiguration"
+ "SelfSoft"
+ "Sending networkKTQuery:application:complete:"
+ "Sending validateSelfForThisDeviceForApplication:pushToken:complete:"
+ "TQ,V_status"
+ "Td,V_timeout"
+ "Tq,V_qualityOfService"
+ "TransparencySelfValidationStatus"
+ "Unknown sasTTR error: %@"
+ "Unknown sasTTR invokeXPCSynchronousCallWithBlock error: %@"
+ "_qualityOfService"
+ "_status"
+ "_timeout"
+ "app: %@ sig: %d created: %@ signed: %@ altDSID: %@[%@] push: %@"
+ "initWithName:"
+ "initWithStatus:pushToken:"
+ "intValue"
+ "invalidResponse"
+ "isAvailable"
+ "isInputsEqual:"
+ "logRockwellFailureForEventNamed:withAttributes:"
+ "logRockwellForEventNamed:withAttributes:"
+ "networkKTQuery:application:complete:"
+ "old-spi"
+ "qos"
+ "qualityOfService"
+ "setQualityOfService:"
+ "setStatus:"
+ "setTimeout:"
+ "testingPeerValidationFailing"
+ "timeout"
+ "v40@0:8@\"NSString\"16@\"NSData\"24@?<v@?B@\"TransparencySelfValidationStatus\"@\"NSError\">32"
+ "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@\"NSData\"@\"NSError\">32"
+ "v48@0:8@\"NSData\"16@\"NSData\"24@\"SWTransparencyOperationConfiguration\"32@?<v@?@\"SWTransparencyExpiringVerificationResult\"@\"NSError\">40"
+ "v52@0:8@16@24@32i40@?44"
+ "validateSelfForThisDeviceForApplication:pushToken:complete:"
+ "valueForKey:"
+ "verify proofs blocked because device is not eligible for GM"
+ "verifyExpiringProofs:forDigest:configuration:completion:"
+ "verifyExpiringProofs:forDigest:configuration:counter:completion:"
+ "verifyExpiringProofs:forObject:configuration:completion:"
+ "verifyProofs:forDigest:configuration:completion:"
- "SelfHard"
- "app: %@ sig: %d created: %@ signed: %@ uploaded: %@ altDSID: %@[%@] push: %@"
- "com.apple.networkserviceproxy"
- "com.apple.transparency"
- "gmEligibility"
- "v40@0:8@\"NSData\"16@\"NSData\"24@?<v@?@\"SWTransparencyExpiringVerificationResult\"@\"NSError\">32"
- "verifyProofs:forObject:completion:"

```
