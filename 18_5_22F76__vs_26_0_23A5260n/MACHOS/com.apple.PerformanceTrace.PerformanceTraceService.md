## com.apple.PerformanceTrace.PerformanceTraceService

> `/System/Library/PrivateFrameworks/PerformanceTrace.framework/XPCServices/com.apple.PerformanceTrace.PerformanceTraceService.xpc/com.apple.PerformanceTrace.PerformanceTraceService`

```diff

-218.2.0.0.0
-  __TEXT.__text: 0xc6d0
-  __TEXT.__auth_stubs: 0x950
-  __TEXT.__objc_stubs: 0x17a0
-  __TEXT.__objc_methlist: 0x7a0
-  __TEXT.__const: 0x11c
-  __TEXT.__gcc_except_tab: 0x34c
-  __TEXT.__objc_methname: 0x1901
-  __TEXT.__oslogstring: 0xc5f
-  __TEXT.__cstring: 0x1737
-  __TEXT.__objc_classname: 0xb9
-  __TEXT.__objc_methtype: 0x448
-  __TEXT.__unwind_info: 0x218
-  __DATA_CONST.__auth_got: 0x4b8
-  __DATA_CONST.__got: 0x140
-  __DATA_CONST.__const: 0x6f0
-  __DATA_CONST.__cfstring: 0x13c0
+234.0.0.0.0
+  __TEXT.__text: 0xe664
+  __TEXT.__auth_stubs: 0x9b0
+  __TEXT.__objc_stubs: 0x1940
+  __TEXT.__objc_methlist: 0x7ec
+  __TEXT.__const: 0x138
+  __TEXT.__gcc_except_tab: 0x3e0
+  __TEXT.__cstring: 0x1c77
+  __TEXT.__oslogstring: 0xeaa
+  __TEXT.__dlopen_cstrs: 0x59
+  __TEXT.__objc_classname: 0xbc
+  __TEXT.__objc_methname: 0x1aed
+  __TEXT.__objc_methtype: 0x459
+  __TEXT.__unwind_info: 0x2b8
+  __DATA_CONST.__auth_got: 0x4e8
+  __DATA_CONST.__got: 0x110
+  __DATA_CONST.__const: 0x868
+  __DATA_CONST.__cfstring: 0x16c0
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA_CONST.__objc_intobj: 0x150
+  __DATA_CONST.__objc_intobj: 0x168
   __DATA_CONST.__objc_arraydata: 0xb0
   __DATA_CONST.__objc_arrayobj: 0xf0
-  __DATA.__objc_const: 0xb48
-  __DATA.__objc_selrefs: 0x708
-  __DATA.__objc_ivar: 0x8c
+  __DATA.__objc_const: 0xba0
+  __DATA.__objc_selrefs: 0x778
+  __DATA.__objc_ivar: 0x90
   __DATA.__objc_data: 0xa0
   __DATA.__data: 0x300
-  __DATA.__bss: 0x8
+  __DATA.__bss: 0x90
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
-  - /System/Library/Frameworks/UserNotifications.framework/UserNotifications
   - /System/Library/PrivateFrameworks/LoggingSupport.framework/LoggingSupport
+  - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/kperf.framework/kperf
   - /System/Library/PrivateFrameworks/ktrace.framework/ktrace
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
-  UUID: 30F53D87-2788-310D-A66E-B0CFC8B5FF9F
-  Functions: 231
-  Symbols:   210
-  CStrings:  782
+  UUID: 6C66FF96-B68C-32A4-9C05-2F02CA5B2A82
+  Functions: 288
+  Symbols:   229
+  CStrings:  883
 
Symbols:
+ _OBJC_CLASS_$_NSAssertionHandler
+ _PTDefaultTraceDirectoryAvailableTraceFileURLs
+ _PTServicesCreateTraceDirectory
+ _PTServicesDeveloperModeIsEnabled
+ _PTServicesDeviceIsInternal
+ _PTServicesMarkPurgeableMediumUrgency
+ _PTServicesPostStateDidChangeNotification
+ _PTServicesSendUserNotification
+ _PTServicesSetFilePosixPermissions
+ __fileAttributes
+ __sl_dlopen
+ _dispatch_once
+ _kPTControlCenterModulePrefsDomainName
+ _kPTControlCenterPrefsAvailableKeyName
+ _kPTControlCenterPrefsCustomTracePlanArgumentsPreferenceKeyName
+ _kPTControlCenterPrefsDomainName
+ _kPTControlCenterPrefsSelectedTracePlanNamePreferenceKeyName
+ _kPTPassiveTracePlanNameLightweightPowerMetrics
+ _kPTPassiveTracePlanNamePassive
+ _kPTTracePlanNameCustom
+ _kPTTracePlanNameDefault
+ _kPTTracePlanNameProfile
+ _objc_destroyWeak
+ _objc_getClass
+ _objc_loadWeakRetained
+ _objc_release_x1
+ _objc_storeWeak
+ _os_log_create
- _OBJC_CLASS_$_UNMutableNotificationContent
- _OBJC_CLASS_$_UNNotificationAction
- _OBJC_CLASS_$_UNNotificationActionIcon
- _OBJC_CLASS_$_UNNotificationCategory
- _OBJC_CLASS_$_UNNotificationRequest
- _OBJC_CLASS_$_UNUserNotificationCenter
- __os_log_default
- _objc_retain_x23
- _objc_retain_x25
CStrings:
+ "%s"
+ "(Legacy) Trace collected with final path: %{public}@"
+ "@48@0:8@16@24@32^@40"
+ "A"
+ "An error occurred getting recording state."
+ "Class getUNMutableNotificationContentClass(void)_block_invoke"
+ "Class getUNNotificationActionClass(void)_block_invoke"
+ "Class getUNNotificationActionIconClass(void)_block_invoke"
+ "Class getUNNotificationCategoryClass(void)_block_invoke"
+ "Class getUNNotificationRequestClass(void)_block_invoke"
+ "Class getUNUserNotificationCenterClass(void)_block_invoke"
+ "Client"
+ "ControlCenterPerformanceTraceCustomTracePlanArguments"
+ "ControlCenterPerformanceTraceIsAvailable"
+ "ControlCenterPerformanceTraceSelectedTracePlanName"
+ "Developer mode is %{public}@"
+ "Failed to post notification for new global state change. Status: %{public}#x"
+ "Failed to read developer mode status: %{darwin.errno}d"
+ "Failed to update POSIX permissions of trace file"
+ "Getting recording state config"
+ "Got recording state: %{public}@"
+ "Not Recording"
+ "Not recording"
+ "PerformanceTraceService"
+ "Posted global state change notification"
+ "Received and accepted new connection from %{public}@ [%d]"
+ "Recording"
+ "SharedServiceFunctionality"
+ "StateChangeNotification"
+ "T@\"NSXPCConnection\",W,V_recordingConnectionPointer"
+ "TB,R,N,V_isInRecordingWorkflow"
+ "Trace collected with final path: %{public}@"
+ "Trace directory is not a directory"
+ "Tried to send a user notification in an unsupported environment"
+ "UNMutableNotificationContent"
+ "UNNotificationAction"
+ "UNNotificationActionIcon"
+ "UNNotificationCategory"
+ "UNNotificationRequest"
+ "UNUserNotificationCenter"
+ "Unable to find class %s"
+ "Updated recording status to '%s'"
+ "UserNotifications.framework is soft-linked and unavailable; Performance Trace cannot post notifications"
+ "UserNotifications_SoftLinking.h"
+ "XPC connection interrupted to %{public}@ [%d]"
+ "XPC connection invalidated to %{public}@ [%d]"
+ "_isInRecordingWorkflow"
+ "_recordingConnectionPointer"
+ "_traceRecordArgsArrayFromConfig:outputFilePath:xpcConnection:error:"
+ "_updateRecordingStatus:"
+ "aar"
+ "atrc"
+ "com.apple.PerformanceTrace.ControlCenterPrefs"
+ "com.apple.control-center.PerformanceTraceModule"
+ "com.apple.performancetrace.global_state_did_change"
+ "contentsOfDirectoryAtURL:includingPropertiesForKeys:options:error:"
+ "currentConnection"
+ "currentHandler"
+ "custom"
+ "default"
+ "disabled"
+ "enabled"
+ "fileExistsAtPath:isDirectory:"
+ "handleFailureInFunction:file:lineNumber:description:"
+ "hasDirectoryPath"
+ "initFileURLWithPath:"
+ "isInRecordingWorkflow"
+ "isInRecordingWorkflow:"
+ "lightweight power metrics"
+ "numberWithBool:"
+ "passive"
+ "passiveTraceError:description:"
+ "pathExtension"
+ "prefs:root=DEVELOPER_SETTINGS&path=PERFORMANCE_TRACE"
+ "profile"
+ "recordingConnectionPointer"
+ "security.mac.amfi.developer_mode_status"
+ "setRecordingConnectionPointer:"
+ "softlink:o:path:/System/Library/Frameworks/UserNotifications.framework/UserNotifications"
+ "tgz"
+ "v20@?0B8@\"NSError\"12"
+ "v24@0:8@?<v@?B@\"NSError\">16"
+ "void *UserNotificationsLibrary(void)"
- "@40@0:8@16@24^@32"
- "B32@0:8@16Q24"
- "T@\"NSXPCConnection\",R,N,V_connection"
- "UserNotifications.framework is weak-linked and unavailable; Performance Trace cannot post notifications"
- "_markPurgable:withUrgency:"
- "_traceRecordArgsArrayFromConfig:outputFilePath:error:"

```
