## assistantd

> `filesystem/System/Library/PrivateFrameworks/AssistantServices.framework/assistantd`

```diff

-3525.5.9.1.1
-  __TEXT.__text: 0x39439c
+3525.5.11.0.0
+  __TEXT.__text: 0x395bd0
   __TEXT.__auth_stubs: 0x3600
-  __TEXT.__objc_stubs: 0x46460
-  __TEXT.__objc_methlist: 0x22fb8
+  __TEXT.__objc_stubs: 0x46480
+  __TEXT.__objc_methlist: 0x22fe8
   __TEXT.__const: 0x10c58
   __TEXT.__dlopen_cstrs: 0x99d
-  __TEXT.__gcc_except_tab: 0x4810
-  __TEXT.__cstring: 0x51b1d
-  __TEXT.__oslogstring: 0x42d20
+  __TEXT.__gcc_except_tab: 0x4894
+  __TEXT.__cstring: 0x51bff
+  __TEXT.__oslogstring: 0x4319b
   __TEXT.__objc_classname: 0x5331
-  __TEXT.__objc_methname: 0x5f901
+  __TEXT.__objc_methname: 0x5fa21
   __TEXT.__objc_methtype: 0xfaa1
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0xa898
+  __TEXT.__unwind_info: 0xa8c8
   __TEXT.__eh_frame: 0x48
   __DATA_CONST.__auth_got: 0x1b10
   __DATA_CONST.__got: 0x3be0
   __DATA_CONST.__auth_ptr: 0x20
-  __DATA_CONST.__const: 0x13f28
+  __DATA_CONST.__const: 0x14038
   __DATA_CONST.__cfstring: 0x12ba0
   __DATA_CONST.__objc_classlist: 0xd40
   __DATA_CONST.__objc_catlist: 0x630

   __DATA_CONST.__objc_dictobj: 0x2f8
   __DATA_CONST.__objc_doubleobj: 0x30
   __DATA_CONST.__objc_floatobj: 0x30
-  __DATA.__objc_const: 0x34438
-  __DATA.__objc_selrefs: 0x14ff8
-  __DATA.__objc_ivar: 0x25e0
+  __DATA.__objc_const: 0x34498
+  __DATA.__objc_selrefs: 0x15020
+  __DATA.__objc_ivar: 0x25e8
   __DATA.__objc_data: 0x8480
   __DATA.__data: 0x5b88
   __DATA.__bss: 0xd88

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libresolv.9.dylib
   - /usr/lib/libz.1.dylib
-  UUID: DF46B61E-AC3C-3793-9899-6AAE35552FF7
-  Functions: 14432
+  UUID: BCD25D06-D98A-32C6-90B8-4FEB23388E05
+  Functions: 14442
   Symbols:   2940
-  CStrings:  30125
+  CStrings:  30159
 
CStrings:
+ "%s  Starting a fetch for zoneinfo: %@ zoneName: %@"
+ "%s Adding zone for iCloudAltDSID: %@, ZoneName: %@, ZoneInfo: %@"
+ "%s Calling _fetchChangesWithZoneInfo for recordZoneInfo: %@"
+ "%s Created new zone for iCloudAltDSID: %@, ZoneName: %@, ZoneInfo: %@"
+ "%s Current owner mapping: "
+ "%s Existing zones for iCloudAltDSID: %@"
+ "%s Fetching changes for zone %@  zoneinfo: %@, dsid %{private}@"
+ "%s Fetching changes for zoneName:%@, zoneInfo: %@"
+ "%s Mapped ownerName %{private}@ → altDSID %{private}@ → zoneInfo %{private}@"
+ "%s No iCloudAltDSID found for container: %@"
+ "%s No zone info found for dsid %{private}@ zoneName %@"
+ "%s Pre existing zone for iCloudAltDSID: %@, ZoneName: %@, ZoneInfo: %@"
+ "%s Resetting _secondaryZoneInfoByDSID and _ckOwnerNameToAltDSID"
+ "%s Unable to start a fetch when a fetch is already in progress for container %@, zoneName: %@, zoneinfo: %@"
+ "%s Updated zones for iCloudAltDSID: %@"
+ "%s Using primary user recordZoneInfo."
+ "%s ZoneName: %@, ZoneInfo: %@"
+ "%s altDSID %{private}@ → zoneInfo %{private}@ -> container %{private}@"
+ "%s ckOwnerName: %{private}@ : iCloudAltDSID: %{private}@"
+ "%s iCloudAltDSID: %@, accountInfo: %@"
+ "%s isCloudKitSecondaryZoneRoutingEnabled is disabled, the fallback mechanism will pick first entry for primary user"
+ "-[ADCloudKitManager _handleCloudKitNotification:]_block_invoke"
+ "-[ADCloudKitManager _handleSubscriptionNotification:container:]_block_invoke"
+ "-[ADCloudKitManager _setupZonesForSecondaryAccount:container:acctInfo:]_block_invoke"
+ "70"
+ "B32@?0@\"NSString\"8@\"NSString\"16^B24"
+ "MobileAssistantDaemons-3525.5.11"
+ "T@\"NSMutableDictionary\",&,N,V_ckOwnerNameToAltDSID"
+ "T@\"NSMutableDictionary\",&,N,V_secondaryZoneInfoByDSID"
+ "_ckOwnerNameToAltDSID"
+ "_secondaryZoneInfoByDSID"
+ "ckOwnerNameToAltDSID"
+ "isCloudKitSecondaryZoneRoutingEnabled"
+ "secondaryZoneInfoByDSID"
+ "setCkOwnerNameToAltDSID:"
+ "setSecondaryZoneInfoByDSID:"
+ "v32@?0@\"NSString\"8@\"ADCloudKitRecordZoneInfo\"16^B24"
- "%s Unable to start a fetch when a fetch is already in progress for container %@, zoneName: %@"
- "-[ADCloudKitManager _setupZonesForSecondaryAccount:container:acctInfo:]_block_invoke_2"
- "MobileAssistantDaemons-3525.5.9.1.1"

```
