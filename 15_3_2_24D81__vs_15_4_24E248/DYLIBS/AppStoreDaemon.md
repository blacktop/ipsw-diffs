## AppStoreDaemon

> `/System/Library/PrivateFrameworks/AppStoreDaemon.framework/Versions/A/AppStoreDaemon`

```diff

-11.2.29.0.0
-  __TEXT.__text: 0x59fc0
+11.4.24.0.0
+  __TEXT.__text: 0x5a5b8
   __TEXT.__auth_stubs: 0x6f0
-  __TEXT.__objc_methlist: 0x7844
-  __TEXT.__cstring: 0xef74
+  __TEXT.__objc_methlist: 0x88c4
   __TEXT.__const: 0x1c8
+  __TEXT.__cstring: 0xefe7
   __TEXT.__swift5_typeref: 0xe
   __TEXT.__constg_swiftt: 0x28
   __TEXT.__swift5_reflstr: 0x21

   __TEXT.__swift5_types: 0x4
   __TEXT.__gcc_except_tab: 0xb7c
   __TEXT.__oslogstring: 0x28f6
-  __TEXT.__unwind_info: 0x1b40
+  __TEXT.__unwind_info: 0x1b50
   __TEXT.__objc_classname: 0x1373
-  __TEXT.__objc_methname: 0x109d7
-  __TEXT.__objc_methtype: 0x2b24
-  __TEXT.__objc_stubs: 0x59e0
+  __TEXT.__objc_methname: 0x10bc1
+  __TEXT.__objc_methtype: 0x2b7b
+  __TEXT.__objc_stubs: 0x5a20
   __DATA_CONST.__got: 0x400
   __DATA_CONST.__const: 0x3f8
   __DATA_CONST.__objc_classlist: 0x508
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x158
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3448
+  __DATA_CONST.__objc_selrefs: 0x37a8
   __DATA_CONST.__objc_protorefs: 0xc0
   __DATA_CONST.__objc_superrefs: 0x280
   __DATA_CONST.__objc_arraydata: 0x30
   __AUTH_CONST.__auth_got: 0x388
-  __AUTH_CONST.__const: 0x2010
-  __AUTH_CONST.__cfstring: 0x3fa0
-  __AUTH_CONST.__objc_const: 0x13b48
+  __AUTH_CONST.__const: 0x2070
+  __AUTH_CONST.__cfstring: 0x4080
+  __AUTH_CONST.__objc_const: 0x11ed0
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH.__objc_data: 0x5a0
-  __DATA.__objc_ivar: 0xc3c
+  __DATA.__objc_ivar: 0xc54
   __DATA.__data: 0x1038
   __DATA.__bss: 0x300
   __DATA.__common: 0x158

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 0F8F847E-137F-336F-BCCC-F086C8EB117B
-  Functions: 3328
-  Symbols:   6871
-  CStrings:  5036
+  UUID: E943F9F7-D045-38C4-98DB-61629A5DA300
+  Functions: 3340
+  Symbols:   6895
+  CStrings:  5074
 
Symbols:
+ +[ASDAppQueryExecutor _executeQueryWithPredicate:isForUpdates:reloadingFromServer:onPairedDevice:remoteDeviceID:usingServiceBroker:withResultHandler:]
+ -[ASDApp isManaged]
+ -[ASDAppQueryExecutor executeQueryWithPredicate:onPairedDevice:remoteDeviceID:withResultHandler:]
+ -[ASDAppQueryExecutor executeUpdatesQueryWithPredicateReloadingFromServer:onPairedDevice:remoteDeviceID:withResultHandler:]
+ -[ASDProgress initWithBundleID:]
+ -[ASDPurchase isPreorder]
+ -[ASDPurchase remoteDownloadIdentifiers]
+ -[ASDPurchase setIsPreorder:]
+ -[ASDPurchase setRemoteDownloadIdentifiers:]
+ -[ASDTestFlightAppMetadata chunkSize]
+ -[ASDTestFlightAppMetadata clearHashes]
+ -[ASDTestFlightAppMetadata cryptHashes]
+ -[ASDTestFlightAppMetadata setChunkSize:]
+ -[ASDTestFlightAppMetadata setClearHashes:]
+ -[ASDTestFlightAppMetadata setCryptHashes:]
+ GCC_except_table18
+ GCC_except_table30
+ GCC_except_table38
+ GCC_except_table44
+ GCC_except_table48
+ GCC_except_table53
+ OBJC_IVAR_$_ASDAppQuery._remoteDeviceID
+ OBJC_IVAR_$_ASDPurchase._isPreorder
+ OBJC_IVAR_$_ASDPurchase._remoteDownloadIdentifiers
+ OBJC_IVAR_$_ASDTestFlightAppMetadata._chunkSize
+ OBJC_IVAR_$_ASDTestFlightAppMetadata._clearHashes
+ OBJC_IVAR_$_ASDTestFlightAppMetadata._cryptHashes
+ __123-[ASDAppQueryExecutor executeUpdatesQueryWithPredicateReloadingFromServer:onPairedDevice:remoteDeviceID:withResultHandler:]_block_invoke.17
+ __123-[ASDAppQueryExecutor executeUpdatesQueryWithPredicateReloadingFromServer:onPairedDevice:remoteDeviceID:withResultHandler:]_block_invoke.18
+ __123-[ASDAppQueryExecutor executeUpdatesQueryWithPredicateReloadingFromServer:onPairedDevice:remoteDeviceID:withResultHandler:]_block_invoke.19
+ __150+[ASDAppQueryExecutor _executeQueryWithPredicate:isForUpdates:reloadingFromServer:onPairedDevice:remoteDeviceID:usingServiceBroker:withResultHandler:]_block_invoke.22
+ __150+[ASDAppQueryExecutor _executeQueryWithPredicate:isForUpdates:reloadingFromServer:onPairedDevice:remoteDeviceID:usingServiceBroker:withResultHandler:]_block_invoke.25
+ __150+[ASDAppQueryExecutor _executeQueryWithPredicate:isForUpdates:reloadingFromServer:onPairedDevice:remoteDeviceID:usingServiceBroker:withResultHandler:]_block_invoke_2.26
+ __150+[ASDAppQueryExecutor _executeQueryWithPredicate:isForUpdates:reloadingFromServer:onPairedDevice:remoteDeviceID:usingServiceBroker:withResultHandler:]_block_invoke_3.27
+ __97-[ASDAppQueryExecutor executeQueryWithPredicate:onPairedDevice:remoteDeviceID:withResultHandler:]_block_invoke.3
+ __97-[ASDAppQueryExecutor executeQueryWithPredicate:onPairedDevice:remoteDeviceID:withResultHandler:]_block_invoke.6
+ __97-[ASDAppQueryExecutor executeQueryWithPredicate:onPairedDevice:remoteDeviceID:withResultHandler:]_block_invoke.9
+ ___123-[ASDAppQueryExecutor executeUpdatesQueryWithPredicateReloadingFromServer:onPairedDevice:remoteDeviceID:withResultHandler:]_block_invoke
+ ___150+[ASDAppQueryExecutor _executeQueryWithPredicate:isForUpdates:reloadingFromServer:onPairedDevice:remoteDeviceID:usingServiceBroker:withResultHandler:]_block_invoke
+ ___150+[ASDAppQueryExecutor _executeQueryWithPredicate:isForUpdates:reloadingFromServer:onPairedDevice:remoteDeviceID:usingServiceBroker:withResultHandler:]_block_invoke_2
+ ___150+[ASDAppQueryExecutor _executeQueryWithPredicate:isForUpdates:reloadingFromServer:onPairedDevice:remoteDeviceID:usingServiceBroker:withResultHandler:]_block_invoke_3
+ ___97-[ASDAppQueryExecutor executeQueryWithPredicate:onPairedDevice:remoteDeviceID:withResultHandler:]_block_invoke
+ ___block_descriptor_65_e8_32s40s48s56bs_e5_v8?0l
+ ___block_descriptor_72_e8_32s40s48s56s64bs_e5_v8?0l
+ ___block_descriptor_90_e8_32s40s48s56s64bs72r_e17_v16?0"NSError"8l
+ ___block_descriptor_90_e8_32s40s48s56s64bs72r_e72_v24?0"<ASDAppLibraryServiceProtocol><NSXPCProxyCreating>"8"NSError"16l
+ ___block_descriptor_90_e8_32s40s48s56s64s72bs_e5_v8?0l
+ ___copy_helper_block_e8_32s40s48s56s64b72r
+ ___copy_helper_block_e8_32s40s48s56s64s72b
+ ___destroy_helper_block_e8_32s40s48s56s64s72r
+ ___destroy_helper_block_e8_32s40s48s56s64s72s
+ _objc_msgSend$executeQueryWithPredicate:onPairedDevice:remoteDeviceID:withResultHandler:
+ _objc_msgSend$executeQueryWithPredicate:onRemoteDevice:withReplyHandler:
+ _objc_msgSend$executeUpdatesQueryWithPredicateReloadingFromServer:onPairedDevice:remoteDeviceID:withResultHandler:
+ _objc_msgSend$isManaged
- +[ASDAppQueryExecutor _executeQueryWithPredicate:isForUpdates:reloadingFromServer:onPairedDevice:usingServiceBroker:withResultHandler:]
- -[ASDAppQueryExecutor executeQueryWithPredicate:onPairedDevice:withResultHandler:]
- -[ASDAppQueryExecutor executeUpdatesQueryWithPredicateReloadingFromServer:onPairedDevice:withResultHandler:]
- -[ASDSystemAppMetadata setBundleID:]
- GCC_except_table33
- GCC_except_table43
- GCC_except_table47
- GCC_except_table52
- __108-[ASDAppQueryExecutor executeUpdatesQueryWithPredicateReloadingFromServer:onPairedDevice:withResultHandler:]_block_invoke.17
- __108-[ASDAppQueryExecutor executeUpdatesQueryWithPredicateReloadingFromServer:onPairedDevice:withResultHandler:]_block_invoke.18
- __108-[ASDAppQueryExecutor executeUpdatesQueryWithPredicateReloadingFromServer:onPairedDevice:withResultHandler:]_block_invoke.19
- __135+[ASDAppQueryExecutor _executeQueryWithPredicate:isForUpdates:reloadingFromServer:onPairedDevice:usingServiceBroker:withResultHandler:]_block_invoke.22
- __135+[ASDAppQueryExecutor _executeQueryWithPredicate:isForUpdates:reloadingFromServer:onPairedDevice:usingServiceBroker:withResultHandler:]_block_invoke.25
- __135+[ASDAppQueryExecutor _executeQueryWithPredicate:isForUpdates:reloadingFromServer:onPairedDevice:usingServiceBroker:withResultHandler:]_block_invoke_2.26
- __82-[ASDAppQueryExecutor executeQueryWithPredicate:onPairedDevice:withResultHandler:]_block_invoke.3
- __82-[ASDAppQueryExecutor executeQueryWithPredicate:onPairedDevice:withResultHandler:]_block_invoke.6
- __82-[ASDAppQueryExecutor executeQueryWithPredicate:onPairedDevice:withResultHandler:]_block_invoke.9
- ___108-[ASDAppQueryExecutor executeUpdatesQueryWithPredicateReloadingFromServer:onPairedDevice:withResultHandler:]_block_invoke
- ___135+[ASDAppQueryExecutor _executeQueryWithPredicate:isForUpdates:reloadingFromServer:onPairedDevice:usingServiceBroker:withResultHandler:]_block_invoke
- ___135+[ASDAppQueryExecutor _executeQueryWithPredicate:isForUpdates:reloadingFromServer:onPairedDevice:usingServiceBroker:withResultHandler:]_block_invoke_2
- ___135+[ASDAppQueryExecutor _executeQueryWithPredicate:isForUpdates:reloadingFromServer:onPairedDevice:usingServiceBroker:withResultHandler:]_block_invoke_3
- ___82-[ASDAppQueryExecutor executeQueryWithPredicate:onPairedDevice:withResultHandler:]_block_invoke
- ___block_descriptor_82_e8_32s40s48s56bs64r_e17_v16?0"NSError"8l
- ___block_descriptor_82_e8_32s40s48s56bs64r_e72_v24?0"<ASDAppLibraryServiceProtocol><NSXPCProxyCreating>"8"NSError"16l
- ___block_descriptor_82_e8_32s40s48s56s64bs_e5_v8?0l
- ___copy_helper_block_e8_32s40s48s56b64r
- ___destroy_helper_block_e8_32s40s48s56s64r
- _objc_msgSend$executeQueryWithPredicate:onPairedDevice:withResultHandler:
- _objc_msgSend$executeUpdatesQueryWithPredicateReloadingFromServer:onPairedDevice:withResultHandler:
CStrings:
+ "CS"
+ "HC"
+ "HE"
+ "MMM d, yyyy"
+ "T@\"NSArray\",C,N,V_clearHashes"
+ "T@\"NSArray\",C,N,V_cryptHashes"
+ "T@\"NSArray\",C,N,V_remoteDownloadIdentifiers"
+ "T@\"NSNumber\",C,N,V_chunkSize"
+ "TB,N,V_isPreorder"
+ "TB,R,GisManaged"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Services/InstallApps/Metadata/ASDWatchAppMetadata.m:156 : Unsupported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Services/InstallApps/Metadata/ASDWatchAppMetadata.m:162 : Unsupported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Services/InstallApps/Metadata/ASDWatchAppMetadata.m:167 : Unsupported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Services/InstallApps/Metadata/ASDWatchAppMetadata.m:172 : Unsupported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAccountLookupRequestOptions_macOS.m:18 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAccountLookupRequest_macOS.m:18 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAccountLookupRequest_macOS.m:24 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAccountLookupResponse_macOS.m:20 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAccountLookupResponse_macOS.m:26 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAccountLookupResponse_macOS.m:32 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAccountLookupResponse_macOS.m:38 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAggregateClusterMappingData_macOS.m:102 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAggregateClusterMappingData_macOS.m:106 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAggregateClusterMappingData_macOS.m:112 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAggregateClusterMappingData_macOS.m:116 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAggregateClusterMappingData_macOS.m:120 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAggregateClusterMappingData_macOS.m:136 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAggregateClusterMappingData_macOS.m:140 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAggregateClusterMappingData_macOS.m:148 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAggregateClusterMappingData_macOS.m:18 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAggregateClusterMappingData_macOS.m:26 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAggregateClusterMappingData_macOS.m:30 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAggregateClusterMappingData_macOS.m:34 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAggregateClusterMappingData_macOS.m:40 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAggregateClusterMappingData_macOS.m:44 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAggregateClusterMappingData_macOS.m:48 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAggregateClusterMappingData_macOS.m:52 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAggregateClusterMappingData_macOS.m:58 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAggregateClusterMappingData_macOS.m:62 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAggregateClusterMappingData_macOS.m:66 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAggregateClusterMappingData_macOS.m:70 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAggregateClusterMappingData_macOS.m:76 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAggregateClusterMappingData_macOS.m:80 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAggregateClusterMappingData_macOS.m:84 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAggregateClusterMappingData_macOS.m:88 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAggregateClusterMappingData_macOS.m:94 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAggregateClusterMappingData_macOS.m:98 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAppCapabilities_macOS.m:19 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAppCapabilities_macOS.m:23 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAppCapabilities_macOS.m:27 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAppCapabilityMetadata_macOS.m:17 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAppCapabilityMetadata_macOS.m:21 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAppCapabilityMetadata_macOS.m:25 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAppCapabilityMetadata_macOS.m:29 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAppCapabilityMetadata_macOS.m:33 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAppCapabilityMetadata_macOS.m:37 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAppClusterMapping_macOS.m:18 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAppClusterMapping_macOS.m:28 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAppClusterMapping_macOS.m:40 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAppClusterMapping_macOS.m:44 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDClaimApplicationsRequestOptions_macOS.m:18 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDClaimApplicationsRequestOptions_macOS.m:24 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDClaimApplicationsRequestOptions_macOS.m:30 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDClaimApplicationsRequest_macOS.m:18 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDClaimApplicationsRequest_macOS.m:24 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDCoding_macOS.m:18 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDCoding_macOS.m:26 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDCoding_macOS.m:32 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDCoding_macOS.m:38 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDCompleteCoordinatorsRequest_macOS.m:18 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDCompleteCoordinatorsRequest_macOS.m:26 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDCreatePlaceholdersRequestOptions_macOS.m:18 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDCreatePlaceholdersRequestOptions_macOS.m:24 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDCreatePlaceholdersRequest_macOS.m:18 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDCreatePlaceholdersRequest_macOS.m:24 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDDebug_macOS.m:18 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDDebug_macOS.m:28 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDDebug_macOS.m:36 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDDebug_macOS.m:42 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDDebug_macOS.m:48 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDDebug_macOS.m:52 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDDebug_macOS.m:56 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDDownloadQueueRequestOptions_macOS.m:18 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDDownloadQueueRequestOptions_macOS.m:24 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDEphemeralRequest_macOS.m:18 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDExternalManifestRequestOptions_macOS.m:18 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDExternalManifestRequest_macOS.m:20 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDExternalManifestRequest_macOS.m:26 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDExternalManifestResponse_macOS.m:18 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDExternalManifestResponse_macOS.m:24 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDExternalManifestResponse_macOS.m:30 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDIAPInfoRequestOptions_macOS.m:18 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDIAPInfoRequest_macOS.m:18 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDIAPInfoResponse_macOS.m:18 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDIAPInfoResponse_macOS.m:24 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDIAPInfoResponse_macOS.m:30 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDIAPInfoUpdateRequest_macOS.m:18 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDInstallManifestRequestOptions_macOS.m:18 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDInstallManifestRequestOptions_macOS.m:24 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDInstallManifestRequestResponse_macOS.m:18 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDInstallManifestRequestResponse_macOS.m:24 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDInstallManifestRequest_macOS.m:20 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJobActivity_macOS.m:18 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJobActivity_macOS.m:26 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJobActivity_macOS.m:34 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJobActivity_macOS.m:46 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJobActivity_macOS.m:50 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJobAsset_macOS.m:18 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJobAsset_macOS.m:28 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJobAsset_macOS.m:40 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJobAsset_macOS.m:44 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJobManagerOptions_macOS.m:18 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJobManagerOptions_macOS.m:28 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJobManagerOptions_macOS.m:40 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJobManagerOptions_macOS.m:44 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJobManager_macOS.m:18 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJobManager_macOS.m:24 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJobManifest_macOS.m:18 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJobManifest_macOS.m:24 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJobManifest_macOS.m:34 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJobManifest_macOS.m:46 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJobManifest_macOS.m:50 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJobOptions_macOS.m:18 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJobOptions_macOS.m:32 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJobOptions_macOS.m:36 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJob_macOS.m:18 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJob_macOS.m:28 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJob_macOS.m:40 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJob_macOS.m:44 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDLaunchableAppsRequestOptions_macOS.m:18 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDLaunchableAppsRequest_macOS.m:18 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDLaunchableAppsRequest_macOS.m:24 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDLaunchableAppsRequest_macOS.m:32 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDLaunchableAppsResponse_macOS.m:20 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDLaunchableAppsResponse_macOS.m:26 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDManagedApplicationRequestOptions_macOS.m:18 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDManagedApplicationRequest_macOS.m:18 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDManagedApplicationRequest_macOS.m:24 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDManagedApplicationRequest_macOS.m:32 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDMigrationRequestOptions_macOS.m:18 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDMigrationRequestOptions_macOS.m:24 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDMigrationRequest_macOS.m:20 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDMigrationRequest_macOS.m:26 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDMigrationRequest_macOS.m:34 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPersistentRequest_macOS.m:18 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPersistentRequest_macOS.m:26 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPersistentRequest_macOS.m:30 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPersonalizationStore_macOS.m:18 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPostBulletinRequestOptions_macOS.m:18 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPostBulletinRequest_macOS.m:20 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPostBulletinRequest_macOS.m:26 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPurchaseRequestOptions_macOS.m:18 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPurchaseRequestOptions_macOS.m:24 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPurchaseRequest_macOS.m:20 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPurchaseRequest_macOS.m:26 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPurgeAppsRequestOptions_macOS.m:18 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPurgeAppsRequestOptions_macOS.m:24 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPurgeAppsRequest_macOS.m:20 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPurgeAppsRequest_macOS.m:26 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPurgeAppsResponse_macOS.m:18 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPurgeAppsResponse_macOS.m:24 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPurgeAppsResponse_macOS.m:30 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPurgeAppsResponse_macOS.m:35 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPurgeableAppRequestOptions_macOS.m:18 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPurgeableAppRequestOptions_macOS.m:24 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPurgeableAppRequest_macOS.m:20 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPurgeableAppRequest_macOS.m:26 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPurgeableAppResponse_macOS.m:18 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPurgeableAppResponse_macOS.m:24 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPurgeableAppResponse_macOS.m:29 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPurgeableAppResponse_macOS.m:35 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPurgeableApp_macOS.m:18 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPurgeableApp_macOS.m:26 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPurgeableApp_macOS.m:34 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPurgeableApp_macOS.m:46 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPurgeableApp_macOS.m:50 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPushCacheDeleteUpdateRequest_macOS.m:18 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPushCacheDeleteUpdateRequest_macOS.m:26 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDRegisterListenerOptions_macOS.m:18 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDRegisterListenerOptions_macOS.m:32 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDRegisterListenerOptions_macOS.m:36 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDRequestBroker_macOS.m:18 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDRequestBroker_macOS.m:24 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDRequestBroker_macOS.m:28 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDRequest_macOS.m:18 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDRequest_macOS.m:26 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDRequest_macOS.m:36 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDRequest_macOS.m:40 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDRestoreApplicationsRequestOptions_macOS.m:18 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDRestoreApplicationsRequestOptions_macOS.m:24 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDRestoreApplicationsRequestResponse_macOS.m:20 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDRestoreApplicationsRequestResponse_macOS.m:26 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDRestoreApplicationsRequest_macOS.m:18 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDRestoreApplicationsRequest_macOS.m:24 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDRestoreDemotedApplicationsRequestOptions_macOS.m:18 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDRestoreDemotedApplicationsRequestOptions_macOS.m:24 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDRestoreDemotedApplicationsRequestOptions_macOS.m:30 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDRestoreDemotedApplicationsRequest_macOS.m:20 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDRestoreDemotedApplicationsRequest_macOS.m:28 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDRollableLog_macOS.m:18 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDRollableLog_macOS.m:24 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDSoftwareUpdateMetrics_macOS.m:18 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDSoftwareUpdateMetrics_macOS.m:28 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDSoftwareUpdateMetrics_macOS.m:40 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDSoftwareUpdateMetrics_macOS.m:44 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDSystemAppRequest_macOS.m:18 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDSystemAppRequest_macOS.m:24 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDSystemAppRequest_macOS.m:30 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDUpdateMetricsStore_macOS.m:18 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDUpdateMetricsStore_macOS.m:26 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDUpdateMetricsStore_macOS.m:30 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDUpdatePollMetrics_macOS.m:18 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDUpdatePollMetrics_macOS.m:24 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDUpdatePollMetrics_macOS.m:32 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDUpdateWatchApps_macOS.m:18 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDUpdateWatchApps_macOS.m:24 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/XPC/Updates/ASDSoftwareUpdatesStore_macOS.m:169 : Not supported on macOS"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/f1d3dab2-fe51-11ef-979c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/XPC/Updates/ASDSoftwareUpdatesStore_macOS.m:200 : Not supported on macOS"
+ "[%@]: bundleID: %@ accountID: %@ bagKey: %@ buyParams: %@ extensionsToEnable: %lu isBackgroundUpdate: %d isRedownload: %d isUpdate: %d isPreorder: %d itemID: %@ itemName: %@ purchaseID: %lld vendorName: %@ softwarePlatform: %ld remoteDownloadIdentifiers: %@]"
+ "_chunkSize"
+ "_clearHashes"
+ "_cryptHashes"
+ "_remoteDeviceID"
+ "_remoteDownloadIdentifiers"
+ "chunkSize"
+ "clearHashes"
+ "cryptHashes"
+ "executeQueryWithPredicate:onPairedDevice:remoteDeviceID:withResultHandler:"
+ "executeQueryWithPredicate:onRemoteDevice:withReplyHandler:"
+ "executeUpdatesQueryWithPredicateReloadingFromServer:onPairedDevice:remoteDeviceID:withResultHandler:"
+ "isManaged"
+ "managed"
+ "managed = 1"
+ "remoteDownloadIdentifiers"
+ "setChunkSize:"
+ "setClearHashes:"
+ "setCryptHashes:"
+ "setRemoteDownloadIdentifiers:"
+ "v40@0:8@\"NSPredicate\"16@\"NSString\"24@?<v@?@\"NSArray\"@\"NSError\">32"
+ "v44@0:8B16@20@28@?36"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Services/InstallApps/Metadata/ASDWatchAppMetadata.m:156 : Unsupported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Services/InstallApps/Metadata/ASDWatchAppMetadata.m:162 : Unsupported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Services/InstallApps/Metadata/ASDWatchAppMetadata.m:167 : Unsupported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Services/InstallApps/Metadata/ASDWatchAppMetadata.m:172 : Unsupported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAccountLookupRequestOptions_macOS.m:18 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAccountLookupRequest_macOS.m:18 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAccountLookupRequest_macOS.m:24 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAccountLookupResponse_macOS.m:20 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAccountLookupResponse_macOS.m:26 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAccountLookupResponse_macOS.m:32 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAccountLookupResponse_macOS.m:38 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAggregateClusterMappingData_macOS.m:102 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAggregateClusterMappingData_macOS.m:106 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAggregateClusterMappingData_macOS.m:112 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAggregateClusterMappingData_macOS.m:116 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAggregateClusterMappingData_macOS.m:120 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAggregateClusterMappingData_macOS.m:136 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAggregateClusterMappingData_macOS.m:140 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAggregateClusterMappingData_macOS.m:148 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAggregateClusterMappingData_macOS.m:18 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAggregateClusterMappingData_macOS.m:26 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAggregateClusterMappingData_macOS.m:30 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAggregateClusterMappingData_macOS.m:34 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAggregateClusterMappingData_macOS.m:40 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAggregateClusterMappingData_macOS.m:44 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAggregateClusterMappingData_macOS.m:48 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAggregateClusterMappingData_macOS.m:52 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAggregateClusterMappingData_macOS.m:58 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAggregateClusterMappingData_macOS.m:62 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAggregateClusterMappingData_macOS.m:66 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAggregateClusterMappingData_macOS.m:70 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAggregateClusterMappingData_macOS.m:76 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAggregateClusterMappingData_macOS.m:80 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAggregateClusterMappingData_macOS.m:84 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAggregateClusterMappingData_macOS.m:88 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAggregateClusterMappingData_macOS.m:94 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAggregateClusterMappingData_macOS.m:98 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAppCapabilities_macOS.m:19 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAppCapabilities_macOS.m:23 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAppCapabilities_macOS.m:27 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAppCapabilityMetadata_macOS.m:17 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAppCapabilityMetadata_macOS.m:21 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAppCapabilityMetadata_macOS.m:25 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAppCapabilityMetadata_macOS.m:29 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAppCapabilityMetadata_macOS.m:33 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAppCapabilityMetadata_macOS.m:37 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAppClusterMapping_macOS.m:18 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAppClusterMapping_macOS.m:28 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAppClusterMapping_macOS.m:40 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDAppClusterMapping_macOS.m:44 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDClaimApplicationsRequestOptions_macOS.m:18 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDClaimApplicationsRequestOptions_macOS.m:24 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDClaimApplicationsRequestOptions_macOS.m:30 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDClaimApplicationsRequest_macOS.m:18 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDClaimApplicationsRequest_macOS.m:24 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDCoding_macOS.m:18 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDCoding_macOS.m:26 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDCoding_macOS.m:32 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDCoding_macOS.m:38 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDCompleteCoordinatorsRequest_macOS.m:18 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDCompleteCoordinatorsRequest_macOS.m:26 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDCreatePlaceholdersRequestOptions_macOS.m:18 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDCreatePlaceholdersRequestOptions_macOS.m:24 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDCreatePlaceholdersRequest_macOS.m:18 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDCreatePlaceholdersRequest_macOS.m:24 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDDebug_macOS.m:18 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDDebug_macOS.m:28 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDDebug_macOS.m:36 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDDebug_macOS.m:42 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDDebug_macOS.m:48 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDDebug_macOS.m:52 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDDebug_macOS.m:56 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDDownloadQueueRequestOptions_macOS.m:18 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDDownloadQueueRequestOptions_macOS.m:24 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDEphemeralRequest_macOS.m:18 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDExternalManifestRequestOptions_macOS.m:18 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDExternalManifestRequest_macOS.m:20 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDExternalManifestRequest_macOS.m:26 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDExternalManifestResponse_macOS.m:18 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDExternalManifestResponse_macOS.m:24 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDExternalManifestResponse_macOS.m:30 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDIAPInfoRequestOptions_macOS.m:18 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDIAPInfoRequest_macOS.m:18 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDIAPInfoResponse_macOS.m:18 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDIAPInfoResponse_macOS.m:24 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDIAPInfoResponse_macOS.m:30 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDIAPInfoUpdateRequest_macOS.m:18 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDInstallManifestRequestOptions_macOS.m:18 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDInstallManifestRequestOptions_macOS.m:24 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDInstallManifestRequestResponse_macOS.m:18 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDInstallManifestRequestResponse_macOS.m:24 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDInstallManifestRequest_macOS.m:20 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJobActivity_macOS.m:18 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJobActivity_macOS.m:26 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJobActivity_macOS.m:34 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJobActivity_macOS.m:46 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJobActivity_macOS.m:50 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJobAsset_macOS.m:18 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJobAsset_macOS.m:28 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJobAsset_macOS.m:40 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJobAsset_macOS.m:44 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJobManagerOptions_macOS.m:18 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJobManagerOptions_macOS.m:28 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJobManagerOptions_macOS.m:40 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJobManagerOptions_macOS.m:44 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJobManager_macOS.m:18 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJobManager_macOS.m:24 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJobManifest_macOS.m:18 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJobManifest_macOS.m:24 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJobManifest_macOS.m:34 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJobManifest_macOS.m:46 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJobManifest_macOS.m:50 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJobOptions_macOS.m:18 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJobOptions_macOS.m:32 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJobOptions_macOS.m:36 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJob_macOS.m:18 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJob_macOS.m:28 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJob_macOS.m:40 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDJob_macOS.m:44 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDLaunchableAppsRequestOptions_macOS.m:18 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDLaunchableAppsRequest_macOS.m:18 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDLaunchableAppsRequest_macOS.m:24 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDLaunchableAppsRequest_macOS.m:32 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDLaunchableAppsResponse_macOS.m:20 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDLaunchableAppsResponse_macOS.m:26 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDManagedApplicationRequestOptions_macOS.m:18 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDManagedApplicationRequest_macOS.m:18 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDManagedApplicationRequest_macOS.m:24 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDManagedApplicationRequest_macOS.m:32 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDMigrationRequestOptions_macOS.m:18 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDMigrationRequestOptions_macOS.m:24 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDMigrationRequest_macOS.m:20 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDMigrationRequest_macOS.m:26 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDMigrationRequest_macOS.m:34 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPersistentRequest_macOS.m:18 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPersistentRequest_macOS.m:26 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPersistentRequest_macOS.m:30 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPersonalizationStore_macOS.m:18 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPostBulletinRequestOptions_macOS.m:18 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPostBulletinRequest_macOS.m:20 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPostBulletinRequest_macOS.m:26 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPurchaseRequestOptions_macOS.m:18 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPurchaseRequestOptions_macOS.m:24 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPurchaseRequest_macOS.m:20 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPurchaseRequest_macOS.m:26 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPurgeAppsRequestOptions_macOS.m:18 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPurgeAppsRequestOptions_macOS.m:24 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPurgeAppsRequest_macOS.m:20 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPurgeAppsRequest_macOS.m:26 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPurgeAppsResponse_macOS.m:18 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPurgeAppsResponse_macOS.m:24 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPurgeAppsResponse_macOS.m:30 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPurgeAppsResponse_macOS.m:35 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPurgeableAppRequestOptions_macOS.m:18 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPurgeableAppRequestOptions_macOS.m:24 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPurgeableAppRequest_macOS.m:20 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPurgeableAppRequest_macOS.m:26 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPurgeableAppResponse_macOS.m:18 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPurgeableAppResponse_macOS.m:24 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPurgeableAppResponse_macOS.m:29 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPurgeableAppResponse_macOS.m:35 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPurgeableApp_macOS.m:18 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPurgeableApp_macOS.m:26 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPurgeableApp_macOS.m:34 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPurgeableApp_macOS.m:46 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPurgeableApp_macOS.m:50 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPushCacheDeleteUpdateRequest_macOS.m:18 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDPushCacheDeleteUpdateRequest_macOS.m:26 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDRegisterListenerOptions_macOS.m:18 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDRegisterListenerOptions_macOS.m:32 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDRegisterListenerOptions_macOS.m:36 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDRequestBroker_macOS.m:18 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDRequestBroker_macOS.m:24 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDRequestBroker_macOS.m:28 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDRequest_macOS.m:18 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDRequest_macOS.m:26 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDRequest_macOS.m:36 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDRequest_macOS.m:40 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDRestoreApplicationsRequestOptions_macOS.m:18 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDRestoreApplicationsRequestOptions_macOS.m:24 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDRestoreApplicationsRequestResponse_macOS.m:20 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDRestoreApplicationsRequestResponse_macOS.m:26 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDRestoreApplicationsRequest_macOS.m:18 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDRestoreApplicationsRequest_macOS.m:24 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDRestoreDemotedApplicationsRequestOptions_macOS.m:18 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDRestoreDemotedApplicationsRequestOptions_macOS.m:24 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDRestoreDemotedApplicationsRequestOptions_macOS.m:30 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDRestoreDemotedApplicationsRequest_macOS.m:20 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDRestoreDemotedApplicationsRequest_macOS.m:28 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDRollableLog_macOS.m:18 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDRollableLog_macOS.m:24 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDSoftwareUpdateMetrics_macOS.m:18 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDSoftwareUpdateMetrics_macOS.m:28 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDSoftwareUpdateMetrics_macOS.m:40 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDSoftwareUpdateMetrics_macOS.m:44 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDSystemAppRequest_macOS.m:18 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDSystemAppRequest_macOS.m:24 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDSystemAppRequest_macOS.m:30 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDUpdateMetricsStore_macOS.m:18 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDUpdateMetricsStore_macOS.m:26 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDUpdateMetricsStore_macOS.m:30 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDUpdatePollMetrics_macOS.m:18 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDUpdatePollMetrics_macOS.m:24 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDUpdatePollMetrics_macOS.m:32 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDUpdateWatchApps_macOS.m:18 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/Stubs/ASDUpdateWatchApps_macOS.m:24 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/XPC/Updates/ASDSoftwareUpdatesStore_macOS.m:169 : Not supported on macOS"
- "Unimplemented at /AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppStoreDaemon/Libraries/AppStoreDaemon/XPC/Updates/ASDSoftwareUpdatesStore_macOS.m:200 : Not supported on macOS"
- "[%@]: bundleID: %@ accountID: %@ bagKey: %@ buyParams: %@ extensionsToEnable: %lu isBackgroundUpdate: %d isRedownload: %d isUpdate: %d itemID: %@ itemName: %@ purchaseID: %lld vendorName: %@ softwarePlatform: %ld]"
- "executeQueryWithPredicate:onPairedDevice:withResultHandler:"
- "executeUpdatesQueryWithPredicateReloadingFromServer:onPairedDevice:withResultHandler:"

```
