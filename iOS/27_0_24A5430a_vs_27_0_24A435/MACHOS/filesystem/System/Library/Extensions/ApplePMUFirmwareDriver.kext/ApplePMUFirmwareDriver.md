## ApplePMUFirmwareDriver

> `/System/Library/Extensions/ApplePMUFirmwareDriver.kext/ApplePMUFirmwareDriver`

### Sections with Same Size but Changed Content

- `__DATA.__data`
- `__DATA_CONST.__mod_init_func`
- `__DATA_CONST.__mod_term_func`
- `__DATA_CONST.__const`

```diff

 7.0.0.0.0
   __TEXT.__const: 0x18
   __TEXT.__cstring: 0x854
-  __TEXT_EXEC.__text: 0x288c
+  __TEXT_EXEC.__text: 0x2940
   __TEXT_EXEC.__auth_stubs: 0x1b0
   __DATA.__data: 0xc8
   __DATA.__common: 0x60
Functions:
~ __ZN32ApplePMUFirmwareDriverUserClient9MetaClassC1Ev : 72 -> 76
~ __ZN32ApplePMUFirmwareDriverUserClientC2EPK11OSMetaClass : 52 -> 56
~ __ZN32ApplePMUFirmwareDriverUserClientC1EPK11OSMetaClass : 52 -> 56
~ __ZN32ApplePMUFirmwareDriverUserClientD0Ev : 68 -> 72
~ __ZN32ApplePMUFirmwareDriverUserClient9MetaClassC2Ev : 72 -> 76
~ __ZNK32ApplePMUFirmwareDriverUserClient9MetaClass5allocEv : 104 -> 108
~ __ZN32ApplePMUFirmwareDriverUserClientC1Ev : 88 -> 92
~ __ZN32ApplePMUFirmwareDriverUserClientC2Ev : 88 -> 92
~ __ZN32ApplePMUFirmwareDriverUserClient11clientCloseEv : 60 -> 64
~ __ZN32ApplePMUFirmwareDriverUserClient14externalMethodEjP31IOExternalMethodArgumentsOpaque : 248 -> 252
~ __ZN32ApplePMUFirmwareDriverUserClient18mailboxTransactionEPvP25IOExternalMethodArguments : 96 -> 100
~ _GLOBAL__sub_I_ApplePMUFirmwareDriverUserClient.cpp : 80 -> 84
~ __ZN22ApplePMUFirmwareDriver9MetaClassC1Ev : 72 -> 76
~ __ZN22ApplePMUFirmwareDriverC2EPK11OSMetaClass : 52 -> 56
~ __ZN22ApplePMUFirmwareDriverC1EPK11OSMetaClass : 52 -> 56
~ __ZN22ApplePMUFirmwareDriverD0Ev : 68 -> 72
~ __ZN22ApplePMUFirmwareDriver9MetaClassC2Ev : 72 -> 76
~ __ZNK22ApplePMUFirmwareDriver9MetaClass5allocEv : 104 -> 108
~ __ZN22ApplePMUFirmwareDriverC1Ev : 88 -> 92
~ __ZN22ApplePMUFirmwareDriverC2Ev : 88 -> 92
~ __ZN22ApplePMUFirmwareDriver5startEP9IOService : 2072 -> 2076
~ __ZN22ApplePMUFirmwareDriver13getDTPropertyItEEbP9IOServicePKcPT_ : 512 -> 516
~ __ZN22ApplePMUFirmwareDriver22handleMailboxInterruptEP22IOInterruptEventSourcei : 276 -> 280
~ __ZN22ApplePMUFirmwareDriver4freeEv : 208 -> 212
~ __ZN22ApplePMUFirmwareDriver18mailboxTransactionEP20PMUFWDMailboxMessageS1_ : 452 -> 456
~ __ZN22ApplePMUFirmwareDriver23mailboxTransactionGatedEP20PMUFWDMailboxMessageS1_ : 1148 -> 1152
~ __ZN22ApplePMUFirmwareDriver12writeHostIRQEh : 264 -> 268
~ __ZN22ApplePMUFirmwareDriver17writeHostIRQGatedEh : 148 -> 152
~ __ZN22ApplePMUFirmwareDriver11setCPMSRateEt : 224 -> 228
~ __ZN22ApplePMUFirmwareDriver24setCPMSVDDDroopThresholdEj : 252 -> 256
~ _GLOBAL__sub_I_ApplePMUFirmwareDriver.cpp : 160 -> 164
~ __ZN32ApplePMUFirmwareDriverUserClient12initWithTaskEP4taskPvjP12OSDictionary : 92 -> 96
~ __ZN32ApplePMUFirmwareDriverUserClient5startEP9IOService : 276 -> 280
~ _ZN22ApplePMUFirmwareDriver5startEP9IOService.cold.1 : 140 -> 144
~ _ZN22ApplePMUFirmwareDriver5startEP9IOService.cold.2 : 148 -> 152
~ _ZN22ApplePMUFirmwareDriver5startEP9IOService.cold.3 : 144 -> 148
~ _ZN22ApplePMUFirmwareDriver5startEP9IOService.cold.4 : 140 -> 144
~ _ZN22ApplePMUFirmwareDriver5startEP9IOService.cold.5 : 140 -> 144
~ _ZN22ApplePMUFirmwareDriver18mailboxTransactionEP20PMUFWDMailboxMessageS1_.cold.1 : 156 -> 160
~ _ZN22ApplePMUFirmwareDriver23mailboxTransactionGatedEP20PMUFWDMailboxMessageS1_.cold.1 : 128 -> 132
~ _ZN22ApplePMUFirmwareDriver23mailboxTransactionGatedEP20PMUFWDMailboxMessageS1_.cold.2 : 128 -> 132
~ _ZN22ApplePMUFirmwareDriver23mailboxTransactionGatedEP20PMUFWDMailboxMessageS1_.cold.3 : 128 -> 132
~ _ZN22ApplePMUFirmwareDriver23mailboxTransactionGatedEP20PMUFWDMailboxMessageS1_.cold.4 : 144 -> 148
~ _ZN22ApplePMUFirmwareDriver23mailboxTransactionGatedEP20PMUFWDMailboxMessageS1_.cold.5 : 144 -> 148
~ _ZN22ApplePMUFirmwareDriver23mailboxTransactionGatedEP20PMUFWDMailboxMessageS1_.cold.6 : 160 -> 164
```
