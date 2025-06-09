## sysdiagnosed

> `/usr/libexec/sysdiagnosed`

```diff

-1438.120.9.0.0
-  __TEXT.__text: 0x64be4
+1512.0.0.0.0
+  __TEXT.__text: 0x64f14
   __TEXT.__auth_stubs: 0x16b0
-  __TEXT.__objc_stubs: 0x9320
-  __TEXT.__objc_methlist: 0x3e54
-  __TEXT.__const: 0x1cc
-  __TEXT.__cstring: 0x106c9
-  __TEXT.__objc_classname: 0x3a4
+  __TEXT.__objc_stubs: 0x93a0
+  __TEXT.__objc_methlist: 0x3e9c
+  __TEXT.__const: 0x1c4
+  __TEXT.__cstring: 0x1067f
+  __TEXT.__objc_classname: 0x3a7
   __TEXT.__objc_methtype: 0x165d
-  __TEXT.__gcc_except_tab: 0x124c
-  __TEXT.__objc_methname: 0xa529
-  __TEXT.__oslogstring: 0x8f04
+  __TEXT.__gcc_except_tab: 0x1268
+  __TEXT.__objc_methname: 0xa5a9
+  __TEXT.__oslogstring: 0x8f10
   __TEXT.__ustring: 0x4e8
   __TEXT.__unwind_info: 0x1190
   __DATA_CONST.__auth_got: 0xb68
   __DATA_CONST.__got: 0x3c0
   __DATA_CONST.__auth_ptr: 0x60
-  __DATA_CONST.__const: 0x13a0
-  __DATA_CONST.__cfstring: 0x10d80
+  __DATA_CONST.__const: 0x13b0
+  __DATA_CONST.__cfstring: 0x11000
   __DATA_CONST.__objc_classlist: 0x138
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x90
-  __DATA_CONST.__objc_arraydata: 0xdc0
-  __DATA_CONST.__objc_arrayobj: 0x1338
+  __DATA_CONST.__objc_arraydata: 0xe30
+  __DATA_CONST.__objc_arrayobj: 0x1368
   __DATA_CONST.__objc_intobj: 0x300
   __DATA_CONST.__objc_floatobj: 0x10
-  __DATA.__objc_const: 0x51f8
-  __DATA.__objc_selrefs: 0x2968
-  __DATA.__objc_ivar: 0x464
+  __DATA.__objc_const: 0x5270
+  __DATA.__objc_selrefs: 0x2990
+  __DATA.__objc_ivar: 0x46c
   __DATA.__objc_data: 0xc30
-  __DATA.__data: 0x2c8
-  __DATA.__bss: 0x268
+  __DATA.__data: 0x2d0
+  __DATA.__bss: 0x270
   - /AppleInternal/Library/Frameworks/TapToRadarKit.framework/TapToRadarKit
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsysdiagnose.dylib
   - /usr/lib/libtailspin.dylib
-  UUID: 549A6761-BC88-3DE2-98E4-84FE18D04341
-  Functions: 1736
+  UUID: 39178E2C-037A-3019-B021-5A19C3F9578E
+  Functions: 1751
   Symbols:   497
-  CStrings:  7366
+  CStrings:  7418
 
CStrings:
+ "%lld"
+ "%llu KB"
+ "%llu MB"
+ "%s target uid to %u for: '%@'"
+ "--last"
+ "--top"
+ "/System/Library/Frameworks/Accounts.framework/Support/acdiagnose"
+ "/private/var/db/accessoryupdater/uarpd/pcapfiles"
+ "/private/var/mobile/Library/Logs/com.apple.StoreServices/HTTPArchives/*.har"
+ "/usr/appleinternal/bin/mediaremotetool"
+ "/usr/appleinternal/bin/suggest_tool"
+ "20"
+ "96"
+ "ACDiagnose"
+ "Atomic"
+ "BackgroundPowerlog"
+ "BatteryHealth"
+ "CloudKitPreferences"
+ "CoreRepair"
+ "EXTENDED_ERROR_DATA"
+ "Error"
+ "Failed to set"
+ "Filesystem"
+ "GEAvailability"
+ "GMSSelfService"
+ "HH:mm:ss"
+ "HIDCrashlogs"
+ "IntelligencePlatform"
+ "Locker"
+ "MAAutoAsset_{%@}_History"
+ "OSEligibility"
+ "ProactiveInputPredictions"
+ "PushNotification"
+ "Received xpc termination for peer"
+ "ReportMemoryExceptions"
+ "ReportMemoryExceptionsListLogs"
+ "Request (%d) not implemented"
+ "SELF.lastPathComponent ENDSWITH '.%@'"
+ "Scheduler"
+ "Secure"
+ "Set"
+ "SiriEnrollment"
+ "Stager"
+ "StoreServices"
+ "T@\"NSDate\",C,V_oldestDateCreatedCutoff"
+ "T@\"NSDate\",C,V_startDiagnosticTime"
+ "T@\"NSString\",C,V_clientName"
+ "TASK_TYPE_ESIM_SETUP"
+ "Tq,V_clientPID"
+ "UnifiedAssetLogs"
+ "_clientName"
+ "_clientPID"
+ "_task"
+ "acdiagnose.txt"
+ "activitySummary"
+ "clientName"
+ "compression-level=6"
+ "compute"
+ "eSIMSetup"
+ "error-"
+ "getDarwinInitStatusContainer"
+ "getMiscInternalLogsContainer"
+ "gms_self_service.json"
+ "gms_self_service.txt"
+ "launched by %@ [%@] at %@"
+ "launchedByString"
+ "logs/dastool/dastool_activity_summary.txt"
+ "logs/eSIMSetup"
+ "requests"
+ "self-service"
+ "setClientName:"
+ "setClientPID:"
+ "swtransparency.log"
+ "sysdiagnose cli"
+ "unexpected peer event with type %s"
+ "zOrderIndex"
- "%@_%@"
- "%lu KB"
- "%lu MB"
- "/System/Library/PrivateFrameworks/CoreSuggestions.framework/Tools/suggest_tool"
- "/private/var/mobile/Library/Logs/com.apple.StoreServices/HTTPArchives"
- "/usr/local/bin/accounts_tool"
- "/usr/local/bin/mediaremotetool"
- "AudioAccessory"
- "Failed to set target uid when launching SDTask."
- "HomePod"
- "Log Generation start\n"
- "MAAutoAsset_{Filesystem,Locker,Atomic,Error,Secure,Stager,Scheduler}_History"
- "Remote device not found"
- "Remote sysdiagnose service not found on the attached device"
- "Request not implemented"
- "SELF.lastPathComponent ENDSWITH '%@'"
- "STDERR"
- "STDOUT"
- "T@\"NSDate\",V_oldestDateCreatedCutoff"
- "T@\"NSDate\",V_startDiagnosticTime"
- "TASK_TYPE_AWD"
- "accounts_list.txt"
- "compression-level=1"
- "dastool_evaluate_all_activities.txt"
- "evaluateallactivities"
- "getStoreServicesContainer"
- "getmiscInternalLogsContainer"
- "har"
- "isExecutableFileAtPath:"
- "listAccounts"
- "logs/AWD"
- "logs/swtransparency.log"
- "pathExtension IN %@"
- "unexpected peer event"

```
