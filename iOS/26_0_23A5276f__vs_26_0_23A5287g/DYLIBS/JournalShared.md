## JournalShared

> `/System/Library/PrivateFrameworks/JournalShared.framework/JournalShared`

```diff

-34.0.0.0.0
-  __TEXT.__text: 0xc97e8
-  __TEXT.__auth_stubs: 0x28b0
+39.0.0.0.1
+  __TEXT.__text: 0xccda4
+  __TEXT.__auth_stubs: 0x29d0
   __TEXT.__objc_methlist: 0x2c4
-  __TEXT.__cstring: 0x2214
-  __TEXT.__const: 0x9e68
-  __TEXT.__constg_swiftt: 0x1d6c
-  __TEXT.__swift5_typeref: 0x23d0
+  __TEXT.__cstring: 0x21c4
+  __TEXT.__const: 0x9eb8
+  __TEXT.__constg_swiftt: 0x1d9c
+  __TEXT.__swift5_typeref: 0x2468
   __TEXT.__swift5_builtin: 0xb4
   __TEXT.__swift5_reflstr: 0x1768
   __TEXT.__swift5_fieldmd: 0x2648
   __TEXT.__swift5_assocty: 0x870
-  __TEXT.__swift5_proto: 0x890
+  __TEXT.__swift5_proto: 0x894
   __TEXT.__swift5_types: 0x2a8
-  __TEXT.__swift5_capture: 0xfc
-  __TEXT.__oslogstring: 0x146a
+  __TEXT.__swift5_capture: 0x10c
+  __TEXT.__oslogstring: 0x151a
   __TEXT.__swift5_protos: 0x30
   __TEXT.__swift_as_entry: 0x40
   __TEXT.__swift_as_ret: 0x38
-  __TEXT.__unwind_info: 0x31a8
-  __TEXT.__eh_frame: 0x4078
+  __TEXT.__unwind_info: 0x31b8
+  __TEXT.__eh_frame: 0x44b8
   __TEXT.__objc_classname: 0x44
-  __TEXT.__objc_methname: 0x1362
+  __TEXT.__objc_methname: 0x13d3
   __TEXT.__objc_methtype: 0xeb
-  __DATA_CONST.__got: 0x7a0
-  __DATA_CONST.__const: 0x810
+  __DATA_CONST.__got: 0x7e0
+  __DATA_CONST.__const: 0x820
   __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x898
+  __DATA_CONST.__objc_selrefs: 0x8b8
   __DATA_CONST.__objc_protorefs: 0x28
-  __AUTH_CONST.__auth_got: 0x1458
-  __AUTH_CONST.__const: 0x3d50
-  __AUTH_CONST.__objc_const: 0xe38
+  __AUTH_CONST.__auth_got: 0x14e8
+  __AUTH_CONST.__const: 0x3e48
+  __AUTH_CONST.__objc_const: 0xe58
   __AUTH.__objc_data: 0x8f8
-  __AUTH.__data: 0x24d0
-  __DATA.__data: 0x2ad8
+  __AUTH.__data: 0x2500
+  __DATA.__data: 0x2b88
   __DATA.__objc_stublist: 0x18
   __DATA.__common: 0x100
-  __DATA.__bss: 0x10d70
+  __DATA.__bss: 0x10df0
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Accelerate

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: D101E0F5-432C-314A-9F8E-72C1B5C8D56E
-  Functions: 4412
-  Symbols:   1506
-  CStrings:  711
+  UUID: 8E91077C-36C1-3602-B440-C8328871C917
+  Functions: 4476
+  Symbols:   1518
+  CStrings:  720
 
Symbols:
+ _OBJC_CLASS_$_NSManagedObjectContext
+ _block_copy_helper.30
+ _block_copy_helper.33
+ _block_descriptor.32
+ _block_descriptor.35
+ _block_destroy_helper.31
+ _block_destroy_helper.34
+ _get_witness_table s23AsyncCompactMapSequenceVySo20NSNotificationCenterC10FoundationE13NotificationsCSo22NSManagedObjectContextC13JournalSharedE0J14IDNotificationVGSciHPyHC.3
+ _swift_isClassType
+ _symbolic So15NSManagedObjectCm
+ _symbolic _____Sg 10Foundation16AttributedStringV
+ _symbolic _____Sg_ABt 13JournalShared14MergeableColorO
+ _symbolic ______pXp 13JournalShared15RecordUploadingP
+ _symbolic _____m 13JournalShared12AppStorageMOC
+ _symbolic _____ySo15NSManagedObjectC_G Sh5IndexV
+ _symbolic _____ySo15NSManagedObjectCmG s23_ContiguousArrayStorageC
+ _symbolic _____y__________G s23AsyncCompactMapSequenceV So20NSNotificationCenterC10FoundationE13NotificationsC So22NSManagedObjectContextC13JournalSharedE0J14IDNotificationV
+ _symbolic _____y______pXpG s23_ContiguousArrayStorageC 13JournalShared15RecordUploadingP
+ _symbolic _____y_____mG s23_ContiguousArrayStorageC 13JournalShared03AppC2MOC
- ___swift_memcpy24_8
- _block_copy_helper.25
- _block_copy_helper.28
- _block_descriptor.27
- _block_descriptor.30
- _block_destroy_helper.26
- _block_destroy_helper.29
- _get_witness_table s16AsyncMapSequenceVySo20NSNotificationCenterC10FoundationE13NotificationsCSo22NSManagedObjectContextC13JournalSharedE0I14IDNotificationVGSciHPyHC.3
- _symbolic _____y__________G s16AsyncMapSequenceV So20NSNotificationCenterC10FoundationE13NotificationsC So22NSManagedObjectContextC13JournalSharedE0I14IDNotificationV
CStrings:
+ "Brown"
+ "Deleting all %s records"
+ "Green"
+ "Local JournalMO changes are newer. Requires merging coherence values with record: %{bool}d."
+ "Marking all %ld %s objects for reuploading"
+ "More than one sync data object found"
+ "Remote Journal record changes are newer. Used LWW for non-mergeable fields; has local attributes to merge: %{bool}d."
+ "Unable to get sync data"
+ "_color"
+ "contentsOfDirectoryAtURL:includingPropertiesForKeys:options:error:"
+ "deleteObject:"
+ "objectID"
+ "removeItemAtURL:error:"
- "(%K == false OR %K == nil) AND %K != nil AND id != %@"
- "(isTip == false) OR (isTip == nil)"
- "JournalMO changes are newer. Requires merging coherence values with record: %{bool}d."
- "Record changes are newer. Used LWW for non-mergeable fields; has local attributes to merge: %{bool}d."

```
