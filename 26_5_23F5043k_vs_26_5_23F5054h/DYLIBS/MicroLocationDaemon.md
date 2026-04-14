## MicroLocationDaemon

> `/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/MicroLocationDaemon`

```diff

-59.0.1.0.15
-  __TEXT.__text: 0x254814
+62.0.2.0.0
+  __TEXT.__text: 0x255168
   __TEXT.__auth_stubs: 0x23a0
-  __TEXT.__objc_methlist: 0x7448
-  __TEXT.__const: 0xd208
-  __TEXT.__gcc_except_tab: 0x2d104
-  __TEXT.__cstring: 0x12653
-  __TEXT.__oslogstring: 0x2ec8c
+  __TEXT.__objc_methlist: 0x74a8
+  __TEXT.__const: 0xd218
+  __TEXT.__gcc_except_tab: 0x2d248
+  __TEXT.__cstring: 0x126a3
+  __TEXT.__oslogstring: 0x2edcc
   __TEXT.__constg_swiftt: 0xc98
   __TEXT.__swift5_typeref: 0x7b5
   __TEXT.__swift5_fieldmd: 0x990

   __TEXT.__swift5_types: 0xf0
   __TEXT.__swift5_protos: 0x18
   __TEXT.__swift5_capture: 0x20
-  __TEXT.__unwind_info: 0xe108
+  __TEXT.__unwind_info: 0xe150
   __TEXT.__eh_frame: 0xd50
   __TEXT.__objc_classname: 0x1a4d
-  __TEXT.__objc_methname: 0x10f33
-  __TEXT.__objc_methtype: 0xf461
-  __TEXT.__objc_stubs: 0xd3a0
-  __DATA_CONST.__got: 0x880
-  __DATA_CONST.__const: 0x1898
+  __TEXT.__objc_methname: 0x110c3
+  __TEXT.__objc_methtype: 0xf471
+  __TEXT.__objc_stubs: 0xd560
+  __DATA_CONST.__got: 0x888
+  __DATA_CONST.__const: 0x18c0
   __DATA_CONST.__objc_classlist: 0x660
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x100
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3d18
+  __DATA_CONST.__objc_selrefs: 0x3d70
   __DATA_CONST.__objc_protorefs: 0x28
-  __DATA_CONST.__objc_superrefs: 0x258
+  __DATA_CONST.__objc_superrefs: 0x260
   __DATA_CONST.__objc_arraydata: 0xba0
   __AUTH_CONST.__auth_got: 0x11e8
   __AUTH_CONST.__const: 0xca68
   __AUTH_CONST.__cfstring: 0x5480
-  __AUTH_CONST.__objc_const: 0xe978
+  __AUTH_CONST.__objc_const: 0xea08
   __AUTH_CONST.__objc_intobj: 0x1a58
   __AUTH_CONST.__objc_doubleobj: 0xb50
   __AUTH_CONST.__objc_floatobj: 0xf0

   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH.__objc_data: 0x14e0
   __AUTH.__data: 0x920
-  __DATA.__objc_ivar: 0x5bc
+  __DATA.__objc_ivar: 0x5c8
   __DATA.__data: 0xd38
   __DATA.__common: 0x70
   __DATA.__bss: 0x2330

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 811EBE51-1627-3E0D-8AB0-5E3DBAF777CC
-  Functions: 10547
-  Symbols:   34220
-  CStrings:  8242
+  UUID: E3149BF6-F7F0-3BE1-AAD4-5ECC9DE91061
+  Functions: 10557
+  Symbols:   34272
+  CStrings:  8266
 
Symbols:
+ -[ULAltitudeBridge altimeter]
+ -[ULAltitudeBridge backgroundUpdatesRunning]
+ -[ULAltitudeBridge handleAltitudeMeasurement:error:]
+ -[ULAltitudeBridge handleAltitudeMeasurement:error:].cold.1
+ -[ULAltitudeBridge handleAltitudeMeasurement:error:].cold.2
+ -[ULAltitudeBridge queue]
+ -[ULAltitudeBridge setAltimeter:]
+ -[ULAltitudeBridge setBackgroundUpdatesRunning:]
+ -[ULAltitudeBridge setDelegate:]
+ -[ULAltitudeBridge setQueue:]
+ -[ULAltitudeBridge startBackgroundUpdates].cold.2
+ -[ULAltitudeBridge stopBackgroundUpdates].cold.2
+ _OBJC_CLASS_$_CMAltimeter
+ _OBJC_IVAR_$_ULAltitudeBridge._altimeter
+ _OBJC_IVAR_$_ULAltitudeBridge._backgroundUpdatesRunning
+ _OBJC_IVAR_$_ULAltitudeBridge._delegate
+ _OBJC_IVAR_$_ULAltitudeBridge._queue
+ ___42-[ULAltitudeBridge startBackgroundUpdates]_block_invoke
+ ___42-[ULAltitudeBridge startBackgroundUpdates]_block_invoke_2
+ ___block_descriptor_40_ea8_32w_e44_v24?0"CMAbsoluteAltitudeData"8"NSError"16lw32l8
+ _objc_msgSend$accuracy
+ _objc_msgSend$altimeter
+ _objc_msgSend$altitude
+ _objc_msgSend$backgroundUpdatesRunning
+ _objc_msgSend$didReceiveAltitudeProviderStateIsAvailable:
+ _objc_msgSend$didReceiveAltitudeUpdate:withError:
+ _objc_msgSend$handleAltitudeMeasurement:error:
+ _objc_msgSend$initWithDeviceIdentifier:altitudeMeters:accuracyMeters:precisionMeters:timestamp:
+ _objc_msgSend$isAbsoluteAltitudeAvailable
+ _objc_msgSend$precision
+ _objc_msgSend$setAltimeter:
+ _objc_msgSend$setBackgroundUpdatesRunning:
+ _objc_msgSend$startAbsoluteAltitudeUpdatesToQueue:withHandler:
+ _objc_msgSend$stopAbsoluteAltitudeUpdates
- _OBJC_IVAR_$_ULAltitudeBridge.delegate
CStrings:
+ "#wifi-bridge, scan measurements: %{private}@"
+ "/AppleInternal/Library/BuildRoots/4~CMfYugD0rbdIb8ktFCaCiiuOFl0jLa_LGYYW8mU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.5.Internal.sdk/usr/local/include/boost/uuid/detail/random_provider_posix.ipp"
+ "/AppleInternal/Library/BuildRoots/4~CMfYugD0rbdIb8ktFCaCiiuOFl0jLa_LGYYW8mU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.5.Internal.sdk/usr/local/include/boost/uuid/string_generator.hpp"
+ "/AppleInternal/Library/BuildRoots/4~CMfYugD0rbdIb8ktFCaCiiuOFl0jLa_LGYYW8mU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.5.Internal.sdk/usr/local/include/google/protobuf/repeated_field.h"
+ "@\"CMAltimeter\""
+ "@IUwbSessionDelegate: Session %{public}p did remove nearby object with reason: '%{public}s'. %{private}s"
+ "Altitude update: %.2fm, accuracy: %.2fm, precision: %.2fm"
+ "Got WiFi CWFEventTypeBSSIDChanged event, eventTS %@ BSSID %{private}@"
+ "IUwbSessionDelegate: discovered object: %{private}s"
+ "Received nil altitude data without error"
+ "T@\"<ULAltitudeDelegate>\",W,N,V_delegate"
+ "T@\"CMAltimeter\",&,N,V_altimeter"
+ "TB,N,V_backgroundUpdatesRunning"
+ "_altimeter"
+ "_backgroundUpdatesRunning"
+ "_handleULRapportMonitorEventDeviceFound: new device: %{private}@"
+ "_handleULRapportMonitorEventIdentities: identities: %{private}@"
+ "accuracy"
+ "altimeter"
+ "altitude"
+ "altitude updates requested but already running, ignoring request"
+ "backgroundUpdatesRunning"
+ "com.apple.milod.ULAltitudeService"
+ "handleAltitudeMeasurement:error:"
+ "isAbsoluteAltitudeAvailable"
+ "precision"
+ "requested altitude, but altimeter is unavailable"
+ "requested to stop altitude updates but already stopped, ignoring request"
+ "setAltimeter:"
+ "setBackgroundUpdatesRunning:"
+ "startAbsoluteAltitudeUpdatesToQueue:withHandler:"
+ "starting altitude updates"
+ "stopAbsoluteAltitudeUpdates"
+ "stopping altitude updates"
+ "v24@?0@\"CMAbsoluteAltitudeData\"8@\"NSError\"16"
+ "{\"msg%{public}.0s\":\"Scan Event generated\", \"method\":%{public, location:escape_only}s, \"scanEventUUID: \":%{public, location:escape_only}s, \"ScanType: \":%{public, location:escape_only}s, \"timestamp: _s\":\"%{public}.09f\", \"scanResult: \":%{public, location:escape_only}s, \"uwbSuspended: \":%{public}d, \"bleSuspended: \":%{public}d, \"wifiDisabled: \":%{public}d, \"MotionState: \":%{public, location:escape_only}s, \"wifiMeasurmentsCount:\":%{public}d, \"bleMeasurementsCount:\":%{public}d, \"uwbMeasurements:\":%{public}d, \"associatedAccessPointInfo.bssid: \":%{private, location:escape_only}s, \"associatedAccessPointInfo.RSSI: \":%{public}d}"
- "#wifi-bridge, scan measurements: %@"
- "/AppleInternal/Library/BuildRoots/4~CLi1ugABRrfsH7B3fE4yI985EzEvvZI81hz_YQQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.5.Internal.sdk/usr/local/include/boost/uuid/detail/random_provider_posix.ipp"
- "/AppleInternal/Library/BuildRoots/4~CLi1ugABRrfsH7B3fE4yI985EzEvvZI81hz_YQQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.5.Internal.sdk/usr/local/include/boost/uuid/string_generator.hpp"
- "/AppleInternal/Library/BuildRoots/4~CLi1ugABRrfsH7B3fE4yI985EzEvvZI81hz_YQQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.5.Internal.sdk/usr/local/include/google/protobuf/repeated_field.h"
- "@IUwbSessionDelegate: Session %{public}p did remove nearby object with reason: '%{public}s'. %{public}s"
- "Got WiFi CWFEventTypeBSSIDChanged event, eventTS %@ BSSID %@"
- "IUwbSessionDelegate: discovered object: %{public}s"
- "T@\"<ULAltitudeDelegate>\",R,W,N,Vdelegate"
- "ULAltitudeBridge: altitude not supported on this platform"
- "_handleULRapportMonitorEventDeviceFound: new device: %@"
- "_handleULRapportMonitorEventIdentities: identities: %@"
- "{\"msg%{public}.0s\":\"Scan Event generated\", \"method\":%{public, location:escape_only}s, \"scanEventUUID: \":%{public, location:escape_only}s, \"ScanType: \":%{public, location:escape_only}s, \"timestamp: _s\":\"%{public}.09f\", \"scanResult: \":%{public, location:escape_only}s, \"uwbSuspended: \":%{public}d, \"bleSuspended: \":%{public}d, \"wifiDisabled: \":%{public}d, \"MotionState: \":%{public, location:escape_only}s, \"wifiMeasurmentsCount:\":%{public}d, \"bleMeasurementsCount:\":%{public}d, \"uwbMeasurements:\":%{public}d, \"associatedAccessPointInfo.bssid: \":%{public, location:escape_only}s, \"associatedAccessPointInfo.RSSI: \":%{public}d}"

```
