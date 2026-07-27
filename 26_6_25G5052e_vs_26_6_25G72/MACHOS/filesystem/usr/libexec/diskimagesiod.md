## diskimagesiod

> `/usr/libexec/diskimagesiod`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__got`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-524.160.10.0.0
-  __TEXT.__text: 0x1cbdd0
+524.160.11.0.0
+  __TEXT.__text: 0x1cc338
   __TEXT.__auth_stubs: 0x2380
-  __TEXT.__objc_stubs: 0x6540
+  __TEXT.__objc_stubs: 0x6560
   __TEXT.__objc_methlist: 0x383c
-  __TEXT.__const: 0x13077
-  __TEXT.__gcc_except_tab: 0x19928
-  __TEXT.__objc_methname: 0x7618
-  __TEXT.__oslogstring: 0x2e5b
-  __TEXT.__cstring: 0x12a20
+  __TEXT.__const: 0x1307f
+  __TEXT.__gcc_except_tab: 0x19a00
+  __TEXT.__objc_methname: 0x7623
+  __TEXT.__oslogstring: 0x2f50
+  __TEXT.__cstring: 0x12b1a
   __TEXT.__objc_classname: 0x6bf
   __TEXT.__objc_methtype: 0x27ab
   __TEXT.__constg_swiftt: 0x60

   __TEXT.__swift5_fieldmd: 0x10
   __TEXT.__swift5_types: 0x4
   __TEXT.__ustring: 0x13c
-  __TEXT.__unwind_info: 0xcc10
+  __TEXT.__unwind_info: 0xcc20
   __TEXT.__eh_frame: 0xf0
   __DATA_CONST.__auth_got: 0x11d8
   __DATA_CONST.__got: 0x680
   __DATA_CONST.__auth_ptr: 0x48
   __DATA_CONST.__const: 0x33a68
-  __DATA_CONST.__cfstring: 0x4bc0
+  __DATA_CONST.__cfstring: 0x4c00
   __DATA_CONST.__objc_classlist: 0x250
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x50

   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA.__objc_const: 0x57f8
-  __DATA.__objc_selrefs: 0x1e08
+  __DATA.__objc_selrefs: 0x1e10
   __DATA.__objc_ivar: 0x2ec
   __DATA.__objc_data: 0x17a0
   __DATA.__data: 0xca0

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 10471
+  Functions: 10472
   Symbols:   807
-  CStrings:  3975
+  CStrings:  3984
 
CStrings:
+ "%.*s: Refusing to decode a network-backed disk image for a caller whose sandbox denies network-outbound (pid=%d)"
+ "%.*s: Refusing to decode a network-backed disk image for an app-sandboxed caller without com.apple.security.network.client (pid=%d)"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hd5tMA/Sources/ParallelCompression/AppleArchive/AAJSONStreams.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hd5tMA/Sources/ParallelCompression/AppleArchive/AASerialization.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hd5tMA/Sources/ParallelCompression/AppleArchiveS3/AAS3Common.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hd5tMA/Sources/ParallelCompression/AppleArchiveS3/AAS3Context.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hd5tMA/Sources/ParallelCompression/AppleArchiveS3/AAS3DownloadStreamCurl.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hd5tMA/Sources/ParallelCompression/AppleArchiveS3/AAS3DownloadStreamURLSession.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hd5tMA/Sources/ParallelCompression/AppleArchiveS3/AAS3Knox.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hd5tMA/Sources/ParallelCompression/Common/Threads.c"
+ "App-sandboxed caller lacks com.apple.security.network.client"
+ "Caller's sandbox denies network-outbound"
+ "auditToken"
+ "auto AEAHelper::key_params_t::run(function &&) [function = di_utils::overloaded<(lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DNnZrq/Sources/DiskImages2/DiskImagesLib/DiskImageParamsXPC.mm:194:8), (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DNnZrq/Sources/DiskImages2/DiskImagesLib/DiskImageParamsXPC.mm:198:8), (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DNnZrq/Sources/DiskImages2/DiskImagesLib/DiskImageParamsXPC.mm:202:8), (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DNnZrq/Sources/DiskImages2/DiskImagesLib/DiskImageParamsXPC.mm:205:8)> &]"
+ "com.apple.security.app-sandbox"
+ "com.apple.security.network.client"
+ "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DNnZrq/Sources/DiskImages2/app/backends/sg_vec.cpp:455:28)]"
+ "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DNnZrq/Sources/DiskImages2/app/disk_images/formats/asif.cpp:1966:32)]"
+ "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DNnZrq/Sources/DiskImages2/app/disk_images/formats/asif.cpp:2002:32)]"
+ "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DNnZrq/Sources/DiskImages2/app/disk_images/formats/plugin_async_di.cpp:370:34)]"
+ "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DNnZrq/Sources/DiskImages2/app/disk_images/formats/plugin_async_di.cpp:450:45)]"
+ "network-outbound"
+ "ssize_t transform(Fn &&, sg_vec_ref::iterator, const sg_vec_ref::iterator &, sg_vec_ref::iterator) [Fn = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DNnZrq/Sources/DiskImages2/app/disk_images/io_breaker.cpp:76:13)]"
+ "ssize_t transform(Fn &&, sg_vec_ref::iterator, const sg_vec_ref::iterator &, sg_vec_ref::iterator) [Fn = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DNnZrq/Sources/DiskImages2/app/utils.cpp:179:13)]"
+ "void crypto::details::unset_futures_errors_reporter<boost::iterators::transform_iterator<(lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DNnZrq/Sources/DiskImages2/app/crypto/crypto_format.cpp:713:35), std::__deque_iterator<crypto_format_backend::promise_io_t, crypto_format_backend::promise_io_t *, crypto_format_backend::promise_io_t &, crypto_format_backend::promise_io_t **, long>>>::report_errors(int) [It = boost::iterators::transform_iterator<(lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DNnZrq/Sources/DiskImages2/app/crypto/crypto_format.cpp:713:35), std::__deque_iterator<crypto_format_backend::promise_io_t, crypto_format_backend::promise_io_t *, crypto_format_backend::promise_io_t &, crypto_format_backend::promise_io_t **, long>>]"
+ "void crypto::details::unset_futures_errors_reporter<std::ranges::transform_view<std::ranges::ref_view<container_it<std::__deque_iterator<FileLocal::promise_io_t, FileLocal::promise_io_t *, FileLocal::promise_io_t &, FileLocal::promise_io_t **, long>>>, (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DNnZrq/Sources/DiskImages2/app/backends/file.cpp:755:24)>::__iterator<false>>::report_errors(int) [It = std::ranges::transform_view<std::ranges::ref_view<container_it<std::__deque_iterator<FileLocal::promise_io_t, FileLocal::promise_io_t *, FileLocal::promise_io_t &, FileLocal::promise_io_t **, long>>>, (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DNnZrq/Sources/DiskImages2/app/backends/file.cpp:755:24)>::__iterator<false>]"
+ "void requireClientNetworkAccessOrThrow(NSXPCConnection *__strong)"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.dHcUmx/Sources/ParallelCompression/AppleArchive/AAJSONStreams.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.dHcUmx/Sources/ParallelCompression/AppleArchive/AASerialization.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.dHcUmx/Sources/ParallelCompression/AppleArchiveS3/AAS3Common.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.dHcUmx/Sources/ParallelCompression/AppleArchiveS3/AAS3Context.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.dHcUmx/Sources/ParallelCompression/AppleArchiveS3/AAS3DownloadStreamCurl.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.dHcUmx/Sources/ParallelCompression/AppleArchiveS3/AAS3DownloadStreamURLSession.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.dHcUmx/Sources/ParallelCompression/AppleArchiveS3/AAS3Knox.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.dHcUmx/Sources/ParallelCompression/Common/Threads.c"
- "auto AEAHelper::key_params_t::run(function &&) [function = di_utils::overloaded<(lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NL9Now/Sources/DiskImages2/DiskImagesLib/DiskImageParamsXPC.mm:194:8), (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NL9Now/Sources/DiskImages2/DiskImagesLib/DiskImageParamsXPC.mm:198:8), (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NL9Now/Sources/DiskImages2/DiskImagesLib/DiskImageParamsXPC.mm:202:8), (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NL9Now/Sources/DiskImages2/DiskImagesLib/DiskImageParamsXPC.mm:205:8)> &]"
- "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NL9Now/Sources/DiskImages2/app/backends/sg_vec.cpp:455:28)]"
- "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NL9Now/Sources/DiskImages2/app/disk_images/formats/asif.cpp:1966:32)]"
- "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NL9Now/Sources/DiskImages2/app/disk_images/formats/asif.cpp:2002:32)]"
- "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NL9Now/Sources/DiskImages2/app/disk_images/formats/plugin_async_di.cpp:370:34)]"
- "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NL9Now/Sources/DiskImages2/app/disk_images/formats/plugin_async_di.cpp:450:45)]"
- "ssize_t transform(Fn &&, sg_vec_ref::iterator, const sg_vec_ref::iterator &, sg_vec_ref::iterator) [Fn = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NL9Now/Sources/DiskImages2/app/disk_images/io_breaker.cpp:76:13)]"
- "ssize_t transform(Fn &&, sg_vec_ref::iterator, const sg_vec_ref::iterator &, sg_vec_ref::iterator) [Fn = (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NL9Now/Sources/DiskImages2/app/utils.cpp:179:13)]"
- "void crypto::details::unset_futures_errors_reporter<boost::iterators::transform_iterator<(lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NL9Now/Sources/DiskImages2/app/crypto/crypto_format.cpp:713:35), std::__deque_iterator<crypto_format_backend::promise_io_t, crypto_format_backend::promise_io_t *, crypto_format_backend::promise_io_t &, crypto_format_backend::promise_io_t **, long>>>::report_errors(int) [It = boost::iterators::transform_iterator<(lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NL9Now/Sources/DiskImages2/app/crypto/crypto_format.cpp:713:35), std::__deque_iterator<crypto_format_backend::promise_io_t, crypto_format_backend::promise_io_t *, crypto_format_backend::promise_io_t &, crypto_format_backend::promise_io_t **, long>>]"
- "void crypto::details::unset_futures_errors_reporter<std::ranges::transform_view<std::ranges::ref_view<container_it<std::__deque_iterator<FileLocal::promise_io_t, FileLocal::promise_io_t *, FileLocal::promise_io_t &, FileLocal::promise_io_t **, long>>>, (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NL9Now/Sources/DiskImages2/app/backends/file.cpp:755:24)>::__iterator<false>>::report_errors(int) [It = std::ranges::transform_view<std::ranges::ref_view<container_it<std::__deque_iterator<FileLocal::promise_io_t, FileLocal::promise_io_t *, FileLocal::promise_io_t &, FileLocal::promise_io_t **, long>>>, (lambda at /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NL9Now/Sources/DiskImages2/app/backends/file.cpp:755:24)>::__iterator<false>]"
```
