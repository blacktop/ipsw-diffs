## CFNetworkAgent

> `/System/Library/Frameworks/CFNetwork.framework/CFNetworkAgent`

```diff

-3826.500.131.0.0
-  __TEXT.__text: 0xbbdc
-  __TEXT.__auth_stubs: 0xec0
+3826.600.31.0.0
+  __TEXT.__text: 0x83e0
+  __TEXT.__auth_stubs: 0xc10
   __TEXT.__objc_stubs: 0x420
   __TEXT.__objc_methlist: 0x1f4
-  __TEXT.__const: 0xf8
-  __TEXT.__gcc_except_tab: 0x630
-  __TEXT.__cstring: 0xbd4
-  __TEXT.__oslogstring: 0xb99
+  __TEXT.__const: 0xd8
+  __TEXT.__gcc_except_tab: 0x45c
+  __TEXT.__oslogstring: 0x814
+  __TEXT.__cstring: 0x537
   __TEXT.__objc_classname: 0x56
   __TEXT.__objc_methname: 0x70a
   __TEXT.__objc_methtype: 0x4d8
-  __TEXT.__unwind_info: 0x3f8
-  __DATA_CONST.__auth_got: 0x770
-  __DATA_CONST.__got: 0x1a0
+  __TEXT.__unwind_info: 0x310
+  __DATA_CONST.__auth_got: 0x618
+  __DATA_CONST.__got: 0x160
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x788
-  __DATA_CONST.__cfstring: 0x700
+  __DATA_CONST.__const: 0x5d8
+  __DATA_CONST.__cfstring: 0x480
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA.__objc_ivar: 0x8
   __DATA.__objc_data: 0x50
   __DATA.__data: 0x120
-  __DATA.__bss: 0x70
+  __DATA.__bss: 0x40
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D606E60D-3625-3388-AD01-EC21551E1D6F
-  Functions: 186
-  Symbols:   300
-  CStrings:  354
+  UUID: D52469DF-857F-3A34-B7DD-D1992D301EB5
+  Functions: 134
+  Symbols:   248
+  CStrings:  269
 
Symbols:
+ _xpc_connection_cancel
- _CFArrayCreate
- _CFDataGetBytes
- _CFDictionaryAddValue
- _CFDictionaryCreateMutable
- _CFDictionaryGetCount
- _CFDictionaryGetKeysAndValues
- _CFEqual
- _CFHTTPMessageAppendBytes
- _CFHTTPMessageCopyBody
- _CFHTTPMessageCopySerializedMessage
- _CFHTTPMessageCreateEmpty
- _CFHTTPMessageCreateRequest
- _CFHTTPMessageIsHeaderComplete
- _CFHTTPMessageSetBody
- _CFHTTPMessageSetHeaderFieldValue
- _CFHostCreateWithName
- _CFReadStreamCopyError
- _CFReadStreamCopyProperty
- _CFReadStreamCreateForHTTPRequest
- _CFReadStreamSetDispatchQueue
- _CFReadStreamSetProperty
- _CFStreamCreatePairWithSocketToCFHost
- _CFStringAppend
- _CFStringCreateMutable
- _CFStringGetCString
- _CFStringGetDoubleValue
- _CFURLCreateWithString
- _CFWriteStreamClose
- _CFWriteStreamCopyError
- _CFWriteStreamOpen
- _CFWriteStreamSetClient
- _CFWriteStreamSetDispatchQueue
- _CFWriteStreamWrite
- _SCDynamicStoreCopyMultiple
- _SCDynamicStoreCreateWithOptions
- _SCDynamicStoreRemoveValue
- _SCDynamicStoreSetValue
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEPKc
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEaSERKS5_
- __ZNSt3__19to_stringEx
- ___cxa_pure_virtual
- ___stderrp
- __kCFStreamSSLShouldSetPeerID
- _bzero
- _dispatch_retain
- _fprintf
- _kCFBooleanFalse
- _kCFBooleanTrue
- _kCFHTTPVersion1_1
- _kCFStreamPropertyHTTPResponseHeader
- _kCFStreamPropertySSLSettings
- _kCFStreamSSLValidatesCertificateChain
- _malloc_type_malloc
CStrings:
+ "PAC unable to send xpc reply for id %{public}@, token %p"
- "%d"
- "%f"
- "."
- ".*"
- "/salt"
- "127.0.0.1"
- "<!DOCTYPE html PUBLIC \"-//IETF//DTD HTML 2.0//EN\">\r\n<HTML>\r\n   <HEAD>\r\n      <TITLE>\r\n         Pipeline Test Result \r\n      </TITLE>\r\n   </HEAD>\r\n<BODY>\r\n   <P>Pipeline Test Result Page 0.</P> \r\n</BODY>\r\n</HTML>\r\n\r\n"
- "<!DOCTYPE html PUBLIC \"-//IETF//DTD HTML 2.0//EN\">\r\n<HTML>\r\n   <HEAD>\r\n      <TITLE>\r\n         Pipeline Test Result \r\n      </TITLE>\r\n   </HEAD>\r\n<BODY>\r\n   <P>Pipeline Test Result Page 1.</P> \r\n</BODY>\r\n</HTML>\r\n\r\n"
- "<!DOCTYPE html PUBLIC \"-//IETF//DTD HTML 2.0//EN\">\r\n<HTML>\r\n   <HEAD>\r\n      <TITLE>\r\n         Pipeline Test Result \r\n      </TITLE>\r\n   </HEAD>\r\n<BODY>\r\n   <P>Pipeline Test Result Page 2.</P> \r\n</BODY>\r\n</HTML>\r\n\r\n"
- "<!DOCTYPE html PUBLIC \"-//IETF//DTD HTML 2.0//EN\">\r\n<HTML>\r\n   <HEAD>\r\n      <TITLE>\r\n         Pipeline Test Result \r\n      </TITLE>\r\n   </HEAD>\r\n<BODY>\r\n   <P>Pipeline Test Result Page 3.</P> \r\n</BODY>\r\n</HTML>\r\n\r\n"
- "Added key-value pair to SCDynamicStore <QueryType=%lld>: <Key=%@, Value=%@>"
- "Added lastPurgeTime k-v pair to SCDynamicStore <Key=%@, Value=%@>"
- "BaseQuery"
- "Body data to split has length 0. This should never happen."
- "CFERROR: {Domain:%s, Code:%ld}"
- "CFNETWORKAGENT_FALSESTART_RESOURCE"
- "CFNETWORKAGENT_FALSESTART_TIMEOUT"
- "CFNETWORKAGENT_HOST"
- "CFNETWORKAGENT_KEY_SPACE_ROOT"
- "CFNETWORKAGENT_PORT"
- "CFNETWORKAGENT_TTL"
- "CFNETWORK_AGENT_STORE"
- "Connection"
- "Content-Length"
- "Did NOT Remove %@ from dynamic store:"
- "Dynamic store is stale, purging"
- "FALSE"
- "Failed to add key-value pair to SCDynamicStore <QueryType=%lld>: <Key=%@, Value=%@>"
- "Failed to add lastPurgeTime k-v pair to SCDynamicStore <Key=%@, Value=%@>"
- "Failed to write after kCFStreamEventCanAcceptBytes <%@, %ld>"
- "False Start request timer fired"
- "FalseStartQuery"
- "GET"
- "HEAD"
- "HTTPPipelining"
- "Host"
- "Keep-Alive"
- "NULL ERROR"
- "PENDING"
- "PipelineQuery"
- "Purge k-v pair not found in dynamic store, creating and adding one."
- "Purging dynamic store"
- "Received <signature=%s> query type=%d> that is already outstanding. Ignoring."
- "Received legacy query type=%lld sig=%s"
- "Received legacy query with no signature (type=%d)"
- "Removed %@ from dynamic store:"
- "Starting Probe for Query<%p>"
- "TLSFalseStart"
- "TRUE"
- "Unable to create query for <signature=%s, query type=%d>. Ignoring."
- "Unable to get keys from dynamic store for removal!"
- "_"
- "_kCFStreamSSLUseFalseStartNoCompatibilityCheck"
- "com.apple.CFNetwork.netcompat"
- "com.apple.CFNetwork.netcompat.lastpurge"
- "com.apple.cfnetwork.cfnetworkagent.legacy"
- "com\\.apple\\.CFNetwork\\.netcompat"
- "configuration.apple.com"
- "guzzoni.apple.com"
- "http://%@:%d/configurations/pep/pipeline/pipeline%d.html"
- "https://"
- "kCFNetworkAgentXPCMessageTypeFalseStart"
- "kCFNetworkAgentXPCMessageTypePipeline"
- "kCFNetworkAgentXPCMessageTypePurgeDynamicStore"
- "sig"
- "v16@?0^v8"

```
