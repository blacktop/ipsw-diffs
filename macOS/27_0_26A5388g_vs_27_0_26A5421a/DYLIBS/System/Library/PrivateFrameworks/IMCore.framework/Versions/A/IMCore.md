## IMCore

> `/System/Library/PrivateFrameworks/IMCore.framework/Versions/A/IMCore`

```diff

-1487.100.6.1.2
-  __TEXT.__text: 0x30a3e8
-  __TEXT.__objc_methlist: 0x18434
-  __TEXT.__const: 0x11678
-  __TEXT.__cstring: 0x12ace
-  __TEXT.__gcc_except_tab: 0x11088
-  __TEXT.__oslogstring: 0x223c7
+1491.100.1.1.9
+  __TEXT.__text: 0x30a4ec
+  __TEXT.__objc_methlist: 0x1851c
+  __TEXT.__const: 0x11688
+  __TEXT.__cstring: 0x12a4e
+  __TEXT.__gcc_except_tab: 0x11114
+  __TEXT.__oslogstring: 0x22557
   __TEXT.__dlopen_cstrs: 0x95
   __TEXT.__ustring: 0x18
   __TEXT.__swift5_typeref: 0x397a

   __TEXT.__swift_as_cont: 0x2e0
   __TEXT.__swift5_protos: 0x28
   __TEXT.__swift5_mpenum: 0x40
-  __TEXT.__unwind_info: 0xb8f0
+  __TEXT.__unwind_info: 0xb918
   __TEXT.__eh_frame: 0x72b4
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1a20
-  __DATA_CONST.__objc_classlist: 0x8c8
+  __DATA_CONST.__const: 0x1a28
+  __DATA_CONST.__objc_classlist: 0x8d8
   __DATA_CONST.__objc_catlist: 0xf8
-  __DATA_CONST.__objc_protolist: 0x560
+  __DATA_CONST.__objc_protolist: 0x568
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xe540
+  __DATA_CONST.__objc_selrefs: 0xe5a8
   __DATA_CONST.__objc_protorefs: 0x1f0
   __DATA_CONST.__objc_superrefs: 0x578
   __DATA_CONST.__objc_arraydata: 0xa8
-  __DATA_CONST.__got: 0x2860
-  __AUTH_CONST.__const: 0x10590
-  __AUTH_CONST.__cfstring: 0xafa0
-  __AUTH_CONST.__objc_const: 0x21678
+  __DATA_CONST.__got: 0x2878
+  __AUTH_CONST.__const: 0x105b0
+  __AUTH_CONST.__cfstring: 0xafe0
+  __AUTH_CONST.__objc_const: 0x218b0
   __AUTH_CONST.__objc_intobj: 0x150
   __AUTH_CONST.__objc_arrayobj: 0xf0
   __AUTH_CONST.__objc_doubleobj: 0x20
-  __AUTH_CONST.__auth_got: 0x1f48
-  __AUTH.__objc_data: 0x2ec8
+  __AUTH_CONST.__auth_got: 0x1f58
+  __AUTH.__objc_data: 0x2f68
   __AUTH.__data: 0x2bd0
-  __DATA.__objc_ivar: 0x1258
-  __DATA.__data: 0x6188
+  __DATA.__objc_ivar: 0x1260
+  __DATA.__data: 0x61e8
   __DATA.__bss: 0x1e460
   __DATA.__common: 0x798
   __DATA_DIRTY.__objc_data: 0x2d10

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 15006
-  Symbols:   2580
-  CStrings:  4798
+  Functions: 15017
+  Symbols:   2588
+  CStrings:  4800
 
Symbols:
+ _IMChatItemsUpdateReasonServiceChanged
+ _IMChatPropertyLastUPIVisibilityCheckDate
+ _IMIsRunningInMessagesNotificationExtension
+ _IMIsStringStewieEmergency
+ _OBJC_CLASS_$_IMNewComposeRichCardMessagePartChatItem
+ _OBJC_CLASS_$_IMNewComposeTextMessagePartChatItem
+ _OBJC_METACLASS_$_IMNewComposeRichCardMessagePartChatItem
+ _OBJC_METACLASS_$_IMNewComposeTextMessagePartChatItem
CStrings:
+ "(IMChat) Welcome messages changed"
+ "Attempted to update security scoped url for transferGUID: %@ but no message exists for transfer"
+ "ServiceChanged"
+ "UPI check triggered: %@ at %@ - oldNeedsHide: %@ newNeedsHide: %@ oldUPIDate: %@ newUPIDate: %@ oldestUPIDate: %@ -> UPIVisibilityChanged: %{bool}d UPIDateChanged: %{bool}d"
+ "UPI visibility changed, updating chat items for chat: %@ - UPIVisibilitySame: %{bool}d UPICheckDateChanged: %{bool}d lastUPIVisibilityCheckDate: %@"
+ "Welcome messages changed, updating chat items for chat: %@"
+ "set sortID %@ guid %@ itemIsUnsentAndFromMe %@"
+ "stage welcome prefilled text for chat: %@"
+ "stage welcome rich card in transcript for chat: %@"
- " doesn't match participants count: "
- "At least one participant is required"
- "Chat record for rowID: %lld: guid: %s has no participants. Continuing export without this chat"
- "Conversation type "
- "Participant list is empty for chat: "
- "UPI visibility changed, updating chat items for chat: %@"
- "set sortID %@ guid %@ unsentIsFromMeItemOrThreadOriginator %@"
```
