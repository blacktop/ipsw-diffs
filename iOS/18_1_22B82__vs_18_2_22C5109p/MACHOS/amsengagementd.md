## amsengagementd

> `/System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/amsengagementd`

```diff

-6.1.20.2.4
-  __TEXT.__text: 0x1b82e0
-  __TEXT.__auth_stubs: 0x3390
+6.2.8.0.0
+  __TEXT.__text: 0x1abdd8
+  __TEXT.__auth_stubs: 0x3370
   __TEXT.__objc_stubs: 0x1e20
-  __TEXT.__objc_methlist: 0x15dc
-  __TEXT.__const: 0x9228
+  __TEXT.__objc_methlist: 0x1554
+  __TEXT.__const: 0x9038
   __TEXT.__gcc_except_tab: 0xb4
-  __TEXT.__cstring: 0xff3a
-  __TEXT.__oslogstring: 0x112c
+  __TEXT.__cstring: 0xf8ca
+  __TEXT.__oslogstring: 0x111c
   __TEXT.__objc_classname: 0x46b
-  __TEXT.__objc_methname: 0x5920
-  __TEXT.__objc_methtype: 0x16eb
+  __TEXT.__objc_methname: 0x59ab
+  __TEXT.__objc_methtype: 0x1750
   __TEXT.__dlopen_cstrs: 0x104
-  __TEXT.__constg_swiftt: 0x4f60
-  __TEXT.__swift5_typeref: 0x57ef
+  __TEXT.__constg_swiftt: 0x4d6c
+  __TEXT.__swift5_typeref: 0x5731
   __TEXT.__swift5_builtin: 0x280
-  __TEXT.__swift5_reflstr: 0x25e6
-  __TEXT.__swift5_fieldmd: 0x3aec
+  __TEXT.__swift5_reflstr: 0x24a6
+  __TEXT.__swift5_fieldmd: 0x3a04
   __TEXT.__swift5_assocty: 0x620
-  __TEXT.__swift5_proto: 0x810
-  __TEXT.__swift5_types: 0x4bc
-  __TEXT.__swift5_capture: 0x37d8
+  __TEXT.__swift5_proto: 0x800
+  __TEXT.__swift5_types: 0x4ac
+  __TEXT.__swift5_capture: 0x337c
   __TEXT.__swift5_protos: 0x80
   __TEXT.__swift5_mpenum: 0x28
-  __TEXT.__unwind_info: 0x6010
-  __TEXT.__eh_frame: 0xa0e0
-  __DATA_CONST.__auth_got: 0x19d8
+  __TEXT.__unwind_info: 0x5d58
+  __TEXT.__eh_frame: 0x9c08
+  __DATA_CONST.__auth_got: 0x19c8
   __DATA_CONST.__got: 0xc70
-  __DATA_CONST.__auth_ptr: 0xfd0
-  __DATA_CONST.__const: 0xe648
+  __DATA_CONST.__auth_ptr: 0x1040
+  __DATA_CONST.__const: 0xdba8
   __DATA_CONST.__cfstring: 0x820
-  __DATA_CONST.__objc_classlist: 0x3a8
+  __DATA_CONST.__objc_classlist: 0x390
   __DATA_CONST.__objc_catlist: 0x68
   __DATA_CONST.__objc_protolist: 0x360
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x1f0
   __DATA_CONST.__objc_superrefs: 0x30
-  __DATA.__objc_const: 0xaa20
-  __DATA.__objc_selrefs: 0x1ba0
+  __DATA.__objc_const: 0xa798
+  __DATA.__objc_selrefs: 0x1bb8
   __DATA.__objc_ivar: 0x48
-  __DATA.__objc_data: 0x3e78
-  __DATA.__data: 0x8d28
-  __DATA.__bss: 0xebb0
-  __DATA.__common: 0x168
+  __DATA.__objc_data: 0x3ba8
+  __DATA.__data: 0x8a78
+  __DATA.__bss: 0xe9b0
+  __DATA.__common: 0x158
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/Combine.framework/Combine

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 9496
-  Symbols:   1449
-  CStrings:  3035
+  Functions: 9185
+  Symbols:   1448
+  CStrings:  3006
 
Symbols:
+ _OBJC_CLASS_$_AMSTreatmentArea
- _$sSo8NSNumberC10FoundationE14booleanLiteralABSb_tcfC
- _dispatch_async
CStrings:
+ ") VALUES (?,?,?,?,?,?)"
+ "@\"JSValue\"32@0:8@\"JSValue\"16@\"NSDictionary\"24"
+ "ALTER TABLE areas ADD COLUMN cacheable INTEGER;"
+ "Failed to fix engagement directory:"
+ "Fetching areas (identifiers: "
+ "Fixing engagement directory "
+ "SELECT cacheable, identifier, salt, seedBagNamespace, seedDomain, seedType FROM areas WHERE identifier = ?"
+ "areasWithIDs:cachePolicy:completion:"
+ "endDate"
+ "fetchTreatments::"
+ "setCacheable:"
+ "treatmentsForAreas:cachePolicy:startDate:endDate:completion:"
+ "treatmentsForAreas:startDate:endDate:"
+ "v56@0:8@\"NSSet\"16q24@\"NSDate\"32@\"NSDate\"40@?<v@?@\"NSDictionary\"@\"NSError\">48"
+ "v56@0:8@16q24@32@40@?48"
- "$__lazy_storage_$_treatmentStoreServicePromise"
- ", Local force sync value: "
- "CREATE TABLE areas (identifier TEXT, namespace TEXT)"
- "Cache is unavailable"
- "Cached treatments configuration successfully"
- "Caching treatments configuration"
- "Checking if synchronization was forced."
- "DynamicTreatmentsStorageAccessQueue"
- "Failed to cache treatments configuration (error: "
- "Failed to fetch remote treatments configuration (error: "
- "Failed to fetch treatments (error: "
- "Failed to fetch treatments configuration cache (error: "
- "Fetched remote treatments configuration successfully"
- "Fetched treatments ("
- "Fetched treatments configuration cache successfully"
- "Fetching remote treatments configuration"
- "Fetching treatments configuration cache"
- "Force sync bag value: "
- "INSERT INTO areas (identifier, namespace) VALUES (?,?)"
- "INSERT INTO treatments (area, endDate, identifier, startDate) VALUES (?,?,?,?)"
- "SELECT identifier FROM areas WHERE namespace = ?"
- "SELECT identifier, salt, seedBagNamespace, seedDomain, seedType FROM areas WHERE identifier = ?"
- "Synchronization was forced."
- "Synchronized treatments "
- "TreatmentStoreForceSynchronization"
- "TreatmentStoreService Failure"
- "_TtC14amsengagementd24DynamicTreatmentsStorage"
- "_TtC14amsengagementd28DynamicTreatmentStoreService"
- "_TtC14amsengagementd34PreCalculatedTreatmentStoreService"
- "amsengagementd.DynamicTreatmentStoreService"
- "amsengagementd.PreCalculatedTreatmentStoreService"
- "amsengagementd/DynamicTreatmentStoreService.swift"
- "cacheURL"
- "configurationCacheURL"
- "fetchTreatments:"
- "insert(area:for:)"
- "insert(treatment:for:endDate:startDate:)"
- "synchronizeTreatmentsPromise"
- "synchronizeTreatmentsPromiseLock"
- "synchronizeTreatmentsRetryInterval"
- "treatment(for:date:)"
- "treatments-pre-calculation-disabled"
- "treatmentsForAreas:"

```
