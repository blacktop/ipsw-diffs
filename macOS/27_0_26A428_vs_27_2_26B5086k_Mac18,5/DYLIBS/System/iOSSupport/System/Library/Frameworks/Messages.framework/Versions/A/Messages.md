## Messages

> `/System/iOSSupport/System/Library/Frameworks/Messages.framework/Versions/A/Messages`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`

```diff

-1491.100.1.1.11
-  __TEXT.__text: 0x28a04
-  __TEXT.__objc_methlist: 0x4da8
+1491.200.63.0.0
+  __TEXT.__text: 0x294b4
+  __TEXT.__objc_methlist: 0x4e00
   __TEXT.__const: 0x454
-  __TEXT.__gcc_except_tab: 0x194
+  __TEXT.__gcc_except_tab: 0x1c0
   __TEXT.__cstring: 0x1ebe
   __TEXT.__oslogstring: 0xe0d
   __TEXT.__dlopen_cstrs: 0x1ca

   __TEXT.__constg_swiftt: 0x50
   __TEXT.__swift5_fieldmd: 0x10
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x1138
+  __TEXT.__unwind_info: 0x1170
   __TEXT.__eh_frame: 0x178
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x670
+  __DATA_CONST.__const: 0x710
   __DATA_CONST.__objc_classlist: 0x138
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0xd8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x26b8
+  __DATA_CONST.__objc_selrefs: 0x26e0
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x108
   __DATA_CONST.__objc_arraydata: 0x30
   __DATA_CONST.__got: 0x548
-  __AUTH_CONST.__const: 0x3c8
+  __AUTH_CONST.__const: 0x3e8
   __AUTH_CONST.__cfstring: 0x1740
-  __AUTH_CONST.__objc_const: 0x5fa0
+  __AUTH_CONST.__objc_const: 0x5fb0
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_doubleobj: 0x40
-  __AUTH_CONST.__auth_got: 0x600
+  __AUTH_CONST.__auth_got: 0x608
   __AUTH.__objc_data: 0x9d0
   __AUTH.__data: 0xc0
   __DATA.__objc_ivar: 0x3f8

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1545
-  Symbols:   3521
+  Functions: 1560
+  Symbols:   3546
   CStrings:  311
 
Symbols:
+ -[MSConversation _insertMessage:replyingToMessage:skipShelf:completionHandler:]
+ -[MSConversation insertMessage:replyingToMessage:completionHandler:]
+ -[_MSMessageAppBundleContext stageAppItem:replyingToMessage:skipShelf:completionHandler:]
+ -[_MSMessageAppBundleHostContext _stageAppItem:replyingToMessage:skipShelf:completionHandler:]
+ -[_MSMessageAppContext stageAppItem:replyingToMessage:skipShelf:completionHandler:]
+ -[_MSMessageAppExtensionContext stageAppItem:replyingToMessage:skipShelf:completionHandler:]
+ -[_MSMessageAppExtensionHostContext _stageAppItem:replyingToMessage:skipShelf:completionHandler:]
+ GCC_except_table53
+ ___79-[MSConversation _insertMessage:replyingToMessage:skipShelf:completionHandler:]_block_invoke
+ ___92-[_MSMessageAppExtensionContext stageAppItem:replyingToMessage:skipShelf:completionHandler:]_block_invoke
+ ___92-[_MSMessageAppExtensionContext stageAppItem:replyingToMessage:skipShelf:completionHandler:]_block_invoke_2
+ ___92-[_MSMessageAppExtensionContext stageAppItem:replyingToMessage:skipShelf:completionHandler:]_block_invoke_3
+ ___92-[_MSMessageAppExtensionContext stageAppItem:replyingToMessage:skipShelf:completionHandler:]_block_invoke_4
+ ___92-[_MSMessageAppExtensionContext stageAppItem:replyingToMessage:skipShelf:completionHandler:]_block_invoke_5
+ ___94-[_MSMessageAppBundleHostContext _stageAppItem:replyingToMessage:skipShelf:completionHandler:]_block_invoke
+ ___97-[_MSMessageAppExtensionHostContext _stageAppItem:replyingToMessage:skipShelf:completionHandler:]_block_invoke
+ ___block_descriptor_40_e8_32bs_e17_v16?0"NSError"8ls32l8
+ ___block_descriptor_40_e8_32bs_e20_v20?0B8"NSError"12ls32l8
+ ___block_descriptor_48_e8_32bs40r_e20_v20?0B8"NSError"12lr40l8s32l8
+ ___block_descriptor_57_e8_32s40s48bs_e17_v16?0"NSError"8ls32l8s48l8s40l8
+ _objc_msgSend$_insertMessage:replyingToMessage:skipShelf:completionHandler:
+ _objc_msgSend$_stageAppItem:replyingToMessage:skipShelf:completionHandler:
+ _objc_msgSend$remoteObjectProxyWithErrorHandler:
+ _objc_msgSend$stageAppItem:replyingToMessage:skipShelf:completionHandler:
+ _objc_release_x2
CStrings:
+ "PhotosUIFoundation"
- "PhotosUICore"
```
