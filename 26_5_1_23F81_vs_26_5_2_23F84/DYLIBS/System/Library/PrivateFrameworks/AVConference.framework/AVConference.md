## AVConference

> `/System/Library/PrivateFrameworks/AVConference.framework/AVConference`

```diff

-  __TEXT.__text: 0x73f974
+  __TEXT.__text: 0x73fa8c
   __TEXT.__auth_stubs: 0x5640
   __TEXT.__objc_methlist: 0x35e28
   __TEXT.__const: 0xbf40
-  __TEXT.__cstring: 0x909e9
-  __TEXT.__oslogstring: 0x117f99
+  __TEXT.__cstring: 0x90a31
+  __TEXT.__oslogstring: 0x11802c
   __TEXT.__gcc_except_tab: 0x2b48
   __TEXT.__ustring: 0x2d4
-  __TEXT.__unwind_info: 0x10ac8
+  __TEXT.__unwind_info: 0x10ad0
   __TEXT.__objc_classname: 0x4ed7
   __TEXT.__objc_methname: 0x7e5d7
   __TEXT.__objc_methtype: 0x284ce

   - /usr/lib/libspindump.dylib
   - /usr/lib/libtailspin.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 32307
-  Symbols:   103100
-  CStrings:  57506
+  Functions: 32306
+  Symbols:   103104
+  CStrings:  57508
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__gcc_except_tab : content changed
~ __DATA_CONST.__got : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__auth_got : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH_CONST.__objc_floatobj : content changed
~ __AUTH_CONST.__objc_doubleobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __AUTH.__objc_data : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__objc_data : content changed
~ __DATA_DIRTY.__data : content changed
Functions:
~ __RTPTransport_ParseMediaPacket : 7400 -> 7388
~ _SRTPVerifyAuthenticationTag : 2060 -> 2048
- _OUTLINED_FUNCTION_23
~ -[VCVideoStream setupMultiwayVideoReceiverConfig:forTransportStream:] : 692 -> 1056
~ _SRTPVerifyAuthenticationTag.cold.11 : 152 -> 160
~ _SRTPVerifyAuthenticationTag.cold.12 : 152 -> 160
~ _SRTPVerifyAuthenticationTag.cold.13 : 152 -> 160
- _SRTPVerifyAuthenticationTag.cold.14
+ -[VCVideoStream setupMultiwayVideoReceiverConfig:forTransportStream:].cold.1
~ -[VCVideoStream onConfigureStreamWithConfiguration:error:].cold.3 : 124 -> 112
~ -[VCVideoStream onConfigureStreamWithConfiguration:error:].cold.4 : 116 -> 104
CStrings:
+ "-[VCVideoStream setupMultiwayVideoReceiverConfig:forTransportStream:]"
+ "2205.3.1.1"
+ "VCVideoStream [%s] %s:%d %@(%p) streamCount=%u reached or exceeded max=%u, dropping excess stream"
+ "VCVideoStream [%s] %s:%d streamCount=%u reached or exceeded max=%u, dropping excess stream"
- " [%s] %s:%d isMKIChanged must not be NULL"
- "2205.3.1"

```
