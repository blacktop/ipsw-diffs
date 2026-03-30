## SafariSharedUI

> `/System/Library/PrivateFrameworks/SafariSharedUI.framework/SafariSharedUI`

```diff

-624.1.16.10.6
-  __TEXT.__text: 0x1251cc
-  __TEXT.__auth_stubs: 0x28c0
+624.2.1.10.1
+  __TEXT.__text: 0x127554
+  __TEXT.__auth_stubs: 0x2960
   __TEXT.__delay_stubs: 0x80
   __TEXT.__delay_helper: 0x14c
-  __TEXT.__objc_methlist: 0xc9ec
-  __TEXT.__const: 0x31c90
-  __TEXT.__gcc_except_tab: 0xf138
-  __TEXT.__oslogstring: 0x9c2d
-  __TEXT.__cstring: 0x118f9
+  __TEXT.__objc_methlist: 0xcafc
+  __TEXT.__const: 0x32110
+  __TEXT.__gcc_except_tab: 0xf16c
+  __TEXT.__oslogstring: 0x9cbd
+  __TEXT.__cstring: 0x119a9
   __TEXT.__ustring: 0x1fc2
   __TEXT.__dlopen_cstrs: 0x363
   __TEXT.__constg_swiftt: 0x57c
-  __TEXT.__swift5_typeref: 0x1c88
+  __TEXT.__swift5_typeref: 0x1cd4
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_reflstr: 0x198
   __TEXT.__swift5_assocty: 0x110
   __TEXT.__swift5_proto: 0x48
   __TEXT.__swift5_types: 0x38
   __TEXT.__swift5_fieldmd: 0x1dc
-  __TEXT.__swift5_capture: 0x3d0
+  __TEXT.__swift5_capture: 0x410
   __TEXT.__swift_as_entry: 0x84
   __TEXT.__swift_as_ret: 0xc4
-  __TEXT.__unwind_info: 0x7678
+  __TEXT.__unwind_info: 0x7708
   __TEXT.__eh_frame: 0x1e44
-  __TEXT.__objc_classname: 0x21b6
-  __TEXT.__objc_methname: 0x2e0af
-  __TEXT.__objc_methtype: 0x627a
-  __TEXT.__objc_stubs: 0x1b520
-  __DATA_CONST.__got: 0x17b0
-  __DATA_CONST.__const: 0x7310
-  __DATA_CONST.__objc_classlist: 0x688
+  __TEXT.__objc_classname: 0x21f6
+  __TEXT.__objc_methname: 0x2e3cf
+  __TEXT.__objc_methtype: 0x629a
+  __TEXT.__objc_stubs: 0x1b680
+  __DATA_CONST.__got: 0x17e0
+  __DATA_CONST.__const: 0x7338
+  __DATA_CONST.__objc_classlist: 0x698
   __DATA_CONST.__objc_catlist: 0x148
   __DATA_CONST.__objc_protolist: 0x230
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8d80
+  __DATA_CONST.__objc_selrefs: 0x8e00
   __DATA_CONST.__objc_protorefs: 0x40
-  __DATA_CONST.__objc_superrefs: 0x4a8
+  __DATA_CONST.__objc_superrefs: 0x4b0
   __DATA_CONST.__objc_arraydata: 0x1a08
-  __AUTH_CONST.__auth_got: 0x1488
-  __AUTH_CONST.__const: 0x26a0
+  __AUTH_CONST.__auth_got: 0x14d8
+  __AUTH_CONST.__const: 0x2890
   __AUTH_CONST.__cfstring: 0x104a0
-  __AUTH_CONST.__objc_const: 0x166a0
+  __AUTH_CONST.__objc_const: 0x168c0
   __AUTH_CONST.__objc_intobj: 0x6a8
   __AUTH_CONST.__objc_doubleobj: 0x50
   __AUTH_CONST.__objc_arrayobj: 0x750
   __AUTH_CONST.__objc_dictobj: 0x1e0
-  __AUTH.__objc_data: 0x3fb0
-  __AUTH.__data: 0x4a8
-  __DATA.__objc_ivar: 0xf98
-  __DATA.__data: 0x21ec
-  __DATA.__bss: 0x1010
+  __AUTH.__objc_data: 0x4070
+  __AUTH.__data: 0x4d8
+  __DATA.__objc_ivar: 0xfa4
+  __DATA.__data: 0x224c
+  __DATA.__bss: 0x1020
   __DATA.__common: 0xb0
   __DATA_DIRTY.__objc_data: 0x370
   __DATA_DIRTY.__bss: 0x19

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 89790FBC-FF38-32D9-BA16-0F86EE7696A6
-  Functions: 6555
-  Symbols:   22227
-  CStrings:  12183
+  UUID: 33E3B1C8-A31A-35A7-A8EA-FF641AF4674E
+  Functions: 6609
+  Symbols:   22323
+  CStrings:  12218
 
Symbols:
+ +[WBSRichSearchSuggestionImageProvider shared]
+ +[WBSRichSearchSuggestionImageProvider shared].cold.1
+ -[WBSRichSearchSuggestionImageProvider .cxx_destruct]
+ -[WBSRichSearchSuggestionImageProvider _callPendingCompletionHandlersForURLString:withImage:]
+ -[WBSRichSearchSuggestionImageProvider _cancelClearSearchSuggestionImageCacheTimer]
+ -[WBSRichSearchSuggestionImageProvider _clearSearchSuggestionImageCache]
+ -[WBSRichSearchSuggestionImageProvider _imageFitsAspectRatio:]
+ -[WBSRichSearchSuggestionImageProvider cachedImageForURLString:]
+ -[WBSRichSearchSuggestionImageProvider clearSearchSuggestionImageCacheNow]
+ -[WBSRichSearchSuggestionImageProvider clearSearchSuggestionImageCacheSoon]
+ -[WBSRichSearchSuggestionImageProvider dealloc]
+ -[WBSRichSearchSuggestionImageProvider fetchImageForURLString:completionHandler:]
+ -[WBSRichSearchSuggestionImageProvider fetchImageForURLString:completionHandler:].cold.1
+ _OBJC_CLASS_$_OS_dispatch_queue
+ _OBJC_CLASS_$_WBSCompletionIconProvider
+ _OBJC_CLASS_$_WBSRichSearchSuggestionImageProvider
+ _OBJC_IVAR_$_WBSRichSearchSuggestionImageProvider._clearSearchSuggestionImageCacheTimer
+ _OBJC_IVAR_$_WBSRichSearchSuggestionImageProvider._pendingCompletionHandlers
+ _OBJC_IVAR_$_WBSRichSearchSuggestionImageProvider._searchSuggestionImageCache
+ _OBJC_METACLASS_$_WBSCompletionIconProvider
+ _OBJC_METACLASS_$_WBSRichSearchSuggestionImageProvider
+ _WBSRichSearchSuggestionImageMaxWidthAndHeight
+ __CLASS_METHODS_WBSCompletionIconProvider
+ __CLASS_PROPERTIES_WBSCompletionIconProvider
+ __DATA_WBSCompletionIconProvider
+ __INSTANCE_METHODS_WBSCompletionIconProvider
+ __IVARS_WBSCompletionIconProvider
+ __METACLASS_DATA_WBSCompletionIconProvider
+ __OBJC_$_CLASS_METHODS_WBSRichSearchSuggestionImageProvider
+ __OBJC_$_CLASS_PROP_LIST_WBSRichSearchSuggestionImageProvider
+ __OBJC_$_INSTANCE_METHODS_WBSRichSearchSuggestionImageProvider
+ __OBJC_$_INSTANCE_VARIABLES_WBSRichSearchSuggestionImageProvider
+ __OBJC_CLASS_RO_$_WBSRichSearchSuggestionImageProvider
+ __OBJC_METACLASS_RO_$_WBSRichSearchSuggestionImageProvider
+ __PROPERTIES_WBSCompletionIconProvider
+ ___46+[WBSRichSearchSuggestionImageProvider shared]_block_invoke
+ ___75-[WBSRichSearchSuggestionImageProvider clearSearchSuggestionImageCacheSoon]_block_invoke
+ ___81-[WBSRichSearchSuggestionImageProvider fetchImageForURLString:completionHandler:]_block_invoke
+ ___81-[WBSRichSearchSuggestionImageProvider fetchImageForURLString:completionHandler:]_block_invoke.cold.1
+ ___block_descriptor_48_e8_32s40w_e17_v16?0"UIImage"8lw40l8s32l8
+ _block_copy_helper.5
+ _block_descriptor.7
+ _block_destroy_helper.6
+ _objc_msgSend$_callPendingCompletionHandlersForURLString:withImage:
+ _objc_msgSend$_cancelClearSearchSuggestionImageCacheTimer
+ _objc_msgSend$_clearSearchSuggestionImageCache
+ _objc_msgSend$_imageFitsAspectRatio:
+ _objc_msgSend$cachedImageForURLString:
+ _objc_msgSend$createIconWithSystemImageName:isDarkMode:
+ _objc_msgSend$iconFetchingQueue
+ _objc_msgSend$imageForDescriptor:
+ _objc_msgSend$placeholder
+ _objc_msgSend$setAppearance:
+ _objc_msgSend$systemImageNames
+ _shared.onceToken
+ _shared.shared
+ _symbolic Say_____G 8Dispatch0A13WorkItemFlagsV
+ _symbolic So25WBSCompletionIconProviderC
+ _symbolic So7UIImageC
+ _symbolic _____ySSSo7UIImageCG s18_DictionaryStorageC
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CL57ugDfFdMXVLjIvRVL0prk2PAE0tlrtFr1b8s/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.5.Internal.sdk/usr/local/include/wtf/HashTable.h"
+ "@\"OS_dispatch_queue\""
+ "Returning nil for cached image due to incompatible aspect ratio"
+ "Rich search suggestion image URL is nil."
+ "T@\"NSArray\",N,R"
+ "T@\"OS_dispatch_queue\",N,R,ViconFetchingQueue"
+ "T@\"WBSCompletionIconProvider\",N,R"
+ "T@\"WBSRichSearchSuggestionImageProvider\",R,N"
+ "Unable to download rich search suggestion image."
+ "WBSCompletionIconProvider"
+ "WBSRichSearchSuggestionImageProvider"
+ "_callPendingCompletionHandlersForURLString:withImage:"
+ "_cancelClearSearchSuggestionImageCacheTimer"
+ "_clearSearchSuggestionImageCache"
+ "_clearSearchSuggestionImageCacheTimer"
+ "_imageFitsAspectRatio:"
+ "_pendingCompletionHandlers"
+ "_searchSuggestionImageCache"
+ "arrow.down.right"
+ "cachedImageForURLString:"
+ "clearSearchSuggestionImageCacheNow"
+ "clearSearchSuggestionImageCacheSoon"
+ "com.apple.Safari.completionListIconFetching"
+ "com.apple.safari.completionlist."
+ "createIconWithSystemImageName:isDarkMode:"
+ "darkModeIcons"
+ "doc.text.magnifyingglass"
+ "fetchImageForURLString:completionHandler:"
+ "iconFetchingQueue"
+ "iconForSystemImageName:isDarkMode:"
+ "imageForDescriptor:"
+ "lightModeIcons"
+ "placeholder"
+ "populateCompletionListIcons"
+ "setAppearance:"
+ "systemImageNames"
- "/AppleInternal/Library/BuildRoots/4~CKdOugA9cUWI4BH-NhSuWwSb2tdDh9Q6cpJTqew/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/include/wtf/HashTable.h"

```
