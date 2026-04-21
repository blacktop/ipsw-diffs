## diskimagescontroller

> `/System/Library/PrivateFrameworks/DiskImages2.framework/XPCServices/diskimagescontroller.xpc/diskimagescontroller`

```diff

-524.120.7.0.0
-  __TEXT.__text: 0x1b2194
+524.120.8.0.0
+  __TEXT.__text: 0x1b2198
   __TEXT.__auth_stubs: 0x2020
   __TEXT.__objc_stubs: 0x5760
   __TEXT.__objc_methlist: 0x31bc

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/local/lib/libcurl.4.dylib
-  UUID: FC5DDC9C-88ED-31D5-994A-76A5B27731E0
+  UUID: 16372BD3-CEA5-32B0-ADC5-6CFB265E31F3
   Functions: 10120
   Symbols:   771
   CStrings:  4012
Functions:
~ sub_100193b7c : 632 -> 636
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CNXwugDiYShwyAwZpYYWTNt1JaMGZu9gDCKsmzI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.5.Internal.sdk/usr/local/include/boost/algorithm/hex.hpp"
+ "/AppleInternal/Library/BuildRoots/4~CNXwugDiYShwyAwZpYYWTNt1JaMGZu9gDCKsmzI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.5.Internal.sdk/usr/local/include/boost/uuid/detail/sha1.hpp"
+ "/AppleInternal/Library/BuildRoots/4~CNXwugDiYShwyAwZpYYWTNt1JaMGZu9gDCKsmzI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.5.Internal.sdk/usr/local/include/boost/uuid/string_generator.hpp"
+ "524.120.8"
+ "auto AEAHelper::key_params_t::run(function &&) [function = di_utils::overloaded<(lambda at /Library/Caches/com.apple.xbs/C668CADA-9511-4AA3-A1EF-1EE1DDA74A31/TemporaryDirectory.1suJgl/Sources/DiskImages2/DiskImagesLib/DiskImageParamsXPC.mm:194:8), (lambda at /Library/Caches/com.apple.xbs/C668CADA-9511-4AA3-A1EF-1EE1DDA74A31/TemporaryDirectory.1suJgl/Sources/DiskImages2/DiskImagesLib/DiskImageParamsXPC.mm:198:8), (lambda at /Library/Caches/com.apple.xbs/C668CADA-9511-4AA3-A1EF-1EE1DDA74A31/TemporaryDirectory.1suJgl/Sources/DiskImages2/DiskImagesLib/DiskImageParamsXPC.mm:202:8), (lambda at /Library/Caches/com.apple.xbs/C668CADA-9511-4AA3-A1EF-1EE1DDA74A31/TemporaryDirectory.1suJgl/Sources/DiskImages2/DiskImagesLib/DiskImageParamsXPC.mm:205:8)> &]"
+ "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /Library/Caches/com.apple.xbs/C668CADA-9511-4AA3-A1EF-1EE1DDA74A31/TemporaryDirectory.1suJgl/Sources/DiskImages2/app/backends/sg_vec.cpp:455:28)]"
+ "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /Library/Caches/com.apple.xbs/C668CADA-9511-4AA3-A1EF-1EE1DDA74A31/TemporaryDirectory.1suJgl/Sources/DiskImages2/app/disk_images/formats/asif.cpp:1963:32)]"
+ "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /Library/Caches/com.apple.xbs/C668CADA-9511-4AA3-A1EF-1EE1DDA74A31/TemporaryDirectory.1suJgl/Sources/DiskImages2/app/disk_images/formats/asif.cpp:1999:32)]"
+ "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /Library/Caches/com.apple.xbs/C668CADA-9511-4AA3-A1EF-1EE1DDA74A31/TemporaryDirectory.1suJgl/Sources/DiskImages2/app/disk_images/formats/plugin_async_di.cpp:370:34)]"
+ "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /Library/Caches/com.apple.xbs/C668CADA-9511-4AA3-A1EF-1EE1DDA74A31/TemporaryDirectory.1suJgl/Sources/DiskImages2/app/disk_images/formats/plugin_async_di.cpp:450:45)]"
+ "ssize_t transform(Fn &&, sg_vec_ref::iterator, const sg_vec_ref::iterator &, sg_vec_ref::iterator) [Fn = (lambda at /Library/Caches/com.apple.xbs/C668CADA-9511-4AA3-A1EF-1EE1DDA74A31/TemporaryDirectory.1suJgl/Sources/DiskImages2/app/disk_images/io_breaker.cpp:76:13)]"
+ "ssize_t transform(Fn &&, sg_vec_ref::iterator, const sg_vec_ref::iterator &, sg_vec_ref::iterator) [Fn = (lambda at /Library/Caches/com.apple.xbs/C668CADA-9511-4AA3-A1EF-1EE1DDA74A31/TemporaryDirectory.1suJgl/Sources/DiskImages2/app/utils.cpp:179:13)]"
+ "void crypto::details::unset_futures_errors_reporter<boost::iterators::transform_iterator<(lambda at /Library/Caches/com.apple.xbs/C668CADA-9511-4AA3-A1EF-1EE1DDA74A31/TemporaryDirectory.1suJgl/Sources/DiskImages2/app/crypto/crypto_format.cpp:713:35), std::__deque_iterator<crypto_format_backend::promise_io_t, crypto_format_backend::promise_io_t *, crypto_format_backend::promise_io_t &, crypto_format_backend::promise_io_t **, long>>>::report_errors(int) [It = boost::iterators::transform_iterator<(lambda at /Library/Caches/com.apple.xbs/C668CADA-9511-4AA3-A1EF-1EE1DDA74A31/TemporaryDirectory.1suJgl/Sources/DiskImages2/app/crypto/crypto_format.cpp:713:35), std::__deque_iterator<crypto_format_backend::promise_io_t, crypto_format_backend::promise_io_t *, crypto_format_backend::promise_io_t &, crypto_format_backend::promise_io_t **, long>>]"
+ "void crypto::details::unset_futures_errors_reporter<std::ranges::transform_view<std::ranges::ref_view<container_it<std::__deque_iterator<FileLocal::promise_io_t, FileLocal::promise_io_t *, FileLocal::promise_io_t &, FileLocal::promise_io_t **, long>>>, (lambda at /Library/Caches/com.apple.xbs/C668CADA-9511-4AA3-A1EF-1EE1DDA74A31/TemporaryDirectory.1suJgl/Sources/DiskImages2/app/backends/file.cpp:755:24)>::__iterator<false>>::report_errors(int) [It = std::ranges::transform_view<std::ranges::ref_view<container_it<std::__deque_iterator<FileLocal::promise_io_t, FileLocal::promise_io_t *, FileLocal::promise_io_t &, FileLocal::promise_io_t **, long>>>, (lambda at /Library/Caches/com.apple.xbs/C668CADA-9511-4AA3-A1EF-1EE1DDA74A31/TemporaryDirectory.1suJgl/Sources/DiskImages2/app/backends/file.cpp:755:24)>::__iterator<false>]"
- "/AppleInternal/Library/BuildRoots/4~CM2rugAu7nh_PGBnvg1cENuCKnOrHaIQ865F3n4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.5.Internal.sdk/usr/local/include/boost/algorithm/hex.hpp"
- "/AppleInternal/Library/BuildRoots/4~CM2rugAu7nh_PGBnvg1cENuCKnOrHaIQ865F3n4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.5.Internal.sdk/usr/local/include/boost/uuid/detail/sha1.hpp"
- "/AppleInternal/Library/BuildRoots/4~CM2rugAu7nh_PGBnvg1cENuCKnOrHaIQ865F3n4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.5.Internal.sdk/usr/local/include/boost/uuid/string_generator.hpp"
- "524.120.7"
- "auto AEAHelper::key_params_t::run(function &&) [function = di_utils::overloaded<(lambda at /Library/Caches/com.apple.xbs/739E7723-005E-40D0-A1BC-288B031015F8/TemporaryDirectory.aBtDD0/Sources/DiskImages2/DiskImagesLib/DiskImageParamsXPC.mm:194:8), (lambda at /Library/Caches/com.apple.xbs/739E7723-005E-40D0-A1BC-288B031015F8/TemporaryDirectory.aBtDD0/Sources/DiskImages2/DiskImagesLib/DiskImageParamsXPC.mm:198:8), (lambda at /Library/Caches/com.apple.xbs/739E7723-005E-40D0-A1BC-288B031015F8/TemporaryDirectory.aBtDD0/Sources/DiskImages2/DiskImagesLib/DiskImageParamsXPC.mm:202:8), (lambda at /Library/Caches/com.apple.xbs/739E7723-005E-40D0-A1BC-288B031015F8/TemporaryDirectory.aBtDD0/Sources/DiskImages2/DiskImagesLib/DiskImageParamsXPC.mm:205:8)> &]"
- "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /Library/Caches/com.apple.xbs/739E7723-005E-40D0-A1BC-288B031015F8/TemporaryDirectory.aBtDD0/Sources/DiskImages2/app/backends/sg_vec.cpp:455:28)]"
- "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /Library/Caches/com.apple.xbs/739E7723-005E-40D0-A1BC-288B031015F8/TemporaryDirectory.aBtDD0/Sources/DiskImages2/app/disk_images/formats/asif.cpp:1963:32)]"
- "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /Library/Caches/com.apple.xbs/739E7723-005E-40D0-A1BC-288B031015F8/TemporaryDirectory.aBtDD0/Sources/DiskImages2/app/disk_images/formats/asif.cpp:1999:32)]"
- "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /Library/Caches/com.apple.xbs/739E7723-005E-40D0-A1BC-288B031015F8/TemporaryDirectory.aBtDD0/Sources/DiskImages2/app/disk_images/formats/plugin_async_di.cpp:370:34)]"
- "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /Library/Caches/com.apple.xbs/739E7723-005E-40D0-A1BC-288B031015F8/TemporaryDirectory.aBtDD0/Sources/DiskImages2/app/disk_images/formats/plugin_async_di.cpp:450:45)]"
- "ssize_t transform(Fn &&, sg_vec_ref::iterator, const sg_vec_ref::iterator &, sg_vec_ref::iterator) [Fn = (lambda at /Library/Caches/com.apple.xbs/739E7723-005E-40D0-A1BC-288B031015F8/TemporaryDirectory.aBtDD0/Sources/DiskImages2/app/disk_images/io_breaker.cpp:76:13)]"
- "ssize_t transform(Fn &&, sg_vec_ref::iterator, const sg_vec_ref::iterator &, sg_vec_ref::iterator) [Fn = (lambda at /Library/Caches/com.apple.xbs/739E7723-005E-40D0-A1BC-288B031015F8/TemporaryDirectory.aBtDD0/Sources/DiskImages2/app/utils.cpp:179:13)]"
- "void crypto::details::unset_futures_errors_reporter<boost::iterators::transform_iterator<(lambda at /Library/Caches/com.apple.xbs/739E7723-005E-40D0-A1BC-288B031015F8/TemporaryDirectory.aBtDD0/Sources/DiskImages2/app/crypto/crypto_format.cpp:713:35), std::__deque_iterator<crypto_format_backend::promise_io_t, crypto_format_backend::promise_io_t *, crypto_format_backend::promise_io_t &, crypto_format_backend::promise_io_t **, long>>>::report_errors(int) [It = boost::iterators::transform_iterator<(lambda at /Library/Caches/com.apple.xbs/739E7723-005E-40D0-A1BC-288B031015F8/TemporaryDirectory.aBtDD0/Sources/DiskImages2/app/crypto/crypto_format.cpp:713:35), std::__deque_iterator<crypto_format_backend::promise_io_t, crypto_format_backend::promise_io_t *, crypto_format_backend::promise_io_t &, crypto_format_backend::promise_io_t **, long>>]"
- "void crypto::details::unset_futures_errors_reporter<std::ranges::transform_view<std::ranges::ref_view<container_it<std::__deque_iterator<FileLocal::promise_io_t, FileLocal::promise_io_t *, FileLocal::promise_io_t &, FileLocal::promise_io_t **, long>>>, (lambda at /Library/Caches/com.apple.xbs/739E7723-005E-40D0-A1BC-288B031015F8/TemporaryDirectory.aBtDD0/Sources/DiskImages2/app/backends/file.cpp:755:24)>::__iterator<false>>::report_errors(int) [It = std::ranges::transform_view<std::ranges::ref_view<container_it<std::__deque_iterator<FileLocal::promise_io_t, FileLocal::promise_io_t *, FileLocal::promise_io_t &, FileLocal::promise_io_t **, long>>>, (lambda at /Library/Caches/com.apple.xbs/739E7723-005E-40D0-A1BC-288B031015F8/TemporaryDirectory.aBtDD0/Sources/DiskImages2/app/backends/file.cpp:755:24)>::__iterator<false>]"

```
