## MXUIServiceClient

> `/System/Library/PrivateFrameworks/MXUIServiceClient.framework/MXUIServiceClient`

```diff

-  __TEXT.__text: 0x1e58
-  __TEXT.__objc_methlist: 0x2dc
+  __TEXT.__text: 0x1e90
+  __TEXT.__objc_methlist: 0x2f4
   __TEXT.__const: 0x68
-  __TEXT.__gcc_except_tab: 0x24
-  __TEXT.__cstring: 0x450
+  __TEXT.__gcc_except_tab: 0x28
+  __TEXT.__cstring: 0x464
   __TEXT.__oslogstring: 0x1f9
   __TEXT.__unwind_info: 0x100
   __TEXT.__objc_stubs: 0x0

   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2c8
+  __DATA_CONST.__objc_selrefs: 0x2e0
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x18
   __DATA_CONST.__got: 0x90

   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 59
-  Symbols:   319
+  Functions: 61
+  Symbols:   325
   CStrings:  59
 
Sections:
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__got : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__objc_data : content changed
Symbols:
+ -[MXUIService_Client _promptForAudioMovedBanner:iconType:sourceApp:]
+ -[MXUIService_Client promptForReceiverEnabledBanner:]
+ -[MXUIService_Client promptForSpeakerEnabledBanner:]
+ _objc_msgSend$_promptForAudioMovedBanner:iconType:sourceApp:
+ _objc_msgSend$showReceiverEnabledBanner:completionHandler:
+ _objc_msgSend$showSpeakerEnabledBanner:completionHandler:
- -[MXUIService_Client promptForAudioMovedBanner:]
- _objc_msgSend$showAudioMovedBanner:completionHandler:
CStrings:
+ "-[MXUIService_Client _promptForAudioMovedBanner:iconType:sourceApp:]"
- "-[MXUIService_Client promptForAudioMovedBanner:]"

```
