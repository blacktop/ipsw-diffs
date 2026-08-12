## CloudKitDaemon

> `/System/Library/PrivateFrameworks/CloudKitDaemon.framework/CloudKitDaemon`

```diff

-2710.116.0.0.0
-  __TEXT.__text: 0x3dacf0
-  __TEXT.__objc_methlist: 0x3156c
+2710.119.0.0.0
+  __TEXT.__text: 0x3dce8c
+  __TEXT.__objc_methlist: 0x316d4
   __TEXT.__const: 0x4c18
   __TEXT.__swift5_typeref: 0x1f5f
-  __TEXT.__oslogstring: 0x32470
+  __TEXT.__oslogstring: 0x3275f
   __TEXT.__swift5_capture: 0x8a4
   __TEXT.__constg_swiftt: 0x1a80
   __TEXT.__swift5_reflstr: 0x1106

   __TEXT.__swift_as_ret: 0x108
   __TEXT.__swift_as_cont: 0x198
   __TEXT.__swift5_protos: 0x38
-  __TEXT.__cstring: 0x2b130
+  __TEXT.__cstring: 0x2b0d5
   __TEXT.__swift5_mpenum: 0x1c
-  __TEXT.__gcc_except_tab: 0xc7dc
+  __TEXT.__gcc_except_tab: 0xc86c
   __TEXT.__ustring: 0x2c
-  __TEXT.__unwind_info: 0xce78
+  __TEXT.__unwind_info: 0xcf10
   __TEXT.__eh_frame: 0x3178
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x99e8
-  __DATA_CONST.__objc_classlist: 0x14d8
+  __DATA_CONST.__objc_classlist: 0x14e8
   __DATA_CONST.__objc_catlist: 0x148
   __DATA_CONST.__objc_protolist: 0x220
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x12ff0
+  __DATA_CONST.__objc_selrefs: 0x130b0
   __DATA_CONST.__objc_protorefs: 0xa0
-  __DATA_CONST.__objc_superrefs: 0x13b8
+  __DATA_CONST.__objc_superrefs: 0x13c8
   __DATA_CONST.__objc_arraydata: 0x1558
-  __DATA_CONST.__got: 0x2038
-  __AUTH_CONST.__const: 0x51c8
-  __AUTH_CONST.__cfstring: 0x23820
-  __AUTH_CONST.__objc_const: 0x4ab70
-  __AUTH_CONST.__objc_intobj: 0xcc0
+  __DATA_CONST.__got: 0x2040
+  __AUTH_CONST.__const: 0x51e8
+  __AUTH_CONST.__cfstring: 0x238c0
+  __AUTH_CONST.__objc_const: 0x4ad60
+  __AUTH_CONST.__objc_intobj: 0xcd8
   __AUTH_CONST.__objc_arrayobj: 0x390
   __AUTH_CONST.__objc_dictobj: 0xbe0
   __AUTH_CONST.__auth_got: 0x2178
-  __AUTH.__objc_data: 0x5300
+  __AUTH.__objc_data: 0x53a0
   __AUTH.__data: 0x5b0
-  __DATA.__objc_ivar: 0x1a88
-  __DATA.__data: 0x1da8
+  __DATA.__objc_ivar: 0x1a8c
+  __DATA.__data: 0x1dc8
   __DATA.__bss: 0x31a0
   __DATA.__common: 0xa0
-  __DATA_DIRTY.__objc_ivar: 0x1964
+  __DATA_DIRTY.__objc_ivar: 0x1970
   __DATA_DIRTY.__objc_data: 0x83c8
   __DATA_DIRTY.__data: 0x2268
   __DATA_DIRTY.__bss: 0x3880

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 20633
-  Symbols:   2947
-  CStrings:  8460
+  Functions: 20664
+  Symbols:   2949
+  CStrings:  8475
 
Symbols:
+ _OBJC_CLASS_$_CKDMMCSRequestOptions
+ _OBJC_METACLASS_$_CKDMMCSRequestOptions
CStrings:
+ "(%@) addZoneID:withParentZoneID: failed with SQLite database error: %@"
+ "(%@) addZoneID:withParentZoneID: ignoring self-parent relation for zone %@"
+ "(%@) ancestorZoneShareIDsForZoneID failed with SQLite database error: %@"
+ "(%@) ancestorZoneShareIDsForZoneID: cycle detected at rowID %@"
+ "(%@) ancestorZoneShareIDsForZoneID: walk exceeded max depth %lu"
+ "(%@) hasParentRecordForRecordID failed with SQLite database error: %@"
+ "(%@) hasParentZoneForZoneID failed with SQLite database error: %@"
+ "(%@) removeParentForZoneID failed with SQLite database error: %@"
+ ", governingShareRecordID=%@"
+ "Couldn't serialize rolled zone PCS for zone %@. Error: %@"
+ "Couldn't serialize rolled zoneish PCS for zone %@. Error: %@"
+ "Error removing previous parent PCS from zone %@. Error: %@"
+ "Error rolling zonePCS for zone %@"
+ "GoverningShareRecordID"
+ "Rolled zone PCS for zone %@ during zone save (ancestor PCS processing was skipped)."
+ "Rolling existing zone %@ due to reparenting to %@ (shared on either side; re-keying to revoke any cached access)"
+ "Self got deallocated while determining ancestor PCS processing"
+ "Skipping key rolling for zone %@: unshared before and after reparent"
+ "Zone-wide share fetch completed without returning every requested record"
+ "ZoneHierarchyTable"
+ "childZoneRowID"
+ "parentZoneRowID"
+ "removeChildrenWithParentZoneRowID"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CloudKitTools/Sources/CloudKitDaemon/Accounts/CKDAccountDataSecurityObserver.m"
- "Attempted to fetch manatee status on incorrect persona. expected: %@, got: %@"
- "Attempted to fetch walrus status on incorrect persona. expected: %@, got: %@"
- "Could not fetch parent PCS for zone %@ while checking whether reparent rolling is needed."
- "Error removing previous parent PCS from zone %@: %@"
- "Rolling existing zone %@ due to reparenting to %@"
- "Self got deallocated while fetching PCS for zone %@"
- "Self got deallocated while fetching parent PCS for zone %@"
```
