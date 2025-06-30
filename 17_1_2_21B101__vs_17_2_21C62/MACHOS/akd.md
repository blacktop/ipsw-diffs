## akd

> `/System/Library/PrivateFrameworks/AuthKit.framework/akd`

```diff

-464.5.0.0.0
-  __TEXT.__text: 0x11cd54
-  __TEXT.__auth_stubs: 0x16c0
-  __TEXT.__objc_stubs: 0x146e0
-  __TEXT.__objc_methlist: 0x761c
-  __TEXT.__const: 0x1a80
-  __TEXT.__gcc_except_tab: 0x1a48
-  __TEXT.__objc_classname: 0x1589
-  __TEXT.__objc_methname: 0x1c68c
+466.7.12.0.0
+  __TEXT.__text: 0x121754
+  __TEXT.__auth_stubs: 0x1730
+  __TEXT.__objc_stubs: 0x14740
+  __TEXT.__objc_methlist: 0x7684
+  __TEXT.__const: 0x1b50
+  __TEXT.__cstring: 0xafb8
+  __TEXT.__objc_classname: 0x15bc
+  __TEXT.__objc_methname: 0x1c80c
   __TEXT.__objc_methtype: 0x4fee
-  __TEXT.__oslogstring: 0x16a60
-  __TEXT.__cstring: 0xa998
-  __TEXT.__swift5_typeref: 0xc30
-  __TEXT.__swift5_fieldmd: 0x450
-  __TEXT.__constg_swiftt: 0x6a8
-  __TEXT.__swift5_reflstr: 0x399
+  __TEXT.__gcc_except_tab: 0x1a30
+  __TEXT.__oslogstring: 0x16b4e
+  __TEXT.__swift5_typeref: 0xca4
+  __TEXT.__swift5_fieldmd: 0x4b4
+  __TEXT.__constg_swiftt: 0x814
+  __TEXT.__swift5_reflstr: 0x3e9
   __TEXT.__swift5_assocty: 0xd8
-  __TEXT.__swift5_capture: 0x778
+  __TEXT.__swift5_capture: 0x710
   __TEXT.__swift5_builtin: 0x3c
-  __TEXT.__swift5_proto: 0x74
-  __TEXT.__swift5_types: 0x70
-  __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x40ec
-  __TEXT.__eh_frame: 0x2a58
-  __DATA_CONST.__auth_got: 0xb70
-  __DATA_CONST.__got: 0xc58
+  __TEXT.__swift5_proto: 0x78
+  __TEXT.__swift5_types: 0x7c
+  __TEXT.__swift5_protos: 0x8
+  __TEXT.__unwind_info: 0x3804
+  __TEXT.__eh_frame: 0x2ff0
+  __DATA_CONST.__auth_got: 0xba8
+  __DATA_CONST.__got: 0xc78
   __DATA_CONST.__auth_ptr: 0x98
-  __DATA_CONST.__const: 0xa3c8
-  __DATA_CONST.__cfstring: 0x5be0
-  __DATA_CONST.__objc_classlist: 0x578
+  __DATA_CONST.__const: 0xa4e8
+  __DATA_CONST.__cfstring: 0x5d20
+  __DATA_CONST.__objc_classlist: 0x5a0
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x220
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA_CONST.__objc_intobj: 0x210
-  __DATA.__objc_const: 0x1b370
-  __DATA.__objc_selrefs: 0x5ed0
+  __DATA.__objc_const: 0x1b700
+  __DATA.__objc_selrefs: 0x5f38
   __DATA.__objc_protorefs: 0x98
-  __DATA.__objc_classrefs: 0xa58
-  __DATA.__objc_superrefs: 0x358
-  __DATA.__objc_ivar: 0x8cc
-  __DATA.__objc_data: 0x41b8
-  __DATA.__data: 0x2160
+  __DATA.__objc_classrefs: 0xa60
+  __DATA.__objc_superrefs: 0x360
+  __DATA.__objc_ivar: 0x8d4
+  __DATA.__objc_data: 0x4260
+  __DATA.__data: 0x2418
   __DATA.__bss: 0x1240
   __DATA.__common: 0xec
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: C886CA12-63D3-39DE-80BC-2D2709083D9E
-  Functions: 5373
-  Symbols:   1037
-  CStrings:  8627
+  UUID: 16EA5569-E9A3-3804-BA9E-8F77B2C9DB98
+  Functions: 5443
+  Symbols:   1050
+  CStrings:  8687
 
Symbols:
+ _$sSS9hashValueSivg
+ _AKAppleIDAuthenticationAppProvidedContextEasyStudentSignIn
+ _AKDeletedDevicesKey
+ _AKDeviceDeletedDateKey
+ _AKDeviceRemovalReasonKey
+ _AKInformationBeneficiaryInfoKey
+ _AKInformationBeneficiaryUuidKey
+ _objc_retain_x10
+ _swift_release_n
+ _swift_retain_n
+ _swift_weakDestroy
+ _swift_weakInit
+ _swift_weakLoadStrong
CStrings:
+ "\x015)\x1f\x0e\x1f\b"
+ "\n(mid, name, serial_number, model, os, os_version, dc, clcg, clbg,\nclhs, dec, circle_status, build_number, trusted, last_updated_date,\nadditional_info, altDSID, services, last_cache_updated_date)\nVALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"
+ "\n(mid, reason, last_updated_date, altDSID, deleted_date)\nVALUES (?, ?, ?, ?, ?);"
+ " AND serial_number IN ("
+ " WHERE altDSID = ?"
+ " WHERE altDSID = ? AND deleted_date <  strftime('%s', datetime('now', '-"
+ "%@: Successfully generated authentication parameters... generating SRP context!"
+ "AKAlertImageURLProvider"
+ "AKPushTokenKeychainWrapper"
+ "An issue was encountered while performing silent authentication for your device. Filing this radar will help determine what went wrong."
+ "CREATE TABLE IF NOT EXISTS deleted_device_list (\nmid TEXT PRIMARY KEY,\nreason INTEGER,\nlast_updated_date DOUBLE,\naltDSID TEXT,\ndeleted_date DOUBLE);"
+ "DeletedDeviceListProvider - Account %@ is missing altDSID. Ineligible for clearing cache."
+ "DeletedDeviceListProvider - Begin clearing stale deleted devices"
+ "DeletedDeviceListProvider - Begin fetching deleted devices from cache for query %s"
+ "DeletedDeviceListProvider - Begin saving deleted device %@"
+ "DeletedDeviceListProvider - Finished clearing cache with success: %{bool}d"
+ "DeletedDeviceListProvider - Finished fetching deleted devices from cache"
+ "DeletedDeviceListProvider - Finished saving deleted device %@ with success: %{bool}d"
+ "DeletedDeviceListProvider - No IdMS accounts found. Ineligible for clearing cache."
+ "DeviceListBaseProvider - Begin clearing %s for altDSID %s"
+ "DeviceListBaseProvider - Finished query: %@"
+ "DeviceListBaseProvider - Missing instance"
+ "DeviceListBaseProvider subclass need to implement tableName"
+ "DeviceListProvider - Begin fetching devices from cache for query %s"
+ "DeviceListProvider - Begin saving device %@"
+ "DeviceListProvider - Finished fetching devices from cache"
+ "DeviceListProvider - Finished saving device %@ with success: %{bool}d"
+ "DeviceListStoreManager - No idms account found for altDSID - %s"
+ "DeviceListStoreManager - failed to save device list version & cache offset for account - %@ with error - %@"
+ "Done creating deleted_device_list table"
+ "Error %@ executing query: %@"
+ "Error %@ fetching deleted devices from cache"
+ "Failed to clear stale devices from cache with error: %@"
+ "Failed to fetch device list from server. Missing entitlement."
+ "Failed to fetch device list with error: %@"
+ "Failed to read push token from keychain, returning nil. Error: %@"
+ "Failed to write push token to keychain. Error: %@"
+ "Fetch device list context is cache only. Skipping fetch from server."
+ "INSERT OR REPLACE INTO "
+ "Public token matches cached token, returning..."
+ "SELECT * FROM deleted_device_list WHERE altDSID = ?"
+ "Silent authentication issue detected"
+ "Start creating deleted_device_list table"
+ "Succesfully cleared stale devices from cache"
+ "T@\"NSArray\",R,N,V_beneficiaryInfo"
+ "This auth is for a student. Skip ACAccount update."
+ "URLForResource:withExtension:"
+ "Unable to get companion Anisette data for %@! Error: %@"
+ "Updating device list cache. Saving server response."
+ "_TtC3akd18DeviceListProvider"
+ "_TtC3akd22DeviceListBaseProvider"
+ "_TtC3akd25DeletedDeviceListProvider"
+ "_beneficiaryInfo"
+ "_updateHeadersWithCompanionAnisetteData:clientProvidedData:completion:"
+ "akd/DeviceListBaseProvider.swift"
+ "appleaccount_mono_icon-60-dark"
+ "beneficiaryInfo"
+ "beneficiaryInfoForAccount:"
+ "cachedToken: %@, publicToken: %@"
+ "clearContinuationTokenIfSupportedWithError:"
+ "clearStaleDevicesWithAccountManager:completionHandler:"
+ "com.apple.AuthKitUI"
+ "com.apple.authkit.lastKnownPushToken"
+ "com.apple.authkit.pushToken.svc"
+ "com.apple.authkit.token.ck.delete"
+ "com.apple.authkit.token.ck.fetch"
+ "com.apple.authkit.token.hb.fetch"
+ "com.apple.authkit.token.prk.delete"
+ "com.apple.authkit.token.prk.fetch"
+ "deletedDate"
+ "deletedDeviceList"
+ "deletedDeviceListProvider"
+ "deletedDevicesCacheExpiryOffset"
+ "deletedDevicesCacheExpiryOffsetForAccount:"
+ "deleted_device_list"
+ "deviceListProvider"
+ "execute(query:params:)"
+ "fetchDeviceListFromCache(with:cdpFactory:serviceController:accountManager:)"
+ "fetchDeviceListFromServer(with:serviceController:accountManager:)"
+ "fetchToken"
+ "initWithInteger:"
+ "png"
+ "removalReason"
+ "removeContinuationTokenForAccount:telemetryFlowID:error:"
+ "serialNumbers"
+ "setBeneficiaryInfo:forAccount:"
+ "setDeletedDevicesCacheExpiryOffset:forAccount:"
+ "updateToken:"
+ "usrt"
+ "v32@0:8@\"AKAccountManager\"16@?<v@?@\"NSError\">24"
- "\x015)\x1f\r\x1f\b"
- "An issue was encountered while performing silent authentication for your HomePod. Filing this radar will help determine what went wrong."
- "DELETE FROM device_list WHERE altDSID = ?"
- "DELETE FROM device_list WHERE trusted = 0 AND last_cache_updated_date <  strftime('%s', datetime('now', '-30 day'))"
- "DeviceListStoreManager - Begin clearing untrusted devices"
- "DeviceListStoreManager - Begin deleting device list for altDSID %s"
- "DeviceListStoreManager - Begin fetching devices from cache for query %s"
- "DeviceListStoreManager - Begin resetting device trust"
- "DeviceListStoreManager - Begin saving device %@"
- "DeviceListStoreManager - Finished clearing untrusted devices"
- "DeviceListStoreManager - Finished deleting device list for altDSID %s"
- "DeviceListStoreManager - Finished fetching devices from cache"
- "DeviceListStoreManager - Finished resetting device trust"
- "DeviceListStoreManager - Finished saving device %@"
- "Eligible for device cache. Saving server response."
- "Error %@ cleaning untrusted devices"
- "Error %@ deleting device list for altDSID %s"
- "Error %@ resetting device trust."
- "Error %@ saving device %@"
- "Failed to clear untrusted device list from cache with error: %@"
- "HomePod Silent authentication issue detected"
- "INSERT OR REPLACE INTO device_list\n(mid, name, serial_number, model, os, os_version, dc, clcg, clbg,\nclhs, dec, circle_status, build_number, trusted, last_updated_date,\nadditional_info, altDSID, services, last_cache_updated_date)\nVALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"
- "No devices found for context: %@"
- "Proximity Authentication is disabled."
- "Proximity Authentication is not enabled on this flow."
- "Proximity Authentication is supported and enabled."
- "Proximity Authentication override feature flag is enabled."
- "Succesfully cleared untrusted device list from cache"
- "UPDATE device_list SET trusted = 0 WHERE altDSID = ?"
- "_shouldDisableProximityAppleDAdvertisement"
- "aidProxAdvertisementDisabled"
- "clearContinuationTokenIfSupported"
- "clearStaleUntrustedDevices()"
- "clearStaleUntrustedDevicesWithCompletionHandler:"
- "configurationAtKey:"
- "deleteDeviceList(with:)"
- "fetchDeviceListFromCache(with:selectQuery:cdpFactory:serviceController:accountManager:)"
- "fetchDeviceListFromServer(with:cdpFactory:serviceController:)"
- "overrideAidProxAdvertismentEnabled"
- "removeContinuationTokenForAccount:"

```
