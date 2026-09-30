## Network

> `/System/Library/Frameworks/Network.framework/Network`

```diff

-4277.40.40.0.1
-  __TEXT.__text: 0xc5110c
+4277.40.63.0.0
+  __TEXT.__text: 0xc533ec
   __TEXT.__auth_stubs: 0x5c20
   __TEXT.__delay_stubs: 0x370
   __TEXT.__delay_helper: 0xb90
   __TEXT.__init_offsets: 0x5a8
-  __TEXT.__objc_methlist: 0x788c
+  __TEXT.__objc_methlist: 0x78a4
   __TEXT.__const: 0xcf250
-  __TEXT.__cstring: 0x5c795
+  __TEXT.__cstring: 0x5c8a2
   __TEXT.__swift5_typeref: 0x36c0
   __TEXT.__swift5_capture: 0x19d0
   __TEXT.__swift5_reflstr: 0x2408

   __TEXT.__swift5_proto: 0x6ec
   __TEXT.__swift5_types: 0x440
   __TEXT.__swift5_protos: 0x58
-  __TEXT.__oslogstring: 0x11e983
-  __TEXT.__gcc_except_tab: 0x8a8e0
-  __TEXT.__unwind_info: 0x180e0
+  __TEXT.__oslogstring: 0x11efc6
+  __TEXT.__gcc_except_tab: 0x8a934
+  __TEXT.__unwind_info: 0x180f8
   __TEXT.__eh_frame: 0x620c
   __TEXT.__objc_classname: 0x2307
-  __TEXT.__objc_methname: 0x13d70
-  __TEXT.__objc_methtype: 0x9004
-  __TEXT.__objc_stubs: 0x9a60
+  __TEXT.__objc_methname: 0x13d9a
+  __TEXT.__objc_methtype: 0x9010
+  __TEXT.__objc_stubs: 0x9a80
   __DATA_CONST.__got: 0xda0
-  __DATA_CONST.__const: 0x12620
+  __DATA_CONST.__const: 0x12640
   __DATA_CONST.__objc_classlist: 0x960
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x4d0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3498
+  __DATA_CONST.__objc_selrefs: 0x34a8
   __DATA_CONST.__objc_protorefs: 0xf8
   __DATA_CONST.__objc_superrefs: 0x6b8
   __AUTH_CONST.__auth_got: 0x2ec8
   __AUTH_CONST.__auth_ptr: 0xe98
-  __AUTH_CONST.__const: 0xc798
+  __AUTH_CONST.__const: 0xc7b8
   __AUTH_CONST.__cfstring: 0x80a0
   __AUTH_CONST.__objc_const: 0x26a58
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH.__objc_data: 0x38e0
   __AUTH.__data: 0x4960
   __DATA.__objc_ivar: 0x260c
-  __DATA.__data: 0x62f8
+  __DATA.__data: 0x6328
   __DATA.__crash_info: 0x40
   __DATA.__bss: 0x107f0
   __DATA.__common: 0x2790

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 21149
-  Symbols:   15211
-  CStrings:  32604
+  Functions: 21156
+  Symbols:   15224
+  CStrings:  32638
 
Symbols:
+ _nw_setting_enable_quic_denominator_old8
+ _nw_setting_disable_quic_old8
+ _SecTrustCopyPolicies
+ _nw_setting_disable_quic_race_old8
+ _SecPolicySetSSLHostname
+ _nw_setting_enable_quic_numerator_old8
+ _nw_setting_enable_accurate_ecn_numerator_old1
+ _nw_setting_enable_accurate_ecn_denominator_old1
+ _SecPolicySetATSPinning
- _SecPolicyCreateSSL
- _SecTrustSetPolicies
- _SecPolicyCreateSSLWithATSPinning
CStrings:
+ "%!{(MISSING)public}s responseCompletionHandler should not be nil for %!@(MISSING) %!@(MISSING), dumping backtrace:%!{(MISSING)public}s"
+ "%!{(MISSING)public}s responseCompletionHandler should not be nil for %!@(MISSING) %!@(MISSING), no backtrace"
+ "4277.40.63"
+ "%!{(MISSING)public}s responseCompletionHandler should not be nil for %!@(MISSING) %!@(MISSING), backtrace limit exceeded"
+ "disable_quic9"
+ "%!{(MISSING)public}s SecPolicySetSSLHostname failed, no backtrace"
+ "enable_accurate_ecn_denominator2"
+ "%!{(MISSING)public}s SecTrustCopyPolicies failed %!d(MISSING), backtrace limit exceeded"
+ "%!{(MISSING)public}s SecTrust has an unexpected number of policies %!l(MISSING)u, dumping backtrace:%!{(MISSING)public}s"
+ "isRegisteredInternal"
+ "%!{(MISSING)public}s SecPolicySetATSPinning failed, backtrace limit exceeded"
+ "%!{(MISSING)public}s Bleaching partial checksum bits: is_partial=%!d(MISSING); start=%!u(MISSING); stuff=%!u(MISSING)"
+ "%!{(MISSING)public}s responseCompletionHandler should not be nil for %!@(MISSING) %!@(MISSING)"
+ "%!{(MISSING)public}s SecTrustCopyPolicies failed %!d(MISSING), dumping backtrace:%!{(MISSING)public}s"
+ "enable_quic_numerator9"
+ "-[NWURLSessionTask loaderDidReceiveServerTrustChallenge:secProtocolMetadata:completionHandler:]"
+ "%!{(MISSING)public}s SecPolicySetATSPinning failed, dumping backtrace:%!{(MISSING)public}s"
+ "%!{(MISSING)public}s __nw_frame_set_internet_checksum failed: is_partial=%!d(MISSING); start=%!u(MISSING); stuff=%!u(MISSING) %!{(MISSING)darwin.errno}d"
+ "%!{(MISSING)public}s SecTrustCopyPolicies failed %!d(MISSING)"
+ "%!{(MISSING)public}s SecPolicySetSSLHostname failed, backtrace limit exceeded"
+ "enable_accurate_ecn_numerator2"
+ "disable_quic_race9"
+ "%!{(MISSING)public}s SecTrust has an unexpected number of policies %!l(MISSING)u, no backtrace"
+ "-[NWURLLoaderHTTP readResponse]"
+ "%!{(MISSING)public}s SecPolicySetATSPinning failed, no backtrace"
+ "I24@0:8^i16"
+ "%!{(MISSING)public}s SecPolicySetATSPinning failed"
+ "%!{(MISSING)public}s SecTrust has an unexpected number of policies %!l(MISSING)u, backtrace limit exceeded"
+ "%!{(MISSING)public}s SecTrust has an unexpected number of policies %!l(MISSING)u"
+ "enable_quic_denominator9"
+ "%!{(MISSING)public}s __nw_frame_get_internet_checksum failed %!{(MISSING)darwin.errno}d"
+ "%!{(MISSING)public}s SecPolicySetSSLHostname failed"
+ "%!{(MISSING)public}s SecTrustCopyPolicies failed %!d(MISSING), no backtrace"
+ "%!{(MISSING)public}s SecPolicySetSSLHostname failed, dumping backtrace:%!{(MISSING)public}s"
+ "tokenCountWithError:"
- "4277.40.40.0.1"

```
