## CloudDocsDaemon

> `/System/Library/PrivateFrameworks/CloudDocsDaemon.framework/CloudDocsDaemon`

```diff

-3097.60.140.0.0
-  __TEXT.__text: 0x32ec0c
+3097.60.152.0.0
+  __TEXT.__text: 0x32fa44
   __TEXT.__auth_stubs: 0x1d60
-  __TEXT.__objc_methlist: 0x17f50
+  __TEXT.__objc_methlist: 0x17fd8
   __TEXT.__const: 0x550
-  __TEXT.__cstring: 0x7e49e
-  __TEXT.__oslogstring: 0x4481e
-  __TEXT.__gcc_except_tab: 0x1d774
+  __TEXT.__cstring: 0x7e73c
+  __TEXT.__oslogstring: 0x448f9
+  __TEXT.__gcc_except_tab: 0x1d85c
   __TEXT.__ustring: 0x36
-  __TEXT.__unwind_info: 0x94b8
-  __TEXT.__objc_classname: 0x24e5
-  __TEXT.__objc_methname: 0x40760
-  __TEXT.__objc_methtype: 0x867c
-  __TEXT.__objc_stubs: 0x2c2a0
-  __DATA_CONST.__got: 0x1688
-  __DATA_CONST.__const: 0x8ea0
-  __DATA_CONST.__objc_classlist: 0x928
+  __TEXT.__unwind_info: 0x94e8
+  __TEXT.__objc_classname: 0x24fe
+  __TEXT.__objc_methname: 0x40963
+  __TEXT.__objc_methtype: 0x8693
+  __TEXT.__objc_stubs: 0x2c400
+  __DATA_CONST.__got: 0x1690
+  __DATA_CONST.__const: 0x8ef0
+  __DATA_CONST.__objc_classlist: 0x930
   __DATA_CONST.__objc_catlist: 0xc8
   __DATA_CONST.__objc_protolist: 0x230
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xdc28
+  __DATA_CONST.__objc_selrefs: 0xdc88
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x840
   __DATA_CONST.__objc_arraydata: 0xd18
   __AUTH_CONST.__auth_got: 0xec0
   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__const: 0x25c8
-  __AUTH_CONST.__cfstring: 0x20f60
-  __AUTH_CONST.__objc_const: 0x3edf0
+  __AUTH_CONST.__cfstring: 0x21040
+  __AUTH_CONST.__objc_const: 0x3ef50
   __AUTH_CONST.__objc_intobj: 0xa08
   __AUTH_CONST.__objc_arrayobj: 0x168
   __AUTH_CONST.__objc_doubleobj: 0x60
-  __AUTH.__objc_data: 0x2760
-  __DATA.__objc_ivar: 0x2088
+  __AUTH.__objc_data: 0x27b0
+  __DATA.__objc_ivar: 0x2098
   __DATA.__data: 0x2258
   __DATA.__bss: 0x360
   __DATA_DIRTY.__objc_data: 0x3430

   - /usr/lib/libprequelite.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 13472
-  Symbols:   16516
-  CStrings:  23620
+  Functions: 13488
+  Symbols:   16538
+  CStrings:  23650
 
Symbols:
+ OBJC_IVAR_$_AppTelemetryInvestigation._underlyingErrorCode
+ OBJC_IVAR_$_AppTelemetryInvestigation._underlyingErrorDomain
+ OBJC_IVAR_$_BRCClientZone._appUninstalledDate
+ _OBJC_CLASS_$_NSThread
CStrings:
+ "\b\x11\"\x11\x1c\x13\x15\x1f\x02\x13\""
+ "-[BRCClientZone _scheduleZoneResetForUninstalledAppIfNecessary]"
+ "-[BRCClientZone _scheduleZoneResetForUninstalledAppIfNecessary]_block_invoke"
+ ".%!@(MISSING).%!l(MISSING)d"
+ "<%!@(MISSING)[%!@(MISSING)] %!@(MISSING) {client:%!@(MISSING) server:%!@(MISSING) sync:%!@(MISSING) %!@(MISSING) rid:%!l(MISSING)lu appuninstalled:%!@(MISSING)}>"
+ "?"
+ "BRCSystemSupportAnalyzer"
+ "CREATE TABLE item_errors ( item_rowid integer NOT NULL, error_domain TEXT NOT NULL default \"unknown\", error_code integer NOT NULL default 0, error_message TEXT, error_timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, service integer NOT NULL, PRIMARY KEY (item_rowid, error_domain, error_code, error_message, service))"
+ "INSERT OR REPLACE INTO item_errors (item_rowid, error_domain, error_code, error_message, underlying_error_domain, underlying_error_code, service) VALUES (%!l(MISSING)lu, %!@(MISSING), %!l(MISSING)d, %!@(MISSING), %!@(MISSING), %!l(MISSING)d, %!d(MISSING))"
+ "SELECT 1 FROM client_items ci WHERE ci.zone_rowid = %!@(MISSING) AND NOT item_id_is_documents(ci.item_id)"
+ "SELECT error_domain, error_code, error_message, error_timestamp, underlying_error_domain, underlying_error_code, service, item_rowid FROM item_errors"
+ "[DEBUG] Don't fetch recents and favorites before initial sync-down of %!@(MISSING).\n%!@(MISSING)%!@(MISSING)"
+ "[DEBUG] cancel zone reset timer for %!@(MISSING)%!@(MISSING)"
+ "[DEBUG] execute zone reset for %!@(MISSING)%!@(MISSING)"
+ "[DEBUG] schedule zone reset timer to run after %!f(MISSING) sec for %!@(MISSING)%!@(MISSING)"
+ "_appUninstalledDate"
+ "_reportUploadErrorForDocument:error:underlyingError:"
+ "_resetAfterAppUninstallTimer"
+ "_scheduleZoneResetForUninstalledAppIfNecessary"
+ "_underlyingErrorCode"
+ "_underlyingErrorDomain"
+ "appUninstalledDate"
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
+ "zone-auto-reset-delay-after-app-uninstall"
+ "zoneAutoResetDelayInSecAfterAppUninstall"
+ "{?=\"errorCode\"b1\"eventTimestamp\"b1\"underlyingErrorCode\"b1\"hasForegroundClients\"b1\"isEnhancedDrivePrivacyEnabled\"b1\"isPCSChained\"b1\"nonDiscretionary\"b1\"sharedZone\"b1}"
- "\b\x11\"\x11\x1c\x13\x14\x1f\x02\x12\""
- "<%!@(MISSING)[%!@(MISSING)] %!@(MISSING) {client:%!@(MISSING) server:%!@(MISSING) sync:%!@(MISSING) %!@(MISSING) rid:%!l(MISSING)lu}>"
- "CREATE TABLE item_errors ( item_rowid integer NOT NULL, error_domain TEXT NOT NULL default \"unknown\", error_code integer NOT NULL default 0, error_message TEXT, error_timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, service integer NOT NULL, PRIMARY KEY (item_rowid, error_domain, error_code, service))"
- "SELECT error_domain, error_code, error_message, error_timestamp, service, item_rowid FROM item_errors"
- "_getCloudDocsUnsupportedError"
- "captureLogsForOperationType:ofSubtype:forError:waitForCompletion:"
- "errorDomain = %!@(MISSING)|errorCode = %!l(MISSING)ld| errorDescription = %!@(MISSING)|"
- "{?=\"errorCode\"b1\"eventTimestamp\"b1\"hasForegroundClients\"b1\"isEnhancedDrivePrivacyEnabled\"b1\"isPCSChained\"b1\"nonDiscretionary\"b1\"sharedZone\"b1}"

```
