## threadradiod

> `/System/Library/PrivateFrameworks/CoreThreadRadio.framework/threadradiod`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-446.0.4.0.0
-  __TEXT.__text: 0x41b030
-  __TEXT.__auth_stubs: 0x12bf0
-  __TEXT.__objc_stubs: 0xa180
-  __TEXT.__init_offsets: 0xb4
-  __TEXT.__objc_methlist: 0x6ae4
-  __TEXT.__gcc_except_tab: 0x2a7f0
-  __TEXT.__const: 0x86a4
-  __TEXT.__oslogstring: 0x28cd9
-  __TEXT.__cstring: 0x37523
-  __TEXT.__objc_classname: 0x6eb
-  __TEXT.__objc_methname: 0xf8d1
-  __TEXT.__objc_methtype: 0x4467
+447.0.1.0.0
+  __TEXT.__text: 0x41d36c
+  __TEXT.__auth_stubs: 0x12c00
+  __TEXT.__objc_stubs: 0xa280
+  __TEXT.__init_offsets: 0xbc
+  __TEXT.__objc_methlist: 0x6b14
+  __TEXT.__gcc_except_tab: 0x2ad28
+  __TEXT.__const: 0x86c4
+  __TEXT.__oslogstring: 0x2907b
+  __TEXT.__cstring: 0x37873
+  __TEXT.__objc_classname: 0x70b
+  __TEXT.__objc_methname: 0xf9d1
+  __TEXT.__objc_methtype: 0x4486
   __TEXT.__swift5_typeref: 0x572
   __TEXT.__swift5_capture: 0x60c
   __TEXT.__swift5_fieldmd: 0x130

   __TEXT.__swift_as_entry: 0xac
   __TEXT.__swift_as_ret: 0x88
   __TEXT.__swift_as_cont: 0x1dc
-  __TEXT.__unwind_info: 0x14818
+  __TEXT.__unwind_info: 0x148b8
   __TEXT.__eh_frame: 0x1f68
   __DATA_CONST.__const: 0xdcc8
-  __DATA_CONST.__cfstring: 0x6de0
+  __DATA_CONST.__cfstring: 0x7060
   __DATA_CONST.__objc_classlist: 0x190
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x140
-  __DATA_CONST.__auth_got: 0x9610
+  __DATA_CONST.__auth_got: 0x9618
   __DATA_CONST.__got: 0xbc0
   __DATA_CONST.__auth_ptr: 0x240
   __DATA.__objc_const: 0x8b68
-  __DATA.__objc_selrefs: 0x38c0
+  __DATA.__objc_selrefs: 0x38f8
   __DATA.__objc_ivar: 0x55c
   __DATA.__objc_data: 0x1060
   __DATA.__data: 0xa39

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 18306
-  Symbols:   23486
-  CStrings:  13565
+  Functions: 18329
+  Symbols:   23509
+  CStrings:  13613
 
