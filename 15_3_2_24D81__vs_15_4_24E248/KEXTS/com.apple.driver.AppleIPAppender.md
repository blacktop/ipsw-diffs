## com.apple.driver.AppleIPAppender

> `com.apple.driver.AppleIPAppender`

```diff

 122.0.0.0.0
   __TEXT.__cstring: 0x63c
-  __TEXT.__const: 0x20
-  __TEXT_EXEC.__text: 0x57b0
+  __TEXT.__const: 0x30
+  __TEXT_EXEC.__text: 0x58e0
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc9
   __DATA.__common: 0x120

   __DATA_CONST.__const: 0x1970
   __DATA_CONST.__kalloc_type: 0x280
   __DATA_CONST.__kalloc_var: 0xf0
-  UUID: 6E832153-E810-3181-8926-180CE807E30E
+  UUID: D6C54145-BE1D-3C7F-A981-B696A01ABD53
   Functions: 168
   Symbols:   588
   CStrings:  47
Functions:
~ __ZN22AppleIPDormancyHandler4initEP10IOWorkLoop : 268 -> 300
~ __ZN22AppleIPDormancyHandler16setDormancyGatedEjj : 76 -> 88
~ __ZN22AppleIPDormancyHandler4freeEv : 280 -> 304
~ __ZN22AppleIPDormancyHandler24updateDormancyDataActiveEj : 120 -> 132
~ __ZN22AppleIPDormancyHandler13enterLowPowerEv : 136 -> 140
~ __ZN25AppleIPAppenderUserClient4freeEv : 104 -> 108
~ __ZN25AppleIPAppenderUserClient14externalMethodEjP25IOExternalMethodArgumentsP24IOExternalMethodDispatchP8OSObjectPv : 64 -> 84
~ __ZN25AppleIPAppenderUserClient16extGetWakeBufferEP15AppleIPAppenderPvP25IOExternalMethodArguments : 96 -> 100
~ __ZN25AppleIPAppenderUserClient26registerFilterRuleCallbackEPS_PvS1_Py : 416 -> 456
~ __ZN15AppleIPAppender13inPacketGatedEP25IOSkywalkNetworkInterfaceP22IOSkywalkNetworkPacket : 684 -> 680
~ __ZN15AppleIPAppender14getStatusGatedEP23AppleIPAppenderStatus_t : 168 -> 164
~ __ZN15AppleIPAppender18setPowerStateGatedEmP9IOService : 320 -> 328
~ __ZN15AppleIPAppender25setLinkQualityMetricGatedEi : 252 -> 248
~ __ZN15AppleIPAppender20reportLinkSpeedGatedEPK27AppleIPAppenderThroughput_t : 148 -> 144
~ __ZN15AppleIPAppender26setIONetworkInterfaceGatedEP18IONetworkInterfaceb : 520 -> 516
~ __ZN15AppleIPAppender24setSkywalkInterfaceGatedEP25IOSkywalkNetworkInterfaceb : 520 -> 524
~ __ZN15AppleIPAppender20getOpenPortsGatedExtEP25AppleIPAppenderPortInfo_tPhPm : 456 -> 452
~ __ZN15AppleIPAppender37enableLowPowerPDPThrottleFeatureGatedEb : 48 -> 60
~ __ZN15AppleIPAppender32activateLowPowerPDPThrottleGatedEb : 36 -> 48
~ __ZN15AppleIPAppender35getNumLowPowerPDPThrottleStatsGatedEP33AppleIPAppenderPDPThrottleStats_t : 48 -> 52
~ __ZN15AppleIPAppender31shouldBlockOutgoingTrafficGatedEj : 60 -> 64
~ __ZN15AppleIPAppender20blockPDPTrafficGatedEjb : 140 -> 148
~ __ZN15AppleIPAppender30getKeepaliveOffloadFramesGatedEjP38AppleIPAppenderKeepaliveOffloadFrame_tPj : 572 -> 552
~ __ZN15AppleIPAppender4freeEv : 308 -> 312
~ __ZN15AppleIPAppender5startEP9IOService : 428 -> 540
~ __ZN15AppleIPAppender6initPMEP9IOService : 316 -> 332
~ __ZN15AppleIPAppender4stopEP9IOService : 244 -> 248
~ __ZN15AppleIPAppender18throttlePDPTrafficEb : 128 -> 132
~ __ZN15AppleIPAppender18wasWokenByBasebandEv : 240 -> 244

```
