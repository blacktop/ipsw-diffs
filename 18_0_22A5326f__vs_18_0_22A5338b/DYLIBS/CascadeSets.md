## CascadeSets

> `/System/Library/PrivateFrameworks/CascadeSets.framework/CascadeSets`

```diff

-153.4.0.0.0
-  __TEXT.__text: 0x45a40
-  __TEXT.__auth_stubs: 0x910
-  __TEXT.__objc_methlist: 0x3b30
-  __TEXT.__const: 0x190
-  __TEXT.__gcc_except_tab: 0xe34
-  __TEXT.__cstring: 0x350f
-  __TEXT.__oslogstring: 0x36b9
+153.5.0.3.0
+  __TEXT.__text: 0x47108
+  __TEXT.__auth_stubs: 0x960
+  __TEXT.__objc_methlist: 0x3bd8
+  __TEXT.__const: 0x198
+  __TEXT.__gcc_except_tab: 0xe6c
+  __TEXT.__cstring: 0x35a9
+  __TEXT.__oslogstring: 0x3b70
   __TEXT.__dlopen_cstrs: 0x24b
-  __TEXT.__unwind_info: 0x1228
+  __TEXT.__unwind_info: 0x12b0
   __TEXT.__objc_classname: 0xa8c
-  __TEXT.__objc_methname: 0x88a2
-  __TEXT.__objc_methtype: 0x1ad8
-  __TEXT.__objc_stubs: 0x5f60
-  __DATA_CONST.__got: 0x450
-  __DATA_CONST.__const: 0x1040
+  __TEXT.__objc_methname: 0x8a49
+  __TEXT.__objc_methtype: 0x1b10
+  __TEXT.__objc_stubs: 0x60e0
+  __DATA_CONST.__got: 0x458
+  __DATA_CONST.__const: 0x10b0
   __DATA_CONST.__objc_classlist: 0x338
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0xd8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1f30
+  __DATA_CONST.__objc_selrefs: 0x1fa0
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x2c8
-  __AUTH_CONST.__auth_got: 0x4a0
-  __AUTH_CONST.__const: 0x1f0
-  __AUTH_CONST.__cfstring: 0x2d40
-  __AUTH_CONST.__objc_const: 0xb288
+  __AUTH_CONST.__auth_got: 0x4c8
+  __AUTH_CONST.__const: 0x1d0
+  __AUTH_CONST.__cfstring: 0x2e00
+  __AUTH_CONST.__objc_const: 0xb2a0
   __AUTH_CONST.__objc_intobj: 0x330
   __AUTH_CONST.__objc_floatobj: 0x20
   __AUTH_CONST.__objc_doubleobj: 0x20
   __DATA.__objc_ivar: 0x480
-  __DATA.__data: 0xa20
+  __DATA.__data: 0xa30
   __DATA.__bss: 0x40
   __DATA_DIRTY.__objc_data: 0x2030
   __DATA_DIRTY.__bss: 0xd8

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 1680
-  Symbols:   2194
-  CStrings:  2546
+  Functions: 1713
+  Symbols:   2235
+  CStrings:  2592
 
Symbols:
+ _NSPOSIXErrorDomain
+ ___error
+ _getxattr
+ _removexattr
+ _setxattr
+ _strerror
CStrings:
+ "Active"
+ "Attempting to obtain read access on a tombstoned set"
+ "B32@0:8Q16^@24"
+ "B52@0:8^@16@24@32B40@?44"
+ "CCDataResource: %!@(MISSING)"
+ "CCDataResourceStatusIsNotDiscoverable received invalid value %!l(MISSING)u"
+ "CCDataResourceStatusToString received invalid value %!l(MISSING)u"
+ "Could not begin database transaction with error: %!@(MISSING)"
+ "Could not close database connection with error: %!@(MISSING)"
+ "Could not commit database transaction with error: %!@(MISSING)"
+ "Could not determine a valid resource version for the current set - returning no results from enumeration"
+ "Could not open database connection with error: %!@(MISSING)"
+ "Could not prepare database connection with error: %!@(MISSING)"
+ "Could not remove tombstone xattr for resource: %!@(MISSING), error: %!s(MISSING)"
+ "Could not remove tombstoned resource: %!@(MISSING) with error: %!@(MISSING)"
+ "Could not resolve set for tombstoned resource: %!@(MISSING) with error: %!@(MISSING)"
+ "Could not resolve set identifier for item type %!h(MISSING)u'"
+ "Could not retrieve tombstone xattr for resource: %!@(MISSING), error: %!s(MISSING)"
+ "Could not set tombstone xattr for resource: %!@(MISSING), error: %!s(MISSING)"
+ "DeletePending"
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
+ "_tombstoneResource:"
+ "clearTombstoneStatus:"
+ "com.apple.cascade.tombstonedate"
+ "dataResource"
+ "deleteSetWithItemType:descriptors:completion:"
+ "deleteSetWithItemType:descriptors:serviceProvider:completion:"
+ "endSetDonationWithOptions:completion:"
+ "enumerateDataResources:setIdentifier:descriptors:includingTombstoned:usingBlock:"
+ "finishWithOptions:error:"
+ "markTombstoned:error:"
+ "provenance enumerator was not initialized, returning nil results"
+ "removeResource:"
+ "removeResource:error:"
+ "resourceStatus"
+ "timeIntervalSinceDate:"
+ "tombstoneDate:"
+ "tombstoneResource:"
+ "v24@?0@\"CCFullSetDonation\"8@\"NSError\"16"
- "B48@0:8^@16@24@32@?40"
- "Failed to begin transaction on prepare operation."
- "Failed to commit transaction on prepare operation."
- "beginWithBookmark: has not been invoked"
- "endSetDonation:"
- "enumerateDataResources:setIdentifier:descriptors:usingBlock:"

```
