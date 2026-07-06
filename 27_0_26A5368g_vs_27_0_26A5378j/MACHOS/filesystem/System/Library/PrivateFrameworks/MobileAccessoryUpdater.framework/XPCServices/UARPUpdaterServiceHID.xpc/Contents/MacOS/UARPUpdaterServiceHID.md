## UARPUpdaterServiceHID

> `/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/UARPUpdaterServiceHID.xpc/Contents/MacOS/UARPUpdaterServiceHID`

```diff

-  __TEXT.__text: 0x1e860
+  __TEXT.__text: 0x1e9cc
   __TEXT.__auth_stubs: 0x6e0
   __TEXT.__objc_stubs: 0x28a0
   __TEXT.__objc_methlist: 0x11a8
   __TEXT.__gcc_except_tab: 0xd8
   __TEXT.__objc_methname: 0x3718
   __TEXT.__objc_classname: 0x199
-  __TEXT.__cstring: 0x20c6
+  __TEXT.__cstring: 0x2083
   __TEXT.__objc_methtype: 0xbad
   __TEXT.__oslogstring: 0x1272
   __TEXT.__const: 0xc0
-  __TEXT.__unwind_info: 0x6e8
+  __TEXT.__unwind_info: 0x6f0
   __DATA_CONST.__const: 0x930
   __DATA_CONST.__cfstring: 0x5e0
   __DATA_CONST.__objc_classlist: 0x40

   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__auth_got: 0x380
-  __DATA_CONST.__got: 0x160
+  __DATA_CONST.__got: 0x168
   __DATA.__objc_const: 0x1c08
   __DATA.__objc_selrefs: 0xd50
   __DATA.__objc_ivar: 0xd8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 798
-  Symbols:   552
-  CStrings:  1074
+  Functions: 802
+  Symbols:   556
+  CStrings:  1073
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA_CONST.__objc_intobj : content changed
~ __DATA.__objc_const : content changed
~ __DATA.__objc_selrefs : content changed
~ __DATA.__data : content changed
Symbols:
+ _uarpDownstreamEndpointProcessReachableMessage
+ _uarpPlatformDownstreamEndpointReachable2
+ _uarpProcessTLV2
+ _uarpProtocolSupportsDownstreamReachableTLVs
+ _uarpSendDownstreamEndpointReachable2
- _uarpTransmitBufferUpstream
CStrings:
+ "%s: ESPRESSO: Message <type=0x%04x, id=0x%04x> Length too big ! expected <%u>, got <%u>"
- "%s: ESPRESSO:Bonus Message <type=0x%04x, length=x0x%04x, id=0x%04x>"
- "%s: ESPRESSO:Message <type=0x%04x, id=0x%04x> Length too big ! expected <%u>, got <%u>"

```
