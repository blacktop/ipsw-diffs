## iMessage

> `/System/Library/Messages/PlugIns/iMessage.imservice/iMessage`

```diff

-1443.100.10.1.5
-  __TEXT.__text: 0xb683c
+1445.100.6.2.4
+  __TEXT.__text: 0xb6ed0
   __TEXT.__auth_stubs: 0x1aa0
-  __TEXT.__objc_stubs: 0xbd00
+  __TEXT.__objc_stubs: 0xbda0
   __TEXT.__objc_methlist: 0x2934
-  __TEXT.__const: 0xba0
-  __TEXT.__gcc_except_tab: 0xb3bc
+  __TEXT.__const: 0xbb0
+  __TEXT.__gcc_except_tab: 0xb3c4
   __TEXT.__cstring: 0x33ad
-  __TEXT.__oslogstring: 0x16096
+  __TEXT.__oslogstring: 0x16256
   __TEXT.__objc_classname: 0x50a
-  __TEXT.__objc_methname: 0x11b54
+  __TEXT.__objc_methname: 0x11bfa
   __TEXT.__objc_methtype: 0x290b
   __TEXT.__ustring: 0x4
-  __TEXT.__swift5_typeref: 0x63e
+  __TEXT.__swift5_typeref: 0x640
   __TEXT.__constg_swiftt: 0x36c
   __TEXT.__swift5_reflstr: 0x2b0
   __TEXT.__swift5_fieldmd: 0x35c

   __TEXT.__swift5_builtin: 0x50
   __TEXT.__swift5_mpenum: 0x38
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x2290
+  __TEXT.__unwind_info: 0x2298
   __TEXT.__eh_frame: 0x680
   __DATA_CONST.__auth_got: 0xd60
-  __DATA_CONST.__got: 0xfc8
-  __DATA_CONST.__auth_ptr: 0x168
+  __DATA_CONST.__got: 0xfd0
+  __DATA_CONST.__auth_ptr: 0x170
   __DATA_CONST.__const: 0x3790
   __DATA_CONST.__cfstring: 0x36c0
   __DATA_CONST.__objc_classlist: 0xe0

   __DATA_CONST.__objc_arrayobj: 0x78
   __DATA_CONST.__objc_doubleobj: 0x20
   __DATA.__objc_const: 0x2e38
-  __DATA.__objc_selrefs: 0x37f8
+  __DATA.__objc_selrefs: 0x3830
   __DATA.__objc_ivar: 0x1d0
   __DATA.__objc_data: 0x9b8
   __DATA.__data: 0xa38

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: DD2661F8-7E8D-35ED-8AD4-95B67056FA5C
+  UUID: 34ED80D1-5E0F-3BAB-85F5-AC775C825A1D
   Functions: 1590
-  Symbols:   849
-  CStrings:  4932
+  Symbols:   850
+  CStrings:  4943
 
Symbols:
+ _OBJC_CLASS_$_IMDChatStatusChangeContext
Functions:
~ sub_34860 : 8660 -> 8688
~ sub_6153c -> sub_61558 : 6380 -> 6368
~ sub_8765c -> sub_8766c : 280 -> 256
~ sub_87774 -> sub_8776c : 288 -> 264
~ sub_931f8 -> sub_931d8 : 4104 -> 4084
~ sub_94244 -> sub_94210 : 836 -> 832
~ sub_96ca0 -> sub_96c68 : 5888 -> 5996
~ sub_9a38c -> sub_9a3c0 : 2300 -> 3204
~ sub_9c8b8 -> sub_9cc74 : 9432 -> 9440
~ sub_9eebc -> sub_9f280 : 716 -> 712
~ sub_a2674 -> sub_a2a34 : 652 -> 660
~ sub_a2900 -> sub_a2cc8 : 3100 -> 3064
~ sub_a6998 -> sub_a6d3c : 1884 -> 2636
CStrings:
+ "Got background version: %llu for chat: %@"
+ "Incoming background version: %llu is lower than current chat background version: %@."
+ "Missing chatIdentifier or chatStyle on chat: ChatStyle: %hhu, %@"
+ "No valid IMChatStyle or chatIdentifier found on chat when removing background. Style: %hhu. Chat identifier: %s, chat: %@"
+ "No valid IMChatStyle or chatIdentifier found on chat. Style: %hhu. Chat identifier: %s, chat: %@"
+ "No valid chatIdentifier or chatStyle found on chat when removing background. ChatStyle: %hhu, Chat identifier: %s, chat: %@"
+ "Not requesting background for chat because it has a newer version: %@. Incoming version: (%llu) Chat: %@."
+ "Setting transferInfo: %s and background version: %llu for chat: %@."
+ "Tried to set a non-valid background version (%llu for chat %@"
+ "__im_nanosecondTimeInterval"
+ "didUpdateChatStatus:chat:style:context:"
+ "initWithUnsignedLongLong:"
+ "setDisplayName:"
+ "setHandleInfo:"
+ "setIsBlackholed:"
+ "setIsMessageSentFromMe:"
+ "v52@0:8@16Q24@32@40B48"
- "Got background version: %ld for chat: %@"
- "Incoming background version: %lu is lower than current chat background version: %@."
- "Not requesting background for chat because it has a newer version: %@. Incoming version: (%ld) Chat: %@."
- "Setting transferInfo: %s and background version: %ld for chat: %@."
- "Tried to set a non-valid background version (%ld for chat %@"
- "v52@0:8@16q24@32@40B48"

```
