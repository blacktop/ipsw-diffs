## NanoAppRegistry

> `/System/Library/PrivateFrameworks/NanoAppRegistry.framework/NanoAppRegistry`

```diff

-71.0.4.0.0
-  __TEXT.__text: 0x2554
-  __TEXT.__auth_stubs: 0x220
+71.0.5.0.0
+  __TEXT.__text: 0x2214
   __TEXT.__objc_methlist: 0x57c
-  __TEXT.__cstring: 0x251
+  __TEXT.__cstring: 0x257
   __TEXT.__const: 0x10
   __TEXT.__gcc_except_tab: 0x2c
-  __TEXT.__unwind_info: 0x170
-  __TEXT.__objc_classname: 0x91
-  __TEXT.__objc_methname: 0xd6f
-  __TEXT.__objc_methtype: 0x271
-  __TEXT.__objc_stubs: 0x6a0
-  __DATA_CONST.__got: 0xb8
+  __TEXT.__unwind_info: 0x140
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x1c0
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x20

   __DATA_CONST.__objc_selrefs: 0x3b0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x28
-  __AUTH_CONST.__auth_got: 0x120
+  __DATA_CONST.__got: 0xb8
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x340
   __AUTH_CONST.__objc_const: 0xbc8
-  __AUTH.__objc_data: 0xf0
+  __AUTH_CONST.__auth_got: 0x0
+  __AUTH.__objc_data: 0xa0
   __DATA.__objc_ivar: 0x54
   __DATA.__data: 0x188
-  __DATA.__bss: 0x30
-  __DATA_DIRTY.__objc_data: 0xa0
+  __DATA.__bss: 0x10
+  __DATA_DIRTY.__objc_data: 0xf0
+  __DATA_DIRTY.__bss: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: EA120324-11E9-3274-BE16-0ACB6A8B54EB
+  UUID: F1C1AFE8-F23D-388B-98B4-90F55E36DED9
   Functions: 106
-  Symbols:   454
-  CStrings:  284
+  Symbols:   458
+  CStrings:  61
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x2
+ _objc_retain_x22
+ _objc_retain_x23
+ _objc_retain_x3
+ _objc_retain_x8
- _objc_retain
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x21
Functions:
~ -[NARGlance encodeWithCoder:] : 252 -> 236
~ -[NARGlance initWithCoder:] : 360 -> 340
~ -[NARGlance description] : 140 -> 132
~ -[NARGlance debugDescription] : 148 -> 140
~ ___41-[NARApplicationWorkspace workspaceInfo:]_block_invoke : 240 -> 236
~ ___41-[NARApplicationWorkspace workspaceInfo:]_block_invoke_2 : 72 -> 16
~ ___41-[NARApplicationWorkspace workspaceInfo:]_block_invoke_3 : 72 -> 16
~ -[NARApplicationWorkspace getWorkspaceInfoWithCompletion:] : 188 -> 184
~ ___58-[NARApplicationWorkspace getWorkspaceInfoWithCompletion:]_block_invoke : 272 -> 260
~ -[NARApplicationWorkspace getWorkspaceInfoIncludingHiddenApps:completion:] : 196 -> 192
~ ___74-[NARApplicationWorkspace getWorkspaceInfoIncludingHiddenApps:completion:]_block_invoke : 280 -> 276
~ -[NARApplicationWorkspace _connectionInvalidated] : 140 -> 136
~ -[NARApplicationWorkspace _loadConnectionIfNeeded] : 296 -> 292
~ -[NARApplicationWorkspace setConnection:] : 64 -> 12
~ -[NARApplicationWorkspace setQueue:] : 64 -> 12
~ _nar_sync_log : 84 -> 68
~ _nar_workspace_log : 84 -> 68
~ -[NARWorkspaceInfo initWithCoder:] : 312 -> 296
~ -[NARWorkspaceInfo encodeWithCoder:] : 136 -> 128
~ -[NARWorkspaceInfo initWithApplications:UUID:sequenceNumber:] : 172 -> 188
~ -[NARApplicationState encodeWithCoder:] : 116 -> 108
~ -[NARApplication initWithCoder:] : 524 -> 492
~ ___32-[NARApplication initWithCoder:]_block_invoke : 240 -> 236
~ -[NARApplication encodeWithCoder:] : 300 -> 288
~ -[NARApplication applicationIdentifier] : 96 -> 88
~ -[NARApplication bundleName] : 96 -> 88
~ -[NARApplication localizedBundleNames] : 204 -> 200
~ ___38-[NARApplication localizedBundleNames]_block_invoke : 128 -> 124
~ -[NARApplication bundleVersion] : 96 -> 88
~ -[NARApplication localizedDisplayName] : 504 -> 436
~ -[NARApplication localizedDisplayNames] : 204 -> 200
~ ___39-[NARApplication localizedDisplayNames]_block_invoke : 128 -> 124
~ -[NARApplication vendorName] : 96 -> 88
~ -[NARApplication itemName] : 96 -> 88
~ -[NARApplication supportedSchemes] : 96 -> 88
~ -[NARApplication localizations] : 84 -> 76
~ -[NARApplication objectForInfoDictionaryKey:] : 116 -> 108
~ -[NARApplication objectForInfoDictionaryKey:localization:] : 156 -> 148
~ -[NARApplication description] : 216 -> 200
~ -[NARApplication setAppTags:] : 64 -> 12
~ -[NARApplication setAppState:] : 64 -> 12
~ -[NARApplication setInfoPlist:] : 64 -> 12
~ -[NARApplication setLocalizedStrings:] : 64 -> 12
~ -[NARApplication setITunesPlistStrings:] : 64 -> 12
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"NARApplicationState\""
- "@\"NSArray\""
- "@\"NSDictionary\""
- "@\"NSNumber\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSUUID\""
- "@\"NSXPCConnection\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@24@0:8@?16"
- "@24@0:8B16B20"
- "@24@0:8^@16"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@32"
- "@48@0:8@16@24@32@40"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "NARApplication"
- "NARApplicationState"
- "NARApplicationWorkspace"
- "NARGlance"
- "NARWorkspaceInfo"
- "NARWorkspaceService"
- "NSCoding"
- "NSObject"
- "NSSecureCoding"
- "Q"
- "Q16@0:8"
- "T#,R"
- "T@\"NARApplicationState\",&,N,V_appState"
- "T@\"NARGlance\",R,N"
- "T@\"NSArray\",&,N,V_appTags"
- "T@\"NSArray\",R,N"
- "T@\"NSArray\",R,N,V_applications"
- "T@\"NSArray\",R,N,V_standaloneGlances"
- "T@\"NSDictionary\",&,N,V_iTunesPlistStrings"
- "T@\"NSDictionary\",&,N,V_infoPlist"
- "T@\"NSDictionary\",&,N,V_localizedStrings"
- "T@\"NSDictionary\",C,N,V_localizedDisplayNameMap"
- "T@\"NSDictionary\",R,N"
- "T@\"NSNumber\",R,N,V_sequenceNumber"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_queue"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",C,N,V_appID"
- "T@\"NSString\",C,N,V_displayName"
- "T@\"NSString\",C,N,V_glanceID"
- "T@\"NSString\",C,N,V_launchServicesBundleType"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,C,N,V_parentApplicationBundleIdentifier"
- "T@\"NSString\",R,N"
- "T@\"NSUUID\",R,N,V_UUID"
- "T@\"NSXPCConnection\",&,N,V_connection"
- "TB,N,V_supportsForegroundApplication"
- "TB,R"
- "TB,R,N"
- "TB,R,N,GisRemovedSystemApp,V_removedSystemApp"
- "TB,R,N,GisRestricted,V_restricted"
- "TQ,N,V_sequenceNumber"
- "TQ,R"
- "Vv16@0:8"
- "Vv24@0:8@?16"
- "Vv24@0:8@?<v@?@\"NARWorkspaceInfo\">16"
- "Vv28@0:8B16@?20"
- "Vv28@0:8B16@?<v@?@\"NARWorkspaceInfo\">20"
- "^{_NSZone=}16@0:8"
- "_UUID"
- "_appID"
- "_appState"
- "_appTags"
- "_applications"
- "_connection"
- "_connectionInvalidated"
- "_displayName"
- "_glanceID"
- "_iTunesPlistStrings"
- "_infoPlist"
- "_launchServicesBundleType"
- "_loadConnectionIfNeeded"
- "_localizedDisplayNameMap"
- "_localizedStrings"
- "_parentApplicationBundleIdentifier"
- "_queue"
- "_removedSystemApp"
- "_restricted"
- "_sequenceNumber"
- "_standaloneGlances"
- "_supportsForegroundApplication"
- "_workspaceServiceWithErrorHandler:"
- "allKeys"
- "applicationIdentifier"
- "autorelease"
- "boolValue"
- "bundleName"
- "bundleVersion"
- "class"
- "componentsSeparatedByString:"
- "conformsToProtocol:"
- "connection"
- "containsObject:"
- "currentLocale"
- "dealloc"
- "debugDescription"
- "decodeBoolForKey:"
- "decodeObjectOfClass:forKey:"
- "decodeObjectOfClasses:forKey:"
- "description"
- "dictionary"
- "encodeBool:forKey:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "enumerateKeysAndObjectsUsingBlock:"
- "firstObject"
- "getWorkspaceInfoIncludingHiddenApps:completion:"
- "getWorkspaceInfoWithCompletion:"
- "glance"
- "hash"
- "init"
- "initWithApplications:UUID:sequenceNumber:"
- "initWithApplications:UUID:sequenceNumber:standaloneGlances:"
- "initWithCoder:"
- "initWithMachServiceName:options:"
- "initWithRestricted:removedSystemApp:"
- "interfaceWithProtocol:"
- "invalidate"
- "isEqual:"
- "isHidden"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "isRemovedSystemApp"
- "isRestricted"
- "languageCode"
- "lastObject"
- "localeIdentifier"
- "localizations"
- "localizedBundleNames"
- "localizedDisplayName"
- "localizedDisplayNames"
- "mainBundle"
- "numberWithBool:"
- "numberWithUnsignedInteger:"
- "objectForInfoDictionaryKey:"
- "objectForInfoDictionaryKey:localization:"
- "objectForKeyedSubscript:"
- "parentApplicationBundleIdentifier"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "preferredLocalizations"
- "queue"
- "release"
- "remoteObjectProxyWithErrorHandler:"
- "respondsToSelector:"
- "resume"
- "retain"
- "retainCount"
- "self"
- "setAppID:"
- "setAppState:"
- "setAppTags:"
- "setConnection:"
- "setDisplayName:"
- "setGlanceID:"
- "setITunesPlistStrings:"
- "setInfoPlist:"
- "setInvalidationHandler:"
- "setLaunchServicesBundleType:"
- "setLocalizedDisplayNameMap:"
- "setLocalizedStrings:"
- "setObject:forKeyedSubscript:"
- "setQueue:"
- "setRemoteObjectInterface:"
- "setSequenceNumber:"
- "setSupportsForegroundApplication:"
- "setWithObjects:"
- "standaloneGlances"
- "stringByAppendingFormat:"
- "stringByAppendingString:"
- "stringWithFormat:"
- "superclass"
- "supportedSchemes"
- "supportsSecureCoding"
- "synchronousRemoteObjectProxyWithErrorHandler:"
- "unsignedIntegerValue"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8Q16"
- "v28@0:8B16@?20"
- "vendorName"
- "workspaceInfo:"
- "zone"

```
