## CascadeSets

> `/System/Library/PrivateFrameworks/CascadeSets.framework/CascadeSets`

```diff

-153.2.0.1.0
-  __TEXT.__text: 0x45c08
-  __TEXT.__auth_stubs: 0x910
-  __TEXT.__objc_methlist: 0x3b80
+153.5.0.2.0
+  __TEXT.__text: 0x46fe4
+  __TEXT.__auth_stubs: 0x960
+  __TEXT.__objc_methlist: 0x3bd8
   __TEXT.__const: 0x198
-  __TEXT.__gcc_except_tab: 0xdb0
-  __TEXT.__cstring: 0x34b6
-  __TEXT.__oslogstring: 0x36ab
+  __TEXT.__gcc_except_tab: 0xe6c
+  __TEXT.__cstring: 0x35a9
+  __TEXT.__oslogstring: 0x3aea
   __TEXT.__dlopen_cstrs: 0x24b
-  __TEXT.__unwind_info: 0x1228
+  __TEXT.__unwind_info: 0x12b0
   __TEXT.__objc_classname: 0xa8c
-  __TEXT.__objc_methname: 0x891a
-  __TEXT.__objc_methtype: 0x1bad
-  __TEXT.__objc_stubs: 0x5f80
-  __DATA_CONST.__got: 0x450
-  __DATA_CONST.__const: 0xfa0
+  __TEXT.__objc_methname: 0x8a49
+  __TEXT.__objc_methtype: 0x1b10
+  __TEXT.__objc_stubs: 0x60e0
+  __DATA_CONST.__got: 0x458
+  __DATA_CONST.__const: 0x10b0
   __DATA_CONST.__objc_classlist: 0x338
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0xd8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1f28
+  __DATA_CONST.__objc_selrefs: 0x1fa0
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x2c8
-  __AUTH_CONST.__auth_got: 0x4a0
-  __AUTH_CONST.__const: 0x1f0
-  __AUTH_CONST.__cfstring: 0x2d40
-  __AUTH_CONST.__objc_const: 0xb348
-  __AUTH_CONST.__objc_intobj: 0x348
+  __AUTH_CONST.__auth_got: 0x4c8
+  __AUTH_CONST.__const: 0x1d0
+  __AUTH_CONST.__cfstring: 0x2e00
+  __AUTH_CONST.__objc_const: 0xb2a0
+  __AUTH_CONST.__objc_intobj: 0x330
   __AUTH_CONST.__objc_floatobj: 0x20
   __AUTH_CONST.__objc_doubleobj: 0x20
-  __AUTH.__objc_data: 0x1e0
   __DATA.__objc_ivar: 0x480
-  __DATA.__data: 0xa20
+  __DATA.__data: 0xa30
   __DATA.__bss: 0x40
-  __DATA_DIRTY.__objc_data: 0x1e50
+  __DATA_DIRTY.__objc_data: 0x2030
   __DATA_DIRTY.__bss: 0xd8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 1682
-  Symbols:   2199
-  CStrings:  2545
+  Functions: 1712
+  Symbols:   2234
+  CStrings:  2591
 
Symbols:
+ _NSPOSIXErrorDomain
+ ___error
+ _getxattr
+ _removexattr
+ _setxattr
+ _strerror
CStrings:
+ "@40@0:8@16C24C28@32"
+ "Active"
+ "Attempting to obtain read access on a tombstoned set"
+ "B16@?0@\"NSNumber\"8"
+ "B28@0:8B16@?20"
+ "B32@0:8Q16^@24"
+ "B52@0:8^@16@24@32B40@?44"
+ "CCDataResource: %!@(MISSING)"
+ "CCDataResourceStatusIsNotDiscoverable received invalid value %!l(MISSING)u"
+ "CCDataResourceStatusToString received invalid value %!l(MISSING)u"
+ "Could not close database connection with error: %!@(MISSING)"
+ "Could not open database connection with error: %!@(MISSING)"
+ "Could not prepare database connection with error: %!@(MISSING)"
+ "Could not remove tombstone xattr for resource: %!@(MISSING), error: %!s(MISSING)"
+ "Could not remove tombstoned resource: %!@(MISSING) with error: %!@(MISSING)"
+ "Could not resolve set for tombstoned resource: %!@(MISSING) with error: %!@(MISSING)"
+ "Could not resolve set identifier for item type %!h(MISSING)u'"
+ "Could not retrieve tombstone xattr for resource: %!@(MISSING), error: %!s(MISSING)"
+ "Could not set tombstone xattr for resource: %!@(MISSING), error: %!s(MISSING)"
+ "DeletePending"
+ "Failed to construct local instance enumerator. %!@(MISSING) error: %!@(MISSING)"
+ "Failed to enumerate provenance rows for tombstoned content: %!@(MISSING)"
+ "Failed to enumerate provenance rows for tombstoned metacontent: %!@(MISSING)"
+ "Local instance enumeration failed. %!@(MISSING) error: %!@(MISSING)"
+ "Resesource: %!@(MISSING), has existing tombstone date: %!@(MISSING), not resetting"
+ "Resource: %!@(MISSING) has no existing tombstone date, not clearing"
+ "Resource: %!@(MISSING) is in state deleting, will purge"
+ "Skipping maintenance for resource: %!@(MISSING) with status: %!@(MISSING)"
+ "Successfully cleared tombstone date for resource: %!@(MISSING)"
+ "Successfully removed tombstoned resource: %!@(MISSING) at path: %!@(MISSING)"
+ "Successfully set tombstone date for resource: %!@(MISSING), date: %!@(MISSING)"
+ "T@\"CCDataResource\",R,N,V_dataResource"
+ "TombstonePending"
+ "Tombstoned"
+ "Unknown - %!l(MISSING)u"
+ "Vv32@0:8Q16@?24"
+ "Vv32@0:8Q16@?<v@?S>24"
+ "_clearTombstoneStatus:"
+ "_createProvenanceSelectCommandFromDeviceRowIdToClockValues:type:state:columns:"
+ "_enumerateLocalInstancesSelectingOnlyUnmodified:usingBlock:"
+ "_tombstoneResource:"
+ "clearTombstoneStatus:"
+ "com.apple.cascade.tombstonedate"
+ "containsIndexesInRange:"
+ "dataResource"
+ "deleteSetWithItemType:descriptors:completion:"
+ "deleteSetWithItemType:descriptors:serviceProvider:completion:"
+ "endSetDonationWithOptions:completion:"
+ "enumerateDataResources:setIdentifier:descriptors:includingTombstoned:usingBlock:"
+ "enumerateKeysAndObjectsUsingBlock:"
+ "enumerateRangesUsingBlock:"
+ "finishWithOptions:error:"
+ "intersectsIndexesInRange:"
+ "markTombstoned:error:"
+ "removeResource:"
+ "removeResource:error:"
+ "resourceStatus"
+ "timeIntervalSinceDate:"
+ "tombstoneDate:"
+ "tombstoneResource:"
+ "v24@?0@\"CCFullSetDonation\"8@\"NSError\"16"
+ "v32@?0@\"NSNumber\"8@\"NSMutableIndexSet\"16^B24"
+ "v32@?0{_NSRange=QQ}8^B24"
- "@52@0:8@16C24@28C36C40@44"
- "B48@0:8^@16@24@32@?40"
- "B60@0:8@\"CCDatabaseSelect\"16Q24Q32B40^@44@?<B@?@\"CCDatabaseValueRow\"^@^B>52"
- "B60@0:8@16Q24Q32B40^@44@?52"
- "B68@0:8@\"CCDatabaseSelect\"16#24Q32Q40B48^@52@?<B@?@\"NSObject<CCDatabaseRecord>\"^@^B>60"
- "B68@0:8@16#24Q32Q40B48^@52@?60"
- "Error during enumeration while checking for tombstoned provenance rows: %!@(MISSING)"
- "Read database batch {offset: %!u(MISSING) batchSize: %!u(MISSING)} total records read: %!u(MISSING)"
- "Returning empty results"
- "Select local instance row returned invalid row: %!@(MISSING), %!@(MISSING)"
- "_createProvenanceSelectCommandFromVector:type:deviceMapping:usingAtomsFromVectorWithState:ignoringAtomsFromVectorWithState:columns:"
- "_deleteLocalInstanceRowId:outProvenanceRowId:"
- "deleteLocalInstanceRowId:"
- "endSetDonation:"
- "enumerateDataResources:setIdentifier:descriptors:usingBlock:"
- "enumerateRecordResultsOfSelect:recordClass:batchSize:offset:enumerateAll:error:usingBlock:"
- "enumerateRowResultsOfSelect:batchSize:offset:enumerateAll:error:usingBlock:"

```
