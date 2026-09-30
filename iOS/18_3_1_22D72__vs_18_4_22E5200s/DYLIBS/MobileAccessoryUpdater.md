## MobileAccessoryUpdater

> `/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/MobileAccessoryUpdater`

```diff

-1170.80.6.0.1
-  __TEXT.__text: 0x61fc
-  __TEXT.__auth_stubs: 0x590
-  __TEXT.__objc_methlist: 0x824
-  __TEXT.__const: 0x38
-  __TEXT.__gcc_except_tab: 0xa8
-  __TEXT.__cstring: 0x1f4f
+1207.100.54.502.1
+  __TEXT.__text: 0x4b84
+  __TEXT.__auth_stubs: 0x500
+  __TEXT.__objc_methlist: 0xc7c
+  __TEXT.__const: 0x28
+  __TEXT.__gcc_except_tab: 0x68
+  __TEXT.__cstring: 0x1993
   __TEXT.__oslogstring: 0x5d
-  __TEXT.__unwind_info: 0x298
+  __TEXT.__unwind_info: 0x230
   __TEXT.__objc_classname: 0x1b2
-  __TEXT.__objc_methname: 0x1879
-  __TEXT.__objc_methtype: 0x86b
-  __TEXT.__objc_stubs: 0xf60
-  __DATA_CONST.__got: 0x108
-  __DATA_CONST.__const: 0x228
+  __TEXT.__objc_methname: 0x1689
+  __TEXT.__objc_methtype: 0x82f
+  __TEXT.__objc_stubs: 0xb40
+  __DATA_CONST.__got: 0xe8
+  __DATA_CONST.__const: 0x188
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x698
+  __DATA_CONST.__objc_selrefs: 0x6b8
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x48
-  __AUTH_CONST.__auth_got: 0x2d8
+  __AUTH_CONST.__auth_got: 0x290
   __AUTH_CONST.__const: 0x1a0
-  __AUTH_CONST.__cfstring: 0x1720
-  __AUTH_CONST.__objc_const: 0x28e0
+  __AUTH_CONST.__cfstring: 0x10a0
+  __AUTH_CONST.__objc_const: 0x20b0
   __AUTH.__objc_data: 0xf0
   __DATA.__objc_ivar: 0xf8
   __DATA.__data: 0x4e0

   - /System/Library/Frameworks/Security.framework/Security
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 227
-  Symbols:   395
-  CStrings:  695
+  Functions: 236
+  Symbols:   400
+  CStrings:  625
 
Symbols:
+ _NSStringFromClass
- _OBJC_CLASS_$_NSNotificationCenter
- __CFXPCCreateXPCObjectFromCFObject
- _objc_opt_respondsToSelector
- _objc_release_x19
- _objc_retain_x19
- _objc_retain_x8
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
