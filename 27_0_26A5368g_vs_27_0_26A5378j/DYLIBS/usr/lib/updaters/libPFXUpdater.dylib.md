## libPFXUpdater.dylib

> `/usr/lib/updaters/libPFXUpdater.dylib`

```diff

-  __TEXT.__text: 0x18764
+  __TEXT.__text: 0x188d4
   __TEXT.__objc_methlist: 0x3b4
-  __TEXT.__cstring: 0x3b29
+  __TEXT.__cstring: 0x3ae6
   __TEXT.__const: 0x80
   __TEXT.__oslogstring: 0x36a
-  __TEXT.__unwind_info: 0x668
+  __TEXT.__unwind_info: 0x670
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 857
-  Symbols:   1183
-  CStrings:  588
+  Functions: 861
+  Symbols:   1187
+  CStrings:  587
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__got : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH.__objc_data : content changed
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
