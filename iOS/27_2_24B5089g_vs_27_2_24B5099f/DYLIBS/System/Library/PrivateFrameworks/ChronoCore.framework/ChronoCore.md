## ChronoCore

> `/System/Library/PrivateFrameworks/ChronoCore.framework/ChronoCore`

```diff

-749.2.7.0.0
-  __TEXT.__text: 0x41b02c
+749.2.12.0.0
+  __TEXT.__text: 0x41ba18
   __TEXT.__objc_methlist: 0x1f28
-  __TEXT.__const: 0x14a48
-  __TEXT.__cstring: 0x6e8b
-  __TEXT.__oslogstring: 0x164e7
+  __TEXT.__const: 0x14a18
+  __TEXT.__cstring: 0x6edb
+  __TEXT.__oslogstring: 0x164c7
   __TEXT.__gcc_except_tab: 0x70
   __TEXT.__dlopen_cstrs: 0x7a
-  __TEXT.__constg_swiftt: 0xbec4
-  __TEXT.__swift5_typeref: 0xc4e8
+  __TEXT.__constg_swiftt: 0xbed4
+  __TEXT.__swift5_typeref: 0xc4b8
   __TEXT.__swift5_reflstr: 0xacdf
   __TEXT.__swift5_fieldmd: 0x8098
   __TEXT.__swift5_builtin: 0x1b8

   __TEXT.__swift5_proto: 0xb6c
   __TEXT.__swift5_types: 0x688
   __TEXT.__swift5_protos: 0x230
-  __TEXT.__swift5_capture: 0x5640
+  __TEXT.__swift5_capture: 0x5634
   __TEXT.__swift_as_entry: 0x18c
-  __TEXT.__swift_as_ret: 0x17c
-  __TEXT.__swift_as_cont: 0x368
+  __TEXT.__swift_as_ret: 0x178
+  __TEXT.__swift_as_cont: 0x360
   __TEXT.__swift5_mpenum: 0x30
-  __TEXT.__unwind_info: 0x9888
-  __TEXT.__eh_frame: 0xcb40
+  __TEXT.__unwind_info: 0x98d0
+  __TEXT.__eh_frame: 0xcc58
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_protorefs: 0x178
   __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__got: 0x1e08
-  __AUTH_CONST.__const: 0x13b48
+  __AUTH_CONST.__const: 0x13ad8
   __AUTH_CONST.__cfstring: 0x60
   __AUTH_CONST.__objc_const: 0x18ab0
-  __AUTH_CONST.__auth_got: 0x4590
+  __AUTH_CONST.__auth_got: 0x4598
   __AUTH.__objc_data: 0x11a8
-  __AUTH.__data: 0x1958
+  __AUTH.__data: 0x1858
   __DATA.__objc_ivar: 0x14
-  __DATA.__data: 0x3580
-  __DATA.__common: 0xd0
-  __DATA_DIRTY.__objc_data: 0x3a08
-  __DATA_DIRTY.__data: 0x104f8
-  __DATA_DIRTY.__bss: 0x99b0
-  __DATA_DIRTY.__common: 0x918
+  __DATA.__data: 0x3370
+  __DATA.__common: 0xc0
+  __DATA_DIRTY.__objc_data: 0x3a10
+  __DATA_DIRTY.__data: 0x10808
+  __DATA_DIRTY.__bss: 0xa030
+  __DATA_DIRTY.__common: 0x928
   - /System/Library/Frameworks/AccessoryLiveActivities.framework/AccessoryLiveActivities
   - /System/Library/Frameworks/AccessoryNotifications.framework/AccessoryNotifications
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 11217
-  Symbols:   4511
-  CStrings:  2018
+  Functions: 11227
+  Symbols:   4509
+  CStrings:  2020
 
Symbols:
+ ___swift_closure_destructor.138Tm
+ ___swift_closure_destructor.157Tm
+ ___swift_closure_destructor.54Tm
- ___swift_closure_destructor.151Tm
- ___swift_closure_destructor.169Tm
- ___swift_closure_destructor.38Tm
- ___swift_closure_destructor.41Tm
- _symbolic _____y______y______y_____y_____y_____GG_____GGG 7Combine10PublishersO16RemoveDuplicatesV AC9MergeManyV AA12AnyPublisherV 14ChronoServices20DeviceScopedIdentityV AJ15TypedIdentifierV AJ0O4TypeO10WidgetHostO s5NeverO
CStrings:
+ "%{public}s is already in the limited allow-list for accessory %{public}s"
+ "Accessory(ies) %{public}s are still registered to %{public}s after refreshing DeviceAccess - forwarding will not work for them until DeviceAccess migrates the companion app"
+ "AccessoryLiveActivities"
+ "Added %{public}s to the limited allow-list for accessory %{public}s without changing its authorization state"
+ "DeviceAccessMigrationIncomplete"
+ "Error refreshing devices: %{public}@"
+ "Failed to add %{public}s to the remembered authorizations for accessory %{public}s: %{public}@"
+ "Failed to refresh DeviceAccess state for %{public}s: %{public}@ - migrating our own authorizations anyway"
+ "Ignoring device refresh because initial device fetch has not completed"
+ "Refreshed %{public}ld of %{public}ld requested accessory(ies); not reported by DeviceAccess: %{public}s"
+ "refreshDevices(forAccessoryIDs:)"
- "Device %{public}s is no longer reported by DeviceAccess, removing it"
- "Error reconciling devices after app migration: %{public}@"
- "Failed to add %{public}s to the limited authorizations for accessory %{public}s: %{public}@"
- "Failed to reconcile DeviceAccess state before replacing %{public}s: %{public}@ - abandoning the migration rather than writing stale state back to DeviceAccess"
- "Ignoring device reconcile because initial device fetch has not completed"
- "Reconciled devices after app migration: %{public}ld fetched, %{public}ld added, %{public}ld updated, %{public}ld removed"
- "Skipping accessory %{public}s - authorization state %{public}s has no limited allow-list to migrate"
- "Skipping accessory %{public}s - still registered to %{public}s, so DeviceAccess did not migrate the companion app"
- "reconcileAfterAppMigration()"
```
