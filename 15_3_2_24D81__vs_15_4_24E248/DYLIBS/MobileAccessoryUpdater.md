## MobileAccessoryUpdater

> `/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/Versions/A/MobileAccessoryUpdater`

```diff

-1170.80.6.0.1
-  __TEXT.__text: 0x6b48
-  __TEXT.__auth_stubs: 0x550
-  __TEXT.__objc_methlist: 0x824
-  __TEXT.__const: 0x40
-  __TEXT.__gcc_except_tab: 0xa8
-  __TEXT.__cstring: 0x2049
+1207.100.66.0.0
+  __TEXT.__text: 0x52b4
+  __TEXT.__auth_stubs: 0x4f0
+  __TEXT.__objc_methlist: 0xc7c
+  __TEXT.__const: 0x30
+  __TEXT.__gcc_except_tab: 0x68
+  __TEXT.__cstring: 0x1a8d
   __TEXT.__oslogstring: 0x1a0
-  __TEXT.__unwind_info: 0x2b8
+  __TEXT.__unwind_info: 0x280
   __TEXT.__objc_classname: 0x1b2
-  __TEXT.__objc_methname: 0x1884
-  __TEXT.__objc_methtype: 0x86b
-  __TEXT.__objc_stubs: 0xfa0
-  __DATA_CONST.__got: 0x108
+  __TEXT.__objc_methname: 0x1694
+  __TEXT.__objc_methtype: 0x82f
+  __TEXT.__objc_stubs: 0xb80
+  __DATA_CONST.__got: 0xe8
   __DATA_CONST.__const: 0x98
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6a0
+  __DATA_CONST.__objc_selrefs: 0x6c0
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x48
-  __AUTH_CONST.__auth_got: 0x2b8
-  __AUTH_CONST.__const: 0x380
-  __AUTH_CONST.__cfstring: 0x1780
-  __AUTH_CONST.__objc_const: 0x28e0
+  __AUTH_CONST.__auth_got: 0x288
+  __AUTH_CONST.__const: 0x2c0
+  __AUTH_CONST.__cfstring: 0x1100
+  __AUTH_CONST.__objc_const: 0x20b0
   __AUTH.__objc_data: 0x370
   __DATA.__objc_ivar: 0xf8
   __DATA.__data: 0x4e0

   - /System/Library/Frameworks/Security.framework/Versions/A/Security
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 23B21B06-FD07-3328-9BB3-42E786340D30
-  Functions: 247
-  Symbols:   790
-  CStrings:  900
+  UUID: C12DE15F-D1B0-3340-AF66-937815B12735
+  Functions: 250
+  Symbols:   752
+  CStrings:  778
 
Symbols:
+ -[FudInternalConnection handleInternalMessage:]
+ -[FudInternalConnection initWithClientIdentifier:handlerQueue:messageHandler:].cold.1
+ -[FudInternalConnection initWithClientIdentifier:handlerQueue:messageHandler:].cold.2
+ -[FudPersonalizationObjectInfo initWithTag:].cold.1
+ -[FudPersonalizationObjectInfo initWithTag:].cold.2
+ -[FudPersonalizationRequest initWithName:].cold.1
+ -[FudPersonalizationRequest initWithName:].cold.2
+ -[FudXPCConnection createSession].cold.1
+ -[FudXPCConnection createSession].cold.2
+ -[FudXPCConnection createSession].cold.3
+ -[FudXPCConnection createSession].cold.4
+ -[FudXPCConnection createSession].cold.5
+ -[FudXPCConnection createSession].cold.6
+ -[FudXPCConnection initWithClientName:replyHandlerQueue:messageHandler:].cold.1
+ -[FudXPCConnection registerForBSDNotifications].cold.1
+ -[FudXPCConnection sendMessageToFud:].cold.1
+ -[FudXPCConnection sendMessageToFud:reply:].cold.1
+ -[FudXPCConnection sendMessageToFud:reply:].cold.2
+ -[FudXPCConnection sendMessageToFud:reply:].cold.3
+ -[MobileAccessoryUpdater initWithDelegate:isInternalClient:options:error:].cold.1
+ -[MobileAccessoryUpdater initWithDelegate:isInternalClient:options:error:].cold.2
+ -[MobileAccessoryUpdater initWithDelegate:isInternalClient:options:error:].cold.3
+ -[MobileAccessoryUpdater initWithDelegate:isInternalClient:options:error:].cold.4
+ -[MobileAccessoryUpdater initWithPluginIdentifier:isGroupIdentifier:delegate:isInternalClient:options:error:].cold.1
+ FudLogger.cold.1
+ FudLogv.cold.4
+ FudLogv.cold.5
+ FudLogv.cold.6
+ FudLogv.cold.7
+ _NSStringFromClass
+ ___47-[FudInternalConnection handleInternalMessage:]_block_invoke
- -[FudInternalConnection handleInboundNotification:]
- -[MobileAccessoryUpdater doesOperationCodeRequireFilter:]
- -[MobileAccessoryUpdater getOperationCodeFromName:]
- -[MobileAccessoryUpdater handleAUNotificationEvent:]
- -[MobileAccessoryUpdater handleInboundEvent:]
- -[MobileAccessoryUpdater sendMessageForCommand:withOptions:requiresFilter:]
- -[MobileAccessoryUpdater sendMessageForCommand:withOptions:requiresFilter:replyHandler:]
- GCC_except_table21
- GCC_except_table28
- GCC_except_table8
- _OBJC_CLASS_$_NSNotificationCenter
- __CFXPCCreateXPCObjectFromCFObject
- ___36-[MobileAccessoryUpdater unregister]_block_invoke
- ___40-[MobileAccessoryUpdater getPluginsList]_block_invoke
- ___40-[MobileAccessoryUpdater queryNextStep:]_block_invoke
- ___42-[MobileAccessoryUpdater createConnection]_block_invoke
- ___45-[MobileAccessoryUpdater handleInboundEvent:]_block_invoke
- ___51-[FudInternalConnection handleInboundNotification:]_block_invoke
- ___66-[MobileAccessoryUpdater registerForIdentifier:isGroupIdentifier:]_block_invoke
- ___block_descriptor_48_e8_32o40o_e33_v16?0"NSObject<OS_xpc_object>"8l
- ___block_descriptor_48_e8_32o40r_e33_v16?0"NSObject<OS_xpc_object>"8l
- ___block_descriptor_56_e8_32o40r48r_e33_v16?0"NSObject<OS_xpc_object>"8l
- ___block_descriptor_64_e8_32o40r48r56r_e33_v16?0"NSObject<OS_xpc_object>"8l
- ___copy_helper_block_e8_32o40r
- ___copy_helper_block_e8_32o40r48r
- ___copy_helper_block_e8_32o40r48r56r
- ___destroy_helper_block_e8_32o40r
- ___destroy_helper_block_e8_32o40r48r
- ___destroy_helper_block_e8_32o40r48r56r
- _objc_msgSend$accessoryName
- _objc_msgSend$addObserver:selector:name:object:
- _objc_msgSend$dataWithBytes:length:
- _objc_msgSend$defaultCenter
- _objc_msgSend$deviceClassAttached:
- _objc_msgSend$deviceClassDetached:error:
- _objc_msgSend$dictionaryWithCapacity:
- _objc_msgSend$dictionaryWithObject:forKey:
- _objc_msgSend$doesOperationCodeRequireFilter:
- _objc_msgSend$getActiveDeviceClass
- _objc_msgSend$getActiveDeviceClassCString
- _objc_msgSend$getNextMessageID
- _objc_msgSend$getOperationCodeFromName:
- _objc_msgSend$handleAUNotificationEvent:
- _objc_msgSend$handleInboundEvent:
- _objc_msgSend$initWithClientIdentifier:handlerQueue:messageHandler:
- _objc_msgSend$initWithClientName:replyHandlerQueue:messageHandler:
- _objc_msgSend$numberWithLongLong:
- _objc_msgSend$performStep:withOptions:
- _objc_msgSend$postNotificationName:object:userInfo:
- _objc_msgSend$removeObserver:
- _objc_msgSend$sendMessageForCommand:withOptions:requiresFilter:
- _objc_msgSend$sendMessageForCommand:withOptions:requiresFilter:replyHandler:
- _objc_msgSend$sendMessageToFud:
- _objc_msgSend$sendMessageToFud:reply:
- _objc_msgSend$stepComplete:deviceClass:successful:info:error:
- _objc_msgSend$stepRunning:deviceClass:progress:overallProgress:info:
- _objc_msgSend$stop
- _objc_msgSend$stringWithCString:encoding:
- _objc_msgSend$type
- _objc_msgSend$unarchivedObjectOfClass:fromData:error:
- _objc_msgSend$unregister
- _objc_msgSend$userInfo
- _objc_opt_respondsToSelector
- _xpc_dictionary_get_double
- _xpc_dictionary_get_remote_connection
- _xpc_dictionary_get_string
- _xpc_dictionary_set_bool
- _xpc_retain
CStrings:
+ "%s: No longer supported"
+ "-[MobileAccessoryUpdater activeFilter]"
+ "-[MobileAccessoryUpdater bundleIdentifier]"
+ "-[MobileAccessoryUpdater clientIdentifier]"
+ "-[MobileAccessoryUpdater doneWithOptions:]"
+ "-[MobileAccessoryUpdater getActiveDeviceClassCString]"
+ "-[MobileAccessoryUpdater getActiveDeviceClass]"
+ "-[MobileAccessoryUpdater getPluginsList]"
+ "-[MobileAccessoryUpdater loadPluginWithAccessoryInfo:options:]"
+ "-[MobileAccessoryUpdater performNextStepWithOptions:]"
+ "-[MobileAccessoryUpdater performStep:withOptions:]"
+ "-[MobileAccessoryUpdater queryNextStep:]"
+ "-[MobileAccessoryUpdater registerForIdentifier:isGroupIdentifier:]"
+ "-[MobileAccessoryUpdater setActiveDeviceClass:]"
+ "-[MobileAccessoryUpdater setLastRemoteFindDate:]"
+ "-[MobileAccessoryUpdater unregister]"
+ "Can't convert XPC msg to Dictionary"
+ "Client messaging no longer supported"
+ "Dropping message, no longer handling internal messages"
+ "External client messaging no longer supported"
+ "Internal client messaging no longer supported"
+ "Internal connections no longer support notifications"
+ "Invalid error class %@"
+ "handleInternalMessage:"
- "%s: Unarchiving Failure Error: %@"
- "-[MobileAccessoryUpdater handleAUNotificationEvent:]"
- "B20@0:8i16"
- "B32@0:8i16@20B28"
- "B40@0:8i16@20B28@?32"
- "Can't convert unknown operation string into opcode: %@"
- "Can't handle NULL notification"
- "Can't handle NULL user info in notification"
- "Can't handle reply with NULL handler"
- "Can't perform nil step"
- "Can't perform query operation without valid connection to fud"
- "Can't process NULL event"
- "Can't process message without filter info"
- "Can't query next step without active filter"
- "Can't reply to NULL message"
- "Can't respond without message ID"
- "Can't return operation code for nil string"
- "Can't send NULL message"
- "Can't send NULL msg"
- "Can't send NULL xpc message"
- "Can't send command since filter is not set, command:%@"
- "Can't send message after it was explicitly stopped"
- "Can't send message after unregistering"
- "Can't send message in reply to NULL original message"
- "Can't send message to NULL connection"
- "Can't send reply message without client identifier"
- "Can't set filter name to nil value"
- "Client got an internal notification"
- "Client sent an internal message"
- "Client sent an internal message, expecting reply for msg ID %lld."
- "Complete"
- "FUD replied error %@"
- "Failed to allocate user info dict"
- "Failed to convert dict to xpc dict"
- "Failed to convert xpc dict into cf dict"
- "Failed to convert xpc msg to CF"
- "Failed to create semaphore to wait for unregistration"
- "Failed to get c client identifier"
- "Failed to get message ID"
- "Failed to get operation code for '%@', can't send request now"
- "Failed to get xpc connection from replyTo dict"
- "Failed to register: %@"
- "FilterIdentifier"
- "Fud finished unregistering client: %@"
- "Fud returned error"
- "GroupIdentifier"
- "Handling registration reply..."
- "Info"
- "InternalClient"
- "InternalMessage"
- "Invalid response operation to registration request! %d"
- "LOADING PLUGIN: _bundleIdentifier = %@, _clientIdentifier = %@ "
- "LastRemoteFindDate"
- "MAUInternalMessageClientNotification"
- "MAUInternalMessageFudNotification"
- "MobileAccessoryUpdater %s Received AU Notification Request: %d, %@"
- "NULL reply from getPluginsList request"
- "NULL reply from query request"
- "NULL reply from registration request"
- "NotificationRequest"
- "Options"
- "OverallProgress"
- "Plugin list from FUD = %@"
- "PluginIdentifier"
- "PluginsList"
- "Progress"
- "Received AU Notification Request"
- "Registration response was missing command"
- "Response was missing command"
- "Sending registration message..."
- "Unknown error occured"
- "Unknown operation code '%d'. I have no idea if this needs a filter... saying yes anyways"
- "Waiting for fud to reply to unregistration request"
- "Waiting for response..."
- "Whoaa... framework got an unknown event!"
- "addObserver:selector:name:object:"
- "dataWithBytes:length:"
- "defaultCenter"
- "dictionaryWithCapacity:"
- "dictionaryWithObject:forKey:"
- "doesOperationCodeRequireFilter:"
- "getOperationCodeFromName:"
- "handleAUNotificationEvent:"
- "handleInboundEvent:"
- "handleInboundNotification:"
- "i24@0:8@16"
- "numberWithLongLong:"
- "postNotificationName:object:userInfo:"
- "removeObserver:"
- "sendMessageForCommand:withOptions:requiresFilter:"
- "sendMessageForCommand:withOptions:requiresFilter:replyHandler:"
- "stringWithCString:encoding:"
- "unarchivedObjectOfClass:fromData:error:"
- "userInfo"

```
