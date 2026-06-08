## CompanionHealthPlugin

> `/System/Library/Health/Plugins/CompanionHealthPlugin.bundle/CompanionHealthPlugin`

```diff

-2026.5.4.0.0
-  __TEXT.__text: 0x784
-  __TEXT.__auth_stubs: 0x190
-  __TEXT.__objc_methlist: 0x364
+2027.0.93.0.0
+  __TEXT.__text: 0x5f8
+  __TEXT.__objc_methlist: 0x36c
   __TEXT.__const: 0x8
   __TEXT.__gcc_except_tab: 0x14
-  __TEXT.__cstring: 0x66
+  __TEXT.__cstring: 0x6a
   __TEXT.__oslogstring: 0x6d
-  __TEXT.__unwind_info: 0xc8
-  __TEXT.__objc_classname: 0xcb
-  __TEXT.__objc_methname: 0x7d1
-  __TEXT.__objc_methtype: 0x2d6
-  __TEXT.__objc_stubs: 0xe0
-  __DATA_CONST.__got: 0x78
+  __TEXT.__unwind_info: 0x98
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x30
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1d0
+  __DATA_CONST.__objc_selrefs: 0x1d8
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0xd8
+  __DATA_CONST.__got: 0x78
   __AUTH_CONST.__cfstring: 0x40
-  __AUTH_CONST.__objc_const: 0x5a0
+  __AUTH_CONST.__objc_const: 0x5a8
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0x24
   __DATA.__data: 0x2a0
   __DATA_DIRTY.__objc_data: 0xa0

   - /System/Library/PrivateFrameworks/HealthDaemonFoundation.framework/HealthDaemonFoundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B8C9E09A-99D8-3048-BEEC-795512577715
+  UUID: 4D36C6FE-F7A3-3578-9D99-7F501236FD18
   Functions: 28
-  Symbols:   50
-  CStrings:  130
+  Symbols:   49
+  CStrings:  7
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x2
- _objc_release
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
Functions:
~ sub_2a8fc3f64 -> sub_247954f64 : 108 -> 104
~ sub_2a8fc3fd8 -> sub_247954fd4 : 132 -> 128
~ sub_2a8fc4068 -> sub_247955060 : 720 -> 696
~ sub_2a8fc4464 -> sub_247955444 : 64 -> 12
~ sub_2a8fc44ac -> sub_247955458 : 64 -> 12
~ sub_2a8fc44f4 -> sub_24795546c : 64 -> 12
~ sub_2a8fc453c -> sub_247955480 : 64 -> 12
~ sub_2a8fc4584 -> sub_247955494 : 64 -> 12
~ sub_2a8fc45cc -> sub_2479554a8 : 64 -> 12
~ sub_2a8fc4614 -> sub_2479554bc : 64 -> 12
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"<HDHealthDaemonExtension>\"24@0:8@\"<HDHealthDaemon>\"16"
- "@\"<HDProfileExtension>\"24@0:8@\"HDProfile\"16"
- "@\"CHActivityApplicationInstallationManager\""
- "@\"CHCoachingDiagnosticManager\""
- "@\"CHCompanionWidgetSchedulingManager\""
- "@\"CHCompanionWorkoutCreditManager\""
- "@\"CHFitnessAppBadgeManager\""
- "@\"CHTrendsNotificationManager\""
- "@\"FCHealthService\""
- "@\"FCHealthService\"16@0:8"
- "@\"HDProfile\""
- "@\"NSArray\"16@0:8"
- "@\"NSString\"16@0:8"
- "@\"NSXPCListenerEndpoint\"32@0:8@\"HDXPCClient\"16^@24"
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@32@0:8:16@24"
- "@32@0:8@16^@24"
- "@40@0:8:16@24@32"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"<HDHealthDaemon>\"16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "CHCompanionHealthPlugin"
- "CHCompanionHealthProfileExtending"
- "CHCompanionHealthProfileExtension"
- "FCHealthProfileExtending"
- "HDDiagnosticObject"
- "HDPlugin"
- "HDProfileExtension"
- "HDTaskServerClassProvider"
- "NSObject"
- "Q16@0:8"
- "T#,R"
- "T@\"CHActivityApplicationInstallationManager\",&,N,V_activityApplicationInstallationManager"
- "T@\"CHCoachingDiagnosticManager\",&,N,V_coachDiagnosticManager"
- "T@\"CHCompanionWidgetSchedulingManager\",&,N,V_widgetSchedulingManager"
- "T@\"CHCompanionWorkoutCreditManager\",&,N,V_companionWorkoutCreditManager"
- "T@\"CHFitnessAppBadgeManager\",&,N,V_fitnessAppBadgeManager"
- "T@\"CHTrendsNotificationManager\",&,N,V_trendsNotificationManager"
- "T@\"FCHealthService\",&,N,V_fitnessCoachingHealthService"
- "T@\"HDProfile\",W,N,V_profile"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,C,N"
- "TQ,R"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_activityApplicationInstallationManager"
- "_coachDiagnosticManager"
- "_companionWorkoutCreditManager"
- "_fitnessAppBadgeManager"
- "_fitnessCoachingHealthService"
- "_profile"
- "_standalonePhoneFitnessModeChangeToken"
- "_trendsNotificationManager"
- "_widgetSchedulingManager"
- "activityApplicationInstallationManager"
- "arrayWithObjects:count:"
- "autorelease"
- "class"
- "coachDiagnosticManager"
- "companionWorkoutCreditManager"
- "conformsToProtocol:"
- "dealloc"
- "debugDescription"
- "description"
- "diagnosticDescription"
- "extensionForHealthDaemon:"
- "extensionForProfile:"
- "fitnessAppBadgeManager"
- "fitnessCoachingHealthService"
- "handleDatabaseObliteration"
- "hash"
- "i"
- "init"
- "initWithProfile:"
- "invalidateAndWait"
- "isEqual:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "listenerEndpointForClient:error:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "pluginIdentifier"
- "prepareForObliteration"
- "profile"
- "profileType"
- "registerFitnessAppBadgeCountProvider:"
- "registerProvider:"
- "release"
- "requestBadgeUpdate"
- "requestFitnessAppBadgeCountUpdate"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "self"
- "setActivityApplicationInstallationManager:"
- "setCoachDiagnosticManager:"
- "setCompanionWorkoutCreditManager:"
- "setFitnessAppBadgeManager:"
- "setFitnessCoachingHealthService:"
- "setProfile:"
- "setTrendsNotificationManager:"
- "setWidgetSchedulingManager:"
- "shouldLoadPluginForDaemon:"
- "superclass"
- "taskServerClasses"
- "trendsNotificationManager"
- "unregisterFitnessAppBadgeCountProvider:"
- "unregisterProvider:"
- "v16@0:8"
- "v24@0:8@\"<CHFitnessAppBadgeCountProvider>\"16"
- "v24@0:8@16"
- "widgetSchedulingManager"
- "zone"

```
