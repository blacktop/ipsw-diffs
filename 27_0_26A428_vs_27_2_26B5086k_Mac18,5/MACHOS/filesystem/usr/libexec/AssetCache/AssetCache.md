## AssetCache

> `/usr/libexec/AssetCache/AssetCache`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-265.0.0.0.0
-  __TEXT.__text: 0x1e2b8c
-  __TEXT.__auth_stubs: 0x10e0
-  __TEXT.__objc_stubs: 0xfce0
-  __TEXT.__objc_methlist: 0x6b24
-  __TEXT.__cstring: 0x8737
+265.40.2.0.0
+  __TEXT.__text: 0x1e315c
+  __TEXT.__auth_stubs: 0x10d0
+  __TEXT.__objc_stubs: 0xff20
+  __TEXT.__objc_methlist: 0x6b8c
+  __TEXT.__cstring: 0x88ec
   __TEXT.__const: 0x3ade0
   __TEXT.__gcc_except_tab: 0x2a88
-  __TEXT.__objc_methname: 0x127d5
-  __TEXT.__oslogstring: 0x7f1d
+  __TEXT.__objc_methname: 0x129b5
+  __TEXT.__oslogstring: 0x80db
   __TEXT.__objc_classname: 0x3b6
-  __TEXT.__objc_methtype: 0x21b3
+  __TEXT.__objc_methtype: 0x21ce
   __TEXT.__ustring: 0x19e
-  __TEXT.__unwind_info: 0x2250
+  __TEXT.__unwind_info: 0x2298
   __TEXT.__eh_frame: 0xc0
-  __DATA_CONST.__const: 0xb2e0
+  __DATA_CONST.__const: 0xb330
   __DATA_CONST.__cfstring: 0x9120
   __DATA_CONST.__objc_classlist: 0x138
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x128
-  __DATA_CONST.__objc_intobj: 0x3f0
+  __DATA_CONST.__objc_intobj: 0x3a8
   __DATA_CONST.__objc_arraydata: 0x1090
   __DATA_CONST.__objc_arrayobj: 0x4b0
   __DATA_CONST.__objc_dictobj: 0x910
-  __DATA_CONST.__auth_got: 0x880
-  __DATA_CONST.__got: 0x910
+  __DATA_CONST.__auth_got: 0x878
+  __DATA_CONST.__got: 0x920
   __DATA_CONST.__auth_ptr: 0x18
-  __DATA.__objc_const: 0xcaf0
-  __DATA.__objc_selrefs: 0x4390
+  __DATA.__objc_const: 0xcb20
+  __DATA.__objc_selrefs: 0x4420
   __DATA.__objc_ivar: 0xaa0
   __DATA.__objc_data: 0xc30
   __DATA.__data: 0xd18

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3465
-  Symbols:   579
-  CStrings:  5710
+  Functions: 3480
+  Symbols:   580
+  CStrings:  5739
 
