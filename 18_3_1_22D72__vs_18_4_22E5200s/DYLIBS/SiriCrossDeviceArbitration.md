## SiriCrossDeviceArbitration

> `/System/Library/PrivateFrameworks/SiriCrossDeviceArbitration.framework/SiriCrossDeviceArbitration`

```diff

-3402.17.1.0.0
-  __TEXT.__text: 0x2f99c
-  __TEXT.__auth_stubs: 0x840
-  __TEXT.__objc_methlist: 0x2ae4
-  __TEXT.__const: 0x198
-  __TEXT.__gcc_except_tab: 0x488
-  __TEXT.__oslogstring: 0x49eb
-  __TEXT.__cstring: 0x59a7
+3404.29.1.0.0
+  __TEXT.__text: 0x2ffdc
+  __TEXT.__auth_stubs: 0x850
+  __TEXT.__objc_methlist: 0x2fbc
   __TEXT.__dlopen_cstrs: 0x164
-  __TEXT.__unwind_info: 0xce8
-  __TEXT.__objc_classname: 0x68e
-  __TEXT.__objc_methname: 0x79f6
-  __TEXT.__objc_methtype: 0x18f1
-  __TEXT.__objc_stubs: 0x5920
-  __DATA_CONST.__got: 0x308
+  __TEXT.__const: 0x1d0
+  __TEXT.__gcc_except_tab: 0x490
+  __TEXT.__oslogstring: 0x4bb4
+  __TEXT.__cstring: 0x5a30
+  __TEXT.__unwind_info: 0xcf8
+  __TEXT.__objc_classname: 0x697
+  __TEXT.__objc_methname: 0x7bcd
+  __TEXT.__objc_methtype: 0x1923
+  __TEXT.__objc_stubs: 0x5aa0
+  __DATA_CONST.__got: 0x310
   __DATA_CONST.__const: 0x10f8
-  __DATA_CONST.__objc_classlist: 0x160
+  __DATA_CONST.__objc_classlist: 0x168
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1c10
-  __DATA_CONST.__objc_superrefs: 0x148
+  __DATA_CONST.__objc_selrefs: 0x1cf8
+  __DATA_CONST.__objc_superrefs: 0x150
   __DATA_CONST.__objc_arraydata: 0x148
-  __AUTH_CONST.__auth_got: 0x430
+  __AUTH_CONST.__auth_got: 0x438
   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__const: 0x320
-  __AUTH_CONST.__cfstring: 0x2720
-  __AUTH_CONST.__objc_const: 0x5e00
+  __AUTH_CONST.__cfstring: 0x26a0
+  __AUTH_CONST.__objc_const: 0x5810
   __AUTH_CONST.__objc_intobj: 0x2b8
   __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH_CONST.__objc_arrayobj: 0xd8
-  __DATA.__objc_ivar: 0x544
+  __AUTH.__objc_data: 0x50
+  __DATA.__objc_ivar: 0x53c
   __DATA.__data: 0x6a8
-  __DATA.__bss: 0xc8
+  __DATA.__bss: 0x198
   __DATA_DIRTY.__objc_data: 0xdc0
-  __DATA_DIRTY.__bss: 0xd8
+  __DATA_DIRTY.__bss: 0x8
   __DATA_DIRTY.__common: 0x10
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 1162
-  Symbols:   1495
-  CStrings:  2572
+  Functions: 1174
+  Symbols:   1513
+  CStrings:  2603
 
Symbols:
+ _OBJC_CLASS_$_SCDADevice
+ _OBJC_METACLASS_$_SCDADevice
+ _objc_retain_x27
- _SCDAProductType
- _hammingDistance
CStrings:
+ "%s #scda Voice trigger with active record, using original with adjusted TB: %@"
+ "%s #scda _shouldUseContextCollector is false"
+ "%s #scda adv dispatch time: %f, voice trigger end time: %f, time since voice trigger: %f (curr time: %llu, time since device boot: %llu), advertisement: %@"
+ "%s #scda attention boost arrived with nil _triggerRecord, likely Siri was dismissed already."
+ "%s #scda clearing trigger record"
+ "%s #scda leaving existing trump signal intact %d"
+ "%s %@, vt_endtime threshold %f"
+ "%s BTLE Updating record table with a late suppression ( %hhu -> %hhu), data= %@, for %@"
+ "%s BTLE daemon wiprox state signaling"
+ "%s BTLE setup-mode voice trigger heard"
+ "%s BTLE startFromVoiceTrigger inTask=REMOVED, inSetupMode=%d, context=%@"
+ "%s BTLE startFromVoiceTrigger inTask=REMOVED, inSetupMode=%d, incomingAdjustment=%d,  context=%@, goodnessScoreContext=%@"
+ "%s Clearing trigger record"
+ "%s In-task trigger detected while direct activating. We shouldn't demote direct triggers."
+ "%s Myriad _inTask is removed. This method is deprecated and always returns NO."
+ "%s Myriad _inTask is removed. This method is deprecated and does nothing."
+ "%s Skipping advertising requested with nil _triggerRecord %@"
+ "%s Unexpectedly lowering goodness score %du for in ear trigger"
+ "%s canceling advertising with nil trigger record, this likely means Siri UI was already dismissed %@"
+ "-[SCDACoordinator _startAdvertisingFromSetupMode]"
+ "-[SCDACoordinator inTask]"
+ "-[SCDACoordinator setInTask:]"
+ "77\x11Q\x117\x11B\x12\x1c\x12\x15"
+ "@\"SCDADevice\""
+ "@40@0:8C16@20C28@32"
+ "BTLE device class: %@ (%hhu), productType: %@ (%hhu), device adjust: %hhd, trump delay %0.3f"
+ "BTLE end advertising.\nPotential winner = %{public}@\nSummary: %{public}@"
+ "Overriden Device"
+ "Overriden Product"
+ "SCDADevice"
+ "T@\"NSString\",R,N,V_deviceClassName"
+ "T@\"NSString\",R,N,V_productTypeName"
+ "Tc,R,N,V_deviceAdjust_DEPRECATED"
+ "Td,R,N,V_inEarDelay"
+ "Td,R,N,V_inEarInterval"
+ "Td,R,N,V_trumpDelay"
+ "Ti,R,N"
+ "_advertisementPayloadSizeForVersion:"
+ "_createEndAnalyticContextFromIntermediateContext:forVersion:sessionId:"
+ "_device"
+ "_getAdvertisementRecordTypeForVersion:data:"
+ "_getDeviceAdjust_DEPRECATED"
+ "_getDeviceClass"
+ "_getInEarDelay"
+ "_getInEarInterval"
+ "_getProductType"
+ "_getTrumpDelay"
+ "_inEarDelay"
+ "_inEarInterval"
+ "_startAdvertisingFromSetupMode"
+ "_trumpDelay"
+ "c"
+ "c16@0:8"
+ "cdaDeviceClass"
+ "cdaDeviceClassForSCDADeviceClass:andProducType:"
+ "deviceAdjust_DEPRECATED"
+ "deviceClassName"
+ "hasEqualAdvertisementData:"
+ "inEarDelay"
+ "inEarInterval"
+ "initWithDeviceClass:deviceClassName:productType:productTypeName:"
+ "isALateSuppressionTrumpFor:"
+ "myriadCoordinator:didReceiveAdvertisement:"
+ "overrideLocalConfiguration:deviceAdjust:trumpDelay:"
+ "productTypeName"
+ "scdaRequestTypeContinuousVoiceTrigger"
+ "trumpDelay"
+ "v32@0:8C16c20d24"
+ "winner_sent_suppression"
- "%s #scda _shouldUseContextCollector is fslse"
- "%s #scda adv dispatch time: %f, voice trigger end time: %f, time since voice trigger: %f (curr time: %llu, time since device boot: %llu), advertisment: %@"
- "%s #scda reading defaults: BTLE device class: %@ (%@) detected, category %ld, adjusting goodness by %ld, std delay %f, trump delay %f, vt_endtime threshold %f"
- "%s BTLE Updating record table with a late supression ( %hhu -> %hhu), data= %@, for %@"
- "%s BTLE daemon wiprox state signalling"
- "%s BTLE device class: %@ (%@) detected, category %ld, adjusting goodness by %ld, std delay %f, trump delay %f, in_ear delay %f interval %f vt_endtime threshold %f"
- "%s BTLE editDist: %d > allowed, ignoring this advert "
- "%s BTLE startFromVoiceTrigger inTask=%d, inSetupMode=%d, context=%@"
- "%s BTLE startFromVoiceTrigger inTask=%d, inSetupMode=%d, incomingAdjustment=%d,  context=%@, goodnessScoreContext=%@"
- "%s inTask=%d"
- "-[SCDACoordinator setInTask:]_block_invoke"
- "7\x11\x11w\x11Q\x117\x11B\x12\x1c\x12\x14"
- "AppleTV"
- "AudioAccessory"
- "B20@0:8C16"
- "BTLE end advertising.\nPotential winner = %@\nSummary: %@"
- "Bridge"
- "Watch"
- "_advertismentPayloadSizeForVersion:"
- "_cdaParticipantForDeviceClass:andProducType:"
- "_createEndAnalyticContexFromIntermediateContext:forVersion:sessionId:"
- "_deviceDelay"
- "_deviceInEarDelay"
- "_deviceInEarInterval"
- "_deviceTrumpDelay"
- "_getAdvertismentRecordTypeForVersion:data:"
- "_ignoreInTaskTimer"
- "_inTask"
- "_isAPhone:"
- "hasEqualAdvertismentData:"
- "iPad"
- "iPhone"
- "iPod"
- "isALateSupressionTrumpFor:"
- "myriadCoordinator:didReceiveAdvertisment:"
- "scdaRequestTypeContiniousVoiceTrigger"
- "valueForKey:"
- "winner_sent_suppresssion"

```
