## libauthinstall.dylib

> `/usr/lib/libauthinstall.dylib`

```diff

-1033.80.3.0.0
-  __TEXT.__text: 0x95e40
-  __TEXT.__auth_stubs: 0x1870
-  __TEXT.__objc_methlist: 0x2738
-  __TEXT.__cstring: 0x1d6a4
-  __TEXT.__const: 0x626b
+1049.100.21.0.0
+  __TEXT.__text: 0x93b20
+  __TEXT.__auth_stubs: 0x1880
+  __TEXT.__objc_methlist: 0x27cc
+  __TEXT.__cstring: 0x1c575
+  __TEXT.__const: 0x6209
   __TEXT.__oslogstring: 0x518
-  __TEXT.__gcc_except_tab: 0x2e3c
-  __TEXT.__unwind_info: 0x2368
-  __TEXT.__objc_classname: 0x89e
-  __TEXT.__objc_methname: 0x28fa
-  __TEXT.__objc_methtype: 0x767
+  __TEXT.__gcc_except_tab: 0x2e78
+  __TEXT.__unwind_info: 0x2560
+  __TEXT.__objc_classname: 0x8a8
+  __TEXT.__objc_methname: 0x28ff
+  __TEXT.__objc_methtype: 0x777
   __TEXT.__objc_stubs: 0x2380
-  __DATA_CONST.__got: 0x3c8
-  __DATA_CONST.__const: 0x2328
+  __DATA_CONST.__got: 0x3b8
+  __DATA_CONST.__const: 0x22a0
   __DATA_CONST.__objc_classlist: 0x200
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x28

   __DATA_CONST.__objc_selrefs: 0xb58
   __DATA_CONST.__objc_superrefs: 0x1f8
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__auth_got: 0xc50
+  __AUTH_CONST.__auth_got: 0xc58
   __AUTH_CONST.__auth_ptr: 0x28
   __AUTH_CONST.__const: 0x1218
-  __AUTH_CONST.__cfstring: 0xd2a0
-  __AUTH_CONST.__objc_const: 0x4ce8
+  __AUTH_CONST.__cfstring: 0xca60
+  __AUTH_CONST.__objc_const: 0x4c18
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH.__objc_data: 0x1400
   __AUTH.__data: 0x20
   __DATA.__objc_ivar: 0x328
   __DATA.__data: 0x768
-  __DATA.__bss: 0xda0
-  __DATA.__common: 0x1010
+  __DATA.__bss: 0xd90
+  __DATA.__common: 0x10
   __DATA_DIRTY.__data: 0x38
   __DATA_DIRTY.__bss: 0x18
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
+  - /usr/lib/updaters/libSavageRestoreInfo_iOS.dylib
   - /usr/lib/updaters/libT200Updater.dylib
-  Functions: 2391
-  Symbols:   3484
-  CStrings:  5019
+  Functions: 3138
+  Symbols:   4309
+  CStrings:  4887
 
Symbols:
+ _AMAuthInstallBundleSetEntryEnabled
+ _AMAuthInstallSupportCreateDataFromMappedFileURL
+ _AMSupportCreateArrayFromFileURL
+ _AMSupportCreateDictionaryFromFileURL
+ _AMSupportPlatformCreateDataFromFileURL
+ _AMSupportPlatformCreateDataFromMappedFileURL
+ _AMSupportPlatformOpenFileStreamWithURL
+ _AMSupportPlatformWriteDataToFileURL
+ _SavageUpdaterCopyFirmwareWithLogging
+ _SavageUpdaterCreateRequestWithLogging
+ _SavageUpdaterGetTagsWithLogging
+ _fileno
- _AMSupportPlatformFileURLExists
- _CFStringGetMaximumSizeForEncoding
- _kCFCopyStringDictionaryKeyCallBacks
- _objc_retain_x25
- _read
- _rewind
- _write
CStrings:
+ "%s::%s: no dataref\n"
+ "%s::%s: no digest in build ID (%s)\n"
+ "%s::%s: optional tag %s missing from build identity, skipping\n"
+ "%s::%s: tag %s missing from firmware, skipping\n"
+ "%s::%s: wrong digest type (%s)\n"
+ "-[MantaFTABFile addSubfileWithTagName:contentsOfURL:]"
+ "-[MantaFTABFile initWithContentsOfURL:]"
+ "-[MantaFTABFile parseFileData]"
+ "@\"MantaFTABSubfile\""
+ "AMAuthInstallPlatformCreateDataFromMappedFileURL returned %d"
+ "Ap,SecurePageTableMonitor"
+ "Ap,TrustedExecutionMonitor"
+ "Ap,cL4"
+ "HelsinkiRestore-56.4.12"
+ "MantaFTABFile"
+ "MantaFTABSubfile"
+ "T@\"MantaFTABSubfile\",R,V_manifest"
+ "VinylRestore-78~6589"
+ "_AMAuthInstallApImg4StitchToURL"
+ "_AMAuthInstallSupportCreateDataFromCopiedOrMappedFileURL"
+ "_WriteStreamIntoFile"
+ "createRequest: no digest in build ID"
+ "createRequest: wrong digest type"
+ "excl"
+ "libauthinstall_device-1049.100.21"
+ "q24@0:8@16"
+ "sptm"
+ "trxm"
- "%@: %s"
- "%@: Input Options: %@"
- "%s [error]: %s \n"
- "%s [input]: BuildIdentity %s \n"
- "%s [input]: DeviceInfo %s \n"
- "%s [input]: FirmwareData %s \n"
- "%s [input]: Input Options - %s \n"
- "%s [input]: SEP Digest from ReceiptManifest - %s \n"
- "%s [input]: SavageMeasurementDict - %s \n"
- "%s [input]: YonkersMeasurementDict - %s \n"
- "%s [output]: %s \n"
- "%s: Device side restoreInfo path \n"
- "%s: Host side restoreInfo path \n"
- "%s::%s: Tag '%s' doesn't exist -- moving along\n"
- "-[FTABFile addSubfileWithTagName:contentsOfURL:]"
- "-[FTABFile initWithContentsOfURL:]"
- "-[FTABFile parseFileData]"
- ".."
- "@\"FTABSubfile\""
- "@Brunor,Ticket"
- "@Savage,Ticket"
- "@Yonkers,Ticket"
- "AMAuthInstallApImg4Stitch"
- "AMAuthInstallPlatformCreateBufferFromNativeFilePath"
- "AMAuthInstallPlatformOpenFileStreamWithURL"
- "AMAuthInstallPlatformWriteBufferToNativeFilePath"
- "AMAuthInstallSupportCreateArrayFromFileURL"
- "AMAuthInstallSupportCreateDataFromFileURL"
- "AMAuthInstallSupportCreateDictionaryFromFileURL"
- "AMAuthInstallSupportWriteDictionarytoFileURL"
- "AMSupportCreateDataFromFileURL returned %d"
- "Brunor,Authenticate"
- "Brunor,FdrRootCaDigest"
- "Brunor,HarvestUnwrap"
- "Brunor,HarvestWrap"
- "Brunor,Ticket"
- "CreateFileData"
- "CreateFileData: AMSupportPlatformFileURLExists returned FALSE"
- "CreateFileData: Fail to run AMSupportCreateDataFromFileURL"
- "CreateFileData: Fail to run AMSupportMakeDirectory with dstFilePathURL"
- "CreateFileData: Fail to run AMSupportPlatformCopyURLWithAppendedComponent with dstBundleURL"
- "CreateFileData: Fail to run AMSupportPlatformCopyURLWithAppendedComponent with srcBundleURL"
- "CreateFileData: Fail to run AMSupportWriteDataToFileURL with dstFilePathURL"
- "CreateFileData: Missing kSavageBuildIdentityInfoKey"
- "CreateFileData: Missing kSavageBuildIdentityPathKey"
- "CreateFileData: Missing kSavageOptionBuildIdentity"
- "CreateFileData: Missing kSavageOptionSourceBundlePath"
- "CreateFileData: bundleDataDict missing expected tag"
- "FTABFile"
- "FTABSubfile"
- "FabRevision"
- "HelsinkiRestore-56.3.2"
- "MeasurementDictPatch"
- "No C string description available."
- "Savage,AccessSecurity"
- "Savage,AccessSensor"
- "Savage,AllowOfflineBoot"
- "Savage,B0-Dev-Patch"
- "Savage,B0-Prod-Patch"
- "Savage,B2-Dev-Patch"
- "Savage,B2-Prod-Patch"
- "Savage,BA-Dev-Patch"
- "Savage,BA-Prod-Patch"
- "Savage,BE-Dev-Patch"
- "Savage,BE-Prod-Patch"
- "Savage,BF-Dev-Patch"
- "Savage,BF-Prod-Patch"
- "Savage,ChipID"
- "Savage,DebugStatus"
- "Savage,FADemote"
- "Savage,Nonce"
- "Savage,PatchEpoch"
- "Savage,ProductionMode"
- "Savage,Provisioning"
- "Savage,ReadECKey"
- "Savage,ReadFWKey"
- "Savage,ReadGID"
- "Savage,Revision"
- "Savage,TempDemote"
- "Savage,Ticket"
- "Savage,UID"
- "Savage,WriteECKey"
- "Savage,WriteEpoch"
- "Savage,WriteUID"
- "SavageCFDictionarySetInteger32"
- "SavageErrorDomain"
- "SavageFirmware"
- "SavagePrivateHelper.cpp"
- "SavageUpdaterCopyFirmware"
- "SavageUpdaterCopyFirmware: Cannot allocate memory for outputDict"
- "SavageUpdaterCopyFirmware: Cannot allocate memory for savageFirmwareData"
- "SavageUpdaterCopyFirmware: Didn't get yonkers patch measurement tags"
- "SavageUpdaterCopyFirmware: Empty Savage firmware file"
- "SavageUpdaterCopyFirmware: Empty Yonkers alt firmware file?"
- "SavageUpdaterCopyFirmware: Empty Yonkers firmware file?"
- "SavageUpdaterCopyFirmware: Missing device info"
- "SavageUpdaterCopyFirmware: Unable to get savage patch measurement tags"
- "SavageUpdaterCopyFirmware: options is NULL"
- "SavageUpdaterCreateRequest"
- "SavageUpdaterCreateRequest: BuildIdentity is NULL in input options"
- "SavageUpdaterCreateRequest: Cannot get DeviceInfo"
- "SavageUpdaterCreateRequest: CreateMeasurementDict fails for Savage (Old way)."
- "SavageUpdaterCreateRequest: CreateMeasurementDict fails for Savage."
- "SavageUpdaterCreateRequest: CreateMeasurementDict fails for Yonkers."
- "SavageUpdaterCreateRequest: CreateRequestDictForTATSU fails."
- "SavageUpdaterCreateRequest: CreateYonkersRequestDictForTATSU fails."
- "SavageUpdaterCreateRequest: ReceiptManifest is missing in input options"
- "SavageUpdaterCreateRequest: kSavageOptionFirmwareData is NULL in input options"
- "SavageUpdaterCreateRequest: options is NULL"
- "SavageUpdaterGetTags"
- "SavageUpdaterGetTags: Cannot allocate memory for outputDict"
- "SavageUpdaterGetTags: Cannot allocate memory for tagsInBI"
- "SavageUpdaterGetTags: Cannot allocate memory for tagsInTssResponse"
- "SavageUpdaterGetTags: DeviceInfo is NULL?"
- "SavageUpdaterGetTags: Unable to get kSavageTagMeasurementPatch"
- "SavageUpdaterGetTags: Unable to get kSavageTagMeasurementPatchRepair"
- "SavageUpdaterGetTags: Unable to get kYonkersTagMeasurementPatch"
- "SavageUpdaterGetTags: options is NULL"
- "T@\"FTABSubfile\",R,V_manifest"
- "Unsupported image type %d"
- "VinylRestore-78~6396"
- "Yonkers,AccessSecurity"
- "Yonkers,AccessSensor"
- "Yonkers,AllowOfflineBoot"
- "Yonkers,BoardID"
- "Yonkers,ChipID"
- "Yonkers,DebugStatus"
- "Yonkers,ECID"
- "Yonkers,FADemote"
- "Yonkers,FabRevision"
- "Yonkers,Nonce"
- "Yonkers,PatchEpoch"
- "Yonkers,ProductionMode"
- "Yonkers,Provisioning"
- "Yonkers,ReadECKey"
- "Yonkers,ReadFWKey"
- "Yonkers,ReadGID"
- "Yonkers,SysTopPatch%X"
- "Yonkers,TempDemote"
- "Yonkers,Ticket"
- "Yonkers,WriteECID"
- "Yonkers,WriteECKey"
- "Yonkers,WriteEpoch"
- "YonkersDeviceInfo"
- "YonkersErrorDomain"
- "YonkersFirmware"
- "YonkersFirmwareAlt"
- "YonkersIsProvisioned"
- "YonkersIsYmgt"
- "failed to convert url to file system representation"
- "failed to create property list: %@"
- "failed to open file for writing: %s"
- "failed to stitch img4 file"
- "fstat failed: %s"
- "libauthinstall_device-1033.80.3"
- "malloc(%d) failed: %s"
- "open failed: %s"
- "path: %s"
- "read failed: %s"
- "srcFileURL is NULL"

```
