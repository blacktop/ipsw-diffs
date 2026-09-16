## ospredictiond

> `/usr/libexec/ospredictiond`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-286.2.1.0.0
-  __TEXT.__text: 0x67550
+288.40.3.0.0
+  __TEXT.__text: 0x67934
   __TEXT.__auth_stubs: 0x920
-  __TEXT.__objc_stubs: 0x9960
+  __TEXT.__objc_stubs: 0x99e0
   __TEXT.__objc_methlist: 0x93a0
   __TEXT.__const: 0x468
-  __TEXT.__cstring: 0x55b4
-  __TEXT.__objc_methname: 0x15478
-  __TEXT.__oslogstring: 0x7474
+  __TEXT.__cstring: 0x5605
+  __TEXT.__objc_methname: 0x154f4
+  __TEXT.__oslogstring: 0x7540
   __TEXT.__objc_classname: 0xe10
   __TEXT.__objc_methtype: 0x248d
   __TEXT.__gcc_except_tab: 0x8d0

   __DATA_CONST.__objc_arrayobj: 0x480
   __DATA_CONST.__objc_doubleobj: 0x70
   __DATA_CONST.__auth_got: 0x4a0
-  __DATA_CONST.__got: 0x4c8
+  __DATA_CONST.__got: 0x4d0
   __DATA.__objc_const: 0x10670
-  __DATA.__objc_selrefs: 0x3da0
+  __DATA.__objc_selrefs: 0x3dc0
   __DATA.__objc_ivar: 0xdc4
   __DATA.__objc_data: 0x27b0
   __DATA.__data: 0x780

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3339
-  Symbols:   287
-  CStrings:  4806
+  Functions: 3340
+  Symbols:   288
+  CStrings:  4814
 
Symbols:
+ _OBJC_CLASS_$_BMDeviceActivityPrediction
CStrings:
+ "Prediction"
+ "Queuing engagementEvent"
+ "Sent inactivity prediction event: confidenceLevel: %d - confidenceValue: %f - predictedDuration: %f - outputReason: %d"
+ "Unsupported Inactivity Predictor Output Confidence Level: %@"
+ "com.apple.osintelligence.inactivityprediction.addEventToActivityPredictionStream"
+ "initWithVersion:predictionType:confidenceLevel:confidenceValue:predictedDuration:outputReason:"
+ "sendEvent:"
+ "source"
```
