## MFAANetwork

> `/System/Library/PrivateFrameworks/MFAAuthentication.framework/XPCServices/MFAANetwork.xpc/MFAANetwork`

```diff

-  __TEXT.__text: 0x1b43f0
+  __TEXT.__text: 0x1b44c4
   __TEXT.__auth_stubs: 0x5e0
   __TEXT.__objc_stubs: 0x1500
   __TEXT.__objc_methlist: 0x74c

   __TEXT.__objc_methtype: 0x608
   __TEXT.__const: 0x1e1c0
   __TEXT.__cstring: 0xcf2
-  __TEXT.__oslogstring: 0x19f8
+  __TEXT.__oslogstring: 0x1a32
   __TEXT.__ustring: 0xa
   __TEXT.__gcc_except_tab: 0x150
   __TEXT.__unwind_info: 0x638

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 622
-  Symbols:   2930
-  CStrings:  787
+  Functions: 623
+  Symbols:   2936
+  CStrings:  788
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__gcc_except_tab : content changed
~ __TEXT.__unwind_info : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA_CONST.__objc_intobj : content changed
~ __DATA.__objc_const : content changed
~ __DATA.__objc_selrefs : content changed
~ __DATA.__data : content changed
Functions:
~ -[MFAANetwork _verifyFairPlaySignatureSync:forData:timedOut:error:] : 604 -> 720
~ -[FairPlaySAPSession initWithDelegate:] : 496 -> 492
~ _systemInfo_copyProductType : 72 -> 96
~ _systemInfo_copyProductVersion : 72 -> 96
+ -[MFAANetwork _requestMetadataForToken:withUUID:requestedLocale:requestInfo:withReply:].cold.15
CStrings:
+ "Cannot verify FairPlay SAP signature with nil parameters!"

```
