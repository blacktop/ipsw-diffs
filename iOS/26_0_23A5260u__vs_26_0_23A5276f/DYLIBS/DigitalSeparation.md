## DigitalSeparation

> `/System/Library/PrivateFrameworks/DigitalSeparation.framework/DigitalSeparation`

```diff

-552.0.0.0.0
-  __TEXT.__text: 0x259c4
+565.0.1.0.0
+  __TEXT.__text: 0x28f6c
   __TEXT.__auth_stubs: 0x680
-  __TEXT.__objc_methlist: 0x1974
+  __TEXT.__objc_methlist: 0x19bc
   __TEXT.__cstring: 0x12d9
   __TEXT.__const: 0x98
-  __TEXT.__gcc_except_tab: 0xcf0
+  __TEXT.__gcc_except_tab: 0x11ac
   __TEXT.__oslogstring: 0x1f61
   __TEXT.__dlopen_cstrs: 0x68
-  __TEXT.__unwind_info: 0x760
-  __TEXT.__objc_classname: 0x22a
-  __TEXT.__objc_methname: 0x4521
+  __TEXT.__unwind_info: 0x790
+  __TEXT.__objc_classname: 0x228
+  __TEXT.__objc_methname: 0x458d
   __TEXT.__objc_methtype: 0x971
-  __TEXT.__objc_stubs: 0x3c60
+  __TEXT.__objc_stubs: 0x3cc0
   __DATA_CONST.__got: 0x3b8
   __DATA_CONST.__const: 0xc68
   __DATA_CONST.__objc_classlist: 0xc0
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1258
+  __DATA_CONST.__objc_selrefs: 0x1270
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x70
   __AUTH_CONST.__auth_got: 0x350
   __AUTH_CONST.__const: 0x200
   __AUTH_CONST.__cfstring: 0x13e0
-  __AUTH_CONST.__objc_const: 0x38c0
+  __AUTH_CONST.__objc_const: 0x38f0
   __AUTH.__objc_data: 0x410
-  __DATA.__objc_ivar: 0x144
+  __DATA.__objc_ivar: 0x148
   __DATA.__data: 0x368
   __DATA.__bss: 0x68
   __DATA_DIRTY.__objc_data: 0x370
-  __DATA_DIRTY.__bss: 0x98
+  __DATA_DIRTY.__bss: 0xa0
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6214920E-E4B8-39B0-990A-E26F9F388552
-  Functions: 700
-  Symbols:   2683
-  CStrings:  1403
+  UUID: 4B66B9BD-945D-3B3D-834C-C47B1277C524
+  Functions: 708
+  Symbols:   2723
+  CStrings:  1407
 
Symbols:
+ +[DSXPCSharingPerson initialize]
+ -[DSXPCSharingPerson participantsBySource]
+ -[DSXPCSharingPerson removeParticipant:fromSource:]
+ -[DSXPCSharingPerson setParticipantsBySource:]
+ -[DSXPCSharingPerson setParticipation:]
+ -[DSXPCSharingPerson stopSharingSources:queue:completion:]
+ -[DSXPCSharingPerson stopSharingSources:queue:completion:].cold.1
+ -[DSXPCSharingPerson stopSharingSources:queue:completion:].cold.2
+ -[DSXPCSharingPerson stopSharingSources:queue:completion:].cold.3
+ -[DSXPCSharingPerson stopSharingSources:queue:completion:].cold.4
+ _OBJC_IVAR_$_DSXPCSharingPerson._participantsBySource
+ ___50-[DSSharingType stopAllSharingOnQueue:completion:]_block_invoke.312
+ ___50-[DSSharingType stopAllSharingOnQueue:completion:]_block_invoke.312.cold.1
+ ___50-[DSSharingType stopAllSharingOnQueue:completion:]_block_invoke.317
+ ___52-[DSSharingType stopSharingPeople:queue:completion:]_block_invoke.324
+ ___54-[DSAppSharing resetShortcutsAutomationTimer:handler:]_block_invoke.391
+ ___55-[DSSharingPerson stopSharingSources:queue:completion:]_block_invoke.328
+ ___55-[DSSharingPerson stopSharingSources:queue:completion:]_block_invoke.328.cold.1
+ ___55-[DSSharingPerson stopSharingSources:queue:completion:]_block_invoke.329
+ ___58-[DSXPCSharingPerson stopSharingSources:queue:completion:]_block_invoke
+ ___58-[DSXPCSharingPerson stopSharingSources:queue:completion:]_block_invoke.346
+ ___58-[DSXPCSharingPerson stopSharingSources:queue:completion:]_block_invoke.346.cold.1
+ ___58-[DSXPCSharingPerson stopSharingSources:queue:completion:]_block_invoke.347
+ ___58-[DSXPCSharingPerson stopSharingSources:queue:completion:]_block_invoke.cold.1
+ ___72-[DSSharingType stopSharingWithPeople:asParticipantsOnQueue:completion:]_block_invoke.319
+ ___72-[DSSharingType stopSharingWithPeople:asParticipantsOnQueue:completion:]_block_invoke.319.cold.1
+ ___72-[DSSharingType stopSharingWithPeople:asParticipantsOnQueue:completion:]_block_invoke.320
+ ___72-[DSSharingType stopSharingWithPeople:asParticipantsOnQueue:completion:]_block_invoke.321
+ ___block_literal_global.330
+ ___block_literal_global.334
+ ___block_literal_global.351
+ _objc_msgSend$participantsBySource
+ _objc_msgSend$setParticipantsBySource:
+ _objc_msgSend$setParticipation:
- ___50-[DSSharingType stopAllSharingOnQueue:completion:]_block_invoke.309
- ___50-[DSSharingType stopAllSharingOnQueue:completion:]_block_invoke.309.cold.1
- ___50-[DSSharingType stopAllSharingOnQueue:completion:]_block_invoke.311
- ___52-[DSSharingType stopSharingPeople:queue:completion:]_block_invoke.321
- ___54-[DSAppSharing resetShortcutsAutomationTimer:handler:]_block_invoke.388
- ___55-[DSSharingPerson stopSharingSources:queue:completion:]_block_invoke.325
- ___55-[DSSharingPerson stopSharingSources:queue:completion:]_block_invoke.325.cold.1
- ___55-[DSSharingPerson stopSharingSources:queue:completion:]_block_invoke.326
- ___72-[DSSharingType stopSharingWithPeople:asParticipantsOnQueue:completion:]_block_invoke.316
- ___72-[DSSharingType stopSharingWithPeople:asParticipantsOnQueue:completion:]_block_invoke.316.cold.1
- ___72-[DSSharingType stopSharingWithPeople:asParticipantsOnQueue:completion:]_block_invoke.317
- ___72-[DSSharingType stopSharingWithPeople:asParticipantsOnQueue:completion:]_block_invoke.318
- ___block_literal_global.327
- ___block_literal_global.331
- ___block_literal_global.348
CStrings:
+ "T@\"NSDictionary\",&,N,V_participantsBySource"
+ "participantsBySource"
+ "setParticipantsBySource:"
+ "setParticipation:"

```
