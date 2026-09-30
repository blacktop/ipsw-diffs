## threadradiod

> `/System/Library/PrivateFrameworks/CoreThreadRadio.framework/threadradiod`

```diff

-328.0.0.0.0
-  __TEXT.__text: 0x3e5e20
+330.0.0.0.0
+  __TEXT.__text: 0x3e6b5c
   __TEXT.__auth_stubs: 0x111f0
   __TEXT.__objc_stubs: 0x98e0
   __TEXT.__init_offsets: 0xa4
   __TEXT.__objc_methlist: 0x6598
   __TEXT.__objc_classname: 0x5f4
-  __TEXT.__cstring: 0x32b8f
+  __TEXT.__cstring: 0x32c77
   __TEXT.__const: 0x9318
-  __TEXT.__gcc_except_tab: 0x2b600
+  __TEXT.__gcc_except_tab: 0x2b5e4
   __TEXT.__objc_methname: 0xebaf
   __TEXT.__oslogstring: 0x22492
-  __TEXT.__objc_methtype: 0x3c97
+  __TEXT.__objc_methtype: 0x3c29
   __TEXT.__unwind_info: 0x7ad8
   __TEXT.__eh_frame: 0x60
   __DATA_CONST.__auth_got: 0x8910

   __DATA.__objc_ivar: 0x538
   __DATA.__objc_data: 0xe60
   __DATA.__data: 0x628
-  __DATA.__common: 0x3e2a8
+  __DATA.__common: 0x3e430
   __DATA.__bss: 0x171cc
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libdns_services.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 5A150194-D8B3-3BAC-8ADE-42229C34F899
-  Functions: 17089
-  Symbols:   88980
-  CStrings:  13372
+  UUID: F681953D-D4E1-3A55-B603-F7C17592D372
+  Functions: 17102
+  Symbols:   89041
+  CStrings:  13376
 
Symbols:
+ __ZN2ot17AppMetricsManager26SetSrpPortIfSrpSerivceDataEPKhhS2_h
+ __ZN2ot17AppMetricsManager34GetThreadReachabilityStatusBitmapsERKyRKbRyS5_S5_
+ __ZN2ot17AppMetricsManager51UpdateAppMapWithPerPacketThreadTXReachabilityStatusE7otErrorRKNS_3Ip67HeadersE
+ __ZN2ot17AppMetricsManager55UpdateSystemWideThreadRXReachabilityStatusLastTimestampE7otErrorPNS_3Ip67HeadersE
+ __ZN2ot17AppMetricsManager55UpdateSystemWideThreadTXReachabilityStatusLastTimestampE20threadTXStatusEnum_t
+ __ZN2ot17AppMetricsManager57UpdateSystemWideThreadMeshReachabilityStatusLastTimestampE22threadMeshStatusEnum_t
+ __ZN2ot17AppMetricsManager5IsMleERKNS_3Ip67HeadersE
+ __ZN2ot17AppMetricsManager5IsSrpERKNS_3Ip67HeadersE
+ __ZN2ot17AppMetricsManager5IsTmfERKNS_3Ip67HeadersE
+ ___copy_helper_block_e8_40c27_ZTS21Ctr_trm_get_ot_data_t72c58_ZTSN8dispatch8callbackIU13block_pointerFvhN5boost3anyEEEE
+ ___destroy_helper_block_e8_40c27_ZTS21Ctr_trm_get_ot_data_t72c58_ZTSN8dispatch8callbackIU13block_pointerFvhN5boost3anyEEEE
+ _otAppGetThreadReachabilityStatusBitmaps
- __ZN21Ctr_trm_get_ot_data_tD2Ev
- ___copy_helper_block_e8_40c27_ZTS21Ctr_trm_get_ot_data_t96c58_ZTSN8dispatch8callbackIU13block_pointerFvhN5boost3anyEEEE
- ___destroy_helper_block_e8_40c27_ZTS21Ctr_trm_get_ot_data_t96c58_ZTSN8dispatch8callbackIU13block_pointerFvhN5boost3anyEEEE
CStrings:
+ " Morty_Version: V0.330"
+ ", Hap T:%u, C:%.2f, M:%u, TK:0x%llx"
+ "/AppleInternal/Library/BuildRoots/4~B5BiugAMug-RhN9sSfcKBuuHcengqm3yuNv57Vg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__memory/construct_at.h:65: assertion __loc != nullptr failed: null pointer given to destroy_at\n"
+ "/AppleInternal/Library/BuildRoots/4~B5BiugAMug-RhN9sSfcKBuuHcengqm3yuNv57Vg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__tree:166: assertion __x != nullptr failed: Root node shouldn't be null\n"
+ "/AppleInternal/Library/BuildRoots/4~B5BiugAMug-RhN9sSfcKBuuHcengqm3yuNv57Vg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__tree:184: assertion __x != nullptr failed: node shouldn't be null\n"
+ "/AppleInternal/Library/BuildRoots/4~B5BiugAMug-RhN9sSfcKBuuHcengqm3yuNv57Vg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__tree:194: assertion __x != nullptr failed: node shouldn't be null\n"
+ "/AppleInternal/Library/BuildRoots/4~B5BiugAMug-RhN9sSfcKBuuHcengqm3yuNv57Vg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__tree:237: assertion __x != nullptr failed: node shouldn't be null\n"
+ "/AppleInternal/Library/BuildRoots/4~B5BiugAMug-RhN9sSfcKBuuHcengqm3yuNv57Vg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__tree:238: assertion __x->__right_ != nullptr failed: node should have a right child\n"
+ "/AppleInternal/Library/BuildRoots/4~B5BiugAMug-RhN9sSfcKBuuHcengqm3yuNv57Vg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__tree:256: assertion __x != nullptr failed: node shouldn't be null\n"
+ "/AppleInternal/Library/BuildRoots/4~B5BiugAMug-RhN9sSfcKBuuHcengqm3yuNv57Vg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__tree:257: assertion __x->__left_ != nullptr failed: node should have a left child\n"
+ "/AppleInternal/Library/BuildRoots/4~B5BiugAMug-RhN9sSfcKBuuHcengqm3yuNv57Vg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__tree:280: assertion __root != nullptr failed: Root of the tree shouldn't be null\n"
+ "/AppleInternal/Library/BuildRoots/4~B5BiugAMug-RhN9sSfcKBuuHcengqm3yuNv57Vg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__tree:281: assertion __x != nullptr failed: Can't attach null node to a leaf\n"
+ "/AppleInternal/Library/BuildRoots/4~B5BiugAMug-RhN9sSfcKBuuHcengqm3yuNv57Vg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__tree:336: assertion __root != nullptr failed: Root node should not be null\n"
+ "/AppleInternal/Library/BuildRoots/4~B5BiugAMug-RhN9sSfcKBuuHcengqm3yuNv57Vg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__tree:337: assertion __z != nullptr failed: The node to remove should not be null\n"
+ "/AppleInternal/Library/BuildRoots/4~B5BiugAMug-RhN9sSfcKBuuHcengqm3yuNv57Vg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__tree:338: assertion std::__tree_invariant(__root) failed: The tree invariants should hold\n"
+ "/AppleInternal/Library/BuildRoots/4~B5BiugAMug-RhN9sSfcKBuuHcengqm3yuNv57Vg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/deque:1546: assertion !empty() failed: deque::front called on an empty deque\n"
+ "/AppleInternal/Library/BuildRoots/4~B5BiugAMug-RhN9sSfcKBuuHcengqm3yuNv57Vg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/deque:2289: assertion !empty() failed: deque::pop_front called on an empty deque\n"
+ "/AppleInternal/Library/BuildRoots/4~B5BiugAMug-RhN9sSfcKBuuHcengqm3yuNv57Vg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/streambuf:271: assertion std::__is_valid_range(__gbeg, __gnext) failed: [gbeg, gnext) must be a valid range\n"
+ "/AppleInternal/Library/BuildRoots/4~B5BiugAMug-RhN9sSfcKBuuHcengqm3yuNv57Vg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/streambuf:272: assertion std::__is_valid_range(__gbeg, __gend) failed: [gbeg, gend) must be a valid range\n"
+ "/AppleInternal/Library/BuildRoots/4~B5BiugAMug-RhN9sSfcKBuuHcengqm3yuNv57Vg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/streambuf:273: assertion std::__is_valid_range(__gnext, __gend) failed: [gnext, gend) must be a valid range\n"
+ "/AppleInternal/Library/BuildRoots/4~B5BiugAMug-RhN9sSfcKBuuHcengqm3yuNv57Vg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/streambuf:289: assertion std::__is_valid_range(__pbeg, __pend) failed: [pbeg, pend) must be a valid range\n"
+ "/AppleInternal/Library/BuildRoots/4~B5BiugAMug-RhN9sSfcKBuuHcengqm3yuNv57Vg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/string:1083: assertion __s != nullptr failed: basic_string(const char*) detected nullptr\n"
+ "/AppleInternal/Library/BuildRoots/4~B5BiugAMug-RhN9sSfcKBuuHcengqm3yuNv57Vg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/string:1967: assertion __s < __min_cap failed: __s should never be greater than or equal to the short string capacity\n"
+ "/AppleInternal/Library/BuildRoots/4~B5BiugAMug-RhN9sSfcKBuuHcengqm3yuNv57Vg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/string:1974: assertion !__rep_.__s.__is_long_ failed: String has to be short when trying to get the short size\n"
+ "/AppleInternal/Library/BuildRoots/4~B5BiugAMug-RhN9sSfcKBuuHcengqm3yuNv57Vg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/string:1983: assertion __rep_.__l.__is_long_ failed: String has to be long when trying to get the long size\n"
+ "/AppleInternal/Library/BuildRoots/4~B5BiugAMug-RhN9sSfcKBuuHcengqm3yuNv57Vg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/string:2001: assertion __rep_.__l.__is_long_ failed: String has to be long when trying to get the long capacity\n"
+ "/AppleInternal/Library/BuildRoots/4~B5BiugAMug-RhN9sSfcKBuuHcengqm3yuNv57Vg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/string:2010: assertion __rep_.__l.__is_long_ failed: String has to be long when trying to get the long pointer\n"
+ "/AppleInternal/Library/BuildRoots/4~B5BiugAMug-RhN9sSfcKBuuHcengqm3yuNv57Vg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/string:2015: assertion __rep_.__l.__is_long_ failed: String has to be long when trying to get the long pointer\n"
+ "Error: HAP response received but there is no HAP request entry in the TX map"
+ "Error: There is no entry in the TX map to update Thread TX reachability status"
+ "Extracted port from aServerData: %u"
+ "Server data too short to extract port"
+ "{Result=i{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}56@0:8{?={basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}Q}16^{any=^{placeholder}}48"
- " Morty_Version: V0.328"
- ", Hap T:%u, C:%.2f, M:%u, TK:0x%x"
- "/AppleInternal/Library/BuildRoots/4~B4EZugA0NxV6aOGd3qWaxY2cZ79lbcqoLBI9Z-k/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__memory/construct_at.h:65: assertion __loc != nullptr failed: null pointer given to destroy_at\n"
- "/AppleInternal/Library/BuildRoots/4~B4EZugA0NxV6aOGd3qWaxY2cZ79lbcqoLBI9Z-k/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__tree:166: assertion __x != nullptr failed: Root node shouldn't be null\n"
- "/AppleInternal/Library/BuildRoots/4~B4EZugA0NxV6aOGd3qWaxY2cZ79lbcqoLBI9Z-k/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__tree:184: assertion __x != nullptr failed: node shouldn't be null\n"
- "/AppleInternal/Library/BuildRoots/4~B4EZugA0NxV6aOGd3qWaxY2cZ79lbcqoLBI9Z-k/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__tree:194: assertion __x != nullptr failed: node shouldn't be null\n"
- "/AppleInternal/Library/BuildRoots/4~B4EZugA0NxV6aOGd3qWaxY2cZ79lbcqoLBI9Z-k/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__tree:237: assertion __x != nullptr failed: node shouldn't be null\n"
- "/AppleInternal/Library/BuildRoots/4~B4EZugA0NxV6aOGd3qWaxY2cZ79lbcqoLBI9Z-k/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__tree:238: assertion __x->__right_ != nullptr failed: node should have a right child\n"
- "/AppleInternal/Library/BuildRoots/4~B4EZugA0NxV6aOGd3qWaxY2cZ79lbcqoLBI9Z-k/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__tree:256: assertion __x != nullptr failed: node shouldn't be null\n"
- "/AppleInternal/Library/BuildRoots/4~B4EZugA0NxV6aOGd3qWaxY2cZ79lbcqoLBI9Z-k/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__tree:257: assertion __x->__left_ != nullptr failed: node should have a left child\n"
- "/AppleInternal/Library/BuildRoots/4~B4EZugA0NxV6aOGd3qWaxY2cZ79lbcqoLBI9Z-k/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__tree:280: assertion __root != nullptr failed: Root of the tree shouldn't be null\n"
- "/AppleInternal/Library/BuildRoots/4~B4EZugA0NxV6aOGd3qWaxY2cZ79lbcqoLBI9Z-k/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__tree:281: assertion __x != nullptr failed: Can't attach null node to a leaf\n"
- "/AppleInternal/Library/BuildRoots/4~B4EZugA0NxV6aOGd3qWaxY2cZ79lbcqoLBI9Z-k/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__tree:336: assertion __root != nullptr failed: Root node should not be null\n"
- "/AppleInternal/Library/BuildRoots/4~B4EZugA0NxV6aOGd3qWaxY2cZ79lbcqoLBI9Z-k/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__tree:337: assertion __z != nullptr failed: The node to remove should not be null\n"
- "/AppleInternal/Library/BuildRoots/4~B4EZugA0NxV6aOGd3qWaxY2cZ79lbcqoLBI9Z-k/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/__tree:338: assertion std::__tree_invariant(__root) failed: The tree invariants should hold\n"
- "/AppleInternal/Library/BuildRoots/4~B4EZugA0NxV6aOGd3qWaxY2cZ79lbcqoLBI9Z-k/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/deque:1546: assertion !empty() failed: deque::front called on an empty deque\n"
- "/AppleInternal/Library/BuildRoots/4~B4EZugA0NxV6aOGd3qWaxY2cZ79lbcqoLBI9Z-k/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/deque:2289: assertion !empty() failed: deque::pop_front called on an empty deque\n"
- "/AppleInternal/Library/BuildRoots/4~B4EZugA0NxV6aOGd3qWaxY2cZ79lbcqoLBI9Z-k/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/streambuf:271: assertion std::__is_valid_range(__gbeg, __gnext) failed: [gbeg, gnext) must be a valid range\n"
- "/AppleInternal/Library/BuildRoots/4~B4EZugA0NxV6aOGd3qWaxY2cZ79lbcqoLBI9Z-k/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/streambuf:272: assertion std::__is_valid_range(__gbeg, __gend) failed: [gbeg, gend) must be a valid range\n"
- "/AppleInternal/Library/BuildRoots/4~B4EZugA0NxV6aOGd3qWaxY2cZ79lbcqoLBI9Z-k/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/streambuf:273: assertion std::__is_valid_range(__gnext, __gend) failed: [gnext, gend) must be a valid range\n"
- "/AppleInternal/Library/BuildRoots/4~B4EZugA0NxV6aOGd3qWaxY2cZ79lbcqoLBI9Z-k/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/streambuf:289: assertion std::__is_valid_range(__pbeg, __pend) failed: [pbeg, pend) must be a valid range\n"
- "/AppleInternal/Library/BuildRoots/4~B4EZugA0NxV6aOGd3qWaxY2cZ79lbcqoLBI9Z-k/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/string:1083: assertion __s != nullptr failed: basic_string(const char*) detected nullptr\n"
- "/AppleInternal/Library/BuildRoots/4~B4EZugA0NxV6aOGd3qWaxY2cZ79lbcqoLBI9Z-k/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/string:1967: assertion __s < __min_cap failed: __s should never be greater than or equal to the short string capacity\n"
- "/AppleInternal/Library/BuildRoots/4~B4EZugA0NxV6aOGd3qWaxY2cZ79lbcqoLBI9Z-k/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/string:1974: assertion !__rep_.__s.__is_long_ failed: String has to be short when trying to get the short size\n"
- "/AppleInternal/Library/BuildRoots/4~B4EZugA0NxV6aOGd3qWaxY2cZ79lbcqoLBI9Z-k/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/string:1983: assertion __rep_.__l.__is_long_ failed: String has to be long when trying to get the long size\n"
- "/AppleInternal/Library/BuildRoots/4~B4EZugA0NxV6aOGd3qWaxY2cZ79lbcqoLBI9Z-k/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/string:2001: assertion __rep_.__l.__is_long_ failed: String has to be long when trying to get the long capacity\n"
- "/AppleInternal/Library/BuildRoots/4~B4EZugA0NxV6aOGd3qWaxY2cZ79lbcqoLBI9Z-k/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/string:2010: assertion __rep_.__l.__is_long_ failed: String has to be long when trying to get the long pointer\n"
- "/AppleInternal/Library/BuildRoots/4~B4EZugA0NxV6aOGd3qWaxY2cZ79lbcqoLBI9Z-k/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/include/c++/v1/string:2015: assertion __rep_.__l.__is_long_ failed: String has to be long when trying to get the long pointer\n"
- "{Result=i{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}80@0:8{?={basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}S{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}16^{any=^{placeholder}}72"

```
