## diskimagescontroller

> `/System/Library/PrivateFrameworks/DiskImages2.framework/XPCServices/diskimagescontroller.xpc/diskimagescontroller`

```diff

-485.0.0.0.0
-  __TEXT.__text: 0x19f120
-  __TEXT.__auth_stubs: 0x1f80
+501.0.0.0.0
+  __TEXT.__text: 0x1a2ef8
+  __TEXT.__auth_stubs: 0x1fb0
   __TEXT.__objc_stubs: 0x5400
   __TEXT.__objc_methlist: 0x3074
-  __TEXT.__gcc_except_tab: 0x175fc
-  __TEXT.__const: 0x11564
-  __TEXT.__cstring: 0x11978
-  __TEXT.__oslogstring: 0x153f
-  __TEXT.__objc_methname: 0x5ea9
+  __TEXT.__gcc_except_tab: 0x17a4c
+  __TEXT.__const: 0x116f4
+  __TEXT.__cstring: 0x11b58
+  __TEXT.__oslogstring: 0x15e8
+  __TEXT.__objc_methname: 0x5ea1
   __TEXT.__objc_classname: 0x5f2
   __TEXT.__objc_methtype: 0x1f59
   __TEXT.__ustring: 0x13c

   __TEXT.__swift5_typeref: 0x58
   __TEXT.__swift5_fieldmd: 0x10
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0xbc78
+  __TEXT.__unwind_info: 0xbef8
   __TEXT.__eh_frame: 0x150
-  __DATA_CONST.__auth_got: 0xfd8
+  __DATA_CONST.__auth_got: 0xff0
   __DATA_CONST.__got: 0x4c0
   __DATA_CONST.__auth_ptr: 0x30
-  __DATA_CONST.__const: 0x31d08
+  __DATA_CONST.__const: 0x32560
   __DATA_CONST.__cfstring: 0x3b20
   __DATA_CONST.__objc_classlist: 0x228
   __DATA_CONST.__objc_catlist: 0x8

   __DATA.__objc_selrefs: 0x1908
   __DATA.__objc_ivar: 0x258
   __DATA.__objc_data: 0x1610
-  __DATA.__data: 0xc68
+  __DATA.__data: 0xc88
   __DATA.__bss: 0x150
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
-  UUID: 91305EB6-EE5D-3C73-A263-287988225B4A
-  Functions: 9608
-  Symbols:   742
-  CStrings:  3810
+  UUID: 903AE767-3F93-3598-BE89-08AD04D15587
+  Functions: 9722
+  Symbols:   741
+  CStrings:  3812
 
Symbols:
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6insertEmPKcm
+ _dispatch_source_cancel
+ _dispatch_source_set_event_handler
+ _dispatch_source_set_timer
+ _ioctl
+ _strnstr
- ___cxa_bad_cast
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
+ "501"
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
- "485"
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
