## iMessage

> `/System/Library/Messages/PlugIns/iMessage.imservice/iMessage`

```diff

-1402.700.53.2.12
-  __TEXT.__text: 0x924ac
+1402.700.53.2.16
+  __TEXT.__text: 0x92758
   __TEXT.__auth_stubs: 0x1340
-  __TEXT.__objc_stubs: 0xb2c0
+  __TEXT.__objc_stubs: 0xb300
   __TEXT.__objc_methlist: 0x26ec
   __TEXT.__const: 0x3da
-  __TEXT.__gcc_except_tab: 0xa9e4
-  __TEXT.__cstring: 0x2ddd
-  __TEXT.__oslogstring: 0x14088
+  __TEXT.__gcc_except_tab: 0xaa44
+  __TEXT.__cstring: 0x2ded
+  __TEXT.__oslogstring: 0x141e8
   __TEXT.__objc_classname: 0x4e2
-  __TEXT.__objc_methname: 0x1045b
+  __TEXT.__objc_methname: 0x10494
   __TEXT.__objc_methtype: 0x277d
   __TEXT.__ustring: 0x4
   __TEXT.__constg_swiftt: 0x178

   __TEXT.__unwind_info: 0x1da0
   __TEXT.__eh_frame: 0x2c0
   __DATA_CONST.__auth_got: 0x9b0
-  __DATA_CONST.__got: 0xdb8
+  __DATA_CONST.__got: 0xdc8
   __DATA_CONST.__auth_ptr: 0x18
   __DATA_CONST.__const: 0x2ac8
   __DATA_CONST.__cfstring: 0x3320

   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__objc_arrayobj: 0x48
   __DATA.__objc_const: 0x2b38
-  __DATA.__objc_selrefs: 0x33e0
+  __DATA.__objc_selrefs: 0x33f0
   __DATA.__objc_ivar: 0x1b0
   __DATA.__objc_data: 0x388
   __DATA.__data: 0x748

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 5ADBBB88-7791-35DE-B421-C0FA382618AB
+  UUID: 1396EF62-FF44-3BD4-8097-E1E389F1BD22
   Functions: 1179
-  Symbols:   780
-  CStrings:  4571
+  Symbols:   782
+  CStrings:  4577
 
Symbols:
+ _IMBalloonBundleIdentifierSafetyMonitor
+ _OBJC_CLASS_$_IMContactStore
Functions:
~ sub_18190 : 1440 -> 1616
~ sub_2c420 -> sub_2c4d0 : 4060 -> 4160
~ sub_2da60 -> sub_2db74 : 11828 -> 12236
CStrings:
+ "   isFromTrustedSender: %@"
+ "MessageService_ChatAsset"
+ "Not notifying coreroutined about incoming CheckIn(messageGUID %@), as it's not from a known sender."
+ "We already have an item for guid: %@, and it is not a IMGroupActionItem. That shouldn't be possible. Generating a new GUID to prevent us overwriting an existing message with an IMGroupActionItem. New guid: %@ Existing item: %@"
+ "fetchCNContactForHandleWithID:"
+ "isCNContactAKnownContact:"

```
