## CoreMedia

> `/System/Library/Frameworks/CoreMedia.framework/CoreMedia`

```diff

-3300.3.1.0.0
-  __TEXT.__text: 0x2905ec
+3300.4.1.0.0
+  __TEXT.__text: 0x29060c
   __TEXT.__auth_stubs: 0x3520
   __TEXT.__objc_methlist: 0x5e4
-  __TEXT.__const: 0x1bd0
-  __TEXT.__oslogstring: 0x2e6fb
+  __TEXT.__const: 0x1be0
+  __TEXT.__oslogstring: 0x2e6f2
   __TEXT.__cstring: 0x59615
   __TEXT.__gcc_except_tab: 0x1dc
   __TEXT.__dlopen_cstrs: 0x190

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 618B60C8-816B-3302-8016-89F4CC3F04FF
+  UUID: 35756680-A25A-33F3-AF96-235FCDC94D3C
   Functions: 10948
   Symbols:   26767
   CStrings:  17556
Functions:
~ _curll_getURLDispatch : 684 -> 712
~ _FigMemoryOriginSetBlockBufferInIPCMessageData : 776 -> 796
~ _FigXPCConnectionCopyMemoryOriginForConnectedProcess : 484 -> 476
~ _FigXPCConnectionCopyMemoryRecipientForConnectedProcess : 576 -> 568
CStrings:
+ "<<<< FigCustomURLHandling >>>> %s: %p: URL: %@ requestID: %llu"
- "<<<< FigCustomURLHandling >>>> %s: %p: URL: %{private}@ requestID: %llu"

```
