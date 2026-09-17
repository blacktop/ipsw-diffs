## nfcd

> `/usr/libexec/nfcd`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-370.42.1.0.0
-  __TEXT.__text: 0x16ef44
+371.7.0.0.0
+  __TEXT.__text: 0x16f7d8
   __TEXT.__auth_stubs: 0x13f0
   __TEXT.__delay_helper: 0x1f4
-  __TEXT.__objc_stubs: 0x9f00
-  __TEXT.__objc_methlist: 0x75e0
+  __TEXT.__objc_stubs: 0x9f20
+  __TEXT.__objc_methlist: 0x7638
   __TEXT.__const: 0x10cc
-  __TEXT.__cstring: 0x1884c
-  __TEXT.__oslogstring: 0x185d6
-  __TEXT.__objc_classname: 0x14f5
-  __TEXT.__objc_methname: 0x10a97
-  __TEXT.__objc_methtype: 0x3dbf
-  __TEXT.__unwind_info: 0x2788
+  __TEXT.__cstring: 0x1886a
+  __TEXT.__oslogstring: 0x18644
+  __TEXT.__objc_classname: 0x14ee
+  __TEXT.__objc_methname: 0x10acb
+  __TEXT.__objc_methtype: 0x3de4
+  __TEXT.__unwind_info: 0x27b8
   __DATA_CONST.__const: 0x6d70
   __DATA_CONST.__cfstring: 0xe980
   __DATA_CONST.__objc_classlist: 0x4d0

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x158
   __DATA_CONST.__objc_superrefs: 0x338
-  __DATA_CONST.__objc_intobj: 0x5ef8
+  __DATA_CONST.__objc_intobj: 0x5f10
   __DATA_CONST.__objc_arraydata: 0x1a38
   __DATA_CONST.__objc_dictobj: 0xbe0
   __DATA_CONST.__objc_arrayobj: 0x180
   __DATA_CONST.__auth_got: 0xa00
   __DATA_CONST.__got: 0x710
-  __DATA.__objc_const: 0x10120
-  __DATA.__objc_selrefs: 0x3a98
-  __DATA.__objc_ivar: 0xcfc
+  __DATA.__objc_const: 0x10180
+  __DATA.__objc_selrefs: 0x3aa0
+  __DATA.__objc_ivar: 0xd08
   __DATA.__objc_data: 0x3020
   __DATA.__data: 0x1dfc
   __DATA.__common: 0x8

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libnfshared.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3120
+  Functions: 3131
   Symbols:   509
-  CStrings:  8803
+  CStrings:  8812
 
CStrings:
+ "%{public}s:%i Queue error %{public}@"
+ "%{public}s:%i Session requires reader mode"
+ "%{public}s:%i eUICC OS reset."
+ "-[NFSMCInterface open]"
+ "-[NFSMCInterface setReaderModeActive:]"
+ "-[NFSMCInterface updateSMC]"
+ "-[_NFHardwareManager(SessionQueue) queueSession:errorHandler:]_block_invoke"
+ "@\"NFSMCInterface\""
+ "NFCD built from (B&I) Stockholm_Base-371.7"
+ "NFSMCInterface"
+ "_currentPower"
+ "_currentTemperature"
+ "_smcInterface"
+ "a"
+ "f"
+ "getSupportedFeatures"
+ "queueSession:errorHandler:"
+ "updateSMC"
+ "v32@0:8@\"_NFSession\"16@?<v@?@\"NSError\">24"
- "-[NFTemperatureReporter open]"
- "-[NFTemperatureReporter setReaderModeActive:]"
- "-[NFTemperatureReporter updateTemperature:]"
- "@\"NFTemperatureReporter\""
- "NFCD built from (B&I) Stockholm_Base-370.42.1"
- "NFTemperatureReporter"
- "_temperatureReporter"
- "eUICC OS reset"
- "queueSession:"
- "updateTemperature:"
```
