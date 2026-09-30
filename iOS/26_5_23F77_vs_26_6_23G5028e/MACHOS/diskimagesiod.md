## diskimagesiod

> `/usr/libexec/diskimagesiod`

```diff

-524.120.8.0.0
-  __TEXT.__text: 0x1a5c74
+524.160.8.0.0
+  __TEXT.__text: 0x1a5d08
   __TEXT.__auth_stubs: 0x21f0
   __TEXT.__objc_stubs: 0x5e80
   __TEXT.__objc_methlist: 0x34cc
-  __TEXT.__gcc_except_tab: 0x1722c
+  __TEXT.__gcc_except_tab: 0x1723c
   __TEXT.__const: 0x1269f
-  __TEXT.__cstring: 0x10d75
+  __TEXT.__cstring: 0x10d9a
   __TEXT.__oslogstring: 0x218c
   __TEXT.__objc_methname: 0x6ced
   __TEXT.__objc_classname: 0x646

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/local/lib/libcurl.4.dylib
-  UUID: 84DF5826-0A69-3E0F-9A08-549AB91BE0A8
+  UUID: 5DB63351-A656-397D-975A-FAFC88039CBE
   Functions: 9891
   Symbols:   749
-  CStrings:  4212
+  CStrings:  4213
 
Functions:
~ sub_1000ffba4 : 424 -> 572
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CPkyugDxJeTIe56DBGJb41VwNzJXj9KeDHAPRDg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.6.Internal.sdk/usr/local/include/boost/algorithm/hex.hpp"
+ "/AppleInternal/Library/BuildRoots/4~CPkyugDxJeTIe56DBGJb41VwNzJXj9KeDHAPRDg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.6.Internal.sdk/usr/local/include/boost/uuid/detail/sha1.hpp"
+ "/AppleInternal/Library/BuildRoots/4~CPkyugDxJeTIe56DBGJb41VwNzJXj9KeDHAPRDg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.6.Internal.sdk/usr/local/include/boost/uuid/string_generator.hpp"
+ "auto AEAHelper::key_params_t::run(function &&) [function = di_utils::overloaded<(lambda at /Library/Caches/com.apple.xbs/F3C30338-38DB-44B5-A07D-D49DB873584C/TemporaryDirectory.vomOSH/Sources/DiskImages2/DiskImagesLib/DiskImageParamsXPC.mm:194:8), (lambda at /Library/Caches/com.apple.xbs/F3C30338-38DB-44B5-A07D-D49DB873584C/TemporaryDirectory.vomOSH/Sources/DiskImages2/DiskImagesLib/DiskImageParamsXPC.mm:198:8), (lambda at /Library/Caches/com.apple.xbs/F3C30338-38DB-44B5-A07D-D49DB873584C/TemporaryDirectory.vomOSH/Sources/DiskImages2/DiskImagesLib/DiskImageParamsXPC.mm:202:8), (lambda at /Library/Caches/com.apple.xbs/F3C30338-38DB-44B5-A07D-D49DB873584C/TemporaryDirectory.vomOSH/Sources/DiskImages2/DiskImagesLib/DiskImageParamsXPC.mm:205:8)> &]"
+ "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /Library/Caches/com.apple.xbs/F3C30338-38DB-44B5-A07D-D49DB873584C/TemporaryDirectory.vomOSH/Sources/DiskImages2/app/backends/sg_vec.cpp:455:28)]"
+ "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /Library/Caches/com.apple.xbs/F3C30338-38DB-44B5-A07D-D49DB873584C/TemporaryDirectory.vomOSH/Sources/DiskImages2/app/disk_images/formats/asif.cpp:1963:32)]"
+ "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /Library/Caches/com.apple.xbs/F3C30338-38DB-44B5-A07D-D49DB873584C/TemporaryDirectory.vomOSH/Sources/DiskImages2/app/disk_images/formats/asif.cpp:1999:32)]"
+ "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /Library/Caches/com.apple.xbs/F3C30338-38DB-44B5-A07D-D49DB873584C/TemporaryDirectory.vomOSH/Sources/DiskImages2/app/disk_images/formats/plugin_async_di.cpp:370:34)]"
+ "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /Library/Caches/com.apple.xbs/F3C30338-38DB-44B5-A07D-D49DB873584C/TemporaryDirectory.vomOSH/Sources/DiskImages2/app/disk_images/formats/plugin_async_di.cpp:450:45)]"
+ "map_element flush failed on creation"
+ "ssize_t transform(Fn &&, sg_vec_ref::iterator, const sg_vec_ref::iterator &, sg_vec_ref::iterator) [Fn = (lambda at /Library/Caches/com.apple.xbs/F3C30338-38DB-44B5-A07D-D49DB873584C/TemporaryDirectory.vomOSH/Sources/DiskImages2/app/disk_images/io_breaker.cpp:76:13)]"
+ "ssize_t transform(Fn &&, sg_vec_ref::iterator, const sg_vec_ref::iterator &, sg_vec_ref::iterator) [Fn = (lambda at /Library/Caches/com.apple.xbs/F3C30338-38DB-44B5-A07D-D49DB873584C/TemporaryDirectory.vomOSH/Sources/DiskImages2/app/utils.cpp:179:13)]"
+ "void crypto::details::unset_futures_errors_reporter<boost::iterators::transform_iterator<(lambda at /Library/Caches/com.apple.xbs/F3C30338-38DB-44B5-A07D-D49DB873584C/TemporaryDirectory.vomOSH/Sources/DiskImages2/app/crypto/crypto_format.cpp:713:35), std::__deque_iterator<crypto_format_backend::promise_io_t, crypto_format_backend::promise_io_t *, crypto_format_backend::promise_io_t &, crypto_format_backend::promise_io_t **, long>>>::report_errors(int) [It = boost::iterators::transform_iterator<(lambda at /Library/Caches/com.apple.xbs/F3C30338-38DB-44B5-A07D-D49DB873584C/TemporaryDirectory.vomOSH/Sources/DiskImages2/app/crypto/crypto_format.cpp:713:35), std::__deque_iterator<crypto_format_backend::promise_io_t, crypto_format_backend::promise_io_t *, crypto_format_backend::promise_io_t &, crypto_format_backend::promise_io_t **, long>>]"
+ "void crypto::details::unset_futures_errors_reporter<std::ranges::transform_view<std::ranges::ref_view<container_it<std::__deque_iterator<FileLocal::promise_io_t, FileLocal::promise_io_t *, FileLocal::promise_io_t &, FileLocal::promise_io_t **, long>>>, (lambda at /Library/Caches/com.apple.xbs/F3C30338-38DB-44B5-A07D-D49DB873584C/TemporaryDirectory.vomOSH/Sources/DiskImages2/app/backends/file.cpp:755:24)>::__iterator<false>>::report_errors(int) [It = std::ranges::transform_view<std::ranges::ref_view<container_it<std::__deque_iterator<FileLocal::promise_io_t, FileLocal::promise_io_t *, FileLocal::promise_io_t &, FileLocal::promise_io_t **, long>>>, (lambda at /Library/Caches/com.apple.xbs/F3C30338-38DB-44B5-A07D-D49DB873584C/TemporaryDirectory.vomOSH/Sources/DiskImages2/app/backends/file.cpp:755:24)>::__iterator<false>]"
- "/AppleInternal/Library/BuildRoots/4~COBvugCJR3Fu3dIN0GckQZhhTHQy2nXKHmkNc1A/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.5.Internal.sdk/usr/local/include/boost/algorithm/hex.hpp"
- "/AppleInternal/Library/BuildRoots/4~COBvugCJR3Fu3dIN0GckQZhhTHQy2nXKHmkNc1A/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.5.Internal.sdk/usr/local/include/boost/uuid/detail/sha1.hpp"
- "/AppleInternal/Library/BuildRoots/4~COBvugCJR3Fu3dIN0GckQZhhTHQy2nXKHmkNc1A/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.5.Internal.sdk/usr/local/include/boost/uuid/string_generator.hpp"
- "auto AEAHelper::key_params_t::run(function &&) [function = di_utils::overloaded<(lambda at /Library/Caches/com.apple.xbs/4B7FC731-2C06-4640-9EC5-E7B09E794719/TemporaryDirectory.jN9jEU/Sources/DiskImages2/DiskImagesLib/DiskImageParamsXPC.mm:194:8), (lambda at /Library/Caches/com.apple.xbs/4B7FC731-2C06-4640-9EC5-E7B09E794719/TemporaryDirectory.jN9jEU/Sources/DiskImages2/DiskImagesLib/DiskImageParamsXPC.mm:198:8), (lambda at /Library/Caches/com.apple.xbs/4B7FC731-2C06-4640-9EC5-E7B09E794719/TemporaryDirectory.jN9jEU/Sources/DiskImages2/DiskImagesLib/DiskImageParamsXPC.mm:202:8), (lambda at /Library/Caches/com.apple.xbs/4B7FC731-2C06-4640-9EC5-E7B09E794719/TemporaryDirectory.jN9jEU/Sources/DiskImages2/DiskImagesLib/DiskImageParamsXPC.mm:205:8)> &]"
- "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /Library/Caches/com.apple.xbs/4B7FC731-2C06-4640-9EC5-E7B09E794719/TemporaryDirectory.jN9jEU/Sources/DiskImages2/app/backends/sg_vec.cpp:455:28)]"
- "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /Library/Caches/com.apple.xbs/4B7FC731-2C06-4640-9EC5-E7B09E794719/TemporaryDirectory.jN9jEU/Sources/DiskImages2/app/disk_images/formats/asif.cpp:1963:32)]"
- "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /Library/Caches/com.apple.xbs/4B7FC731-2C06-4640-9EC5-E7B09E794719/TemporaryDirectory.jN9jEU/Sources/DiskImages2/app/disk_images/formats/asif.cpp:1999:32)]"
- "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /Library/Caches/com.apple.xbs/4B7FC731-2C06-4640-9EC5-E7B09E794719/TemporaryDirectory.jN9jEU/Sources/DiskImages2/app/disk_images/formats/plugin_async_di.cpp:370:34)]"
- "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /Library/Caches/com.apple.xbs/4B7FC731-2C06-4640-9EC5-E7B09E794719/TemporaryDirectory.jN9jEU/Sources/DiskImages2/app/disk_images/formats/plugin_async_di.cpp:450:45)]"
- "ssize_t transform(Fn &&, sg_vec_ref::iterator, const sg_vec_ref::iterator &, sg_vec_ref::iterator) [Fn = (lambda at /Library/Caches/com.apple.xbs/4B7FC731-2C06-4640-9EC5-E7B09E794719/TemporaryDirectory.jN9jEU/Sources/DiskImages2/app/disk_images/io_breaker.cpp:76:13)]"
- "ssize_t transform(Fn &&, sg_vec_ref::iterator, const sg_vec_ref::iterator &, sg_vec_ref::iterator) [Fn = (lambda at /Library/Caches/com.apple.xbs/4B7FC731-2C06-4640-9EC5-E7B09E794719/TemporaryDirectory.jN9jEU/Sources/DiskImages2/app/utils.cpp:179:13)]"
- "void crypto::details::unset_futures_errors_reporter<boost::iterators::transform_iterator<(lambda at /Library/Caches/com.apple.xbs/4B7FC731-2C06-4640-9EC5-E7B09E794719/TemporaryDirectory.jN9jEU/Sources/DiskImages2/app/crypto/crypto_format.cpp:713:35), std::__deque_iterator<crypto_format_backend::promise_io_t, crypto_format_backend::promise_io_t *, crypto_format_backend::promise_io_t &, crypto_format_backend::promise_io_t **, long>>>::report_errors(int) [It = boost::iterators::transform_iterator<(lambda at /Library/Caches/com.apple.xbs/4B7FC731-2C06-4640-9EC5-E7B09E794719/TemporaryDirectory.jN9jEU/Sources/DiskImages2/app/crypto/crypto_format.cpp:713:35), std::__deque_iterator<crypto_format_backend::promise_io_t, crypto_format_backend::promise_io_t *, crypto_format_backend::promise_io_t &, crypto_format_backend::promise_io_t **, long>>]"
- "void crypto::details::unset_futures_errors_reporter<std::ranges::transform_view<std::ranges::ref_view<container_it<std::__deque_iterator<FileLocal::promise_io_t, FileLocal::promise_io_t *, FileLocal::promise_io_t &, FileLocal::promise_io_t **, long>>>, (lambda at /Library/Caches/com.apple.xbs/4B7FC731-2C06-4640-9EC5-E7B09E794719/TemporaryDirectory.jN9jEU/Sources/DiskImages2/app/backends/file.cpp:755:24)>::__iterator<false>>::report_errors(int) [It = std::ranges::transform_view<std::ranges::ref_view<container_it<std::__deque_iterator<FileLocal::promise_io_t, FileLocal::promise_io_t *, FileLocal::promise_io_t &, FileLocal::promise_io_t **, long>>>, (lambda at /Library/Caches/com.apple.xbs/4B7FC731-2C06-4640-9EC5-E7B09E794719/TemporaryDirectory.jN9jEU/Sources/DiskImages2/app/backends/file.cpp:755:24)>::__iterator<false>]"

```
