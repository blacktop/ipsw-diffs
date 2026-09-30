## FeedbackCore

> `/System/Library/PrivateFrameworks/FeedbackCore.framework/FeedbackCore`

```diff

-187.0.0.0.0
-  __TEXT.__text: 0x140c58
-  __TEXT.__auth_stubs: 0x2c60
-  __TEXT.__objc_methlist: 0xb4d0
+189.0.0.0.0
+  __TEXT.__text: 0x141594
+  __TEXT.__auth_stubs: 0x2c70
+  __TEXT.__objc_methlist: 0xb540
   __TEXT.__const: 0x2df4
-  __TEXT.__cstring: 0xc041
-  __TEXT.__oslogstring: 0xa166
+  __TEXT.__cstring: 0xc101
+  __TEXT.__oslogstring: 0xa196
   __TEXT.__gcc_except_tab: 0x1bec
   __TEXT.__ustring: 0xe6
   __TEXT.__dlopen_cstrs: 0x62

   __TEXT.__swift5_types: 0x13c
   __TEXT.__swift5_capture: 0xcb8
   __TEXT.__swift5_protos: 0x8
-  __TEXT.__unwind_info: 0x4a60
+  __TEXT.__unwind_info: 0x4a90
   __TEXT.__eh_frame: 0x1680
   __TEXT.__objc_classname: 0x11c9
-  __TEXT.__objc_methname: 0x1ce3e
+  __TEXT.__objc_methname: 0x1cfee
   __TEXT.__objc_methtype: 0x3dc2
-  __TEXT.__objc_stubs: 0x14b40
-  __DATA_CONST.__got: 0x11d8
-  __DATA_CONST.__const: 0x3f10
+  __TEXT.__objc_stubs: 0x14c60
+  __DATA_CONST.__got: 0x11f8
+  __DATA_CONST.__const: 0x3f60
   __DATA_CONST.__objc_classlist: 0x530
   __DATA_CONST.__objc_catlist: 0xc0
   __DATA_CONST.__objc_protolist: 0x238
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x74d8
+  __DATA_CONST.__objc_selrefs: 0x7530
   __DATA_CONST.__objc_protorefs: 0x98
   __DATA_CONST.__objc_superrefs: 0x288
   __DATA_CONST.__objc_arraydata: 0x4d0
-  __AUTH_CONST.__auth_got: 0x1640
-  __AUTH_CONST.__const: 0x44c8
+  __AUTH_CONST.__auth_got: 0x1648
+  __AUTH_CONST.__const: 0x45f0
   __AUTH_CONST.__cfstring: 0x8e00
   __AUTH_CONST.__objc_const: 0x1d508
   __AUTH_CONST.__objc_intobj: 0x300

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 53A88FA9-6F67-3EE5-90AC-CB50270A64D2
-  Functions: 7266
-  Symbols:   15528
-  CStrings:  9316
+  UUID: 9A9F8236-03B0-3C52-9D74-DE2E801F58E6
+  Functions: 7281
+  Symbols:   15564
+  CStrings:  9341
 
Symbols:
+ -[FBKFileCollector _conditionalDebuggingAroundImageAttachingCode:]
+ -[FBKFileCollector _finishAddingImageWithData:attachment:imageURL:]
+ -[FBKFileCollector _preferredRegisteredContentImageTypeForProvider:]
+ -[FBKFileCollector _prepareToAttachImageWithUTType:completion:]
+ -[FBKFileCollector getUniqueFileNameForAttachmentType:utType:]
+ -[FBKFileCollector newAttachmentWithType:utType:]
+ -[UIViewController(Spinner) fbk_setToolbarItemsHidden:animated:]
+ GCC_except_table43
+ GCC_except_table73
+ _OBJC_CLASS_$_UTType
+ _UIContentSizeCategoryAccessibilityExtraLarge
+ _UIContentSizeCategoryAccessibilityLarge
+ _UTTypeImage
+ _UTTypePNG
+ __CLASS_METHODS__TtC12FeedbackCore25FBKTableSectionHeaderView
+ ___44-[FBKFileCollector _attachURL:toAttachment:]_block_invoke.115
+ ___44-[FBKFileCollector addFileFromItemProvider:]_block_invoke.73
+ ___45-[FBKFileCollector addImageWithItemProvider:]_block_invoke.58
+ ___45-[FBKFileCollector addImageWithItemProvider:]_block_invoke_3
+ ___45-[FBKFileCollector addImageWithItemProvider:]_block_invoke_3.cold.1
+ ___45-[FBKFileCollector addVideoFromItemProvider:]_block_invoke.67
+ ___50-[FBKFileCollector commitWithForm:withCompletion:]_block_invoke.103
+ ___62-[FBKFileCollector getUniqueFileNameForAttachmentType:utType:]_block_invoke
+ ___62-[FBKFileCollector getUniqueFileNameForAttachmentType:utType:]_block_invoke_2
+ ___64-[FBKFileCollector processFileFromURL:movingFile:forAttachment:]_block_invoke.75
+ ___64-[FBKFileCollector processFileFromURL:movingFile:forAttachment:]_block_invoke.82
+ ___67-[FBKFileCollector _finishAddingImageWithData:attachment:imageURL:]_block_invoke
+ ___67-[FBKFileCollector _finishAddingImageWithData:attachment:imageURL:]_block_invoke_2
+ ___67-[FBKFileCollector _finishAddingImageWithData:attachment:imageURL:]_block_invoke_2.cold.1
+ ___70-[FBKFileCollector attachLocalFiles:withRequirements:shouldCopyFiles:]_block_invoke.44
+ ___79+[FBKFileCollector findExistingFilesForFilerForm:matcherPredicates:completion:]_block_invoke.52
+ ___block_descriptor_56_e8_32s40s48s_e33_v24?0"FBKAttachment"8"NSURL"16ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56s_e28_v24?0"NSData"8"NSError"16ls32l8s40l8s48l8s56l8
+ ___block_descriptor_80_e8_32s40s48s56s64s72s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8
+ ___block_literal_global.105
+ ___block_literal_global.109
+ ___block_literal_global.113
+ ___block_literal_global.70
+ ___block_literal_global.85
+ ___block_literal_global.99
+ ___swift_memcpy0_1
+ _objc_msgSend$_conditionalDebuggingAroundImageAttachingCode:
+ _objc_msgSend$_finishAddingImageWithData:attachment:imageURL:
+ _objc_msgSend$_preferredRegisteredContentImageTypeForProvider:
+ _objc_msgSend$_prepareToAttachImageWithUTType:completion:
+ _objc_msgSend$fbk_setToolbarItemsHidden:animated:
+ _objc_msgSend$getUniqueFileNameForAttachmentType:utType:
+ _objc_msgSend$loadDataRepresentationForContentType:completionHandler:
+ _objc_msgSend$newAttachmentWithType:utType:
+ _objc_msgSend$preferredFilenameExtension
+ _objc_msgSend$registeredContentTypesConformingToContentType:
+ _objc_msgSend$typeWithIdentifier:
- GCC_except_table36
- ___44-[FBKFileCollector _attachURL:toAttachment:]_block_invoke.108
- ___44-[FBKFileCollector addFileFromItemProvider:]_block_invoke.72
- ___45-[FBKFileCollector addImageWithItemProvider:]_block_invoke.61
- ___45-[FBKFileCollector addImageWithItemProvider:]_block_invoke.62
- ___45-[FBKFileCollector addImageWithItemProvider:]_block_invoke.cold.1
- ___45-[FBKFileCollector addImageWithItemProvider:]_block_invoke_2.cold.1
- ___45-[FBKFileCollector addVideoFromItemProvider:]_block_invoke.64
- ___50-[FBKFileCollector commitWithForm:withCompletion:]_block_invoke.96
- ___55-[FBKFileCollector getUniqueFileNameForAttachmentType:]_block_invoke
- ___55-[FBKFileCollector getUniqueFileNameForAttachmentType:]_block_invoke_2
- ___64-[FBKFileCollector processFileFromURL:movingFile:forAttachment:]_block_invoke.74
- ___64-[FBKFileCollector processFileFromURL:movingFile:forAttachment:]_block_invoke.81
- ___70-[FBKFileCollector attachLocalFiles:withRequirements:shouldCopyFiles:]_block_invoke.47
- ___79+[FBKFileCollector findExistingFilesForFilerForm:matcherPredicates:completion:]_block_invoke.55
- ___block_descriptor_56_e8_32s40s48s_e45_v24?0"<NSItemProviderReading>"8"NSError"16ls32l8s40l8s48l8
- ___block_literal_global.102
- ___block_literal_global.104
- ___block_literal_global.69
- ___block_literal_global.84
- ___block_literal_global.98
- _objc_msgSend$getUniqueFileNameForAttachmentType:
- _objc_msgSend$loadObjectOfClass:completionHandler:
- _xmlFree
CStrings:
+ "."
+ ".%@"
+ "?"
+ "@\"FBKQuestionGroup\""
+ "@\"OBPrivacyLinkController\""
+ "@\"UIImage\""
+ "Preparing to add photo of content type %@"
+ "Will add photo [%{public}@]"
+ "_conditionalDebuggingAroundImageAttachingCode:"
+ "_finishAddingImageWithData:attachment:imageURL:"
+ "_preferredRegisteredContentImageTypeForProvider:"
+ "_prepareToAttachImageWithUTType:completion:"
+ "fbk_setToolbarItemsHidden:animated:"
+ "feedback editor for form response [%lu] change to state [%{public}@]"
+ "getUniqueFileNameForAttachmentType:utType:"
+ "loadDataRepresentationForContentType:completionHandler:"
+ "newAttachmentWithType:utType:"
+ "preferredFilenameExtension"
+ "public.heif-standard"
+ "registeredContentTypesConformingToContentType:"
+ "shouldPinCustomHeader"
+ "typeWithIdentifier:"
+ "v24@?0@\"FBKAttachment\"8@\"NSURL\"16"
+ "v24@?0@\"NSData\"8@\"NSError\"16"
- ".mov"
- ".png"
- "Will add image [%{public}@]"
- "_%.2d%@"
- "feedback editor for form [%li] change to state [%{public}@]"
- "loadObjectOfClass:completionHandler:"
- "v24@?0@\"<NSItemProviderReading>\"8@\"NSError\"16"

```
