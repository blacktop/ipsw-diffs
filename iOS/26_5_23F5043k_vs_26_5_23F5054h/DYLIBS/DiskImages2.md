## DiskImages2

> `/System/Library/PrivateFrameworks/DiskImages2.framework/DiskImages2`

```diff

-524.120.3.0.0
-  __TEXT.__text: 0x1c40b0
-  __TEXT.__auth_stubs: 0x2220
-  __TEXT.__objc_methlist: 0x38ec
+524.120.7.0.0
+  __TEXT.__text: 0x1c6b60
+  __TEXT.__auth_stubs: 0x2290
+  __TEXT.__objc_methlist: 0x3914
   __TEXT.__const: 0x12dea
-  __TEXT.__gcc_except_tab: 0x187d4
-  __TEXT.__cstring: 0x12128
-  __TEXT.__oslogstring: 0x18d2
+  __TEXT.__gcc_except_tab: 0x189f8
+  __TEXT.__cstring: 0x12678
+  __TEXT.__oslogstring: 0x19c5
   __TEXT.__ustring: 0x13c
   __TEXT.__constg_swiftt: 0x60
   __TEXT.__swift5_typeref: 0x58
   __TEXT.__swift5_fieldmd: 0x10
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0xcf50
+  __TEXT.__unwind_info: 0xcfa8
   __TEXT.__eh_frame: 0xf0
   __TEXT.__objc_classname: 0x6c9
-  __TEXT.__objc_methname: 0x721b
+  __TEXT.__objc_methname: 0x7379
   __TEXT.__objc_methtype: 0x2465
-  __TEXT.__objc_stubs: 0x6260
-  __DATA_CONST.__got: 0x5d0
+  __TEXT.__objc_stubs: 0x63c0
+  __DATA_CONST.__got: 0x628
   __DATA_CONST.__const: 0xfb0
   __DATA_CONST.__objc_classlist: 0x278
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1d70
+  __DATA_CONST.__objc_selrefs: 0x1dc8
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x1f0
   __DATA_CONST.__objc_arraydata: 0xb8
-  __AUTH_CONST.__auth_got: 0x1128
-  __AUTH_CONST.__const: 0x34da0
-  __AUTH_CONST.__cfstring: 0x4500
+  __AUTH_CONST.__auth_got: 0x1160
+  __AUTH_CONST.__const: 0x34dc0
+  __AUTH_CONST.__cfstring: 0x4a20
   __AUTH_CONST.__objc_const: 0x5a40
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__objc_arrayobj: 0x30

   __AUTH.__objc_data: 0x1890
   __AUTH.__data: 0x68
   __DATA.__objc_ivar: 0x2f4
-  __DATA.__data: 0xb10
+  __DATA.__data: 0xb18
   __DATA.__common: 0x19
-  __DATA.__bss: 0x160
+  __DATA.__bss: 0x180
   __DATA_DIRTY.__objc_data: 0xa0
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/local/lib/libcurl.4.dylib
-  UUID: 669BE60E-B3BE-3EB0-83F5-07DB837C012F
-  Functions: 10755
-  Symbols:   30879
-  CStrings:  4296
+  UUID: B3154EB5-8F62-3069-9A7E-77DBF03F8850
+  Functions: 10773
+  Symbols:   30953
+  CStrings:  4401
 
Symbols:
+ +[DIKeyRetriever WKMSKeyWithAuthData:destKey:destKeySize:error:]
+ +[DIKeyRetriever WKMSShippingKeyWithURL:metadata:error:]
+ +[DIKeyRetriever ensureDeviceIdentityWithError:]
+ +[DIKeyRetriever ensureDeviceIdentityWithError:].cold.1
+ +[DIKeyRetriever newOIDCTokenForHost:error:]
+ _MGCopyAnswer
+ _NSUnderlyingErrorKey
+ _OBJC_CLASS_$_NSURLConnection
+ _SecAccessControlCreateWithFlags
+ _SecCertificateCopyData
+ _SecGenerateSelfSignedCertificate
+ _SecKeyCreateRandomKey
+ __ZN6di_log10logger_bufINS_11log_printerILm106EEEE4syncEv
+ __ZN6di_log10logger_bufINS_11log_printerILm106EEEE5_syncEv
+ __ZN6di_log10logger_bufINS_11log_printerILm106EEEE6xsputnEPKcl
+ __ZN6di_log10logger_bufINS_11log_printerILm106EEEE8overflowEi
+ __ZN6di_log10logger_bufINS_11log_printerILm106EEEEC2ERKS2_
+ __ZN6di_log10logger_bufINS_11log_printerILm106EEEED0Ev
+ __ZN6di_log10logger_bufINS_11log_printerILm106EEEED1Ev
+ __ZN6di_log10logger_bufINS_11log_printerILm106EEEED2Ev
+ __ZN6di_log10logger_bufINS_11log_printerILm120EEEE4syncEv
+ __ZN6di_log10logger_bufINS_11log_printerILm120EEEE5_syncEv
+ __ZN6di_log10logger_bufINS_11log_printerILm120EEEE6xsputnEPKcl
+ __ZN6di_log10logger_bufINS_11log_printerILm120EEEE8overflowEi
+ __ZN6di_log10logger_bufINS_11log_printerILm120EEEEC2ERKS2_
+ __ZN6di_log10logger_bufINS_11log_printerILm120EEEED0Ev
+ __ZN6di_log10logger_bufINS_11log_printerILm120EEEED1Ev
+ __ZN6di_log10logger_bufINS_11log_printerILm120EEEED2Ev
+ __ZN6di_log10logger_bufINS_11log_printerILm127EEEE4syncEv
+ __ZN6di_log10logger_bufINS_11log_printerILm127EEEE5_syncEv
+ __ZN6di_log10logger_bufINS_11log_printerILm127EEEE6xsputnEPKcl
+ __ZN6di_log10logger_bufINS_11log_printerILm127EEEE8overflowEi
+ __ZN6di_log10logger_bufINS_11log_printerILm127EEEEC2ERKS2_
+ __ZN6di_log10logger_bufINS_11log_printerILm127EEEED0Ev
+ __ZN6di_log10logger_bufINS_11log_printerILm127EEEED1Ev
+ __ZN6di_log10logger_bufINS_11log_printerILm127EEEED2Ev
+ __ZN6di_log6loggerINS_11log_printerILm106EEEEC1ERKS2_
+ __ZN6di_log6loggerINS_11log_printerILm106EEEED0Ev
+ __ZN6di_log6loggerINS_11log_printerILm106EEEED1Ev
+ __ZN6di_log6loggerINS_11log_printerILm120EEEEC1ERKS2_
+ __ZN6di_log6loggerINS_11log_printerILm120EEEED0Ev
+ __ZN6di_log6loggerINS_11log_printerILm120EEEED1Ev
+ __ZN6di_log6loggerINS_11log_printerILm127EEEEC1ERKS2_
+ __ZN6di_log6loggerINS_11log_printerILm127EEEED0Ev
+ __ZN6di_log6loggerINS_11log_printerILm127EEEED1Ev
+ __ZN9AEAHelper12key_params_t7emplaceINS_6wkms_tEJRKN10AEAwrapper8AuthDataEEEEvNSt3__115in_place_type_tIT_EEDpOT0_
+ __ZNK6di_log11log_printerILm106EE3logERKNSt3__112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEE
+ __ZNK6di_log11log_printerILm120EE3logERKNSt3__112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEE
+ __ZNK6di_log11log_printerILm127EE3logERKNSt3__112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEE
+ __ZTCN6di_log6loggerINS_11log_printerILm106EEEEE360_NSt3__113basic_ostreamIcNS3_11char_traitsIcEEEE
+ __ZTCN6di_log6loggerINS_11log_printerILm120EEEEE360_NSt3__113basic_ostreamIcNS3_11char_traitsIcEEEE
+ __ZTCN6di_log6loggerINS_11log_printerILm127EEEEE360_NSt3__113basic_ostreamIcNS3_11char_traitsIcEEEE
+ __ZTIN6di_log10logger_bufINS_11log_printerILm106EEEEE
+ __ZTIN6di_log10logger_bufINS_11log_printerILm120EEEEE
+ __ZTIN6di_log10logger_bufINS_11log_printerILm127EEEEE
+ __ZTIN6di_log6loggerINS_11log_printerILm106EEEEE
+ __ZTIN6di_log6loggerINS_11log_printerILm120EEEEE
+ __ZTIN6di_log6loggerINS_11log_printerILm127EEEEE
+ __ZTSN6di_log10logger_bufINS_11log_printerILm106EEEEE
+ __ZTSN6di_log10logger_bufINS_11log_printerILm120EEEEE
+ __ZTSN6di_log10logger_bufINS_11log_printerILm127EEEEE
+ __ZTSN6di_log6loggerINS_11log_printerILm106EEEEE
+ __ZTSN6di_log6loggerINS_11log_printerILm120EEEEE
+ __ZTSN6di_log6loggerINS_11log_printerILm127EEEEE
+ __ZTTN6di_log6loggerINS_11log_printerILm106EEEEE
+ __ZTTN6di_log6loggerINS_11log_printerILm120EEEEE
+ __ZTTN6di_log6loggerINS_11log_printerILm127EEEEE
+ __ZTVN6di_log10logger_bufINS_11log_printerILm106EEEEE
+ __ZTVN6di_log10logger_bufINS_11log_printerILm120EEEEE
+ __ZTVN6di_log10logger_bufINS_11log_printerILm127EEEEE
+ __ZTVN6di_log6loggerINS_11log_printerILm106EEEEE
+ __ZTVN6di_log6loggerINS_11log_printerILm120EEEEE
+ __ZTVN6di_log6loggerINS_11log_printerILm127EEEEE
+ __ZThn360_N6di_log6loggerINS_11log_printerILm106EEEED0Ev
+ __ZThn360_N6di_log6loggerINS_11log_printerILm106EEEED1Ev
+ __ZThn360_N6di_log6loggerINS_11log_printerILm120EEEED0Ev
+ __ZThn360_N6di_log6loggerINS_11log_printerILm120EEEED1Ev
+ __ZThn360_N6di_log6loggerINS_11log_printerILm127EEEED0Ev
+ __ZThn360_N6di_log6loggerINS_11log_printerILm127EEEED1Ev
+ __ZTv0_n24_N6di_log6loggerINS_11log_printerILm106EEEED0Ev
+ __ZTv0_n24_N6di_log6loggerINS_11log_printerILm106EEEED1Ev
+ __ZTv0_n24_N6di_log6loggerINS_11log_printerILm120EEEED0Ev
+ __ZTv0_n24_N6di_log6loggerINS_11log_printerILm120EEEED1Ev
+ __ZTv0_n24_N6di_log6loggerINS_11log_printerILm127EEEED0Ev
+ __ZTv0_n24_N6di_log6loggerINS_11log_printerILm127EEEED1Ev
+ __ZZ48+[DIKeyRetriever ensureDeviceIdentityWithError:]E10setupError
+ __ZZ48+[DIKeyRetriever ensureDeviceIdentityWithError:]E7success
+ __ZZ48+[DIKeyRetriever ensureDeviceIdentityWithError:]E9onceToken
+ ___48+[DIKeyRetriever ensureDeviceIdentityWithError:]_block_invoke
+ ___assert_rtn
+ _create_json_url_request
+ _do_saks_url_request
+ _do_wkms_url_request
+ _dprintf
+ _fetch_json_url_response
+ _frk_generate_device_identity_certificates
+ _frk_generate_identity_certificates
+ _frk_set_device_identity_certificates
+ _frk_set_device_identity_certificates.cold.1
+ _frk_set_device_identity_certificates.cold.2
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
+ _objc_msgSend$URLByAppendingPathComponent:isDirectory:
+ _objc_msgSend$WKMSKeyWithAuthData:destKey:destKeySize:error:
+ _objc_msgSend$WKMSShippingKeyWithURL:metadata:error:
+ _objc_msgSend$base64EncodedStringWithOptions:
+ _objc_msgSend$containsString:
+ _objc_msgSend$ensureDeviceIdentityWithError:
+ _objc_msgSend$initWithURL:cachePolicy:timeoutInterval:
+ _objc_msgSend$localizedStringForStatusCode:
+ _objc_msgSend$newOIDCTokenForHost:error:
+ _objc_msgSend$sendSynchronousRequest:returningResponse:error:
+ _objc_msgSend$setCachePolicy:
+ _objc_msgSend$whitespaceAndNewlineCharacterSet
+ _sDevicePrivateKey
+ _sIdentityCertificates
- +[DIKeyRetriever WKMSKeyWithURL:authData:destKey:destKeySize:error:]
- __ZN6di_log10logger_bufINS_11log_printerILm108EEEE4syncEv
- __ZN6di_log10logger_bufINS_11log_printerILm108EEEE5_syncEv
- __ZN6di_log10logger_bufINS_11log_printerILm108EEEE6xsputnEPKcl
- __ZN6di_log10logger_bufINS_11log_printerILm108EEEE8overflowEi
- __ZN6di_log10logger_bufINS_11log_printerILm108EEEEC2ERKS2_
- __ZN6di_log10logger_bufINS_11log_printerILm108EEEED0Ev
- __ZN6di_log10logger_bufINS_11log_printerILm108EEEED1Ev
- __ZN6di_log10logger_bufINS_11log_printerILm108EEEED2Ev
- __ZN6di_log10logger_bufINS_11log_printerILm115EEEE4syncEv
- __ZN6di_log10logger_bufINS_11log_printerILm115EEEE5_syncEv
- __ZN6di_log10logger_bufINS_11log_printerILm115EEEE6xsputnEPKcl
- __ZN6di_log10logger_bufINS_11log_printerILm115EEEE8overflowEi
- __ZN6di_log10logger_bufINS_11log_printerILm115EEEEC2ERKS2_
- __ZN6di_log10logger_bufINS_11log_printerILm115EEEED0Ev
- __ZN6di_log10logger_bufINS_11log_printerILm115EEEED1Ev
- __ZN6di_log10logger_bufINS_11log_printerILm115EEEED2Ev
- __ZN6di_log10logger_bufINS_11log_printerILm129EEEE4syncEv
- __ZN6di_log10logger_bufINS_11log_printerILm129EEEE5_syncEv
- __ZN6di_log10logger_bufINS_11log_printerILm129EEEE6xsputnEPKcl
- __ZN6di_log10logger_bufINS_11log_printerILm129EEEE8overflowEi
- __ZN6di_log10logger_bufINS_11log_printerILm129EEEEC2ERKS2_
- __ZN6di_log10logger_bufINS_11log_printerILm129EEEED0Ev
- __ZN6di_log10logger_bufINS_11log_printerILm129EEEED1Ev
- __ZN6di_log10logger_bufINS_11log_printerILm129EEEED2Ev
- __ZN6di_log6loggerINS_11log_printerILm108EEEEC1ERKS2_
- __ZN6di_log6loggerINS_11log_printerILm108EEEED0Ev
- __ZN6di_log6loggerINS_11log_printerILm108EEEED1Ev
- __ZN6di_log6loggerINS_11log_printerILm115EEEEC1ERKS2_
- __ZN6di_log6loggerINS_11log_printerILm115EEEED0Ev
- __ZN6di_log6loggerINS_11log_printerILm115EEEED1Ev
- __ZN6di_log6loggerINS_11log_printerILm129EEEEC1ERKS2_
- __ZN6di_log6loggerINS_11log_printerILm129EEEED0Ev
- __ZN6di_log6loggerINS_11log_printerILm129EEEED1Ev
- __ZN9AEAHelper12key_params_t7emplaceINS_6wkms_tEJRNSt3__112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEERKN10AEAwrapper8AuthDataEEEEvNS3_15in_place_type_tIT_EEDpOT0_
- __ZNK6di_log11log_printerILm108EE3logERKNSt3__112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEE
- __ZNK6di_log11log_printerILm115EE3logERKNSt3__112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEE
- __ZNK6di_log11log_printerILm129EE3logERKNSt3__112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEE
- __ZNSt3__18optionalIN9AEAHelper6wkms_tEE7emplaceB9nqe210106IJRNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEERKN10AEAwrapper8AuthDataEELi0EEERS2_DpOT_
- __ZTCN6di_log6loggerINS_11log_printerILm108EEEEE360_NSt3__113basic_ostreamIcNS3_11char_traitsIcEEEE
- __ZTCN6di_log6loggerINS_11log_printerILm115EEEEE360_NSt3__113basic_ostreamIcNS3_11char_traitsIcEEEE
- __ZTCN6di_log6loggerINS_11log_printerILm129EEEEE360_NSt3__113basic_ostreamIcNS3_11char_traitsIcEEEE
- __ZTIN6di_log10logger_bufINS_11log_printerILm108EEEEE
- __ZTIN6di_log10logger_bufINS_11log_printerILm115EEEEE
- __ZTIN6di_log10logger_bufINS_11log_printerILm129EEEEE
- __ZTIN6di_log6loggerINS_11log_printerILm108EEEEE
- __ZTIN6di_log6loggerINS_11log_printerILm115EEEEE
- __ZTIN6di_log6loggerINS_11log_printerILm129EEEEE
- __ZTSN6di_log10logger_bufINS_11log_printerILm108EEEEE
- __ZTSN6di_log10logger_bufINS_11log_printerILm115EEEEE
- __ZTSN6di_log10logger_bufINS_11log_printerILm129EEEEE
- __ZTSN6di_log6loggerINS_11log_printerILm108EEEEE
- __ZTSN6di_log6loggerINS_11log_printerILm115EEEEE
- __ZTSN6di_log6loggerINS_11log_printerILm129EEEEE
- __ZTTN6di_log6loggerINS_11log_printerILm108EEEEE
- __ZTTN6di_log6loggerINS_11log_printerILm115EEEEE
- __ZTTN6di_log6loggerINS_11log_printerILm129EEEEE
- __ZTVN6di_log10logger_bufINS_11log_printerILm108EEEEE
- __ZTVN6di_log10logger_bufINS_11log_printerILm115EEEEE
- __ZTVN6di_log10logger_bufINS_11log_printerILm129EEEEE
- __ZTVN6di_log6loggerINS_11log_printerILm108EEEEE
- __ZTVN6di_log6loggerINS_11log_printerILm115EEEEE
- __ZTVN6di_log6loggerINS_11log_printerILm129EEEEE
- __ZThn360_N6di_log6loggerINS_11log_printerILm108EEEED0Ev
- __ZThn360_N6di_log6loggerINS_11log_printerILm108EEEED1Ev
- __ZThn360_N6di_log6loggerINS_11log_printerILm115EEEED0Ev
- __ZThn360_N6di_log6loggerINS_11log_printerILm115EEEED1Ev
- __ZThn360_N6di_log6loggerINS_11log_printerILm129EEEED0Ev
- __ZThn360_N6di_log6loggerINS_11log_printerILm129EEEED1Ev
- __ZTv0_n24_N6di_log6loggerINS_11log_printerILm108EEEED0Ev
- __ZTv0_n24_N6di_log6loggerINS_11log_printerILm108EEEED1Ev
- __ZTv0_n24_N6di_log6loggerINS_11log_printerILm115EEEED0Ev
- __ZTv0_n24_N6di_log6loggerINS_11log_printerILm115EEEED1Ev
- __ZTv0_n24_N6di_log6loggerINS_11log_printerILm129EEEED0Ev
- __ZTv0_n24_N6di_log6loggerINS_11log_printerILm129EEEED1Ev
- _objc_msgSend$WKMSKeyWithURL:authData:destKey:destKeySize:error:
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
+ "diskimage_uio::details::diskimage_impl::diskimage_impl(iter_t, iter_t, uint32_t) [iter_t = boost::iterators::transform_iterator<(lambda at /Library/Caches/com.apple.xbs/739E7723-005E-40D0-A1BC-288B031015F8/TemporaryDirectory.aBtDD0/Sources/DiskImages2/libdiskimagesio/diskimage_uio.cpp:1713:29), const diskimage_uio::rref_capture<diskimage_uio::diskimage_open_params_pair> *>]"
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
+ "static diskimage_impl *diskimage_uio::details::diskimage_impl::create_diskimage_impl(iter_t, iter_t, uint32_t) [iter_t = boost::iterators::transform_iterator<(lambda at /Library/Caches/com.apple.xbs/739E7723-005E-40D0-A1BC-288B031015F8/TemporaryDirectory.aBtDD0/Sources/DiskImages2/libdiskimagesio/diskimage_uio.cpp:1713:29), const diskimage_uio::rref_capture<diskimage_uio::diskimage_open_params_pair> *>]"
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
- "diskimage_uio::details::diskimage_impl::diskimage_impl(iter_t, iter_t, uint32_t) [iter_t = boost::iterators::transform_iterator<(lambda at /Library/Caches/com.apple.xbs/9582C130-148B-4E00-9B23-52C8C2FDF55E/TemporaryDirectory.was1id/Sources/DiskImages2/libdiskimagesio/diskimage_uio.cpp:1713:29), const diskimage_uio::rref_capture<diskimage_uio::diskimage_open_params_pair> *>]"
- "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /Library/Caches/com.apple.xbs/9582C130-148B-4E00-9B23-52C8C2FDF55E/TemporaryDirectory.was1id/Sources/DiskImages2/app/backends/sg_vec.cpp:455:28)]"
- "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /Library/Caches/com.apple.xbs/9582C130-148B-4E00-9B23-52C8C2FDF55E/TemporaryDirectory.was1id/Sources/DiskImages2/app/disk_images/formats/asif.cpp:1963:32)]"
- "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /Library/Caches/com.apple.xbs/9582C130-148B-4E00-9B23-52C8C2FDF55E/TemporaryDirectory.was1id/Sources/DiskImages2/app/disk_images/formats/asif.cpp:1999:32)]"
- "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /Library/Caches/com.apple.xbs/9582C130-148B-4E00-9B23-52C8C2FDF55E/TemporaryDirectory.was1id/Sources/DiskImages2/app/disk_images/formats/plugin_async_di.cpp:370:34)]"
- "io_result_t details::for_each_sg_in_vec_internal(Fn &&, sg_vec_ref::iterator, sg_vec::iterator, size_t, bool) [Fn = (lambda at /Library/Caches/com.apple.xbs/9582C130-148B-4E00-9B23-52C8C2FDF55E/TemporaryDirectory.was1id/Sources/DiskImages2/app/disk_images/formats/plugin_async_di.cpp:450:45)]"
- "ssize_t transform(Fn &&, sg_vec_ref::iterator, const sg_vec_ref::iterator &, sg_vec_ref::iterator) [Fn = (lambda at /Library/Caches/com.apple.xbs/9582C130-148B-4E00-9B23-52C8C2FDF55E/TemporaryDirectory.was1id/Sources/DiskImages2/app/disk_images/io_breaker.cpp:76:13)]"
- "ssize_t transform(Fn &&, sg_vec_ref::iterator, const sg_vec_ref::iterator &, sg_vec_ref::iterator) [Fn = (lambda at /Library/Caches/com.apple.xbs/9582C130-148B-4E00-9B23-52C8C2FDF55E/TemporaryDirectory.was1id/Sources/DiskImages2/app/utils.cpp:179:13)]"
- "static diskimage_impl *diskimage_uio::details::diskimage_impl::create_diskimage_impl(iter_t, iter_t, uint32_t) [iter_t = boost::iterators::transform_iterator<(lambda at /Library/Caches/com.apple.xbs/9582C130-148B-4E00-9B23-52C8C2FDF55E/TemporaryDirectory.was1id/Sources/DiskImages2/libdiskimagesio/diskimage_uio.cpp:1713:29), const diskimage_uio::rref_capture<diskimage_uio::diskimage_open_params_pair> *>]"
- "void crypto::details::unset_futures_errors_reporter<boost::iterators::transform_iterator<(lambda at /Library/Caches/com.apple.xbs/9582C130-148B-4E00-9B23-52C8C2FDF55E/TemporaryDirectory.was1id/Sources/DiskImages2/app/crypto/crypto_format.cpp:713:35), std::__deque_iterator<crypto_format_backend::promise_io_t, crypto_format_backend::promise_io_t *, crypto_format_backend::promise_io_t &, crypto_format_backend::promise_io_t **, long>>>::report_errors(int) [It = boost::iterators::transform_iterator<(lambda at /Library/Caches/com.apple.xbs/9582C130-148B-4E00-9B23-52C8C2FDF55E/TemporaryDirectory.was1id/Sources/DiskImages2/app/crypto/crypto_format.cpp:713:35), std::__deque_iterator<crypto_format_backend::promise_io_t, crypto_format_backend::promise_io_t *, crypto_format_backend::promise_io_t &, crypto_format_backend::promise_io_t **, long>>]"
- "void crypto::details::unset_futures_errors_reporter<std::ranges::transform_view<std::ranges::ref_view<container_it<std::__deque_iterator<FileLocal::promise_io_t, FileLocal::promise_io_t *, FileLocal::promise_io_t &, FileLocal::promise_io_t **, long>>>, (lambda at /Library/Caches/com.apple.xbs/9582C130-148B-4E00-9B23-52C8C2FDF55E/TemporaryDirectory.was1id/Sources/DiskImages2/app/backends/file.cpp:755:24)>::__iterator<false>>::report_errors(int) [It = std::ranges::transform_view<std::ranges::ref_view<container_it<std::__deque_iterator<FileLocal::promise_io_t, FileLocal::promise_io_t *, FileLocal::promise_io_t &, FileLocal::promise_io_t **, long>>>, (lambda at /Library/Caches/com.apple.xbs/9582C130-148B-4E00-9B23-52C8C2FDF55E/TemporaryDirectory.was1id/Sources/DiskImages2/app/backends/file.cpp:755:24)>::__iterator<false>]"

```
