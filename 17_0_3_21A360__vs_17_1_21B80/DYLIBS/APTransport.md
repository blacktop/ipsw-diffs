## APTransport

> `/System/Library/PrivateFrameworks/APTransport.framework/APTransport`

```diff

-710.79.1.1.1
-  __TEXT.__text: 0x7df54
-  __TEXT.__auth_stubs: 0x2ae0
+745.13.4.0.0
+  __TEXT.__text: 0x7ec10
+  __TEXT.__auth_stubs: 0x2b30
   __TEXT.__objc_methlist: 0x7a4
-  __TEXT.__cstring: 0x23f6f
+  __TEXT.__cstring: 0x2439a
   __TEXT.__const: 0x204
   __TEXT.__gcc_except_tab: 0x2cc
   __TEXT.__oslogstring: 0x16e
-  __TEXT.__unwind_info: 0x13d8
+  __TEXT.__unwind_info: 0x13e8
   __TEXT.__objc_classname: 0xfa
-  __TEXT.__objc_methname: 0x2b87
+  __TEXT.__objc_methname: 0x2ba1
   __TEXT.__objc_methtype: 0xab2
-  __TEXT.__objc_stubs: 0x2c60
-  __DATA_CONST.__got: 0x200
-  __DATA_CONST.__const: 0x2b48
+  __TEXT.__objc_stubs: 0x2c80
+  __DATA_CONST.__got: 0x210
+  __DATA_CONST.__const: 0x2b88
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x12a8
-  __DATA_CONST.__objc_selrefs: 0xbd0
+  __DATA_CONST.__objc_selrefs: 0xbd8
   __DATA_CONST.__objc_arraydata: 0x10
   __AUTH_CONST.__const: 0x29c0
   __AUTH_CONST.__cfstring: 0x4f60
   __AUTH_CONST.__objc_const: 0x1f8
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_intobj: 0x30
-  __AUTH_CONST.__auth_got: 0x1580
+  __AUTH_CONST.__auth_got: 0x15a8
   __AUTH.__data: 0xb8
   __AUTH.__objc_data: 0xa0
   __DATA.__objc_classrefs: 0x178

   - /usr/lib/libIOReport.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1646
-  Symbols:   5229
-  CStrings:  4123
+  Functions: 1650
+  Symbols:   5247
+  CStrings:  4141
 
Symbols:
+ _APBrokeredReceiverGetDeviceID
+ _APBrokeredReceiverGetTypeID.initOnce
+ _APBrokeredReceiverGetTypeID.typeID
+ _CFHash
+ _CFSetSetValue
+ _HTTPClientSetConnectionLogging
+ _HTTPClientSetLogging
+ __APBrokerHTTPSendRequestToURL
+ __APBrokeredReceiverClassRegister
+ __APBrokeredReceiverEqual
+ __APBrokeredReceiverHash
+ ____APBrokerHTTPSendRequestToURL_block_invoke
+ ___block_descriptor_48_e10_v16?0r^v8l
+ ___block_descriptor_64_e5_v8?0l
+ ___block_descriptor_tmp.112
+ ___block_descriptor_tmp.114
+ ___block_descriptor_tmp.120
+ ___block_descriptor_tmp.122
+ ___block_descriptor_tmp.127
+ ___block_descriptor_tmp.132
+ ___block_descriptor_tmp.136
+ ___block_descriptor_tmp.148
+ ___block_descriptor_tmp.163
+ ___block_descriptor_tmp.166
+ ___block_descriptor_tmp.58
+ ___block_descriptor_tmp.96
+ ___block_descriptor_tmp.99
+ ___browser_flushAllBrokerResults_block_invoke
+ _gLogCategory_AsyncCnx
+ _gLogCategory_HTTPClientCore
+ _nw_parameters_prohibit_interface_type
+ _objc_msgSend$setAllowsCellularAccess:
- _APBrokeredReceiverIsSameReceiver
- __APBrokeredReceiverGetTypeID
- ____APBrokerHTTPSendRequestToAddress_block_invoke
- ___block_descriptor_tmp.106
- ___block_descriptor_tmp.108
- ___block_descriptor_tmp.111
- ___block_descriptor_tmp.119
- ___block_descriptor_tmp.121
- ___block_descriptor_tmp.125
- ___block_descriptor_tmp.130
- ___block_descriptor_tmp.135
- ___block_descriptor_tmp.138
- ___block_descriptor_tmp.147
- ___block_descriptor_tmp.162
- ___block_descriptor_tmp.165
- ___block_descriptor_tmp.36
- ___block_descriptor_tmp.39
- ___block_descriptor_tmp.57
- ___block_descriptor_tmp.60
- ___block_descriptor_tmp.62
- ___block_descriptor_tmp.95
- ___block_literal_global.34
- _gAPBrokeredReceiverInitOnce
- _gAPBrokeredReceiverTypeID
CStrings:
+ "%@%?{end}:%hu"
+ "%s://%@%@"
+ "745.13.4"
+ "Bonjour"
+ "Boolean _APBrokerShouldConnectToBonjourServiceName(CFDictionaryRef)"
+ "DNS"
+ "Failed to create brokerFeatures with string %'@ (%#m)\n"
+ "HTTPClient for %@ connecting to %@:%d with CID 0x%08X\n"
+ "Invalid"
+ "OSStatus _APBrokerHTTPResolve(void *, CFStringRef, APBrokerHTTPResolveHandler)"
+ "OSStatus browser_flushAllBrokerResults(APBrowserRef)"
+ "OSStatus browser_flushAllBrokerResults(APBrowserRef)_block_invoke"
+ "OSStatus httpconnection_handleEvent(HTTPConnectionRef, HTTPMessageRef, void *)"
+ "OSStatus stream_createConnectionState(APTransportConnectionRef, APTransportConnectionEventCallback, FigTransportStreamRef, APTransportStreamDirection, APTransportStreamConnectionStateRef *)"
+ "[%{ptr}] APTransportStream with name %@ holds %s connection [%{ptr}].\n"
+ "[%{ptr}] Brokered receiver [%{ptr}] add or update event%?{end} deviceID=%@\n"
+ "[%{ptr}] Brokered receiver [%{ptr}] remove event%?{end} deviceID=%@\n"
+ "[%{ptr}] Event message received from %##a, Header %zu bytes, Body %zu bytes, ID 0x%04X\n"
+ "[%{ptr}] Event message reply sent to %##a, HTTP Status: %d, Body %zu bytes, ID 0x%04X\n"
+ "[%{ptr}] Flush all %d broker results\n"
+ "[%{ptr}] Flushing brokeredReceiver [%{ptr}]%?{end} deviceID=%@\n"
+ "[%{ptr}] Prohibiting cellular interfaces"
+ "[%{ptr}] Sending %s %s to %@ (%s). URI: %@\n"
+ "[%{ptr}] Starting %s %s to %@"
+ "[%{ptr}] Starting HTTP %s to destination=%@ (%s) URL=%@ with options: %@\n"
+ "[%{ptr}] Starting resolve of %@"
+ "_APBrokerHTTPSendRequestToURL"
+ "browser_flushAllBrokerResults_block_invoke"
+ "hp"
+ "setAllowsCellularAccess:"
+ "void APBrokerHTTPSendRequest(void *, CFTypeRef, CFStringRef, APBrokerHTTPRequestDestinationType, int, CFStringRef, CFDictionaryRef, CFTypeRef, CFDictionaryRef, APBrokerHTTPResponseHandler)"
+ "void _APBrokerHTTPSendRequestToURL(APBrokerHTTPRequestData *, CFStringRef)"
- "710.79.1"
- "HTTPClient for %@ connected to %@:%d with CID 0x%08X\n"
- "OSStatus _APBrokerHTTPResolve(void *, const char *, APBrokerHTTPResolveHandler)"
- "[%{ptr}] Brokered receiver add or update event\n"
- "[%{ptr}] Brokered receiver remove event\n"
- "[%{ptr}] Sending %s %s to %s. URI: %@\n"
- "[%{ptr}] Starting %s %s to %@(%##a)%@"
- "[%{ptr}] Starting HTTP %s to %@ with options: %@\n"
- "[%{ptr}] Starting resolve of %s"
- "[%{ptr}] URL is %@\n"
- "_APBrokerHTTPSendRequestToAddress"
- "com.apple.CoreUtils"
- "void APBrokerHTTPSendRequest(void *, CFTypeRef, const char *, int, CFStringRef, CFDictionaryRef, CFTypeRef, CFDictionaryRef, APBrokerHTTPResponseHandler)"
- "void _APBrokerHTTPSendRequestToAddress(APBrokerHTTPRequestData *)"

```
