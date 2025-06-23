## PowerUI

> `/System/Library/PrivateFrameworks/PowerUI.framework/PowerUI`

```diff

-684.0.0.0.0
-  __TEXT.__text: 0xc17f8
+691.0.0.0.0
+  __TEXT.__text: 0xc20e0
   __TEXT.__auth_stubs: 0xaf0
-  __TEXT.__objc_methlist: 0x1b664
-  __TEXT.__const: 0x528
-  __TEXT.__cstring: 0xe082
-  __TEXT.__oslogstring: 0xba6d
+  __TEXT.__objc_methlist: 0x1b6cc
+  __TEXT.__const: 0x520
+  __TEXT.__cstring: 0xe0bb
+  __TEXT.__oslogstring: 0xbcbb
   __TEXT.__gcc_except_tab: 0x125c
-  __TEXT.__unwind_info: 0x1cc8
+  __TEXT.__unwind_info: 0x1ce0
   __TEXT.__objc_classname: 0xb55
-  __TEXT.__objc_methname: 0x3e11d
+  __TEXT.__objc_methname: 0x3e2bb
   __TEXT.__objc_methtype: 0x40f1
-  __TEXT.__objc_stubs: 0xc9e0
+  __TEXT.__objc_stubs: 0xca60
   __DATA_CONST.__got: 0x500
   __DATA_CONST.__const: 0x14c0
   __DATA_CONST.__objc_classlist: 0x2f8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x53d8
+  __DATA_CONST.__objc_selrefs: 0x5420
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x2d0
   __DATA_CONST.__objc_arraydata: 0x6f48
   __AUTH_CONST.__auth_got: 0x588
   __AUTH_CONST.__const: 0x640
-  __AUTH_CONST.__cfstring: 0xbd00
-  __AUTH_CONST.__objc_const: 0x363c0
+  __AUTH_CONST.__cfstring: 0xbd60
+  __AUTH_CONST.__objc_const: 0x36450
   __AUTH_CONST.__objc_intobj: 0x960
   __AUTH_CONST.__objc_arrayobj: 0x3a8
   __AUTH_CONST.__objc_doubleobj: 0xd0
   __AUTH_CONST.__objc_dictobj: 0x280
   __AUTH.__objc_data: 0x1400
-  __DATA.__objc_ivar: 0x3c1c
+  __DATA.__objc_ivar: 0x3c28
   __DATA.__data: 0x6c8
-  __DATA.__bss: 0xc0
+  __DATA.__bss: 0xd8
   __DATA_DIRTY.__objc_data: 0x9b0
   __DATA_DIRTY.__data: 0x20
   __DATA_DIRTY.__bss: 0x1a0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4CD90FC9-821E-369A-9202-A589CAA49805
-  Functions: 9778
-  Symbols:   26831
-  CStrings:  8860
+  UUID: 902FA9B9-C5DD-3B48-B778-B094B42C270C
+  Functions: 9796
+  Symbols:   26875
+  CStrings:  8887
 
Symbols:
+ +[PowerUICECUtilities resetStateOnUnplug]
+ +[PowerUICECUtilities resetStateOnUnplug].cold.1
+ -[PowerUIDemoCECManager checkPluggedInState]
+ -[PowerUIDemoCECManager queryForecastTimer]
+ -[PowerUIDemoCECManager registerCleanSegmentTimer:afterTime:withInterval:]
+ -[PowerUIDemoCECManager registerCleanSegmentTimer:afterTime:withInterval:].cold.1
+ -[PowerUIDemoCECManager registerCleanSegmentTimer]
+ -[PowerUIDemoCECManager registerReevaluateEngagementTimer:afterTime:withInterval:]
+ -[PowerUIDemoCECManager registerReevaluateEngagementTimer:afterTime:withInterval:].cold.1
+ -[PowerUIDemoCECManager registerUnpluggedTimer:afterTime:withInterval:]
+ -[PowerUIDemoCECManager registerUnpluggedTimer:afterTime:withInterval:].cold.1
+ -[PowerUIDemoCECManager requeryForecastTries]
+ -[PowerUIDemoCECManager setQueryForecastTimer:]
+ -[PowerUIDemoCECManager setRequeryForecastTries:]
+ -[PowerUIDemoCECManager setUnpluggedTimer:]
+ -[PowerUIDemoCECManager unpluggedTimer]
+ GCC_except_table43
+ GCC_except_table48
+ GCC_except_table52
+ GCC_except_table79
+ GCC_except_table83
+ _OBJC_IVAR_$_PowerUIDemoCECManager._queryForecastTimer
+ _OBJC_IVAR_$_PowerUIDemoCECManager._requeryForecastTries
+ _OBJC_IVAR_$_PowerUIDemoCECManager._unpluggedTimer
+ ___46-[PowerUIDemoCECManager initWithContextStore:]_block_invoke_4
+ ___46-[PowerUIDemoCECManager initWithContextStore:]_block_invoke_5
+ ___47-[PowerUIDemoCECManager monitorPluggedInChange]_block_invoke.133
+ ___71-[PowerUIDemoCECManager registerUnpluggedTimer:afterTime:withInterval:]_block_invoke
+ ___74-[PowerUIDemoCECManager registerCleanSegmentTimer:afterTime:withInterval:]_block_invoke
+ ___82-[PowerUIDemoCECManager registerReevaluateEngagementTimer:afterTime:withInterval:]_block_invoke
+ _kTopOffProtectionSoCFloor
+ _objc_msgSend$checkPluggedInState
+ _objc_msgSend$registerCleanSegmentTimer
+ _objc_msgSend$registerCleanSegmentTimer:afterTime:withInterval:
+ _objc_msgSend$registerReevaluateEngagementTimer:afterTime:withInterval:
+ _objc_msgSend$registerUnpluggedTimer:afterTime:withInterval:
+ _objc_msgSend$resetStateOnUnplug
+ _registerCleanSegmentTimer:afterTime:withInterval:.timerToken
+ _registerReevaluateEngagementTimer:afterTime:withInterval:.timerToken
+ _registerUnpluggedTimer:afterTime:withInterval:.timerToken
- +[PowerUISmartChargeUtilities drainBetweenRelevantEventsBefore:withMinimumDuration:]
- -[PowerUIDemoCECManager handleCallback:].cold.6
- -[PowerUIDemoCECManager registerEngagementTimer:afterTime:withInterval:]
- -[PowerUIDemoCECManager registerEngagementTimer:afterTime:withInterval:].cold.1
- -[PowerUIDemoCECManager registerEngagementTimer]
- GCC_except_table74
- GCC_except_table80
- ___47-[PowerUIDemoCECManager monitorPluggedInChange]_block_invoke.127
- ___72-[PowerUIDemoCECManager registerEngagementTimer:afterTime:withInterval:]_block_invoke
- _objc_msgSend$registerEngagementTimer
- _objc_msgSend$registerEngagementTimer:afterTime:withInterval:
- _registerEngagementTimer:afterTime:withInterval:.timerToken
CStrings:
+ "DemoCECManager Loaded state from defaults. Current phase: %@, current state: %@, isDemoCECEnabled %@, lastPluggedInDate %@, lastUnpluggedDate %@, pauseChargingCheckDate %@, pluggedInBatteryLevel %ld, _lastEngagementCheckDate %@, _requeryForecastTries %ld"
+ "Device no longer plugged into a power source after waiting %.0f mins (lastUnpluggedDate: %@,  current time: %@). Disengaging and resetting state."
+ "No longer re-querying forecast. requeryForecastTries: %ld , stillMissingForecast: %d"
+ "Query forecast timer"
+ "Registering clean segment timer for waitTime: %.0f minutes"
+ "Registering timer to re-evaluate engagement in the current session for waitTime: %.0f minutes and interval: %.0f minutes"
+ "Registering unplugged check timer for waitTime: %.0f minutes and interval: %.0f minutes"
+ "Sending analytics for session."
+ "T@\"NSObject<OS_dispatch_source>\",&,N,V_queryForecastTimer"
+ "T@\"NSObject<OS_dispatch_source>\",&,N,V_unpluggedTimer"
+ "TestMode: Allow reset state on unplug set to %d"
+ "Tq,N,V_requeryForecastTries"
+ "Tried to requery forecast for the %ld time, but still missing forecast."
+ "_queryForecastTimer"
+ "_requeryForecastTries"
+ "_unpluggedTimer"
+ "checkPluggedInState"
+ "queryForecastTimer"
+ "registerCleanSegmentTimer"
+ "registerCleanSegmentTimer:afterTime:withInterval:"
+ "registerReevaluateEngagementTimer:afterTime:withInterval:"
+ "registerUnpluggedTimer:afterTime:withInterval:"
+ "requeryForecastTries"
+ "resetStateOnUnplug"
+ "setQueryForecastTimer:"
+ "setRequeryForecastTries:"
+ "setUnpluggedTimer:"
+ "testResetState"
+ "unpluggedTimer"
- "DemoCECManager Loaded state from defaults. Current phase: %@, current state: %@, isDemoCECEnabled %@, lastPluggedInDate %@, pluggedInBatteryLevel %ld, _lastEngagementCheckDate %@,"
- "Device no longer plugged into a power source. Disengaging and resetting state."
- "Registering engagement timer for waitTime: %.0f minutes"
- "drainBetweenRelevantEventsBefore:withMinimumDuration:"
- "registerEngagementTimer"
- "registerEngagementTimer:afterTime:withInterval:"

```
