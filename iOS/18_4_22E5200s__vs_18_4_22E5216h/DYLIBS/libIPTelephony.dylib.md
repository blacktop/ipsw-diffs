## libIPTelephony.dylib

> `/System/Library/PrivateFrameworks/IPTelephony.framework/Support/libIPTelephony.dylib`

```diff

-2372.2.0.0.0
-  __TEXT.__text: 0x4a9f94
-  __TEXT.__auth_stubs: 0x2bf0
-  __TEXT.__init_offsets: 0x11c
+2375.2.1.0.0
+  __TEXT.__text: 0x4b2818
+  __TEXT.__auth_stubs: 0x2d30
+  __TEXT.__init_offsets: 0x120
   __TEXT.__objc_methlist: 0x6a8
-  __TEXT.__const: 0x19383
-  __TEXT.__cstring: 0x3d096
-  __TEXT.__gcc_except_tab: 0x49fe0
+  __TEXT.__const: 0x19513
+  __TEXT.__cstring: 0x3da21
+  __TEXT.__gcc_except_tab: 0x4a84c
   __TEXT.__oslogstring: 0xa4
-  __TEXT.__unwind_info: 0x18000
+  __TEXT.__unwind_info: 0x181b0
   __TEXT.__objc_classname: 0x110
   __TEXT.__objc_methname: 0x192d
   __TEXT.__objc_methtype: 0x10c7
   __TEXT.__objc_stubs: 0x18a0
   __DATA_CONST.__got: 0x458
-  __DATA_CONST.__const: 0x35a0
+  __DATA_CONST.__const: 0x3600
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x868
   __DATA_CONST.__objc_superrefs: 0x30
-  __AUTH_CONST.__auth_got: 0x1608
+  __AUTH_CONST.__auth_got: 0x16a8
   __AUTH_CONST.__auth_ptr: 0x18
-  __AUTH_CONST.__const: 0x371d0
+  __AUTH_CONST.__const: 0x37b78
   __AUTH_CONST.__cfstring: 0x2600
   __AUTH_CONST.__objc_const: 0xb08
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH.__objc_data: 0x140
   __DATA.__objc_ivar: 0x5c
   __DATA.__data: 0x370
-  __DATA.__common: 0x110
+  __DATA.__common: 0x120
   __DATA.__bss: 0x14
   __DATA_DIRTY.__objc_data: 0xa0
   __DATA_DIRTY.__data: 0x128
   __DATA_DIRTY.__common: 0xb280
-  __DATA_DIRTY.__bss: 0xe58
+  __DATA_DIRTY.__bss: 0xe70
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreLocation.framework/CoreLocation

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprotobuf-lite.dylib
   - /usr/lib/libxml2.2.dylib
-  Functions: 15774
-  Symbols:   17723
-  CStrings:  9221
+  Functions: 15852
+  Symbols:   17826
+  CStrings:  9296
 
Symbols:
+ _CFReadStreamSetDispatchQueue
+ _CFWriteStreamSetDispatchQueue
+ __ZN3ctu4hex0Eh
+ __ZN6AriSdk33ARI_IBINetDcUacAccessCheckReq_SDKC1Ev
+ __ZN6AriSdk33ARI_IBINetDcUacAccessCheckReq_SDKD1Ev
+ __ZN6AriSdk35ARI_IBINetDcUacAccessCheckRspCb_SDK6unpackEv
+ __ZN6AriSdk35ARI_IBINetDcUacAccessCheckRspCb_SDKC1EPKhj
+ __ZN6AriSdk35ARI_IBINetDcUacAccessCheckRspCb_SDKD1Ev
+ __ZN6AriSdk35ARI_IBINetDcUacBarringInfoIndCb_SDK6unpackEv
+ __ZN6AriSdk35ARI_IBINetDcUacBarringInfoIndCb_SDKC1EPKhj
+ __ZN6AriSdk35ARI_IBINetDcUacBarringInfoIndCb_SDKD1Ev
+ __ZN6AriSdk42ARI_IBINetDcImsSignallingStatusInfoReq_SDKC1Ev
+ __ZN6AriSdk42ARI_IBINetDcImsSignallingStatusInfoReq_SDKD1Ev
+ __ZN6AriSdk44ARI_IBINetDcImsSignallingStatusInfoRspcb_SDK6unpackEv
+ __ZN6AriSdk44ARI_IBINetDcImsSignallingStatusInfoRspcb_SDKC1EPKhj
+ __ZN6AriSdk44ARI_IBINetDcImsSignallingStatusInfoRspcb_SDKD1Ev
+ _dispatch_activate
+ _dispatch_queue_attr_make_initially_inactive
+ _dispatch_queue_create_with_target$V2
+ _dispatch_set_qos_class_floor
+ _nw_ip_options_set_dscp_value
+ _nw_listener_copy_local_endpoint
+ _nw_listener_get_port
+ _nw_parameters_copy_default_protocol_stack
+ _nw_protocol_stack_copy_internet_protocol
- _CFReadStreamScheduleWithRunLoop
- _CFReadStreamUnscheduleFromRunLoop
- _CFWriteStreamScheduleWithRunLoop
- _CFWriteStreamUnscheduleFromRunLoop
- _nw_connection_copy_connected_local_endpoint
CStrings:
+ "    Proxy-List "
+ "    no-op: mask is none"
+ "    notifyDelegates for curretly barred services="
+ "    notifyDelegates for newly alleviated services="
+ "    old barred services="
+ " != my seqCnt="
+ " allowed"
+ " barred"
+ " hex="
+ ", mask="
+ ", sendRequest..."
+ ", signedSignature="
+ ". Next ims counter will be "
+ ". Next lazuli counter will be "
+ ". Next thumper counter will be "
+ "/AppleInternal/Library/BuildRoots/e3acf947-f363-11ef-bc4c-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/include/ARI/ari_sdk_msg.h"
+ "/AppleInternal/Library/BuildRoots/e3acf947-f363-11ef-bc4c-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/include/google/protobuf/repeated_field.h"
+ "401 Invalid Opaque Value"
+ ": UAC check returned an unknown error"
+ ": callback is old. no op"
+ ": services "
+ "Attestation service timeout"
+ "AttestationServiceHelper is no longer existing: no op"
+ "AttestationServiceHelper starts with seqCnt="
+ "AttestationServiceHelperSigningTimer"
+ "AttestationServiceHelperSigningTimer expired. continueSendRequest with no opaque. seqCnt="
+ "Cannot handle disconnect due to null socket"
+ "Handling read stream callback with event '"
+ "Handling write stream callback with event '"
+ "INT: updated secondsUntilNextRetry to "
+ "INTSipLogger: "
+ "ImsTcpSocket require interface "
+ "Initialized lazuli Group template SDP ("
+ "Invalid lazuli 1:1 SDP template"
+ "Invalid lazuli Group SDP template"
+ "NW listener ready on port "
+ "NW listener timed out"
+ "Removed stack tag "
+ "Resetting decoder state"
+ "Sending registration signaling status START for instance "
+ "Sending registration signaling status STOP for instance "
+ "Set DSCP to "
+ "Set xcap queue for read stream"
+ "Set xcap queue for write stream"
+ "SipRegistrationClient is no longer existing: no op"
+ "SipRegistrationClient(2) is no longer existing: no op"
+ "SipStack is no longer existing: no op"
+ "SipStack(2) is no longer existing: no op"
+ "Skip Reporting call status "
+ "Skipping to next proxy for lazuli stack due to termination before we reached Active state."
+ "Strange: how could stack be null? startCall() failed."
+ "WiFi to Cellular handover: will send SESSION_STARTED event to BB"
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
+ "failed to extract UAC indication params"
+ "failed to extract UAC response params"
+ "got back seqCnt="
+ "ibi.nas.handleUacAccessCheckResp"
+ "int.nas"
+ "int.nas.uac"
+ "no NAS client object"
+ "not empty"
+ "received UacAccessCheckResp for instance "
+ "received UacBarringInd for instance "
+ "reporting active port"
+ "reporting active port "
+ "reporting default port "
+ "reporting default port << "
+ "sending call status "
+ "signedData is "
+ "start line empty"
+ "updateBarredServices: instance="
- "/AppleInternal/Library/BuildRoots/80a4978a-ebfc-11ef-ae29-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/include/ARI/ari_sdk_msg.h"
- "/AppleInternal/Library/BuildRoots/80a4978a-ebfc-11ef-ae29-3e0a6b9ba2ed/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.4.Internal.sdk/usr/local/include/google/protobuf/repeated_field.h"
- "Signing digest timed out with result = "
- "handleReadStreamCallback: Event - "
- "handleWriteStreamCallback: Event - "

```
