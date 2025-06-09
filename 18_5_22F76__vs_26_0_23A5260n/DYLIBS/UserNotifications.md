## UserNotifications

> `/System/Library/Frameworks/UserNotifications.framework/UserNotifications`

```diff

-579.6.4.0.0
-  __TEXT.__text: 0x2dbac
+616.0.1.0.0
+  __TEXT.__text: 0x2f978
   __TEXT.__auth_stubs: 0x670
-  __TEXT.__objc_methlist: 0x3378
-  __TEXT.__cstring: 0x320f
-  __TEXT.__const: 0xc8
-  __TEXT.__oslogstring: 0x2023
-  __TEXT.__gcc_except_tab: 0x220
+  __TEXT.__objc_methlist: 0x3680
+  __TEXT.__cstring: 0x336d
+  __TEXT.__const: 0xd0
+  __TEXT.__oslogstring: 0x2092
+  __TEXT.__gcc_except_tab: 0x26c
   __TEXT.__dlopen_cstrs: 0x8a
-  __TEXT.__unwind_info: 0xbf0
-  __TEXT.__objc_classname: 0x8e5
-  __TEXT.__objc_methname: 0x933e
-  __TEXT.__objc_methtype: 0x11e6
-  __TEXT.__objc_stubs: 0x4de0
-  __DATA_CONST.__got: 0x390
-  __DATA_CONST.__const: 0xae0
-  __DATA_CONST.__objc_classlist: 0x180
+  __TEXT.__unwind_info: 0xcd0
+  __TEXT.__objc_classname: 0x99a
+  __TEXT.__objc_methname: 0x9605
+  __TEXT.__objc_methtype: 0x1268
+  __TEXT.__objc_stubs: 0x4fe0
+  __DATA_CONST.__got: 0x3b0
+  __DATA_CONST.__const: 0xaf0
+  __DATA_CONST.__objc_classlist: 0x1a0
   __DATA_CONST.__objc_catlist: 0x68
-  __DATA_CONST.__objc_protolist: 0x98
+  __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1b40
-  __DATA_CONST.__objc_protorefs: 0x28
-  __DATA_CONST.__objc_superrefs: 0x118
+  __DATA_CONST.__objc_selrefs: 0x1bf8
+  __DATA_CONST.__objc_protorefs: 0x38
+  __DATA_CONST.__objc_superrefs: 0x130
   __AUTH_CONST.__auth_got: 0x348
-  __AUTH_CONST.__const: 0x2c0
-  __AUTH_CONST.__cfstring: 0x32a0
-  __AUTH_CONST.__objc_const: 0x9578
+  __AUTH_CONST.__const: 0x360
+  __AUTH_CONST.__cfstring: 0x33c0
+  __AUTH_CONST.__objc_const: 0xa498
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH.__objc_data: 0xa0
-  __DATA.__objc_ivar: 0x314
-  __DATA.__data: 0x728
-  __DATA.__bss: 0x78
-  __DATA_DIRTY.__objc_data: 0xe60
-  __DATA_DIRTY.__bss: 0x68
+  __AUTH.__objc_data: 0x2d0
+  __DATA.__objc_ivar: 0x33c
+  __DATA.__data: 0x848
+  __DATA.__bss: 0x88
+  __DATA_DIRTY.__objc_data: 0xd70
+  __DATA_DIRTY.__bss: 0x98
   __DATA_DIRTY.__common: 0xa0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7A4B2EEC-12F2-35F5-AC22-E0B7742C1FEA
-  Functions: 1254
-  Symbols:   4387
-  CStrings:  2524
+  UUID: D4740582-0518-3F31-8F04-ABED4A996A04
+  Functions: 1330
+  Symbols:   4649
+  CStrings:  2593
 
Symbols:
+ +[UNNotificationIcon iconWithUTI:]
+ +[UNOneTimeCode supportsSecureCoding]
+ +[UNOneTimeCodeClient currentClient]
+ +[UNOneTimeCodeClient currentClient].cold.1
+ +[UNOneTimeCodeService clientInterface]
+ +[UNOneTimeCodeService clientInterface].cold.1
+ +[UNOneTimeCodeService serverInterface]
+ +[UNOneTimeCodeService serverInterface].cold.1
+ +[UNOneTimeCodeServiceConnection sharedInstance]
+ +[UNOneTimeCodeServiceConnection sharedInstance].cold.1
+ -[UNNotificationIcon uti]
+ -[UNOneTimeCode .cxx_destruct]
+ -[UNOneTimeCode _descriptionForRedacted:]
+ -[UNOneTimeCode applicationIdentifier]
+ -[UNOneTimeCode code]
+ -[UNOneTimeCode copyWithZone:]
+ -[UNOneTimeCode description]
+ -[UNOneTimeCode encodeWithCoder:]
+ -[UNOneTimeCode hash]
+ -[UNOneTimeCode initWithCode:applicationIdentifier:notificationIdentifier:timestamp:]
+ -[UNOneTimeCode initWithCoder:]
+ -[UNOneTimeCode isEqual:]
+ -[UNOneTimeCode notificationIdentifier]
+ -[UNOneTimeCode redactedDescription]
+ -[UNOneTimeCode timestamp]
+ -[UNOneTimeCodeClient .cxx_destruct]
+ -[UNOneTimeCodeClient _init]
+ -[UNOneTimeCodeClient addObserver:]
+ -[UNOneTimeCodeClient consumeCode:]
+ -[UNOneTimeCodeClient dealloc]
+ -[UNOneTimeCodeClient init]
+ -[UNOneTimeCodeClient observers]
+ -[UNOneTimeCodeClient oneTimeCodeServiceConnection:detectedOneTimeCodes:]
+ -[UNOneTimeCodeClient queue]
+ -[UNOneTimeCodeClient removeObserver:]
+ -[UNOneTimeCodeClient setObservers:]
+ -[UNOneTimeCodeClient setQueue:]
+ -[UNOneTimeCodeServiceConnection .cxx_destruct]
+ -[UNOneTimeCodeServiceConnection _invalidate]
+ -[UNOneTimeCodeServiceConnection _queue_addObserver:]
+ -[UNOneTimeCodeServiceConnection _queue_ensureConnection]
+ -[UNOneTimeCodeServiceConnection _queue_interruptedConnection]
+ -[UNOneTimeCodeServiceConnection _queue_invalidatedConnection]
+ -[UNOneTimeCodeServiceConnection _queue_removeObserver:]
+ -[UNOneTimeCodeServiceConnection addObserver:]
+ -[UNOneTimeCodeServiceConnection callOutQueue]
+ -[UNOneTimeCodeServiceConnection connection]
+ -[UNOneTimeCodeServiceConnection consumeCode:]
+ -[UNOneTimeCodeServiceConnection detectedOneTimeCodes:]
+ -[UNOneTimeCodeServiceConnection init]
+ -[UNOneTimeCodeServiceConnection queue]
+ -[UNOneTimeCodeServiceConnection registerForUpdates]
+ -[UNOneTimeCodeServiceConnection removeObserver:]
+ -[UNOneTimeCodeServiceConnection setCallOutQueue:]
+ -[UNOneTimeCodeServiceConnection setConnection:]
+ -[UNOneTimeCodeServiceConnection setQueue:]
+ GCC_except_table17
+ _OBJC_CLASS_$_UNOneTimeCode
+ _OBJC_CLASS_$_UNOneTimeCodeClient
+ _OBJC_CLASS_$_UNOneTimeCodeService
+ _OBJC_CLASS_$_UNOneTimeCodeServiceConnection
+ _OBJC_IVAR_$_UNOneTimeCode._applicationIdentifier
+ _OBJC_IVAR_$_UNOneTimeCode._code
+ _OBJC_IVAR_$_UNOneTimeCode._notificationIdentifier
+ _OBJC_IVAR_$_UNOneTimeCode._timestamp
+ _OBJC_IVAR_$_UNOneTimeCodeClient._observers
+ _OBJC_IVAR_$_UNOneTimeCodeClient._queue
+ _OBJC_IVAR_$_UNOneTimeCodeServiceConnection._callOutQueue
+ _OBJC_IVAR_$_UNOneTimeCodeServiceConnection._connection
+ _OBJC_IVAR_$_UNOneTimeCodeServiceConnection._observers
+ _OBJC_IVAR_$_UNOneTimeCodeServiceConnection._queue
+ _OBJC_METACLASS_$_UNOneTimeCode
+ _OBJC_METACLASS_$_UNOneTimeCodeClient
+ _OBJC_METACLASS_$_UNOneTimeCodeService
+ _OBJC_METACLASS_$_UNOneTimeCodeServiceConnection
+ _UNOneTimeCodeMachServiceName
+ __OBJC_$_CLASS_METHODS_UNOneTimeCode
+ __OBJC_$_CLASS_METHODS_UNOneTimeCodeClient
+ __OBJC_$_CLASS_METHODS_UNOneTimeCodeService
+ __OBJC_$_CLASS_METHODS_UNOneTimeCodeServiceConnection
+ __OBJC_$_CLASS_PROP_LIST_UNOneTimeCode
+ __OBJC_$_INSTANCE_METHODS_UNOneTimeCode
+ __OBJC_$_INSTANCE_METHODS_UNOneTimeCodeClient
+ __OBJC_$_INSTANCE_METHODS_UNOneTimeCodeServiceConnection
+ __OBJC_$_INSTANCE_VARIABLES_UNOneTimeCode
+ __OBJC_$_INSTANCE_VARIABLES_UNOneTimeCodeClient
+ __OBJC_$_INSTANCE_VARIABLES_UNOneTimeCodeServiceConnection
+ __OBJC_$_PROP_LIST_UNOneTimeCode
+ __OBJC_$_PROP_LIST_UNOneTimeCodeClient
+ __OBJC_$_PROP_LIST_UNOneTimeCodeServiceConnection
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_UNOneTimeCodeServiceConnectionObserver
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_UNOneTimeCodeClientProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_UNOneTimeCodeServerProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_UNOneTimeCodeClientProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_UNOneTimeCodeServerProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_UNOneTimeCodeServiceConnectionObserver
+ __OBJC_$_PROTOCOL_REFS_UNOneTimeCodeClientProtocol
+ __OBJC_$_PROTOCOL_REFS_UNOneTimeCodeServerProtocol
+ __OBJC_$_PROTOCOL_REFS_UNOneTimeCodeServiceConnectionObserver
+ __OBJC_CLASS_PROTOCOLS_$_UNOneTimeCode
+ __OBJC_CLASS_PROTOCOLS_$_UNOneTimeCodeClient
+ __OBJC_CLASS_PROTOCOLS_$_UNOneTimeCodeServiceConnection
+ __OBJC_CLASS_RO_$_UNOneTimeCode
+ __OBJC_CLASS_RO_$_UNOneTimeCodeClient
+ __OBJC_CLASS_RO_$_UNOneTimeCodeService
+ __OBJC_CLASS_RO_$_UNOneTimeCodeServiceConnection
+ __OBJC_LABEL_PROTOCOL_$_UNOneTimeCodeClientProtocol
+ __OBJC_LABEL_PROTOCOL_$_UNOneTimeCodeServerProtocol
+ __OBJC_LABEL_PROTOCOL_$_UNOneTimeCodeServiceConnectionObserver
+ __OBJC_METACLASS_RO_$_UNOneTimeCode
+ __OBJC_METACLASS_RO_$_UNOneTimeCodeClient
+ __OBJC_METACLASS_RO_$_UNOneTimeCodeService
+ __OBJC_METACLASS_RO_$_UNOneTimeCodeServiceConnection
+ __OBJC_PROTOCOL_$_UNOneTimeCodeClientProtocol
+ __OBJC_PROTOCOL_$_UNOneTimeCodeServerProtocol
+ __OBJC_PROTOCOL_$_UNOneTimeCodeServiceConnectionObserver
+ __OBJC_PROTOCOL_REFERENCE_$_UNOneTimeCodeClientProtocol
+ __OBJC_PROTOCOL_REFERENCE_$_UNOneTimeCodeServerProtocol
+ ___35-[UNOneTimeCodeClient addObserver:]_block_invoke
+ ___36+[UNOneTimeCodeClient currentClient]_block_invoke
+ ___38-[UNOneTimeCodeClient removeObserver:]_block_invoke
+ ___38-[UNOneTimeCodeServiceConnection init]_block_invoke
+ ___39+[UNOneTimeCodeService clientInterface]_block_invoke
+ ___39+[UNOneTimeCodeService serverInterface]_block_invoke
+ ___46-[UNOneTimeCodeServiceConnection addObserver:]_block_invoke
+ ___46-[UNOneTimeCodeServiceConnection consumeCode:]_block_invoke
+ ___46-[UNOneTimeCodeServiceConnection consumeCode:]_block_invoke_2
+ ___46-[UNOneTimeCodeServiceConnection consumeCode:]_block_invoke_2.cold.1
+ ___48+[UNOneTimeCodeServiceConnection sharedInstance]_block_invoke
+ ___49-[UNOneTimeCodeServiceConnection removeObserver:]_block_invoke
+ ___52-[UNOneTimeCodeServiceConnection registerForUpdates]_block_invoke
+ ___52-[UNOneTimeCodeServiceConnection registerForUpdates]_block_invoke_2
+ ___52-[UNOneTimeCodeServiceConnection registerForUpdates]_block_invoke_2.cold.1
+ ___57-[UNOneTimeCodeServiceConnection _queue_ensureConnection]_block_invoke
+ ___57-[UNOneTimeCodeServiceConnection _queue_ensureConnection]_block_invoke_2
+ ___57-[UNOneTimeCodeServiceConnection _queue_ensureConnection]_block_invoke_3
+ ___57-[UNOneTimeCodeServiceConnection _queue_ensureConnection]_block_invoke_4
+ ___73-[UNOneTimeCodeClient oneTimeCodeServiceConnection:detectedOneTimeCodes:]_block_invoke
+ ___block_literal_global.5
+ ___block_literal_global.50
+ _currentClient.__sharedInstance
+ _currentClient.onceToken
+ _objc_msgSend$_descriptionForRedacted:
+ _objc_msgSend$_queue_addObserver:
+ _objc_msgSend$_queue_removeObserver:
+ _objc_msgSend$activate
+ _objc_msgSend$addObserver:
+ _objc_msgSend$applicationIdentifier
+ _objc_msgSend$code
+ _objc_msgSend$consumeCode:
+ _objc_msgSend$initWithCode:applicationIdentifier:notificationIdentifier:timestamp:
+ _objc_msgSend$notificationIdentifier
+ _objc_msgSend$oneTimeCodeClient:detectedOneTimeCodes:
+ _objc_msgSend$oneTimeCodeServiceConnection:detectedOneTimeCodes:
+ _objc_msgSend$registerForUpdates
+ _objc_msgSend$removeObserver:
+ _objc_msgSend$timestamp
+ _objc_msgSend$weakObjectsHashTable
CStrings:
+ "<%@: %p; code: %@; applicationIdentifier: %@; notificationIdentifier: %@; timestamp: %@>"
+ "@\"NSHashTable\""
+ "@\"NSMutableArray\""
+ "Consume OTC code: %@"
+ "Failed to consume code: %@"
+ "Failed to register for otc updates"
+ "Registering for OTC updates"
+ "T@\"NSDate\",R,C,N,V_timestamp"
+ "T@\"NSHashTable\",&,N,V_observers"
+ "T@\"NSString\",R,C,N,V_applicationIdentifier"
+ "T@\"NSString\",R,C,N,V_code"
+ "T@\"NSString\",R,C,N,V_notificationIdentifier"
+ "UNOneTimeCode"
+ "UNOneTimeCodeClient"
+ "UNOneTimeCodeClient.m"
+ "UNOneTimeCodeClientProtocol"
+ "UNOneTimeCodeServerProtocol"
+ "UNOneTimeCodeService"
+ "UNOneTimeCodeServiceConnection"
+ "UNOneTimeCodeServiceConnectionObserver"
+ "Uniform Type Identifier"
+ "_applicationIdentifier"
+ "_code"
+ "_descriptionForRedacted:"
+ "_notificationIdentifier"
+ "_observers"
+ "_queue_addObserver:"
+ "_queue_removeObserver:"
+ "_timestamp"
+ "activate"
+ "addObserver:"
+ "code"
+ "com.apple.UserNotifications.OneTimeCodeService"
+ "com.apple.usernotifications.UNOneTimeCodeClient"
+ "com.apple.usernotifications.UNOneTimeCodeServiceConnection"
+ "consumeCode:"
+ "currentClient"
+ "dealloc"
+ "detectedOneTimeCodes:"
+ "iconWithUTI:"
+ "initWithCode:applicationIdentifier:notificationIdentifier:timestamp:"
+ "notificationIdentifier"
+ "observers"
+ "oneTimeCodeClient:detectedOneTimeCodes:"
+ "oneTimeCodeServiceConnection:detectedOneTimeCodes:"
+ "redactedDescription"
+ "registerForUpdates"
+ "removeObserver:"
+ "setObservers:"
+ "timestamp"
+ "use +currentClient"
+ "uti"
+ "v24@0:8@\"NSSet\"16"
+ "v24@0:8@\"UNOneTimeCode\"16"
+ "v32@0:8@\"UNOneTimeCodeServiceConnection\"16@\"NSSet\"24"
+ "weakObjectsHashTable"

```
