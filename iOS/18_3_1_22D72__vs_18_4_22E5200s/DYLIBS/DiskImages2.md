## DiskImages2

> `/System/Library/PrivateFrameworks/DiskImages2.framework/DiskImages2`

```diff

-379.60.1.0.0
-  __TEXT.__text: 0x15d7e4
-  __TEXT.__auth_stubs: 0x1ea0
-  __TEXT.__objc_methlist: 0x2d08
-  __TEXT.__const: 0xc1b4
-  __TEXT.__gcc_except_tab: 0x12af4
-  __TEXT.__cstring: 0xe238
-  __TEXT.__oslogstring: 0x1336
+385.100.25.0.0
+  __TEXT.__text: 0x167b98
+  __TEXT.__auth_stubs: 0x1ee0
+  __TEXT.__objc_methlist: 0x2f24
+  __TEXT.__const: 0xd034
+  __TEXT.__gcc_except_tab: 0x133dc
+  __TEXT.__cstring: 0xe9b8
+  __TEXT.__oslogstring: 0x1357
   __TEXT.__ustring: 0x13c
   __TEXT.__constg_swiftt: 0x60
   __TEXT.__swift5_typeref: 0x4f
   __TEXT.__swift5_fieldmd: 0x10
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x9fd0
-  __TEXT.__eh_frame: 0xf0
+  __TEXT.__unwind_info: 0xa4c0
+  __TEXT.__eh_frame: 0x158
   __TEXT.__objc_classname: 0x597
-  __TEXT.__objc_methname: 0x6158
-  __TEXT.__objc_methtype: 0x1d8c
-  __TEXT.__objc_stubs: 0x5220
-  __DATA_CONST.__got: 0x510
+  __TEXT.__objc_methname: 0x61a6
+  __TEXT.__objc_methtype: 0x1da4
+  __TEXT.__objc_stubs: 0x5240
+  __DATA_CONST.__got: 0x520
   __DATA_CONST.__const: 0xd00
   __DATA_CONST.__objc_classlist: 0x210
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x18c0
+  __DATA_CONST.__objc_selrefs: 0x1958
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x1a0
   __DATA_CONST.__objc_arraydata: 0x78
-  __AUTH_CONST.__auth_got: 0xf68
-  __AUTH_CONST.__auth_ptr: 0x28
-  __AUTH_CONST.__const: 0x29928
-  __AUTH_CONST.__cfstring: 0x3940
-  __AUTH_CONST.__objc_const: 0x4db0
+  __AUTH_CONST.__auth_got: 0xf88
+  __AUTH_CONST.__auth_ptr: 0x30
+  __AUTH_CONST.__const: 0x2c038
+  __AUTH_CONST.__cfstring: 0x39e0
+  __AUTH_CONST.__objc_const: 0x4a10
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_dictobj: 0x28

   __DATA.__objc_ivar: 0x260
   __DATA.__data: 0xae8
   __DATA.__common: 0x9
-  __DATA.__bss: 0x120
+  __DATA.__bss: 0x128
   __DATA_DIRTY.__objc_data: 0xa0
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
   - /usr/local/lib/libcurl.4.dylib
-  Functions: 8200
-  Symbols:   9091
-  CStrings:  3174
+  Functions: 8499
+  Symbols:   9407
+  CStrings:  3224
 
Symbols:
+ _DADiskMountWithArguments
+ __ZNKSt3__14__fs10filesystem4path10__filenameEv
+ __ZNKSt3__14__fs10filesystem4path16__root_directoryEv
+ __ZNSt3__117bad_function_callD1Ev
+ __ZTINSt3__117bad_function_callE
+ __ZTVNSt3__117bad_function_callE
+ _os_variant_is_darwinos
CStrings:
+ " backend size "
+ " failed, error "
+ " in dir I/O, error "
+ " length "
+ "%.*s: %{public}@ mounted successfully"
+ "%.*s: Mount error: %@"
+ "(locked)"
+ "(unlocked)"
+ "-[DIDiskArb mountWithDeviceName:args:filesystem:mountURL:error:]"
+ "-o"
+ "/AppleInternal/Library/BuildRoots/80a4978a-ebfc-11ef-ae29-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/include/boost/algorithm/hex.hpp"
+ "/AppleInternal/Library/BuildRoots/80a4978a-ebfc-11ef-ae29-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/include/boost/uuid/detail/sha1.hpp"
+ "/AppleInternal/Library/BuildRoots/80a4978a-ebfc-11ef-ae29-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/include/boost/uuid/string_generator.hpp"
+ "/sbin/mount"
+ "B56@0:8@16@24@32@40^@48"
+ "Backend barrier failed after dir offset changed, error "
+ "Backend barrier failed during allocator failures handling, error "
+ "Backend barrier failed during bitmap allocator failures handling, error "
+ "Backend barrier failed during dir flush, error "
+ "Barrier failed after defrag, error "
+ "Can't flush asif on map element close, backend barrier failed"
+ "Can't flush asif on table close, backend barrier failed"
+ "Can't flush asif on table flush, backend barrier failed"
+ "Can't flush asif table, backend barrier failed"
+ "Can't flush asif table, backend write failed"
+ "Can't flush asif table, bitmap flush failed "
+ "Can't load bitmap while flushing asif table "
+ "Error during ASIF flush: "
+ "Failed barrier after writing full dir"
+ "Failed barrier at start of dir flush, error"
+ "Failed during data entry write in table write, error "
+ "Failed during table "
+ "Failed to create DADisk during mount"
+ "Failed to write asif header, error "
+ "Failed writing first block of dir"
+ "Failed writing full dir"
+ "Final asif "
+ "First block of dir write failed with "
+ "Flush failed after defrag, ignoring. Error "
+ "Full dir write failed with "
+ "Requested write is out of range - offset "
+ "Root dir flush failed, error "
+ "Table flush failed during dir flush: "
+ "The specified image is a folder but not a sparsebundle"
+ "Too many mount arguments"
+ "Write header failed after dir offset changed, error "
+ "backend write failed during locked flush of map element, error "
+ "componentsJoinedByString:"
+ "diskimage_uio::details::diskimage_impl::diskimage_impl(iter_t, iter_t, uint32_t) [iter_t = boost::iterators::transform_iterator<(lambda at /Library/Caches/com.apple.xbs/Sources/DiskImages2/libdiskimagesio/diskimage_uio.cpp:1702:29), const diskimage_uio::rref_capture<diskimage_uio::diskimage_open_params_pair> *>]"
+ "flush"
+ "int di_asif::details::dir::flush(ContextASIF &, uint64_t, bool)"
+ "int di_asif::details::dir::flush_dir(ContextASIF &, uint64_t)"
+ "int di_asif::details::dir::handle_all_failures(ContextASIF &)"
+ "int di_asif::details::map_element::flush_locked(ContextASIF &, table *, size_t)"
+ "int di_asif::header::write_header(Backend &)"
+ "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /Library/Caches/com.apple.xbs/Sources/DiskImages2/app/disk_images/formats/asif.cpp:1284:32)]"
+ "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /Library/Caches/com.apple.xbs/Sources/DiskImages2/app/disk_images/formats/asif.cpp:1472:30)]"
+ "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /Library/Caches/com.apple.xbs/Sources/DiskImages2/app/disk_images/formats/asif.cpp:1757:32)]"
+ "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /Library/Caches/com.apple.xbs/Sources/DiskImages2/app/disk_images/formats/asif.cpp:1793:32)]"
+ "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /Library/Caches/com.apple.xbs/Sources/DiskImages2/app/disk_images/formats/plugin_async_di.cpp:306:45)]"
+ "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /Library/Caches/com.apple.xbs/Sources/DiskImages2/app/disk_images/formats/plugin_async_di.cpp:386:45)]"
+ "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at app/disk_images/formats/raw.h:72:22)]"
+ "io_result_t di_asif::details::dir::do_io(ContextASIF &, const sg_vec::iterator &, const sg_vec::iterator &, bool)"
+ "mountWithDeviceName:args:filesystem:mountURL:error:"
+ "read"
+ "set size failed"
+ "static diskimage_impl *diskimage_uio::details::diskimage_impl::create_diskimage_impl(iter_t, iter_t, uint32_t) [iter_t = boost::iterators::transform_iterator<(lambda at /Library/Caches/com.apple.xbs/Sources/DiskImages2/libdiskimagesio/diskimage_uio.cpp:1702:29), const diskimage_uio::rref_capture<diskimage_uio::diskimage_open_params_pair> *>]"
+ "table flush failed during close: "
+ "virtual int DiskImageASIF::flush(DiskImage::Context &, di_flush_mode)"
+ "virtual io_result_t DiskImageRaw::write(DiskImage::Context &, const sg_vec::iterator &, const sg_vec::iterator &)"
+ "void di_asif::details::dir::defrag(std::function<int (ContextASIF &)>)"
- "%.*s: Ejecting %{private}@"
- "/AppleInternal/Library/BuildRoots/774ff07e-d344-11ef-9a16-36218cb420d5/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/include/boost/algorithm/hex.hpp"
- "/AppleInternal/Library/BuildRoots/774ff07e-d344-11ef-9a16-36218cb420d5/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/include/boost/uuid/detail/sha1.hpp"
- "/AppleInternal/Library/BuildRoots/774ff07e-d344-11ef-9a16-36218cb420d5/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/include/boost/uuid/string_generator.hpp"
- "Can't flush asif"
- "Can't flush asif on bitmap close, backend flush failed"
- "Can't flush asif, backend flush failed"
- "Can't flush asif, bitmap flush failed"
- "Can't load bitmap while flushing"
- "Diskimages2 - ASIF - bad map entry reserved bits "
- "bool di_asif::details::table_entry_map::validate() const"
- "diskimage_uio::details::diskimage_impl::diskimage_impl(iter_t, iter_t, uint32_t) [iter_t = boost::iterators::transform_iterator<(lambda at /Library/Caches/com.apple.xbs/Sources/DiskImages2/libdiskimagesio/diskimage_uio.cpp:1699:29), const diskimage_uio::rref_capture<diskimage_uio::diskimage_open_params_pair> *>]"
- "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /Library/Caches/com.apple.xbs/Sources/DiskImages2/app/disk_images/formats/asif.cpp:1274:32)]"
- "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /Library/Caches/com.apple.xbs/Sources/DiskImages2/app/disk_images/formats/asif.cpp:1462:30)]"
- "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /Library/Caches/com.apple.xbs/Sources/DiskImages2/app/disk_images/formats/asif.cpp:1729:32)]"
- "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /Library/Caches/com.apple.xbs/Sources/DiskImages2/app/disk_images/formats/asif.cpp:1765:32)]"
- "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /Library/Caches/com.apple.xbs/Sources/DiskImages2/app/disk_images/formats/plugin_async_di.cpp:305:45)]"
- "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /Library/Caches/com.apple.xbs/Sources/DiskImages2/app/disk_images/formats/plugin_async_di.cpp:385:45)]"
- "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at app/disk_images/formats/raw.h:67:22)]"
- "static diskimage_impl *diskimage_uio::details::diskimage_impl::create_diskimage_impl(iter_t, iter_t, uint32_t) [iter_t = boost::iterators::transform_iterator<(lambda at /Library/Caches/com.apple.xbs/Sources/DiskImages2/libdiskimagesio/diskimage_uio.cpp:1699:29), const diskimage_uio::rref_capture<diskimage_uio::diskimage_open_params_pair> *>]"
- "void di_asif::details::dir::defrag(std::function<void (ContextASIF &)>)"

```
