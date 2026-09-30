## AUSettings

> `/System/Library/PrivateFrameworks/AUSettings.framework/AUSettings`

```diff

-1170.80.6.0.1
-  __TEXT.__text: 0x3068
-  __TEXT.__auth_stubs: 0x300
-  __TEXT.__objc_methlist: 0x12c
-  __TEXT.__const: 0x70
-  __TEXT.__cstring: 0x2436
-  __TEXT.__oslogstring: 0xef
+1207.100.54.502.1
+  __TEXT.__text: 0x54d8
+  __TEXT.__auth_stubs: 0x330
+  __TEXT.__objc_methlist: 0x56c
+  __TEXT.__const: 0x80
+  __TEXT.__cstring: 0x2538
+  __TEXT.__oslogstring: 0x164
   __TEXT.__gcc_except_tab: 0x14
-  __TEXT.__unwind_info: 0x170
-  __TEXT.__objc_classname: 0x60
-  __TEXT.__objc_methname: 0x75a
-  __TEXT.__objc_methtype: 0x19e
-  __TEXT.__objc_stubs: 0x7c0
-  __DATA_CONST.__got: 0x98
-  __DATA_CONST.__const: 0xe60
-  __DATA_CONST.__objc_classlist: 0x10
+  __TEXT.__unwind_info: 0x1b8
+  __TEXT.__objc_classname: 0x9c
+  __TEXT.__objc_methname: 0xfe4
+  __TEXT.__objc_methtype: 0x249
+  __TEXT.__objc_stubs: 0xb20
+  __DATA_CONST.__got: 0xa0
+  __DATA_CONST.__const: 0xee8
+  __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x10
+  __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x210
+  __DATA_CONST.__objc_selrefs: 0x468
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x190
+  __DATA_CONST.__objc_superrefs: 0x18
+  __AUTH_CONST.__auth_got: 0x1a8
   __AUTH_CONST.__const: 0x200
-  __AUTH_CONST.__cfstring: 0x33a0
-  __AUTH_CONST.__objc_const: 0x530
-  __AUTH.__objc_data: 0xa0
-  __DATA.__objc_ivar: 0x8
-  __DATA.__data: 0xc0
+  __AUTH_CONST.__cfstring: 0x3500
+  __AUTH_CONST.__objc_const: 0x848
+  __AUTH.__objc_data: 0xf0
+  __DATA.__objc_ivar: 0x60
+  __DATA.__data: 0x1e0
   __DATA.__bss: 0x100
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/CoreUARP.framework/CoreUARP
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 79
-  Symbols:   572
-  CStrings:  567
+  Functions: 158
+  Symbols:   667
+  CStrings:  697
 
Symbols:
+ _OBJC_CLASS_$_NSNull
+ _OBJC_CLASS_$_UARPSettingsAccessory
+ _OBJC_METACLASS_$_UARPSettingsAccessory
+ _dropboxFileUpdateForAccessory
+ _findPartnerSerialNumberForAccessoryID
+ _generateAssetLocationBasePath
+ _getAccessoryDatabaseKeyForAccessory
+ _isOTAUpdateDisabledForAccessory
+ _kAccessorySupportsDeveloperSettingsKey
+ _kUARPStringMetadataDevicePayloadOrderedIndex
+ _kUARPStringMetadataDeviceTlvFlashSectionLength
+ _kUARPStringMobileAssetAssetsKey
+ _kUARPStringMobileAssetDeploymentCountryListKey
+ _kUARPStringMobileAssetDeploymentDeploymentLimitKey
+ _kUARPStringMobileAssetDeploymentGoLiveDateKey
+ _kUARPStringMobileAssetDeploymentRampPeriodKey
+ _kUARPStringPersonalizationOptionUIDMode
+ _kUARPSupportedAccessoryKeyTransportIP
+ _kUARPSupportedAccessoryKeyTransportSerial
+ _objc_getProperty
+ _objc_opt_new
+ _objc_retain_x25
+ _objc_retain_x26
+ _objc_retain_x4
+ _updateReachabilityForAccessory
- _OBJC_CLASS_$_UARPSupportedAccessory
- _objc_autorelease
- _objc_retain_x23
CStrings:
+ "\x01\x1f\x01"
+ "%@/%@/%@%@"
+ "%@/AirPods2022Seed"
+ "%s: Invalid key value / pair = %@ / %@"
+ "%s: setting %@"
+ "%s: unknown key/value pair %@/%@"
+ "-[AUDeveloperSettingsDatabase accessoryList]_block_invoke"
+ "-[AUDeveloperSettingsDatabase updateAccessoryWithSerialNumber:info:]"
+ "@\"NSArray\""
+ "@\"NSDictionary\""
+ "@\"NSString\""
+ "@24@0:8@\"NSCoder\"16"
+ "@24@0:8^{_NSZone=}16"
+ "@48@0:8@16@24@32@40"
+ "AUDeveloperSettingsUpdateAccessory:withKey:"
+ "AirPodsDeveloperSeed"
+ "Assets"
+ "B"
+ "Flash Section Length"
+ "IP"
+ "NSCoding"
+ "NSCopying"
+ "NSSecureCoding"
+ "Payload Ordered Index"
+ "Removing accessory from database %@"
+ "Serial"
+ "T@\"NSArray\",R,V_partnerSerialNumbers"
+ "T@\"NSString\",R,V_activeVersion"
+ "T@\"NSString\",R,V_assetLocation"
+ "T@\"NSString\",R,V_assetURLOverride"
+ "T@\"NSString\",R,V_customBuild"
+ "T@\"NSString\",R,V_customTrain"
+ "T@\"NSString\",R,V_downloadedVersion"
+ "T@\"NSString\",R,V_dropboxVersion"
+ "T@\"NSString\",R,V_hwFusing"
+ "T@\"NSString\",R,V_hwRevision"
+ "T@\"NSString\",R,V_modelNumber"
+ "T@\"NSString\",R,V_name"
+ "T@\"NSString\",R,V_serialNumber"
+ "T@\"NSString\",R,V_supplementalAssetLocation"
+ "T@\"NSString\",R,V_supplementalCustomBuild"
+ "T@\"NSString\",R,V_supplementalCustomTrain"
+ "TB,R"
+ "TB,R,V_accessoryReachable"
+ "TB,R,V_authListingEnabled"
+ "TB,R,V_otaDisabled"
+ "TB,R,V_personalizationRequired"
+ "TB,R,V_supportsDeveloperSettings"
+ "UARPSettingsAccessory"
+ "UID_MODE"
+ "Updating database with %@ / %@"
+ "_accessoryReachable"
+ "_activeVersion"
+ "_assetLocation"
+ "_assetURLOverride"
+ "_authListingEnabled"
+ "_customBuild"
+ "_customTrain"
+ "_downloadedVersion"
+ "_dropboxVersion"
+ "_hwFusing"
+ "_hwRevision"
+ "_modelNumber"
+ "_name"
+ "_originalSettings"
+ "_otaDisabled"
+ "_partnerSerialNumbers"
+ "_personalizationRequired"
+ "_serialNumber"
+ "_supplementalAssetLocation"
+ "_supplementalCustomBuild"
+ "_supplementalCustomTrain"
+ "_supportsDeveloperSettings"
+ "accessoryList"
+ "copyAccessoryForSignature:modelNumber:fusingType:partnerSerialNumbers:"
+ "copyAccessoryWithSerialNumber:"
+ "copyWithZone:"
+ "countryList"
+ "customBuild"
+ "customTrain"
+ "decodeBoolForKey:"
+ "decodeObjectOfClass:forKey:"
+ "deploymentLimit"
+ "encodeAsChangedDictionary"
+ "encodeAsDictionary"
+ "encodeBool:forKey:"
+ "encodeObject:forKey:"
+ "encodeWithCoder:"
+ "goLiveDate"
+ "https://basejumper.apple.com"
+ "hwFusing"
+ "initWithCoder:"
+ "initWithDictionary:"
+ "isEqualToArray:"
+ "isEqualToNumber:"
+ "null"
+ "otaDisabled"
+ "rampPeriod"
+ "removeAccessory:"
+ "setAccessoryReachable:"
+ "setActiveVersion:"
+ "setAssetLocation:"
+ "setAssetURLOverride:"
+ "setAuthListingEnabled:"
+ "setCustomBuild:"
+ "setCustomTrain:"
+ "setDownloadedVersion:"
+ "setDropboxVersion:"
+ "setHwFusing:"
+ "setHwRevision:"
+ "setModelNumber:"
+ "setName:"
+ "setOtaDisabled:"
+ "setPartnerSerialNumbers:"
+ "setPersonalizationRequired:"
+ "setSerialNumber:"
+ "setSupplementalAssetLocation:"
+ "setSupplementalCustomBuild:"
+ "setSupplementalCustomTrain:"
+ "setSupportsDeveloperSettings:"
+ "stringByAppendingPathComponent:"
+ "stringByStandardizingPath"
+ "supplementalCustomBuild"
+ "supplementalCustomTrain"
+ "supportsDeveloperSettings"
+ "supportsSecureCoding"
+ "updateAccessory:"
+ "updateAccessoryWithSerialNumber:info:"
+ "userPreferenceUpdateAccessorySettings:withKey:"
+ "v20@0:8B16"
+ "v24@0:8@\"NSCoder\"16"
+ "v32@0:8@\"NSDictionary\"16@\"NSString\"24"
+ "v32@?0@8@16^B24"
- "%s: dictionary = %@"
- "%s: seting %@:%@"
- "+"
- "-[AUDeveloperSettingsDatabase seedParticipationDictionary]"
- "componentsSeparatedByString:"
- "containsObject:"
- "dictionary"
- "findByAppleModelNumber:"
- "migrateExistingDefaults"
- "objectAtIndexedSubscript:"
- "prod"
- "seedParticipation"
- "seedParticipationDictionary"
- "supportsInternalSettings"

```
