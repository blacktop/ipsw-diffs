## Diagnostic-8187

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8187.appex/Diagnostic-8187`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

 1374.2.2.0.0
-  __TEXT.__text: 0xa270
-  __TEXT.__auth_stubs: 0x650
-  __TEXT.__objc_stubs: 0x2760
-  __TEXT.__objc_methlist: 0xfe4
-  __TEXT.__gcc_except_tab: 0x878
+  __TEXT.__text: 0xad44
+  __TEXT.__auth_stubs: 0x670
+  __TEXT.__objc_stubs: 0x28e0
+  __TEXT.__objc_methlist: 0x107c
+  __TEXT.__gcc_except_tab: 0x8b0
   __TEXT.__const: 0x1fc
-  __TEXT.__objc_methname: 0x3063
+  __TEXT.__objc_methname: 0x3284
   __TEXT.__objc_classname: 0x193
-  __TEXT.__cstring: 0x831
-  __TEXT.__objc_methtype: 0xb3d
-  __TEXT.__oslogstring: 0xce7
-  __TEXT.__unwind_info: 0x3d8
-  __DATA_CONST.__const: 0xe0
-  __DATA_CONST.__cfstring: 0x7a0
+  __TEXT.__cstring: 0x917
+  __TEXT.__objc_methtype: 0xb48
+  __TEXT.__oslogstring: 0xebd
+  __TEXT.__unwind_info: 0x408
+  __DATA_CONST.__const: 0x108
+  __DATA_CONST.__cfstring: 0x8a0
   __DATA_CONST.__objc_classlist: 0x80
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_superrefs: 0x50
   __DATA_CONST.__objc_intobj: 0xc0
   __DATA_CONST.__objc_floatobj: 0x20
-  __DATA_CONST.__objc_doubleobj: 0x30
-  __DATA_CONST.__auth_got: 0x340
+  __DATA_CONST.__objc_doubleobj: 0x50
+  __DATA_CONST.__auth_got: 0x350
   __DATA_CONST.__got: 0x1d8
-  __DATA.__objc_const: 0x2160
-  __DATA.__objc_selrefs: 0xd38
-  __DATA.__objc_ivar: 0x18c
+  __DATA.__objc_const: 0x2208
+  __DATA.__objc_selrefs: 0xda0
+  __DATA.__objc_ivar: 0x198
   __DATA.__objc_data: 0x500
   __DATA.__data: 0x308
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 294
-  Symbols:   222
-  CStrings:  861
+  Functions: 313
+  Symbols:   224
+  CStrings:  899
 
Symbols:
+ _IOPSShippingChargeLimitEnable
+ _IOPSShippingChargeLimitGetState
CStrings:
+ "%1"
+ "B20@0:8f16"
+ "Device is not shipping compliant. Starting drain."
+ "Failed to enable shipping charge limit: 0x%x"
+ "Failed to query shipping charge limit state: 0x%x"
+ "Reached variance target (%.0f%%). Enabling charge limit."
+ "ShipChargeLimitCompliant"
+ "ShipChargeLimitEnabled"
+ "ShipChargeLimitSupported"
+ "Shipping charge limit enable completion failed: 0x%x"
+ "Shipping charge limit not supported on this device"
+ "Shipping compliant at %.0f%%. Completing compliance flow."
+ "Shipping compliant at %.0f%%. Draining to %.0f%% for variance."
+ "Successfully enabled shipping charge limit"
+ "T@\"NSNumber\",&,N,V_shippingComplianceDrainVariance"
+ "TB,N,V_shippingComplianceMode"
+ "Tf,N,V_varianceDrainTarget"
+ "Tf,R"
+ "_shippingComplianceDrainVariance"
+ "_shippingComplianceMode"
+ "_varianceDrainTarget"
+ "completeShippingComplianceFlow"
+ "enableShippingChargeLimit"
+ "handleShippingComplianceCheckAtBatteryLevel:"
+ "handleShippingCompliantAtLevel:"
+ "isShippingChargeLimitSupported"
+ "isShippingCompliant"
+ "minLOD"
+ "s"
+ "setShippingComplianceDrainVariance:"
+ "setShippingComplianceMode:"
+ "setVarianceDrainTarget:"
+ "shipChargeLimitCompliant"
+ "shipChargeLimitEnabled"
+ "shipChargeLimitSupported"
+ "shippingComplianceDrainVariance"
+ "shippingComplianceMode"
+ "v20@?0i8^{__CFDictionary=}12"
+ "varianceDrainTarget"
- "S"
```
