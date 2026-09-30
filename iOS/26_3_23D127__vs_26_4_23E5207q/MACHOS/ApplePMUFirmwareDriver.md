## ApplePMUFirmwareDriver

> `/System/Library/Extensions/ApplePMUFirmwareDriver.kext/ApplePMUFirmwareDriver`

```diff

 7.0.0.0.0
   __TEXT.__const: 0x18
   __TEXT.__cstring: 0x854
-  __TEXT_EXEC.__text: 0x2f54
+  __TEXT_EXEC.__text: 0x288c
   __TEXT_EXEC.__auth_stubs: 0x1b0
   __DATA.__data: 0xc8
   __DATA.__common: 0x60

   __DATA_CONST.__mod_term_func: 0x10
   __DATA_CONST.__const: 0xcb8
   __DATA_CONST.__kalloc_type: 0x80
-  UUID: 4F591342-FCC3-3792-9FA6-F45EC071BCC9
-  Functions: 80
-  Symbols:   666
+  UUID: 2F9D303A-27C4-3D30-87CD-106225E76276
+  Functions: 81
+  Symbols:   671
   CStrings:  63
 
Symbols:
+ /Library/Caches/com.apple.xbs/D117CB6F-A300-4F43-9158-222BD35FC4A0/TemporaryDirectory.8vL1hn/Binaries/ApplePMUFirmwareDriver/install/TempContent/Objects/ApplePMUFirmwareDriver.build/ApplePMUFirmwareDriver.build/DerivedSources/
+ /Library/Caches/com.apple.xbs/D117CB6F-A300-4F43-9158-222BD35FC4A0/TemporaryDirectory.8vL1hn/Binaries/ApplePMUFirmwareDriver/install/TempContent/Objects/ApplePMUFirmwareDriver.build/ApplePMUFirmwareDriver.build/Objects-normal/arm64e/ApplePMUFirmwareDriver.o
+ /Library/Caches/com.apple.xbs/D117CB6F-A300-4F43-9158-222BD35FC4A0/TemporaryDirectory.8vL1hn/Binaries/ApplePMUFirmwareDriver/install/TempContent/Objects/ApplePMUFirmwareDriver.build/ApplePMUFirmwareDriver.build/Objects-normal/arm64e/ApplePMUFirmwareDriverUserClient.o
+ /Library/Caches/com.apple.xbs/D117CB6F-A300-4F43-9158-222BD35FC4A0/TemporaryDirectory.8vL1hn/Binaries/ApplePMUFirmwareDriver/install/TempContent/Objects/ApplePMUFirmwareDriver.build/ApplePMUFirmwareDriver.build/Objects-normal/arm64e/ApplePMUFirmwareDriver_info.o
+ /Library/Caches/com.apple.xbs/D117CB6F-A300-4F43-9158-222BD35FC4A0/TemporaryDirectory.8vL1hn/Sources/ApplePMUFirmwareDriver/
- /Library/Caches/com.apple.xbs/Binaries/ApplePMUFirmwareDriver/install/TempContent/Objects/ApplePMUFirmwareDriver.build/ApplePMUFirmwareDriver.build/DerivedSources/
- /Library/Caches/com.apple.xbs/Binaries/ApplePMUFirmwareDriver/install/TempContent/Objects/ApplePMUFirmwareDriver.build/ApplePMUFirmwareDriver.build/Objects-normal/arm64e/ApplePMUFirmwareDriver.o
- /Library/Caches/com.apple.xbs/Binaries/ApplePMUFirmwareDriver/install/TempContent/Objects/ApplePMUFirmwareDriver.build/ApplePMUFirmwareDriver.build/Objects-normal/arm64e/ApplePMUFirmwareDriverUserClient.o
- /Library/Caches/com.apple.xbs/Binaries/ApplePMUFirmwareDriver/install/TempContent/Objects/ApplePMUFirmwareDriver.build/ApplePMUFirmwareDriver.build/Objects-normal/arm64e/ApplePMUFirmwareDriver_info.o
- /Library/Caches/com.apple.xbs/Sources/ApplePMUFirmwareDriver/
Functions:
~ __ZN32ApplePMUFirmwareDriverUserClient11clientCloseEv : 68 -> 60
+ _OUTLINED_FUNCTION_0
~ __ZN22ApplePMUFirmwareDriver5startEP9IOService : 2640 -> 2072
~ __ZN22ApplePMUFirmwareDriver13getDTPropertyItEEbP9IOServicePKcPT_ : 636 -> 512
~ __ZN22ApplePMUFirmwareDriver22handleMailboxInterruptEP22IOInterruptEventSourcei : 312 -> 276
~ __ZN22ApplePMUFirmwareDriver4freeEv : 236 -> 208
~ __ZN22ApplePMUFirmwareDriver18mailboxTransactionEP20PMUFWDMailboxMessageS1_ : 524 -> 452
~ __ZN22ApplePMUFirmwareDriver23mailboxTransactionGatedEP20PMUFWDMailboxMessageS1_ : 1340 -> 1148
~ __ZN22ApplePMUFirmwareDriver12writeHostIRQEh : 300 -> 264
~ __ZN22ApplePMUFirmwareDriver17writeHostIRQGatedEh : 140 -> 148
~ __ZN22ApplePMUFirmwareDriver11setCPMSRateEt : 260 -> 224
~ __ZN22ApplePMUFirmwareDriver24setCPMSVDDDroopThresholdEj : 288 -> 252
~ _OUTLINED_FUNCTION_1 : 16 -> 20
~ _OUTLINED_FUNCTION_3 : 12 -> 16
~ _OUTLINED_FUNCTION_4 : 16 -> 12
~ _OUTLINED_FUNCTION_5 : 12 -> 20
~ _OUTLINED_FUNCTION_6 : 12 -> 16
~ __ZN32ApplePMUFirmwareDriverUserClient5startEP9IOService : 392 -> 276
~ _ZN22ApplePMUFirmwareDriver5startEP9IOService.cold.1 : 184 -> 140
~ _ZN22ApplePMUFirmwareDriver5startEP9IOService.cold.2 : 188 -> 148
~ _ZN22ApplePMUFirmwareDriver5startEP9IOService.cold.3 : 180 -> 144
~ _ZN22ApplePMUFirmwareDriver5startEP9IOService.cold.4 : 184 -> 140
~ _ZN22ApplePMUFirmwareDriver5startEP9IOService.cold.5 : 184 -> 140
~ _ZN22ApplePMUFirmwareDriver18mailboxTransactionEP20PMUFWDMailboxMessageS1_.cold.1 : 188 -> 156
~ _ZN22ApplePMUFirmwareDriver23mailboxTransactionGatedEP20PMUFWDMailboxMessageS1_.cold.1 : 172 -> 128
~ _ZN22ApplePMUFirmwareDriver23mailboxTransactionGatedEP20PMUFWDMailboxMessageS1_.cold.2 : 172 -> 128
~ _ZN22ApplePMUFirmwareDriver23mailboxTransactionGatedEP20PMUFWDMailboxMessageS1_.cold.3 : 172 -> 128
~ _ZN22ApplePMUFirmwareDriver23mailboxTransactionGatedEP20PMUFWDMailboxMessageS1_.cold.4 : 188 -> 144
~ _ZN22ApplePMUFirmwareDriver23mailboxTransactionGatedEP20PMUFWDMailboxMessageS1_.cold.5 : 188 -> 144
~ _ZN22ApplePMUFirmwareDriver23mailboxTransactionGatedEP20PMUFWDMailboxMessageS1_.cold.6 : 196 -> 160
~ _ZN22ApplePMUFirmwareDriver17writeHostIRQGatedEh.cold.1 : 188 -> 160

```
