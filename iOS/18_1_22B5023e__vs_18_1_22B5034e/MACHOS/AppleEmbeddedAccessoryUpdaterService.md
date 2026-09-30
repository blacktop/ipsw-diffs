## AppleEmbeddedAccessoryUpdaterService

> `/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/AppleEmbeddedAccessoryUpdaterService.xpc/AppleEmbeddedAccessoryUpdaterService`

```diff

-3148.40.4.0.1
-  __TEXT.__text: 0x6d9e0
-  __TEXT.__auth_stubs: 0x1730
+3148.40.18.0.0
+  __TEXT.__text: 0x70320
+  __TEXT.__auth_stubs: 0x1750
   __TEXT.__objc_stubs: 0x2c80
   __TEXT.__objc_methlist: 0x2b38
-  __TEXT.__const: 0x57d0
+  __TEXT.__const: 0x57e0
   __TEXT.__gcc_except_tab: 0x1d4
-  __TEXT.__cstring: 0x1613a
+  __TEXT.__cstring: 0x166d9
   __TEXT.__objc_methname: 0x3610
   __TEXT.__objc_classname: 0xb08
   __TEXT.__objc_methtype: 0xd10
-  __TEXT.__oslogstring: 0x7ff
-  __TEXT.__unwind_info: 0x15f8
-  __DATA_CONST.__auth_got: 0xba8
+  __TEXT.__oslogstring: 0x835
+  __TEXT.__unwind_info: 0x1608
+  __DATA_CONST.__auth_got: 0xbb8
   __DATA_CONST.__got: 0x358
   __DATA_CONST.__auth_ptr: 0x18
   __DATA_CONST.__const: 0x2060
-  __DATA_CONST.__cfstring: 0xf3c0
+  __DATA_CONST.__cfstring: 0xf460
   __DATA_CONST.__objc_classlist: 0x218
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x58

   __DATA.__objc_selrefs: 0xea0
   __DATA.__objc_ivar: 0x37c
   __DATA.__objc_data: 0x14f0
-  __DATA.__data: 0xaa0
-  __DATA.__bss: 0x958
+  __DATA.__data: 0xab0
+  __DATA.__bss: 0xb00
   __DATA.__common: 0x28
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/liblzma.5.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 1952
-  Symbols:   1729
-  CStrings:  4393
+  Functions: 2010
+  Symbols:   1733
+  CStrings:  4452
 
Symbols:
+ _AMSupportLogSetHandler
+ _AMRestoreCaptureSubsystemLogs
+ _AMRestoreCaptureSubsystemLogsIfNeeded
+ _AMFDRLogSetHandler
+ _dlerror
- _AMRecoveryModeDeviceCopyEpochsData
CStrings:
+ "AMFDRSealingMapGetEntry"
+ "libauthinstall_device-1033.40.2"
+ "AMFDRCopyDisposableKeys"
+ "AMFDRSealedDataPopulate"
+ "AMFDRSealingMapVerifySealing"
+ "AMFDRSetSealingMap"
+ "AMFDRSealingMapRecoverCurrentDevice"
+ "AMFDRCreateWithOptions"
+ "AMFDRDataMultiPut"
+ "failed to load '%!s(MISSING)' from '%!s(MISSING)'\n"
+ "AMFDRSealingMapCreateAndPopulateSealedData"
+ "AMFDRDataCopySslRoots"
+ "AMFDRSealingMapCopyRequiredIdentifiers"
+ "AMFDRDataPrefetch"
+ "AMFDRDataPresent"
+ "AMFDRLogSetHandler"
+ "AMFDRDataPut"
+ "AMFDRGetTrustError"
+ "AMFDRDataMultiExport"
+ "AMFDRSetOption"
+ "AMFDRSetRecoveryVerifier"
+ "AMFDRDataDelete"
+ "AMFDRDataLocalCreateFullKey"
+ "AMFDRSealedDataCreate"
+ "Failed to read build variant."
+ "Info.RequiresNonceSlot"
+ "AMFDRSealingMapCopyLocalData"
+ "AMFDRCreateLocalPending"
+ "AMFDRSealingMapGetEntriesForDevice"
+ "AMFDRAppendPermissionsString"
+ "AMFDRSealingMapSetMGCopyAnswer"
+ "AMFDRCreateInstanceString"
+ "AMFDRDataMultiDelete"
+ "AMFDRDataCopyDigest"
+ "AMFDRDataRecover"
+ "AMFDRSealingMapCopyLocalDataForClass"
+ "AMFDRDataPutForSysCfgKey"
+ "AMFDRDataCopyTrustObject"
+ "AMFDRCopyUnderlyingDictionary"
+ "Device will not use nonce slots"
+ "Device will use nonce slots"
+ "AMFDRGetSealingMap"
+ "AMFDRSealingMapCopyLocalMinimalManifestForInstance"
+ "AMFDRCopyClientId"
+ "AMFDRCopyDeviceKeys"
+ "AMFDRSealedDataCreateSealingRequest"
+ "Failed to read build identity."
+ "AMFDRGetCert"
+ "AMFDRSealingMapVerifyAndCommitSealedData"
+ "AMFDRDataExport"
+ "AMFDRPerformManifestCheck"
+ "AMFDRDataMultiCopy"
+ "failed to load %!s(MISSING): %!s(MISSING)\n"
+ "AMFDRSealingMapCopyInstanceWithIdentifiers"
+ "AMFDRDataIterate"
+ "AMFDRDataCopy"
+ "AMFDRGetInfo"
+ "AMFDRGetOptions"
+ "AMFDRSealingMapCreateRecoveryPermissions"
+ "AMFDRCreatePermissionsString"
- "libauthinstall_device-1033.40.1"

```
