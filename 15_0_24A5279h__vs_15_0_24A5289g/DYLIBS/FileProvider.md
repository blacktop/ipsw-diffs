## FileProvider

> `/System/Library/Frameworks/FileProvider.framework/Versions/A/FileProvider`

```diff

-2727.0.0.0.0
-  __TEXT.__text: 0x143dac
-  __TEXT.__auth_stubs: 0x1b00
-  __TEXT.__objc_methlist: 0xc0a8
+2732.0.26.0.0
+  __TEXT.__text: 0x144044
+  __TEXT.__auth_stubs: 0x1bb0
+  __TEXT.__objc_methlist: 0xc0b8
   __TEXT.__const: 0x530
-  __TEXT.__gcc_except_tab: 0xa0b0
-  __TEXT.__cstring: 0x13dd3
+  __TEXT.__gcc_except_tab: 0xa0c8
+  __TEXT.__cstring: 0x13e32
   __TEXT.__oslogstring: 0xd493
   __TEXT.__dlopen_cstrs: 0x709
   __TEXT.__ustring: 0x1e2
-  __TEXT.__unwind_info: 0x53b8
-  __TEXT.__objc_classname: 0x1f80
-  __TEXT.__objc_methname: 0x22891
-  __TEXT.__objc_methtype: 0x624d
-  __TEXT.__objc_stubs: 0x132e0
-  __DATA_CONST.__got: 0xaa0
-  __DATA_CONST.__const: 0x16b8
+  __TEXT.__unwind_info: 0x53c0
+  __TEXT.__objc_classname: 0x1f75
+  __TEXT.__objc_methname: 0x2290e
+  __TEXT.__objc_methtype: 0x62a7
+  __TEXT.__objc_stubs: 0x13320
+  __DATA_CONST.__got: 0xaa8
+  __DATA_CONST.__const: 0x15f8
   __DATA_CONST.__objc_classlist: 0x670
   __DATA_CONST.__objc_catlist: 0x90
   __DATA_CONST.__objc_protolist: 0x290
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6778
+  __DATA_CONST.__objc_selrefs: 0x6788
   __DATA_CONST.__objc_protorefs: 0x148
   __DATA_CONST.__objc_superrefs: 0x528
   __DATA_CONST.__objc_arraydata: 0xa90
-  __AUTH_CONST.__auth_got: 0xd90
+  __AUTH_CONST.__auth_got: 0xde8
   __AUTH_CONST.__auth_ptr: 0x38
-  __AUTH_CONST.__const: 0x6830
-  __AUTH_CONST.__cfstring: 0x10be0
-  __AUTH_CONST.__objc_const: 0x26800
+  __AUTH_CONST.__const: 0x6850
+  __AUTH_CONST.__cfstring: 0x10c60
+  __AUTH_CONST.__objc_const: 0x26860
   __AUTH_CONST.__objc_intobj: 0x108
   __AUTH_CONST.__objc_arrayobj: 0x150
   __AUTH.__objc_data: 0x1400
   __DATA.__objc_ivar: 0xfc8
-  __DATA.__data: 0x2258
-  __DATA.__bss: 0x918
+  __DATA.__data: 0x2270
+  __DATA.__bss: 0x928
   __DATA_DIRTY.__objc_data: 0x2c60
   __DATA_DIRTY.__data: 0x10
   __DATA_DIRTY.__bss: 0x100

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsandbox.1.dylib
-  Functions: 6834
-  Symbols:   15699
-  CStrings:  2954
+  Functions: 6837
+  Symbols:   15717
+  CStrings:  2958
 
Symbols:
+ +[FPProviderDomain accumulatedSizeOfItemsInDomain:completion:]
+ -[FPItem isKeepDownloaded]
+ -[NSUUID(FPAdditions) fp_UUIDWithObfuscation:]
+ -[NSUUID(FPAdditions) fp_UUID]
+ _CONTAINER_PERSONA_PRIMARY
+ _FPAccumulatedEvictableSize
+ _FPAccumulatedMaterializedSize
+ _FPDocumentCount
+ __53-[FPProviderDomain domainStateWithCompletionHandler:]_block_invoke.350
+ __66+[FPItemToURLResourcesConverter dictionaryFromItem:requestedKeys:]_block_invoke.364
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSUUID_$_FPAdditions
+ __OBJC_$_CATEGORY_NSUUID_$_FPAdditions
+ ___44+[FPProviderMonitor isProviderIDForeground:]_block_invoke
+ ___block_descriptor_44_e8_i12?0i8l
+ ___block_descriptor_73_e5_i8?0l
+ ___block_descriptor_73_e8_i12?0i8l
+ __block_literal_global.225
+ __block_literal_global.362
+ __block_literal_global.374
+ __block_literal_global.383
+ __block_literal_global.447
+ __block_literal_global.5
+ __block_literal_global.526
+ __block_literal_global.528
+ _container_error_copy_unlocalized_description
+ _container_get_path
+ _container_query_create
+ _container_query_free
+ _container_query_get_last_error
+ _container_query_get_single_result
+ _container_query_operation_set_flags
+ _container_query_set_class
+ _container_query_set_group_identifiers
+ _container_query_set_persona_unique_string
+ _container_query_set_transient
+ _objc_msgSend$accumulatedSizeOfItemsInDomain:completion:
+ _objc_msgSend$downloadingProgress
+ _xpc_string_create
+ isProviderIDForeground:.onceToken
+ isProviderIDForeground:.tokensCache
- -[NSUUID(FPAddtions) fp_UUIDWithObfuscation:]
- -[NSUUID(FPAddtions) fp_UUID]
- __53-[FPProviderDomain domainStateWithCompletionHandler:]_block_invoke.341
- __66+[FPItemToURLResourcesConverter dictionaryFromItem:requestedKeys:]_block_invoke.361
- __OBJC_$_CATEGORY_INSTANCE_METHODS_NSUUID_$_FPAddtions
- __OBJC_$_CATEGORY_NSUUID_$_FPAddtions
- __block_descriptor_tmp.11
- __block_descriptor_tmp.12
- __block_descriptor_tmp.13
- __block_descriptor_tmp.23
- __block_descriptor_tmp.28
- __block_descriptor_tmp.8
- __block_literal_global.224
- __block_literal_global.359
- __block_literal_global.373
- __block_literal_global.382
- __block_literal_global.446
- __block_literal_global.525
- __block_literal_global.527
- _container_get_error_description
CStrings:
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FileProvider/extension/FPXDomainContext.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FileProvider/extension/FPXEnumerator.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FileProvider/extension/FPXExtensionContext.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FileProvider/extension/FPXFakeDefaultDomainExtension.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FileProvider/fileproviderd/action operation engine/FPActionOperationLocator.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FileProvider/framework/FPDaemonConnection.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FileProvider/framework/FPItem.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FileProvider/framework/FPTestingOperations.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FileProvider/framework/FPXPCSanitizer.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FileProvider/framework/NSFileProviderManager.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/FileProvider/framework/NSXPCConnection+FPAdditions.m"
+ "2732.0.26"
+ "FPAccumulatedEvictableSize"
+ "FPAccumulatedMaterializedSize"
+ "FPDocumentCount"
+ "fpfs_package.m"
+ "isKeepDownloaded"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FileProvider/extension/FPXDomainContext.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FileProvider/extension/FPXEnumerator.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FileProvider/extension/FPXExtensionContext.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FileProvider/extension/FPXFakeDefaultDomainExtension.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FileProvider/fileproviderd/action operation engine/FPActionOperationLocator.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FileProvider/framework/FPDaemonConnection.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FileProvider/framework/FPItem.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FileProvider/framework/FPTestingOperations.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FileProvider/framework/FPXPCSanitizer.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FileProvider/framework/NSFileProviderManager.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/FileProvider/framework/NSXPCConnection+FPAdditions.m"
- "2727"
- "fpfs_package.c"

```