Symbols:
+ -[THThreadNetworkCredentialsKeychainBackingStore getActiveRecords:matchPolicy:]
+ -[ThreadNetworkManagerInstance saveThreadConfigurationAOD:passPhrase:uuid:]
+ -[ThreadNetworkManagerInstance(MB_extension) performMeshCoPBrowse:]
+ -[ThreadNetworkManagerInstance(TimeSyncMetrics) deserializeTimeSyncAggregatedFromByteStream:intoDictionary:]
+ -[ThreadNetworkManagerInstance(TimeSyncMetrics) deserializeTimeSyncMetricsFromByteStreamPerRecord:intoDictionary:]
+ -[ThreadNetworkManagerInstance(TimeSyncMetrics) getTimeSyncMetrics]
+ /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Binaries/CoreThreadRadio/install/Symbols/BuiltProducts/libopenthread-ftd.a(heap-2921d12db529945fad3eee3a28d64a60.o)
+ /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Binaries/CoreThreadRadio/install/Symbols/BuiltProducts/libopenthread-ftd.a(heap-b711cf914b43b7f5d57de48f7ac0f025.o)
+ __GLOBAL__sub_I_ThreadNetworkManagerInstance_MB_extension.mm
+ __GLOBAL__sub_I_ThreadNetworkManagerInstance_TimeSyncMetrics_extension.mm
+ __OBJC_$_INSTANCE_METHODS_ThreadNetworkManagerInstance(MB_extension|SM_extension|TimeSyncMetrics|syslog_extension|RCP2CAMetrics_extension)
+ __ZL11hexFromDataP6NSData
+ __ZL11strFromDataP6NSData
+ __ZN5boost8any_castIKNSt3__16vectorIhNS1_9allocatorIhEEEEEEPT_PNS_3anyE
+ __ZN5boost8any_castIRKNSt3__16vectorIhNS1_9allocatorIhEEEEEET_RNS_3anyE
+ __ZZ67-[ThreadNetworkManagerInstance(MB_extension) performMeshCoPBrowse:]ENK3$_0clEPKcP8NSString
+ ___67-[ThreadNetworkManagerInstance(MB_extension) performMeshCoPBrowse:]_block_invoke
+ ___67-[ThreadNetworkManagerInstance(TimeSyncMetrics) getTimeSyncMetrics]_block_invoke
+ ___67-[ThreadNetworkManagerInstance(TimeSyncMetrics) getTimeSyncMetrics]_block_invoke_2
+ ___75-[ThreadNetworkManagerInstance saveThreadConfigurationAOD:passPhrase:uuid:]_block_invoke
+ _objc_msgSend$BAFinder
+ _objc_msgSend$deserializeTimeSyncAggregatedFromByteStream:intoDictionary:
+ _objc_msgSend$deserializeTimeSyncMetricsFromByteStreamPerRecord:intoDictionary:
+ _objc_msgSend$getActiveRecords:matchPolicy:
+ _objc_msgSend$numberWithLongLong:
+ _objc_msgSend$numberWithShort:
+ _objc_msgSend$numberWithUnsignedChar:
+ _objc_msgSend$performMeshCoPBrowse:
+ _objc_msgSend$saveThreadConfigurationAOD:passPhrase:uuid:
+ _objc_msgSend$setBAFinder:
+ _objc_opt_respondsToSelector
- -[THThreadNetworkCredentialsKeychainBackingStore getActiveRecords:]
- -[ThreadNetworkManagerInstance saveThreadConfigurationAOD:passPhrase:]
- /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Binaries/CoreThreadRadio/install/Symbols/BuiltProducts/libopenthread-ftd.a(heap-0f747e41226482d301b012c4009d050a.o)
- /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Binaries/CoreThreadRadio/install/Symbols/BuiltProducts/libopenthread-ftd.a(heap-b7bc1e5ca63c0bc1cbfecc051573a328.o)
- __OBJC_$_INSTANCE_METHODS_ThreadNetworkManagerInstance(SM_extension|syslog_extension|RCP2CAMetrics_extension)
- ___70-[ThreadNetworkManagerInstance saveThreadConfigurationAOD:passPhrase:]_block_invoke
- _objc_msgSend$getActiveRecords:
- _objc_msgSend$saveThreadConfigurationAOD:passPhrase:
CStrings:
+ " Morty_Version: V0.447.0.1"
+ "%s : %d: malformed xp key in TXT record for server :%@, expected %d bytes but got %lu, skipping."
+ "%s : %d: network name :%@ matches with mdns record :%@, but xpanid :%@ differs from :%@"
+ "%s : %d: no xp key in TXT record for server :%@, continue to next network if available."
+ "%s : %d: xpanid :%@ matches with mdns record :%@"
+ "%s : MeshCoP browse found %ld border agents"
+ "%s : MeshCoP browse started..."
+ "%s : MeshCoP browse timed out"
+ "%s : Must not be called on main thread"
+ "%s : [%ld] name=%@, nn=%@, xp=%@, xa=%@"
+ "%s : performMeshCoPBrowse failed with ret=%d"
+ "%s:%d: Entered. Matching records (%lu) with Mdns records, policy :%lu"
+ "%s:%d: Failed to allocate matchedRecords"
+ "%s:%d: record for network %@ already matched by earlier border router, skipping"
+ "%s_%s"
+ "-[THThreadNetworkCredentialsKeychainBackingStore getActiveRecords:matchPolicy:]"
+ "-[ThreadNetworkManagerInstance saveThreadConfigurationAOD:passPhrase:uuid:]"
+ "-[ThreadNetworkManagerInstance(MB_extension) performMeshCoPBrowse:]"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.3.Internal.sdk/usr/include/c++/v1/__hash_table:1855: libc++ Hardening assertion __p != end() failed: unordered container::erase(iterator) called with a non-dereferenceable iterator\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.3.Internal.sdk/usr/include/c++/v1/__hash_table:242: libc++ Hardening assertion __node_ != nullptr failed: Attempted to dereference a non-dereferenceable unordered container iterator\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.3.Internal.sdk/usr/include/c++/v1/__hash_table:248: libc++ Hardening assertion __node_ != nullptr failed: Attempted to dereference a non-dereferenceable unordered container iterator\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.3.Internal.sdk/usr/include/c++/v1/__hash_table:254: libc++ Hardening assertion __node_ != nullptr failed: Attempted to increment a non-incrementable unordered container iterator\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.3.Internal.sdk/usr/include/c++/v1/__memory/construct_at.h:47: libc++ Hardening assertion __location != nullptr failed: null pointer given to construct_at\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.3.Internal.sdk/usr/include/c++/v1/__memory/construct_at.h:59: libc++ Hardening assertion __loc != nullptr failed: null pointer given to destroy_at\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.3.Internal.sdk/usr/include/c++/v1/__memory/unique_ptr.h:583: libc++ Hardening assertion __checker_.__in_bounds<deleter_type>(std::__to_address(__ptr_), __i) failed: unique_ptr<T[]>::operator[](index): index out of range\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.3.Internal.sdk/usr/include/c++/v1/deque:1565: libc++ Hardening assertion !empty() failed: deque::front called on an empty deque\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.3.Internal.sdk/usr/include/c++/v1/deque:2199: libc++ Hardening assertion !empty() failed: deque::pop_front called on an empty deque\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.3.Internal.sdk/usr/include/c++/v1/streambuf:301: libc++ Hardening assertion std::__is_valid_range(__gbeg, __gnext) failed: [gbeg, gnext) must be a valid range\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.3.Internal.sdk/usr/include/c++/v1/streambuf:302: libc++ Hardening assertion std::__is_valid_range(__gbeg, __gend) failed: [gbeg, gend) must be a valid range\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.3.Internal.sdk/usr/include/c++/v1/streambuf:303: libc++ Hardening assertion std::__is_valid_range(__gnext, __gend) failed: [gnext, gend) must be a valid range\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.3.Internal.sdk/usr/include/c++/v1/streambuf:319: libc++ Hardening assertion std::__is_valid_range(__pbeg, __pend) failed: [pbeg, pend) must be a valid range\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.3.Internal.sdk/usr/include/c++/v1/string:1074: libc++ Hardening assertion __s != nullptr failed: basic_string(const char*) detected nullptr\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.3.Internal.sdk/usr/include/c++/v1/string:2219: libc++ Hardening assertion __s < __min_cap failed: __s should never be greater than or equal to the short string capacity\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.3.Internal.sdk/usr/include/c++/v1/string:2226: libc++ Hardening assertion !__rep_.__s.__is_long_ failed: String has to be short when trying to get the short size\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.3.Internal.sdk/usr/include/c++/v1/string:2235: libc++ Hardening assertion __rep_.__l.__is_long_ failed: String has to be long when trying to get the long size\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.3.Internal.sdk/usr/include/c++/v1/string:2247: libc++ Hardening assertion __rep_.__l.__is_long_ failed: String has to be long when trying to get the long capacity\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.3.Internal.sdk/usr/include/c++/v1/string:2252: libc++ Hardening assertion __rep_.__l.__is_long_ failed: String has to be long when trying to get the long pointer\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.3.Internal.sdk/usr/include/c++/v1/string:2257: libc++ Hardening assertion __rep_.__l.__is_long_ failed: String has to be long when trying to get the long pointer\n"
+ "@32@0:8@16Q24"
+ "B32@0:8r*16@24"
+ "MB_extension"
+ "MeshCoPBrowse"
+ "TNM:TimeSync: error processing metrics: %s"
+ "TNM:TimeSync: failed to get kWPANTUNDProperty_TimeSyncMetrics: %s(%d)"
+ "TNM:TimeSync: no activity this window, deferred"
+ "TNM:TimeSync: stream is %zu bytes, expected at least %zu"
+ "TNM:TimeSync: submitted aggregated event plus %lu of %u records"
+ "TimeSyncMetrics"
+ "ba_%ld"
+ "border_agent_count"
+ "com.apple.Flagstone.flagstoneTimeSyncAggregatedMetrics"
+ "com.apple.Flagstone.flagstoneTimeSyncClientInfoMetrics"
+ "deserializeTimeSyncAggregatedFromByteStream:intoDictionary:"
+ "deserializeTimeSyncMetricsFromByteStreamPerRecord:intoDictionary:"
+ "getActiveRecords:matchPolicy:"
+ "getTimeSyncMetrics"
+ "mn"
+ "numberWithLongLong:"
+ "numberWithShort:"
+ "numberWithUnsignedChar:"
+ "performMeshCoPBrowse:"
+ "saveThreadConfigurationAOD:passPhrase:uuid:"
+ "timeSync_client_publish_totalAcksSent"
+ "timeSync_client_publish_totalRequestsSent"
+ "timeSync_client_publish_totalResponsesReceived"
+ "timeSync_server_publish_clientInfo_clientToServerDirtyBit"
+ "timeSync_server_publish_clientInfo_driftPpm"
+ "timeSync_server_publish_clientInfo_e2eDelayUs"
+ "timeSync_server_publish_clientInfo_e2eErrorUs"
+ "timeSync_server_publish_clientInfo_numHops"
+ "timeSync_server_publish_clientInfo_serverToClientDirtyBit"
+ "timeSync_server_publish_totalAcksReceived"
+ "timeSync_server_publish_totalDurationMs"
+ "timeSync_server_publish_totalRequestsReceived"
+ "timeSync_server_publish_totalResponsesSent"
- " Morty_Version: V0.446.0.4"
- "%s:%d: Entered. Matching records (%lu) with Mdns records"
- "%s:%d: Failed to allocate recordList"
- "-[THThreadNetworkCredentialsKeychainBackingStore getActiveRecords:]"
- "-[ThreadNetworkManagerInstance saveThreadConfigurationAOD:passPhrase:]"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/include/c++/v1/__hash_table:1855: libc++ Hardening assertion __p != end() failed: unordered container::erase(iterator) called with a non-dereferenceable iterator\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/include/c++/v1/__hash_table:242: libc++ Hardening assertion __node_ != nullptr failed: Attempted to dereference a non-dereferenceable unordered container iterator\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/include/c++/v1/__hash_table:248: libc++ Hardening assertion __node_ != nullptr failed: Attempted to dereference a non-dereferenceable unordered container iterator\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/include/c++/v1/__hash_table:254: libc++ Hardening assertion __node_ != nullptr failed: Attempted to increment a non-incrementable unordered container iterator\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/include/c++/v1/__memory/construct_at.h:47: libc++ Hardening assertion __location != nullptr failed: null pointer given to construct_at\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/include/c++/v1/__memory/construct_at.h:59: libc++ Hardening assertion __loc != nullptr failed: null pointer given to destroy_at\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/include/c++/v1/__memory/unique_ptr.h:583: libc++ Hardening assertion __checker_.__in_bounds<deleter_type>(std::__to_address(__ptr_), __i) failed: unique_ptr<T[]>::operator[](index): index out of range\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/include/c++/v1/deque:1565: libc++ Hardening assertion !empty() failed: deque::front called on an empty deque\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/include/c++/v1/deque:2199: libc++ Hardening assertion !empty() failed: deque::pop_front called on an empty deque\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/include/c++/v1/streambuf:301: libc++ Hardening assertion std::__is_valid_range(__gbeg, __gnext) failed: [gbeg, gnext) must be a valid range\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/include/c++/v1/streambuf:302: libc++ Hardening assertion std::__is_valid_range(__gbeg, __gend) failed: [gbeg, gend) must be a valid range\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/include/c++/v1/streambuf:303: libc++ Hardening assertion std::__is_valid_range(__gnext, __gend) failed: [gnext, gend) must be a valid range\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/include/c++/v1/streambuf:319: libc++ Hardening assertion std::__is_valid_range(__pbeg, __pend) failed: [pbeg, pend) must be a valid range\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/include/c++/v1/string:1074: libc++ Hardening assertion __s != nullptr failed: basic_string(const char*) detected nullptr\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/include/c++/v1/string:2219: libc++ Hardening assertion __s < __min_cap failed: __s should never be greater than or equal to the short string capacity\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/include/c++/v1/string:2226: libc++ Hardening assertion !__rep_.__s.__is_long_ failed: String has to be short when trying to get the short size\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/include/c++/v1/string:2235: libc++ Hardening assertion __rep_.__l.__is_long_ failed: String has to be long when trying to get the long size\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/include/c++/v1/string:2247: libc++ Hardening assertion __rep_.__l.__is_long_ failed: String has to be long when trying to get the long capacity\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/include/c++/v1/string:2252: libc++ Hardening assertion __rep_.__l.__is_long_ failed: String has to be long when trying to get the long pointer\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/include/c++/v1/string:2257: libc++ Hardening assertion __rep_.__l.__is_long_ failed: String has to be long when trying to get the long pointer\n"
- "getActiveRecords:"
- "saveThreadConfigurationAOD:passPhrase:"
```