Symbols:
+ _OBJC_CLASS_$_AssetCacheConfiguration
+ _OBJC_CLASS_$_AssetCacheSettingsMissingAlert
+ _fwrite
- _CFPreferencesAppValueIsForced
- _CFPreferencesCopyAppValue
CStrings:
+ "(version 1)\n(deny default)\n(import \"system.sb\")\n(system-network)\n\n; don't spam logs with these denials\n(deny file-read*\n  (subpath \"/Users\")\n  (regex #\"/Library/Keychains/login\\.keychain\")\n  (with no-log))\n(deny file-write*\n  (regex #\"/Library/Caches/AssetCache\")\n  (with no-log))\n(deny mach-lookup\n  (global-name \"com.apple.cookied\")\n  (global-name \"com.apple.network.EAPOLController\")\n  (with no-log))\n(deny system-socket\n  (require-all\n    (socket-domain AF_SYSTEM)\n    (socket-protocol 1)) ; SYSPROTO_EVENT\n  (with no-log))\n\n(allow file-read*\n  (subpath \"/usr/libexec/AssetCache\")\n  (subpath \"/System\")\n  (subpath (param \"PROGRAM_PATH\"))\t\t; subpath for resource fork\n  (subpath (param \"DATA_PATH\"))\n  (subpath (param \"LOG_PATH\"))\n  (subpath (param \"METRICS_PATH\"))\n  (subpath (param \"PREFS_PATH\"))\n  (literal \"/Library/Keychains/System.keychain\")\n  (literal \"/Library/Application Support/CrashReporter/SubmitDiagInfo.domains\")\n  (subpath \"/Library/Managed Preferences\")\n  (subpath \"/Library/Preferences\")\n  (subpath \"/Library/Caching\")\n  (literal \"/private\")\n  (regex #\"^/(private/)?(etc|tmp|var)($|/)\")\n  (regex #\"/Library/Server/Caching/Data($|/)\")\t; for absorbing\n  (regex #\"/Library/Application Support/Apple/AssetCache/Data($|/)\"))\t; for absorbing\n\n(allow file-read-metadata\n  (literal \"/\")\n  (subpath \"/Library\")\n  (literal \"/Applications\")\n  (literal \"/private\")\n  (regex #\"^/(private/)?(etc|tmp|var)($|/)\")\n  (literal \"/var\")\n  (regex #\"/\\.TemporaryItems\")\n  (literal %@))\n\n(allow file-write*\n  (subpath \"/Library/Caching\")\n  (subpath \"/private/var/folders\")\n  (regex #\"/\\.TemporaryItems\")\n  (regex #\"/Library/Server/Caching/Data($|/)\")\t; for destructive absorbing\n  (regex #\"/Library/Application Support/Apple/AssetCache/Data($|/)\")\t; for destructive absorbing\n  (subpath (param \"DATA_PATH\"))\n  (subpath (param \"LOG_PATH\"))\n  (subpath (param \"METRICS_PATH\"))\n  (subpath (param \"PREFS_PATH\")))\n\n(allow file-write-data\n  (literal \"/private/var/db/mds/system/mds.lock\"))\n\n(allow file-read* file-write*\n  (subpath \"/private/var/db/mds/system\"))\n\n(when (param \"DATA_MIGRATION_FROM_PATH\")\n  (allow file-read* file-write*\n    (subpath (param \"DATA_MIGRATION_FROM_PATH\"))))\n(when (param \"DATA_MIGRATION_TO_PATH\")\n  (allow file-read* file-write*\n    (subpath (param \"DATA_MIGRATION_TO_PATH\"))))\n\n; the copy of the settings we export for legacy readers.  /Library/Preferences belongs to root, so only\n; the file itself is writable and only in place -- we cannot replace it.\n(when (param \"LEGACY_PREFS_PATH\")\n  (allow file-write*\n    (literal (param \"LEGACY_PREFS_PATH\"))))\n\n(allow ipc-posix-shm\n  (ipc-posix-name \"com.apple.AppleDatabaseChanged\")\n  (ipc-posix-name \"apple.shm.notification_center\"))\n\n(allow mach-per-user-lookup)\n\n(allow mach-lookup\n  (global-name \"com.apple.AssetCacheTetheratorService\")\n  (global-name \"com.apple.DiskArbitration.diskarbitrationd\")\n  (global-name \"com.apple.SecurityServer\")\n  (global-name \"com.apple.SystemConfiguration.configd\")\n  (global-name \"com.apple.cfnetwork.cfnetworkagent\")\n  (global-name \"com.apple.lsd.mapdb\")\n  (global-name \"com.apple.metadata.mds\")\n  (global-name \"com.apple.ocspd\")\n  (global-name \"com.apple.system.opendirectoryd.membership\")\n  (global-name \"com.apple.securityd.xpc\")\n  (global-name \"com.apple.securityd.systemkeychain\")\n  (global-name \"com.apple.wifi.anqp\"))\n\n(allow network-outbound)\n\n(allow signal (target self))\n\n(allow system-fsctl\n  (fsctl-command (_IO \"h\" 47)))    ; HFSIOC_SET_HOTFILE_STATE\n\n(allow file-read* file-write*\n  (literal \"/private/var/run/com.apple.AssetCache/LastAlerts.plist\"))\n\n(allow mach-lookup\n  (global-name-regex #\"^com\\.apple\\.distributed_notifications\"))\n(allow distributed-notification-post)\n\n(allow iokit-open\n  (iokit-user-client-class \"RootDomainUserClient\"))\n(allow mach-lookup\n  (global-name \"com.apple.PowerManagement.control\"))\n\n(allow mach-lookup\n  (global-name \"com.apple.AssetCacheManagerService\"))\n\n(allow mach-lookup\n  (global-name \"com.apple.apsd\")\n  (global-name \"com.apple.applepushserviced\")\n  (global-name \"com.apple.AssetCacheLocatorService\"))\n\n(allow mach-lookup\n  (global-name \"com.apple.cache_delete\"))\n"
+ "265.40.2"
+ "@\"AssetCacheConfiguration\""
+ "B24@?0@\"NSMutableDictionary\"8^@16"
+ "Cannot reach the settings container and waiting will not help; see the AssetCacheServices Configuration log for why"
+ "Cannot sandbox: the settings container could not be resolved"
+ "LEGACY_PREFS_PATH"
+ "T@\"AssetCacheConfiguration\",&,V_configuration"
+ "T@\"NSString\",R"
+ "TB,R"
+ "Timed out waiting for the settings container to be created"
+ "Unable to resolve the settings container; waiting for AssetCacheManagerService to create it\n"
+ "Unable to save preferences to %@: %@"
+ "Unable to update the legacy copy of the preferences: %@"
+ "Waiting for AssetCacheManagerService to create the settings container"
+ "_configuration"
+ "configOnSameSettings"
+ "containerPath"
+ "containerUnavailablePermanently"
+ "defaultSettings"
+ "exportSettingsToLegacyLocationWithError:"
+ "initWithConfiguration:URL:queue:queueIdentityKey:"
+ "isManagedByDDM"
+ "manageablePreferenceKeys"
+ "mdmManageableKeys"
+ "policyFlagForKey:consideringLocalPrefs:"
+ "prefsContainerPath"
+ "prefsContainerUnavailablePermanently"
+ "realpath(%s) failed: %s; the legacy copy of the preferences will not be updated"
+ "setConfiguration:"
+ "setMetricsCollectionEnabled:"
+ "settings"
+ "settingsPath"
+ "sharedConfiguration"
+ "updateSettingsWithBlock:error:"
+ "v16@?0@\"NSMutableDictionary\"8"
+ "wait4SettingsContainerWithTimeout:"
- "(version 1)\n(deny default)\n(import \"system.sb\")\n(system-network)\n\n; don't spam logs with these denials\n(deny file-read*\n  (subpath \"/Users\")\n  (regex #\"/Library/Keychains/login\\.keychain\")\n  (with no-log))\n(deny file-write*\n  (regex #\"/Library/Caches/AssetCache\")\n  (with no-log))\n(deny mach-lookup\n  (global-name \"com.apple.cookied\")\n  (global-name \"com.apple.network.EAPOLController\")\n  (with no-log))\n(deny system-socket\n  (require-all\n    (socket-domain AF_SYSTEM)\n    (socket-protocol 1)) ; SYSPROTO_EVENT\n  (with no-log))\n\n(allow file-read*\n  (subpath \"/usr/libexec/AssetCache\")\n  (subpath \"/System\")\n  (subpath (param \"PROGRAM_PATH\"))\t\t; subpath for resource fork\n  (subpath (param \"DATA_PATH\"))\n  (subpath (param \"LOG_PATH\"))\n  (subpath (param \"METRICS_PATH\"))\n  (subpath (param \"PREFS_PATH\"))\n  (literal \"/Library/Keychains/System.keychain\")\n  (literal \"/Library/Application Support/CrashReporter/SubmitDiagInfo.domains\")\n  (subpath \"/Library/Managed Preferences\")\n  (subpath \"/Library/Preferences\")\n  (subpath \"/Library/Caching\")\n  (literal \"/private\")\n  (regex #\"^/(private/)?(etc|tmp|var)($|/)\")\n  (regex #\"/Library/Server/Caching/Data($|/)\")\t; for absorbing\n  (regex #\"/Library/Application Support/Apple/AssetCache/Data($|/)\"))\t; for absorbing\n\n(allow file-read-metadata\n  (literal \"/\")\n  (subpath \"/Library\")\n  (literal \"/Applications\")\n  (literal \"/private\")\n  (regex #\"^/(private/)?(etc|tmp|var)($|/)\")\n  (literal \"/var\")\n  (regex #\"/\\.TemporaryItems\")\n  (literal %@))\n\n(allow file-write*\n  (subpath \"/Library/Caching\")\n  (subpath \"/private/var/folders\")\n  (regex #\"/\\.TemporaryItems\")\n  (regex #\"/Library/Server/Caching/Data($|/)\")\t; for destructive absorbing\n  (regex #\"/Library/Application Support/Apple/AssetCache/Data($|/)\")\t; for destructive absorbing\n  (subpath (param \"DATA_PATH\"))\n  (subpath (param \"LOG_PATH\"))\n  (subpath (param \"METRICS_PATH\"))\n  (subpath (param \"PREFS_PATH\")))\n\n(allow file-write-data\n  (literal \"/private/var/db/mds/system/mds.lock\"))\n\n(allow file-read* file-write*\n  (subpath \"/private/var/db/mds/system\"))\n\n(when (param \"DATA_MIGRATION_FROM_PATH\")\n  (allow file-read* file-write*\n    (subpath (param \"DATA_MIGRATION_FROM_PATH\"))))\n(when (param \"DATA_MIGRATION_TO_PATH\")\n  (allow file-read* file-write*\n    (subpath (param \"DATA_MIGRATION_TO_PATH\"))))\n\n(allow ipc-posix-shm\n  (ipc-posix-name \"com.apple.AppleDatabaseChanged\")\n  (ipc-posix-name \"apple.shm.notification_center\"))\n\n(allow mach-per-user-lookup)\n\n(allow mach-lookup\n  (global-name \"com.apple.AssetCacheTetheratorService\")\n  (global-name \"com.apple.DiskArbitration.diskarbitrationd\")\n  (global-name \"com.apple.SecurityServer\")\n  (global-name \"com.apple.SystemConfiguration.configd\")\n  (global-name \"com.apple.cfnetwork.cfnetworkagent\")\n  (global-name \"com.apple.lsd.mapdb\")\n  (global-name \"com.apple.metadata.mds\")\n  (global-name \"com.apple.ocspd\")\n  (global-name \"com.apple.system.opendirectoryd.membership\")\n  (global-name \"com.apple.securityd.xpc\")\n  (global-name \"com.apple.securityd.systemkeychain\")\n  (global-name \"com.apple.wifi.anqp\"))\n\n(allow network-outbound)\n\n(allow signal (target self))\n\n(allow system-fsctl\n  (fsctl-command (_IO \"h\" 47)))    ; HFSIOC_SET_HOTFILE_STATE\n\n(allow file-read* file-write*\n  (literal \"/private/var/run/com.apple.AssetCache/LastAlerts.plist\"))\n\n(allow mach-lookup\n  (global-name-regex #\"^com\\.apple\\.distributed_notifications\"))\n(allow distributed-notification-post)\n\n(allow iokit-open\n  (iokit-user-client-class \"RootDomainUserClient\"))\n(allow mach-lookup\n  (global-name \"com.apple.PowerManagement.control\"))\n\n(allow mach-lookup\n  (global-name \"com.apple.AssetCacheManagerService\"))\n\n(allow mach-lookup\n  (global-name \"com.apple.apsd\")\n  (global-name \"com.apple.applepushserviced\")\n  (global-name \"com.apple.AssetCacheLocatorService\"))\n\n(allow mach-lookup\n  (global-name \"com.apple.cache_delete\"))\n"
- "265"
- "CurrentDDMConfig"
- "T@\"NSString\",&,V_prefsPath"
- "Unable to save preferences to %@"
- "_prefsPath"
- "initWithPrefsPath:URL:queue:queueIdentityKey:"
- "setPrefsPath:"
```
