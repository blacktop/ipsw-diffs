## EAUpdaterService

> `/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/EAUpdaterService.xpc/EAUpdaterService`

```diff

-1170.80.6.0.1
-  __TEXT.__text: 0x10f34
+1207.100.54.502.1
+  __TEXT.__text: 0xf584
   __TEXT.__auth_stubs: 0x5b0
-  __TEXT.__objc_stubs: 0x31e0
-  __TEXT.__objc_methlist: 0xbe0
-  __TEXT.__cstring: 0x6ec0
+  __TEXT.__objc_stubs: 0x2e00
+  __TEXT.__objc_methlist: 0xd64
+  __TEXT.__cstring: 0x6b3b
   __TEXT.__const: 0x68
-  __TEXT.__gcc_except_tab: 0x114
-  __TEXT.__objc_methname: 0x37e7
-  __TEXT.__oslogstring: 0x265
-  __TEXT.__objc_classname: 0x107
-  __TEXT.__objc_methtype: 0x794
+  __TEXT.__gcc_except_tab: 0x118
+  __TEXT.__objc_methname: 0x340e
+  __TEXT.__oslogstring: 0x176
+  __TEXT.__objc_classname: 0xb3
+  __TEXT.__objc_methtype: 0x6dd
   __TEXT.__dlopen_cstrs: 0x52
-  __TEXT.__unwind_info: 0x420
+  __TEXT.__unwind_info: 0x3b8
   __DATA_CONST.__auth_got: 0x2e8
-  __DATA_CONST.__got: 0x1a0
+  __DATA_CONST.__got: 0x1c0
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x11d8
-  __DATA_CONST.__cfstring: 0x6240
-  __DATA_CONST.__objc_classlist: 0x38
-  __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x40
+  __DATA_CONST.__const: 0x1070
+  __DATA_CONST.__cfstring: 0x6040
+  __DATA_CONST.__objc_classlist: 0x28
+  __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x38
+  __DATA_CONST.__objc_superrefs: 0x28
   __DATA_CONST.__objc_intobj: 0x48
-  __DATA.__objc_const: 0x2328
-  __DATA.__objc_selrefs: 0xee0
-  __DATA.__objc_ivar: 0x1ac
-  __DATA.__objc_data: 0x230
-  __DATA.__data: 0x300
-  __DATA.__bss: 0x118
+  __DATA.__objc_const: 0x1958
+  __DATA.__objc_selrefs: 0xe68
+  __DATA.__objc_ivar: 0x1a4
+  __DATA.__objc_data: 0x190
+  __DATA.__data: 0x2a0
+  __DATA.__bss: 0xf8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreTelephony.framework/CoreTelephony
   - /System/Library/Frameworks/ExternalAccessory.framework/ExternalAccessory
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/AUDeveloperSettings.framework/AUDeveloperSettings
+  - /System/Library/PrivateFrameworks/AUSettings.framework/AUSettings
   - /System/Library/PrivateFrameworks/CoreUARP.framework/CoreUARP
   - /System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/MobileAccessoryUpdater
   - /System/Library/PrivateFrameworks/MobileAssetUpdater.framework/MobileAssetUpdater

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 367
-  Symbols:   652
-  CStrings:  1733
+  Functions: 361
+  Symbols:   626
+  CStrings:  1637
 
Symbols:
+ _kAUAssetLocationTypeMobileAssetServerBasejumperBaseStr
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
+ _objc_release_x26
- _AUDeveloperSettingsAccessoryFusingStringToType
- _OBJC_CLASS_$_AUHelperInstance
- _OBJC_CLASS_$_NSSet
- _OBJC_CLASS_$_NSUserDefaults
- _OBJC_CLASS_$_NSXPCConnection
- _OBJC_CLASS_$_NSXPCInterface
- _OBJC_CLASS_$_UARPSupportedAccessory
- _OBJC_METACLASS_$_AUDeveloperSettingsDatabase
- _OBJC_METACLASS_$_AUHelperInstance
- __os_log_debug_impl
- _cleanupPersonalizedUpdateAvailable
- _configuredToDefaultAssetLocationForAccessory
- _dropboxFileUpdateForAccessoryID
- _findPartnerSerialNumberForAccessory
- _findPartnerSerialNumbersInDatabase
- _getAccessoryDatabaseKeyForAccessoryID
- _getInfoForAccessory
- _getuid
- _isOTAUpdateDisabledForAccessoryID
- _kAUDeveloperSettingsDatabaseDefaultsSuite
- _kAccessoryReachableKey
- _kAssetURLOverrideKey
- _kAuthListingEnabledKey
- _kClientIndentifier
- _kDownloadedVersionKey
- _kDropboxVersionKey
- _kHWRevisionKey
- _kInternalSettingsPaneURL
- _kPartnerSerialNumbersKey
- _kPersonalizationRequiredKey
- _kSerialNumberKey
- _kSupplementalAssetLocationKey
- _kSupplementalBasejumperBuildKey
- _kSupplementalBasejumperTrainKey
- _objc_allocWithZone
- _objc_opt_isKindOfClass
- _os_log_create
- _updateReachabilityForAccessoryID
CStrings:
+ "Assets"
+ "CrystalSeedUpdate"
+ "Flash Section Length"
+ "IP"
+ "Payload Ordered Index"
+ "Serial"
+ "UID_MODE"
+ "countryList"
+ "deploymentLimit"
+ "goLiveDate"
+ "https://basejumper.apple.com"
+ "rampPeriod"
- "%@/MarimbaSeed"
- "%s: Failed to get remote object: %@"
- "%s: Failed to get xpc connection"
- "%s: Not adding empty serial number with info = %@"
- "%s: Updating location = %s for accessoryName = %@"
- "%s: dictionary = %@"
- "%s: received unknown object = %@"
- "%s: seting %@:%@"
- "+"
- "+[AUHelperInstance xpcConnectionToHelper]"
- "-[AUDeveloperSettingsDatabase accessoriesDictionary]"
- "-[AUDeveloperSettingsDatabase addAccessoryWithSerialNumber:info:]"
- "-[AUDeveloperSettingsDatabase seedParticipationDictionary]"
- "-[AUDeveloperSettingsDatabase setAccessoriesDictionary:]"
- "-[AUDeveloperSettingsDatabase updateAccessory:locationType:]"
- "-[AUHelperInstance remoteObject]_block_invoke"
- "@\"NSObject<OS_os_log>\""
- "@\"NSXPCConnection\""
- "AUDeveloperSettingsDatabase"
- "AUDeveloperSettingsObjectWithKey:"
- "AUDeveloperSettingsSetObject:withKey:"
- "AUHelperExtend"
- "AUHelperInstance"
- "AUHelperServiceProtocol"
- "B24@0:8Q16"
- "Basejumper"
- "CrystalD"
- "Custom Basejumper"
- "Customer"
- "Dev"
- "Internal Seed"
- "Livability"
- "Mesu Staging"
- "Pending"
- "Prod"
- "Public Seed"
- "Q24@0:8@16"
- "T@\"<AUHelperServiceProtocol>\",R"
- "T@\"AUHelperInstance\",R"
- "T@\"NSDictionary\",R"
- "Unfused"
- "_log"
- "_xpcConnection"
- "accessories"
- "accessoryNameForIdentifier:name:serialNumber:fusingType:"
- "accessoryReachable"
- "activeVersion"
- "assetURLOverride"
- "authListingEnabled"
- "basejumperBuild"
- "basejumperTrain"
- "com.apple.accessoryupdater.launchauhelper"
- "containsObject:"
- "default"
- "downloadedVersion"
- "dropboxVersion"
- "enumerateKeysAndObjectsUsingBlock:"
- "findByAppleModelNumber:"
- "fusing"
- "hwFusingType"
- "hwRevision"
- "initWithMachServiceName:options:"
- "initWithSuiteName:"
- "interfaceWithProtocol:"
- "isOTADisabled"
- "isSeedParticipationEnabled:"
- "isValidLocationType:"
- "migrateExistingDefaults"
- "partnerSerialNumbers"
- "personalizationRequired"
- "prefs:root=INTERNAL_SETTINGS&path=AccessoriesFirmwareUpdate"
- "prod"
- "remoteObject"
- "remoteObjectInterface"
- "removeAccessoryWithSerialNumber:"
- "removeObjectForKey:"
- "resume"
- "seedParticipation"
- "seedParticipationDictionary"
- "setAccessoriesDictionary:"
- "setClasses:forSelector:argumentIndex:ofReply:"
- "setRemoteObjectInterface:"
- "setWithObjects:"
- "sharedInstance"
- "supplementalAssetLocation"
- "supplementalBasejumperBuild"
- "supplementalBasejumperTrain"
- "supportsInternalSettings"
- "synchronousRemoteObjectProxyWithErrorHandler:"
- "unrecognized"
- "updateAccessory:locationType:"
- "urlLocationTypeForAccessory:"
- "userPreferenceObjectForSuite:withKey:withReply:"
- "userPreferenceSetObject:forSuite:withKey:"
- "v16@?0@8"
- "v32@?0@\"NSString\"8@\"NSDictionary\"16^B24"
- "v40@0:8@16Q24@\"NSString\"32"
- "v40@0:8@16Q24@32"
- "v40@0:8Q16@\"NSString\"24@?<v@?@>32"
- "v40@0:8Q16@24@?32"
- "v48@0:8@16^@24^@32^Q40"
- "xpcConnectionToHelper"

```
