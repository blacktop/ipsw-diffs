## bluetoothd

> `/usr/sbin/bluetoothd`

```diff

-  __TEXT.__text: 0x8f113c
-  __TEXT.__auth_stubs: 0x51d0
-  __TEXT.__objc_stubs: 0x19800
+  __TEXT.__text: 0x8f3dd8
+  __TEXT.__auth_stubs: 0x5210
+  __TEXT.__objc_stubs: 0x199c0
   __TEXT.__init_offsets: 0x6c
-  __TEXT.__objc_methlist: 0x9a5c
-  __TEXT.__const: 0x25d80
-  __TEXT.__gcc_except_tab: 0x6f470
-  __TEXT.__cstring: 0xc5f36
-  __TEXT.__objc_classname: 0xa12
-  __TEXT.__objc_methname: 0x1f0f1
-  __TEXT.__objc_methtype: 0x5972
-  __TEXT.__oslogstring: 0xbf716
+  __TEXT.__objc_methlist: 0x9b64
+  __TEXT.__const: 0x25d70
+  __TEXT.__gcc_except_tab: 0x6f6b0
+  __TEXT.__cstring: 0xc6a63
+  __TEXT.__objc_classname: 0xa32
+  __TEXT.__objc_methname: 0x1f434
+  __TEXT.__objc_methtype: 0x5a2b
+  __TEXT.__oslogstring: 0xbfb9e
   __TEXT.__swift5_typeref: 0x152
   __TEXT.__swift5_capture: 0xd0
   __TEXT.__constg_swiftt: 0x50

   __TEXT.__swift_as_cont: 0x18
   __TEXT.__ustring: 0x34
   __TEXT.__dlopen_cstrs: 0xd4
-  __TEXT.__unwind_info: 0x25ec8
+  __TEXT.__unwind_info: 0x26030
   __TEXT.__eh_frame: 0x2b0
-  __DATA_CONST.__const: 0x33b30
-  __DATA_CONST.__cfstring: 0x25e80
-  __DATA_CONST.__objc_classlist: 0x2f0
+  __DATA_CONST.__const: 0x33be0
+  __DATA_CONST.__cfstring: 0x26200
+  __DATA_CONST.__objc_classlist: 0x2f8
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0xe8
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arraydata: 0x428
   __DATA_CONST.__objc_dictobj: 0x2f8
   __DATA_CONST.__objc_arrayobj: 0x1e0
-  __DATA_CONST.__auth_got: 0x2900
-  __DATA_CONST.__got: 0xdd0
+  __DATA_CONST.__auth_got: 0x2920
+  __DATA_CONST.__got: 0xe30
   __DATA_CONST.__auth_ptr: 0x258
-  __DATA.__objc_const: 0x106f8
-  __DATA.__objc_selrefs: 0x7650
-  __DATA.__objc_ivar: 0x119c
-  __DATA.__objc_data: 0x1dd0
-  __DATA.__data: 0x4f10
+  __DATA.__objc_const: 0x108a8
+  __DATA.__objc_selrefs: 0x76d0
+  __DATA.__objc_ivar: 0x11b4
+  __DATA.__objc_data: 0x1e20
+  __DATA.__data: 0x4f20
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0x76c5a
+  __DATA.__bss: 0x76c82
   __DATA.__common: 0x15c78
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 37132
-  Symbols:   1790
-  CStrings:  47617
+  Functions: 37199
+  Symbols:   1794
+  CStrings:  47766
 
Sections:
~ __TEXT.__init_offsets : content changed
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__swift5_capture : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_fieldmd : content changed
~ __TEXT.__swift_as_entry : content changed
~ __TEXT.__swift_as_ret : content changed
~ __TEXT.__swift_as_cont : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_intobj : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __DATA_CONST.__objc_dictobj : content changed
~ __DATA_CONST.__objc_arrayobj : content changed
~ __DATA_CONST.__auth_ptr : content changed
Symbols:
+ __ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEElsEx
+ _sqlite3_bind_int64
+ _sqlite3_changes
+ _sqlite3_column_int64
CStrings:
+ "\n    Filter: action=%@, model=%@, rssi=%@"
+ "### CBExtension: CompanionSetup filter is unreachable after catch-all fallback: %@"
+ "### CBExtension: ignoring invalid CompanionSetup filter RSSI: %@"
+ ",?%lu"
+ "-[CBExtensionsDaemon _companionSetupFiltersFromDiscoveryInfo:]"
+ "23:50:06"
+ "?%lu"
+ "AFPreferences"
+ "AssistantServices Framework not available"
+ "B24@0:8^{sqlite3=}16"
+ "B40@0:8^{sqlite3=}16@24^q32"
+ "B44@0:8@16B24^{sqlite3=}28^v36"
+ "CBExtension: ignore CompanionSetup with no matching filter: extensionID=%@, %@"
+ "CBExtension: ignore non-CompanionSetup device: extensionID=%@, %@"
+ "CBExtensionCompanionSetupFilter"
+ "CREATE TRIGGER IF NOT EXISTS %s_DeleteCustomPropertiesCascade AFTER DELETE ON %s BEGIN DELETE FROM %s WHERE %s = OLD.Uuid; END"
+ "Cloud: Cleared pending cloud removal (unpair committed) for %s"
+ "Cloud: Skipping stale Updated (cloud removal pending) for %s"
+ "CustomProperties JSON query failed for this lookup; using row-by-row scan"
+ "CustomProperties JSON query failed to prepare (%{public}s): %{public}s"
+ "CustomProperties JSON query failed with error %d (%{public}s, %d)"
+ "CustomProperties lookups DEGRADED to row-by-row scan: libsqlite3 is missing JSON1"
+ "CustomProperties lookups using SQLite json_each fast path"
+ "DELETE FROM %s WHERE NOT EXISTS (SELECT 1 FROM %s d WHERE d.Uuid = %s.%s)"
+ "DELETE FROM OtherDevices WHERE LastConnectionTime != 0 AND ROWID NOT IN (SELECT ROWID FROM OtherDevices WHERE LastConnectionTime != 0 ORDER BY ROWID DESC LIMIT %d)"
+ "DELETE FROM OtherDevices WHERE LastConnectionTime = 0 AND ROWID NOT IN (SELECT ROWID FROM OtherDevices WHERE LastConnectionTime = 0 ORDER BY ROWID DESC LIMIT %d)"
+ "Device found changed: %{public}@"
+ "Device found new: %{public}@"
+ "EnhancedUUIDFilterPrecedence"
+ "Error Response"
+ "Execute Write Request"
+ "Execute Write Response"
+ "Failed to count OtherDevices rows before trim"
+ "Find By Type Value Request"
+ "Find By Type Value Response"
+ "Find Information Request"
+ "Find Information Response"
+ "FindNearbyLocalFindableAccessoryExtendedRange"
+ "Handle Multiple Notifications"
+ "Handle Value Confirmation"
+ "Handle Value Indication"
+ "Handle Value Notification"
+ "HighPERPct"
+ "Identification - device has resolved address %{public}.6P (OUI masked)"
+ "Invalid handle, there is no active session associated with the handle, lmHandle: 0x%x, AttOpcode: %s, AttHandle: 0x%04x, bufLen: %d"
+ "Jul  1 2026"
+ "LE_CIS_ReallocConnHandleInCig CIG %d CIS %d cisHandle 0x%x"
+ "LE_CIS_ReallocConnHandleInCig no resource for cisHandle 0x%x"
+ "LE_CIS_ReallocConnHandleInCig stale record for cisHandle 0x%x"
+ "LE_CsProcedureEnableComplete: peer-initiated stop, tearing down session"
+ "MTU Request"
+ "MTU Response"
+ "MaxPERInInterval"
+ "NetworkRelayParserWriteOutputCallback self is null"
+ "NumPoorRSSISamples"
+ "OtherDevices cache has %d row(s), over the cap (%d connected + %d seen); trimming before index build"
+ "OtherDevices index build hit backstop (%zu rows scanned); stopping to avoid init OOM"
+ "P90LatencyMs"
+ "P95LatencyMs"
+ "PoorRSSIPct"
+ "Prepare Write Response"
+ "RSSIBinGTMinus50dBm"
+ "RSSIBinLTMinus95dBm"
+ "RSSIBinMinus50ToMinus65dBm"
+ "RSSIBinMinus65ToMinus75dBm"
+ "RSSIBinMinus75ToMinus85dBm"
+ "RSSIBinMinus85ToMinus90dBm"
+ "RSSIBinMinus90ToMinus95dBm"
+ "Read Blob Request"
+ "Read Blob Response"
+ "Read By Group Type Request"
+ "Read By Group Type Response"
+ "Read By Type Request"
+ "Read By Type Response"
+ "Read Multiple Request"
+ "Read Multiple Response"
+ "Read Multiple Variable Length Request"
+ "Read Multiple Variable Length Response"
+ "Read Request"
+ "Read Response"
+ "Reconciled %d orphaned CustomProperties row(s) for '%{public}s'"
+ "Rejected SMP/BR-EDR pairing request: link not AES-CCM/P-256 encrypted"
+ "SELECT %s FROM %s"
+ "SELECT %s, %s FROM %s"
+ "SELECT COUNT() FROM OtherDevices"
+ "SELECT COUNT() FROM OtherDevices WHERE LastConnectionTime != 0"
+ "SELECT COUNT() FROM OtherDevices WHERE LastConnectionTime = 0"
+ "SELECT DISTINCT cp.%s FROM %s AS cp, json_each(CASE WHEN json_valid(cp.%s) THEN cp.%s ELSE '{}' END) AS je WHERE je.key IN (%@)"
+ "SELECT cp.%s FROM %s AS cp, json_each(CASE WHEN json_valid(cp.%s) THEN cp.%s ELSE '{}' END) AS je WHERE je.key IN (%@) GROUP BY cp.%s HAVING COUNT(DISTINCT je.key) = %lu"
+ "SELECT key FROM json_each('{}')"
+ "SystemSettings: AssistantServices not available, skipping Siri notification registration."
+ "SystemSettings: kAFPreferencesDidChangeDarwinNotification symbol not found in AssistantServices bundle"
+ "T@\"NSArray\",C,N,V_companionSetupFilters"
+ "T@\"NSMutableSet\",&,N,V_pendingCloudRemovals"
+ "T@\"NSNumber\",C,N,V_action"
+ "T@\"NSNumber\",C,N,V_model"
+ "T@\"NSNumber\",C,N,V_rssi"
+ "Timeout waiting for ATT response, forcing a disconnect, lmHandle: 0x%x, addr: %: (no requestPdu)"
+ "Timeout waiting for ATT response, forcing a disconnect, lmHandle: 0x%x, addr: %:, AttOpcode: %s, AttHandle: 0x%04x, requestPduLength: %d"
+ "Write Response"
+ "_companionSetupFilters"
+ "_companionSetupFiltersFromDiscoveryInfo:"
+ "_customPropertiesJSONQuerySupport"
+ "_model"
+ "_pendingCloudRemovals"
+ "appendUUIDsUsingJSONQueryForProperties:matchAll:fromDatabase:into:"
+ "appendUUIDsUsingScanForProperties:matchAll:fromDatabase:into:"
+ "appendUUIDsWithProperties:matchAll:fromDatabase:into:"
+ "clearPendingCloudRemovalForAddress:"
+ "companionSetupFilters"
+ "companionSetupInfo"
+ "countryCodes_regV6.0_sarV1.13.plist"
+ "customPropertiesJSONQuerySupportedForDatabase:"
+ "filters %d"
+ "findUUIDsWithProperties:matchAll:"
+ "initClassicDeviceIdentificationForMetrics - device %@ chipset %d lmpVersion %d"
+ "initLeDeviceIdentificationForMetrics - device %@ chipset %d lmpVersion %d appearance %d"
+ "orderedSetWithArray:"
+ "parseAACPSetupComplete TIPI table opcodeLength %u too small for header"
+ "parseAACPSetupComplete TIPI table sourceCount %u exceeds remaining opcodeLength %u"
+ "pendingCloudRemovals"
+ "protectCustomPropertiesIntegrityInDatabase:type:"
+ "readInt64FromDatabase:statement:value:"
+ "remoteVersionInfoAvailable - address %{public}s chipset %d lmpVersion %d lmpSubVersion %d appearance %d"
+ "remoteVersionInfoAvailable - device %@ chipset %d lmpVersion %d lmpSubVersion %d"
+ "remoteVersionInfoAvailable: device not found in cache for address %{public}s"
+ "remoteVersionInfoAvailable: no device for %@"
+ "remoteVersionInfoAvailable: no device found for address %{public}s"
+ "setCompanionSetupFilters:"
+ "setPendingCloudRemovals:"
+ "statedump: Other devices: %u row(s) on disk, %zu address(es) in memory index"
+ "trimOtherDevicesCacheToCap"
+ "updateClassicDevicePnpIdForMetrics - device %@ vidSrc %d vid %d pid %d"
+ "updateLeDeviceAppearanceForMetrics - device %@ appearance %d"
+ "updateLeDevicePnpIdForMetrics - device %@ vidSrc %d vid %d pid %d"
+ "v44@0:8@16B24^{sqlite3=}28^v36"
+ "{vector<std::string, std::allocator<std::string>>=^v^v{?=^v}}28@0:8@16B24"
- "20:05:31"
- "Identification - device has resolved address %{public}.6P and OUI %{public}.3P"
- "In memory index and database sizes do not match"
- "Invalid handle, there is no active session associated with the handle."
- "Jun 18 2026"
- "SELECT COUNT() FROM OtherDevices WHERE LastConnectionTime > 0"
- "SELECT COUNT() FROM OtherDevices WHERE LastSeenTime > 0 AND LastConnectionTime = 0"
- "Timeout waiting for ATT response, forcing a disconnect."
- "Unhandled infoChangedTypes %d"
- "addDeviceIdentification Device %@ -- Adding Information with VendorID %d ProductID %d chipset %d"
- "deviceInfoChanged DEVICE_INFO_CHANGED_TYPE_SDP"
- "eLinkReady - device has chipsetManufacturerName %d lmpVersion %d"
- "updateClassicDeviceIdentificationData - device has public address %{public}.6P and OUI %{public}.3P"
- "updateClassicDeviceIdentificationData Device Name %s Device address %@"
- "updateClassicDeviceIdentificationData Device address %@ Result %d ChipSet %d LmpVersion %d LmpSubversion %d"
- "updateClassicDeviceIdentificationData Device address %@ no longer present, skipping update"
- "updateLeDeviceIdentificationDataForMetrics - device has chipsetManufacturerName %d lmpVersion %d"
- "updateLeDeviceIdentificationDataForMetrics - device has public address %{public}.6P and OUI %{public}.3P"
- "updateLeDeviceIdentificationDataForMetrics le device has address type Public %d, Resolvable %d, Static %d, NonResolvable %d, Valid %d"

```
