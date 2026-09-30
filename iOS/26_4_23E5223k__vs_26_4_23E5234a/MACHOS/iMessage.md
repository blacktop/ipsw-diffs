## iMessage

> `/System/Library/Messages/PlugIns/iMessage.imservice/iMessage`

```diff

-1450.500.214.2.1
-  __TEXT.__text: 0xc3eb0
-  __TEXT.__auth_stubs: 0x1c10
-  __TEXT.__objc_stubs: 0xd300
+1450.500.221.2.9
+  __TEXT.__text: 0xc3e20
+  __TEXT.__auth_stubs: 0x1c20
+  __TEXT.__objc_stubs: 0xd2e0
   __TEXT.__objc_methlist: 0x29bc
   __TEXT.__const: 0xe58
   __TEXT.__gcc_except_tab: 0xa058
   __TEXT.__cstring: 0x327d
-  __TEXT.__oslogstring: 0x173ab
+  __TEXT.__oslogstring: 0x1738b
   __TEXT.__objc_classname: 0x61c
-  __TEXT.__objc_methname: 0x12824
+  __TEXT.__objc_methname: 0x12804
   __TEXT.__objc_methtype: 0x2c69
   __TEXT.__ustring: 0x4
   __TEXT.__swift5_typeref: 0x67e

   __TEXT.__swift5_protos: 0x4
   __TEXT.__unwind_info: 0x2330
   __TEXT.__eh_frame: 0x988
-  __DATA_CONST.__auth_got: 0xe18
+  __DATA_CONST.__auth_got: 0xe20
   __DATA_CONST.__got: 0x10d8
   __DATA_CONST.__auth_ptr: 0x1d8
   __DATA_CONST.__const: 0x3a48

   __DATA_CONST.__objc_arrayobj: 0x78
   __DATA_CONST.__objc_doubleobj: 0x20
   __DATA.__objc_const: 0x2e08
-  __DATA.__objc_selrefs: 0x3ac8
+  __DATA.__objc_selrefs: 0x3ac0
   __DATA.__objc_ivar: 0x1c8
   __DATA.__objc_data: 0x9c0
   __DATA.__data: 0xa60

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 8F850C89-AB02-38E0-A39F-928C09DEAB3C
+  UUID: 95C89B97-D474-32AB-83F0-DFAC73717D2C
   Functions: 1668
-  Symbols:   891
-  CStrings:  5120
+  Symbols:   892
+  CStrings:  5119
 
Symbols:
+ _IMIsMessageEligibleForStrugglingMessage
Functions:
~ sub_82adc : 340 -> 248
~ sub_887f0 -> sub_88794 : 284 -> 192
~ sub_8cb0c -> sub_8ca54 : 772 -> 768
~ sub_913f4 -> sub_91338 : 2032 -> 2056
~ sub_94064 -> sub_93fc0 : 2632 -> 2652
CStrings:
+ "Item NOT eligible for Stewie. NOT monitoring failedEvent for struggling experience."
+ "Item eligible for Stewie. Monitoring failedEvent for struggling experience."
+ "strugglingMessageIndicationSent"
+ "trackSentMessageEventOfType:subtype:originalServiceName:messageSize:sendDuration:receiverType:receiverGroupType:wasSuccessful:isEmergencyNumber:isPartiallyActiveSIM:isEncrypted:strugglingMessageIndicationSent:error:"
- "Stewie is NOT enabled in fringe cellular. NOT monitoring failedEvent for struggling experience."
- "Stewie is enabled in fringe cellular. Monitoring failedEvent for struggling experience."
- "bestCandidateGroupChatWithFromIdentifier:toIdentifier:displayName:participants:groupID:"
- "isOneChatEnabled"
- "trackSentMessageEventOfType:subtype:originalServiceName:messageSize:sendDuration:receiverType:receiverGroupType:wasSuccessful:isEmergencyNumber:isPartiallyActiveSIM:isEncrypted:error:"

```
