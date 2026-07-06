## UARPUpdaterServiceHID

> `/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/UARPUpdaterServiceHID.xpc/UARPUpdaterServiceHID`

```diff

-  __TEXT.__text: 0x1cef4
+  __TEXT.__text: 0x1d064
   __TEXT.__auth_stubs: 0x820
   __TEXT.__objc_stubs: 0x2820
   __TEXT.__objc_methlist: 0x11a8
   __TEXT.__gcc_except_tab: 0xd8
   __TEXT.__objc_methname: 0x36db
   __TEXT.__objc_classname: 0x199
-  __TEXT.__cstring: 0x1fc3
+  __TEXT.__cstring: 0x1f80
   __TEXT.__objc_methtype: 0xbad
   __TEXT.__oslogstring: 0x112f
   __TEXT.__const: 0xb0
-  __TEXT.__unwind_info: 0x790
+  __TEXT.__unwind_info: 0x7a0
   __DATA_CONST.__const: 0x8b8
   __DATA_CONST.__cfstring: 0x580
   __DATA_CONST.__objc_classlist: 0x40

   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__auth_got: 0x420
-  __DATA_CONST.__got: 0x158
+  __DATA_CONST.__got: 0x160
   __DATA.__objc_const: 0x1c08
   __DATA.__objc_selrefs: 0xd30
   __DATA.__objc_ivar: 0xd8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 776
-  Symbols:   571
-  CStrings:  1051
+  Functions: 780
+  Symbols:   575
+  CStrings:  1050
 
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
