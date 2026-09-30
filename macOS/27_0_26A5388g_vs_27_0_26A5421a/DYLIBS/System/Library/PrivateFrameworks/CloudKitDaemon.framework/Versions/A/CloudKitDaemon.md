## CloudKitDaemon

> `/System/Library/PrivateFrameworks/CloudKitDaemon.framework/Versions/A/CloudKitDaemon`

```diff

-2710.116.0.0.0
-  __TEXT.__text: 0x40a630
-  __TEXT.__objc_methlist: 0x314bc
+2710.120.0.0.0
+  __TEXT.__text: 0x40c9d4
+  __TEXT.__objc_methlist: 0x31624
   __TEXT.__const: 0x4c28
   __TEXT.__swift5_typeref: 0x1f5f
-  __TEXT.__oslogstring: 0x31fe0
+  __TEXT.__oslogstring: 0x322cf
   __TEXT.__swift5_capture: 0x8a4
   __TEXT.__constg_swiftt: 0x1a80
   __TEXT.__swift5_reflstr: 0x1106

   __TEXT.__swift_as_ret: 0x108
   __TEXT.__swift_as_cont: 0x198
   __TEXT.__swift5_protos: 0x38
-  __TEXT.__cstring: 0x2b2d8
+  __TEXT.__cstring: 0x2b253
   __TEXT.__swift5_mpenum: 0x1c
-  __TEXT.__gcc_except_tab: 0xc860
+  __TEXT.__gcc_except_tab: 0xc8f4
   __TEXT.__ustring: 0x2c
-  __TEXT.__unwind_info: 0xc9a8
+  __TEXT.__unwind_info: 0xca40
   __TEXT.__eh_frame: 0x3158
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x2060
-  __DATA_CONST.__objc_classlist: 0x14d0
+  __DATA_CONST.__objc_classlist: 0x14e0
   __DATA_CONST.__objc_catlist: 0x148
   __DATA_CONST.__objc_protolist: 0x220
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x12fb0
+  __DATA_CONST.__objc_selrefs: 0x13070
   __DATA_CONST.__objc_protorefs: 0xa0
-  __DATA_CONST.__objc_superrefs: 0x13b0
+  __DATA_CONST.__objc_superrefs: 0x13c0
   __DATA_CONST.__objc_arraydata: 0x1558
-  __DATA_CONST.__got: 0x2030
-  __AUTH_CONST.__const: 0xd958
-  __AUTH_CONST.__cfstring: 0x236e0
-  __AUTH_CONST.__objc_const: 0x4a9d8
-  __AUTH_CONST.__objc_intobj: 0xcc0
+  __DATA_CONST.__got: 0x2038
+  __AUTH_CONST.__const: 0xd978
+  __AUTH_CONST.__cfstring: 0x23780
+  __AUTH_CONST.__objc_const: 0x4abc8
+  __AUTH_CONST.__objc_intobj: 0xcd8
   __AUTH_CONST.__objc_arrayobj: 0x390
   __AUTH_CONST.__objc_dictobj: 0xbe0
   __AUTH_CONST.__auth_got: 0x1f78
-  __AUTH.__objc_data: 0x5300
+  __AUTH.__objc_data: 0x53a0
   __AUTH.__data: 0x5b0
-  __DATA.__objc_ivar: 0x1a80
-  __DATA.__data: 0x1da8
+  __DATA.__objc_ivar: 0x1a84
+  __DATA.__data: 0x1dc8
   __DATA.__bss: 0x31a0
   __DATA.__common: 0xa0
-  __DATA_DIRTY.__objc_ivar: 0x1960
+  __DATA_DIRTY.__objc_ivar: 0x196c
   __DATA_DIRTY.__objc_data: 0x8378
   __DATA_DIRTY.__data: 0x2228
   __DATA_DIRTY.__bss: 0x3880

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 20806
-  Symbols:   2881
-  CStrings:  8431
+  Functions: 20837
+  Symbols:   2883
+  CStrings:  8446
 
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
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/CloudKitTools/Sources/CloudKitDaemon/Accounts/CKDAccountDataSecurityObserver.m"
- "Attempted to fetch manatee status on incorrect persona. expected: %@, got: %@"
- "Attempted to fetch walrus status on incorrect persona. expected: %@, got: %@"
- "Could not fetch parent PCS for zone %@ while checking whether reparent rolling is needed."
- "Error removing previous parent PCS from zone %@: %@"
- "Rolling existing zone %@ due to reparenting to %@"
- "Self got deallocated while fetching PCS for zone %@"
- "Self got deallocated while fetching parent PCS for zone %@"
```
