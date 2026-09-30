## AssetCache

> `/usr/libexec/AssetCache/AssetCache`

```diff

-247.0.0.0.0
-  __TEXT.__text: 0x18291c
+248.0.0.0.0
+  __TEXT.__text: 0x182a5c
   __TEXT.__auth_stubs: 0x1070
-  __TEXT.__objc_stubs: 0xe6e0
+  __TEXT.__objc_stubs: 0xe700
   __TEXT.__objc_methlist: 0x5f54
   __TEXT.__cstring: 0x7994
   __TEXT.__const: 0x43e30
   __TEXT.__gcc_except_tab: 0x3570
-  __TEXT.__objc_methname: 0x10fa8
-  __TEXT.__oslogstring: 0x7325
+  __TEXT.__objc_methname: 0x10fba
+  __TEXT.__oslogstring: 0x7359
   __TEXT.__objc_classname: 0x3b9
   __TEXT.__objc_methtype: 0x1c91
   __TEXT.__ustring: 0x19e
-  __TEXT.__info_plist: 0x570
-  __TEXT.__unwind_info: 0x1b20
+  __TEXT.__info_plist: 0x571
+  __TEXT.__unwind_info: 0x1b18
   __TEXT.__eh_frame: 0x88
   __DATA_CONST.__auth_got: 0x848
   __DATA_CONST.__got: 0x810

   __DATA_CONST.__objc_arrayobj: 0x4b0
   __DATA_CONST.__objc_dictobj: 0x8e8
   __DATA.__objc_const: 0xc410
-  __DATA.__objc_selrefs: 0x3c78
+  __DATA.__objc_selrefs: 0x3c80
   __DATA.__objc_ivar: 0x9f4
   __DATA.__objc_data: 0xaf0
   __DATA.__data: 0x838

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3224
+  Functions: 3225
   Symbols:   554
   CStrings:  1274
 
CStrings:
+ "(version 1)\n(deny default)\n(import \"system.sb\")\n(system-network)\n\n; don't spam logs with these denials\n(deny file-read*\n  (subpath \"/Users\")\n  (regex #\"/Library/Keychains/login\\.keychain\")\n  (with no-log))\n(deny file-write*\n  (regex #\"/Library/Caches/AssetCache\")\n  (with no-log))\n(deny mach-lookup\n  (global-name \"com.apple.cookied\")\n  (global-name \"com.apple.network.EAPOLController\")\n  (with no-log))\n(deny system-socket\n  (require-all\n    (socket-domain AF_SYSTEM)\n    (socket-protocol 1)) ; SYSPROTO_EVENT\n  (with no-log))\n\n(allow file-read*\n  (subpath \"/usr/libexec/AssetCache\")\n  (subpath \"/System\")\n  (subpath (param \"PROGRAM_PATH\"))\t\t; subpath for resource fork\n  (subpath (param \"DATA_PATH\"))\n  (subpath (param \"LOG_PATH\"))\n  (subpath (param \"METRICS_PATH\"))\n  (subpath (param \"PREFS_PATH\"))\n  (literal \"/Library/Keychains/System.keychain\")\n  (literal \"/Library/Application Support/CrashReporter/SubmitDiagInfo.domains\")\n  (subpath \"/Library/Managed Preferences\")\n  (subpath \"/Library/Preferences\")\n  (subpath \"/Library/Caching\")\n  (literal \"/private\")\n  (regex #\"^/(private/)?(etc|tmp|var)($|/)\")\n  (regex #\"/Library/Server/Caching/Data($|/)\")\t; for absorbing\n  (regex #\"/Library/Application Support/Apple/AssetCache/Data($|/)\"))\t; for absorbing\n\n(allow file-read-metadata\n  (literal \"/\")\n  (subpath \"/Library\")\n  (literal \"/Applications\")\n  (literal \"/private\")\n  (regex #\"^/(private/)?(etc|tmp|var)($|/)\")\n  (literal \"/var\")\n  (regex #\"/\\.TemporaryItems\")\n  (literal %!@(MISSING)))\n\n(allow file-write*\n  (subpath \"/Library/Caching\")\n  (subpath \"/private/var/folders\")\n  (regex #\"/\\.TemporaryItems\")\n  (regex #\"/Library/Server/Caching/Data($|/)\")\t; for destructive absorbing\n  (regex #\"/Library/Application Support/Apple/AssetCache/Data($|/)\")\t; for destructive absorbing\n  (subpath (param \"DATA_PATH\"))\n  (subpath (param \"LOG_PATH\"))\n  (subpath (param \"METRICS_PATH\"))\n  (subpath (param \"PREFS_PATH\")))\n\n(allow file-write-data\n  (literal \"/private/var/db/mds/system/mds.lock\"))\n\n(when (param \"DATA_MIGRATION_FROM_PATH\")\n  (allow file-read* file-write*\n    (subpath (param \"DATA_MIGRATION_FROM_PATH\"))))\n(when (param \"DATA_MIGRATION_TO_PATH\")\n  (allow file-read* file-write*\n    (subpath (param \"DATA_MIGRATION_TO_PATH\"))))\n\n(allow ipc-posix-shm\n  (ipc-posix-name \"com.apple.AppleDatabaseChanged\")\n  (ipc-posix-name \"apple.shm.notification_center\"))\n\n(allow mach-per-user-lookup)\n\n(allow mach-lookup\n  (global-name \"com.apple.AssetCacheTetheratorService\")\n  (global-name \"com.apple.DiskArbitration.diskarbitrationd\")\n  (global-name \"com.apple.SecurityServer\")\n  (global-name \"com.apple.SystemConfiguration.configd\")\n  (global-name \"com.apple.cfnetwork.cfnetworkagent\")\n  (global-name \"com.apple.lsd.mapdb\")\n  (global-name \"com.apple.metadata.mds\")\n  (global-name \"com.apple.ocspd\")\n  (global-name \"com.apple.system.opendirectoryd.membership\")\n  (global-name \"com.apple.wifi.anqp\"))\n\n(allow network-outbound)\n\n(allow signal (target self))\n\n(allow system-fsctl\n  (fsctl-command (_IO \"h\" 47)))    ; HFSIOC_SET_HOTFILE_STATE\n\n(allow file-read* file-write*\n  (literal \"/private/var/run/com.apple.AssetCache/LastAlerts.plist\"))\n\n(allow mach-lookup\n  (global-name-regex #\"^com\\.apple\\.distributed_notifications\"))\n(allow distributed-notification-post)\n\n(allow iokit-open\n  (iokit-user-client-class \"RootDomainUserClient\"))\n(allow mach-lookup\n  (global-name \"com.apple.PowerManagement.control\"))\n\n(allow mach-lookup\n  (global-name \"com.apple.AssetCacheManagerService\"))\n\n(allow mach-lookup\n  (global-name \"com.apple.apsd\")\n  (global-name \"com.apple.applepushserviced\")\n  (global-name \"com.apple.AssetCacheLocatorService\"))\n\n(allow mach-lookup\n  (global-name \"com.apple.cache_delete\"))\n"
+ "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/EdgeCache/EdgeCache/ECAssetHandler.m"
+ "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/EdgeCache/EdgeCache/ECAssetRequestor.m"
+ "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/EdgeCache/EdgeCache/ECAssetUploader.m"
+ "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/EdgeCache/EdgeCache/ECCacheManager.m"
+ "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/EdgeCache/EdgeCache/ECCacheReader.m"
+ "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/EdgeCache/EdgeCache/ECCacheWriter.m"
+ "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/EdgeCache/EdgeCache/ECConfig.m"
+ "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/EdgeCache/EdgeCache/ECConnection.m"
+ "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/EdgeCache/EdgeCache/ECExtent.m"
+ "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/EdgeCache/EdgeCache/ECMetricsManager.m"
+ "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/EdgeCache/EdgeCache/ECNetworkUtilities.m"
+ "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/EdgeCache/EdgeCache/ECParentManager.m"
+ "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/EdgeCache/EdgeCache/ECPeerManager.m"
+ "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/EdgeCache/EdgeCache/ECPeerNotify.m"
+ "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/EdgeCache/EdgeCache/ECPeerQuery.m"
+ "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/EdgeCache/EdgeCache/ECRegistrant.m"
+ "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/EdgeCache/EdgeCache/ECRemoteServerManager.m"
+ "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/EdgeCache/EdgeCache/ECResponse.m"
+ "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/EdgeCache/EdgeCache/ECServer.m"
+ "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/EdgeCache/EdgeCache/ECStatisticsAggregator.m"
+ "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/EdgeCache/EdgeCache/ECStatisticsReporter.m"
+ "/private/var/run/com.apple.AssetCache/LastAlerts.plist"
+ "248"
- "(version 1)\n(deny default)\n(import \"system.sb\")\n(system-network)\n\n; don't spam logs with these denials\n(deny file-read*\n  (subpath \"/Users\")\n  (regex #\"/Library/Keychains/login\\.keychain\")\n  (with no-log))\n(deny file-write*\n  (regex #\"/Library/Caches/AssetCache\")\n  (with no-log))\n(deny mach-lookup\n  (global-name \"com.apple.cookied\")\n  (global-name \"com.apple.network.EAPOLController\")\n  (with no-log))\n(deny system-socket\n  (require-all\n    (socket-domain AF_SYSTEM)\n    (socket-protocol 1)) ; SYSPROTO_EVENT\n  (with no-log))\n\n(allow file-read*\n  (subpath \"/usr/libexec/AssetCache\")\n  (subpath \"/System\")\n  (subpath (param \"PROGRAM_PATH\"))\t\t; subpath for resource fork\n  (subpath (param \"DATA_PATH\"))\n  (subpath (param \"LOG_PATH\"))\n  (subpath (param \"METRICS_PATH\"))\n  (subpath (param \"PREFS_PATH\"))\n  (literal \"/Library/Keychains/System.keychain\")\n  (literal \"/Library/Application Support/CrashReporter/SubmitDiagInfo.domains\")\n  (subpath \"/Library/Managed Preferences\")\n  (subpath \"/Library/Preferences\")\n  (subpath \"/Library/Caching\")\n  (literal \"/private\")\n  (regex #\"^/(private/)?(etc|tmp|var)($|/)\")\n  (regex #\"/Library/Server/Caching/Data($|/)\")\t; for absorbing\n  (regex #\"/Library/Application Support/Apple/AssetCache/Data($|/)\"))\t; for absorbing\n\n(allow file-read-metadata\n  (literal \"/\")\n  (subpath \"/Library\")\n  (literal \"/Applications\")\n  (literal \"/private\")\n  (regex #\"^/(private/)?(etc|tmp|var)($|/)\")\n  (literal \"/var\")\n  (regex #\"/\\.TemporaryItems\")\n  (literal %!@(MISSING)))\n\n(allow file-write*\n  (subpath \"/Library/Caching\")\n  (subpath \"/private/var/folders\")\n  (regex #\"/\\.TemporaryItems\")\n  (regex #\"/Library/Server/Caching/Data($|/)\")\t; for destructive absorbing\n  (regex #\"/Library/Application Support/Apple/AssetCache/Data($|/)\")\t; for destructive absorbing\n  (subpath (param \"DATA_PATH\"))\n  (subpath (param \"LOG_PATH\"))\n  (subpath (param \"METRICS_PATH\"))\n  (subpath (param \"PREFS_PATH\")))\n\n(allow file-write-data\n  (literal \"/private/var/db/mds/system/mds.lock\"))\n\n(when (param \"DATA_MIGRATION_FROM_PATH\")\n  (allow file-read* file-write*\n    (subpath (param \"DATA_MIGRATION_FROM_PATH\"))))\n(when (param \"DATA_MIGRATION_TO_PATH\")\n  (allow file-read* file-write*\n    (subpath (param \"DATA_MIGRATION_TO_PATH\"))))\n\n(allow ipc-posix-shm\n  (ipc-posix-name \"com.apple.AppleDatabaseChanged\")\n  (ipc-posix-name \"apple.shm.notification_center\"))\n\n(allow mach-per-user-lookup)\n\n(allow mach-lookup\n  (global-name \"com.apple.AssetCacheTetheratorService\")\n  (global-name \"com.apple.DiskArbitration.diskarbitrationd\")\n  (global-name \"com.apple.SecurityServer\")\n  (global-name \"com.apple.SystemConfiguration.configd\")\n  (global-name \"com.apple.cfnetwork.cfnetworkagent\")\n  (global-name \"com.apple.lsd.mapdb\")\n  (global-name \"com.apple.metadata.mds\")\n  (global-name \"com.apple.ocspd\")\n  (global-name \"com.apple.system.opendirectoryd.membership\")\n  (global-name \"com.apple.wifi.anqp\"))\n\n(allow network-outbound)\n\n(allow signal (target self))\n\n(allow system-fsctl\n  (fsctl-command (_IO \"h\" 47)))    ; HFSIOC_SET_HOTFILE_STATE\n\n(allow file-read* file-write*\n  (literal \"/private/var/tmp/com.apple.AssetCache.LastAlerts.plist\"))\n\n(allow mach-lookup\n  (global-name-regex #\"^com\\.apple\\.distributed_notifications\"))\n(allow distributed-notification-post)\n\n(allow iokit-open\n  (iokit-user-client-class \"RootDomainUserClient\"))\n(allow mach-lookup\n  (global-name \"com.apple.PowerManagement.control\"))\n\n(allow mach-lookup\n  (global-name \"com.apple.AssetCacheManagerService\"))\n\n(allow mach-lookup\n  (global-name \"com.apple.apsd\")\n  (global-name \"com.apple.applepushserviced\")\n  (global-name \"com.apple.AssetCacheLocatorService\"))\n\n(allow mach-lookup\n  (global-name \"com.apple.cache_delete\"))\n"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/EdgeCache/EdgeCache/ECAssetHandler.m"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/EdgeCache/EdgeCache/ECAssetRequestor.m"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/EdgeCache/EdgeCache/ECAssetUploader.m"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/EdgeCache/EdgeCache/ECCacheManager.m"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/EdgeCache/EdgeCache/ECCacheReader.m"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/EdgeCache/EdgeCache/ECCacheWriter.m"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/EdgeCache/EdgeCache/ECConfig.m"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/EdgeCache/EdgeCache/ECConnection.m"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/EdgeCache/EdgeCache/ECExtent.m"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/EdgeCache/EdgeCache/ECMetricsManager.m"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/EdgeCache/EdgeCache/ECNetworkUtilities.m"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/EdgeCache/EdgeCache/ECParentManager.m"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/EdgeCache/EdgeCache/ECPeerManager.m"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/EdgeCache/EdgeCache/ECPeerNotify.m"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/EdgeCache/EdgeCache/ECPeerQuery.m"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/EdgeCache/EdgeCache/ECRegistrant.m"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/EdgeCache/EdgeCache/ECRemoteServerManager.m"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/EdgeCache/EdgeCache/ECResponse.m"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/EdgeCache/EdgeCache/ECServer.m"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/EdgeCache/EdgeCache/ECStatisticsAggregator.m"
- "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/EdgeCache/EdgeCache/ECStatisticsReporter.m"
- "/private/var/tmp/com.apple.AssetCache.LastAlerts.plist"
- "247"

```
