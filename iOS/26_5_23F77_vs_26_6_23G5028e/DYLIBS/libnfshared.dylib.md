## libnfshared.dylib

> `/usr/lib/libnfshared.dylib`

```diff

-365.3.1.0.0
-  __TEXT.__text: 0x20bc4
-  __TEXT.__auth_stubs: 0xaf0
+366.4.0.0.0
+  __TEXT.__text: 0x22568
+  __TEXT.__auth_stubs: 0xb00
   __TEXT.__delay_stubs: 0x40
   __TEXT.__delay_helper: 0xdc
-  __TEXT.__objc_methlist: 0x2024
+  __TEXT.__objc_methlist: 0x22a4
   __TEXT.__const: 0x210
-  __TEXT.__cstring: 0x4113
-  __TEXT.__oslogstring: 0x133a
-  __TEXT.__unwind_info: 0x6c8
-  __TEXT.__objc_classname: 0x354
-  __TEXT.__objc_methname: 0x4390
-  __TEXT.__objc_methtype: 0x9bd
-  __TEXT.__objc_stubs: 0x26a0
-  __DATA_CONST.__got: 0x1a8
+  __TEXT.__cstring: 0x42a4
+  __TEXT.__oslogstring: 0x136a
+  __TEXT.__unwind_info: 0x728
+  __TEXT.__objc_classname: 0x3c6
+  __TEXT.__objc_methname: 0x4a31
+  __TEXT.__objc_methtype: 0xa29
+  __TEXT.__objc_stubs: 0x2a00
+  __DATA_CONST.__got: 0x1b8
   __DATA_CONST.__const: 0x560
-  __DATA_CONST.__objc_classlist: 0x100
+  __DATA_CONST.__objc_classlist: 0x118
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1210
+  __DATA_CONST.__objc_selrefs: 0x1320
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0xc0
+  __DATA_CONST.__objc_superrefs: 0xd8
   __DATA_CONST.__objc_arraydata: 0x4c8
-  __AUTH_CONST.__auth_got: 0x588
+  __AUTH_CONST.__auth_got: 0x590
   __AUTH_CONST.__const: 0x200
-  __AUTH_CONST.__cfstring: 0x3e80
-  __AUTH_CONST.__objc_const: 0x3820
+  __AUTH_CONST.__cfstring: 0x4100
+  __AUTH_CONST.__objc_const: 0x3f78
   __AUTH_CONST.__objc_intobj: 0xf0
   __AUTH_CONST.__objc_dictobj: 0x190
   __AUTH_CONST.__objc_arrayobj: 0x48
-  __AUTH.__objc_data: 0x460
-  __DATA.__objc_ivar: 0x228
+  __AUTH.__objc_data: 0x550
+  __DATA.__objc_ivar: 0x290
   __DATA.__data: 0x3d0
   __DATA.__bss: 0x10
   __DATA.__common: 0x68

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1DF04D96-F622-3049-AC06-9661A6017B59
-  Functions: 678
-  Symbols:   377
-  CStrings:  2324
+  UUID: 51664EF5-B103-3E98-8B13-D037465AFFE5
+  Functions: 726
+  Symbols:   384
+  CStrings:  2456
 
Symbols:
+ _OBJC_CLASS_$_NFLocation
+ _OBJC_CLASS_$_NFPaymentTagReaderDeveloperPresentmentReport
+ _OBJC_CLASS_$_NFPaymentTagReaderDeveloperPresentmentSessionData
+ _OBJC_METACLASS_$_NFLocation
+ _OBJC_METACLASS_$_NFPaymentTagReaderDeveloperPresentmentReport
+ _OBJC_METACLASS_$_NFPaymentTagReaderDeveloperPresentmentSessionData
+ _SecTaskCopyTeamIdentifier
CStrings:
+ "%s:%i Error fetching teamID: %{public}@"
+ "%{public}s:%i Error fetching teamID: %{public}@"
+ ", delayCHRestart=1"
+ ", devTestMode=1"
+ ", startOnLocUpdate=1"
+ "-[NFServiceWhitelistChecker _initCoreNFCEntitlements:secTask:]"
+ "@\"NSUUID\""
+ "@56@0:8@16Q24@32@40@48"
+ "@60@0:8Q16Q24@32@40B48B52B56"
+ "@72@0:8d16d24d32d40@48@56@64"
+ "@96@0:8Q16Q24d32d40d48d56@64@72@80Q88"
+ "NFLocation"
+ "NFPaymentTagReaderDeveloperPresentmentReport"
+ "NFPaymentTagReaderDeveloperPresentmentSessionData"
+ "T@\"NSArray\",R,V_developmentPresentments"
+ "T@\"NSString\",R,N,V_city"
+ "T@\"NSString\",R,N,V_country"
+ "T@\"NSString\",R,N,V_state"
+ "T@\"NSString\",R,N,V_teamIdentifier"
+ "T@\"NSString\",R,V_bundleID"
+ "T@\"NSString\",R,V_city"
+ "T@\"NSString\",R,V_country"
+ "T@\"NSString\",R,V_state"
+ "T@\"NSString\",R,V_teamID"
+ "T@\"NSUUID\",R,V_reportId"
+ "TB,N,V_isDevTestMode"
+ "TB,N,V_startOnLocationUpdate"
+ "TB,R,N,V_nfcPaymentTagReaderDeveloperMode"
+ "TQ,R,V_endTimestamp"
+ "TQ,R,V_startTimestamp"
+ "TQ,R,V_successfulTapCount"
+ "TQ,R,V_timestampDay"
+ "Td,R,N,V_altitude"
+ "Td,R,N,V_horizontalAccuracy"
+ "Td,R,N,V_latitude"
+ "Td,R,N,V_longitude"
+ "Td,R,V_altitude"
+ "Td,R,V_horizontalAccuracy"
+ "Td,R,V_latitude"
+ "Td,R,V_longitude"
+ "_altitude"
+ "_bundleID"
+ "_city"
+ "_country"
+ "_developmentPresentments"
+ "_endTimestamp"
+ "_horizontalAccuracy"
+ "_isDevTestMode"
+ "_latitude"
+ "_longitude"
+ "_nfcPaymentTagReaderDeveloperMode"
+ "_reportId"
+ "_startOnLocationUpdate"
+ "_startTimestamp"
+ "_state"
+ "_successfulTapCount"
+ "_teamID"
+ "_teamIdentifier"
+ "_timestampDay"
+ "altitude"
+ "arrayWithCapacity:"
+ "bundleID"
+ "c"
+ "city"
+ "com.apple.developer.nfc.paymentreader.development"
+ "country"
+ "d"
+ "decodeDoubleForKey:"
+ "decodeInt64ForKey:"
+ "developmentPresentments"
+ "doubleValue"
+ "encodeDouble:forKey:"
+ "encodeInt64:forKey:"
+ "endTimestamp"
+ "horizontalAccuracy"
+ "initWithLatitude:longitude:altitude:horizontalAccuracy:city:state:country:"
+ "initWithReportId:timestampDay:bundleID:teamID:developmentPresentments:"
+ "initWithStartTimestamp:endTimestamp:latitude:longitude:altitude:horizontalAccuracy:city:state:country:successfulTapCount:"
+ "initWithUUIDString:"
+ "isDevTestMode"
+ "jsonDictionary"
+ "latitude"
+ "longitude"
+ "mode=%lu, type=%@%@%@%@"
+ "nfcPaymentTagReaderDeveloperMode"
+ "numberWithDouble:"
+ "reportId"
+ "sessionConfigWithUIMode:sessionType:initialScanText:vasPass:delayConnectionHandoverRestart:startOnLocationUpdate:isDevTestMode:"
+ "setIsDevTestMode:"
+ "setStartOnLocationUpdate:"
+ "setWithObjects:"
+ "startOnLocationUpdate"
+ "startTimestamp"
+ "successfulTapCount"
+ "teamID"
+ "teamIdentifier"
+ "timestampDay"
- "@52@0:8Q16Q24@32@40B48"
- "mode=%lu, type=%@, delayCHRestart=%d"
- "sessionConfigWithUIMode:sessionType:initialScanText:vasPass:delayConnectionHandoverRestart:"

```
