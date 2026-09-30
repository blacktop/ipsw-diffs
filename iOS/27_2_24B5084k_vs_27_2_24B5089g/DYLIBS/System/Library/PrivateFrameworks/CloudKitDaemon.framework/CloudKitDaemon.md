## CloudKitDaemon

> `/System/Library/PrivateFrameworks/CloudKitDaemon.framework/CloudKitDaemon`

```diff

-2720.14.0.0.0
-  __TEXT.__text: 0x3d9030
-  __TEXT.__objc_methlist: 0x3177c
-  __TEXT.__const: 0x4e08
+2720.15.0.0.0
+  __TEXT.__text: 0x3daaa0
+  __TEXT.__objc_methlist: 0x31834
+  __TEXT.__const: 0x4e10
   __TEXT.__swift5_typeref: 0x21a1
-  __TEXT.__oslogstring: 0x32f64
+  __TEXT.__oslogstring: 0x330f8
   __TEXT.__swift5_capture: 0x918
   __TEXT.__constg_swiftt: 0x1ac0
   __TEXT.__swift5_reflstr: 0x1136

   __TEXT.__swift_as_ret: 0x16c
   __TEXT.__swift_as_cont: 0x23c
   __TEXT.__swift5_protos: 0x38
-  __TEXT.__cstring: 0x2b11e
+  __TEXT.__cstring: 0x2b395
   __TEXT.__swift5_mpenum: 0x1c
-  __TEXT.__gcc_except_tab: 0xc894
+  __TEXT.__gcc_except_tab: 0xc988
   __TEXT.__ustring: 0x2c
-  __TEXT.__unwind_info: 0xecb0
+  __TEXT.__unwind_info: 0xed08
   __TEXT.__eh_frame: 0x3ba8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x9a18
+  __DATA_CONST.__const: 0x9a68
   __DATA_CONST.__objc_classlist: 0x14f0
   __DATA_CONST.__objc_catlist: 0x148
   __DATA_CONST.__objc_protolist: 0x220
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x13100
+  __DATA_CONST.__objc_selrefs: 0x13180
   __DATA_CONST.__objc_protorefs: 0xa0
   __DATA_CONST.__objc_superrefs: 0x13c8
   __DATA_CONST.__objc_arraydata: 0x1558
   __DATA_CONST.__got: 0x2090
-  __AUTH_CONST.__const: 0x53a8
-  __AUTH_CONST.__cfstring: 0x238e0
-  __AUTH_CONST.__objc_const: 0x4ae60
+  __AUTH_CONST.__const: 0x5388
+  __AUTH_CONST.__cfstring: 0x23a20
+  __AUTH_CONST.__objc_const: 0x4af20
   __AUTH_CONST.__objc_intobj: 0xcd8
   __AUTH_CONST.__objc_arrayobj: 0x390
   __AUTH_CONST.__objc_dictobj: 0xbe0
   __AUTH_CONST.__auth_got: 0x2310
   __AUTH.__objc_data: 0x5410
   __AUTH.__data: 0x5d8
-  __DATA.__objc_ivar: 0x1a90
+  __DATA.__objc_ivar: 0x1a94
   __DATA.__data: 0x1ef0
   __DATA.__common: 0xa0
-  __DATA_DIRTY.__objc_ivar: 0x1978
+  __DATA_DIRTY.__objc_ivar: 0x1984
   __DATA_DIRTY.__objc_data: 0x83c8
   __DATA_DIRTY.__data: 0x2248
   __DATA_DIRTY.__bss: 0x3880

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 20972
+  Functions: 20995
   Symbols:   3030
-  CStrings:  8514
+  CStrings:  8528
 
CStrings:
+ "Couldn't decrypt ancestor share %@: %@"
+ "Couldn't decrypt the share PCS for fetched zone %@: %@"
+ "Couldn't decrypt the share PCS of zone %@"
+ "Couldn't decrypt the zone PCS for fetched zone %@"
+ "Couldn't decrypt the zone PCS for fetched zone %@: %@"
+ "Couldn't decrypt the zoneish PCS for zone %@"
+ "Couldn't spawn an operation to decrypt fetched ancestor shares"
+ "Decrypting record %@ with the zone PCS supplied for zone %@ instead of fetching it"
+ "FailFirstDecryptWithSuppliedZonePCS"
+ "FailIfZonePCSFetchNeededToDecryptRecord"
+ "Failed to decrypt publicPCS for share %@ on zone %@ using invitedPCS"
+ "Fetch operation was deallocated before its ancestor chain could be wired"
+ "Fetch operation was deallocated before its ancestor shares could be decrypted"
+ "Fetch operation was deallocated before zone %@ could be decrypted"
+ "Fetched an ancestor zone without a zoneID"
+ "Fetched discontinuous ancestors for zone %@: zone %@ has parent %@, which is not the next zone returned, %@"
+ "Missing decrypted share PCS for fetched zone %@; rolling its parent requires the share's invitedPCS"
+ "Missing decrypted share PCS for zone %@"
+ "Missing decrypted zonePCS for fetched zone %@; rolling requires every ancestor zone's PCS"
+ "Missing decrypted zonePCS for zone %@"
+ "Record %@ needed a zone PCS fetch to decrypt, which this test forbids"
+ "Record %@ was failed on its supplied zone PCS by a test hook"
+ "Skipping ancestor PCS processing for zones %@ because encryption is disabled"
+ "Supplied zone PCS for zone %@ has no zoneish PCS but record %@ needs one. Fetching instead"
+ "v40@?0@\"CKRecordZoneID\"8@\"NSArray\"16@\"NSDictionary\"24@\"NSError\"32"
- "Could not decrypt zonePCS for zone %@"
- "Could not decrypt zoneishPCS for zone %@. "
- "Failed to decrypt invitedPCS for share %@ on zone %@ using parent zonePCS. Error:%@"
- "Failed to decrypt publicPCS for share %@ using invitedPCS %@"
- "Failed to decrypt publicPCS for share %@ using invitedPCS %@. Error %@."
- "Fetched ancestor zone is not continuous. Last zone: %@. Last zone's parent ID %@ does not match the current zoneID %@"
- "Fetched discontinuous ancestor array for leaf zone %@. Ancestors:%@"
- "Fetched zone %@ lacks protectionData."
- "We don't have zone PCS data to decrypt for zone %@"
- "Zone:%@. Parent:%@"
- "com.apple.cloudkit.processAncestors"
```
