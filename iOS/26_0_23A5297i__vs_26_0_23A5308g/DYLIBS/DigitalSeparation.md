## DigitalSeparation

> `/System/Library/PrivateFrameworks/DigitalSeparation.framework/DigitalSeparation`

```diff

-574.0.0.0.0
-  __TEXT.__text: 0x2b2e4
+579.0.0.0.0
+  __TEXT.__text: 0x2b334
   __TEXT.__auth_stubs: 0x6d0
   __TEXT.__objc_methlist: 0x1dc4
   __TEXT.__cstring: 0x13b0

   __AUTH_CONST.__cfstring: 0x1500
   __AUTH_CONST.__objc_const: 0x4290
   __AUTH_CONST.__objc_intobj: 0x30
-  __AUTH.__objc_data: 0x500
+  __AUTH.__objc_data: 0x410
   __DATA.__objc_ivar: 0x17c
   __DATA.__data: 0x4e8
-  __DATA.__bss: 0x88
-  __DATA_DIRTY.__objc_data: 0x370
-  __DATA_DIRTY.__bss: 0xa0
+  __DATA.__bss: 0x80
+  __DATA_DIRTY.__objc_data: 0x460
+  __DATA_DIRTY.__bss: 0xb0
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 90633CB9-7382-3F65-891C-A0EDFF852BF7
+  UUID: A5C33C14-6F1E-3F3B-A5BB-A4D8B6260665
   Functions: 803
-  Symbols:   3069
+  Symbols:   3070
   CStrings:  1524
 
Symbols:
+ ___50-[DSSharingType stopAllSharingOnQueue:completion:]_block_invoke.312
+ ___50-[DSSharingType stopAllSharingOnQueue:completion:]_block_invoke.312.cold.1
+ ___50-[DSSharingType stopAllSharingOnQueue:completion:]_block_invoke.317
+ ___52-[DSSharingType stopSharingPeople:queue:completion:]_block_invoke.324
+ ___54-[DSAppSharing resetShortcutsAutomationTimer:handler:]_block_invoke.391
+ ___55-[DSSharingPerson stopSharingSources:queue:completion:]_block_invoke.328
+ ___55-[DSSharingPerson stopSharingSources:queue:completion:]_block_invoke.328.cold.1
+ ___55-[DSSharingPerson stopSharingSources:queue:completion:]_block_invoke.329
+ ___72-[DSSharingType stopSharingWithPeople:asParticipantsOnQueue:completion:]_block_invoke.319
+ ___72-[DSSharingType stopSharingWithPeople:asParticipantsOnQueue:completion:]_block_invoke.319.cold.1
+ ___72-[DSSharingType stopSharingWithPeople:asParticipantsOnQueue:completion:]_block_invoke.320
+ ___72-[DSSharingType stopSharingWithPeople:asParticipantsOnQueue:completion:]_block_invoke.321
+ ___block_literal_global.317
+ ___block_literal_global.330
+ ___block_literal_global.334
+ ___block_literal_global.351
+ _kDescriptorCacheLock
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
- ___block_literal_global.314
- ___block_literal_global.327
- ___block_literal_global.331
- ___block_literal_global.348
Functions:
~ +[DSSourceDescriptor setDescriptorCache:] : 116 -> 140
~ +[DSSourceDescriptor sourceDescriptorForSource:localizationBundle:] : 408 -> 464

```
