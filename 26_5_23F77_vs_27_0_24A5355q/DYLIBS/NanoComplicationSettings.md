## NanoComplicationSettings

> `/System/Library/PrivateFrameworks/NanoComplicationSettings.framework/NanoComplicationSettings`

```diff

 19.0.0.0.0
-  __TEXT.__text: 0x2c40
-  __TEXT.__auth_stubs: 0x340
+  __TEXT.__text: 0x2b00
   __TEXT.__objc_methlist: 0x2ac
   __TEXT.__const: 0x70
-  __TEXT.__cstring: 0x251
+  __TEXT.__cstring: 0x257
   __TEXT.__gcc_except_tab: 0x90
-  __TEXT.__unwind_info: 0x188
-  __TEXT.__objc_classname: 0x4e
-  __TEXT.__objc_methname: 0x9fa
-  __TEXT.__objc_methtype: 0x100
-  __TEXT.__objc_stubs: 0x940
-  __DATA_CONST.__got: 0xa0
+  __TEXT.__unwind_info: 0x180
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x258
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_catlist: 0x8

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x2d0
   __DATA_CONST.__objc_superrefs: 0x18
-  __AUTH_CONST.__auth_got: 0x1b0
+  __DATA_CONST.__got: 0xa0
   __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__cfstring: 0x220
   __AUTH_CONST.__objc_const: 0x4b0
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0xf0
   __DATA.__objc_ivar: 0x34
   __DATA.__data: 0x60

   - /System/Library/PrivateFrameworks/Preferences.framework/Preferences
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4ED4ADE8-3C11-37BC-957D-A11EB89DECE6
+  UUID: 1AF6E2E3-D6B8-3626-9FC6-4EE32548A35D
   Functions: 81
-  Symbols:   387
-  CStrings:  179
+  Symbols:   391
+  CStrings:  39
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x8
- _objc_retainAutoreleasedReturnValue
Functions:
~ -[NCSInternalSettingsManager selectedComplicationIdentifier] : 156 -> 144
~ -[NCSInternalSettingsManager setSelectedComplicationIdentifier:] : 244 -> 236
~ -[NCSInternalSettingsManager addComplicationDefinition:] : 160 -> 152
~ -[NCSInternalSettingsManager removeComplicationDefinitionsInArray:] : 168 -> 172
~ ___73-[NCSInternalSettingsManager enumerateComplicationDefinitionsUsingBlock:]_block_invoke : 128 -> 120
~ -[NCSInternalSettingsManager enumerateAllComplicationDefinitionsUsingBlock:] : 352 -> 356
~ ___74-[NCSInternalSettingsManager moveComplicationDefinitionFromIndex:toIndex:]_block_invoke : 124 -> 120
~ -[NCSInternalSettingsManager complicationDefinitionForAppBundleIdentifier:] : 300 -> 308
~ ___75-[NCSInternalSettingsManager complicationDefinitionForAppBundleIdentifier:]_block_invoke : 164 -> 152
~ -[NCSInternalSettingsManager complicationDefinitionForComplicationIdentifier:] : 300 -> 308
~ ___78-[NCSInternalSettingsManager complicationDefinitionForComplicationIdentifier:]_block_invoke : 164 -> 152
~ -[NCSInternalSettingsManager complicationDefinitionForWatchKitIdentifier:] : 300 -> 308
~ ___74-[NCSInternalSettingsManager complicationDefinitionForWatchKitIdentifier:]_block_invoke : 164 -> 152
~ -[NCSInternalSettingsManager _saveSettings] : 504 -> 496
~ -[NCSInternalSettingsManager complicationIdentifierForComplicationDefinitionAtIndex:] : 288 -> 284
~ ___85-[NCSInternalSettingsManager complicationIdentifierForComplicationDefinitionAtIndex:]_block_invoke : 88 -> 84
~ ___42-[NCSInternalSettingsManager loadSettings]_block_invoke : 684 -> 648
~ +[NSDictionary(NCSComplication) dictionaryWithComplication:] : 452 -> 416
~ -[NCSComplication initWithDictionary:] : 392 -> 368
~ -[NCSComplication complicationIdentifier] : 120 -> 100
~ -[NCSComplication copyWithZone:] : 272 -> 256
~ +[NCSSettingsManager sharedSettingsManager] : 84 -> 68
~ -[NCSSettingsManager init] : 336 -> 332
~ -[NCSSettingsManager dealloc] : 188 -> 184
~ -[NCSSettingsManager setDelegate:] : 172 -> 168
~ -[NCSSettingsManager loadSettings] : 120 -> 116
~ ___52-[NCSSettingsManager _updateSockPuppetComplications]_block_invoke : 540 -> 488
~ -[NCSSettingsManager _fetchSockPuppetComplications] : 748 -> 764
~ ___51-[NCSSettingsManager _fetchSockPuppetComplications]_block_invoke_2 : 112 -> 96
~ ___51-[NCSSettingsManager _fetchSockPuppetComplications]_block_invoke_4 : 112 -> 96
~ ___51-[NCSSettingsManager _fetchSockPuppetComplications]_block_invoke_5 : 640 -> 612
CStrings:
- ".cxx_destruct"
- "@\"<NCSSettingsManagerDelegate>\""
- "@\"NPSManager\""
- "@\"NSArray\""
- "@\"NSMutableArray\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSString\""
- "@16@0:8"
- "@24@0:8@16"
- "@24@0:8Q16"
- "@24@0:8^{_NSZone=}16"
- "B"
- "B16@0:8"
- "NCSComplication"
- "NCSInternalSettingsManager"
- "NCSSettingsManager"
- "NSCopying"
- "Q"
- "Q16@0:8"
- "T@\"<NCSSettingsManagerDelegate>\",W,N,V_delegate"
- "T@\"NSObject<OS_dispatch_queue>\",R,N,V_queue"
- "T@\"NSString\",C,N"
- "T@\"NSString\",C,N,V_appBundleIdentifier"
- "T@\"NSString\",C,N,V_complicationBundleIdentifier"
- "T@\"NSString\",C,N,V_name"
- "T@\"NSString\",C,N,V_sockPuppetIdentifier"
- "T@\"NSString\",R,N"
- "TB,N,GisActive,V_active"
- "TB,N,V_cannotBeDisabled"
- "TB,R,N"
- "TQ,N,V_installState"
- "_active"
- "_appBundleIdentifier"
- "_cannotBeDisabled"
- "_complicationBundleIdentifier"
- "_complicationDefinitions"
- "_delegate"
- "_fetchSockPuppetComplications"
- "_handleLocaleChange:"
- "_installState"
- "_localizedNameForComplication:"
- "_name"
- "_numberOfActiveComplications"
- "_queue"
- "_saveSettings"
- "_selectedComplicationIdentifier"
- "_sockPuppetIdentifier"
- "_storedSettings"
- "_syncManager"
- "_updateSockPuppetComplications"
- "addComplicationDefinition:"
- "addObject:"
- "addObserver:selector:name:object:"
- "allValues"
- "allocWithZone:"
- "appBundleIdentifier"
- "applicationProxyForIdentifier:"
- "array"
- "arrayForKey:"
- "arrayWithCapacity:"
- "boolValue"
- "cannotBeDisabled"
- "complicationBundleIdentifier"
- "complicationDefinitionForAppBundleIdentifier:"
- "complicationDefinitionForComplicationIdentifier:"
- "complicationDefinitionForWatchKitIdentifier:"
- "complicationIdentifier"
- "complicationIdentifierForComplicationDefinitionAtIndex:"
- "copy"
- "copyWithZone:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "dealloc"
- "defaultCenter"
- "delegate"
- "description"
- "dictionary"
- "dictionaryWithCapacity:"
- "dictionaryWithComplication:"
- "enumerateAllComplicationDefinitionsUsingBlock:"
- "enumerateComplicationDefinitionsUsingBlock:"
- "enumerateObjectsUsingBlock:"
- "fetchInstalledApplicationsForPairedDevice:completion:"
- "fetchInstalledComplicationsForPairedDevice:completion:"
- "hasSettings"
- "init"
- "initWithDictionary:"
- "initWithDomain:"
- "insertObject:atIndex:"
- "intValue"
- "integerValue"
- "isActive"
- "isEqualToArray:"
- "isEqualToString:"
- "isInstalled"
- "loadSettings"
- "localizedName"
- "moveComplicationDefinitionFromIndex:toIndex:"
- "mutableCopy"
- "numberWithBool:"
- "numberWithUnsignedInteger:"
- "objectAtIndexedSubscript:"
- "objectForKeyedSubscript:"
- "queue"
- "removeComplicationDefinitionsInArray:"
- "removeObjectAtIndex:"
- "removeObjectForKey:"
- "removeObjectsInArray:"
- "removeObserver:"
- "saveSettings"
- "selectedComplicationIdentifier"
- "setActive:"
- "setAppBundleIdentifier:"
- "setCannotBeDisabled:"
- "setComplicationBundleIdentifier:"
- "setDelegate:"
- "setInstallState:"
- "setName:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "setSelectedComplicationIdentifier:"
- "setSockPuppetIdentifier:"
- "setWithObject:"
- "settingsManagerReloadedComplications:"
- "sharedDeviceConnection"
- "sharedSettingsManager"
- "stringForKey:"
- "stringWithFormat:"
- "synchronize"
- "synchronizeNanoDomain:keys:"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8Q16"
- "v32@0:8Q16Q24"

```
