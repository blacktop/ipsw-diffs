## AirPlaySender

> `/System/Library/PrivateFrameworks/AirPlaySender.framework/AirPlaySender`

```diff

-1005.12.1.0.0
-  __TEXT.__text: 0x23b074
+1005.13.1.1.0
+  __TEXT.__text: 0x23b730
   __TEXT.__objc_methlist: 0x81c
-  __TEXT.__cstring: 0x8ff1c
+  __TEXT.__cstring: 0x901d6
   __TEXT.__const: 0x6190
   __TEXT.__gcc_except_tab: 0xaf4
   __TEXT.__dlopen_cstrs: 0x61a
   __TEXT.__oslogstring: 0x1009
-  __TEXT.__unwind_info: 0x92c8
+  __TEXT.__unwind_info: 0x92e8
   __TEXT.__eh_frame: 0x48
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x77c8
+  __DATA_CONST.__const: 0x77e8
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb58
+  __DATA_CONST.__objc_selrefs: 0xb78
   __DATA_CONST.__objc_superrefs: 0x38
   __DATA_CONST.__objc_arraydata: 0x170
-  __DATA_CONST.__got: 0x23c0
+  __DATA_CONST.__got: 0x23d0
   __AUTH_CONST.__const: 0x77d0
-  __AUTH_CONST.__cfstring: 0x14a60
+  __AUTH_CONST.__cfstring: 0x14aa0
   __AUTH_CONST.__objc_const: 0xed0
   __AUTH_CONST.__objc_dictobj: 0x1b8
   __AUTH_CONST.__objc_intobj: 0x150

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 11496
-  Symbols:   8711
-  CStrings:  11672
+  Functions: 11503
+  Symbols:   8721
+  CStrings:  11689
 
Symbols:
+ GCC_except_table129
+ _APSIsHomeAccessory
+ _OBJC_CLASS_$_CUSystemMonitor
+ ___endpoint_startPowerSourceMonitorIfNeeded_block_invoke
+ ___endpoint_startPowerSourceMonitorIfNeeded_block_invoke_2
+ ___endpoint_startPowerSourceMonitorIfNeeded_block_invoke_3
+ _airPlayDescription_isAppleHomeAccessory
+ _endpoint_startPowerSourceMonitorIfNeeded
+ _endpoint_stopPowerSourceMonitor
+ _endpoint_updateInactivityTimer
+ _kAPSDynamicLatencyManagerVariantIdentifier_B525
+ _kFigEndpointSubType_HomeAccessory
- GCC_except_table128
- _endpoint_startInactivityTimer
CStrings:
+ "1005.13.1.1"
+ "APEndpointInactivityTimeoutType endpoint_determineInactivityTimeoutBehavior(FigEndpointRef, FigEndpointFeatures, CFDictionaryRef)"
+ "AudioAccessory11"
+ "HomeAccessory"
+ "NoIdleTimeout activation option"
+ "P2POnly"
+ "P2POnlyOnBattery"
+ "[%{ptr}] Inactivity timeout type: %s%?{end} (%s)\n"
+ "[%{ptr}] Monitoring power source for inactivity timer\n"
+ "[%{ptr}] Power source changed: now on %s power\n"
+ "[%{ptr}] Power source monitor creation fail"
+ "[%{ptr}] Stopped monitoring power source\n"
+ "[%{ptr}] Using inactivity timeout? %s%?{end} (type: %s)\n"
+ "battery"
+ "no platform-specific policy"
+ "void endpoint_handlePowerSourceChanged(FigEndpointRef)"
+ "void endpoint_startPowerSourceMonitorIfNeeded(FigEndpointRef)"
+ "void endpoint_stopPowerSourceMonitor(FigEndpointRef)"
+ "void endpoint_updateInactivityTimer(FigEndpointRef, Boolean)"
+ "wall"
- "1005.12.1"
- "[%{ptr}] Using inactivity timeout? %d\n"
- "void endpoint_startInactivityTimer(FigEndpointRef)"
```
