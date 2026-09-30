## CoreAccessories

> `/System/Library/PrivateFrameworks/CoreAccessories.framework/CoreAccessories`

```diff

-1139.40.6.0.0
-  __TEXT.__text: 0x2a758
-  __TEXT.__auth_stubs: 0x710
-  __TEXT.__objc_methlist: 0x187c
+1139.60.9.0.0
+  __TEXT.__text: 0x2a274
+  __TEXT.__auth_stubs: 0x720
+  __TEXT.__objc_methlist: 0x18c4
   __TEXT.__const: 0x150
-  __TEXT.__cstring: 0x3b89
-  __TEXT.__oslogstring: 0x422d
-  __TEXT.__gcc_except_tab: 0xe94
+  __TEXT.__cstring: 0x3ba8
+  __TEXT.__oslogstring: 0x40cd
+  __TEXT.__gcc_except_tab: 0xe24
   __TEXT.__ustring: 0xa
-  __TEXT.__unwind_info: 0x928
+  __TEXT.__unwind_info: 0x960
   __TEXT.__objc_classname: 0x25a
-  __TEXT.__objc_methname: 0x474e
-  __TEXT.__objc_methtype: 0x1609
-  __TEXT.__objc_stubs: 0x2de0
+  __TEXT.__objc_methname: 0x485c
+  __TEXT.__objc_methtype: 0x15e0
+  __TEXT.__objc_stubs: 0x2ec0
   __DATA_CONST.__got: 0x148
-  __DATA_CONST.__const: 0x1e78
+  __DATA_CONST.__const: 0x1ec8
   __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xec0
+  __DATA_CONST.__objc_selrefs: 0xf00
   __DATA_CONST.__objc_protorefs: 0x50
   __DATA_CONST.__objc_superrefs: 0x48
   __DATA_CONST.__objc_arraydata: 0xd8
-  __AUTH_CONST.__auth_got: 0x398
-  __AUTH_CONST.__const: 0xae0
+  __AUTH_CONST.__auth_got: 0x3a0
+  __AUTH_CONST.__const: 0xa20
   __AUTH_CONST.__cfstring: 0x39a0
-  __AUTH_CONST.__objc_const: 0x22e8
+  __AUTH_CONST.__objc_const: 0x2318
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_ivar: 0xd8
+  __DATA.__objc_ivar: 0xdc
   __DATA.__data: 0x758
   __DATA.__bss: 0xd8
   __DATA_DIRTY.__objc_data: 0x320

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2FD06EFE-98CF-3F15-B36B-25AF45D4F801
-  Functions: 765
-  Symbols:   4067
-  CStrings:  2093
+  UUID: 4C11B896-E97B-35F8-869A-F4F2D6939DE6
+  Functions: 771
+  Symbols:   4046
+  CStrings:  2100
 
Symbols:
+ -[ACCExternalAccessoryProvider _handleConnectionInterruption]
+ -[ACCExternalAccessoryProvider _handleConnectionInvalidation]
+ -[ACCExternalAccessoryProvider _safeRemoteObject]
+ -[ACCExternalAccessoryProvider _safeSynchronousRemoteObject]
+ -[ACCExternalAccessoryProvider connectionQueue]
+ -[ACCExternalAccessoryProvider isClientRegistered]
+ -[ACCExternalAccessoryProvider setConnectionQueue:]
+ -[ACCExternalAccessoryProvider setIsClientRegistered:]
+ GCC_except_table42
+ GCC_except_table51
+ _OBJC_IVAR_$_ACCExternalAccessoryProvider._connectionQueue
+ _OBJC_IVAR_$_ACCExternalAccessoryProvider._isClientRegistered
+ ___48-[ACCExternalAccessoryProvider connectToServer:]_block_invoke.215
+ ___48-[ACCExternalAccessoryProvider connectToServer:]_block_invoke.215.cold.1
+ ___48-[ACCExternalAccessoryProvider connectToServer:]_block_invoke.215.cold.2
+ ___48-[ACCExternalAccessoryProvider connectToServer:]_block_invoke.217
+ ___48-[ACCExternalAccessoryProvider connectToServer:]_block_invoke.217.cold.1
+ ___48-[ACCExternalAccessoryProvider connectToServer:]_block_invoke_2
+ ___49-[ACCExternalAccessoryProvider _safeRemoteObject]_block_invoke
+ ___49-[ACCExternalAccessoryProvider _safeRemoteObject]_block_invoke_2
+ ___49-[ACCExternalAccessoryProvider _safeRemoteObject]_block_invoke_2.cold.1
+ ___49-[ACCExternalAccessoryProvider _safeRemoteObject]_block_invoke_2.cold.2
+ ___57-[ACCExternalAccessoryProvider ExternalAccessoryArrived:]_block_invoke.cold.3
+ ___60-[ACCExternalAccessoryProvider _safeSynchronousRemoteObject]_block_invoke
+ ___60-[ACCExternalAccessoryProvider _safeSynchronousRemoteObject]_block_invoke_2
+ ___60-[ACCExternalAccessoryProvider _safeSynchronousRemoteObject]_block_invoke_2.cold.1
+ ___60-[ACCExternalAccessoryProvider _safeSynchronousRemoteObject]_block_invoke_2.cold.2
+ ___61-[ACCExternalAccessoryProvider _handleConnectionInterruption]_block_invoke
+ ___61-[ACCExternalAccessoryProvider _handleConnectionInterruption]_block_invoke.cold.1
+ ___61-[ACCExternalAccessoryProvider _handleConnectionInvalidation]_block_invoke
+ ___61-[ACCExternalAccessoryProvider _handleConnectionInvalidation]_block_invoke.cold.1
+ ___block_descriptor_41_e8_32s_e5_v8?0ls32l8
+ ___block_descriptor_48_e8_32s40r_e5_v8?0lr40l8s32l8
+ _dispatch_queue_attr_make_with_autorelease_frequency
+ _objc_msgSend$_handleConnectionInterruption
+ _objc_msgSend$_handleConnectionInvalidation
+ _objc_msgSend$_safeRemoteObject
+ _objc_msgSend$_safeSynchronousRemoteObject
+ _objc_msgSend$connectionQueue
+ _objc_msgSend$isClientRegistered
+ _objc_msgSend$setIsClientRegistered:
- -[ACCExternalAccessoryProvider connectToServer:].cold.1
- -[ACCExternalAccessoryProvider connectToServer:].cold.2
- -[ACCExternalAccessoryProvider connectToServer:].cold.3
- -[ACCExternalAccessoryProvider connectToServer:].cold.4
- -[ACCExternalAccessoryProvider remoteObject]
- -[ACCExternalAccessoryProvider sendGPRMCDataStatus:ValueV:ValueX:forAccessoryUUID:].cold.2
- -[ACCExternalAccessoryProvider sendNMEAFilterList:forAccessoryUUID:].cold.2
- -[ACCExternalAccessoryProvider setRemoteObject:]
- -[ACCExternalAccessoryProvider startLocationInformationForAccessoryUUID:].cold.2
- -[ACCExternalAccessoryProvider stopLocationInformationForAccessoryUUID:].cold.2
- GCC_except_table41
- GCC_except_table89
- _OBJC_IVAR_$_ACCExternalAccessoryProvider._remoteObject
- ___107-[ACCExternalAccessoryProvider createExternalAccessorySessionForProtocol:accessoryUUID:withEASessionReply:]_block_invoke.240
- ___107-[ACCExternalAccessoryProvider createExternalAccessorySessionForProtocol:accessoryUUID:withEASessionReply:]_block_invoke.240.cold.1
- ___107-[ACCExternalAccessoryProvider createExternalAccessorySessionForProtocol:accessoryUUID:withEASessionReply:]_block_invoke.cold.2
- ___48-[ACCExternalAccessoryProvider connectToServer:]_block_invoke.213.cold.1
- ___48-[ACCExternalAccessoryProvider connectToServer:]_block_invoke.214
- ___48-[ACCExternalAccessoryProvider connectToServer:]_block_invoke.214.cold.1
- ___48-[ACCExternalAccessoryProvider connectToServer:]_block_invoke.214.cold.2
- ___48-[ACCExternalAccessoryProvider connectToServer:]_block_invoke.216
- ___48-[ACCExternalAccessoryProvider connectToServer:]_block_invoke.216.cold.1
- ___48-[ACCExternalAccessoryProvider connectToServer:]_block_invoke.216.cold.2
- ___48-[ACCExternalAccessoryProvider connectToServer:]_block_invoke.219
- ___48-[ACCExternalAccessoryProvider connectToServer:]_block_invoke.219.cold.1
- ___51-[ACCExternalAccessoryProvider currentVehicleInfo:]_block_invoke.259
- ___51-[ACCExternalAccessoryProvider currentVehicleInfo:]_block_invoke.259.cold.1
- ___51-[ACCExternalAccessoryProvider currentVehicleInfo:]_block_invoke.cold.2
- ___57-[ACCExternalAccessoryProvider ExternalAccessoryArrived:]_block_invoke.234.cold.2
- ___57-[ACCExternalAccessoryProvider ExternalAccessoryArrived:]_block_invoke.234.cold.3
- ___57-[ACCExternalAccessoryProvider ExternalAccessoryArrived:]_block_invoke.235
- ___57-[ACCExternalAccessoryProvider ExternalAccessoryArrived:]_block_invoke.235.cold.1
- ___60-[ACCExternalAccessoryProvider openSocketForAccessoryToApp:]_block_invoke
- ___60-[ACCExternalAccessoryProvider openSocketForAccessoryToApp:]_block_invoke.cold.1
- ___60-[ACCExternalAccessoryProvider openSocketForAccessoryToApp:]_block_invoke.cold.2
- ___60-[ACCExternalAccessoryProvider openSocketForAppToAccessory:]_block_invoke
- ___60-[ACCExternalAccessoryProvider openSocketForAppToAccessory:]_block_invoke.cold.1
- ___60-[ACCExternalAccessoryProvider openSocketForAppToAccessory:]_block_invoke.cold.2
- ___62-[ACCExternalAccessoryProvider closeExternalAccessorySession:]_block_invoke
- ___62-[ACCExternalAccessoryProvider closeExternalAccessorySession:]_block_invoke.cold.1
- ___62-[ACCExternalAccessoryProvider closeExternalAccessorySession:]_block_invoke.cold.2
- ___99-[ACCExternalAccessoryProvider sendOutgoingExternalAccessoryData:forEASessionIdentifier:withReply:]_block_invoke.250
- ___99-[ACCExternalAccessoryProvider sendOutgoingExternalAccessoryData:forEASessionIdentifier:withReply:]_block_invoke.250.cold.1
- ___99-[ACCExternalAccessoryProvider sendOutgoingExternalAccessoryData:forEASessionIdentifier:withReply:]_block_invoke.cold.2
- ___block_literal_global.218
- ___block_literal_global.243
- ___block_literal_global.245
- ___block_literal_global.247
- ___block_literal_global.249
CStrings:
+ "B"
+ "T@\"NSDictionary\",&,V_eaClientRegistrationInfo"
+ "T@\"NSMutableSet\",&,V_currentlyConnectedAccessories"
+ "T@\"NSObject<OS_dispatch_queue>\",&,V_connectionQueue"
+ "T@\"NSXPCConnection\",&,V_serverConnection"
+ "TB,V_isClientRegistered"
+ "Ti,V_clientCapabilities"
+ "[#ExternalAccessory] EA XPC connection cleanup completed"
+ "[#ExternalAccessory] Error retrieving remote proxy: %@"
+ "[#ExternalAccessory] Error retrieving synchronous remote proxy: %@"
+ "_connectionQueue"
+ "_handleConnectionInterruption"
+ "_handleConnectionInvalidation"
+ "_isClientRegistered"
+ "_safeRemoteObject"
+ "_safeSynchronousRemoteObject"
+ "com.apple.EAProvider.xpc.queue"
+ "connectionQueue"
+ "isClientRegistered"
+ "setConnectionQueue:"
+ "setIsClientRegistered:"
- "@\"<ACCExternalAccessoryXPCServerProtocol>\""
- "T@\"<ACCExternalAccessoryXPCServerProtocol>\",&,N,V_remoteObject"
- "T@\"NSDictionary\",&,N,V_eaClientRegistrationInfo"
- "T@\"NSMutableSet\",&,N,V_currentlyConnectedAccessories"
- "Ti,N,V_clientCapabilities"
- "[#ExternalAccessory] EA XPC begin invalidation handler!"
- "[#ExternalAccessory] EA XPC connection invalidated!"
- "[#ExternalAccessory] Getting remote object..."
- "[#ExternalAccessory] self.remoteObject = %@"
- "[#Location] No remoteObject to send activateLocationForUUID %@"
- "[#Location] No remoteObject to send sendGPRMCDataStatus: %d ValueV: %d ValueX: %d forUUID: %@"
- "[#Location] No remoteObject to send sendNMEAFilterList %@ for UUID: %@"
- "[#Location] No remoteObject to send stopLocationForUUID %@"
- "[#VehicleInfoStatus] XPC connection error: %@"

```
