## SummariesHealthDaemon

> `/System/Library/PrivateFrameworks/SummariesHealthDaemon.framework/SummariesHealthDaemon`

```diff

-6200.6.8.2.1
-  __TEXT.__text: 0x87c
-  __TEXT.__auth_stubs: 0x200
-  __TEXT.__objc_methlist: 0x27c
-  __TEXT.__cstring: 0x50
+7027.0.52.2.6
+  __TEXT.__text: 0x758
+  __TEXT.__objc_methlist: 0x284
+  __TEXT.__cstring: 0x54
   __TEXT.__const: 0x10
   __TEXT.__oslogstring: 0x1df
-  __TEXT.__unwind_info: 0xa0
-  __TEXT.__objc_classname: 0xb2
-  __TEXT.__objc_methname: 0x554
-  __TEXT.__objc_methtype: 0x229
-  __TEXT.__objc_stubs: 0x1a0
-  __DATA_CONST.__got: 0x20
+  __TEXT.__unwind_info: 0x90
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x8
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x190
+  __DATA_CONST.__objc_selrefs: 0x198
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x108
+  __DATA_CONST.__got: 0x18
   __AUTH_CONST.__cfstring: 0x60
-  __AUTH_CONST.__objc_const: 0x448
+  __AUTH_CONST.__objc_const: 0x450
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0xc
   __DATA.__data: 0x1e0
   __DATA_DIRTY.__objc_data: 0xa0

   - /System/Library/PrivateFrameworks/HealthDaemon.framework/HealthDaemon
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 60BD0DFD-644B-3E16-BE24-61F20D57C3B1
-  Functions: 21
-  Symbols:   143
-  CStrings:  111
+  UUID: 6D607C89-01CC-3512-B394-BFF7E1B588DA
+  Functions: 19
+  Symbols:   138
+  CStrings:  13
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_release_x26
+ _objc_retain
+ _objc_retain_x2
+ _objc_retain_x8
- _OUTLINED_FUNCTION_2
- _OUTLINED_FUNCTION_3
- ___stack_chk_fail
- ___stack_chk_guard
- _objc_release
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
- _objc_retain_x21
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"<HDHealthDaemonExtension>\"24@0:8@\"<HDHealthDaemon>\"16"
- "@\"<HDProfileExtension>\"24@0:8@\"HDProfile\"16"
- "@\"HDNotificationSyncClient\""
- "@\"HDPrimaryProfile\""
- "@\"NSString\"16@0:8"
- "@\"NSXPCListenerEndpoint\"32@0:8@\"HDXPCClient\"16^@24"
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@32@0:8:16@24"
- "@32@0:8@16^@24"
- "@40@0:8:16@24@32"
- "@?"
- "@?16@0:8"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"<HDHealthDaemon>\"16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "HDHealthDaemonReadyObserver"
- "HDNotificationSyncClientDelegate"
- "HDPlugin"
- "HDProfileExtension"
- "HDSummariesHealthDaemonPlugin"
- "HDSummariesHealthDaemonPluginProfileExtension"
- "NSObject"
- "Q16@0:8"
- "T#,R"
- "T@\"HDNotificationSyncClient\",&,N,V_notificationSyncClient"
- "T@\"HDPrimaryProfile\",R,W,N,V_profile"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,C,N"
- "T@?,C,N,V_unitTest_didProcessNotificationInstruction"
- "TQ,R"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_handleDismissInstructionWithClient:"
- "_notificationSyncClient"
- "_profile"
- "_unitTest_didProcessNotificationInstruction"
- "allObjects"
- "autorelease"
- "categoryIdentifiers"
- "class"
- "conformsToProtocol:"
- "daemonReady:"
- "debugDescription"
- "description"
- "extensionForHealthDaemon:"
- "extensionForProfile:"
- "handleDatabaseObliteration"
- "hash"
- "healthDaemon"
- "init"
- "initWithProfile:"
- "initWithProfile:clientIdentifier:queue:"
- "invalidateAndWait"
- "isEqual:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "listenerEndpointForClient:error:"
- "markPendingNotificationInstructionsAsProcessed:error:"
- "messageIdentifiers"
- "notificationManager"
- "notificationSyncClient"
- "notificationSyncClient:didReceiveInstructionWithAction:"
- "pendingNotificationDismissInstructionsWithError:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "pluginIdentifier"
- "prepareForObliteration"
- "profile"
- "registerDaemonReadyObserver:queue:"
- "release"
- "removeDeliveredNotificationsWithIdentifiers:"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "self"
- "setDelegate:"
- "setNotificationSyncClient:"
- "setUnitTest_didProcessNotificationInstruction:"
- "shouldLoadPluginForDaemon:"
- "superclass"
- "unitTest_didProcessNotificationInstruction"
- "v16@0:8"
- "v24@0:8@\"<HDHealthDaemon>\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v32@0:8@\"HDNotificationSyncClient\"16q24"
- "v32@0:8@16q24"
- "zone"

```
