## threadradiod

> `/System/Library/PrivateFrameworks/CoreThreadRadio.framework/threadradiod`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-442.0.0.0.0
-  __TEXT.__text: 0x41808c
-  __TEXT.__auth_stubs: 0x12bd0
+446.0.2.0.1
+  __TEXT.__text: 0x41813c
+  __TEXT.__auth_stubs: 0x12be0
   __TEXT.__objc_stubs: 0xa100
   __TEXT.__init_offsets: 0xb4
   __TEXT.__objc_methlist: 0x6aa4
   __TEXT.__gcc_except_tab: 0x2a39c
   __TEXT.__const: 0x8664
   __TEXT.__oslogstring: 0x28004
-  __TEXT.__cstring: 0x37256
+  __TEXT.__cstring: 0x371d9
   __TEXT.__objc_classname: 0x6eb
   __TEXT.__objc_methname: 0xf7d7
   __TEXT.__objc_methtype: 0x4451

   __TEXT.__swift_as_entry: 0xac
   __TEXT.__swift_as_ret: 0x88
   __TEXT.__swift_as_cont: 0x1dc
-  __TEXT.__unwind_info: 0x147d8
+  __TEXT.__unwind_info: 0x147e0
   __TEXT.__eh_frame: 0x1f68
   __DATA_CONST.__const: 0xdcc8
   __DATA_CONST.__cfstring: 0x6ce0

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x140
-  __DATA_CONST.__auth_got: 0x9600
+  __DATA_CONST.__auth_got: 0x9608
   __DATA_CONST.__got: 0xbc0
   __DATA_CONST.__auth_ptr: 0x240
   __DATA.__objc_const: 0x8b38

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 18296
-  Symbols:   24095
-  CStrings:  13489
+  Functions: 18298
+  Symbols:   24097
+  CStrings:  13485
 
