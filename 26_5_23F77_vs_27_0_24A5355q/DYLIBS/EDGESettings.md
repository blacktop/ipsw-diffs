## EDGESettings

> `/System/Library/PreferenceBundles/EDGESettings.bundle/EDGESettings`

```diff

-1077.0.0.0.0
-  __TEXT.__text: 0x3d84
-  __TEXT.__auth_stubs: 0x290
+1078.0.0.0.0
+  __TEXT.__text: 0x3e0c
   __TEXT.__objc_methlist: 0x3ec
   __TEXT.__cstring: 0x560
   __TEXT.__const: 0x50
   __TEXT.__oslogstring: 0x1a4
   __TEXT.__unwind_info: 0x148
-  __TEXT.__objc_classname: 0x5b
-  __TEXT.__objc_methname: 0xdee
-  __TEXT.__objc_methtype: 0x1ec
-  __TEXT.__objc_stubs: 0xbc0
-  __DATA_CONST.__got: 0x108
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x98
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x10

   __DATA_CONST.__objc_selrefs: 0x430
   __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__objc_arraydata: 0x20
-  __AUTH_CONST.__auth_got: 0x150
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__cfstring: 0xa00
   __AUTH_CONST.__objc_const: 0x690
   __AUTH_CONST.__objc_arrayobj: 0x60
+  __AUTH_CONST.__auth_got: 0x150
   __AUTH.__objc_data: 0xa0
   __DATA.__objc_ivar: 0x74
   __DATA.__data: 0xc8

   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 43F4BA01-108E-3114-BDAB-4FAA782A80B1
-  Functions: 90
-  Symbols:   424
-  CStrings:  382
+  UUID: 33E93951-63EA-3C5B-A4A7-2E45AC4F2E8F
+  Functions: 88
+  Symbols:   420
+  CStrings:  177
 
Symbols:
- _OUTLINED_FUNCTION_3
- _OUTLINED_FUNCTION_4
CStrings:
- "#16@0:8"
- "@\"CTXPCServiceSubscriptionContext\""
- "@\"CoreTelephonyClient\""
- "@\"NSArray\""
- "@\"NSDictionary\""
- "@\"NSMutableDictionary\""
- "@\"NSString\"16@0:8"
- "@\"PSSystemConfiguration\""
- "@16@0:8"
- "@20@0:8i16"
- "@24@0:8:16"
- "@24@0:8@16"
- "@32@0:8:16@24"
- "@40@0:8:16@24@32"
- "B"
- "B16@0:8"
- "B20@0:8i16"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B28@0:8@16i24"
- "CoreTelephonyClientDeviceManagementDelegate"
- "EdgeController"
- "EdgeSettingsController"
- "NSObject"
- "Q16@0:8"
- "T#,R"
- "T@\"CTXPCServiceSubscriptionContext\",&,N,V_context"
- "T@\"CoreTelephonyClient\",&,N,V_coreTelephonyClient"
- "T@\"NSArray\",&,N,V_currectSet"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "TQ,R"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_APNDictionaryForServiceFromSC:"
- "_IMSContextSpecifiers"
- "_InternetContextSpecifiers"
- "_MMSContextSpecifiers"
- "_VVMContextSpecifiers"
- "_advancedSpecifiers"
- "_blankAPNDictionaryWithTypeMask:"
- "_cacheInitialized"
- "_context"
- "_coreTelephonyClient"
- "_currectSet"
- "_getAPNDictinaryForService:"
- "_getMMSObjectForKey:"
- "_group1Specifiers"
- "_imsSettingsDictionary"
- "_internetSettingsDictionary"
- "_isAPNDictionaryBlank:"
- "_lastAttachAPNDict"
- "_lastProxyDict"
- "_lteAttachAPNSpecifiers"
- "_manualSpecifiers"
- "_mmsSettingsDictionary"
- "_newAttachAPNDict"
- "_pacSpecifiers"
- "_proxyAuth"
- "_proxyAuthSpecifiers"
- "_resetSpecifiers"
- "_setMMSOverrideValue:forKey:"
- "_shouldShowUIForServiceType:"
- "_switchSpecifiers"
- "_systemConfig"
- "_tetheringContextSpecifiers"
- "_tetheringSettingsDictionary"
- "_updateKey:toValue:forServiceType:"
- "_vvmSettingsDictionary"
- "actionWithTitle:style:handler:"
- "addAction:"
- "addEntriesFromDictionary:"
- "addObject:"
- "addObjectsFromArray:"
- "alertControllerWithTitle:message:preferredStyle:"
- "applicationDidResume"
- "applicationWillSuspend"
- "array"
- "arrayWithObjects:"
- "attachAPNSettings"
- "autorelease"
- "boolValue"
- "bundleForClass:"
- "cellType"
- "class"
- "commitAPNsSettings"
- "commitAttachAPNSettings"
- "componentsJoinedByString:"
- "conformsToProtocol:"
- "context"
- "context:getAttachApnSettings:"
- "context:getCarrierBundleValue:error:"
- "context:modifyAttachApnSettings:"
- "context:modifyAttachApnSettings:completion:"
- "coreTelephonyClient"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "currectSet"
- "dataServiceID"
- "dealloc"
- "debugDescription"
- "description"
- "dictionary"
- "didChangeDeviceManagementSettings:"
- "edgeDNS:"
- "getAPNDataForSpecifier:"
- "getAttachAPNDataForSpecifier:"
- "getConfiguredApns:error:"
- "getDefaultSettings:"
- "getGSMASettingsUIControl"
- "getGSMAUIControlSetting:error:"
- "getMMSNumericValueForSpecifier:"
- "getMMSValueForSpecifier:"
- "getUIConfiguredApns:error:"
- "groupSpecifierWithName:"
- "hash"
- "identifier"
- "init"
- "initAPNCacheDictionaries"
- "initDictionaryForUIApn:forServiceType:"
- "initWithObjects:"
- "initWithObjectsAndKeys:"
- "initWithQueue:"
- "intValue"
- "isAttachAPNEditingAllowed"
- "isAttachApnSettingAllowed:error:"
- "isEqual:"
- "isEqualToDictionary:"
- "isEqualToString:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "isTetheringEditingSupported:error:"
- "isTypeOfService:ofServiceType:"
- "length"
- "loadCurrentAPNs"
- "loadGSMASettings:state:"
- "loadSpecifiersFromPlistName:target:"
- "localizedStringForKey:value:table:"
- "makeUIApnBasedOn:"
- "mutableCopy"
- "numberWithBool:"
- "numberWithInt:"
- "objectAtIndex:"
- "objectForKey:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "preferenceSpecifierNamed:target:set:get:detail:cell:edit:"
- "presentViewController:animated:completion:"
- "propertyForKey:"
- "protocolConfigurationValueForKey:protocolType:serviceID:"
- "release"
- "reloadSpecifier:"
- "reloadSpecifiers"
- "removeObjectForKey:"
- "resetAPNsDictionaries"
- "resetAllConfiguredSettings"
- "resetAttachAPNSettings"
- "resetCarrierSettings:"
- "resetUIConfiguredApns:completion:"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "self"
- "setAPNData:forSpecifier:"
- "setAttachAPNData:forSpecifier:"
- "setBasebandValue:forTraceName:property:"
- "setContext:"
- "setCoreTelephonyClient:"
- "setCurrectSet:"
- "setDefaultSettings:specifier:"
- "setDelegate:"
- "setEdgeDNS:specifier:"
- "setIdentifier:"
- "setMMSNumericValue:forSpecifier:"
- "setMMSValue:forSpecifier:"
- "setObject:forKey:"
- "setProperty:forKey:"
- "setTitle:"
- "setUIConfiguredApns:apns:completion:"
- "sharedInstance"
- "shouldResetAttachAPN"
- "showCarrierSettingsEraseAlert:"
- "slotID"
- "specifier"
- "specifierForID:"
- "specifiers"
- "specifiersWithSpecifier:"
- "stringValue"
- "superclass"
- "uploadSettingsOnCT:"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@\"CTXPCServiceSubscriptionContext\"16"
- "v24@0:8@16"
- "v28@0:8^@16i24"
- "v32@0:8@16@24"
- "v36@0:8@16@24i32"
- "v40@0:8@16@24@32"
- "valueForKey:"
- "viewDidDisappear:"
- "zone"

```
