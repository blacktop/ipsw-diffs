## sysdiagnosed

> `/usr/libexec/sysdiagnosed`

```diff

-1438.80.3.0.0
-  __TEXT.__text: 0x63bac
-  __TEXT.__auth_stubs: 0x16d0
-  __TEXT.__objc_stubs: 0x9340
-  __TEXT.__objc_methlist: 0x3990
-  __TEXT.__const: 0x1b4
-  __TEXT.__cstring: 0x104ea
+1438.100.33.0.0
+  __TEXT.__text: 0x64664
+  __TEXT.__auth_stubs: 0x16b0
+  __TEXT.__objc_stubs: 0x9320
+  __TEXT.__objc_methlist: 0x3e54
+  __TEXT.__const: 0x1cc
+  __TEXT.__cstring: 0x1048a
   __TEXT.__objc_classname: 0x3a4
-  __TEXT.__objc_methtype: 0x164e
-  __TEXT.__gcc_except_tab: 0x1248
-  __TEXT.__objc_methname: 0xa545
-  __TEXT.__oslogstring: 0x8d30
+  __TEXT.__objc_methtype: 0x165d
+  __TEXT.__gcc_except_tab: 0x124c
+  __TEXT.__objc_methname: 0xa529
+  __TEXT.__oslogstring: 0x8ee0
   __TEXT.__ustring: 0x4e8
-  __TEXT.__unwind_info: 0x1108
-  __DATA_CONST.__auth_got: 0xb78
-  __DATA_CONST.__got: 0x418
-  __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x1350
-  __DATA_CONST.__cfstring: 0x10b40
+  __TEXT.__unwind_info: 0x1198
+  __DATA_CONST.__auth_got: 0xb68
+  __DATA_CONST.__got: 0x3c0
+  __DATA_CONST.__auth_ptr: 0x60
+  __DATA_CONST.__const: 0x1398
+  __DATA_CONST.__cfstring: 0x10a60
   __DATA_CONST.__objc_classlist: 0x138
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x90
-  __DATA_CONST.__objc_arraydata: 0xe08
+  __DATA_CONST.__objc_arraydata: 0xda0
   __DATA_CONST.__objc_arrayobj: 0x12f0
   __DATA_CONST.__objc_intobj: 0x300
-  __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__objc_floatobj: 0x10
-  __DATA.__objc_const: 0x5be8
-  __DATA.__objc_selrefs: 0x27e8
-  __DATA.__objc_ivar: 0x46c
+  __DATA.__objc_const: 0x51f8
+  __DATA.__objc_selrefs: 0x2968
+  __DATA.__objc_ivar: 0x464
   __DATA.__objc_data: 0xc30
   __DATA.__data: 0x2c8
-  __DATA.__bss: 0x238
+  __DATA.__bss: 0x268
   - /AppleInternal/Library/Frameworks/TapToRadarKit.framework/TapToRadarKit
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsysdiagnose.dylib
   - /usr/lib/libtailspin.dylib
-  Functions: 1693
-  Symbols:   500
-  CStrings:  5205
+  Functions: 1735
+  Symbols:   497
+  CStrings:  5203
 
Symbols:
- _OBJC_CLASS_$_NSConstantDictionary
- _geteuid
- _seteuid
CStrings:
+ "--diagnostics-path"
+ "/System/Library/Frameworks/ManagedSettings.framework/managedsettingsdiagnoticstool"
+ "/private/var/tmp/manta-cores/*soc_mcu*/*soc-mcu*-panic-bkupsram.txt"
+ "/usr/bin/darwin-init"
+ "/usr/libexec/demod_helper"
+ "/usr/local/bin/exbright_tester"
+ "Added (%llu bytes)"
+ "B28@0:8i16r*20"
+ "BOOL getLongCFPrefIfSet(NSString *__strong, NSString *__strong, long *)"
+ "CSRemoteXPCProxy: Allowing remote invocation because DeviceSupportsUntrustedRemoteSysdiagnose"
+ "DarwinInitStatus"
+ "Deleted: %{public}s"
+ "DeviceSupportsUntrustedRemoteSysdiagnose"
+ "EXBrightSIL"
+ "EXBrightSILDebug.txt"
+ "Failed to create file enumerator"
+ "Failed to fetch file date for file: %{public}@ with error %{public}@"
+ "Failed to fetch file date for file: %{public}s with error %{public}@"
+ "Failed to fetch purgeable flags for '%{public}s' with err: (%d) '%{public}s'"
+ "Failed to mark '%{public}s' as purgeable (flags 0x%llx) with err: (%d) '%{public}s'"
+ "Failed to remove %{public}s, err: %{public}@"
+ "FileProvider"
+ "Found %ld files already marked as purgeable"
+ "Found %ld files; max: %ld, deleting: %ld"
+ "Leaving new file untouched: %{public}s"
+ "MCUPanicLogs"
+ "ManagedSettings"
+ "Not Found"
+ "Not clearing history since max_count is negative (%ld)"
+ "Number of process specific time-sensitive groups: %d"
+ "Partially added (%llu / %llu bytes)"
+ "Received purge request for volume '%{public}@"
+ "Returning (overridden: %{BOOL}d) val for key %{public}@: %ld"
+ "assertion failure: \"(task_get_special_port((mach_task_self_), 4, (&bootstrap_port)))\" -> %llu"
+ "assertion failure: \"[proxies count] <= 1\" -> %llu"
+ "assertion failure: \"bootstrap_check_in(bootstrap_port, \"com.apple.sysdiagnose\" \".kernel.ipc\", &server_port)\" -> %llu"
+ "assertion failure: \"init_mig_server()\" -> %llu"
+ "assertion failure: \"init_xpc_server()\" -> %llu"
+ "assertion failure: \"launchPath\" -> %llu"
+ "assertion failure: \"name\" -> %llu"
+ "assertion failure: \"self.requestSource != SDRequestSourceUnknown\" -> %llu"
+ "assertion failure: \"xpc_get_type(event) == (&_xpc_type_dictionary)\" -> %llu"
+ "clearHistory unsupported on this config. Manual override: %{BOOL}d"
+ "darwin_init_status.txt"
+ "deleter_ttl"
+ "deletion-max-age-days"
+ "deletion-max-count"
+ "deletion-min-age-minutes"
+ "fileIsMarkedPurgeable:fileName:"
+ "fileproviderctl_diagnose.log"
+ "getManagedSettingsContainer"
+ "helper"
+ "logs/EXBrightSILDebug"
+ "logs/MCUPanics"
+ "logs/ManagedSettings"
+ "managed_settings_diagnostic_tool_stdout.txt"
+ "markFileAsPurgeable:alreadyMarkedPurgeable:"
+ "silDebug"
- "\nShould run full idstool dump: %s\n\n"
- "<TMPOUTPUTDIR>/fileproviderctl_dump.log"
- "A preference was found! Domain %@ with variable %@"
- "APSWriteLogs"
- "Added"
- "CallLogging"
- "Could not drop to mobile with error: %s"
- "Could not return to original euid with error: %s"
- "Error removing '%@': %@"
- "Failed to mark '%{public}s' as purgeable with error %d (%{public}s) (flags 0x%llx)"
- "Found %ld files in history with max of %ld"
- "IDSLogging"
- "IMLoggingAgent"
- "MadridLogging"
- "NotFound"
- "Number of process specific time-sensitive groups: %lu"
- "PCWriteLogs"
- "Partially Added"
- "Received purge request for volume '%{public}@. Skipping"
- "RegistrationLogging"
- "Removing '%@' at index '%lu'"
- "TB,V_shouldRunIDSDump"
- "Tq,V_maxHistory"
- "TransportLogging"
- "VerboseCallLogging"
- "VisualVoicemailLogging"
- "_maxHistory"
- "_shouldRunIDSDump"
- "assertion failure: \"(task_get_special_port((mach_task_self_), 4, (&bootstrap_port)))\" -> %lld"
- "assertion failure: \"[proxies count] <= 1\" -> %lld"
- "assertion failure: \"bootstrap_check_in(bootstrap_port, \"com.apple.sysdiagnose\" \".kernel.ipc\", &server_port)\" -> %lld"
- "assertion failure: \"init_mig_server()\" -> %lld"
- "assertion failure: \"init_xpc_server()\" -> %lld"
- "assertion failure: \"launchPath\" -> %lld"
- "assertion failure: \"name\" -> %lld"
- "assertion failure: \"self.requestSource != SDRequestSourceUnknown\" -> %lld"
- "assertion failure: \"xpc_get_type(event) == (&_xpc_type_dictionary)\" -> %lld"
- "availability"
- "com.apple.applepushservice"
- "com.apple.logging"
- "com.apple.persistentconnection"
- "current"
- "maxHistory"
- "setMaxHistory:"
- "setShouldRunIDSDump:"
- "shouldRunIDSDump"

```
