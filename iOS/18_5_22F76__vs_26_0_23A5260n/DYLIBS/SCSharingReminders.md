## SCSharingReminders

> `/System/Library/PrivateFrameworks/SCSharingReminders.framework/SCSharingReminders`

```diff

-425.0.114.0.0
-  __TEXT.__text: 0xd7a0
-  __TEXT.__auth_stubs: 0x4f0
-  __TEXT.__objc_methlist: 0xf10
-  __TEXT.__const: 0xd0
-  __TEXT.__gcc_except_tab: 0x3cc
-  __TEXT.__cstring: 0xa22
-  __TEXT.__oslogstring: 0xea4
-  __TEXT.__unwind_info: 0x468
-  __TEXT.__objc_classname: 0x2ee
-  __TEXT.__objc_methname: 0x226e
-  __TEXT.__objc_methtype: 0x62b
-  __TEXT.__objc_stubs: 0x2140
-  __DATA_CONST.__got: 0x1d0
-  __DATA_CONST.__const: 0x5c0
-  __DATA_CONST.__objc_classlist: 0xa8
-  __DATA_CONST.__objc_protolist: 0x58
+552.0.0.0.0
+  __TEXT.__text: 0xbd68
+  __TEXT.__auth_stubs: 0x4b0
+  __TEXT.__objc_methlist: 0xcc8
+  __TEXT.__const: 0xc8
+  __TEXT.__gcc_except_tab: 0x3bc
+  __TEXT.__cstring: 0x951
+  __TEXT.__oslogstring: 0xd61
+  __TEXT.__unwind_info: 0x3f8
+  __TEXT.__objc_classname: 0x28c
+  __TEXT.__objc_methname: 0x1e6d
+  __TEXT.__objc_methtype: 0x5a1
+  __TEXT.__objc_stubs: 0x1c60
+  __DATA_CONST.__got: 0x190
+  __DATA_CONST.__const: 0x570
+  __DATA_CONST.__objc_classlist: 0x88
+  __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa18
+  __DATA_CONST.__objc_selrefs: 0x8c0
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x80
+  __DATA_CONST.__objc_superrefs: 0x68
   __DATA_CONST.__objc_arraydata: 0x38
-  __AUTH_CONST.__auth_got: 0x288
+  __AUTH_CONST.__auth_got: 0x268
   __AUTH_CONST.__const: 0x158
-  __AUTH_CONST.__cfstring: 0x8a0
-  __AUTH_CONST.__objc_const: 0x1900
+  __AUTH_CONST.__cfstring: 0x7c0
+  __AUTH_CONST.__objc_const: 0x1410
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH.__objc_data: 0x230
-  __DATA.__objc_ivar: 0x98
-  __DATA.__data: 0x428
-  __DATA.__bss: 0x20
-  __DATA_DIRTY.__objc_data: 0x460
+  __AUTH.__objc_data: 0x1e0
+  __DATA.__objc_ivar: 0x74
+  __DATA.__data: 0x368
+  __DATA.__bss: 0x10
+  __DATA_DIRTY.__objc_data: 0x370
   __DATA_DIRTY.__bss: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1A60EF8B-5716-368A-8D72-5A242D201759
-  Functions: 358
-  Symbols:   1469
-  CStrings:  750
+  UUID: 4E6AC5A4-D781-369E-A026-70C321256543
+  Functions: 312
+  Symbols:   1277
+  CStrings:  658
 
Symbols:
+ +[SCSharingReminderServiceProvider tasks]
+ -[SCSharingReminderServiceProvider .cxx_destruct]
+ -[SCSharingReminderServiceProvider fetchStatusWithCompletion:]
+ -[SCSharingReminderServiceProvider handleSignals:completion:]
+ -[SCSharingReminderServiceProvider handleXPCEventWithName:]
+ -[SCSharingReminderServiceProvider handleXPCEventWithName:].cold.1
+ -[SCSharingReminderServiceProvider init]
+ -[SCSharingReminderServiceProvider interestedEvents]
+ -[SCSharingReminderServiceProvider postWifiSyncNotificationWithCompletion:]
+ -[SCSharingReminderServiceProvider resetFeatureWithCompletion:]
+ -[SCSharingReminderServiceProvider setReminderDelays:completion:]
+ -[SCSharingReminderServiceProvider setSharingReminderManager:]
+ -[SCSharingReminderServiceProvider sharingReminderManager]
+ -[SCSharingReminderServiceProvider userOpenedSafetyCheckWithCompletion:]
+ _OBJC_CLASS_$_SCSharingReminderServiceProvider
+ _OBJC_IVAR_$_SCSharingReminderServiceProvider._sharingReminderManager
+ _OBJC_METACLASS_$_SCSharingReminderServiceProvider
+ __OBJC_$_CLASS_METHODS_SCSharingReminderServiceProvider
+ __OBJC_$_INSTANCE_METHODS_SCSharingReminderServiceProvider
+ __OBJC_$_INSTANCE_VARIABLES_SCSharingReminderServiceProvider
+ __OBJC_$_PROP_LIST_SCSharingReminderServiceProvider
+ __OBJC_CLASS_PROTOCOLS_$_SCSharingReminderServiceProvider
+ __OBJC_CLASS_RO_$_SCSharingReminderServiceProvider
+ __OBJC_METACLASS_RO_$_SCSharingReminderServiceProvider
- +[SCDaemon sharedDaemon]
- +[SCPair pairWithFirst:second:]
- +[SCSharingReminderXPCService tasks]
- -[SCDaemon .cxx_destruct]
- -[SCDaemon XPCListenerPairs]
- -[SCDaemon _listenersByEventName]
- -[SCDaemon activeXPCListenerPairs]
- -[SCDaemon backgroundSystemTasks]
- -[SCDaemon init]
- -[SCDaemon notifyDListeners]
- -[SCDaemon registerBackgroundSystemTasks]
- -[SCDaemon registerXPCEventHandlers]
- -[SCDaemon setActiveXPCListenerPairs:]
- -[SCDaemon setWorkQueue:]
- -[SCDaemon start]
- -[SCDaemon wakeXPCListeners]
- -[SCDaemon workQueue]
- -[SCPair .cxx_destruct]
- -[SCPair copyWithZone:]
- -[SCPair description]
- -[SCPair first]
- -[SCPair hash]
- -[SCPair initNonMemoizedWithFirst:second:]
- -[SCPair isEqual:]
- -[SCPair isEqualToPair:]
- -[SCPair second]
- -[SCPair setFirst:]
- -[SCPair setSecond:]
- -[SCSharingReminderDelegate listener:shouldAcceptNewConnection:]
- -[SCSharingReminderXPCClient .cxx_destruct]
- -[SCSharingReminderXPCClient clientBundle]
- -[SCSharingReminderXPCClient clientBundle].cold.1
- -[SCSharingReminderXPCClient hasAccess]
- -[SCSharingReminderXPCClient hasFeatureAccess]
- -[SCSharingReminderXPCClient initWithConnection:]
- -[SCSharingReminderXPCClient name]
- -[SCSharingReminderXPCClient name].cold.1
- -[SCSharingReminderXPCClient xpcConnection]
- -[SCSharingReminderXPCService .cxx_destruct]
- -[SCSharingReminderXPCService fetchStatusWithCompletion:]
- -[SCSharingReminderXPCService handleSignals:completion:]
- -[SCSharingReminderXPCService handleXPCEventWithName:]
- -[SCSharingReminderXPCService handleXPCEventWithName:].cold.1
- -[SCSharingReminderXPCService initWithClient:]
- -[SCSharingReminderXPCService init]
- -[SCSharingReminderXPCService interestedEvents]
- -[SCSharingReminderXPCService postWifiSyncNotificationWithCompletion:]
- -[SCSharingReminderXPCService rejectRequest:withCompletion:]
- -[SCSharingReminderXPCService rejectRequest:withCompletion:].cold.1
- -[SCSharingReminderXPCService rejectRequest:withCompletion:].cold.2
- -[SCSharingReminderXPCService resetFeatureWithCompletion:]
- -[SCSharingReminderXPCService serviceClient]
- -[SCSharingReminderXPCService setReminderDelays:completion:]
- -[SCSharingReminderXPCService setServiceClient:]
- -[SCSharingReminderXPCService setSharingReminderManager:]
- -[SCSharingReminderXPCService sharingReminderManager]
- -[SCSharingReminderXPCService userOpenedSafetyCheckWithCompletion:]
- OBJC_IVAR_$_SCPair._first
- OBJC_IVAR_$_SCPair._second
- _OBJC_CLASS_$_NSDictionary
- _OBJC_CLASS_$_NSXPCListener
- _OBJC_CLASS_$_SCDaemon
- _OBJC_CLASS_$_SCPair
- _OBJC_CLASS_$_SCSharingReminderDelegate
- _OBJC_CLASS_$_SCSharingReminderXPCClient
- _OBJC_CLASS_$_SCSharingReminderXPCService
- _OBJC_IVAR_$_SCDaemon._activeXPCListenerPairs
- _OBJC_IVAR_$_SCDaemon._workQueue
- _OBJC_IVAR_$_SCSharingReminderXPCClient._clientBundle
- _OBJC_IVAR_$_SCSharingReminderXPCClient._name
- _OBJC_IVAR_$_SCSharingReminderXPCClient._pid
- _OBJC_IVAR_$_SCSharingReminderXPCClient._xpcConnection
- _OBJC_IVAR_$_SCSharingReminderXPCService._serviceClient
- _OBJC_IVAR_$_SCSharingReminderXPCService._sharingReminderManager
- _OBJC_METACLASS_$_SCDaemon
- _OBJC_METACLASS_$_SCPair
- _OBJC_METACLASS_$_SCSharingReminderDelegate
- _OBJC_METACLASS_$_SCSharingReminderXPCClient
- _OBJC_METACLASS_$_SCSharingReminderXPCService
- __OBJC_$_CLASS_METHODS_SCDaemon
- __OBJC_$_CLASS_METHODS_SCPair
- __OBJC_$_CLASS_METHODS_SCSharingReminderXPCService
- __OBJC_$_INSTANCE_METHODS_SCDaemon
- __OBJC_$_INSTANCE_METHODS_SCPair
- __OBJC_$_INSTANCE_METHODS_SCSharingReminderDelegate
- __OBJC_$_INSTANCE_METHODS_SCSharingReminderXPCClient
- __OBJC_$_INSTANCE_METHODS_SCSharingReminderXPCService
- __OBJC_$_INSTANCE_VARIABLES_SCDaemon
- __OBJC_$_INSTANCE_VARIABLES_SCPair
- __OBJC_$_INSTANCE_VARIABLES_SCSharingReminderXPCClient
- __OBJC_$_INSTANCE_VARIABLES_SCSharingReminderXPCService
- __OBJC_$_PROP_LIST_SCDaemon
- __OBJC_$_PROP_LIST_SCPair
- __OBJC_$_PROP_LIST_SCSharingReminderDelegate
- __OBJC_$_PROP_LIST_SCSharingReminderXPCClient
- __OBJC_$_PROP_LIST_SCSharingReminderXPCService
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSXPCListenerDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSXPCListenerDelegate
- __OBJC_$_PROTOCOL_REFS_NSXPCListenerDelegate
- __OBJC_CLASS_PROTOCOLS_$_SCPair
- __OBJC_CLASS_PROTOCOLS_$_SCSharingReminderDelegate
- __OBJC_CLASS_PROTOCOLS_$_SCSharingReminderXPCService
- __OBJC_CLASS_RO_$_SCDaemon
- __OBJC_CLASS_RO_$_SCPair
- __OBJC_CLASS_RO_$_SCSharingReminderDelegate
- __OBJC_CLASS_RO_$_SCSharingReminderXPCClient
- __OBJC_CLASS_RO_$_SCSharingReminderXPCService
- __OBJC_LABEL_PROTOCOL_$_NSCopying
- __OBJC_LABEL_PROTOCOL_$_NSXPCListenerDelegate
- __OBJC_METACLASS_RO_$_SCDaemon
- __OBJC_METACLASS_RO_$_SCPair
- __OBJC_METACLASS_RO_$_SCSharingReminderDelegate
- __OBJC_METACLASS_RO_$_SCSharingReminderXPCClient
- __OBJC_METACLASS_RO_$_SCSharingReminderXPCService
- __OBJC_PROTOCOL_$_NSCopying
- __OBJC_PROTOCOL_$_NSXPCListenerDelegate
- ___24+[SCDaemon sharedDaemon]_block_invoke
- ___36-[SCDaemon registerXPCEventHandlers]_block_invoke
- ___57-[SCSharingReminderXPCService fetchStatusWithCompletion:]_block_invoke
- ___block_descriptor_40_e8_32bs_e20_v20?0B8"NSError"12ls32l8
- ___block_descriptor_40_e8_32s_e33_v16?0"NSObject<OS_xpc_object>"8ls32l8
- __xpc_event_key_name
- _objc_msgSend$XPCListenerPairs
- _objc_msgSend$_listenersByEventName
- _objc_msgSend$allKeys
- _objc_msgSend$backgroundSystemTasks
- _objc_msgSend$bundleIdentifier
- _objc_msgSend$bundleWithPath:
- _objc_msgSend$clientBundle
- _objc_msgSend$dictionaryWithObjects:forKeys:count:
- _objc_msgSend$first
- _objc_msgSend$handleXPCEventWithName:
- _objc_msgSend$hasAccess
- _objc_msgSend$hasFeatureAccess
- _objc_msgSend$initNonMemoizedWithFirst:second:
- _objc_msgSend$initWithClient:
- _objc_msgSend$initWithConnection:
- _objc_msgSend$initWithMachServiceName:
- _objc_msgSend$isEqualToPair:
- _objc_msgSend$name
- _objc_msgSend$notifyDListeners
- _objc_msgSend$objectForKeyedSubscript:
- _objc_msgSend$pairWithFirst:second:
- _objc_msgSend$processIdentifier
- _objc_msgSend$registerBackgroundSystemTasks
- _objc_msgSend$registerForTaskUsingQueue:
- _objc_msgSend$registerXPCEventHandlers
- _objc_msgSend$rejectRequest:withCompletion:
- _objc_msgSend$resume
- _objc_msgSend$second
- _objc_msgSend$serviceClient
- _objc_msgSend$serviceName
- _objc_msgSend$setActiveXPCListenerPairs:
- _objc_msgSend$setExportedInterface:
- _objc_msgSend$setExportedObject:
- _objc_msgSend$setServiceClient:
- _objc_msgSend$stringByDeletingLastPathComponent
- _objc_msgSend$stringWithUTF8String:
- _objc_msgSend$tasks
- _objc_msgSend$valueForEntitlement:
- _objc_msgSend$wakeXPCListeners
- _proc_name
- _proc_pidpath
- _sharedDaemon.__sharedDaemon
- _sharedDaemon.onceToken
- _xpc_dictionary_get_string
- _xpc_set_event_stream_handler
CStrings:
+ "SCSharingReminderServiceProvider"
- "\"Accepting new connection with listener: %@ for: %@\""
- "\"Could not resolve path for process identifier: %d\""
- "\"Rejecting process %d because it is not entitled to use SCSharingReminders\""
- "\"proc_name failed for process identifier: %d\""
- "<%@: %p first:%@ second:%@>"
- "@"
- "@\"NSArray\""
- "@\"NSBundle\""
- "@\"Rejecting %@ request from: %@, client is not entitled\""
- "@\"Rejecting %@ request, client is nil\""
- "@\"SCSharingReminderXPCClient\""
- "@24@0:8^{_NSZone=}16"
- "B32@0:8@\"NSXPCListener\"16@\"NSXPCConnection\"24"
- "B32@0:8@16@24"
- "NSCopying"
- "NSXPCListenerDelegate"
- "SCDaemon"
- "SCPair"
- "SCSharingReminderDelegate"
- "SCSharingReminderXPCClient"
- "SCSharingReminderXPCService"
- "T@\"NSArray\",&,N,V_activeXPCListenerPairs"
- "T@\"NSString\",R,N"
- "T@\"SCSharingReminderXPCClient\",&,N,V_serviceClient"
- "T@,C,N,V_first"
- "T@,C,N,V_second"
- "TB,R,N"
- "XPCListenerPairs"
- "_activeXPCListenerPairs"
- "_clientBundle"
- "_first"
- "_listenersByEventName"
- "_name"
- "_pid"
- "_second"
- "_serviceClient"
- "activeXPCListenerPairs"
- "allKeys"
- "backgroundSystemTasks"
- "bundleIdentifier"
- "bundleWithPath:"
- "clientBundle"
- "com.apple.safetycheckd.queue"
- "copyWithZone:"
- "dictionaryWithObjects:forKeys:count:"
- "fetchStatus"
- "first"
- "handleSignals"
- "hasAccess"
- "hasFeatureAccess"
- "i"
- "initNonMemoizedWithFirst:second:"
- "initWithClient:"
- "initWithConnection:"
- "initWithMachServiceName:"
- "isEqualToPair:"
- "listener:shouldAcceptNewConnection:"
- "name"
- "notifyDListeners"
- "objectForKeyedSubscript:"
- "pairWithFirst:second:"
- "postWifiSyncNotification"
- "processIdentifier"
- "registerBackgroundSystemTasks"
- "registerXPCEventHandlers"
- "rejectRequest:withCompletion:"
- "resetFeatureWithCompletion"
- "resume"
- "second"
- "serviceClient"
- "serviceName"
- "setActiveXPCListenerPairs:"
- "setExportedInterface:"
- "setExportedObject:"
- "setFirst:"
- "setReminderDelays"
- "setSecond:"
- "setServiceClient:"
- "sharedDaemon"
- "start"
- "stringByDeletingLastPathComponent"
- "stringWithUTF8String:"
- "userOpenedSafetyCheck"
- "v16@?0@\"NSObject<OS_xpc_object>\"8"
- "valueForEntitlement:"
- "wakeXPCListeners"

```
