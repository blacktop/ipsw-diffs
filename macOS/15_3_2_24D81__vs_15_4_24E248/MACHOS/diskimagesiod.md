## diskimagesiod

> `/usr/libexec/diskimagesiod`

```diff

-379.60.1.0.0
-  __TEXT.__text: 0x15f454
-  __TEXT.__auth_stubs: 0x2020
-  __TEXT.__objc_stubs: 0x58e0
-  __TEXT.__objc_methlist: 0x2f40
-  __TEXT.__gcc_except_tab: 0x12f08
-  __TEXT.__const: 0xbcb4
-  __TEXT.__cstring: 0xe431
-  __TEXT.__oslogstring: 0x265c
-  __TEXT.__objc_methname: 0x6660
+385.101.1.0.0
+  __TEXT.__text: 0x16bfb0
+  __TEXT.__auth_stubs: 0x2060
+  __TEXT.__objc_stubs: 0x5940
+  __TEXT.__objc_methlist: 0x31b4
+  __TEXT.__gcc_except_tab: 0x13a38
+  __TEXT.__const: 0xcccc
+  __TEXT.__cstring: 0xeffb
+  __TEXT.__oslogstring: 0x2693
+  __TEXT.__objc_methname: 0x6706
   __TEXT.__objc_classname: 0x5c0
-  __TEXT.__objc_methtype: 0x1f7b
+  __TEXT.__objc_methtype: 0x1f93
   __TEXT.__constg_swiftt: 0x60
   __TEXT.__swift5_typeref: 0x4f
   __TEXT.__swift5_fieldmd: 0x10
   __TEXT.__swift5_types: 0x4
   __TEXT.__ustring: 0x13c
-  __TEXT.__unwind_info: 0x9a58
-  __TEXT.__eh_frame: 0xf0
-  __DATA_CONST.__auth_got: 0x1028
-  __DATA_CONST.__got: 0x588
-  __DATA_CONST.__auth_ptr: 0x28
-  __DATA_CONST.__const: 0x27378
-  __DATA_CONST.__cfstring: 0x3da0
+  __TEXT.__unwind_info: 0xa018
+  __TEXT.__eh_frame: 0x158
+  __DATA_CONST.__auth_got: 0x1048
+  __DATA_CONST.__got: 0x5b8
+  __DATA_CONST.__auth_ptr: 0x30
+  __DATA_CONST.__const: 0x2a0a8
+  __DATA_CONST.__cfstring: 0x3f00
   __DATA_CONST.__objc_classlist: 0x218
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x48

   __DATA_CONST.__objc_arraydata: 0x88
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__objc_arrayobj: 0x30
-  __DATA.__objc_const: 0x52c0
-  __DATA.__objc_selrefs: 0x1a10
-  __DATA.__objc_ivar: 0x2a8
+  __DATA.__objc_const: 0x4ee0
+  __DATA.__objc_selrefs: 0x1ab8
+  __DATA.__objc_ivar: 0x2ac
   __DATA.__objc_data: 0x1570
   __DATA.__data: 0xc00
-  __DATA.__bss: 0x118
+  __DATA.__bss: 0x120
   __DATA.__common: 0x9
   - /System/Library/Frameworks/CFNetwork.framework/Versions/A/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 7F0DD8D2-4656-3087-AB3F-AEE3F85DF093
-  Functions: 7936
-  Symbols:   731
-  CStrings:  3924
+  UUID: 47ACFF38-F023-384D-85AD-FE0DF2AD878A
+  Functions: 8266
+  Symbols:   742
+  CStrings:  4000
 
Symbols:
+ _DADiskMountWithArguments
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
CStrings:
+ " auth entry"
+ " backend size "
+ " failed, error "
+ " in dir I/O, error "
+ " length "
+ "%.*s: %{public}@ mounted successfully"
+ "%.*s: %{public}@: mounted on %{private}@, %u bytes block size, %{public}@, barriers %@supported"
+ "%.*s: Mount error: %@"
+ "(locked)"
+ "(unlocked)"
+ "+[DIKeyRetriever requestSynchronousDataWithRequest:session:error:]_block_invoke"
+ "-[DIDiskArb mountWithDeviceName:args:filesystem:mountURL:error:]"
+ "-o"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ParallelCompression/AppleArchive/AAJSONStreams.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ParallelCompression/AppleArchive/AASerialization.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ParallelCompression/AppleArchiveS3/AAS3Common.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ParallelCompression/AppleArchiveS3/AAS3Context.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ParallelCompression/AppleArchiveS3/AAS3DownloadStreamCurl.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ParallelCompression/AppleArchiveS3/AAS3DownloadStreamURLSession.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ParallelCompression/AppleArchiveS3/AAS3Knox.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ParallelCompression/Common/Threads.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.4.Internal.sdk/usr/local/include/boost/algorithm/hex.hpp"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.4.Internal.sdk/usr/local/include/boost/uuid/detail/sha1.hpp"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.4.Internal.sdk/usr/local/include/boost/uuid/string_generator.hpp"
+ "/sbin/mount"
+ "B56@0:8@16@24@32@40^@48"
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
+ "Failed to create DADisk during mount"
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
+ "Too many mount arguments"
+ "Unexpected response type: %@"
+ "Write header failed after dir offset changed, error "
+ "_supportsBarrier"
+ "attempting to authenticate with aea key"
+ "attempting to authenticate with kms"
+ "attempting to authenticate with saks"
+ "attempting to authenticate with wkms fcs"
+ "auto AEAHelper::key_params_t::run(function &&) [function = di_utils::overloaded<(lambda at /AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/DiskImages2/DiskImagesLib/DiskImageParamsXPC.mm:170:8), (lambda at /AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/DiskImages2/DiskImagesLib/DiskImageParamsXPC.mm:174:8), (lambda at /AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/DiskImages2/DiskImagesLib/DiskImageParamsXPC.mm:178:8), (lambda at /AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/DiskImages2/DiskImagesLib/DiskImageParamsXPC.mm:182:8)> &]"
+ "backend write failed during locked flush of map element, error "
+ "caseInsensitiveCompare:"
+ "componentsJoinedByString:"
+ "int di_asif::details::dir::flush(ContextASIF &, uint64_t, bool)"
+ "int di_asif::details::dir::flush_dir(ContextASIF &, uint64_t)"
+ "int di_asif::details::dir::handle_all_failures(ContextASIF &)"
+ "int di_asif::details::map_element::flush_locked(ContextASIF &, table *, size_t)"
+ "int di_asif::header::write_header(Backend &)"
+ "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/DiskImages2/app/disk_images/formats/asif.cpp:1284:32)]"
+ "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/DiskImages2/app/disk_images/formats/asif.cpp:1472:30)]"
+ "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/DiskImages2/app/disk_images/formats/asif.cpp:1757:32)]"
+ "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/DiskImages2/app/disk_images/formats/asif.cpp:1793:32)]"
+ "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/DiskImages2/app/disk_images/formats/plugin_async_di.cpp:306:45)]"
+ "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/DiskImages2/app/disk_images/formats/plugin_async_di.cpp:386:45)]"
+ "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at app/disk_images/formats/raw.h:72:22)]"
+ "io_result_t di_asif::details::dir::do_io(ContextASIF &, const sg_vec::iterator &, const sg_vec::iterator &, bool)"
+ "mountWithDeviceName:args:filesystem:mountURL:error:"
+ "not "
+ "requestSynchronousDataWithRequest:session:error:"
+ "set size failed"
+ "ssize_t transform(Fn &&, sg_vec_ref::iterator, const sg_vec_ref::iterator &, sg_vec_ref::iterator) [Fn = (lambda at /AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/DiskImages2/app/disk_images/io_breaker.cpp:76:13)]"
+ "ssize_t transform(Fn &&, sg_vec_ref::iterator, const sg_vec_ref::iterator &, sg_vec_ref::iterator) [Fn = (lambda at /AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/DiskImages2/app/utils.cpp:180:13)]"
+ "supportsBarrier"
+ "table flush failed during close: "
+ "virtual int DiskImageASIF::flush(DiskImage::Context &, di_flush_mode)"
+ "virtual io_result_t DiskImageRaw::write(DiskImage::Context &, const sg_vec::iterator &, const sg_vec::iterator &)"
+ "void di_asif::details::dir::defrag(std::function<int (ContextASIF &)>)"
- "%.*s: %{public}@: mounted on %{private}@, %u bytes block size, %{public}@"
- "%.*s: Ejecting %{private}@"
- "+[DIKeyRetriever requestSynchronousDataWithRequest:session:]_block_invoke"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.3.Internal.sdk/usr/local/include/boost/algorithm/hex.hpp"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.3.Internal.sdk/usr/local/include/boost/uuid/detail/sha1.hpp"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.3.Internal.sdk/usr/local/include/boost/uuid/string_generator.hpp"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ParallelCompression/AppleArchive/AAJSONStreams.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ParallelCompression/AppleArchive/AASerialization.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ParallelCompression/AppleArchiveS3/AAS3Common.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ParallelCompression/AppleArchiveS3/AAS3Context.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ParallelCompression/AppleArchiveS3/AAS3DownloadStreamCurl.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ParallelCompression/AppleArchiveS3/AAS3DownloadStreamURLSession.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ParallelCompression/AppleArchiveS3/AAS3Knox.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/ParallelCompression/Common/Threads.c"
- "Can't flush asif"
- "Can't flush asif on bitmap close, backend flush failed"
- "Can't flush asif, backend flush failed"
- "Can't flush asif, bitmap flush failed"
- "Can't load bitmap while flushing"
- "Diskimages2 - ASIF - bad map entry reserved bits "
- "bool di_asif::details::table_entry_map::validate() const"
- "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/DiskImages2/app/disk_images/formats/asif.cpp:1274:32)]"
- "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/DiskImages2/app/disk_images/formats/asif.cpp:1462:30)]"
- "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/DiskImages2/app/disk_images/formats/asif.cpp:1729:32)]"
- "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/DiskImages2/app/disk_images/formats/asif.cpp:1765:32)]"
- "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/DiskImages2/app/disk_images/formats/plugin_async_di.cpp:305:45)]"
- "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/DiskImages2/app/disk_images/formats/plugin_async_di.cpp:385:45)]"
- "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at app/disk_images/formats/raw.h:67:22)]"
- "requestSynchronousDataWithRequest:session:"
- "ssize_t transform(Fn &&, sg_vec_ref::iterator, const sg_vec_ref::iterator &, sg_vec_ref::iterator) [Fn = (lambda at /AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/DiskImages2/app/disk_images/io_breaker.cpp:76:13)]"
- "ssize_t transform(Fn &&, sg_vec_ref::iterator, const sg_vec_ref::iterator &, sg_vec_ref::iterator) [Fn = (lambda at /AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/DiskImages2/app/utils.cpp:180:13)]"
- "void di_asif::details::dir::defrag(std::function<void (ContextASIF &)>)"

```
