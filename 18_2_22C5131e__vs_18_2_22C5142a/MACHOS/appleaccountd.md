## appleaccountd

> `/usr/libexec/appleaccountd`

```diff

-1007.227.1.0.0
-  __TEXT.__text: 0x289be8
+1007.229.4.0.0
+  __TEXT.__text: 0x28c00c
   __TEXT.__auth_stubs: 0x2690
   __TEXT.__objc_methlist: 0x664
-  __TEXT.__objc_methname: 0x40ef
+  __TEXT.__objc_methname: 0x4124
   __TEXT.__objc_classname: 0x20a
   __TEXT.__objc_methtype: 0x1466
-  __TEXT.__cstring: 0x81e4
-  __TEXT.__swift5_typeref: 0x5d89
+  __TEXT.__cstring: 0x8214
+  __TEXT.__swift5_typeref: 0x5da9
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__const: 0xbe90
-  __TEXT.__constg_swiftt: 0x9a48
-  __TEXT.__swift5_reflstr: 0x4fb4
-  __TEXT.__swift5_fieldmd: 0x4f5c
+  __TEXT.__const: 0xbf10
+  __TEXT.__constg_swiftt: 0x9a94
+  __TEXT.__swift5_reflstr: 0x4ff4
+  __TEXT.__swift5_fieldmd: 0x4f84
   __TEXT.__swift5_builtin: 0x1a4
   __TEXT.__swift5_assocty: 0x650
-  __TEXT.__swift5_proto: 0x950
-  __TEXT.__swift5_types: 0x4b4
+  __TEXT.__swift5_proto: 0x958
+  __TEXT.__swift5_types: 0x4b8
   __TEXT.__swift5_protos: 0x1cc
-  __TEXT.__oslogstring: 0x16456
-  __TEXT.__swift5_capture: 0x5474
+  __TEXT.__oslogstring: 0x16636
+  __TEXT.__swift5_capture: 0x5484
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x5370
-  __TEXT.__eh_frame: 0x5cb8
+  __TEXT.__unwind_info: 0x5400
+  __TEXT.__eh_frame: 0x5e40
   __DATA_CONST.__auth_got: 0x1348
-  __DATA_CONST.__got: 0xc28
-  __DATA_CONST.__auth_ptr: 0x1e48
-  __DATA_CONST.__const: 0x10490
+  __DATA_CONST.__got: 0xc38
+  __DATA_CONST.__auth_ptr: 0x1f48
+  __DATA_CONST.__const: 0x10550
   __DATA_CONST.__objc_classlist: 0x4d8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x160

   __DATA_CONST.__objc_protorefs: 0xb0
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA.__objc_const: 0x15208
-  __DATA.__objc_selrefs: 0x11b8
+  __DATA.__objc_selrefs: 0x11c8
   __DATA.__objc_ivar: 0x4
   __DATA.__objc_data: 0x2728
-  __DATA.__data: 0xf710
+  __DATA.__data: 0xf7c0
   __DATA.__objc_stublist: 0x68
-  __DATA.__bss: 0xe280
+  __DATA.__bss: 0xe380
   __DATA.__common: 0x3b0
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 7656
-  Symbols:   1185
-  CStrings:  3250
+  Functions: 7689
+  Symbols:   1187
+  CStrings:  3260
 
Symbols:
+ _OBJC_CLASS_$_NSThread
+ _kAAAnalyticsEventCustodianRecoveryExperimentalRecoveryInfoNotFoundFetchFromCloud
CStrings:
+ "Cloud storage object is not confirm to cloud sync"
+ "Error fetching recovery info from cloud %@"
+ "Fetching changes from shared database failed: %@"
+ "Fetching changes from shared database for container: %s"
+ "New sync delegete set: %s"
+ "Recovery Info record not found. Fetching the record from cloud."
+ "Successfully fetched changes from shared database"
+ "Sync delegate found nil. Obtaining delegate from dependency registry: %s - %s"
+ "callStackSymbols"
+ "fetchRecoveryInfoFromCache()"
+ "fetchSharedRecoveryInfoFromCloud()"
+ "shouldSkipRecoveryInfoRecordStorage"
+ "unsafeSyncDelegate"
- "RCUpsellMiniBuddy"
- "fetchRecoveryInfo(with:)"
- "syncDelegate"

```
