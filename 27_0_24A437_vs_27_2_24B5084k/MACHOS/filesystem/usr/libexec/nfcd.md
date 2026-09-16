## nfcd

> `/usr/libexec/nfcd`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__got`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-370.42.1.0.0
-  __TEXT.__text: 0x1ea820
+371.7.0.0.0
+  __TEXT.__text: 0x1eb3e0
   __TEXT.__auth_stubs: 0x1920
   __TEXT.__delay_stubs: 0x540
   __TEXT.__delay_helper: 0x1878
-  __TEXT.__objc_stubs: 0xe3c0
-  __TEXT.__objc_methlist: 0x9f4c
-  __TEXT.__const: 0x144c
-  __TEXT.__cstring: 0x23238
-  __TEXT.__oslogstring: 0x20c81
-  __TEXT.__objc_classname: 0x1d83
-  __TEXT.__objc_methname: 0x15f91
-  __TEXT.__objc_methtype: 0x4e81
-  __TEXT.__unwind_info: 0x3a38
+  __TEXT.__objc_stubs: 0xe3e0
+  __TEXT.__objc_methlist: 0x9fcc
+  __TEXT.__const: 0x143c
+  __TEXT.__cstring: 0x23254
+  __TEXT.__oslogstring: 0x20d8b
+  __TEXT.__objc_classname: 0x1d7c
+  __TEXT.__objc_methname: 0x1600c
+  __TEXT.__objc_methtype: 0x4e7a
+  __TEXT.__unwind_info: 0x3a78
   __DATA_CONST.__const: 0x9ae0
   __DATA_CONST.__cfstring: 0x11920
   __DATA_CONST.__objc_classlist: 0x658

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x1d8
   __DATA_CONST.__objc_superrefs: 0x488
-  __DATA_CONST.__objc_intobj: 0x7db8
+  __DATA_CONST.__objc_intobj: 0x7dd0
   __DATA_CONST.__objc_arraydata: 0x1ea0
   __DATA_CONST.__objc_dictobj: 0x1090
   __DATA_CONST.__objc_arrayobj: 0x378
   __DATA_CONST.__auth_got: 0xd40
   __DATA_CONST.__got: 0xa18
   __DATA_CONST.__auth_ptr: 0x18
-  __DATA.__objc_const: 0x15238
-  __DATA.__objc_selrefs: 0x4cf8
-  __DATA.__objc_ivar: 0x1180
+  __DATA.__objc_const: 0x152a0
+  __DATA.__objc_selrefs: 0x4d08
+  __DATA.__objc_ivar: 0x118c
   __DATA.__objc_data: 0x3f70
   __DATA.__data: 0x2ba0
   __DATA.__common: 0x18

   - /usr/lib/libTelephonyBasebandDynamic.dylib
   - /usr/lib/libnfshared.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 4334
+  Functions: 4350
   Symbols:   686
-  CStrings:  11583
+  CStrings:  11591
 
CStrings:
+ "%{public}s:%i Dropping express capable field notification: expActive=%{public}d, sessionRequestedDrop=%{public}d, expDelayOrPaused=%{public}d"
+ "%{public}s:%i Queue error %{public}@"
+ "%{public}s:%i Session requires reader mode"
+ "%{public}s:%i Thermal pressure is moderate but cooloff already running."
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
+ "getSupportedFeatures"
+ "profileConnectionDidReceiveAllowCloudSyncChangedNotification:userInfo:"
+ "queueSession:errorHandler:"
+ "updateSMC"
- "%{public}s:%i Dropping express capable field notification"
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
