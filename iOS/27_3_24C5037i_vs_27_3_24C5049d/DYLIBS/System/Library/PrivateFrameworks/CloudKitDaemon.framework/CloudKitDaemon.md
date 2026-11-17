## CloudKitDaemon

> `/System/Library/PrivateFrameworks/CloudKitDaemon.framework/CloudKitDaemon`

```diff

-2730.18.0.0.0
-  __TEXT.__text: 0x3e0da8
-  __TEXT.__objc_methlist: 0x31bb4
+2730.20.0.0.0
+  __TEXT.__text: 0x3e1678
+  __TEXT.__objc_methlist: 0x31c6c
   __TEXT.__const: 0x4e10
   __TEXT.__swift5_typeref: 0x21a1
-  __TEXT.__oslogstring: 0x33abc
+  __TEXT.__oslogstring: 0x33e06
   __TEXT.__swift5_capture: 0x918
   __TEXT.__constg_swiftt: 0x1ac0
   __TEXT.__swift5_reflstr: 0x1136

   __TEXT.__swift_as_ret: 0x16c
   __TEXT.__swift_as_cont: 0x23c
   __TEXT.__swift5_protos: 0x38
-  __TEXT.__cstring: 0x2bbc2
+  __TEXT.__cstring: 0x2babe
   __TEXT.__swift5_mpenum: 0x1c
-  __TEXT.__gcc_except_tab: 0xcb84
+  __TEXT.__gcc_except_tab: 0xcb7c
   __TEXT.__ustring: 0x2c
-  __TEXT.__unwind_info: 0xee70
+  __TEXT.__unwind_info: 0xee78
   __TEXT.__eh_frame: 0x3ba8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x9b58
-  __DATA_CONST.__objc_classlist: 0x1518
+  __DATA_CONST.__const: 0x9ba8
+  __DATA_CONST.__objc_classlist: 0x1510
   __DATA_CONST.__objc_catlist: 0x148
   __DATA_CONST.__objc_protolist: 0x220
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x132c8
+  __DATA_CONST.__objc_selrefs: 0x13340
   __DATA_CONST.__objc_protorefs: 0xa0
   __DATA_CONST.__objc_superrefs: 0x13e0
   __DATA_CONST.__objc_arraydata: 0x1558
-  __DATA_CONST.__got: 0x20c0
+  __DATA_CONST.__got: 0x20b8
   __AUTH_CONST.__const: 0x5388
-  __AUTH_CONST.__cfstring: 0x23f40
-  __AUTH_CONST.__objc_const: 0x4b470
+  __AUTH_CONST.__cfstring: 0x23e80
+  __AUTH_CONST.__objc_const: 0x4b540
   __AUTH_CONST.__objc_intobj: 0xcf0
   __AUTH_CONST.__objc_arrayobj: 0x390
   __AUTH_CONST.__objc_dictobj: 0xbe0
-  __AUTH_CONST.__auth_got: 0x2328
-  __AUTH.__objc_data: 0x53e8
+  __AUTH_CONST.__auth_got: 0x2330
+  __AUTH.__objc_data: 0x5398
   __AUTH.__data: 0x5b0
-  __DATA.__objc_ivar: 0x1a9c
+  __DATA.__objc_ivar: 0x1aa0
   __DATA.__data: 0x1ee0
   __DATA.__common: 0xa0
-  __DATA_DIRTY.__objc_ivar: 0x19ac
+  __DATA_DIRTY.__objc_ivar: 0x19c4
   __DATA_DIRTY.__objc_data: 0x8580
   __DATA_DIRTY.__data: 0x2288
   __DATA_DIRTY.__bss: 0x3900

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 21084
-  Symbols:   3043
-  CStrings:  8608
+  Functions: 21096
+  Symbols:   3042
+  CStrings:  8609
 
Symbols:
+ _PCSFPCopyUpgradedToVersion2
+ _os_unfair_recursive_lock_lock
- _OBJC_CLASS_$_CKDSelfAddedPCSUpgrader
- _OBJC_METACLASS_$_CKDSelfAddedPCSUpgrader
- _os_unfair_recursive_lock_lock_with_options
CStrings:
+ "Can't remove public identities from a nil share"
+ "Cannot verify screening key: the share owner's user ID is unavailable for share %@"
+ "Couldn't upgrade selfAddedPCS to v2: %@"
+ "Failed to remove stale screening key from private share %@ during fetch; returning the fetched share: %@"
+ "Fetch found %lu stale screening key(s) in private share %@ (role %{public}@); saving the share to remove them"
+ "Forced share save failure after PCS serialization for testing"
+ "No selfAddedPCS to upgrade to v2"
+ "Not removing stale screening key from private share %@ during fetch: the enclosing save removes it"
+ "Not removing stale screening key from private share %@: current user is neither owner nor administrator"
+ "PCS couldn't upgrade the selfAddedPCS to v2"
+ "Removed %lu stale screening key(s) from selfAddedPCS of share %@"
+ "Removed %lu stale screening key(s) from selfAddedPCS of share %@ before the removal failed"
+ "Removed stale screening key from private share %@ during fetch"
+ "Saving participant is not the share owner or an administrator for share %@"
+ "Screening key signer user ID taken from the container scoped user ID of the owner of share %@"
+ "Screening key signer user ID taken from the zone owner name of share %@"
+ "Share %@ was switched to private and back to public before saving and is eligible for screening"
+ "TestForceShareSaveFailureAfterPCSSerialization"
+ "Upgraded selfAddedPCS to v2 with %lu private keys, %lu sharees and %lu master key IDs"
+ "Upgrading selfAddedPCS from version %ld to v2"
+ "selfAddedPCS version %ld %{public}@ an upgrade to v2"
- "CKDFetchScreeningKeyURLRequest.m"
- "Can't upgrade a share PCS that is not read-write"
- "Cannot verify screening key: containerScopedUserID unavailable for share %@"
- "Couldn't copy a private key into the v2 share PCS"
- "Couldn't copy a sharee into the v2 share PCS"
- "Couldn't create a v2 share PCS"
- "Couldn't set the current private key of the v2 share PCS"
- "Couldn't upgrade share PCS to v2: %@"
- "Error upgrading selfAddedPCS %@ to v2: %@"
- "No share PCS to upgrade to v2"
- "Saving participant is not the share owner for share %@"
- "Share PCS version %ld %{public}@ an upgrade to v2"
- "The upgraded share PCS has a different current private key"
- "The upgraded share PCS has different private keys"
- "The upgraded share PCS has different sharees or sharee flags"
- "The upgraded share PCS is not v2"
- "Upgraded selfAddedPCS %@ to v2 PCS %@"
- "Upgraded share PCS to v2 with %lu private keys and %lu sharees"
- "Upgrading selfAddedPCS %@ to v2"
- "Upgrading share PCS from version %ld to v2"
```
