## libAce3Updater.dylib

> `/usr/lib/updaters/libAce3Updater.dylib`

```diff

-  __TEXT.__text: 0x1f204
+  __TEXT.__text: 0x1f4e4
   __TEXT.__objc_methlist: 0x3b4
-  __TEXT.__cstring: 0x5ebb
+  __TEXT.__cstring: 0x5e78
   __TEXT.__const: 0x200
   __TEXT.__oslogstring: 0x7
-  __TEXT.__unwind_info: 0x7a0
+  __TEXT.__unwind_info: 0x7a8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x2c0
-  __DATA_CONST.__objc_superrefs: 0x18
-  __DATA_CONST.__got: 0xc0
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x30
   __AUTH_CONST.__cfstring: 0xfe0
   __AUTH_CONST.__objc_const: 0x918
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x190
+  __DATA.__objc_classrefs: 0x50
+  __DATA.__objc_superrefs: 0x18
   __DATA.__objc_ivar: 0x98
   __DATA.__data: 0x38
   __DATA.__bss: 0x1974

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 955
-  Symbols:   1307
-  CStrings:  824
+  Functions: 959
+  Symbols:   1311
+  CStrings:  823
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH.__objc_data : content changed
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _uarpDownstreamEndpointProcessReachableMessage
+ _uarpPlatformDownstreamEndpointReachable2
+ _uarpProcessTLV2
+ _uarpProtocolSupportsDownstreamReachableTLVs
+ _uarpSendDownstreamEndpointReachable2
- _objc_claimAutoreleasedReturnValue
- _uarpTransmitBufferUpstream
CStrings:
+ "%s: ESPRESSO: Message <type=0x%04x, id=0x%04x> Length too big ! expected <%u>, got <%u>"
- "%s: ESPRESSO:Bonus Message <type=0x%04x, length=x0x%04x, id=0x%04x>"
- "%s: ESPRESSO:Message <type=0x%04x, id=0x%04x> Length too big ! expected <%u>, got <%u>"

```
