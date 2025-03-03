## libIPTelephony.dylib

> `/System/Library/PrivateFrameworks/IPTelephony.framework/Support/libIPTelephony.dylib`

```diff

-2315.0.0.0.0
-  __TEXT.__text: 0x4ab268
-  __TEXT.__auth_stubs: 0x2a80
-  __TEXT.__init_offsets: 0x11c
-  __TEXT.__objc_methlist: 0x328
-  __TEXT.__gcc_except_tab: 0x49354
-  __TEXT.__const: 0x1913b
-  __TEXT.__cstring: 0x3c92d
+2375.2.1.0.0
+  __TEXT.__text: 0x4b2818
+  __TEXT.__auth_stubs: 0x2d30
+  __TEXT.__init_offsets: 0x120
+  __TEXT.__objc_methlist: 0x6a8
+  __TEXT.__const: 0x19513
+  __TEXT.__cstring: 0x3da21
+  __TEXT.__gcc_except_tab: 0x4a84c
   __TEXT.__oslogstring: 0xa4
-  __TEXT.__unwind_info: 0x17f28
+  __TEXT.__unwind_info: 0x181b0
   __TEXT.__objc_classname: 0x110
-  __TEXT.__objc_methname: 0x18df
-  __TEXT.__objc_methtype: 0x1117
-  __TEXT.__objc_stubs: 0x1840
-  __DATA_CONST.__got: 0x418
-  __DATA_CONST.__const: 0x3588
+  __TEXT.__objc_methname: 0x192d
+  __TEXT.__objc_methtype: 0x10c7
+  __TEXT.__objc_stubs: 0x18a0
+  __DATA_CONST.__got: 0x458
+  __DATA_CONST.__const: 0x3600
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6f8
+  __DATA_CONST.__objc_selrefs: 0x868
   __DATA_CONST.__objc_superrefs: 0x30
-  __AUTH_CONST.__auth_got: 0x1550
+  __AUTH_CONST.__auth_got: 0x16a8
   __AUTH_CONST.__auth_ptr: 0x18
-  __AUTH_CONST.__const: 0x37240
+  __AUTH_CONST.__const: 0x37b78
   __AUTH_CONST.__cfstring: 0x2600
-  __AUTH_CONST.__objc_const: 0x1198
+  __AUTH_CONST.__objc_const: 0xb08
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH.__objc_data: 0x140
   __DATA.__objc_ivar: 0x5c
   __DATA.__data: 0x370
-  __DATA.__common: 0x10c
+  __DATA.__common: 0x120
   __DATA.__bss: 0x14
   __DATA_DIRTY.__objc_data: 0xa0
-  __DATA_DIRTY.__data: 0x110
-  __DATA_DIRTY.__common: 0xb170
-  __DATA_DIRTY.__bss: 0xe58
+  __DATA_DIRTY.__data: 0x128
+  __DATA_DIRTY.__common: 0xb280
+  __DATA_DIRTY.__bss: 0xe70
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreLocation.framework/CoreLocation
+  - /System/Library/Frameworks/DeviceCheck.framework/DeviceCheck
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/Network.framework/Network

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprotobuf-lite.dylib
   - /usr/lib/libxml2.2.dylib
-  Functions: 15742
-  Symbols:   17610
-  CStrings:  9153
+  Functions: 15852
+  Symbols:   17826
+  CStrings:  9296
 
Symbols:
+ _CC_SHA256
+ _CFReadStreamSetDispatchQueue
+ _CFWriteStreamSetDispatchQueue
+ _OBJC_CLASS_$_DCAppAttestServicePriv
+ _SecCertificateCopyKey
+ _SecCertificateCopySHA256Digest
+ _SecKeyCopyAttributes
+ _SecKeyCopyExternalRepresentation
+ _SecTrustCopyCertificateChain
+ _SecTrustEvaluateWithError
+ __ZN14IMSCallManager24trackMTOnlyLazuliSessionERKNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEENS0_10shared_ptrI13LazuliSessionEE
+ __ZN3ctu4hex0Eh
+ __ZNSt3__117bad_function_callD1Ev
+ __ZTINSt3__117bad_function_callE
+ __ZTVNSt3__117bad_function_callE
+ __nw_content_context_default_stream
+ _dispatch_activate
+ _dispatch_data_create
+ _dispatch_queue_attr_make_initially_inactive
+ _dispatch_queue_create_with_target$V2
+ _dispatch_set_qos_class_floor
+ _kSecAttrKeyTypeECSECPrimeRandom
+ _kSecCMSHashingAlgorithmSHA256
+ _kSecCMSSignHashAlgorithm
+ _nw_connection_copy_description
+ _nw_connection_copy_endpoint
+ _nw_connection_create
+ _nw_connection_force_cancel
+ _nw_connection_read_buffer
+ _nw_connection_send
+ _nw_endpoint_copy_address_string
+ _nw_endpoint_get_address
+ _nw_ip_options_set_dscp_value
+ _nw_listener_copy_local_endpoint
+ _nw_listener_get_port
+ _nw_parameters_copy_default_protocol_stack
+ _nw_parameters_create_legacy_tcp_socket
+ _nw_parameters_create_secure_tcp
+ _nw_parameters_set_indefinite
+ _nw_parameters_set_server_mode
+ _nw_parameters_set_source_application_by_bundle_id
+ _nw_parameters_set_traffic_class
+ _nw_protocol_stack_copy_internet_protocol
+ _nw_tcp_options_set_connection_timeout
+ _nw_tcp_options_set_enable_keepalive
+ _nw_tcp_options_set_keepalive_count
+ _nw_tcp_options_set_keepalive_idle_time
+ _nw_tcp_options_set_keepalive_interval
+ _nw_tcp_options_set_maximum_segment_size
+ _nw_tls_copy_sec_protocol_options
+ _sec_identity_create
+ _sec_protocol_options_set_local_identity
+ _sec_protocol_options_set_min_tls_protocol_version
+ _sec_protocol_options_set_tls_server_name
+ _sec_protocol_options_set_verify_block
+ _sec_trust_copy_ref
+ _strerror
- _CFReadStreamScheduleWithRunLoop
- _CFReadStreamUnscheduleFromRunLoop
- _CFWriteStreamScheduleWithRunLoop
- _CFWriteStreamUnscheduleFromRunLoop
- __ZNKSt9exception4whatEv
- __ZTISt9exception
- _objc_retain_x25
CStrings:
+ "    Proxy-List "
+ " != my seqCnt="
+ " UseLibnetcoreForRcs="
+ " forceTls="
+ " gone for terminate request reason "
+ " hex="
+ " interface="
+ " isLazuliConnection="
+ " isLazuliEnabled="
+ " length="
+ " mustSignDigest="
+ " pinned CA hash is "
+ " pinnedCertificates = "
+ " prevState="
+ " privateKey="
+ " remote address="
+ " useNw="
+ " with privateKey="
+ ", sendRequest..."
+ ", signedSignature="
+ "----- Group-Leave Lazuli Sessions ("
+ "----- Store-And-Forward Lazuli Sessions ("
+ ". Next ims counter will be "
+ ". Next lazuli counter will be "
+ ". Next thumper counter will be "
+ "/AppleInternal/Library/BuildRoots/e3acf947-f363-11ef-bc4c-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/include/ARI/ari_sdk_msg.h"
+ "/AppleInternal/Library/BuildRoots/e3acf947-f363-11ef-bc4c-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/include/google/protobuf/repeated_field.h"
+ "0Y0\x13\x06\a*\x86H\xce=\x02\x01\x06\b*\x86H\xce=\x03\x01\a\x03B"
+ "401 Invalid Opaque Value"
+ ": Triggering lazuli registration termination"
+ ": callback is old. no op"
+ "@48@0:8{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=(__rep={__short=[23c][0C]b7b1}{__long=*Qb63b1})}}16^{ImsNetworkPathDelegate=^^?}40"
+ "@76@0:8{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=(__rep={__short=[23c][0C]b7b1}{__long=*Qb63b1})}}16d40d48B56{weak_ptr<ImsKeepAliveDelegate>=^{ImsKeepAliveDelegate}^{__shared_weak_count}}60"
+ "AlwaysCheckRegistrationRefreshTimerAfterSystemClockChange"
+ "Attestation service timeout"
+ "AttestationPrivateKey"
+ "AttestationServiceHelper is no longer existing: no op"
+ "AttestationServiceHelper starts with seqCnt="
+ "AttestationServiceHelperSigningTimer"
+ "AttestationServiceHelperSigningTimer expired. continueSendRequest with no opaque. seqCnt="
+ "B68@?0{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=(__rep={__short=[23c][0C]b7b1}{__long=*Qb63b1})}}8^v32^v40^v48B56r^v60"
+ "Cannot handle disconnect due to null socket"
+ "Certificate chain is null"
+ "Connection is not ready to receive data"
+ "Connection read error: "
+ "Contact header is missing.  Patching in To header"
+ "Contact is not a phone number.  Patching in To header"
+ "CoreTelephony"
+ "Did not set bundle UUID"
+ "Did not set required interface"
+ "Failed to create TCP nw_parameters"
+ "Failed to create TLS nw_parameters"
+ "Failed to create nw_connection"
+ "Failed to create nw_connection due to invalid parameters"
+ "Failed to create nw_endpoint for listener"
+ "Failed to encode certificate digest in base64"
+ "Failed to initialize nw_listener with null localAddress"
+ "Handle incoming connection connectionId="
+ "Handling read stream callback with event '"
+ "Handling write stream callback with event '"
+ "ImsTcpNw received data connectionId="
+ "ImsTcpNw: no delegate to handle, closing myself"
+ "ImsTcpNw: remote end closed connection"
+ "ImsTcpNw::connect (async) outgoing connection id="
+ "ImsTcpNw::sendOverSocket "
+ "ImsTcpNw::writeToNw "
+ "ImsTcpSocket require interface "
+ "Initialize SipTcpTransport for stack "
+ "Initialize outgoing SipTcpConnection for stack "
+ "Initialized lazuli Group template SDP ("
+ "Intermediate CA is not available"
+ "Intermediate CA is null"
+ "Intermediate CA public key SHA-256 digest "
+ "Invalid lazuli 1:1 SDP template"
+ "Invalid lazuli Group SDP template"
+ "IsSignedSipEnabled"
+ "Lazuli attestation private key: "
+ "Lazuli pinned certificate digests: "
+ "MT-only session already established "
+ "NW listener already initialized"
+ "NW listener ready on port "
+ "NW listener timed out"
+ "PinnedCertificateDigests"
+ "Provisioning expired"
+ "Removed stack tag "
+ "Require interface "
+ "Resetting decoder state"
+ "SIP INVITE response "
+ "SIP MESSAGE response "
+ "SIP OPTIONS response "
+ "SecTrust could not be evaluated"
+ "Set DSCP to "
+ "Set xcap queue for read stream"
+ "Set xcap queue for write stream"
+ "Signing blob of length="
+ "Signing digest failed with error = "
+ "SipRegistrationClient is no longer existing: no op"
+ "SipRegistrationClient(2) is no longer existing: no op"
+ "SipSignedDigest"
+ "SipStack is no longer existing: no op"
+ "SipStack(2) is no longer existing: no op"
+ "Skipping to next proxy for lazuli stack due to termination before we reached Active state."
+ "TCP KeepAlive time = "
+ "TCP NW "
+ "TLS NW "
+ "TLS handshake done for "
+ "Terminating store-and-forward session "
+ "Tracking MT-only lazuli session "
+ "Transport layer is null "
+ "Unresponsive peer detection interval = "
+ "Unresponsive peer detection probe count = "
+ "UseLibnetcoreForRcs"
+ "Will NOT notify SD of connection termination due to Disabled|Reprovision registration mode"
+ "attestation service is null"
+ "base64EncodedStringWithOptions:"
+ "com.apple.ipTelephony.xcap.queue"
+ "continueSendRequest(): _request is gone. no op"
+ "continueSendRequest(): callback seqCnt="
+ "continueSendRequest(): cancel AttestationServiceHelperSigningTimer, if it is still running"
+ "continueSendRequest(): seqCnt="
+ "continueSendRequest(): set opaque="
+ "decode failure on body"
+ "decode failure on headers"
+ "decode failure on start line"
+ "empty"
+ "err="
+ "failed connectionId="
+ "got back seqCnt="
+ "initialized on "
+ "net.listenw"
+ "net.tcpnw"
+ "net.tlsnw"
+ "new incoming connection Id="
+ "not empty"
+ "not notifying delegate of duplicate or suppressed state change"
+ "nw_connection failed with error="
+ "nw_connection_send failed uuid="
+ "nw_connection_send success uuid="
+ "preparing connectionId="
+ "queueing "
+ "received Forbidden responses from all proxies. Trigger RCS reprovisioning."
+ "reporting active port"
+ "reporting active port "
+ "reporting default port "
+ "reporting default port << "
+ "sendChallengeToDelegate isLazuliEnabled="
+ "sharedService"
+ "sign:withKey:completionHandler:"
+ "signedData is "
+ "skipping incoming connection id="
+ "start line empty"
+ "systemClockDidChange, device not registered: keep checking registration refresh timer "
+ "v16@?0^{nw_error=}8"
+ "v16@?0^{nw_protocol_options=}8"
+ "v20@?0Q8i16"
+ "v24@?0@\"NSData\"8@\"NSError\"16"
+ "v32@?0^{sec_protocol_metadata=}8^{sec_trust=}16@?<v@?B>24"
+ "v88@?0{ImsResult=^^?^{ImsResultDomain}i^{ImsStringOutStream}^{ImsResult}^{ImsResultItem}{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=(__rep={__short=[23c][0C]b7b1}{__long=*Qb63b1})}}}8r^v80"
+ "waiting connectionId="
+ "{basic_string<char, std::char_traits<char>, std::allocator<char>>=\"__r_\"{__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=\"__value_\"(__rep=\"__s\"{__short=\"__data_\"[23c]\"__padding_\"[0C]\"__size_\"b7\"__is_long_\"b1}\"__l\"{__long=\"__data_\"*\"__size_\"Q\"__cap_\"b63\"__is_long_\"b1})}}"
+ "{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=(__rep={__short=[23c][0C]b7b1}{__long=*Qb63b1})}}16@0:8"
- "/AppleInternal/Library/BuildRoots/c71e92b8-bf80-11ef-98d7-36218cb420d5/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/include/ARI/ari_sdk_msg.h"
- "/AppleInternal/Library/BuildRoots/c71e92b8-bf80-11ef-98d7-36218cb420d5/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.3.Internal.sdk/usr/local/include/google/protobuf/repeated_field.h"
- "@48@0:8{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>={__rep=(?={__short=[23c][0C]b7b1}{__long=*Qb63b1}{__raw=[3Q]})}}}16^{ImsNetworkPathDelegate=^^?}40"
- "@76@0:8{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>={__rep=(?={__short=[23c][0C]b7b1}{__long=*Qb63b1}{__raw=[3Q]})}}}16d40d48B56{weak_ptr<ImsKeepAliveDelegate>=^{ImsKeepAliveDelegate}^{__shared_weak_count}}60"
- "B68@?0{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>={__rep=(?={__short=[23c][0C]b7b1}{__long=*Qb63b1}{__raw=[3Q]})}}}8^v32^v40^v48B56r^v60"
- "Contact header is missing in SipLazuliManager::handleOptionsError"
- "Lazuli registration refresh"
- "MsrpTransportTcp::initConnection()"
- "MsrpTransportTcp::initListener()"
- "Will NOT notify SD of connection termination due to Disabled registration mode"
- "botplatform"
- "handleReadStreamCallback: Event - "
- "handleWriteStreamCallback: Event - "
- "initialized on local port "
- "not notifying delegate of duplicate or surpressed state change"
- "v88@?0{ImsResult=^^?^{ImsResultDomain}i^{ImsStringOutStream}^{ImsResult}^{ImsResultItem}{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>={__rep=(?={__short=[23c][0C]b7b1}{__long=*Qb63b1}{__raw=[3Q]})}}}}8r^v80"
- "{basic_string<char, std::char_traits<char>, std::allocator<char>>=\"__r_\"{__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=\"__value_\"{__rep=\"\"(?=\"__s\"{__short=\"__data_\"[23c]\"__padding_\"[0C]\"__size_\"b7\"__is_long_\"b1}\"__l\"{__long=\"__data_\"*\"__size_\"Q\"__cap_\"b63\"__is_long_\"b1}\"__r\"{__raw=\"__words\"[3Q]})}}}"
- "{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>={__rep=(?={__short=[23c][0C]b7b1}{__long=*Qb63b1}{__raw=[3Q]})}}}16@0:8"

```
