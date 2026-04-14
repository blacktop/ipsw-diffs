## diskimagescontroller

> `filesystem/System/Library/PrivateFrameworks/DiskImages2.framework/XPCServices/diskimagescontroller.xpc/diskimagescontroller`

```diff

-524.120.3.0.0
-  __TEXT.__text: 0x1aee24
-  __TEXT.__auth_stubs: 0x1fb0
-  __TEXT.__objc_stubs: 0x55e0
-  __TEXT.__objc_methlist: 0x3194
-  __TEXT.__gcc_except_tab: 0x18118
-  __TEXT.__const: 0x12d3a
-  __TEXT.__cstring: 0x125c8
-  __TEXT.__oslogstring: 0x167d
-  __TEXT.__objc_methname: 0x61a8
+524.120.7.0.0
+  __TEXT.__text: 0x1b2194
+  __TEXT.__auth_stubs: 0x2020
+  __TEXT.__objc_stubs: 0x5760
+  __TEXT.__objc_methlist: 0x31bc
+  __TEXT.__gcc_except_tab: 0x18394
+  __TEXT.__const: 0x12d9a
+  __TEXT.__cstring: 0x12b18
+  __TEXT.__oslogstring: 0x1770
+  __TEXT.__objc_methname: 0x631b
   __TEXT.__objc_classname: 0x669
   __TEXT.__objc_methtype: 0x2105
   __TEXT.__ustring: 0x13c

   __TEXT.__swift5_typeref: 0x58
   __TEXT.__swift5_fieldmd: 0x10
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0xc5e0
+  __TEXT.__unwind_info: 0xc688
   __TEXT.__eh_frame: 0xf0
-  __DATA_CONST.__auth_got: 0xff0
-  __DATA_CONST.__got: 0x4d0
+  __DATA_CONST.__auth_got: 0x1028
+  __DATA_CONST.__got: 0x530
   __DATA_CONST.__auth_ptr: 0x40
-  __DATA_CONST.__const: 0x33250
-  __DATA_CONST.__cfstring: 0x3ba0
+  __DATA_CONST.__const: 0x33490
+  __DATA_CONST.__cfstring: 0x40e0
   __DATA_CONST.__objc_classlist: 0x238
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x40

   __DATA_CONST.__objc_intobj: 0x18
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA.__objc_const: 0x4f48
-  __DATA.__objc_selrefs: 0x19a0
+  __DATA.__objc_selrefs: 0x1a00
   __DATA.__objc_ivar: 0x26c
   __DATA.__objc_data: 0x16b0
-  __DATA.__data: 0xc90
-  __DATA.__bss: 0x150
+  __DATA.__data: 0xc98
+  __DATA.__bss: 0x170
   __DATA.__common: 0x19
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/local/lib/libcurl.4.dylib
-  UUID: 746FDE77-F84E-3E71-B9FC-FA570F57DE04
-  Functions: 10086
-  Symbols:   742
-  CStrings:  3904
+  UUID: FC5DDC9C-88ED-31D5-994A-76A5B27731E0
+  Functions: 10120
+  Symbols:   771
+  CStrings:  4012
 
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
+ _do_saks_url_request
+ _do_wkms_url_request
+ _dprintf
+ _frk_generate_device_identity_certificates
+ _frk_generate_identity_certificates
+ _frk_set_device_identity_certificates
+ _frk_shipping_private_key_url_from_metadata
+ _frk_unwrap_wrapped_key_dictionary
+ _frk_unwrapped_encryption_key_for_metadata
+ _frk_wkms_host_url_from_metadata
+ _frk_wrapped_key_dictionary_for_metadata
+ _kSecAttrAccessControl
+ _kSecAttrAccessibleAfterFirstUnlockThisDeviceOnly
+ _kSecAttrIsPermanent
+ _kSecAttrKeySizeInBits
+ _kSecAttrKeyType
+ _kSecAttrKeyTypeECSECPrimeRandom
+ _kSecOidCommonName
+ _kSecOidCountryName
+ _kSecOidOrganization
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
+ "-o"
+ "/AppleInternal/Library/BuildRoots/4~CM2rugAu7nh_PGBnvg1cENuCKnOrHaIQ865F3n4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.5.Internal.sdk/usr/local/include/boost/algorithm/hex.hpp"
+ "/AppleInternal/Library/BuildRoots/4~CM2rugAu7nh_PGBnvg1cENuCKnOrHaIQ865F3n4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.5.Internal.sdk/usr/local/include/boost/uuid/detail/sha1.hpp"
+ "/AppleInternal/Library/BuildRoots/4~CM2rugAu7nh_PGBnvg1cENuCKnOrHaIQ865F3n4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.5.Internal.sdk/usr/local/include/boost/uuid/string_generator.hpp"
+ "524.120.7"
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
- "524.120.3"
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
