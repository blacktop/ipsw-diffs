## idcredd

> `/usr/libexec/idcredd`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift5_entry`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`

```diff

-9.38.0.0.0
-  __TEXT.__text: 0x1b6914
-  __TEXT.__auth_stubs: 0x4160
-  __TEXT.__objc_stubs: 0x1ec0
-  __TEXT.__objc_methlist: 0x8e4
-  __TEXT.__const: 0x5828
-  __TEXT.__constg_swiftt: 0x22f8
-  __TEXT.__swift5_typeref: 0x27e8
+9.42.0.0.0
+  __TEXT.__text: 0x1cd40c
+  __TEXT.__auth_stubs: 0x43d0
+  __TEXT.__objc_stubs: 0x2280
+  __TEXT.__objc_methlist: 0x95c
+  __TEXT.__const: 0x5e28
+  __TEXT.__objc_classname: 0x804
+  __TEXT.__objc_methname: 0x31e5
+  __TEXT.__constg_swiftt: 0x2434
+  __TEXT.__swift5_typeref: 0x2910
+  __TEXT.__swift5_reflstr: 0x1947
+  __TEXT.__swift5_fieldmd: 0x1944
   __TEXT.__swift5_builtin: 0x1b8
-  __TEXT.__swift5_reflstr: 0x1867
   __TEXT.__swift5_assocty: 0x1c8
-  __TEXT.__cstring: 0xe1f9
-  __TEXT.__oslogstring: 0xad28
-  __TEXT.__swift5_fieldmd: 0x1758
-  __TEXT.__swift5_proto: 0x16c
-  __TEXT.__swift5_types: 0x1f4
-  __TEXT.__objc_classname: 0x7b4
-  __TEXT.__objc_methname: 0x2e05
-  __TEXT.__swift_as_entry: 0x634
-  __TEXT.__swift_as_ret: 0x7bc
-  __TEXT.__swift_as_cont: 0xf00
-  __TEXT.__swift5_capture: 0x2204
+  __TEXT.__cstring: 0xe80a
+  __TEXT.__oslogstring: 0xad99
+  __TEXT.__swift5_proto: 0x18c
+  __TEXT.__swift5_types: 0x20c
+  __TEXT.__swift_as_entry: 0x664
+  __TEXT.__swift_as_ret: 0x7e8
+  __TEXT.__swift_as_cont: 0xf34
+  __TEXT.__swift5_capture: 0x2b9c
   __TEXT.__swift5_protos: 0x38
-  __TEXT.__objc_methtype: 0xfc3
+  __TEXT.__objc_methtype: 0x10f3
   __TEXT.__swift5_mpenum: 0x10
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0x57b8
-  __TEXT.__eh_frame: 0x1466c
-  __DATA_CONST.__const: 0x6238
-  __DATA_CONST.__objc_classlist: 0x140
+  __TEXT.__unwind_info: 0x5b80
+  __TEXT.__eh_frame: 0x15170
+  __DATA_CONST.__const: 0x6e40
+  __DATA_CONST.__objc_classlist: 0x150
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__linkguard: 0xe
-  __DATA_CONST.__auth_got: 0x20b8
-  __DATA_CONST.__got: 0x17c0
-  __DATA_CONST.__auth_ptr: 0x9e0
-  __DATA.__objc_const: 0x2708
-  __DATA.__objc_selrefs: 0xa80
-  __DATA.__objc_data: 0xc78
-  __DATA.__data: 0x4158
-  __DATA.__bss: 0x21d0
-  __DATA.__common: 0xf0
+  __DATA_CONST.__auth_got: 0x21f0
+  __DATA_CONST.__got: 0x1860
+  __DATA_CONST.__auth_ptr: 0xa98
+  __DATA.__objc_const: 0x28c0
+  __DATA.__objc_selrefs: 0xb98
+  __DATA.__objc_data: 0xcb8
+  __DATA.__data: 0x4470
+  __DATA.__bss: 0x25d0
+  __DATA.__common: 0xf8
   - /AppleInternal/Library/Frameworks/TapToRadarKit.framework/TapToRadarKit
   - /System/Library/Frameworks/CoreData.framework/CoreData
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/CoreIDCred.framework/CoreIDCred
   - /System/Library/PrivateFrameworks/CoreIDVDaemonSupport.framework/CoreIDVDaemonSupport
   - /System/Library/PrivateFrameworks/CoreIDVShared.framework/CoreIDVShared
+  - /System/Library/PrivateFrameworks/PassKitCore.framework/PassKitCore
   - /System/Library/PrivateFrameworks/SEService.framework/SEService
   - /usr/appleinternal/lib/liblinkguard.dylib
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
+  - /usr/lib/swift/libswiftAVFoundation.dylib
+  - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
+  - /usr/lib/swift/libswiftCoreLocation.dylib
+  - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftIntents.dylib
+  - /usr/lib/swift/libswiftMLCompute.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftQuartzCore.dylib
+  - /usr/lib/swift/libswiftRegexBuilder.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 4145
-  Symbols:   1943
-  CStrings:  2184
+  - /usr/lib/swift/libswiftsimd.dylib
+  Functions: 4352
+  Symbols:   2026
+  CStrings:  2257
 
Symbols:
+ _$s10CoreIDCred15DocumentRequestV19alternativeElements7docType17issuerIdentifiers10namespacesACSDySSSDySSSaySayAC11DataElementVGGGG_SSShy10Foundation0L0VGSDySSSDySSAA021CredentialPresentmentmD4InfoVGGtcfC
+ _$s10Foundation11JSONEncoderC16OutputFormattingV10sortedKeysAEvgZ
+ _$s10Foundation11JSONEncoderC16OutputFormattingV13prettyPrintedAEvgZ
+ _$s10Foundation11JSONEncoderC16OutputFormattingV22withoutEscapingSlashesAEvgZ
+ _$s10Foundation11JSONEncoderC16OutputFormattingVMa
+ _$s10Foundation11JSONEncoderC16OutputFormattingVMn
+ _$s10Foundation11JSONEncoderC16OutputFormattingVs10SetAlgebraAAMc
+ _$s10Foundation11JSONEncoderC16outputFormattingAC06OutputD0VvsTj
+ _$s10Foundation11JSONEncoderC20DateEncodingStrategyO7iso8601yA2EmFWC
+ _$s10Foundation11JSONEncoderC20DateEncodingStrategyOMa
+ _$s10Foundation11JSONEncoderC20dateEncodingStrategyAC04DatedE0OvsTj
+ _$s10Foundation15ContiguousBytesMp
+ _$s10Foundation3URLV20CoreIDVDaemonSupportE36credentialAuditLogManagedObjectModelACSgvgZ
+ _$s10Foundation4DataV15_RepresentationO15replaceSubrange_4with5countySnySiG_SVSgSitF
+ _$s10Foundation4DataV15_RepresentationO6append10contentsOfySW_tF
+ _$s10Foundation4DataV15_RepresentationON
+ _$s10Foundation4DateVSEAAMc
+ _$s10Foundation4DateVSeAAMc
+ _$s13CoreIDVShared25CredentialOperationReasonO024garbageCollectionInvalidC0yA2CmFWC
+ _$s13CoreIDVShared25CredentialOperationReasonO027garbageCollectionIncompleteC0yA2CmFWC
+ _$s13CoreIDVShared25CredentialOperationReasonO24piiReconciliationRestoreyA2CmFWC
+ _$s13CoreIDVShared25CredentialOperationReasonO8rawValueSSvg
+ _$s13CoreIDVShared25CredentialOperationReasonOMa
+ _$s13CoreIDVShared26DaemonInternalDefaultsKeysO27overrideTapToRadarRateLimitSSvgZ
+ _$s13CoreIDVShared8DIPErrorV4CodeO28coreDataDatabaseInaccessibleyA2EmFWC
+ _$s13CoreIDVShared8DIPErrorVs23CustomStringConvertibleAAMc
+ _$s20CoreIDVDaemonSupport28StoredCredentialOperationLogC12fetchRequestSo07NSFetchI0CyACGyFZ
+ _$s20CoreIDVDaemonSupport28StoredCredentialOperationLogCMa
+ _$sSE6encode2toys7Encoder_p_tKFTq
+ _$sSEMp
+ _$sSK17_StringProcessingSs11SubSequenceRtzrlE6starts4withSbqd___tAA14RegexComponentRd__lF
+ _$sSS17_StringProcessing14RegexComponent0C7BuilderMc
+ _$sSS18_fromUTF8RepairingySS6result_Sb11repairsMadetSRys5UInt8VGFZ
+ _$sSS8UTF8ViewVN
+ _$sSSSKsMc
+ _$sSa28_allocateBufferUninitialized15minimumCapacitys06_ArrayB0VyxGSi_tFZ
+ _$sSayxGSTsMc
+ _$sSe4fromxs7Decoder_p_tKcfCTq
+ _$sSeMp
+ _$ss10SetAlgebraPyxqd__ncSTRd__7ElementQyd__ACRtzlufCTj
+ _$ss10__CocoaSetV10startIndexAB0D0Vvg
+ _$ss10__CocoaSetV5IndexV2eeoiySbAD_ADtFZ
+ _$ss10__CocoaSetV5IndexV3ages5Int32Vvg
+ _$ss10__CocoaSetV5IndexV7elementyXlvg
+ _$ss10__CocoaSetV7element2atyXlAB5IndexV_tF
+ _$ss10__CocoaSetV8endIndexAB0D0Vvg
+ _$ss11_StringGutsV8copyUTF84intoSiSgSrys5UInt8VG_tF
+ _$ss12_ArrayBufferV18_typeCheckSlowPathyySiF
+ _$ss18_CocoaArrayWrapperVys12_SliceBufferVyyXlGSnySiGcig
+ _$ss22KeyedDecodingContainerV15decodeIfPresent_6forKeySSSgSSm_xtKF
+ _$ss22KeyedDecodingContainerV6decode_6forKeyS2Sm_xtKF
+ _$ss22KeyedDecodingContainerV6decode_6forKeyS2bm_xtKF
+ _$ss22KeyedDecodingContainerV6decode_6forKeyS2im_xtKF
+ _$ss22KeyedDecodingContainerV6decode_6forKeyqd__qd__m_xtKSeRd__lF
+ _$ss22KeyedDecodingContainerVMn
+ _$ss22KeyedEncodingContainerV15encodeIfPresent_6forKeyySSSg_xtKF
+ _$ss22KeyedEncodingContainerV6encode_6forKeyySS_xtKF
+ _$ss22KeyedEncodingContainerV6encode_6forKeyySb_xtKF
+ _$ss22KeyedEncodingContainerV6encode_6forKeyySi_xtKF
+ _$ss22KeyedEncodingContainerV6encode_6forKeyyqd___xtKSERd__lF
+ _$ss22KeyedEncodingContainerVMn
+ _$ss28CustomDebugStringConvertibleMp
+ _$ss28CustomDebugStringConvertibleP16debugDescriptionSSvgTq
+ _$ss4Int8VN
+ _$ss7DecoderP9container7keyedBys22KeyedDecodingContainerVyqd__Gqd__m_tKs9CodingKeyRd__lFTj
+ _$ss7EncoderP9container7keyedBys22KeyedEncodingContainerVyqd__Gqd__m_ts9CodingKeyRd__lFTj
+ _$ss9CodingKeyMp
+ _$ss9CodingKeyP11stringValueSSvgTq
+ _$ss9CodingKeyP11stringValuexSgSS_tcfCTq
+ _$ss9CodingKeyP8intValueSiSgvgTq
+ _$ss9CodingKeyP8intValuexSgSi_tcfCTq
+ _$ss9CodingKeyPs23CustomStringConvertibleTb
+ _$ss9CodingKeyPs28CustomDebugStringConvertibleTb
+ _$ss9CodingKeyPsE11descriptionSSvg
+ _$ss9CodingKeyPsE16debugDescriptionSSvg
+ _OBJC_CLASS_$_NSProcessInfo
+ _OBJC_CLASS_$_NSSortDescriptor
+ _OBJC_CLASS_$_PKAppletSubcredential
+ _OBJC_CLASS_$_PKPass
+ _OBJC_CLASS_$_PKPassLibrary
+ _OBJC_CLASS_$_PKPaymentApplication
+ _OBJC_CLASS_$_PKSecureElementPass
+ __swift_FORCE_LOAD_$_swiftAVFoundation
+ __swift_FORCE_LOAD_$_swiftAccelerate
+ __swift_FORCE_LOAD_$_swiftCompression
+ __swift_FORCE_LOAD_$_swiftCoreLocation
+ __swift_FORCE_LOAD_$_swiftCoreMIDI
+ __swift_FORCE_LOAD_$_swiftIntents
+ __swift_FORCE_LOAD_$_swiftMLCompute
+ __swift_FORCE_LOAD_$_swiftQuartzCore
+ __swift_FORCE_LOAD_$_swiftsimd
+ _proc_name
- _$s10CoreIDCred15DocumentRequestV10regionCode10Foundation6LocaleV6RegionVSgvg
- _$s10CoreIDCred15DocumentRequestV19alternativeElements7docType17issuerIdentifiers10regionCode10namespacesACSDySSSDySSSaySayAC11DataElementVGGGG_SSShy10Foundation0N0VGAO6LocaleV6RegionVSgSDySSSDySSAA021CredentialPresentmentoD4InfoVGGtcfC
- _$s10Foundation6LocaleV6RegionV10identifierSSvg
- _$s10Foundation6LocaleV6RegionVMa
- _$s10Foundation6LocaleV6RegionVMn
- _$s13CoreIDVShared13IDCSAnalyticsC26PIIReconciliationEventTypeO15strandedPIIHashyA2EmFWC
- _$s13CoreIDVShared13IDCSAnalyticsC26PIIReconciliationEventTypeO17orphanedPIIBackupyA2EmFWC
- _$s13CoreIDVShared8DIPErrorV4CodeO28failedToDeletePIIHashLocallyyA2EmFWC
- _$sSS8IteratorV4nextSJSgyF
CStrings:
+ ". Credential identifier: "
+ "A PII token was requested but could not be found in the syncable key store. Token identifier: "
+ "A credential payload failed to ingest during replacePayload. Credential identifier: "
+ "A credential payload was deleted, but the pass itself is still present in Wallet."
+ "Credential audit log managed object model is unavailable"
+ "CredentialStoreSessionProxy resetCredentialOperationLog for credential %s"
+ "CredentialStoreSessionProxy retrieveCredentialOperationLogs"
+ "Did not find pass for credential %s"
+ "Failed to record credential operation audit log: %{public}@"
+ "Found pass %s for credential %s"
+ "Generating a key required to back a pass failed during "
+ "PII reconciler: backfilling piiTokenIdentifier for %ld legacy credential(s)"
+ "PII reconciler: keychain hash missing but local present; leaving shared keychain untouched"
+ "PII reconciler: keychain token missing but local present; leaving shared keychain untouched"
+ "PII token missing on retrieval"
+ "PII token missing on retrieval from keychain, filing Tap-to-Radar"
+ "PII token missing on retrieval, filing Tap-to-Radar"
+ "Pass key generation failed ("
+ "Payload ingestion failed"
+ "Payload ingestion failed: %{public}@, filing Tap-to-Radar"
+ "Wallet pass not deleted after credential deletion"
+ "Wallet pass still present after deleting PII token, filing Tap-to-Radar"
+ "Wallet pass still present after deleting credential %{public}s, filing Tap-to-Radar"
+ "_TtC7idcredd23CredentialAuditLogStore"
+ "_TtC7idcredd29CredentialAuditLogDataContext"
+ "a PII token was missing on retrieval"
+ "a Wallet pass was not deleted with its credential"
+ "a credential payload failed to ingest"
+ "a pass key failed to generate"
+ "auditLogger"
+ "callerProcessName"
+ "createCredential"
+ "credentialIdentifier == %@"
+ "credential_audit.sqlite"
+ "credentialauditlog"
+ "dataType"
+ "deleteCredential"
+ "deleteCredential(_:reason:)"
+ "deleteCredential:reason:completion:"
+ "deleteCredentialOperationLogs(forCredentialIdentifier:)"
+ "deletePIIDataFromSyncableKeyStore(forIdentifier:keystoreType:piiDataType:credentialIdentifier:reason:)"
+ "deletePIIDataFromSyncableKeyStoreForIdentifier:keystoreType:piiDataType:credentialIdentifier:reason:completion:"
+ "detail"
+ "devicePaymentApplications"
+ "error deleting credential operation logs: "
+ "error fetching credential operation logs: "
+ "error trimming credential operation logs: "
+ "errorCode"
+ "errorDescription"
+ "fetchAllCredentialOperationLogs()"
+ "generateAccountKeyAuthorization"
+ "generateDeviceEncryptionKey"
+ "generateKeySigningKey"
+ "generatePresentmentKey"
+ "generatePresentmentKeys"
+ "idcredd/CredentialAuditLogDataContext+StoredCredentialOperationLog.swift"
+ "idcredd/CredentialAuditLogStore.swift"
+ "idcredd/CredentialOperationAuditLogger.swift"
+ "initWithKey:ascending:"
+ "isIdentityPass"
+ "keystoreType"
+ "operation"
+ "passesOfType:"
+ "processInfo"
+ "processName"
+ "reason"
+ "record(_:dataType:keystoreType:identifier:credentialIdentifier:detail:callerProcessName:reason:error:)"
+ "resetCredentialOperationLogForCredential:completion:"
+ "retrieveCredentialOperationLogsWithCompletion:"
+ "retrievePIITokenFromSyncableKeyStore(forIdentifier:keystoreType:credentialIdentifier:fileTapToRadarOnMissing:)"
+ "setCallerProcessName:"
+ "setDataType:"
+ "setDetail:"
+ "setErrorCode:"
+ "setErrorDescription:"
+ "setIsUserInitiated:"
+ "setKeystoreType:"
+ "setOperation:"
+ "setReason:"
+ "setSortDescriptors:"
+ "setSucceeded:"
+ "setTimestamp:"
+ "storePIIDataInSyncableKeyStore(forIdentifier:data:keystoreType:piiDataType:credentialIdentifier:reason:)"
+ "storePIIDataInSyncableKeyStoreForIdentifier:data:keystoreType:piiDataType:credentialIdentifier:reason:completion:"
+ "subcredentials"
+ "succeeded"
+ "timestamp"
+ "trimCredentialOperationLogs(toMostRecent:)"
+ "uniqueID"
+ "updatePIIDataInSyncableKeyStore(forIdentifier:attributesToUpdate:keystoreType:piiDataType:credentialIdentifier:reason:)"
+ "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@\"NSError\">32"
+ "v64@0:8@\"NSString\"16Q24Q32@\"NSString\"40@\"NSString\"48@?<v@?@\"NSError\">56"
+ "v64@0:8@16Q24Q32@40@48@?56"
+ "v72@0:8@\"NSString\"16@\"NSData\"24Q32Q40@\"NSString\"48@\"NSString\"56@?<v@?@\"NSError\">64"
+ "v72@0:8@16@24Q32Q40@48@56@?64"
- "Credential region '%s' code does not match request region code '%s', skipping credential"
- "Error deleting stranded keychain hash during reconciliation"
- "Error during PII orphan cleanup"
- "Error during stranded keychain hash cleanup"
- "Error processing keychain backup during reconciliation"
- "Failed to delete local PII hash: %{public}@"
- "Failed to delete local hash"
- "ISO18013PackagePayloadProcessor update region to US for docType: %s region: %s"
- "PII reconciler: deleting fully orphaned keychain backup"
- "PII reconciler: deleting stranded keychain hash with no parent token"
- "PII reconciler: no credential list for keychain backup, deleting"
- "PII reconciler: no keychain hash to delete for orphan cleanup"
- "PII reconciler: pruning credential list from %ld to %ld entries"
- "PII reconciler: restoring keychain PII hash from local copy"
- "PII reconciler: restoring keychain PII token from local copy"
- "PII reconciler: scanning keychain for orphaned backups"
- "PII reconciler: scanning keychain for stranded hash backups"
- "debug.force-US-region-for-photo-id-presentment"
- "deletePIIDataFromSyncableKeyStore(forIdentifier:keystoreType:piiDataType:credentialIdentifier:)"
- "retrievePIITokenFromSyncableKeyStore(forIdentifier:keystoreType:credentialIdentifier:)"
- "storePIIDataInSyncableKeyStore(forIdentifier:data:keystoreType:piiDataType:credentialIdentifier:)"
- "updatePIIDataInSyncableKeyStore(forIdentifier:attributesToUpdate:keystoreType:piiDataType:credentialIdentifier:)"
```
