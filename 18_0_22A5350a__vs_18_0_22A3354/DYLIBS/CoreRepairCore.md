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
+ _AMFDRSealingManifestCopyMinimalManifestClassesAndInstances
+ _kYonkersSkipOption
+ _CRIsSelfRepairedComponent
+ _AMFDRSealingMapCopyMinimalManifestClassesAndInstances
+ _kBrunorTagResponseTicket
+ _kYonkersOptions
+ _MGIsDeviceOfType
+ _reboot3
+ _SavageUpdaterGetTagsWithLogging
+ _IOServiceNameMatching
+ _kSavageOptionOptions
+ _kSavageRestoreSystemPartition
+ _AMFDRDataCreateSikInstanceString
+ _kSavagePostFDRSealingOption
CStrings:
+ "updaterOptions"
+ "minimal-manifest"
+ "IPHONE MCTUB"
+ "NBCl"
+ "AMFDRSealingMapCopyMinimalManifestClassesAndInstances failed: %!@(MISSING)"
+ "setBootIntentAndRebootToCheckerboardWithLocale:reply:"
+ "Get prebootPath failed"
+ "Update streaming DAT file failed"
+ "Failed to get boot intent purpose"
+ "cachedPreFlightResults"
+ "options Empty"
+ "Get customAMAuthInstallRef failed"
+ "Copying Firmware ..."
+ "setAllowSelfService:"
+ "verifyPSD3WithReply:"
+ "updateBrunorDATFirmware"
+ "ForceEnclosureStatus"
+ "yyyy-MM-dd"
+ "checkerboard"
+ "4"
+ "B44@0:8@16^@24B32^@36"
+ "one-time-boot-command"
+ "service is NULL"
+ "B20@0:8i16"
+ "v24@0:8@?<v@?B@\"NSData\"@\"NSError\">16"
+ "SSR999"
+ "challenge is NULL"
+ "setAllowUsedPart:"
+ "Not allow used part %!@(MISSING) (%!@(MISSING)): %!@(MISSING)"
+ "Create optionsDict failed"
+ "purpose"
+ "Clear %!@(MISSING) failed:%!@(MISSING)"
+ "SavageUpdaterExecCommand failed: %!@(MISSING)"
+ "_allowSelfService"
+ "MainMicrophone"
+ "Failed to set minimal sealing meta"
+ "SavageUpdater failed with error: %!@(MISSING)"
+ "updateBrunorDATFirmwareWithReply:"
+ "perform next stage: %!@(MISSING)"
+ "_allowUsedPart"
+ "x-fdr-manifest-prop-mpub-key"
+ "Failed to deserialize data for boot intent dictionary, error %!@(MISSING)"
+ "Failed to get component for %!d(MISSING)"
+ "updaterOptions: %!@(MISSING) updaterLoopCount: %!d(MISSING)"
+ "Skip checking for SSR"
+ "getRepairTicket:"
+ "Decode KBB sealing manifest failed: %!@(MISSING)"
+ "v32@0:8@\"NSString\"16@?<v@?B@\"NSError\">24"
+ "/private/var/tmp/usr/standalone/firmware/Savage/"
+ "prpcSign:outSignature:outDeviceNonce:outError:"
+ "deviceInfoDict: %!@(MISSING)"
+ "MesaSensorIDSensorSN"
+ "Error get updater tags: %!@(MISSING)"
+ "supportCameraDepth"
+ "Create customObj failed"
+ "AuthChallengeOption"
+ "readNVRAMValueForKey value: %!@(MISSING)"
+ "BarometerFactorySerialNumber"
+ "Failed to get local psd3, error: %!@(MISSING)"
+ "Reboot failed with error:%!d(MISSING)"
+ "Creating Savage Updater"
+ "auth"
+ "MSRk"
+ "Updating Yonkers ..."
+ "getSsrBootIntentWithError:"
+ "updaterOptions missing"
+ "allowSelfService validation failed."
+ "KBB MinimalManifests: %!@(MISSING), %!@(MISSING), %!@(MISSING)"
+ "SavageAuthResponse"
+ "self-service-repair"
+ "Brunor ticket not found in response"
+ "missing mesa SN"
+ "N"
+ "property %!@(MISSING) found: %!@(MISSING)"
+ "MultiSealingMetadata: %!@(MISSING)"
+ "SavageUpdater work done. LoopCounter = %!d(MISSING)."
+ "Unexpected SSR boot intent purpose format"
+ "allowUsedPart validation failed."
+ "clearBootIntent:"
+ "diagnostic-boot-intent"
+ "allowUsedPart"
+ "isSelfRepairedComponent:"
+ "IPHONE COMP ENCL"
+ "IPHONE COMP RCAM"
+ "sikStr is NULL"
+ "LCfg"
+ "verifyPSD3"
+ "TB,N,V_allowSelfService"
+ "challenge: %!@(MISSING)"
+ "SavageRestoreInfo"
+ "No %!@(MISSING) property found"
+ "Failed to create SavageUpdater: %!@(MISSING)"
+ "hasSuffix:"
+ "innerHeaderKey failed to create"
+ "verifyFDRData %!p(MISSING) %!z(MISSING)u\n"
+ "SavageAuthSalt"
+ "setBrunorMinimalSealingMeta:instances:"
+ "0x5065"
+ "AMFDRSealingManifestCopyMinimalManifestClassesAndInstances failed: %!@(MISSING)"
+ "psd3"
+ "checkUsedStatusFor:withHistory:withClaimCount:"
+ "MultiSealingMetadata"
+ "JSON serialization got an error: %!@(MISSING)"
+ "Failed to verify psd3, pearlStatus: %!d(MISSING)"
+ "2024-09-16"
+ "mesa unsealed"
+ "key: %!@(MISSING), spc: %!@(MISSING), cc: %!@(MISSING)"
+ "%!@(MISSING):%!@(MISSING)"
+ "mpub"
+ "Create updaterOptions failed"
+ "BM05"
+ "getBrunorTicketForBrunorFWUpdateWithOptions:BrunorTicket:auth:error:"
+ "isSelfServiceSalesDistrict:"
+ "_getClaimCountEnforceDate"
+ "KBB sealing manifest not found"
+ "Verify PSD3 failed"
+ "v24@0:8@?<v@?B@\"NSError\">16"
+ "Final options: %!@(MISSING)"
+ "PersonalizedFirmwareRootPath"
+ "getUseCountExceptionsWith:"
+ "Unexpected SSR boot intent format"
+ "x-fdr-add-manifest-props"
+ "brunorFirmware"
+ "BarometerLiveSerialNumber"
+ "SSR boot intent not found"
+ "signature is NULL"
+ "MidEnclosure"
+ "allowSelfService"
+ "Get ticket failed"
+ "Set boot intent and reboot to Checkerboard"
+ "Set %!@(MISSING) failed with error %!@(MISSING)"
+ "auth missing"
+ "%!@(MISSING) has usedCount"
+ "SS04"
+ "Unable to create metaDataDict"
+ "Updating Brunor ..."
+ "fullStr is NULL"
+ "supportHarvestPearl"
+ "isEqualToSet:"
+ "Create optionsYonkersDict failed"
+ "Unable to create multiSealingMetadata"
+ "Brunor,Ticket"
+ "-[CRComponentSigning prpcSign:outSignature:outDeviceNonce:outError:]"
+ "Get Yonkers ticket failed"
+ "matchingDict is NULL"
+ "Add encrypted WiFi credentials and locale"
+ "TB,N,V_allowUsedPart"
+ "Failed to read live sensor number, error: %!@(MISSING)"
+ "Not allow self repaired %!@(MISSING) (%!@(MISSING)): %!@(MISSING)"
+ "Verify psd3 successfully"
+ "deviceSupportsRepairBootIntent"
+ "component failed preflight proceeding"
+ "Current MinimalManifests: %!@(MISSING), %!@(MISSING), %!@(MISSING)"
+ "not supported in this mode or device"
+ "Get Brunor ticket failed"
+ "supportMctubMinus"
+ "hasPrefix:"
+ "B32@0:8^{__AMFDR=}16@24"
+ "dataLength > 0"
+ "prpc"
+ "readNVRAMValueForKey %!@(MISSING) failed: %!@(MISSING)"
+ "supportMSRk"
+ "Cannot serialize boot intent dictionary, abort"
+ "instance full string: %!@(MISSING)"
+ "wifi-credentials"
+ "verifyFDRData -> %!d(MISSING)\n"
+ "powerCycleSensor failed with error: %!@(MISSING)"
+ "key: %!@(MISSING), spc: %!@(MISSING), sd: %!@(MISSING)"
+ "Get osBootHash failed"
+ "repairDate:%!@(MISSING) in the past:%!@(MISSING)"

```
