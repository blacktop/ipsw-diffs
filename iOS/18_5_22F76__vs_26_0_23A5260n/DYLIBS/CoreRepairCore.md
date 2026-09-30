## CoreRepairCore

> `/System/Library/PrivateFrameworks/CoreRepairCore.framework/CoreRepairCore`

```diff

-696.120.5.0.0
-  __TEXT.__text: 0x78df4
-  __TEXT.__auth_stubs: 0x15f0
-  __TEXT.__objc_methlist: 0x340c
-  __TEXT.__const: 0x9c8
-  __TEXT.__oslogstring: 0x877a
-  __TEXT.__cstring: 0x4e24
-  __TEXT.__gcc_except_tab: 0x15c4
-  __TEXT.__unwind_info: 0xfb8
-  __TEXT.__objc_classname: 0x7dd
-  __TEXT.__objc_methname: 0x71c3
-  __TEXT.__objc_methtype: 0x12a3
-  __TEXT.__objc_stubs: 0x59c0
-  __DATA_CONST.__got: 0x3c0
-  __DATA_CONST.__const: 0x7b0
-  __DATA_CONST.__objc_classlist: 0x2b8
+921.0.34.0.0
+  __TEXT.__text: 0x7f538
+  __TEXT.__auth_stubs: 0x1670
+  __TEXT.__objc_methlist: 0x38a4
+  __TEXT.__const: 0x7f0
+  __TEXT.__oslogstring: 0x8aeb
+  __TEXT.__cstring: 0x54f5
+  __TEXT.__gcc_except_tab: 0x14c8
+  __TEXT.__unwind_info: 0x1100
+  __TEXT.__objc_classname: 0x7c8
+  __TEXT.__objc_methname: 0x7bde
+  __TEXT.__objc_methtype: 0x14a7
+  __TEXT.__objc_stubs: 0x60e0
+  __DATA_CONST.__got: 0x550
+  __DATA_CONST.__const: 0x870
+  __DATA_CONST.__objc_classlist: 0x2b0
   __DATA_CONST.__objc_catlist: 0x20
-  __DATA_CONST.__objc_protolist: 0x60
+  __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1c78
-  __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0x1d0
-  __DATA_CONST.__objc_arraydata: 0x740
-  __AUTH_CONST.__auth_got: 0xb08
-  __AUTH_CONST.__const: 0x440
-  __AUTH_CONST.__cfstring: 0x6200
-  __AUTH_CONST.__objc_const: 0x5568
-  __AUTH_CONST.__objc_intobj: 0x258
+  __DATA_CONST.__objc_selrefs: 0x1ed0
+  __DATA_CONST.__objc_protorefs: 0x28
+  __DATA_CONST.__objc_superrefs: 0x1e8
+  __DATA_CONST.__objc_arraydata: 0x890
+  __AUTH_CONST.__auth_got: 0xb48
+  __AUTH_CONST.__const: 0x480
+  __AUTH_CONST.__cfstring: 0x6a00
+  __AUTH_CONST.__objc_const: 0x5788
   __AUTH_CONST.__objc_arrayobj: 0x588
-  __AUTH_CONST.__objc_dictobj: 0x190
-  __AUTH.__objc_data: 0x1040
-  __DATA.__objc_ivar: 0x2a4
+  __AUTH_CONST.__objc_intobj: 0x288
+  __AUTH_CONST.__objc_dictobj: 0x168
+  __AUTH.__objc_data: 0xeb0
+  __DATA.__objc_ivar: 0x2e0
   __DATA.__data: 0x690
-  __DATA.__common: 0x18
-  __DATA.__bss: 0x78
-  __DATA_DIRTY.__objc_data: 0xaf0
-  __DATA_DIRTY.__bss: 0xe8
+  __DATA.__bss: 0xb0
+  __DATA.__common: 0x30
+  __DATA_DIRTY.__objc_data: 0xc30
+  __DATA_DIRTY.__bss: 0x100
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/updaters/libSavageRestoreInfo_iOS.dylib
   - /usr/lib/updaters/libSavageUpdater_iOS.dylib
   - /usr/lib/updaters/libT200Updater.dylib
-  UUID: 5224E099-9DA4-38DE-9476-841FD0E72CAD
-  Functions: 2060
-  Symbols:   542
-  CStrings:  4285
+  UUID: 05772402-23D0-36D3-BE57-07F1C5998411
+  Functions: 2203
+  Symbols:   7295
+  CStrings:  4561
 
Symbols:
+ +[CRAttestationHelper sharedInstance]
+ +[CRAttestationHelper sharedInstance].cold.1
+ +[CRBatteryController setBatteryDateOfFirstUse:error:]
+ +[CRBootIntentController clearBootIntentWithError:]
+ +[CRBootIntentController clearBootIntentWithError:].cold.1
+ +[CRBootIntentController clearBootIntentWithError:].cold.2
+ +[CRBootIntentController getSsrBootIntentWithError:]
+ +[CRBootIntentController getSsrBootIntentWithError:].cold.1
+ +[CRBootIntentController getSsrBootIntentWithError:].cold.2
+ +[CRBootIntentController getSsrBootIntentWithError:].cold.3
+ +[CRBootIntentController getSsrBootIntentWithError:].cold.4
+ +[CRBootIntentController getSsrBootIntentWithError:].cold.5
+ +[CRBootIntentController getSsrBootIntentWithError:].cold.6
+ +[CRBootIntentController setBootIntentWithLocale:error:]
+ +[CRBootIntentController setBootIntentWithLocale:error:].cold.1
+ +[CRBootIntentController setBootIntentWithLocale:error:].cold.2
+ +[CRBootIntentController setBootIntentWithLocale:error:].cold.3
+ +[CRBootIntentController setBootIntentWithLocale:error:].cold.4
+ +[CRChallengeObject supportsSecureCoding]
+ +[CRChallengeResponse supportsSecureCoding]
+ +[CRComponentBase sharedSingleton]
+ +[CRComponentBatteryRoswell sharedSingleton]
+ +[CRComponentDisplayRoswell sharedSingleton]
+ +[CRComponentPearl sharedSingleton]
+ +[CRComponentTsid sharedSingleton]
+ +[CRComponentVeridian sharedSingleton]
+ +[CRDaemonController controlWithParameters:withReply:]
+ +[CRDaemonController controlWithParametersImpl:withReply:]
+ +[CRDaemonController controlWithParametersImpl:withReply:].cold.1
+ +[CRDaemonController controlWithParametersImpl:withReply:].cold.2
+ +[CRDaemonController controlWithParametersImpl:withReply:].cold.3
+ +[CRDaemonController controlWithParametersImpl:withReply:].cold.4
+ +[CRDaemonController controlWithParametersImpl:withReply:].cold.5
+ +[CRDaemonController controlWithParametersImpl:withReply:].cold.6
+ +[CRDaemonController controlWithParametersImpl:withReply:].cold.7
+ +[CRDaemonController doLaunchControl:action:]
+ +[CRDaemonController doLaunchControl:action:].cold.1
+ +[CRDaemonController doLaunchControl:action:].cold.2
+ +[CRDaemonController getAllowedListFromEntitlements:]
+ +[CRDaemonController getLibXPCInternalWithSymbol:]
+ +[CRDaemonController getLibXPCInternalWithSymbol:].cold.1
+ +[CRDaemonController getLibXPCInternalWithSymbol:].cold.2
+ +[CRDaemonController getLibXPCInternalWithSymbol:].cold.3
+ +[CRDaemonController safeGetStringParam:key:]
+ +[CRDeviceMap currentDevice]
+ +[CRDeviceMap currentDevice].cold.1
+ +[CRDeviceMap getComponentName:]
+ +[CRDeviceMap getComponentNameWithSPC:]
+ +[CRDeviceMap getComponentNameWithSPC:].cold.1
+ +[CRDeviceMap getComponentNameWithSPC:].cold.2
+ +[CRDeviceMap getComponentNameWithSPC:].cold.3
+ +[CRDeviceMap getComponentTypeWithSPC:]
+ +[CRDeviceMap getComponentTypeWithSPC:].cold.1
+ +[CRDeviceMap getInternalName:]
+ +[CRDeviceMap getKeysInComponent:]
+ +[CRDeviceMap getLocalizationKey:]
+ +[CRDeviceMap getSPCWithComponent:]
+ +[CRDeviceMap getSupportedComponentTypes]
+ +[CRDeviceMap hasMesa]
+ +[CRDeviceMap isStrongComponent:]
+ +[CRDeviceMap supportElabel]
+ +[CRDeviceMap supportHarvestPearl]
+ +[CRDeviceMap supportLiDAR]
+ +[CRDeviceMap supportPeCoNet]
+ +[CRDeviceMap supportRepair:]
+ +[CRFDRBaseDeviceHandler _getDataClassUsingComponentAuthName:]
+ +[CRFDRBaseDeviceHandler _populateSealingMapForCurrentDevice]
+ +[CRFDRBaseDeviceHandler _populateSealingMapProperties]
+ +[CRFDRBaseDeviceHandler copySealingManifestDataInstanceForComponent:]
+ +[CRFDRBaseDeviceHandler copySealingManifestDataInstanceForComponent:].cold.1
+ +[CRFDRBaseDeviceHandler copySealingManifestDataInstanceForComponent:].cold.2
+ +[CRFDRBaseDeviceHandler getDeviceHandlerForProductType:]
+ +[CRFDRBaseDeviceHandler getPropertyArrayFrom:]
+ +[CRFDRBaseDeviceHandler getPropertyArrayFrom:].cold.1
+ +[CRFDRBaseDeviceHandler getPropertyArrayFrom:].cold.2
+ +[CRFDRBaseDeviceHandler getRegisterChangeDictUsingComponentAuthName:]
+ +[CRFDRBaseDeviceHandler getRegisterChangeDictUsingComponentAuthName:].cold.1
+ +[CRFDRBaseDeviceHandler getSealingMap]
+ +[CRFDRBaseDeviceHandler getUnsealedSPCWithDataClass:]
+ +[CRFDRBaseDeviceHandler initSealingMap]
+ +[CRFDRBaseDeviceHandler isFDRDataClassSupported:]
+ +[CRFDRBaseDeviceHandler isFDRPrimaryDataClass:]
+ +[CRFDRBaseDeviceHandler isFDRPropertySupported:]
+ +[CRFDRCompute1DeviceHandler getDeviceHandlerForProductType:]
+ +[CRFDRCompute1DeviceHandler isCompute1ProductType:]
+ +[CRFDRDeviceController sharedSingleton]
+ +[CRFDRDisplay1DeviceHandler getDeviceHandlerForProductType:]
+ +[CRFDRDisplay1DeviceHandler isDisplay1ProductType:]
+ +[CRFDRGen1DeviceHandler getDeviceHandlerForProductType:]
+ +[CRFDRGen1DeviceHandler isGen1ProductType:]
+ +[CRFDRGen2DeviceHandler getDeviceHandlerForProductType:]
+ +[CRFDRGen2DeviceHandler isGen2ProductType:]
+ +[CRFDRGen3DeviceHandler getDeviceHandlerForProductType:]
+ +[CRFDRGen3DeviceHandler isGen3ProductType:]
+ +[CRFDRGen4DeviceHandler getDeviceHandlerForProductType:]
+ +[CRFDRGen4DeviceHandler isGen4ProductType:]
+ +[CRFDRGen5DeviceHandler getDeviceHandlerForProductType:]
+ +[CRFDRGen5DeviceHandler isGen5ProductType:]
+ +[CRFDRGen6DeviceHandler getDeviceHandlerForProductType:]
+ +[CRFDRGen6DeviceHandler isGen6ProductType:]
+ +[CRFDRGen7DeviceHandler getDeviceHandlerForProductType:]
+ +[CRFDRGen7DeviceHandler isGen7ProductType:]
+ +[CRFDRLegacy2DeviceHandler getDeviceHandlerForProductType:]
+ +[CRFDRLegacy2DeviceHandler isLegacy2ProductType:]
+ +[CRFDRLegacyDeviceHandler getDeviceHandlerForProductType:]
+ +[CRFDRLegacyDeviceHandler isLegacyProductType:]
+ +[CRFDRRetryController sharedInstance]
+ +[CRFDRRetryController sharedInstance].cold.1
+ +[CRFDRSeal currentProcessHasEntitlement:]
+ +[CRFDRSeal currentProcessHasEntitlement:].cold.1
+ +[CRFDRUtils _compareSealedAndLiveDataClasses:instances:liveClasses:liveInstances:results:]
+ +[CRFDRUtils _compareSealedAndLiveDataClasses:instances:liveClasses:liveInstances:results:].cold.1
+ +[CRFDRUtils _compareSerialNumberProperties:missingLiveData:results:]
+ +[CRFDRUtils _compareSerialNumberProperties:missingLiveData:results:].cold.1
+ +[CRFDRUtils _createFDRLocal]
+ +[CRFDRUtils _getAllLiveDataClasses:liveInstances:missingLiveData:mesaState:error:]
+ +[CRFDRUtils _getAllLiveDataClasses:liveInstances:missingLiveData:mesaState:error:].cold.1
+ +[CRFDRUtils _getAllLiveDataClasses:liveInstances:missingLiveData:mesaState:error:].cold.2
+ +[CRFDRUtils _getAllLiveDataClasses:liveInstances:missingLiveData:mesaState:error:].cold.3
+ +[CRFDRUtils _getAllLiveDataClasses:liveInstances:missingLiveData:mesaState:error:].cold.4
+ +[CRFDRUtils _getAllSealedDataAndPropertiesFromManifest:properties:classes:instances:error:]
+ +[CRFDRUtils _getAllSealedDataAndPropertiesFromManifest:properties:classes:instances:error:].cold.1
+ +[CRFDRUtils _getDataClassesFromSealingManifest]
+ +[CRFDRUtils _getDataClassesFromSealingManifest].cold.1
+ +[CRFDRUtils _getDataClassesFromSealingManifest].cold.2
+ +[CRFDRUtils _getDataClassesFromSealingManifest].cold.3
+ +[CRFDRUtils _getDataClassesFromSealingMap]
+ +[CRFDRUtils _getDataClassesFromSealingMap].cold.1
+ +[CRFDRUtils _getDataClassesFromSealingMap].cold.2
+ +[CRFDRUtils _getManifestForDataClass:]
+ +[CRFDRUtils _getManifestForDataClass:].cold.1
+ +[CRFDRUtils _getManifestForDataClass:].cold.2
+ +[CRFDRUtils _getManifestForDataClass:].cold.3
+ +[CRFDRUtils _getMesaState]
+ +[CRFDRUtils _getPropertiesFromSealingMap]
+ +[CRFDRUtils _getPropertyArrayFrom:]
+ +[CRFDRUtils _getPropertyArrayFrom:].cold.1
+ +[CRFDRUtils _getPropertyArrayFrom:].cold.2
+ +[CRFDRUtils _getUnsealedMesaData:mesaState:]
+ +[CRFDRUtils _getUnsealedMesaData:mesaState:].cold.1
+ +[CRFDRUtils _getUnsealedMesaData:mesaState:].cold.2
+ +[CRFDRUtils extractComponentsAndIdentifiers:]
+ +[CRFDRUtils findUnsealedDataWithError:]
+ +[CRFDRUtils findUnsealedDataWithError:].cold.1
+ +[CRFDRUtils findUnsealedDataWithKey:error:]
+ +[CRFDRUtils findUnsealedDataWithKey:error:].cold.1
+ +[CRFDRUtils findUnsealedDataWithKey:error:].cold.2
+ +[CRFDRUtils findUnsealedDataWithKey:error:].cold.3
+ +[CRFDRUtils findUnsealedDataWithKey:error:].cold.4
+ +[CRFDRUtils getData:instance:]
+ +[CRFDRUtils getData:instance:].cold.1
+ +[CRFDRUtils getData:instance:].cold.2
+ +[CRFDRUtils getDataPayload:instance:]
+ +[CRFDRUtils getDataPayload:instance:].cold.1
+ +[CRFDRUtils getDataPayload:instance:].cold.2
+ +[CRFDRUtils getDataPayload:instance:].cold.3
+ +[CRFDRUtils getDataPayloadDictWithClass:instance:]
+ +[CRFDRUtils getDataPayloadDictWithClass:instance:].cold.1
+ +[CRFDRUtils getLocalSealingManifestWithError:]
+ +[CRFDRUtils getLocalSealingManifestWithError:].cold.1
+ +[CRFDRUtils getLocalSealingManifest]
+ +[CRFDRUtils getMacSupportedSPCs]
+ +[CRFDRUtils getStringFromCert:WithTag:AndOID:]
+ +[CRFDRUtils hasMesaUnsealedData]
+ +[CRFDRUtils hasMesaUnsealedData].cold.1
+ +[CRFDRUtils isDataClassSupported:]
+ +[CRFDRUtils isDcSignedCombinedDataClass:error:]
+ +[CRFDRUtils isDcSignedCombinedDataClass:error:].cold.1
+ +[CRFDRUtils isDcSignedDataClass:instance:error:]
+ +[CRFDRUtils isDcSignedDataClass:instance:error:].cold.1
+ +[CRFDRUtils isDcSignedSealingManifest:]
+ +[CRFDRUtils isDcSignedSealingManifest:].cold.1
+ +[CRFDRUtils isPropertySupported:]
+ +[CRFDRUtils isServicePartWithError:]
+ +[CRFDRUtils isServicePartWithError:].cold.1
+ +[CRFDRUtils isServicePartWithError:].cold.2
+ +[CRFDRUtils isServicePartWithError:].cold.3
+ +[CRFDRUtils localManifestProperties]
+ +[CRFDRUtils localManifestProperties].cold.1
+ +[CRFDRUtils localManifestProperties].cold.2
+ +[CRFDRUtils queryDeviceStagedSealedFromEAN:error:]
+ +[CRFDRUtils queryDeviceStagedSealedFromEAN:error:].cold.1
+ +[CRFDRUtils queryDeviceStagedSealedFromEAN:error:].cold.2
+ +[CRFDRUtils queryDeviceStagedSealedFromEAN:error:].cold.3
+ +[CRFDRUtils queryDeviceStagedSealedFromEAN:error:].cold.4
+ +[CRFDRUtils queryDeviceStagedSealedFromEAN:error:].cold.5
+ +[CRFDRUtils queryDeviceStagedSealedFromEAN:error:].cold.6
+ +[CRFDRUtils(ComponentState) isDcSignedComponent:error:]
+ +[CRFDRUtils(ComponentState) isDcSignedComponent:error:].cold.1
+ +[CRFDRUtils(ComponentState) isDcSignedComponent:error:].cold.2
+ +[CRFDRiPad1DeviceHandler getDeviceHandlerForProductType:]
+ +[CRFDRiPad1DeviceHandler getUnsealedSPCWithDataClass:]
+ +[CRFDRiPad1DeviceHandler getUnsealedSPCWithDataClass:].cold.1
+ +[CRFDRiPad1DeviceHandler getUnsealedSPCWithDataClass:].cold.2
+ +[CRFDRiPad1DeviceHandler getUnsealedSPCWithDataClass:].cold.3
+ +[CRFDRiPad1DeviceHandler getUnsealedSPCWithDataClass:].cold.4
+ +[CRFDRiPad1DeviceHandler isiPad1ProductType:]
+ +[CRFileSystemController sharedSingleton]
+ +[CRLocalization localizedStringWithFormat:component:]
+ +[CRLocalization localizedStringWithFormat:component:].cold.1
+ +[CRLocalization localizedStringWithFormat:component:].cold.2
+ +[CRLocalization localizedStringWithKey:]
+ +[CRLocalization localizedStringWithKey:].cold.1
+ +[CRMesaController getProtocolVersion]
+ +[CRMesaController getProtocolVersion].cold.1
+ +[CRNVRAMController deleteNVRAMValueForKey:error:]
+ +[CRNVRAMController deleteNVRAMValueForKey:error:].cold.1
+ +[CRNVRAMController deleteNVRAMValueForKey:error:].cold.2
+ +[CRNVRAMController deleteNVRAMValueForKey:error:].cold.3
+ +[CRNVRAMController readNVRAMValueForKey:error:]
+ +[CRNVRAMController readNVRAMValueForKey:error:].cold.1
+ +[CRNVRAMController readNVRAMValueForKey:error:].cold.2
+ +[CRNVRAMController readNVRAMValueForKey:error:].cold.3
+ +[CRNVRAMController setNVRAMValueForKey:value:error:]
+ +[CRNVRAMController setNVRAMValueForKey:value:error:].cold.1
+ +[CRNVRAMController setNVRAMValueForKey:value:error:].cold.2
+ +[CRNVRAMController setNVRAMValueForKey:value:error:].cold.3
+ +[CRPatchUtils decodePatchItems:]
+ +[CRPatchUtils decodePatchItems:].cold.1
+ +[CRPatchUtils decodePatchItems:].cold.2
+ +[CRPatchUtils encodePatchItems:dataInstance:subCCDict:]
+ +[CRPatchUtils encodePatchItems:dataInstance:subCCDict:].cold.1
+ +[CRPersonalizationManager IsTatsuErrorNetworkingRelated:]
+ +[CRPersonalizationManager _copySikaFuse]
+ +[CRPersonalizationManager createBaseAMAIObject]
+ +[CRPersonalizationManager defaultManager]
+ +[CRPersonalizationManager enableSSO:]
+ +[CRPersonalizationManager enableSSO:].cold.1
+ +[CRPersonalizationManager enableSSO:].cold.2
+ +[CRPersonalizationManager enableSSO:].cold.3
+ +[CRPersonalizationManager enableSSO:].cold.4
+ +[CRPersonalizationManager getDefaultAMAuthInstallRef]
+ +[CRPersonalizationManager initWithAuthInstallObj:]
+ +[CRPersonalizationManager shouldPersonalizeWithSSOByDefault]
+ +[CRPreflightHelper sharedInstance]
+ +[CRPreflightHelper sharedInstance].cold.1
+ +[CRPreflightRequest request]
+ +[CRPreflightUtils _hasSameKey:this:other:]
+ +[CRPreflightUtils _mergeActivationLocks:]
+ +[CRPreflightUtils activationResults:]
+ +[CRPreflightUtils activationResults:].cold.1
+ +[CRPreflightUtils activationResults:].cold.2
+ +[CRPreflightUtils activationResults:].cold.3
+ +[CRPreflightUtils activationResults:].cold.4
+ +[CRPreflightUtils parseChallengeObject:withHandler:]
+ +[CRPreflightUtils parseChallengeObject:withHandler:].cold.1
+ +[CRPreflightUtils parseChallengeObject:withHandler:].cold.2
+ +[CRPreflightUtils parseChallengeObject:withHandler:].cold.3
+ +[CRPreflightUtils parseChallengeObject:withHandler:].cold.4
+ +[CRPreflightUtils spcResults:]
+ +[CRPreflightUtils spcResults:].cold.1
+ +[CRPreflightUtils spcResults:].cold.2
+ +[CRPreflightUtils spcResults:].cold.3
+ +[CRPreflightUtils spcResults:].cold.4
+ +[CRPreflightUtils spcResults:].cold.5
+ +[CRPreflightUtils spcResults:].cold.6
+ +[CRPreflightUtils spcResults:].cold.7
+ +[CRRepairReport _checkComponentResealedWithRCHL:usedPart:error:]
+ +[CRRepairReport checkComponentFailed:error:]
+ +[CRRepairReport checkComponentResealed:usedPart:error:]
+ +[CRRepairReport checkComponentUnsealed:error:]
+ +[CRRepairReport checkNonSecureRepair:error:]
+ +[CRRepairReport determineRepairStatus:repairHistory:]
+ +[CRRepairReport generateReport:error:]
+ +[CRRepairReport getComponentState:error:]
+ +[CRRepairReport getComponentState:error:].cold.1
+ +[CRRepairReport getRepairDate:]
+ +[CRRepairReport getSupportedComponents]
+ +[CRRepairReport insertItem:item:]
+ +[CRRepairReport isSelfRepairedComponent:]
+ +[CRRepairReport populateDCSignedComponents]
+ +[CRRepairReport populateIssueComponents]
+ +[CRRepairReport populateRCHLHistory]
+ +[CRRepairReport populateUnsealedComponents]
+ +[CRRepairReportItem itemWithName:]
+ +[CRRepairStatusLite getData:instance:]
+ +[CRRepairStatusLite getDataForDataClass:]
+ +[CRRepairStatusLite getDataPayload:instance:]
+ +[CRRepairStatusLite getDataPayloadForDataClass:]
+ +[CRRepairStatusLite getSsrBootIntentWithError:]
+ +[CRRepairStatusLite isDeviceStagedSealed]
+ +[CRRepairStatusLite isVeridianFWUpdateRequiredLite]
+ +[CRRepairStatusLite isVeridianFWUpdateRequiredLite].cold.1
+ +[CRRepairStatusLite isVeridianFWUpdateRequiredLite].cold.2
+ +[CRRepairStatusLite isVeridianFWUpdateRequired]
+ +[CRRepairStatusLite isVeridianFWUpdateRequired].cold.1
+ +[CRStrongComponent supportsSecureCoding]
+ +[CRSysConfig sharedAccess]
+ +[CRSysConfig sharedAccess].cold.1
+ +[CRUtils foundInMultiRequestError:dataClass:dataInstance:]
+ +[CRUtils getInnermostNSError:]
+ +[CRUtils getInnermostNSErrorCode:]
+ +[CRUtils powerCycleSensor:]
+ +[CRWiFiCredEncryption decryptUserData:]
+ +[CRWiFiCredEncryption decryptUserData:].cold.1
+ +[CRWiFiCredEncryption decryptUserData:].cold.2
+ +[CRWiFiCredEncryption decryptUserData:].cold.3
+ +[CRWiFiCredEncryption encryptUserData:]
+ +[CRWiFiCredEncryption encryptUserData:].cold.1
+ +[CRWiFiCredEncryption encryptUserData:].cold.2
+ +[CRWiFiCredEncryption encryptUserData:].cold.3
+ +[CRWiFiCredentials createEncryptedCredentialsDataWithLocale:]
+ +[CRWiFiCredentials createEncryptedCredentialsDataWithLocale:].cold.1
+ +[CRWiFiCredentials createEncryptedCredentialsDataWithLocale:].cold.2
+ +[CRWiFiCredentials decryptWiFiCredDictFromCredentialsData:]
+ +[CRWiFiCredentials decryptWiFiCredDictFromCredentialsData:].cold.1
+ +[CRWiFiCredentials decryptWiFiCredDictFromCredentialsData:].cold.2
+ +[CRWiFiCredentials decryptWiFiCredDictFromCredentialsData:].cold.3
+ +[CRWiFiCredentials readAccessPointInfo]
+ +[CoreRepairHelper sharedInstance]
+ +[CoreRepairHelper sharedInstance].cold.1
+ +[NSData(HexString) dataWithHexString:]
+ +[NSData(HexString) dataWithHexString:].cold.1
+ -[CRAttestationHelper challengeComponentsWith:withReply:]
+ -[CRAttestationHelper getStrongComponentsWithReply:]
+ -[CRAudioCodecStatus copyComponentStatus]
+ -[CRAudioCodecStatus init]
+ -[CRAudioCodecStatus isComponentFailed]
+ -[CRAudioCodecStatus isComponentFailed].cold.1
+ -[CRAudioStatus copyComponentStatus]
+ -[CRAudioStatus init]
+ -[CRAudioStatus isComponentFailed]
+ -[CRAudioStatus isComponentFailed].cold.1
+ -[CRBackGlassStatus copyComponentStatus]
+ -[CRBackGlassStatus init]
+ -[CRBasebandStatus copyComponentStatus]
+ -[CRBasebandStatus init]
+ -[CRBasebandStatus isComponentFailed]
+ -[CRBatteryStatus copyComponentStatus]
+ -[CRBatteryStatus init]
+ -[CRBatteryStatus isComponentFailed]
+ -[CRBluetoothStatus copyComponentStatus]
+ -[CRBluetoothStatus init]
+ -[CRBluetoothStatus isComponentFailed]
+ -[CRBootIntentHelper clearBootIntent:]
+ -[CRBootIntentHelper clearBootIntentAndReboot:]
+ -[CRBootIntentHelper clearBootIntentAndReboot:].cold.1
+ -[CRBootIntentHelper clearBootIntentAndReboot:].cold.2
+ -[CRBootIntentHelper clearRepairBackup:]
+ -[CRBootIntentHelper getRepairTicket:]
+ -[CRBootIntentHelper getRepairTicket:].cold.1
+ -[CRBootIntentHelper setBootIntentAndRebootToCheckerboardWithLocale:reply:]
+ -[CRBootIntentHelper setBootIntentAndRebootToCheckerboardWithLocale:reply:].cold.1
+ -[CRBootIntentHelper setBootIntentAndRebootToCheckerboardWithLocale:reply:].cold.2
+ -[CRCAttestationManager .cxx_destruct]
+ -[CRCAttestationManager URLSession:didReceiveChallenge:completionHandler:]
+ -[CRCAttestationManager challengeComponentsWith:challengeResponse:error:]
+ -[CRCAttestationManager getStrongComponentsWithError:resultobtained:]
+ -[CRCAttestationManager init]
+ -[CRCAttestationManager issueClientCertificateWithCompletionOnQueue:withOptions:completion:]
+ -[CRCAttestationManager issueClientCertificateWithCompletionOnQueue:withOptions:completion:].cold.1
+ -[CRCAttestationManager issueClientCertificateWithCompletionOnQueue:withOptions:completion:].cold.2
+ -[CRCAttestationManager issueClientCertificateWithCompletionOnQueue:withOptions:completion:].cold.3
+ -[CRCAttestationManager issueClientCertificateWithCompletionOnQueue:withOptions:completion:].cold.4
+ -[CRCAttestationManager issueClientCertificateWithCompletionOnQueue:withOptions:completion:].cold.5
+ -[CRCAttestationManager issueClientCertificateWithCompletionOnQueue:withOptions:completion:].cold.6
+ -[CRCAttestationManager issueClientCertificateWithCompletionOnQueue:withOptions:completion:].cold.7
+ -[CRCAttestationManager issueClientCertificateWithCompletionOnQueue:withOptions:completion:].cold.8
+ -[CRCAttestationManager progress]
+ -[CRCAttestationManager sendCertIssueRequestWith:serverCertResponse:error:]
+ -[CRCAttestationManager sendChallengeRequestWith:serverResponse:error:]
+ -[CRCAttestationManager transformChallengeResponseWithError:blockChallengeResponse:resultobtained:]
+ -[CRCAttestationManager transformChallengeResponseWithError:blockChallengeResponse:resultobtained:].cold.1
+ -[CRCAttestationManager transformServerCertResponseUsing:serverCertResponseArray:error:]
+ -[CRCAttestationManager transformServerCertResponseUsing:serverCertResponseArray:error:].cold.1
+ -[CRCAttestationManager transformStrongWithError:blockComponents:resultobtained:]
+ -[CRCAttestationManager transformStrongWithError:blockComponents:resultobtained:].cold.1
+ -[CRCCertificate .cxx_destruct]
+ -[CRCCertificate certifcateType]
+ -[CRCCertificate certificates]
+ -[CRCCertificate copyCertificatePEMWithError:]
+ -[CRCCertificate copyCertificatePEMWithError:].cold.1
+ -[CRCCertificate copyCertificatePEMWithError:].cold.2
+ -[CRCCertificate extractCAAAttestationOIDDataWithError:]
+ -[CRCCertificate extractCAAAttestationOIDDataWithError:].cold.1
+ -[CRCCertificate extractCAAAttestationOIDDataWithError:].cold.2
+ -[CRCCertificate extractRepairHistoryWithError:]
+ -[CRCCertificate extractRepairHistoryWithError:].cold.1
+ -[CRCCertificate initWithRefKey:certificates:certType:]
+ -[CRCCertificate initWithRefKey:certificates:certType:].cold.1
+ -[CRCCertificate init]
+ -[CRCCertificate referenceKey]
+ -[CRCCertificate setCertifcateType:]
+ -[CRCCertificate setCertificates:]
+ -[CRCCertificate setReferenceKey:]
+ -[CRCameraAuth copyComponentStatus]
+ -[CRCameraAuth getCmClValidationStatus]
+ -[CRCameraAuth getCmClValidationStatus].cold.1
+ -[CRCameraAuth init]
+ -[CRCameraAuth isComponentFailed]
+ -[CRCameraAuthUsingProperty copyComponentStatus]
+ -[CRCameraAuthUsingProperty init]
+ -[CRChallengeObject .cxx_destruct]
+ -[CRChallengeObject componentType]
+ -[CRChallengeObject encodeWithCoder:]
+ -[CRChallengeObject initWithCoder:]
+ -[CRChallengeObject initWithComponentType:challenge:keyIndex:properties:]
+ -[CRChallengeObject init]
+ -[CRChallengeObject keyIndex]
+ -[CRChallengeObject nonce]
+ -[CRChallengeObject properties]
+ -[CRChallengeObject setComponentType:]
+ -[CRChallengeObject setKeyIndex:]
+ -[CRChallengeObject setNonce:]
+ -[CRChallengeObject setProperties:]
+ -[CRChallengeResponse .cxx_destruct]
+ -[CRChallengeResponse componentType]
+ -[CRChallengeResponse description]
+ -[CRChallengeResponse encodeWithCoder:]
+ -[CRChallengeResponse identifier]
+ -[CRChallengeResponse initWithCoder:]
+ -[CRChallengeResponse initWithComponentType:identifier:signedResponse:keyIndex:properties:]
+ -[CRChallengeResponse init]
+ -[CRChallengeResponse keyIndex]
+ -[CRChallengeResponse properties]
+ -[CRChallengeResponse setComponentType:]
+ -[CRChallengeResponse setIdentifier:]
+ -[CRChallengeResponse setKeyIndex:]
+ -[CRChallengeResponse setProperties:]
+ -[CRChallengeResponse setSignedResponse:]
+ -[CRChallengeResponse signedResponse]
+ -[CRChassisController checkRepairEnvironment]
+ -[CRChassisController diffWithSealed:live:]
+ -[CRChassisController getAndVerifyDataInstance:]
+ -[CRChassisController getAndVerifyDataInstance:].cold.1
+ -[CRChassisController getAndVerifyDataInstance:].cold.2
+ -[CRChassisController getLiveChMf]
+ -[CRChassisController getLiveChMf].cold.1
+ -[CRChassisController getOSEnvironment]
+ -[CRChassisController overrideFromNVRam:]
+ -[CRChassisController overrideFromNVRam:].cold.1
+ -[CRChassisController overrideParameters:]
+ -[CRChassisController replyWithError:reply:]
+ -[CRChassisController replyWithMessage:status:results:reply:]
+ -[CRChassisController seal:withReply:]
+ -[CRChassisController shouldIgnorePatching:]
+ -[CRComponentAuth .cxx_destruct]
+ -[CRComponentAuth _checkForComponentFailureInDefaults:]
+ -[CRComponentAuth _getObjectForKeyFromDefaults:]
+ -[CRComponentAuth componentName]
+ -[CRComponentAuth convertIORegDataToStatus:authPass:]
+ -[CRComponentAuth copyComponentStatus]
+ -[CRComponentAuth findUnsealedData]
+ -[CRComponentAuth findUnsealedData].cold.1
+ -[CRComponentAuth getAuthCPComponentStatus:]
+ -[CRComponentAuth getAuthCPComponentStatus:].cold.1
+ -[CRComponentAuth initWithComponentName:]
+ -[CRComponentAuth init]
+ -[CRComponentAuth isComponentFailed]
+ -[CRComponentAuth isFirstAuthComplete]
+ -[CRComponentAuth setComponentName:]
+ -[CRComponentAuth synchronouslycopyAuthStatus]
+ -[CRComponentAuth synchronouslycopyAuthStatus].cold.1
+ -[CRComponentAuth synchronouslycopyAuthStatus].cold.2
+ -[CRComponentBase .cxx_destruct]
+ -[CRComponentBase CRCreateECDSADerData:responseDer:]
+ -[CRComponentBase CRCreateECDSADerData:responseDer:].cold.1
+ -[CRComponentBase CRCreateECDSADerData:responseDer:].cold.10
+ -[CRComponentBase CRCreateECDSADerData:responseDer:].cold.2
+ -[CRComponentBase CRCreateECDSADerData:responseDer:].cold.3
+ -[CRComponentBase CRCreateECDSADerData:responseDer:].cold.4
+ -[CRComponentBase CRCreateECDSADerData:responseDer:].cold.5
+ -[CRComponentBase CRCreateECDSADerData:responseDer:].cold.6
+ -[CRComponentBase CRCreateECDSADerData:responseDer:].cold.7
+ -[CRComponentBase CRCreateECDSADerData:responseDer:].cold.8
+ -[CRComponentBase CRCreateECDSADerData:responseDer:].cold.9
+ -[CRComponentBase challengeComponentWith:withReply:]
+ -[CRComponentBase identifierBase64]
+ -[CRComponentBase init]
+ -[CRComponentBase setIdentifierBase64:]
+ -[CRComponentBase sha256:]
+ -[CRComponentBatteryRoswell .cxx_destruct]
+ -[CRComponentBatteryRoswell _init]
+ -[CRComponentBatteryRoswell _init].cold.1
+ -[CRComponentBatteryRoswell challengeComponentWith:withReply:]
+ -[CRComponentBatteryRoswell challengeComponentWith:withReply:].cold.1
+ -[CRComponentBatteryRoswell identifierBase64]
+ -[CRComponentBatteryRoswell init]
+ -[CRComponentBatteryRoswell setIdentifierBase64:]
+ -[CRComponentBatteryRoswell signbatteryRoswellWith:withReply:]
+ -[CRComponentBatteryRoswell signbatteryRoswellWith:withReply:].cold.1
+ -[CRComponentBatteryRoswell signbatteryRoswellWith:withReply:].cold.2
+ -[CRComponentBatteryRoswell signbatteryRoswellWith:withReply:].cold.3
+ -[CRComponentBatteryRoswell signbatteryRoswellWith:withReply:].cold.4
+ -[CRComponentDisplayRoswell .cxx_destruct]
+ -[CRComponentDisplayRoswell _init]
+ -[CRComponentDisplayRoswell _init].cold.1
+ -[CRComponentDisplayRoswell challengeComponentWith:withReply:]
+ -[CRComponentDisplayRoswell challengeComponentWith:withReply:].cold.1
+ -[CRComponentDisplayRoswell identifierBase64]
+ -[CRComponentDisplayRoswell init]
+ -[CRComponentDisplayRoswell setIdentifierBase64:]
+ -[CRComponentDisplayRoswell signDisplayRoswellWith:withReply:]
+ -[CRComponentDisplayRoswell signDisplayRoswellWith:withReply:].cold.1
+ -[CRComponentDisplayRoswell signDisplayRoswellWith:withReply:].cold.2
+ -[CRComponentDisplayRoswell signDisplayRoswellWith:withReply:].cold.3
+ -[CRComponentDisplayRoswell signDisplayRoswellWith:withReply:].cold.4
+ -[CRComponentPearl .cxx_destruct]
+ -[CRComponentPearl _init]
+ -[CRComponentPearl _init].cold.1
+ -[CRComponentPearl challengeComponentWith:withReply:]
+ -[CRComponentPearl challengeComponentWith:withReply:].cold.1
+ -[CRComponentPearl identifierBase64]
+ -[CRComponentPearl init]
+ -[CRComponentPearl setIdentifierBase64:]
+ -[CRComponentSigning bcrtSign:outSignature:outDeviceNonce:outError:]
+ -[CRComponentSigning prpcSign:outSignature:outDeviceNonce:outError:]
+ -[CRComponentSigning prpcSign:outSignature:outDeviceNonce:outError:].cold.1
+ -[CRComponentSigning prpcSign:outSignature:outDeviceNonce:outError:].cold.10
+ -[CRComponentSigning prpcSign:outSignature:outDeviceNonce:outError:].cold.11
+ -[CRComponentSigning prpcSign:outSignature:outDeviceNonce:outError:].cold.12
+ -[CRComponentSigning prpcSign:outSignature:outDeviceNonce:outError:].cold.13
+ -[CRComponentSigning prpcSign:outSignature:outDeviceNonce:outError:].cold.14
+ -[CRComponentSigning prpcSign:outSignature:outDeviceNonce:outError:].cold.15
+ -[CRComponentSigning prpcSign:outSignature:outDeviceNonce:outError:].cold.16
+ -[CRComponentSigning prpcSign:outSignature:outDeviceNonce:outError:].cold.17
+ -[CRComponentSigning prpcSign:outSignature:outDeviceNonce:outError:].cold.18
+ -[CRComponentSigning prpcSign:outSignature:outDeviceNonce:outError:].cold.19
+ -[CRComponentSigning prpcSign:outSignature:outDeviceNonce:outError:].cold.2
+ -[CRComponentSigning prpcSign:outSignature:outDeviceNonce:outError:].cold.20
+ -[CRComponentSigning prpcSign:outSignature:outDeviceNonce:outError:].cold.21
+ -[CRComponentSigning prpcSign:outSignature:outDeviceNonce:outError:].cold.22
+ -[CRComponentSigning prpcSign:outSignature:outDeviceNonce:outError:].cold.23
+ -[CRComponentSigning prpcSign:outSignature:outDeviceNonce:outError:].cold.3
+ -[CRComponentSigning prpcSign:outSignature:outDeviceNonce:outError:].cold.4
+ -[CRComponentSigning prpcSign:outSignature:outDeviceNonce:outError:].cold.5
+ -[CRComponentSigning prpcSign:outSignature:outDeviceNonce:outError:].cold.6
+ -[CRComponentSigning prpcSign:outSignature:outDeviceNonce:outError:].cold.7
+ -[CRComponentSigning prpcSign:outSignature:outDeviceNonce:outError:].cold.8
+ -[CRComponentSigning prpcSign:outSignature:outDeviceNonce:outError:].cold.9
+ -[CRComponentSigning tcrtSign:outSignature:outDeviceNonce:outError:]
+ -[CRComponentSigning vcrtSign:outSignature:outDeviceNonce:outError:]
+ -[CRComponentSigning vcrtSign:outSignature:outDeviceNonce:outError:].cold.1
+ -[CRComponentSigning vcrtSign:outSignature:outDeviceNonce:outError:].cold.2
+ -[CRComponentSigning vcrtSign:outSignature:outDeviceNonce:outError:].cold.3
+ -[CRComponentSigning vcrtSign:outSignature:outDeviceNonce:outError:].cold.4
+ -[CRComponentSigning vcrtSign:outSignature:outDeviceNonce:outError:].cold.5
+ -[CRComponentSigning vcrtSign:outSignature:outDeviceNonce:outError:].cold.6
+ -[CRComponentSigning vcrtSign:outSignature:outDeviceNonce:outError:].cold.7
+ -[CRComponentSigning vcrtSign:outSignature:outDeviceNonce:outError:].cold.8
+ -[CRComponentSigning vcrtSign:outSignature:outDeviceNonce:outError:].cold.9
+ -[CRComponentTsid .cxx_destruct]
+ -[CRComponentTsid _init]
+ -[CRComponentTsid _init].cold.1
+ -[CRComponentTsid _init].cold.2
+ -[CRComponentTsid _init].cold.3
+ -[CRComponentTsid challengeComponentWith:withReply:]
+ -[CRComponentTsid challengeComponentWith:withReply:].cold.1
+ -[CRComponentTsid challengeComponentWith:withReply:].cold.2
+ -[CRComponentTsid challengeComponentWith:withReply:].cold.3
+ -[CRComponentTsid connectToIO:withError:]
+ -[CRComponentTsid connectToIO:withError:].cold.1
+ -[CRComponentTsid connectToIO:withError:].cold.2
+ -[CRComponentTsid identifierBase64]
+ -[CRComponentTsid init]
+ -[CRComponentTsid issueChallenge:index:reponse:options:connection:withError:]
+ -[CRComponentTsid setIdentifierBase64:]
+ -[CRComponentVeridian .cxx_destruct]
+ -[CRComponentVeridian _init]
+ -[CRComponentVeridian _init].cold.1
+ -[CRComponentVeridian challengeComponentWith:withReply:]
+ -[CRComponentVeridian challengeComponentWith:withReply:].cold.1
+ -[CRComponentVeridian identifierBase64]
+ -[CRComponentVeridian init]
+ -[CRComponentVeridian setIdentifierBase64:]
+ -[CRComponentVeridian signVeridianWith:withReply:]
+ -[CRComponentVeridian signVeridianWith:withReply:].cold.1
+ -[CRComponentVeridian signVeridianWith:withReply:].cold.2
+ -[CRComponentVeridian signVeridianWith:withReply:].cold.3
+ -[CRComponentVeridian signVeridianWith:withReply:].cold.4
+ -[CRCoverGlassStatus copyComponentStatus]
+ -[CRCoverGlassStatus init]
+ -[CRDevice .cxx_destruct]
+ -[CRDevice components]
+ -[CRDevice getComponentBySPC:]
+ -[CRDevice getComponentByType:]
+ -[CRDevice initWithComponents:]
+ -[CRDevice populateLookupDictionary:]
+ -[CRDevice setComponents:]
+ -[CRDevice setSpcToComponent:]
+ -[CRDevice setSupportElabel:]
+ -[CRDevice setTypeToComponent:]
+ -[CRDevice spcToComponent]
+ -[CRDevice supportElabel]
+ -[CRDevice typeToComponent]
+ -[CRDeviceComponent .cxx_destruct]
+ -[CRDeviceComponent _checkStrongIdentity:]
+ -[CRDeviceComponent fdrKeys]
+ -[CRDeviceComponent hasStrongIdentity]
+ -[CRDeviceComponent initWithType:locKey:]
+ -[CRDeviceComponent initWithType:locKey:spc:fdrKeys:]
+ -[CRDeviceComponent initWithType:locKey:spc:fdrKeys:superModule:]
+ -[CRDeviceComponent initWithType:locKey:superModule:fdrKeys:]
+ -[CRDeviceComponent locKey]
+ -[CRDeviceComponent setFdrKeys:]
+ -[CRDeviceComponent setHasStrongIdentity:]
+ -[CRDeviceComponent setLocKey:]
+ -[CRDeviceComponent setSpc:]
+ -[CRDeviceComponent setSuperModule:]
+ -[CRDeviceComponent setType:]
+ -[CRDeviceComponent spc]
+ -[CRDeviceComponent superModule]
+ -[CRDeviceComponent type]
+ -[CRDisplayStatus copyComponentStatus]
+ -[CRDisplayStatus init]
+ -[CRDisplayStatus isComponentFailed]
+ -[CREANController .cxx_destruct]
+ -[CREANController _apticketCopyDataObjectPropertyWithTag:property:]
+ -[CREANController _apticketCopyDataObjectPropertyWithTag:property:].cold.1
+ -[CREANController _apticketCopyDataObjectPropertyWithTag:property:].cold.2
+ -[CREANController _apticketCopyDataObjectPropertyWithTag:property:].cold.3
+ -[CREANController _getDataClassesToWrite]
+ -[CREANController _getDataClassesToWrite].cold.1
+ -[CREANController _getDataClassesToWrite].cold.2
+ -[CREANController _getQuerykeyFromDataClass:]
+ -[CREANController _getQuerykeyFromDataClass:].cold.1
+ -[CREANController _ticketCopyHashDataWithNode:]
+ -[CREANController _ticketCopyHashDataWithNode:].cold.1
+ -[CREANController _ticketCopyHashDataWithNode:].cold.2
+ -[CREANController _ticketCopyHashDataWithNode:].cold.3
+ -[CREANController _writeDataToEAN:withKey:]
+ -[CREANController _writeDataToEAN:withKey:].cold.1
+ -[CREANController _writeDataToEAN:withKey:].cold.2
+ -[CREANController _writeDataToEAN:withKey:].cold.3
+ -[CREANController _writeDataToEAN:withKey:].cold.4
+ -[CREANController _writeDataToEAN:withKey:].cold.5
+ -[CREANController _writeDataToEAN:withKey:].cold.6
+ -[CREANController _writeDataToEAN:withKey:].cold.7
+ -[CREANController apticketCopyHashData]
+ -[CREANController apticketCopyHashData].cold.1
+ -[CREANController apticketCopyHashData].cold.2
+ -[CREANController calculateDerLength:actualSize:]
+ -[CREANController calculateDerLength:actualSize:].cold.1
+ -[CREANController copyCurrentFDREANValuesWithdataDir:error:]
+ -[CREANController copyCurrentFDREANValuesWithdataDir:error:].cold.1
+ -[CREANController copyCurrentFDREANValuesWithdataDir:error:].cold.2
+ -[CREANController copyCurrentFDREANValuesWithdataDir:error:].cold.3
+ -[CREANController copyCurrentFDREANValuesWithdataDir:error:].cold.4
+ -[CREANController copyCurrentFDREANValuesWithdataDir:error:].cold.5
+ -[CREANController copyCurrentFDREANValuesWithdataDir:error:].cold.6
+ -[CREANController copyCurrentFDREANValuesWithdataDir:error:].cold.7
+ -[CREANController copyCurrentFDREANValuesWithdataDir:error:].cold.8
+ -[CREANController copyFDREANValues:outgenerationCount:outManifesthash:]
+ -[CREANController copyFDREANValues:outgenerationCount:outManifesthash:].cold.1
+ -[CREANController copyFDREANValues:outgenerationCount:outManifesthash:].cold.2
+ -[CREANController copyFDREANValues:outgenerationCount:outManifesthash:].cold.3
+ -[CREANController copyFDREANValues:outgenerationCount:outManifesthash:].cold.4
+ -[CREANController copyFDREANValues:outgenerationCount:outManifesthash:].cold.5
+ -[CREANController copyFDREANValues:outgenerationCount:outManifesthash:].cold.6
+ -[CREANController copyFDREANValues:outgenerationCount:outManifesthash:].cold.7
+ -[CREANController copyStagedFDREanDataWithdataDir:error:]
+ -[CREANController copyStagedFDREanDataWithdataDir:error:].cold.1
+ -[CREANController copyStagedFDREanDataWithdataDir:error:].cold.2
+ -[CREANController copyStagedFDREanDataWithdataDir:error:].cold.3
+ -[CREANController deleteFDRDataFromEANWithDataClass:]
+ -[CREANController deleteFDRDataFromEANWithDataClass:].cold.1
+ -[CREANController deleteFDRDataFromEANWithDataClass:].cold.2
+ -[CREANController deleteFDRDataFromEANWithDataClass:].cold.3
+ -[CREANController deleteFDRDataFromEANWithDataClass:].cold.4
+ -[CREANController deleteFDRDataFromEANWithDataClass:].cold.5
+ -[CREANController isEANSupported]
+ -[CREANController isEANSupported].cold.1
+ -[CREANController nextEANGenerationCount]
+ -[CREANController readFDRDataFromEANWithDataClass:outData:stripPadding:]
+ -[CREANController readFDRDataFromEANWithDataClass:outData:stripPadding:].cold.1
+ -[CREANController readFDRDataFromEANWithDataClass:outData:stripPadding:].cold.2
+ -[CREANController readFDRDataFromEANWithDataClass:outData:stripPadding:].cold.3
+ -[CREANController readFDRDataFromEANWithDataClass:outData:stripPadding:].cold.4
+ -[CREANController readFDRDataFromEANWithDataClass:outData:stripPadding:].cold.5
+ -[CREANController readFDRDataFromEANWithDataClass:outData:stripPadding:].cold.6
+ -[CREANController readFDRDataFromEANWithDataClass:outData:stripPadding:].cold.7
+ -[CREANController readFDRDataFromEANWithDataClass:outData:stripPadding:].cold.8
+ -[CREANController setupVersionedFDRWithApTicket:]
+ -[CREANController setupVersionedFDRWithApTicket:].cold.1
+ -[CREANController setupVersionedFDRWithApTicket:].cold.2
+ -[CREANController setupVersionedFDRWithApTicket:].cold.3
+ -[CREANController setupVersionedFDRWithApTicket:].cold.4
+ -[CREANController setupVersionedFDRWithApTicket:].cold.5
+ -[CREANController sizeEAN:]
+ -[CREANController sizeEAN:].cold.1
+ -[CREANController sizeEAN:].cold.2
+ -[CREANController sizeEAN:].cold.3
+ -[CREANController sizeEAN:].cold.4
+ -[CREANController sizeEAN:].cold.5
+ -[CREANController sizeEAN:].cold.6
+ -[CREANController stageVersionedFDREANWithdataDir:error:]
+ -[CREANController stageVersionedFDREANWithdataDir:error:].cold.1
+ -[CREANController stageVersionedFDREANWithdataDir:error:].cold.2
+ -[CREANController swapEAN:withKey:]
+ -[CREANController swapEAN:withKey:].cold.1
+ -[CREANController swapEAN:withKey:].cold.2
+ -[CREANController swapEAN:withKey:].cold.3
+ -[CREANController swapEAN:withKey:].cold.4
+ -[CREANController swapEAN:withKey:].cold.5
+ -[CREANController swapEAN:withKey:].cold.6
+ -[CREANController swapEAN:withKey:].cold.7
+ -[CREANController swapEAN:withKey:].cold.8
+ -[CREANController swapVersionedFDR]
+ -[CREANController swapVersionedFDR].cold.1
+ -[CREANController swapVersionedFDR].cold.2
+ -[CREANController verifyFDRDataFromEANUsingCache:cachedData:]
+ -[CREANController verifyFDRDataFromEANUsingCache:cachedData:].cold.1
+ -[CREANController verifyFDRDataFromEANUsingCache:cachedData:].cold.2
+ -[CREANController verifyFDRDataFromEANUsingCache:cachedData:].cold.3
+ -[CREANController verifyFDRDataFromEANUsingCache:cachedData:].cold.4
+ -[CREANController verifyFDRDataFromEANUsingCache:cachedData:].cold.5
+ -[CREANController writeEAN:isImg4:]
+ -[CREANController writeEAN:isImg4:].cold.1
+ -[CREANController writeEAN:isImg4:].cold.2
+ -[CREANController writeEAN:isImg4:].cold.3
+ -[CREANController writeEAN:isImg4:].cold.4
+ -[CREANController writeEAN:isImg4:].cold.5
+ -[CREANController writeFDRDataToEANWithdataDir:]
+ -[CREANController writeFDRDataToEANWithdataDir:].cold.1
+ -[CREANController writeFDRDataToEANWithdataDir:].cold.2
+ -[CREANController writeFDRDataToEANWithdataDir:].cold.3
+ -[CREnclosureStatus copyComponentStatus]
+ -[CREnclosureStatus init]
+ -[CRFDRBaseDeviceHandler .cxx_destruct]
+ -[CRFDRBaseDeviceHandler KBBDataClasses]
+ -[CRFDRBaseDeviceHandler KBBDataInstances]
+ -[CRFDRBaseDeviceHandler KBBECID]
+ -[CRFDRBaseDeviceHandler KBBSIK]
+ -[CRFDRBaseDeviceHandler KBBSealInstance]
+ -[CRFDRBaseDeviceHandler KBBSerialNumber]
+ -[CRFDRBaseDeviceHandler KGBSerialNumber]
+ -[CRFDRBaseDeviceHandler _addDataClassAndInstanceToMutableDictionary:dataClass:withError:]
+ -[CRFDRBaseDeviceHandler _addDataClassAndInstanceToMutableDictionary:dataClass:withError:].cold.1
+ -[CRFDRBaseDeviceHandler _addDataClassAndInstancesToMutableArray:dataClasses:dataInstances:withError:]
+ -[CRFDRBaseDeviceHandler _addDataClassAndInstancesToMutableArray:dataClasses:dataInstances:withError:].cold.1
+ -[CRFDRBaseDeviceHandler _addPropertyToMutableDictionary:property:withError:]
+ -[CRFDRBaseDeviceHandler allowFactoryReset]
+ -[CRFDRBaseDeviceHandler allowMissingData]
+ -[CRFDRBaseDeviceHandler challengeComponentsWith:withReply:]
+ -[CRFDRBaseDeviceHandler challengeComponentsWith:withReply:].cold.1
+ -[CRFDRBaseDeviceHandler componentsMapping]
+ -[CRFDRBaseDeviceHandler copyWithZone:]
+ -[CRFDRBaseDeviceHandler currentDataClasses]
+ -[CRFDRBaseDeviceHandler currentDataInstances]
+ -[CRFDRBaseDeviceHandler currentProperties]
+ -[CRFDRBaseDeviceHandler getClaimDataClassesAndInstancesWithPartSPC:withError:]
+ -[CRFDRBaseDeviceHandler getCurrentManifestDataClassesAndInstancesWithPartSPC:fdr:currentClasses:currentInstances:currentProperties:fdrError:]
+ -[CRFDRBaseDeviceHandler getCurrentManifestDataClassesAndInstancesWithPartSPC:fdr:currentClasses:currentInstances:currentProperties:fdrError:].cold.1
+ -[CRFDRBaseDeviceHandler getCurrentManifestDataClassesAndInstancesWithPartSPC:fdr:currentClasses:currentInstances:currentProperties:fdrError:].cold.2
+ -[CRFDRBaseDeviceHandler getCurrentManifestDataClassesAndInstancesWithPartSPC:fdr:currentClasses:currentInstances:currentProperties:fdrError:].cold.3
+ -[CRFDRBaseDeviceHandler getCurrentManifestDataClassesAndInstancesWithPartSPC:fdr:currentClasses:currentInstances:currentProperties:fdrError:].cold.4
+ -[CRFDRBaseDeviceHandler getCurrentMinimalManifestsWithVersions:fdrRemote:minimalSealingDataInstances:minimalSealedDataClasses:minimalSealedDataInstances:minimalSealedVersions:]
+ -[CRFDRBaseDeviceHandler getCurrentMinimalManifestsWithVersions:fdrRemote:minimalSealingDataInstances:minimalSealedDataClasses:minimalSealedDataInstances:minimalSealedVersions:].cold.1
+ -[CRFDRBaseDeviceHandler getDataClassesAndInstancesOfKBBWith:dataClasses:dataInstances:propertiesDict:fdrError:]
+ -[CRFDRBaseDeviceHandler getDataClassesAndInstancesOfKBBWith:dataClasses:dataInstances:propertiesDict:fdrError:].cold.1
+ -[CRFDRBaseDeviceHandler getDataClassesAndInstancesOfKBBWith:propertiesDict:fdrError:]
+ -[CRFDRBaseDeviceHandler getDataClassesAndInstancesOfKBBWith:propertiesDict:fdrError:].cold.1
+ -[CRFDRBaseDeviceHandler getDataValueOfKBBWithDataClass:fdrRemote:error:]
+ -[CRFDRBaseDeviceHandler getDataValueOfKBBWithDataClass:fdrRemote:error:].cold.1
+ -[CRFDRBaseDeviceHandler getExcludedPropertiesForFactoryReset]
+ -[CRFDRBaseDeviceHandler getExcludedPropertiesForSealedVerify]
+ -[CRFDRBaseDeviceHandler getExpectedPatchInfo:]
+ -[CRFDRBaseDeviceHandler getKBBMinimalManifestsWithVersions:minimalSealingDataInstances:minimalSealedDataClasses:minimalSealedDataInstances:minimalSealedVersions:]
+ -[CRFDRBaseDeviceHandler getKBBMinimalManifestsWithVersions:minimalSealingDataInstances:minimalSealedDataClasses:minimalSealedDataInstances:minimalSealedVersions:].cold.1
+ -[CRFDRBaseDeviceHandler getKBBMinimalManifestsWithVersions:minimalSealingDataInstances:minimalSealedDataClasses:minimalSealedDataInstances:minimalSealedVersions:].cold.2
+ -[CRFDRBaseDeviceHandler getKBBMinimalManifestsWithVersions:minimalSealingDataInstances:minimalSealedDataClasses:minimalSealedDataInstances:minimalSealedVersions:].cold.3
+ -[CRFDRBaseDeviceHandler getKBBSealInstanceWithError:fdrRemote:]
+ -[CRFDRBaseDeviceHandler getMakeDataClassesAndInstancesWithPartSPC:fdrRemote:makeClasses:makeInstances:makePropertiesDict:fdrError:]
+ -[CRFDRBaseDeviceHandler getMinimalManifestsClassesAndInstancesWithPartSPC:fdrLocal:fdrRemote:minimalSealingDataInstances:minimalSealedDataClasses:minimalSealedDataInstances:minimalSealedVersions:error:]
+ -[CRFDRBaseDeviceHandler getPatchDataClassesAndInstancesWithPartSPC:fdrRemote:patchClasses:patchInstances:patchValues:error:]
+ -[CRFDRBaseDeviceHandler getPatchExpectedDataWithPartSPC:amfdr:expectedClasses:expectedInstances:expectedValues:expectedDatas:validClasses:validInstances:error:]
+ -[CRFDRBaseDeviceHandler getPatchExpectedDataWithPartSPC:amfdr:expectedClasses:expectedInstances:expectedValues:expectedDatas:validClasses:validInstances:error:].cold.1
+ -[CRFDRBaseDeviceHandler getPatchExpectedDataWithPartSPC:amfdr:expectedClasses:expectedInstances:expectedValues:expectedDatas:validClasses:validInstances:error:].cold.2
+ -[CRFDRBaseDeviceHandler getPatchExpectedDataWithPartSPC:amfdr:expectedClasses:expectedInstances:expectedValues:expectedDatas:validClasses:validInstances:error:].cold.3
+ -[CRFDRBaseDeviceHandler getPatchExpectedDataWithPartSPC:amfdr:expectedClasses:expectedInstances:expectedValues:expectedDatas:validClasses:validInstances:error:].cold.4
+ -[CRFDRBaseDeviceHandler getPatchExpectedDataWithPartSPC:amfdr:expectedClasses:expectedInstances:expectedValues:expectedDatas:validClasses:validInstances:error:].cold.5
+ -[CRFDRBaseDeviceHandler getPatchInfoPerSPC]
+ -[CRFDRBaseDeviceHandler getSealDateFromSealingManifestData:]
+ -[CRFDRBaseDeviceHandler getSealDateFromSealingManifestData:].cold.1
+ -[CRFDRBaseDeviceHandler getSealDateFromSealingManifestData:].cold.2
+ -[CRFDRBaseDeviceHandler getSealDateFromSealingManifestData:].cold.3
+ -[CRFDRBaseDeviceHandler getSealDateFromSealingManifestData:].cold.4
+ -[CRFDRBaseDeviceHandler getSealDateFromSealingManifestData:].cold.5
+ -[CRFDRBaseDeviceHandler getStrongComponentsWithReply:]
+ -[CRFDRBaseDeviceHandler getUpdateDataClassesAndInstancesWithPartSPC:withError:]
+ -[CRFDRBaseDeviceHandler getUpdatePropertyWithPartSPC:propertiesFromParam:]
+ -[CRFDRBaseDeviceHandler init]
+ -[CRFDRBaseDeviceHandler isServicePart]
+ -[CRFDRBaseDeviceHandler kbbCGSN]
+ -[CRFDRBaseDeviceHandler kbbSealDate]
+ -[CRFDRBaseDeviceHandler kbbSealingManifest]
+ -[CRFDRBaseDeviceHandler performPostSealingStage:]
+ -[CRFDRBaseDeviceHandler previousCGSN]
+ -[CRFDRBaseDeviceHandler sealDate]
+ -[CRFDRBaseDeviceHandler setAllowFactoryReset:]
+ -[CRFDRBaseDeviceHandler setAllowMissingData:]
+ -[CRFDRBaseDeviceHandler setComponentsMapping:]
+ -[CRFDRBaseDeviceHandler setCurrentDataClasses:]
+ -[CRFDRBaseDeviceHandler setCurrentDataInstances:]
+ -[CRFDRBaseDeviceHandler setCurrentProperties:]
+ -[CRFDRBaseDeviceHandler setIsServicePart:]
+ -[CRFDRBaseDeviceHandler setKBBDataClasses:]
+ -[CRFDRBaseDeviceHandler setKBBDataInstances:]
+ -[CRFDRBaseDeviceHandler setKBBECID:]
+ -[CRFDRBaseDeviceHandler setKBBSIK:]
+ -[CRFDRBaseDeviceHandler setKBBSealInstance:]
+ -[CRFDRBaseDeviceHandler setKBBSerialNumber:]
+ -[CRFDRBaseDeviceHandler setKGBSerialNumber:]
+ -[CRFDRBaseDeviceHandler setKbbCGSN:]
+ -[CRFDRBaseDeviceHandler setKbbSealDate:]
+ -[CRFDRBaseDeviceHandler setKbbSealingManifest:]
+ -[CRFDRBaseDeviceHandler setMinimalSealingMeta:hintDataClass:sealingInstances:]
+ -[CRFDRBaseDeviceHandler setMinimalSealingMeta:hintDataClass:sealingInstances:].cold.1
+ -[CRFDRBaseDeviceHandler setMinimalSealingMeta:hintDataClass:sealingInstances:].cold.2
+ -[CRFDRBaseDeviceHandler setMinimalSealingMeta:hintDataClass:sealingInstances:].cold.3
+ -[CRFDRBaseDeviceHandler setMinimalSealingMeta:hintDataClass:sealingInstances:].cold.4
+ -[CRFDRBaseDeviceHandler setMinimalSealingMeta:hintDataClass:sealingInstances:].cold.5
+ -[CRFDRBaseDeviceHandler setPreviousCGSN:]
+ -[CRFDRBaseDeviceHandler setSealDate:]
+ -[CRFDRBaseDeviceHandler setUpdateProperties:]
+ -[CRFDRBaseDeviceHandler setWarnings:]
+ -[CRFDRBaseDeviceHandler spcInPartSPC:withDataClass:]
+ -[CRFDRBaseDeviceHandler spcWithComponent:withIdentifier:]
+ -[CRFDRBaseDeviceHandler storeWarningStrings:]
+ -[CRFDRBaseDeviceHandler supportPatch]
+ -[CRFDRBaseDeviceHandler timeIntervalSinceLastSealing:]
+ -[CRFDRBaseDeviceHandler updateProperties]
+ -[CRFDRBaseDeviceHandler validateAndFilterPatchWithPartSPC:patchClasses:patchInstances:patchValues:validClasses:validInstances:error:]
+ -[CRFDRBaseDeviceHandler validateAndFilterPatchWithPartSPC:patchClasses:patchInstances:patchValues:validClasses:validInstances:error:].cold.1
+ -[CRFDRBaseDeviceHandler validateAndSetSerialNumbersUsingPartSPC:KGBSerialNumber:KBBSerialNumber:withError:]
+ -[CRFDRBaseDeviceHandler validateDisplaySwapped:lessThan:]
+ -[CRFDRBaseDeviceHandler validateSwappedForDays:currentSN:previousSN:sealDate:]
+ -[CRFDRBaseDeviceHandler validateSwappedForDays:currentSN:previousSN:sealDate:].cold.1
+ -[CRFDRBaseDeviceHandler warnings]
+ -[CRFDRCompute1DeviceHandler .cxx_destruct]
+ -[CRFDRCompute1DeviceHandler copyAttestationRequestWithError:challenge:]
+ -[CRFDRCompute1DeviceHandler copyAttestationRequestWithError:challenge:].cold.1
+ -[CRFDRCompute1DeviceHandler copyAttestationRequestWithError:challenge:].cold.2
+ -[CRFDRCompute1DeviceHandler copyAttestationRequestWithError:challenge:].cold.3
+ -[CRFDRCompute1DeviceHandler copyChallengeRequestWithError:]
+ -[CRFDRCompute1DeviceHandler copyChallengeRequestWithError:].cold.1
+ -[CRFDRCompute1DeviceHandler copyChallengeRequestWithError:].cold.2
+ -[CRFDRCompute1DeviceHandler copyWithZone:]
+ -[CRFDRCompute1DeviceHandler getDataInstance]
+ -[CRFDRCompute1DeviceHandler getDataInstance].cold.1
+ -[CRFDRCompute1DeviceHandler getLiveChMf]
+ -[CRFDRCompute1DeviceHandler getLiveChMf].cold.1
+ -[CRFDRCompute1DeviceHandler getStrongComponents]
+ -[CRFDRCompute1DeviceHandler getStrongComponents].cold.1
+ -[CRFDRCompute1DeviceHandler init]
+ -[CRFDRCompute1DeviceHandler supportPatch]
+ -[CRFDRCompute1DeviceHandler validateAndFilterPatchWithPartSPC:patchClasses:patchInstances:patchValues:validClasses:validInstances:error:]
+ -[CRFDRDeviceController .cxx_destruct]
+ -[CRFDRDeviceController _init]
+ -[CRFDRDeviceController getHandlerForDevice]
+ -[CRFDRDeviceController init]
+ -[CRFDRDisplay1DeviceHandler .cxx_destruct]
+ -[CRFDRDisplay1DeviceHandler KBBMLBSerialNumber]
+ -[CRFDRDisplay1DeviceHandler KBBTransferProperties]
+ -[CRFDRDisplay1DeviceHandler copyWithZone:]
+ -[CRFDRDisplay1DeviceHandler getClaimDataClassesAndInstancesWithPartSPC:]
+ -[CRFDRDisplay1DeviceHandler getClaimDataClassesAndInstancesWithPartSPC:].cold.1
+ -[CRFDRDisplay1DeviceHandler getExcludedPropertiesForFactoryReset]
+ -[CRFDRDisplay1DeviceHandler getMakeDataClassesAndInstancesWithPartSPC:fdrRemote:makeClasses:makeInstances:makePropertiesDict:fdrError:]
+ -[CRFDRDisplay1DeviceHandler getMakeDataClassesAndInstancesWithPartSPC:fdrRemote:makeClasses:makeInstances:makePropertiesDict:fdrError:].cold.1
+ -[CRFDRDisplay1DeviceHandler getMakeDataClassesAndInstancesWithPartSPC:fdrRemote:makeClasses:makeInstances:makePropertiesDict:fdrError:].cold.2
+ -[CRFDRDisplay1DeviceHandler getMakeDataClassesAndInstancesWithPartSPC:fdrRemote:makePropertiesDict:fdrError:]
+ -[CRFDRDisplay1DeviceHandler getMakeDataClassesAndInstancesWithPartSPC:fdrRemote:makePropertiesDict:fdrError:].cold.1
+ -[CRFDRDisplay1DeviceHandler getMakeDataClassesAndInstancesWithPartSPC:fdrRemote:makePropertiesDict:fdrError:].cold.2
+ -[CRFDRDisplay1DeviceHandler getMakeDataClassesAndInstancesWithPartSPC:fdrRemote:makePropertiesDict:fdrError:].cold.3
+ -[CRFDRDisplay1DeviceHandler getMakeDataClassesAndInstancesWithPartSPC:fdrRemote:makePropertiesDict:fdrError:].cold.4
+ -[CRFDRDisplay1DeviceHandler getMakeDataClassesAndInstancesWithPartSPC:fdrRemote:makePropertiesDict:fdrError:].cold.5
+ -[CRFDRDisplay1DeviceHandler mlbRepairChecks]
+ -[CRFDRDisplay1DeviceHandler performPostSealingStage:]
+ -[CRFDRDisplay1DeviceHandler performPostSealingStage:].cold.1
+ -[CRFDRDisplay1DeviceHandler performPostSealingStage:].cold.2
+ -[CRFDRDisplay1DeviceHandler performPostSealingStage:].cold.3
+ -[CRFDRDisplay1DeviceHandler setKBBMLBSerialNumber:]
+ -[CRFDRDisplay1DeviceHandler setKBBTransferProperties:]
+ -[CRFDRDisplay1DeviceHandler syncSysConfig:key:inBuffer:]
+ -[CRFDRDisplay1DeviceHandler syncSysConfig:key:inBuffer:].cold.1
+ -[CRFDRDisplay1DeviceHandler syncSysConfig:key:inBuffer:].cold.2
+ -[CRFDRDisplay1DeviceHandler validateAndSetSerialNumbersUsingPartSPC:KGBSerialNumber:KBBSerialNumber:withError:]
+ -[CRFDRDisplay1DeviceHandler validateAndSetSerialNumbersUsingPartSPC:KGBSerialNumber:KBBSerialNumber:withError:].cold.1
+ -[CRFDRDisplay1DeviceHandler validateAndSetSerialNumbersUsingPartSPC:KGBSerialNumber:KBBSerialNumber:withError:].cold.2
+ -[CRFDRDisplay1DeviceHandler validateAndSetSerialNumbersUsingPartSPC:KGBSerialNumber:KBBSerialNumber:withError:].cold.3
+ -[CRFDRGen1DeviceHandler copyWithZone:]
+ -[CRFDRGen1DeviceHandler getClaimDataClassesAndInstancesWithPartSPC:withError:]
+ -[CRFDRGen1DeviceHandler getClaimDataClassesAndInstancesWithPartSPC:withError:].cold.1
+ -[CRFDRGen1DeviceHandler getClaimDataClassesAndInstancesWithPartSPC:withError:].cold.2
+ -[CRFDRGen1DeviceHandler getMakeDataClassesAndInstancesWithPartSPC:fdrRemote:makeClasses:makeInstances:makePropertiesDict:fdrError:]
+ -[CRFDRGen1DeviceHandler getMakeDataClassesAndInstancesWithPartSPC:fdrRemote:makeClasses:makeInstances:makePropertiesDict:fdrError:].cold.1
+ -[CRFDRGen1DeviceHandler getMakeDataClassesAndInstancesWithPartSPC:fdrRemote:makeClasses:makeInstances:makePropertiesDict:fdrError:].cold.2
+ -[CRFDRGen1DeviceHandler getMakeDataClassesAndInstancesWithPartSPC:fdrRemote:makePropertiesDict:fdrError:]
+ -[CRFDRGen1DeviceHandler getMakeDataClassesAndInstancesWithPartSPC:fdrRemote:makePropertiesDict:fdrError:].cold.1
+ -[CRFDRGen1DeviceHandler getUpdateDataClassesAndInstancesWithPartSPC:withError:]
+ -[CRFDRGen1DeviceHandler getUpdateDataClassesAndInstancesWithPartSPC:withError:].cold.1
+ -[CRFDRGen1DeviceHandler init]
+ -[CRFDRGen1DeviceHandler spcInPartSPC:withDataClass:]
+ -[CRFDRGen2DeviceHandler copyWithZone:]
+ -[CRFDRGen2DeviceHandler getClaimDataClassesAndInstancesWithPartSPC:withError:]
+ -[CRFDRGen2DeviceHandler getClaimDataClassesAndInstancesWithPartSPC:withError:].cold.1
+ -[CRFDRGen2DeviceHandler getClaimDataClassesAndInstancesWithPartSPC:withError:].cold.2
+ -[CRFDRGen2DeviceHandler getMakeDataClassesAndInstancesWithPartSPC:fdrRemote:makeClasses:makeInstances:makePropertiesDict:fdrError:]
+ -[CRFDRGen2DeviceHandler getMakeDataClassesAndInstancesWithPartSPC:fdrRemote:makeClasses:makeInstances:makePropertiesDict:fdrError:].cold.1
+ -[CRFDRGen2DeviceHandler getMakeDataClassesAndInstancesWithPartSPC:fdrRemote:makeClasses:makeInstances:makePropertiesDict:fdrError:].cold.2
+ -[CRFDRGen2DeviceHandler getMakeDataClassesAndInstancesWithPartSPC:fdrRemote:makePropertiesDict:fdrError:]
+ -[CRFDRGen2DeviceHandler getMakeDataClassesAndInstancesWithPartSPC:fdrRemote:makePropertiesDict:fdrError:].cold.1
+ -[CRFDRGen2DeviceHandler getUpdateDataClassesAndInstancesWithPartSPC:withError:]
+ -[CRFDRGen2DeviceHandler getUpdateDataClassesAndInstancesWithPartSPC:withError:].cold.1
+ -[CRFDRGen2DeviceHandler init]
+ -[CRFDRGen2DeviceHandler spcInPartSPC:withDataClass:]
+ -[CRFDRGen3DeviceHandler copyWithZone:]
+ -[CRFDRGen3DeviceHandler getBackglassDataClasses]
+ -[CRFDRGen3DeviceHandler getCameraDataClasses]
+ -[CRFDRGen3DeviceHandler getClaimDataClassesAndInstancesWithPartSPC:withError:]
+ -[CRFDRGen3DeviceHandler getClaimDataClassesAndInstancesWithPartSPC:withError:].cold.1
+ -[CRFDRGen3DeviceHandler getClaimDataClassesAndInstancesWithPartSPC:withError:].cold.2
+ -[CRFDRGen3DeviceHandler getMTUBDataClasses]
+ -[CRFDRGen3DeviceHandler getMakeDataClassesAndInstancesWithPartSPC:fdrRemote:makeClasses:makeInstances:makePropertiesDict:fdrError:]
+ -[CRFDRGen3DeviceHandler getMakeDataClassesAndInstancesWithPartSPC:fdrRemote:makeClasses:makeInstances:makePropertiesDict:fdrError:].cold.1
+ -[CRFDRGen3DeviceHandler getMakeDataClassesAndInstancesWithPartSPC:fdrRemote:makeClasses:makeInstances:makePropertiesDict:fdrError:].cold.2
+ -[CRFDRGen3DeviceHandler getMakeDataClassesAndInstancesWithPartSPC:fdrRemote:makePropertiesDict:fdrError:]
+ -[CRFDRGen3DeviceHandler getMakeDataClassesAndInstancesWithPartSPC:fdrRemote:makePropertiesDict:fdrError:].cold.1
+ -[CRFDRGen3DeviceHandler getMakeDataClassesAndInstancesWithPartSPC:fdrRemote:makePropertiesDict:fdrError:].cold.2
+ -[CRFDRGen3DeviceHandler getMakeDataClassesAndInstancesWithPartSPC:fdrRemote:makePropertiesDict:fdrError:].cold.3
+ -[CRFDRGen3DeviceHandler getMakeDataClassesAndInstancesWithPartSPC:fdrRemote:makePropertiesDict:fdrError:].cold.4
+ -[CRFDRGen3DeviceHandler getMakeDataClassesAndInstancesWithPartSPC:fdrRemote:makePropertiesDict:fdrError:].cold.5
+ -[CRFDRGen3DeviceHandler getMakeDataClassesAndInstancesWithPartSPC:fdrRemote:makePropertiesDict:fdrError:].cold.6
+ -[CRFDRGen3DeviceHandler getPearlDataClasses]
+ -[CRFDRGen3DeviceHandler getUpdateDataClassesAndInstancesWithPartSPC:withError:]
+ -[CRFDRGen3DeviceHandler getUpdateDataClassesAndInstancesWithPartSPC:withError:].cold.1
+ -[CRFDRGen3DeviceHandler getUpdatePropertyWithPartSPC:propertiesFromParam:]
+ -[CRFDRGen3DeviceHandler getUpdatePropertyWithPartSPC:propertiesFromParam:].cold.1
+ -[CRFDRGen3DeviceHandler hasCameraRepair:]
+ -[CRFDRGen3DeviceHandler hasMTUBRepair:]
+ -[CRFDRGen3DeviceHandler init]
+ -[CRFDRGen3DeviceHandler spcInPartSPC:withDataClass:]
+ -[CRFDRGen3DeviceHandler spcWithComponent:withIdentifier:]
+ -[CRFDRGen3DeviceHandler validateAndSetSerialNumbersUsingPartSPC:KGBSerialNumber:KBBSerialNumber:withError:]
+ -[CRFDRGen3DeviceHandler validateDisplaySwapped:lessThan:]
+ -[CRFDRGen4DeviceHandler copyWithZone:]
+ -[CRFDRGen4DeviceHandler getClaimDataClassesAndInstancesWithPartSPC:withError:]
+ -[CRFDRGen4DeviceHandler getClaimDataClassesAndInstancesWithPartSPC:withError:].cold.1
+ -[CRFDRGen4DeviceHandler getMakeDataClassesAndInstancesWithPartSPC:fdrRemote:makeClasses:makeInstances:makePropertiesDict:fdrError:]
+ -[CRFDRGen4DeviceHandler getMakeDataClassesAndInstancesWithPartSPC:fdrRemote:makeClasses:makeInstances:makePropertiesDict:fdrError:].cold.1
+ -[CRFDRGen4DeviceHandler getMakeDataClassesAndInstancesWithPartSPC:fdrRemote:makeClasses:makeInstances:makePropertiesDict:fdrError:].cold.2
+ -[CRFDRGen4DeviceHandler getMakeDataClassesAndInstancesWithPartSPC:fdrRemote:makePropertiesDict:fdrError:]
+ -[CRFDRGen4DeviceHandler getMakeDataClassesAndInstancesWithPartSPC:fdrRemote:makePropertiesDict:fdrError:].cold.1
+ -[CRFDRGen4DeviceHandler getMakeDataClassesAndInstancesWithPartSPC:fdrRemote:makePropertiesDict:fdrError:].cold.2
+ -[CRFDRGen4DeviceHandler init]
+ -[CRFDRGen4DeviceHandler spcInPartSPC:withDataClass:]
+ -[CRFDRGen4DeviceHandler spcWithComponent:withIdentifier:]
+ -[CRFDRGen4DeviceHandler validateDisplaySwapped:lessThan:]
+ -[CRFDRGen5DeviceHandler init]
+ -[CRFDRGen6DeviceHandler copyWithZone:]
+ -[CRFDRGen6DeviceHandler getBackglassDataClasses]
+ -[CRFDRGen6DeviceHandler getCameraDataClasses]
+ -[CRFDRGen6DeviceHandler getClaimDataClassesAndInstancesWithPartSPC:withError:]
+ -[CRFDRGen6DeviceHandler getClaimDataClassesAndInstancesWithPartSPC:withError:].cold.1
+ -[CRFDRGen6DeviceHandler getClaimDataClassesAndInstancesWithPartSPC:withError:].cold.2
+ -[CRFDRGen6DeviceHandler getClaimDataClassesAndInstancesWithPartSPC:withError:].cold.3
+ -[CRFDRGen6DeviceHandler getMTUBDataClasses]
+ -[CRFDRGen6DeviceHandler getMakeDataClassesAndInstancesWithPartSPC:fdrRemote:makeClasses:makeInstances:makePropertiesDict:fdrError:]
+ -[CRFDRGen6DeviceHandler getMakeDataClassesAndInstancesWithPartSPC:fdrRemote:makeClasses:makeInstances:makePropertiesDict:fdrError:].cold.1
+ -[CRFDRGen6DeviceHandler getMakeDataClassesAndInstancesWithPartSPC:fdrRemote:makeClasses:makeInstances:makePropertiesDict:fdrError:].cold.2
+ -[CRFDRGen6DeviceHandler getMakeDataClassesAndInstancesWithPartSPC:fdrRemote:makeClasses:makeInstances:makePropertiesDict:fdrError:].cold.3
+ -[CRFDRGen6DeviceHandler getMinimalManifestsClassesAndInstancesWithPartSPC:fdrLocal:fdrRemote:minimalSealingDataInstances:minimalSealedDataClasses:minimalSealedDataInstances:minimalSealedVersions:error:]
+ -[CRFDRGen6DeviceHandler getMinimalManifestsClassesAndInstancesWithPartSPC:fdrLocal:fdrRemote:minimalSealingDataInstances:minimalSealedDataClasses:minimalSealedDataInstances:minimalSealedVersions:error:].cold.1
+ -[CRFDRGen6DeviceHandler getMinimalManifestsClassesAndInstancesWithPartSPC:fdrLocal:fdrRemote:minimalSealingDataInstances:minimalSealedDataClasses:minimalSealedDataInstances:minimalSealedVersions:error:].cold.2
+ -[CRFDRGen6DeviceHandler getMinimalManifestsClassesAndInstancesWithPartSPC:fdrLocal:fdrRemote:minimalSealingDataInstances:minimalSealedDataClasses:minimalSealedDataInstances:minimalSealedVersions:error:].cold.3
+ -[CRFDRGen6DeviceHandler getMinimalManifestsClassesAndInstancesWithPartSPC:fdrLocal:fdrRemote:minimalSealingDataInstances:minimalSealedDataClasses:minimalSealedDataInstances:minimalSealedVersions:error:].cold.4
+ -[CRFDRGen6DeviceHandler getMinimalManifestsClassesAndInstancesWithPartSPC:fdrLocal:fdrRemote:minimalSealingDataInstances:minimalSealedDataClasses:minimalSealedDataInstances:minimalSealedVersions:error:].cold.5
+ -[CRFDRGen6DeviceHandler getPatchInfoPerSPC]
+ -[CRFDRGen6DeviceHandler getPearlDataClasses]
+ -[CRFDRGen6DeviceHandler getUpdateDataClassesAndInstancesWithPartSPC:withError:]
+ -[CRFDRGen6DeviceHandler getUpdateDataClassesAndInstancesWithPartSPC:withError:].cold.1
+ -[CRFDRGen6DeviceHandler hasCameraRepair:]
+ -[CRFDRGen6DeviceHandler hasMTUBRepair:]
+ -[CRFDRGen6DeviceHandler init]
+ -[CRFDRGen6DeviceHandler spcInPartSPC:withDataClass:]
+ -[CRFDRGen6DeviceHandler spcWithComponent:withIdentifier:]
+ -[CRFDRGen6DeviceHandler supportCameraDepth]
+ -[CRFDRGen6DeviceHandler supportHarvestPearl]
+ -[CRFDRGen6DeviceHandler supportMctubMinus]
+ -[CRFDRGen6DeviceHandler supportPatch]
+ -[CRFDRGen6DeviceHandler validateAndFilterPatchWithPartSPC:patchClasses:patchInstances:patchValues:validClasses:validInstances:error:]
+ -[CRFDRGen7DeviceHandler copyWithZone:]
+ -[CRFDRGen7DeviceHandler getClaimDataClassesAndInstancesWithPartSPC:withError:]
+ -[CRFDRGen7DeviceHandler getClaimDataClassesAndInstancesWithPartSPC:withError:].cold.1
+ -[CRFDRGen7DeviceHandler getClaimDataClassesAndInstancesWithPartSPC:withError:].cold.2
+ -[CRFDRGen7DeviceHandler getClaimDataClassesAndInstancesWithPartSPC:withError:].cold.3
+ -[CRFDRGen7DeviceHandler getExcludedPropertiesForSealedVerify]
+ -[CRFDRGen7DeviceHandler getMakeDataClassesAndInstancesWithPartSPC:fdrRemote:makeClasses:makeInstances:makePropertiesDict:fdrError:]
+ -[CRFDRGen7DeviceHandler getMakeDataClassesAndInstancesWithPartSPC:fdrRemote:makeClasses:makeInstances:makePropertiesDict:fdrError:].cold.1
+ -[CRFDRGen7DeviceHandler getMakeDataClassesAndInstancesWithPartSPC:fdrRemote:makeClasses:makeInstances:makePropertiesDict:fdrError:].cold.2
+ -[CRFDRGen7DeviceHandler getMakeDataClassesAndInstancesWithPartSPC:fdrRemote:makeClasses:makeInstances:makePropertiesDict:fdrError:].cold.3
+ -[CRFDRGen7DeviceHandler getMakeDataClassesAndInstancesWithPartSPC:fdrRemote:makeClasses:makeInstances:makePropertiesDict:fdrError:].cold.4
+ -[CRFDRGen7DeviceHandler getMakeDataClassesAndInstancesWithPartSPC:fdrRemote:makeClasses:makeInstances:makePropertiesDict:fdrError:].cold.5
+ -[CRFDRGen7DeviceHandler getMakeDataClassesAndInstancesWithPartSPC:fdrRemote:makeClasses:makeInstances:makePropertiesDict:fdrError:].cold.6
+ -[CRFDRGen7DeviceHandler getMinimalManifestsClassesAndInstancesWithPartSPC:fdrLocal:fdrRemote:minimalSealingDataInstances:minimalSealedDataClasses:minimalSealedDataInstances:minimalSealedVersions:error:]
+ -[CRFDRGen7DeviceHandler getPatchInfoPerSPC]
+ -[CRFDRGen7DeviceHandler init]
+ -[CRFDRGen7DeviceHandler spcInPartSPC:withDataClass:]
+ -[CRFDRGen7DeviceHandler spcWithComponent:withIdentifier:]
+ -[CRFDRGen7DeviceHandler supportArgonRepair]
+ -[CRFDRGen7DeviceHandler supportPatch]
+ -[CRFDRGen7DeviceHandler validateAndFilterPatchWithPartSPC:patchClasses:patchInstances:patchValues:validClasses:validInstances:error:]
+ -[CRFDRGen7DeviceHandler validateAndSetSerialNumbersUsingPartSPC:KGBSerialNumber:KBBSerialNumber:withError:]
+ -[CRFDRGen7DeviceHandler validateDisplaySwapped:lessThan:]
+ -[CRFDRLegacy2DeviceHandler copyWithZone:]
+ -[CRFDRLegacy2DeviceHandler init]
+ -[CRFDRLegacyDeviceHandler copyWithZone:]
+ -[CRFDRLegacyDeviceHandler getClaimDataClassesAndInstancesWithPartSPC:withError:]
+ -[CRFDRLegacyDeviceHandler getClaimDataClassesAndInstancesWithPartSPC:withError:].cold.1
+ -[CRFDRLegacyDeviceHandler getMakeDataClassesAndInstancesWithPartSPC:fdrRemote:makeClasses:makeInstances:makePropertiesDict:fdrError:]
+ -[CRFDRLegacyDeviceHandler getMakeDataClassesAndInstancesWithPartSPC:fdrRemote:makeClasses:makeInstances:makePropertiesDict:fdrError:].cold.1
+ -[CRFDRLegacyDeviceHandler getMakeDataClassesAndInstancesWithPartSPC:fdrRemote:makeClasses:makeInstances:makePropertiesDict:fdrError:].cold.2
+ -[CRFDRLegacyDeviceHandler getMakeDataClassesAndInstancesWithPartSPC:fdrRemote:makePropertiesDict:fdrError:]
+ -[CRFDRLegacyDeviceHandler getUpdateDataClassesAndInstancesWithPartSPC:withError:]
+ -[CRFDRLegacyDeviceHandler getUpdateDataClassesAndInstancesWithPartSPC:withError:].cold.1
+ -[CRFDRLegacyDeviceHandler init]
+ -[CRFDRLegacyDeviceHandler spcInPartSPC:withDataClass:]
+ -[CRFDRRCHL .cxx_destruct]
+ -[CRFDRRCHL dataClasses]
+ -[CRFDRRCHL description]
+ -[CRFDRRCHL initWithrepairDateStr:repairDate:repairCenter:dataClasses:properties:]
+ -[CRFDRRCHL initWithrepairDateStr:repairDate:repairCenter:dataClasses:properties:].cold.1
+ -[CRFDRRCHL init]
+ -[CRFDRRCHL properties]
+ -[CRFDRRCHL repairCenter]
+ -[CRFDRRCHL repairDateStr]
+ -[CRFDRRCHL repairDate]
+ -[CRFDRRCHL setDataClasses:]
+ -[CRFDRRCHL setProperties:]
+ -[CRFDRRCHL setRepairCenter:]
+ -[CRFDRRCHL setRepairDate:]
+ -[CRFDRRCHL setRepairDateStr:]
+ -[CRFDRRetryController .cxx_destruct]
+ -[CRFDRRetryController disableRetry]
+ -[CRFDRRetryController disableRetry].cold.1
+ -[CRFDRRetryController enableRetry]
+ -[CRFDRRetryController enableRetry].cold.1
+ -[CRFDRRetryController enableRetry].cold.2
+ -[CRFDRRetryController init]
+ -[CRFDRSeal .cxx_destruct]
+ -[CRFDRSeal CRFDRCheckVerificationFatalErrors:fdrLocal:sealedData:strict:]
+ -[CRFDRSeal CRFDRDataRepairRecover:fdrRemote:syncEAN:fdrError:]
+ -[CRFDRSeal CRFDRDataRepairRecover:fdrRemote:syncEAN:fdrError:].cold.1
+ -[CRFDRSeal CRFDRDataRepairRecover:fdrRemote:syncEAN:fdrError:].cold.2
+ -[CRFDRSeal CRFDRDataRepairRecover:fdrRemote:syncEAN:fdrError:].cold.3
+ -[CRFDRSeal CRFDRDataRepairRecover:fdrRemote:syncEAN:fdrError:].cold.4
+ -[CRFDRSeal CRFDRDataRepairRecover:fdrRemote:syncEAN:fdrError:].cold.5
+ -[CRFDRSeal CRFDRDataRepairRecover:fdrRemote:syncEAN:fdrError:].cold.6
+ -[CRFDRSeal CRFDRDataRepairRecover:fdrRemote:syncEAN:fdrError:].cold.7
+ -[CRFDRSeal CRFDRLocalPopulate:fdrRemote:sealedData:fdrError:]
+ -[CRFDRSeal CRFDRLocalPopulate:fdrRemote:sealedData:fdrError:].cold.1
+ -[CRFDRSeal CRFDRLocalPopulate:fdrRemote:sealedData:fdrError:].cold.2
+ -[CRFDRSeal CRFDRLocalPopulate:fdrRemote:sealedData:fdrError:].cold.3
+ -[CRFDRSeal CRFDRLocalPopulate:fdrRemote:sealedData:fdrError:].cold.4
+ -[CRFDRSeal CRFDRLocalPopulate:fdrRemote:sealedData:fdrError:].cold.5
+ -[CRFDRSeal CRFDRLocalPopulate:fdrRemote:sealedData:fdrError:].cold.6
+ -[CRFDRSeal CRFDRPostRecoverVerify:fdrRemote:syncEAN:fdrError:]
+ -[CRFDRSeal CRFDRPostRecoverVerify:fdrRemote:syncEAN:fdrError:].cold.1
+ -[CRFDRSeal CRFDRPostRecoverVerify:fdrRemote:syncEAN:fdrError:].cold.2
+ -[CRFDRSeal CRFDRPostRecoverVerify:fdrRemote:syncEAN:fdrError:].cold.3
+ -[CRFDRSeal CRFDRPostRecoverVerify:fdrRemote:syncEAN:fdrError:].cold.4
+ -[CRFDRSeal CRFDRRecoverMissingData:fdrLocal:fdrRemote:]
+ -[CRFDRSeal CRFDRRecoverMissingData:fdrLocal:fdrRemote:].cold.1
+ -[CRFDRSeal CRFDRRecoverMissingData:fdrLocal:fdrRemote:].cold.2
+ -[CRFDRSeal CRFDRRecoverMissingData:fdrLocal:fdrRemote:].cold.3
+ -[CRFDRSeal CRFDRRecoverMissingData:fdrLocal:fdrRemote:].cold.4
+ -[CRFDRSeal CRFDRRecoverMissingData:fdrLocal:fdrRemote:].cold.5
+ -[CRFDRSeal CRFDRRecoverMissingData:fdrLocal:fdrRemote:].cold.6
+ -[CRFDRSeal CRFDRVerifyLocal:fdrRemote:sealedData:mergedDataClasses:mergedDataInstances:currentManifestProperties:fdrError:syncEAN:postSeal:ignoreBenignError:]
+ -[CRFDRSeal CRFDRVerifyLocal:fdrRemote:sealedData:mergedDataClasses:mergedDataInstances:currentManifestProperties:fdrError:syncEAN:postSeal:ignoreBenignError:].cold.1
+ -[CRFDRSeal CRFDRVerifyLocal:fdrRemote:sealedData:mergedDataClasses:mergedDataInstances:currentManifestProperties:fdrError:syncEAN:postSeal:ignoreBenignError:].cold.10
+ -[CRFDRSeal CRFDRVerifyLocal:fdrRemote:sealedData:mergedDataClasses:mergedDataInstances:currentManifestProperties:fdrError:syncEAN:postSeal:ignoreBenignError:].cold.11
+ -[CRFDRSeal CRFDRVerifyLocal:fdrRemote:sealedData:mergedDataClasses:mergedDataInstances:currentManifestProperties:fdrError:syncEAN:postSeal:ignoreBenignError:].cold.2
+ -[CRFDRSeal CRFDRVerifyLocal:fdrRemote:sealedData:mergedDataClasses:mergedDataInstances:currentManifestProperties:fdrError:syncEAN:postSeal:ignoreBenignError:].cold.3
+ -[CRFDRSeal CRFDRVerifyLocal:fdrRemote:sealedData:mergedDataClasses:mergedDataInstances:currentManifestProperties:fdrError:syncEAN:postSeal:ignoreBenignError:].cold.4
+ -[CRFDRSeal CRFDRVerifyLocal:fdrRemote:sealedData:mergedDataClasses:mergedDataInstances:currentManifestProperties:fdrError:syncEAN:postSeal:ignoreBenignError:].cold.5
+ -[CRFDRSeal CRFDRVerifyLocal:fdrRemote:sealedData:mergedDataClasses:mergedDataInstances:currentManifestProperties:fdrError:syncEAN:postSeal:ignoreBenignError:].cold.6
+ -[CRFDRSeal CRFDRVerifyLocal:fdrRemote:sealedData:mergedDataClasses:mergedDataInstances:currentManifestProperties:fdrError:syncEAN:postSeal:ignoreBenignError:].cold.7
+ -[CRFDRSeal CRFDRVerifyLocal:fdrRemote:sealedData:mergedDataClasses:mergedDataInstances:currentManifestProperties:fdrError:syncEAN:postSeal:ignoreBenignError:].cold.8
+ -[CRFDRSeal CRFDRVerifyLocal:fdrRemote:sealedData:mergedDataClasses:mergedDataInstances:currentManifestProperties:fdrError:syncEAN:postSeal:ignoreBenignError:].cold.9
+ -[CRFDRSeal CRFDRVerifyProperties:currentManifestProperties:fdrError:]
+ -[CRFDRSeal _baseFDROptionsWithDataStore:]
+ -[CRFDRSeal _baseFDROptionsWithDataStore:].cold.1
+ -[CRFDRSeal _baseFDROptionsWithDataStore:].cold.2
+ -[CRFDRSeal _commitData:fdrlocal:fdrError:]
+ -[CRFDRSeal _commitData:fdrlocal:fdrError:].cold.1
+ -[CRFDRSeal _commitData:fdrlocal:fdrError:].cold.2
+ -[CRFDRSeal _commitData:fdrlocal:fdrError:].cold.3
+ -[CRFDRSeal _commitData:fdrlocal:fdrError:].cold.4
+ -[CRFDRSeal _commitSealedData:fdrRemote:sealedData:syncEAN:returnError:]
+ -[CRFDRSeal _commitSealedData:fdrRemote:sealedData:syncEAN:returnError:].cold.1
+ -[CRFDRSeal _commitSealedData:fdrRemote:sealedData:syncEAN:returnError:].cold.2
+ -[CRFDRSeal _commitSealedData:fdrRemote:sealedData:syncEAN:returnError:].cold.3
+ -[CRFDRSeal _commitSealedData:fdrRemote:sealedData:syncEAN:returnError:].cold.4
+ -[CRFDRSeal _commitSealedData:fdrRemote:sealedData:syncEAN:returnError:].cold.5
+ -[CRFDRSeal _commitSealedData:fdrRemote:sealedData:syncEAN:returnError:].cold.6
+ -[CRFDRSeal _commitSealedData:fdrRemote:sealedData:syncEAN:returnError:].cold.7
+ -[CRFDRSeal _commitSealedData:fdrRemote:sealedData:syncEAN:returnError:].cold.8
+ -[CRFDRSeal _commitSealedData:fdrRemote:sealedData:syncEAN:returnError:].cold.9
+ -[CRFDRSeal _copyFDROptionsForPatch:]
+ -[CRFDRSeal _copyFDROptionsForPatch:].cold.1
+ -[CRFDRSeal _copyFDROptionsForPatch:].cold.2
+ -[CRFDRSeal _fetchRemoteTrustObject:apTrustObjectDigest:remoteTrustObject:fdrError:]
+ -[CRFDRSeal _fetchRemoteTrustObject:apTrustObjectDigest:remoteTrustObject:fdrError:].cold.1
+ -[CRFDRSeal _fetchRemoteTrustObject:apTrustObjectDigest:remoteTrustObject:fdrError:].cold.2
+ -[CRFDRSeal _fetchRemoteTrustObject:apTrustObjectDigest:remoteTrustObject:fdrError:].cold.3
+ -[CRFDRSeal _fetchRemoteTrustObject:apTrustObjectDigest:remoteTrustObject:fdrError:].cold.4
+ -[CRFDRSeal _getCRFDRMetaDataDictionary]
+ -[CRFDRSeal _logSealingRequest:]
+ -[CRFDRSeal _personalizeTrustObjectWithDigest:withError:]
+ -[CRFDRSeal _urlsOverrideIsAllowed]
+ -[CRFDRSeal _writeBatteryDateOfFirstUse:error:]
+ -[CRFDRSeal _writeBatteryDateOfFirstUse:error:].cold.1
+ -[CRFDRSeal _writeBatteryDateOfFirstUse:error:].cold.2
+ -[CRFDRSeal allowSelfService]
+ -[CRFDRSeal allowUsedPart]
+ -[CRFDRSeal apTicketData]
+ -[CRFDRSeal claimDict]
+ -[CRFDRSeal currentClasses]
+ -[CRFDRSeal currentInstances]
+ -[CRFDRSeal currentProperties]
+ -[CRFDRSeal delegate]
+ -[CRFDRSeal deleteLocalData:]
+ -[CRFDRSeal deleteLocalData:dataClass:]
+ -[CRFDRSeal failedSPC]
+ -[CRFDRSeal generateFinalData]
+ -[CRFDRSeal generateFinalData].cold.1
+ -[CRFDRSeal generateFinalData].cold.2
+ -[CRFDRSeal generateFinalData].cold.3
+ -[CRFDRSeal generateFinalData].cold.4
+ -[CRFDRSeal handler]
+ -[CRFDRSeal initForRegisterChangeWithParameters:]
+ -[CRFDRSeal initForRegisterChangeWithParameters:].cold.1
+ -[CRFDRSeal initForRegisterChangeWithParameters:].cold.2
+ -[CRFDRSeal initForRegisterChangeWithParameters:].cold.3
+ -[CRFDRSeal initForRegisterChangeWithParameters:].cold.4
+ -[CRFDRSeal initForRegisterChangeWithParameters:].cold.5
+ -[CRFDRSeal initWithParameters:]
+ -[CRFDRSeal initWithParameters:].cold.1
+ -[CRFDRSeal initWithParameters:].cold.10
+ -[CRFDRSeal initWithParameters:].cold.11
+ -[CRFDRSeal initWithParameters:].cold.12
+ -[CRFDRSeal initWithParameters:].cold.13
+ -[CRFDRSeal initWithParameters:].cold.14
+ -[CRFDRSeal initWithParameters:].cold.15
+ -[CRFDRSeal initWithParameters:].cold.16
+ -[CRFDRSeal initWithParameters:].cold.17
+ -[CRFDRSeal initWithParameters:].cold.18
+ -[CRFDRSeal initWithParameters:].cold.19
+ -[CRFDRSeal initWithParameters:].cold.2
+ -[CRFDRSeal initWithParameters:].cold.20
+ -[CRFDRSeal initWithParameters:].cold.3
+ -[CRFDRSeal initWithParameters:].cold.4
+ -[CRFDRSeal initWithParameters:].cold.5
+ -[CRFDRSeal initWithParameters:].cold.6
+ -[CRFDRSeal initWithParameters:].cold.7
+ -[CRFDRSeal initWithParameters:].cold.8
+ -[CRFDRSeal initWithParameters:].cold.9
+ -[CRFDRSeal init]
+ -[CRFDRSeal localPatch:dataClasses:dataInstances:values:error:]
+ -[CRFDRSeal makeClasses]
+ -[CRFDRSeal makeInstances]
+ -[CRFDRSeal makeProperties]
+ -[CRFDRSeal mergedDataClasses]
+ -[CRFDRSeal mergedDataInstances]
+ -[CRFDRSeal minimalSealedClasses]
+ -[CRFDRSeal minimalSealedInstances]
+ -[CRFDRSeal minimalSealedVersions]
+ -[CRFDRSeal minimalSealingInstances]
+ -[CRFDRSeal partSPC]
+ -[CRFDRSeal patchDataClasses]
+ -[CRFDRSeal patchDataInstances]
+ -[CRFDRSeal patchItems]
+ -[CRFDRSeal patchValues]
+ -[CRFDRSeal patchWithOptions:amfdr:dataClasses:dataInstances:values:datas:error:local:]
+ -[CRFDRSeal patchWithOptions:amfdr:dataClasses:dataInstances:values:datas:error:local:].cold.1
+ -[CRFDRSeal patchWithOptions:amfdr:dataClasses:dataInstances:values:datas:error:local:].cold.10
+ -[CRFDRSeal patchWithOptions:amfdr:dataClasses:dataInstances:values:datas:error:local:].cold.11
+ -[CRFDRSeal patchWithOptions:amfdr:dataClasses:dataInstances:values:datas:error:local:].cold.12
+ -[CRFDRSeal patchWithOptions:amfdr:dataClasses:dataInstances:values:datas:error:local:].cold.13
+ -[CRFDRSeal patchWithOptions:amfdr:dataClasses:dataInstances:values:datas:error:local:].cold.14
+ -[CRFDRSeal patchWithOptions:amfdr:dataClasses:dataInstances:values:datas:error:local:].cold.15
+ -[CRFDRSeal patchWithOptions:amfdr:dataClasses:dataInstances:values:datas:error:local:].cold.16
+ -[CRFDRSeal patchWithOptions:amfdr:dataClasses:dataInstances:values:datas:error:local:].cold.17
+ -[CRFDRSeal patchWithOptions:amfdr:dataClasses:dataInstances:values:datas:error:local:].cold.2
+ -[CRFDRSeal patchWithOptions:amfdr:dataClasses:dataInstances:values:datas:error:local:].cold.3
+ -[CRFDRSeal patchWithOptions:amfdr:dataClasses:dataInstances:values:datas:error:local:].cold.4
+ -[CRFDRSeal patchWithOptions:amfdr:dataClasses:dataInstances:values:datas:error:local:].cold.5
+ -[CRFDRSeal patchWithOptions:amfdr:dataClasses:dataInstances:values:datas:error:local:].cold.6
+ -[CRFDRSeal patchWithOptions:amfdr:dataClasses:dataInstances:values:datas:error:local:].cold.7
+ -[CRFDRSeal patchWithOptions:amfdr:dataClasses:dataInstances:values:datas:error:local:].cold.8
+ -[CRFDRSeal patchWithOptions:amfdr:dataClasses:dataInstances:values:datas:error:local:].cold.9
+ -[CRFDRSeal performHTTPChallengeClaim:fdrLocal:fdrError:claimClassDict:registerOnly:]
+ -[CRFDRSeal performHTTPChallengeClaim:fdrLocal:fdrError:claimClassDict:registerOnly:].cold.1
+ -[CRFDRSeal performHTTPChallengeClaim:fdrLocal:fdrError:claimClassDict:registerOnly:].cold.2
+ -[CRFDRSeal performHTTPChallengeClaim:fdrLocal:fdrError:claimClassDict:registerOnly:].cold.3
+ -[CRFDRSeal performHTTPChallengeClaim:fdrLocal:fdrError:claimClassDict:registerOnly:].cold.4
+ -[CRFDRSeal performHTTPChallengeClaim:fdrLocal:fdrError:claimClassDict:registerOnly:].cold.5
+ -[CRFDRSeal prefetchPermissionsForSealing:fdrRemote:fdrLocal:claimClassDict:makeClasses:makeInstances:patchClasses:patchInstances:]
+ -[CRFDRSeal prefetchPermissionsWith:returnError:]
+ -[CRFDRSeal recoverDataClasses]
+ -[CRFDRSeal recoverDataInstances]
+ -[CRFDRSeal registerChangeForComponent:fdrError:]
+ -[CRFDRSeal registerChangeForComponent:fdrError:].cold.1
+ -[CRFDRSeal remotePatch:dataClasses:dataInstances:values:datas:error:]
+ -[CRFDRSeal seal:oldSealingManifest:newSealingManifest:stats:]
+ -[CRFDRSeal seal:oldSealingManifest:newSealingManifest:stats:].cold.1
+ -[CRFDRSeal sealWithDataClass:fdrError:registerOnly:]
+ -[CRFDRSeal sealWithDataClass:fdrError:registerOnly:].cold.1
+ -[CRFDRSeal sealWithDataClass:fdrError:registerOnly:].cold.10
+ -[CRFDRSeal sealWithDataClass:fdrError:registerOnly:].cold.11
+ -[CRFDRSeal sealWithDataClass:fdrError:registerOnly:].cold.12
+ -[CRFDRSeal sealWithDataClass:fdrError:registerOnly:].cold.13
+ -[CRFDRSeal sealWithDataClass:fdrError:registerOnly:].cold.14
+ -[CRFDRSeal sealWithDataClass:fdrError:registerOnly:].cold.15
+ -[CRFDRSeal sealWithDataClass:fdrError:registerOnly:].cold.16
+ -[CRFDRSeal sealWithDataClass:fdrError:registerOnly:].cold.2
+ -[CRFDRSeal sealWithDataClass:fdrError:registerOnly:].cold.3
+ -[CRFDRSeal sealWithDataClass:fdrError:registerOnly:].cold.4
+ -[CRFDRSeal sealWithDataClass:fdrError:registerOnly:].cold.5
+ -[CRFDRSeal sealWithDataClass:fdrError:registerOnly:].cold.6
+ -[CRFDRSeal sealWithDataClass:fdrError:registerOnly:].cold.7
+ -[CRFDRSeal sealWithDataClass:fdrError:registerOnly:].cold.8
+ -[CRFDRSeal sealWithDataClass:fdrError:registerOnly:].cold.9
+ -[CRFDRSeal sealedDataInstance]
+ -[CRFDRSeal setAllowSelfService:]
+ -[CRFDRSeal setAllowUsedPart:]
+ -[CRFDRSeal setApTicketData:]
+ -[CRFDRSeal setClaimDict:]
+ -[CRFDRSeal setCurrentClasses:]
+ -[CRFDRSeal setCurrentInstances:]
+ -[CRFDRSeal setCurrentProperties:]
+ -[CRFDRSeal setDelegate:]
+ -[CRFDRSeal setFailedSPC:]
+ -[CRFDRSeal setHandler:]
+ -[CRFDRSeal setLocalAndRemotePermission:fdrRemote:]
+ -[CRFDRSeal setLocalAndRemotePermission:fdrRemote:].cold.1
+ -[CRFDRSeal setLocalAndRemotePermission:fdrRemote:].cold.2
+ -[CRFDRSeal setLocalAndRemotePermission:fdrRemote:].cold.3
+ -[CRFDRSeal setLocalAndRemoteTrustObject:fdrLocal:remoteTrustObjectDigest:fdrError:]
+ -[CRFDRSeal setLocalAndRemoteTrustObject:fdrLocal:remoteTrustObjectDigest:fdrError:].cold.1
+ -[CRFDRSeal setLocalAndRemoteTrustObject:fdrLocal:remoteTrustObjectDigest:fdrError:].cold.2
+ -[CRFDRSeal setLocalAndRemoteTrustObject:fdrLocal:remoteTrustObjectDigest:fdrError:].cold.3
+ -[CRFDRSeal setMakeClasses:]
+ -[CRFDRSeal setMakeInstances:]
+ -[CRFDRSeal setMakeProperties:]
+ -[CRFDRSeal setMergedDataClasses:]
+ -[CRFDRSeal setMergedDataInstances:]
+ -[CRFDRSeal setMinimalSealedClasses:]
+ -[CRFDRSeal setMinimalSealedInstances:]
+ -[CRFDRSeal setMinimalSealedVersions:]
+ -[CRFDRSeal setMinimalSealingInstances:]
+ -[CRFDRSeal setPartSPC:]
+ -[CRFDRSeal setPatchDataClasses:]
+ -[CRFDRSeal setPatchDataInstances:]
+ -[CRFDRSeal setPatchItems:]
+ -[CRFDRSeal setPatchValues:]
+ -[CRFDRSeal setRecoverDataClasses:]
+ -[CRFDRSeal setRecoverDataInstances:]
+ -[CRFDRSeal setSealedDataInstance:]
+ -[CRFDRSeal setSkipStageEAN:]
+ -[CRFDRSeal setUpdateClassDict:]
+ -[CRFDRSeal setUpdateProperties:]
+ -[CRFDRSeal skipStageEAN]
+ -[CRFDRSeal summarizePatchInputs]
+ -[CRFDRSeal updateClassDict]
+ -[CRFDRSeal updateProperties]
+ -[CRFDRSeal verifyClaimCountAndSalesDistrictWithError:]
+ -[CRFDRSeal(RealSealing) performMake:fdrLocal:fdrError:]
+ -[CRFDRSeal(RealSealing) performMake:fdrLocal:fdrError:].cold.1
+ -[CRFDRSeal(RealSealing) performMake:fdrLocal:fdrError:].cold.2
+ -[CRFDRSeal(RealSealing) performMake:fdrLocal:fdrError:].cold.3
+ -[CRFDRSeal(RealSealing) performRealToRealRepair:fdrLocal:fdrRemote:]
+ -[CRFDRSeal(RealSealing) performRealToRealRepair:fdrLocal:fdrRemote:].cold.1
+ -[CRFDRSeal(RealSealing) performRealToRealRepair:fdrLocal:fdrRemote:].cold.2
+ -[CRFDRSeal(RealSealing) performRealToRealRepair:fdrLocal:fdrRemote:].cold.3
+ -[CRFDRSeal(RealSealing) performRealToRealRepair:fdrLocal:fdrRemote:].cold.4
+ -[CRFDRSeal(RealSealing) performRealToRealRepair:fdrLocal:fdrRemote:].cold.5
+ -[CRFDRSeal(RealSealing) performRealToRealRepair:fdrLocal:fdrRemote:].cold.6
+ -[CRFDRSeal(RealSealing) performRealToRealRepair:fdrLocal:fdrRemote:].cold.7
+ -[CRFDRSeal(RealSealing) performRealToRealRepair:fdrLocal:fdrRemote:].cold.8
+ -[CRFDRSeal(RealSealing) performRealToRealRepair:fdrLocal:fdrRemote:].cold.9
+ -[CRFDRSeal(RealSealing) performSealing:fdrLocal:fdrError:]
+ -[CRFDRSeal(RealSealing) performSealing:fdrLocal:fdrError:].cold.1
+ -[CRFDRSeal(RealSealing) performStagedToRealRepair:fdrLocal:fdrRemote:]
+ -[CRFDRSeal(RealSealing) performStagedToRealRepair:fdrLocal:fdrRemote:].cold.1
+ -[CRFDRSeal(RealSealing) performStagedToRealRepair:fdrLocal:fdrRemote:].cold.10
+ -[CRFDRSeal(RealSealing) performStagedToRealRepair:fdrLocal:fdrRemote:].cold.11
+ -[CRFDRSeal(RealSealing) performStagedToRealRepair:fdrLocal:fdrRemote:].cold.12
+ -[CRFDRSeal(RealSealing) performStagedToRealRepair:fdrLocal:fdrRemote:].cold.2
+ -[CRFDRSeal(RealSealing) performStagedToRealRepair:fdrLocal:fdrRemote:].cold.3
+ -[CRFDRSeal(RealSealing) performStagedToRealRepair:fdrLocal:fdrRemote:].cold.4
+ -[CRFDRSeal(RealSealing) performStagedToRealRepair:fdrLocal:fdrRemote:].cold.5
+ -[CRFDRSeal(RealSealing) performStagedToRealRepair:fdrLocal:fdrRemote:].cold.6
+ -[CRFDRSeal(RealSealing) performStagedToRealRepair:fdrLocal:fdrRemote:].cold.7
+ -[CRFDRSeal(RealSealing) performStagedToRealRepair:fdrLocal:fdrRemote:].cold.8
+ -[CRFDRSeal(RealSealing) performStagedToRealRepair:fdrLocal:fdrRemote:].cold.9
+ -[CRFDRSeal(StagedSealing) performRealToStagedRepair:fdrLocal:fdrRemote:]
+ -[CRFDRSeal(StagedSealing) performRealToStagedRepair:fdrLocal:fdrRemote:].cold.1
+ -[CRFDRSeal(StagedSealing) performRealToStagedRepair:fdrLocal:fdrRemote:].cold.10
+ -[CRFDRSeal(StagedSealing) performRealToStagedRepair:fdrLocal:fdrRemote:].cold.2
+ -[CRFDRSeal(StagedSealing) performRealToStagedRepair:fdrLocal:fdrRemote:].cold.3
+ -[CRFDRSeal(StagedSealing) performRealToStagedRepair:fdrLocal:fdrRemote:].cold.4
+ -[CRFDRSeal(StagedSealing) performRealToStagedRepair:fdrLocal:fdrRemote:].cold.5
+ -[CRFDRSeal(StagedSealing) performRealToStagedRepair:fdrLocal:fdrRemote:].cold.6
+ -[CRFDRSeal(StagedSealing) performRealToStagedRepair:fdrLocal:fdrRemote:].cold.7
+ -[CRFDRSeal(StagedSealing) performRealToStagedRepair:fdrLocal:fdrRemote:].cold.8
+ -[CRFDRSeal(StagedSealing) performRealToStagedRepair:fdrLocal:fdrRemote:].cold.9
+ -[CRFDRSeal(StagedSealing) performStagedChallengeClaim:fdrLocal:fdrError:claimClassDict:]
+ -[CRFDRSeal(StagedSealing) performStagedChallengeClaim:fdrLocal:fdrError:claimClassDict:].cold.1
+ -[CRFDRSeal(StagedSealing) performStagedMake:fdrLocal:fdrError:]
+ -[CRFDRSeal(StagedSealing) performStagedMake:fdrLocal:fdrError:].cold.1
+ -[CRFDRSeal(StagedSealing) performStagedMake:fdrLocal:fdrError:].cold.2
+ -[CRFDRSeal(StagedSealing) performStagedSealing:fdrLocal:fdrError:]
+ -[CRFDRSeal(StagedSealing) performStagedSealing:fdrLocal:fdrError:].cold.1
+ -[CRFDRSeal(StagedSealing) performStagedSealing:fdrLocal:fdrError:].cold.2
+ -[CRFDRSeal(StagedSealing) performStagedToStagedRepair:fdrLocal:fdrRemote:]
+ -[CRFDRSeal(StagedSealing) performStagedToStagedRepair:fdrLocal:fdrRemote:].cold.1
+ -[CRFDRSeal(StagedSealing) performStagedToStagedRepair:fdrLocal:fdrRemote:].cold.2
+ -[CRFDRSeal(StagedSealing) performStagedToStagedRepair:fdrLocal:fdrRemote:].cold.3
+ -[CRFDRSeal(StagedSealing) performStagedToStagedRepair:fdrLocal:fdrRemote:].cold.4
+ -[CRFDRSeal(StagedSealing) performStagedToStagedRepair:fdrLocal:fdrRemote:].cold.5
+ -[CRFDRSeal(StagedSealing) performStagedToStagedRepair:fdrLocal:fdrRemote:].cold.6
+ -[CRFDRSeal(StagedSealing) prefetchPermissionsForStagedSealing:fdrRemote:fdrLocal:claimClassDict:makeClasses:makeInstances:patchClasses:patchInstances:]
+ -[CRFDRSeal(StagedSealing) prefetchPermissionsForStagedSealing:fdrRemote:fdrLocal:claimClassDict:makeClasses:makeInstances:patchClasses:patchInstances:].cold.1
+ -[CRFDRSeal(StagedSealing) prefetchPermissionsForStagedSealing:fdrRemote:fdrLocal:claimClassDict:makeClasses:makeInstances:patchClasses:patchInstances:].cold.2
+ -[CRFDRSeal(StagedSealing) prefetchPermissionsForStagedSealing:fdrRemote:fdrLocal:claimClassDict:makeClasses:makeInstances:patchClasses:patchInstances:].cold.3
+ -[CRFDRSeal(StagedSealing) prefetchPermissionsForStagedSealing:fdrRemote:fdrLocal:claimClassDict:makeClasses:makeInstances:patchClasses:patchInstances:].cold.4
+ -[CRFDRSeal(StagedSealing) prefetchPermissionsForStagedSealing:fdrRemote:fdrLocal:claimClassDict:makeClasses:makeInstances:patchClasses:patchInstances:].cold.5
+ -[CRFDRSeal(StagedSealing) prefetchPermissionsForStagedSealing:fdrRemote:fdrLocal:claimClassDict:makeClasses:makeInstances:patchClasses:patchInstances:].cold.6
+ -[CRFDRSeal(StagedSealing) stageDataClasses:dataInstances:fdrRemote:fdrLocal:fdrError:]
+ -[CRFDRSeal(StagedSealing) stageDataClasses:dataInstances:fdrRemote:fdrLocal:fdrError:].cold.1
+ -[CRFDRSeal(StagedSealing) stageDataClasses:dataInstances:fdrRemote:fdrLocal:fdrError:].cold.2
+ -[CRFDRSeal(StagedSealing) stageDataClasses:dataInstances:fdrRemote:fdrLocal:fdrError:].cold.3
+ -[CRFDRSeal(StagedSealing) stageDataClasses:dataInstances:fdrRemote:fdrLocal:fdrError:].cold.4
+ -[CRFDRiPad1DeviceHandler _addAlsCToMutableArrayWithPartSPC:dataClasses:dataInstances:error:]
+ -[CRFDRiPad1DeviceHandler _addAlsCToMutableArrayWithPartSPC:dataClasses:dataInstances:error:].cold.1
+ -[CRFDRiPad1DeviceHandler _addAlsCToMutableArrayWithPartSPC:dataClasses:dataInstances:error:].cold.2
+ -[CRFDRiPad1DeviceHandler _addHmCAToMutableArrayWithFdrRemote:dataClasses:dataInstances:error:]
+ -[CRFDRiPad1DeviceHandler _addHmCAToMutableArrayWithFdrRemote:dataClasses:dataInstances:error:].cold.1
+ -[CRFDRiPad1DeviceHandler _hasALSOnDisplay]
+ -[CRFDRiPad1DeviceHandler _hasRearALS]
+ -[CRFDRiPad1DeviceHandler copyWithZone:]
+ -[CRFDRiPad1DeviceHandler getClaimDataClassesAndInstancesWithPartSPC:withError:]
+ -[CRFDRiPad1DeviceHandler getClaimDataClassesAndInstancesWithPartSPC:withError:].cold.1
+ -[CRFDRiPad1DeviceHandler getMakeDataClassesAndInstancesWithPartSPC:fdrRemote:makeClasses:makeInstances:makePropertiesDict:fdrError:]
+ -[CRFDRiPad1DeviceHandler getMakeDataClassesAndInstancesWithPartSPC:fdrRemote:makeClasses:makeInstances:makePropertiesDict:fdrError:].cold.1
+ -[CRFDRiPad1DeviceHandler getMakeDataClassesAndInstancesWithPartSPC:fdrRemote:makeClasses:makeInstances:makePropertiesDict:fdrError:].cold.2
+ -[CRFDRiPad1DeviceHandler getMakeDataClassesAndInstancesWithPartSPC:fdrRemote:makeClasses:makeInstances:makePropertiesDict:fdrError:].cold.3
+ -[CRFDRiPad1DeviceHandler getMakeDataClassesAndInstancesWithPartSPC:fdrRemote:makeClasses:makeInstances:makePropertiesDict:fdrError:].cold.4
+ -[CRFDRiPad1DeviceHandler getMakeDataClassesAndInstancesWithPartSPC:fdrRemote:makeClasses:makeInstances:makePropertiesDict:fdrError:].cold.5
+ -[CRFDRiPad1DeviceHandler getMakeDataClassesAndInstancesWithPartSPC:fdrRemote:makeClasses:makeInstances:makePropertiesDict:fdrError:].cold.6
+ -[CRFDRiPad1DeviceHandler getMakeDataClassesAndInstancesWithPartSPC:fdrRemote:makeClasses:makeInstances:makePropertiesDict:fdrError:].cold.7
+ -[CRFDRiPad1DeviceHandler getMakeDataClassesAndInstancesWithPartSPC:fdrRemote:makeClasses:makeInstances:makePropertiesDict:fdrError:].cold.8
+ -[CRFDRiPad1DeviceHandler getPatchInfoPerSPC]
+ -[CRFDRiPad1DeviceHandler getUpdateDataClassesAndInstancesWithPartSPC:withError:]
+ -[CRFDRiPad1DeviceHandler getUpdateDataClassesAndInstancesWithPartSPC:withError:].cold.1
+ -[CRFDRiPad1DeviceHandler init]
+ -[CRFDRiPad1DeviceHandler spcWithComponent:withIdentifier:]
+ -[CRFDRiPad1DeviceHandler spcWithComponent:withIdentifier:].cold.1
+ -[CRFDRiPad1DeviceHandler supportMesaRepair]
+ -[CRFDRiPad1DeviceHandler supportPatch]
+ -[CRFaceIDStatus copyComponentStatus]
+ -[CRFaceIDStatus init]
+ -[CRFaceIDStatus isComponentFailed]
+ -[CRFileSystemController .cxx_destruct]
+ -[CRFileSystemController _init]
+ -[CRFileSystemController _init].cold.1
+ -[CRFileSystemController cleanupFileSystemForRepair]
+ -[CRFileSystemController cleanupFileSystemForRepair].cold.1
+ -[CRFileSystemController clearRepairBackup:]
+ -[CRFileSystemController clearRepairBackup:].cold.1
+ -[CRFileSystemController commitToFileSystem]
+ -[CRFileSystemController commitToFileSystem].cold.1
+ -[CRFileSystemController init]
+ -[CRFileSystemController setupAlternativeFDRPath:]
+ -[CRFileSystemController setupAlternativeFDRPath:].cold.1
+ -[CRFileSystemController setupAlternativeFDRPath:].cold.2
+ -[CRFileSystemController setupAlternativeFDRPath:].cold.3
+ -[CRFileSystemController setupAlternativeFDRPath:].cold.4
+ -[CRFileSystemController setupAlternativeFDRPath:].cold.5
+ -[CRFileSystemController setupAlternativeFDRPath:].cold.6
+ -[CRFileSystemController setupAlternativeFDRPath:].cold.7
+ -[CRFileSystemController setupFileSystemForRepair]
+ -[CRFileSystemController setupFileSystemForRepair].cold.1
+ -[CRFileSystemController setupFileSystemForRepair].cold.2
+ -[CRFileSystemController setupFileSystemForRepair].cold.3
+ -[CRFileSystemController syncAlternativeFDRPath]
+ -[CRFileSystemController syncAlternativeFDRPath].cold.1
+ -[CRFileSystemController syncAlternativeFDRPath].cold.2
+ -[CRFileSystemController syncAlternativeFDRPath].cold.3
+ -[CRFileSystemController syncAlternativeFDRPath].cold.4
+ -[CRFileSystemController syncAlternativeFDRPath].cold.5
+ -[CRFileSystemController syncFDRDataAtPath:toPath:]
+ -[CRMesaController clearPhysicalPresence]
+ -[CRMesaController clearPhysicalPresence].cold.1
+ -[CRMesaController isPaired:]
+ -[CRMesaController isPaired:].cold.1
+ -[CRMesaController isPhysicalPresenceAsserted]
+ -[CRMesaController isPhysicalPresenceAsserted].cold.1
+ -[CRNFCStatus copyComponentStatus]
+ -[CRNFCStatus init]
+ -[CRNFCStatus isComponentFailed]
+ -[CRPearlController _copyCombinedFDRData:withError:]
+ -[CRPearlController decompressPearlFrames]
+ -[CRPearlController decompressPearlFrames].cold.1
+ -[CRPearlController updateBrunorDATFirmware]
+ -[CRPearlController updateSavageDATFirmware]
+ -[CRPearlController updateSavageDATFirmware].cold.1
+ -[CRPearlController updateSavageDATFirmware].cold.2
+ -[CRPearlController verifyPSD3]
+ -[CRPersonalizationElement .cxx_destruct]
+ -[CRPersonalizationElement data]
+ -[CRPersonalizationElement elementId]
+ -[CRPersonalizationElement initWithID:param:requestFunction:responseFunction:]
+ -[CRPersonalizationElement init]
+ -[CRPersonalizationElement param]
+ -[CRPersonalizationElement personalizationMeasurementCreator]
+ -[CRPersonalizationElement personalizationResponseParser]
+ -[CRPersonalizationElement setData:]
+ -[CRPersonalizationElement setElementId:]
+ -[CRPersonalizationElement setParam:]
+ -[CRPersonalizationElement setPersonalizationMeasurementCreator:]
+ -[CRPersonalizationElement setPersonalizationResponseParser:]
+ -[CRPersonalizationManager .cxx_destruct]
+ -[CRPersonalizationManager AddResponseTicketForSavageUpdaterOptions:auth:error:]
+ -[CRPersonalizationManager _init:]
+ -[CRPersonalizationManager _init:].cold.1
+ -[CRPersonalizationManager _init:].cold.2
+ -[CRPersonalizationManager _init:].cold.3
+ -[CRPersonalizationManager _personalizeWithElement:useCache:parsedResponseData:error:]
+ -[CRPersonalizationManager _personalizeWithElement:useCache:parsedResponseData:error:].cold.1
+ -[CRPersonalizationManager addCustomPersonalizationElementWithId:personalizationElement:error:]
+ -[CRPersonalizationManager addCustomPersonalizationElementWithId:personalizationElement:error:].cold.1
+ -[CRPersonalizationManager addCustomPersonalizationElementWithId:personalizationElement:error:].cold.2
+ -[CRPersonalizationManager getApTicketForLthTransferWithOptions:apTicketData:error:]
+ -[CRPersonalizationManager getApTicketForSeaCookiePairingWithOptions:pairingTicket:error:]
+ -[CRPersonalizationManager getBMUTicketForVeridianFWUpdateWithOptions:BMUTicket:error:]
+ -[CRPersonalizationManager getPDIAPTicketUsingCache:apTicketData:error:]
+ -[CRPersonalizationManager getRemoteTrustObjectDigestWithExistedDigest:digestData:error:]
+ -[CRPersonalizationManager getRepairTicket:error:]
+ -[CRPersonalizationManager getSavageTicketForSavageFWUpdateWithOptions:SavageTicket:error:]
+ -[CRPersonalizationManager getYonkersTicketForYonkersFWUpdateWithOptions:YonkersTicket:error:]
+ -[CRPersonalizationManager init]
+ -[CRPersonalizationManager personalizeVeridianWithError:parsedResponseData:]
+ -[CRPersonalizationManager personalizeVeridianWithError:parsedResponseData:].cold.1
+ -[CRPersonalizationManager personalizeWithElements:error:]
+ -[CRPersonalizationManager personalizeWithElements:error:].cold.1
+ -[CRPersonalizationManager personalizeWithElements:error:].cold.2
+ -[CRPersonalizationManager personalizeWithElements:error:].cold.3
+ -[CRPersonalizationManager personalizeWithElements:error:].cold.4
+ -[CRPersonalizationManager personalizeWithElements:error:].cold.5
+ -[CRPreflight _getVersionInfo:]
+ -[CRPreflight _getVersionInfo:].cold.1
+ -[CRPreflight _getVersionInfo:].cold.2
+ -[CRPreflight _getVersionInfo:].cold.3
+ -[CRPreflight _sendBAARequest:proxySettings:withError:]
+ -[CRPreflight _sendBAARequest:proxySettings:withError:].cold.1
+ -[CRPreflight challengeStrongComponents:withReply:]
+ -[CRPreflight challengeStrongComponents:withReply:].cold.1
+ -[CRPreflight issueRepairCert:withReply:]
+ -[CRPreflight queryRepairDeltaWithReply:]
+ -[CRPreflight queryRepairDeltaWithReply:].cold.1
+ -[CRPreflight queryRepairDeltaWithReply:].cold.2
+ -[CRPreflight requestBAACertificates:apticket:proxySettings:withError:]
+ -[CRPreflight requestBAACertificates:apticket:proxySettings:withError:].cold.1
+ -[CRPreflight requestBAACertificates:apticket:proxySettings:withError:].cold.2
+ -[CRPreflight requestBAACertificates:apticket:proxySettings:withError:].cold.3
+ -[CRPreflight requestBAACertificates:apticket:proxySettings:withError:].cold.4
+ -[CRPreflight sha256Data:]
+ -[CRPreflight sign:keyBlob:]
+ -[CRPreflight sign:keyBlob:].cold.1
+ -[CRPreflight sign:keyBlob:].cold.2
+ -[CRPreflight sign:keyBlob:].cold.3
+ -[CRPreflight sign:keyBlob:].cold.4
+ -[CRPreflight verify:signature:keyBlob:]
+ -[CRPreflight verify:signature:keyBlob:].cold.1
+ -[CRPreflight verify:signature:keyBlob:].cold.2
+ -[CRPreflight verify:signature:keyBlob:].cold.3
+ -[CRPreflightController .cxx_destruct]
+ -[CRPreflightController challengeStrongComponents:responses:error:]
+ -[CRPreflightController components:withState:]
+ -[CRPreflightController connectionToService]
+ -[CRPreflightController createPEMFromCerts:]
+ -[CRPreflightController deltaComponents:strongComponents:error:]
+ -[CRPreflightController deltaComponents:strongComponents:error:].cold.1
+ -[CRPreflightController deltaComponents:strongComponents:error:].cold.2
+ -[CRPreflightController deltaComponents:strongComponents:error:].cold.3
+ -[CRPreflightController filteredPhase2Components:response:]
+ -[CRPreflightController getSupportedStrongComponents]
+ -[CRPreflightController isErrorResponse:]
+ -[CRPreflightController isErrorResponse:].cold.1
+ -[CRPreflightController isErrorResponse:].cold.2
+ -[CRPreflightController issueRepairCert:keyBlob:error:]
+ -[CRPreflightController miniPreflight]
+ -[CRPreflightController preflight:withReply:]
+ -[CRPreflightController preflightPhase1:withReply:]
+ -[CRPreflightController preflightPhase1:withReply:].cold.1
+ -[CRPreflightController preflightPhase1:withReply:].cold.2
+ -[CRPreflightController preflightPhase1:withReply:].cold.3
+ -[CRPreflightController preflightPhase1:withReply:].cold.4
+ -[CRPreflightController preflightPhase2:withReply:]
+ -[CRPreflightController preflightPhase2:withReply:].cold.1
+ -[CRPreflightController preflightPhase2:withReply:].cold.2
+ -[CRPreflightController preflightPhase2:withReply:].cold.3
+ -[CRPreflightController preflightPhase2:withReply:].cold.4
+ -[CRPreflightController preflightPhase2:withReply:].cold.5
+ -[CRPreflightController preflightPhase2:withReply:].cold.6
+ -[CRPreflightController queryRepairDelta:error:]
+ -[CRPreflightController sendRequest:keyBlob:error:]
+ -[CRPreflightController setComponentsState:withResponseDetails:]
+ -[CRPreflightController setComponentsState:withResponseDetails:].cold.1
+ -[CRPreflightController setComponentsState:withResponseDetails:].cold.2
+ -[CRPreflightController setConnectionToService:]
+ -[CRPreflightController setMiniPreflight:]
+ -[CRPreflightController setSocksHost:]
+ -[CRPreflightController setSocksPort:]
+ -[CRPreflightController sign:keyBlob:]
+ -[CRPreflightController socksHost]
+ -[CRPreflightController socksPort]
+ -[CRPreflightController verify:signature:keyBlob:]
+ -[CRPreflightHelper challengeStrongComponents:withReply:]
+ -[CRPreflightHelper issueRepairCert:withReply:]
+ -[CRPreflightHelper queryRepairDeltaWithReply:]
+ -[CRPreflightHelper sign:keyBlob:withReply:]
+ -[CRPreflightHelper verify:signature:keyBlob:withReply:]
+ -[CRPreflightRequest .cxx_destruct]
+ -[CRPreflightRequest activationResponses]
+ -[CRPreflightRequest bikCertificate]
+ -[CRPreflightRequest componentResponses]
+ -[CRPreflightRequest components]
+ -[CRPreflightRequest description]
+ -[CRPreflightRequest init]
+ -[CRPreflightRequest payload]
+ -[CRPreflightRequest payload].cold.1
+ -[CRPreflightRequest phase]
+ -[CRPreflightRequest requestID]
+ -[CRPreflightRequest server]
+ -[CRPreflightRequest sessionID]
+ -[CRPreflightRequest setActivationResponses:]
+ -[CRPreflightRequest setBikCertificate:]
+ -[CRPreflightRequest setComponentResponses:]
+ -[CRPreflightRequest setComponents:]
+ -[CRPreflightRequest setPhase:]
+ -[CRPreflightRequest setRequestID:]
+ -[CRPreflightRequest setServer:]
+ -[CRPreflightRequest setSessionID:]
+ -[CRPreflightRequest setSignatureChallenge:]
+ -[CRPreflightRequest signatureChallenge]
+ -[CRPreflightRequestComponent .cxx_destruct]
+ -[CRPreflightRequestComponent asid]
+ -[CRPreflightRequestComponent identifier]
+ -[CRPreflightRequestComponent initWithComponentType:identifier:asid:]
+ -[CRPreflightRequestComponent setAsid:]
+ -[CRPreflightRequestComponent setIdentifier:]
+ -[CRPreflightRequestComponent setState:]
+ -[CRPreflightRequestComponent setType:]
+ -[CRPreflightRequestComponent state]
+ -[CRPreflightRequestComponent type]
+ -[CRPreflightResponse .cxx_destruct]
+ -[CRPreflightResponse activationChallenges]
+ -[CRPreflightResponse componentChallenges]
+ -[CRPreflightResponse description]
+ -[CRPreflightResponse details]
+ -[CRPreflightResponse errorCode]
+ -[CRPreflightResponse errorMessage]
+ -[CRPreflightResponse initWithDictionary:]
+ -[CRPreflightResponse rawResponse]
+ -[CRPreflightResponse requestID]
+ -[CRPreflightResponse sessionID]
+ -[CRPreflightResponse setActivationChallenges:]
+ -[CRPreflightResponse setComponentChallenges:]
+ -[CRPreflightResponse setDetails:]
+ -[CRPreflightResponse setErrorCode:]
+ -[CRPreflightResponse setErrorMessage:]
+ -[CRPreflightResponse setRawResponse:]
+ -[CRPreflightResponse setRequestID:]
+ -[CRPreflightResponse setSessionID:]
+ -[CRPreflightResponse setSignatureChallenge:]
+ -[CRPreflightResponse setSpecVersion:]
+ -[CRPreflightResponse setStatus:]
+ -[CRPreflightResponse signatureChallenge]
+ -[CRPreflightResponse specVersion]
+ -[CRPreflightResponse status]
+ -[CRRCamStatus copyComponentStatus]
+ -[CRRCamStatus getIORegComponentStatus]
+ -[CRRCamStatus getIORegComponentStatus].cold.1
+ -[CRRCamStatus init]
+ -[CRRCamStatus isComponentFailed]
+ -[CRRIK attestationBlob]
+ -[CRRIK attestationBlob].cold.1
+ -[CRRIK createWithKeyBlob:]
+ -[CRRIK createWithKeyBlob:].cold.1
+ -[CRRIK create]
+ -[CRRIK create].cold.1
+ -[CRRIK create].cold.2
+ -[CRRIK create].cold.3
+ -[CRRIK create].cold.4
+ -[CRRIK create].cold.5
+ -[CRRIK dealloc]
+ -[CRRIK initWithKeyBlob:]
+ -[CRRIK init]
+ -[CRRIK keyBlob]
+ -[CRRIK key]
+ -[CRRIK pubKeyBlob]
+ -[CRRIK purge]
+ -[CRRIK rk]
+ -[CRRIK setRk:]
+ -[CRRIK sign:]
+ -[CRRIK sign:].cold.1
+ -[CRRIK sign:].cold.2
+ -[CRRIK verify:signature:]
+ -[CRRIK verify:signature:].cold.1
+ -[CRRepairHistory .cxx_destruct]
+ -[CRRepairHistory CAABasedRepairDateForComponent:withHistory:]
+ -[CRRepairHistory CAABasedRepairForComponent:withHistory:]
+ -[CRRepairHistory RCHLBasedRepairDateForComponent:withHistory:]
+ -[CRRepairHistory _getClaimCountEnforceDate]
+ -[CRRepairHistory checkUsedStatusFor:withHistory:withClaimCount:]
+ -[CRRepairHistory deviceSupportsRepairBootIntent]
+ -[CRRepairHistory extractRCHLRepairHistoryAndClaimCount:]
+ -[CRRepairHistory extractRCHLRepairHistoryAndClaimCount:].cold.1
+ -[CRRepairHistory extractRCHLRepairHistory]
+ -[CRRepairHistory extractRepairCentersWithRCHLHistory:]
+ -[CRRepairHistory extractRepairHistoryAsDictionary]
+ -[CRRepairHistory extractRepairsAfterACRZWithHistory:]
+ -[CRRepairHistory findRCHLHistoryObjectForComponent:withHistory:]
+ -[CRRepairHistory getCAAForRepairHistoryWithCompletion:]
+ -[CRRepairHistory getRCHLComponentWithType:]
+ -[CRRepairHistory getRepairHistoryItemswithCAAHistory:]
+ -[CRRepairHistory getRepairHistoryMap]
+ -[CRRepairHistory getUseCountExceptionsWith:]
+ -[CRRepairHistory hasHadRCHLBasedRepairForComponent:withHistory:]
+ -[CRRepairHistory hasInvalidRCHL]
+ -[CRRepairHistory init]
+ -[CRRepairHistory isRCHLRepairHistoryDevice]
+ -[CRRepairHistory isRCHLRepairHistoryDevice].cold.1
+ -[CRRepairHistory isRCHLRepairHistoryDevice].cold.2
+ -[CRRepairHistory isSelfServiceSalesDistrict:]
+ -[CRRepairHistory isSupportedIPad]
+ -[CRRepairHistory rawRCHLBasedRepairDateForComponent:withHistory:]
+ -[CRRepairHistory repairCenterForComponent:withRCHLHistory:]
+ -[CRRepairHistory repairDateForComponent:withRCHLHistory:withCAAHistory:]
+ -[CRRepairHistoryItem .cxx_destruct]
+ -[CRRepairHistoryItem componentName]
+ -[CRRepairHistoryItem componentType]
+ -[CRRepairHistoryItem description]
+ -[CRRepairHistoryItem initWithComponentName:CRComponentType:isRepaired:isUsed:repairDate:]
+ -[CRRepairHistoryItem isRepaired]
+ -[CRRepairHistoryItem isUsed]
+ -[CRRepairHistoryItem repairDate]
+ -[CRRepairHistoryItem setComponentName:]
+ -[CRRepairHistoryItem setComponentType:]
+ -[CRRepairHistoryItem setIsRepaired:]
+ -[CRRepairHistoryItem setIsUsed:]
+ -[CRRepairHistoryItem setRepairDate:]
+ -[CRRepairReportItem .cxx_destruct]
+ -[CRRepairReportItem error]
+ -[CRRepairReportItem initWithName:]
+ -[CRRepairReportItem name]
+ -[CRRepairReportItem setError:]
+ -[CRRepairReportItem setName:]
+ -[CRRepairReportItem setStatusCode:]
+ -[CRRepairReportItem statusCode]
+ -[CRRepairReportItem withError:]
+ -[CRRepairReportItem withStatus:]
+ -[CRStrongComponent .cxx_destruct]
+ -[CRStrongComponent componentType]
+ -[CRStrongComponent description]
+ -[CRStrongComponent encodeWithCoder:]
+ -[CRStrongComponent fwVersion]
+ -[CRStrongComponent identifier]
+ -[CRStrongComponent initWithCoder:]
+ -[CRStrongComponent initWithComponentType:identifier:fwVersion:]
+ -[CRStrongComponent init]
+ -[CRStrongComponent setComponentType:]
+ -[CRStrongComponent setFwVersion:]
+ -[CRStrongComponent setIdentifier:]
+ -[CRSysConfig createStringForKey:]
+ -[CRSysConfig dataIsValid:length:]
+ -[CRSysConfig dataIsValid:length:].cold.1
+ -[CRSysConfig dataIsValid:length:].cold.2
+ -[CRSysConfig dataIsValid:length:].cold.3
+ -[CRSysConfig findEntry:key:]
+ -[CRSysConfig findEntry:key:].cold.1
+ -[CRSysConfig findEntry:key:].cold.2
+ -[CRSysConfig findSyscfgAccess]
+ -[CRSysConfig findSyscfgAccess].cold.1
+ -[CRSysConfig init]
+ -[CRSysConfig isADDASysCfgAccessType]
+ -[CRSysConfig readSystemConfigAll]
+ -[CRSysConfig readSystemConfigAll].cold.1
+ -[CRSysConfig readSystemConfigAll].cold.2
+ -[CRSysConfig readSystemConfigAll].cold.3
+ -[CRSysConfig readSystemConfigArea]
+ -[CRSysConfig readSystemConfigArea].cold.1
+ -[CRSysConfig readSystemConfigArea].cold.2
+ -[CRSysConfig readSystemConfigArea].cold.3
+ -[CRSysConfig setIsADDASysCfgAccessType:]
+ -[CRSysConfig setSyscfgAccess:]
+ -[CRSysConfig syscfgAccess]
+ -[CRSysConfig syscfgUpdate:key:buffer:length:]
+ -[CRSysConfig syscfgUpdate:key:buffer:length:].cold.1
+ -[CRSysConfig syscfgUpdate:key:buffer:length:].cold.2
+ -[CRSysConfig syscfgUpdate:key:buffer:length:].cold.3
+ -[CRSysConfig syscfgUpdate:key:buffer:length:].cold.4
+ -[CRSysConfig writeSystemConfig:inBuffer:]
+ -[CRSysConfig writeSystemConfig:inBuffer:].cold.1
+ -[CRSysConfig writeSystemConfig:inBuffer:].cold.2
+ -[CRSysConfig writeSystemConfig:inBuffer:].cold.3
+ -[CRSysConfig writeSystemConfig:inBuffer:].cold.4
+ -[CRSysConfig writeSystemConfig:inBuffer:].cold.5
+ -[CRSysConfig writeSystemConfig:inBuffer:].cold.6
+ -[CRTouchIDStatus _isLegacyMesaInInvalidState]
+ -[CRTouchIDStatus copyComponentStatus]
+ -[CRTouchIDStatus init]
+ -[CRTouchIDStatus isComponentFailed]
+ -[CRUWBStatus copyComponentStatus]
+ -[CRUWBStatus init]
+ -[CRUWBStatus isComponentFailed]
+ -[CRUserDefaults .cxx_destruct]
+ -[CRUserDefaults boolForKey:]
+ -[CRUserDefaults defaultValues]
+ -[CRUserDefaults dictionaryForKey:]
+ -[CRUserDefaults initWithSuiteName:]
+ -[CRUserDefaults initWithSuiteName:internalOnly:]
+ -[CRUserDefaults initWithSuiteName:internalOnly:].cold.1
+ -[CRUserDefaults objectForKey:]
+ -[CRUserDefaults setDefaultValues:]
+ -[CRUserDefaults setSuiteName:]
+ -[CRUserDefaults stringForKey:]
+ -[CRUserDefaults suiteName]
+ -[CRUtils base64Preprocess:]
+ -[CRUtils convertDataToHexInDictionary:]
+ -[CRUtils currentProcessHasEntitlement:]
+ -[CRUtils currentProcessHasEntitlement:].cold.1
+ -[CRUtils currentProcessHasEntitlement:].cold.2
+ -[CRUtils currentProcessHasEntitlement:].cold.3
+ -[CRUtils getAPTicket]
+ -[CRUtils getAPTicket].cold.1
+ -[CRUtils getAPTicket].cold.2
+ -[CRUtils getPathForApTicketWithError:]
+ -[CRUtils getPathForApTicketWithError:].cold.1
+ -[CRUtils getPathForBorsFirmwareWithError:]
+ -[CRUtils getPathForBrunorFirmwareWithError:]
+ -[CRUtils getPathForSavageFirmwareWithError:]
+ -[CRUtils getPathForYonkersFirmwareWithError:]
+ -[CRUtils hasEntitlementAATC]
+ -[CRUtils hasEntitlementBoolForTag:inAPTicket:]
+ -[CRUtils hasEntitlementBoolForTag:inAPTicket:].cold.1
+ -[CRUtils hasEntitlementBoolForTag:inAPTicket:].cold.2
+ -[CRUtils isHorizonRamdiskBootInApticket:]
+ -[CRUtils isHorizonRamdiskBootInApticket:].cold.1
+ -[CRUtils isHorizonRamdiskBootInApticket:].cold.2
+ -[CRUtils isHorizonRamdiskBootInApticket:].cold.3
+ -[CRVolumeButtonStatus copyComponentStatus]
+ -[CRVolumeButtonStatus init]
+ -[CRWifiStatus copyComponentStatus]
+ -[CRWifiStatus init]
+ -[CRWifiStatus isComponentFailed]
+ -[CoreRepairHelper _mount:withFlag:]
+ -[CoreRepairHelper challengeComponentsWith:withReply:]
+ -[CoreRepairHelper daemonControl:withReply:]
+ -[CoreRepairHelper decompressPearlFramesWithReply:]
+ -[CoreRepairHelper factoryServiceOn]
+ -[CoreRepairHelper getStrongComponentsWithReply:]
+ -[CoreRepairHelper init]
+ -[CoreRepairHelper seal:withReply:]
+ -[CoreRepairHelper seal:withReply:].cold.1
+ -[CoreRepairHelper seal:withReply:].cold.2
+ -[CoreRepairHelper seal:withReply:].cold.3
+ -[CoreRepairHelper seal:withReply:].cold.4
+ -[CoreRepairHelper seal:withReply:].cold.5
+ -[CoreRepairHelper setFactoryServiceOn:]
+ -[CoreRepairHelper setupModuleChallengeCallBack:]
+ -[CoreRepairHelper updateBrunorDATFirmwareWithReply:]
+ -[CoreRepairHelper updateSavageDATFirmwareWithReply:]
+ -[CoreRepairHelper verifyPSD3WithReply:]
+ -[NSData(Digest) SHA256DigestData]
+ -[NSData(Digest) SHA256DigestData].cold.1
+ -[NSData(Digest) SHA256DigestString]
+ -[NSData(Digest) SHA384DigestData]
+ -[NSData(Digest) SHA384DigestData].cold.1
+ -[NSData(HexString) convertToHexString]
+ -[NSDictionary(CRValidations) BOOLFromKey:defaultValue:failed:]
+ -[NSDictionary(CRValidations) BOOLFromRequiredKey:failed:]
+ -[NSDictionary(CRValidations) NSArrayFromKey:inSet:maxLength:defaultValue:failed:]
+ -[NSDictionary(CRValidations) NSArrayFromKey:types:maxLength:defaultValue:failed:]
+ -[NSDictionary(CRValidations) NSArrayFromKey:types:maxLength:defaultValue:failed:validator:]
+ -[NSDictionary(CRValidations) NSArrayFromRequiredKey:inSet:maxLength:failed:]
+ -[NSDictionary(CRValidations) NSArrayFromRequiredKey:types:maxLength:failed:]
+ -[NSDictionary(CRValidations) NSArrayFromRequiredKey:types:maxLength:failed:validator:]
+ -[NSDictionary(CRValidations) NSDataFromKey:defaultValue:failed:]
+ -[NSDictionary(CRValidations) NSDictionaryFromKey:defaultValue:failed:]
+ -[NSDictionary(CRValidations) NSDictionaryFromKey:limitedToKeys:defaultValue:failed:]
+ -[NSDictionary(CRValidations) NSDictionaryFromRequiredKey:failed:]
+ -[NSDictionary(CRValidations) NSDictionaryFromRequiredKey:limitedToKeys:failed:]
+ -[NSDictionary(CRValidations) NSNumberFromKey:lowerBound:upperBound:defaultValue:failed:]
+ -[NSDictionary(CRValidations) NSNumberFromRequiredKey:lowerBound:upperBound:failed:]
+ -[NSDictionary(CRValidations) NSSetFromKey:defaultValue:failed:]
+ -[NSDictionary(CRValidations) NSStringFromKey:defaultValue:failed:]
+ -[NSDictionary(CRValidations) NSStringFromKey:inSet:defaultValue:failed:]
+ -[NSDictionary(CRValidations) NSStringFromRequiredKey:inSet:failed:]
+ -[NSDictionary(CRValidations) NSStringFromRequiredKey:maxLength:failed:]
+ -[NSString(Digest) SHA256DigestData]
+ -[NSString(Digest) SHA256DigestString]
+ -[NSString(FDR) dataIdentifier]
+ -[NSString(FDR) dataIdentifier].cold.1
+ -[NSString(FDR) dataKey]
+ -[NSString(FDR) dataKey].cold.1
+ -[NSString(Utils) stringByStrippingPrefix:]
+ -[NSURL(Digest) SHA256DigestData]
+ -[NSURL(Digest) SHA256DigestData].cold.1
+ -[NSURL(Digest) SHA256DigestData].cold.2
+ -[NSURL(Digest) SHA256DigestString]
+ -[NSURL(Digest) SHA384DigestData]
+ -[NSURL(Digest) SHA384DigestData].cold.1
+ -[NSURL(Digest) SHA384DigestData].cold.2
+ <redacted>
+ GCC_except_table0
+ GCC_except_table1
+ GCC_except_table10
+ GCC_except_table13
+ GCC_except_table16
+ GCC_except_table17
+ GCC_except_table18
+ GCC_except_table2
+ GCC_except_table20
+ GCC_except_table22
+ GCC_except_table23
+ GCC_except_table26
+ GCC_except_table27
+ GCC_except_table3
+ GCC_except_table4
+ GCC_except_table5
+ GCC_except_table7
+ GCC_except_table8
+ _AMFDRSealedDataSetMinimalManifestClassInstanceWithVersions
+ _AMFDRSealingManifestCopyLocalDictForClass
+ _AMFDRSealingManifestCopyMinimalManifestClassesAndInstancesVersions
+ _AMFDRSealingMapSetKeyQueryRetry
+ _BlockedYonkersSPKI
+ _BlockedYonkers_spki
+ _CRGetRepairDate
+ _CRIsRepairAvailable
+ _CTOidAppleImg4Manifest
+ _CTParseCertificateSet
+ _CoreRepairCoreVersionNumber
+ _CoreRepairCoreVersionString
+ _CoreRepairFDRSignBattery
+ _CoreRepairFDRSignDisplay
+ _CoreRepairFDRSignPearl
+ _CoreRepairFDRSignVeridian
+ _CryptoBufferAllocate
+ _CryptoBufferAllocate.cold.1
+ _DERDecodeItem
+ _DERDecodeItemPartialBufferGetLength
+ _DERDecodeSeqContentInit
+ _DERDecodeSeqNext
+ _DERImg4CertificateItemSpecs
+ _DERImg4CompressionItemSpecs
+ _DERImg4Decode
+ _DERImg4DecodeCertificate
+ _DERImg4DecodeFindProperty
+ _DERImg4DecodeFindPropertyInSequence
+ _DERImg4DecodeManifest
+ _DERImg4DecodeManifestCommon
+ _DERImg4DecodeParseManifestProperties
+ _DERImg4DecodeParseManifestPropertiesInternal
+ _DERImg4DecodePayload
+ _DERImg4DecodePayloadCompression
+ _DERImg4DecodePayloadProperties
+ _DERImg4DecodePayloadWithProperties
+ _DERImg4DecodePropertyWithItem
+ _DERImg4DecodeRestoreInfo
+ _DERImg4DecodeTagCompare
+ _DERImg4DecodeUnsignedCertificate
+ _DERImg4DecodeUnsignedManifest
+ _DERImg4ItemSpecs
+ _DERImg4ManifestItemSpecs
+ _DERImg4PayloadItemSpecs
+ _DERImg4PayloadPropertiesItemSpecs
+ _DERImg4PayloadWithPropertiesItemSpecs
+ _DERImg4RestoreInfoItemSpecs
+ _DERImg4UnsignedManifestItemSpecs
+ _DERParseBoolean
+ _DERParseInteger
+ _DERParseInteger64
+ _DERParseSequenceContentToObject
+ _DERParseSequenceToObject
+ _Img4DecodeGetBooleanFromSection
+ _Img4DecodeGetIntegerFromSection
+ _Img4DecodeGetObjectProperty
+ _Img4DecodeGetObjectPropertyData
+ _Img4DecodeGetPayload
+ _Img4DecodeGetPropertyFromSection
+ _Img4DecodeInit
+ _Img4DecodeInitManifest
+ _Img4DecodeInitManifestCommon
+ _Img4DecodeSectionExists
+ _OBJC_CLASS_$_CRAttestationHelper
+ _OBJC_CLASS_$_CRBatteryController
+ _OBJC_CLASS_$_CRBootIntentController
+ _OBJC_CLASS_$_CRComponentBase
+ _OBJC_CLASS_$_CRComponentBatteryRoswell
+ _OBJC_CLASS_$_CRComponentDisplayRoswell
+ _OBJC_CLASS_$_CRComponentPearl
+ _OBJC_CLASS_$_CRComponentTsid
+ _OBJC_CLASS_$_CRComponentVeridian
+ _OBJC_CLASS_$_CRDaemonController
+ _OBJC_CLASS_$_CRDevice
+ _OBJC_CLASS_$_CRDeviceComponent
+ _OBJC_CLASS_$_CRDeviceMap
+ _OBJC_CLASS_$_CRFDRCompute1DeviceHandler
+ _OBJC_CLASS_$_CRFDRDisplay1DeviceHandler
+ _OBJC_CLASS_$_CRFDRGen1DeviceHandler
+ _OBJC_CLASS_$_CRFDRGen2DeviceHandler
+ _OBJC_CLASS_$_CRFDRGen3DeviceHandler
+ _OBJC_CLASS_$_CRFDRGen4DeviceHandler
+ _OBJC_CLASS_$_CRFDRGen5DeviceHandler
+ _OBJC_CLASS_$_CRFDRGen6DeviceHandler
+ _OBJC_CLASS_$_CRFDRGen7DeviceHandler
+ _OBJC_CLASS_$_CRFDRLegacy2DeviceHandler
+ _OBJC_CLASS_$_CRFDRLegacyDeviceHandler
+ _OBJC_CLASS_$_CRFDRRCHL
+ _OBJC_CLASS_$_CRFDRRetryController
+ _OBJC_CLASS_$_CRFDRiPad1DeviceHandler
+ _OBJC_CLASS_$_CRMesaController
+ _OBJC_CLASS_$_CRPatchUtils
+ _OBJC_CLASS_$_CRPreflight
+ _OBJC_CLASS_$_CRPreflightResponse
+ _OBJC_CLASS_$_CRRIK
+ _OBJC_CLASS_$_CRRepairHistoryItem
+ _OBJC_CLASS_$_CRRepairReportItem
+ _OBJC_CLASS_$_CRWiFiCredEncryption
+ _OBJC_CLASS_$_NSLock
+ _OBJC_IVAR_$_CRCAttestationManager.progress
+ _OBJC_IVAR_$_CRCCertificate.certifcateType
+ _OBJC_IVAR_$_CRCCertificate.certificates
+ _OBJC_IVAR_$_CRCCertificate.referenceKey
+ _OBJC_IVAR_$_CRChallengeObject.componentType
+ _OBJC_IVAR_$_CRChallengeObject.keyIndex
+ _OBJC_IVAR_$_CRChallengeObject.nonce
+ _OBJC_IVAR_$_CRChallengeObject.properties
+ _OBJC_IVAR_$_CRChallengeResponse.componentType
+ _OBJC_IVAR_$_CRChallengeResponse.identifier
+ _OBJC_IVAR_$_CRChallengeResponse.keyIndex
+ _OBJC_IVAR_$_CRChallengeResponse.properties
+ _OBJC_IVAR_$_CRChallengeResponse.signedResponse
+ _OBJC_IVAR_$_CRComponentAuth.componentName
+ _OBJC_IVAR_$_CRComponentBase.identifierBase64
+ _OBJC_IVAR_$_CRComponentBatteryRoswell.identifierBase64
+ _OBJC_IVAR_$_CRComponentDisplayRoswell.identifierBase64
+ _OBJC_IVAR_$_CRComponentPearl.identifierBase64
+ _OBJC_IVAR_$_CRComponentTsid.identifierBase64
+ _OBJC_IVAR_$_CRComponentVeridian.identifierBase64
+ _OBJC_IVAR_$_CRDevice._components
+ _OBJC_IVAR_$_CRDevice._spcToComponent
+ _OBJC_IVAR_$_CRDevice._supportElabel
+ _OBJC_IVAR_$_CRDevice._typeToComponent
+ _OBJC_IVAR_$_CRDeviceComponent._fdrKeys
+ _OBJC_IVAR_$_CRDeviceComponent._hasStrongIdentity
+ _OBJC_IVAR_$_CRDeviceComponent._locKey
+ _OBJC_IVAR_$_CRDeviceComponent._spc
+ _OBJC_IVAR_$_CRDeviceComponent._superModule
+ _OBJC_IVAR_$_CRDeviceComponent._type
+ _OBJC_IVAR_$_CREANController.apTicket
+ _OBJC_IVAR_$_CRFDRBaseDeviceHandler._KBBDataClasses
+ _OBJC_IVAR_$_CRFDRBaseDeviceHandler._KBBDataInstances
+ _OBJC_IVAR_$_CRFDRBaseDeviceHandler._KBBECID
+ _OBJC_IVAR_$_CRFDRBaseDeviceHandler._KBBSIK
+ _OBJC_IVAR_$_CRFDRBaseDeviceHandler._KBBSealInstance
+ _OBJC_IVAR_$_CRFDRBaseDeviceHandler._KBBSerialNumber
+ _OBJC_IVAR_$_CRFDRBaseDeviceHandler._KGBSerialNumber
+ _OBJC_IVAR_$_CRFDRBaseDeviceHandler._kbbCGSN
+ _OBJC_IVAR_$_CRFDRBaseDeviceHandler._kbbSealDate
+ _OBJC_IVAR_$_CRFDRBaseDeviceHandler._kbbSealingManifest
+ _OBJC_IVAR_$_CRFDRBaseDeviceHandler._previousCGSN
+ _OBJC_IVAR_$_CRFDRBaseDeviceHandler._sealDate
+ _OBJC_IVAR_$_CRFDRBaseDeviceHandler._updateProperties
+ _OBJC_IVAR_$_CRFDRBaseDeviceHandler.allowFactoryReset
+ _OBJC_IVAR_$_CRFDRBaseDeviceHandler.allowMissingData
+ _OBJC_IVAR_$_CRFDRBaseDeviceHandler.componentsMapping
+ _OBJC_IVAR_$_CRFDRBaseDeviceHandler.currentDataClasses
+ _OBJC_IVAR_$_CRFDRBaseDeviceHandler.currentDataInstances
+ _OBJC_IVAR_$_CRFDRBaseDeviceHandler.currentProperties
+ _OBJC_IVAR_$_CRFDRBaseDeviceHandler.isServicePart
+ _OBJC_IVAR_$_CRFDRBaseDeviceHandler.warnings
+ _OBJC_IVAR_$_CRFDRCompute1DeviceHandler.instance
+ _OBJC_IVAR_$_CRFDRCompute1DeviceHandler.liveChMf
+ _OBJC_IVAR_$_CRFDRCompute1DeviceHandler.strongComponents
+ _OBJC_IVAR_$_CRFDRDeviceController.handler
+ _OBJC_IVAR_$_CRFDRDisplay1DeviceHandler.KBBMLBSerialNumber
+ _OBJC_IVAR_$_CRFDRDisplay1DeviceHandler._KBBTransferProperties
+ _OBJC_IVAR_$_CRFDRRCHL._dataClasses
+ _OBJC_IVAR_$_CRFDRRCHL._properties
+ _OBJC_IVAR_$_CRFDRRCHL._repairCenter
+ _OBJC_IVAR_$_CRFDRRCHL._repairDate
+ _OBJC_IVAR_$_CRFDRRCHL._repairDateStr
+ _OBJC_IVAR_$_CRFDRRetryController._lock
+ _OBJC_IVAR_$_CRFDRRetryController._refCount
+ _OBJC_IVAR_$_CRFDRSeal.FDRCAURL
+ _OBJC_IVAR_$_CRFDRSeal.FDRDSURL
+ _OBJC_IVAR_$_CRFDRSeal.FDRPersistentDataPath
+ _OBJC_IVAR_$_CRFDRSeal.FDRSealingURL
+ _OBJC_IVAR_$_CRFDRSeal.KBBECID
+ _OBJC_IVAR_$_CRFDRSeal.KBBSIK
+ _OBJC_IVAR_$_CRFDRSeal.KBBSerialNumber
+ _OBJC_IVAR_$_CRFDRSeal.KGBSerialNumber
+ _OBJC_IVAR_$_CRFDRSeal.SOCKSHost
+ _OBJC_IVAR_$_CRFDRSeal.SOCKSPort
+ _OBJC_IVAR_$_CRFDRSeal._allowSelfService
+ _OBJC_IVAR_$_CRFDRSeal._allowUsedPart
+ _OBJC_IVAR_$_CRFDRSeal._claimDict
+ _OBJC_IVAR_$_CRFDRSeal._currentClasses
+ _OBJC_IVAR_$_CRFDRSeal._currentInstances
+ _OBJC_IVAR_$_CRFDRSeal._currentProperties
+ _OBJC_IVAR_$_CRFDRSeal._failedSPC
+ _OBJC_IVAR_$_CRFDRSeal._makeClasses
+ _OBJC_IVAR_$_CRFDRSeal._makeInstances
+ _OBJC_IVAR_$_CRFDRSeal._makeProperties
+ _OBJC_IVAR_$_CRFDRSeal._mergedDataClasses
+ _OBJC_IVAR_$_CRFDRSeal._mergedDataInstances
+ _OBJC_IVAR_$_CRFDRSeal._minimalSealedClasses
+ _OBJC_IVAR_$_CRFDRSeal._minimalSealedInstances
+ _OBJC_IVAR_$_CRFDRSeal._minimalSealedVersions
+ _OBJC_IVAR_$_CRFDRSeal._minimalSealingInstances
+ _OBJC_IVAR_$_CRFDRSeal._partSPC
+ _OBJC_IVAR_$_CRFDRSeal._patchDataClasses
+ _OBJC_IVAR_$_CRFDRSeal._patchDataInstances
+ _OBJC_IVAR_$_CRFDRSeal._patchItems
+ _OBJC_IVAR_$_CRFDRSeal._patchValues
+ _OBJC_IVAR_$_CRFDRSeal._recoverDataClasses
+ _OBJC_IVAR_$_CRFDRSeal._recoverDataInstances
+ _OBJC_IVAR_$_CRFDRSeal._sealedDataInstance
+ _OBJC_IVAR_$_CRFDRSeal._skipStageEAN
+ _OBJC_IVAR_$_CRFDRSeal._updateClassDict
+ _OBJC_IVAR_$_CRFDRSeal._updateProperties
+ _OBJC_IVAR_$_CRFDRSeal.apTicketData
+ _OBJC_IVAR_$_CRFDRSeal.currentMLBSerialNumber
+ _OBJC_IVAR_$_CRFDRSeal.currentSerialNumber
+ _OBJC_IVAR_$_CRFDRSeal.dataDirectoryURL
+ _OBJC_IVAR_$_CRFDRSeal.delegate
+ _OBJC_IVAR_$_CRFDRSeal.displayMaxDuration
+ _OBJC_IVAR_$_CRFDRSeal.doSeal
+ _OBJC_IVAR_$_CRFDRSeal.enableProxy
+ _OBJC_IVAR_$_CRFDRSeal.enableStagedSeal
+ _OBJC_IVAR_$_CRFDRSeal.handler
+ _OBJC_IVAR_$_CRFDRSeal.ignoreStagedData
+ _OBJC_IVAR_$_CRFDRSeal.isStagedSealed
+ _OBJC_IVAR_$_CRFDRSeal.keyBlob
+ _OBJC_IVAR_$_CRFDRSeal.manifestDataClassesAndInstances
+ _OBJC_IVAR_$_CRFDRSeal.metadataDict
+ _OBJC_IVAR_$_CRFDRSeal.overridePropertySet
+ _OBJC_IVAR_$_CRFDRSeal.postSealingManifest
+ _OBJC_IVAR_$_CRFDRSeal.preSealingManifest
+ _OBJC_IVAR_$_CRFDRSeal.removedProperties
+ _OBJC_IVAR_$_CRFDRSeal.repairStats
+ _OBJC_IVAR_$_CRFDRSeal.sealCount
+ _OBJC_IVAR_$_CRFDRSeal.trustObjectURL
+ _OBJC_IVAR_$_CRFileSystemController.activeFDRDataPathStr
+ _OBJC_IVAR_$_CRFileSystemController.alternativeFDRPathStr
+ _OBJC_IVAR_$_CRFileSystemController.alternativeFDRRealPathStr
+ _OBJC_IVAR_$_CRFileSystemController.defaultFDRPathStr
+ _OBJC_IVAR_$_CRFileSystemController.tmpFDRDataPathStr
+ _OBJC_IVAR_$_CRPersonalizationElement._data
+ _OBJC_IVAR_$_CRPersonalizationElement._elementId
+ _OBJC_IVAR_$_CRPersonalizationElement._param
+ _OBJC_IVAR_$_CRPersonalizationElement._personalizationMeasurementCreator
+ _OBJC_IVAR_$_CRPersonalizationElement._personalizationResponseParser
+ _OBJC_IVAR_$_CRPersonalizationManager.amai
+ _OBJC_IVAR_$_CRPersonalizationManager.personalizationMap
+ _OBJC_IVAR_$_CRPreflightController._connectionToService
+ _OBJC_IVAR_$_CRPreflightController._miniPreflight
+ _OBJC_IVAR_$_CRPreflightController._socksHost
+ _OBJC_IVAR_$_CRPreflightController._socksPort
+ _OBJC_IVAR_$_CRPreflightRequest._activationResponses
+ _OBJC_IVAR_$_CRPreflightRequest._bikCertificate
+ _OBJC_IVAR_$_CRPreflightRequest._componentResponses
+ _OBJC_IVAR_$_CRPreflightRequest._components
+ _OBJC_IVAR_$_CRPreflightRequest._phase
+ _OBJC_IVAR_$_CRPreflightRequest._requestID
+ _OBJC_IVAR_$_CRPreflightRequest._server
+ _OBJC_IVAR_$_CRPreflightRequest._sessionID
+ _OBJC_IVAR_$_CRPreflightRequest._signatureChallenge
+ _OBJC_IVAR_$_CRPreflightRequestComponent._asid
+ _OBJC_IVAR_$_CRPreflightRequestComponent._identifier
+ _OBJC_IVAR_$_CRPreflightRequestComponent._state
+ _OBJC_IVAR_$_CRPreflightRequestComponent._type
+ _OBJC_IVAR_$_CRPreflightResponse._activationChallenges
+ _OBJC_IVAR_$_CRPreflightResponse._componentChallenges
+ _OBJC_IVAR_$_CRPreflightResponse._details
+ _OBJC_IVAR_$_CRPreflightResponse._errorCode
+ _OBJC_IVAR_$_CRPreflightResponse._errorMessage
+ _OBJC_IVAR_$_CRPreflightResponse._rawResponse
+ _OBJC_IVAR_$_CRPreflightResponse._requestID
+ _OBJC_IVAR_$_CRPreflightResponse._sessionID
+ _OBJC_IVAR_$_CRPreflightResponse._signatureChallenge
+ _OBJC_IVAR_$_CRPreflightResponse._specVersion
+ _OBJC_IVAR_$_CRPreflightResponse._status
+ _OBJC_IVAR_$_CRRIK._rk
+ _OBJC_IVAR_$_CRRepairHistory.componentMap
+ _OBJC_IVAR_$_CRRepairHistory.repairHistoryMap
+ _OBJC_IVAR_$_CRRepairHistory.useCountExceptionKeys
+ _OBJC_IVAR_$_CRRepairHistoryItem._componentName
+ _OBJC_IVAR_$_CRRepairHistoryItem._componentType
+ _OBJC_IVAR_$_CRRepairHistoryItem._isRepaired
+ _OBJC_IVAR_$_CRRepairHistoryItem._isUsed
+ _OBJC_IVAR_$_CRRepairHistoryItem._repairDate
+ _OBJC_IVAR_$_CRRepairReportItem._error
+ _OBJC_IVAR_$_CRRepairReportItem._name
+ _OBJC_IVAR_$_CRRepairReportItem._statusCode
+ _OBJC_IVAR_$_CRStrongComponent.componentType
+ _OBJC_IVAR_$_CRStrongComponent.fwVersion
+ _OBJC_IVAR_$_CRStrongComponent.identifier
+ _OBJC_IVAR_$_CRSysConfig._isADDASysCfgAccessType
+ _OBJC_IVAR_$_CRSysConfig._syscfgAccess
+ _OBJC_IVAR_$_CRUserDefaults._defaultValues
+ _OBJC_IVAR_$_CRUserDefaults._suiteName
+ _OBJC_IVAR_$_CoreRepairHelper._factoryServiceOn
+ _OBJC_METACLASS_$_CRAttestationHelper
+ _OBJC_METACLASS_$_CRAudioCodecStatus
+ _OBJC_METACLASS_$_CRAudioStatus
+ _OBJC_METACLASS_$_CRBackGlassStatus
+ _OBJC_METACLASS_$_CRBasebandStatus
+ _OBJC_METACLASS_$_CRBatteryController
+ _OBJC_METACLASS_$_CRBatteryStatus
+ _OBJC_METACLASS_$_CRBluetoothStatus
+ _OBJC_METACLASS_$_CRBootIntentController
+ _OBJC_METACLASS_$_CRBootIntentHelper
+ _OBJC_METACLASS_$_CRCAttestationManager
+ _OBJC_METACLASS_$_CRCCertificate
+ _OBJC_METACLASS_$_CRCameraAuth
+ _OBJC_METACLASS_$_CRCameraAuthUsingProperty
+ _OBJC_METACLASS_$_CRChallengeObject
+ _OBJC_METACLASS_$_CRChallengeResponse
+ _OBJC_METACLASS_$_CRChassisController
+ _OBJC_METACLASS_$_CRComponentAuth
+ _OBJC_METACLASS_$_CRComponentBase
+ _OBJC_METACLASS_$_CRComponentBatteryRoswell
+ _OBJC_METACLASS_$_CRComponentDisplayRoswell
+ _OBJC_METACLASS_$_CRComponentPearl
+ _OBJC_METACLASS_$_CRComponentSigning
+ _OBJC_METACLASS_$_CRComponentTsid
+ _OBJC_METACLASS_$_CRComponentVeridian
+ _OBJC_METACLASS_$_CRCoverGlassStatus
+ _OBJC_METACLASS_$_CRDaemonController
+ _OBJC_METACLASS_$_CRDevice
+ _OBJC_METACLASS_$_CRDeviceComponent
+ _OBJC_METACLASS_$_CRDeviceMap
+ _OBJC_METACLASS_$_CRDisplayStatus
+ _OBJC_METACLASS_$_CREANController
+ _OBJC_METACLASS_$_CREnclosureStatus
+ _OBJC_METACLASS_$_CRFDRCompute1DeviceHandler
+ _OBJC_METACLASS_$_CRFDRDeviceController
+ _OBJC_METACLASS_$_CRFDRDisplay1DeviceHandler
+ _OBJC_METACLASS_$_CRFDRGen1DeviceHandler
+ _OBJC_METACLASS_$_CRFDRGen2DeviceHandler
+ _OBJC_METACLASS_$_CRFDRGen3DeviceHandler
+ _OBJC_METACLASS_$_CRFDRGen4DeviceHandler
+ _OBJC_METACLASS_$_CRFDRGen5DeviceHandler
+ _OBJC_METACLASS_$_CRFDRGen6DeviceHandler
+ _OBJC_METACLASS_$_CRFDRGen7DeviceHandler
+ _OBJC_METACLASS_$_CRFDRLegacy2DeviceHandler
+ _OBJC_METACLASS_$_CRFDRLegacyDeviceHandler
+ _OBJC_METACLASS_$_CRFDRRCHL
+ _OBJC_METACLASS_$_CRFDRRetryController
+ _OBJC_METACLASS_$_CRFDRSeal
+ _OBJC_METACLASS_$_CRFDRUtils
+ _OBJC_METACLASS_$_CRFDRiPad1DeviceHandler
+ _OBJC_METACLASS_$_CRFaceIDStatus
+ _OBJC_METACLASS_$_CRFileSystemController
+ _OBJC_METACLASS_$_CRLocalization
+ _OBJC_METACLASS_$_CRMesaController
+ _OBJC_METACLASS_$_CRNFCStatus
+ _OBJC_METACLASS_$_CRNVRAMController
+ _OBJC_METACLASS_$_CRPatchUtils
+ _OBJC_METACLASS_$_CRPearlController
+ _OBJC_METACLASS_$_CRPersonalizationElement
+ _OBJC_METACLASS_$_CRPersonalizationManager
+ _OBJC_METACLASS_$_CRPreflight
+ _OBJC_METACLASS_$_CRPreflightHelper
+ _OBJC_METACLASS_$_CRPreflightRequest
+ _OBJC_METACLASS_$_CRPreflightRequestComponent
+ _OBJC_METACLASS_$_CRPreflightResponse
+ _OBJC_METACLASS_$_CRPreflightUtils
+ _OBJC_METACLASS_$_CRRCamStatus
+ _OBJC_METACLASS_$_CRRIK
+ _OBJC_METACLASS_$_CRRepairHistoryItem
+ _OBJC_METACLASS_$_CRRepairReport
+ _OBJC_METACLASS_$_CRRepairReportItem
+ _OBJC_METACLASS_$_CRRepairStatusLite
+ _OBJC_METACLASS_$_CRStrongComponent
+ _OBJC_METACLASS_$_CRSysConfig
+ _OBJC_METACLASS_$_CRTouchIDStatus
+ _OBJC_METACLASS_$_CRUWBStatus
+ _OBJC_METACLASS_$_CRUserDefaults
+ _OBJC_METACLASS_$_CRUtils
+ _OBJC_METACLASS_$_CRVolumeButtonStatus
+ _OBJC_METACLASS_$_CRWiFiCredEncryption
+ _OBJC_METACLASS_$_CRWiFiCredentials
+ _OBJC_METACLASS_$_CRWifiStatus
+ _OSLogInit.onceToken
+ _OUTLINED_FUNCTION_0
+ _OUTLINED_FUNCTION_1
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_12
+ _OUTLINED_FUNCTION_13
+ _OUTLINED_FUNCTION_14
+ _OUTLINED_FUNCTION_15
+ _OUTLINED_FUNCTION_16
+ _OUTLINED_FUNCTION_17
+ _OUTLINED_FUNCTION_18
+ _OUTLINED_FUNCTION_19
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_21
+ _OUTLINED_FUNCTION_22
+ _OUTLINED_FUNCTION_23
+ _OUTLINED_FUNCTION_24
+ _OUTLINED_FUNCTION_25
+ _OUTLINED_FUNCTION_26
+ _OUTLINED_FUNCTION_27
+ _OUTLINED_FUNCTION_28
+ _OUTLINED_FUNCTION_29
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_30
+ _OUTLINED_FUNCTION_31
+ _OUTLINED_FUNCTION_32
+ _OUTLINED_FUNCTION_33
+ _OUTLINED_FUNCTION_34
+ _OUTLINED_FUNCTION_36
+ _OUTLINED_FUNCTION_38
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_40
+ _OUTLINED_FUNCTION_45
+ _OUTLINED_FUNCTION_49
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_59
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_7
+ _OUTLINED_FUNCTION_8
+ _OUTLINED_FUNCTION_9
+ _X509CertificateParse
+ _X509CertificateParseImplicit
+ _X509CertificateParseWithExtension
+ _X509CertificateVerifyOnlyOneAppleExtension
+ _X509ExtensionParseAppleExtension
+ _X509ExtensionParseAuthorityKeyIdentifier
+ _X509ExtensionParseBasicConstraints
+ _X509ExtensionParseCertifiedChipIntermediate
+ _X509ExtensionParseComponentAuth
+ _X509ExtensionParseDeviceAttestationIdentity
+ _X509ExtensionParseExtendedKeyUsage
+ _X509ExtensionParseGenericSSLMarker
+ _X509ExtensionParseKeyUsage
+ _X509ExtensionParseMFI4Properties
+ _X509ExtensionParseMFIAuthv3Leaf
+ _X509ExtensionParseMFISWAuth
+ _X509ExtensionParseServerAuthMarker
+ _X509ExtensionParseSubjectAltName
+ _X509ExtensionParseSubjectKeyIdentifier
+ _X509PolicyCheckForBlockedKeys
+ __OBJC_$_CATEGORY_CLASS_METHODS_NSData_$_HexString
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSDictionary_$_CRValidations
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSURL_$_Digest
+ __OBJC_$_CATEGORY_NSData_$_HexString
+ __OBJC_$_CATEGORY_NSDictionary_$_CRValidations
+ __OBJC_$_CATEGORY_NSString_$_FDR
+ __OBJC_$_CATEGORY_NSURL_$_Digest
+ __OBJC_$_CLASS_METHODS_CRAttestationHelper
+ __OBJC_$_CLASS_METHODS_CRBatteryController
+ __OBJC_$_CLASS_METHODS_CRBootIntentController
+ __OBJC_$_CLASS_METHODS_CRChallengeObject
+ __OBJC_$_CLASS_METHODS_CRChallengeResponse
+ __OBJC_$_CLASS_METHODS_CRComponentBase
+ __OBJC_$_CLASS_METHODS_CRComponentBatteryRoswell
+ __OBJC_$_CLASS_METHODS_CRComponentDisplayRoswell
+ __OBJC_$_CLASS_METHODS_CRComponentPearl
+ __OBJC_$_CLASS_METHODS_CRComponentTsid
+ __OBJC_$_CLASS_METHODS_CRComponentVeridian
+ __OBJC_$_CLASS_METHODS_CRDaemonController
+ __OBJC_$_CLASS_METHODS_CRDeviceMap
+ __OBJC_$_CLASS_METHODS_CRFDRBaseDeviceHandler
+ __OBJC_$_CLASS_METHODS_CRFDRCompute1DeviceHandler
+ __OBJC_$_CLASS_METHODS_CRFDRDeviceController
+ __OBJC_$_CLASS_METHODS_CRFDRDisplay1DeviceHandler
+ __OBJC_$_CLASS_METHODS_CRFDRGen1DeviceHandler
+ __OBJC_$_CLASS_METHODS_CRFDRGen2DeviceHandler
+ __OBJC_$_CLASS_METHODS_CRFDRGen3DeviceHandler
+ __OBJC_$_CLASS_METHODS_CRFDRGen4DeviceHandler
+ __OBJC_$_CLASS_METHODS_CRFDRGen5DeviceHandler
+ __OBJC_$_CLASS_METHODS_CRFDRGen6DeviceHandler
+ __OBJC_$_CLASS_METHODS_CRFDRGen7DeviceHandler
+ __OBJC_$_CLASS_METHODS_CRFDRLegacy2DeviceHandler
+ __OBJC_$_CLASS_METHODS_CRFDRLegacyDeviceHandler
+ __OBJC_$_CLASS_METHODS_CRFDRRetryController
+ __OBJC_$_CLASS_METHODS_CRFDRSeal
+ __OBJC_$_CLASS_METHODS_CRFDRUtils(ComponentState)
+ __OBJC_$_CLASS_METHODS_CRFDRiPad1DeviceHandler
+ __OBJC_$_CLASS_METHODS_CRFileSystemController
+ __OBJC_$_CLASS_METHODS_CRLocalization
+ __OBJC_$_CLASS_METHODS_CRMesaController
+ __OBJC_$_CLASS_METHODS_CRNVRAMController
+ __OBJC_$_CLASS_METHODS_CRPatchUtils
+ __OBJC_$_CLASS_METHODS_CRPersonalizationManager
+ __OBJC_$_CLASS_METHODS_CRPreflightHelper
+ __OBJC_$_CLASS_METHODS_CRPreflightRequest
+ __OBJC_$_CLASS_METHODS_CRPreflightUtils
+ __OBJC_$_CLASS_METHODS_CRRepairReport
+ __OBJC_$_CLASS_METHODS_CRRepairReportItem
+ __OBJC_$_CLASS_METHODS_CRRepairStatusLite
+ __OBJC_$_CLASS_METHODS_CRStrongComponent
+ __OBJC_$_CLASS_METHODS_CRSysConfig
+ __OBJC_$_CLASS_METHODS_CRUtils
+ __OBJC_$_CLASS_METHODS_CRWiFiCredEncryption
+ __OBJC_$_CLASS_METHODS_CRWiFiCredentials
+ __OBJC_$_CLASS_METHODS_CoreRepairHelper
+ __OBJC_$_CLASS_PROP_LIST_CRChallengeObject
+ __OBJC_$_CLASS_PROP_LIST_CRChallengeResponse
+ __OBJC_$_CLASS_PROP_LIST_CRStrongComponent
+ __OBJC_$_CLASS_PROP_LIST_NSSecureCoding
+ __OBJC_$_INSTANCE_METHODS_CRAttestationHelper
+ __OBJC_$_INSTANCE_METHODS_CRAudioCodecStatus
+ __OBJC_$_INSTANCE_METHODS_CRAudioStatus
+ __OBJC_$_INSTANCE_METHODS_CRBackGlassStatus
+ __OBJC_$_INSTANCE_METHODS_CRBasebandStatus
+ __OBJC_$_INSTANCE_METHODS_CRBatteryStatus
+ __OBJC_$_INSTANCE_METHODS_CRBluetoothStatus
+ __OBJC_$_INSTANCE_METHODS_CRBootIntentHelper
+ __OBJC_$_INSTANCE_METHODS_CRCAttestationManager
+ __OBJC_$_INSTANCE_METHODS_CRCCertificate
+ __OBJC_$_INSTANCE_METHODS_CRCameraAuth
+ __OBJC_$_INSTANCE_METHODS_CRCameraAuthUsingProperty
+ __OBJC_$_INSTANCE_METHODS_CRChallengeObject
+ __OBJC_$_INSTANCE_METHODS_CRChallengeResponse
+ __OBJC_$_INSTANCE_METHODS_CRChassisController
+ __OBJC_$_INSTANCE_METHODS_CRComponentAuth
+ __OBJC_$_INSTANCE_METHODS_CRComponentBase
+ __OBJC_$_INSTANCE_METHODS_CRComponentBatteryRoswell
+ __OBJC_$_INSTANCE_METHODS_CRComponentDisplayRoswell
+ __OBJC_$_INSTANCE_METHODS_CRComponentPearl
+ __OBJC_$_INSTANCE_METHODS_CRComponentSigning
+ __OBJC_$_INSTANCE_METHODS_CRComponentTsid
+ __OBJC_$_INSTANCE_METHODS_CRComponentVeridian
+ __OBJC_$_INSTANCE_METHODS_CRCoverGlassStatus
+ __OBJC_$_INSTANCE_METHODS_CRDevice
+ __OBJC_$_INSTANCE_METHODS_CRDeviceComponent
+ __OBJC_$_INSTANCE_METHODS_CRDisplayStatus
+ __OBJC_$_INSTANCE_METHODS_CREANController
+ __OBJC_$_INSTANCE_METHODS_CREnclosureStatus
+ __OBJC_$_INSTANCE_METHODS_CRFDRBaseDeviceHandler
+ __OBJC_$_INSTANCE_METHODS_CRFDRCompute1DeviceHandler
+ __OBJC_$_INSTANCE_METHODS_CRFDRDeviceController
+ __OBJC_$_INSTANCE_METHODS_CRFDRDisplay1DeviceHandler
+ __OBJC_$_INSTANCE_METHODS_CRFDRGen1DeviceHandler
+ __OBJC_$_INSTANCE_METHODS_CRFDRGen2DeviceHandler
+ __OBJC_$_INSTANCE_METHODS_CRFDRGen3DeviceHandler
+ __OBJC_$_INSTANCE_METHODS_CRFDRGen4DeviceHandler
+ __OBJC_$_INSTANCE_METHODS_CRFDRGen5DeviceHandler
+ __OBJC_$_INSTANCE_METHODS_CRFDRGen6DeviceHandler
+ __OBJC_$_INSTANCE_METHODS_CRFDRGen7DeviceHandler
+ __OBJC_$_INSTANCE_METHODS_CRFDRLegacy2DeviceHandler
+ __OBJC_$_INSTANCE_METHODS_CRFDRLegacyDeviceHandler
+ __OBJC_$_INSTANCE_METHODS_CRFDRRCHL
+ __OBJC_$_INSTANCE_METHODS_CRFDRRetryController
+ __OBJC_$_INSTANCE_METHODS_CRFDRSeal(StagedSealing|RealSealing)
+ __OBJC_$_INSTANCE_METHODS_CRFDRiPad1DeviceHandler
+ __OBJC_$_INSTANCE_METHODS_CRFaceIDStatus
+ __OBJC_$_INSTANCE_METHODS_CRFileSystemController
+ __OBJC_$_INSTANCE_METHODS_CRMesaController
+ __OBJC_$_INSTANCE_METHODS_CRNFCStatus
+ __OBJC_$_INSTANCE_METHODS_CRPearlController
+ __OBJC_$_INSTANCE_METHODS_CRPersonalizationElement
+ __OBJC_$_INSTANCE_METHODS_CRPersonalizationManager
+ __OBJC_$_INSTANCE_METHODS_CRPreflight
+ __OBJC_$_INSTANCE_METHODS_CRPreflightController
+ __OBJC_$_INSTANCE_METHODS_CRPreflightHelper
+ __OBJC_$_INSTANCE_METHODS_CRPreflightRequest
+ __OBJC_$_INSTANCE_METHODS_CRPreflightRequestComponent
+ __OBJC_$_INSTANCE_METHODS_CRPreflightResponse
+ __OBJC_$_INSTANCE_METHODS_CRRCamStatus
+ __OBJC_$_INSTANCE_METHODS_CRRIK
+ __OBJC_$_INSTANCE_METHODS_CRRepairHistory
+ __OBJC_$_INSTANCE_METHODS_CRRepairHistoryItem
+ __OBJC_$_INSTANCE_METHODS_CRRepairReportItem
+ __OBJC_$_INSTANCE_METHODS_CRStrongComponent
+ __OBJC_$_INSTANCE_METHODS_CRSysConfig
+ __OBJC_$_INSTANCE_METHODS_CRTouchIDStatus
+ __OBJC_$_INSTANCE_METHODS_CRUWBStatus
+ __OBJC_$_INSTANCE_METHODS_CRUserDefaults
+ __OBJC_$_INSTANCE_METHODS_CRUtils
+ __OBJC_$_INSTANCE_METHODS_CRVolumeButtonStatus
+ __OBJC_$_INSTANCE_METHODS_CRWifiStatus
+ __OBJC_$_INSTANCE_METHODS_CoreRepairHelper
+ __OBJC_$_INSTANCE_METHODS_NSData(HexString|Digest)
+ __OBJC_$_INSTANCE_METHODS_NSString(FDR|Digest|Utils)
+ __OBJC_$_INSTANCE_VARIABLES_CRCAttestationManager
+ __OBJC_$_INSTANCE_VARIABLES_CRCCertificate
+ __OBJC_$_INSTANCE_VARIABLES_CRChallengeObject
+ __OBJC_$_INSTANCE_VARIABLES_CRChallengeResponse
+ __OBJC_$_INSTANCE_VARIABLES_CRComponentAuth
+ __OBJC_$_INSTANCE_VARIABLES_CRComponentBase
+ __OBJC_$_INSTANCE_VARIABLES_CRComponentBatteryRoswell
+ __OBJC_$_INSTANCE_VARIABLES_CRComponentDisplayRoswell
+ __OBJC_$_INSTANCE_VARIABLES_CRComponentPearl
+ __OBJC_$_INSTANCE_VARIABLES_CRComponentTsid
+ __OBJC_$_INSTANCE_VARIABLES_CRComponentVeridian
+ __OBJC_$_INSTANCE_VARIABLES_CRDevice
+ __OBJC_$_INSTANCE_VARIABLES_CRDeviceComponent
+ __OBJC_$_INSTANCE_VARIABLES_CREANController
+ __OBJC_$_INSTANCE_VARIABLES_CRFDRBaseDeviceHandler
+ __OBJC_$_INSTANCE_VARIABLES_CRFDRCompute1DeviceHandler
+ __OBJC_$_INSTANCE_VARIABLES_CRFDRDeviceController
+ __OBJC_$_INSTANCE_VARIABLES_CRFDRDisplay1DeviceHandler
+ __OBJC_$_INSTANCE_VARIABLES_CRFDRRCHL
+ __OBJC_$_INSTANCE_VARIABLES_CRFDRRetryController
+ __OBJC_$_INSTANCE_VARIABLES_CRFDRSeal
+ __OBJC_$_INSTANCE_VARIABLES_CRFileSystemController
+ __OBJC_$_INSTANCE_VARIABLES_CRPersonalizationElement
+ __OBJC_$_INSTANCE_VARIABLES_CRPersonalizationManager
+ __OBJC_$_INSTANCE_VARIABLES_CRPreflightController
+ __OBJC_$_INSTANCE_VARIABLES_CRPreflightRequest
+ __OBJC_$_INSTANCE_VARIABLES_CRPreflightRequestComponent
+ __OBJC_$_INSTANCE_VARIABLES_CRPreflightResponse
+ __OBJC_$_INSTANCE_VARIABLES_CRRIK
+ __OBJC_$_INSTANCE_VARIABLES_CRRepairHistory
+ __OBJC_$_INSTANCE_VARIABLES_CRRepairHistoryItem
+ __OBJC_$_INSTANCE_VARIABLES_CRRepairReportItem
+ __OBJC_$_INSTANCE_VARIABLES_CRStrongComponent
+ __OBJC_$_INSTANCE_VARIABLES_CRSysConfig
+ __OBJC_$_INSTANCE_VARIABLES_CRUserDefaults
+ __OBJC_$_INSTANCE_VARIABLES_CoreRepairHelper
+ __OBJC_$_PROP_LIST_CRCAttestationManager
+ __OBJC_$_PROP_LIST_CRCCertificate
+ __OBJC_$_PROP_LIST_CRChallengeObject
+ __OBJC_$_PROP_LIST_CRChallengeResponse
+ __OBJC_$_PROP_LIST_CRComponentAuth
+ __OBJC_$_PROP_LIST_CRComponentBase
+ __OBJC_$_PROP_LIST_CRDevice
+ __OBJC_$_PROP_LIST_CRDeviceComponent
+ __OBJC_$_PROP_LIST_CRFDRBaseDeviceHandler
+ __OBJC_$_PROP_LIST_CRFDRDisplay1DeviceHandler
+ __OBJC_$_PROP_LIST_CRFDRRCHL
+ __OBJC_$_PROP_LIST_CRFDRSeal
+ __OBJC_$_PROP_LIST_CRPersonalizationElement
+ __OBJC_$_PROP_LIST_CRPreflightController
+ __OBJC_$_PROP_LIST_CRPreflightRequest
+ __OBJC_$_PROP_LIST_CRPreflightRequestComponent
+ __OBJC_$_PROP_LIST_CRPreflightResponse
+ __OBJC_$_PROP_LIST_CRRIK
+ __OBJC_$_PROP_LIST_CRRepairHistoryItem
+ __OBJC_$_PROP_LIST_CRRepairReportItem
+ __OBJC_$_PROP_LIST_CRStrongComponent
+ __OBJC_$_PROP_LIST_CRSysConfig
+ __OBJC_$_PROP_LIST_CRUserDefaults
+ __OBJC_$_PROP_LIST_CoreRepairHelper
+ __OBJC_$_PROP_LIST_NSObject
+ __OBJC_$_PROP_LIST_NSProgressReporting
+ __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CRAttestationProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CRFDR
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CoreRepairBootIntentProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CoreRepairCoreNetworkXPCServiceProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CoreRepairCoreXPCServiceProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CoreRepairHelperProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CoreRepairPreflightProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSProgressReporting
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSURLSessionDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_setupModuleChallengeCallBack
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CRAttestationProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CRFDR
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CoreRepairBootIntentProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CoreRepairCoreNetworkXPCServiceProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CoreRepairCoreXPCServiceProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CoreRepairHelperProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CoreRepairPreflightProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSProgressReporting
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSURLSessionDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_setupModuleChallengeCallBack
+ __OBJC_$_PROTOCOL_REFS_CRFDR
+ __OBJC_$_PROTOCOL_REFS_CoreRepairHelperProtocol
+ __OBJC_$_PROTOCOL_REFS_NSProgressReporting
+ __OBJC_$_PROTOCOL_REFS_NSSecureCoding
+ __OBJC_$_PROTOCOL_REFS_NSURLSessionDelegate
+ __OBJC_$_PROTOCOL_REFS_setupModuleChallengeCallBack
+ __OBJC_CLASS_PROTOCOLS_$_CRAttestationHelper
+ __OBJC_CLASS_PROTOCOLS_$_CRBootIntentHelper
+ __OBJC_CLASS_PROTOCOLS_$_CRCAttestationManager
+ __OBJC_CLASS_PROTOCOLS_$_CRChallengeObject
+ __OBJC_CLASS_PROTOCOLS_$_CRChallengeResponse
+ __OBJC_CLASS_PROTOCOLS_$_CRFDRSeal
+ __OBJC_CLASS_PROTOCOLS_$_CRPreflightController
+ __OBJC_CLASS_PROTOCOLS_$_CRPreflightHelper
+ __OBJC_CLASS_PROTOCOLS_$_CRStrongComponent
+ __OBJC_CLASS_PROTOCOLS_$_CoreRepairHelper
+ __OBJC_CLASS_RO_$_CRAttestationHelper
+ __OBJC_CLASS_RO_$_CRAudioCodecStatus
+ __OBJC_CLASS_RO_$_CRAudioStatus
+ __OBJC_CLASS_RO_$_CRBackGlassStatus
+ __OBJC_CLASS_RO_$_CRBasebandStatus
+ __OBJC_CLASS_RO_$_CRBatteryController
+ __OBJC_CLASS_RO_$_CRBatteryStatus
+ __OBJC_CLASS_RO_$_CRBluetoothStatus
+ __OBJC_CLASS_RO_$_CRBootIntentController
+ __OBJC_CLASS_RO_$_CRBootIntentHelper
+ __OBJC_CLASS_RO_$_CRCAttestationManager
+ __OBJC_CLASS_RO_$_CRCCertificate
+ __OBJC_CLASS_RO_$_CRCameraAuth
+ __OBJC_CLASS_RO_$_CRCameraAuthUsingProperty
+ __OBJC_CLASS_RO_$_CRChallengeObject
+ __OBJC_CLASS_RO_$_CRChallengeResponse
+ __OBJC_CLASS_RO_$_CRChassisController
+ __OBJC_CLASS_RO_$_CRComponentAuth
+ __OBJC_CLASS_RO_$_CRComponentBase
+ __OBJC_CLASS_RO_$_CRComponentBatteryRoswell
+ __OBJC_CLASS_RO_$_CRComponentDisplayRoswell
+ __OBJC_CLASS_RO_$_CRComponentPearl
+ __OBJC_CLASS_RO_$_CRComponentSigning
+ __OBJC_CLASS_RO_$_CRComponentTsid
+ __OBJC_CLASS_RO_$_CRComponentVeridian
+ __OBJC_CLASS_RO_$_CRCoverGlassStatus
+ __OBJC_CLASS_RO_$_CRDaemonController
+ __OBJC_CLASS_RO_$_CRDevice
+ __OBJC_CLASS_RO_$_CRDeviceComponent
+ __OBJC_CLASS_RO_$_CRDeviceMap
+ __OBJC_CLASS_RO_$_CRDisplayStatus
+ __OBJC_CLASS_RO_$_CREANController
+ __OBJC_CLASS_RO_$_CREnclosureStatus
+ __OBJC_CLASS_RO_$_CRFDRBaseDeviceHandler
+ __OBJC_CLASS_RO_$_CRFDRCompute1DeviceHandler
+ __OBJC_CLASS_RO_$_CRFDRDeviceController
+ __OBJC_CLASS_RO_$_CRFDRDisplay1DeviceHandler
+ __OBJC_CLASS_RO_$_CRFDRGen1DeviceHandler
+ __OBJC_CLASS_RO_$_CRFDRGen2DeviceHandler
+ __OBJC_CLASS_RO_$_CRFDRGen3DeviceHandler
+ __OBJC_CLASS_RO_$_CRFDRGen4DeviceHandler
+ __OBJC_CLASS_RO_$_CRFDRGen5DeviceHandler
+ __OBJC_CLASS_RO_$_CRFDRGen6DeviceHandler
+ __OBJC_CLASS_RO_$_CRFDRGen7DeviceHandler
+ __OBJC_CLASS_RO_$_CRFDRLegacy2DeviceHandler
+ __OBJC_CLASS_RO_$_CRFDRLegacyDeviceHandler
+ __OBJC_CLASS_RO_$_CRFDRRCHL
+ __OBJC_CLASS_RO_$_CRFDRRetryController
+ __OBJC_CLASS_RO_$_CRFDRSeal
+ __OBJC_CLASS_RO_$_CRFDRUtils
+ __OBJC_CLASS_RO_$_CRFDRiPad1DeviceHandler
+ __OBJC_CLASS_RO_$_CRFaceIDStatus
+ __OBJC_CLASS_RO_$_CRFileSystemController
+ __OBJC_CLASS_RO_$_CRLocalization
+ __OBJC_CLASS_RO_$_CRMesaController
+ __OBJC_CLASS_RO_$_CRNFCStatus
+ __OBJC_CLASS_RO_$_CRNVRAMController
+ __OBJC_CLASS_RO_$_CRPatchUtils
+ __OBJC_CLASS_RO_$_CRPearlController
+ __OBJC_CLASS_RO_$_CRPersonalizationElement
+ __OBJC_CLASS_RO_$_CRPersonalizationManager
+ __OBJC_CLASS_RO_$_CRPreflight
+ __OBJC_CLASS_RO_$_CRPreflightController
+ __OBJC_CLASS_RO_$_CRPreflightHelper
+ __OBJC_CLASS_RO_$_CRPreflightRequest
+ __OBJC_CLASS_RO_$_CRPreflightRequestComponent
+ __OBJC_CLASS_RO_$_CRPreflightResponse
+ __OBJC_CLASS_RO_$_CRPreflightUtils
+ __OBJC_CLASS_RO_$_CRRCamStatus
+ __OBJC_CLASS_RO_$_CRRIK
+ __OBJC_CLASS_RO_$_CRRepairHistory
+ __OBJC_CLASS_RO_$_CRRepairHistoryItem
+ __OBJC_CLASS_RO_$_CRRepairReport
+ __OBJC_CLASS_RO_$_CRRepairReportItem
+ __OBJC_CLASS_RO_$_CRRepairStatusLite
+ __OBJC_CLASS_RO_$_CRStrongComponent
+ __OBJC_CLASS_RO_$_CRSysConfig
+ __OBJC_CLASS_RO_$_CRTouchIDStatus
+ __OBJC_CLASS_RO_$_CRUWBStatus
+ __OBJC_CLASS_RO_$_CRUserDefaults
+ __OBJC_CLASS_RO_$_CRUtils
+ __OBJC_CLASS_RO_$_CRVolumeButtonStatus
+ __OBJC_CLASS_RO_$_CRWiFiCredEncryption
+ __OBJC_CLASS_RO_$_CRWiFiCredentials
+ __OBJC_CLASS_RO_$_CRWifiStatus
+ __OBJC_CLASS_RO_$_CoreRepairHelper
+ __OBJC_LABEL_PROTOCOL_$_CRAttestationProtocol
+ __OBJC_LABEL_PROTOCOL_$_CRFDR
+ __OBJC_LABEL_PROTOCOL_$_CoreRepairBootIntentProtocol
+ __OBJC_LABEL_PROTOCOL_$_CoreRepairCoreNetworkXPCServiceProtocol
+ __OBJC_LABEL_PROTOCOL_$_CoreRepairCoreXPCServiceProtocol
+ __OBJC_LABEL_PROTOCOL_$_CoreRepairHelperProtocol
+ __OBJC_LABEL_PROTOCOL_$_CoreRepairPreflightProtocol
+ __OBJC_LABEL_PROTOCOL_$_NSCoding
+ __OBJC_LABEL_PROTOCOL_$_NSObject
+ __OBJC_LABEL_PROTOCOL_$_NSProgressReporting
+ __OBJC_LABEL_PROTOCOL_$_NSSecureCoding
+ __OBJC_LABEL_PROTOCOL_$_NSURLSessionDelegate
+ __OBJC_LABEL_PROTOCOL_$_setupModuleChallengeCallBack
+ __OBJC_METACLASS_RO_$_CRAttestationHelper
+ __OBJC_METACLASS_RO_$_CRAudioCodecStatus
+ __OBJC_METACLASS_RO_$_CRAudioStatus
+ __OBJC_METACLASS_RO_$_CRBackGlassStatus
+ __OBJC_METACLASS_RO_$_CRBasebandStatus
+ __OBJC_METACLASS_RO_$_CRBatteryController
+ __OBJC_METACLASS_RO_$_CRBatteryStatus
+ __OBJC_METACLASS_RO_$_CRBluetoothStatus
+ __OBJC_METACLASS_RO_$_CRBootIntentController
+ __OBJC_METACLASS_RO_$_CRBootIntentHelper
+ __OBJC_METACLASS_RO_$_CRCAttestationManager
+ __OBJC_METACLASS_RO_$_CRCCertificate
+ __OBJC_METACLASS_RO_$_CRCameraAuth
+ __OBJC_METACLASS_RO_$_CRCameraAuthUsingProperty
+ __OBJC_METACLASS_RO_$_CRChallengeObject
+ __OBJC_METACLASS_RO_$_CRChallengeResponse
+ __OBJC_METACLASS_RO_$_CRChassisController
+ __OBJC_METACLASS_RO_$_CRComponentAuth
+ __OBJC_METACLASS_RO_$_CRComponentBase
+ __OBJC_METACLASS_RO_$_CRComponentBatteryRoswell
+ __OBJC_METACLASS_RO_$_CRComponentDisplayRoswell
+ __OBJC_METACLASS_RO_$_CRComponentPearl
+ __OBJC_METACLASS_RO_$_CRComponentSigning
+ __OBJC_METACLASS_RO_$_CRComponentTsid
+ __OBJC_METACLASS_RO_$_CRComponentVeridian
+ __OBJC_METACLASS_RO_$_CRCoverGlassStatus
+ __OBJC_METACLASS_RO_$_CRDaemonController
+ __OBJC_METACLASS_RO_$_CRDevice
+ __OBJC_METACLASS_RO_$_CRDeviceComponent
+ __OBJC_METACLASS_RO_$_CRDeviceMap
+ __OBJC_METACLASS_RO_$_CRDisplayStatus
+ __OBJC_METACLASS_RO_$_CREANController
+ __OBJC_METACLASS_RO_$_CREnclosureStatus
+ __OBJC_METACLASS_RO_$_CRFDRBaseDeviceHandler
+ __OBJC_METACLASS_RO_$_CRFDRCompute1DeviceHandler
+ __OBJC_METACLASS_RO_$_CRFDRDeviceController
+ __OBJC_METACLASS_RO_$_CRFDRDisplay1DeviceHandler
+ __OBJC_METACLASS_RO_$_CRFDRGen1DeviceHandler
+ __OBJC_METACLASS_RO_$_CRFDRGen2DeviceHandler
+ __OBJC_METACLASS_RO_$_CRFDRGen3DeviceHandler
+ __OBJC_METACLASS_RO_$_CRFDRGen4DeviceHandler
+ __OBJC_METACLASS_RO_$_CRFDRGen5DeviceHandler
+ __OBJC_METACLASS_RO_$_CRFDRGen6DeviceHandler
+ __OBJC_METACLASS_RO_$_CRFDRGen7DeviceHandler
+ __OBJC_METACLASS_RO_$_CRFDRLegacy2DeviceHandler
+ __OBJC_METACLASS_RO_$_CRFDRLegacyDeviceHandler
+ __OBJC_METACLASS_RO_$_CRFDRRCHL
+ __OBJC_METACLASS_RO_$_CRFDRRetryController
+ __OBJC_METACLASS_RO_$_CRFDRSeal
+ __OBJC_METACLASS_RO_$_CRFDRUtils
+ __OBJC_METACLASS_RO_$_CRFDRiPad1DeviceHandler
+ __OBJC_METACLASS_RO_$_CRFaceIDStatus
+ __OBJC_METACLASS_RO_$_CRFileSystemController
+ __OBJC_METACLASS_RO_$_CRLocalization
+ __OBJC_METACLASS_RO_$_CRMesaController
+ __OBJC_METACLASS_RO_$_CRNFCStatus
+ __OBJC_METACLASS_RO_$_CRNVRAMController
+ __OBJC_METACLASS_RO_$_CRPatchUtils
+ __OBJC_METACLASS_RO_$_CRPearlController
+ __OBJC_METACLASS_RO_$_CRPersonalizationElement
+ __OBJC_METACLASS_RO_$_CRPersonalizationManager
+ __OBJC_METACLASS_RO_$_CRPreflight
+ __OBJC_METACLASS_RO_$_CRPreflightController
+ __OBJC_METACLASS_RO_$_CRPreflightHelper
+ __OBJC_METACLASS_RO_$_CRPreflightRequest
+ __OBJC_METACLASS_RO_$_CRPreflightRequestComponent
+ __OBJC_METACLASS_RO_$_CRPreflightResponse
+ __OBJC_METACLASS_RO_$_CRPreflightUtils
+ __OBJC_METACLASS_RO_$_CRRCamStatus
+ __OBJC_METACLASS_RO_$_CRRIK
+ __OBJC_METACLASS_RO_$_CRRepairHistory
+ __OBJC_METACLASS_RO_$_CRRepairHistoryItem
+ __OBJC_METACLASS_RO_$_CRRepairReport
+ __OBJC_METACLASS_RO_$_CRRepairReportItem
+ __OBJC_METACLASS_RO_$_CRRepairStatusLite
+ __OBJC_METACLASS_RO_$_CRStrongComponent
+ __OBJC_METACLASS_RO_$_CRSysConfig
+ __OBJC_METACLASS_RO_$_CRTouchIDStatus
+ __OBJC_METACLASS_RO_$_CRUWBStatus
+ __OBJC_METACLASS_RO_$_CRUserDefaults
+ __OBJC_METACLASS_RO_$_CRUtils
+ __OBJC_METACLASS_RO_$_CRVolumeButtonStatus
+ __OBJC_METACLASS_RO_$_CRWiFiCredEncryption
+ __OBJC_METACLASS_RO_$_CRWiFiCredentials
+ __OBJC_METACLASS_RO_$_CRWifiStatus
+ __OBJC_METACLASS_RO_$_CoreRepairHelper
+ __OBJC_PROTOCOL_$_CRAttestationProtocol
+ __OBJC_PROTOCOL_$_CRFDR
+ __OBJC_PROTOCOL_$_CoreRepairBootIntentProtocol
+ __OBJC_PROTOCOL_$_CoreRepairCoreNetworkXPCServiceProtocol
+ __OBJC_PROTOCOL_$_CoreRepairCoreXPCServiceProtocol
+ __OBJC_PROTOCOL_$_CoreRepairHelperProtocol
+ __OBJC_PROTOCOL_$_CoreRepairPreflightProtocol
+ __OBJC_PROTOCOL_$_NSCoding
+ __OBJC_PROTOCOL_$_NSObject
+ __OBJC_PROTOCOL_$_NSProgressReporting
+ __OBJC_PROTOCOL_$_NSSecureCoding
+ __OBJC_PROTOCOL_$_NSURLSessionDelegate
+ __OBJC_PROTOCOL_$_setupModuleChallengeCallBack
+ __OBJC_PROTOCOL_REFERENCE_$_CRAttestationProtocol
+ __OBJC_PROTOCOL_REFERENCE_$_CoreRepairCoreNetworkXPCServiceProtocol
+ __OBJC_PROTOCOL_REFERENCE_$_CoreRepairCoreXPCServiceProtocol
+ __OBJC_PROTOCOL_REFERENCE_$_CoreRepairHelperProtocol
+ __OBJC_PROTOCOL_REFERENCE_$_CoreRepairPreflightProtocol
+ ___27+[CRSysConfig sharedAccess]_block_invoke
+ ___28+[CRDeviceMap currentDevice]_block_invoke
+ ___32-[CRFDRSeal initWithParameters:]_block_invoke
+ ___32-[CRFDRSeal initWithParameters:]_block_invoke.cold.1
+ ___33+[CRPatchUtils decodePatchItems:]_block_invoke
+ ___33-[CRFDRSeal summarizePatchInputs]_block_invoke
+ ___34+[CRComponentBase sharedSingleton]_block_invoke
+ ___34+[CRComponentTsid sharedSingleton]_block_invoke
+ ___34+[CRFDRUtils isPropertySupported:]_block_invoke
+ ___34+[CoreRepairHelper sharedInstance]_block_invoke
+ ___35+[CRComponentPearl sharedSingleton]_block_invoke
+ ___35+[CRFDRUtils isDataClassSupported:]_block_invoke
+ ___35+[CRPreflightHelper sharedInstance]_block_invoke
+ ___35-[CRComponentAuth findUnsealedData]_block_invoke
+ ___35-[CRComponentAuth findUnsealedData]_block_invoke.30
+ ___35-[CRComponentAuth findUnsealedData]_block_invoke.30.cold.1
+ ___35-[CRComponentAuth findUnsealedData]_block_invoke.30.cold.2
+ ___35-[CRComponentAuth findUnsealedData]_block_invoke.cold.1
+ ___35-[CRComponentAuth findUnsealedData]_block_invoke_2
+ ___35-[CRComponentAuth findUnsealedData]_block_invoke_2.cold.1
+ ___37+[CRAttestationHelper sharedInstance]_block_invoke
+ ___38+[CRComponentVeridian sharedSingleton]_block_invoke
+ ___38+[CRFDRRetryController sharedInstance]_block_invoke
+ ___38+[CRMesaController getProtocolVersion]_block_invoke
+ ___38+[CRMesaController getProtocolVersion]_block_invoke.cold.1
+ ___38-[CRChassisController seal:withReply:]_block_invoke
+ ___38-[CRPreflightController sign:keyBlob:]_block_invoke
+ ___38-[CRPreflightController sign:keyBlob:]_block_invoke.153
+ ___38-[CRPreflightController sign:keyBlob:]_block_invoke.cold.1
+ ___39-[CRFDRSeal deleteLocalData:dataClass:]_block_invoke
+ ___40+[CRFDRDeviceController sharedSingleton]_block_invoke
+ ___41+[CRDeviceMap getSupportedComponentTypes]_block_invoke
+ ___41+[CRFileSystemController sharedSingleton]_block_invoke
+ ___41+[CRLocalization localizedStringWithKey:]_block_invoke
+ ___44+[CRComponentBatteryRoswell sharedSingleton]_block_invoke
+ ___44+[CRComponentDisplayRoswell sharedSingleton]_block_invoke
+ ___44-[CRFDRDeviceController getHandlerForDevice]_block_invoke
+ ___45+[CRDaemonController doLaunchControl:action:]_block_invoke
+ ___45+[CRDaemonController doLaunchControl:action:]_block_invoke.cold.1
+ ___45+[CRDaemonController doLaunchControl:action:]_block_invoke.cold.2
+ ___45-[CRPreflightController preflight:withReply:]_block_invoke
+ ___45-[CRPreflightController preflight:withReply:]_block_invoke_2
+ ___46-[CRComponentAuth synchronouslycopyAuthStatus]_block_invoke
+ ___47-[CRFDRBaseDeviceHandler getExpectedPatchInfo:]_block_invoke
+ ___48-[CREANController writeFDRDataToEANWithdataDir:]_block_invoke
+ ___48-[CREANController writeFDRDataToEANWithdataDir:]_block_invoke.cold.1
+ ___48-[CRPreflightController queryRepairDelta:error:]_block_invoke
+ ___48-[CRPreflightController queryRepairDelta:error:]_block_invoke.192
+ ___48-[CRPreflightController queryRepairDelta:error:]_block_invoke.cold.1
+ ___50+[CRDaemonController getLibXPCInternalWithSymbol:]_block_invoke
+ ___50-[CRComponentVeridian signVeridianWith:withReply:]_block_invoke
+ ___50-[CRPreflightController verify:signature:keyBlob:]_block_invoke
+ ___50-[CRPreflightController verify:signature:keyBlob:]_block_invoke.157
+ ___50-[CRPreflightController verify:signature:keyBlob:]_block_invoke.cold.1
+ ___51-[CRFileSystemController syncFDRDataAtPath:toPath:]_block_invoke
+ ___51-[CRFileSystemController syncFDRDataAtPath:toPath:]_block_invoke.37
+ ___51-[CRPreflightController sendRequest:keyBlob:error:]_block_invoke
+ ___51-[CRPreflightController sendRequest:keyBlob:error:]_block_invoke_2
+ ___54+[CRBatteryController setBatteryDateOfFirstUse:error:]_block_invoke
+ ___55-[CRPreflight _sendBAARequest:proxySettings:withError:]_block_invoke
+ ___55-[CRPreflight _sendBAARequest:proxySettings:withError:]_block_invoke_2
+ ___55-[CRPreflightController issueRepairCert:keyBlob:error:]_block_invoke
+ ___55-[CRPreflightController issueRepairCert:keyBlob:error:]_block_invoke.194
+ ___55-[CRPreflightController issueRepairCert:keyBlob:error:]_block_invoke.cold.1
+ ___56-[CRComponentVeridian challengeComponentWith:withReply:]_block_invoke
+ ___56-[CRRepairHistory getCAAForRepairHistoryWithCompletion:]_block_invoke
+ ___56-[CRRepairHistory getCAAForRepairHistoryWithCompletion:]_block_invoke_2
+ ___56-[CRRepairHistory getCAAForRepairHistoryWithCompletion:]_block_invoke_2.cold.1
+ ___56-[CRRepairHistory getCAAForRepairHistoryWithCompletion:]_block_invoke_2.cold.2
+ ___60-[CRFDRBaseDeviceHandler challengeComponentsWith:withReply:]_block_invoke
+ ___60-[CRFDRBaseDeviceHandler challengeComponentsWith:withReply:]_block_invoke.244
+ ___60-[CRFDRBaseDeviceHandler challengeComponentsWith:withReply:]_block_invoke_2
+ ___60-[CRFDRBaseDeviceHandler challengeComponentsWith:withReply:]_block_invoke_2.cold.1
+ ___62-[CRComponentBatteryRoswell challengeComponentWith:withReply:]_block_invoke
+ ___62-[CRComponentBatteryRoswell signbatteryRoswellWith:withReply:]_block_invoke
+ ___62-[CRComponentDisplayRoswell challengeComponentWith:withReply:]_block_invoke
+ ___62-[CRComponentDisplayRoswell signDisplayRoswellWith:withReply:]_block_invoke
+ ___67-[CRPreflightController challengeStrongComponents:responses:error:]_block_invoke
+ ___67-[CRPreflightController challengeStrongComponents:responses:error:]_block_invoke.200
+ ___67-[CRPreflightController challengeStrongComponents:responses:error:]_block_invoke.cold.1
+ ___69-[CRCAttestationManager getStrongComponentsWithError:resultobtained:]_block_invoke
+ ___69-[CRCAttestationManager getStrongComponentsWithError:resultobtained:]_block_invoke.121
+ ___69-[CRCAttestationManager getStrongComponentsWithError:resultobtained:]_block_invoke.cold.1
+ ___71-[CRCAttestationManager sendChallengeRequestWith:serverResponse:error:]_block_invoke
+ ___71-[CRCAttestationManager sendChallengeRequestWith:serverResponse:error:]_block_invoke.199
+ ___71-[CRCAttestationManager sendChallengeRequestWith:serverResponse:error:]_block_invoke.cold.1
+ ___71-[CRCAttestationManager sendChallengeRequestWith:serverResponse:error:]_block_invoke.cold.2
+ ___71-[CRCAttestationManager sendChallengeRequestWith:serverResponse:error:]_block_invoke.cold.3
+ ___73-[CRCAttestationManager challengeComponentsWith:challengeResponse:error:]_block_invoke
+ ___73-[CRCAttestationManager challengeComponentsWith:challengeResponse:error:]_block_invoke.129
+ ___73-[CRCAttestationManager challengeComponentsWith:challengeResponse:error:]_block_invoke.cold.1
+ ___75-[CRCAttestationManager sendCertIssueRequestWith:serverCertResponse:error:]_block_invoke
+ ___75-[CRCAttestationManager sendCertIssueRequestWith:serverCertResponse:error:]_block_invoke.218
+ ___75-[CRCAttestationManager sendCertIssueRequestWith:serverCertResponse:error:]_block_invoke.cold.1
+ ___75-[CRCAttestationManager sendCertIssueRequestWith:serverCertResponse:error:]_block_invoke.cold.2
+ ___75-[CRCAttestationManager sendCertIssueRequestWith:serverCertResponse:error:]_block_invoke.cold.3
+ ___82-[NSDictionary(CRValidations) NSArrayFromKey:types:maxLength:defaultValue:failed:]_block_invoke
+ ___92-[CRCAttestationManager issueClientCertificateWithCompletionOnQueue:withOptions:completion:]_block_invoke
+ ___92-[CRCAttestationManager issueClientCertificateWithCompletionOnQueue:withOptions:completion:]_block_invoke.37
+ ___92-[CRCAttestationManager issueClientCertificateWithCompletionOnQueue:withOptions:completion:]_block_invoke.37.cold.1
+ ___92-[CRCAttestationManager issueClientCertificateWithCompletionOnQueue:withOptions:completion:]_block_invoke.37.cold.2
+ ___92-[CRCAttestationManager issueClientCertificateWithCompletionOnQueue:withOptions:completion:]_block_invoke.43
+ ___92-[CRCAttestationManager issueClientCertificateWithCompletionOnQueue:withOptions:completion:]_block_invoke.79
+ ___92-[CRCAttestationManager issueClientCertificateWithCompletionOnQueue:withOptions:completion:]_block_invoke.cold.1
+ ___92-[CRCAttestationManager issueClientCertificateWithCompletionOnQueue:withOptions:completion:]_block_invoke_2
+ ___Block_byref_object_copy_
+ ___Block_byref_object_dispose_
+ ___OSLogInit_block_invoke
+ ___OSLogInit_block_invoke.cold.1
+ ____generateRepairReportXPC_block_invoke
+ ____generateRepairReportXPC_block_invoke_2
+ ____getComponentStateXPC_block_invoke
+ ____getComponentStateXPC_block_invoke_2
+ ___block_descriptor_32_e17_v16?0"NSError"8l
+ ___block_descriptor_32_e29_32?08"NSDictionary"16^24l
+ ___block_descriptor_32_e34_"NSDictionary"24?0"NSData"8^16l
+ ___block_descriptor_32_e36_"NSDictionary"24?0"NSString"8^16l
+ ___block_descriptor_32_e37_"NSData"32?08"NSDictionary"16^24l
+ ___block_descriptor_32_e47_"NSDictionary"24?0"NSMutableDictionary"8^16l
+ ___block_descriptor_32_e58_"NSData"32?0"NSMutableDictionary"8"NSDictionary"16^24l
+ ___block_descriptor_32_e5_v8?0l
+ ___block_descriptor_32_e8_B16?08l
+ ___block_descriptor_40_e5_v8?0l
+ ___block_descriptor_40_e8_32bs_e39_v28?0B8"CRCCertificate"12"NSError"20ls32l8
+ ___block_descriptor_40_e8_32r_e15_v32?08Q16^B24lr32l8
+ ___block_descriptor_40_e8_32r_e17_v16?0"NSError"8lr32l8
+ ___block_descriptor_40_e8_32s_e12_v24?0#8^B16ls32l8
+ ___block_descriptor_40_e8_32s_e15_v32?0816^B24ls32l8
+ ___block_descriptor_40_e8_32s_e17_v16?0"NSError"8ls32l8
+ ___block_descriptor_41_e8_32r_e37_B24?0r*8"NSObject<OS_xpc_object>"16lr32l8
+ ___block_descriptor_48_e8_32r40r_e19_v20?0B8"NSData"12lr32l8r40l8
+ ___block_descriptor_48_e8_32r40r_e5_v8?0lr32l8r40l8
+ ___block_descriptor_48_e8_32s40r_e15_v32?0816^B24ls32l8r40l8
+ ___block_descriptor_48_e8_32s40r_e15_v32?08Q16^B24ls32l8r40l8
+ ___block_descriptor_48_e8_32s40r_e16_v16?0"NSData"8lr40l8s32l8
+ ___block_descriptor_48_e8_32s40r_e17_v16?0"NSError"8lr40l8s32l8
+ ___block_descriptor_48_e8_32s40r_e5_v8?0lr40l8s32l8
+ ___block_descriptor_48_e8_32s40r_e8_v12?0B8lr40l8s32l8
+ ___block_descriptor_48_e8_32s40s_e32_v28?0B8"NSArray"12"NSError"20ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_56_e8_32r40r48r_e22_v20?0i8^{__CFDate=}12lr32l8r40l8r48l8
+ ___block_descriptor_56_e8_32r40r48r_e30_v28?0B8"NSData"12"NSData"20lr32l8r40l8r48l8
+ ___block_descriptor_56_e8_32r40r48r_e36_v36?0B8"NSData"12"NSData"20B28i32lr32l8r40l8r48l8
+ ___block_descriptor_56_e8_32r40r48r_e37_v28?0B8"NSDictionary"12"NSError"20lr32l8r40l8r48l8
+ ___block_descriptor_56_e8_32s40r48r_e20_v20?0i8"NSError"12lr40l8r48l8s32l8
+ ___block_descriptor_56_e8_32s40s48bs_e22_v16?0"NSDictionary"8ls32l8s48l8s40l8
+ ___block_descriptor_56_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s48r_e22_v16?0"NSDictionary"8lr48l8s32l8s40l8
+ ___block_descriptor_56_e8_32s40s48s_e15_v32?0816^B24ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32r40r48r56r_e30_v28?0"NSData"8"NSData"16i24lr32l8r40l8r48l8r56l8
+ ___block_descriptor_64_e8_32r40r48r56r_e32_v28?0B8"NSArray"12"NSError"20lr32l8r40l8r48l8r56l8
+ ___block_descriptor_64_e8_32r40r48r56r_e46_v32?0"NSData"8"NSURLResponse"16"NSError"24lr32l8r40l8r48l8r56l8
+ ___block_descriptor_64_e8_32s40bs48r56r_e5_v8?0ls40l8r48l8s32l8r56l8
+ ___block_descriptor_64_e8_32s40r48r56r_e32_v28?0B8"NSArray"12"NSError"20lr40l8r48l8r56l8s32l8
+ ___block_descriptor_64_e8_32s40s48s56s_e44_v28?0B8"NSError"12"CRChallengeResponse"20ls32l8s40l8s48l8s56l8
+ ___block_descriptor_72_e8_32r40r48r56r64r_e87_v32?0^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}8"NSArray"16"NSError"24lr32l8r40l8r48l8r56l8r64l8
+ ___block_descriptor_72_e8_32s40r48r56r64r_e43_v36?0B8"NSData"12"NSArray"20"NSError"28lr40l8r48l8r56l8r64l8s32l8
+ ___block_descriptor_72_e8_32s40r48r56r64r_e5_v8?0lr40l8r48l8s32l8r56l8r64l8
+ ___block_descriptor_72_e8_32s40r_e19_"NSDictionary"8?0ls32l8r40l8
+ ___block_descriptor_72_e8_32s40s48r56r64r_e32_v28?0"NSArray"8i16"NSError"20lr48l8r56l8r64l8s32l8s40l8
+ ___block_descriptor_72_e8_32s40s48r56r64r_e37_v28?0"NSDictionary"8i16"NSError"20lr48l8r56l8r64l8s32l8s40l8
+ ___block_descriptor_72_e8_32s40s48s56s64s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_88_e8_32r40r48r56r64r72r80r_e5_v8?0lr32l8r40l8r48l8r56l8r64l8r72l8r80l8
+ ___block_descriptor_tmp
+ ___block_descriptor_tmp.150
+ ___block_descriptor_tmp.169
+ ___block_literal_global
+ ___block_literal_global.152
+ ___block_literal_global.156
+ ___block_literal_global.159
+ ___block_literal_global.161
+ ___block_literal_global.163
+ ___block_literal_global.171
+ ___block_literal_global.174
+ ___block_literal_global.176
+ ___block_literal_global.190
+ ___block_literal_global.192
+ ___block_literal_global.197
+ ___block_literal_global.200
+ ___block_literal_global.208
+ ___block_literal_global.34
+ ___block_literal_global.44
+ ___block_literal_global.46
+ ___block_literal_global.61
+ ___block_literal_global.78
+ ___block_literal_global.81
+ ___block_literal_global.94
+ ___der_key_access_groups
+ ___der_key_acm_handle
+ ___der_key_auth_data
+ ___der_key_data
+ ___der_key_ecdh_iv
+ ___der_key_ecdh_seed
+ ___der_key_external_data
+ ___der_key_gid_ref_key_options
+ ___der_key_keybag_class
+ ___der_key_op
+ ___der_key_op_create
+ ___der_key_op_sign
+ ___der_key_op_sik_attest
+ ___der_key_options
+ ___der_key_persona_uuid
+ ___der_key_pka_flags
+ ___der_key_public_key
+ ___der_key_raw_output
+ ___der_key_ref_key
+ ___der_key_remote_session_signing_key_certificate
+ ___der_key_remote_session_signing_key_type
+ ___der_key_salt
+ ___der_key_seed
+ ___der_key_shared_info
+ ___der_key_shared_info2
+ ___der_key_sub_key_type
+ ___der_key_system_key_client_seed
+ ___der_key_system_key_no_img4
+ ___der_key_system_key_options
+ ___der_key_test_flags
+ ___der_key_transcode_ecdh_seed
+ ___der_key_transcode_shared_info
+ ___der_key_transcode_shared_info2
+ ___der_key_type
+ ___der_key_volume_uuid
+ ___get_aks_client_connection_block_invoke
+ ___get_aks_client_dispatch_queue_block_invoke
+ ___handleForCategory_block_invoke
+ ___memcpy_chk
+ ___osLog
+ ___osLogPearlLib
+ ___osLogPearlLibTrace
+ ___osLogTrace
+ ___performCommand
+ ___performCommand.cold.1
+ ___performCommand.cold.2
+ ___signChallenge_block_invoke
+ ___signChallenge_block_invoke_2
+ ___signVeridian_block_invoke
+ ___signVeridian_block_invoke.cold.1
+ ___signVeridian_block_invoke.cold.2
+ __aks_operation
+ __connect
+ __copy_aks_client_connection
+ __dict_find_value_cb
+ __encode_list_find_key
+ __getCameraService
+ __getXPCConnection
+ __get_merged_params
+ __logHandler.cold.1
+ __logHandler.cold.2
+ __merge_dict_cb
+ __merge_dict_cb.cold.1
+ __merge_dict_cb.cold.2
+ __op_attest
+ __os_signpost_emit_with_name_impl
+ __params_get_der_key
+ __qsort_compare
+ __set_blob
+ __testMode
+ __testProvisionState
+ _aks_params_create
+ _aks_params_free
+ _aks_params_get_der
+ _aks_params_set_number
+ _aks_ref_key_create
+ _aks_ref_key_create_with_blob
+ _aks_ref_key_free
+ _aks_ref_key_get_blob
+ _aks_ref_key_get_public_key
+ _aks_ref_key_get_type
+ _aks_ref_key_sign
+ _aks_ref_key_verify_sig
+ _aks_sik_attest
+ _ccder_blob_check_null
+ _ccder_blob_decode_AlgorithmIdentifierNULL
+ _commonNameOIDBytes
+ _compare_octet_string
+ _compare_octet_string_raw
+ _copyCameraIORegValue
+ _copyCameraIORegValue.cold.1
+ _copyCameraIORegValue.cold.2
+ _copyCertificateValidityDate
+ _cpGetInternalComponents
+ _createCRError
+ _createCRError.cold.1
+ _createECDSADerData
+ _createECDSADerData.cold.1
+ _createECDSADerData.cold.2
+ _createECDSADerData.cold.3
+ _createECDSADerData.cold.4
+ _createECDSADerData.cold.5
+ _createECDSADerData.cold.6
+ _createECDSADerData.cold.7
+ _createECDSADerData.cold.8
+ _createECDSADerData.cold.9
+ _createError
+ _ctlPhysicalPresence
+ _ctlPhysicalPresence.cold.1
+ _ctlPhysicalPresence.cold.2
+ _ctlPhysicalPresence.cold.3
+ _ctlPhysicalPresence.cold.4
+ _ctlPhysicalPresence.cold.5
+ _ctlPhysicalPresence.cold.6
+ _ctlPhysicalPresence.cold.7
+ _currentDevice.device
+ _currentDevice.onceToken
+ _decompressReferenceFrames
+ _decompressReferenceFrames.cold.1
+ _decompressReferenceFrames.cold.10
+ _decompressReferenceFrames.cold.11
+ _decompressReferenceFrames.cold.12
+ _decompressReferenceFrames.cold.13
+ _decompressReferenceFrames.cold.14
+ _decompressReferenceFrames.cold.15
+ _decompressReferenceFrames.cold.16
+ _decompressReferenceFrames.cold.17
+ _decompressReferenceFrames.cold.18
+ _decompressReferenceFrames.cold.19
+ _decompressReferenceFrames.cold.2
+ _decompressReferenceFrames.cold.20
+ _decompressReferenceFrames.cold.21
+ _decompressReferenceFrames.cold.22
+ _decompressReferenceFrames.cold.23
+ _decompressReferenceFrames.cold.24
+ _decompressReferenceFrames.cold.25
+ _decompressReferenceFrames.cold.26
+ _decompressReferenceFrames.cold.27
+ _decompressReferenceFrames.cold.28
+ _decompressReferenceFrames.cold.3
+ _decompressReferenceFrames.cold.4
+ _decompressReferenceFrames.cold.5
+ _decompressReferenceFrames.cold.6
+ _decompressReferenceFrames.cold.7
+ _decompressReferenceFrames.cold.8
+ _decompressReferenceFrames.cold.9
+ _der_dict_find_value
+ _der_dict_iterate
+ _der_equal
+ _der_get_boolean
+ _der_get_number
+ _der_get_sizeof
+ _der_key_access_groups
+ _der_key_acm_handle
+ _der_key_auth_data
+ _der_key_data
+ _der_key_ecdh_iv
+ _der_key_ecdh_seed
+ _der_key_external_data
+ _der_key_gid_ref_key_options
+ _der_key_keybag_class
+ _der_key_op
+ _der_key_op_create
+ _der_key_op_sign
+ _der_key_op_sik_attest
+ _der_key_options
+ _der_key_persona_uuid
+ _der_key_pka_flags
+ _der_key_public_key
+ _der_key_raw_output
+ _der_key_ref_key
+ _der_key_remote_session_signing_key_certificate
+ _der_key_remote_session_signing_key_type
+ _der_key_salt
+ _der_key_seed
+ _der_key_shared_info
+ _der_key_shared_info2
+ _der_key_sub_key_type
+ _der_key_system_key_client_seed
+ _der_key_system_key_no_img4
+ _der_key_system_key_options
+ _der_key_test_flags
+ _der_key_transcode_ecdh_seed
+ _der_key_transcode_shared_info
+ _der_key_transcode_shared_info2
+ _der_key_type
+ _der_key_volume_uuid
+ _der_utils_decode_implicit_raw_octet_string
+ _derivedEncryptionKey
+ _derivedEncryptionKey.deviceKeySeed
+ _encode_list_add_data
+ _encode_list_add_der
+ _encode_list_add_key
+ _encode_list_add_number
+ _encode_list_dict
+ _encode_list_free
+ _encode_list_merge_dict
+ _encode_list_remove_key
+ _findUnsealedData.onceToken
+ _findUnsealedData.returnResults
+ _firebloom_cp_prime_bitlen
+ _firebloom_cp_prime_size
+ _gSealHeader
+ _gSealingMapClassSet
+ _gSealingMapPropertyDict
+ _generateLthTransferRequestWithOptions
+ _generateLthTransferRequestWithOptions_block_invoke_15
+ _generateLthTransferRequestWithOptions_block_invoke_15.cold.1
+ _generateLthTransferRequestWithOptions_block_invoke_15.cold.2
+ _generateLthTransferRequestWithOptions_block_invoke_15.cold.3
+ _generateLthTransferRequestWithOptions_block_invoke_15.cold.4
+ _generatePDIRequestWithPath
+ _generatePDIRequestWithPath_block_invoke_5
+ _generatePDIRequestWithPath_block_invoke_5.cold.1
+ _generatePDIRequestWithPath_block_invoke_5.cold.2
+ _generatePDIRequestWithPath_block_invoke_5.cold.3
+ _generatePDIRequestWithPath_block_invoke_5.cold.4
+ _generateRepairTicket
+ _generateRepairTicket_block_invoke_4
+ _generateRepairTicket_block_invoke_4.cold.1
+ _generateRepairTicket_block_invoke_4.cold.2
+ _generateRepairTicket_block_invoke_4.cold.3
+ _generateRepairTicket_block_invoke_4.cold.4
+ _generateRepairTicket_block_invoke_4.cold.5
+ _generateRepairTicket_block_invoke_4.cold.6
+ _generateRepairTicket_block_invoke_4.cold.7
+ _generateSavageFWRequestWithOptions
+ _generateSavageFWRequestWithOptions_block_invoke_8
+ _generateSavageUpdaterTicketRequestWithOptions
+ _generateSavageUpdaterTicketRequestWithOptions_block_invoke_18
+ _generateSeaCookiePairingRequestWithOptions
+ _generateSeaCookiePairingRequestWithOptions_block_invoke_13
+ _generateSeaCookiePairingRequestWithOptions_block_invoke_13.cold.1
+ _generateSeaCookiePairingRequestWithOptions_block_invoke_13.cold.2
+ _generateSeaCookiePairingRequestWithOptions_block_invoke_13.cold.3
+ _generateTrustObjectDigestRequestWithDigest
+ _generateTrustObjectDigestRequestWithDigest_block_invoke_2
+ _generateTrustObjectDigestRequestWithDigest_block_invoke_2.cold.1
+ _generateVeridianFWRequestWithOptions
+ _generateVeridianFWRequestWithOptions_block_invoke_7
+ _generateVeridianFWRequestWithOptions_block_invoke_7.cold.1
+ _generateVeridianFWRequestWithOptions_block_invoke_7.cold.2
+ _generateVeridianFWRequestWithOptions_block_invoke_7.cold.3
+ _generateVeridianFWRequestWithOptions_block_invoke_7.cold.4
+ _generateYonkersFWRequestWithOptions
+ _generateYonkersFWRequestWithOptions_block_invoke_11
+ _getLibXPCInternalWithSymbol:.lib
+ _getLibXPCInternalWithSymbol:.onceToken
+ _getProtocolVersion.onceToken
+ _getProtocolVersion.version
+ _getProvisioningStateReal
+ _getProvisioningStateReal.cold.1
+ _getProvisioningStateReal.cold.2
+ _getSensorProvisioningState
+ _getSensorType
+ _getSensorType.cold.1
+ _getSensorType.cold.2
+ _getSensorType.cold.3
+ _getSensorType.cold.4
+ _getSensorType.cold.5
+ _getSensorType.cold.6
+ _getSupportedComponentTypes.onceToken
+ _getSupportedComponentTypes.result
+ _get_aks_client_connection
+ _get_aks_client_connection.cold.1
+ _get_aks_client_connection.connection
+ _get_aks_client_dispatch_queue.connection_queue
+ _get_aks_client_dispatch_queue.onceToken
+ _handleForCategory.cold.1
+ _handleForCategory.logHandles
+ _handleForCategory.onceToken
+ _initialize
+ _initialize.cold.1
+ _initialize.cold.2
+ _isDataClassSupported:.classes
+ _isDataClassSupported:.onceToken
+ _isPropertySupported:.onceToken
+ _isPropertySupported:.properties
+ _kAMFDRSealingMapAttributeEarlyAccess
+ _kAPTKFourCharCode
+ _localizedStringWithKey:.bundle
+ _localizedStringWithKey:.onceToken
+ _logAndParse
+ _logMsg
+ _objc_msgSend$AddResponseTicketForSavageUpdaterOptions:auth:error:
+ _objc_msgSend$BOOLFromKey:defaultValue:failed:
+ _objc_msgSend$CAABasedRepairDateForComponent:withHistory:
+ _objc_msgSend$CAABasedRepairForComponent:withHistory:
+ _objc_msgSend$CRCreateECDSADerData:responseDer:
+ _objc_msgSend$CRFDRCheckVerificationFatalErrors:fdrLocal:sealedData:strict:
+ _objc_msgSend$CRFDRDataRepairRecover:fdrRemote:syncEAN:fdrError:
+ _objc_msgSend$CRFDRLocalPopulate:fdrRemote:sealedData:fdrError:
+ _objc_msgSend$CRFDRPostRecoverVerify:fdrRemote:syncEAN:fdrError:
+ _objc_msgSend$CRFDRRecoverMissingData:fdrLocal:fdrRemote:
+ _objc_msgSend$CRFDRVerifyLocal:fdrRemote:sealedData:mergedDataClasses:mergedDataInstances:currentManifestProperties:fdrError:syncEAN:postSeal:ignoreBenignError:
+ _objc_msgSend$CRFDRVerifyProperties:currentManifestProperties:fdrError:
+ _objc_msgSend$HTTPBody
+ _objc_msgSend$IsTatsuErrorNetworkingRelated:
+ _objc_msgSend$JSONObjectWithData:options:error:
+ _objc_msgSend$KBBDataClasses
+ _objc_msgSend$KBBDataInstances
+ _objc_msgSend$KBBECID
+ _objc_msgSend$KBBMLBSerialNumber
+ _objc_msgSend$KBBSIK
+ _objc_msgSend$KBBSealInstance
+ _objc_msgSend$KBBSerialNumber
+ _objc_msgSend$KBBTransferProperties
+ _objc_msgSend$NSArrayFromKey:inSet:maxLength:defaultValue:failed:
+ _objc_msgSend$NSArrayFromKey:types:maxLength:defaultValue:failed:
+ _objc_msgSend$NSArrayFromKey:types:maxLength:defaultValue:failed:validator:
+ _objc_msgSend$NSDataFromKey:defaultValue:failed:
+ _objc_msgSend$NSDictionaryFromKey:defaultValue:failed:
+ _objc_msgSend$NSDictionaryFromRequiredKey:failed:
+ _objc_msgSend$NSNumberFromKey:lowerBound:upperBound:defaultValue:failed:
+ _objc_msgSend$NSSetFromKey:defaultValue:failed:
+ _objc_msgSend$NSStringFromKey:defaultValue:failed:
+ _objc_msgSend$NSStringFromKey:inSet:defaultValue:failed:
+ _objc_msgSend$RCHLBasedRepairDateForComponent:withHistory:
+ _objc_msgSend$SHA256DigestData
+ _objc_msgSend$SHA256DigestString
+ _objc_msgSend$SHA384DigestData
+ _objc_msgSend$URLWithString:
+ _objc_msgSend$URLWithString:relativeToURL:
+ _objc_msgSend$UTF8String
+ _objc_msgSend$UUID
+ _objc_msgSend$UUIDString
+ _objc_msgSend$_addAlsCToMutableArrayWithPartSPC:dataClasses:dataInstances:error:
+ _objc_msgSend$_addDataClassAndInstanceToMutableDictionary:dataClass:withError:
+ _objc_msgSend$_addDataClassAndInstancesToMutableArray:dataClasses:dataInstances:withError:
+ _objc_msgSend$_addHmCAToMutableArrayWithFdrRemote:dataClasses:dataInstances:error:
+ _objc_msgSend$_addPropertyToMutableDictionary:property:withError:
+ _objc_msgSend$_apticketCopyDataObjectPropertyWithTag:property:
+ _objc_msgSend$_baseFDROptionsWithDataStore:
+ _objc_msgSend$_checkComponentResealedWithRCHL:usedPart:error:
+ _objc_msgSend$_checkForComponentFailureInDefaults:
+ _objc_msgSend$_checkStrongIdentity:
+ _objc_msgSend$_commitData:fdrlocal:fdrError:
+ _objc_msgSend$_commitSealedData:fdrRemote:sealedData:syncEAN:returnError:
+ _objc_msgSend$_compareSealedAndLiveDataClasses:instances:liveClasses:liveInstances:results:
+ _objc_msgSend$_compareSerialNumberProperties:missingLiveData:results:
+ _objc_msgSend$_copyCombinedFDRData:withError:
+ _objc_msgSend$_copyFDROptionsForPatch:
+ _objc_msgSend$_copySikaFuse
+ _objc_msgSend$_createFDRLocal
+ _objc_msgSend$_fetchRemoteTrustObject:apTrustObjectDigest:remoteTrustObject:fdrError:
+ _objc_msgSend$_getAllLiveDataClasses:liveInstances:missingLiveData:mesaState:error:
+ _objc_msgSend$_getAllSealedDataAndPropertiesFromManifest:properties:classes:instances:error:
+ _objc_msgSend$_getCRFDRMetaDataDictionary
+ _objc_msgSend$_getClaimCountEnforceDate
+ _objc_msgSend$_getDataClassUsingComponentAuthName:
+ _objc_msgSend$_getDataClassesFromSealingMap
+ _objc_msgSend$_getDataClassesToWrite
+ _objc_msgSend$_getManifestForDataClass:
+ _objc_msgSend$_getMesaState
+ _objc_msgSend$_getObjectForKeyFromDefaults:
+ _objc_msgSend$_getPropertiesFromSealingMap
+ _objc_msgSend$_getPropertyArrayFrom:
+ _objc_msgSend$_getQuerykeyFromDataClass:
+ _objc_msgSend$_getUnsealedMesaData:mesaState:
+ _objc_msgSend$_getVersionInfo:
+ _objc_msgSend$_hasALSOnDisplay
+ _objc_msgSend$_hasRearALS
+ _objc_msgSend$_hasSameKey:this:other:
+ _objc_msgSend$_init
+ _objc_msgSend$_init:
+ _objc_msgSend$_isLegacyMesaInInvalidState
+ _objc_msgSend$_logSealingRequest:
+ _objc_msgSend$_mergeActivationLocks:
+ _objc_msgSend$_personalizeTrustObjectWithDigest:withError:
+ _objc_msgSend$_personalizeWithElement:useCache:parsedResponseData:error:
+ _objc_msgSend$_populateSealingMapForCurrentDevice
+ _objc_msgSend$_populateSealingMapProperties
+ _objc_msgSend$_sendBAARequest:proxySettings:withError:
+ _objc_msgSend$_ticketCopyHashDataWithNode:
+ _objc_msgSend$_urlsOverrideIsAllowed
+ _objc_msgSend$_writeBatteryDateOfFirstUse:error:
+ _objc_msgSend$_writeDataToEAN:withKey:
+ _objc_msgSend$absoluteString
+ _objc_msgSend$activationChallenges
+ _objc_msgSend$activationResponses
+ _objc_msgSend$addEntriesFromDictionary:
+ _objc_msgSend$addIndex:
+ _objc_msgSend$addObject:
+ _objc_msgSend$addObjectsFromArray:
+ _objc_msgSend$allHTTPHeaderFields
+ _objc_msgSend$allHeaderFields
+ _objc_msgSend$allKeys
+ _objc_msgSend$allObjects
+ _objc_msgSend$allowFactoryReset
+ _objc_msgSend$allowMissingData
+ _objc_msgSend$allowSelfService
+ _objc_msgSend$allowUsedPart
+ _objc_msgSend$alphanumericCharacterSet
+ _objc_msgSend$anyObject
+ _objc_msgSend$appendBytes:length:
+ _objc_msgSend$appendData:
+ _objc_msgSend$appendFormat:
+ _objc_msgSend$appendString:
+ _objc_msgSend$apticketCopyHashData
+ _objc_msgSend$array
+ _objc_msgSend$arrayWithObject:
+ _objc_msgSend$arrayWithObjects:count:
+ _objc_msgSend$asid
+ _objc_msgSend$attestationBlob
+ _objc_msgSend$authenticateBatteryWithChallenge:completionHandler:
+ _objc_msgSend$authenticateTouchControllerWithChallenge:completionHandler:
+ _objc_msgSend$base64EncodedStringWithOptions:
+ _objc_msgSend$base64Preprocess:
+ _objc_msgSend$bcrtSign:outSignature:outDeviceNonce:outError:
+ _objc_msgSend$bikCertificate
+ _objc_msgSend$boolForKey:
+ _objc_msgSend$boolValue
+ _objc_msgSend$bundleForClass:
+ _objc_msgSend$bytes
+ _objc_msgSend$cStringUsingEncoding:
+ _objc_msgSend$calculateDerLength:actualSize:
+ _objc_msgSend$certifcateType
+ _objc_msgSend$certificates
+ _objc_msgSend$challengeComponentWith:withReply:
+ _objc_msgSend$challengeComponentsWith:challengeResponse:error:
+ _objc_msgSend$challengeComponentsWith:withReply:
+ _objc_msgSend$challengeStrongComponents:responses:error:
+ _objc_msgSend$challengeStrongComponents:withReply:
+ _objc_msgSend$characterAtIndex:
+ _objc_msgSend$characterSetWithCharactersInString:
+ _objc_msgSend$checkComponentFailed:error:
+ _objc_msgSend$checkComponentResealed:usedPart:error:
+ _objc_msgSend$checkComponentUnsealed:error:
+ _objc_msgSend$checkNonSecureRepair:error:
+ _objc_msgSend$checkRepairEnvironment
+ _objc_msgSend$checkUsedStatusFor:withHistory:withClaimCount:
+ _objc_msgSend$claimDict
+ _objc_msgSend$cleanupFileSystemForRepair
+ _objc_msgSend$clearBootIntentWithError:
+ _objc_msgSend$clearRepairBackup:
+ _objc_msgSend$code
+ _objc_msgSend$commitToFileSystem
+ _objc_msgSend$compare:
+ _objc_msgSend$compare:options:range:
+ _objc_msgSend$componentChallenges
+ _objc_msgSend$componentName
+ _objc_msgSend$componentResponses
+ _objc_msgSend$componentType
+ _objc_msgSend$components
+ _objc_msgSend$components:withState:
+ _objc_msgSend$componentsMapping
+ _objc_msgSend$componentsSeparatedByCharactersInSet:
+ _objc_msgSend$componentsSeparatedByString:
+ _objc_msgSend$connectToIO:withError:
+ _objc_msgSend$containsObject:
+ _objc_msgSend$containsString:
+ _objc_msgSend$contentsOfDirectoryAtPath:error:
+ _objc_msgSend$controlWithParametersImpl:withReply:
+ _objc_msgSend$convertDataToHexInDictionary:
+ _objc_msgSend$convertIORegDataToStatus:authPass:
+ _objc_msgSend$convertToHexString
+ _objc_msgSend$copy
+ _objc_msgSend$copyAttestationRequestWithError:challenge:
+ _objc_msgSend$copyChallengeRequestWithError:
+ _objc_msgSend$copyComponentStatus
+ _objc_msgSend$copyCurrentFDREANValuesWithdataDir:error:
+ _objc_msgSend$copyFDREANValues:outgenerationCount:outManifesthash:
+ _objc_msgSend$copyItemAtPath:toPath:error:
+ _objc_msgSend$copyMountPointForVolumeType:error:
+ _objc_msgSend$copyPathForPersistentData:error:
+ _objc_msgSend$copyPathForPersonalizedData:error:
+ _objc_msgSend$copyStagedFDREanDataWithdataDir:error:
+ _objc_msgSend$count
+ _objc_msgSend$countByEnumeratingWithState:objects:count:
+ _objc_msgSend$create
+ _objc_msgSend$createBaseAMAIObject
+ _objc_msgSend$createDirectoryAtPath:withIntermediateDirectories:attributes:error:
+ _objc_msgSend$createEncryptedCredentialsDataWithLocale:
+ _objc_msgSend$createPEMFromCerts:
+ _objc_msgSend$createStringForKey:
+ _objc_msgSend$createSymbolicLinkAtPath:withDestinationPath:error:
+ _objc_msgSend$createWithKeyBlob:
+ _objc_msgSend$credentialForTrust:
+ _objc_msgSend$currentConnection
+ _objc_msgSend$currentDevice
+ _objc_msgSend$currentLocale
+ _objc_msgSend$currentProcessHasEntitlement:
+ _objc_msgSend$currentProperties
+ _objc_msgSend$daemonControl:withReply:
+ _objc_msgSend$data
+ _objc_msgSend$dataClasses
+ _objc_msgSend$dataIdentifier
+ _objc_msgSend$dataIsValid:length:
+ _objc_msgSend$dataKey
+ _objc_msgSend$dataTaskWithRequest:completionHandler:
+ _objc_msgSend$dataUsingEncoding:
+ _objc_msgSend$dataWithBytes:length:
+ _objc_msgSend$dataWithBytesNoCopy:length:
+ _objc_msgSend$dataWithBytesNoCopy:length:freeWhenDone:
+ _objc_msgSend$dataWithCapacity:
+ _objc_msgSend$dataWithContentsOfFile:
+ _objc_msgSend$dataWithContentsOfFile:options:error:
+ _objc_msgSend$dataWithHexString:
+ _objc_msgSend$dataWithJSONObject:options:error:
+ _objc_msgSend$dataWithLength:
+ _objc_msgSend$dataWithPropertyList:format:options:error:
+ _objc_msgSend$date
+ _objc_msgSend$dateByAddingTimeInterval:
+ _objc_msgSend$dateFromString:
+ _objc_msgSend$dateWithTimeIntervalSinceReferenceDate:
+ _objc_msgSend$decodeObjectOfClasses:forKey:
+ _objc_msgSend$decodePatchItems:
+ _objc_msgSend$decompressPearlFrames
+ _objc_msgSend$decryptUserData:
+ _objc_msgSend$decryptWiFiCredDictFromCredentialsData:
+ _objc_msgSend$defaultManager
+ _objc_msgSend$deleteFDRDataFromEANWithDataClass:
+ _objc_msgSend$deleteLocalData:
+ _objc_msgSend$deleteLocalData:dataClass:
+ _objc_msgSend$deleteNVRAMValueForKey:error:
+ _objc_msgSend$deltaComponents:strongComponents:error:
+ _objc_msgSend$description
+ _objc_msgSend$details
+ _objc_msgSend$determineRepairStatus:repairHistory:
+ _objc_msgSend$deviceSupportsRepairBootIntent
+ _objc_msgSend$dictionary
+ _objc_msgSend$dictionaryWithCapacity:
+ _objc_msgSend$dictionaryWithContentsOfFile:
+ _objc_msgSend$dictionaryWithDictionary:
+ _objc_msgSend$dictionaryWithObjects:forKeys:count:
+ _objc_msgSend$dictionaryWithValuesForKeys:
+ _objc_msgSend$diffWithSealed:live:
+ _objc_msgSend$disableRetry
+ _objc_msgSend$doLaunchControl:action:
+ _objc_msgSend$domain
+ _objc_msgSend$enableRetry
+ _objc_msgSend$enableSSO:
+ _objc_msgSend$encodeObject:forKey:
+ _objc_msgSend$encryptUserData:
+ _objc_msgSend$enumerateKeysAndObjectsUsingBlock:
+ _objc_msgSend$enumerateObjectsUsingBlock:
+ _objc_msgSend$ephemeralSessionConfiguration
+ _objc_msgSend$error
+ _objc_msgSend$errorCode
+ _objc_msgSend$errorMessage
+ _objc_msgSend$errorWithDomain:code:userInfo:
+ _objc_msgSend$extractCAAAttestationOIDDataWithError:
+ _objc_msgSend$extractComponentsAndIdentifiers:
+ _objc_msgSend$extractRCHLRepairHistoryAndClaimCount:
+ _objc_msgSend$extractRepairCentersWithRCHLHistory:
+ _objc_msgSend$extractRepairHistoryWithError:
+ _objc_msgSend$extractRepairsAfterACRZWithHistory:
+ _objc_msgSend$factoryServiceOn
+ _objc_msgSend$fdrKeys
+ _objc_msgSend$fileExistsAtPath:
+ _objc_msgSend$fileHandleForReadingAtPath:
+ _objc_msgSend$fileURLWithPath:
+ _objc_msgSend$filteredArrayUsingPredicate:
+ _objc_msgSend$filteredPhase2Components:response:
+ _objc_msgSend$findEntry:key:
+ _objc_msgSend$findRCHLHistoryObjectForComponent:withHistory:
+ _objc_msgSend$findSyscfgAccess
+ _objc_msgSend$findUnsealedData
+ _objc_msgSend$findUnsealedDataWithError:
+ _objc_msgSend$findUnsealedDataWithKey:error:
+ _objc_msgSend$firstMatchInString:options:range:
+ _objc_msgSend$firstObject
+ _objc_msgSend$formUnionWithCharacterSet:
+ _objc_msgSend$foundInMultiRequestError:dataClass:dataInstance:
+ _objc_msgSend$fwVersion
+ _objc_msgSend$generateFinalData
+ _objc_msgSend$generateRepairReport:withReply:
+ _objc_msgSend$getAPTicket
+ _objc_msgSend$getAllowedListFromEntitlements:
+ _objc_msgSend$getAndVerifyDataInstance:
+ _objc_msgSend$getAuthCPComponentStatus:
+ _objc_msgSend$getBackglassDataClasses
+ _objc_msgSend$getBytes:length:
+ _objc_msgSend$getCameraDataClasses
+ _objc_msgSend$getClaimDataClassesAndInstancesWithPartSPC:withError:
+ _objc_msgSend$getCmClValidationStatus
+ _objc_msgSend$getComponentBySPC:
+ _objc_msgSend$getComponentByType:
+ _objc_msgSend$getComponentState:withReply:
+ _objc_msgSend$getCurrentManifestDataClassesAndInstancesWithPartSPC:fdr:currentClasses:currentInstances:currentProperties:fdrError:
+ _objc_msgSend$getData:instance:
+ _objc_msgSend$getDataClassesAndInstancesOfKBBWith:propertiesDict:fdrError:
+ _objc_msgSend$getDataInstance
+ _objc_msgSend$getDataPayload:instance:
+ _objc_msgSend$getDataPayloadDictWithClass:instance:
+ _objc_msgSend$getDefaultAMAuthInstallRef
+ _objc_msgSend$getDeviceHandlerForProductType:
+ _objc_msgSend$getExcludedPropertiesForFactoryReset
+ _objc_msgSend$getExcludedPropertiesForSealedVerify
+ _objc_msgSend$getExpectedPatchInfo:
+ _objc_msgSend$getHandlerForDevice
+ _objc_msgSend$getIORegComponentStatus
+ _objc_msgSend$getInnermostNSError:
+ _objc_msgSend$getInnermostNSErrorCode:
+ _objc_msgSend$getInternalName:
+ _objc_msgSend$getKBBSealInstanceWithError:fdrRemote:
+ _objc_msgSend$getKeysInComponent:
+ _objc_msgSend$getLibXPCInternalWithSymbol:
+ _objc_msgSend$getLiveChMf
+ _objc_msgSend$getLocalSealingManifest
+ _objc_msgSend$getLocalSealingManifestWithError:
+ _objc_msgSend$getLocalizationKey:
+ _objc_msgSend$getMTUBDataClasses
+ _objc_msgSend$getMakeDataClassesAndInstancesWithPartSPC:fdrRemote:makeClasses:makeInstances:makePropertiesDict:fdrError:
+ _objc_msgSend$getMakeDataClassesAndInstancesWithPartSPC:fdrRemote:makePropertiesDict:fdrError:
+ _objc_msgSend$getMinimalManifestsClassesAndInstancesWithPartSPC:fdrLocal:fdrRemote:minimalSealingDataInstances:minimalSealedDataClasses:minimalSealedDataInstances:minimalSealedVersions:error:
+ _objc_msgSend$getOSEnvironment
+ _objc_msgSend$getPatchDataClassesAndInstancesWithPartSPC:fdrRemote:patchClasses:patchInstances:patchValues:error:
+ _objc_msgSend$getPatchExpectedDataWithPartSPC:amfdr:expectedClasses:expectedInstances:expectedValues:expectedDatas:validClasses:validInstances:error:
+ _objc_msgSend$getPatchInfoPerSPC
+ _objc_msgSend$getPathForApTicketWithError:
+ _objc_msgSend$getPathForBorsFirmwareWithError:
+ _objc_msgSend$getPathForBrunorFirmwareWithError:
+ _objc_msgSend$getPathForSavageFirmwareWithError:
+ _objc_msgSend$getPathForYonkersFirmwareWithError:
+ _objc_msgSend$getPearlDataClasses
+ _objc_msgSend$getPropertyArrayFrom:
+ _objc_msgSend$getRegisterChangeDictUsingComponentAuthName:
+ _objc_msgSend$getRemoteTrustObjectDigestWithExistedDigest:digestData:error:
+ _objc_msgSend$getRepairDate:
+ _objc_msgSend$getRepairHistoryMap
+ _objc_msgSend$getRepairTicket:error:
+ _objc_msgSend$getSPCWithComponent:
+ _objc_msgSend$getSavageTicketForSavageFWUpdateWithOptions:SavageTicket:error:
+ _objc_msgSend$getSealDateFromSealingManifestData:
+ _objc_msgSend$getSealingMap
+ _objc_msgSend$getSsrBootIntentWithError:
+ _objc_msgSend$getStringFromCert:WithTag:AndOID:
+ _objc_msgSend$getStrongComponents
+ _objc_msgSend$getStrongComponentsWithError:resultobtained:
+ _objc_msgSend$getStrongComponentsWithReply:
+ _objc_msgSend$getSupportedComponentTypes
+ _objc_msgSend$getSupportedComponents
+ _objc_msgSend$getUnsealedSPCWithDataClass:
+ _objc_msgSend$getUpdateDataClassesAndInstancesWithPartSPC:withError:
+ _objc_msgSend$getUpdatePropertyWithPartSPC:propertiesFromParam:
+ _objc_msgSend$getValue:
+ _objc_msgSend$getYonkersTicketForYonkersFWUpdateWithOptions:YonkersTicket:error:
+ _objc_msgSend$handler
+ _objc_msgSend$hasCameraRepair:
+ _objc_msgSend$hasEntitlementBoolForTag:inAPTicket:
+ _objc_msgSend$hasHadRCHLBasedRepairForComponent:withHistory:
+ _objc_msgSend$hasInvalidRCHL
+ _objc_msgSend$hasMTUBRepair:
+ _objc_msgSend$hasPrefix:
+ _objc_msgSend$hasStrongIdentity
+ _objc_msgSend$hasSuffix:
+ _objc_msgSend$identifier
+ _objc_msgSend$identifierBase64
+ _objc_msgSend$indexSet
+ _objc_msgSend$initSealingMap
+ _objc_msgSend$initWithAuthInstallObj:
+ _objc_msgSend$initWithBase64EncodedString:options:
+ _objc_msgSend$initWithBytes:length:
+ _objc_msgSend$initWithBytes:length:encoding:
+ _objc_msgSend$initWithCapacity:
+ _objc_msgSend$initWithComponentName:CRComponentType:isRepaired:isUsed:repairDate:
+ _objc_msgSend$initWithComponentType:challenge:keyIndex:properties:
+ _objc_msgSend$initWithComponentType:identifier:asid:
+ _objc_msgSend$initWithComponentType:identifier:fwVersion:
+ _objc_msgSend$initWithComponentType:identifier:signedResponse:keyIndex:properties:
+ _objc_msgSend$initWithComponents:
+ _objc_msgSend$initWithData:encoding:
+ _objc_msgSend$initWithDictionary:
+ _objc_msgSend$initWithFormat:arguments:
+ _objc_msgSend$initWithID:param:requestFunction:responseFunction:
+ _objc_msgSend$initWithKeyBlob:
+ _objc_msgSend$initWithLocaleIdentifier:
+ _objc_msgSend$initWithMachServiceName:options:
+ _objc_msgSend$initWithName:
+ _objc_msgSend$initWithParameters:
+ _objc_msgSend$initWithPattern:options:error:
+ _objc_msgSend$initWithRefKey:certificates:certType:
+ _objc_msgSend$initWithServiceName:
+ _objc_msgSend$initWithSuiteName:
+ _objc_msgSend$initWithSuiteName:internalOnly:
+ _objc_msgSend$initWithTimeIntervalSince1970:
+ _objc_msgSend$initWithType:locKey:
+ _objc_msgSend$initWithType:locKey:spc:fdrKeys:
+ _objc_msgSend$initWithType:locKey:spc:fdrKeys:superModule:
+ _objc_msgSend$initWithrepairDateStr:repairDate:repairCenter:dataClasses:properties:
+ _objc_msgSend$insertItem:item:
+ _objc_msgSend$intValue
+ _objc_msgSend$integerValue
+ _objc_msgSend$interfaceWithProtocol:
+ _objc_msgSend$intersectSet:
+ _objc_msgSend$intersectsSet:
+ _objc_msgSend$invalidate
+ _objc_msgSend$invertedSet
+ _objc_msgSend$isAbsolutePath
+ _objc_msgSend$isComponentFailed
+ _objc_msgSend$isCompute1ProductType:
+ _objc_msgSend$isDataClassSupported:
+ _objc_msgSend$isDcSignedCombinedDataClass:error:
+ _objc_msgSend$isDcSignedComponent:error:
+ _objc_msgSend$isDcSignedDataClass:instance:error:
+ _objc_msgSend$isDcSignedSealingManifest:
+ _objc_msgSend$isDisplay1ProductType:
+ _objc_msgSend$isEANSupported
+ _objc_msgSend$isEqual:
+ _objc_msgSend$isEqualToData:
+ _objc_msgSend$isEqualToNumber:
+ _objc_msgSend$isEqualToSet:
+ _objc_msgSend$isEqualToString:
+ _objc_msgSend$isErrorResponse:
+ _objc_msgSend$isFDRDataClassSupported:
+ _objc_msgSend$isFDRPrimaryDataClass:
+ _objc_msgSend$isFDRPropertySupported:
+ _objc_msgSend$isFirstAuthComplete
+ _objc_msgSend$isGen1ProductType:
+ _objc_msgSend$isGen2ProductType:
+ _objc_msgSend$isGen3ProductType:
+ _objc_msgSend$isGen4ProductType:
+ _objc_msgSend$isGen5ProductType:
+ _objc_msgSend$isGen6ProductType:
+ _objc_msgSend$isGen7ProductType:
+ _objc_msgSend$isHorizonRamdiskBootInApticket:
+ _objc_msgSend$isLegacy2ProductType:
+ _objc_msgSend$isLegacyProductType:
+ _objc_msgSend$isPropertySupported:
+ _objc_msgSend$isRCHLRepairHistoryDevice
+ _objc_msgSend$isRepaired
+ _objc_msgSend$isSelfRepairedComponent:
+ _objc_msgSend$isSelfServiceSalesDistrict:
+ _objc_msgSend$isServicePart
+ _objc_msgSend$isServicePartWithError:
+ _objc_msgSend$isSubsetOfSet:
+ _objc_msgSend$isSupportedIPad
+ _objc_msgSend$isUsed
+ _objc_msgSend$isValidJSONObject:
+ _objc_msgSend$isiPad1ProductType:
+ _objc_msgSend$issueChallenge:index:reponse:options:connection:withError:
+ _objc_msgSend$issueClientCertificateWithCompletionOnQueue:withOptions:completion:
+ _objc_msgSend$issueRepairCert:keyBlob:error:
+ _objc_msgSend$issueRepairCert:withReply:
+ _objc_msgSend$itemWithName:
+ _objc_msgSend$kbbCGSN
+ _objc_msgSend$kbbSealDate
+ _objc_msgSend$kbbSealingManifest
+ _objc_msgSend$keyBlob
+ _objc_msgSend$keyIndex
+ _objc_msgSend$lastObject
+ _objc_msgSend$length
+ _objc_msgSend$lengthOfBytesUsingEncoding:
+ _objc_msgSend$locKey
+ _objc_msgSend$localManifestProperties
+ _objc_msgSend$localPatch:dataClasses:dataInstances:values:error:
+ _objc_msgSend$localTimeZone
+ _objc_msgSend$localizedDescription
+ _objc_msgSend$localizedStringForKey:value:table:
+ _objc_msgSend$localizedStringWithKey:
+ _objc_msgSend$lock
+ _objc_msgSend$longLongValue
+ _objc_msgSend$lowercaseString
+ _objc_msgSend$makeClasses
+ _objc_msgSend$makeInstances
+ _objc_msgSend$makeProperties
+ _objc_msgSend$mergedDataClasses
+ _objc_msgSend$mergedDataInstances
+ _objc_msgSend$miniPreflight
+ _objc_msgSend$minusSet:
+ _objc_msgSend$mlbRepairChecks
+ _objc_msgSend$mutableBytes
+ _objc_msgSend$mutableCopy
+ _objc_msgSend$name
+ _objc_msgSend$nextEANGenerationCount
+ _objc_msgSend$nonce
+ _objc_msgSend$null
+ _objc_msgSend$numberOfRanges
+ _objc_msgSend$numberWithBool:
+ _objc_msgSend$numberWithDouble:
+ _objc_msgSend$numberWithInt:
+ _objc_msgSend$numberWithInteger:
+ _objc_msgSend$numberWithUnsignedInt:
+ _objc_msgSend$numberWithUnsignedInteger:
+ _objc_msgSend$objectAtIndex:
+ _objc_msgSend$objectAtIndexedSubscript:
+ _objc_msgSend$objectForKey:
+ _objc_msgSend$objectForKeyedSubscript:
+ _objc_msgSend$overrideFromNVRam:
+ _objc_msgSend$overrideParameters:
+ _objc_msgSend$param
+ _objc_msgSend$parseChallengeObject:withHandler:
+ _objc_msgSend$partSPC
+ _objc_msgSend$patchDataClasses
+ _objc_msgSend$patchDataInstances
+ _objc_msgSend$patchValues
+ _objc_msgSend$patchWithOptions:amfdr:dataClasses:dataInstances:values:datas:error:local:
+ _objc_msgSend$path
+ _objc_msgSend$payload
+ _objc_msgSend$performHTTPChallengeClaim:fdrLocal:fdrError:claimClassDict:registerOnly:
+ _objc_msgSend$performMake:fdrLocal:fdrError:
+ _objc_msgSend$performPostSealingStage:
+ _objc_msgSend$performRealToRealRepair:fdrLocal:fdrRemote:
+ _objc_msgSend$performRealToStagedRepair:fdrLocal:fdrRemote:
+ _objc_msgSend$performSealing:fdrLocal:fdrError:
+ _objc_msgSend$performStagedChallengeClaim:fdrLocal:fdrError:claimClassDict:
+ _objc_msgSend$performStagedMake:fdrLocal:fdrError:
+ _objc_msgSend$performStagedSealing:fdrLocal:fdrError:
+ _objc_msgSend$performStagedToRealRepair:fdrLocal:fdrRemote:
+ _objc_msgSend$performStagedToStagedRepair:fdrLocal:fdrRemote:
+ _objc_msgSend$persistentDomainForName:
+ _objc_msgSend$personalizationMeasurementCreator
+ _objc_msgSend$personalizationResponseParser
+ _objc_msgSend$personalizeVeridianWithError:parsedResponseData:
+ _objc_msgSend$personalizeWithElements:error:
+ _objc_msgSend$phase
+ _objc_msgSend$populateDCSignedComponents
+ _objc_msgSend$populateIssueComponents
+ _objc_msgSend$populateLookupDictionary:
+ _objc_msgSend$populateRCHLHistory
+ _objc_msgSend$populateUnsealedComponents
+ _objc_msgSend$powerCycleSensor:
+ _objc_msgSend$predicateWithFormat:
+ _objc_msgSend$prefetchPermissionsForSealing:fdrRemote:fdrLocal:claimClassDict:makeClasses:makeInstances:patchClasses:patchInstances:
+ _objc_msgSend$prefetchPermissionsForStagedSealing:fdrRemote:fdrLocal:claimClassDict:makeClasses:makeInstances:patchClasses:patchInstances:
+ _objc_msgSend$prefetchPermissionsWith:returnError:
+ _objc_msgSend$preflightPhase1:withReply:
+ _objc_msgSend$preflightPhase2:withReply:
+ _objc_msgSend$previousCGSN
+ _objc_msgSend$processInfo
+ _objc_msgSend$processName
+ _objc_msgSend$progressWithTotalUnitCount:
+ _objc_msgSend$properties
+ _objc_msgSend$propertyListWithData:options:format:error:
+ _objc_msgSend$protectionSpace
+ _objc_msgSend$prpcSign:outSignature:outDeviceNonce:outError:
+ _objc_msgSend$pubKeyBlob
+ _objc_msgSend$purge
+ _objc_msgSend$queryDeviceStagedSealedFromEAN:error:
+ _objc_msgSend$queryRepairDelta:error:
+ _objc_msgSend$queryRepairDeltaWithReply:
+ _objc_msgSend$raise:format:
+ _objc_msgSend$range
+ _objc_msgSend$rangeAtIndex:
+ _objc_msgSend$rangeOfString:
+ _objc_msgSend$rawRCHLBasedRepairDateForComponent:withHistory:
+ _objc_msgSend$rawResponse
+ _objc_msgSend$readAccessPointInfo
+ _objc_msgSend$readDataOfLength:
+ _objc_msgSend$readFDRDataFromEANWithDataClass:outData:stripPadding:
+ _objc_msgSend$readNVRAMValueForKey:error:
+ _objc_msgSend$readSystemConfigAll
+ _objc_msgSend$readSystemConfigArea
+ _objc_msgSend$referenceKey
+ _objc_msgSend$regularExpressionWithPattern:options:error:
+ _objc_msgSend$remoteObjectInterface
+ _objc_msgSend$remoteObjectProxy
+ _objc_msgSend$remoteObjectProxyWithErrorHandler:
+ _objc_msgSend$remotePatch:dataClasses:dataInstances:values:datas:error:
+ _objc_msgSend$removeItemAtPath:error:
+ _objc_msgSend$removeObject:
+ _objc_msgSend$removeObjectAtIndex:
+ _objc_msgSend$removeObjectsAtIndexes:
+ _objc_msgSend$removeObjectsForKeys:
+ _objc_msgSend$repairCenter
+ _objc_msgSend$repairCenterForComponent:withRCHLHistory:
+ _objc_msgSend$repairDate
+ _objc_msgSend$repairDateForComponent:withRCHLHistory:withCAAHistory:
+ _objc_msgSend$repairDateStr
+ _objc_msgSend$replaceBytesInRange:withBytes:
+ _objc_msgSend$replyWithError:reply:
+ _objc_msgSend$replyWithMessage:status:results:reply:
+ _objc_msgSend$request
+ _objc_msgSend$requestBAACertificates:apticket:proxySettings:withError:
+ _objc_msgSend$requestID
+ _objc_msgSend$requestWithURL:cachePolicy:timeoutInterval:
+ _objc_msgSend$resetBytesInRange:
+ _objc_msgSend$resume
+ _objc_msgSend$rk
+ _objc_msgSend$safeGetStringParam:key:
+ _objc_msgSend$seal:oldSealingManifest:newSealingManifest:stats:
+ _objc_msgSend$seal:withReply:
+ _objc_msgSend$sealDate
+ _objc_msgSend$sealWithDataClass:fdrError:registerOnly:
+ _objc_msgSend$sendBAARequest:options:withReply:
+ _objc_msgSend$sendCertIssueRequestWith:serverCertResponse:error:
+ _objc_msgSend$sendChallengeRequestWith:serverResponse:error:
+ _objc_msgSend$sendPreflightRequest:options:withReply:
+ _objc_msgSend$sendRequest:keyBlob:error:
+ _objc_msgSend$server
+ _objc_msgSend$serverTrust
+ _objc_msgSend$sessionID
+ _objc_msgSend$sessionWithConfiguration:delegate:delegateQueue:
+ _objc_msgSend$set
+ _objc_msgSend$setActivationResponses:
+ _objc_msgSend$setAllowFactoryReset:
+ _objc_msgSend$setAllowMissingData:
+ _objc_msgSend$setAttributes:ofItemAtPath:error:
+ _objc_msgSend$setBatteryDateOfFirstUse:error:
+ _objc_msgSend$setBikCertificate:
+ _objc_msgSend$setBootIntentWithLocale:error:
+ _objc_msgSend$setByAddingObject:
+ _objc_msgSend$setClasses:forSelector:argumentIndex:ofReply:
+ _objc_msgSend$setCompletedUnitCount:
+ _objc_msgSend$setComponentName:
+ _objc_msgSend$setComponentResponses:
+ _objc_msgSend$setComponents:
+ _objc_msgSend$setComponentsState:withResponseDetails:
+ _objc_msgSend$setConnectionProxyDictionary:
+ _objc_msgSend$setData:
+ _objc_msgSend$setDateFormat:
+ _objc_msgSend$setDateStyle:
+ _objc_msgSend$setDelegate:
+ _objc_msgSend$setFailedSPC:
+ _objc_msgSend$setFormattingContext:
+ _objc_msgSend$setHTTPBody:
+ _objc_msgSend$setHTTPMethod:
+ _objc_msgSend$setKBBDataClasses:
+ _objc_msgSend$setKBBDataInstances:
+ _objc_msgSend$setKBBECID:
+ _objc_msgSend$setKBBMLBSerialNumber:
+ _objc_msgSend$setKBBSIK:
+ _objc_msgSend$setKBBSealInstance:
+ _objc_msgSend$setKBBSerialNumber:
+ _objc_msgSend$setKBBTransferProperties:
+ _objc_msgSend$setKGBSerialNumber:
+ _objc_msgSend$setKbbCGSN:
+ _objc_msgSend$setKbbSealDate:
+ _objc_msgSend$setKbbSealingManifest:
+ _objc_msgSend$setLocalAndRemotePermission:fdrRemote:
+ _objc_msgSend$setLocalAndRemoteTrustObject:fdrLocal:remoteTrustObjectDigest:fdrError:
+ _objc_msgSend$setLocale:
+ _objc_msgSend$setMinimalSealingMeta:hintDataClass:sealingInstances:
+ _objc_msgSend$setNVRAMValueForKey:value:error:
+ _objc_msgSend$setObject:forKey:
+ _objc_msgSend$setObject:forKeyedSubscript:
+ _objc_msgSend$setParam:
+ _objc_msgSend$setPhase:
+ _objc_msgSend$setPreviousCGSN:
+ _objc_msgSend$setRemoteObjectInterface:
+ _objc_msgSend$setRequestID:
+ _objc_msgSend$setRk:
+ _objc_msgSend$setSealDate:
+ _objc_msgSend$setServer:
+ _objc_msgSend$setSessionID:
+ _objc_msgSend$setSignatureChallenge:
+ _objc_msgSend$setState:
+ _objc_msgSend$setTimeStyle:
+ _objc_msgSend$setTimeZone:
+ _objc_msgSend$setURL:
+ _objc_msgSend$setValue:forHTTPHeaderField:
+ _objc_msgSend$setValue:forKey:
+ _objc_msgSend$setWithArray:
+ _objc_msgSend$setWithObject:
+ _objc_msgSend$setWithObjects:
+ _objc_msgSend$setWithSet:
+ _objc_msgSend$setupAlternativeFDRPath:
+ _objc_msgSend$setupFileSystemForRepair
+ _objc_msgSend$setupModuleChallengeCallBack:
+ _objc_msgSend$setupVersionedFDRWithApTicket:
+ _objc_msgSend$sha256:
+ _objc_msgSend$sha256Data:
+ _objc_msgSend$sharedAccess
+ _objc_msgSend$sharedDataAccessor
+ _objc_msgSend$sharedInstance
+ _objc_msgSend$sharedManager
+ _objc_msgSend$sharedSingleton
+ _objc_msgSend$shouldIgnorePatching:
+ _objc_msgSend$shouldPersonalizeWithSSOByDefault
+ _objc_msgSend$sign:
+ _objc_msgSend$sign:keyBlob:
+ _objc_msgSend$sign:keyBlob:withReply:
+ _objc_msgSend$signDisplayRoswellWith:withReply:
+ _objc_msgSend$signVeridianChallenge:completionHandler:
+ _objc_msgSend$signVeridianWith:withReply:
+ _objc_msgSend$signatureChallenge
+ _objc_msgSend$signbatteryRoswellWith:withReply:
+ _objc_msgSend$signedResponse
+ _objc_msgSend$sizeEAN:
+ _objc_msgSend$skipStageEAN
+ _objc_msgSend$socksHost
+ _objc_msgSend$socksPort
+ _objc_msgSend$spc
+ _objc_msgSend$spcInPartSPC:withDataClass:
+ _objc_msgSend$spcResults:
+ _objc_msgSend$spcWithComponent:withIdentifier:
+ _objc_msgSend$specVersion
+ _objc_msgSend$stageDataClasses:dataInstances:fdrRemote:fdrLocal:fdrError:
+ _objc_msgSend$stageVersionedFDREANWithdataDir:error:
+ _objc_msgSend$state
+ _objc_msgSend$status
+ _objc_msgSend$statusCode
+ _objc_msgSend$storeWarningStrings:
+ _objc_msgSend$string
+ _objc_msgSend$stringByAppendingPathComponent:
+ _objc_msgSend$stringByAppendingString:
+ _objc_msgSend$stringByDeletingLastPathComponent
+ _objc_msgSend$stringByReplacingOccurrencesOfString:withString:
+ _objc_msgSend$stringByStrippingPrefix:
+ _objc_msgSend$stringByTrimmingCharactersInSet:
+ _objc_msgSend$stringForKey:
+ _objc_msgSend$stringFromDate:
+ _objc_msgSend$stringValue
+ _objc_msgSend$stringWithCapacity:
+ _objc_msgSend$stringWithContentsOfFile:encoding:error:
+ _objc_msgSend$stringWithFormat:
+ _objc_msgSend$stringWithString:
+ _objc_msgSend$stringWithUTF8String:
+ _objc_msgSend$subdataWithRange:
+ _objc_msgSend$substringFromIndex:
+ _objc_msgSend$substringToIndex:
+ _objc_msgSend$substringWithRange:
+ _objc_msgSend$summarizePatchInputs
+ _objc_msgSend$supportArgonRepair
+ _objc_msgSend$supportCameraDepth
+ _objc_msgSend$supportElabel
+ _objc_msgSend$supportHarvestPearl
+ _objc_msgSend$supportMctubMinus
+ _objc_msgSend$supportMesaRepair
+ _objc_msgSend$supportPatch
+ _objc_msgSend$supportRepair:
+ _objc_msgSend$swapEAN:withKey:
+ _objc_msgSend$swapVersionedFDR
+ _objc_msgSend$syncAlternativeFDRPath
+ _objc_msgSend$syncFDRDataAtPath:toPath:
+ _objc_msgSend$syncSysConfig:key:inBuffer:
+ _objc_msgSend$synchronize
+ _objc_msgSend$synchronousRemoteObjectProxyWithErrorHandler:
+ _objc_msgSend$syscfgUpdate:key:buffer:length:
+ _objc_msgSend$tcrtSign:outSignature:outDeviceNonce:outError:
+ _objc_msgSend$timeIntervalSince1970
+ _objc_msgSend$timeIntervalSinceDate:
+ _objc_msgSend$timeIntervalSinceLastSealing:
+ _objc_msgSend$timeIntervalSinceNow
+ _objc_msgSend$timeIntervalSinceReferenceDate
+ _objc_msgSend$timeZoneWithName:
+ _objc_msgSend$transformChallengeResponseWithError:blockChallengeResponse:resultobtained:
+ _objc_msgSend$transformServerCertResponseUsing:serverCertResponseArray:error:
+ _objc_msgSend$transformStrongWithError:blockComponents:resultobtained:
+ _objc_msgSend$type
+ _objc_msgSend$unionSet:
+ _objc_msgSend$unlock
+ _objc_msgSend$unsignedIntegerValue
+ _objc_msgSend$unsignedLongLongValue
+ _objc_msgSend$updateBrunorDATFirmware
+ _objc_msgSend$updateClassDict
+ _objc_msgSend$updateProperties
+ _objc_msgSend$updateSavageDATFirmware
+ _objc_msgSend$userInfo
+ _objc_msgSend$validateAndFilterPatchWithPartSPC:patchClasses:patchInstances:patchValues:validClasses:validInstances:error:
+ _objc_msgSend$validateAndSetSerialNumbersUsingPartSPC:KGBSerialNumber:KBBSerialNumber:withError:
+ _objc_msgSend$validateDisplaySwapped:lessThan:
+ _objc_msgSend$validateSwappedForDays:currentSN:previousSN:sealDate:
+ _objc_msgSend$valueForEntitlement:
+ _objc_msgSend$valueForKey:
+ _objc_msgSend$valueWithBytes:objCType:
+ _objc_msgSend$vcrtSign:outSignature:outDeviceNonce:outError:
+ _objc_msgSend$verify:signature:
+ _objc_msgSend$verify:signature:keyBlob:
+ _objc_msgSend$verify:signature:keyBlob:withReply:
+ _objc_msgSend$verifyClaimCountAndSalesDistrictWithError:
+ _objc_msgSend$verifyFDRDataFromEANUsingCache:cachedData:
+ _objc_msgSend$verifyPSD3
+ _objc_msgSend$warnings
+ _objc_msgSend$withStatus:
+ _objc_msgSend$writeFDRDataToEANWithdataDir:
+ _objc_msgSend$writeSystemConfig:inBuffer:
+ _objc_msgSend$writeToFile:atomically:
+ _objc_opt_self
+ _os_signpost_enabled
+ _os_signpost_id_generate
+ _parsePersonalizationResponseForLthTransfer
+ _parsePersonalizationResponseForLthTransfer_block_invoke_16
+ _parsePersonalizationResponseForLthTransfer_block_invoke_16.cold.1
+ _parsePersonalizationResponseForLthTransfer_block_invoke_16.cold.2
+ _parsePersonalizationResponseForPDI
+ _parsePersonalizationResponseForPDI_block_invoke_6
+ _parsePersonalizationResponseForPDI_block_invoke_6.cold.1
+ _parsePersonalizationResponseForPDI_block_invoke_6.cold.2
+ _parsePersonalizationResponseForSavageFW
+ _parsePersonalizationResponseForSavageFW_block_invoke_10
+ _parsePersonalizationResponseForSavageFW_block_invoke_10.cold.1
+ _parsePersonalizationResponseForSavageFW_block_invoke_10.cold.2
+ _parsePersonalizationResponseForSavageUpdaterTicket
+ _parsePersonalizationResponseForSavageUpdaterTicket_block_invoke_17
+ _parsePersonalizationResponseForSavageUpdaterTicket_block_invoke_17.cold.1
+ _parsePersonalizationResponseForSavageUpdaterTicket_block_invoke_17.cold.2
+ _parsePersonalizationResponseForSavageUpdaterTicket_block_invoke_17.cold.3
+ _parsePersonalizationResponseForSavageUpdaterTicket_block_invoke_17.cold.4
+ _parsePersonalizationResponseForSavageUpdaterTicket_block_invoke_17.cold.5
+ _parsePersonalizationResponseForSeaCookiePairing
+ _parsePersonalizationResponseForSeaCookiePairing_block_invoke_14
+ _parsePersonalizationResponseForSeaCookiePairing_block_invoke_14.cold.1
+ _parsePersonalizationResponseForSeaCookiePairing_block_invoke_14.cold.2
+ _parsePersonalizationResponseForTrustObject
+ _parsePersonalizationResponseForTrustObject_block_invoke
+ _parsePersonalizationResponseForTrustObject_block_invoke.cold.1
+ _parsePersonalizationResponseForTrustObject_block_invoke.cold.2
+ _parsePersonalizationResponseForTrustObject_block_invoke.cold.3
+ _parsePersonalizationResponseForTrustObject_block_invoke.cold.4
+ _parsePersonalizationResponseForTrustObject_block_invoke.cold.5
+ _parsePersonalizationResponseForVeridianFW
+ _parsePersonalizationResponseForVeridianFW_block_invoke_9
+ _parsePersonalizationResponseForVeridianFW_block_invoke_9.cold.1
+ _parsePersonalizationResponseForVeridianFW_block_invoke_9.cold.2
+ _parsePersonalizationResponseForYonkersFW
+ _parsePersonalizationResponseForYonkersFW_block_invoke_12
+ _parsePersonalizationResponseForYonkersFW_block_invoke_12.cold.1
+ _parsePersonalizationResponseForYonkersFW_block_invoke_12.cold.2
+ _parseRepairTicket
+ _parseRepairTicket_block_invoke_3
+ _parseRepairTicket_block_invoke_3.cold.1
+ _parseRepairTicket_block_invoke_3.cold.2
+ _performCommand
+ _performCommand.cold.1
+ _resetSensor
+ _resetSensor.cold.1
+ _sharedAccess.once
+ _sharedAccess.sharedInstance
+ _sharedInstance.instance
+ _sharedInstance.onceToken
+ _sharedSingleton.once
+ _sharedSingleton.sharedInstance
+ _signChallenge
+ _signChallenge.cold.1
+ _signChallenge.cold.10
+ _signChallenge.cold.2
+ _signChallenge.cold.3
+ _signChallenge.cold.4
+ _signChallenge.cold.5
+ _signChallenge.cold.6
+ _signChallenge.cold.7
+ _signChallenge.cold.8
+ _signChallenge.cold.9
+ _updater_log
+ _verifyFDRData
+ _verifyFDRData.cold.1
+ _verifyFDRData.cold.2
+ _verifyFDRData.cold.3
+ _verifyFDRData.cold.4
+ _verifyFDRData.cold.5
+ _verifyFDRData.cold.6
+ _verifyFDRData.cold.7
- _AMFDRSealedDataSetMinimalManifestClassInstance
- _OBJC_CLASS_$_CRAttestationHandler
- _kBrunorTagResponseTicket
CStrings:
+ "%08llX"
+ "%@ has no localized name"
+ "%@ has no part name"
+ "%@ is not a valid SPC"
+ "%@ ticket not found in response"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s aks connection failed%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s bad 1%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s fail%s\n"
+ "+[CRDaemonController controlWithParametersImpl:withReply:]"
+ "/Library/Caches/com.apple.xbs/Sources/Mesa/AppleBiometricServices/MesaFactoryC/MesaFactoryC.c"
+ "/tmp/baa_request"
+ "0x%@"
+ "@\"CRDeviceComponent\""
+ "@\"NSData\"32@?0@\"NSMutableDictionary\"8@\"NSDictionary\"16^@24"
+ "@\"NSData\"32@?0@8@\"NSDictionary\"16^@24"
+ "@\"NSLock\""
+ "@28@0:8@16B24"
+ "@28@0:8@16i24"
+ "@32@?0@8@\"NSDictionary\"16^@24"
+ "@36@0:8i16@20@28"
+ "@44@0:8@16i24B28B32@36"
+ "@52@0:8i16@20@28@36@44"
+ "AMFDRSealedDataSetMinimalManifestClassInstanceWithVersions failed with error: %@"
+ "AMFDRSealingMapCopyDataClassesWithAttribute EarlyAccess returned error%@."
+ "AMFDRSealingMapCopyDataClassesWithAttribute EarlyAccessMultiData returned error %@."
+ "Add Pearl ticket failed"
+ "Add Pearl ticket failed: %@"
+ "Add response ticket ..."
+ "AddResponseTicketForSavageUpdaterOptions:auth:error:"
+ "Additional PATCH is not allowed when transit from staged to real sealing"
+ "Additional UPDATE properties is not allowed when transit from staged to real sealing"
+ "Ap,AuthorizeRepairService"
+ "AppleBiometricServices"
+ "AuthCP Components: %@"
+ "B24@0:8^i16"
+ "B28@0:8i16@20"
+ "B36@0:8@16B24^@28"
+ "B36@0:8i16@20@28"
+ "B40@0:8^{__AMFDR=}16@24@32"
+ "B56@0:8@16^@24^@32^@40^@48"
+ "B56@0:8^@16^@24@32@40^@48"
+ "B56@0:8^@16^@24^@32^@40^@48"
+ "B56@0:8^{__AMFDR=}16^@24^@32^@40^@48"
+ "B64@0:8^@16^{__AMFDR=}24^@32^@40^@48^@56"
+ "B72@0:8@16^@24^@32^@40@48@56^@64"
+ "B80@0:8@16^{__AMFDR=}24^{__AMFDR=}32^@40^@48^@56^@64^@72"
+ "BIK:%@ Certs:%@"
+ "CAABasedRepairForComponent:withHistory:"
+ "CRAttestationHelper"
+ "CRBootIntentController"
+ "CRFDRGen7DeviceHandler"
+ "CRFDRLegacy2DeviceHandler"
+ "CRFDRRetryController"
+ "CRMesaController"
+ "CRRepairHistoryItem"
+ "Call corerepaird to control daemon: %@"
+ "Challenge responseArray: %@"
+ "Clear PhysicalPresence failed: 0x%x"
+ "Clear PhysicalPresence successfully"
+ "Component %@ has no keys"
+ "ComponentState"
+ "CoreRepairCoreNetworkXPCServiceProtocol"
+ "Couldn't create OS Log for 'com.apple.BiometricKit.Library-MesaFactory'!\n"
+ "DumpBAARequest"
+ "Empty bundleDataDict"
+ "Enable proxy for attestation, host: %@, port: %@"
+ "Excluded properties for sealed verify: %@"
+ "FSC2"
+ "Failed get sepi digest with error: 0x%X"
+ "Failed to KBB data info"
+ "Failed to clear boot intent"
+ "Failed to decode base64 identifier"
+ "Failed to decode sealing manifest"
+ "Failed to fetch properties, error: %@"
+ "Failed to get KBB seal manifest"
+ "Failed to get SavageChipID"
+ "Failed to get filtered components"
+ "Failed to get response tags"
+ "Failed to get sensor type: 0x%x"
+ "Failed to read apTicketData"
+ "Failed to set boot intent"
+ "Fetched live instance: %@"
+ "File not exists in path: %@"
+ "Force%@Status"
+ "ForceRepaired"
+ "ForceUsed"
+ "Get PhysicalPresenceAsserted failed: 0x%x"
+ "Get make dataClasses failed"
+ "GetComponentStateXPC"
+ "Getting CAA for Repair History"
+ "HTTPBody"
+ "Has update data, continue to recover"
+ "Image size: %lu DER size: %ld"
+ "Invalid identifier type: %@"
+ "Invalid patch classes ignored: %@"
+ "Invalid patch data instances count."
+ "Invalid patch instances ignored: %@"
+ "Invalid patch values count."
+ "Invalid patch values ignored: %@"
+ "KBBDataClasses"
+ "KBBDataInstances"
+ "KBBECID"
+ "KBBSIK"
+ "KEYBOARD"
+ "KGB isServicePart without McMinus SPC"
+ "Key not in component map: %@"
+ "Library-MesaFactory"
+ "LogicBoard"
+ "MLB TOUCHID REUSE"
+ "MPU"
+ "Make dataClasses from KBB: %@"
+ "Mesa protocol version %d"
+ "Mesa sensor type: 0x%x"
+ "Microphone"
+ "Missing buildIdentityDict"
+ "Missing required patch info."
+ "Network XPC call failed"
+ "No excluded properties for sealed verify, skipping."
+ "PART_"
+ "PART_BACK_GLASS"
+ "PART_BATTERY"
+ "PART_COVER_GLASS"
+ "PART_DISPLAY"
+ "PART_ENCLOSURE"
+ "PART_LOGIC_BOARD"
+ "PART_MAIN_MIC"
+ "PART_REAR_CAMERA"
+ "PART_TOUCH_ID"
+ "PART_TRUE_DEPTH_CAMERA"
+ "PART_VOLUME_BUTTON"
+ "Parsing response ticket %@"
+ "Patch error ignored: %@"
+ "Patch validation failed: %@"
+ "Perform next stage: %@"
+ "Phase"
+ "Physical Presence -> %d"
+ "Properties: %@"
+ "RC"
+ "RECOVER"
+ "ResponseTags"
+ "Retry is already enabled"
+ "SECURE MODULE"
+ "SPEAKER"
+ "SSD"
+ "SYSTEM"
+ "SavageChipID is too short"
+ "Sealed system manifest: %@"
+ "Server response missing:%@"
+ "Set boot intent and boot command"
+ "Skip reading unknown Mesa: %@"
+ "Strong components: %@"
+ "T@\"CRDeviceComponent\",&,N,V_superModule"
+ "T@\"NSArray\",&,N,V_KBBDataClasses"
+ "T@\"NSArray\",&,N,V_KBBDataInstances"
+ "T@\"NSArray\",&,N,V_minimalSealedVersions"
+ "T@\"NSDictionary\",&,N,V_spcToComponent"
+ "T@\"NSString\",&,N,V_KBBECID"
+ "T@\"NSString\",&,N,V_KBBSIK"
+ "T@\"NSString\",&,N,V_componentName"
+ "T@\"NSString\",&,N,V_repairDate"
+ "T@\"NSString\",N,V_locKey"
+ "TB,N,V_hasStrongIdentity"
+ "TB,N,V_isRepaired"
+ "TB,N,V_isUsed"
+ "TB,N,V_supportElabel"
+ "Ti,N,V_componentType"
+ "UNDEFINED"
+ "Unable to fetch drp#: %@"
+ "Unable to get ChipID"
+ "Unable to get chipId"
+ "Unable to get identifier: %@"
+ "Unable to get make dataClasses: %@"
+ "Unable to get mesa provisioning state: %d"
+ "Unable to read Pearl identifier:%@"
+ "Unexpected Yonkers ticket in auth flow"
+ "Unknown"
+ "Unsupported Class:%d::Product:%lld"
+ "Utils"
+ "WIRELESS DEVICE"
+ "[CRRepairHistoryItem: componentName:%@: componentType:%d: isRepaired:%d: isUsed:%d: repairDate:%@:]"
+ "_KBBDataClasses"
+ "_KBBDataInstances"
+ "_KBBECID"
+ "_KBBSIK"
+ "_checkStrongIdentity:"
+ "_compareSealedAndLiveDataClasses:instances:liveClasses:liveInstances:results:"
+ "_compareSerialNumberProperties:missingLiveData:results:"
+ "_componentName"
+ "_componentType"
+ "_getAllLiveDataClasses:liveInstances:missingLiveData:mesaState:error:"
+ "_getAllSealedDataAndPropertiesFromManifest:properties:classes:instances:error:"
+ "_getMesaState"
+ "_getPropertiesFromSealingMap"
+ "_getPropertyArrayFrom:"
+ "_getUnsealedMesaData:mesaState:"
+ "_hasStrongIdentity"
+ "_isRepaired"
+ "_isUsed"
+ "_locKey"
+ "_lock"
+ "_minimalSealedVersions"
+ "_refCount"
+ "_sendBAARequest:proxySettings:withError:"
+ "_spcToComponent"
+ "_superModule"
+ "_supportElabel"
+ "arc#"
+ "async"
+ "authFlow"
+ "bundleForClass:"
+ "caaSocksHost"
+ "caaSocksPort"
+ "cert der length:%lu"
+ "clearBootIntentAndReboot:"
+ "clearBootIntentWithError:"
+ "clearPhysicalPresence"
+ "com.apple.CoreRepairCoreNetworkXPCService"
+ "com.apple.mobilerepaird"
+ "component %d"
+ "component %d not defined: %@"
+ "componentMap"
+ "control != kMesaFactoryPhysicalPresenceGetState || state"
+ "control < kMesaFactoryPhysicalPresenceCount"
+ "controlWithParametersImpl:withReply:"
+ "disable query retry"
+ "disableRetry"
+ "enable query retry"
+ "enableRetry"
+ "failed to open connection to %s: %d\n"
+ "failed to open userclient via %s: %d\n"
+ "fetched RCHL successfully: %{public}@ length = %lu"
+ "filteredPhase2Components:response:"
+ "findRCHLHistoryObjectForComponent:withHistory:"
+ "formatString must contain exactly one placeholder"
+ "getBackglassDataClasses"
+ "getCAAForRepairHistoryWithCompletion:"
+ "getCameraDataClasses"
+ "getComponentBySPC:"
+ "getComponentNameWithSPC:"
+ "getComponentTypeWithSPC:"
+ "getCurrentMinimalManifestsWithVersions:fdrRemote:minimalSealingDataInstances:minimalSealedDataClasses:minimalSealedDataInstances:minimalSealedVersions:"
+ "getDataClassesAndInstancesOfKBBWith:dataClasses:dataInstances:propertiesDict:fdrError:"
+ "getExcludedPropertiesForSealedVerify"
+ "getInternalName:"
+ "getKBBMinimalManifestsWithVersions:minimalSealingDataInstances:minimalSealedDataClasses:minimalSealedDataInstances:minimalSealedVersions:"
+ "getLocalSealingManifestWithError:"
+ "getLocalizationKey:"
+ "getMTUBDataClasses"
+ "getMacSupportedSPCs"
+ "getMinimalManifestsClassesAndInstancesWithPartSPC:fdrLocal:fdrRemote:minimalSealingDataInstances:minimalSealedDataClasses:minimalSealedDataInstances:minimalSealedVersions:error:"
+ "getPearlDataClasses"
+ "getProtocolVersion"
+ "getRepairDate:"
+ "getRepairHistoryItemswithCAAHistory:"
+ "getRepairHistoryMap"
+ "getSPCWithComponent:"
+ "getSensorProvisioningState -> err:0x%x, state:%d\n"
+ "getSensorProvisioningState(%p)\n"
+ "getSensorType -> err:0x%x, type:%d\n"
+ "getSensorType(%p)\n"
+ "hasCameraRepair:"
+ "hasEntitlementAATC"
+ "hasMTUBRepair:"
+ "hasMesa"
+ "hasMesaUnsealedData"
+ "hasStrongIdentity"
+ "initWithComponentName:CRComponentType:isRepaired:isUsed:repairDate:"
+ "initWithSuiteName:internalOnly:"
+ "initWithType:locKey:"
+ "initWithType:locKey:spc:fdrKeys:"
+ "initWithType:locKey:spc:fdrKeys:superModule:"
+ "initWithType:locKey:superModule:fdrKeys:"
+ "isEqualToNumber:"
+ "isGen7ProductType:"
+ "isInternal: %@, isProduction: %@, hasAATC: %@"
+ "isLegacy2ProductType:"
+ "isPaired:"
+ "isPhysicalPresenceAsserted"
+ "isPropertySupported:"
+ "isRepaired"
+ "isStrongComponent:"
+ "isUsed"
+ "kbbECID"
+ "kbbSIK"
+ "lidar-scanner"
+ "locKey"
+ "localizedStringWithFormat:component:"
+ "m9OWD0Y4Br0TZHUl6rGcOg"
+ "mesa paired with unknown key"
+ "minimalSealedVersions"
+ "number of ranges:%lu"
+ "rawRCHLBasedRepairDateForComponent:withHistory:"
+ "repairHistory: %@ error: %@"
+ "repairHistoryForUI:%@"
+ "repairticket: %{private}@"
+ "responseTags"
+ "responseTags missing"
+ "savageFirmware"
+ "savageUpdaterTicket"
+ "sendActivationRequest:options:withReply:"
+ "sendBAARequest:options:withReply:"
+ "sendPreflightRequest:options:withReply:"
+ "sendRequest:keyBlob:error:"
+ "setBootIntentWithLocale:error:"
+ "setHasStrongIdentity:"
+ "setIsRepaired:"
+ "setIsUsed:"
+ "setKBBDataClasses:"
+ "setKBBDataInstances:"
+ "setKBBECID:"
+ "setKBBSIK:"
+ "setLocKey:"
+ "setMinimalSealedVersions:"
+ "setMinimalSealingMeta:hintDataClass:sealingInstances:"
+ "setPhysicalPresence -> err:0x%x\n"
+ "setPhysicalPresence(control:%d, state:%p)\n"
+ "setSpcToComponent:"
+ "setSuperModule:"
+ "setSupportElabel:"
+ "signpost"
+ "sik-%@-%@-%@"
+ "size == sizeof(sensorInfo)"
+ "size == sizeof(state)"
+ "spcToComponent"
+ "stringByStrippingPrefix:"
+ "super getMakeDataClassesAndInstancesWithPartSPC failed"
+ "superModule"
+ "supportArgonRepair"
+ "supportElabel"
+ "supportLiDAR"
+ "supportPeCoNet"
+ "supportRepair:"
+ "temp make properties: %@"
+ "transferring properties: %@"
+ "unlock"
+ "unsealed mesa: %@"
+ "unsignedLongLongValue"
+ "v28@?0@\"NSArray\"8i16@\"NSError\"20"
+ "v28@?0@\"NSDictionary\"8i16@\"NSError\"20"
+ "v28@?0B8@\"CRCCertificate\"12@\"NSError\"20"
+ "v40@0:8@\"NSURLRequest\"16@\"NSDictionary\"24@?<v@?@\"NSArray\"i@\"NSError\">32"
+ "v40@0:8@\"NSURLRequest\"16@\"NSDictionary\"24@?<v@?@\"NSData\"@\"NSURLResponse\"@\"NSError\">32"
+ "v40@0:8@\"NSURLRequest\"16@\"NSDictionary\"24@?<v@?@\"NSDictionary\"i@\"NSError\">32"
+ "v40@0:8@16@24@32"
+ "v56@0:8@16@24@32@40@48"
+ "validateAndFilterPatchWithPartSPC:patchClasses:patchInstances:patchValues:validClasses:validInstances:error:"
+ "yonkersFirmware"
+ "\xf0\xd1"
- "%s%s:%s%s%s%s%u:%s%u:%s aks connection failed%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s bad 1%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s bad 2%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s fail%s\n"
- "+[CRDaemonController controlWithParameters:withReply:]"
- "-----BEGIN CERTIFICATE-----(.+?)-----END CERTIFICATE-----\n"
- "/System/Library/PrivateFrameworks/CoreRepairCore.framework"
- "0x5065"
- "@\"CRAttestationBaseDeviceHandler\""
- "@\"NSData\"24@?0@\"NSDictionary\"8^@16"
- "@24@?0@\"NSDictionary\"8^@16"
- "@48@0:8i16@20@28B36@40"
- "AMFDRSealedDataSetMinimalManifestClassInstance failed with error: %@"
- "Additional PATCH is not allowed when transit between real and staged sealing"
- "Additional UPDATE properties is not allowed when transit between real and staged sealing"
- "B32@0:8^{__AMFDR=}16@24"
- "B44@0:8@16^@24B32^@36"
- "B48@0:8@16^@24@32^@40"
- "B64@0:8@16@24@32@40@48@56"
- "B72@0:8@16^{__AMFDR=}24^{__AMFDR=}32^@40^@48^@56^@64"
- "Brunor ticket not found in response"
- "CRAttestationBaseDeviceHandler"
- "CRAttestationDeviceCompute"
- "CRAttestationDeviceGen1Handler"
- "CRAttestationDeviceGen2Handler"
- "CRAttestationDeviceGen3Handler"
- "CRAttestationDeviceGen4Handler"
- "CRAttestationDeviceiPad1Handler"
- "CRAttestationHandler"
- "CRPreflightRequest_%@: %@"
- "CRPreflightResponse_%@: %@"
- "Challenge ResponseArray:%@"
- "Components: %@"
- "Content-Length: %ld"
- "Copying Savage Firmware ..."
- "Copying Yonkers Firmware ..."
- "Empty configuration"
- "Empty session"
- "Fail to get KBB seal manifest"
- "Failed to create return response: %@"
- "Failed to get chosen info"
- "Failed to get component for %d"
- "Failed to get syscfg-erly-kbgs-data-class"
- "Final Savage options: %@"
- "Final Yonkers options: %@"
- "Get Brunor ticket failed"
- "Get Make DataClasses failed"
- "Get Yonkers ticket failed"
- "Get ticket failed"
- "HTTP Error: %@"
- "HTTP Request Header: %@"
- "HTTP Request: %@"
- "HTTP Response Header: %@"
- "HTTP Response: %@"
- "HTTP Status: %d"
- "Image size: %ld DER size: %ld"
- "Invalid component type"
- "KBBDataClassAndInstanceDict"
- "KGB isServicePart without MTUB SPC"
- "Legacy device:"
- "MainMicrophone"
- "MidEnclosure"
- "Missing required patch info"
- "No baa certs found"
- "Patch validation failed"
- "Properties fetch failed:%@"
- "Properties:%@"
- "RearSystem"
- "Request BAA timeout"
- "Server Data: %@"
- "Server response missing Challenge"
- "Set boot intent and reboot to Checkerboard"
- "Skip reading unknown Mesa: %d"
- "Stong Components:%@"
- "System"
- "T@\"NSDictionary\",&,N,V_KBBDataClassAndInstanceDict"
- "T@\"NSString\",&,N,V_date"
- "T@\"NSString\",N,V_name"
- "TB,N,V_secure"
- "Unable to allocate memory for byte reversal"
- "Unable to get Identifier:%@"
- "Unsupported Class:%d::Product:%ld"
- "Updating Brunor ..."
- "Updating Yonkers ..."
- "_KBBDataClassAndInstanceDict"
- "_date"
- "_extractCertsFromResponse:"
- "_httpSendRequest:proxySettings:withError:"
- "_secure"
- "auth"
- "brunorFirmware"
- "bundleWithPath:"
- "cert der length:%ld"
- "dataTaskWithRequest error: %@"
- "der_key_validate"
- "earlyKBGSDataClass %@ length is not multiple of 4"
- "enumerateMatchesInString:options:range:usingBlock:"
- "failed to open connection to %s\n"
- "fetched RCHL successfully: %{public}@ length = %{public}ld"
- "fetched live instance:%@"
- "fixUpPseudoMSRk:mesaWithSCKey:"
- "getBrunorTicketForBrunorFWUpdateWithOptions:BrunorTicket:auth:error:"
- "getMinimalManifestsClassesAndInstancesWithPartSPC:fdrLocal:fdrRemote:minimalSealingDataInstances:minimalSealedDataClasses:minimalSealedDataInstances:error:"
- "getSavageTicketForZenithSavageFWUpdateWithOptions:SavageTicket:error:"
- "getYonkersTicketForZenithYonkersFWUpdateWithOptions:YonkersTicket:error:"
- "initWithType:name:"
- "initWithType:name:spc:fdrKeys:"
- "initWithType:spc:name:secure:fdrKeys:"
- "isGen1Device:"
- "isGen2Device:"
- "isGen3Device:"
- "isGen4Device:"
- "number of ranges:%ld"
- "ramdiskSavageFirmware"
- "ramdiskYonkersFirmware"
- "request_%@: %@"
- "response_%@: %@"
- "secure"
- "sendRequest:response:keyBlob:error:"
- "sessionWithConfiguration:"
- "setBrunorMinimalSealingMeta:instances:"
- "setDate:"
- "setKBBDataClassAndInstanceDict:"
- "setSecure:"
- "supportMSRk"
- "syscfg-erly-kbgs-data-class"
- "temp makeProperties:%@"
- "transferring properties:%@"
- "translateToExternalName:"
- "unable to get identifier:%@"
- "v28@0:8@16B24"
- "v32@?0@\"NSTextCheckingResult\"8Q16^B24"
- "validatePatchWithPartSPC:originalClasses:originalInstances:originalValues:validClasses:validInstances:"
- "withDate:"
- "zenithSavageFirmware"
- "zenithYonkersFirmware"
- "\xf0\xb1"

```
