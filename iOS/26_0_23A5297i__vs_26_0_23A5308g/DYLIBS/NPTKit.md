## NPTKit

> `/System/Library/PrivateFrameworks/NPTKit.framework/NPTKit`

```diff

-186.0.0.0.0
-  __TEXT.__text: 0x4d3c8
-  __TEXT.__auth_stubs: 0x1190
-  __TEXT.__objc_methlist: 0x4c3c
+190.0.0.0.0
+  __TEXT.__text: 0x4d5a0
+  __TEXT.__auth_stubs: 0x11b0
+  __TEXT.__objc_methlist: 0x4c4c
   __TEXT.__const: 0x528
-  __TEXT.__cstring: 0x4238
+  __TEXT.__cstring: 0x4078
   __TEXT.__gcc_except_tab: 0xad4
   __TEXT.__oslogstring: 0x1065
   __TEXT.__swift5_typeref: 0x64f

   __TEXT.__swift_as_ret: 0x54
   __TEXT.__swift5_assocty: 0x18
   __TEXT.__swift5_proto: 0xc
-  __TEXT.__unwind_info: 0xd30
+  __TEXT.__unwind_info: 0xd38
   __TEXT.__eh_frame: 0x898
   __TEXT.__objc_classname: 0x3b1
-  __TEXT.__objc_methname: 0xdfbe
+  __TEXT.__objc_methname: 0xdfed
   __TEXT.__objc_methtype: 0x1967
-  __TEXT.__objc_stubs: 0x8620
+  __TEXT.__objc_stubs: 0x8680
   __DATA_CONST.__got: 0x390
   __DATA_CONST.__const: 0xa68
   __DATA_CONST.__objc_classlist: 0xf8
   __DATA_CONST.__objc_catlist: 0x70
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x35b8
+  __DATA_CONST.__objc_selrefs: 0x35d0
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x80
   __DATA_CONST.__objc_arraydata: 0x2c8
-  __AUTH_CONST.__auth_got: 0x8d8
-  __AUTH_CONST.__const: 0xe88
-  __AUTH_CONST.__cfstring: 0x6140
+  __AUTH_CONST.__auth_got: 0x8e8
+  __AUTH_CONST.__const: 0xef8
+  __AUTH_CONST.__cfstring: 0x6240
   __AUTH_CONST.__objc_const: 0xc4b8
   __AUTH_CONST.__objc_intobj: 0x2e8
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0xc0
-  __AUTH.__objc_data: 0x140
+  __AUTH.__objc_data: 0xf0
   __AUTH.__data: 0x258
   __DATA.__objc_ivar: 0x740
   __DATA.__data: 0x718
   __DATA.__bss: 0x180
   __DATA.__common: 0x30
-  __DATA_DIRTY.__objc_data: 0x780
+  __DATA_DIRTY.__objc_data: 0x7d0
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreTelephony.framework/CoreTelephony

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 90E09376-BB09-3C0F-9E3F-3DF2A0F5CFE8
-  Functions: 2028
-  Symbols:   5899
-  CStrings:  4514
+  UUID: 5DD74122-2B4D-34D9-B471-CBF18ED144AD
+  Functions: 2008
+  Symbols:   5858
+  CStrings:  4504
 
Symbols:
+ -[SimplePing packetDidFailToSendDelegate:error:]
+ ___swift_memcpy0_1
+ _close
+ _objc_msgSend$asn
+ _objc_msgSend$asnName
+ _objc_msgSend$packetDidFailToSendDelegate:error:
+ _objc_release_x1
- -[SimplePing dealloc].cold.1
- -[SimplePing dealloc].cold.2
- -[SimplePing didFailWithError:].cold.1
- -[SimplePing pingPacketWithType:payload:requiresChecksum:].cold.1
- -[SimplePing readData].cold.1
- -[SimplePing readData].cold.2
- -[SimplePing sendPingWithData:].cold.1
- -[SimplePing sendPingWithData:].cold.2
- -[SimplePing sendPingWithData:].cold.3
- -[SimplePing sendPingWithData:].cold.4
- -[SimplePing startWithHostAddress].cold.2
- -[SimplePing startWithHostAddress].cold.3
- -[SimplePing startWithHostAddress].cold.4
- -[SimplePing startWithHostAddress].cold.5
- _HostResolveCallback.cold.1
- _HostResolveCallback.cold.2
- _HostResolveCallback.cold.3
- _SocketReadCallback.cold.1
- _SocketReadCallback.cold.2
- _SocketReadCallback.cold.3
- _SocketReadCallback.cold.4
- _SocketReadCallback.cold.5
- ___19-[SimplePing start]_block_invoke.cold.1
- ___19-[SimplePing start]_block_invoke.cold.2
- ___19-[SimplePing start]_block_invoke.cold.3
CStrings:
+ "Failed to allocate buffer"
+ "Failed to create CFHost"
+ "Failed to create Socket"
+ "Failed to create packet"
+ "Failed to read packet data"
+ "Unknown error occurred"
+ "asn"
+ "asnName"
+ "hostAddress is nil"
+ "hostAddressFamily is not compatible"
+ "packetDidFailToSendDelegate:error:"
- "-[SimplePing dealloc]"
- "-[SimplePing didFailWithError:]"
- "-[SimplePing pingPacketWithType:payload:requiresChecksum:]"
- "-[SimplePing readData]"
- "-[SimplePing sendPingWithData:]"
- "-[SimplePing start]_block_invoke"
- "HostResolveCallback"
- "SocketReadCallback"
- "[obj isKindOfClass:[SimplePing class]]"
- "[payload length] == 56"
- "address == nil"
- "buffer != NULL"
- "data == nil"
- "error != nil"
- "fd == -1"
- "packet != nil"
- "payload != nil"
- "rls != NULL"
- "s == obj.socket"
- "self->_host == NULL"
- "self->_socket == NULL"
- "self.host != NULL"
- "self.host == NULL"
- "self.hostAddress != nil"
- "self.hostAddress == nil"
- "self.socket != NULL"
- "theHost == obj.host"
- "type == kCFSocketReadCallBack"
- "typeInfo == kCFHostAddresses"

```
