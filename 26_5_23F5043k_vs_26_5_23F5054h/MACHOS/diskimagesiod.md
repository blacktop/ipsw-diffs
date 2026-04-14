## diskimagesiod

> `filesystem/usr/libexec/diskimagesiod`

```diff

-524.120.3.0.0
-  __TEXT.__text: 0x1a31c0
-  __TEXT.__auth_stubs: 0x2140
-  __TEXT.__objc_stubs: 0x5d00
-  __TEXT.__objc_methlist: 0x34a4
-  __TEXT.__gcc_except_tab: 0x17008
-  __TEXT.__const: 0x1268f
-  __TEXT.__cstring: 0x10826
-  __TEXT.__oslogstring: 0x2099
-  __TEXT.__objc_methname: 0x6b7a
+524.120.7.0.0
+  __TEXT.__text: 0x1a5c70
+  __TEXT.__auth_stubs: 0x21f0
+  __TEXT.__objc_stubs: 0x5e80
+  __TEXT.__objc_methlist: 0x34cc
+  __TEXT.__gcc_except_tab: 0x1722c
+  __TEXT.__const: 0x1269f
+  __TEXT.__cstring: 0x10d75
+  __TEXT.__oslogstring: 0x218c
+  __TEXT.__objc_methname: 0x6ced
   __TEXT.__objc_classname: 0x646
-  __TEXT.__objc_methtype: 0x22d3
+  __TEXT.__objc_methtype: 0x22d0
   __TEXT.__constg_swiftt: 0x60
   __TEXT.__swift5_typeref: 0x58
   __TEXT.__swift5_fieldmd: 0x10
   __TEXT.__swift5_types: 0x4
   __TEXT.__ustring: 0x13c
-  __TEXT.__unwind_info: 0xbf70
+  __TEXT.__unwind_info: 0xbfc8
   __TEXT.__eh_frame: 0xf0
-  __DATA_CONST.__auth_got: 0x10b8
-  __DATA_CONST.__got: 0x520
+  __DATA_CONST.__auth_got: 0x1110
+  __DATA_CONST.__got: 0x580
   __DATA_CONST.__auth_ptr: 0x40
-  __DATA_CONST.__const: 0x31e28
-  __DATA_CONST.__cfstring: 0x3e80
+  __DATA_CONST.__const: 0x31e48
+  __DATA_CONST.__cfstring: 0x43a0
   __DATA_CONST.__objc_classlist: 0x230
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x48

   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA.__objc_const: 0x52d0
-  __DATA.__objc_selrefs: 0x1be8
+  __DATA.__objc_selrefs: 0x1c48
   __DATA.__objc_ivar: 0x2c4
   __DATA.__objc_data: 0x1660
-  __DATA.__data: 0xc38
-  __DATA.__bss: 0x160
+  __DATA.__data: 0xc40
+  __DATA.__bss: 0x180
   __DATA.__common: 0x19
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/local/lib/libcurl.4.dylib
-  UUID: 4D4DA449-587F-3F81-B3AD-65563A09D168
-  Functions: 9873
-  Symbols:   726
-  CStrings:  4106
+  UUID: C1777774-44CD-39E7-A4BD-342DD282CBD2
+  Functions: 9891
+  Symbols:   749
+  CStrings:  4212
 
Symbols:
+ _MGCopyAnswer
+ _NSUnderlyingErrorKey
+ _OBJC_CLASS_$_NSURLConnection
+ _SecAccessControlCreateWithFlags
+ _SecCertificateCopyData
+ _SecGenerateSelfSignedCertificate
+ _SecKeyCreateRandomKey
+ ___assert_rtn
+ ___kCFBooleanFalse
+ _dprintf
+ _kSecAttrAccessControl
+ _kSecAttrAccessibleAfterFirstUnlockThisDeviceOnly
+ _kSecAttrIsPermanent
+ _kSecAttrKeySizeInBits
+ _kSecAttrKeyType
+ _kSecAttrKeyTypeECSECPrimeRandom
+ _kSecOidCommonName
+ _kSecOidCountryName
+ _kSecOidOrganization
+ _objc_autoreleasePoolPop
+ _objc_autoreleasePoolPush
+ _objc_opt_new
+ _objc_retain_x27
CStrings:
+ "%.*s: Cannot check if input and output are on the same fs: %{public}s, skipping squash optimization"
+ "%.*s: Failed to generate device identity: %@"
+ "%.*s: Successfully retrieved WKMS non-shipping key"
+ "%.*s: Successfully retrieved WKMS shipping key"
+ "+[DIKeyRetriever WKMSKeyWithAuthData:destKey:destKeySize:error:]"
+ "+[DIKeyRetriever WKMSShippingKeyWithURL:metadata:error:]"
+ "+[DIKeyRetriever ensureDeviceIdentityWithError:]_block_invoke"
+ "--oauth-grant-type"
+ "-C"
+ "-[DIConvertParams shouldPerformInplaceSquash]"
+ "/AppleInternal/Library/BuildRoots/4~CM2rugAu7nh_PGBnvg1cENuCKnOrHaIQ865F3n4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.5.Internal.sdk/usr/local/include/boost/algorithm/hex.hpp"
+ "/AppleInternal/Library/BuildRoots/4~CM2rugAu7nh_PGBnvg1cENuCKnOrHaIQ865F3n4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.5.Internal.sdk/usr/local/include/boost/uuid/detail/sha1.hpp"
+ "/AppleInternal/Library/BuildRoots/4~CM2rugAu7nh_PGBnvg1cENuCKnOrHaIQ865F3n4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.5.Internal.sdk/usr/local/include/boost/uuid/string_generator.hpp"
+ "9999"
+ "Accept"
+ "Apple Inc"
+ "B48@0:8r^{AuthData=^{AEAAuthData_impl}}16*24Q32^@40"
+ "BuildVersion"
+ "Could not generate OIDC token - AppleConnect Failure"
+ "Could not parse OIDC token from AppleConnect output"
+ "ERROR: Failed to serialize request: %@ error: %@"
+ "ERROR: enc-request failed base64 decode"
+ "ERROR: wrapped-key failed base64 decode"
+ "Error: failed to unwrap key. Error: %s\n"
+ "Failed to generate self signed certificate"
+ "Failed to get data from self signed certificate"
+ "No WKMS key source available in AEA metadata"
+ "Request failed with HTTP error: %lu %@: %@\n%@"
+ "The URL encoded into the AEA authdata is missing or invalid."
+ "URLByAppendingPathComponent:isDirectory:"
+ "US"
+ "WKMSKeyWithAuthData:destKey:destKeySize:error:"
+ "WKMSShippingKeyWithURL:metadata:error:"
+ "applicationId"
+ "assetAttr"
+ "attempting to authenticate with wkms"
+ "auth-data"
+ "auto AEAHelper::key_params_t::run(function &&) [function = di_utils::overloaded<(lambda at /Library/Caches/com.apple.xbs/739E7723-005E-40D0-A1BC-288B031015F8/TemporaryDirectory.aBtDD0/Sources/DiskImages2/DiskImagesLib/DiskImageParamsXPC.mm:194:8), (lambda at /Library/Caches/com.apple.xbs/739E7723-005E-40D0-A1BC-288B031015F8/TemporaryDirectory.aBtDD0/Sources/DiskImages2/DiskImagesLib/DiskImageParamsXPC.mm:198:8), (lambda at /Library/Caches/com.apple.xbs/739E7723-005E-40D0-A1BC-288B031015F8/TemporaryDirectory.aBtDD0/Sources/DiskImages2/DiskImagesLib/DiskImageParamsXPC.mm:202:8), (lambda at /Library/Caches/com.apple.xbs/739E7723-005E-40D0-A1BC-288B031015F8/TemporaryDirectory.aBtDD0/Sources/DiskImages2/DiskImagesLib/DiskImageParamsXPC.mm:205:8)> &]"
+ "base64EncodedStringWithOptions:"
+ "cert-chain"
+ "com.apple.MobileAsset.AssetType"
+ "com.apple.wkms.auth-data"
+ "com.apple.wkms.url"
+ "containsString:"
+ "devicePrivateKey"
+ "ensureDeviceIdentityWithError:"
+ "fetch_restore_key/%s OS/%@"
+ "fetch_restore_keys self signed cert"
+ "fetch_restore_keys_ephemeral"
+ "fetch_restore_keys_key_handling.m"
+ "frk_set_device_identity_certificates"
+ "g54xhr7fct39kf7ahbkys1sjhoymlz"
+ "https://%@"
+ "identityCertificates && [identityCertificates count] >= 1"
+ "initWithURL:cachePolicy:timeoutInterval:"
+ "intermediate-certs"
+ "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /Library/Caches/com.apple.xbs/739E7723-005E-40D0-A1BC-288B031015F8/TemporaryDirectory.aBtDD0/Sources/DiskImages2/app/backends/sg_vec.cpp:455:28)]"
+ "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /Library/Caches/com.apple.xbs/739E7723-005E-40D0-A1BC-288B031015F8/TemporaryDirectory.aBtDD0/Sources/DiskImages2/app/disk_images/formats/asif.cpp:1963:32)]"
+ "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /Library/Caches/com.apple.xbs/739E7723-005E-40D0-A1BC-288B031015F8/TemporaryDirectory.aBtDD0/Sources/DiskImages2/app/disk_images/formats/asif.cpp:1999:32)]"
+ "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /Library/Caches/com.apple.xbs/739E7723-005E-40D0-A1BC-288B031015F8/TemporaryDirectory.aBtDD0/Sources/DiskImages2/app/disk_images/formats/plugin_async_di.cpp:370:34)]"
+ "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /Library/Caches/com.apple.xbs/739E7723-005E-40D0-A1BC-288B031015F8/TemporaryDirectory.aBtDD0/Sources/DiskImages2/app/disk_images/formats/plugin_async_di.cpp:450:45)]"
+ "keys/fetch"
+ "leaf-cert"
+ "localizedDescription"
+ "localizedStringForStatusCode:"
+ "newOIDCTokenForHost:error:"
+ "oauth"
+ "oauth-id-token:"
+ "oma-context"
+ "openid,dsid,accountname"
+ "oztr9gq8xv5mu18jnglkhxj3qr9xgh"
+ "pkce"
+ "sendSynchronousRequest:returningResponse:error:"
+ "setCachePolicy:"
+ "ssize_t transform(Fn &&, sg_vec_ref::iterator, const sg_vec_ref::iterator &, sg_vec_ref::iterator) [Fn = (lambda at /Library/Caches/com.apple.xbs/739E7723-005E-40D0-A1BC-288B031015F8/TemporaryDirectory.aBtDD0/Sources/DiskImages2/app/disk_images/io_breaker.cpp:76:13)]"
+ "ssize_t transform(Fn &&, sg_vec_ref::iterator, const sg_vec_ref::iterator &, sg_vec_ref::iterator) [Fn = (lambda at /Library/Caches/com.apple.xbs/739E7723-005E-40D0-A1BC-288B031015F8/TemporaryDirectory.aBtDD0/Sources/DiskImages2/app/utils.cpp:179:13)]"
+ "v1/ac/decrypt"
+ "void crypto::details::unset_futures_errors_reporter<boost::iterators::transform_iterator<(lambda at /Library/Caches/com.apple.xbs/739E7723-005E-40D0-A1BC-288B031015F8/TemporaryDirectory.aBtDD0/Sources/DiskImages2/app/crypto/crypto_format.cpp:713:35), std::__deque_iterator<crypto_format_backend::promise_io_t, crypto_format_backend::promise_io_t *, crypto_format_backend::promise_io_t &, crypto_format_backend::promise_io_t **, long>>>::report_errors(int) [It = boost::iterators::transform_iterator<(lambda at /Library/Caches/com.apple.xbs/739E7723-005E-40D0-A1BC-288B031015F8/TemporaryDirectory.aBtDD0/Sources/DiskImages2/app/crypto/crypto_format.cpp:713:35), std::__deque_iterator<crypto_format_backend::promise_io_t, crypto_format_backend::promise_io_t *, crypto_format_backend::promise_io_t &, crypto_format_backend::promise_io_t **, long>>]"
+ "void crypto::details::unset_futures_errors_reporter<std::ranges::transform_view<std::ranges::ref_view<container_it<std::__deque_iterator<FileLocal::promise_io_t, FileLocal::promise_io_t *, FileLocal::promise_io_t &, FileLocal::promise_io_t **, long>>>, (lambda at /Library/Caches/com.apple.xbs/739E7723-005E-40D0-A1BC-288B031015F8/TemporaryDirectory.aBtDD0/Sources/DiskImages2/app/backends/file.cpp:755:24)>::__iterator<false>>::report_errors(int) [It = std::ranges::transform_view<std::ranges::ref_view<container_it<std::__deque_iterator<FileLocal::promise_io_t, FileLocal::promise_io_t *, FileLocal::promise_io_t &, FileLocal::promise_io_t **, long>>>, (lambda at /Library/Caches/com.apple.xbs/739E7723-005E-40D0-A1BC-288B031015F8/TemporaryDirectory.aBtDD0/Sources/DiskImages2/app/backends/file.cpp:755:24)>::__iterator<false>]"
+ "whitespaceAndNewlineCharacterSet"
+ "wkms"
- "/AppleInternal/Library/BuildRoots/4~CLiwugDPJK1VdABggASA-6dd-XIe15o8GogXbZk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.5.Internal.sdk/usr/local/include/boost/algorithm/hex.hpp"
- "/AppleInternal/Library/BuildRoots/4~CLiwugDPJK1VdABggASA-6dd-XIe15o8GogXbZk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.5.Internal.sdk/usr/local/include/boost/uuid/detail/sha1.hpp"
- "/AppleInternal/Library/BuildRoots/4~CLiwugDPJK1VdABggASA-6dd-XIe15o8GogXbZk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.5.Internal.sdk/usr/local/include/boost/uuid/string_generator.hpp"
- "B56@0:8@16r^{AuthData=^{AEAAuthData_impl}}24*32Q40^@48"
- "WKMSKeyWithURL:authData:destKey:destKeySize:error:"
- "attempting to authenticate with wkms fcs"
- "auto AEAHelper::key_params_t::run(function &&) [function = di_utils::overloaded<(lambda at /Library/Caches/com.apple.xbs/9582C130-148B-4E00-9B23-52C8C2FDF55E/TemporaryDirectory.was1id/Sources/DiskImages2/DiskImagesLib/DiskImageParamsXPC.mm:194:8), (lambda at /Library/Caches/com.apple.xbs/9582C130-148B-4E00-9B23-52C8C2FDF55E/TemporaryDirectory.was1id/Sources/DiskImages2/DiskImagesLib/DiskImageParamsXPC.mm:198:8), (lambda at /Library/Caches/com.apple.xbs/9582C130-148B-4E00-9B23-52C8C2FDF55E/TemporaryDirectory.was1id/Sources/DiskImages2/DiskImagesLib/DiskImageParamsXPC.mm:202:8), (lambda at /Library/Caches/com.apple.xbs/9582C130-148B-4E00-9B23-52C8C2FDF55E/TemporaryDirectory.was1id/Sources/DiskImages2/DiskImagesLib/DiskImageParamsXPC.mm:206:8)> &]"
- "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /Library/Caches/com.apple.xbs/9582C130-148B-4E00-9B23-52C8C2FDF55E/TemporaryDirectory.was1id/Sources/DiskImages2/app/backends/sg_vec.cpp:455:28)]"
- "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /Library/Caches/com.apple.xbs/9582C130-148B-4E00-9B23-52C8C2FDF55E/TemporaryDirectory.was1id/Sources/DiskImages2/app/disk_images/formats/asif.cpp:1963:32)]"
- "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /Library/Caches/com.apple.xbs/9582C130-148B-4E00-9B23-52C8C2FDF55E/TemporaryDirectory.was1id/Sources/DiskImages2/app/disk_images/formats/asif.cpp:1999:32)]"
- "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /Library/Caches/com.apple.xbs/9582C130-148B-4E00-9B23-52C8C2FDF55E/TemporaryDirectory.was1id/Sources/DiskImages2/app/disk_images/formats/plugin_async_di.cpp:370:34)]"
- "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /Library/Caches/com.apple.xbs/9582C130-148B-4E00-9B23-52C8C2FDF55E/TemporaryDirectory.was1id/Sources/DiskImages2/app/disk_images/formats/plugin_async_di.cpp:450:45)]"
- "ssize_t transform(Fn &&, sg_vec_ref::iterator, const sg_vec_ref::iterator &, sg_vec_ref::iterator) [Fn = (lambda at /Library/Caches/com.apple.xbs/9582C130-148B-4E00-9B23-52C8C2FDF55E/TemporaryDirectory.was1id/Sources/DiskImages2/app/disk_images/io_breaker.cpp:76:13)]"
- "ssize_t transform(Fn &&, sg_vec_ref::iterator, const sg_vec_ref::iterator &, sg_vec_ref::iterator) [Fn = (lambda at /Library/Caches/com.apple.xbs/9582C130-148B-4E00-9B23-52C8C2FDF55E/TemporaryDirectory.was1id/Sources/DiskImages2/app/utils.cpp:179:13)]"
- "void crypto::details::unset_futures_errors_reporter<boost::iterators::transform_iterator<(lambda at /Library/Caches/com.apple.xbs/9582C130-148B-4E00-9B23-52C8C2FDF55E/TemporaryDirectory.was1id/Sources/DiskImages2/app/crypto/crypto_format.cpp:713:35), std::__deque_iterator<crypto_format_backend::promise_io_t, crypto_format_backend::promise_io_t *, crypto_format_backend::promise_io_t &, crypto_format_backend::promise_io_t **, long>>>::report_errors(int) [It = boost::iterators::transform_iterator<(lambda at /Library/Caches/com.apple.xbs/9582C130-148B-4E00-9B23-52C8C2FDF55E/TemporaryDirectory.was1id/Sources/DiskImages2/app/crypto/crypto_format.cpp:713:35), std::__deque_iterator<crypto_format_backend::promise_io_t, crypto_format_backend::promise_io_t *, crypto_format_backend::promise_io_t &, crypto_format_backend::promise_io_t **, long>>]"
- "void crypto::details::unset_futures_errors_reporter<std::ranges::transform_view<std::ranges::ref_view<container_it<std::__deque_iterator<FileLocal::promise_io_t, FileLocal::promise_io_t *, FileLocal::promise_io_t &, FileLocal::promise_io_t **, long>>>, (lambda at /Library/Caches/com.apple.xbs/9582C130-148B-4E00-9B23-52C8C2FDF55E/TemporaryDirectory.was1id/Sources/DiskImages2/app/backends/file.cpp:755:24)>::__iterator<false>>::report_errors(int) [It = std::ranges::transform_view<std::ranges::ref_view<container_it<std::__deque_iterator<FileLocal::promise_io_t, FileLocal::promise_io_t *, FileLocal::promise_io_t &, FileLocal::promise_io_t **, long>>>, (lambda at /Library/Caches/com.apple.xbs/9582C130-148B-4E00-9B23-52C8C2FDF55E/TemporaryDirectory.was1id/Sources/DiskImages2/app/backends/file.cpp:755:24)>::__iterator<false>]"

```
