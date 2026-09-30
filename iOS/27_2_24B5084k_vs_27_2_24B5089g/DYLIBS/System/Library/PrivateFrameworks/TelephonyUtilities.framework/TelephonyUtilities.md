## TelephonyUtilities

> `/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`

```diff

-1626.200.53.0.0
-  __TEXT.__text: 0x1ac9e4
-  __TEXT.__objc_methlist: 0x1ba28
-  __TEXT.__cstring: 0x14546
-  __TEXT.__const: 0x4acc
-  __TEXT.__oslogstring: 0x14857
+1626.200.65.0.0
+  __TEXT.__text: 0x1ad1f4
+  __TEXT.__objc_methlist: 0x1ba80
+  __TEXT.__cstring: 0x14616
+  __TEXT.__const: 0x4adc
+  __TEXT.__oslogstring: 0x14877
   __TEXT.__gcc_except_tab: 0x183c
   __TEXT.__ustring: 0xde
   __TEXT.__dlopen_cstrs: 0x8a5

   __TEXT.__swift_as_cont: 0x194
   __TEXT.__swift5_protos: 0x14
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x9628
+  __TEXT.__unwind_info: 0x9640
   __TEXT.__eh_frame: 0x2a78
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x3898
+  __DATA_CONST.__const: 0x3910
   __DATA_CONST.__objc_classlist: 0x8a8
   __DATA_CONST.__objc_catlist: 0xc0
   __DATA_CONST.__objc_protolist: 0x410
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb890
+  __DATA_CONST.__objc_selrefs: 0xb8c0
   __DATA_CONST.__objc_protorefs: 0x110
   __DATA_CONST.__objc_superrefs: 0x6e8
   __DATA_CONST.__objc_arraydata: 0xac0
   __DATA_CONST.__got: 0x10b0
   __AUTH_CONST.__const: 0x4dd8
-  __AUTH_CONST.__cfstring: 0x127a0
-  __AUTH_CONST.__objc_const: 0x2b598
+  __AUTH_CONST.__cfstring: 0x12820
+  __AUTH_CONST.__objc_const: 0x2b648
   __AUTH_CONST.__objc_intobj: 0x570
   __AUTH_CONST.__objc_doubleobj: 0x40
   __AUTH_CONST.__objc_arrayobj: 0x2e8
   __AUTH_CONST.__auth_got: 0x1690
-  __AUTH.__objc_data: 0x3228
-  __AUTH.__data: 0xde8
-  __DATA.__objc_ivar: 0x1940
-  __DATA.__data: 0x3f10
+  __AUTH.__objc_data: 0x2b70
+  __AUTH.__data: 0xde0
+  __DATA.__objc_ivar: 0x194c
+  __DATA.__data: 0x3f20
   __DATA.__common: 0xb0
-  __DATA_DIRTY.__objc_data: 0x26f0
-  __DATA_DIRTY.__data: 0x58
+  __DATA_DIRTY.__objc_data: 0x2da8
+  __DATA_DIRTY.__data: 0x78
   __DATA_DIRTY.__bss: 0x1e8
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CallKit.framework/CallKit

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 11970
-  Symbols:   20684
-  CStrings:  4668
+  Functions: 11979
+  Symbols:   20704
+  CStrings:  4673
 
Symbols:
+ -[TUCall relayHostCallScreeningEligibility]
+ -[TUIDSLookupManager lastForcedQueryTimestamps]
+ -[TUSimulatedIDSIDQueryController _currentCachedRemoteDevicesForDestinations:service:preferredFromID:listenerID:]
+ -[TUSimulatedIDSIDQueryController currentRemoteDevicesForDestinations:service:preferredFromID:listenerID:queue:completionBlockWithError:]
+ -[TUSimulatedParticipantUpdate isVideoEnabled]
+ -[TUSimulatedParticipantUpdate setVideoEnabled:]
+ _OBJC_IVAR_$_TUCall._relayHostCallScreeningEligibility
+ _OBJC_IVAR_$_TUIDSLookupManager._lastForcedQueryTimestamps
+ _OBJC_IVAR_$_TUSimulatedParticipantUpdate._videoEnabled
+ ___58-[TUIDSLookupManager beginQueryWithDestination:onService:]_block_invoke_2
+ ___58-[TUIDSLookupManager beginQueryWithDestination:onService:]_block_invoke_3
+ ___block_descriptor_40_e8_32s_e33_B32?0"NSString"8"NSDate"16^B24ls32l8
+ ___block_descriptor_56_e8_32s40s48s_e22_v16?0"NSDictionary"8ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56s_e22_v16?0"NSDictionary"8ls32l8s40l8s48l8s56l8
+ ___block_descriptor_80_e8_32s40s48s56s64s72bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8
+ __endpointsDictionaryForDestinations
+ _objc_msgSend$_currentCachedRemoteDevicesForDestinations:service:preferredFromID:listenerID:
+ _objc_msgSend$keysOfEntriesPassingTest:
+ _objc_msgSend$lastForcedQueryTimestamps
+ _objc_msgSend$relayHostCallScreeningEligibility
+ _objc_msgSend$removeObjectsForKeys:
- ___block_descriptor_56_e8_32s40s48bs_e22_v16?0"NSDictionary"8ls32l8s40l8s48l8
CStrings:
+ " rhse=%ld"
+ "B32@?0@\"NSString\"8@\"NSDate\"16^B24"
+ "Companion Software Not Compatible"
+ "The companion device could not complete the operation because it is on an incompatible software version."
+ "isEligibleForScreening: YES because the host device reported this relay call as eligible"
+ "relayHostCallScreeningEligibility"
+ "smartHoldingAvailability=%i, callSupportsScreening=%i validRemoteParticipantCount=%i validNotConferenced=%i, validSystemProvider=%i, validNotEmergencyCall=%i, validCallStatus=%i(%i), validEndpointOnCurrentDevice=%i, validIsNotVideo=%i, validLocale=%i(%@), validCaptioningAvailable=%i, isGASRAvailable=%i, validLockdownMode=%i, qfaLocaleExpansionEnabled=%i, qfaLocaleExpansionItPtEnabled=%i"
- "isEligibleForScreening: YES because it is a relay call that can screen"
- "smartHoldingAvailability=%i, validRemoteParticipantCount=%i validNotConferenced=%i, validSystemProvider=%i, validNotEmergencyCall=%i, validCallStatus=%i(%i), validEndpointOnCurrentDevice=%i, validIsNotVideo=%i, validLocale=%i(%@), validCaptioningAvailable=%i, isGASRAvailable=%i, validLockdownMode=%i, qfaLocaleExpansionEnabled=%i, qfaLocaleExpansionItPtEnabled=%i"
```
