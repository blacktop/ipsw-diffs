## batteryintelligenced

> `/usr/libexec/batteryintelligenced`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__got`
- `__DATA.__objc_data`

```diff

-231.40.1.0.0
-  __TEXT.__text: 0x45f44
+238.60.2.0.0
+  __TEXT.__text: 0x47004
   __TEXT.__auth_stubs: 0xb10
-  __TEXT.__objc_stubs: 0x54e0
-  __TEXT.__objc_methlist: 0x35c4
-  __TEXT.__cstring: 0x3922
-  __TEXT.__objc_classname: 0x7f6
-  __TEXT.__objc_methname: 0x71c9
-  __TEXT.__objc_methtype: 0x1601
+  __TEXT.__objc_stubs: 0x5740
+  __TEXT.__objc_methlist: 0x36fc
+  __TEXT.__cstring: 0x3a06
+  __TEXT.__objc_classname: 0x803
+  __TEXT.__objc_methname: 0x73e5
+  __TEXT.__objc_methtype: 0x1697
   __TEXT.__const: 0x3f0
-  __TEXT.__oslogstring: 0x8d70
+  __TEXT.__oslogstring: 0x8fdd
   __TEXT.__gcc_except_tab: 0x38c
-  __TEXT.__unwind_info: 0x1508
-  __DATA_CONST.__const: 0xd40
-  __DATA_CONST.__cfstring: 0x4300
+  __TEXT.__unwind_info: 0x1548
+  __DATA_CONST.__const: 0xd60
+  __DATA_CONST.__cfstring: 0x4460
   __DATA_CONST.__objc_classlist: 0x1f8
-  __DATA_CONST.__objc_protolist: 0x60
+  __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x1d8
-  __DATA_CONST.__objc_arraydata: 0xde0
+  __DATA_CONST.__objc_arraydata: 0xde8
   __DATA_CONST.__objc_arrayobj: 0x558
-  __DATA_CONST.__objc_intobj: 0xf00
-  __DATA_CONST.__objc_doubleobj: 0xd0
+  __DATA_CONST.__objc_intobj: 0xf90
+  __DATA_CONST.__objc_doubleobj: 0x120
   __DATA_CONST.__objc_dictobj: 0x50
   __DATA_CONST.__auth_got: 0x598
   __DATA_CONST.__got: 0x348
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA.__objc_const: 0x7eb0
-  __DATA.__objc_selrefs: 0x1b40
-  __DATA.__objc_ivar: 0x3b0
+  __DATA.__objc_const: 0x82b0
+  __DATA.__objc_selrefs: 0x1bd0
+  __DATA.__objc_ivar: 0x3bc
   __DATA.__objc_data: 0x13b0
-  __DATA.__data: 0x528
+  __DATA.__data: 0x588
   - /AppleInternal/Library/Frameworks/PerformanceControlKitInternal.framework/PerformanceControlKitInternal
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreML.framework/CoreML

   - /usr/lib/libSMC.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1638
+  Functions: 1662
   Symbols:   283
-  CStrings:  2770
+  CStrings:  2819
 
CStrings:
+ "@\"<SMCAccessing>\""
+ "@\"NSData\"28@0:8@\"NSString\"16I24"
+ "@\"NSNumber\"24@0:8@\"NSString\"16"
+ "B24@0:8@\"NSString\"16"
+ "B28@0:8@\"NSString\"16I24"
+ "B28@0:8@\"NSString\"16f24"
+ "BATTERYINTELLIGENCE_TLC"
+ "Lookup table prediction: SOC=%.2f in bucket [%@-%@] threshold=%.2f°C, temp=%.2f°C, willHitTLC=%d, confidence=%.2f"
+ "Lookup table prediction: SOC=%.2f is not covered by any bucket, willHitTLC=0, confidence=%.2f"
+ "ML model not loaded, falling back to the lookup table"
+ "No %@ from trial, using default %.2f°C"
+ "No predictionMethod from trial, using method %ld"
+ "Notifying %lu registered clients of prediction update"
+ "Plugged in at SOC %u, caching a prediction"
+ "SMCAccessing"
+ "Sending TLC update to client: willHitTLC=%d, confidence=%.2f, error=%{public}@"
+ "T@\"<SMCAccessing>\",&,N,V_smcManager"
+ "T@\"NSDictionary\",C,N,V_trialLookupThresholds"
+ "TLCLookupTableThreshold60To64"
+ "TLCLookupTableThreshold65To69"
+ "TLCLookupTableThreshold70To74"
+ "TLCLookupTableThreshold75To79"
+ "TLCLookupTableThreshold80To99"
+ "Tq,N,V_predictionMethod"
+ "Trial %@ of %.2f°C is outside [%.1f, %.1f]°C, using default %.2f°C"
+ "Trial predictionMethod %lld is not a supported method, using method %ld"
+ "Using %@ = %.2f°C from trial"
+ "Using predictionMethod %ld from trial"
+ "_predictionMethod"
+ "_trialLookupThresholds"
+ "batteryChargerData"
+ "currentUISOC"
+ "hashTableWithOptions:"
+ "isModelLoaded"
+ "loadLookupThresholds"
+ "loadPredictionMethod"
+ "longValue"
+ "lookupBucketForSOC:"
+ "lookupBuckets"
+ "lookupConfidenceForMargin:"
+ "maxSOC"
+ "maxTempC"
+ "minSOC"
+ "predictionMethod"
+ "rawBatteryVirtualTemperatureCentiC"
+ "rawNominalChargeCapacityMah"
+ "runLookupTableWithInputs:"
+ "runModelPrediction:error:"
+ "setInterface:forSelector:argumentIndex:ofReply:"
+ "setPredictionMethod:"
+ "setTrialLookupThresholds:"
+ "strongToStrongObjectsMapTable"
+ "trialFactor"
+ "trialLookupThresholds"
+ "willHitTLC"
- ")"
- "ML model not loaded, cannot run prediction"
- "Using fallback prediction: willHitTLC=%d, confidence=%.2f, method=Fallback"
- "fallbackPredictionWithInputs:"
- "weakObjectsHashTable"
- "weakToWeakObjectsMapTable"
```
