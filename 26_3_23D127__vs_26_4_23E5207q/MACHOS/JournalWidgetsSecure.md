## JournalWidgetsSecure

> `/private/var/staged_system_apps/Journal.app/PlugIns/JournalWidgetsSecure.appex/JournalWidgetsSecure`

```diff

-49.80.2.0.0
-  __TEXT.__text: 0xd9398
-  __TEXT.__auth_stubs: 0x4290
+49.100.4.0.0
+  __TEXT.__text: 0xcb040
+  __TEXT.__auth_stubs: 0x4100
+  __TEXT.__objc_stubs: 0x25e0
   __TEXT.__objc_methlist: 0x80c
-  __TEXT.__const: 0x95e4
-  __TEXT.__cstring: 0x4e02
-  __TEXT.__constg_swiftt: 0x4490
-  __TEXT.__swift5_typeref: 0x7524
-  __TEXT.__swift5_fieldmd: 0x2890
-  __TEXT.__swift5_builtin: 0x208
-  __TEXT.__swift5_reflstr: 0x1c81
-  __TEXT.__swift5_assocty: 0x960
-  __TEXT.__objc_methname: 0x1c07
-  __TEXT.__oslogstring: 0x15da
-  __TEXT.__swift5_proto: 0x600
-  __TEXT.__swift5_types: 0x34c
+  __TEXT.__const: 0x9474
+  __TEXT.__constg_swiftt: 0x4428
+  __TEXT.__swift5_typeref: 0x7294
+  __TEXT.__swift5_fieldmd: 0x27a4
+  __TEXT.__swift5_builtin: 0x1f4
+  __TEXT.__swift5_reflstr: 0x1b81
+  __TEXT.__swift5_assocty: 0x948
+  __TEXT.__oslogstring: 0x11fa
+  __TEXT.__swift5_proto: 0x5fc
+  __TEXT.__swift5_types: 0x344
+  __TEXT.__objc_classname: 0x11b4
+  __TEXT.__objc_methname: 0x2821
+  __TEXT.__cstring: 0x2b62
+  __TEXT.__objc_methtype: 0x373
   __TEXT.__swift5_protos: 0x38
-  __TEXT.__swift5_capture: 0x594
-  __TEXT.__swift_as_entry: 0xd0
-  __TEXT.__swift_as_ret: 0xe8
+  __TEXT.__swift5_capture: 0x464
+  __TEXT.__swift_as_entry: 0xc4
+  __TEXT.__swift_as_ret: 0xdc
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__objc_classname: 0x26
-  __TEXT.__objc_methtype: 0x119
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0x2820
-  __TEXT.__eh_frame: 0x3814
-  __DATA_CONST.__auth_got: 0x2148
-  __DATA_CONST.__got: 0x1488
-  __DATA_CONST.__auth_ptr: 0x1678
-  __DATA_CONST.__const: 0x4640
+  __TEXT.__unwind_info: 0x2548
+  __TEXT.__eh_frame: 0x311c
+  __DATA_CONST.__auth_got: 0x2088
+  __DATA_CONST.__got: 0x1470
+  __DATA_CONST.__auth_ptr: 0x1628
+  __DATA_CONST.__const: 0x3f00
   __DATA_CONST.__objc_classlist: 0x230
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA.__objc_const: 0x3968
-  __DATA.__objc_selrefs: 0xbb0
-  __DATA.__objc_data: 0x74a8
-  __DATA.__data: 0x7550
-  __DATA.__objc_stublist: 0x40
-  __DATA.__common: 0x620
-  __DATA.__bss: 0xb448
+  __DATA.__objc_const: 0x3878
+  __DATA.__objc_selrefs: 0xb10
+  __DATA.__objc_data: 0x7408
+  __DATA.__data: 0x7420
+  __DATA.__objc_stublist: 0x38
+  __DATA.__bss: 0xb3c8
+  __DATA.__common: 0x5f0
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accessibility.framework/Accessibility
   - /System/Library/Frameworks/AppIntents.framework/AppIntents

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
-  UUID: 123A6214-CCD6-3152-B171-6EB94DF22706
-  Functions: 3435
-  Symbols:   438
-  CStrings:  1057
+  UUID: 3A9F5D23-2645-325B-B558-B31DC747E8D0
+  Functions: 3255
+  Symbols:   437
+  CStrings:  986
 
Symbols:
+ _swift_cvw_initEnumMetadataSinglePayloadWithLayoutString
+ _swift_cvw_singlePayloadEnumGeneric_destructiveInjectEnumTag
+ _swift_cvw_singlePayloadEnumGeneric_getEnumTag
- _NSAdaptiveImageGlyphAttributeName
- _OBJC_CLASS_$_NSMutableAttributedString
- __swift_FORCE_LOAD_$_swiftCoreAudio_Private
- _memset_pattern16
CStrings:
+ "JournalEntryAssetFileAttachmentMO is missing filePath. ID: %{public}s"
+ "JournalWidgetsSecure"
+ "Recently Deleted"
- "BATCH_RECORD_DOWNLOAD_QUEUE"
- "Batch record download queue"
- "CustomAttributeProviderConcrete"
- "JournalEntryAssetFileAttachmentMO is missing filePath. ID: %s"
- "JournalWidgetsSecure.BatchRecordDownloadOperation"
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
- "_TtC20JournalWidgetsSecure28BatchRecordDownloadOperation"
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
