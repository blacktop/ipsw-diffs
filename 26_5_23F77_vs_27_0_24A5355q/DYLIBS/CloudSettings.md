## CloudSettings

> `/System/Library/PrivateFrameworks/CloudSettings.framework/CloudSettings`

```diff

 113.0.0.0.0
-  __TEXT.__text: 0x6d30
-  __TEXT.__auth_stubs: 0x300
+  __TEXT.__text: 0x64d8
   __TEXT.__objc_methlist: 0x53c
   __TEXT.__const: 0x98
-  __TEXT.__cstring: 0x335
+  __TEXT.__cstring: 0x33d
   __TEXT.__oslogstring: 0x2456
   __TEXT.__gcc_except_tab: 0x50
-  __TEXT.__unwind_info: 0x128
-  __TEXT.__objc_classname: 0xd5
-  __TEXT.__objc_methname: 0xa45
-  __TEXT.__objc_methtype: 0x2ea
-  __TEXT.__objc_stubs: 0x9c0
-  __DATA_CONST.__got: 0x90
+  __TEXT.__unwind_info: 0x110
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x70
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x20

   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_arraydata: 0x200
-  __AUTH_CONST.__auth_got: 0x190
+  __DATA_CONST.__got: 0x90
   __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__cfstring: 0x340
   __AUTH_CONST.__objc_const: 0x808
   __AUTH_CONST.__objc_dictobj: 0x2a8
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0x20
   __DATA.__data: 0x180
   __DATA_DIRTY.__objc_data: 0x190

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 02B8E211-07C0-3FF6-87C9-686C63D34C60
+  UUID: FC8AA6E1-39EF-395D-BCDD-FEBACC63265B
   Functions: 77
-  Symbols:   385
-  CStrings:  388
+  Symbols:   390
+  CStrings:  202
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x2
+ _objc_retain_x3
+ _objc_retain_x8
- _objc_retainAutoreleasedReturnValue
Functions:
~ +[CloudSettingsManager sharedCloudSettingsManager] : 84 -> 68
~ -[CloudSettingsManager setEnabled:forStore:] : 696 -> 644
~ -[CloudSettingsManager isEnabledForStore:] : 660 -> 608
~ -[CloudSettingsManager setConflict:forStore:] : 472 -> 420
~ -[CloudSettingsManager conflictStateForStore:] : 548 -> 496
~ -[CloudSettingsManager isServiceKnownForStore:] : 348 -> 296
~ -[CloudSettingsManager performFirstTimeSetup:] : 1140 -> 1128
~ -[CloudSettingsManager applyCloudSettingsToDevice:forStore:] : 636 -> 588
~ -[CloudSettingsManager writeToCloudSettings:forStore:] : 636 -> 588
~ -[CloudSettingsManager deviceSettingsForStore:] : 816 -> 760
~ -[CloudSettingsManager applySettingsToDevice:forStore:] : 744 -> 696
~ -[CloudSettingsManager defaultSettingsDictionary] : 400 -> 388
~ -[CloudSettingsManager writeSettingsDictionaryToPrefs:] : 216 -> 172
~ -[CloudSettingsManager currentStateDictionary] : 548 -> 492
~ -[CloudSettingsManager activeXPCConnectionForStore:] : 284 -> 236
~ -[CloudSettingsManager currentConflictDictionary] : 548 -> 492
~ -[CloudSettingsManager writeConflictsDictionaryToPrefs:] : 216 -> 172
~ -[CloudSettingsStore initWithStoreIdentifier:] : 500 -> 464
~ -[CloudSettingsStore keyExists:andIsOfType:] : 1020 -> 972
~ -[CloudSettingsStore setBool:forKey:] : 568 -> 512
~ -[CloudSettingsStore boolForKey:] : 540 -> 488
~ -[CloudSettingsStore setNumber:forKey:] : 544 -> 496
~ -[CloudSettingsStore numberForKey:] : 772 -> 716
~ -[CloudSettingsStore setString:forKey:] : 544 -> 496
~ -[CloudSettingsStore stringForKey:] : 772 -> 716
~ -[CloudSettingsStore setArray:forKey:] : 544 -> 496
~ -[CloudSettingsStore arrayForKey:] : 772 -> 716
~ -[CloudSettingsStore setData:forKey:] : 544 -> 496
~ -[CloudSettingsStore dataForKey:] : 772 -> 716
~ -[CloudSettingsStore setDictionary:forKey:] : 640 -> 588
~ -[CloudSettingsStore dictionaryForKey:] : 564 -> 508
~ -[CloudSettingsStore removeObjectForKey:] : 624 -> 568
~ -[CloudSettingsStore syncNow:] : 496 -> 420
~ -[CloudSettingsStore setObject:forKey:] : 504 -> 456
~ -[CloudSettingsStore objectForKey:] : 460 -> 408
~ -[CloudSettingsService initWithStoreIdentifier:settingsMediator:] : 176 -> 180
~ -[CloudSettingsService performFirstTimeSetupForStore:newDevice:] : 596 -> 536
~ -[CloudSettingsService applyCloudSettingsToDevice:forStore:] : 952 -> 912
~ -[CloudSettingsService writeToCloudSettingsDict:forStore:] : 756 -> 724
~ -[CloudSettingsService writeToCloudSettings:forStore:] : 152 -> 148
~ -[CloudSettingsService performSmartMergeWithStoreSettings:] : 1444 -> 1384
~ -[CloudSettingsService setIdentifier:] : 64 -> 12
~ -[CloudSettingsService setStore:] : 64 -> 12
~ -[CloudSettingsService setMediator:] : 64 -> 12
~ -[CloudSettingsServiceDelegate initWithStoreIdentifier:settingsMediator:] : 156 -> 160
~ -[CloudSettingsServiceDelegate listener:shouldAcceptNewConnection:] : 156 -> 148
~ -[CloudSettingsDispatchingMediator registerKey:getter:setter:merger:type:] : 388 -> 372
~ -[CloudSettingsDispatchingMediator deviceSettingsForKeys:] : 580 -> 560
~ -[CloudSettingsDispatchingMediator mergeSettings:] : 1216 -> 1176
~ ___50-[CloudSettingsDispatchingMediator mergeSettings:]_block_invoke : 112 -> 108
~ ___50-[CloudSettingsDispatchingMediator mergeSettings:]_block_invoke.3 : 140 -> 132
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"<CloudSettingsMediator>\""
- "@\"CloudSettingsService\""
- "@\"CloudSettingsStore\""
- "@\"NSDictionary\"16@0:8"
- "@\"NSDictionary\"24@0:8@\"NSArray\"16"
- "@\"NSDictionary\"24@0:8@\"NSDictionary\"16"
- "@\"NSMutableDictionary\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSUbiquitousKeyValueStore\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@40@0:8:16@24@32"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B32@0:8@\"NSXPCListener\"16@\"NSXPCConnection\"24"
- "B32@0:8@16@24"
- "CloudSettingsDispatchingMediator"
- "CloudSettingsManager"
- "CloudSettingsMediator"
- "CloudSettingsService"
- "CloudSettingsServiceDelegate"
- "CloudSettingsServiceProtocol"
- "CloudSettingsStore"
- "NSObject"
- "NSXPCListenerDelegate"
- "Q16@0:8"
- "T#,R"
- "T@\"<CloudSettingsMediator>\",&,N,V_mediator"
- "T@\"CloudSettingsService\",&,V_service"
- "T@\"CloudSettingsStore\",&,N,V_store"
- "T@\"NSMutableDictionary\",&,V_keysMap"
- "T@\"NSString\",&,N,V_identifier"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,V_serviceIdentifier"
- "T@\"NSUbiquitousKeyValueStore\",R,V_kvsStore"
- "TB,V_dispatchSettersOnMain"
- "TQ,R"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_dispatchSettersOnMain"
- "_identifier"
- "_initWithStoreIdentifier:usingEndToEndEncryption:"
- "_keysMap"
- "_kvsStore"
- "_mediator"
- "_service"
- "_serviceIdentifier"
- "_store"
- "activeXPCConnectionForStore:"
- "allKeys"
- "applyCloudSettingsToDevice:forStore:"
- "applySettings:"
- "applySettingsToDevice:"
- "applySettingsToDevice:forStore:"
- "arrayForKey:"
- "arrayWithObjects:count:"
- "autorelease"
- "boolForKey:"
- "boolValue"
- "class"
- "conflictStateForStore:"
- "conformsToProtocol:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "currentConflictDictionary"
- "currentStateDictionary"
- "dataForKey:"
- "debugDescription"
- "defaultSettingsDictionary"
- "description"
- "deviceSettings"
- "deviceSettingsForKeys:"
- "deviceSettingsForStore:"
- "dictionary"
- "dictionaryForKey:"
- "dictionaryRepresentation"
- "dictionaryWithDictionary:"
- "dictionaryWithObjects:forKeys:count:"
- "dispatchSettersOnMain"
- "hash"
- "i32@0:8@16@24"
- "identifier"
- "init"
- "initWithServiceName:"
- "initWithStoreIdentifier:"
- "initWithStoreIdentifier:settingsMediator:"
- "intValue"
- "interfaceWithProtocol:"
- "invalidate"
- "isEnabledForStore:"
- "isEqual:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "isServiceKnownForStore:"
- "keyExists:andIsOfType:"
- "keysMap"
- "knownServiceNames"
- "kvsStore"
- "length"
- "listener:shouldAcceptNewConnection:"
- "mediator"
- "mergeSettings:"
- "methodForSelector:"
- "numberForKey:"
- "numberWithBool:"
- "numberWithInteger:"
- "objectAtIndexedSubscript:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "performFirstTimeSetup:"
- "performFirstTimeSetupForStore:"
- "performFirstTimeSetupForStore:newDevice:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "performSmartMergeWithStoreSettings:"
- "q24@0:8@16"
- "registerKey:getter:setter:"
- "registerKey:getter:setter:merger:type:"
- "registerKeys"
- "release"
- "remoteObjectProxy"
- "removeObjectForKey:"
- "respondsToSelector:"
- "resume"
- "retain"
- "retainCount"
- "self"
- "service"
- "serviceIdentifier"
- "setArray:forKey:"
- "setBool:forKey:"
- "setConflict:forStore:"
- "setData:forKey:"
- "setDictionary:forKey:"
- "setDispatchSettersOnMain:"
- "setEnabled:forStore:"
- "setExportedInterface:"
- "setExportedObject:"
- "setIdentifier:"
- "setKeysMap:"
- "setMediator:"
- "setNumber:forKey:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "setRemoteObjectInterface:"
- "setService:"
- "setStore:"
- "setString:forKey:"
- "sharedCloudSettingsManager"
- "store"
- "stringForKey:"
- "stringWithFormat:"
- "superclass"
- "syncNow:"
- "synchronize"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@\"NSDictionary\"16"
- "v24@0:8@\"NSString\"16"
- "v24@0:8@16"
- "v28@0:8@\"NSString\"16B24"
- "v28@0:8@16B24"
- "v28@0:8B16@20"
- "v32@0:8@\"NSArray\"16@\"NSString\"24"
- "v32@0:8@16@24"
- "v32@0:8q16@24"
- "v40@0:8@16:24:32"
- "v56@0:8@16:24:32:40@48"
- "writeConflictsDictionaryToPrefs:"
- "writeSettingsDictionaryToPrefs:"
- "writeToCloudSettings:forStore:"
- "writeToCloudSettingsDict:forStore:"
- "zone"

```
