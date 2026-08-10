## IMCore

> `/System/Library/PrivateFrameworks/IMCore.framework/IMCore`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-1487.100.6.2.2
-  __TEXT.__text: 0x2fcdc0
+1491.100.1.2.11
+  __TEXT.__text: 0x2fd190
   __TEXT.__delay_stubs: 0x80
   __TEXT.__delay_helper: 0x14c
-  __TEXT.__objc_methlist: 0x18d4c
+  __TEXT.__objc_methlist: 0x18e4c
   __TEXT.__const: 0x116f0
-  __TEXT.__gcc_except_tab: 0x1193c
-  __TEXT.__cstring: 0x13405
-  __TEXT.__oslogstring: 0x23b3b
+  __TEXT.__gcc_except_tab: 0x119c4
+  __TEXT.__cstring: 0x13355
+  __TEXT.__oslogstring: 0x23d1b
   __TEXT.__ustring: 0xc0
   __TEXT.__dlopen_cstrs: 0x184
   __TEXT.__swift5_typeref: 0x39ae

   __TEXT.__swift_as_ret: 0x130
   __TEXT.__swift_as_cont: 0x2e0
   __TEXT.__swift5_mpenum: 0x40
-  __TEXT.__unwind_info: 0xc390
+  __TEXT.__unwind_info: 0xc3c0
   __TEXT.__eh_frame: 0x72b0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x58a0
-  __DATA_CONST.__objc_classlist: 0x908
+  __DATA_CONST.__const: 0x58a8
+  __DATA_CONST.__objc_classlist: 0x918
   __DATA_CONST.__objc_catlist: 0xf0
-  __DATA_CONST.__objc_protolist: 0x578
+  __DATA_CONST.__objc_protolist: 0x580
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xeaa8
+  __DATA_CONST.__objc_selrefs: 0xeb20
   __DATA_CONST.__objc_protorefs: 0x1f0
   __DATA_CONST.__objc_superrefs: 0x5b8
   __DATA_CONST.__objc_arraydata: 0xa8
-  __DATA_CONST.__got: 0x2878
+  __DATA_CONST.__got: 0x2890
   __AUTH_CONST.__const: 0xc3f8
-  __AUTH_CONST.__cfstring: 0xbaa0
-  __AUTH_CONST.__objc_const: 0x221d0
+  __AUTH_CONST.__cfstring: 0xbac0
+  __AUTH_CONST.__objc_const: 0x22418
   __AUTH_CONST.__objc_arrayobj: 0xf0
   __AUTH_CONST.__objc_intobj: 0x168
   __AUTH_CONST.__objc_doubleobj: 0x20
-  __AUTH_CONST.__auth_got: 0x21a0
-  __AUTH.__objc_data: 0x4020
+  __AUTH_CONST.__auth_got: 0x21a8
+  __AUTH.__objc_data: 0x40c0
   __AUTH.__data: 0x2d20
-  __DATA.__objc_ivar: 0x12bc
-  __DATA.__data: 0x64f8
+  __DATA.__objc_ivar: 0x12c4
+  __DATA.__data: 0x6558
   __DATA.__bss: 0x1eae0
   __DATA.__common: 0x7e0
   __DATA_DIRTY.__objc_data: 0x1e38

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 15211
-  Symbols:   2689
-  CStrings:  5023
+  Functions: 15223
+  Symbols:   2696
+  CStrings:  5025
 
Symbols:
+ _IMChatItemsUpdateReasonServiceChanged
+ _IMChatPropertyLastUPIVisibilityCheckDate
+ _IMIsRunningInMessagesNotificationExtension
+ _OBJC_CLASS_$_IMNewComposeRichCardMessagePartChatItem
+ _OBJC_CLASS_$_IMNewComposeTextMessagePartChatItem
+ _OBJC_METACLASS_$_IMNewComposeRichCardMessagePartChatItem
+ _OBJC_METACLASS_$_IMNewComposeTextMessagePartChatItem
CStrings:
+ "(IMChat) Welcome messages changed"
+ "Attempted to update security scoped url for transferGUID: %@ but no message exists for transfer"
+ "ServiceChanged"
+ "Struggling message awaiting satellite decision, don't downgrade: %@"
+ "UPI check triggered: %@ at %@ - oldNeedsHide: %@ newNeedsHide: %@ oldUPIDate: %@ newUPIDate: %@ oldestUPIDate: %@ -> UPIVisibilityChanged: %{bool}d UPIDateChanged: %{bool}d"
+ "UPI visibility changed, updating chat items for chat: %@ - UPIVisibilitySame: %{bool}d UPICheckDateChanged: %{bool}d lastUPIVisibilityCheckDate: %@"
+ "Welcome messages changed, updating chat items for chat: %@"
+ "set sortID %@ guid %@ itemIsUnsentAndFromMe %@"
+ "stage welcome prefilled text for chat: %@"
+ "stage welcome rich card in transcript for chat: %@"
- " doesn't match participants count: "
- "(IMChat) Service for sending changed"
- "At least one participant is required"
- "Chat record for rowID: %lld: guid: %s has no participants. Continuing export without this chat"
- "Conversation type "
- "Participant list is empty for chat: "
- "UPI visibility changed, updating chat items for chat: %@"
- "set sortID %@ guid %@ unsentIsFromMeItemOrThreadOriginator %@"
```
