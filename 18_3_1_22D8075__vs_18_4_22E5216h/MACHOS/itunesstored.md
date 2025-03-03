## itunesstored

> `/System/Library/PrivateFrameworks/iTunesStore.framework/Support/itunesstored`

```diff

-1451.2.8.0.0
-  __TEXT.__text: 0x2e5e6c
-  __TEXT.__auth_stubs: 0x23e0
-  __TEXT.__objc_stubs: 0x23cc0
-  __TEXT.__objc_methlist: 0xfad0
-  __TEXT.__const: 0x18d30
-  __TEXT.__gcc_except_tab: 0x5870
-  __TEXT.__cstring: 0x10e49
-  __TEXT.__objc_methname: 0x2be86
-  __TEXT.__objc_classname: 0x2839
-  __TEXT.__oslogstring: 0x178ca
-  __TEXT.__objc_methtype: 0x438b
+1451.4.9.0.0
+  __TEXT.__text: 0x2e3e94
+  __TEXT.__auth_stubs: 0x2380
+  __TEXT.__objc_stubs: 0x238a0
+  __TEXT.__objc_methlist: 0x10764
+  __TEXT.__const: 0x18d70
+  __TEXT.__gcc_except_tab: 0x5734
+  __TEXT.__cstring: 0x10803
+  __TEXT.__objc_methname: 0x2b9ff
+  __TEXT.__objc_classname: 0x27b1
+  __TEXT.__oslogstring: 0x173cc
+  __TEXT.__objc_methtype: 0x431d
   __TEXT.__ustring: 0x92
-  __TEXT.__unwind_info: 0x51d0
-  __TEXT.__eh_frame: 0x1d68
-  __DATA_CONST.__auth_got: 0x1208
-  __DATA_CONST.__got: 0x1ef0
-  __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x15c10
-  __DATA_CONST.__cfstring: 0xeca0
-  __DATA_CONST.__objc_classlist: 0xb30
+  __TEXT.__unwind_info: 0x4fe8
+  __TEXT.__eh_frame: 0x1d38
+  __DATA_CONST.__auth_got: 0x11d8
+  __DATA_CONST.__got: 0x1f08
+  __DATA_CONST.__auth_ptr: 0x18
+  __DATA_CONST.__const: 0x15fd0
+  __DATA_CONST.__cfstring: 0xe900
+  __DATA_CONST.__objc_classlist: 0xb08
   __DATA_CONST.__objc_catlist: 0x40
-  __DATA_CONST.__objc_protolist: 0x188
+  __DATA_CONST.__objc_protolist: 0x178
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x810
+  __DATA_CONST.__objc_superrefs: 0x7f8
   __DATA_CONST.__objc_intobj: 0xf90
-  __DATA_CONST.__objc_arraydata: 0xb0
-  __DATA_CONST.__objc_arrayobj: 0x90
+  __DATA_CONST.__objc_arraydata: 0x98
+  __DATA_CONST.__objc_arrayobj: 0x78
   __DATA_CONST.__objc_doubleobj: 0x40
   __DATA_CONST.__objc_dictobj: 0x50
-  __DATA.__objc_const: 0x21b00
-  __DATA.__objc_selrefs: 0xa390
-  __DATA.__objc_ivar: 0x160c
-  __DATA.__objc_data: 0x6fe0
-  __DATA.__data: 0x1758
-  __DATA.__bss: 0x4a8
-  __DATA.__common: 0xa98
+  __DATA.__objc_const: 0x1fa08
+  __DATA.__objc_selrefs: 0xa708
+  __DATA.__objc_ivar: 0x15f0
+  __DATA.__objc_data: 0x6e50
+  __DATA.__data: 0x1698
+  __DATA.__bss: 0x460
+  __DATA.__common: 0xaa0
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 6943
-  Symbols:   1619
-  CStrings:  12017
+  Functions: 6848
+  Symbols:   1612
+  CStrings:  11908
 
Symbols:
+ _OBJC_CLASS_$_SSAMSPurchase
- _OBJC_CLASS_$_AMSPurchase
- _OBJC_METACLASS_$_AMSPurchase
- __os_log_debug_impl
- __os_log_error_impl
- _dispatch_group_create
- _dispatch_group_enter
- _dispatch_group_leave
- _dispatch_group_notify
CStrings:
+ "\x19"
+ "21:27:29"
+ "Feb 25 2025"
+ "lJIqliFcwusu4FxD:be2xk53Wn161LTDz:completion:"
+ "v40@0:8@\"NSArray\"16@\"NSString\"24@?<v@?@\"NSError\">32"
- "\x12"
- "\x1a"
- "%{public}@: Sampling fraud v2 with percentage: %{public}@, duration: %{public}@, result: %{public}@"
- "(?, ?, %i), "
- "-shm"
- "-wal"
- "/System/Library/PrivateFrameworks/CoreODI.framework/CoreODI"
- "21:24:51"
- "?, "
- "@\"ODISession\""
- "@\"PromotedIAPDatabase\""
- "@24@0:8@\"NSCoder\"16"
- "B16@?0@\"PromotedIAPDatabaseTransaction\"8"
- "CREATE TABLE IF NOT EXISTS promoted_iaps_order_table (product_id TEXT, bundle_id TEXT, iap_order INTEGER, pid INTEGER PRIMARY KEY);"
- "CREATE TABLE IF NOT EXISTS promoted_iaps_visibility_table (product_id TEXT, bundle_id TEXT, visibility INTEGER, pid INTEGER PRIMARY KEY);"
- "DELETE FROM promoted_iaps_order_table WHERE bundle_id = ?;"
- "DELETE FROM promoted_iaps_visibility_table WHERE bundle_id = ?;"
- "Error getting data, %@"
- "FraudScore"
- "Got distnoted event: %s with bundle IDs %@: %@"
- "INSERT OR REPLACE INTO promoted_iaps_order_table (product_id, bundle_id, iap_order) VALUES %@;"
- "INSERT OR REPLACE INTO promoted_iaps_visibility_table (product_id, bundle_id, visibility) VALUES (?, ?, %li);"
- "INSERT OR REPLACE INTO promoted_iaps_visibility_table (product_id, bundle_id, visibility, pid) VALUES (?, ?, %li, %@);"
- "Jan  1 2025"
- "NSCoding"
- "NSSecureCoding"
- "ODIAdditionalAttributes"
- "ODISession"
- "PromotedIAPDatabase"
- "PromotedIAPDatabaseSchema"
- "PromotedIAPDatabaseTransaction"
- "PromotedIAPManager"
- "PromotedIAPs.sqlitedb"
- "Returning data"
- "SELECT pid FROM promoted_iaps_visibility_table WHERE product_id = ? AND bundle_id = ?;"
- "SELECT product_id, iap_order FROM promoted_iaps_order_table WHERE bundle_id = ? ORDER BY iap_order ASC;"
- "SELECT product_id, visibility FROM promoted_iaps_visibility_table WHERE bundle_id = ?;"
- "SELECT product_id, visibility FROM promoted_iaps_visibility_table WHERE product_id IN (%@) AND bundle_id = ?;"
- "SSAMSPurchase"
- "T@\"NSString\",C,N,V_mediaType"
- "T@\"ODISession\",&,N,V_odiSession"
- "TB,N,GisPreauthenticated,V_preauthenticated"
- "[%{public}@] Failed updating Promoted IAP Database to version %li"
- "[%{public}@] No Promoted IAP Database migration function for %li => %li"
- "[%{public}@]: (Internal client) Got IAP info for app: %{public}@. Order: %@, hidden product ids: %@, shown product ids: %@"
- "[%{public}@]: Error setting IAP order: %@, for app: %{public}@"
- "[%{public}@]: Error setting IAP visibility: %{public}li, for product: %@, app: %{public}@"
- "[%{public}@]: Got IAP order: %@, for app: %{public}@"
- "[%{public}@]: Got IAP visibility: %@, for app: %{public}@"
- "[%{public}@]: Set IAP order: %@, for app: %{public}@"
- "[%{public}@]: Set IAP visibility: %{public}li, for product: %@, app: %{public}@"
- "[%{public}@]: Timed out getting promoted IAP internal info for bundle id: %@"
- "[%{public}@]: Timed out getting promoted IAP order for bundle id: %@"
- "[%{public}@]: Timed out getting promoted IAP visibility for bundle id: %{public}@, IAP: %@"
- "[%{public}@]: Timed out setting promoted IAP order for bundle id: %@, IAPs: %@"
- "[%{public}@]: Timed out setting promoted IAP visibility for product: %@, app: %{public}@"
- "_createDatabaseDirectory"
- "_mediaType"
- "_odiSession"
- "_shouldEnableDeviceScoringV2"
- "afds-enabled"
- "afds-enabled-v2-ramp"
- "afds-enabled-v2-ramp-duration"
- "bundleIDs"
- "com.apple.amp.all.sp.paidBuyV2"
- "databasePath_11_0_00"
- "decodeBoolForKey:"
- "decodeObjectOfClass:forKey:"
- "encodeBool:forKey:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "error calling getAssessment"
- "getAssessment:"
- "getInfoInternalForApp:completionHandler:"
- "getOrderForIAPsInApp:completionHandler:"
- "getPromotedIAPInfoInternalWithMessage:connection:"
- "getPromotedIAPOrderWithMessage:connection:"
- "getPromotedIAPVisibilityWithMessage:connection:"
- "getUUIDBytes:"
- "getVisibilityForAllIAPsInApp:completionHandler:"
- "getVisibilityForIAPs:app:completionHandler:"
- "initWithCoder:"
- "initWithServiceIdentifier:forDSIDType:"
- "isEqualToPurchase:"
- "isPaidBuyV2"
- "manager:didFinishDeviceTransferPreflight:error:"
- "odiSession"
- "prepare: switching to ODIFLOW"
- "prepareBindingsFromContext:"
- "promoted_iaps.sqlitedb"
- "provideFeedback:"
- "provideFeedbackOnPayloadOutcome:"
- "removeOverridesForApp:completionHandler:"
- "setAttributes:"
- "setDate:"
- "setOdiSession:"
- "setOrderForIAPs:app:completionHandler:"
- "setPromotedIAPOrderWithMessage:connection:"
- "setPromotedIAPVisibilityWithMessage:connection:"
- "setVisibility:forIAP:app:completionHandler:"
- "setWithSet:"
- "supportsSecureCoding"
- "triggerCoreODI"
- "updateWithAdditionalAttributes:"
- "v24@0:8@\"NSCoder\"16"
- "v24@?0@\"cBEET4QRedIfcDrp\"8^B16"
- "v40@0:8@\"MBManager\"16@\"MBDeviceTransferPreflight\"24@\"NSError\"32"
- "v40@?0@\"NSArray\"8@\"NSSet\"16@\"NSSet\"24@\"NSError\"32"
- "v48@0:8q16@24@32@?40"

```
