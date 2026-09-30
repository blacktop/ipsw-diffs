## ShareKit

> `/System/Library/PrivateFrameworks/ShareKit.framework/Versions/A/ShareKit`

```diff

-2130.10.2.1.5
-  __TEXT.__text: 0x76050
-  __TEXT.__objc_methlist: 0x5a44
+2131.20.65.1.1
+  __TEXT.__text: 0x770b8
+  __TEXT.__objc_methlist: 0x5b24
   __TEXT.__const: 0x20c
-  __TEXT.__cstring: 0x45fb
+  __TEXT.__cstring: 0x4737
   __TEXT.__gcc_except_tab: 0x13e0
-  __TEXT.__oslogstring: 0x62ba
+  __TEXT.__oslogstring: 0x635e
   __TEXT.__ustring: 0x128
   __TEXT.__dlopen_cstrs: 0x52
-  __TEXT.__unwind_info: 0x2200
+  __TEXT.__unwind_info: 0x2248
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x3b0
-  __DATA_CONST.__objc_classlist: 0x258
+  __DATA_CONST.__objc_classlist: 0x260
   __DATA_CONST.__objc_catlist: 0x70
   __DATA_CONST.__objc_protolist: 0x108
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x47d8
+  __DATA_CONST.__objc_selrefs: 0x4840
   __DATA_CONST.__objc_protorefs: 0x50
-  __DATA_CONST.__objc_superrefs: 0x1a0
+  __DATA_CONST.__objc_superrefs: 0x1a8
   __DATA_CONST.__objc_arraydata: 0x68
-  __DATA_CONST.__got: 0x918
-  __AUTH_CONST.__const: 0x2e30
-  __AUTH_CONST.__cfstring: 0x4c60
-  __AUTH_CONST.__objc_const: 0xae40
+  __DATA_CONST.__got: 0x920
+  __AUTH_CONST.__const: 0x2e90
+  __AUTH_CONST.__cfstring: 0x4d40
+  __AUTH_CONST.__objc_const: 0xb0d0
   __AUTH_CONST.__objc_doubleobj: 0x70
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0x12c0
-  __AUTH.__data: 0x138
-  __DATA.__objc_ivar: 0x55c
+  __AUTH.__objc_data: 0x1310
+  __AUTH.__data: 0x140
+  __DATA.__objc_ivar: 0x574
   __DATA.__data: 0xce0
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x4b0

   - /System/Library/PrivateFrameworks/ViewBridge.framework/Versions/A/ViewBridge
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2547
-  Symbols:   6239
-  CStrings:  1245
+  Functions: 2573
+  Symbols:   6295
+  CStrings:  1255
 
Symbols:
+ +[NSSharingPlugInHelper _asyncExtractFromExtensionItem:wantsTextItems:wantsFileURLItems:wantsDistantURLs:wantsImages:wantsCKShareProviders:treatImagesAsFileURLItems:wantsOrderedItems:completionHandler:]
+ +[SHKOrderedContentItem fileItemWithFileURL:]
+ +[SHKOrderedContentItem supportsSecureCoding]
+ +[SHKOrderedContentItem textItemWithText:]
+ +[SHKOrderedContentItem urlItemWithURLString:]
+ -[SHKMessagesLaunchEventContext orderedContentItems]
+ -[SHKOrderedContentItem .cxx_destruct]
+ -[SHKOrderedContentItem _initWithKind:text:urlString:fileURL:]
+ -[SHKOrderedContentItem encodeWithCoder:]
+ -[SHKOrderedContentItem fileURL]
+ -[SHKOrderedContentItem initWithCoder:]
+ -[SHKOrderedContentItem kind]
+ -[SHKOrderedContentItem text]
+ -[SHKOrderedContentItem urlString]
+ -[SHKSharingServicePicker _repopulateCollaborativeServicesIfPublicCollaborationChanged:]
+ -[SHKSharingServicePicker isPublicCollaborationForServices]
+ -[SHKSharingServicePicker setIsPublicCollaborationForServices:]
+ GCC_except_table57
+ OBJC_IVAR_$_SHKMessagesLaunchEventContext._orderedContentItems
+ OBJC_IVAR_$_SHKOrderedContentItem._fileURL
+ OBJC_IVAR_$_SHKOrderedContentItem._kind
+ OBJC_IVAR_$_SHKOrderedContentItem._text
+ OBJC_IVAR_$_SHKOrderedContentItem._urlString
+ OBJC_IVAR_$_SHKSharingServicePicker._isPublicCollaborationForServices
+ _CKAllowedSharingOptionsFunction
+ _OBJC_CLASS_$_SHKOrderedContentItem
+ _OBJC_METACLASS_$_SHKOrderedContentItem
+ __202+[NSSharingPlugInHelper _asyncExtractFromExtensionItem:wantsTextItems:wantsFileURLItems:wantsDistantURLs:wantsImages:wantsCKShareProviders:treatImagesAsFileURLItems:wantsOrderedItems:completionHandler:]_block_invoke
+ __OBJC_$_CLASS_METHODS_SHKOrderedContentItem
+ __OBJC_$_CLASS_PROP_LIST_SHKOrderedContentItem
+ __OBJC_$_INSTANCE_METHODS_SHKOrderedContentItem
+ __OBJC_$_INSTANCE_VARIABLES_SHKOrderedContentItem
+ __OBJC_$_PROP_LIST_SHKOrderedContentItem
+ __OBJC_CLASS_PROTOCOLS_$_SHKOrderedContentItem
+ __OBJC_CLASS_RO_$_SHKOrderedContentItem
+ __OBJC_METACLASS_RO_$_SHKOrderedContentItem
+ ___202+[NSSharingPlugInHelper _asyncExtractFromExtensionItem:wantsTextItems:wantsFileURLItems:wantsDistantURLs:wantsImages:wantsCKShareProviders:treatImagesAsFileURLItems:wantsOrderedItems:completionHandler:]_block_invoke
+ ___202+[NSSharingPlugInHelper _asyncExtractFromExtensionItem:wantsTextItems:wantsFileURLItems:wantsDistantURLs:wantsImages:wantsCKShareProviders:treatImagesAsFileURLItems:wantsOrderedItems:completionHandler:]_block_invoke_2
+ ___202+[NSSharingPlugInHelper _asyncExtractFromExtensionItem:wantsTextItems:wantsFileURLItems:wantsDistantURLs:wantsImages:wantsCKShareProviders:treatImagesAsFileURLItems:wantsOrderedItems:completionHandler:]_block_invoke_3
+ ___202+[NSSharingPlugInHelper _asyncExtractFromExtensionItem:wantsTextItems:wantsFileURLItems:wantsDistantURLs:wantsImages:wantsCKShareProviders:treatImagesAsFileURLItems:wantsOrderedItems:completionHandler:]_block_invoke_4
+ ___block_descriptor_104_e8_32s40s48s56s64s72s80s88s96bs_e5_v8?0l
+ ___block_descriptor_40_e8_32bs_e94_v64?0"NSArray"8"NSArray"16"NSArray"24"NSArray"32"NSArray"40"NSDictionary"48"NSArray"56l
+ ___block_descriptor_56_e8_32s40s_e28_v16?0"NSAttributedString"8l
+ ___block_descriptor_58_e8_32s40s48bs_e5_v8?0l
+ ___block_descriptor_89_e8_32s40s48s56s64s_e15_v16?0"NSURL"8l
+ ___copy_helper_block_e8_32s40s48s56s64s72s80s88s96b
+ ___destroy_helper_block_e8_32s40s48s56s64s72s80s88s96s
+ _classCKAllowedSharingOptions
+ _getCKAllowedSharingOptionsClass
+ _initCKAllowedSharingOptions
+ _objc_msgSend$_asyncExtractFromExtensionItem:wantsTextItems:wantsFileURLItems:wantsDistantURLs:wantsImages:wantsCKShareProviders:treatImagesAsFileURLItems:wantsOrderedItems:completionHandler:
+ _objc_msgSend$_initWithKind:text:urlString:fileURL:
+ _objc_msgSend$_repopulateCollaborativeServicesIfPublicCollaborationChanged:
+ _objc_msgSend$fileItemWithFileURL:
+ _objc_msgSend$isAnyoneWithLinkSharingAvailable
+ _objc_msgSend$isCollaborationItemPrivateShare:
+ _objc_msgSend$isPublicCollaborationForServices
+ _objc_msgSend$kind
+ _objc_msgSend$orderedContentItems
+ _objc_msgSend$setIsPublicCollaborationForServices:
+ _objc_msgSend$textItemWithText:
+ _objc_msgSend$urlItemWithURLString:
+ _objc_msgSend$urlString
+ initCKAllowedSharingOptions
- GCC_except_table49
- __184+[NSSharingPlugInHelper _asyncExtractFromExtensionItem:wantsTextItems:wantsFileURLItems:wantsDistantURLs:wantsImages:wantsCKShareProviders:treatImagesAsFileURLItems:completionHandler:]_block_invoke
- ___184+[NSSharingPlugInHelper _asyncExtractFromExtensionItem:wantsTextItems:wantsFileURLItems:wantsDistantURLs:wantsImages:wantsCKShareProviders:treatImagesAsFileURLItems:completionHandler:]_block_invoke_2
- ___184+[NSSharingPlugInHelper _asyncExtractFromExtensionItem:wantsTextItems:wantsFileURLItems:wantsDistantURLs:wantsImages:wantsCKShareProviders:treatImagesAsFileURLItems:completionHandler:]_block_invoke_3
- ___184+[NSSharingPlugInHelper _asyncExtractFromExtensionItem:wantsTextItems:wantsFileURLItems:wantsDistantURLs:wantsImages:wantsCKShareProviders:treatImagesAsFileURLItems:completionHandler:]_block_invoke_4
- ___block_descriptor_57_e8_32s40s48bs_e5_v8?0l
- ___block_descriptor_72_e8_32s40s48s56s_e15_v16?0"NSURL"8l
- ___block_descriptor_96_e8_32s40s48s56s64s72s80s88bs_e5_v8?0l
CStrings:
+ "Access option changed, isPublicCollaboration: %@"
+ "CKAllowedSharingOptions"
+ "Decoded SHKOrderedContentItem with unknown kind: %ld"
+ "Failed to resolve bookmark data for SHKOrderedContentItem: %@"
+ "SHARE_LINK_ACCESS_REQUESTS_ALREADY_ON_MESSAGE_NO_PUBLIC_SHARING"
+ "SHARE_LINK_ACCESS_REQUESTS_OFF_MESSAGE_NO_PUBLIC_SHARING"
+ "SHARE_LINK_ACCESS_REQUESTS_UNSUPPORTED_MESSAGE_NO_PUBLIC_SHARING"
+ "fileBookmark"
+ "kind"
+ "orderedContent"
+ "urlString"
+ "v64@?0@\"NSArray\"8@\"NSArray\"16@\"NSArray\"24@\"NSArray\"32@\"NSArray\"40@\"NSDictionary\"48@\"NSArray\"56"
- "TelephonyUtilities"
- "mochiEnabled"
```
