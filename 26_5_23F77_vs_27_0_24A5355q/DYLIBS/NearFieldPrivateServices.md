## NearFieldPrivateServices

> `/System/Library/PrivateFrameworks/NearFieldPrivateServices.framework/NearFieldPrivateServices`

```diff

-365.3.1.0.0
-  __TEXT.__text: 0x6c7c
-  __TEXT.__auth_stubs: 0x410
-  __TEXT.__objc_methlist: 0x48c
-  __TEXT.__const: 0x90
+370.33.1.0.0
+  __TEXT.__text: 0x79e0
+  __TEXT.__objc_methlist: 0x61c
+  __TEXT.__const: 0x98
   __TEXT.__dlopen_cstrs: 0x166
-  __TEXT.__cstring: 0x142c
-  __TEXT.__oslogstring: 0x638
-  __TEXT.__unwind_info: 0x190
-  __TEXT.__objc_classname: 0x10f
-  __TEXT.__objc_methname: 0x9ec
-  __TEXT.__objc_methtype: 0x29f
-  __TEXT.__objc_stubs: 0x7e0
-  __DATA_CONST.__got: 0x88
-  __DATA_CONST.__const: 0x508
-  __DATA_CONST.__objc_classlist: 0x40
+  __TEXT.__cstring: 0x173d
+  __TEXT.__oslogstring: 0x6e4
+  __TEXT.__unwind_info: 0x1a8
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x540
+  __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x378
+  __DATA_CONST.__objc_selrefs: 0x4b8
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x28
-  __DATA_CONST.__objc_arraydata: 0x80
-  __AUTH_CONST.__auth_got: 0x210
-  __AUTH_CONST.__const: 0x60
-  __AUTH_CONST.__cfstring: 0x580
-  __AUTH_CONST.__objc_const: 0x758
-  __AUTH_CONST.__objc_dictobj: 0xa0
-  __AUTH_CONST.__objc_intobj: 0xf0
-  __AUTH.__objc_data: 0xf0
-  __DATA.__objc_ivar: 0x1c
+  __DATA_CONST.__objc_superrefs: 0x38
+  __DATA_CONST.__got: 0xb8
+  __AUTH_CONST.__const: 0x80
+  __AUTH_CONST.__cfstring: 0x820
+  __AUTH_CONST.__objc_const: 0x940
+  __AUTH_CONST.__objc_intobj: 0x108
+  __AUTH_CONST.__auth_got: 0x0
+  __AUTH.__objc_data: 0x190
+  __DATA.__objc_ivar: 0x30
   __DATA.__data: 0x180
   __DATA.__bss: 0x68
   __DATA_DIRTY.__objc_data: 0x190

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libnfshared.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 756E4C9E-45B6-39C0-9950-B1B354FDEEC0
-  Functions: 94
-  Symbols:   102
-  CStrings:  453
+  UUID: 7C897C31-EBA9-3B82-894C-443413AE6F78
+  Functions: 126
+  Symbols:   119
+  CStrings:  332
 
Symbols:
+ _OBJC_CLASS_$_NFLocation
+ _OBJC_CLASS_$_NFLocationService
+ _OBJC_CLASS_$_NFLocationServiceListener
+ _OBJC_CLASS_$_NSData
+ _OBJC_CLASS_$_NSMutableDictionary
+ _OBJC_CLASS_$_NSSet
+ _OBJC_CLASS_$_NSUUID
+ _OBJC_METACLASS_$_NFLocationService
+ _OBJC_METACLASS_$_NFLocationServiceListener
+ ___assert_rtn
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x25
+ _objc_retain_x26
+ _objc_retain_x3
+ _objc_retain_x8
+ _objc_storeWeak
- _OBJC_CLASS_$_NSConstantDictionary
- _objc_retainAutoreleasedReturnValue
CStrings:
+ "!"
+ "%s:%i Disconnect service due to 0 listeners registered"
+ "%s:%i Failed to call into service for operation %@, model %@ : %@"
+ "%s:%i Failed to call into service for operation %@, model %@ : no result.."
+ "%s:%i Listener not found for bundle %{public}@"
+ "%{public}s:%i Disconnect service due to 0 listeners registered"
+ "%{public}s:%i Failed to call into service for operation %@, model %@ : %@"
+ "%{public}s:%i Failed to call into service for operation %@, model %@ : no result.."
+ "%{public}s:%i Listener not found for bundle %{public}@"
+ "-[NFLocationService invalidateListener:]"
+ "-[NFLocationService notifyLocationAuthDenied:]"
+ "-[NFLocationService notifyLocationSimulationDetected:]"
+ "-[NFLocationService notifyLocationUpdate:location:]"
+ "-[NFLocationService startListenerWithBundleIdentifier:delegate:error:]"
+ "-[NFStorageService executeOperation:onModel:withParams:outError:]"
+ "CoreNFCUI_Access"
+ "CoreNFCUI_ScanMode"
+ "Delete"
+ "DeveloperPresentment"
+ "DeveloperPresentmentReceipt"
+ "Location service is not authorized"
+ "Location simulation detected"
+ "NFLocationService.m"
+ "Params"
+ "User has denied access to location services"
+ "action"
+ "authDenied"
+ "begin"
+ "bundleID"
+ "com.apple.stockholm.services.NFLocationService"
+ "isOnDenyList"
+ "lastSentTimestamp"
+ "location"
+ "locationSimulated"
+ "locationUpdate"
+ "nil != bundleIdentifier"
+ "nil != listener"
+ "presentmentData"
+ "reportID"
+ "reportReadyToSend"
+ "teamID"
+ "timestampDay"
- "#16@0:8"
- "%s:%i Failed to call into service : %@"
- "%s:%i Failed to call into service : no result.."
- "%{public}s:%i Failed to call into service : %@"
- "%{public}s:%i Failed to call into service : no result.."
- "-[NFStorageService deleteAllAppletEntities]"
- "-[NFStorageService deleteAllESEExpressEntities]"
- "-[NFStorageService updateAppletEntitiesWithConfig:]"
- "-[NFStorageService updateESEExpressEntitiesWithConfig:]"
- ".cxx_destruct"
- "@"
- "@\"BSServiceConnection<BSServiceConnectionClient>\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSString\"16@0:8"
- "@\"NSXPCConnection\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@24@0:8^@16"
- "@32@0:8:16@24"
- "@32@0:8@16^@24"
- "@40@0:8:16@24@32"
- "@?"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "Config"
- "NFBSClient_BackgroundTagReading"
- "NFBSService_BackgroundTagReadingXPC"
- "NFBSService_BackgroundTagReadingXPCProtocol"
- "NFPrivateService"
- "NFPrivateServiceFrameworkInterface"
- "NFPrivateServiceInterface"
- "NFRadioPowerSwitch"
- "NFRestoreService"
- "NFStorageService"
- "NFUIService"
- "NSObject"
- "Q16@0:8"
- "T#,R"
- "T@\"BSServiceConnection<BSServiceConnectionClient>\",&,N,V_connection"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_workQueue"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@,&,V_debugContext"
- "TB,N,V_invalidated"
- "TQ,R"
- "Vv16@0:8"
- "Vv24@0:8@16"
- "Vv32@0:8@\"NSDictionary\"16@\"NSError\"24"
- "Vv32@0:8@\"NSDictionary\"16@?<v@?@\"NSDictionary\"@\"NSError\">24"
- "Vv32@0:8@16@24"
- "Vv32@0:8@16@?24"
- "^{_NSZone=}16@0:8"
- "_activate"
- "_connection"
- "_debugContext"
- "_iVarLock"
- "_init"
- "_invalidateFromRemote:"
- "_invalidated"
- "_setQueue:"
- "_sync_disconnect"
- "_uiInvalidationHandler"
- "_workQueue"
- "_xpcConnection"
- "activate"
- "arrayWithObjects:count:"
- "attributeWithDomain:name:"
- "autorelease"
- "boolValue"
- "canRun"
- "class"
- "code"
- "configureConnection:"
- "conformsToProtocol:"
- "connectToService:outError:"
- "connection"
- "connectionWithEndpoint:"
- "copy"
- "coreNFCShowPaymentSessionGoToSettingsPrompt:"
- "coreNFCUIActivateWithCompletion:"
- "coreNFCUIInvalidate"
- "coreNFCUISetInvalidationHandler:"
- "coreNFCUISetMode:"
- "coreNFCUISetScanText:"
- "coreNFCUITagScannedCount:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "dealloc"
- "debugContext"
- "debugDescription"
- "deleteAllAppletEntities"
- "deleteAllESEExpressEntities"
- "description"
- "dictionaryWithDictionary:"
- "dictionaryWithObjects:forKeys:count:"
- "disconnect"
- "endpointForMachName:service:instance:"
- "errorWithDomain:code:userInfo:"
- "executeWithLock:"
- "fetchAppletEntitiesWithError:"
- "fetchESEExpressEntitiesWithError:"
- "hash"
- "init"
- "initWithDictionary:"
- "initWithDomain:code:userInfo:"
- "initWithFormat:"
- "initWithServiceName:"
- "integerValue"
- "interface"
- "interfaceWithIdentifier:"
- "interfaceWithProtocol:"
- "invalidated"
- "isEqual:"
- "isEqualToString:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "isResultSuccessful:"
- "launchBundleWithIdentifier:launchReason:launchDomain:"
- "numberWithDouble:"
- "numberWithInteger:"
- "numberWithUnsignedInteger:"
- "objectForKey:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "processNDEF:tag:reply:"
- "protocolForProtocol:"
- "release"
- "remoteObjectProxyWithErrorHandler:"
- "remoteTarget"
- "remoteTargetWithLaunchingAssertionAttributes:"
- "requestUserSettingsNotificationWithCompletion:popupInterval:"
- "respondsToSelector:"
- "resume"
- "retain"
- "retainCount"
- "runService:"
- "runService:callback:"
- "runService:withCompletion:"
- "sceneServiceAvailable"
- "sceneServiceBackgroundTagReadingWithNDEF:tag:completion:"
- "self"
- "serviceName"
- "serviceNotificationReceived:"
- "serviceNotificationReceived:error:"
- "setConnection:"
- "setDebugContext:"
- "setExportedInterface:"
- "setExportedObject:"
- "setInterface:"
- "setInvalidated:"
- "setInvalidationHandler:"
- "setRemoteObjectInterface:"
- "setServer:"
- "setServiceQuality:"
- "setTargetQueue:"
- "setWorkQueue:"
- "sharedClient"
- "stringWithUTF8String:"
- "superclass"
- "synchronousRemoteObjectProxyWithErrorHandler:"
- "updateAppletEntitiesWithConfig:"
- "updateESEExpressEntitiesWithConfig:"
- "userInitiated"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8q16"
- "v32@0:8@16@?24"
- "v32@0:8@?16d24"
- "v40@0:8@\"NSData\"16@\"NSData\"24@?<v@?@\"NSError\">32"
- "v40@0:8@16@24@?32"
- "v40@0:8@16Q24q32"
- "valueForKey:"
- "workQueue"
- "zone"
- "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"

```
