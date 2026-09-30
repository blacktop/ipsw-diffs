## com.apple.iokit.IOFireWireAVC

> `com.apple.iokit.IOFireWireAVC`

```diff

 434.0.0.0.0
-  __TEXT.__const: 0x10
+  __TEXT.__const: 0x8
   __TEXT.__cstring: 0x788
-  __TEXT_EXEC.__text: 0x10b18
+  __TEXT_EXEC.__text: 0x10df4
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x3a0

   __DATA_CONST.__mod_term_func: 0x30
   __DATA_CONST.__const: 0x52d0
   __DATA_CONST.__kalloc_type: 0x540
-  UUID: 6F3FA975-C376-301B-949F-D2C7AD1804A0
-  Functions: 459
-  Symbols:   1001
+  UUID: 9F5468F1-38B4-3345-AD89-6C4BC2516745
+  Functions: 457
+  Symbols:   999
   CStrings:  64
 
Symbols:
- _ZN31IOFireWireAVCProtocolUserClient23avcTargetCommandHandlerEPK21AVCCommandHandlerInfojtPKvjR9IOFWSpeedj.cold.1
- _ZN31IOFireWireAVCProtocolUserClient23avcTargetCommandHandlerEPK21AVCCommandHandlerInfojtPKvjR9IOFWSpeedj.cold.2
Functions:
~ __ZN32IOFireWireAVCAsynchronousCommand4freeEv : 508 -> 512
~ __ZN32IOFireWireAVCAsynchronousCommand6submitEP16IOFireWireAVCNub : 808 -> 788
~ __ZN17IOFireWireAVCUnit14updateSubUnitsEb : 2152 -> 2204
~ __ZN17IOFireWireAVCUnit5startEP9IOService : 2176 -> 2132
~ __ZN17IOFireWireAVCUnit4freeEv : 584 -> 608
~ __ZN17IOFireWireAVCUnit18matchPropertyTableEP12OSDictionary : 472 -> 464
~ __ZN17IOFireWireAVCUnit10AVCCommandEPKhjPhPj : 424 -> 464
~ __ZN17IOFireWireAVCUnit22AVCCommandInGenerationEjPKhjPhPj : 264 -> 272
~ __ZN20IOFireWireAVCCommand14handleResponseEtjPKv : 452 -> 476
~ __ZN20IOFireWireAVCCommand4freeEv : 396 -> 400
~ __ZN20IOFireWireAVCCommand7executeEv : 120 -> 128
~ __ZN20IOFireWireAVCCommand4initEP13IOFireWireNubPKhjPhPj : 592 -> 600
~ __ZN25IOFireWireAVCCommandInGen4initEP13IOFireWireNubjPKhjPhPj : 664 -> 672
~ __ZN18IOFireWirePCRSpace7doWriteEtR9IOFWSpeed15FWAddressStructjPKvPv : 444 -> 424
~ __ZN18IOFireWirePCRSpace10deactivateEv : 132 -> 144
~ __ZN18IOFireWirePCRSpace22clearAllP2PConnectionsEv : 376 -> 392
~ __ZN23IOFireWireAVCUserClient4freeEv : 440 -> 444
~ __ZN23IOFireWireAVCUserClient4stopEP9IOService : 504 -> 524
~ __ZN23IOFireWireAVCUserClient11clientCloseEv : 160 -> 164
~ __ZN23IOFireWireAVCUserClient13getSessionRefEPyPvS1_S1_S1_S1_ : 44 -> 48
~ __ZN23IOFireWireAVCUserClient5closeEPvS0_S0_S0_S0_S0_ : 188 -> 200
~ __ZN23IOFireWireAVCUserClient10AVCCommandEPhS0_jPj : 88 -> 92
~ __ZN23IOFireWireAVCUserClient15AVCCommandInGenEPhS0_jPj : 112 -> 116
~ __ZN23IOFireWireAVCUserClient23updateAVCCommandTimeoutEPvS0_S0_S0_S0_S0_ : 92 -> 104
~ __ZN23IOFireWireAVCUserClient14updateP2PCountEjibj9IOFWSpeed : 780 -> 836
~ __ZN23IOFireWireAVCUserClient7messageEjP9IOServicePv : 152 -> 164
~ __ZN23IOFireWireAVCUserClient37installUserLibAsyncAVCCommandCallbackEPyyS0_ : 60 -> 68
~ __ZN23IOFireWireAVCUserClient21CreateAVCAsyncCommandEPhS0_jPj : 764 -> 788
~ __ZN23IOFireWireAVCUserClient22ReleaseAVCAsyncCommandEj : 488 -> 508
~ __ZN23IOFireWireAVCUserClient28HandleUCAsyncCommandCallbackEP35IOFireWireAVCUserClientAsyncCommand : 344 -> 304
~ __ZN31IOFireWireAVCProtocolUserClient23avcTargetCommandHandlerEPK21AVCCommandHandlerInfojtPKvjR9IOFWSpeedj : 492 -> 496
~ __ZN31IOFireWireAVCProtocolUserClient21avcSubunitPlugHandlerEPK14AVCSubunitInfo26IOFWAVCSubunitPlugMessages16IOFWAVCPlugTypesjjjt : 184 -> 192
~ __ZN31IOFireWireAVCProtocolUserClient4freeEv : 1012 -> 1056
~ __ZN31IOFireWireAVCProtocolUserClient13newUserClientEP4taskPvjP12OSDictionaryPP12IOUserClient : 276 -> 284
~ __ZN14AVCSubunitInfo6createEv : 192 -> 212
~ __ZN14AVCSubunitInfo4initEv : 28 -> 32
~ __ZN14AVCSubunitInfo4freeEv : 96 -> 100
~ __ZN24IOFireWireAVCTargetSpace21handleUnitInfoCommandEtjPKcj : 452 -> 456
~ __ZN24IOFireWireAVCTargetSpace24handleSubUnitInfoCommandEtjPKcj : 688 -> 696
~ __ZN24IOFireWireAVCTargetSpace20handleConnectCommandEtjPKcj : 1176 -> 1192
~ __ZN24IOFireWireAVCTargetSpace23handleDisconnectCommandEtjPKcj : 492 -> 488
~ __ZN24IOFireWireAVCTargetSpace34handleInputPlugSignalFormatCommandEtjPKcj : 692 -> 704
~ __ZN24IOFireWireAVCTargetSpace35handleOutputPlugSignalFormatCommandEtjPKcj : 692 -> 704
~ __ZN24IOFireWireAVCTargetSpace24handleConnectionsCommandEtjPKcj : 524 -> 532
~ __ZN24IOFireWireAVCTargetSpace21handlePlugInfoCommandEtjPKcj : 480 -> 484
~ __ZN24IOFireWireAVCTargetSpace24deactivateWithUserClientEP31IOFireWireAVCProtocolUserClient : 1732 -> 1876
~ __ZN24IOFireWireAVCTargetSpace24installAVCCommandHandlerEP31IOFireWireAVCProtocolUserClientPFvPK21AVCCommandHandlerInfojtPKvjR9IOFWSpeedjEPyjjyy : 332 -> 360
~ __ZN24IOFireWireAVCTargetSpace10addSubunitEP31IOFireWireAVCProtocolUserClientPFvPK14AVCSubunitInfo26IOFWAVCSubunitPlugMessages16IOFWAVCPlugTypesjjjtEPyjjjyyPj : 504 -> 520
~ __ZN24IOFireWireAVCTargetSpace26setSubunitPlugSignalFormatEP31IOFireWireAVCProtocolUserClientj16IOFWAVCPlugTypesjj : 200 -> 204
~ __ZN24IOFireWireAVCTargetSpace26getSubunitPlugSignalFormatEP31IOFireWireAVCProtocolUserClientj16IOFWAVCPlugTypesjPj : 184 -> 188
~ __ZN24IOFireWireAVCTargetSpace18connectTargetPlugsEP31IOFireWireAVCProtocolUserClientP30_AVCConnectTargetPlugsInParamsP31_AVCConnectTargetPlugsOutParams : 2000 -> 2028
~ __ZN24IOFireWireAVCTargetSpace21disconnectTargetPlugsEP31IOFireWireAVCProtocolUserClientj16IOFWAVCPlugTypesjjS2_j : 708 -> 808
~ __ZN24IOFireWireAVCTargetSpace23getTargetPlugConnectionEP31IOFireWireAVCProtocolUserClientP35_AVCGetTargetPlugConnectionInParamsP36_AVCGetTargetPlugConnectionOutParams : 440 -> 460

```
