## sysdiagnosed

> `/usr/libexec/sysdiagnosed`

```diff

-1438.80.3.0.0
-  __TEXT.__text: 0x61e48
-  __TEXT.__auth_stubs: 0x1400
-  __TEXT.__objc_stubs: 0x8020
-  __TEXT.__objc_methlist: 0x341c
-  __TEXT.__const: 0x1e4
-  __TEXT.__cstring: 0xe509
-  __TEXT.__oslogstring: 0x7b52
+1438.100.41.0.0
+  __TEXT.__text: 0x636d8
+  __TEXT.__auth_stubs: 0x1420
+  __TEXT.__objc_stubs: 0x8160
+  __TEXT.__objc_methlist: 0x3774
+  __TEXT.__const: 0x1fc
+  __TEXT.__cstring: 0xe58b
+  __TEXT.__oslogstring: 0x7ee3
   __TEXT.__objc_classname: 0x336
-  __TEXT.__objc_methtype: 0xdd2
-  __TEXT.__gcc_except_tab: 0x122c
-  __TEXT.__objc_methname: 0x8a2f
-  __TEXT.__unwind_info: 0xf70
-  __DATA_CONST.__auth_got: 0xa10
-  __DATA_CONST.__got: 0x380
-  __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x10b8
-  __DATA_CONST.__cfstring: 0xf900
+  __TEXT.__objc_methtype: 0xde1
+  __TEXT.__gcc_except_tab: 0x1230
+  __TEXT.__objc_methname: 0x8b33
+  __TEXT.__unwind_info: 0x1018
+  __DATA_CONST.__auth_got: 0xa20
+  __DATA_CONST.__got: 0x328
+  __DATA_CONST.__auth_ptr: 0x60
+  __DATA_CONST.__const: 0x1140
+  __DATA_CONST.__cfstring: 0xf940
   __DATA_CONST.__objc_classlist: 0x128
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x90
-  __DATA_CONST.__objc_arraydata: 0x12a8
+  __DATA_CONST.__objc_arraydata: 0x1230
   __DATA_CONST.__objc_arrayobj: 0x1788
   __DATA_CONST.__objc_intobj: 0x228
-  __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0x4fc0
-  __DATA.__objc_selrefs: 0x2280
+  __DATA.__objc_const: 0x4990
+  __DATA.__objc_selrefs: 0x2350
   __DATA.__objc_ivar: 0x3fc
   __DATA.__objc_data: 0xb90
   __DATA.__data: 0x1a0
-  __DATA.__bss: 0x1a0
+  __DATA.__bss: 0x1d0
   __CGPreLoginApp.__cgpreloginapp: 0x0
   - /AppleInternal/Library/Frameworks/TapToRadarKit.framework/Versions/A/TapToRadarKit
   - /System/Library/Frameworks/CoreBluetooth.framework/Versions/A/CoreBluetooth

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsysdiagnose.dylib
   - /usr/lib/libtailspin.dylib
-  UUID: 6D1E9B9A-7F9C-3A48-910D-B5D52C08C7FF
-  Functions: 1536
-  Symbols:   436
-  CStrings:  6601
+  UUID: FB038AE0-C5B1-350B-AD8D-3B19CFD08C89
+  Functions: 1580
+  Symbols:   437
+  CStrings:  6636
 
Symbols:
+ _MGGetBoolAnswer
+ _os_parse_boot_arg_int
- _OBJC_CLASS_$_NSConstantDictionary
CStrings:
+ "--diagnostics-path"
+ "--path"
+ "/Library/Apple/usr/libexec/demod_helper"
+ "/System/Library/Frameworks/ManagedSettings.framework/managedsettingsdiagnoticstool"
+ "/usr/bin/darwin-init"
+ "/usr/local/bin/wifi_sysdiagnose.sh"
+ "Added (%llu bytes)"
+ "B28@0:8i16r*20"
+ "CSRemoteXPCProxy: Allowing remote invocation because DeviceSupportsUntrustedRemoteSysdiagnose"
+ "CoreBrightness"
+ "DarwinInitStatus"
+ "Deleted: %{public}s"
+ "DeviceSupportsUntrustedRemoteSysdiagnose"
+ "Failed to create file enumerator"
+ "Failed to fetch file date for file: %{public}@ with error %{public}@"
+ "Failed to fetch file date for file: %{public}s with error %{public}@"
+ "Failed to fetch purgeable flags for '%{public}s' with err: (%d) '%{public}s'"
+ "Failed to mark '%{public}s' as purgeable (flags 0x%llx) with err: (%d) '%{public}s'"
+ "Failed to remove %{public}s, err: %{public}@"
+ "FileProvider"
+ "Found %ld files already marked as purgeable"
+ "Found %ld files; max: %ld, deleting: %ld"
+ "Found nil home dir for uid %u - skipping RMD container's user scope"
+ "Leaving new file untouched: %{public}s"
+ "ManagedSettings"
+ "Not Found"
+ "Not clearing history since max_count is negative (%ld)"
+ "Number of process specific time-sensitive groups: %d"
+ "Partially added (%llu / %llu bytes)"
+ "Received purge request for volume '%{public}@"
+ "Returning (overridden: %{BOOL}d) val for key %{public}@: %ld"
+ "Skipping wifi dext log collection"
+ "TASK_TYPE_SYSCTL"
+ "TB,V_collectWifiDextCoreFiles"
+ "Task returned error (%d): %{public}s"
+ "Task timed out after %lf duration: %{public}s"
+ "_collectWifiDextCoreFiles"
+ "assertion failure: \"(task_get_special_port((mach_task_self_), 4, (&bootstrap_port)))\" -> %llu"
+ "assertion failure: \"[proxies count] <= 1\" -> %llu"
+ "assertion failure: \"bootstrap_check_in(bootstrap_port, \"com.apple.sysdiagnose\" \".kernel.ipc\", &server_port)\" -> %llu"
+ "assertion failure: \"init_mig_server()\" -> %llu"
+ "assertion failure: \"init_xpc_server()\" -> %llu"
+ "assertion failure: \"launchPath\" -> %llu"
+ "assertion failure: \"name\" -> %llu"
+ "assertion failure: \"xpc_get_type(event) == (&_xpc_type_dictionary)\" -> %llu"
+ "clearHistory"
+ "clearHistory unsupported on this config. Manual override: %{BOOL}d"
+ "cli argument passed - running wifi dext log collection"
+ "collectWifiDextCoreFiles"
+ "darwin_init_status.txt"
+ "deleter_ttl"
+ "deletion-max-age-days"
+ "deletion-max-count"
+ "deletion-min-age-minutes"
+ "diagnostics"
+ "errors/wifi_dext_errors.txt"
+ "fileIsMarkedPurgeable:fileName:"
+ "fileproviderctl_diagnose.log"
+ "getManagedSettingsContainer"
+ "getWifiDextCorefilesContainer"
+ "helper"
+ "logs/CoreBrightness"
+ "logs/ManagedSettings"
+ "logs/wifi_dext_core_files"
+ "managed_settings_diagnostic_tool_stdout.txt"
+ "markFileAsPurgeable:alreadyMarkedPurgeable:"
+ "q24@?0@\"NSURL\"8@\"NSURL\"16"
+ "removeItemAtURL:error:"
+ "setCollectWifiDextCoreFiles:"
+ "shouldRunWifiDextCoreFilesCollection"
+ "sortUsingComparator:"
+ "status-info-internal"
+ "status_info.plist"
+ "wifi dext core files"
+ "wlan.dk"
+ "wlan.dk boot arg set - running wifi dext log collection"
- "\nShould run full idstool dump: %s\n\n"
- "<TMPOUTPUTDIR>/fileproviderctl_dump.log"
- "A preference was found! Domain %@ with variable %@"
- "APSWriteLogs"
- "Added"
- "CallLogging"
- "Failed to mark '%{public}s' as purgeable with error %d (%{public}s) (flags 0x%llx)"
- "IDSLogging"
- "IMLoggingAgent"
- "MadridLogging"
- "NotFound"
- "Number of process specific time-sensitive groups: %lu"
- "PCWriteLogs"
- "Partially Added"
- "Received purge request for volume '%{public}@. Skipping"
- "RegistrationLogging"
- "TB,V_shouldRunIDSDump"
- "TransportLogging"
- "VerboseCallLogging"
- "VisualVoicemailLogging"
- "_shouldRunIDSDump"
- "assertion failure: \"(task_get_special_port((mach_task_self_), 4, (&bootstrap_port)))\" -> %lld"
- "assertion failure: \"[proxies count] <= 1\" -> %lld"
- "assertion failure: \"bootstrap_check_in(bootstrap_port, \"com.apple.sysdiagnose\" \".kernel.ipc\", &server_port)\" -> %lld"
- "assertion failure: \"init_mig_server()\" -> %lld"
- "assertion failure: \"init_xpc_server()\" -> %lld"
- "assertion failure: \"launchPath\" -> %lld"
- "assertion failure: \"name\" -> %lld"
- "assertion failure: \"xpc_get_type(event) == (&_xpc_type_dictionary)\" -> %lld"
- "availability"
- "com.apple.applepushservice"
- "com.apple.logging"
- "com.apple.persistentconnection"
- "current"
- "setShouldRunIDSDump:"
- "shouldRunIDSDump"

```
