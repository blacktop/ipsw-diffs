## safetycheckd

> `/usr/libexec/safetycheckd`

```diff

-425.0.114.0.0
-  __TEXT.__text: 0xd50
-  __TEXT.__auth_stubs: 0x1d0
-  __TEXT.__objc_stubs: 0x560
-  __TEXT.__objc_methlist: 0x138
-  __TEXT.__const: 0x8
-  __TEXT.__cstring: 0x93
-  __TEXT.__objc_classname: 0x1a
-  __TEXT.__objc_methname: 0x42b
-  __TEXT.__objc_methtype: 0x85
-  __TEXT.__unwind_info: 0xb0
-  __DATA_CONST.__auth_got: 0xf0
-  __DATA_CONST.__got: 0x88
-  __DATA_CONST.__const: 0x48
-  __DATA_CONST.__cfstring: 0x20
-  __DATA_CONST.__objc_classlist: 0x10
+552.0.0.0.0
+  __TEXT.__text: 0x2900
+  __TEXT.__auth_stubs: 0x2e0
+  __TEXT.__objc_stubs: 0xa40
+  __TEXT.__objc_methlist: 0x4c8
+  __TEXT.__const: 0x38
+  __TEXT.__objc_methname: 0xac0
+  __TEXT.__oslogstring: 0x225
+  __TEXT.__objc_classname: 0xe8
+  __TEXT.__objc_methtype: 0x34d
+  __TEXT.__cstring: 0x215
+  __TEXT.__gcc_except_tab: 0x10
+  __TEXT.__unwind_info: 0x140
+  __DATA_CONST.__auth_got: 0x180
+  __DATA_CONST.__got: 0xa8
+  __DATA_CONST.__const: 0x198
+  __DATA_CONST.__cfstring: 0x180
+  __DATA_CONST.__objc_classlist: 0x28
+  __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x10
-  __DATA.__objc_const: 0x230
-  __DATA.__objc_selrefs: 0x188
-  __DATA.__objc_ivar: 0x10
-  __DATA.__objc_data: 0xa0
-  __DATA.__data: 0x8
-  __DATA.__bss: 0x10
+  __DATA_CONST.__objc_protorefs: 0x8
+  __DATA_CONST.__objc_superrefs: 0x28
+  __DATA.__objc_const: 0x8a0
+  __DATA.__objc_selrefs: 0x368
+  __DATA.__objc_ivar: 0x38
+  __DATA.__objc_data: 0x190
+  __DATA.__data: 0x248
+  __DATA.__bss: 0x30
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/BackgroundSystemTasks.framework/BackgroundSystemTasks
+  - /System/Library/PrivateFrameworks/DigitalSeparation.framework/DigitalSeparation
   - /System/Library/PrivateFrameworks/SCSharingReminders.framework/SCSharingReminders
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: FC031C7A-1E82-3713-BB61-83CA40C8D5E2
-  Functions: 26
-  Symbols:   53
-  CStrings:  78
+  UUID: AFDF9C40-08AC-3E7B-9595-BDE088C29B9A
+  Functions: 79
+  Symbols:   76
+  CStrings:  237
 
Symbols:
+ _OBJC_CLASS_$_DSError
+ _OBJC_CLASS_$_DSSharingPermissions
+ _OBJC_CLASS_$_NSBundle
+ _OBJC_CLASS_$_NSDate
+ _OBJC_CLASS_$_NSXPCInterface
+ _OBJC_CLASS_$_SCSharingReminderServiceProvider
+ __NSConcreteGlobalBlock
+ __Unwind_Resume
+ ___objc_personality_v0
+ __os_log_error_impl
+ __os_log_impl
+ _dispatch_async
+ _dispatch_queue_attr_make_with_autorelease_frequency
+ _dispatch_queue_attr_make_with_qos_class
+ _kSCSharingRemindersEntitlement
+ _kSCSharingRemindersEntitlementInternal
+ _kSafetyCheckWhenBlockingEntitlement
+ _objc_release
+ _objc_retain_x1
+ _objc_retain_x19
+ _objc_retain_x2
+ _objc_retain_x20
+ _objc_retain_x21
+ _objc_retain_x22
+ _objc_retain_x8
+ _os_log_create
+ _os_log_type_enabled
+ _proc_name
+ _proc_pidpath
- _OBJC_CLASS_$_NSDictionary
- _OBJC_CLASS_$_SCPair
- _OBJC_CLASS_$_SCSharingReminderDelegate
- _OBJC_CLASS_$_SCSharingReminderXPCService
- _kSharingRemindersMachServiceName
- _objc_release_x25
CStrings:
+ "\"Could not resolve path for process identifier: %d\""
+ "\"Received new connection: %@\""
+ "\"SCPermissionsService finished permissions fetch in %.2fs and error %@.\""
+ "\"Trying to stop all sharing for person %{private}@, but they aren't in the permissions model\""
+ "\"Trying to stop selected sharing for person %{private}@, but they aren't in the permissions model\""
+ "\"proc_name failed for process identifier: %d\""
+ "#16@0:8"
+ "@\"DSSharingPermissions\""
+ "@\"NSBundle\""
+ "@\"NSString\""
+ "@\"NSString\"16@0:8"
+ "@\"NSXPCConnection\""
+ "@\"NSXPCInterface\"16@0:8"
+ "@\"NSXPCListener\""
+ "@\"Rejecting %@ request from: %@, client is not entitled\""
+ "@\"Rejecting %@ request, client is nil\""
+ "@\"SCDaemonClient\""
+ "@\"SCPermissionsService\""
+ "@\"SCSharingReminderServiceProvider\""
+ "@\"Stopping sharing from %{public}@ for person %{private}@\""
+ "@24@0:8:16"
+ "@24@0:8@16"
+ "@32@0:8:16@24"
+ "@40@0:8:16@24@32"
+ "B16@0:8"
+ "B24@0:8#16"
+ "B24@0:8:16"
+ "B24@0:8@\"Protocol\"16"
+ "B24@0:8@16"
+ "B32@0:8@\"NSXPCListener\"16@\"NSXPCConnection\"24"
+ "B32@0:8@16@24"
+ "DSSafetyCheckBlocking"
+ "NSObject"
+ "NSXPCListenerDelegate"
+ "None"
+ "Q16@0:8"
+ "SCDaemonClient"
+ "SCDaemonClientInterface"
+ "SCDaemonService"
+ "SCLogger"
+ "SCPermissionsService"
+ "SCSharingReminderFeatureControlling"
+ "SCSharingReminderPreferencesDelegate"
+ "T#,R"
+ "T@\"DSSharingPermissions\",&,N,V_permissions"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",R,C"
+ "T@\"NSString\",R,N"
+ "T@\"NSXPCConnection\",R,N,V_xpcConnection"
+ "T@\"NSXPCListener\",&,N,V_xpcListener"
+ "T@\"SCDaemonClient\",&,N,V_client"
+ "T@\"SCPermissionsService\",&,N,V_sharingPermissionsService"
+ "T@\"SCSharingReminderServiceProvider\",&,N,V_sharingReminderService"
+ "TB,R,N"
+ "TQ,R"
+ "Vv16@0:8"
+ "^{_NSZone=}16@0:8"
+ "_client"
+ "_clientBundle"
+ "_dispatchQueue"
+ "_name"
+ "_permissions"
+ "_pid"
+ "_sharingPermissionsService"
+ "_sharingReminderService"
+ "_xpcConnection"
+ "_xpcListener"
+ "allPeople"
+ "autorelease"
+ "boolValue"
+ "bundleIdentifier"
+ "bundleWithPath:"
+ "class"
+ "client"
+ "clientBundle"
+ "com.apple.safetycheckd"
+ "com.apple.safetycheckd.SCPermissionsService.dispatchQueue"
+ "com.apple.safetycheckd.SCPermissionsService.workQueue"
+ "conformsToProtocol:"
+ "copy"
+ "debugDescription"
+ "description"
+ "exportedInterface"
+ "fetchPermissionsOnQueue:completion:"
+ "fetchSharingPeopleWithCompletion:"
+ "fetchStatus"
+ "fetchStatusWithCompletion:"
+ "handleSignals"
+ "handleSignals:completion:"
+ "hasBlockingAccess"
+ "hasSharingReminderAccess"
+ "hasSharingReminderFeatureAccess"
+ "hash"
+ "i"
+ "initWithClient:"
+ "initWithConnection:"
+ "interfaceWithProtocol:"
+ "isEqual:"
+ "isKindOfClass:"
+ "isMemberOfClass:"
+ "isProxy"
+ "listener:shouldAcceptNewConnection:"
+ "matchesXPCRepresentation:"
+ "name"
+ "performSelector:"
+ "performSelector:withObject:"
+ "performSelector:withObject:withObject:"
+ "permissions"
+ "personInModelMatchingShallowPerson:"
+ "postWifiSyncNotification"
+ "postWifiSyncNotificationWithCompletion:"
+ "processIdentifier"
+ "rejectBlockingRequest:withCompletion:"
+ "rejectRequest:withCompletion:"
+ "release"
+ "resetFeatureWithCompletion"
+ "resetFeatureWithCompletion:"
+ "respondsToSelector:"
+ "retain"
+ "retainCount"
+ "self"
+ "setClient:"
+ "setExportedInterface:"
+ "setExportedObject:"
+ "setPermissions:"
+ "setReminderDelays"
+ "setReminderDelays:completion:"
+ "setSharingPermissionsService:"
+ "setSharingReminderService:"
+ "setXpcListener:"
+ "sharingPermissionsService"
+ "sharingReminderService"
+ "stopAllSharingOnQueue:completion:"
+ "stopAllSharingWithPerson:"
+ "stopAllSharingWithPerson:completion:"
+ "stopSharingSourceNames:queue:completion:"
+ "stopSharingSources:"
+ "stopSharingSources:withPerson:completion:"
+ "stringByDeletingLastPathComponent"
+ "superclass"
+ "timeIntervalSinceReferenceDate"
+ "userOpenedSafetyCheck"
+ "userOpenedSafetyCheckWithCompletion:"
+ "v16@?0@\"NSError\"8"
+ "v20@?0B8@\"NSError\"12"
+ "v24@0:8@?16"
+ "v24@0:8@?<v@?@\"NSArray\"@\"NSError\">16"
+ "v24@0:8@?<v@?B@\"NSError\">16"
+ "v24@0:8@?<v@?{?={?=QQQQ}{?=C@@@}}>16"
+ "v32@0:8@\"DSXPCSharingPerson\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"NSArray\"16@?<v@?B@\"NSError\">24"
+ "v32@0:8@16@?24"
+ "v40@0:8@\"NSArray\"16@\"DSXPCSharingPerson\"24@?<v@?@\"NSError\">32"
+ "v40@0:8@16@24@?32"
+ "valueForEntitlement:"
+ "xpcConnection"
+ "xpcListener"
+ "xpcRepresentation"
+ "zone"
- "@\"NSArray\""
- "T@\"NSArray\",&,N,V_activeXPCListenerPairs"
- "XPCListenerPairs"
- "_activeXPCListenerPairs"
- "activeXPCListenerPairs"
- "allKeys"
- "dictionaryWithObjects:forKeys:count:"
- "first"
- "pairWithFirst:second:"
- "setActiveXPCListenerPairs:"
- "valueForKey:"
- "wakeXPCListeners"

```
