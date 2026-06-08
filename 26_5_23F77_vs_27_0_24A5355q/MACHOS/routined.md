## routined

> `/usr/libexec/routined`

```diff

-1075.0.2.0.0
-  __TEXT.__text: 0xd50
-  __TEXT.__auth_stubs: 0x1f0
-  __TEXT.__objc_stubs: 0x300
-  __TEXT.__objc_methlist: 0x100
-  __TEXT.__cstring: 0xe6
-  __TEXT.__oslogstring: 0x50
-  __TEXT.__const: 0x8
-  __TEXT.__objc_classname: 0x24
-  __TEXT.__objc_methname: 0x3fa
-  __TEXT.__objc_methtype: 0x51
-  __TEXT.__unwind_info: 0xb8
-  __DATA_CONST.__auth_got: 0x100
-  __DATA_CONST.__got: 0x58
+1109.0.3.0.0
+  __TEXT.__text: 0x1c64
+  __TEXT.__auth_stubs: 0x2a0
+  __TEXT.__objc_stubs: 0x1080
+  __TEXT.__objc_methlist: 0x1f0
+  __TEXT.__const: 0x60
+  __TEXT.__objc_methname: 0xb84
+  __TEXT.__oslogstring: 0x144
+  __TEXT.__cstring: 0x14b
+  __TEXT.__objc_classname: 0x2d
+  __TEXT.__objc_methtype: 0xcb
+  __TEXT.__unwind_info: 0xc0
   __DATA_CONST.__const: 0x68
-  __DATA_CONST.__cfstring: 0xa0
+  __DATA_CONST.__cfstring: 0xc0
   __DATA_CONST.__objc_classlist: 0x10
+  __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x8
-  __DATA.__objc_const: 0x290
-  __DATA.__objc_selrefs: 0x130
+  __DATA_CONST.__objc_superrefs: 0x30
+  __DATA_CONST.__auth_got: 0x158
+  __DATA_CONST.__got: 0xa8
+  __DATA.__objc_const: 0x3d0
+  __DATA.__objc_selrefs: 0x4b0
   __DATA.__objc_ivar: 0x1c
   __DATA.__objc_data: 0xa0
   __DATA.__data: 0x18
   __DATA.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/_LocationEssentials.framework/_LocationEssentials
   - /System/Library/PrivateFrameworks/CoreRoutine.framework/CoreRoutine
+  - /System/Library/PrivateFrameworks/CoreRoutineProtobuf.framework/CoreRoutineProtobuf
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcoreroutine.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1024C867-0265-374A-AF6A-98390BD24D5D
-  Functions: 27
-  Symbols:   50
-  CStrings:  76
+  UUID: C5F5F9FA-71B8-30A3-BA4F-32732D2F6152
+  Functions: 41
+  Symbols:   73
+  CStrings:  204
 
Symbols:
+ _OBJC_CLASS_$_RTPAddress
+ _OBJC_CLASS_$_RTPLocation
+ _OBJC_CLASS_$_RTPMapItem
+ _OBJC_CLASS_$_RTPMapItemExtendedAttributes
+ _OBJC_CLASS_$_RTPPOIBusinessHours
+ _OBJC_CLASS_$_RTPPOIDailyHours
+ _OBJC_CLASS_$_RTPPOILocalTimeInterval
+ _OBJC_CLASS_$_RTPWiFiAccessPoint
+ _kCLLocationIntegrityHigh
+ _kCLLocationIntegrityLow
+ _kCLLocationIntegrityMedium
+ _kCLLocationIntegrityNone
+ _objc_alloc
+ _objc_alloc_init
+ _objc_claimAutoreleasedReturnValue
+ _objc_opt_class
+ _objc_release_x23
+ _objc_release_x26
+ _objc_release_x27
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x2
+ _objc_retain_x21
+ _objc_retain_x23
+ _objc_retain_x25
+ _objc_retain_x3
- _objc_autoreleaseReturnValue
- _objc_release
CStrings:
+ ""
+ "-[RTPLocation(RTExtensions) initWithCLLocation:]"
+ "-[RTPLocation(RTExtensions) initWithLocation:]"
+ "@24@0:8@16"
+ "@68@0:8d16d24d32i40@44d52d60"
+ "@80@0:8d16d24d32i40@44d52d60i68I72i76"
+ "Invalid parameter not satisfying: accessPoint"
+ "Invalid parameter not satisfying: address"
+ "Invalid parameter not satisfying: location (in %s:%d)"
+ "Invalid parameter not satisfying: mapItem"
+ "Invalid parameter not satisfying: mapItemExtendedAttributes"
+ "RTExtensions"
+ "UUIDString"
+ "addAlternateCategoryMUIDs:"
+ "addBusinessHours:"
+ "addDailyHours:"
+ "addTimeIntervals:"
+ "address"
+ "administrativeArea"
+ "administrativeAreaCode"
+ "age"
+ "alternateCategoryMUIDs"
+ "businessHours"
+ "category"
+ "categoryMUID"
+ "channel"
+ "convertLocationIntegrityType:"
+ "convertLocationReferenceFrame:"
+ "convertLocationType:"
+ "convertSignalEnvironmentType:"
+ "convertToRTPWiFiFingerprintLabelType:"
+ "convertToWiFiFingerprintLabelType:"
+ "coordinate"
+ "country"
+ "countryCode"
+ "dailyHours"
+ "date"
+ "description"
+ "endTime"
+ "extendedAttributes"
+ "horizontalAccuracy"
+ "horizontalUncertainty"
+ "hoursType"
+ "i20@0:8I16"
+ "i20@0:8i16"
+ "i24@0:8q16"
+ "identifier"
+ "initWithAddress:"
+ "initWithCLLocation:"
+ "initWithLatitude:longitude:uncertainty:referenceFrame:date:speed:speedAccuracy:"
+ "initWithLatitude:longitude:uncertainty:referenceFrame:date:speed:speedAccuracy:locationType:integrity:signalEnvironment:"
+ "initWithLocation:"
+ "initWithMapItem:"
+ "initWithRTMapItemExtendedAttributes:"
+ "initWithRTWiFiAccessPoint:"
+ "integrity"
+ "latitude"
+ "locality"
+ "location"
+ "longitude"
+ "mac"
+ "mapItemPlaceType"
+ "muid"
+ "name"
+ "postalCode"
+ "q20@0:8i16"
+ "referenceFrame"
+ "resultProviderID"
+ "rssi"
+ "setAddress:"
+ "setAddressString:"
+ "setAdministrativeArea:"
+ "setAdministrativeAreaCode:"
+ "setAge:"
+ "setCategory:"
+ "setCategoryMUID:"
+ "setChannel:"
+ "setCountry:"
+ "setCountryCode:"
+ "setEndTime:"
+ "setHoursType:"
+ "setIntegrity:"
+ "setLatitude:"
+ "setLocality:"
+ "setLocation:"
+ "setLongitude:"
+ "setMac:"
+ "setMapItemExtendedAttributes:"
+ "setMapItemPlaceType:"
+ "setMapItemSourceBitMask:"
+ "setMuid:"
+ "setName:"
+ "setPostalCode:"
+ "setReferenceFrame:"
+ "setResultProviderID:"
+ "setRssi:"
+ "setSignalEnvironmentType:"
+ "setSpeed:"
+ "setSpeedAccuracy:"
+ "setStartTime:"
+ "setSubAdministrativeArea:"
+ "setSubLocality:"
+ "setSubThoroughfare:"
+ "setThoroughfare:"
+ "setTimestamp:"
+ "setType:"
+ "setUncertainty:"
+ "setUuid:"
+ "setWeekday:"
+ "setWifiConfidence:"
+ "setWifiFingerprintLabelType:"
+ "signalEnvironmentType"
+ "source"
+ "speed"
+ "speedAccuracy"
+ "startTime"
+ "subAdministrativeArea"
+ "subLocality"
+ "subThoroughfare"
+ "thoroughfare"
+ "timeIntervalSinceReferenceDate"
+ "timeIntervals"
+ "timestamp"
+ "type"
+ "unsignedLongLongValue"
+ "weekday"
+ "wifiConfidence"
+ "wifiFingerprintLabelType"

```
