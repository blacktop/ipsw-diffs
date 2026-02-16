## JournalNotifications

> `/System/Library/PreferenceBundles/JournalNotifications.bundle/JournalNotifications`

```diff

-49.80.2.0.0
-  __TEXT.__text: 0xc2ca4
-  __TEXT.__auth_stubs: 0x3b00
+49.100.4.0.0
+  __TEXT.__text: 0xb4234
+  __TEXT.__auth_stubs: 0x3960
+  __TEXT.__objc_stubs: 0x3060
   __TEXT.__objc_methlist: 0xabc
-  __TEXT.__cstring: 0x4904
-  __TEXT.__const: 0x8584
-  __TEXT.__constg_swiftt: 0x3eec
-  __TEXT.__swift5_typeref: 0x3a44
-  __TEXT.__swift5_builtin: 0x230
-  __TEXT.__swift5_reflstr: 0x1d1b
-  __TEXT.__swift5_fieldmd: 0x2788
-  __TEXT.__swift5_assocty: 0x850
-  __TEXT.__objc_methname: 0x269e
-  __TEXT.__swift5_proto: 0x5e0
-  __TEXT.__swift5_types: 0x304
-  __TEXT.__oslogstring: 0x1646
-  __TEXT.__swift5_capture: 0x5e8
-  __TEXT.__objc_classname: 0x47
-  __TEXT.__objc_methtype: 0x1ee
-  __TEXT.__swift_as_entry: 0xc8
-  __TEXT.__swift_as_ret: 0xe0
+  __TEXT.__const: 0x8464
+  __TEXT.__constg_swiftt: 0x3e84
+  __TEXT.__swift5_typeref: 0x391e
+  __TEXT.__swift5_builtin: 0x21c
+  __TEXT.__swift5_reflstr: 0x1c2b
+  __TEXT.__swift5_fieldmd: 0x269c
+  __TEXT.__swift5_assocty: 0x838
+  __TEXT.__swift5_proto: 0x5dc
+  __TEXT.__swift5_types: 0x2fc
+  __TEXT.__objc_classname: 0x10f4
+  __TEXT.__objc_methname: 0x3616
+  __TEXT.__oslogstring: 0x1276
+  __TEXT.__cstring: 0x23ef
+  __TEXT.__objc_methtype: 0x4e2
+  __TEXT.__swift5_capture: 0x4b8
+  __TEXT.__swift_as_entry: 0xbc
+  __TEXT.__swift_as_ret: 0xd4
   __TEXT.__swift5_protos: 0x38
   __TEXT.__swift5_mpenum: 0x1c
-  __TEXT.__unwind_info: 0x2598
-  __TEXT.__eh_frame: 0x35b8
-  __DATA_CONST.__auth_got: 0x1d80
-  __DATA_CONST.__got: 0x12f0
-  __DATA_CONST.__auth_ptr: 0xfb8
-  __DATA_CONST.__const: 0x4730
+  __TEXT.__unwind_info: 0x22e0
+  __TEXT.__eh_frame: 0x2e78
+  __DATA_CONST.__auth_got: 0x1cb8
+  __DATA_CONST.__got: 0x12d8
+  __DATA_CONST.__auth_ptr: 0xf80
+  __DATA_CONST.__const: 0x3fc8
   __DATA_CONST.__objc_classlist: 0x218
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA.__objc_const: 0x39b8
-  __DATA.__objc_selrefs: 0xf48
-  __DATA.__objc_data: 0x7888
-  __DATA.__data: 0x6270
-  __DATA.__objc_stublist: 0x40
-  __DATA.__bss: 0xaf30
-  __DATA.__common: 0x4e0
+  __DATA.__objc_const: 0x38c8
+  __DATA.__objc_selrefs: 0xea8
+  __DATA.__objc_data: 0x77e8
+  __DATA.__data: 0x6138
+  __DATA.__objc_stublist: 0x38
+  __DATA.__bss: 0xaeb0
+  __DATA.__common: 0x4b0
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accessibility.framework/Accessibility
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
-  - /usr/lib/swift/libswiftCoreAudio_Private.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 6E7C7EF9-77B2-33D7-A869-70866F3DE817
-  Functions: 3164
-  Symbols:   461
-  CStrings:  1189
+  UUID: C3EB5C04-8583-3BD0-882B-F035A8354485
+  Functions: 2974
+  Symbols:   459
+  CStrings:  1105
 
Symbols:
+ _swift_cvw_initEnumMetadataSinglePayloadWithLayoutString
+ _swift_cvw_singlePayloadEnumGeneric_destructiveInjectEnumTag
+ _swift_cvw_singlePayloadEnumGeneric_getEnumTag
- _NSAdaptiveImageGlyphAttributeName
- _OBJC_CLASS_$_NSMutableAttributedString
- __swift_FORCE_LOAD_$_swiftCoreAudio_Private
- _malloc
- _memset_pattern16
CStrings:
+ "JournalEntryAssetFileAttachmentMO is missing filePath. ID: %{public}s"
+ "JournalNotifications"
+ "Recently Deleted"
- "BATCH_RECORD_DOWNLOAD_QUEUE"
- "Batch record download queue"
- "CustomAttributeProviderConcrete"
- "JournalEntryAssetFileAttachmentMO is missing filePath. ID: %s"
- "JournalNotifications.BatchRecordDownloadOperation"
- "Migrating legacy fields to mergeable attributes (mode: %{public}s) for entry ID %{public}s"
- "Move Asset undo/redo button label"
- "No JournalEntryMO field match for key: %s"
- "No changed fields found from NSManagedObjectContextObjectsDidChange notification."
- "Notified of %ld deletes:"
- "Processing %ld refreshed objects"
- "Processing %ld updated objects"
- "Processing deletion %s"
- "Replacing mergeable text with a non-mergeable string. This will likely result in an incorrect merge. Call `mergeText(_:)` with the relevant `MergeableAttributedString` instead."
- "Replacing mergeable title with a non-mergeable string. This may result in an incorrect merge."
- "Responding to NSManagedObjectContextObjectsDidChange notification: %s"
- "Tracked %s CoreData changes and %s inspected changes to entry with ID %s"
- "Typing undo/redo button label"
- "_TtC20JournalNotifications28BatchRecordDownloadOperation"
- "assetOrdering"
- "batchRecordDownloadQueue"
- "changedValuesForCurrentEvent"
- "enumerateAttributesInRange:options:usingBlock:"
- "flagged"
- "getRed:green:blue:alpha:"
- "isFullyRemoved"
- "isRemovedFromCloud"
- "isUploadedToCloud"
- "length"
- "managedObjectClassName"
- "markUndoPoint"
- "mergeableAttributes changed to nil value for entry %s. This implies an incorrect assignment rather than a merge operation somewhere."
- "multiPinMapUpdateDate"
- "other"
- "parentIDs"
- "performBlockAndWait:"
- "pl_shortURI"
- "prompt"
- "setActionName:"
- "setAttributes:range:"
- "setFlagged:"
- "setIsUploadedToCloud:"
- "setMergeableAttributes:"
- "setPrompt:"
- "systemFontOfSize:"
- "undoable (%s)"
- "uniqueID"
- "v40@?0@\"NSDictionary\"8{_NSRange=QQ}16^B32"

```
