## batteryintelligenced

> `/usr/libexec/batteryintelligenced`

```diff

-167.0.0.0.1
-  __TEXT.__text: 0x30424
+174.0.0.0.0
+  __TEXT.__text: 0x30b80
   __TEXT.__auth_stubs: 0x8b0
-  __TEXT.__objc_stubs: 0x3640
-  __TEXT.__objc_methlist: 0x1f94
-  __TEXT.__cstring: 0x2999
+  __TEXT.__objc_stubs: 0x3660
+  __TEXT.__objc_methlist: 0x1f8c
+  __TEXT.__cstring: 0x29b3
   __TEXT.__objc_classname: 0x5d9
-  __TEXT.__objc_methtype: 0x766
+  __TEXT.__objc_methtype: 0x771
   __TEXT.__const: 0x1f8
-  __TEXT.__oslogstring: 0x52ae
-  __TEXT.__objc_methname: 0x4295
+  __TEXT.__objc_methname: 0x42b2
+  __TEXT.__oslogstring: 0x54bb
   __TEXT.__gcc_except_tab: 0x278
-  __TEXT.__unwind_info: 0x888
+  __TEXT.__unwind_info: 0x890
   __DATA_CONST.__auth_got: 0x468
   __DATA_CONST.__got: 0x230
-  __DATA_CONST.__const: 0x988
-  __DATA_CONST.__cfstring: 0x2ec0
+  __DATA_CONST.__const: 0x9a8
+  __DATA_CONST.__cfstring: 0x2ee0
   __DATA_CONST.__objc_classlist: 0x170
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_superrefs: 0x150
   __DATA_CONST.__objc_arraydata: 0x6a0
   __DATA_CONST.__objc_arrayobj: 0x480
-  __DATA_CONST.__objc_intobj: 0x810
-  __DATA_CONST.__objc_doubleobj: 0x40
+  __DATA_CONST.__objc_intobj: 0x840
+  __DATA_CONST.__objc_doubleobj: 0x50
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA.__objc_const: 0x5038
   __DATA.__objc_selrefs: 0x1088
   __DATA.__objc_ivar: 0x23c
   __DATA.__objc_data: 0xe60
   __DATA.__data: 0x2e0
-  __DATA.__bss: 0x1c8
+  __DATA.__bss: 0x1d8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreML.framework/CoreML
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9A71C492-34D0-3054-9503-8E8120BCA81F
-  Functions: 985
+  UUID: ACD4E385-D214-310D-9FE3-31439F4349BB
+  Functions: 993
   Symbols:   226
-  CStrings:  2163
+  CStrings:  2170
 
CStrings:
+ "D79"
+ "Device does not contain power telemetry table. Using default (median) system power value instead: %@ mW."
+ "Device reached %@ endSOC within %0.02f secs. Short charging session threshold: %.02f secs."
+ "Device reached %d in %@, First estimate for the latest charging session was %@."
+ "Did not receive a valid endSOC Enum value. Returning 0 seconds as short charging session threshold"
+ "Did not receive a valid short charging session threshold. Aborting computing core analytics metrics."
+ "Estimate for %@ target updated - output: %@, additional information: %@"
+ "Sent BIBatteryAnalysisOutput for %@ target - output: %@, additional information: %@."
+ "Successfully posted internal comparison notification."
+ "Target %@ updated with additional information: %@"
+ "Unable to load power telemetry table for device."
+ "XPC handler is nil/invalid for target: %@. Client disconnected or connection invalid. Cannot deliver response."
+ "d24@0:8q16"
+ "shortChargingSessionThresholdForEndSOCEnum:"
- "Battery Analysis additionalInformation for %@ target updated: %@"
- "Battery Analysis estimate for %@ target updated:%@"
- "Device reached %@ endSOC within %0.02f seconds"
- "Device reached %d in %@, First estimate at plugin was %@."
- "Sent BIBatteryAnalysisOutput for %@ target: %@."
- "Successfully posted internal notification."
- "getDeviceModel"

```
