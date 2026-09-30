## iCloudDriveCore

> `/System/Library/PrivateFrameworks/iCloudDriveCore.framework/iCloudDriveCore`

```diff

-3097.60.140.0.0
-  __TEXT.__text: 0x2d5c28
+3097.60.152.0.0
+  __TEXT.__text: 0x2d7438
   __TEXT.__auth_stubs: 0x1b60
-  __TEXT.__objc_methlist: 0x167a8
+  __TEXT.__objc_methlist: 0x16828
   __TEXT.__const: 0x4c8
-  __TEXT.__cstring: 0x7861f
-  __TEXT.__oslogstring: 0x3987d
-  __TEXT.__gcc_except_tab: 0x17fa4
+  __TEXT.__cstring: 0x791ee
+  __TEXT.__oslogstring: 0x39a15
+  __TEXT.__gcc_except_tab: 0x180b8
   __TEXT.__ustring: 0x36
-  __TEXT.__unwind_info: 0x8628
-  __TEXT.__objc_classname: 0x238d
-  __TEXT.__objc_methname: 0x3d55f
-  __TEXT.__objc_methtype: 0x75e9
-  __TEXT.__objc_stubs: 0x2a280
-  __DATA_CONST.__got: 0x1660
-  __DATA_CONST.__const: 0x8738
-  __DATA_CONST.__objc_classlist: 0x8e8
+  __TEXT.__unwind_info: 0x8730
+  __TEXT.__objc_classname: 0x23a6
+  __TEXT.__objc_methname: 0x3d785
+  __TEXT.__objc_methtype: 0x7600
+  __TEXT.__objc_stubs: 0x2a400
+  __DATA_CONST.__got: 0x1668
+  __DATA_CONST.__const: 0x87b0
+  __DATA_CONST.__objc_classlist: 0x8f0
   __DATA_CONST.__objc_catlist: 0xd0
   __DATA_CONST.__objc_protolist: 0x208
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xd120
+  __DATA_CONST.__objc_selrefs: 0xd180
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x7f0
   __DATA_CONST.__objc_arraydata: 0xe00
   __AUTH_CONST.__auth_got: 0xdc0
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__const: 0x2778
-  __AUTH_CONST.__cfstring: 0x21480
-  __AUTH_CONST.__objc_const: 0x39ba0
+  __AUTH_CONST.__const: 0x27a8
+  __AUTH_CONST.__cfstring: 0x216c0
+  __AUTH_CONST.__objc_const: 0x39d00
   __AUTH_CONST.__objc_intobj: 0xa68
   __AUTH_CONST.__objc_arrayobj: 0x1c8
   __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH_CONST.__objc_doubleobj: 0x60
-  __AUTH.__objc_data: 0x24e0
+  __AUTH.__objc_data: 0x2530
   __AUTH.__data: 0x18
-  __DATA.__objc_ivar: 0x1d54
+  __DATA.__objc_ivar: 0x1d64
   __DATA.__data: 0x2168
   __DATA.__bss: 0x228
   __DATA_DIRTY.__objc_data: 0x3430

   - /usr/lib/libprequelite.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 12390
-  Symbols:   15133
-  CStrings:  21774
+  Functions: 12413
+  Symbols:   15164
+  CStrings:  21819
 
Symbols:
+ OBJC_IVAR_$_AppTelemetryInvestigation._underlyingErrorCode
+ OBJC_IVAR_$_AppTelemetryInvestigation._underlyingErrorDomain
+ OBJC_IVAR_$_BRCClientZone._appUninstalledDate
+ _OBJC_CLASS_$_NSThread
CStrings:
+ "\b\x11\"\x11\x1c\x13\x15\x1e\x13$"
+ "-[BRCAppLibrary waitForRootIngestionWithCompletion:]"
+ "-[BRCClientZone _scheduleZoneResetForUninstalledAppIfNecessary]"
+ "-[BRCClientZone _scheduleZoneResetForUninstalledAppIfNecessary]_block_invoke"
+ "-[BRCXPCClient _waitForContainerToBeForcedIngestWithContainerID:containerURL:sandboxExtension:bundleVersion:error:reply:]_block_invoke"
+ ".%!@(MISSING).%!l(MISSING)d"
+ "<%!@(MISSING)[%!@(MISSING)] %!@(MISSING) {client:%!@(MISSING) server:%!@(MISSING) sync:%!@(MISSING) %!@(MISSING) rid:%!l(MISSING)lu appuninstalled:%!@(MISSING)}>"
+ "?"
+ "ALTER TABLE aggregated_daily_telemetry RENAME TO temp_aggregated_daily_telemetry"
+ "BRCSystemSupportAnalyzer"
+ "CREATE TABLE aggregated_daily_telemetry (  app_telemetry_identifier integer NOT NULL, zone_mangled_id text NOT NULL, item_id text NOT NULL, enhanced_drive_privacy_enabled text NOT NULL, error_domain text NOT NULL, error_code int NOT NULL, error_description text NOT NULL, underlying_error_domain text NOT NULL DEFAULT '', underlying_error_code int NOT NULL DEFAULT 0, count int NOT NULL DEFAULT 1, PRIMARY KEY (app_telemetry_identifier, zone_mangled_id, item_id, enhanced_drive_privacy_enabled, error_domain, error_code, underlying_error_domain, underlying_error_code))"
+ "CREATE TABLE item_errors ( item_rowid integer NOT NULL, error_domain TEXT NOT NULL default \"unknown\", error_code integer NOT NULL default 0, error_message TEXT, error_timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, service integer NOT NULL, PRIMARY KEY (item_rowid, error_domain, error_code, error_message, service))"
+ "CREATE TABLE item_errors ( item_rowid integer NOT NULL, error_domain TEXT NOT NULL default \"unknown\", error_code integer NOT NULL default 0, error_message TEXT, error_timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, underlying_error_domain TEXT NOT NULL default '', underlying_error_code integer NOT NULL default 0, service integer NOT NULL, PRIMARY KEY (item_rowid, error_domain, error_code, underlying_error_domain, underlying_error_code, service))"
+ "DROP TABLE temp_aggregated_daily_telemetry"
+ "INSERT INTO aggregated_daily_telemetry (app_telemetry_identifier, zone_mangled_id, item_id, enhanced_drive_privacy_enabled, error_domain, error_code, error_description, underlying_error_domain, underlying_error_code) VALUES (%!d(MISSING), %!@(MISSING), %!@(MISSING), %!@(MISSING), %!@(MISSING), %!l(MISSING)d, %!@(MISSING), %!@(MISSING), %!l(MISSING)d) ON CONFLICT DO UPDATE SET count=count+1"
+ "INSERT OR REPLACE INTO aggregated_daily_telemetry SELECT app_telemetry_identifier, zone_mangled_id, item_id, enhanced_drive_privacy_enabled, error_domain, error_code, error_description, '', 0, count FROM temp_aggregated_daily_telemetry"
+ "INSERT OR REPLACE INTO item_errors (item_rowid, error_domain, error_code, error_message, underlying_error_domain, underlying_error_code, service) VALUES (%!l(MISSING)lu, %!@(MISSING), %!l(MISSING)d, %!@(MISSING), %!@(MISSING), %!l(MISSING)d, %!d(MISSING))"
+ "INSERT OR REPLACE INTO item_errors SELECT item_rowid, error_domain, error_code, error_message, error_timestamp, '', 0, service FROM temp_item_errors"
+ "Identified an item that is missing a sync up job"
+ "Item %!@(MISSING) need to sync up but missing a sync up job"
+ "SELECT 1 FROM client_items ci WHERE ci.zone_rowid = %!@(MISSING) AND NOT item_id_is_documents(ci.item_id)"
+ "SELECT 1 FROM client_sync_up WHERE throttle_state != 0   AND throttle_id = %!l(MISSING)ld   LIMIT 1"
+ "SELECT app_telemetry_identifier, zone_mangled_id, item_id, enhanced_drive_privacy_enabled, error_domain, error_code, error_description, underlying_error_domain, underlying_error_code, count FROM aggregated_daily_telemetry"
+ "SELECT error_domain, error_code, error_message, error_timestamp, underlying_error_domain, underlying_error_code, service, item_rowid FROM item_errors"
+ "[DEBUG] Boost force ingesting documents %!@(MISSING)%!@(MISSING)"
+ "[DEBUG] Boost force ingesting root %!@(MISSING)%!@(MISSING)"
+ "[DEBUG] Don't fetch recents and favorites before initial sync-down of %!@(MISSING).\n%!@(MISSING)%!@(MISSING)"
+ "[DEBUG] Force ingestion was not done for %!@(MISSING), let's invoke another force ingest to boost the job in FP%!@(MISSING)"
+ "[DEBUG] cancel zone reset timer for %!@(MISSING)%!@(MISSING)"
+ "[DEBUG] execute zone reset for %!@(MISSING)%!@(MISSING)"
+ "[DEBUG] schedule zone reset timer to run after %!f(MISSING) sec for %!@(MISSING)%!@(MISSING)"
+ "[SyncHealth] Identified an item that is missing a sync up job"
+ "_appUninstalledDate"
+ "_reportUploadErrorForDocument:error:underlyingError:"
+ "_resetAfterAppUninstallTimer"
+ "_scheduleZoneResetForUninstalledAppIfNecessary"
+ "_underlyingErrorCode"
+ "_underlyingErrorDomain"
+ "appUninstalledDate"
+ "brc_errorDamagedDocumentOnDiskWithUnderlyingError:"
+ "captureLogsForOperationType:ofSubtype:forError:underlyingError:"
+ "captureLogsForOperationType:ofSubtype:forError:underlyingError:waitForCompletion:"
+ "errorDomain = %!@(MISSING)|errorCode = %!l(MISSING)ld| errorDescription = %!@(MISSING)| underlyingErrorDomain = %!@(MISSING)| underlyingErrorCode = %!l(MISSING)ld"
+ "hasUnderlyingErrorCode"
+ "hasUnderlyingErrorDomain"
+ "isCloudDocsSupportedWithError:"
+ "setHasUnderlyingErrorCode:"
+ "setUnderlyingErrorCode:"
+ "setUnderlyingErrorDomain:"
+ "sortWithOptions:usingComparator:"
+ "underlyingErrorCode"
+ "underlyingErrorDomain"
+ "waitForRootIngestionWithCompletion:"
+ "zone-auto-reset-delay-after-app-uninstall"
+ "zoneAutoResetDelayInSecAfterAppUninstall"
+ "{?=\"errorCode\"b1\"eventTimestamp\"b1\"underlyingErrorCode\"b1\"hasForegroundClients\"b1\"isEnhancedDrivePrivacyEnabled\"b1\"isPCSChained\"b1\"nonDiscretionary\"b1\"sharedZone\"b1}"
- "\b\x11\"\x11\x1c\x13\x14\x1e\x12$"
- "-[BRCAppLibrary waitForRootIngestion]"
- "<%!@(MISSING)[%!@(MISSING)] %!@(MISSING) {client:%!@(MISSING) server:%!@(MISSING) sync:%!@(MISSING) %!@(MISSING) rid:%!l(MISSING)lu}>"
- "INSERT INTO aggregated_daily_telemetry (app_telemetry_identifier, zone_mangled_id, item_id, enhanced_drive_privacy_enabled, error_domain, error_code, error_description) VALUES (%!d(MISSING), %!@(MISSING), %!@(MISSING), %!@(MISSING), %!@(MISSING), %!l(MISSING)d, %!@(MISSING)) ON CONFLICT DO UPDATE SET count=count+1"
- "SELECT app_telemetry_identifier, zone_mangled_id, item_id, enhanced_drive_privacy_enabled, error_domain, error_code, error_description, count FROM aggregated_daily_telemetry"
- "SELECT error_domain, error_code, error_message, error_timestamp, service, item_rowid FROM item_errors"
- "_getCloudDocsUnsupportedError"
- "brc_errorDamagedDocumentOnDisk"
- "captureLogsForOperationType:ofSubtype:forError:waitForCompletion:"
- "errorDomain = %!@(MISSING)|errorCode = %!l(MISSING)ld| errorDescription = %!@(MISSING)|"
- "waitForRootIngestion"
- "{?=\"errorCode\"b1\"eventTimestamp\"b1\"hasForegroundClients\"b1\"isEnhancedDrivePrivacyEnabled\"b1\"isPCSChained\"b1\"nonDiscretionary\"b1\"sharedZone\"b1}"

```
