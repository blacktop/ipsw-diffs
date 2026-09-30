## FeedbackCore

> `/System/Library/PrivateFrameworks/FeedbackCore.framework/FeedbackCore`

```diff

-150.12.0.0.0
-  __TEXT.__text: 0x141e88
+150.14.0.0.0
+  __TEXT.__text: 0x14148c
   __TEXT.__auth_stubs: 0x2b20
-  __TEXT.__objc_methlist: 0xb3d0
+  __TEXT.__objc_methlist: 0xb388
   __TEXT.__const: 0x2c14
-  __TEXT.__cstring: 0xbe0c
-  __TEXT.__oslogstring: 0xa0c6
+  __TEXT.__cstring: 0xbd5c
+  __TEXT.__oslogstring: 0xa066
   __TEXT.__gcc_except_tab: 0x1bec
   __TEXT.__ustring: 0xe6
   __TEXT.__dlopen_cstrs: 0x62

   __TEXT.__swift5_types: 0x134
   __TEXT.__swift5_capture: 0xcd8
   __TEXT.__swift5_protos: 0x8
-  __TEXT.__unwind_info: 0x4a08
+  __TEXT.__unwind_info: 0x49e8
   __TEXT.__eh_frame: 0x1640
   __TEXT.__objc_classname: 0x11cb
-  __TEXT.__objc_methname: 0x1c920
+  __TEXT.__objc_methname: 0x1c7b8
   __TEXT.__objc_methtype: 0x3cdc
-  __TEXT.__objc_stubs: 0x148e0
-  __DATA_CONST.__got: 0x1198
-  __DATA_CONST.__const: 0x3f78
+  __TEXT.__objc_stubs: 0x14800
+  __DATA_CONST.__got: 0x1190
+  __DATA_CONST.__const: 0x3f28
   __DATA_CONST.__objc_classlist: 0x528
   __DATA_CONST.__objc_catlist: 0xc0
   __DATA_CONST.__objc_protolist: 0x238
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x73b0
+  __DATA_CONST.__objc_selrefs: 0x7370
   __DATA_CONST.__objc_protorefs: 0x98
   __DATA_CONST.__objc_superrefs: 0x288
   __DATA_CONST.__objc_arraydata: 0x4d0
   __AUTH_CONST.__auth_got: 0x15a0
   __AUTH_CONST.__auth_ptr: 0x930
   __AUTH_CONST.__const: 0x44a8
-  __AUTH_CONST.__cfstring: 0x8e40
+  __AUTH_CONST.__cfstring: 0x8e20
   __AUTH_CONST.__objc_const: 0x1d3c0
   __AUTH_CONST.__objc_intobj: 0x300
   __AUTH_CONST.__objc_dictobj: 0xa0

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 7201
-  Symbols:   15483
-  CStrings:  8139
+  Functions: 7188
+  Symbols:   15447
+  CStrings:  8124
 
Symbols:
+ -[FBKFileCollector addImageWithItemProvider:]
+ GCC_except_table36
+ ___44-[FBKFileCollector _attachURL:toAttachment:]_block_invoke.108
+ ___44-[FBKFileCollector addFileFromItemProvider:]_block_invoke.72
+ ___45-[FBKFileCollector addImageWithItemProvider:]_block_invoke
+ ___45-[FBKFileCollector addImageWithItemProvider:]_block_invoke.61
+ ___45-[FBKFileCollector addImageWithItemProvider:]_block_invoke.62
+ ___45-[FBKFileCollector addImageWithItemProvider:]_block_invoke.cold.1
+ ___45-[FBKFileCollector addImageWithItemProvider:]_block_invoke_2
+ ___45-[FBKFileCollector addImageWithItemProvider:]_block_invoke_2.cold.1
+ ___45-[FBKFileCollector addVideoFromItemProvider:]_block_invoke.64
+ ___45-[FBKFileCollector addVideoFromItemProvider:]_block_invoke.65
+ ___50-[FBKFileCollector commitWithForm:withCompletion:]_block_invoke.96
+ ___55-[FBKFileCollector getUniqueFileNameForAttachmentType:]_block_invoke
+ ___55-[FBKFileCollector getUniqueFileNameForAttachmentType:]_block_invoke_2
+ ___64-[FBKFileCollector processFileFromURL:movingFile:forAttachment:]_block_invoke.74
+ ___64-[FBKFileCollector processFileFromURL:movingFile:forAttachment:]_block_invoke.81
+ ___block_literal_global.102
+ ___block_literal_global.69
+ ___block_literal_global.84
+ ___block_literal_global.92
+ _objc_msgSend$addImageWithItemProvider:
+ _objc_msgSend$getUniqueFileNameForAttachmentType:
- -[FBKFileCollector _conditionalDebuggingAroundImageAttachingCode:]
- -[FBKFileCollector _finishAddingImageWithData:attachment:imageURL:]
- -[FBKFileCollector _prepareToAttachImageWithUTTypeIdentifier:completion:]
- -[FBKFileCollector addHEICPhotoWithItemProvider:]
- -[FBKFileCollector addScreenshotWithItemProvider:]
- -[FBKFileCollector getUniqueFileNameForAttachmentType:utTypeIdentifier:]
- -[FBKFileCollector newAttachmentWithType:utTypeIdentifier:]
- GCC_except_table47
- _UTTypeHEIC
- ___44-[FBKFileCollector _attachURL:toAttachment:]_block_invoke.114
- ___44-[FBKFileCollector addFileFromItemProvider:]_block_invoke.74
- ___45-[FBKFileCollector addVideoFromItemProvider:]_block_invoke.67
- ___45-[FBKFileCollector addVideoFromItemProvider:]_block_invoke.68
- ___49-[FBKFileCollector addHEICPhotoWithItemProvider:]_block_invoke
- ___49-[FBKFileCollector addHEICPhotoWithItemProvider:]_block_invoke.61
- ___49-[FBKFileCollector addHEICPhotoWithItemProvider:]_block_invoke_2
- ___49-[FBKFileCollector addHEICPhotoWithItemProvider:]_block_invoke_3
- ___49-[FBKFileCollector addHEICPhotoWithItemProvider:]_block_invoke_3.cold.1
- ___50-[FBKFileCollector addScreenshotWithItemProvider:]_block_invoke
- ___50-[FBKFileCollector addScreenshotWithItemProvider:]_block_invoke.64
- ___50-[FBKFileCollector addScreenshotWithItemProvider:]_block_invoke_2
- ___50-[FBKFileCollector addScreenshotWithItemProvider:]_block_invoke_3
- ___50-[FBKFileCollector addScreenshotWithItemProvider:]_block_invoke_3.cold.1
- ___50-[FBKFileCollector commitWithForm:withCompletion:]_block_invoke.102
- ___64-[FBKFileCollector processFileFromURL:movingFile:forAttachment:]_block_invoke.76
- ___64-[FBKFileCollector processFileFromURL:movingFile:forAttachment:]_block_invoke.83
- ___67-[FBKFileCollector _finishAddingImageWithData:attachment:imageURL:]_block_invoke
- ___67-[FBKFileCollector _finishAddingImageWithData:attachment:imageURL:]_block_invoke_2
- ___67-[FBKFileCollector _finishAddingImageWithData:attachment:imageURL:]_block_invoke_2.cold.1
- ___72-[FBKFileCollector getUniqueFileNameForAttachmentType:utTypeIdentifier:]_block_invoke
- ___72-[FBKFileCollector getUniqueFileNameForAttachmentType:utTypeIdentifier:]_block_invoke_2
- ___block_descriptor_48_e8_32s40s_e33_v24?0"FBKAttachment"8"NSURL"16ls32l8s40l8
- ___block_descriptor_56_e8_32s40s48s_e28_v24?0"NSData"8"NSError"16ls32l8s40l8s48l8
- ___block_literal_global.108
- ___block_literal_global.110
- ___block_literal_global.112
- ___block_literal_global.71
- ___block_literal_global.86
- _objc_msgSend$_conditionalDebuggingAroundImageAttachingCode:
- _objc_msgSend$_finishAddingImageWithData:attachment:imageURL:
- _objc_msgSend$_prepareToAttachImageWithUTTypeIdentifier:completion:
- _objc_msgSend$addHEICPhotoWithItemProvider:
- _objc_msgSend$addScreenshotWithItemProvider:
- _objc_msgSend$getUniqueFileNameForAttachmentType:utTypeIdentifier:
- _objc_msgSend$loadDataRepresentationForContentType:completionHandler:
- _objc_msgSend$newAttachmentWithType:utTypeIdentifier:
- _objc_msgSend$preferredFilenameExtension
CStrings:
+ "addImageWithItemProvider:"
+ "feedback editor for form [%li] change to state [%{public}@]"
- "-[FBKFileCollector addHEICPhotoWithItemProvider:]"
- "-[FBKFileCollector addScreenshotWithItemProvider:]"
- ".%@"
- "Couldn't load HEIC image with error: [%{public}@]"
- "Will add photo [%{public}@]"
- "_conditionalDebuggingAroundImageAttachingCode:"
- "_finishAddingImageWithData:attachment:imageURL:"
- "_prepareToAttachImageWithUTTypeIdentifier:completion:"
- "addHEICPhotoWithItemProvider:"
- "addScreenshotWithItemProvider:"
- "feedback editor for form response [%lu] change to state [%{public}@]"
- "getUniqueFileNameForAttachmentType:utTypeIdentifier:"
- "loadDataRepresentationForContentType:completionHandler:"
- "newAttachmentWithType:utTypeIdentifier:"
- "preferredFilenameExtension"
- "v24@?0@\"FBKAttachment\"8@\"NSURL\"16"
- "v24@?0@\"NSData\"8@\"NSError\"16"

```
