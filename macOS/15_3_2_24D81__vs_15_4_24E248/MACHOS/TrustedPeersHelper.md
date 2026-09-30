## TrustedPeersHelper

> `/System/Library/Frameworks/Security.framework/Versions/A/XPCServices/TrustedPeersHelper.xpc/Contents/MacOS/TrustedPeersHelper`

```diff

-61439.81.1.0.0
-  __TEXT.__text: 0x22ea94
-  __TEXT.__auth_stubs: 0x1ec0
-  __TEXT.__objc_stubs: 0x2840
-  __TEXT.__objc_methlist: 0x2b34
-  __TEXT.__const: 0x9650
-  __TEXT.__cstring: 0x1641c
-  __TEXT.__objc_methname: 0x8265
-  __TEXT.__oslogstring: 0xa23e
+61439.101.1.0.0
+  __TEXT.__text: 0x242774
+  __TEXT.__auth_stubs: 0x1e60
+  __TEXT.__objc_stubs: 0x2520
+  __TEXT.__objc_methlist: 0x2824
+  __TEXT.__const: 0x9628
+  __TEXT.__cstring: 0x15ff9
+  __TEXT.__objc_methname: 0x74a6
+  __TEXT.__oslogstring: 0xa2fe
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__constg_swiftt: 0x3474
-  __TEXT.__swift5_typeref: 0x35da
+  __TEXT.__constg_swiftt: 0x347c
+  __TEXT.__swift5_typeref: 0x3608
   __TEXT.__swift5_fieldmd: 0x2458
   __TEXT.__swift5_reflstr: 0x1e27
   __TEXT.__swift5_builtin: 0xb4
   __TEXT.__swift5_assocty: 0x360
   __TEXT.__swift5_proto: 0x844
-  __TEXT.__swift5_types: 0x274
-  __TEXT.__objc_classname: 0x49a
-  __TEXT.__objc_methtype: 0x2169
+  __TEXT.__swift5_types: 0x270
+  __TEXT.__objc_classname: 0x42d
+  __TEXT.__objc_methtype: 0x204a
   __TEXT.__swift5_mpenum: 0x18
-  __TEXT.__swift5_capture: 0x3530
-  __TEXT.__gcc_except_tab: 0x11c
+  __TEXT.__swift5_capture: 0x3664
+  __TEXT.__gcc_except_tab: 0x138
+  __TEXT.__dlopen_cstrs: 0x10e
   __TEXT.__swift5_protos: 0x18
-  __TEXT.__dlopen_cstrs: 0xb4
-  __TEXT.__unwind_info: 0x4f18
-  __TEXT.__eh_frame: 0x7280
-  __DATA_CONST.__auth_got: 0xf70
-  __DATA_CONST.__got: 0x880
-  __DATA_CONST.__auth_ptr: 0x668
-  __DATA_CONST.__const: 0xfbc8
-  __DATA_CONST.__cfstring: 0x1f40
-  __DATA_CONST.__objc_classlist: 0x270
+  __TEXT.__unwind_info: 0x4b88
+  __TEXT.__eh_frame: 0x7308
+  __DATA_CONST.__auth_got: 0xf40
+  __DATA_CONST.__got: 0x900
+  __DATA_CONST.__auth_ptr: 0x680
+  __DATA_CONST.__const: 0xfc18
+  __DATA_CONST.__cfstring: 0x18e0
+  __DATA_CONST.__objc_classlist: 0x250
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0xe8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x60
-  __DATA_CONST.__objc_superrefs: 0x108
-  __DATA.__objc_const: 0x7fc8
-  __DATA.__objc_selrefs: 0x1ed8
-  __DATA.__objc_ivar: 0x2b4
-  __DATA.__objc_data: 0x2a48
-  __DATA.__data: 0x76b0
+  __DATA_CONST.__objc_superrefs: 0xe8
+  __DATA.__objc_const: 0x6800
+  __DATA.__objc_selrefs: 0x1cd0
+  __DATA.__objc_ivar: 0x208
+  __DATA.__objc_data: 0x2908
+  __DATA.__data: 0x7670
   __DATA.__objc_stublist: 0x90
-  __DATA.__common: 0x8d0
-  __DATA.__bss: 0x10508
+  __DATA.__bss: 0x10518
+  __DATA.__common: 0x890
   - /System/Library/Frameworks/CloudKit.framework/Versions/A/CloudKit
   - /System/Library/Frameworks/CoreData.framework/Versions/A/CoreData
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 34F63642-3066-34D8-9962-7BB78842E237
-  Functions: 8149
-  Symbols:   491
-  CStrings:  3634
+  UUID: A3C2779F-3B17-3369-9219-42D84B59C69A
+  Functions: 8047
+  Symbols:   503
+  CStrings:  3377
 
Symbols:
+ _kSecurityRTCEventNameFetchAfterEstablish
+ _kSecurityRTCEventNameFetchRecoverableTLKShares
+ _kSecurityRTCEventNameJoinWithVoucherInTPH
+ _kSecurityRTCEventNameOnqueueEstablishTPH
+ _kSecurityRTCEventNamePreflightVouchWithBottle
+ _kSecurityRTCEventNameUpdateTrust
+ _kSecurityRTCEventNameVouchWithBottleTPH
+ _kSecurityRTCFieldTotalNumberOfCustodians
+ _kSecurityRTCFieldTotalNumberOfDistrustedRecoveryKeys
+ _kSecurityRTCFieldTotalNumberOfPeers
+ _kSecurityRTCFieldTotalNumberOfPreapprovals
+ _kSecurityRTCFieldTotalNumberOfRecoveryKeys
+ _kSecurityRTCFieldTotalNumberOfTrustedCustodians
+ _kSecurityRTCFieldTotalNumberOfTrustedRecoveryKeys
- _OTEscrowRecordMetadataPasscodeGenerationReadFrom
- _PBDataWriterWriteUint64Field
CStrings:
+ "CRK cleanup unable to save %{public}@"
+ "StreamingEncoder could not write final byte: %@"
+ "attemptPreapprovedJoinWithSpecificUser:ckksKeys:tlkShares:preapprovedKeys:altDSID:flowID:deviceSessionID:canSendMetrics:reply:"
+ "countOfDistrustedRecoveryKeys"
+ "countTotalNumberOfRecoveryKeys"
+ "countTotalTrustedCustodians"
+ "establish(ckksKeys:tlkShares:preapprovedKeys:altDSID:flowID:deviceSessionID:canSendMetrics:reply:)"
+ "establishWithSpecificUser:ckksKeys:tlkShares:preapprovedKeys:altDSID:flowID:deviceSessionID:canSendMetrics:reply:"
+ "fetchRecoverableTLKSharesWithSpecificUser:peerID:altDSID:flowID:deviceSessionID:canSendMetrics:reply:"
+ "initWithInteger:"
+ "loadModel error enumerating CRKs: %{public}@"
+ "onqueueRemoveDuplicateOrInvalidCRKs start"
+ "preapprovedJoin(ckksKeys:tlkShares:preapprovedKeys:altDSID:flowID:deviceSessionID:canSendMetrics:reply:)"
+ "preflightVouchWithBottle(bottleID:altDSID:flowID:deviceSessionID:canSendMetrics:reply:)"
+ "preflightVouchWithBottleWithSpecificUser:bottleID:altDSID:flowID:deviceSessionID:canSendMetrics:reply:"
+ "v68@0:8@\"TPSpecificUser\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40@\"NSString\"48B56@?<v@?@\"NSArray\"@\"NSError\">60"
+ "v68@0:8@\"TPSpecificUser\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40@\"NSString\"48B56@?<v@?@\"NSString\"@\"TPSyncingPolicy\"B@\"NSError\">60"
+ "v68@0:8@16@24@32@40@48B56@?60"
+ "v84@0:8@\"TPSpecificUser\"16@\"NSArray\"24@\"NSArray\"32@\"NSArray\"40@\"NSString\"48@\"NSString\"56@\"NSString\"64B72@?<v@?@\"NSString\"@\"NSArray\"@\"TPSyncingPolicy\"@\"NSError\">76"
+ "v84@0:8@16@24@32@40@48@56@64B72@?76"
+ "v92@0:8@\"TPSpecificUser\"16@\"NSString\"24@\"NSData\"32@\"NSString\"40@\"NSArray\"48@\"NSString\"56@\"NSString\"64@\"NSString\"72B80@?<v@?@\"NSData\"@\"NSData\"@\"NSArray\"@\"TrustedPeersHelperTLKRecoveryResult\"@\"NSError\">84"
+ "vouchWithBottle(bottleID:entropy:bottleSalt:tlkShares:altDSID:flowID:deviceSessionID:canSendMetrics:reply:)"
+ "vouchWithBottleWithSpecificUser:bottleID:entropy:bottleSalt:tlkShares:altDSID:flowID:deviceSessionID:canSendMetrics:reply:"
- ")"
- "@\"OTEscrowRecordMetadata\""
- "@\"OTEscrowRecordMetadataClientMetadata\""
- "@\"OTEscrowRecordMetadataPasscodeGeneration\""
- "Can't construct Array with count < 0"
- "Division by zero"
- "Division results in an overflow"
- "E!"
- "Insufficient space allocated to copy string contents"
- "Negative value is not representable"
- "OTEscrowMoveRequestContext"
- "OTEscrowRecord"
- "OTEscrowRecordMetadata"
- "OTEscrowRecordMetadataClientMetadata"
- "RECORD_VIABILITY_FULLY_VIABLE"
- "RECORD_VIABILITY_LEGACY"
- "RECORD_VIABILITY_PARTIALLY_VIABLE"
- "RECOVERY_STATUS_HARD_LIMIT_REACHED"
- "RECOVERY_STATUS_SOFT_LIMIT_REACHED"
- "RECOVERY_STATUS_VALID"
- "StreamingEncoderBase could not write final byte"
- "StringAsRecordStatus:"
- "StringAsRecordViability:"
- "StringAsRecoveryStatus:"
- "StringAsViabilityStatus:"
- "Swift/Array.swift"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/IntegerTypes.swift"
- "Swift/Integers.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "T@\"NSData\",&,N,V_backupKeybagDigest"
- "T@\"NSData\",&,N,V_escrowedSpki"
- "T@\"NSData\",&,N,V_peerInfo"
- "T@\"NSString\",&,N,V_bottleId"
- "T@\"NSString\",&,N,V_bottleValidity"
- "T@\"NSString\",&,N,V_build"
- "T@\"NSString\",&,N,V_currentFederation"
- "T@\"NSString\",&,N,V_deviceColor"
- "T@\"NSString\",&,N,V_deviceEnclosureColor"
- "T@\"NSString\",&,N,V_deviceMid"
- "T@\"NSString\",&,N,V_deviceModel"
- "T@\"NSString\",&,N,V_deviceModelClass"
- "T@\"NSString\",&,N,V_deviceModelVersion"
- "T@\"NSString\",&,N,V_deviceName"
- "T@\"NSString\",&,N,V_escrowRecordLabel"
- "T@\"NSString\",&,N,V_expectedFederationId"
- "T@\"NSString\",&,N,V_federationId"
- "T@\"NSString\",&,N,V_intendedFederation"
- "T@\"NSString\",&,N,V_label"
- "T@\"NSString\",&,N,V_recordId"
- "T@\"NSString\",&,N,V_serial"
- "T@\"NSString\",&,N,V_serialNumber"
- "T@\"OTEscrowRecordMetadata\",&,N,V_escrowInformationMetadata"
- "T@\"OTEscrowRecordMetadataClientMetadata\",&,N,V_clientMetadata"
- "T@\"OTEscrowRecordMetadataPasscodeGeneration\",&,N,V_passcodeGeneration"
- "TB,N"
- "TQ,N,V_coolOffEnd"
- "TQ,N,V_creationDate"
- "TQ,N,V_devicePlatform"
- "TQ,N,V_remainingAttempts"
- "TQ,N,V_secureBackupMetadataTimestamp"
- "TQ,N,V_secureBackupNumericPassphraseLength"
- "TQ,N,V_secureBackupTimestamp"
- "TQ,N,V_secureBackupUsesComplexPassphrase"
- "TQ,N,V_secureBackupUsesMultipleIcscs"
- "TQ,N,V_secureBackupUsesNumericPassphrase"
- "TQ,N,V_silentAttemptAllowed"
- "Ti,N,V_recordStatus"
- "Ti,N,V_recordViability"
- "Ti,N,V_recoveryStatus"
- "Ti,N,V_viabilityStatus"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutablePointer.initialize with negative count"
- "UnsafeMutablePointer.moveInitialize with negative count"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "W"
- "_bottleId"
- "_bottleValidity"
- "_coolOffEnd"
- "_creationDate"
- "_currentFederation"
- "_deviceColor"
- "_deviceEnclosureColor"
- "_deviceMid"
- "_deviceModel"
- "_deviceModelClass"
- "_deviceModelVersion"
- "_deviceName"
- "_devicePlatform"
- "_escrowInformationMetadata"
- "_escrowRecordLabel"
- "_expectedFederationId"
- "_federationId"
- "_has"
- "_intendedFederation"
- "_label"
- "_recordId"
- "_recordStatus"
- "_recordViability"
- "_recoveryStatus"
- "_remainingAttempts"
- "_secureBackupMetadataTimestamp"
- "_secureBackupNumericPassphraseLength"
- "_secureBackupUsesComplexPassphrase"
- "_secureBackupUsesNumericPassphrase"
- "_serialNumber"
- "_silentAttemptAllowed"
- "_viabilityStatus"
- "attemptPreapprovedJoinWithSpecificUser:ckksKeys:tlkShares:preapprovedKeys:reply:"
- "bottleId"
- "bottleValidity"
- "bottle_validity"
- "coolOffEnd"
- "cool_off_end"
- "currentFederation"
- "escrowInformationMetadata"
- "escrowRecordLabel"
- "escrowedSpki"
- "establish(ckksKeys:tlkShares:preapprovedKeys:reply:)"
- "establishWithSpecificUser:ckksKeys:tlkShares:preapprovedKeys:reply:"
- "expectedFederationId"
- "federationId"
- "fetchRecoverableTLKSharesWithSpecificUser:peerID:reply:"
- "hasBackupKeybagDigest"
- "hasBottleId"
- "hasBottleValidity"
- "hasBuild"
- "hasClientMetadata"
- "hasCoolOffEnd"
- "hasCreationDate"
- "hasCurrentFederation"
- "hasDeviceColor"
- "hasDeviceEnclosureColor"
- "hasDeviceMid"
- "hasDeviceModel"
- "hasDeviceModelClass"
- "hasDeviceModelVersion"
- "hasDeviceName"
- "hasDevicePlatform"
- "hasEscrowInformationMetadata"
- "hasEscrowRecordLabel"
- "hasEscrowedSpki"
- "hasExpectedFederationId"
- "hasFederationId"
- "hasIntendedFederation"
- "hasLabel"
- "hasPasscodeGeneration"
- "hasPeerInfo"
- "hasRecordId"
- "hasRecordStatus"
- "hasRecordViability"
- "hasRecoveryStatus"
- "hasRemainingAttempts"
- "hasSecureBackupMetadataTimestamp"
- "hasSecureBackupNumericPassphraseLength"
- "hasSecureBackupTimestamp"
- "hasSecureBackupUsesComplexPassphrase"
- "hasSecureBackupUsesMultipleIcscs"
- "hasSecureBackupUsesNumericPassphrase"
- "hasSerial"
- "hasSerialNumber"
- "hasSilentAttemptAllowed"
- "hasViabilityStatus"
- "intendedFederation"
- "invalid Collection: less than 'count' elements in collection"
- "preapprovedJoin(ckksKeys:tlkShares:preapprovedKeys:reply:)"
- "preflightVouchWithBottle(bottleID:reply:)"
- "preflightVouchWithBottleWithSpecificUser:bottleID:reply:"
- "recordId"
- "recordStatusAsString:"
- "recordViability"
- "recordViabilityAsString:"
- "record_id"
- "record_viability"
- "recoveryStatus"
- "recoveryStatusAsString:"
- "recovery_status"
- "secureBackupUsesMultipleIcscs"
- "setBottleValidity:"
- "setCoolOffEnd:"
- "setHasCoolOffEnd:"
- "setHasCreationDate:"
- "setHasDevicePlatform:"
- "setHasRecordStatus:"
- "setHasRecordViability:"
- "setHasRecoveryStatus:"
- "setHasRemainingAttempts:"
- "setHasSecureBackupMetadataTimestamp:"
- "setHasSecureBackupNumericPassphraseLength:"
- "setHasSecureBackupTimestamp:"
- "setHasSecureBackupUsesComplexPassphrase:"
- "setHasSecureBackupUsesMultipleIcscs:"
- "setHasSecureBackupUsesNumericPassphrase:"
- "setHasSilentAttemptAllowed:"
- "setHasViabilityStatus:"
- "setRecordId:"
- "setRecoveryStatus:"
- "setSerialNumber:"
- "v40@0:8@\"TPSpecificUser\"16@\"NSString\"24@?<v@?@\"NSArray\"@\"NSError\">32"
- "v40@0:8@\"TPSpecificUser\"16@\"NSString\"24@?<v@?@\"NSString\"@\"TPSyncingPolicy\"B@\"NSError\">32"
- "v56@0:8@\"TPSpecificUser\"16@\"NSArray\"24@\"NSArray\"32@\"NSArray\"40@?<v@?@\"NSString\"@\"NSArray\"@\"TPSyncingPolicy\"@\"NSError\">48"
- "v64@0:8@\"TPSpecificUser\"16@\"NSString\"24@\"NSData\"32@\"NSString\"40@\"NSArray\"48@?<v@?@\"NSData\"@\"NSData\"@\"NSArray\"@\"TrustedPeersHelperTLKRecoveryResult\"@\"NSError\">56"
- "v64@0:8@16@24@32@40@48@?56"
- "viabilityStatus"
- "viabilityStatusAsString:"
- "vouchWithBottle(bottleID:entropy:bottleSalt:tlkShares:reply:)"
- "vouchWithBottleWithSpecificUser:bottleID:entropy:bottleSalt:tlkShares:reply:"
- "{?=\"coolOffEnd\"b1\"creationDate\"b1\"remainingAttempts\"b1\"silentAttemptAllowed\"b1\"recordStatus\"b1\"recordViability\"b1\"recoveryStatus\"b1\"viabilityStatus\"b1}"
- "{?=\"devicePlatform\"b1\"secureBackupMetadataTimestamp\"b1\"secureBackupNumericPassphraseLength\"b1\"secureBackupUsesComplexPassphrase\"b1\"secureBackupUsesNumericPassphrase\"b1}"
- "{?=\"secureBackupTimestamp\"b1\"secureBackupUsesMultipleIcscs\"b1}"

```
