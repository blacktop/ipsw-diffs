## MXUIServiceClient

> `/System/Library/PrivateFrameworks/MXUIServiceClient.framework/MXUIServiceClient`

```diff

-330.6.1.0.0
-  __TEXT.__text: 0x2558
-  __TEXT.__auth_stubs: 0x190
-  __TEXT.__objc_methlist: 0x2e4
-  __TEXT.__const: 0x60
-  __TEXT.__cstring: 0x485
-  __TEXT.__oslogstring: 0x1bd
-  __TEXT.__unwind_info: 0xf0
-  __TEXT.__objc_classname: 0xba
-  __TEXT.__objc_methname: 0x7bb
-  __TEXT.__objc_methtype: 0x3a8
-  __TEXT.__objc_stubs: 0x5c0
-  __DATA_CONST.__got: 0x80
-  __DATA_CONST.__const: 0x158
+360.58.1.0.0
+  __TEXT.__text: 0x1e58
+  __TEXT.__objc_methlist: 0x2dc
+  __TEXT.__const: 0x68
+  __TEXT.__gcc_except_tab: 0x24
+  __TEXT.__cstring: 0x450
+  __TEXT.__oslogstring: 0x1f9
+  __TEXT.__unwind_info: 0x100
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x190
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x278
+  __DATA_CONST.__objc_selrefs: 0x2c8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x18
-  __AUTH_CONST.__auth_got: 0xd0
+  __DATA_CONST.__got: 0x90
   __AUTH_CONST.__const: 0xa0
-  __AUTH_CONST.__cfstring: 0x200
-  __AUTH_CONST.__objc_const: 0x8b8
+  __AUTH_CONST.__cfstring: 0x240
+  __AUTH_CONST.__objc_const: 0x840
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0x20
   __DATA.__data: 0x180
   __DATA.__common: 0x40

   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B279627E-5C56-3F0A-BCF1-64ACFA3578A1
-  Functions: 74
-  Symbols:   329
-  CStrings:  196
+  UUID: 7671BB0E-F328-3691-8D1D-5FC07C1822AD
+  Functions: 59
+  Symbols:   319
+  CStrings:  59
 
Symbols:
+ +[MXUIService_ServerDelegate translateActionToResponse:]
+ -[MXUIService_Client _lockedRemoteTarget]
+ -[MXUIService_Client _promptForBannerWithType:primaryText:withIconType:callbackHandler:]
+ -[MXUIService_Client newBasicBannerParameters:connectionType:bannerType:]
+ -[MXUIService_Client promptForAudioMovedBanner:]
+ -[MXUIService_Client promptForBasicBanner:callbackHandler:]
+ -[MXUIService_ServerDelegate showBannerBasedOnConfiguration:completionHandler:]
+ GCC_except_table10
+ _MXUIService_CommonUIParam_BannerType
+ _MXUIService_CommonUIParam_ConnectionType
+ _MXUIService_CommonUIParam_HeadsetString
+ _MXUIService_CommonUIParam_RouteToCar
+ _MXUIService_CommonUIParam_SourceAppName
+ _MXUIService_CommonUIParam_UUID
+ _MXUIService_CommonUIResponse_BannerTimeout
+ _MXUIService_CommonUIResponse_ButtonPressed
+ _NSOSStatusErrorDomain
+ _OBJC_CLASS_$_NSError
+ __Block_object_assign
+ __Block_object_dispose
+ __OBJC_$_CLASS_METHODS_MXUIService_ServerDelegate
+ __Unwind_Resume
+ ___51-[MXUIService_Client recreateConnectionIfNecessary]_block_invoke.82
+ ___51-[MXUIService_Client recreateConnectionIfNecessary]_block_invoke.83
+ ___59-[MXUIService_Client promptForBasicBanner:callbackHandler:]_block_invoke
+ ___79-[MXUIService_ServerDelegate showBannerBasedOnConfiguration:completionHandler:]_block_invoke
+ ___Block_byref_object_copy_
+ ___Block_byref_object_dispose_
+ ___block_descriptor_48_e8_32b40r_e20_v20?0i8"NSError"12lr40l8s32l8
+ ___block_literal_global.61
+ ___block_literal_global.81
+ ___objc_personality_v0
+ _objc_autorelease
+ _objc_msgSend$_lockedRemoteTarget
+ _objc_msgSend$_promptForBannerWithType:primaryText:withIconType:callbackHandler:
+ _objc_msgSend$errorWithDomain:code:userInfo:
+ _objc_msgSend$initWithUUIDString:
+ _objc_msgSend$intValue
+ _objc_msgSend$newBasicBannerParameters:connectionType:bannerType:
+ _objc_msgSend$promptForBasicBanner:callbackHandler:
+ _objc_msgSend$showAudioMovedBanner:completionHandler:
+ _objc_msgSend$showBannerBasedOnConfiguration:completionHandler:
+ _objc_msgSend$translateActionToResponse:
- -[MXUIService_Client copyCarPlayVideoBannerParameters:routeToCar:]
- -[MXUIService_ServerDelegate showCarPlayVideoBanner:completionHandler:]
- -[MXUIService_ServerDelegate showConnectButton:completionHandler:]
- -[MXUIService_ServerDelegate showDisconnectedButton:completionHandler:]
- -[MXUIService_ServerDelegate showUndoButton:completionHandler:]
- _MXUIService_CommonButtonParam_ConnectionType
- _MXUIService_CommonButtonParam_HeadsetString
- _MXUIService_CommonButtonParam_RouteToCar
- _MXUIService_CommonButtonParam_UUID
- _MXUIService_CommonButtonResponse_BannerTimeout
- _MXUIService_CommonButtonResponse_ButtonPressed
- _OUTLINED_FUNCTION_12
- _OUTLINED_FUNCTION_13
- _OUTLINED_FUNCTION_14
- _OUTLINED_FUNCTION_15
- _OUTLINED_FUNCTION_16
- _OUTLINED_FUNCTION_17
- _OUTLINED_FUNCTION_18
- _OUTLINED_FUNCTION_19
- _OUTLINED_FUNCTION_20
- _OUTLINED_FUNCTION_21
- _OUTLINED_FUNCTION_22
- _OUTLINED_FUNCTION_23
- _OUTLINED_FUNCTION_24
- ___51-[MXUIService_Client recreateConnectionIfNecessary]_block_invoke.85
- ___51-[MXUIService_Client recreateConnectionIfNecessary]_block_invoke.86
- ___63-[MXUIService_ServerDelegate showUndoButton:completionHandler:]_block_invoke
- ___66-[MXUIService_ServerDelegate showConnectButton:completionHandler:]_block_invoke
- ___71-[MXUIService_Client promptForUndoBanner:withIconType:callbackHandler:]_block_invoke
- ___71-[MXUIService_ServerDelegate showCarPlayVideoBanner:completionHandler:]_block_invoke
- ___71-[MXUIService_ServerDelegate showDisconnectedButton:completionHandler:]_block_invoke
- ___74-[MXUIService_Client promptForConnectDialog:withIconType:callbackHandler:]_block_invoke
- ___77-[MXUIService_Client promptForCarPlayVideoBanner:routeToCar:callbackHandler:]_block_invoke
- ___79-[MXUIService_Client promptForDisconnectedBanner:withIconType:callbackHandler:]_block_invoke
- ___block_literal_global.64
- ___block_literal_global.84
- _objc_msgSend$copyCarPlayVideoBannerParameters:routeToCar:
- _objc_release_x20
CStrings:
+ "-MXUIServiceClient- %s: Audio Moved Banner UUID: %{public}@"
+ "-[MXUIService_Client _promptForBannerWithType:primaryText:withIconType:callbackHandler:]"
+ "-[MXUIService_Client promptForAudioMovedBanner:]"
+ "-[MXUIService_Client promptForCarPlayVideoBanner:routeToCar:callbackHandler:]"
+ "BannerType"
+ "SourceAppName"
- "#16@0:8"
- "-[MXUIService_Client copyCarPlayVideoBannerParameters:routeToCar:]"
- "-[MXUIService_Client promptForConnectDialog:withIconType:callbackHandler:]"
- "-[MXUIService_Client promptForDisconnectedBanner:withIconType:callbackHandler:]"
- "-[MXUIService_Client promptForUndoBanner:withIconType:callbackHandler:]"
- "@\"<MXUIServiceDelegateProtocol>\""
- "@\"BSServiceConnection<BSServiceConnectionClient>\""
- "@\"BSServiceConnectionEndpoint\""
- "@\"BSServiceConnectionListener\""
- "@\"MXUIService_ServerDelegate\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSString\"16@0:8"
- "@16@0:8"
- "@20@0:8i16"
- "@24@0:8:16"
- "@24@0:8@16"
- "@28@0:8@16B24"
- "@32@0:8:16@24"
- "@36@0:8@16B24@?28"
- "@36@0:8@16i24@?28"
- "@40@0:8:16@24@32"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B32@0:8@16@24"
- "BSServiceConnectionListenerDelegate"
- "MXUIService_Banner_ClientProtocol"
- "MXUIService_Banner_ServerProtocol"
- "MXUIService_Client"
- "MXUIService_ServerDelegate"
- "MXUIService_ServerListener"
- "NSObject"
- "Q16@0:8"
- "T#,R"
- "T@\"BSServiceConnectionListener\",&,V_listener"
- "T@\"MXUIService_ServerDelegate\",&,V_delegate"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "TQ,R"
- "UUIDString"
- "Vv16@0:8"
- "Vv32@0:8@\"NSDictionary\"16@?<v@?@\"NSDictionary\"@\"NSError\">24"
- "Vv32@0:8@\"NSString\"16@\"NSString\"24"
- "Vv32@0:8@\"NSUUID\"16@\"NSNumber\"24"
- "Vv32@0:8@16@24"
- "Vv32@0:8@16@?24"
- "Vv40@0:8@\"NSString\"16@\"NSNumber\"24@?<v@?@\"NSDictionary\"@\"NSError\">32"
- "Vv40@0:8@16@24@?32"
- "^{_NSZone=}16@0:8"
- "_connection"
- "_delegate"
- "_endpoint"
- "_listener"
- "_lock"
- "_queue"
- "_shouldCreateConnection"
- "_uiDelegate"
- "activate"
- "arrayWithObjects:count:"
- "attributeWithDomain:name:"
- "autorelease"
- "boolValue"
- "class"
- "configureConnection:"
- "conformsToProtocol:"
- "connectionWithEndpoint:"
- "copy"
- "copyCarPlayVideoBannerParameters:routeToCar:"
- "dealloc"
- "debugDescription"
- "delegate"
- "description"
- "dismissBannerWithUUID:withResponse:"
- "endpointForMachName:service:instance:"
- "hash"
- "init"
- "init:"
- "interfaceWithIdentifier:"
- "invalidate"
- "isEqual:"
- "isEqualToString:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "listener"
- "listener:didReceiveConnection:withContext:"
- "listenerWithConfigurator:"
- "numberWithBool:"
- "numberWithInt:"
- "numberWithUnsignedChar:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "promptForCarPlayVideoBanner:routeToCar:callbackHandler:"
- "promptForConnectDialog:withIconType:callbackHandler:"
- "promptForDisconnectedBanner:withIconType:callbackHandler:"
- "promptForUndoBanner:withIconType:callbackHandler:"
- "protocolForProtocol:"
- "recreateConnectionIfNecessary"
- "release"
- "remoteTargetWithLaunchingAssertionAttributes:"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "self"
- "setActivationHandler:"
- "setClient:"
- "setClientMessagingExpectation:"
- "setDelegate:"
- "setDomain:"
- "setInterface:"
- "setInterfaceTarget:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setListener:"
- "setServer:"
- "setService:"
- "setServiceQuality:"
- "setTargetQueue:"
- "setValue:forKey:"
- "sharedInstance"
- "showCarPlayVideoBanner:completionHandler:"
- "showConnectButton:completionHandler:"
- "showDisconnectedButton:completionHandler:"
- "showInputDeviceReplacementPillForConnectedDevice:replacedDevice:"
- "showUndoButton:completionHandler:"
- "stringWithFormat:"
- "superclass"
- "updateSTBackgroundActivitiesStatusPill:showOrRemove:callbackHandler:"
- "updateSTBackgroundActivitiesStatusPill:showOrRemove:completionHandler:"
- "userActionToString:"
- "userInitiated"
- "v16@0:8"
- "v24@0:8@16"
- "v32@0:8@16@24"
- "v36@0:8@16C24@?28"
- "v40@0:8@\"BSServiceConnectionListener\"16@\"BSServiceConnection<BSServiceConnectionHost>\"24@\"<BSXPCDecoding>\"32"
- "v40@0:8@16@24@32"
- "valueForKey:"
- "zone"
- "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"

```
