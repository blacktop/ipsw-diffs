## threadradiod

> `/System/Library/PrivateFrameworks/CoreThreadRadio.framework/threadradiod`

```diff

-333.0.1.0.0
-  __TEXT.__text: 0x3ece64
+333.0.2.0.0
+  __TEXT.__text: 0x3ed230
   __TEXT.__auth_stubs: 0x11280
-  __TEXT.__objc_stubs: 0x98e0
+  __TEXT.__objc_stubs: 0x9920
   __TEXT.__init_offsets: 0xa4
-  __TEXT.__objc_methlist: 0x6598
+  __TEXT.__objc_methlist: 0x65b0
   __TEXT.__objc_classname: 0x5f4
-  __TEXT.__cstring: 0x33203
+  __TEXT.__cstring: 0x3323e
   __TEXT.__const: 0x93e8
-  __TEXT.__gcc_except_tab: 0x2b798
-  __TEXT.__objc_methname: 0xebaf
-  __TEXT.__oslogstring: 0x22bcd
+  __TEXT.__gcc_except_tab: 0x2b7b8
+  __TEXT.__objc_methname: 0xebe5
+  __TEXT.__oslogstring: 0x22caf
   __TEXT.__objc_methtype: 0x3c29
-  __TEXT.__unwind_info: 0x7af8
+  __TEXT.__unwind_info: 0x7af0
   __TEXT.__eh_frame: 0x60
   __DATA_CONST.__auth_got: 0x8958
   __DATA_CONST.__got: 0x930
   __DATA_CONST.__auth_ptr: 0x60
   __DATA_CONST.__const: 0xd5a0
-  __DATA_CONST.__cfstring: 0x6000
+  __DATA_CONST.__cfstring: 0x6040
   __DATA_CONST.__objc_classlist: 0x170
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x140
   __DATA.__objc_const: 0x8518
-  __DATA.__objc_selrefs: 0x3658
+  __DATA.__objc_selrefs: 0x3668
   __DATA.__objc_ivar: 0x538
   __DATA.__objc_data: 0xe60
   __DATA.__data: 0x648
-  __DATA.__common: 0x3e4d0
+  __DATA.__common: 0x3e4d8
   __DATA.__bss: 0x171d4
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libdns_services.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1E225D29-E311-3485-9DB0-F8F808E17B57
-  Functions: 17131
-  Symbols:   89239
-  CStrings:  13467
+  UUID: C204D7A3-3249-3216-B030-4A2768BA63AA
+  Functions: 17133
+  Symbols:   89243
+  CStrings:  13479
 
Symbols:
+ -[ThreadNetworkManagerInstance(RCP2CAMetrics_extension) updateBusyFailureCount]
+ -[ThreadNetworkManagerInstance(RCP2CAMetrics_extension) updateWEDConnectionReqDupCount]
+ _objc_msgSend$updateBusyFailureCount
+ _objc_msgSend$updateWEDConnectionReqDupCount
CStrings:
+ " Morty_Version: V0.333.0.2"
+ "%s: #mOS:Error, Wed semaphore wait timed out "
+ "%sbusyFailures exceeds uint32 range."
+ "%sdupConnReq exceeds uint32 range."
+ "%sfailureConnReq exceeds uint32 range."
+ "%slinkFailures exceeds uint32 range."
+ "%ssuccessfulConnReq exceeds uint32 range."
+ "%stotalConnReq exceeds uint32 range."
+ "/AppleInternal/Library/BuildRoots/4~B-raugDt-KWaL2iLnv7J0FUNL1L_9Wk2rvyiUH8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/__memory/construct_at.h:65: assertion __loc != nullptr failed: null pointer given to destroy_at\n"
+ "/AppleInternal/Library/BuildRoots/4~B-raugDt-KWaL2iLnv7J0FUNL1L_9Wk2rvyiUH8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/__tree:166: assertion __x != nullptr failed: Root node shouldn't be null\n"
+ "/AppleInternal/Library/BuildRoots/4~B-raugDt-KWaL2iLnv7J0FUNL1L_9Wk2rvyiUH8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/__tree:184: assertion __x != nullptr failed: node shouldn't be null\n"
+ "/AppleInternal/Library/BuildRoots/4~B-raugDt-KWaL2iLnv7J0FUNL1L_9Wk2rvyiUH8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/__tree:194: assertion __x != nullptr failed: node shouldn't be null\n"
+ "/AppleInternal/Library/BuildRoots/4~B-raugDt-KWaL2iLnv7J0FUNL1L_9Wk2rvyiUH8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/__tree:237: assertion __x != nullptr failed: node shouldn't be null\n"
+ "/AppleInternal/Library/BuildRoots/4~B-raugDt-KWaL2iLnv7J0FUNL1L_9Wk2rvyiUH8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/__tree:238: assertion __x->__right_ != nullptr failed: node should have a right child\n"
+ "/AppleInternal/Library/BuildRoots/4~B-raugDt-KWaL2iLnv7J0FUNL1L_9Wk2rvyiUH8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/__tree:256: assertion __x != nullptr failed: node shouldn't be null\n"
+ "/AppleInternal/Library/BuildRoots/4~B-raugDt-KWaL2iLnv7J0FUNL1L_9Wk2rvyiUH8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/__tree:257: assertion __x->__left_ != nullptr failed: node should have a left child\n"
+ "/AppleInternal/Library/BuildRoots/4~B-raugDt-KWaL2iLnv7J0FUNL1L_9Wk2rvyiUH8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/__tree:280: assertion __root != nullptr failed: Root of the tree shouldn't be null\n"
+ "/AppleInternal/Library/BuildRoots/4~B-raugDt-KWaL2iLnv7J0FUNL1L_9Wk2rvyiUH8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/__tree:281: assertion __x != nullptr failed: Can't attach null node to a leaf\n"
+ "/AppleInternal/Library/BuildRoots/4~B-raugDt-KWaL2iLnv7J0FUNL1L_9Wk2rvyiUH8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/__tree:336: assertion __root != nullptr failed: Root node should not be null\n"
+ "/AppleInternal/Library/BuildRoots/4~B-raugDt-KWaL2iLnv7J0FUNL1L_9Wk2rvyiUH8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/__tree:337: assertion __z != nullptr failed: The node to remove should not be null\n"
+ "/AppleInternal/Library/BuildRoots/4~B-raugDt-KWaL2iLnv7J0FUNL1L_9Wk2rvyiUH8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/__tree:338: assertion std::__tree_invariant(__root) failed: The tree invariants should hold\n"
+ "/AppleInternal/Library/BuildRoots/4~B-raugDt-KWaL2iLnv7J0FUNL1L_9Wk2rvyiUH8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/deque:1546: assertion !empty() failed: deque::front called on an empty deque\n"
+ "/AppleInternal/Library/BuildRoots/4~B-raugDt-KWaL2iLnv7J0FUNL1L_9Wk2rvyiUH8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/deque:2289: assertion !empty() failed: deque::pop_front called on an empty deque\n"
+ "/AppleInternal/Library/BuildRoots/4~B-raugDt-KWaL2iLnv7J0FUNL1L_9Wk2rvyiUH8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/streambuf:271: assertion std::__is_valid_range(__gbeg, __gnext) failed: [gbeg, gnext) must be a valid range\n"
+ "/AppleInternal/Library/BuildRoots/4~B-raugDt-KWaL2iLnv7J0FUNL1L_9Wk2rvyiUH8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/streambuf:272: assertion std::__is_valid_range(__gbeg, __gend) failed: [gbeg, gend) must be a valid range\n"
+ "/AppleInternal/Library/BuildRoots/4~B-raugDt-KWaL2iLnv7J0FUNL1L_9Wk2rvyiUH8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/streambuf:273: assertion std::__is_valid_range(__gnext, __gend) failed: [gnext, gend) must be a valid range\n"
+ "/AppleInternal/Library/BuildRoots/4~B-raugDt-KWaL2iLnv7J0FUNL1L_9Wk2rvyiUH8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/streambuf:289: assertion std::__is_valid_range(__pbeg, __pend) failed: [pbeg, pend) must be a valid range\n"
+ "/AppleInternal/Library/BuildRoots/4~B-raugDt-KWaL2iLnv7J0FUNL1L_9Wk2rvyiUH8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/string:1083: assertion __s != nullptr failed: basic_string(const char*) detected nullptr\n"
+ "/AppleInternal/Library/BuildRoots/4~B-raugDt-KWaL2iLnv7J0FUNL1L_9Wk2rvyiUH8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/string:1967: assertion __s < __min_cap failed: __s should never be greater than or equal to the short string capacity\n"
+ "/AppleInternal/Library/BuildRoots/4~B-raugDt-KWaL2iLnv7J0FUNL1L_9Wk2rvyiUH8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/string:1974: assertion !__rep_.__s.__is_long_ failed: String has to be short when trying to get the short size\n"
+ "/AppleInternal/Library/BuildRoots/4~B-raugDt-KWaL2iLnv7J0FUNL1L_9Wk2rvyiUH8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/string:1983: assertion __rep_.__l.__is_long_ failed: String has to be long when trying to get the long size\n"
+ "/AppleInternal/Library/BuildRoots/4~B-raugDt-KWaL2iLnv7J0FUNL1L_9Wk2rvyiUH8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/string:2001: assertion __rep_.__l.__is_long_ failed: String has to be long when trying to get the long capacity\n"
+ "/AppleInternal/Library/BuildRoots/4~B-raugDt-KWaL2iLnv7J0FUNL1L_9Wk2rvyiUH8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/string:2010: assertion __rep_.__l.__is_long_ failed: String has to be long when trying to get the long pointer\n"
+ "/AppleInternal/Library/BuildRoots/4~B-raugDt-KWaL2iLnv7J0FUNL1L_9Wk2rvyiUH8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/string:2015: assertion __rep_.__l.__is_long_ failed: String has to be long when trying to get the long pointer\n"
+ "updateBusyFailureCount"
+ "updateWEDConnectionReqDupCount"
+ "wed_conn_req_kbusy_fail_count"
+ "wed_duplicate_conn_req_count"
- " Morty_Version: V0.333.0.1"
- "%s: #mOS: Error, Wed semaphore wait timed out "
- "/AppleInternal/Library/BuildRoots/4~B9_rugDXSyMuoMjNa99w5P-1ESHkL6N0QVSUE1I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/__memory/construct_at.h:65: assertion __loc != nullptr failed: null pointer given to destroy_at\n"
- "/AppleInternal/Library/BuildRoots/4~B9_rugDXSyMuoMjNa99w5P-1ESHkL6N0QVSUE1I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/__tree:166: assertion __x != nullptr failed: Root node shouldn't be null\n"
- "/AppleInternal/Library/BuildRoots/4~B9_rugDXSyMuoMjNa99w5P-1ESHkL6N0QVSUE1I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/__tree:184: assertion __x != nullptr failed: node shouldn't be null\n"
- "/AppleInternal/Library/BuildRoots/4~B9_rugDXSyMuoMjNa99w5P-1ESHkL6N0QVSUE1I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/__tree:194: assertion __x != nullptr failed: node shouldn't be null\n"
- "/AppleInternal/Library/BuildRoots/4~B9_rugDXSyMuoMjNa99w5P-1ESHkL6N0QVSUE1I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/__tree:237: assertion __x != nullptr failed: node shouldn't be null\n"
- "/AppleInternal/Library/BuildRoots/4~B9_rugDXSyMuoMjNa99w5P-1ESHkL6N0QVSUE1I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/__tree:238: assertion __x->__right_ != nullptr failed: node should have a right child\n"
- "/AppleInternal/Library/BuildRoots/4~B9_rugDXSyMuoMjNa99w5P-1ESHkL6N0QVSUE1I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/__tree:256: assertion __x != nullptr failed: node shouldn't be null\n"
- "/AppleInternal/Library/BuildRoots/4~B9_rugDXSyMuoMjNa99w5P-1ESHkL6N0QVSUE1I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/__tree:257: assertion __x->__left_ != nullptr failed: node should have a left child\n"
- "/AppleInternal/Library/BuildRoots/4~B9_rugDXSyMuoMjNa99w5P-1ESHkL6N0QVSUE1I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/__tree:280: assertion __root != nullptr failed: Root of the tree shouldn't be null\n"
- "/AppleInternal/Library/BuildRoots/4~B9_rugDXSyMuoMjNa99w5P-1ESHkL6N0QVSUE1I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/__tree:281: assertion __x != nullptr failed: Can't attach null node to a leaf\n"
- "/AppleInternal/Library/BuildRoots/4~B9_rugDXSyMuoMjNa99w5P-1ESHkL6N0QVSUE1I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/__tree:336: assertion __root != nullptr failed: Root node should not be null\n"
- "/AppleInternal/Library/BuildRoots/4~B9_rugDXSyMuoMjNa99w5P-1ESHkL6N0QVSUE1I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/__tree:337: assertion __z != nullptr failed: The node to remove should not be null\n"
- "/AppleInternal/Library/BuildRoots/4~B9_rugDXSyMuoMjNa99w5P-1ESHkL6N0QVSUE1I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/__tree:338: assertion std::__tree_invariant(__root) failed: The tree invariants should hold\n"
- "/AppleInternal/Library/BuildRoots/4~B9_rugDXSyMuoMjNa99w5P-1ESHkL6N0QVSUE1I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/deque:1546: assertion !empty() failed: deque::front called on an empty deque\n"
- "/AppleInternal/Library/BuildRoots/4~B9_rugDXSyMuoMjNa99w5P-1ESHkL6N0QVSUE1I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/deque:2289: assertion !empty() failed: deque::pop_front called on an empty deque\n"
- "/AppleInternal/Library/BuildRoots/4~B9_rugDXSyMuoMjNa99w5P-1ESHkL6N0QVSUE1I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/streambuf:271: assertion std::__is_valid_range(__gbeg, __gnext) failed: [gbeg, gnext) must be a valid range\n"
- "/AppleInternal/Library/BuildRoots/4~B9_rugDXSyMuoMjNa99w5P-1ESHkL6N0QVSUE1I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/streambuf:272: assertion std::__is_valid_range(__gbeg, __gend) failed: [gbeg, gend) must be a valid range\n"
- "/AppleInternal/Library/BuildRoots/4~B9_rugDXSyMuoMjNa99w5P-1ESHkL6N0QVSUE1I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/streambuf:273: assertion std::__is_valid_range(__gnext, __gend) failed: [gnext, gend) must be a valid range\n"
- "/AppleInternal/Library/BuildRoots/4~B9_rugDXSyMuoMjNa99w5P-1ESHkL6N0QVSUE1I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/streambuf:289: assertion std::__is_valid_range(__pbeg, __pend) failed: [pbeg, pend) must be a valid range\n"
- "/AppleInternal/Library/BuildRoots/4~B9_rugDXSyMuoMjNa99w5P-1ESHkL6N0QVSUE1I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/string:1083: assertion __s != nullptr failed: basic_string(const char*) detected nullptr\n"
- "/AppleInternal/Library/BuildRoots/4~B9_rugDXSyMuoMjNa99w5P-1ESHkL6N0QVSUE1I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/string:1967: assertion __s < __min_cap failed: __s should never be greater than or equal to the short string capacity\n"
- "/AppleInternal/Library/BuildRoots/4~B9_rugDXSyMuoMjNa99w5P-1ESHkL6N0QVSUE1I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/string:1974: assertion !__rep_.__s.__is_long_ failed: String has to be short when trying to get the short size\n"
- "/AppleInternal/Library/BuildRoots/4~B9_rugDXSyMuoMjNa99w5P-1ESHkL6N0QVSUE1I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/string:1983: assertion __rep_.__l.__is_long_ failed: String has to be long when trying to get the long size\n"
- "/AppleInternal/Library/BuildRoots/4~B9_rugDXSyMuoMjNa99w5P-1ESHkL6N0QVSUE1I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/string:2001: assertion __rep_.__l.__is_long_ failed: String has to be long when trying to get the long capacity\n"
- "/AppleInternal/Library/BuildRoots/4~B9_rugDXSyMuoMjNa99w5P-1ESHkL6N0QVSUE1I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/string:2010: assertion __rep_.__l.__is_long_ failed: String has to be long when trying to get the long pointer\n"
- "/AppleInternal/Library/BuildRoots/4~B9_rugDXSyMuoMjNa99w5P-1ESHkL6N0QVSUE1I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/include/c++/v1/string:2015: assertion __rep_.__l.__is_long_ failed: String has to be long when trying to get the long pointer\n"

```
