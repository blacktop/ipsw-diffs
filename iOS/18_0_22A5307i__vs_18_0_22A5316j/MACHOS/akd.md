## akd

> `/System/Library/PrivateFrameworks/AuthKit.framework/akd`

```diff

-488.2.0.0.0
-  __TEXT.__text: 0x179e9c
-  __TEXT.__auth_stubs: 0x1d70
-  __TEXT.__objc_stubs: 0x16d80
-  __TEXT.__objc_methlist: 0x87fc
+488.6.0.0.0
+  __TEXT.__text: 0x178d7c
+  __TEXT.__auth_stubs: 0x1d40
+  __TEXT.__objc_stubs: 0x16e00
+  __TEXT.__objc_methlist: 0x8814
   __TEXT.__const: 0x2cd0
-  __TEXT.__cstring: 0xa9e3
+  __TEXT.__cstring: 0xaa43
   __TEXT.__objc_classname: 0x181c
-  __TEXT.__objc_methname: 0x203fe
+  __TEXT.__objc_methname: 0x20475
   __TEXT.__objc_methtype: 0x5736
   __TEXT.__gcc_except_tab: 0x2284
   __TEXT.__oslogstring: 0x1efc8
   __TEXT.__dlopen_cstrs: 0x5a
-  __TEXT.__swift5_typeref: 0x1652
+  __TEXT.__swift5_typeref: 0x159a
   __TEXT.__swift5_fieldmd: 0xb6c
-  __TEXT.__constg_swiftt: 0x1190
+  __TEXT.__constg_swiftt: 0x1188
   __TEXT.__swift5_reflstr: 0xae0
   __TEXT.__swift5_assocty: 0x150
-  __TEXT.__swift5_capture: 0x87c
+  __TEXT.__swift5_capture: 0x850
   __TEXT.__swift5_builtin: 0x78
   __TEXT.__swift5_proto: 0x118
   __TEXT.__swift5_types: 0xec
   __TEXT.__swift5_protos: 0x34
   __TEXT.__info_plist: 0x57d
-  __TEXT.__unwind_info: 0x4e30
-  __TEXT.__eh_frame: 0x6dd8
-  __DATA_CONST.__auth_got: 0xec8
-  __DATA_CONST.__got: 0x1580
-  __DATA_CONST.__auth_ptr: 0x460
-  __DATA_CONST.__const: 0xab68
-  __DATA_CONST.__cfstring: 0x6920
+  __TEXT.__unwind_info: 0x4df0
+  __TEXT.__eh_frame: 0x6ce0
+  __DATA_CONST.__auth_got: 0xeb0
+  __DATA_CONST.__got: 0x1560
+  __DATA_CONST.__auth_ptr: 0x430
+  __DATA_CONST.__const: 0xab18
+  __DATA_CONST.__cfstring: 0x6940
   __DATA_CONST.__objc_classlist: 0x6d0
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x2b0

   __DATA_CONST.__linkguard: 0x3e
   __DATA_CONST.__objc_dictobj: 0x118
   __DATA.__objc_const: 0x249f0
-  __DATA.__objc_selrefs: 0x6ba8
+  __DATA.__objc_selrefs: 0x6be0
   __DATA.__objc_ivar: 0x998
-  __DATA.__objc_data: 0x5338
-  __DATA.__data: 0x3a78
+  __DATA.__objc_data: 0x5330
+  __DATA.__data: 0x3a08
   __DATA.__bss: 0x2160
   __DATA.__common: 0x111
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 6467
-  Symbols:   1293
-  CStrings:  9162
+  Functions: 6454
+  Symbols:   1285
+  CStrings:  9170
 
Symbols:
- _$sScG17makeAsyncIteratorScG0C0Vyx_GyF
- _$sScG8IteratorVMn
- _$sScG8IteratorVyx_GScIsMc
- _$sScI4next7ElementQzSgyYaKFTj
- _$sScI4next7ElementQzSgyYaKFTjTu
- _$ss5NeverON
- _$ss5NeverOs5ErrorsWP
- _swift_willThrowTypedImpl
CStrings:
+ "ALTER TABLE authorized_applications ADD COLUMN client_name TEXT;"
+ "Fetcing SIWA accounts from local store for altDSID %!s(MISSING)"
+ "INSERT OR REPLACE INTO authorized_applications (client_id, team_id, scopes, origin, credential_state, transfer_state, primary_client_id, authorizedAppListVersion, creation_date, client_name) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
+ "SELECT client_id, scopes, credential_state, transfer_state, primary_client_id, origin, creation_date, client_name FROM authorized_applications WHERE team_id = ?"
+ "Upgrading database to schema version: 7"
+ "Using WWDR client names for bundleIDs : %!s(MISSING)"
+ "_createV7Database"
+ "_upgradeToSchemaVersion7"
+ "adamID"
+ "isAccountNotProvisioned"
+ "setAppStoreAdamID:"
+ "setClientName:"
- "Error fetching app metadata for bundleID %!s(MISSING) : %!@(MISSING)"
- "Fetcing SIWA accounts from local store"
- "INSERT OR REPLACE INTO authorized_applications (client_id, team_id, scopes, origin, credential_state, transfer_state, primary_client_id, authorizedAppListVersion, creation_date) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"
- "SELECT client_id, scopes, credential_state, transfer_state, primary_client_id, origin, creation_date FROM authorized_applications WHERE team_id = ?"
- "Using bundleID as app name %!s(MISSING)"

```