Symbols:
+ /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Binaries/CoreThreadRadio/install/Symbols/BuiltProducts/libopenthread-ftd.a(heap-16dd3b2b8cab5b944232e64e8968a5e8.o)
+ /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Binaries/CoreThreadRadio/install/Symbols/BuiltProducts/libopenthread-ftd.a(heap-3a411b3d0959a68cc965778d5b58371b.o)
+ __ZN2ot10KeyManager8ClearKekEv
+ __ZNK2ot10KeyManager8IsKekSetEv
- /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Binaries/CoreThreadRadio/install/Symbols/BuiltProducts/libopenthread-ftd.a(heap-907cf6985676bcfa85796b69de7a3ca2.o)
- /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Binaries/CoreThreadRadio/install/Symbols/BuiltProducts/libopenthread-ftd.a(heap-e09d5eb68d8170f36b42857da0a1dc1e.o)
Functions:
~ __Z50CAMetricsHandlers_handle_getprop_RCP2_generic_histPU24objcproto13OS_xpc_object8NSObjectP19NSMutableDictionarytP8NSString : 2484 -> 2520
~ _GLOBAL__sub_I_host_context.cpp : 212 -> 248
~ __ZN2ot6Spinel11RadioSpinel15ParseRadioFrameER12otRadioFramePKhtRi : 992 -> 892
~ __ZN2ot3Mac3Mac22ProcessReceiveSecurityERNS0_7RxFrameERKNS0_7AddressEPNS_8NeighborE : 2628 -> 2668
+ __ZNK2ot10KeyManager8IsKekSetEv
~ __ZN2ot7MeshCoP6Joiner6FinishE7otError : 212 -> 224
~ __ZN2ot7MeshCoP12JoinerRouter27HandleJoinerEntrustResponseEPNS_4Coap7MessageEPKNS_3Ip611MessageInfoE7otError : 212 -> 224
~ __ZN2ot10KeyManagerC2ERNS_8InstanceE : 228 -> 244
~ __ZN2ot10KeyManager6SetKekERKNS_3Mac3KeyE : 72 -> 88
+ __ZN2ot10KeyManager8ClearKekEv
CStrings:
+ " Morty_Version: V0.446.0.3"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/include/c++/v1/__hash_table:1855: libc++ Hardening assertion __p != end() failed: unordered container::erase(iterator) called with a non-dereferenceable iterator\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/include/c++/v1/__hash_table:242: libc++ Hardening assertion __node_ != nullptr failed: Attempted to dereference a non-dereferenceable unordered container iterator\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/include/c++/v1/__hash_table:248: libc++ Hardening assertion __node_ != nullptr failed: Attempted to dereference a non-dereferenceable unordered container iterator\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/include/c++/v1/__hash_table:254: libc++ Hardening assertion __node_ != nullptr failed: Attempted to increment a non-incrementable unordered container iterator\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/include/c++/v1/__memory/construct_at.h:47: libc++ Hardening assertion __location != nullptr failed: null pointer given to construct_at\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/include/c++/v1/__memory/construct_at.h:59: libc++ Hardening assertion __loc != nullptr failed: null pointer given to destroy_at\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/include/c++/v1/__memory/unique_ptr.h:583: libc++ Hardening assertion __checker_.__in_bounds<deleter_type>(std::__to_address(__ptr_), __i) failed: unique_ptr<T[]>::operator[](index): index out of range\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/include/c++/v1/deque:1565: libc++ Hardening assertion !empty() failed: deque::front called on an empty deque\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/include/c++/v1/deque:2199: libc++ Hardening assertion !empty() failed: deque::pop_front called on an empty deque\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/include/c++/v1/streambuf:301: libc++ Hardening assertion std::__is_valid_range(__gbeg, __gnext) failed: [gbeg, gnext) must be a valid range\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/include/c++/v1/streambuf:302: libc++ Hardening assertion std::__is_valid_range(__gbeg, __gend) failed: [gbeg, gend) must be a valid range\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/include/c++/v1/streambuf:303: libc++ Hardening assertion std::__is_valid_range(__gnext, __gend) failed: [gnext, gend) must be a valid range\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/include/c++/v1/streambuf:319: libc++ Hardening assertion std::__is_valid_range(__pbeg, __pend) failed: [pbeg, pend) must be a valid range\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/include/c++/v1/string:1074: libc++ Hardening assertion __s != nullptr failed: basic_string(const char*) detected nullptr\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/include/c++/v1/string:2219: libc++ Hardening assertion __s < __min_cap failed: __s should never be greater than or equal to the short string capacity\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/include/c++/v1/string:2226: libc++ Hardening assertion !__rep_.__s.__is_long_ failed: String has to be short when trying to get the short size\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/include/c++/v1/string:2235: libc++ Hardening assertion __rep_.__l.__is_long_ failed: String has to be long when trying to get the long size\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/include/c++/v1/string:2247: libc++ Hardening assertion __rep_.__l.__is_long_ failed: String has to be long when trying to get the long capacity\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/include/c++/v1/string:2252: libc++ Hardening assertion __rep_.__l.__is_long_ failed: String has to be long when trying to get the long pointer\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/include/c++/v1/string:2257: libc++ Hardening assertion __rep_.__l.__is_long_ failed: String has to be long when trying to get the long pointer\n"
- " Morty_Version: V0.442"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__hash_table:1855: libc++ Hardening assertion __p != end() failed: unordered container::erase(iterator) called with a non-dereferenceable iterator\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__hash_table:242: libc++ Hardening assertion __node_ != nullptr failed: Attempted to dereference a non-dereferenceable unordered container iterator\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__hash_table:248: libc++ Hardening assertion __node_ != nullptr failed: Attempted to dereference a non-dereferenceable unordered container iterator\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__hash_table:254: libc++ Hardening assertion __node_ != nullptr failed: Attempted to increment a non-incrementable unordered container iterator\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__memory/construct_at.h:47: libc++ Hardening assertion __location != nullptr failed: null pointer given to construct_at\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__memory/construct_at.h:59: libc++ Hardening assertion __loc != nullptr failed: null pointer given to destroy_at\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__memory/unique_ptr.h:583: libc++ Hardening assertion __checker_.__in_bounds<deleter_type>(std::__to_address(__ptr_), __i) failed: unique_ptr<T[]>::operator[](index): index out of range\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/deque:1565: libc++ Hardening assertion !empty() failed: deque::front called on an empty deque\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/deque:2199: libc++ Hardening assertion !empty() failed: deque::pop_front called on an empty deque\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/streambuf:301: libc++ Hardening assertion std::__is_valid_range(__gbeg, __gnext) failed: [gbeg, gnext) must be a valid range\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/streambuf:302: libc++ Hardening assertion std::__is_valid_range(__gbeg, __gend) failed: [gbeg, gend) must be a valid range\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/streambuf:303: libc++ Hardening assertion std::__is_valid_range(__gnext, __gend) failed: [gnext, gend) must be a valid range\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/streambuf:319: libc++ Hardening assertion std::__is_valid_range(__pbeg, __pend) failed: [pbeg, pend) must be a valid range\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/string:1074: libc++ Hardening assertion __s != nullptr failed: basic_string(const char*) detected nullptr\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/string:2219: libc++ Hardening assertion __s < __min_cap failed: __s should never be greater than or equal to the short string capacity\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/string:2226: libc++ Hardening assertion !__rep_.__s.__is_long_ failed: String has to be short when trying to get the short size\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/string:2235: libc++ Hardening assertion __rep_.__l.__is_long_ failed: String has to be long when trying to get the long size\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/string:2247: libc++ Hardening assertion __rep_.__l.__is_long_ failed: String has to be long when trying to get the long capacity\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/string:2252: libc++ Hardening assertion __rep_.__l.__is_long_ failed: String has to be long when trying to get the long pointer\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/string:2257: libc++ Hardening assertion __rep_.__l.__is_long_ failed: String has to be long when trying to get the long pointer\n"
- "OT_ERROR_PARSE <<frame_unpack>>"
- "OT_ERROR_PARSE <<mac_data_unpack>>"
- "OT_ERROR_PARSE <<receiveError>>"
- "OT_ERROR_PARSE <<receiveErrorOutOfRange>>"
```
