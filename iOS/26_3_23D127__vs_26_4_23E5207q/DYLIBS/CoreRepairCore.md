## CoreRepairCore

> `/System/Library/PrivateFrameworks/CoreRepairCore.framework/CoreRepairCore`

```diff

-921.80.171.0.1
-  __TEXT.__text: 0x89ee4
-  __TEXT.__auth_stubs: 0x16b0
-  __TEXT.__objc_methlist: 0x3dcc
-  __TEXT.__const: 0x800
-  __TEXT.__oslogstring: 0x958e
-  __TEXT.__cstring: 0x5c70
-  __TEXT.__gcc_except_tab: 0x17ac
-  __TEXT.__unwind_info: 0x1270
-  __TEXT.__objc_classname: 0x863
-  __TEXT.__objc_methname: 0x8518
-  __TEXT.__objc_methtype: 0x1580
-  __TEXT.__objc_stubs: 0x6aa0
-  __DATA_CONST.__got: 0x570
+921.100.255.0.0
+  __TEXT.__text: 0x8e224
+  __TEXT.__auth_stubs: 0x1660
+  __TEXT.__objc_methlist: 0x3eb4
+  __TEXT.__const: 0x828
+  __TEXT.__oslogstring: 0x976b
+  __TEXT.__cstring: 0x5ffa
+  __TEXT.__gcc_except_tab: 0x183c
+  __TEXT.__unwind_info: 0x15f0
+  __TEXT.__objc_classname: 0x8af
+  __TEXT.__objc_methname: 0x86cd
+  __TEXT.__objc_methtype: 0x15dd
+  __TEXT.__objc_stubs: 0x6c20
+  __DATA_CONST.__got: 0x598
   __DATA_CONST.__const: 0x8d8
-  __DATA_CONST.__objc_classlist: 0x2e0
+  __DATA_CONST.__objc_classlist: 0x300
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x21b0
+  __DATA_CONST.__objc_selrefs: 0x2220
   __DATA_CONST.__objc_protorefs: 0x28
-  __DATA_CONST.__objc_superrefs: 0x208
+  __DATA_CONST.__objc_superrefs: 0x218
   __DATA_CONST.__objc_arraydata: 0xb70
-  __AUTH_CONST.__auth_got: 0xb68
+  __AUTH_CONST.__auth_got: 0xb40
   __AUTH_CONST.__const: 0x520
-  __AUTH_CONST.__cfstring: 0x7520
-  __AUTH_CONST.__objc_const: 0x5da0
+  __AUTH_CONST.__cfstring: 0x7880
+  __AUTH_CONST.__objc_const: 0x6020
   __AUTH_CONST.__objc_arrayobj: 0x7b0
   __AUTH_CONST.__objc_dictobj: 0x230
-  __AUTH_CONST.__objc_intobj: 0x2e8
-  __AUTH.__objc_data: 0xff0
-  __DATA.__objc_ivar: 0x310
+  __AUTH_CONST.__objc_intobj: 0x348
+  __AUTH.__objc_data: 0x1130
+  __DATA.__objc_ivar: 0x314
   __DATA.__data: 0x690
   __DATA.__common: 0x30
   __DATA.__bss: 0x98

   - /System/Library/PrivateFrameworks/DeviceIdentity.framework/DeviceIdentity
   - /System/Library/PrivateFrameworks/HID.framework/HID
   - /System/Library/PrivateFrameworks/MSUDataAccessor.framework/MSUDataAccessor
+  - /System/Library/PrivateFrameworks/MobileActivation.framework/MobileActivation
   - /System/Library/PrivateFrameworks/MobileWiFi.framework/MobileWiFi
   - /System/Library/PrivateFrameworks/SavageCameraInterface.framework/SavageCameraInterface
   - /System/Library/PrivateFrameworks/ServiceManagement.framework/ServiceManagement

   - /usr/lib/updaters/libSavageRestoreInfo_iOS.dylib
   - /usr/lib/updaters/libSavageUpdater_iOS.dylib
   - /usr/lib/updaters/libT200Updater.dylib
-  UUID: 74BBD558-D59F-3679-BA0A-6A307168672B
-  Functions: 2338
-  Symbols:   7738
-  CStrings:  4958
+  UUID: AA5E819E-5FE4-3151-8C72-15FA7972A9D8
+  Functions: 2396
+  Symbols:   8216
+  CStrings:  5051
 
Symbols:
+ +[CRCCertificateCrypto copyCertificateValidityDate:queryNotValidAfter:error:]
+ +[CRCCertificateCrypto queryCertificateProperties:oid:error:]
+ +[CRCCertificateUtils createPEMFromCertificates:]
+ +[CRCCertificateUtils decodePEM:]
+ +[CRCCertificateUtils pemFormattedStringFromData:]
+ +[CRSalvageStatus isDateAfterEffectiveDate:]
+ +[CRSalvageStatus isSalvagedKBBFromBAA:]
+ +[CRSalvageStatus isSalvagedKBBFromBAA:].cold.1
+ +[CRSalvageStatus isSalvagedKBBFromBAA:].cold.2
+ +[CRSalvageStatus isSalvagedKBBFromBAA:].cold.3
+ +[CRSalvageStatus isSalvagedKBBFromUCRT]
+ +[CRSalvageStatus isSalvagedKBBFromUCRT].cold.1
+ -[CRAttestationHelper .cxx_destruct]
+ -[CRAttestationHelper handler]
+ -[CRAttestationHelper init]
+ -[CRAttestationHelper setHandler:]
+ -[CRCAttestationManager sendCertIssueRequestWith:requestID:serverCertResponse:error:]
+ -[CRCAttestationManager sendChallengeRequestWith:requestID:serverResponse:error:]
+ -[CRCCertificate extractSalvageState:error:]
+ -[CRFDRBaseDeviceHandler initComponentsMapping]
+ -[CRFDRGen1DeviceHandler initComponentsMapping]
+ -[CRFDRGen2DeviceHandler initComponentsMapping]
+ -[CRFDRGen3DeviceHandler initComponentsMapping]
+ -[CRFDRGen4DeviceHandler initComponentsMapping]
+ -[CRFDRGen5DeviceHandler initComponentsMapping]
+ -[CRFDRGen6DeviceHandler initComponentsMapping]
+ -[CRFDRGen7DeviceHandler initComponentsMapping]
+ -[CRFDRLegacy2DeviceHandler initComponentsMapping]
+ -[CRFDRLegacyDeviceHandler initComponentsMapping]
+ -[CRFDRWatch1DeviceHandler initComponentsMapping]
+ -[CRFDRiPad1DeviceHandler initComponentsMapping]
+ -[CRLogicBoardStatus copyComponentStatus]
+ -[CRLogicBoardStatus init]
+ GCC_except_table24
+ GCC_except_table29
+ _DERDecodeSeqInit
+ _MAEGetUCRTSalvageStateWithError
+ _OBJC_CLASS_$_CRCCertificateCrypto
+ _OBJC_CLASS_$_CRCCertificateUtils
+ _OBJC_CLASS_$_CRLogicBoardStatus
+ _OBJC_CLASS_$_CRSalvageStatus
+ _OBJC_CLASS_$_NSScanner
+ _OBJC_IVAR_$_CRAttestationHelper._handler
+ _OBJC_METACLASS_$_CRCCertificateCrypto
+ _OBJC_METACLASS_$_CRCCertificateUtils
+ _OBJC_METACLASS_$_CRLogicBoardStatus
+ _OBJC_METACLASS_$_CRSalvageStatus
+ _OUTLINED_FUNCTION_20
+ _OUTLINED_FUNCTION_38
+ _OUTLINED_FUNCTION_39
+ _OUTLINED_FUNCTION_41
+ _OUTLINED_FUNCTION_43
+ _OUTLINED_FUNCTION_44
+ _OUTLINED_FUNCTION_46
+ _OUTLINED_FUNCTION_48
+ _OUTLINED_FUNCTION_55
+ _OUTLINED_FUNCTION_56
+ _OUTLINED_FUNCTION_62
+ _OUTLINED_FUNCTION_68
+ __OBJC_$_CLASS_METHODS_CRCCertificateCrypto
+ __OBJC_$_CLASS_METHODS_CRCCertificateUtils
+ __OBJC_$_CLASS_METHODS_CRSalvageStatus
+ __OBJC_$_INSTANCE_METHODS_CRLogicBoardStatus
+ __OBJC_$_INSTANCE_VARIABLES_CRAttestationHelper
+ __OBJC_$_PROP_LIST_CRAttestationHelper
+ __OBJC_CLASS_RO_$_CRCCertificateCrypto
+ __OBJC_CLASS_RO_$_CRCCertificateUtils
+ __OBJC_CLASS_RO_$_CRLogicBoardStatus
+ __OBJC_CLASS_RO_$_CRSalvageStatus
+ __OBJC_METACLASS_RO_$_CRCCertificateCrypto
+ __OBJC_METACLASS_RO_$_CRCCertificateUtils
+ __OBJC_METACLASS_RO_$_CRLogicBoardStatus
+ __OBJC_METACLASS_RO_$_CRSalvageStatus
+ ___38-[CRPreflightController sign:keyBlob:]_block_invoke.162
+ ___48-[CRPreflightController queryRepairDelta:error:]_block_invoke.207
+ ___50-[CRPreflightController verify:signature:keyBlob:]_block_invoke.172
+ ___51-[CRPreflightController _diskImageSupportPreflight]_block_invoke.169
+ ___55-[CRPreflightController issueRepairCert:keyBlob:error:]_block_invoke.209
+ ___60-[CRFDRBaseDeviceHandler challengeComponentsWith:withReply:]_block_invoke.261
+ ___67-[CRPreflightController challengeStrongComponents:responses:error:]_block_invoke.215
+ ___81-[CRCAttestationManager sendChallengeRequestWith:requestID:serverResponse:error:]_block_invoke
+ ___81-[CRCAttestationManager sendChallengeRequestWith:requestID:serverResponse:error:]_block_invoke.225
+ ___81-[CRCAttestationManager sendChallengeRequestWith:requestID:serverResponse:error:]_block_invoke.cold.1
+ ___81-[CRCAttestationManager sendChallengeRequestWith:requestID:serverResponse:error:]_block_invoke.cold.2
+ ___81-[CRCAttestationManager sendChallengeRequestWith:requestID:serverResponse:error:]_block_invoke.cold.3
+ ___85-[CRCAttestationManager sendCertIssueRequestWith:requestID:serverCertResponse:error:]_block_invoke
+ ___85-[CRCAttestationManager sendCertIssueRequestWith:requestID:serverCertResponse:error:]_block_invoke.244
+ ___85-[CRCAttestationManager sendCertIssueRequestWith:requestID:serverCertResponse:error:]_block_invoke.cold.1
+ ___85-[CRCAttestationManager sendCertIssueRequestWith:requestID:serverCertResponse:error:]_block_invoke.cold.2
+ ___85-[CRCAttestationManager sendCertIssueRequestWith:requestID:serverCertResponse:error:]_block_invoke.cold.3
+ ___block_descriptor_tmp.181
+ ___block_literal_global.168
+ ___block_literal_global.171
+ ___block_literal_global.183
+ __verboseLogHandler
+ __verboseLogHandler.cold.1
+ _kMAUCRTSLVGStateKBBSharedSerial
+ _kMAUCRTSLVGStateKBBUniqueSerial
+ _objc_msgSend$copyCertificateValidityDate:queryNotValidAfter:error:
+ _objc_msgSend$decodePEM:
+ _objc_msgSend$extractSalvageState:error:
+ _objc_msgSend$initComponentsMapping
+ _objc_msgSend$isAtEnd
+ _objc_msgSend$isDateAfterEffectiveDate:
+ _objc_msgSend$isSalvagedKBBFromBAA:
+ _objc_msgSend$isSalvagedKBBFromUCRT
+ _objc_msgSend$localeWithLocaleIdentifier:
+ _objc_msgSend$pemFormattedStringFromData:
+ _objc_msgSend$queryCertificateProperties:oid:error:
+ _objc_msgSend$replaceObjectsAtIndexes:withObjects:
+ _objc_msgSend$scanString:intoString:
+ _objc_msgSend$scanUpToString:intoString:
+ _objc_msgSend$scannerWithString:
+ _objc_msgSend$sendCertIssueRequestWith:requestID:serverCertResponse:error:
+ _objc_msgSend$sendChallengeRequestWith:requestID:serverResponse:error:
- -[CRCAttestationManager sendCertIssueRequestWith:serverCertResponse:error:]
- -[CRCAttestationManager sendChallengeRequestWith:serverResponse:error:]
- -[CRFDRGen1DeviceHandler init]
- -[CRFDRGen2DeviceHandler init]
- -[CRFDRGen3DeviceHandler init]
- -[CRFDRGen4DeviceHandler init]
- -[CRFDRGen5DeviceHandler init]
- -[CRFDRGen6DeviceHandler init]
- -[CRFDRGen7DeviceHandler init]
- -[CRFDRLegacy2DeviceHandler init]
- -[CRFDRLegacyDeviceHandler init]
- -[CRFDRWatch1DeviceHandler init]
- -[CRFDRiPad1DeviceHandler init]
- GCC_except_table27
- ___38-[CRPreflightController sign:keyBlob:]_block_invoke.157
- ___48-[CRPreflightController queryRepairDelta:error:]_block_invoke.203
- ___50-[CRPreflightController verify:signature:keyBlob:]_block_invoke.167
- ___51-[CRPreflightController _diskImageSupportPreflight]_block_invoke.164
- ___55-[CRPreflightController issueRepairCert:keyBlob:error:]_block_invoke.205
- ___60-[CRFDRBaseDeviceHandler challengeComponentsWith:withReply:]_block_invoke.258
- ___67-[CRPreflightController challengeStrongComponents:responses:error:]_block_invoke.211
- ___71-[CRCAttestationManager sendChallengeRequestWith:serverResponse:error:]_block_invoke
- ___71-[CRCAttestationManager sendChallengeRequestWith:serverResponse:error:]_block_invoke.225
- ___71-[CRCAttestationManager sendChallengeRequestWith:serverResponse:error:]_block_invoke.cold.1
- ___71-[CRCAttestationManager sendChallengeRequestWith:serverResponse:error:]_block_invoke.cold.2
- ___71-[CRCAttestationManager sendChallengeRequestWith:serverResponse:error:]_block_invoke.cold.3
- ___75-[CRCAttestationManager sendCertIssueRequestWith:serverCertResponse:error:]_block_invoke
- ___75-[CRCAttestationManager sendCertIssueRequestWith:serverCertResponse:error:]_block_invoke.244
- ___75-[CRCAttestationManager sendCertIssueRequestWith:serverCertResponse:error:]_block_invoke.cold.1
- ___75-[CRCAttestationManager sendCertIssueRequestWith:serverCertResponse:error:]_block_invoke.cold.2
- ___75-[CRCAttestationManager sendCertIssueRequestWith:serverCertResponse:error:]_block_invoke.cold.3
- ___block_descriptor_tmp.170
- ___block_literal_global.163
- ___block_literal_global.166
- ___block_literal_global.172
- _copyCertificateValidityDate
- _createError
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$componentsWithRepairable:
- _objc_msgSend$initWithFormat:arguments:
- _objc_msgSend$removeObjectsAtIndexes:
- _objc_msgSend$sendCertIssueRequestWith:serverCertResponse:error:
- _objc_msgSend$sendChallengeRequestWith:serverResponse:error:
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x6
- _objc_retain_x9
CStrings:
+ "%@ count mismatch: sealed: %ld live: %ld"
+ "%@%@%@"
+ "/Library/Caches/com.apple.xbs/05BC2D32-1B21-4498-8369-DABC4A1C2388/TemporaryDirectory.TPxQAa/Sources/Pearl_Kernel/PearlFactoryLib/PearlFactoryLib.m"
+ "/Library/Caches/com.apple.xbs/0D5DB0DE-8B78-4337-8C24-2A796C2A60A9/TemporaryDirectory.9CsVvz/Sources/Mesa/AppleBiometricServices/MesaFactoryC/MesaFactoryC.c"
+ "2025/11/01"
+ "@32@0:8^@16^@24"
+ "@36@0:8@16B24^@28"
+ "@40@0:8^{__SecCertificate=}16@24^@32"
+ "Add ticket failed, error: %@, deviceInfo: %@"
+ "Adding local timezone: %@"
+ "B48@0:8@16@24^@32^@40"
+ "CAA repairHistory: %@ error: %@"
+ "CRCCertificateCrypto"
+ "CRCCertificateUtils"
+ "CRLogicBoardStatus"
+ "CRSalvageStatus"
+ "Cannot getting salvage state"
+ "DER sequence is invalid: %d"
+ "Error extracting salvage state from BAA: %@"
+ "Error getting salvage state: %@"
+ "Expected ASN1_CONSTR_SEQUENCE tag."
+ "Expected ASN1_CONSTR_SET or ASN1_CONSTR_SEQUENCE tag."
+ "Failed to PerformNextStage, error: %@, deviceInfo: %@"
+ "Failed to allocate dictionary."
+ "Failed to create string."
+ "Failed to decode BAA cert"
+ "Failed to decode DER encoded ANS1_OCTET_STRING."
+ "Failed to decode DER encoded ASN1_BOOLEAN: %d"
+ "Failed to decode DER encoded ASN1_INTEGER: %d"
+ "Failed to decode DER sequence: %d"
+ "Failed to intialize DER sequence: %d"
+ "Failed to parse BAA cert"
+ "Failed to parse DER integer: %d"
+ "Failed to personalize FW, error: %@, deviceInfo: %@"
+ "Failed to query DERSequence data for OID %@."
+ "Failed to read salvage date: %@"
+ "ForceMTUBStatus"
+ "Invalid DER tag."
+ "Invalid input(s)."
+ "Invalid property key length: %ld"
+ "KBB is salvaged in BAA. State: %@, Date: %@"
+ "KBB is salvaged in UCRT"
+ "Missing salvage date."
+ "No BAA cert provided"
+ "PerformNextStage failed, error: %@, deviceInfo: %@"
+ "SLVG"
+ "SavageCamInterface not supported"
+ "T@\"CRFDRBaseDeviceHandler\",&,V_handler"
+ "Timezone from boot intent: %@"
+ "UCRT salvage state: %@. date: %@"
+ "_handler"
+ "component: %@ isComponentRepairedUsingCAA: %d"
+ "component: %@ isComponentRepairedUsingFDR: %d"
+ "component: %@ isComponentRepairedUsingRCHL: %d"
+ "copyCertificateValidityDate:queryNotValidAfter:error:"
+ "createPEMFromCertificates:"
+ "decodePEM:"
+ "extractSalvageState:error:"
+ "initComponentsMapping"
+ "isAtEnd"
+ "isDateAfterEffectiveDate:"
+ "isSalvagedKBBFromBAA:"
+ "isSalvagedKBBFromUCRT"
+ "localeWithLocaleIdentifier:"
+ "pemFormattedStringFromData:"
+ "queryCertificateProperties:oid:error:"
+ "replaceObjectsAtIndexes:withObjects:"
+ "salvaged"
+ "scanString:intoString:"
+ "scanUpToString:intoString:"
+ "scannerWithString:"
+ "sendCertIssueRequestWith:requestID:serverCertResponse:error:"
+ "sendChallengeRequestWith:requestID:serverResponse:error:"
+ "slvd"
+ "timezone"
+ "yyyy/MM/dd"
+ "yyyyMMddHHmmss'Z'"
- "/Library/Caches/com.apple.xbs/Sources/Mesa/AppleBiometricServices/MesaFactoryC/MesaFactoryC.c"
- "/Library/Caches/com.apple.xbs/Sources/Pearl_Kernel/PearlFactoryLib/PearlFactoryLib.m"
- "Add Pearl ticket failed"
- "Failed to exec SavageUpdater command, result: %@"
- "Failed to personalize Savage FW, status: %d, error: %@"
- "SavageUpdaterExecCommand NextStage failed"
- "initWithFormat:arguments:"
- "removeObjectsAtIndexes:"
- "repairHistory: %@ error: %@"
- "sendCertIssueRequestWith:serverCertResponse:error:"
- "sendChallengeRequestWith:serverResponse:error:"

```
