## NearFieldPrivateServices

> `/System/Library/PrivateFrameworks/NearFieldPrivateServices.framework/NearFieldPrivateServices`

```diff

-355.4.0.0.0
-  __TEXT.__text: 0x5708
-  __TEXT.__auth_stubs: 0x3a0
-  __TEXT.__objc_methlist: 0x36c
+360.33.0.0.0
+  __TEXT.__text: 0x77dc
+  __TEXT.__auth_stubs: 0x440
+  __TEXT.__objc_methlist: 0x45c
   __TEXT.__const: 0x98
-  __TEXT.__cstring: 0xcf4
-  __TEXT.__oslogstring: 0x533
-  __TEXT.__gcc_except_tab: 0xf4
-  __TEXT.__unwind_info: 0x118
-  __TEXT.__objc_classname: 0xb2
-  __TEXT.__objc_methname: 0x6d1
-  __TEXT.__objc_methtype: 0x1d4
-  __TEXT.__objc_stubs: 0x480
-  __DATA_CONST.__got: 0x80
-  __DATA_CONST.__const: 0x330
-  __DATA_CONST.__objc_classlist: 0x38
-  __DATA_CONST.__objc_protolist: 0x18
+  __TEXT.__dlopen_cstrs: 0x166
+  __TEXT.__cstring: 0x10c0
+  __TEXT.__oslogstring: 0x74d
+  __TEXT.__unwind_info: 0x170
+  __TEXT.__objc_classname: 0x10f
+  __TEXT.__objc_methname: 0x9a3
+  __TEXT.__objc_methtype: 0x263
+  __TEXT.__objc_stubs: 0x7a0
+  __DATA_CONST.__got: 0x88
+  __DATA_CONST.__const: 0x4b0
+  __DATA_CONST.__objc_classlist: 0x40
+  __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x278
-  __DATA_CONST.__objc_protorefs: 0x10
+  __DATA_CONST.__objc_selrefs: 0x360
+  __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x28
   __DATA_CONST.__objc_arraydata: 0x80
-  __AUTH_CONST.__auth_got: 0x1e0
-  __AUTH_CONST.__cfstring: 0x540
-  __AUTH_CONST.__objc_const: 0x878
+  __AUTH_CONST.__auth_got: 0x228
+  __AUTH_CONST.__const: 0x40
+  __AUTH_CONST.__cfstring: 0x580
+  __AUTH_CONST.__objc_const: 0x6d8
   __AUTH_CONST.__objc_dictobj: 0xa0
-  __AUTH_CONST.__objc_intobj: 0xd8
-  __AUTH.__objc_data: 0x140
-  __DATA.__objc_ivar: 0xc
-  __DATA.__data: 0x120
-  __DATA_DIRTY.__objc_data: 0xf0
+  __AUTH_CONST.__objc_intobj: 0xf0
+  __AUTH.__objc_data: 0xf0
+  __DATA.__objc_ivar: 0x18
+  __DATA.__data: 0x180
+  __DATA.__bss: 0x68
+  __DATA_DIRTY.__objc_data: 0x190
+  __DATA_DIRTY.__bss: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
+  - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libnfshared.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0DB9EA6C-253C-3A04-8678-0B6047C914D8
-  Functions: 50
-  Symbols:   292
-  CStrings:  332
+  UUID: 9FD3C3CB-89A8-32D1-A020-EB8B52364DA9
+  Functions: 85
+  Symbols:   105
+  CStrings:  416
 
Symbols:
+ _OBJC_CLASS_$_NFBSService_BackgroundTagReadingXPC
+ _OBJC_METACLASS_$_NFBSService_BackgroundTagReadingXPC
+ __NSConcreteGlobalBlock
+ __os_activity_create
+ __os_activity_current
+ __sl_dlopen
+ _dispatch_once
+ _dispatch_sync
+ _objc_copyWeak
+ _objc_destroyWeak
+ _objc_getClass
+ _objc_initWeak
+ _objc_loadWeakRetained
+ _objc_release_x1
+ _objc_retainAutoreleaseReturnValue
+ _os_activity_scope_enter
+ _os_activity_scope_leave
- +[NFPrivateService isResultSuccessful:]
- +[NFPrivateServiceInterface interface]
- -[NFPrivateService .cxx_destruct]
- -[NFPrivateService canRun]
- -[NFPrivateService connectToService:]
- -[NFPrivateService dealloc]
- -[NFPrivateService disconnect]
- -[NFPrivateService runService:]
- -[NFPrivateService runService:withCompletion:]
- -[NFPrivateService serviceName]
- -[NFPrivateService serviceNotificationReceived:]
- -[NFRadioPowerSwitch canRun]
- -[NFRadioPowerSwitch requestUserSettingsNotificationWithCompletion:popupInterval:]
- -[NFRadioPowerSwitch serviceName]
- -[NFRestoreService canRun]
- -[NFRestoreService serviceName]
- -[NFStorageService canRun]
- -[NFStorageService deleteAllAppletEntities]
- -[NFStorageService deleteAllESEExpressEntities]
- -[NFStorageService fetchAppletEntitiesWithError:]
- -[NFStorageService fetchESEExpressEntitiesWithError:]
- -[NFStorageService serviceName]
- -[NFStorageService updateAppletEntitiesWithConfig:]
- -[NFStorageService updateESEExpressEntitiesWithConfig:]
- -[NFTagProcessorService canRun]
- -[NFTagProcessorService processURL:forNDEFTag:completionHandler:]
- -[NFTagProcessorService serviceName]
- -[NFUIService .cxx_destruct]
- -[NFUIService canRun]
- -[NFUIService coreNFCUIActivateWithCompletion:]
- -[NFUIService coreNFCUIInvalidate]
- -[NFUIService coreNFCUISetInvalidationHandler:]
- -[NFUIService coreNFCUISetMode:]
- -[NFUIService coreNFCUISetScanText:]
- -[NFUIService coreNFCUITagScannedCount:]
- -[NFUIService debugContext]
- -[NFUIService launchBundleWithIdentifier:launchReason:launchDomain:]
- -[NFUIService serviceName]
- -[NFUIService serviceNotificationReceived:error:]
- -[NFUIService setDebugContext:]
- <redacted>
- GCC_except_table2
- GCC_except_table4
- _NFResultCodeString
- _OBJC_CLASS_$_NFPrivateServiceInterface
- _OBJC_CLASS_$_NFTagProcessorService
- _OBJC_IVAR_$_NFPrivateService._xpcConnection
- _OBJC_IVAR_$_NFUIService._debugContext
- _OBJC_IVAR_$_NFUIService._uiInvalidationHandler
- _OBJC_METACLASS_$_NFPrivateServiceInterface
- _OBJC_METACLASS_$_NFTagProcessorService
- __OBJC_$_CLASS_METHODS_NFPrivateService
- __OBJC_$_CLASS_METHODS_NFPrivateServiceInterface
- __OBJC_$_INSTANCE_METHODS_NFPrivateService
- __OBJC_$_INSTANCE_METHODS_NFRadioPowerSwitch
- __OBJC_$_INSTANCE_METHODS_NFRestoreService
- __OBJC_$_INSTANCE_METHODS_NFStorageService
- __OBJC_$_INSTANCE_METHODS_NFTagProcessorService
- __OBJC_$_INSTANCE_METHODS_NFUIService
- __OBJC_$_INSTANCE_VARIABLES_NFPrivateService
- __OBJC_$_INSTANCE_VARIABLES_NFUIService
- __OBJC_$_PROP_LIST_NFUIService
- __OBJC_$_PROP_LIST_NSObject
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NFPrivateServiceFrameworkInterface
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NFPrivateServiceInterface
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject
- __OBJC_$_PROTOCOL_METHOD_TYPES_NFPrivateServiceFrameworkInterface
- __OBJC_$_PROTOCOL_METHOD_TYPES_NFPrivateServiceInterface
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject
- __OBJC_$_PROTOCOL_REFS_NFPrivateServiceFrameworkInterface
- __OBJC_$_PROTOCOL_REFS_NFPrivateServiceInterface
- __OBJC_CLASS_RO_$_NFPrivateService
- __OBJC_CLASS_RO_$_NFPrivateServiceInterface
- __OBJC_CLASS_RO_$_NFRadioPowerSwitch
- __OBJC_CLASS_RO_$_NFRestoreService
- __OBJC_CLASS_RO_$_NFStorageService
- __OBJC_CLASS_RO_$_NFTagProcessorService
- __OBJC_CLASS_RO_$_NFUIService
- __OBJC_LABEL_PROTOCOL_$_NFPrivateServiceFrameworkInterface
- __OBJC_LABEL_PROTOCOL_$_NFPrivateServiceInterface
- __OBJC_LABEL_PROTOCOL_$_NSObject
- __OBJC_METACLASS_RO_$_NFPrivateService
- __OBJC_METACLASS_RO_$_NFPrivateServiceInterface
- __OBJC_METACLASS_RO_$_NFRadioPowerSwitch
- __OBJC_METACLASS_RO_$_NFRestoreService
- __OBJC_METACLASS_RO_$_NFStorageService
- __OBJC_METACLASS_RO_$_NFTagProcessorService
- __OBJC_METACLASS_RO_$_NFUIService
- __OBJC_PROTOCOL_$_NFPrivateServiceFrameworkInterface
- __OBJC_PROTOCOL_$_NFPrivateServiceInterface
- __OBJC_PROTOCOL_$_NSObject
- __OBJC_PROTOCOL_REFERENCE_$_NFPrivateServiceFrameworkInterface
- __OBJC_PROTOCOL_REFERENCE_$_NFPrivateServiceInterface
- __Unwind_Resume
- ___31-[NFPrivateService runService:]_block_invoke
- ___31-[NFPrivateService runService:]_block_invoke.65
- ___46-[NFPrivateService runService:withCompletion:]_block_invoke
- ___46-[NFPrivateService runService:withCompletion:]_block_invoke.68
- ___47-[NFUIService coreNFCUIActivateWithCompletion:]_block_invoke
- ___65-[NFTagProcessorService processURL:forNDEFTag:completionHandler:]_block_invoke
- ___68-[NFUIService launchBundleWithIdentifier:launchReason:launchDomain:]_block_invoke
- ___82-[NFRadioPowerSwitch requestUserSettingsNotificationWithCompletion:popupInterval:]_block_invoke
- ___Block_byref_object_copy_
- ___Block_byref_object_dispose_
- ___block_descriptor_40_e8_32bs_e22_v16?0"NSDictionary"8ls32l8
- ___block_descriptor_40_e8_32bs_e34_v24?0"NSDictionary"8"NSError"16ls32l8
- ___block_descriptor_48_e8_32r40r_e34_v24?0"NSDictionary"8"NSError"16lr32l8r40l8
- ___block_descriptor_56_e8_32s40bs_e17_v16?0"NSError"8ls32l8s40l8
- ___block_descriptor_56_e8_32s40r_e17_v16?0"NSError"8ls32l8r40l8
- ___block_descriptor_56_e8_32s_e22_v16?0"NSDictionary"8ls32l8
- ___objc_personality_v0
- _kNFUIServiceCoreNFC_UserCancel
- _objc_msgSend$_setQueue:
- _objc_msgSend$absoluteString
- _objc_msgSend$boolValue
- _objc_msgSend$canRun
- _objc_msgSend$code
- _objc_msgSend$connectToService:
- _objc_msgSend$count
- _objc_msgSend$countByEnumeratingWithState:objects:count:
- _objc_msgSend$dictionaryWithDictionary:
- _objc_msgSend$dictionaryWithObjects:forKeys:count:
- _objc_msgSend$disconnect
- _objc_msgSend$errorWithDomain:code:userInfo:
- _objc_msgSend$initWithDomain:code:userInfo:
- _objc_msgSend$initWithFormat:
- _objc_msgSend$initWithServiceName:
- _objc_msgSend$integerValue
- _objc_msgSend$interface
- _objc_msgSend$interfaceWithProtocol:
- _objc_msgSend$invalidate
- _objc_msgSend$isEqualToString:
- _objc_msgSend$isResultSuccessful:
- _objc_msgSend$numberWithDouble:
- _objc_msgSend$numberWithInteger:
- _objc_msgSend$numberWithUnsignedInteger:
- _objc_msgSend$objectForKey:
- _objc_msgSend$objectForKeyedSubscript:
- _objc_msgSend$remoteObjectProxyWithErrorHandler:
- _objc_msgSend$resume
- _objc_msgSend$runService:callback:
- _objc_msgSend$serviceName
- _objc_msgSend$setExportedInterface:
- _objc_msgSend$setExportedObject:
- _objc_msgSend$setRemoteObjectInterface:
- _objc_msgSend$stringWithUTF8String:
- _objc_msgSend$synchronousRemoteObjectProxyWithErrorHandler:
- _objc_msgSend$valueForKey:
- _objc_retain_x23
- _objc_retain_x4
CStrings:
+ "%c[%{public}s %{public}s]:%i "
+ "%c[%{public}s %{public}s]:%i %{public}@ invalidated"
+ "%c[%{public}s %{public}s]:%i BSService endpoint error"
+ "%c[%{public}s %{public}s]:%i BSServiceConnection=%@"
+ "%c[%{public}s %{public}s]:%i BSServiceConnectionEndpoint=%@"
+ "%c[%{public}s %{public}s]:%i Reactivate connection"
+ "%c[%{public}s %{public}s]:%i Remote proxy unavailable"
+ "%c[%{public}s %{public}s]:%i Remote scene service %{public}s"
+ "%c[%{public}s %{public}s]:%i processNDEF error=%@"
+ "@\"BSServiceConnection<BSServiceConnectionClient>\""
+ "@\"NSObject<OS_dispatch_queue>\""
+ "B"
+ "BSMutableServiceInterface"
+ "BSObjCProtocol"
+ "BSServiceConnection"
+ "BSServiceConnectionEndpoint"
+ "BSServiceQuality"
+ "BackgroundTagReading"
+ "BackgroundTagReadingClient activate"
+ "BackgroundTagReadingClient invalidate"
+ "CRS error caused by demo mode"
+ "Cache missed"
+ "Command Error"
+ "CoreNFCShowPaymentSessionGotoSettingsPrompt"
+ "NFBSClient_BackgroundTagReading"
+ "NFBSService_BackgroundTagReadingXPC"
+ "NFBSService_BackgroundTagReadingXPCProtocol"
+ "NFCPaymentTagReaderSession start request"
+ "RBSDomainAttribute"
+ "T@\"BSServiceConnection<BSServiceConnectionClient>\",&,N,V_connection"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_workQueue"
+ "TB,N,V_invalidated"
+ "Unavailable - System Will Sleep"
+ "_activate"
+ "_connection"
+ "_init"
+ "_invalidateFromRemote:"
+ "_invalidated"
+ "_workQueue"
+ "activate"
+ "arrayWithObjects:count:"
+ "attributeWithDomain:name:"
+ "available"
+ "com.apple.NFCUISceneService"
+ "com.apple.NFCUISceneService.remote-ui"
+ "com.apple.nfc.background.tag.reading"
+ "com.apple.nfc.background.tag.reading_XPC"
+ "configureConnection:"
+ "connection"
+ "connectionWithEndpoint:"
+ "copy"
+ "coreNFCShowPaymentSessionGoToSettingsPrompt:"
+ "endpointForMachName:service:instance:"
+ "init"
+ "interfaceWithIdentifier:"
+ "invalidated"
+ "processNDEF:tag:reply:"
+ "protocolForProtocol:"
+ "remoteTarget"
+ "remoteTargetWithLaunchingAssertionAttributes:"
+ "sceneServiceAvailable"
+ "sceneServiceBackgroundTagReadingWithNDEF:tag:completion:"
+ "setConnection:"
+ "setInterface:"
+ "setInvalidated:"
+ "setInvalidationHandler:"
+ "setServer:"
+ "setServiceQuality:"
+ "setTargetQueue:"
+ "setWorkQueue:"
+ "sharedClient"
+ "softlink:o:path:/System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard"
+ "softlink:o:path:/System/Library/PrivateFrameworks/BoardServices.framework/BoardServices"
+ "softlink:o:path:/System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices"
+ "unavailable"
+ "userInitiated"
+ "v16@?0@\"<BSServiceConnectionConfiguring>\"8"
+ "v16@?0@\"BSServiceConnection<BSServiceConnectionContext>\"8"
+ "v20@0:8B16"
+ "v40@0:8@\"NSData\"16@\"NSData\"24@?<v@?@\"NSError\">32"
+ "v8@?0"
+ "workQueue"
- "Actionable"
- "Commmand Error"
- "NFTagProcessorService"
- "TAG"
- "URL"
- "absoluteString"
- "com.apple.stockholm.services.NFTagProcessorService"
- "objectForKeyedSubscript:"
- "processURL:forNDEFTag:completionHandler:"

```
