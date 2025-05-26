## WirelessRadioManagerd

> `/usr/sbin/WirelessRadioManagerd`

```diff

-1625.1.0.0.0
-  __TEXT.__text: 0x1270b4
+1630.1.5.0.0
+  __TEXT.__text: 0x1276b0
   __TEXT.__auth_stubs: 0x1fc0
-  __TEXT.__objc_stubs: 0x19bc0
-  __TEXT.__objc_methlist: 0xd0a4
-  __TEXT.__objc_methname: 0x27fb6
-  __TEXT.__cstring: 0x422e9
+  __TEXT.__objc_stubs: 0x19ce0
+  __TEXT.__objc_methlist: 0xd134
+  __TEXT.__objc_methname: 0x28258
+  __TEXT.__cstring: 0x426a0
   __TEXT.__objc_classname: 0xcf6
-  __TEXT.__objc_methtype: 0x6a6f
-  __TEXT.__const: 0x21068
-  __TEXT.__gcc_except_tab: 0x34e0
+  __TEXT.__objc_methtype: 0x6a8e
+  __TEXT.__const: 0x21070
+  __TEXT.__gcc_except_tab: 0x34c8
   __TEXT.__dlopen_cstrs: 0x2b4
   __TEXT.__oslogstring: 0x85
-  __TEXT.__unwind_info: 0x3ebc
+  __TEXT.__unwind_info: 0x3ecc
   __TEXT.__eh_frame: 0x88
   __DATA_CONST.__auth_got: 0xff8
   __DATA_CONST.__got: 0x470
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x44d0
-  __DATA_CONST.__cfstring: 0x251e0
+  __DATA_CONST.__cfstring: 0x254a0
   __DATA_CONST.__objc_classlist: 0x3d8
   __DATA_CONST.__objc_catlist: 0x0
   __DATA_CONST.__objc_protolist: 0x70

   __DATA_CONST.__objc_intobj: 0x2bf8
   __DATA_CONST.__objc_dictobj: 0x78
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA.__objc_const: 0x16f08
-  __DATA.__objc_selrefs: 0x7710
+  __DATA.__objc_const: 0x17048
+  __DATA.__objc_selrefs: 0x7770
   __DATA.__objc_classrefs: 0x508
   __DATA.__objc_superrefs: 0x400
-  __DATA.__objc_ivar: 0x1760
+  __DATA.__objc_ivar: 0x1784
   __DATA.__objc_data: 0x2670
   __DATA.__data: 0x5a0
   __DATA.__common: 0x13a
-  __DATA.__bss: 0x3f8
+  __DATA.__bss: 0x3e8
   - /System/Library/Frameworks/CallKit.framework/CallKit
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreData.framework/CoreData

   - /System/Library/PrivateFrameworks/Symptoms.framework/Frameworks/SymptomAnalytics.framework/SymptomAnalytics
   - /System/Library/PrivateFrameworks/Symptoms.framework/Frameworks/SymptomPresentationFeed.framework/SymptomPresentationFeed
   - /System/Library/PrivateFrameworks/Trial.framework/Trial
+  - /System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/WiFiPeerToPeer
   - /usr/lib/libARI.dylib
   - /usr/lib/libATCommandStudioDynamic.dylib
   - /usr/lib/libICEClient.dylib

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 6536
+  Functions: 6544
   Symbols:   728
-  CStrings:  12930
+  CStrings:  12977
 
CStrings:
+ "%s Event: %@"
+ "%s Invalid RSRP: %f"
+ "%s Invalid latestStrongTimeStamp %@. Persisting changeTimeStamp %@ for SOS"
+ "%s Invalid mStrongestSOSRSRP %f"
+ "%s Invalid mStrongestSOSTimeStamp %@"
+ "%s Invalid mStrongestSOSTimeStamp %@ as SOS patch is less than %d seconds (mEnterSOSTimeStamp %@ - changeTimeStamp %@)"
+ "%s Invalid mStrongestSOSTimeStamp as before mEnterSOSTimeStamp "
+ "%s NIL latestStrongTimeStamp %f  mStrongestSOSTimeStamp %f"
+ "%s NOT NIL latestStrongTimeStamp %f mStrongestSOSTimeStamp %f"
+ "%s Reset to initial values. mEnterSOSTimeStamp %@ mStrongestSOSRSRP %f, mStrongestSOSTimeStamp %@"
+ "%s Resetting mStrongestSOSTimeStamp to %@ as too close to entry SOS timestamp"
+ "%s Setting latestStrongTimeStamp %@ to mStrongestSOSTimeStamp %@ with RSRP %f aboveThreshold %d"
+ "%s mStrongestSOSRSRP %f, mStrongestSOSTimeStamp %@"
+ "%s mStrongestSOSRSRP %f, rsrp %f"
+ "%s mStrongestSOSTimeStamp %@ within %f seconds of mEnterSOSTimeStamp %@. "
+ "%s: Skipping event as %d same as previous status %d\n"
+ "%s: changeTimeStamp %@ combinedRegistrationStatus: %d mCellularAvailabilityStatus %@\n"
+ "-[WRM_EnhancedCTService initializeStrongestSOSSignal:]"
+ "-[WRM_EnhancedCTService monitorStrongSOSSignal:]"
+ "-[WRM_EnhancedCTService validateStrongestSOSTimeStamp:]"
+ "-[WRM_EnhancedCTService writeToCellularAvailabilityStatusBiomeStream::]"
+ "AWDLRealTimeModeEnabled"
+ "B24@0:8d16"
+ "B28@0:8I16C20B24"
+ "RCU2 Controller - No change in btWirelessLoad, not updating"
+ "RCU2 Controller AWDLRealTime status changed from %d to %d"
+ "RCU2 Controller No Change in AWDLRealTime state - not updating"
+ "RCU2 Controller No Change in WiFi Band - Not Updataing"
+ "RCU2 Controller WiFi band changed from %d to %d"
+ "RCU2 Controller updating btWirelessLoad from %d to %d"
+ "RCU2Init"
+ "SOS Waypoint RSRP Th  : %lld"
+ "SOSWaypointRSRPTh"
+ "TB,N,V_mRealTimeAwdlTrafficEnabled"
+ "Tq,N,V_sosWaypointRSRPTh"
+ "_mRealTimeAwdlTrafficEnabled"
+ "_sosWaypointRSRPTh"
+ "btWirelessLoad"
+ "dateWithTimeIntervalSince1970:"
+ "initSOSWaypointThreshold"
+ "initSOSWaypointThreshold Error: invalid tempiRATConfig. Setting to default value of -115"
+ "initSOSWaypointThreshold: Setting to %f"
+ "initWithTimeStamp:deviceType:deviceRegistrationStatus:previousDeviceRegistrationStatus:aboveThreshold:latestStrongTimeStamp:"
+ "initializeStrongestSOSSignal:"
+ "mEnterSOSTimeStamp"
+ "mRealTimeAwdlTrafficEnabled"
+ "mSOSRSRPThreshold"
+ "mStrongestSOSRSRP"
+ "mStrongestSOSTimeStamp"
+ "monitorStrongSOSSignal:"
+ "sendFullWirelessLoad:wifiBandInfo:AWDLRealTimeModeInfo:"
+ "setMRealTimeAwdlTrafficEnabled:"
+ "setSosWaypointRSRPTh:"
+ "sosWaypointRSRPTh"
+ "updateAWDLRealTimeMode:"
+ "updateWiFiBand:"
+ "v28@0:8d16B24"
+ "v44@0:8@16q24d32B40"
+ "validateStrongestSOSTimeStamp:"
+ "wifiBandLoad"
- "B20@0:8I16"
- "BMDeviceCellularAvailabilityStatusDeviceTypeAsString"
- "BMDeviceCellularAvailabilityStatusStateAsString"
- "NSString *BMDeviceCellularAvailabilityStatusDeviceTypeAsString_SOFT(BMDeviceCellularAvailabilityStatusDeviceType)"
- "NSString *BMDeviceCellularAvailabilityStatusStateAsString_SOFT(BMDeviceCellularAvailabilityStatusState)"
- "RCU2 Controller - RCU2_SUPPORT_IOS - Feature not enabled"
- "RCU2 Controller - setWirelessLoad- Feature not compiled"
- "WRM_EnhancedCTService:writeToCellularAvailabilityStatusBiomeStream: Skipping event as %d same as previous status %d\n"
- "WRM_EnhancedCTService:writeToCellularAvailabilityStatusBiomeStream: Timestamp %s, deviceRegistrationStatus %d %@, previousRegistrationStatus: %@, on deviceType %@ \n"
- "WRM_EnhancedCTService:writeToCellularAvailabilityStatusBiomeStream: combinedRegistrationStatus: %d mCellularAvailabilityStatus %@\n"
- "setDateStyle:"
- "setTimeStyle:"
- "v44@0:8@16q24@32B40"

```
