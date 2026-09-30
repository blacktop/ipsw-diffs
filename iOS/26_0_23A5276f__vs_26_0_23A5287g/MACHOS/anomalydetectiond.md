## anomalydetectiond

> `/usr/libexec/anomalydetectiond`

```diff

-145.0.0.0.0
-  __TEXT.__text: 0x34dfd8
-  __TEXT.__auth_stubs: 0x1660
+145.0.2.0.0
+  __TEXT.__text: 0x34f044
+  __TEXT.__auth_stubs: 0x1680
   __TEXT.__objc_stubs: 0x90c0
   __TEXT.__objc_methlist: 0x8c10
-  __TEXT.__gcc_except_tab: 0x10fa8
-  __TEXT.__const: 0x92d6
-  __TEXT.__cstring: 0x1a430
-  __TEXT.__oslogstring: 0xfe12
+  __TEXT.__gcc_except_tab: 0x11004
+  __TEXT.__const: 0x92fe
+  __TEXT.__cstring: 0x1a507
+  __TEXT.__oslogstring: 0xfe5f
   __TEXT.__objc_classname: 0x10a6
-  __TEXT.__objc_methtype: 0x5cd5
-  __TEXT.__objc_methname: 0xbde0
+  __TEXT.__objc_methtype: 0x5d3a
+  __TEXT.__objc_methname: 0xbde6
   __TEXT.__ustring: 0x10ae
-  __TEXT.__unwind_info: 0xbdc8
+  __TEXT.__unwind_info: 0xbde8
   __TEXT.__eh_frame: 0x590
-  __DATA_CONST.__auth_got: 0xb48
+  __DATA_CONST.__auth_got: 0xb58
   __DATA_CONST.__got: 0x5a0
   __DATA_CONST.__auth_ptr: 0x30
-  __DATA_CONST.__const: 0x22d00
-  __DATA_CONST.__cfstring: 0x6380
+  __DATA_CONST.__const: 0x22d50
+  __DATA_CONST.__cfstring: 0x6480
   __DATA_CONST.__objc_classlist: 0x4c0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x128

   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA_CONST.__objc_dictobj: 0x320
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA.__objc_const: 0xff08
+  __DATA.__objc_const: 0xff28
   __DATA.__objc_selrefs: 0x2f50
-  __DATA.__objc_ivar: 0x92c
+  __DATA.__objc_ivar: 0x930
   __DATA.__objc_data: 0x2f80
   __DATA.__data: 0x2010
   __DATA.__bss: 0x230

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 21DF8F3D-95BF-33B4-8515-481A8CC9B4BF
-  Functions: 15870
-  Symbols:   564
-  CStrings:  9673
+  UUID: 08F454FC-7D15-341D-BCB0-59028C3293B4
+  Functions: 15888
+  Symbols:   566
+  CStrings:  9694
 
Symbols:
+ _os_unfair_lock_lock
+ _os_unfair_lock_unlock
CStrings:
+ "Attempted to release a null power assertion"
+ "Releasing power assertion failed"
+ "_lock"
+ "gestureQuaternion"
+ "isMicBlockedDuringEscalations"
+ "kappaTokenAllocated"
+ "martyAlphaCrashTokenCount"
+ "martyEarlyCrashTokenCount"
+ "martyPunchThruTokenCount"
+ "martyTokenAllocated"
+ "receivedLentPunchThru"
+ "receivedPunchThruRetraction"
+ "{KappaSessionInfo=\"detectionDecision\"B\"isCompanionConnected\"B\"didCompanionTrigger\"B\"companionDetectionDecision\"B\"trigger_bitmap\"i\"drivingTimeStartToFirstTrigger\"i\"sessionStartTimestamp\"d\"sessionDuration\"i\"gpsDuration\"i\"numTriggers\"i\"numPlanarCrashes\"i\"numRolloverCrashes\"i\"numHighSpeedCrashes\"i\"numDeescalations\"i\"coarseLat\"f\"coarseLong\"f\"sunElevation\"f\"signalEnvironment\"i\"maxDeltaVXYBiggestImpact\"i\"maxDeltaVXYOverEpoch\"i\"serverConfigVersion\"f\"didRaiseUI\"B\"didRaiseUI_companion\"B\"didCancelUI\"B\"didCancelUI_companion\"B\"isSOSResponseSuccess\"B\"isSOSResponseSuccessPushedToCompanion\"B\"isSOSResponseAlreadyActive\"B\"isSOSResponseFailed\"B\"isSOSResponseNotSupported\"B\"isSOSResponseNotEnabled\"B\"isSOSUserInitiated\"B\"isSOSAutoInitiated\"B\"didPlaceCall\"B\"isMicBlockedDuringEscalations\"B\"outgoingCallTimestamp\"Q}"
+ "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"
- "{KappaSessionInfo=\"detectionDecision\"B\"isCompanionConnected\"B\"didCompanionTrigger\"B\"companionDetectionDecision\"B\"trigger_bitmap\"i\"drivingTimeStartToFirstTrigger\"i\"sessionStartTimestamp\"d\"sessionDuration\"i\"gpsDuration\"i\"numTriggers\"i\"numPlanarCrashes\"i\"numRolloverCrashes\"i\"numHighSpeedCrashes\"i\"numDeescalations\"i\"coarseLat\"f\"coarseLong\"f\"sunElevation\"f\"signalEnvironment\"i\"maxDeltaVXYBiggestImpact\"i\"maxDeltaVXYOverEpoch\"i\"serverConfigVersion\"f\"didRaiseUI\"B\"didRaiseUI_companion\"B\"didCancelUI\"B\"didCancelUI_companion\"B\"isSOSResponseSuccess\"B\"isSOSResponseSuccessPushedToCompanion\"B\"isSOSResponseAlreadyActive\"B\"isSOSResponseFailed\"B\"isSOSResponseNotSupported\"B\"isSOSResponseNotEnabled\"B\"isSOSUserInitiated\"B\"isSOSAutoInitiated\"B\"didPlaceCall\"B}"

```
