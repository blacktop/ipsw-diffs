## diskimagescontroller

> `/System/Library/PrivateFrameworks/DiskImages2.framework/XPCServices/diskimagescontroller.xpc/diskimagescontroller`

```diff

-379.60.1.0.0
-  __TEXT.__text: 0x14f264
-  __TEXT.__auth_stubs: 0x1e20
-  __TEXT.__objc_stubs: 0x4f20
-  __TEXT.__objc_methlist: 0x2b20
-  __TEXT.__gcc_except_tab: 0x12aac
-  __TEXT.__const: 0xbcb4
-  __TEXT.__cstring: 0xf848
-  __TEXT.__oslogstring: 0x148f
-  __TEXT.__objc_methname: 0x5a6b
+385.100.32.0.0
+  __TEXT.__text: 0x15c920
+  __TEXT.__auth_stubs: 0x1e50
+  __TEXT.__objc_stubs: 0x4fa0
+  __TEXT.__objc_methlist: 0x2d7c
+  __TEXT.__gcc_except_tab: 0x13728
+  __TEXT.__const: 0xcd54
+  __TEXT.__cstring: 0x102c8
+  __TEXT.__oslogstring: 0x14a5
+  __TEXT.__objc_methname: 0x5b23
   __TEXT.__objc_classname: 0x5af
-  __TEXT.__objc_methtype: 0x1d9e
+  __TEXT.__objc_methtype: 0x1dc7
   __TEXT.__ustring: 0x13c
   __TEXT.__constg_swiftt: 0x60
   __TEXT.__swift5_typeref: 0x4f
   __TEXT.__swift5_fieldmd: 0x10
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x9710
-  __TEXT.__eh_frame: 0xf0
-  __DATA_CONST.__auth_got: 0xf28
-  __DATA_CONST.__got: 0x458
-  __DATA_CONST.__auth_ptr: 0x30
-  __DATA_CONST.__const: 0x27048
-  __DATA_CONST.__cfstring: 0x38a0
+  __TEXT.__unwind_info: 0x9d80
+  __TEXT.__eh_frame: 0x158
+  __DATA_CONST.__auth_got: 0xf40
+  __DATA_CONST.__got: 0x490
+  __DATA_CONST.__auth_ptr: 0x28
+  __DATA_CONST.__const: 0x29f98
+  __DATA_CONST.__cfstring: 0x3960
   __DATA_CONST.__objc_classlist: 0x210
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x40

   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__objc_intobj: 0x18
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0x4cb8
-  __DATA.__objc_selrefs: 0x1720
-  __DATA.__objc_ivar: 0x240
+  __DATA.__objc_const: 0x48f8
+  __DATA.__objc_selrefs: 0x17c8
+  __DATA.__objc_ivar: 0x244
   __DATA.__objc_data: 0x1520
   __DATA.__data: 0xbc8
-  __DATA.__bss: 0x198
+  __DATA.__bss: 0x1a0
   __DATA.__common: 0x9
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
   - /usr/local/lib/libcurl.4.dylib
-  Functions: 7660
-  Symbols:   700
-  CStrings:  3106
+  Functions: 8028
+  Symbols:   709
+  CStrings:  3168
 
Symbols:
+ _OBJC_CLASS_$_NSHTTPURLResponse
+ __ZNKSt3__14__fs10filesystem4path10__filenameEv
+ __ZNKSt3__14__fs10filesystem4path16__root_directoryEv
+ __ZNSt19bad_optional_accessD1Ev
+ __ZNSt3__117bad_function_callD1Ev
+ __ZTINSt3__117bad_function_callE
+ __ZTISt19bad_optional_access
+ __ZTVNSt3__117bad_function_callE
+ __ZTVSt19bad_optional_access
+ _os_variant_is_darwinos
- __ZN13diskimage_uio16stack_image_nodeD1Ev
CStrings:
+ " auth entry"
+ " backend size "
+ " failed, error "
+ " in dir I/O, error "
+ " length "
+ "%.*s: %{public}@: mounted on %{private}@, %u bytes block size, %{public}@, barriers %@supported"
+ "(locked)"
+ "(unlocked)"
+ "+[DIKeyRetriever requestSynchronousDataWithRequest:session:error:]_block_invoke"
+ "-[DIController2IO_XPCHandlerAttach updateQuarantineFlagWithHandlerArray:flags:buffer:error:]"
+ "/AppleInternal/Library/BuildRoots/e3acf947-f363-11ef-bc4c-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/include/boost/algorithm/hex.hpp"
+ "/AppleInternal/Library/BuildRoots/e3acf947-f363-11ef-bc4c-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/include/boost/uuid/detail/sha1.hpp"
+ "/AppleInternal/Library/BuildRoots/e3acf947-f363-11ef-bc4c-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/include/boost/uuid/string_generator.hpp"
+ "385.100.32"
+ "B40@0:8*16^@24^@32"
+ "B48@0:8@16*24^@32^@40"
+ "Backend barrier failed after dir offset changed, error "
+ "Backend barrier failed during allocator failures handling, error "
+ "Backend barrier failed during bitmap allocator failures handling, error "
+ "Backend barrier failed during dir flush, error "
+ "Barrier"
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
+ "Failed to write asif header, error "
+ "Failed writing first block of dir"
+ "Failed writing full dir"
+ "Final asif "
+ "First block of dir write failed with "
+ "Flush failed after defrag, ignoring. Error "
+ "Full dir write failed with "
+ "HTTP request failed with status code: %ld"
+ "IOStorageFeatures"
+ "Not allowed more than one instance of "
+ "Requested write is out of range - offset "
+ "Root dir flush failed, error "
+ "TB,R,N,V_supportsBarrier"
+ "Table flush failed during dir flush: "
+ "The specified image is a folder but not a sparsebundle"
+ "Unexpected response type: %@"
+ "Write header failed after dir offset changed, error "
+ "_supportsBarrier"
+ "attempting to authenticate with aea key"
+ "attempting to authenticate with kms"
+ "attempting to authenticate with saks"
+ "attempting to authenticate with wkms fcs"
+ "auto AEAHelper::key_params_t::run(function &&) [function = di_utils::overloaded<(lambda at /Library/Caches/com.apple.xbs/Sources/DiskImages2/DiskImagesLib/DiskImageParamsXPC.mm:170:8), (lambda at /Library/Caches/com.apple.xbs/Sources/DiskImages2/DiskImagesLib/DiskImageParamsXPC.mm:174:8), (lambda at /Library/Caches/com.apple.xbs/Sources/DiskImages2/DiskImagesLib/DiskImageParamsXPC.mm:178:8), (lambda at /Library/Caches/com.apple.xbs/Sources/DiskImages2/DiskImagesLib/DiskImageParamsXPC.mm:182:8)> &]"
+ "backend write failed during locked flush of map element, error "
+ "caseInsensitiveCompare:"
+ "checkQuarantineWithFlags:buffer:error:"
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
+ "not "
+ "read"
+ "requestSynchronousDataWithRequest:session:error:"
+ "supportsBarrier"
+ "table flush failed during close: "
+ "updateQuarantineFlagWithHandlerArray:flags:buffer:error:"
+ "virtual int DiskImageASIF::flush(DiskImage::Context &, di_flush_mode)"
+ "virtual io_result_t DiskImageRaw::write(DiskImage::Context &, const sg_vec::iterator &, const sg_vec::iterator &)"
+ "void di_asif::details::dir::defrag(std::function<int (ContextASIF &)>)"
- "%.*s: %{public}@: mounted on %{private}@, %u bytes block size, %{public}@"
- "+[DIKeyRetriever requestSynchronousDataWithRequest:session:]_block_invoke"
- "/AppleInternal/Library/BuildRoots/df152cea-cc22-11ef-8a59-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/include/boost/algorithm/hex.hpp"
- "/AppleInternal/Library/BuildRoots/df152cea-cc22-11ef-8a59-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/include/boost/uuid/detail/sha1.hpp"
- "/AppleInternal/Library/BuildRoots/df152cea-cc22-11ef-8a59-4ee2841743e9/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/include/boost/uuid/string_generator.hpp"
- "379.60.1"
- "Can't flush asif"
- "Can't flush asif on bitmap close, backend flush failed"
- "Can't flush asif, backend flush failed"
- "Can't flush asif, bitmap flush failed"
- "Can't load bitmap while flushing"
- "Diskimages2 - ASIF - bad map entry reserved bits "
- "bool di_asif::details::table_entry_map::validate() const"
- "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /Library/Caches/com.apple.xbs/Sources/DiskImages2/app/disk_images/formats/asif.cpp:1274:32)]"
- "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /Library/Caches/com.apple.xbs/Sources/DiskImages2/app/disk_images/formats/asif.cpp:1462:30)]"
- "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /Library/Caches/com.apple.xbs/Sources/DiskImages2/app/disk_images/formats/asif.cpp:1729:32)]"
- "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /Library/Caches/com.apple.xbs/Sources/DiskImages2/app/disk_images/formats/asif.cpp:1765:32)]"
- "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /Library/Caches/com.apple.xbs/Sources/DiskImages2/app/disk_images/formats/plugin_async_di.cpp:305:45)]"
- "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /Library/Caches/com.apple.xbs/Sources/DiskImages2/app/disk_images/formats/plugin_async_di.cpp:385:45)]"
- "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at app/disk_images/formats/raw.h:67:22)]"
- "requestSynchronousDataWithRequest:session:"
- "void di_asif::details::dir::defrag(std::function<void (ContextASIF &)>)"

```
