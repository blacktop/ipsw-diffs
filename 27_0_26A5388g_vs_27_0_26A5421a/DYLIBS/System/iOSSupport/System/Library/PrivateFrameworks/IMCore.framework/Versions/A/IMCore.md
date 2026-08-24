## IMCore

> `/System/iOSSupport/System/Library/PrivateFrameworks/IMCore.framework/Versions/A/IMCore`

```diff

-1487.100.6.1.2
-  __TEXT.__text: 0x2f29ec
-  __TEXT.__objc_methlist: 0x188fc
-  __TEXT.__const: 0x116d0
-  __TEXT.__gcc_except_tab: 0x11168
-  __TEXT.__cstring: 0x13206
-  __TEXT.__oslogstring: 0x229c9
+1491.100.1.1.9
+  __TEXT.__text: 0x2f2ac4
+  __TEXT.__objc_methlist: 0x189ec
+  __TEXT.__const: 0x116e0
+  __TEXT.__gcc_except_tab: 0x111f0
+  __TEXT.__cstring: 0x13186
+  __TEXT.__oslogstring: 0x22b59
   __TEXT.__ustring: 0xc0
   __TEXT.__dlopen_cstrs: 0x184
   __TEXT.__swift5_typeref: 0x397a

   __TEXT.__swift_as_ret: 0x130
   __TEXT.__swift_as_cont: 0x2e0
   __TEXT.__swift5_mpenum: 0x40
-  __TEXT.__unwind_info: 0xba40
+  __TEXT.__unwind_info: 0xba68
   __TEXT.__eh_frame: 0x72b0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x5760
-  __DATA_CONST.__objc_classlist: 0x8f0
+  __DATA_CONST.__const: 0x5768
+  __DATA_CONST.__objc_classlist: 0x900
   __DATA_CONST.__objc_catlist: 0xf0
-  __DATA_CONST.__objc_protolist: 0x570
+  __DATA_CONST.__objc_protolist: 0x578
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xe718
+  __DATA_CONST.__objc_selrefs: 0xe780
   __DATA_CONST.__objc_protorefs: 0x1f0
   __DATA_CONST.__objc_superrefs: 0x5a0
   __DATA_CONST.__objc_arraydata: 0xb0
-  __DATA_CONST.__got: 0x27b8
-  __AUTH_CONST.__const: 0xc370
-  __AUTH_CONST.__cfstring: 0xb600
-  __AUTH_CONST.__objc_const: 0x21d38
+  __DATA_CONST.__got: 0x27d0
+  __AUTH_CONST.__const: 0xc390
+  __AUTH_CONST.__cfstring: 0xb640
+  __AUTH_CONST.__objc_const: 0x21f70
   __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH_CONST.__objc_intobj: 0x180
   __AUTH_CONST.__objc_doubleobj: 0x20
-  __AUTH_CONST.__auth_got: 0x2140
-  __AUTH.__objc_data: 0x2e78
+  __AUTH_CONST.__auth_got: 0x2150
+  __AUTH.__objc_data: 0x2f18
   __AUTH.__data: 0x2bd8
-  __DATA.__objc_ivar: 0x1298
-  __DATA.__data: 0x6248
+  __DATA.__objc_ivar: 0x12a0
+  __DATA.__data: 0x62a8
   __DATA.__bss: 0x1e4e0
   __DATA.__common: 0x798
   __DATA_DIRTY.__objc_data: 0x2ef0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 15087
-  Symbols:   2652
-  CStrings:  4897
+  Functions: 15098
+  Symbols:   2660
+  CStrings:  4899
 
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
