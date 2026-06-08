## libSavageUpdater_iOS.dylib

> `/usr/lib/updaters/libSavageUpdater_iOS.dylib`

```diff

-6.72.7.0.0
-  __TEXT.__text: 0x18e10
-  __TEXT.__auth_stubs: 0x5e0
-  __TEXT.__cstring: 0x2fee
-  __TEXT.__const: 0x238
-  __TEXT.__gcc_except_tab: 0xd0
-  __TEXT.__oslogstring: 0xa0c
-  __TEXT.__unwind_info: 0x3e0
-  __TEXT.__objc_methname: 0x174
-  __TEXT.__objc_stubs: 0x200
-  __DATA_CONST.__got: 0x350
-  __DATA_CONST.__const: 0xd8
+7.113.1.0.0
+  __TEXT.__text: 0x1dc18
+  __TEXT.__gcc_except_tab: 0x114
+  __TEXT.__const: 0x638
+  __TEXT.__oslogstring: 0xa3a
+  __TEXT.__cstring: 0x481c
+  __TEXT.__unwind_info: 0x4d8
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_methname: 0x0
+  __DATA_CONST.__const: 0x680
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x80
-  __AUTH_CONST.__auth_got: 0x300
+  __DATA_CONST.__objc_selrefs: 0x88
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0xa0
-  __AUTH_CONST.__cfstring: 0x1000
+  __AUTH_CONST.__cfstring: 0x1ea0
+  __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__objc_intobj: 0x30
-  __DATA.__common: 0x1040
-  __DATA.__bss: 0x1020
+  __AUTH_CONST.__auth_got: 0x300
+  __DATA.__data: 0x20
+  __DATA.__common: 0x1050
+  __DATA.__bss: 0x2020
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/updaters/libSavageRestoreInfo_iOS.dylib
-  UUID: A2CA7F2F-3E35-370D-93B4-AC2F8DCFC821
-  Functions: 427
-  Symbols:   1331
-  CStrings:  624
+  UUID: 128675EC-51D9-3924-B1E5-5D976830301E
+  Functions: 486
+  Symbols:   1509
+  CStrings:  899
 
Symbols:
+ GCC_except_table8
+ _CFDataSetLength
+ _CreateCFErrorWithinSavageDomain
+ _GetYonkersIRFabRevisionTags
+ _GetYonkersIRMeasurementTags
+ _GetYonkersIRxMeasurementTags
+ __ZL16supportedFabRevs
+ __ZN16YonkersIRxDevice10myInstanceE
+ __ZN16YonkersIRxDevice11SetupDeviceEv
+ __ZN16YonkersIRxDevice11getInstanceEv
+ __ZN16YonkersIRxDevice14PrePersonalizeEj
+ __ZN16YonkersIRxDevice15destroyInstanceEv
+ __ZN16YonkersIRxDevice17PublishToRegistryEPK10__CFStringS2_PK8__CFData
+ __ZN16YonkersIRxDevice19YonkersIRxDeviceLogEPKcz
+ __ZN16YonkersIRxDevice20CreateDeviceInfoDictEP14__CFDictionaryj
+ __ZN16YonkersIRxDevice20YonkersIRxDeviceOpenEv
+ __ZN16YonkersIRxDevice20YonkersIRxDeviceOpenEv.cold.1
+ __ZN16YonkersIRxDevice21YonkersIRxDeviceCloseEv
+ __ZN16YonkersIRxDevice23CheckProvisioningStatusEj
+ __ZN16YonkersIRxDevice6FusingEjPKhj
+ __ZN16YonkersIRxDevice8AuthFlowEjPKhj
+ __ZN16YonkersIRxDevice9PreFusingEj
+ __ZN16YonkersIRxDeviceC1Ev
+ __ZN16YonkersIRxDeviceC2Ev
+ __ZN16YonkersIRxDeviceD1Ev
+ __ZN16YonkersIRxDeviceD2Ev
+ __ZN26YonkersIRxUpdateController10myInstanceE
+ __ZN26YonkersIRxUpdateController11execCommandEPK10__CFStringPK14__CFDictionaryPS5_
+ __ZN26YonkersIRxUpdateController11getFirmwareEPPhPjPK10__CFString
+ __ZN26YonkersIRxUpdateController11getInstanceEPK14__CFDictionaryPvS3_
+ __ZN26YonkersIRxUpdateController13YonkersIRxLogEPKcz
+ __ZN26YonkersIRxUpdateController14getTSSResponseEv
+ __ZN26YonkersIRxUpdateController14libFDRCallbackE18AMFDRCryptoVersionPK8__CFDataPS3_Pv
+ __ZN26YonkersIRxUpdateController15destroyInstanceEv
+ __ZN26YonkersIRxUpdateController16getAuthChallengeEv
+ __ZN26YonkersIRxUpdateController17eventCmdQueryInfoEv
+ __ZN26YonkersIRxUpdateController18writeDataToFileURLEPhjPK10__CFString
+ __ZN26YonkersIRxUpdateController20formatAndStitchFilesEv
+ __ZN26YonkersIRxUpdateController20getSignedCertificateEPhj
+ __ZN26YonkersIRxUpdateController22writeFilesToFileSystemEv
+ __ZN26YonkersIRxUpdateController24eventCmdPerformNextStageEv
+ __ZN26YonkersIRxUpdateController29eventCmdQueryInfoPreflightingEv
+ __ZN26YonkersIRxUpdateController5startEPK14__CFDictionary
+ __ZN26YonkersIRxUpdateControllerC1Ev
+ __ZN26YonkersIRxUpdateControllerC2Ev
+ __ZN26YonkersIRxUpdateControllerD1Ev
+ __ZN26YonkersIRxUpdateControllerD2Ev
+ _cleanIOServiceConnection
+ _cleanIOServiceConnection.cold.1
+ _decompressReferenceFrames.cold.29
+ _initializeIOServiceConnectionWithName
+ _initializeIOServiceConnectionWithName.cold.1
+ _initializeIOServiceConnectionWithName.cold.2
+ _initializeIOServiceConnectionWithName.cold.3
+ _initializeIOServiceConnectionWithName.cold.4
+ _kYonkersIR1TagAllowOfflineBoot
+ _kYonkersIR1TagAuthenticate
+ _kYonkersIR1TagChipID
+ _kYonkersIR1TagDeviceInfo
+ _kYonkersIR1TagECID
+ _kYonkersIR1TagFabRevision
+ _kYonkersIR1TagFirmwareData
+ _kYonkersIR1TagNonce
+ _kYonkersIR1TagProductionMode
+ _kYonkersIR1TagProvenance
+ _kYonkersIR1TagReadECKey
+ _kYonkersIR1TagReadFWKey
+ _kYonkersIR1TagReadGID
+ _kYonkersIR1TagResponseTicket
+ _kYonkersIR1TagWriteECID
+ _kYonkersIR1TagWriteECKey
+ _kYonkersIR2TagAllowOfflineBoot
+ _kYonkersIR2TagAuthenticate
+ _kYonkersIR2TagChipID
+ _kYonkersIR2TagDeviceInfo
+ _kYonkersIR2TagECID
+ _kYonkersIR2TagFabRevision
+ _kYonkersIR2TagFirmwareData
+ _kYonkersIR2TagNonce
+ _kYonkersIR2TagProductionMode
+ _kYonkersIR2TagProvenance
+ _kYonkersIR2TagReadECKey
+ _kYonkersIR2TagReadFWKey
+ _kYonkersIR2TagReadGID
+ _kYonkersIR2TagResponseTicket
+ _kYonkersIR2TagWriteECID
+ _kYonkersIR2TagWriteECKey
+ _kYonkersIR3TagChipID
+ _kYonkersIR3TagDeviceInfo
+ _kYonkersIR3TagECID
+ _kYonkersIR3TagFabRevision
+ _kYonkersIR3TagFirmwareData
+ _kYonkersIR3TagNonce
+ _kYonkersIR3TagProductionMode
+ _kYonkersIR3TagResponseTicket
+ _kYonkersIR4TagChipID
+ _kYonkersIR4TagDeviceInfo
+ _kYonkersIR4TagECID
+ _kYonkersIR4TagFabRevision
+ _kYonkersIR4TagFirmwareData
+ _kYonkersIR4TagNonce
+ _kYonkersIR4TagProductionMode
+ _kYonkersIR4TagResponseTicket
+ _kYonkersIRErrorDomain
+ _kYonkersIROptions
+ _kYonkersIRPreflightRequiredOption
+ _kYonkersIRSkipOption
+ _kYonkersIRxErrorDomain
+ _objc_msgSend$stringByAppendingPathComponent:
+ _objc_storeStrong
+ _yonkersIRSensorNames
- _GetJasmineIRFabRevisionTags
- _OUTLINED_FUNCTION_55
- _OUTLINED_FUNCTION_56
- _OUTLINED_FUNCTION_57
- _OUTLINED_FUNCTION_58
- _OUTLINED_FUNCTION_59
- _OUTLINED_FUNCTION_60
- _OUTLINED_FUNCTION_61
- _OUTLINED_FUNCTION_62
- _SavageUpdaterExecCmd
- _SavageUpdaterSupported
- __ZN13YonkersDevice18CreateCertInfoBlobEP26YonkersToBeCertifiedBlob_t
- __ZN15JasmineIRDevice18CreateCertInfoBlobEP28JasmineIRToBeCertifiedBlob_t
CStrings:
+ "\n YonkersIRx: %s \n"
+ "%s"
+ "%s - %p (%p) - UpdaterIsSupported = %d; numInstances = %d; \n"
+ "%s - %p (%p) - UpdaterIsSupported = %d; numInstances = %d; YonkersIRIsPresent[%d] = %d \n"
+ "%s - Finding %s \n"
+ "%s - YonkersIRxIsPresent[%d] = %d; chipID = 0x%04x\n"
+ "%s - numInstances = %d; updaterSupported = %d\n"
+ "%s: Begin Provenance Certification Flow \n"
+ "%s: Begin reading info needed for certification - %d\n"
+ "%s: Begin reading info needed for provenance certification - %d\n"
+ "%s: Entering execCommand: command = %s, numPersoLoopForInstance[%d] = %d \n"
+ "%s: Exiting execCommand: command = %s, result = 0x%X, numInstance = %d \n"
+ "%s: Extracting provenance certification data is done with result = 0x%02X (tryAgain = %d) \n"
+ "%s: Finished Personalization - %d \n"
+ "%s: Finished eventCmdQueryInfo %d \n"
+ "%s: Finished pre-prov-certification \n"
+ "%s: Including auth challenge key in the DAT file \n"
+ "%s: Missing FDRDataEncryptionKey in ioreg - 0x%02X \n"
+ "%sPubKey"
+ "%sPubKeyHmac"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/Pearl_Kernel/PearlSupport/PearlSupportUtils.m"
+ "/usr/standalone/firmware/"
+ "AssertMacros: %s (value = 0x%lx), %s file: %s, line: %d\n"
+ "AuthCSR"
+ "AuthPubKey"
+ "AuthPubKeyHmac"
+ "AuthResponse"
+ "AuthSalt"
+ "CheckProvisioningStatus"
+ "CreateDeviceInfoDict"
+ "ECPubKey"
+ "ECPubKeyHmac"
+ "PersonalizeOnlyThisInstance"
+ "ProvPubKey"
+ "ProvPubKeyHmac"
+ "ProvenanceCertOption"
+ "SavageMacAlgo"
+ "SavageUpdaterCreate - no yonkersIRx controller instance"
+ "SavageUpdaterExecCommand - no yonkersIRx controller instance"
+ "SavageUpdaterIsDone - no yonkersIRx controller instance"
+ "YonkersIR%d,SysTopPatch%X"
+ "YonkersIR/YonkersIR.Dev.fw"
+ "YonkersIR/YonkersIR.Prod.fw"
+ "YonkersIR/YonkersIR1BinaryPlusHeaderPatch.FW"
+ "YonkersIR/YonkersIR1BinaryPlusHeaderPatchAuthCertification.FW"
+ "YonkersIR/YonkersIR1BinaryPlusHeaderPatchCertification.FW"
+ "YonkersIR/YonkersIR1BinaryPlusHeaderPatchFusing.FW"
+ "YonkersIR/YonkersIR1BinaryPlusHeaderPatchProvCertification.FW"
+ "YonkersIR/YonkersIR1Patch.DAT"
+ "YonkersIR/YonkersIR1Patch.DER"
+ "YonkersIR/YonkersIR1PatchAuthCertification.DAT"
+ "YonkersIR/YonkersIR1PatchAuthCertification.DER"
+ "YonkersIR/YonkersIR1PatchCertification.DAT"
+ "YonkersIR/YonkersIR1PatchCertification.DER"
+ "YonkersIR/YonkersIR1PatchFusing.DAT"
+ "YonkersIR/YonkersIR1PatchFusing.DER"
+ "YonkersIR/YonkersIR1PatchProvCertification.DAT"
+ "YonkersIR/YonkersIR1PatchProvCertification.DER"
+ "YonkersIR/YonkersIR2BinaryPlusHeaderPatch.FW"
+ "YonkersIR/YonkersIR2BinaryPlusHeaderPatchAuthCertification.FW"
+ "YonkersIR/YonkersIR2BinaryPlusHeaderPatchCertification.FW"
+ "YonkersIR/YonkersIR2BinaryPlusHeaderPatchFusing.FW"
+ "YonkersIR/YonkersIR2BinaryPlusHeaderPatchProvCertification.FW"
+ "YonkersIR/YonkersIR2Patch.DAT"
+ "YonkersIR/YonkersIR2Patch.DER"
+ "YonkersIR/YonkersIR2PatchAuthCertification.DAT"
+ "YonkersIR/YonkersIR2PatchAuthCertification.DER"
+ "YonkersIR/YonkersIR2PatchCertification.DAT"
+ "YonkersIR/YonkersIR2PatchCertification.DER"
+ "YonkersIR/YonkersIR2PatchFusing.DAT"
+ "YonkersIR/YonkersIR2PatchFusing.DER"
+ "YonkersIR/YonkersIR2PatchProvCertification.DAT"
+ "YonkersIR/YonkersIR2PatchProvCertification.DER"
+ "YonkersIR/YonkersIR3BinaryPlusHeaderPatch.FW"
+ "YonkersIR/YonkersIR3BinaryPlusHeaderPatchAuthCertification.FW"
+ "YonkersIR/YonkersIR3BinaryPlusHeaderPatchCertification.FW"
+ "YonkersIR/YonkersIR3BinaryPlusHeaderPatchFusing.FW"
+ "YonkersIR/YonkersIR3BinaryPlusHeaderPatchProvCertification.FW"
+ "YonkersIR/YonkersIR3Patch.DAT"
+ "YonkersIR/YonkersIR3Patch.DER"
+ "YonkersIR/YonkersIR3PatchAuthCertification.DAT"
+ "YonkersIR/YonkersIR3PatchAuthCertification.DER"
+ "YonkersIR/YonkersIR3PatchCertification.DAT"
+ "YonkersIR/YonkersIR3PatchCertification.DER"
+ "YonkersIR/YonkersIR3PatchFusing.DAT"
+ "YonkersIR/YonkersIR3PatchFusing.DER"
+ "YonkersIR/YonkersIR3PatchProvCertification.DAT"
+ "YonkersIR/YonkersIR3PatchProvCertification.DER"
+ "YonkersIR/YonkersIR4BinaryPlusHeaderPatch.FW"
+ "YonkersIR/YonkersIR4BinaryPlusHeaderPatchAuthCertification.FW"
+ "YonkersIR/YonkersIR4BinaryPlusHeaderPatchCertification.FW"
+ "YonkersIR/YonkersIR4BinaryPlusHeaderPatchFusing.FW"
+ "YonkersIR/YonkersIR4BinaryPlusHeaderPatchProvCertification.FW"
+ "YonkersIR/YonkersIR4Patch.DAT"
+ "YonkersIR/YonkersIR4Patch.DER"
+ "YonkersIR/YonkersIR4PatchAuthCertification.DAT"
+ "YonkersIR/YonkersIR4PatchAuthCertification.DER"
+ "YonkersIR/YonkersIR4PatchCertification.DAT"
+ "YonkersIR/YonkersIR4PatchCertification.DER"
+ "YonkersIR/YonkersIR4PatchFusing.DAT"
+ "YonkersIR/YonkersIR4PatchFusing.DER"
+ "YonkersIR/YonkersIR4PatchProvCertification.DAT"
+ "YonkersIR/YonkersIR4PatchProvCertification.DER"
+ "YonkersIR1"
+ "YonkersIR1AuthPubKey"
+ "YonkersIR1AuthPubKeyHmac"
+ "YonkersIR1AuthResponse"
+ "YonkersIR1AuthSalt"
+ "YonkersIR1ChipID"
+ "YonkersIR1ECPubKeyHmac"
+ "YonkersIR1FabRevision"
+ "YonkersIR1MNS"
+ "YonkersIR1MacAlgo"
+ "YonkersIR1Nonce"
+ "YonkersIR1ProvPubKeyHmac"
+ "YonkersIR1UID"
+ "YonkersIR2"
+ "YonkersIR2AuthPubKey"
+ "YonkersIR2AuthPubKeyHmac"
+ "YonkersIR2AuthResponse"
+ "YonkersIR2AuthSalt"
+ "YonkersIR2ChipID"
+ "YonkersIR2ECPubKeyHmac"
+ "YonkersIR2FabRevision"
+ "YonkersIR2MNS"
+ "YonkersIR2MacAlgo"
+ "YonkersIR2Nonce"
+ "YonkersIR2ProvPubKeyHmac"
+ "YonkersIR2UID"
+ "YonkersIR3"
+ "YonkersIR3AuthPubKey"
+ "YonkersIR3AuthPubKeyHmac"
+ "YonkersIR3AuthResponse"
+ "YonkersIR3AuthSalt"
+ "YonkersIR3ChipID"
+ "YonkersIR3ECPubKeyHmac"
+ "YonkersIR3FabRevision"
+ "YonkersIR3MNS"
+ "YonkersIR3MacAlgo"
+ "YonkersIR3Nonce"
+ "YonkersIR3ProvPubKeyHmac"
+ "YonkersIR3UID"
+ "YonkersIR4"
+ "YonkersIR4propNam"
+ "YonkersIRErrorDomain"
+ "YonkersIRUpdateController::start: isProvisioned[%d]=0x%llX; numPersoLoopForInstance[%d]=%d \n"
+ "YonkersIRx: No yonkersIRxOptions \n"
+ "YonkersIRx: Signed Certificate (TSS Response):-------------- Length = %d \n"
+ "YonkersIRx: YonkersIRxUpdateController::eventCmdQueryInfoPreflighting: Begin Preflighting for sensor number %d \n"
+ "YonkersIRx: YonkersIRxUpdateController::eventCmdQueryInfoPreflighting: Finished Preflighting for sensor number %d (result = %d)\n"
+ "YonkersIRx: restoreOptions missing or not a dictionary\n"
+ "YonkersIRxDeviceLog: %s \n"
+ "YonkersIRxDeviceOpen"
+ "YonkersIRxErrorDomain"
+ "YonkersIRxLog: %s \n"
+ "YonkersIRxUpdateController::formatAndStitchFiles() -  theCompletePatchFileLen=%d, signedCertificateLen=%d, firmwareDataLen=%d \n"
+ "YonkersIRxUpdateController::writeFilesToFileSystem(): %s (%d)\n"
+ "YonkersIRxUpdateController::writeFilesToFileSystem: numPersoLoopForInstance[%d]=%d, isProd=%d \n"
+ "_LeftBcam"
+ "_LeftEcam"
+ "_RightBcam"
+ "_RightEcam"
+ "_connect != ((io_object_t) 0)"
+ "camChannel"
+ "connect"
+ "dataInfo->setCount <= (4)"
+ "furei"
+ "glenbrook"
+ "lakeville"
+ "numSensorInstance"
+ "outConnect"
+ "pData"
+ "sensorIsProvisioned"
+ "sensorType"
+ "serviceName"
- "URLWithString:"
- "UTF8String"
- "YonkersPubKey"
- "bytes"
- "createDirectoryAtPath:withIntermediateDirectories:attributes:error:"
- "dataWithBytesNoCopy:length:freeWhenDone:"
- "defaultManager"
- "dictionary"
- "dictionaryWithDictionary:"
- "dictionaryWithObjects:forKeys:count:"
- "fileExistsAtPath:"
- "length"
- "removeItemAtPath:error:"
- "setObject:forKeyedSubscript:"
- "stringWithFormat:"
- "stringWithUTF8String:"
- "writeToFile:atomically:"

```
