## LightSourceSupport

> `/System/Library/PrivateFrameworks/LightSourceSupport.framework/LightSourceSupport`

```diff

-7.0.84.1.102
-  __TEXT.__text: 0xf0f0
+7.1.4.0.0
+  __TEXT.__text: 0xf484
   __TEXT.__auth_stubs: 0x7b0
   __TEXT.__objc_methlist: 0xb94
   __TEXT.__const: 0xe0
-  __TEXT.__cstring: 0xb91
-  __TEXT.__oslogstring: 0x7e2
+  __TEXT.__cstring: 0xb7a
+  __TEXT.__oslogstring: 0x863
   __TEXT.__gcc_except_tab: 0x46c
-  __TEXT.__unwind_info: 0x5f8
+  __TEXT.__unwind_info: 0x600
   __TEXT.__objc_classname: 0x2d5
-  __TEXT.__objc_methname: 0x1602
-  __TEXT.__objc_methtype: 0x83e
+  __TEXT.__objc_methname: 0x1638
+  __TEXT.__objc_methtype: 0x841
   __TEXT.__objc_stubs: 0x1000
   __DATA_CONST.__got: 0x158
-  __DATA_CONST.__const: 0x3d0
+  __DATA_CONST.__const: 0x3d8
   __DATA_CONST.__objc_classlist: 0xf0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x38

   __DATA_CONST.__objc_arraydata: 0x20
   __AUTH_CONST.__auth_got: 0x3f0
   __AUTH_CONST.__const: 0x340
-  __AUTH_CONST.__cfstring: 0x660
-  __AUTH_CONST.__objc_const: 0x3000
+  __AUTH_CONST.__cfstring: 0x680
+  __AUTH_CONST.__objc_const: 0x3060
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH_CONST.__objc_doubleobj: 0x120
+  __AUTH_CONST.__objc_doubleobj: 0x130
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH.__objc_data: 0x2d0
   __AUTH.__thread_vars: 0x30
   __AUTH.__thread_bss: 0x38
-  __DATA.__objc_ivar: 0x260
+  __DATA.__objc_ivar: 0x26c
   __DATA.__data: 0x2a8
   __DATA_DIRTY.__objc_data: 0x690
   __DATA_DIRTY.__bss: 0x190

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: DBB33FC4-7944-340E-A60C-6FC849021376
-  Functions: 411
-  Symbols:   1756
-  CStrings:  741
+  UUID: 9560C2A2-3B08-3ADD-B2C2-DBCDAB837604
+  Functions: 414
+  Symbols:   1770
+  CStrings:  748
 
Symbols:
+ -[LSSCAParamsDictionary count]
+ -[LSSCAParamsDictionary initWithObjects:forKeys:count:]
+ -[LSSCAParamsDictionary keyEnumerator]
+ -[LSSCAParamsDictionary objectForKey:]
+ -[LSSCAParamsDictionary params]
+ -[LSSCAParamsDictionary setParams:]
+ -[LSSCAService setLightForDynamicDisplays:].cold.3
+ -[LSSMotionBasedProvider _updateLight:motionLevel:activateLevel:deactivateLevel:timestamp:]
+ -[LSSMotionBasedProvider _updateReference:motionLevel:activateLevel:deactivateLevel:]
+ _LSSCAParamsAlmostEqual
+ _LSSCAParamsMake
+ _LSSLightDirectionFromTimeInInterval.cold.2
+ _LSSLightDirectionFromTimeInInterval.cold.3
+ _LSSLightDirectionFromTimeInInterval.cold.4
+ _LSSLogMotionBasedLightService
+ _LSSLogMotionBasedLightService.cold.1
+ _LSSSettingsMotionLightFullQualityThreshold
+ _OBJC_CLASS_$_LSSCAParamsDictionary
+ _OBJC_IVAR_$_LSSCAParamsDictionary._params
+ _OBJC_IVAR_$_LSSCAService._actualUpdateCount
+ _OBJC_IVAR_$_LSSCAService._requestedUpdateCount
+ _OBJC_IVAR_$_LSSMotionBasedProvider._motionIsLow
+ _OBJC_METACLASS_$_LSSCAParamsDictionary
+ __OBJC_$_INSTANCE_METHODS_LSSCAParamsDictionary
+ __OBJC_$_INSTANCE_VARIABLES_LSSCAParamsDictionary
+ __OBJC_$_PROP_LIST_LSSCAParamsDictionary
+ __OBJC_CLASS_RO_$_LSSCAParamsDictionary
+ __OBJC_METACLASS_RO_$_LSSCAParamsDictionary
+ ___63-[LSSCAService observeValueForKeyPath:ofObject:change:context:]_block_invoke.18
+ ___block_literal_global.161
+ ___block_literal_global.175
+ ___block_literal_global.177
- -[LSSMotionBasedProvider _updateLight:motionLevel:timestamp:]
- -[LSSMotionBasedProvider _updateReference:motionLevel:]
- -[_LSSCAParamsDictionary count]
- -[_LSSCAParamsDictionary initWithObjects:forKeys:count:]
- -[_LSSCAParamsDictionary keyEnumerator]
- -[_LSSCAParamsDictionary objectForKey:]
- -[_LSSCAParamsDictionary params]
- -[_LSSCAParamsDictionary setParams:]
- _LSSLightDirectionInterp
- _LSSLightDirectionInterp.cold.1
- _LSSLightDirectionInterp.cold.2
- _OBJC_CLASS_$__LSSCAParamsDictionary
- _OBJC_IVAR_$__LSSCAParamsDictionary._params
- _OBJC_METACLASS_$__LSSCAParamsDictionary
- __OBJC_$_INSTANCE_METHODS__LSSCAParamsDictionary
- __OBJC_$_INSTANCE_VARIABLES__LSSCAParamsDictionary
- __OBJC_$_PROP_LIST__LSSCAParamsDictionary
- __OBJC_CLASS_RO_$__LSSCAParamsDictionary
- __OBJC_METACLASS_RO_$__LSSCAParamsDictionary
- ___49-[LSSMotionBasedProvider initWithQueue:delegate:]_block_invoke.cold.3
- ___63-[LSSCAService observeValueForKeyPath:ofObject:change:context:]_block_invoke.34
- ___block_literal_global.156
- ___block_literal_global.160
- ___block_literal_global.172
CStrings:
+ "@\"LSSCAParamsDictionary\""
+ "@112@0:8{?=d{?=}fI}16"
+ "LSSCAParamsDictionary"
+ "[32{?=\"time\"d\"direction\"\"referenceOrientation\"{?=\"vector\"}\"intensity\"f\"activityLevel\"I}]"
+ "_InterpLightState"
+ "_actualUpdateCount"
+ "_motionIsLow"
+ "_requestedUpdateCount"
+ "a.time <= time"
+ "high quality"
+ "infinite quaternion (%f, %f, %f, %f) -> (%f, %f, %f, %f)"
+ "motion_lightFullQualityThreshold"
+ "time <= b.time"
+ "update filter. requested: %lu. actual: %lu. percentage: %g"
+ "v112@0:8{?=d{?=}fI}16"
+ "v120@0:8@\"<LSSProvider>\"16{?=d{?=}fI}24"
+ "v120@0:8@\"LSSXPCClient\"16{?=d{?=}fI}24"
+ "v120@0:8@16{?=d{?=}fI}24"
+ "{?=\"time\"d\"direction\"\"referenceOrientation\"{?=\"vector\"}\"intensity\"f\"activityLevel\"I}"
+ "\xa1"
- "!a.expectPause"
- "@\"_LSSCAParamsDictionary\""
- "@112@0:8{?=dd{?=}B}16"
- "LSSLightDirectionInterp"
- "[32{?=\"time\"d\"intensity\"d\"direction\"\"referenceOrientation\"{?=\"vector\"}\"expectPause\"B}]"
- "_LSSCAParamsDictionary"
- "_QuaternionFromCMAttitudeQuaternion"
- "simd_all(isfinite(r.vector))"
- "v112@0:8{?=dd{?=}B}16"
- "v120@0:8@\"<LSSProvider>\"16{?=dd{?=}B}24"
- "v120@0:8@\"LSSXPCClient\"16{?=dd{?=}B}24"
- "v120@0:8@16{?=dd{?=}B}24"
- "{?=\"time\"d\"intensity\"d\"direction\"\"referenceOrientation\"{?=\"vector\"}\"expectPause\"B}"
- "\x81"

```
