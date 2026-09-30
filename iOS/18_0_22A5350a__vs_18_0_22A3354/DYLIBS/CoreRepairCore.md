## CoreRepairCore

> `/System/Library/PrivateFrameworks/CoreRepairCore.framework/CoreRepairCore`

```diff

 625.2.2.0.0
-  __TEXT.__text: 0x693fc
-  __TEXT.__auth_stubs: 0x1540
-  __TEXT.__objc_methlist: 0x2dd0
-  __TEXT.__const: 0x928
-  __TEXT.__cstring: 0x438a
-  __TEXT.__oslogstring: 0x7a0f
-  __TEXT.__gcc_except_tab: 0x1428
-  __TEXT.__unwind_info: 0xd70
+  __TEXT.__text: 0x71600
+  __TEXT.__auth_stubs: 0x15b0
+  __TEXT.__objc_methlist: 0x2f20
+  __TEXT.__const: 0x978
+  __TEXT.__cstring: 0x473d
+  __TEXT.__oslogstring: 0x8354
+  __TEXT.__gcc_except_tab: 0x148c
+  __TEXT.__unwind_info: 0xde0
   __TEXT.__objc_classname: 0x781
-  __TEXT.__objc_methname: 0x6975
-  __TEXT.__objc_methtype: 0x1196
-  __TEXT.__objc_stubs: 0x5220
-  __DATA_CONST.__got: 0x3b0
+  __TEXT.__objc_methname: 0x6c92
+  __TEXT.__objc_methtype: 0x1239
+  __TEXT.__objc_stubs: 0x55e0
+  __DATA_CONST.__got: 0x3e0
   __DATA_CONST.__const: 0x738
   __DATA_CONST.__objc_classlist: 0x290
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x19c8
+  __DATA_CONST.__objc_selrefs: 0x1aa8
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x1b8
-  __DATA_CONST.__objc_arraydata: 0x5a8
-  __AUTH_CONST.__auth_got: 0xab0
+  __DATA_CONST.__objc_arraydata: 0x748
+  __AUTH_CONST.__auth_got: 0xae8
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__const: 0x400
-  __AUTH_CONST.__cfstring: 0x5500
-  __AUTH_CONST.__objc_const: 0x5558
-  __AUTH_CONST.__objc_intobj: 0x210
-  __AUTH_CONST.__objc_arrayobj: 0x3c0
-  __AUTH_CONST.__objc_dictobj: 0xf0
+  __AUTH_CONST.__const: 0x440
+  __AUTH_CONST.__cfstring: 0x5b40
+  __AUTH_CONST.__objc_const: 0x5680
+  __AUTH_CONST.__objc_intobj: 0x228
+  __AUTH_CONST.__objc_arrayobj: 0x4e0
+  __AUTH_CONST.__objc_dictobj: 0x190
   __AUTH.__objc_data: 0x1400
-  __DATA.__objc_ivar: 0x284
-  __DATA.__data: 0x678
+  __DATA.__objc_ivar: 0x28c
+  __DATA.__data: 0x690
   __DATA.__common: 0x18
   __DATA.__bss: 0x88
   __DATA_DIRTY.__objc_data: 0x5a0

   - /usr/lib/updaters/libSavageRestoreInfo_iOS.dylib
   - /usr/lib/updaters/libSavageUpdater_iOS.dylib
   - /usr/lib/updaters/libT200Updater.dylib
-  Functions: 1775
-  Symbols:   502
-  CStrings:  3184
+  Functions: 1873
+  Symbols:   516
+  CStrings:  3357
 
Symbols:
+ _IOServiceNameMatching
+ _reboot3
+ _kYonkersSkipOption
+ _MGIsDeviceOfType
+ _AMFDRDataCreateSikInstanceString
+ _kSavageOptionOptions
+ _kSavagePostFDRSealingOption
+ _kYonkersOptions
+ _AMFDRSealingMapCopyMinimalManifestClassesAndInstances
+ _AMFDRSealingManifestCopyMinimalManifestClassesAndInstances
+ _CRIsSelfRepairedComponent
+ _kBrunorTagResponseTicket
+ _SavageUpdaterGetTagsWithLogging
+ _kSavageRestoreSystemPartition
CStrings:
+ "allowUsedPart"
+ "key: %!@(MISSING), spc: %!@(MISSING), sd: %!@(MISSING)"
+ "No %!@(MISSING) property found"
+ "Not allow used part %!@(MISSING) (%!@(MISSING)): %!@(MISSING)"
+ "0x5065"
+ "updateBrunorDATFirmware"
+ "MultiSealingMetadata"
+ "Brunor,Ticket"
+ "isSelfRepairedComponent:"
+ "setAllowSelfService:"
+ "checkUsedStatusFor:withHistory:withClaimCount:"
+ "setBootIntentAndRebootToCheckerboardWithLocale:reply:"
+ "IPHONE MCTUB"
+ "AMFDRSealingManifestCopyMinimalManifestClassesAndInstances failed: %!@(MISSING)"
+ "getRepairTicket:"
+ "_allowUsedPart"
+ "Add encrypted WiFi credentials and locale"
+ "updaterOptions missing"
+ "isSelfServiceSalesDistrict:"
+ "deviceSupportsRepairBootIntent"
+ "TB,N,V_allowUsedPart"
+ "%!@(MISSING) has usedCount"
+ "Clear %!@(MISSING) failed:%!@(MISSING)"
+ "deviceInfoDict: %!@(MISSING)"
+ "TB,N,V_allowSelfService"
+ "%!@(MISSING):%!@(MISSING)"
+ "Get Yonkers ticket failed"
+ "MidEnclosure"
+ "clearBootIntent:"
+ "Verify PSD3 failed"
+ "/private/var/tmp/usr/standalone/firmware/Savage/"
+ "Get osBootHash failed"
+ "Get prebootPath failed"
+ "challenge is NULL"
+ "component failed preflight proceeding"
+ "verifyFDRData -> %!d(MISSING)\n"
+ "allowUsedPart validation failed."
+ "SSR boot intent not found"
+ "Unexpected SSR boot intent format"
+ "Failed to read live sensor number, error: %!@(MISSING)"
+ "v24@0:8@?<v@?B@\"NSData\"@\"NSError\">16"
+ "N"
+ "Brunor ticket not found in response"
+ "Failed to deserialize data for boot intent dictionary, error %!@(MISSING)"
+ "SavageUpdater failed with error: %!@(MISSING)"
+ "Skip checking for SSR"
+ "AuthChallengeOption"
+ "KBB MinimalManifests: %!@(MISSING), %!@(MISSING), %!@(MISSING)"
+ "BM05"
+ "repairDate:%!@(MISSING) in the past:%!@(MISSING)"
+ "x-fdr-manifest-prop-mpub-key"
+ "not supported in this mode or device"
+ "AMFDRSealingMapCopyMinimalManifestClassesAndInstances failed: %!@(MISSING)"
+ "Failed to create SavageUpdater: %!@(MISSING)"
+ "SavageAuthSalt"
+ "readNVRAMValueForKey value: %!@(MISSING)"
+ "Cannot serialize boot intent dictionary, abort"
+ "prpcSign:outSignature:outDeviceNonce:outError:"
+ "diagnostic-boot-intent"
+ "Verify psd3 successfully"
+ "readNVRAMValueForKey %!@(MISSING) failed: %!@(MISSING)"
+ "minimal-manifest"
+ "SavageRestoreInfo"
+ "Updating Yonkers ..."
+ "SavageUpdaterExecCommand failed: %!@(MISSING)"
+ "Error get updater tags: %!@(MISSING)"
+ "_allowSelfService"
+ "Decode KBB sealing manifest failed: %!@(MISSING)"
+ "Unable to create metaDataDict"
+ "Unexpected SSR boot intent purpose format"
+ "auth missing"
+ "Create updaterOptions failed"
+ "verifyPSD3WithReply:"
+ "LCfg"
+ "brunorFirmware"
+ "B32@0:8^{__AMFDR=}16@24"
+ "psd3"
+ "setBrunorMinimalSealingMeta:instances:"
+ "Current MinimalManifests: %!@(MISSING), %!@(MISSING), %!@(MISSING)"
+ "getUseCountExceptionsWith:"
+ "property %!@(MISSING) found: %!@(MISSING)"
+ "BarometerFactorySerialNumber"
+ "JSON serialization got an error: %!@(MISSING)"
+ "cachedPreFlightResults"
+ "options Empty"
+ "purpose"
+ "supportCameraDepth"
+ "Create customObj failed"
+ "Update streaming DAT file failed"
+ "Set %!@(MISSING) failed with error %!@(MISSING)"
+ "-[CRComponentSigning prpcSign:outSignature:outDeviceNonce:outError:]"
+ "Failed to get local psd3, error: %!@(MISSING)"
+ "allowSelfService"
+ "fullStr is NULL"
+ "B44@0:8@16^@24B32^@36"
+ "instance full string: %!@(MISSING)"
+ "x-fdr-add-manifest-props"
+ "service is NULL"
+ "SSR999"
+ "powerCycleSensor failed with error: %!@(MISSING)"
+ "getBrunorTicketForBrunorFWUpdateWithOptions:BrunorTicket:auth:error:"
+ "verifyPSD3"
+ "Get ticket failed"
+ "Creating Savage Updater"
+ "MainMicrophone"
+ "v32@0:8@\"NSString\"16@?<v@?B@\"NSError\">24"
+ "MultiSealingMetadata: %!@(MISSING)"
+ "Create optionsDict failed"
+ "updateBrunorDATFirmwareWithReply:"
+ "SavageAuthResponse"
+ "Unable to create multiSealingMetadata"
+ "auth"
+ "mpub"
+ "B20@0:8i16"
+ "supportMSRk"
+ "yyyy-MM-dd"
+ "perform next stage: %!@(MISSING)"
+ "KBB sealing manifest not found"
+ "IPHONE COMP ENCL"
+ "hasSuffix:"
+ "prpc"
+ "Failed to set minimal sealing meta"
+ "BarometerLiveSerialNumber"
+ "setAllowUsedPart:"
+ "Updating Brunor ..."
+ "PersonalizedFirmwareRootPath"
+ "Copying Firmware ..."
+ "Failed to get component for %!d(MISSING)"
+ "getSsrBootIntentWithError:"
+ "matchingDict is NULL"
+ "verifyFDRData %!p(MISSING) %!z(MISSING)u\n"
+ "mesa unsealed"
+ "IPHONE COMP RCAM"
+ "signature is NULL"
+ "dataLength > 0"
+ "checkerboard"
+ "Create optionsYonkersDict failed"
+ "Final options: %!@(MISSING)"
+ "innerHeaderKey failed to create"
+ "Failed to verify psd3, pearlStatus: %!d(MISSING)"
+ "supportHarvestPearl"
+ "MesaSensorIDSensorSN"
+ "challenge: %!@(MISSING)"
+ "SS04"
+ "2024-09-16"
+ "wifi-credentials"
+ "MSRk"
+ "v24@0:8@?<v@?B@\"NSError\">16"
+ "isEqualToSet:"
+ "missing mesa SN"
+ "updaterOptions"
+ "Not allow self repaired %!@(MISSING) (%!@(MISSING)): %!@(MISSING)"
+ "supportMctubMinus"
+ "one-time-boot-command"
+ "sikStr is NULL"
+ "NBCl"
+ "key: %!@(MISSING), spc: %!@(MISSING), cc: %!@(MISSING)"
+ "updaterOptions: %!@(MISSING) updaterLoopCount: %!d(MISSING)"
+ "4"
+ "SavageUpdater work done. LoopCounter = %!d(MISSING)."
+ "_getClaimCountEnforceDate"
+ "Get Brunor ticket failed"
+ "ForceEnclosureStatus"
+ "allowSelfService validation failed."
+ "Set boot intent and reboot to Checkerboard"
+ "Reboot failed with error:%!d(MISSING)"
+ "self-service-repair"
+ "Failed to get boot intent purpose"
+ "Get customAMAuthInstallRef failed"
+ "hasPrefix:"

```
