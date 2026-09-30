## CoreRepairCore

> `/System/Library/PrivateFrameworks/CoreRepairCore.framework/CoreRepairCore`

```diff

-645.40.4.0.0
-  __TEXT.__text: 0x696d8
-  __TEXT.__auth_stubs: 0x1550
-  __TEXT.__objc_methlist: 0x2dc0
-  __TEXT.__const: 0x928
-  __TEXT.__cstring: 0x4407
-  __TEXT.__oslogstring: 0x7a4a
+645.40.12.0.0
+  __TEXT.__text: 0x6ea50
+  __TEXT.__auth_stubs: 0x15c0
+  __TEXT.__objc_methlist: 0x2e70
+  __TEXT.__const: 0x958
+  __TEXT.__cstring: 0x4678
+  __TEXT.__oslogstring: 0x80cb
   __TEXT.__gcc_except_tab: 0x1428
-  __TEXT.__unwind_info: 0xd78
+  __TEXT.__unwind_info: 0xdb8
   __TEXT.__objc_classname: 0x781
-  __TEXT.__objc_methname: 0x695d
-  __TEXT.__objc_methtype: 0x1196
-  __TEXT.__objc_stubs: 0x5200
-  __DATA_CONST.__got: 0x3b8
+  __TEXT.__objc_methname: 0x6af5
+  __TEXT.__objc_methtype: 0x11c4
+  __TEXT.__objc_stubs: 0x53e0
+  __DATA_CONST.__got: 0x3e8
   __DATA_CONST.__const: 0x738
   __DATA_CONST.__objc_classlist: 0x290
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x19c0
+  __DATA_CONST.__objc_selrefs: 0x1a38
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x1b8
-  __DATA_CONST.__objc_arraydata: 0x5c0
-  __AUTH_CONST.__auth_got: 0xab8
+  __DATA_CONST.__objc_arraydata: 0x738
+  __AUTH_CONST.__auth_got: 0xaf0
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__const: 0x400
-  __AUTH_CONST.__cfstring: 0x55a0
-  __AUTH_CONST.__objc_const: 0x5558
-  __AUTH_CONST.__objc_intobj: 0x210
-  __AUTH_CONST.__objc_arrayobj: 0x3d8
-  __AUTH_CONST.__objc_dictobj: 0xf0
+  __AUTH_CONST.__const: 0x440
+  __AUTH_CONST.__cfstring: 0x59a0
+  __AUTH_CONST.__objc_const: 0x5598
+  __AUTH_CONST.__objc_intobj: 0x228
+  __AUTH_CONST.__objc_arrayobj: 0x4b0
+  __AUTH_CONST.__objc_dictobj: 0x168
   __AUTH.__objc_data: 0x1400
   __DATA.__objc_ivar: 0x284
-  __DATA.__data: 0x678
+  __DATA.__data: 0x690
   __DATA.__common: 0x18
-  __DATA.__bss: 0x88
+  __DATA.__bss: 0x98
   __DATA_DIRTY.__objc_data: 0x5a0
   __DATA_DIRTY.__bss: 0xb8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/updaters/libSavageRestoreInfo_iOS.dylib
   - /usr/lib/updaters/libSavageUpdater_iOS.dylib
   - /usr/lib/updaters/libT200Updater.dylib
-  Functions: 1776
-  Symbols:   504
-  CStrings:  3191
+  Functions: 1849
+  Symbols:   517
+  CStrings:  3303
 
Symbols:
+ _kBrunorTagResponseTicket
+ _kSavagePostFDRSealingOption
+ _kYonkersOptions
+ _AMFDRSealingMapCopyMinimalManifestClassesAndInstances
+ _kSavageRestoreSystemPartition
+ _AMFDRSealingManifestCopyMinimalManifestClassesAndInstances
+ _IOServiceNameMatching
+ _AMFDRSealingMapCopyDataClassesWithAttribute
+ _SavageUpdaterGetTagsWithLogging
+ _AMFDRDataCreateSikInstanceString
+ _kYonkersSkipOption
+ _MGIsDeviceOfType
+ _kSavageOptionOptions
CStrings:
+ "hasSuffix:"
+ "updaterOptions"
+ "verifyPSD3"
+ "Get Brunor ticket failed"
+ "Get Yonkers ticket failed"
+ "getBrunorTicketForBrunorFWUpdateWithOptions:BrunorTicket:auth:error:"
+ "NBCl"
+ "x-fdr-add-manifest-props"
+ "Classes is not an array"
+ "SavageAuthResponse"
+ "Failed to verify psd3, pearlStatus: %!d(MISSING)"
+ "MidEnclosure"
+ "BM05"
+ "Failed to decode sealing map: %!@(MISSING)"
+ "MainMicrophone"
+ "verifyFDRData %!p(MISSING) %!z(MISSING)u\n"
+ "challenge: %!@(MISSING)"
+ "SavageRestoreInfo"
+ "Failed to set minimal sealing meta"
+ "setByAddingObject:"
+ "Get customAMAuthInstallRef failed"
+ "Decode KBB sealing manifest failed: %!@(MISSING)"
+ "minimal-manifest"
+ "Update streaming DAT file failed"
+ "Current MinimalManifests: %!@(MISSING), %!@(MISSING), %!@(MISSING)"
+ "updaterOptions missing"
+ "IPHONE MCTUB"
+ "prpc"
+ "SavageUpdater failed with error: %!@(MISSING)"
+ "psd3"
+ "PersonalizedFirmwareRootPath"
+ "Unable to create multiSealingMetadata"
+ "Failed to get local psd3, error: %!@(MISSING)"
+ "Creating Savage Updater"
+ "_getDataClassesFromSealingManifest"
+ "Get ticket failed"
+ "LCfg"
+ "mpub"
+ "Updating Yonkers ..."
+ "x-fdr-manifest-prop-mpub-key"
+ "Brunor ticket not found in response"
+ "supportHarvestPearl"
+ "AMFDRSealingManifestCopyMinimalManifestClassesAndInstances failed: %!@(MISSING)"
+ "setBrunorMinimalSealingMeta:instances:"
+ "auth"
+ "perform next stage: %!@(MISSING)"
+ "IPHONE COMP RCAM"
+ "-[CRComponentSigning prpcSign:outSignature:outDeviceNonce:outError:]"
+ "0x5065"
+ "AMFDRSealingMapCopyMinimalManifestClassesAndInstances failed: %!@(MISSING)"
+ "service is NULL"
+ "hasPrefix:"
+ "Final options: %!@(MISSING)"
+ "brunorFirmware"
+ "ForceEnclosureStatus"
+ "matchingDict is NULL"
+ "SavageUpdater work done. LoopCounter = %!d(MISSING)."
+ "powerCycleSensor failed with error: %!@(MISSING)"
+ "No %!@(MISSING) property found"
+ "IPHONE COMP ENCL"
+ "Brunor,Ticket"
+ "Create customObj failed"
+ "N"
+ "B32@0:8^{__AMFDR=}16@24"
+ "KBB MinimalManifests: %!@(MISSING), %!@(MISSING), %!@(MISSING)"
+ "updateBrunorDATFirmware"
+ "4"
+ "innerHeaderKey failed to create"
+ "Copying Firmware ..."
+ "Get osBootHash failed"
+ "updateBrunorDATFirmwareWithReply:"
+ "dataLength > 0"
+ "B44@0:8@16^@24B32^@36"
+ "Unable to create metaDataDict"
+ "_getDataClassesFromSealingMap"
+ "deviceInfoDict: %!@(MISSING)"
+ "property %!@(MISSING) found: %!@(MISSING)"
+ "sikStr is NULL"
+ "BarometerLiveSerialNumber"
+ "Create updaterOptions failed"
+ "Verify psd3 successfully"
+ "supportMctubMinus"
+ "MultiSealingMetadata"
+ "Create optionsDict failed"
+ "AuthChallengeOption"
+ "verifyFDRData -> %!d(MISSING)\n"
+ "updaterOptions: %!@(MISSING) updaterLoopCount: %!d(MISSING)"
+ "signature is NULL"
+ "Error get updater tags: %!@(MISSING)"
+ "SavageUpdaterExecCommand failed: %!@(MISSING)"
+ "prpcSign:outSignature:outDeviceNonce:outError:"
+ "instance full string: %!@(MISSING)"
+ "Get prebootPath failed"
+ "BarometerFactorySerialNumber"
+ "fullStr is NULL"
+ "MultiSealingMetadata: %!@(MISSING)"
+ "auth missing"
+ "%!@(MISSING):%!@(MISSING)"
+ "/private/var/tmp/usr/standalone/firmware/Savage/"
+ "Verify PSD3 failed"
+ "SavageAuthSalt"
+ "Updating Brunor ..."
+ "Create optionsYonkersDict failed"
+ "challenge is NULL"
+ "supportCameraDepth"
+ "Failed to create SavageUpdater: %!@(MISSING)"
+ "verifyPSD3WithReply:"
+ "KBB sealing manifest not found"
+ "options Empty"

```
