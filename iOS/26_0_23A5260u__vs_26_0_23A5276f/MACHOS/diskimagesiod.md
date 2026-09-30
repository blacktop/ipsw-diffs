## diskimagesiod

> `/usr/libexec/diskimagesiod`

```diff

-485.0.0.0.0
-  __TEXT.__text: 0x192554
-  __TEXT.__auth_stubs: 0x2160
+501.0.0.0.0
+  __TEXT.__text: 0x195a6c
+  __TEXT.__auth_stubs: 0x2170
   __TEXT.__objc_stubs: 0x5b80
   __TEXT.__objc_methlist: 0x340c
-  __TEXT.__gcc_except_tab: 0x164ec
-  __TEXT.__const: 0x10e24
-  __TEXT.__cstring: 0xfcaf
-  __TEXT.__oslogstring: 0x2001
-  __TEXT.__objc_methname: 0x691e
+  __TEXT.__gcc_except_tab: 0x16908
+  __TEXT.__const: 0x10f24
+  __TEXT.__cstring: 0xfe89
+  __TEXT.__oslogstring: 0x20aa
+  __TEXT.__objc_methname: 0x6916
   __TEXT.__objc_classname: 0x604
   __TEXT.__objc_methtype: 0x2151
   __TEXT.__constg_swiftt: 0x60

   __TEXT.__swift5_fieldmd: 0x10
   __TEXT.__swift5_types: 0x4
   __TEXT.__ustring: 0x13c
-  __TEXT.__unwind_info: 0xb5a0
+  __TEXT.__unwind_info: 0xb7d8
   __TEXT.__eh_frame: 0x150
-  __DATA_CONST.__auth_got: 0x10c8
+  __DATA_CONST.__auth_got: 0x10d0
   __DATA_CONST.__got: 0x510
   __DATA_CONST.__auth_ptr: 0x38
-  __DATA_CONST.__const: 0x304e0
+  __DATA_CONST.__const: 0x30b08
   __DATA_CONST.__cfstring: 0x3e00
   __DATA_CONST.__objc_classlist: 0x230
   __DATA_CONST.__objc_catlist: 0x8

   __DATA.__objc_selrefs: 0x1b68
   __DATA.__objc_ivar: 0x2bc
   __DATA.__objc_data: 0x1660
-  __DATA.__data: 0xc28
+  __DATA.__data: 0xc30
   __DATA.__bss: 0x160
   __DATA.__common: 0x19
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCryptoTokenKit.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/local/lib/libcurl.4.dylib
-  UUID: F260880C-88C5-3A5E-8328-ECC3755B9010
-  Functions: 9383
-  Symbols:   731
-  CStrings:  4030
+  UUID: 1268BCD0-ADA7-3D4C-9DBA-0190E100BAF6
+  Functions: 9480
+  Symbols:   728
+  CStrings:  4032
 
Symbols:
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6insertEmPKcm
+ _dispatch_source_set_timer
+ _strnstr
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- _objc_retain_x25
- _statfs
CStrings:
+ " not found in registry"
+ "%.*s: A valid plist was given, but it has no pstack version key"
+ "%.*s: Device with dev name %s not found in registry"
+ "%.*s: Unable to create ioreg iterator from io_obj %d"
+ "+[DiskImageGraph loadPlistDictFromFileHandle:dict:error:]"
+ "/AppleInternal/Library/BuildRoots/4~B3QlugCigXSQj3UNmCdpQk14JvFbxyNl1F5tRpQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/include/boost/algorithm/hex.hpp"
+ "/AppleInternal/Library/BuildRoots/4~B3QlugCigXSQj3UNmCdpQk14JvFbxyNl1F5tRpQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/include/boost/uuid/detail/sha1.hpp"
+ "/AppleInternal/Library/BuildRoots/4~B3QlugCigXSQj3UNmCdpQk14JvFbxyNl1F5tRpQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/include/boost/uuid/string_generator.hpp"
+ "Failed to read file for pstack parsing"
+ "IOBlockStorageDriver"
+ "IOBlockStorageDriver device not found in registry iteration"
+ "IOMedia device not found in registry iteration"
+ "Physical block_size is "
+ "UDIF images are currently not supported in diskimage_uio"
+ "Unable to create ioreg iterator"
+ "Unable to get IOMedia preferred block size"
+ "auto AEAHelper::key_params_t::run(function &&) [function = di_utils::overloaded<(lambda at /Library/Caches/com.apple.xbs/Sources/DiskImages2/DiskImagesLib/DiskImageParamsXPC.mm:185:8), (lambda at /Library/Caches/com.apple.xbs/Sources/DiskImages2/DiskImagesLib/DiskImageParamsXPC.mm:189:8), (lambda at /Library/Caches/com.apple.xbs/Sources/DiskImages2/DiskImagesLib/DiskImageParamsXPC.mm:193:8), (lambda at /Library/Caches/com.apple.xbs/Sources/DiskImages2/DiskImagesLib/DiskImageParamsXPC.mm:197:8)> &]"
+ "could not create iterator (begin)"
+ "could not create iterator (end)"
+ "device with dev name "
+ "disk image kernel return"
+ "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /Library/Caches/com.apple.xbs/Sources/DiskImages2/app/disk_images/formats/asif.cpp:1942:32)]"
+ "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /Library/Caches/com.apple.xbs/Sources/DiskImages2/app/disk_images/formats/asif.cpp:1978:32)]"
+ "iokit_utils::di_io_obj_iterator::di_io_obj_iterator(IOOptionBits, const di_io_obj_t &)"
+ "iokit_utils::di_io_obj_t::di_io_obj_t(const char *)"
+ "kern_return_t was "
+ "loadPlistDictFromFileHandle:dict:error:"
+ "rdisk"
+ "static expected<std::pair<hdr_variant, image_format>, diskimage_err> diskimage_uio::details::diskimage_open_params_impl::get_disk_image_hdr_udif(std::shared_ptr<Backend> &)"
+ "static void DIAnalytics::sendEvent(const std::string_view &, const std::map<std::string, data_t> &)"
+ "uint32_t FileDescriptor::fetch_physical_block_size() const"
+ "void crypto::details::unset_futures_errors_reporter<std::ranges::transform_view<std::ranges::ref_view<container_it<std::__deque_iterator<FileLocal::promise_io_t, FileLocal::promise_io_t *, FileLocal::promise_io_t &, FileLocal::promise_io_t **, long>>>, (lambda at /Library/Caches/com.apple.xbs/Sources/DiskImages2/app/backends/file.cpp:755:24)>::__iterator<false>>::report_errors(int) [It = std::ranges::transform_view<std::ranges::ref_view<container_it<std::__deque_iterator<FileLocal::promise_io_t, FileLocal::promise_io_t *, FileLocal::promise_io_t &, FileLocal::promise_io_t **, long>>>, (lambda at /Library/Caches/com.apple.xbs/Sources/DiskImages2/app/backends/file.cpp:755:24)>::__iterator<false>]"
+ "void di_asif::details::dir::defrag(std::function<int (ContextASIF &)>)"
- "/AppleInternal/Library/BuildRoots/4~B2JqugAdJRGnUCghDcthjHcw70PdJ_AhtJDxlAg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/include/boost/algorithm/hex.hpp"
- "/AppleInternal/Library/BuildRoots/4~B2JqugAdJRGnUCghDcthjHcw70PdJ_AhtJDxlAg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/include/boost/uuid/detail/sha1.hpp"
- "/AppleInternal/Library/BuildRoots/4~B2JqugAdJRGnUCghDcthjHcw70PdJ_AhtJDxlAg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/include/boost/uuid/string_generator.hpp"
- "Failed to read from fd."
- "File system block_size is "
- "TB,N,V_isCache"
- "auto AEAHelper::key_params_t::run(function &&) [function = di_utils::overloaded<(lambda at /Library/Caches/com.apple.xbs/Sources/DiskImages2/DiskImagesLib/DiskImageParamsXPC.mm:182:8), (lambda at /Library/Caches/com.apple.xbs/Sources/DiskImages2/DiskImagesLib/DiskImageParamsXPC.mm:186:8), (lambda at /Library/Caches/com.apple.xbs/Sources/DiskImages2/DiskImagesLib/DiskImageParamsXPC.mm:190:8), (lambda at /Library/Caches/com.apple.xbs/Sources/DiskImages2/DiskImagesLib/DiskImageParamsXPC.mm:194:8)> &]"
- "device block size not found in registry"
- "fullDataBytes"
- "fullDataEntry"
- "hasBitmapDataEntry"
- "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /Library/Caches/com.apple.xbs/Sources/DiskImages2/app/disk_images/formats/asif.cpp:1912:32)]"
- "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /Library/Caches/com.apple.xbs/Sources/DiskImages2/app/disk_images/formats/asif.cpp:1948:32)]"
- "loadPlistDictFromURL:dict:error:"
- "numChuncksDefraged"
- "numChunksInAllocator"
- "numChunksOfBitmap"
- "numChunksOfData"
- "numOfTables"
- "statfs failed"
- "static void DIAnalytics::sendEvent(const std::string_view &, const std::map<std::string_view, data_t> &)"
- "telemetryID"
- "telemetryIndex"
- "uint32_t FileDescriptor::fetch_fs_block_size() const"
- "uninitDataBytes"
- "uninitDataEntry"
- "unmappedDataBytes"
- "unmappedDataEntry"
- "virtualDiskSize"
- "void crypto::details::unset_futures_errors_reporter<std::ranges::transform_view<std::ranges::ref_view<container_it<std::__deque_iterator<FileLocal::promise_io_t, FileLocal::promise_io_t *, FileLocal::promise_io_t &, FileLocal::promise_io_t **, long>>>, (lambda at /Library/Caches/com.apple.xbs/Sources/DiskImages2/app/backends/file.cpp:624:24)>::__iterator<false>>::report_errors(int) [It = std::ranges::transform_view<std::ranges::ref_view<container_it<std::__deque_iterator<FileLocal::promise_io_t, FileLocal::promise_io_t *, FileLocal::promise_io_t &, FileLocal::promise_io_t **, long>>>, (lambda at /Library/Caches/com.apple.xbs/Sources/DiskImages2/app/backends/file.cpp:624:24)>::__iterator<false>]"
- "void di_asif::details::dir::defrag(std::function<int (ContextASIF &)>, std::function<void (uint64_t)>)"

```
