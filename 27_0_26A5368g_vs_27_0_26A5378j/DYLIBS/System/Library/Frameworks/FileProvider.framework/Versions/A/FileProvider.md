## FileProvider

> `/System/Library/Frameworks/FileProvider.framework/Versions/A/FileProvider`

```diff

-  __TEXT.__text: 0x13f0b8
-  __TEXT.__objc_methlist: 0xe85c
+  __TEXT.__text: 0x13f718
+  __TEXT.__objc_methlist: 0xe89c
   __TEXT.__const: 0x8aa
-  __TEXT.__cstring: 0x14fe6
-  __TEXT.__gcc_except_tab: 0x8914
+  __TEXT.__cstring: 0x14ff4
+  __TEXT.__gcc_except_tab: 0x892c
   __TEXT.__oslogstring: 0xe08b
   __TEXT.__dlopen_cstrs: 0x6ba
   __TEXT.__ustring: 0x21e

   __TEXT.__swift_as_entry: 0x4
   __TEXT.__swift_as_ret: 0x4
   __TEXT.__swift_as_cont: 0xc
-  __TEXT.__unwind_info: 0x57f8
+  __TEXT.__unwind_info: 0x5810
   __TEXT.__eh_frame: 0xa0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1648
+  __DATA_CONST.__const: 0x1668
   __DATA_CONST.__objc_classlist: 0x690
   __DATA_CONST.__objc_catlist: 0x90
   __DATA_CONST.__objc_protolist: 0x2a8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6fb8
+  __DATA_CONST.__objc_selrefs: 0x6fe8
   __DATA_CONST.__objc_protorefs: 0x158
   __DATA_CONST.__objc_superrefs: 0x548
   __DATA_CONST.__objc_arraydata: 0xab0
-  __DATA_CONST.__got: 0xb08
+  __DATA_CONST.__got: 0xb50
   __AUTH_CONST.__const: 0x6f88
-  __AUTH_CONST.__cfstring: 0x11900
-  __AUTH_CONST.__objc_const: 0x24f58
+  __AUTH_CONST.__cfstring: 0x11920
+  __AUTH_CONST.__objc_const: 0x24fd0
   __AUTH_CONST.__objc_intobj: 0x120
   __AUTH_CONST.__objc_arrayobj: 0x198
   __AUTH_CONST.__auth_got: 0xf18
-  __AUTH.__objc_data: 0x4b0
+  __AUTH.__objc_data: 0x2490
   __AUTH.__data: 0x10
   __DATA.__objc_ivar: 0x10c8
   __DATA.__data: 0x23f0
   __DATA.__bss: 0xbc0
   __DATA.__common: 0x2b
-  __DATA_DIRTY.__objc_data: 0x3cf0
+  __DATA_DIRTY.__objc_data: 0x1d10
   __DATA_DIRTY.__data: 0x1
   __DATA_DIRTY.__bss: 0x348
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  Functions: 7504
-  Symbols:   16788
-  CStrings:  6309
+  Functions: 7514
+  Symbols:   16802
+  CStrings:  6311
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_fieldmd : content changed
~ __TEXT.__swift5_builtin : content changed
~ __TEXT.__swift5_assocty : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__swift5_types : content changed
~ __TEXT.__swift_as_entry : content changed
~ __TEXT.__swift_as_ret : content changed
~ __TEXT.__swift_as_cont : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH.__data : content changed
~ __DATA.__data : content changed
Symbols:
+ -[FPItemManager _fetchSearchableItemIdentifiersForURL:synchronously:skipURLValidation:completionHandler:]
+ -[FPItemManager fetchSearchableItemIdentifiersForURL:completionHandler:]
+ -[FPItemManager searchableItemIdentifiersForURL:error:]
+ GCC_except_table146
+ _FPFileLockedByFlock
+ _FPURLIsKnownCiaoLocalStorage
+ ___105-[FPItemManager _fetchSearchableItemIdentifiersForURL:synchronously:skipURLValidation:completionHandler:]_block_invoke
+ ___55-[FPItemManager searchableItemIdentifiersForURL:error:]_block_invoke
+ ___block_descriptor_48_e8_i12?0i8l
+ ___fpfs_get_purgeable_info_at_block_invoke
+ ___fpfs_unset_purgeable_at_block_invoke
+ _fpfs_get_purgeable_info_at
+ _fpfs_query_purgeable_bytes
+ _fpfs_unset_purgeable_at
+ _objc_msgSend$_fetchSearchableItemIdentifiersForURL:synchronously:skipURLValidation:completionHandler:
+ _objc_msgSend$searchableItemIdentifiersForURL:completionHandler:
- GCC_except_table141
- ___fpfs_t_unset_evictable_at_block_invoke
- _fpfs_t_unset_evictable_at
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mDsJh7/Sources/FileProvider/extension/FPXDomainContext.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mDsJh7/Sources/FileProvider/extension/FPXEnumerator.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mDsJh7/Sources/FileProvider/extension/FPXExtensionContext.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mDsJh7/Sources/FileProvider/extension/FPXFakeDefaultDomainExtension.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mDsJh7/Sources/FileProvider/extension/search-on-server/FPXSearchEnumeratorObserver.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mDsJh7/Sources/FileProvider/fileproviderd/action operation engine/FPActionOperationLocator.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mDsJh7/Sources/FileProvider/framework/FPDaemonConnection.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mDsJh7/Sources/FileProvider/framework/FPItem.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mDsJh7/Sources/FileProvider/framework/FPTestingOperations.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mDsJh7/Sources/FileProvider/framework/FPXPCSanitizer.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mDsJh7/Sources/FileProvider/framework/NSFileProviderManager.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mDsJh7/Sources/FileProvider/framework/NSURL+FPAdditions.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mDsJh7/Sources/FileProvider/framework/NSXPCConnection+FPAdditions.m"
+ "4838.0.70"
+ "FileLockedByFlock"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kURcwO/Sources/FileProvider/extension/FPXDomainContext.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kURcwO/Sources/FileProvider/extension/FPXEnumerator.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kURcwO/Sources/FileProvider/extension/FPXExtensionContext.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kURcwO/Sources/FileProvider/extension/FPXFakeDefaultDomainExtension.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kURcwO/Sources/FileProvider/extension/search-on-server/FPXSearchEnumeratorObserver.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kURcwO/Sources/FileProvider/fileproviderd/action operation engine/FPActionOperationLocator.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kURcwO/Sources/FileProvider/framework/FPDaemonConnection.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kURcwO/Sources/FileProvider/framework/FPItem.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kURcwO/Sources/FileProvider/framework/FPTestingOperations.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kURcwO/Sources/FileProvider/framework/FPXPCSanitizer.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kURcwO/Sources/FileProvider/framework/NSFileProviderManager.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kURcwO/Sources/FileProvider/framework/NSURL+FPAdditions.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kURcwO/Sources/FileProvider/framework/NSXPCConnection+FPAdditions.m"
- "4838.0.29.0.1"

```
