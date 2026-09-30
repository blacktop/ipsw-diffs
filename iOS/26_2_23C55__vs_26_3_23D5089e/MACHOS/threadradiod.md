## threadradiod

> `/System/Library/PrivateFrameworks/CoreThreadRadio.framework/threadradiod`

```diff

-333.0.3.0.0
-  __TEXT.__text: 0x3ed984
+333.0.5.0.0
+  __TEXT.__text: 0x3efbcc
   __TEXT.__auth_stubs: 0x11280
-  __TEXT.__objc_stubs: 0x9920
+  __TEXT.__objc_stubs: 0x9980
   __TEXT.__init_offsets: 0xa4
-  __TEXT.__objc_methlist: 0x65b0
+  __TEXT.__objc_methlist: 0x65d0
   __TEXT.__objc_classname: 0x5f4
-  __TEXT.__cstring: 0x3323e
+  __TEXT.__cstring: 0x33547
   __TEXT.__const: 0x9488
-  __TEXT.__gcc_except_tab: 0x2b830
-  __TEXT.__objc_methname: 0xebe5
-  __TEXT.__oslogstring: 0x22d1f
-  __TEXT.__objc_methtype: 0x3ccd
-  __TEXT.__unwind_info: 0x7b10
+  __TEXT.__gcc_except_tab: 0x2ba38
+  __TEXT.__objc_methname: 0xec8e
+  __TEXT.__oslogstring: 0x233a3
+  __TEXT.__objc_methtype: 0x3ce2
+  __TEXT.__unwind_info: 0x7b58
   __TEXT.__eh_frame: 0x60
   __DATA_CONST.__auth_got: 0x8958
   __DATA_CONST.__got: 0x930
   __DATA_CONST.__auth_ptr: 0x60
-  __DATA_CONST.__const: 0xd5a0
-  __DATA_CONST.__cfstring: 0x6040
+  __DATA_CONST.__const: 0xd618
+  __DATA_CONST.__cfstring: 0x6060
   __DATA_CONST.__objc_classlist: 0x170
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x140
   __DATA.__objc_const: 0x8518
-  __DATA.__objc_selrefs: 0x3668
+  __DATA.__objc_selrefs: 0x3680
   __DATA.__objc_ivar: 0x538
   __DATA.__objc_data: 0xe60
   __DATA.__data: 0x648

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libdns_services.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 765F9045-8F3E-30AA-918F-0827ACF508CA
-  Functions: 17130
-  Symbols:   89235
-  CStrings:  13483
+  UUID: A0B1AEA9-7DB7-3B55-B240-E6B3EEC20613
+  Functions: 17146
+  Symbols:   89277
+  CStrings:  13521
 
Symbols:
+ -[THThreadNetworkCredentialsKeychainBackingStore deleteCurrentNetworkFromRetrieveOrGenerate:]
+ -[THThreadNetworkCredentialsKeychainBackingStore deleteCurrentNetworkFromRetrieveOrGenerate:].cold.1
+ -[THThreadNetworkCredentialsKeychainBackingStore performSyncOperationWithRecord:queue:timeoutValInSec:completion:]
+ -[THThreadNetworkCredentialsKeychainBackingStore storeActiveDataSetRecordAndSyncWithErrComletion:completion:]
+ -[THThreadNetworkCredentialsKeychainBackingStore storeActiveDataSetRecordAndSyncWithErrComletion:completion:].cold.1
+ -[THThreadNetworkCredentialsKeychainBackingStore storeActiveDataSetRecordAndSyncWithErrComletion:completion:].cold.2
+ __100-[THThreadNetworkCredentialsKeychainBackingStore getRecordForPreferredNetwork:anyDsFormat:skipScan:]_block_invoke.120
+ __109-[THThreadNetworkCredentialsKeychainBackingStore retrieveOrGeneratePreferredNetworkInternallyWithCompletion:]_block_invoke.122
+ __109-[THThreadNetworkCredentialsKeychainBackingStore retrieveOrGeneratePreferredNetworkInternallyWithCompletion:]_block_invoke.cold.3
+ __109-[THThreadNetworkCredentialsKeychainBackingStore storeActiveDataSetRecordAndSyncWithErrComletion:completion:]_block_invoke.100
+ __114-[THThreadNetworkCredentialsKeychainBackingStore performSyncOperationWithRecord:queue:timeoutValInSec:completion:]_block_invoke.98
+ __114-[THThreadNetworkCredentialsKeychainBackingStore performSyncOperationWithRecord:queue:timeoutValInSec:completion:]_block_invoke.99
+ __94-[THThreadNetworkCredentialsKeychainBackingStore storeCachedAODasPreferredNetwork:completion:]_block_invoke.114
+ __ZN2ot5Posix18HardwareIdentifier15getHCITransportEv
+ __ZN2ot5Posix18HardwareIdentifier18isProximaTransportEv
+ __ZN2ot5Posix18HardwareIdentifier19getHCITransportTypeEPKc
+ __ZN2ot5Posix18HardwareIdentifier24isCCMappingVendor2Ver101Ev
+ ___109-[THThreadNetworkCredentialsKeychainBackingStore storeActiveDataSetRecordAndSyncWithErrComletion:completion:]_block_invoke
+ ___114-[THThreadNetworkCredentialsKeychainBackingStore performSyncOperationWithRecord:queue:timeoutValInSec:completion:]_block_invoke
+ ___block_descriptor_48_e8_32s40r_e17_v16?0"NSError"8lr40l8s32l8
+ ___block_descriptor_80_e8_32s40s48s56bs64r72r_e17_v16?0"NSError"8lr64l8s32l8r72l8s40l8s48l8s56l8
+ ___block_descriptor_82_e8_32s40s48s56s64bs72r_e8_v16?0Q8lr72l8s32l8s64l8s40l8s48l8s56l8
+ __block_literal_global.119
+ __block_literal_global.187
+ __block_literal_global.195
+ _objc_msgSend$deleteCurrentNetworkFromRetrieveOrGenerate:
+ _objc_msgSend$performSyncOperationWithRecord:queue:timeoutValInSec:completion:
+ _objc_msgSend$storeActiveDataSetRecordAndSyncWithErrComletion:completion:
- __100-[THThreadNetworkCredentialsKeychainBackingStore getRecordForPreferredNetwork:anyDsFormat:skipScan:]_block_invoke.117
- __94-[THThreadNetworkCredentialsKeychainBackingStore storeCachedAODasPreferredNetwork:completion:]_block_invoke.111
- __block_literal_global.116
- __block_literal_global.183
- __block_literal_global.191
CStrings:
+ " Morty_Version: V0.333.0.5"
+ "%s: CKKS response for known is Not good, retrun with error: %@"
+ "%s: CKKS response for known state is Likely good"
+ "%s: Checking CKKS state before storing Thread credentials with sync"
+ "%s: Error, Sync failure %@"
+ "%s: Exiting early - keychain add operation failed, handled duplicate/error scenario (error = %d)"
+ "%s: Failed to create CKKS control object: %@"
+ "%s: Failed to create keychain add dictionary - bad parameter: %@"
+ "%s: Operation already completed by another thread/callback, ignoring duplicate completion"
+ "%s: Returning from sync timeout handler after notifying completion with timeout error: %@"
+ "%s: Sync operation completion handler finished (syncDone=%d)"
+ "%s: Timer Fired, CKKS response for known is Not good as it timedout, retrun with error: %@"
+ "%s:%d Adding Thread network credentials to keychain with sync notification"
+ "%s:%d Initiated keychain add operation for Thread network credentials (network='%@', xpanid=%@, baId=%@, status=%d)"
+ "%s:%d Timer Fired for sync !!! "
+ "%s:%d _SecItemAddAndNotifyOnSync returned success, waiting for async completion"
+ "%s:%d sync is done, syncDone : %d"
+ "%s:%d: Delete current network result: (err=%d)"
+ "%s:%d: Error, Preferred network exists (name : %@, xpanid : %@)  ! But newly created netowrk (name : %@, xpanid : %@) doesn't match with it, let's delete this new network credentials.."
+ "%s:%d: Failed deleting current network credentials: %@"
+ "%s:%d: Request to delete current network for border agent %@"
+ "%s:%d: Timeout waiting for storeActiveDataSetRecordAndSyncWithErrComletion"
+ "%s:%d:Failed to get Preferred network after sync"
+ "%s:%d:Preferred Network exist, use it to start Thread"
+ "-[THThreadNetworkCredentialsKeychainBackingStore deleteCurrentNetworkFromRetrieveOrGenerate:]"
+ "-[THThreadNetworkCredentialsKeychainBackingStore performSyncOperationWithRecord:queue:timeoutValInSec:completion:]"
+ "-[THThreadNetworkCredentialsKeychainBackingStore performSyncOperationWithRecord:queue:timeoutValInSec:completion:]_block_invoke"
+ "-[THThreadNetworkCredentialsKeychainBackingStore retrieveOrGeneratePreferredNetworkInternallyWithCompletion:]_block_invoke_2"
+ "-[THThreadNetworkCredentialsKeychainBackingStore storeActiveDataSetRecordAndSyncWithErrComletion:completion:]"
+ "-[THThreadNetworkCredentialsKeychainBackingStore storeActiveDataSetRecordAndSyncWithErrComletion:completion:]_block_invoke"
+ "/AppleInternal/Library/BuildRoots/4~CDyrugDNGwRmI6zUgbNuBBZAb5NjjTGQZWdutQA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/include/c++/v1/__memory/construct_at.h:65: assertion __loc != nullptr failed: null pointer given to destroy_at\n"
+ "/AppleInternal/Library/BuildRoots/4~CDyrugDNGwRmI6zUgbNuBBZAb5NjjTGQZWdutQA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/include/c++/v1/__tree:166: assertion __x != nullptr failed: Root node shouldn't be null\n"
+ "/AppleInternal/Library/BuildRoots/4~CDyrugDNGwRmI6zUgbNuBBZAb5NjjTGQZWdutQA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/include/c++/v1/__tree:184: assertion __x != nullptr failed: node shouldn't be null\n"
+ "/AppleInternal/Library/BuildRoots/4~CDyrugDNGwRmI6zUgbNuBBZAb5NjjTGQZWdutQA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/include/c++/v1/__tree:194: assertion __x != nullptr failed: node shouldn't be null\n"
+ "/AppleInternal/Library/BuildRoots/4~CDyrugDNGwRmI6zUgbNuBBZAb5NjjTGQZWdutQA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/include/c++/v1/__tree:237: assertion __x != nullptr failed: node shouldn't be null\n"
+ "/AppleInternal/Library/BuildRoots/4~CDyrugDNGwRmI6zUgbNuBBZAb5NjjTGQZWdutQA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/include/c++/v1/__tree:238: assertion __x->__right_ != nullptr failed: node should have a right child\n"
+ "/AppleInternal/Library/BuildRoots/4~CDyrugDNGwRmI6zUgbNuBBZAb5NjjTGQZWdutQA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/include/c++/v1/__tree:256: assertion __x != nullptr failed: node shouldn't be null\n"
+ "/AppleInternal/Library/BuildRoots/4~CDyrugDNGwRmI6zUgbNuBBZAb5NjjTGQZWdutQA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/include/c++/v1/__tree:257: assertion __x->__left_ != nullptr failed: node should have a left child\n"
+ "/AppleInternal/Library/BuildRoots/4~CDyrugDNGwRmI6zUgbNuBBZAb5NjjTGQZWdutQA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/include/c++/v1/__tree:280: assertion __root != nullptr failed: Root of the tree shouldn't be null\n"
+ "/AppleInternal/Library/BuildRoots/4~CDyrugDNGwRmI6zUgbNuBBZAb5NjjTGQZWdutQA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/include/c++/v1/__tree:281: assertion __x != nullptr failed: Can't attach null node to a leaf\n"
+ "/AppleInternal/Library/BuildRoots/4~CDyrugDNGwRmI6zUgbNuBBZAb5NjjTGQZWdutQA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/include/c++/v1/__tree:336: assertion __root != nullptr failed: Root node should not be null\n"
+ "/AppleInternal/Library/BuildRoots/4~CDyrugDNGwRmI6zUgbNuBBZAb5NjjTGQZWdutQA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/include/c++/v1/__tree:337: assertion __z != nullptr failed: The node to remove should not be null\n"
+ "/AppleInternal/Library/BuildRoots/4~CDyrugDNGwRmI6zUgbNuBBZAb5NjjTGQZWdutQA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/include/c++/v1/__tree:338: assertion std::__tree_invariant(__root) failed: The tree invariants should hold\n"
+ "/AppleInternal/Library/BuildRoots/4~CDyrugDNGwRmI6zUgbNuBBZAb5NjjTGQZWdutQA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/include/c++/v1/deque:1546: assertion !empty() failed: deque::front called on an empty deque\n"
+ "/AppleInternal/Library/BuildRoots/4~CDyrugDNGwRmI6zUgbNuBBZAb5NjjTGQZWdutQA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/include/c++/v1/deque:2289: assertion !empty() failed: deque::pop_front called on an empty deque\n"
+ "/AppleInternal/Library/BuildRoots/4~CDyrugDNGwRmI6zUgbNuBBZAb5NjjTGQZWdutQA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/include/c++/v1/streambuf:271: assertion std::__is_valid_range(__gbeg, __gnext) failed: [gbeg, gnext) must be a valid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CDyrugDNGwRmI6zUgbNuBBZAb5NjjTGQZWdutQA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/include/c++/v1/streambuf:272: assertion std::__is_valid_range(__gbeg, __gend) failed: [gbeg, gend) must be a valid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CDyrugDNGwRmI6zUgbNuBBZAb5NjjTGQZWdutQA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/include/c++/v1/streambuf:273: assertion std::__is_valid_range(__gnext, __gend) failed: [gnext, gend) must be a valid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CDyrugDNGwRmI6zUgbNuBBZAb5NjjTGQZWdutQA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/include/c++/v1/streambuf:289: assertion std::__is_valid_range(__pbeg, __pend) failed: [pbeg, pend) must be a valid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CDyrugDNGwRmI6zUgbNuBBZAb5NjjTGQZWdutQA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/include/c++/v1/string:1093: assertion __s != nullptr failed: basic_string(const char*) detected nullptr\n"
+ "/AppleInternal/Library/BuildRoots/4~CDyrugDNGwRmI6zUgbNuBBZAb5NjjTGQZWdutQA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/include/c++/v1/string:1977: assertion __s < __min_cap failed: __s should never be greater than or equal to the short string capacity\n"
+ "/AppleInternal/Library/BuildRoots/4~CDyrugDNGwRmI6zUgbNuBBZAb5NjjTGQZWdutQA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/include/c++/v1/string:1984: assertion !__rep_.__s.__is_long_ failed: String has to be short when trying to get the short size\n"
+ "/AppleInternal/Library/BuildRoots/4~CDyrugDNGwRmI6zUgbNuBBZAb5NjjTGQZWdutQA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/include/c++/v1/string:1993: assertion __rep_.__l.__is_long_ failed: String has to be long when trying to get the long size\n"
+ "/AppleInternal/Library/BuildRoots/4~CDyrugDNGwRmI6zUgbNuBBZAb5NjjTGQZWdutQA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/include/c++/v1/string:2011: assertion __rep_.__l.__is_long_ failed: String has to be long when trying to get the long capacity\n"
+ "/AppleInternal/Library/BuildRoots/4~CDyrugDNGwRmI6zUgbNuBBZAb5NjjTGQZWdutQA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/include/c++/v1/string:2020: assertion __rep_.__l.__is_long_ failed: String has to be long when trying to get the long pointer\n"
+ "/AppleInternal/Library/BuildRoots/4~CDyrugDNGwRmI6zUgbNuBBZAb5NjjTGQZWdutQA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/include/c++/v1/string:2025: assertion __rep_.__l.__is_long_ failed: String has to be long when trying to get the long pointer\n"
+ "/System/Library/PrivateFrameworks/CoreThreadRadio.framework/com.apple.ccmapping_ios_vendor2_ver_101"
+ "EDT transport=%d"
+ "Error: failed to sync store record (%s)\n"
+ "bluetooth"
+ "deleteCurrentNetworkFromRetrieveOrGenerate:"
+ "performSyncOperationWithRecord:queue:timeoutValInSec:completion:"
+ "storeActiveDataSetRecordAndSyncWithErrComletion:completion:"
+ "transport-encoding"
+ "v44@0:8@16@24S32@?36"
- " Morty_Version: V0.333.0.3"
- "/AppleInternal/Library/BuildRoots/4~CB3mugDhUlw3NQWvY_m1h1-RDGvYb-XfURR8eIg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/__memory/construct_at.h:65: assertion __loc != nullptr failed: null pointer given to destroy_at\n"
- "/AppleInternal/Library/BuildRoots/4~CB3mugDhUlw3NQWvY_m1h1-RDGvYb-XfURR8eIg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/__tree:166: assertion __x != nullptr failed: Root node shouldn't be null\n"
- "/AppleInternal/Library/BuildRoots/4~CB3mugDhUlw3NQWvY_m1h1-RDGvYb-XfURR8eIg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/__tree:184: assertion __x != nullptr failed: node shouldn't be null\n"
- "/AppleInternal/Library/BuildRoots/4~CB3mugDhUlw3NQWvY_m1h1-RDGvYb-XfURR8eIg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/__tree:194: assertion __x != nullptr failed: node shouldn't be null\n"
- "/AppleInternal/Library/BuildRoots/4~CB3mugDhUlw3NQWvY_m1h1-RDGvYb-XfURR8eIg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/__tree:237: assertion __x != nullptr failed: node shouldn't be null\n"
- "/AppleInternal/Library/BuildRoots/4~CB3mugDhUlw3NQWvY_m1h1-RDGvYb-XfURR8eIg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/__tree:238: assertion __x->__right_ != nullptr failed: node should have a right child\n"
- "/AppleInternal/Library/BuildRoots/4~CB3mugDhUlw3NQWvY_m1h1-RDGvYb-XfURR8eIg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/__tree:256: assertion __x != nullptr failed: node shouldn't be null\n"
- "/AppleInternal/Library/BuildRoots/4~CB3mugDhUlw3NQWvY_m1h1-RDGvYb-XfURR8eIg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/__tree:257: assertion __x->__left_ != nullptr failed: node should have a left child\n"
- "/AppleInternal/Library/BuildRoots/4~CB3mugDhUlw3NQWvY_m1h1-RDGvYb-XfURR8eIg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/__tree:280: assertion __root != nullptr failed: Root of the tree shouldn't be null\n"
- "/AppleInternal/Library/BuildRoots/4~CB3mugDhUlw3NQWvY_m1h1-RDGvYb-XfURR8eIg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/__tree:281: assertion __x != nullptr failed: Can't attach null node to a leaf\n"
- "/AppleInternal/Library/BuildRoots/4~CB3mugDhUlw3NQWvY_m1h1-RDGvYb-XfURR8eIg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/__tree:336: assertion __root != nullptr failed: Root node should not be null\n"
- "/AppleInternal/Library/BuildRoots/4~CB3mugDhUlw3NQWvY_m1h1-RDGvYb-XfURR8eIg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/__tree:337: assertion __z != nullptr failed: The node to remove should not be null\n"
- "/AppleInternal/Library/BuildRoots/4~CB3mugDhUlw3NQWvY_m1h1-RDGvYb-XfURR8eIg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/__tree:338: assertion std::__tree_invariant(__root) failed: The tree invariants should hold\n"
- "/AppleInternal/Library/BuildRoots/4~CB3mugDhUlw3NQWvY_m1h1-RDGvYb-XfURR8eIg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/deque:1546: assertion !empty() failed: deque::front called on an empty deque\n"
- "/AppleInternal/Library/BuildRoots/4~CB3mugDhUlw3NQWvY_m1h1-RDGvYb-XfURR8eIg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/deque:2289: assertion !empty() failed: deque::pop_front called on an empty deque\n"
- "/AppleInternal/Library/BuildRoots/4~CB3mugDhUlw3NQWvY_m1h1-RDGvYb-XfURR8eIg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/streambuf:271: assertion std::__is_valid_range(__gbeg, __gnext) failed: [gbeg, gnext) must be a valid range\n"
- "/AppleInternal/Library/BuildRoots/4~CB3mugDhUlw3NQWvY_m1h1-RDGvYb-XfURR8eIg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/streambuf:272: assertion std::__is_valid_range(__gbeg, __gend) failed: [gbeg, gend) must be a valid range\n"
- "/AppleInternal/Library/BuildRoots/4~CB3mugDhUlw3NQWvY_m1h1-RDGvYb-XfURR8eIg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/streambuf:273: assertion std::__is_valid_range(__gnext, __gend) failed: [gnext, gend) must be a valid range\n"
- "/AppleInternal/Library/BuildRoots/4~CB3mugDhUlw3NQWvY_m1h1-RDGvYb-XfURR8eIg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/streambuf:289: assertion std::__is_valid_range(__pbeg, __pend) failed: [pbeg, pend) must be a valid range\n"
- "/AppleInternal/Library/BuildRoots/4~CB3mugDhUlw3NQWvY_m1h1-RDGvYb-XfURR8eIg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/string:1093: assertion __s != nullptr failed: basic_string(const char*) detected nullptr\n"
- "/AppleInternal/Library/BuildRoots/4~CB3mugDhUlw3NQWvY_m1h1-RDGvYb-XfURR8eIg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/string:1977: assertion __s < __min_cap failed: __s should never be greater than or equal to the short string capacity\n"
- "/AppleInternal/Library/BuildRoots/4~CB3mugDhUlw3NQWvY_m1h1-RDGvYb-XfURR8eIg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/string:1984: assertion !__rep_.__s.__is_long_ failed: String has to be short when trying to get the short size\n"
- "/AppleInternal/Library/BuildRoots/4~CB3mugDhUlw3NQWvY_m1h1-RDGvYb-XfURR8eIg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/string:1993: assertion __rep_.__l.__is_long_ failed: String has to be long when trying to get the long size\n"
- "/AppleInternal/Library/BuildRoots/4~CB3mugDhUlw3NQWvY_m1h1-RDGvYb-XfURR8eIg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/string:2011: assertion __rep_.__l.__is_long_ failed: String has to be long when trying to get the long capacity\n"
- "/AppleInternal/Library/BuildRoots/4~CB3mugDhUlw3NQWvY_m1h1-RDGvYb-XfURR8eIg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/string:2020: assertion __rep_.__l.__is_long_ failed: String has to be long when trying to get the long pointer\n"
- "/AppleInternal/Library/BuildRoots/4~CB3mugDhUlw3NQWvY_m1h1-RDGvYb-XfURR8eIg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/include/c++/v1/string:2025: assertion __rep_.__l.__is_long_ failed: String has to be long when trying to get the long pointer\n"
- "Error while adding preferred network entry"

```
