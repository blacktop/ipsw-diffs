## libMobileGestaltExtensions.dylib

> `/usr/lib/libMobileGestaltExtensions.dylib`

```diff

-1484.120.3.0.0
-  __TEXT.__text: 0x684c
-  __TEXT.__auth_stubs: 0x610
-  __TEXT.__objc_methlist: 0x364
+1608.0.0.0.0
+  __TEXT.__text: 0x5fd4
+  __TEXT.__objc_methlist: 0x32c
   __TEXT.__const: 0x58
-  __TEXT.__cstring: 0x15f7
-  __TEXT.__gcc_except_tab: 0x10c
-  __TEXT.__oslogstring: 0x6bf
+  __TEXT.__cstring: 0x1773
+  __TEXT.__gcc_except_tab: 0xe4
+  __TEXT.__oslogstring: 0x74f
   __TEXT.__dlopen_cstrs: 0xc4
-  __TEXT.__unwind_info: 0x260
-  __TEXT.__objc_classname: 0x9d
-  __TEXT.__objc_methname: 0xb86
-  __TEXT.__objc_methtype: 0x3ca
-  __TEXT.__objc_stubs: 0xba0
-  __DATA_CONST.__got: 0xc0
-  __DATA_CONST.__const: 0x8e0
-  __DATA_CONST.__objc_classlist: 0x20
+  __TEXT.__unwind_info: 0x240
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x900
+  __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3d8
+  __DATA_CONST.__objc_selrefs: 0x3c0
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0x318
+  __DATA_CONST.__objc_superrefs: 0x18
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x80
   __AUTH_CONST.__cfstring: 0x6e0
-  __AUTH_CONST.__objc_const: 0x6c8
-  __AUTH.__objc_data: 0x50
-  __DATA.__objc_ivar: 0x4c
-  __DATA.__data: 0x184
-  __DATA.__bss: 0x70
-  __DATA.__common: 0x1c
+  __AUTH_CONST.__objc_const: 0x550
+  __AUTH_CONST.__auth_got: 0x0
+  __DATA.__objc_ivar: 0x30
+  __DATA.__data: 0x180
+  __DATA.__bss: 0x80
+  __DATA.__common: 0x10
   __DATA_DIRTY.__objc_data: 0xf0
   __DATA_DIRTY.__bss: 0x18
   __DATA_DIRTY.__common: 0x18

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 52517774-BFB4-38EC-89BD-857A9BCDE36E
-  Functions: 167
-  Symbols:   128
-  CStrings:  475
+  UUID: 1554A0E5-EE08-3348-8D8A-8793E5DE5855
+  Functions: 153
+  Symbols:   120
+  CStrings:  288
 
Symbols:
+ ___stderrp
+ _fwrite
+ _kIOMainPortDefault
+ _os_unfair_lock_lock
+ _os_unfair_lock_unlock
- __dispatch_source_type_vnode
- _close
- _dispatch_release
- _dispatch_resume
- _dispatch_source_cancel
- _dispatch_source_create
- _dispatch_source_set_cancel_handler
- _dispatch_source_set_event_handler
- _fstat
- _kIOMasterPortDefault
- _objc_retain_x22
- _open
- _rindex
CStrings:
+ "!!! IMPL ERROR !!! RefCount is non-zero yet _connection is null!\n"
+ "!!! IMPL ERROR !!! RefCount is zero yet _connection is non-null!\n"
+ "AppleBiometricServices io_service_t failed to be released!"
+ "Error: Connection to AppleBiometricServices could not be initialized!"
+ "Error: RefCount equal to zero is trying to get decremented!"
+ "Error: RefCount reached its maximum value!"
+ "IOObjectRelease(service) == 0 "
+ "Implementation error: Connection handle to AppleBiometricServices has a non-zero refcount and should be non-null but the handle is null!"
+ "Implementation error: Connection handle to AppleBiometricServices has a refcount of zero and should be null but the handle is non-null!"
+ "MGNotificationTypeFile not supported"
+ "MGNotifications.m"
+ "_connectHandle != ((io_object_t) 0)"
+ "_connectHandleRefCount < 4294967295U"
+ "_connectHandleRefCount > 0"
+ "err != (((signed)((((unsigned)(0x38))&0x3f)<<26))|(((0)&0xfff)<<14)|0x1)"
+ "wasRetained"
- "#16@0:8"
- "(?=\"_darwinTokens\"@\"NSMutableArray\"\"_scPrefs\"^{__SCPreferences}\"_fileWatcher\"@\"MGFileWatcher\"\"_mcConnection\"@\"MCProfileConnection\"\"_mainDisplay\"@\"CADisplay\"\"_swBehaviorHandle\"^v\"_ctCenter\"^{__CTServerConnection}\"_scdynaStore\"^{__SCDynamicStore})"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/MobileGestaltSupport/MobileGestaltExtensions/MGNotifications.m"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/MobileGestaltSupport/MobileGestaltExtensions/MobileGestaltSupport.m"
- "@\"<MobileGestaltHelper>\""
- "@\"NSMutableDictionary\""
- "@\"NSMutableSet\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSObject<OS_dispatch_source>\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSXPCConnection\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8^{_NSZone=}16"
- "@28@0:8i16@20"
- "@32@0:8:16@24"
- "@32@0:8@16@?24"
- "@40@0:8:16@24@32"
- "@?"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B36@0:8i16r*20@28"
- "MCProfileConnectionObserver"
- "MGFileWatcher"
- "MGNotificationObserver"
- "MGNotificationRegistration"
- "MobileGestaltHelper"
- "MobileGestaltHelperProxy"
- "NSCopying"
- "NSObject"
- "Q"
- "Q16@0:8"
- "T#,R"
- "T@\"<MobileGestaltHelper>\",R,V_helper"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSXPCConnection\",R,V_connection"
- "TQ,R"
- "Ti,V_error"
- "UTF8String"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_addBlock:"
- "_argument"
- "_block"
- "_blocks"
- "_cancelRegistration"
- "_connection"
- "_deliverNotifications"
- "_error"
- "_helper"
- "_inode"
- "_mtime"
- "_observers"
- "_parentSrc"
- "_path"
- "_queue"
- "_registration"
- "_removeBlock:"
- "_requestedRegistrations"
- "_src"
- "_type"
- "_xpcConnection"
- "addObject:"
- "addObserver:"
- "addObserver:forKeyPath:options:context:"
- "allObjects"
- "arrayWithObjects:count:"
- "autorelease"
- "awdKey"
- "boolValue"
- "bundleWithPath:"
- "can't open parent for %@"
- "cancel"
- "class"
- "code"
- "com.apple.MobileGestalt.MGFileWatcher"
- "componentsSeparatedByString:"
- "conformsToProtocol:"
- "connection"
- "copy"
- "copyWithZone:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "crashreporterKey"
- "currentHandler"
- "dataWithPropertyList:format:options:error:"
- "dealloc"
- "debugDescription"
- "description"
- "dictionaryWithContentsOfFile:"
- "domain"
- "effectiveBoolValueForSetting:"
- "fileSystemRepresentation"
- "getAppleTVMode:"
- "getMobileEquipmentInfo:"
- "getPhoneNumber:error:"
- "getSIMStatus:error:"
- "getSIMTrayStatusOrError:"
- "getServerAnswerForQuestion:reply:"
- "getSpringboardRegionOverride:reply:"
- "getSubscriptionInfoWithError:"
- "handleFailureInFunction:file:lineNumber:description:"
- "hash"
- "helper"
- "i"
- "i16@0:8"
- "init"
- "initWithFormat:"
- "initWithMachServiceName:options:"
- "initWithPath:block:"
- "initWithQueue:block:"
- "initWithString:"
- "initWithType:argument:"
- "intValue"
- "interfaceWithProtocol:"
- "invalidate"
- "invokeBlocks"
- "isEqual:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isPresent"
- "isProxy"
- "localizations"
- "localizedDescription"
- "localizedStringForKey:value:table:"
- "localizedStringForKey:value:table:localization:"
- "mainDisplay"
- "meInfoList"
- "number"
- "numberWithInt:"
- "objectAtIndexedSubscript:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "observeValueForKeyPath:ofObject:change:context:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "preferredLocalizationsFromArray:forPreferences:"
- "processIdentifier"
- "profileConnectionDidReceiveAppWhitelistChangedNotification:userInfo:"
- "profileConnectionDidReceiveDefaultsChangedNotification:userInfo:"
- "profileConnectionDidReceiveEffectiveSettingsChangedNotification:userInfo:"
- "profileConnectionDidReceivePasscodeChangedNotification:userInfo:"
- "profileConnectionDidReceivePasscodePolicyChangedNotification:userInfo:"
- "profileConnectionDidReceiveProfileListChangedNotification:userInfo:"
- "profileConnectionDidReceiveRestrictionChangedNotification:userInfo:"
- "proxy"
- "proxyRebuildCache"
- "proxySetCacheSentinel"
- "rebuildCache:"
- "registerForNotification:argument:question:"
- "release"
- "removeAllObjects"
- "removeObject:"
- "removeObjectForKey:"
- "removeObserver:"
- "removeObserver:forKeyPath:"
- "respondsToSelector:"
- "resume"
- "retain"
- "retainCount"
- "self"
- "setCacheSentinel:"
- "setError:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "setRemoteObjectInterface:"
- "sharedClient"
- "sharedConnection"
- "slotID"
- "slotId"
- "start"
- "startDynaStoreMonitoringWithArgument:"
- "stringByDeletingLastPathComponent"
- "stringWithUTF8String:"
- "subscriptions"
- "superclass"
- "synchronousRemoteObjectProxyWithErrorHandler:"
- "updateWatcher"
- "v16@0:8"
- "v20@0:8i16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?@\"NSDictionary\">16"
- "v24@0:8@?<v@?B>16"
- "v32@0:8@\"MCProfileConnection\"16@\"NSDictionary\"24"
- "v32@0:8@\"NSString\"16@?<v@?@\"NSDictionary\">24"
- "v32@0:8@\"NSString\"16@?<v@?@\"NSNumber\">24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v48@0:8@16@24@32^v40"
- "valueForEntitlement:"
- "writeToFile:options:error:"
- "zone"
- "{timespec=\"tv_sec\"q\"tv_nsec\"q}"

```
