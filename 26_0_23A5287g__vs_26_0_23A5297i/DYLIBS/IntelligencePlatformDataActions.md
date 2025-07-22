## IntelligencePlatformDataActions

> `/System/Library/PrivateFrameworks/IntelligencePlatformDataActions.framework/IntelligencePlatformDataActions`

```diff

-151.0.3.0.0
-  __TEXT.__text: 0x2e4e8
-  __TEXT.__auth_stubs: 0x16a0
+153.1.0.0.0
+  __TEXT.__text: 0x307a4
+  __TEXT.__auth_stubs: 0x17a0
   __TEXT.__objc_methlist: 0x1bc
-  __TEXT.__const: 0x1cc8
-  __TEXT.__cstring: 0x13dc
+  __TEXT.__const: 0x1ce8
+  __TEXT.__cstring: 0x14cc
   __TEXT.__constg_swiftt: 0xa90
-  __TEXT.__swift5_typeref: 0xc74
-  __TEXT.__swift5_reflstr: 0xc13
-  __TEXT.__swift5_fieldmd: 0xef0
+  __TEXT.__swift5_typeref: 0xcf8
+  __TEXT.__swift5_reflstr: 0xc63
+  __TEXT.__swift5_fieldmd: 0xefc
   __TEXT.__swift5_builtin: 0xb4
   __TEXT.__swift5_assocty: 0x258
   __TEXT.__swift5_proto: 0x100
   __TEXT.__swift5_types: 0xd0
-  __TEXT.__oslogstring: 0xb08
+  __TEXT.__oslogstring: 0xd41
   __TEXT.__swift_as_entry: 0x34
   __TEXT.__swift5_capture: 0x114
   __TEXT.__swift5_protos: 0x10
   __TEXT.__swift_as_ret: 0x2c
-  __TEXT.__unwind_info: 0xce8
-  __TEXT.__eh_frame: 0x14f0
+  __TEXT.__unwind_info: 0xd10
+  __TEXT.__eh_frame: 0x1530
   __TEXT.__objc_methname: 0x33a
-  __DATA_CONST.__got: 0x2e0
+  __DATA_CONST.__got: 0x300
   __DATA_CONST.__const: 0x168
   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x178
   __DATA_CONST.__objc_protorefs: 0x8
-  __AUTH_CONST.__auth_got: 0xb50
+  __AUTH_CONST.__auth_got: 0xbd0
   __AUTH_CONST.__const: 0x1570
   __AUTH_CONST.__objc_const: 0xa30
   __AUTH.__objc_data: 0x408
   __AUTH.__data: 0xcb0
-  __DATA.__data: 0x670
+  __DATA.__data: 0x6c8
   __DATA.__bss: 0x1e00
   __DATA.__common: 0x58
   - /System/Library/Frameworks/AppIntents.framework/AppIntents

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: D088C586-7D9E-3CDE-AB1D-D314D325A901
-  Functions: 1302
-  Symbols:   171
-  CStrings:  218
+  UUID: EBD89BD8-134D-3581-81E6-A9AD02B1E288
+  Functions: 1352
+  Symbols:   174
+  CStrings:  228
 
Symbols:
+ _swift_bridgeObjectRelease_n
+ _swift_initStackObject
+ _swift_setDeallocating
CStrings:
+ "    SELECT\n        SA.bundleIdentifier,\n        SA.isApplication,\n        SUM(SA.duration) AS totalDuration\n    FROM ScreentimeActivity AS SA\n    WHERE 1"
+ "$__lazy_storage_$_appInfoCache"
+ "$__lazy_storage_$_dataSource"
+ "$__lazy_storage_$_dataStore"
+ "DeviceActivityHelpers: Failed to authorize DeviceActivity framework. Query is returning empty results"
+ "DeviceActivityHelpers: Local user identifier not found. Returning default device"
+ "DeviceActivityHelpers: No devices found for current user. Assuming local device as default."
+ "DeviceActivityHelpers: No user information provided, skipping"
+ "DeviceActivityHelpers: Refreshed segments: %s"
+ "DeviceActivityHelpers: Refreshing local activity as local device is queried."
+ "SportsAction: Could not create event for %{sensitive}s"
+ "SportsAction: Failed to create team from SQL for %s"
+ "SportsAction: Games array is empty for: %{sensitive}s and found events: %{sensitive}s"
+ "SportsAction: games found: %{sensitive}s"
+ "SportsEvent: Event %{sensitive}s has %ld teams instead of 2"
+ "SportsEvent: Event %{sensitive}s is earlier than yesterday: %s"
+ "SportsEvent: Event has an empty ID"
+ "SportsTeam: Cannot initialize with empty name for team with id:%{sensitive}s"
+ "SportsTeam: Team has an empty ID"
- "AppInfoCache is not initialized. Query is returning empty results. This might result in missing metadata for non-installed apps"
- "DeviceActivityDataSource is not initialized. Query is returning empty results"
- "Failed to authorize DeviceActivity framework. DeviceActivity data will not be available."
- "Failed to authorize DeviceActivity framework. Query is returning empty results"
- "No user information provided, skipping"
- "Refreshing local activity as local device is queried."
- "appInfoCache"
- "dataSource"
- "dataStore"

```
