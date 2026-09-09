## ATCRTManager

> `/System/Library/Extensions/ATCRTManager.kext/ATCRTManager`

### Sections with Same Size but Changed Content

- `__DATA.__data`
- `__DATA_CONST.__mod_init_func`
- `__DATA_CONST.__mod_term_func`
- `__DATA_CONST.__const`

```diff

 4.0.2.0.0
   __TEXT.__cstring: 0x132a
   __TEXT.__const: 0x14
-  __TEXT_EXEC.__text: 0x3ea0
+  __TEXT_EXEC.__text: 0x3fa8
   __TEXT_EXEC.__auth_stubs: 0x2f0
   __DATA.__data: 0xc8
   __DATA.__common: 0x60
Functions:
~ __ZN12ATCRTManager9MetaClassC1Ev : 72 -> 76
~ __ZN12ATCRTManagerC2EPK11OSMetaClass : 52 -> 56
~ __ZN12ATCRTManagerC1EPK11OSMetaClass : 52 -> 56
~ __ZN12ATCRTManagerD0Ev : 68 -> 72
~ __ZN12ATCRTManager9MetaClassC2Ev : 72 -> 76
~ __ZNK12ATCRTManager9MetaClass5allocEv : 104 -> 108
~ __ZN12ATCRTManagerC1Ev : 88 -> 92
~ __ZN12ATCRTManagerC2Ev : 88 -> 92
~ __ZN12ATCRTManager5startEP9IOService : 2976 -> 2980
~ __ZN12ATCRTManager18pollStatusRegisterEP8OSObjectP18IOTimerEventSource : 212 -> 216
~ __ZN12ATCRTManager29processConnectionStateChangesEP8OSObjectP18IOTimerEventSource : 568 -> 572
~ __ZN12ATCRTManager32registerForTransportPublicationsEv : 304 -> 308
~ __ZN12ATCRTManager18transportPublishedEPvP9IOServiceP10IONotifier : 536 -> 540
~ __ZN12ATCRTManager16transportMessageEPvjP9IOServiceS0_m : 488 -> 492
~ __ZN12ATCRTManager24armConnectionChangeTimerEv : 96 -> 100
~ __ZN12ATCRTManager24captureTransportSnapshotEPNS_22TransportStateSnapshotE : 408 -> 412
~ __ZN12ATCRTManager23writeConnectionRegisterER28i2c_ap_register_connection_t : 200 -> 204
~ __ZN12ATCRTManager4stopEP9IOService : 972 -> 976
~ __ZN12ATCRTManager13setPowerStateEmP9IOService : 216 -> 220
~ __ZN12ATCRTManager13newUserClientEP4taskPvjPP12IOUserClient : 476 -> 480
~ __ZN12ATCRTManager20callPlatformFunctionEPK8OSSymbolbPvS3_S3_S3_ : 340 -> 344
~ __ZN12ATCRTManager7readRegEhPhyb : 248 -> 252
~ __ZN12ATCRTManager8writeRegEhPKhy : 244 -> 248
~ __ZN12ATCRTManager24updateConnectionFromDockEv : 100 -> 104
~ __ZN12ATCRTManager18handleStatusChangeE24i2c_ap_register_status_t : 136 -> 140
~ __ZN12ATCRTManager18handleRetimerErrorEv : 280 -> 284
~ __ZN12ATCRTManager18clearInterruptBitsE24i2c_ap_register_status_t : 212 -> 216
~ __ZN12ATCRTManager13putRetimerDFUEv : 144 -> 148
~ __ZN12ATCRTManager12resetRetimerEv : 144 -> 148
~ _GLOBAL__sub_I_ATCRTManager.cpp : 80 -> 84
~ __ZN22ATCRTManagerUserClient9MetaClassC1Ev : 72 -> 76
~ __ZN22ATCRTManagerUserClientC2EPK11OSMetaClass : 52 -> 56
~ __ZN22ATCRTManagerUserClientC1EPK11OSMetaClass : 52 -> 56
~ __ZN22ATCRTManagerUserClientD0Ev : 68 -> 72
~ __ZN22ATCRTManagerUserClient9MetaClassC2Ev : 72 -> 76
~ __ZNK22ATCRTManagerUserClient9MetaClass5allocEv : 104 -> 108
~ __ZN22ATCRTManagerUserClientC1Ev : 88 -> 92
~ __ZN22ATCRTManagerUserClientC2Ev : 88 -> 92
~ __ZN22ATCRTManagerUserClient12initWithTaskEP4taskPvjP12OSDictionary : 104 -> 108
~ __ZN22ATCRTManagerUserClient5startEP9IOService : 212 -> 216
~ __ZN22ATCRTManagerUserClient4stopEP9IOService : 96 -> 100
~ __ZN22ATCRTManagerUserClient11clientCloseEv : 144 -> 148
~ __ZN22ATCRTManagerUserClient10clientDiedEv : 108 -> 112
~ __ZN22ATCRTManagerUserClient14externalMethodEjP25IOExternalMethodArgumentsP24IOExternalMethodDispatchP8OSObjectPv : 548 -> 552
~ __ZN22ATCRTManagerUserClient18readStatusRegisterEPvP25IOExternalMethodArguments : 156 -> 160
~ __ZN22ATCRTManagerUserClient19writeStatusRegisterEPvP25IOExternalMethodArguments : 132 -> 136
~ __ZN22ATCRTManagerUserClient22readConnectionRegisterEPvP25IOExternalMethodArguments : 156 -> 160
~ __ZN22ATCRTManagerUserClient23writeConnectionRegisterEPvP25IOExternalMethodArguments : 156 -> 160
~ __ZN22ATCRTManagerUserClient18getFwVersionStringEPvP25IOExternalMethodArguments : 172 -> 176
~ __ZN22ATCRTManagerUserClient17getRetimerVersionEPvP25IOExternalMethodArguments : 156 -> 160
~ __ZN22ATCRTManagerUserClient24updateConnectionFromDockEPvP25IOExternalMethodArguments : 104 -> 108
~ _GLOBAL__sub_I_ATCRTManagerUserClient.cpp : 80 -> 84
~ __ZN12ATCRTManager18getFwVersionStringEPc : 108 -> 112
~ __ZN12ATCRTManager10takeoverRTEP18IOTimerEventSource : 400 -> 404
~ _ZN12ATCRTManager5startEP9IOService.cold.1 : 72 -> 76
~ _ZN12ATCRTManager5startEP9IOService.cold.2 : 72 -> 76
~ _ZN12ATCRTManager5startEP9IOService.cold.3 : 84 -> 88
~ _ZN12ATCRTManager5startEP9IOService.cold.4 : 84 -> 88
~ _ZN12ATCRTManager5startEP9IOService.cold.5 : 72 -> 76
~ _ZN12ATCRTManager5startEP9IOService.cold.6 : 84 -> 88
~ _ZN12ATCRTManager5startEP9IOService.cold.7 : 84 -> 88
~ _ZN12ATCRTManager5startEP9IOService.cold.8 : 72 -> 76
~ _ZN12ATCRTManager5startEP9IOService.cold.9 : 72 -> 76
~ _ZN12ATCRTManager5startEP9IOService.cold.10 : 72 -> 76
~ _ZN12ATCRTManager5startEP9IOService.cold.11 : 72 -> 76
~ _ZN12ATCRTManager18handleStatusChangeE24i2c_ap_register_status_t.cold.1 : 192 -> 196
```
