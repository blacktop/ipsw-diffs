## NotesAppMigrationExtension

> `/private/var/staged_system_apps/MobileNotes.app/Extensions/NotesAppMigrationExtension.appex/NotesAppMigrationExtension`

```diff

-2952.40.7.0.0
-  __TEXT.__text: 0x7a524
-  __TEXT.__auth_stubs: 0x1c00
+2952.40.10.0.0
+  __TEXT.__text: 0x81128
+  __TEXT.__auth_stubs: 0x1e20
   __TEXT.__objc_methlist: 0x104
-  __TEXT.__cstring: 0xf44
-  __TEXT.__objc_methname: 0x1b28
-  __TEXT.__swift5_typeref: 0x17c1
-  __TEXT.__const: 0x4cc0
-  __TEXT.__constg_swiftt: 0xd3c
+  __TEXT.__cstring: 0x10d4
+  __TEXT.__objc_methname: 0x1ce9
+  __TEXT.__swift5_typeref: 0x1883
+  __TEXT.__const: 0x4fc0
+  __TEXT.__constg_swiftt: 0xd8c
   __TEXT.__swift5_builtin: 0xdc
-  __TEXT.__swift5_reflstr: 0xf62
-  __TEXT.__swift5_fieldmd: 0x19f0
+  __TEXT.__swift5_reflstr: 0x1062
+  __TEXT.__swift5_fieldmd: 0x1ab8
   __TEXT.__swift5_assocty: 0x360
-  __TEXT.__swift5_proto: 0x4f4
-  __TEXT.__swift5_types: 0x158
+  __TEXT.__swift5_proto: 0x524
+  __TEXT.__swift5_types: 0x160
   __TEXT.__swift5_protos: 0xc
+  __TEXT.__swift5_capture: 0x504
   __TEXT.__swift5_mpenum: 0x10
   __TEXT.__oslogstring: 0xe96
-  __TEXT.__swift5_capture: 0x440
   __TEXT.__swift5_entry: 0x8
   __TEXT.__swift_as_entry: 0x24
   __TEXT.__swift_as_ret: 0x20
   __TEXT.__ustring: 0x10
-  __TEXT.__unwind_info: 0x1830
-  __TEXT.__eh_frame: 0x2f08
-  __DATA_CONST.__auth_got: 0xe00
-  __DATA_CONST.__got: 0x5e8
-  __DATA_CONST.__auth_ptr: 0x588
-  __DATA_CONST.__const: 0x3ae0
+  __TEXT.__unwind_info: 0x19d8
+  __TEXT.__eh_frame: 0x31a8
+  __DATA_CONST.__auth_got: 0xf10
+  __DATA_CONST.__got: 0x630
+  __DATA_CONST.__auth_ptr: 0x650
+  __DATA_CONST.__const: 0x3dd8
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0x5a0
-  __DATA.__objc_selrefs: 0xb28
+  __DATA.__objc_selrefs: 0xba8
   __DATA.__objc_data: 0x280
-  __DATA.__data: 0x2108
-  __DATA.__bss: 0x9a80
-  __DATA.__common: 0x72
+  __DATA.__data: 0x2300
+  __DATA.__bss: 0xa080
+  __DATA.__common: 0xa2
   - /System/Library/Frameworks/AppMigrationKit.framework/AppMigrationKit
   - /System/Library/Frameworks/CoreData.framework/CoreData
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/UIKit.framework/UIKit
+  - /System/Library/PrivateFrameworks/InternalSwiftProtobuf.framework/InternalSwiftProtobuf
   - /System/Library/PrivateFrameworks/NotesShared.framework/NotesShared
   - /System/Library/PrivateFrameworks/NotesSupport.framework/NotesSupport
   - /System/Library/PrivateFrameworks/NotesUI.framework/NotesUI

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 518D884C-6189-31E8-A4DC-1EBDE38BF341
-  Functions: 1996
-  Symbols:   247
-  CStrings:  585
+  UUID: A2D3229C-013B-3026-B681-B523AEA7FFB4
+  Functions: 2131
+  Symbols:   249
+  CStrings:  615
 
Symbols:
+ _NSURLFileSizeKey
+ _objc_release_x11
CStrings:
+ "addHashtagToNoteBodyIfMissing:"
+ "audio_attachments_meta"
+ "audio_file_name"
+ "audio_name"
+ "convertTextInNoteBodyToHashtag:"
+ "creation_date_millis_since_epoch"
+ "enumerateAttachmentsInOrderUsingBlock:"
+ "enumerateInlineAttachmentsInOrderUsingBlock:"
+ "enumerateNotesInContext:batchSize:visibleOnly:saveAfterBatch:usingBlock:"
+ "fileExistsAtPath:isDirectory:"
+ "fileURL"
+ "ic_hashtagCharacterString"
+ "ic_stringByTrimmingLeadingCharactersInSet:"
+ "isAudio"
+ "isCallRecording"
+ "is_call_recording"
+ "last_modified_date_millis_since_epoch"
+ "length"
+ "performBlockAndWait:"
+ "recordingSummaryAsPlainText"
+ "setIsCallRecording:"
+ "summary_file_name"
+ "tags"
+ "transcriptAsPlainText"
+ "transcript_file_name"
+ "v24@?0@\"ICNote\"8^B16"
+ "v40@?0@\"ICAttachment\"8{_NSRange=QQ}16^B32"
+ "v40@?0@\"ICInlineAttachment\"8{_NSRange=QQ}16^B32"

```
