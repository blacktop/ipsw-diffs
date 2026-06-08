## libWISSupport.dylib

> `/usr/lib/libWISSupport.dylib`

```diff

-283.0.0.0.0
-  __TEXT.__text: 0x287fc
-  __TEXT.__auth_stubs: 0x880
-  __TEXT.__gcc_except_tab: 0x309c
-  __TEXT.__cstring: 0x638
-  __TEXT.__const: 0xdfa
+335.0.0.0.0
+  __TEXT.__text: 0x281fc
+  __TEXT.__gcc_except_tab: 0x2fdc
+  __TEXT.__cstring: 0x710
+  __TEXT.__const: 0xdfb
   __TEXT.__oslogstring: 0x7a
-  __TEXT.__unwind_info: 0x11c8
-  __DATA_CONST.__got: 0xb0
-  __DATA_CONST.__const: 0x138
-  __AUTH_CONST.__auth_got: 0x448
+  __TEXT.__unwind_info: 0x1238
+  __TEXT.__auth_stubs: 0x0
+  __DATA_CONST.__const: 0x160
+  __DATA_CONST.__weak_got: 0x8
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x1580
-  __AUTH_CONST.__cfstring: 0x180
+  __AUTH_CONST.__cfstring: 0x220
+  __AUTH_CONST.__weak_auth_got: 0x18
+  __AUTH_CONST.__auth_got: 0x0
+  __DATA.__data: 0x28
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libprotobuf-lite.dylib
-  UUID: 680BCB76-832D-332A-9DF8-4364AC3EAC60
-  Functions: 810
-  Symbols:   312
-  CStrings:  153
+  UUID: 735F359A-81A2-3BBD-96F4-983569D4D231
+  Functions: 822
+  Symbols:   322
+  CStrings:  168
 
Symbols:
+ __ZN3wis23kWISAnomalyLearnMoreKeyE
+ __ZN3wis24kWISAnomalyResolutionKeyE
+ __ZN3wis25kWISAnomalyCarrierNameKeyE
+ __ZN3wis37kWISAnomalySubCategoryOutageConfirmedE
+ __ZN3wis37kWISAnomalySubCategoryOutagePotentialE
+ __ZN3wis44WISCellularOutageAwarenessDataRequestMessageE
+ __ZN3wis46WISCellularQualityGetCurrentDataRequestMessageE
+ __ZN3wis49WISCellularQualityDataAvailabilityCallbackMessageE
+ __ZN3wis64WISCellularQualityRegisterDataAvailabilityCallbackRequestMessageE
+ __ZN3wis66WISCellularQualityUnregisterDataAvailabilityCallbackRequestMessageE
CStrings:
+ "CarrierName"
+ "GetCellularOutageDetails"
+ "GetCurrentData"
+ "LearnMore"
+ "OutageConfirmed"
+ "OutagePotential"
+ "RegisterDataAvailabilityCallback"
+ "Resolution"
+ "UnregisterDataAvailabilityCallback"
+ "WISCellularQualityDataAvailabilityCallback"

```
