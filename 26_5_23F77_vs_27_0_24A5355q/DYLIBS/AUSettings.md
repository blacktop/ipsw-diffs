## AUSettings

> `/System/Library/PrivateFrameworks/AUSettings.framework/AUSettings`

```diff

-1345.120.5.0.0
-  __TEXT.__text: 0x57cc
-  __TEXT.__auth_stubs: 0x300
-  __TEXT.__objc_methlist: 0x6bc
+1576.0.0.0.0
+  __TEXT.__text: 0x5a50
+  __TEXT.__objc_methlist: 0x6f4
   __TEXT.__const: 0x88
-  __TEXT.__cstring: 0xd7f
-  __TEXT.__oslogstring: 0x1bb
-  __TEXT.__gcc_except_tab: 0x14
-  __TEXT.__unwind_info: 0x180
-  __TEXT.__objc_classname: 0xeb
-  __TEXT.__objc_methname: 0x138e
-  __TEXT.__objc_methtype: 0x28a
-  __TEXT.__objc_stubs: 0x9e0
-  __DATA_CONST.__got: 0xb8
-  __DATA_CONST.__const: 0x580
+  __TEXT.__cstring: 0xe0f
+  __TEXT.__oslogstring: 0x1ec
+  __TEXT.__gcc_except_tab: 0x28
+  __TEXT.__unwind_info: 0x198
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x588
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x528
+  __DATA_CONST.__objc_selrefs: 0x558
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0x190
+  __DATA_CONST.__got: 0xb8
   __AUTH_CONST.__const: 0x60
-  __AUTH_CONST.__cfstring: 0xf60
-  __AUTH_CONST.__objc_const: 0xd98
+  __AUTH_CONST.__cfstring: 0xf80
+  __AUTH_CONST.__objc_const: 0xdc8
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x140
-  __DATA.__objc_ivar: 0x88
+  __DATA.__objc_ivar: 0x8c
   __DATA.__data: 0x240
   __DATA.__bss: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C00D5827-6E15-3BB6-BD82-468F65C02F92
-  Functions: 150
-  Symbols:   675
-  CStrings:  580
+  UUID: DEF1A082-E79D-3D79-BE1F-608FD663CE73
+  Functions: 159
+  Symbols:   701
+  CStrings:  297
 
Symbols:
+ +[NSUserDefaults(AUHelperExtend) AUDeveloperSettingsAccessoryDatabase]
+ -[AUDeveloperSettingsDatabase copyAccessoryWithSerialNumber:directMatchOnly:]
+ -[AUDeveloperSettingsDatabase remoteAccessoryList]
+ -[AUDeveloperSettingsDatabase remoteAccessoryList].cold.1
+ -[UARPSettingsAccessory parentSerialNumber]
+ -[UARPSettingsAccessory setParentSerialNumber:]
+ GCC_except_table6
+ _OBJC_IVAR_$_UARPSettingsAccessory._parentSerialNumber
+ ___50-[AUDeveloperSettingsDatabase remoteAccessoryList]_block_invoke
+ ___50-[AUDeveloperSettingsDatabase remoteAccessoryList]_block_invoke.cold.1
+ ___70+[NSUserDefaults(AUHelperExtend) AUDeveloperSettingsAccessoryDatabase]_block_invoke
+ ___kCFBooleanTrue
+ _kParentSerialNumberKey
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$AUDeveloperSettingsAccessoryDatabase
+ _objc_msgSend$arrayWithObject:
+ _objc_msgSend$copyAccessoryWithSerialNumber:directMatchOnly:
+ _objc_msgSend$parentSerialNumber
+ _objc_msgSend$setAssetLocation:
+ _objc_msgSend$updateAccessory:
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x27
+ _objc_retain_x3
+ _objc_retain_x8
- ___kCFBooleanFalse
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x23
- _objc_retain_x24
- _objc_retain_x28
CStrings:
+ "%s: Missing entry for %{public}@"
+ "%s: Updating location = %{public}s for accessoryName = %{public}@"
+ "-[AUDeveloperSettingsDatabase remoteAccessoryList]"
+ "-[AUDeveloperSettingsDatabase remoteAccessoryList]_block_invoke"
+ "parentSerialNumber"
- "#16@0:8"
- "%s: Updating location = %s for accessoryName = %@"
- ".cxx_destruct"
- "@\"NSArray\""
- "@\"NSDictionary\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSObject<OS_os_log>\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSXPCConnection\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@24@0:8^{_NSZone=}16"
- "@32@0:8:16@24"
- "@40@0:8:16@24@32"
- "@48@0:8@16@24@32@40"
- "AUDeveloperSettingsDatabase"
- "AUDeveloperSettingsObjectWithKey:"
- "AUDeveloperSettingsSetObject:withKey:"
- "AUDeveloperSettingsUpdateAccessory:withKey:"
- "AUHelperExtend"
- "AUHelperInstance"
- "AUHelperServiceProtocol"
- "AUInternalSettingsAssetManagerXPC"
- "AUInternalSettingsAssetManagerXPCProvider"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B24@0:8Q16"
- "NSCoding"
- "NSCopying"
- "NSObject"
- "NSSecureCoding"
- "Q"
- "Q16@0:8"
- "Q24@0:8@16"
- "T#,R"
- "T@\"<AUHelperServiceProtocol>\",R"
- "T@\"AUHelperInstance\",R"
- "T@\"NSArray\",R,V_partnerSerialNumbers"
- "T@\"NSDictionary\",R"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,V_activeVersion"
- "T@\"NSString\",R,V_assetLocation"
- "T@\"NSString\",R,V_assetURLOverride"
- "T@\"NSString\",R,V_customBuild"
- "T@\"NSString\",R,V_customTrain"
- "T@\"NSString\",R,V_downloadedVersion"
- "T@\"NSString\",R,V_dropboxVersion"
- "T@\"NSString\",R,V_hwFusing"
- "T@\"NSString\",R,V_hwRevision"
- "T@\"NSString\",R,V_mobileAssetModelNumber"
- "T@\"NSString\",R,V_modelNumber"
- "T@\"NSString\",R,V_name"
- "T@\"NSString\",R,V_pallasAudienceOverride"
- "T@\"NSString\",R,V_serialNumber"
- "T@\"NSString\",R,V_supplementalAssetLocation"
- "T@\"NSString\",R,V_supplementalCustomBuild"
- "T@\"NSString\",R,V_supplementalCustomTrain"
- "TB,R"
- "TB,R,V_accessoryReachable"
- "TB,R,V_authListingEnabled"
- "TB,R,V_forceInstall"
- "TB,R,V_otaDisabled"
- "TB,R,V_pallasInternalAssetVariant"
- "TB,R,V_pallasSupportEnabled"
- "TB,R,V_personalizationRequired"
- "TB,R,V_softwareUpdateAssetType"
- "TB,R,V_softwareUpdateEraseInstall"
- "TB,R,V_supportsDeveloperSettings"
- "TQ,R"
- "TQ,R,V_pallasAudience"
- "UARPSettingsAccessory"
- "UTF8String"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_accessoryReachable"
- "_activeVersion"
- "_assetLocation"
- "_assetURLOverride"
- "_authListingEnabled"
- "_customBuild"
- "_customTrain"
- "_downloadedVersion"
- "_dropboxVersion"
- "_forceInstall"
- "_hwFusing"
- "_hwRevision"
- "_internalQueue"
- "_log"
- "_mobileAssetModelNumber"
- "_modelNumber"
- "_name"
- "_originalSettings"
- "_otaDisabled"
- "_pallasAudience"
- "_pallasAudienceOverride"
- "_pallasInternalAssetVariant"
- "_pallasSupportEnabled"
- "_partnerSerialNumbers"
- "_personalizationRequired"
- "_serialNumber"
- "_softwareUpdateAssetType"
- "_softwareUpdateEraseInstall"
- "_supplementalAssetLocation"
- "_supplementalCustomBuild"
- "_supplementalCustomTrain"
- "_supportsDeveloperSettings"
- "_xpcConnection"
- "accessoriesDictionary"
- "accessoryList"
- "accessoryNameForIdentifier:name:serialNumber:fusingType:"
- "addAccessoryWithSerialNumber:info:"
- "addObject:"
- "allKeys"
- "array"
- "arrayWithArray:"
- "autorelease"
- "boolValue"
- "bundleIdentifier"
- "caseInsensitiveCompare:"
- "class"
- "conformsToProtocol:"
- "containsObject:"
- "copy"
- "copyAccessoryForSignature:modelNumber:fusingType:partnerSerialNumbers:"
- "copyAccessoryWithSerialNumber:"
- "copyWithZone:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "customBuild"
- "customTrain"
- "dealloc"
- "debugDescription"
- "decodeBoolForKey:"
- "decodeIntegerForKey:"
- "decodeObjectOfClass:forKey:"
- "dictionaryWithDictionary:"
- "encodeAsChangedDictionary"
- "encodeAsDictionary"
- "encodeBool:forKey:"
- "encodeInteger:forKey:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "enumerateKeysAndObjectsUsingBlock:"
- "hash"
- "hwFusing"
- "hwFusingType"
- "init"
- "initWithCoder:"
- "initWithDictionary:"
- "initWithMachServiceName:options:"
- "initWithSuiteName:"
- "integerValue"
- "interfaceWithProtocol:"
- "invalidate"
- "isEqual:"
- "isEqualToArray:"
- "isEqualToDictionary:"
- "isEqualToNumber:"
- "isEqualToString:"
- "isFusingEqual:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "isSeedParticipationEnabled:"
- "isValidLocationType:"
- "length"
- "mainBundle"
- "mutableCopy"
- "null"
- "numberWithBool:"
- "numberWithUnsignedInteger:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "otaDisabled"
- "pallasInternalAssetVariant"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "release"
- "remoteObject"
- "remoteObjectInterface"
- "removeAccessory:"
- "removeAccessoryWithSerialNumber:"
- "removeObjectForKey:"
- "respondsToSelector:"
- "resume"
- "retain"
- "retainCount"
- "self"
- "setAccessoriesDictionary:"
- "setAccessoryReachable:"
- "setActiveVersion:"
- "setAssetLocation:"
- "setAssetURLOverride:"
- "setAuthListingEnabled:"
- "setClasses:forSelector:argumentIndex:ofReply:"
- "setCustomBuild:"
- "setCustomTrain:"
- "setDownloadedVersion:"
- "setDropboxVersion:"
- "setForceInstall:"
- "setHwFusing:"
- "setHwRevision:"
- "setMobileAssetModelNumber:"
- "setModelNumber:"
- "setName:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "setOtaDisabled:"
- "setPallasAudience:"
- "setPallasAudienceOverride:"
- "setPallasInternalAssetVariant:"
- "setPallasSupportEnabled:"
- "setPartnerSerialNumbers:"
- "setPersonalizationRequired:"
- "setRemoteObjectInterface:"
- "setSerialNumber:"
- "setSoftwareUpdateAssetType:"
- "setSoftwareUpdateEraseInstall:"
- "setSupplementalAssetLocation:"
- "setSupplementalCustomBuild:"
- "setSupplementalCustomTrain:"
- "setSupportsDeveloperSettings:"
- "setWithObjects:"
- "settingsChangedForSerialNumber:"
- "sharedDatabase"
- "sharedInstance"
- "softwareUpdateAssetType"
- "softwareUpdateEraseInstall"
- "stringWithFormat:"
- "stringWithUTF8String:"
- "superclass"
- "supplementalCustomBuild"
- "supplementalCustomTrain"
- "supportsDeveloperSettings"
- "supportsSecureCoding"
- "synchronousRemoteObjectProxyWithErrorHandler:"
- "updateAccessory:"
- "updateAccessory:locationType:"
- "updateAccessoryWithSerialNumber:info:"
- "urlLocationTypeForAccessory:"
- "userPreferenceObjectForSuite:withKey:withReply:"
- "userPreferenceSetObject:forSuite:withKey:"
- "userPreferenceUpdateAccessorySettings:withKey:"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@\"NSString\"16"
- "v24@0:8@16"
- "v24@0:8Q16"
- "v32@0:8@\"NSDictionary\"16@\"NSString\"24"
- "v32@0:8@16@24"
- "v32@0:8@16Q24"
- "v40@0:8@16Q24@\"NSString\"32"
- "v40@0:8@16Q24@32"
- "v40@0:8Q16@\"NSString\"24@?<v@?@>32"
- "v40@0:8Q16@24@?32"
- "v48@0:8@16^@24^@32^Q40"
- "xpcConnectionToDaemon"
- "xpcConnectionToHelper"
- "zone"

```
