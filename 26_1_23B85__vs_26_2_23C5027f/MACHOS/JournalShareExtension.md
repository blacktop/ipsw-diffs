## JournalShareExtension

> `/private/var/staged_system_apps/Journal.app/PlugIns/JournalShareExtension.appex/JournalShareExtension`

```diff

-49.40.16.0.0
-  __TEXT.__text: 0xfcdc4
-  __TEXT.__auth_stubs: 0x3cf0
-  __TEXT.__objc_methlist: 0x15f4
-  __TEXT.__cstring: 0x5cf5
-  __TEXT.__const: 0x6474
-  __TEXT.__constg_swiftt: 0x42f4
-  __TEXT.__swift5_typeref: 0x2c76
-  __TEXT.__swift5_fieldmd: 0x216c
+49.60.4.0.0
+  __TEXT.__text: 0xfe44c
+  __TEXT.__auth_stubs: 0x3cd0
+  __TEXT.__objc_methlist: 0x15fc
+  __TEXT.__cstring: 0x5c05
+  __TEXT.__const: 0x64b4
+  __TEXT.__constg_swiftt: 0x431c
+  __TEXT.__swift5_typeref: 0x2c6e
+  __TEXT.__swift5_fieldmd: 0x2184
   __TEXT.__swift5_builtin: 0x294
-  __TEXT.__swift5_reflstr: 0x1c31
+  __TEXT.__swift5_reflstr: 0x1c51
   __TEXT.__swift5_assocty: 0x668
   __TEXT.__swift5_proto: 0x3e4
   __TEXT.__swift5_types: 0x2a4
   __TEXT.__objc_classname: 0x12f
-  __TEXT.__objc_methname: 0x5408
+  __TEXT.__objc_methname: 0x5446
   __TEXT.__objc_methtype: 0x141d
-  __TEXT.__oslogstring: 0x25d4
+  __TEXT.__oslogstring: 0x27e4
   __TEXT.__swift5_capture: 0xf94
   __TEXT.__swift5_protos: 0x44
   __TEXT.__swift_as_entry: 0x160
-  __TEXT.__swift_as_ret: 0x210
+  __TEXT.__swift_as_ret: 0x214
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x2e60
-  __TEXT.__eh_frame: 0x5db0
-  __DATA_CONST.__auth_got: 0x1e78
-  __DATA_CONST.__got: 0x1238
+  __TEXT.__unwind_info: 0x2e78
+  __TEXT.__eh_frame: 0x5e88
+  __DATA_CONST.__auth_got: 0x1e68
+  __DATA_CONST.__got: 0x1230
   __DATA_CONST.__auth_ptr: 0xe40
   __DATA_CONST.__const: 0x54a8
   __DATA_CONST.__objc_classlist: 0x2b0

   __DATA_CONST.__objc_protolist: 0xf8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x80
-  __DATA.__objc_const: 0x4f20
-  __DATA.__objc_selrefs: 0x1b40
-  __DATA.__objc_data: 0x8b00
-  __DATA.__data: 0x6358
+  __DATA.__objc_const: 0x4f60
+  __DATA.__objc_selrefs: 0x1b58
+  __DATA.__objc_data: 0x8b10
+  __DATA.__data: 0x6390
   __DATA.__objc_stublist: 0x40
   __DATA.__bss: 0x6b30
-  __DATA.__common: 0x6d0
+  __DATA.__common: 0x6d8
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accessibility.framework/Accessibility

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: BF546823-1407-3F8A-A6AC-B44499985A03
-  Functions: 3501
+  UUID: 6E686198-F868-3E10-8438-1B5F86660E63
+  Functions: 3503
   Symbols:   479
-  CStrings:  1874
+  CStrings:  1878
 
CStrings:
+ "%@ - can't find video attachments [%{public}s]"
+ "%@ - error creating thumbnail from MKMap [%{public}s]"
+ "%@ - error generating video preview image: %@ [%{public}s]"
+ "%@ - image generated [%{public}s]"
+ "Image created from file [%{public}s]"
+ "Image found in cache [%{public}s]"
+ "Image was not found in cache or in an attachment file. Asset type: %{public}s, Attachments count: %{public}ld [%{public}s]"
+ "Legacy support - Failed to retrieve assetMO based on NSManagedObjectID"
+ "Legacy support - assetID is nil"
+ "Legacy support - can't create image from data (size: %{bytes}ld)"
+ "Legacy support - context is nil"
+ "Legacy support - data attachment [0] is nil"
+ "Legacy support - will try to get image from Core Data"
+ "MKMapSnapshotter: Unable to create Location Preview Map Snapshot with error: %@ [%{public}s]"
+ "ThumbnailCacheOperation"
+ "createdDate"
+ "entryCreatedDate"
+ "entryType"
+ "error creating thumbnail from video preview image [%{public}s]"
+ "error generating route map image [%{public}s]"
+ "generateImage no route info in metadata [%{public}s]"
+ "getImageStoredInFile can't create image from file %s [%{public}s]"
+ "getImageStoredInFile can't find image attachment [%{public}s]"
+ "getImageStoredInFile imageURL is nil [%{public}s]"
+ "no visits data [%{public}s]"
+ "registerUndoWithTarget:selector:object:"
+ "v40@0:8@16:24@32"
- "\n\n-------------------- Asset --------------------\n "
- "\n\n-------------------- Entry --------------------\n "
- "%@ - error creating thumbnail from MKMap"
- "%@ - error generating video preview image: %@"
- "Asset metadata being set to nil"
- "Cache hit."
- "Failed to retrieve assetMO based on NSManagedObjectID"
- "Image file attachment found."
- "Initialized"
- "MKMapSnapshotter: Unable to create Location Preview Map Snapshot with error: %@"
- "Potential data corruption detected"
- "Potential data corruption detected: Asset metadata being set to nil"
- "ThumbnailCacheOperation "
- "Will try to get image from Core Data (legacy support)"
- "assetID is nil"
- "can't create image from data (size: %{bytes}ld)"
- "context is nil"
- "data attachment [0] is nil"
- "did not find image file attachment, attachments.count=%ld"
- "error creating thumbnail from video preview image"
- "error generating route map image"
- "generateImage no route info in metadata"
- "getImageStoredInFile can't create image from %s"
- "no visits data"

```
