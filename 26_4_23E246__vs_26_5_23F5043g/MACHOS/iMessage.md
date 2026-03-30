## iMessage

> `/System/Library/Messages/PlugIns/iMessage.imservice/iMessage`

```diff

-1450.500.221.2.9
-  __TEXT.__text: 0xc3e20
+1450.600.13.2.2
+  __TEXT.__text: 0xc40cc
   __TEXT.__auth_stubs: 0x1c20
-  __TEXT.__objc_stubs: 0xd2e0
+  __TEXT.__objc_stubs: 0xd300
   __TEXT.__objc_methlist: 0x29bc
   __TEXT.__const: 0xe58
-  __TEXT.__gcc_except_tab: 0xa058
-  __TEXT.__cstring: 0x327d
+  __TEXT.__gcc_except_tab: 0xa090
+  __TEXT.__cstring: 0x326d
   __TEXT.__oslogstring: 0x1738b
   __TEXT.__objc_classname: 0x61c
-  __TEXT.__objc_methname: 0x12804
+  __TEXT.__objc_methname: 0x127f4
   __TEXT.__objc_methtype: 0x2c69
   __TEXT.__ustring: 0x4
   __TEXT.__swift5_typeref: 0x67e

   __TEXT.__unwind_info: 0x2330
   __TEXT.__eh_frame: 0x988
   __DATA_CONST.__auth_got: 0xe20
-  __DATA_CONST.__got: 0x10d8
+  __DATA_CONST.__got: 0x10e0
   __DATA_CONST.__auth_ptr: 0x1d8
-  __DATA_CONST.__const: 0x3a48
+  __DATA_CONST.__const: 0x3a38
   __DATA_CONST.__cfstring: 0x3840
   __DATA_CONST.__objc_classlist: 0xe0
   __DATA_CONST.__objc_catlist: 0x38

   __DATA_CONST.__objc_arrayobj: 0x78
   __DATA_CONST.__objc_doubleobj: 0x20
   __DATA.__objc_const: 0x2e08
-  __DATA.__objc_selrefs: 0x3ac0
+  __DATA.__objc_selrefs: 0x3ac8
   __DATA.__objc_ivar: 0x1c8
   __DATA.__objc_data: 0x9c0
   __DATA.__data: 0xa60

   - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftAppleArchive.dylib
-  - /usr/lib/swift/libswiftCallKit.dylib
   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 95C89B97-D474-32AB-83F0-DFAC73717D2C
+  UUID: E508A44D-0C1A-3348-BF21-B370801BF11E
   Functions: 1668
   Symbols:   892
   CStrings:  5119
Symbols:
+ _OBJC_CLASS_$_IMDChatDisplayNameChangeContext
- __swift_FORCE_LOAD_$_swiftCallKit
Functions:
~ sub_15a40 -> sub_159f8 : 9600 -> 9704
~ sub_18440 -> sub_18460 : 4980 -> 5128
~ sub_2001c -> sub_200d0 : 1756 -> 1788
~ sub_22fb0 -> sub_23084 : 1576 -> 1600
~ sub_38c10 -> sub_38cfc : 1380 -> 1384
~ sub_39174 -> sub_39264 : 9548 -> 9636
~ sub_3bd00 -> sub_3be48 : 4668 -> 4740
~ sub_722fc -> sub_7248c : 1344 -> 1388
~ sub_76a5c -> sub_76c18 : 1164 -> 1276
~ sub_88d58 -> sub_88f84 : 7228 -> 7284
CStrings:
+ "Failed to read payload data with error: %@"
+ "didChangeChatWithContexts:"
+ "initWithChatStatus:chat:style:displayName:groupID:handleInfo:account:isBlackholed:"
+ "initWithDisplayName:fromID:toIdentifier:forChat:style:account:"
+ "initWithDisplayName:messageGUID:fromID:toIdentifier:forChat:style:account:"
+ "initWithMemberStatus:forHandle:fromHandle:unformattedNumber:countryCode:forChat:style:account:destinationCallerID:"
+ "setChatStatus:"
+ "setChatStyle:"
- "Incoming plugin message data string: %@"
- "InternalPayload"
- "didChangeMemberStatus:"
- "didChangeMemberStatus:forHandle:fromHandle:unformattedNumber:countryCode:forChat:style:account:destinationCallerID:"
- "didReceiveDisplayNameChange:fromID:toIdentifier:forChat:style:account:"
- "didReceiveDisplayNameChange:guid:fromID:toIdentifier:forChat:style:account:"
- "didUpdateChatStatus:chat:style:context:"
- "didUpdateChatStatus:chat:style:displayName:groupID:handleInfo:account:isBlackholed:"

```
