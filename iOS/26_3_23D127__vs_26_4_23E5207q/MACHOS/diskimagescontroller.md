## diskimagescontroller

> `/System/Library/PrivateFrameworks/DiskImages2.framework/XPCServices/diskimagescontroller.xpc/diskimagescontroller`

```diff

-514.80.3.0.0
-  __TEXT.__text: 0x1a2358
+524.100.20.0.0
+  __TEXT.__text: 0x1b2290
   __TEXT.__auth_stubs: 0x1fc0
-  __TEXT.__objc_stubs: 0x5520
-  __TEXT.__objc_methlist: 0x30b4
-  __TEXT.__gcc_except_tab: 0x17c48
-  __TEXT.__const: 0x1178a
-  __TEXT.__cstring: 0x11cb8
-  __TEXT.__oslogstring: 0x1655
-  __TEXT.__objc_methname: 0x600a
-  __TEXT.__objc_classname: 0x5f0
-  __TEXT.__objc_methtype: 0x2079
+  __TEXT.__objc_stubs: 0x55e0
+  __TEXT.__objc_methlist: 0x3194
+  __TEXT.__gcc_except_tab: 0x181b4
+  __TEXT.__const: 0x12d2a
+  __TEXT.__cstring: 0x152b8
+  __TEXT.__oslogstring: 0x167d
+  __TEXT.__objc_methname: 0x61a8
+  __TEXT.__objc_classname: 0x669
+  __TEXT.__objc_methtype: 0x2105
   __TEXT.__ustring: 0x13c
   __TEXT.__constg_swiftt: 0x60
   __TEXT.__swift5_typeref: 0x58
   __TEXT.__swift5_fieldmd: 0x10
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0xbe98
-  __TEXT.__eh_frame: 0x150
+  __TEXT.__unwind_info: 0xc648
+  __TEXT.__eh_frame: 0xf0
   __DATA_CONST.__auth_got: 0xff8
-  __DATA_CONST.__got: 0x4c8
+  __DATA_CONST.__got: 0x4d0
   __DATA_CONST.__auth_ptr: 0x40
-  __DATA_CONST.__const: 0x31de8
-  __DATA_CONST.__cfstring: 0x3b80
-  __DATA_CONST.__objc_classlist: 0x228
-  __DATA_CONST.__objc_catlist: 0x8
+  __DATA_CONST.__const: 0x33250
+  __DATA_CONST.__cfstring: 0x3ba0
+  __DATA_CONST.__objc_classlist: 0x238
+  __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0x1c8
+  __DATA_CONST.__objc_superrefs: 0x1d8
   __DATA_CONST.__objc_arraydata: 0x78
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__objc_intobj: 0x18
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0x4cb8
-  __DATA.__objc_selrefs: 0x1958
-  __DATA.__objc_ivar: 0x25c
-  __DATA.__objc_data: 0x1610
+  __DATA.__objc_const: 0x4f48
+  __DATA.__objc_selrefs: 0x19a0
+  __DATA.__objc_ivar: 0x26c
+  __DATA.__objc_data: 0x16b0
   __DATA.__data: 0xc90
   __DATA.__bss: 0x150
   __DATA.__common: 0x19

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/local/lib/libcurl.4.dylib
-  UUID: 99866C99-6A59-3966-8A76-38948BB578FC
-  Functions: 9691
-  Symbols:   742
-  CStrings:  3848
+  UUID: A31FC570-31B9-3885-BA4C-0BA8EC181C07
+  Functions: 10110
+  Symbols:   743
+  CStrings:  3938
 
Symbols:
+ __ZNSt3__132__internal_log_hardening_failureEPKc
+ _objc_opt_new
+ _objc_retain_x24
+ _objc_retain_x25
+ _objc_retain_x27
+ _objc_retain_x28
- _objc_claimAutoreleasedReturnValue
- _objc_opt_respondsToSelector
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x3
- _objc_retain_x9
CStrings:
+ "  - clientID: %s\n"
+ "  obtaining an OIDC token from the appleconnect CLI\n"
+ "%.*s: Cleaned up folder copy connection"
+ "+[DIControllerServiceConnection sendHandleToClient:clientConnection:outError:]_block_invoke"
+ "+[DIControllerServiceConnection tryAttachWithParams:clientConnection:outError:]"
+ "-[DIControllerServiceConnection checkAttachEntitlementWithError:]"
+ "-[DIControllerServiceConnection cleanup]"
+ "-[DIControllerServiceConnection dupWithStderrHandle:reply:]"
+ "-[DIControllerServiceConnection init]"
+ "/AppleInternal/Library/BuildRoots/4~CIsMugDVAk3e7DmVz9fr_Ynz-tviWmRdejr9kmM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:293: libc++ Hardening assertion __k != __leftmost failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CIsMugDVAk3e7DmVz9fr_Ynz-tviWmRdejr9kmM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:603: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CIsMugDVAk3e7DmVz9fr_Ynz-tviWmRdejr9kmM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:615: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CIsMugDVAk3e7DmVz9fr_Ynz-tviWmRdejr9kmM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:633: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CIsMugDVAk3e7DmVz9fr_Ynz-tviWmRdejr9kmM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:638: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CIsMugDVAk3e7DmVz9fr_Ynz-tviWmRdejr9kmM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:669: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CIsMugDVAk3e7DmVz9fr_Ynz-tviWmRdejr9kmM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:682: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CIsMugDVAk3e7DmVz9fr_Ynz-tviWmRdejr9kmM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:692: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CIsMugDVAk3e7DmVz9fr_Ynz-tviWmRdejr9kmM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:697: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CIsMugDVAk3e7DmVz9fr_Ynz-tviWmRdejr9kmM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__expected/expected.h:799: libc++ Hardening assertion this->__has_val() failed: expected::operator-> requires the expected to contain a value\n"
+ "/AppleInternal/Library/BuildRoots/4~CIsMugDVAk3e7DmVz9fr_Ynz-tviWmRdejr9kmM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__expected/expected.h:811: libc++ Hardening assertion this->__has_val() failed: expected::operator* requires the expected to contain a value\n"
+ "/AppleInternal/Library/BuildRoots/4~CIsMugDVAk3e7DmVz9fr_Ynz-tviWmRdejr9kmM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__expected/expected.h:873: libc++ Hardening assertion !this->__has_val() failed: expected::error requires the expected to contain an error\n"
+ "/AppleInternal/Library/BuildRoots/4~CIsMugDVAk3e7DmVz9fr_Ynz-tviWmRdejr9kmM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__hash_table:1892: libc++ Hardening assertion __p != end() failed: unordered container::erase(iterator) called with a non-dereferenceable iterator\n"
+ "/AppleInternal/Library/BuildRoots/4~CIsMugDVAk3e7DmVz9fr_Ynz-tviWmRdejr9kmM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__memory/unique_ptr.h:582: libc++ Hardening assertion __checker_.__in_bounds<deleter_type>(std::__to_address(__ptr_), __i) failed: unique_ptr<T[]>::operator[](index): index out of range\n"
+ "/AppleInternal/Library/BuildRoots/4~CIsMugDVAk3e7DmVz9fr_Ynz-tviWmRdejr9kmM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CIsMugDVAk3e7DmVz9fr_Ynz-tviWmRdejr9kmM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CIsMugDVAk3e7DmVz9fr_Ynz-tviWmRdejr9kmM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:425: libc++ Hardening assertion !empty() failed: front() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CIsMugDVAk3e7DmVz9fr_Ynz-tviWmRdejr9kmM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:429: libc++ Hardening assertion !empty() failed: front() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CIsMugDVAk3e7DmVz9fr_Ynz-tviWmRdejr9kmM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:433: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CIsMugDVAk3e7DmVz9fr_Ynz-tviWmRdejr9kmM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:437: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CIsMugDVAk3e7DmVz9fr_Ynz-tviWmRdejr9kmM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:486: libc++ Hardening assertion !empty() failed: vector::pop_back called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CIsMugDVAk3e7DmVz9fr_Ynz-tviWmRdejr9kmM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/array:271: libc++ Hardening assertion __n < _Size failed: out-of-bounds access in std::array<T, N>\n"
+ "/AppleInternal/Library/BuildRoots/4~CIsMugDVAk3e7DmVz9fr_Ynz-tviWmRdejr9kmM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:1522: libc++ Hardening assertion __i < size() failed: deque::operator[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CIsMugDVAk3e7DmVz9fr_Ynz-tviWmRdejr9kmM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:1553: libc++ Hardening assertion !empty() failed: deque::front called on an empty deque\n"
+ "/AppleInternal/Library/BuildRoots/4~CIsMugDVAk3e7DmVz9fr_Ynz-tviWmRdejr9kmM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:2296: libc++ Hardening assertion !empty() failed: deque::pop_front called on an empty deque\n"
+ "/AppleInternal/Library/BuildRoots/4~CIsMugDVAk3e7DmVz9fr_Ynz-tviWmRdejr9kmM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/list:1420: libc++ Hardening assertion __p != end() failed: list::erase(iterator) called with a non-dereferenceable iterator\n"
+ "/AppleInternal/Library/BuildRoots/4~CIsMugDVAk3e7DmVz9fr_Ynz-tviWmRdejr9kmM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:796: libc++ Hardening assertion this->has_value() failed: optional operator-> called on a disengaged value\n"
+ "/AppleInternal/Library/BuildRoots/4~CIsMugDVAk3e7DmVz9fr_Ynz-tviWmRdejr9kmM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:801: libc++ Hardening assertion this->has_value() failed: optional operator-> called on a disengaged value\n"
+ "/AppleInternal/Library/BuildRoots/4~CIsMugDVAk3e7DmVz9fr_Ynz-tviWmRdejr9kmM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:806: libc++ Hardening assertion this->has_value() failed: optional operator* called on a disengaged value\n"
+ "/AppleInternal/Library/BuildRoots/4~CIsMugDVAk3e7DmVz9fr_Ynz-tviWmRdejr9kmM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:811: libc++ Hardening assertion this->has_value() failed: optional operator* called on a disengaged value\n"
+ "/AppleInternal/Library/BuildRoots/4~CIsMugDVAk3e7DmVz9fr_Ynz-tviWmRdejr9kmM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:816: libc++ Hardening assertion this->has_value() failed: optional operator* called on a disengaged value\n"
+ "/AppleInternal/Library/BuildRoots/4~CIsMugDVAk3e7DmVz9fr_Ynz-tviWmRdejr9kmM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/span:457: libc++ Hardening assertion __last - __first >= 0 failed: invalid range in span's constructor (iterator, sentinel)\n"
+ "/AppleInternal/Library/BuildRoots/4~CIsMugDVAk3e7DmVz9fr_Ynz-tviWmRdejr9kmM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/span:525: libc++ Hardening assertion __idx < size() failed: span<T>::operator[](index): index out of range\n"
+ "/AppleInternal/Library/BuildRoots/4~CIsMugDVAk3e7DmVz9fr_Ynz-tviWmRdejr9kmM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:341: libc++ Hardening assertion (__end - __begin) >= 0 failed: std::string_view::string_view(iterator, sentinel) received invalid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CIsMugDVAk3e7DmVz9fr_Ynz-tviWmRdejr9kmM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/include/boost/algorithm/hex.hpp"
+ "/AppleInternal/Library/BuildRoots/4~CIsMugDVAk3e7DmVz9fr_Ynz-tviWmRdejr9kmM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/include/boost/uuid/detail/sha1.hpp"
+ "/AppleInternal/Library/BuildRoots/4~CIsMugDVAk3e7DmVz9fr_Ynz-tviWmRdejr9kmM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/include/boost/uuid/string_generator.hpp"
+ "/Library/Caches/com.apple.xbs/B65DF3A4-AF11-4BE0-AF07-2DC2EF4DDBAA/TemporaryDirectory.dwsI1I/Sources/ParallelCompression/AppleArchive/AAJSONStreams.c"
+ "/Library/Caches/com.apple.xbs/B65DF3A4-AF11-4BE0-AF07-2DC2EF4DDBAA/TemporaryDirectory.dwsI1I/Sources/ParallelCompression/AppleArchive/AASerialization.c"
+ "/Library/Caches/com.apple.xbs/B65DF3A4-AF11-4BE0-AF07-2DC2EF4DDBAA/TemporaryDirectory.dwsI1I/Sources/ParallelCompression/AppleArchiveS3/AAS3Common.c"
+ "/Library/Caches/com.apple.xbs/B65DF3A4-AF11-4BE0-AF07-2DC2EF4DDBAA/TemporaryDirectory.dwsI1I/Sources/ParallelCompression/AppleArchiveS3/AAS3Context.c"
+ "/Library/Caches/com.apple.xbs/B65DF3A4-AF11-4BE0-AF07-2DC2EF4DDBAA/TemporaryDirectory.dwsI1I/Sources/ParallelCompression/AppleArchiveS3/AAS3DownloadStreamCurl.c"
+ "/Library/Caches/com.apple.xbs/B65DF3A4-AF11-4BE0-AF07-2DC2EF4DDBAA/TemporaryDirectory.dwsI1I/Sources/ParallelCompression/AppleArchiveS3/AAS3DownloadStreamURLSession.m"
+ "/Library/Caches/com.apple.xbs/B65DF3A4-AF11-4BE0-AF07-2DC2EF4DDBAA/TemporaryDirectory.dwsI1I/Sources/ParallelCompression/AppleArchiveS3/AAS3Knox.c"
+ "/Library/Caches/com.apple.xbs/B65DF3A4-AF11-4BE0-AF07-2DC2EF4DDBAA/TemporaryDirectory.dwsI1I/Sources/ParallelCompression/Common/Threads.c"
+ "/usr/local/bin/appleconnect getToken --token-type oauth --oauth-grant-type pkce --oauth-scope openid,dsid,accountname --oauth-client-ID %s | grep oauth-id-token"
+ "524.100.20"
+ "@\"DIClient2Controller_XPCHandler\""
+ "@\"DIController2IO_XPCHandlerRootCopier\""
+ "@28@0:8i16B20B24"
+ "AES = 0x80000001"
+ "AES_KEY = 0x80000001"
+ "Authorization: Bearer openid-id-token-%s"
+ "CBCPADIV8 = 6"
+ "CBC_IV8 = 5, XTS = 0x80000001"
+ "DES3_3KEY = 17, AES_KEY = 0x80000001"
+ "DIController2IO_XPCHandlerStats"
+ "DIControllerServiceConnection"
+ "DIControllerServiceQueue"
+ "DiskImages2"
+ "Error creating disk image params"
+ "IV_TWEAK_SIZE_16 = 16"
+ "KEY_BITS_128 = 128, KEY_BITS_256 = 256"
+ "KEY_BITS_160 = 160, KEY_BITS_NONE = 0"
+ "KNOX_OIDC_TOKEN"
+ "KNOX_OIDC_TOKEN_FILE"
+ "NONE = 0"
+ "OIDC token"
+ "PKCS1 = 10, OEAP_SHA1 = 0x80000001"
+ "PKCS5_PBKDF2 = 103"
+ "PKCS5_PBKDF2_PRF_HMAC_SHA1 = 0"
+ "PKCS7 = 7"
+ "RSA = 42"
+ "SHA1_HMAC = 91, NONE = 0"
+ "T@\"DIClient2Controller_XPCHandler\",&,N,V_folderCopyXPCHandler"
+ "T@\"DIController2IO_XPCHandlerRootCopier\",&,N,V_folderCopyHandler"
+ "T@\"NSUUID\",R,N,V_instanceID"
+ "V2 = 2"
+ "_folderCopyHandler"
+ "_folderCopyXPCHandler"
+ "auto AEAHelper::key_params_t::run(function &&) [function = di_utils::overloaded<(lambda at /Library/Caches/com.apple.xbs/F4F03BAE-9D5B-4F20-86A1-FE773D0AA2A0/TemporaryDirectory.R07lTx/Sources/DiskImages2/DiskImagesLib/DiskImageParamsXPC.mm:194:8), (lambda at /Library/Caches/com.apple.xbs/F4F03BAE-9D5B-4F20-86A1-FE773D0AA2A0/TemporaryDirectory.R07lTx/Sources/DiskImages2/DiskImagesLib/DiskImageParamsXPC.mm:198:8), (lambda at /Library/Caches/com.apple.xbs/F4F03BAE-9D5B-4F20-86A1-FE773D0AA2A0/TemporaryDirectory.R07lTx/Sources/DiskImages2/DiskImagesLib/DiskImageParamsXPC.mm:202:8), (lambda at /Library/Caches/com.apple.xbs/F4F03BAE-9D5B-4F20-86A1-FE773D0AA2A0/TemporaryDirectory.R07lTx/Sources/DiskImages2/DiskImagesLib/DiskImageParamsXPC.mm:206:8)> &]"
+ "boolValueForEntitlement:"
+ "cleanup"
+ "clientID"
+ "contextGetOIDCToken"
+ "dirty = bit(0)"
+ "folderCopyHandler"
+ "folderCopyXPCHandler"
+ "getting OIDC/Westgate token"
+ "getting clientid"
+ "header_size_512 = 512, header_size_4k = 4096"
+ "initWithCapacity:"
+ "initWithFileDescriptor:writable:locked:"
+ "initWithParams:instanceID:"
+ "invalid length"
+ "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /Library/Caches/com.apple.xbs/F4F03BAE-9D5B-4F20-86A1-FE773D0AA2A0/TemporaryDirectory.R07lTx/Sources/DiskImages2/app/backends/sg_vec.cpp:455:28)]"
+ "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /Library/Caches/com.apple.xbs/F4F03BAE-9D5B-4F20-86A1-FE773D0AA2A0/TemporaryDirectory.R07lTx/Sources/DiskImages2/app/disk_images/formats/asif.cpp:1963:32)]"
+ "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /Library/Caches/com.apple.xbs/F4F03BAE-9D5B-4F20-86A1-FE773D0AA2A0/TemporaryDirectory.R07lTx/Sources/DiskImages2/app/disk_images/formats/asif.cpp:1999:32)]"
+ "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /Library/Caches/com.apple.xbs/F4F03BAE-9D5B-4F20-86A1-FE773D0AA2A0/TemporaryDirectory.R07lTx/Sources/DiskImages2/app/disk_images/formats/plugin_async_di.cpp:370:34)]"
+ "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /Library/Caches/com.apple.xbs/F4F03BAE-9D5B-4F20-86A1-FE773D0AA2A0/TemporaryDirectory.R07lTx/Sources/DiskImages2/app/disk_images/formats/plugin_async_di.cpp:450:45)]"
+ "loading OIDC token"
+ "missing OIDC/Westgate token"
+ "newWithBackendXPC:error:"
+ "oidc"
+ "read_only_cache = bit(0)"
+ "setFolderCopyHandler:"
+ "setFolderCopyXPCHandler:"
+ "ssize_t transform(Fn &&, sg_vec_ref::iterator, const sg_vec_ref::iterator &, sg_vec_ref::iterator) [Fn = (lambda at /Library/Caches/com.apple.xbs/F4F03BAE-9D5B-4F20-86A1-FE773D0AA2A0/TemporaryDirectory.R07lTx/Sources/DiskImages2/app/disk_images/io_breaker.cpp:76:13)]"
+ "ssize_t transform(Fn &&, sg_vec_ref::iterator, const sg_vec_ref::iterator &, sg_vec_ref::iterator) [Fn = (lambda at /Library/Caches/com.apple.xbs/F4F03BAE-9D5B-4F20-86A1-FE773D0AA2A0/TemporaryDirectory.R07lTx/Sources/DiskImages2/app/utils.cpp:179:13)]"
+ "vbuf validator"
+ "version_1 = 1, version_2 = 2, version_3 = 3"
+ "void crypto::details::unset_futures_errors_reporter<boost::iterators::transform_iterator<(lambda at /Library/Caches/com.apple.xbs/F4F03BAE-9D5B-4F20-86A1-FE773D0AA2A0/TemporaryDirectory.R07lTx/Sources/DiskImages2/app/crypto/crypto_format.cpp:713:35), std::__deque_iterator<crypto_format_backend::promise_io_t, crypto_format_backend::promise_io_t *, crypto_format_backend::promise_io_t &, crypto_format_backend::promise_io_t **, long>>>::report_errors(int) [It = boost::iterators::transform_iterator<(lambda at /Library/Caches/com.apple.xbs/F4F03BAE-9D5B-4F20-86A1-FE773D0AA2A0/TemporaryDirectory.R07lTx/Sources/DiskImages2/app/crypto/crypto_format.cpp:713:35), std::__deque_iterator<crypto_format_backend::promise_io_t, crypto_format_backend::promise_io_t *, crypto_format_backend::promise_io_t &, crypto_format_backend::promise_io_t **, long>>]"
+ "void crypto::details::unset_futures_errors_reporter<std::ranges::transform_view<std::ranges::ref_view<container_it<std::__deque_iterator<FileLocal::promise_io_t, FileLocal::promise_io_t *, FileLocal::promise_io_t &, FileLocal::promise_io_t **, long>>>, (lambda at /Library/Caches/com.apple.xbs/F4F03BAE-9D5B-4F20-86A1-FE773D0AA2A0/TemporaryDirectory.R07lTx/Sources/DiskImages2/app/backends/file.cpp:755:24)>::__iterator<false>>::report_errors(int) [It = std::ranges::transform_view<std::ranges::ref_view<container_it<std::__deque_iterator<FileLocal::promise_io_t, FileLocal::promise_io_t *, FileLocal::promise_io_t &, FileLocal::promise_io_t **, long>>>, (lambda at /Library/Caches/com.apple.xbs/F4F03BAE-9D5B-4F20-86A1-FE773D0AA2A0/TemporaryDirectory.R07lTx/Sources/DiskImages2/app/backends/file.cpp:755:24)>::__iterator<false>]"
- "+[DIControllerServiceDelegate sendHandleToClient:clientConnection:outError:]_block_invoke"
- "+[DIControllerServiceDelegate tryAttachWithParams:clientConnection:outError:]"
- "-[DIControllerServiceDelegate checkAttachEntitlementWithError:]"
- "-[DIControllerServiceDelegate dupWithStderrHandle:reply:]"
- "/AppleInternal/Library/BuildRoots/4~CHziugAb_8Zc4Vs5InEZgqBEoVTAgVIj8hsGb-o/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/boost/algorithm/hex.hpp"
- "/AppleInternal/Library/BuildRoots/4~CHziugAb_8Zc4Vs5InEZgqBEoVTAgVIj8hsGb-o/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/boost/uuid/detail/sha1.hpp"
- "/AppleInternal/Library/BuildRoots/4~CHziugAb_8Zc4Vs5InEZgqBEoVTAgVIj8hsGb-o/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/boost/uuid/string_generator.hpp"
- "/Library/Caches/com.apple.xbs/Sources/ParallelCompression/AppleArchive/AAJSONStreams.c"
- "/Library/Caches/com.apple.xbs/Sources/ParallelCompression/AppleArchive/AASerialization.c"
- "/Library/Caches/com.apple.xbs/Sources/ParallelCompression/AppleArchiveS3/AAS3Common.c"
- "/Library/Caches/com.apple.xbs/Sources/ParallelCompression/AppleArchiveS3/AAS3Context.c"
- "/Library/Caches/com.apple.xbs/Sources/ParallelCompression/AppleArchiveS3/AAS3DownloadStreamCurl.c"
- "/Library/Caches/com.apple.xbs/Sources/ParallelCompression/AppleArchiveS3/AAS3DownloadStreamURLSession.m"
- "/Library/Caches/com.apple.xbs/Sources/ParallelCompression/AppleArchiveS3/AAS3Knox.c"
- "/Library/Caches/com.apple.xbs/Sources/ParallelCompression/Common/Threads.c"
- "514.80.3"
- "allObjects"
- "auto AEAHelper::key_params_t::run(function &&) [function = di_utils::overloaded<(lambda at /Library/Caches/com.apple.xbs/Sources/DiskImages2/DiskImagesLib/DiskImageParamsXPC.mm:185:8), (lambda at /Library/Caches/com.apple.xbs/Sources/DiskImages2/DiskImagesLib/DiskImageParamsXPC.mm:189:8), (lambda at /Library/Caches/com.apple.xbs/Sources/DiskImages2/DiskImagesLib/DiskImageParamsXPC.mm:193:8), (lambda at /Library/Caches/com.apple.xbs/Sources/DiskImages2/DiskImagesLib/DiskImageParamsXPC.mm:197:8)> &]"
- "could not parse service name and realm"
- "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /Library/Caches/com.apple.xbs/Sources/DiskImages2/app/backends/sg_vec.cpp:455:28)]"
- "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /Library/Caches/com.apple.xbs/Sources/DiskImages2/app/disk_images/formats/asif.cpp:1954:32)]"
- "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /Library/Caches/com.apple.xbs/Sources/DiskImages2/app/disk_images/formats/asif.cpp:1990:32)]"
- "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /Library/Caches/com.apple.xbs/Sources/DiskImages2/app/disk_images/formats/plugin_async_di.cpp:370:34)]"
- "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /Library/Caches/com.apple.xbs/Sources/DiskImages2/app/disk_images/formats/plugin_async_di.cpp:450:45)]"
- "missing Westgate token"
- "missing service name or realm"
- "ssize_t transform(Fn &&, sg_vec_ref::iterator, const sg_vec_ref::iterator &, sg_vec_ref::iterator) [Fn = (lambda at /Library/Caches/com.apple.xbs/Sources/DiskImages2/app/disk_images/io_breaker.cpp:76:13)]"
- "ssize_t transform(Fn &&, sg_vec_ref::iterator, const sg_vec_ref::iterator &, sg_vec_ref::iterator) [Fn = (lambda at /Library/Caches/com.apple.xbs/Sources/DiskImages2/app/utils.cpp:180:13)]"
- "void crypto::details::unset_futures_errors_reporter<boost::iterators::transform_iterator<(lambda at /Library/Caches/com.apple.xbs/Sources/DiskImages2/app/crypto/crypto_format.cpp:712:35), std::__deque_iterator<crypto_format_backend::promise_io_t, crypto_format_backend::promise_io_t *, crypto_format_backend::promise_io_t &, crypto_format_backend::promise_io_t **, long>>>::report_errors(int) [It = boost::iterators::transform_iterator<(lambda at /Library/Caches/com.apple.xbs/Sources/DiskImages2/app/crypto/crypto_format.cpp:712:35), std::__deque_iterator<crypto_format_backend::promise_io_t, crypto_format_backend::promise_io_t *, crypto_format_backend::promise_io_t &, crypto_format_backend::promise_io_t **, long>>]"
- "void crypto::details::unset_futures_errors_reporter<std::ranges::transform_view<std::ranges::ref_view<container_it<std::__deque_iterator<FileLocal::promise_io_t, FileLocal::promise_io_t *, FileLocal::promise_io_t &, FileLocal::promise_io_t **, long>>>, (lambda at /Library/Caches/com.apple.xbs/Sources/DiskImages2/app/backends/file.cpp:755:24)>::__iterator<false>>::report_errors(int) [It = std::ranges::transform_view<std::ranges::ref_view<container_it<std::__deque_iterator<FileLocal::promise_io_t, FileLocal::promise_io_t *, FileLocal::promise_io_t &, FileLocal::promise_io_t **, long>>>, (lambda at /Library/Caches/com.apple.xbs/Sources/DiskImages2/app/backends/file.cpp:755:24)>::__iterator<false>]"

```
