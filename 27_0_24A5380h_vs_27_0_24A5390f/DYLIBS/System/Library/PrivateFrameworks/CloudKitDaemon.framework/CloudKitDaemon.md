## CloudKitDaemon

> `/System/Library/PrivateFrameworks/CloudKitDaemon.framework/CloudKitDaemon`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_capture`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH.__data`

```diff

-2710.114.0.0.0
-  __TEXT.__text: 0x3d8d80
-  __TEXT.__objc_methlist: 0x31444
-  __TEXT.__const: 0x4bf8
+2710.116.0.0.0
+  __TEXT.__text: 0x3dacf0
+  __TEXT.__objc_methlist: 0x3156c
+  __TEXT.__const: 0x4c18
   __TEXT.__swift5_typeref: 0x1f5f
-  __TEXT.__oslogstring: 0x322e8
+  __TEXT.__oslogstring: 0x32470
   __TEXT.__swift5_capture: 0x8a4
   __TEXT.__constg_swiftt: 0x1a80
   __TEXT.__swift5_reflstr: 0x1106

   __TEXT.__swift_as_ret: 0x108
   __TEXT.__swift_as_cont: 0x198
   __TEXT.__swift5_protos: 0x38
-  __TEXT.__cstring: 0x2b0de
+  __TEXT.__cstring: 0x2b130
   __TEXT.__swift5_mpenum: 0x1c
-  __TEXT.__gcc_except_tab: 0xc664
+  __TEXT.__gcc_except_tab: 0xc7dc
   __TEXT.__ustring: 0x2c
-  __TEXT.__unwind_info: 0xce40
+  __TEXT.__unwind_info: 0xce78
   __TEXT.__eh_frame: 0x3178
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x99c0
-  __DATA_CONST.__objc_classlist: 0x14d0
+  __DATA_CONST.__const: 0x99e8
+  __DATA_CONST.__objc_classlist: 0x14d8
   __DATA_CONST.__objc_catlist: 0x148
   __DATA_CONST.__objc_protolist: 0x220
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x12f40
+  __DATA_CONST.__objc_selrefs: 0x12ff0
   __DATA_CONST.__objc_protorefs: 0xa0
-  __DATA_CONST.__objc_superrefs: 0x13b0
+  __DATA_CONST.__objc_superrefs: 0x13b8
   __DATA_CONST.__objc_arraydata: 0x1558
   __DATA_CONST.__got: 0x2038
   __AUTH_CONST.__const: 0x51c8
-  __AUTH_CONST.__cfstring: 0x237a0
-  __AUTH_CONST.__objc_const: 0x4a9b0
+  __AUTH_CONST.__cfstring: 0x23820
+  __AUTH_CONST.__objc_const: 0x4ab70
   __AUTH_CONST.__objc_intobj: 0xcc0
   __AUTH_CONST.__objc_arrayobj: 0x390
   __AUTH_CONST.__objc_dictobj: 0xbe0
-  __AUTH_CONST.__auth_got: 0x2168
-  __AUTH.__objc_data: 0x5a30
+  __AUTH_CONST.__auth_got: 0x2178
+  __AUTH.__objc_data: 0x5300
   __AUTH.__data: 0x5b0
-  __DATA.__objc_ivar: 0x1a84
-  __DATA.__data: 0x1df8
+  __DATA.__objc_ivar: 0x1a88
+  __DATA.__data: 0x1da8
   __DATA.__bss: 0x31a0
   __DATA.__common: 0xa0
-  __DATA_DIRTY.__objc_ivar: 0x1950
-  __DATA_DIRTY.__objc_data: 0x7c48
-  __DATA_DIRTY.__data: 0x2218
+  __DATA_DIRTY.__objc_ivar: 0x1964
+  __DATA_DIRTY.__objc_data: 0x83c8
+  __DATA_DIRTY.__data: 0x2268
   __DATA_DIRTY.__bss: 0x3880
   __DATA_DIRTY.__common: 0x10
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 20606
-  Symbols:   2944
-  CStrings:  8446
+  Functions: 20633
+  Symbols:   2947
+  CStrings:  8460
 
Symbols:
+ _CKDPCSExistingFetchOptionsCanSatisfyRequestedOptions
+ _CKLinkCheck67c944b220f944039d015d402e20c1e8
+ _CKStringFromParticipantPermission
+ _OBJC_METACLASS_$_NSFileHandle
- _CKDPCSFetchOptionsCanSatisfyOptions
CStrings:
+ "Clearing only the SQL PCS cache for container %p"
+ "Clearing only the record cache for container %p"
+ "Clearing the SQL PCS cache, leaving the in-memory caches intact"
+ "Could not fetch parent PCS for zone %@ while checking whether reparent rolling is needed."
+ "End traffic log for operation"
+ "Failed to register push token for %@: %@"
+ "Fetch for zone %@ %@ the zone parentPCS"
+ "Missing PCS for zone %@ while aligning parent PCS"
+ "No parent identity found on updated child zone PCS for zone %@ while preparing share %@"
+ "Parent %@ of zone %@ PCS not found in cache, attempting to decrypt via direct share"
+ "Self got deallocated while fetching PCS for zone %@"
+ "Self got deallocated while fetching parent PCS for zone %@"
+ "Skipping ancestor PCS prepping. Operation uses encryption: %@. Container uses zone-wide PCS: %@. Database scope is %@. Save PCS only: %@."
+ "Skipping dependent zone PCS fetch for share %@ to avoid a share/zone fetch cycle"
+ "Skipping parent PCS prep for PCS only zone save."
+ "Skipping push token registration for test container tuple %@"
+ "Skipping push token removal for test container tuple %@"
+ "Skipping push token unregister for test container tuple %@"
+ "Skipping share PCS prep for PCS only zone save."
+ "Skipping zone PCS prep for PCS only zone save."
+ "Traffic log for request "
+ "Updating permission for %@ participant %@ from %{public}@ -> %{public}@ to match the public permission on share %@"
+ "did not request"
+ "requested"
+ "skip-dependent-zone"
- "Detected zone PCS oplock for zone %@ with missing local parent and parent-tagged PCS. Fetching full zone metadata before retry."
- "Failed to fetch zone %@ while recovering from parent-tagged PCS oplock. Continuing with standard retry path. Error: %@"
- "Fetched zone %@ for parent-tagged PCS oplock recovery did not include usable protection data. Falling back to PCS reset and re-fetch."
- "Fetched zone %@ while recovering from parent-tagged PCS oplock did not have a repairable parent. Continuing with standard retry path."
- "Parent %@ of zone %@ PCS not found in cache, attempting share-based decryption"
- "Skipping ancestor PCS prepping. Operation uses encryption: %@. Container uses zone-wide PCS: %@. Database scope is %@. Operation originator is %lu."
- "Unable to fetch zone %@ while recovering from zone PCS oplock"
- "Warn: Failed to register push token for %@: %@"
- "ck26eecl"
- "pcs sharee is incorrectly tagged as parent pcs key"
- "v24@?0@\"CKRecordZone\"8@\"NSError\"16"
```
