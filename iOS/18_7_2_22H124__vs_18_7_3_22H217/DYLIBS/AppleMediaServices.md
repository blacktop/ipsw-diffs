## AppleMediaServices

> `/System/Library/PrivateFrameworks/AppleMediaServices.framework/AppleMediaServices`

```diff

-8.6.8.0.0
-  __TEXT.__text: 0x695164
+8.6.8.1.0
+  __TEXT.__text: 0x696a84
   __TEXT.__auth_stubs: 0x40c0
-  __TEXT.__objc_methlist: 0x20b9c
+  __TEXT.__objc_methlist: 0x20c7c
   __TEXT.__const: 0x540e0
   __TEXT.__dlopen_cstrs: 0x8d3
-  __TEXT.__cstring: 0x25366
+  __TEXT.__cstring: 0x25461
   __TEXT.__swift5_typeref: 0x3eb1
   __TEXT.__swift5_reflstr: 0x1f18
   __TEXT.__swift5_assocty: 0x9d8

   __TEXT.__swift5_capture: 0x1e10
   __TEXT.__swift5_mpenum: 0x48
   __TEXT.__swift5_protos: 0x80
-  __TEXT.__oslogstring: 0x2e7b7
-  __TEXT.__gcc_except_tab: 0x7b2c
+  __TEXT.__oslogstring: 0x2ead0
+  __TEXT.__gcc_except_tab: 0x7c4c
   __TEXT.__ustring: 0x1b2
-  __TEXT.__unwind_info: 0xd490
+  __TEXT.__unwind_info: 0xd4e8
   __TEXT.__eh_frame: 0xd314
-  __TEXT.__objc_classname: 0x3bf6
-  __TEXT.__objc_methname: 0x4119d
-  __TEXT.__objc_methtype: 0x7374
-  __TEXT.__objc_stubs: 0x2d280
+  __TEXT.__objc_classname: 0x3c2e
+  __TEXT.__objc_methname: 0x412b9
+  __TEXT.__objc_methtype: 0x73df
+  __TEXT.__objc_stubs: 0x2d340
   __DATA_CONST.__got: 0x17d0
-  __DATA_CONST.__const: 0xba78
-  __DATA_CONST.__objc_classlist: 0x12c0
+  __DATA_CONST.__const: 0xbb18
+  __DATA_CONST.__objc_classlist: 0x12c8
   __DATA_CONST.__objc_catlist: 0xf8
-  __DATA_CONST.__objc_protolist: 0x3a8
+  __DATA_CONST.__objc_protolist: 0x3b0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xe700
-  __DATA_CONST.__objc_protorefs: 0x1b8
-  __DATA_CONST.__objc_superrefs: 0xc58
+  __DATA_CONST.__objc_selrefs: 0xe748
+  __DATA_CONST.__objc_protorefs: 0x1c0
+  __DATA_CONST.__objc_superrefs: 0xc60
   __DATA_CONST.__objc_arraydata: 0x568
   __AUTH_CONST.__auth_got: 0x2078
   __AUTH_CONST.__const: 0x24e30
-  __AUTH_CONST.__cfstring: 0x213a0
-  __AUTH_CONST.__objc_const: 0x38400
+  __AUTH_CONST.__cfstring: 0x21400
+  __AUTH_CONST.__objc_const: 0x38538
   __AUTH_CONST.__objc_intobj: 0xcd8
   __AUTH_CONST.__objc_arrayobj: 0x120
   __AUTH_CONST.__objc_dictobj: 0x118
-  __AUTH.__objc_data: 0x7f40
+  __AUTH.__objc_data: 0x7f90
   __AUTH.__data: 0x12b0
-  __DATA.__objc_ivar: 0x17d8
-  __DATA.__data: 0x4d80
+  __DATA.__objc_ivar: 0x17e0
+  __DATA.__data: 0x4de0
   __DATA.__bss: 0xa0c1
   __DATA.__common: 0xb78
   __DATA_DIRTY.__objc_ivar: 0x65c

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: A663F0CC-D2E8-3E70-B7A3-999938E61640
-  Functions: 19899
-  Symbols:   46191
-  CStrings:  24029
+  UUID: 12A42B9A-FD28-3B8F-94B6-83639D23325E
+  Functions: 19923
+  Symbols:   46267
+  CStrings:  24067
 
Symbols:
+ +[AMSDaemonConnectionInterface _safariDataUpdateServiceInterface]
+ -[AMSDaemonConnection safariDataUpdateServiceProxy]
+ -[AMSSafariDataUpdate .cxx_destruct]
+ -[AMSSafariDataUpdate _handleUpdateAvailableNotification:]
+ -[AMSSafariDataUpdate _invokeHandlersWithURL:]
+ -[AMSSafariDataUpdate dealloc]
+ -[AMSSafariDataUpdate init]
+ -[AMSSafariDataUpdate publishUpdate:]
+ -[AMSSafariDataUpdate queue]
+ -[AMSSafariDataUpdate registerForUpdatesWithHandler:]
+ -[AMSSafariDataUpdate setQueue:]
+ -[AMSSafariDataUpdate setUpdateHandlers:]
+ -[AMSSafariDataUpdate updateHandlers]
+ _OBJC_CLASS_$_AMSSafariDataUpdate
+ _OBJC_IVAR_$_AMSSafariDataUpdate._queue
+ _OBJC_IVAR_$_AMSSafariDataUpdate._updateHandlers
+ _OBJC_METACLASS_$_AMSSafariDataUpdate
+ __OBJC_$_INSTANCE_METHODS_AMSSafariDataUpdate
+ __OBJC_$_INSTANCE_VARIABLES_AMSSafariDataUpdate
+ __OBJC_$_PROP_LIST_AMSSafariDataUpdate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AMSSafariDataUpdateServiceInterface
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AMSSafariDataUpdateServiceInterface
+ __OBJC_$_PROTOCOL_REFS_AMSSafariDataUpdateServiceInterface
+ __OBJC_CLASS_RO_$_AMSSafariDataUpdate
+ __OBJC_LABEL_PROTOCOL_$_AMSSafariDataUpdateServiceInterface
+ __OBJC_METACLASS_RO_$_AMSSafariDataUpdate
+ __OBJC_PROTOCOL_$_AMSSafariDataUpdateServiceInterface
+ __OBJC_PROTOCOL_REFERENCE_$_AMSSafariDataUpdateServiceInterface
+ ___37-[AMSSafariDataUpdate publishUpdate:]_block_invoke
+ ___37-[AMSSafariDataUpdate publishUpdate:]_block_invoke.19
+ ___46-[AMSSafariDataUpdate _invokeHandlersWithURL:]_block_invoke
+ ___51-[AMSDaemonConnection safariDataUpdateServiceProxy]_block_invoke
+ ___51-[AMSDaemonConnection safariDataUpdateServiceProxy]_block_invoke_2
+ ___53-[AMSSafariDataUpdate registerForUpdatesWithHandler:]_block_invoke
+ ___58-[AMSSafariDataUpdate _handleUpdateAvailableNotification:]_block_invoke
+ ___58-[AMSSafariDataUpdate _handleUpdateAvailableNotification:]_block_invoke.22
+ ___58-[AMSSafariDataUpdate _handleUpdateAvailableNotification:]_block_invoke.23
+ ___block_descriptor_48_e8_32s40r_e30_v24?0"NSString"8"NSError"16ls32l8r40l8
+ ___block_descriptor_48_e8_32s40r_e59_v24?0"<AMSSafariDataUpdateServiceInterface>"8"NSError"16ls32l8r40l8
+ ___block_descriptor_48_e8_32s40s_e79_v24?0"<AMSSafariDataUpdateServiceInterface><NSXPCProxyCreating>"8"NSError"16ls32l8s40l8
+ ___block_descriptor_64_e8_32s40s48s56r_e59_v24?0"<AMSSafariDataUpdateServiceInterface>"8"NSError"16ls32l8s40l8r56l8s48l8
+ _objc_msgSend$_invokeHandlersWithURL:
+ _objc_msgSend$_safariDataUpdateServiceInterface
+ _objc_msgSend$fetchPendingSafariDataUpdate:
+ _objc_msgSend$getSafariDataUpdateServiceProxyWithReplyHandler:
+ _objc_msgSend$publishSafariDataUpdate:completion:
+ _objc_msgSend$safariDataUpdateServiceProxy
- GCC_except_table63
CStrings:
+ "%{public}@: Cannot register nil handler"
+ "%{public}@: Failed to get proxy for fetch: %{public}@"
+ "%{public}@: Failed to get proxy for publish: %{public}@"
+ "%{public}@: Fetch failed: %{public}@"
+ "%{public}@: Fetched pending update: %{public}@"
+ "%{public}@: Handler threw exception: %{public}@"
+ "%{public}@: Initialized and observing distributed notifications"
+ "%{public}@: Invalid URL for publish"
+ "%{public}@: Invoking %ld handler(s) with URL: %{public}@"
+ "%{public}@: No handlers registered, skipping fetch"
+ "%{public}@: No pending update available (may have expired)"
+ "%{public}@: Publish failed: %{public}@"
+ "%{public}@: Publish succeeded"
+ "%{public}@: Publishing Safari Data Update: %{public}@"
+ "%{public}@: Received distributed notification for Safari Data Update"
+ "%{public}@: Registered handler, total handlers: %ld"
+ "AMSSafariDataUpdate"
+ "AMSSafariDataUpdate Error"
+ "AMSSafariDataUpdateServiceInterface"
+ "Invalid URL for publish"
+ "_handleUpdateAvailableNotification:"
+ "_invokeHandlersWithURL:"
+ "_safariDataUpdateServiceInterface"
+ "com.apple.AMS.SafariDataUpdate"
+ "com.apple.AMSSafariDataUpdate"
+ "fetchPendingSafariDataUpdate:"
+ "getSafariDataUpdateServiceProxyWithReplyHandler:"
+ "publishSafariDataUpdate:completion:"
+ "publishUpdate:"
+ "registerForUpdatesWithHandler:"
+ "safariDataUpdateServiceProxy"
+ "v24@0:8@?<v@?@\"<AMSSafariDataUpdateServiceInterface>\"@\"NSError\">16"
+ "v24@?0@\"<AMSSafariDataUpdateServiceInterface>\"8@\"NSError\"16"
+ "v24@?0@\"<AMSSafariDataUpdateServiceInterface><NSXPCProxyCreating>\"8@\"NSError\"16"
+ "v32@0:8@\"NSString\"16@?<v@?@\"NSError\">24"

```
