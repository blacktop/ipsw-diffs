## diskimagesiod

> `/usr/libexec/diskimagesiod`

```diff

-385.101.1.0.0
-  __TEXT.__text: 0x16bfb0
-  __TEXT.__auth_stubs: 0x2060
+385.120.3.0.0
+  __TEXT.__text: 0x16d2d4
+  __TEXT.__auth_stubs: 0x2070
   __TEXT.__objc_stubs: 0x5940
   __TEXT.__objc_methlist: 0x31b4
-  __TEXT.__gcc_except_tab: 0x13a38
-  __TEXT.__const: 0xcccc
+  __TEXT.__gcc_except_tab: 0x13af8
+  __TEXT.__const: 0xcd8c
   __TEXT.__cstring: 0xeffb
   __TEXT.__oslogstring: 0x2693
   __TEXT.__objc_methname: 0x6706

   __TEXT.__swift5_fieldmd: 0x10
   __TEXT.__swift5_types: 0x4
   __TEXT.__ustring: 0x13c
-  __TEXT.__unwind_info: 0xa018
+  __TEXT.__unwind_info: 0xa0b8
   __TEXT.__eh_frame: 0x158
-  __DATA_CONST.__auth_got: 0x1048
+  __DATA_CONST.__auth_got: 0x1050
   __DATA_CONST.__got: 0x5b8
   __DATA_CONST.__auth_ptr: 0x30
-  __DATA_CONST.__const: 0x2a0a8
+  __DATA_CONST.__const: 0x2a4e8
   __DATA_CONST.__cfstring: 0x3f00
   __DATA_CONST.__objc_classlist: 0x218
   __DATA_CONST.__objc_catlist: 0x8

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 8266
-  Symbols:   742
+  Functions: 8298
+  Symbols:   743
   CStrings:  3509
 
Symbols:
+ __ZNSt3__115system_categoryEv
CStrings:
+ "/AppleInternal/Library/BuildRoots/1d1afd2a-039a-11f0-91c4-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/ParallelCompression/AppleArchive/AAJSONStreams.c"
+ "/AppleInternal/Library/BuildRoots/1d1afd2a-039a-11f0-91c4-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/ParallelCompression/AppleArchive/AASerialization.c"
+ "/AppleInternal/Library/BuildRoots/1d1afd2a-039a-11f0-91c4-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/ParallelCompression/AppleArchiveS3/AAS3Common.c"
+ "/AppleInternal/Library/BuildRoots/1d1afd2a-039a-11f0-91c4-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/ParallelCompression/AppleArchiveS3/AAS3Context.c"
+ "/AppleInternal/Library/BuildRoots/1d1afd2a-039a-11f0-91c4-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/ParallelCompression/AppleArchiveS3/AAS3DownloadStreamCurl.c"
+ "/AppleInternal/Library/BuildRoots/1d1afd2a-039a-11f0-91c4-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/ParallelCompression/AppleArchiveS3/AAS3DownloadStreamURLSession.m"
+ "/AppleInternal/Library/BuildRoots/1d1afd2a-039a-11f0-91c4-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/ParallelCompression/AppleArchiveS3/AAS3Knox.c"
+ "/AppleInternal/Library/BuildRoots/1d1afd2a-039a-11f0-91c4-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/ParallelCompression/Common/Threads.c"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.5.Internal.sdk/usr/local/include/boost/algorithm/hex.hpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.5.Internal.sdk/usr/local/include/boost/uuid/detail/sha1.hpp"
+ "/AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.5.Internal.sdk/usr/local/include/boost/uuid/string_generator.hpp"
+ "auto AEAHelper::key_params_t::run(function &&) [function = di_utils::overloaded<(lambda at /AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/DiskImages2/DiskImagesLib/DiskImageParamsXPC.mm:170:8), (lambda at /AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/DiskImages2/DiskImagesLib/DiskImageParamsXPC.mm:174:8), (lambda at /AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/DiskImages2/DiskImagesLib/DiskImageParamsXPC.mm:178:8), (lambda at /AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/DiskImages2/DiskImagesLib/DiskImageParamsXPC.mm:182:8)> &]"
+ "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/DiskImages2/app/disk_images/formats/asif.cpp:1284:32)]"
+ "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/DiskImages2/app/disk_images/formats/asif.cpp:1472:30)]"
+ "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/DiskImages2/app/disk_images/formats/asif.cpp:1757:32)]"
+ "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/DiskImages2/app/disk_images/formats/asif.cpp:1793:32)]"
+ "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/DiskImages2/app/disk_images/formats/plugin_async_di.cpp:306:45)]"
+ "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/DiskImages2/app/disk_images/formats/plugin_async_di.cpp:386:45)]"
+ "ssize_t transform(Fn &&, sg_vec_ref::iterator, const sg_vec_ref::iterator &, sg_vec_ref::iterator) [Fn = (lambda at /AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/DiskImages2/app/disk_images/io_breaker.cpp:76:13)]"
+ "ssize_t transform(Fn &&, sg_vec_ref::iterator, const sg_vec_ref::iterator &, sg_vec_ref::iterator) [Fn = (lambda at /AppleInternal/Library/BuildRoots/9eb49808-0a13-11f0-927b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/DiskImages2/app/utils.cpp:180:13)]"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ParallelCompression/AppleArchive/AAJSONStreams.c"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ParallelCompression/AppleArchive/AASerialization.c"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ParallelCompression/AppleArchiveS3/AAS3Common.c"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ParallelCompression/AppleArchiveS3/AAS3Context.c"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ParallelCompression/AppleArchiveS3/AAS3DownloadStreamCurl.c"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ParallelCompression/AppleArchiveS3/AAS3DownloadStreamURLSession.m"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ParallelCompression/AppleArchiveS3/AAS3Knox.c"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ParallelCompression/Common/Threads.c"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.4.Internal.sdk/usr/local/include/boost/algorithm/hex.hpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.4.Internal.sdk/usr/local/include/boost/uuid/detail/sha1.hpp"
- "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.4.Internal.sdk/usr/local/include/boost/uuid/string_generator.hpp"
- "auto AEAHelper::key_params_t::run(function &&) [function = di_utils::overloaded<(lambda at /AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/DiskImages2/DiskImagesLib/DiskImageParamsXPC.mm:170:8), (lambda at /AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/DiskImages2/DiskImagesLib/DiskImageParamsXPC.mm:174:8), (lambda at /AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/DiskImages2/DiskImagesLib/DiskImageParamsXPC.mm:178:8), (lambda at /AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/DiskImages2/DiskImagesLib/DiskImageParamsXPC.mm:182:8)> &]"
- "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/DiskImages2/app/disk_images/formats/asif.cpp:1284:32)]"
- "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/DiskImages2/app/disk_images/formats/asif.cpp:1472:30)]"
- "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/DiskImages2/app/disk_images/formats/asif.cpp:1757:32)]"
- "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/DiskImages2/app/disk_images/formats/asif.cpp:1793:32)]"
- "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/DiskImages2/app/disk_images/formats/plugin_async_di.cpp:306:45)]"
- "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/DiskImages2/app/disk_images/formats/plugin_async_di.cpp:386:45)]"
- "ssize_t transform(Fn &&, sg_vec_ref::iterator, const sg_vec_ref::iterator &, sg_vec_ref::iterator) [Fn = (lambda at /AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/DiskImages2/app/disk_images/io_breaker.cpp:76:13)]"
- "ssize_t transform(Fn &&, sg_vec_ref::iterator, const sg_vec_ref::iterator &, sg_vec_ref::iterator) [Fn = (lambda at /AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/DiskImages2/app/utils.cpp:180:13)]"

```
