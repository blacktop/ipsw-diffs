## NetworkQuality

> `/System/Library/PrivateFrameworks/NetworkQuality.framework/NetworkQuality`

```diff

-186.0.0.0.0
-  __TEXT.__text: 0x18e60
-  __TEXT.__auth_stubs: 0xb70
+191.0.0.0.0
+  __TEXT.__text: 0x19148
+  __TEXT.__auth_stubs: 0xb80
   __TEXT.__objc_methlist: 0x1704
-  __TEXT.__const: 0x188
+  __TEXT.__const: 0x178
   __TEXT.__gcc_except_tab: 0x538
-  __TEXT.__cstring: 0x24c9
-  __TEXT.__oslogstring: 0x1731
-  __TEXT.__unwind_info: 0x4e8
+  __TEXT.__cstring: 0x2509
+  __TEXT.__oslogstring: 0x177a
+  __TEXT.__unwind_info: 0x4e0
   __TEXT.__objc_classname: 0x344
-  __TEXT.__objc_methname: 0x3f8a
+  __TEXT.__objc_methname: 0x3f8d
   __TEXT.__objc_methtype: 0xcd8
   __TEXT.__objc_stubs: 0x3400
   __DATA_CONST.__got: 0x188

   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0xa0
   __DATA_CONST.__objc_arraydata: 0x58
-  __AUTH_CONST.__auth_got: 0x5c8
+  __AUTH_CONST.__auth_got: 0x5d0
   __AUTH_CONST.__const: 0x80
   __AUTH_CONST.__cfstring: 0x1960
-  __AUTH_CONST.__objc_const: 0x3780
+  __AUTH_CONST.__objc_const: 0x3750
   __AUTH_CONST.__objc_intobj: 0x1c8
   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x7d0
-  __DATA.__objc_ivar: 0x3c4
+  __DATA.__objc_ivar: 0x3c0
   __DATA.__data: 0x360
   __DATA.__bss: 0x20
   __DATA.__common: 0x8

   - /System/Library/PrivateFrameworks/Rapport.framework/Rapport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 04878546-A4A8-3F2A-9B52-1A04803D40F5
-  Functions: 564
-  Symbols:   2328
-  CStrings:  1617
+  UUID: 761206DA-D980-32C7-870E-03EAD88A7C76
+  Functions: 563
+  Symbols:   2316
+  CStrings:  1618
 
Symbols:
+ -[NetworkQualityConfiguration hasCustomConfigurationSet]
+ -[NetworkQualityExecutions validateAndAdjustRuntimeParameters:]
+ -[NetworkQualityExecutions validateAndAdjustRuntimeParameters:].cold.1
+ GCC_except_table38
+ GCC_except_table50
+ _OBJC_IVAR_$_ThroughputDelegate._saturationReached
+ _network_config_get_l4s_enabled
+ _objc_msgSend$hasCustomConfigurationSet
+ _objc_msgSend$validateAndAdjustRuntimeParameters:
- -[NetworkQualityConfiguration setUseL4SServerPool:]
- -[NetworkQualityConfiguration useL4SServerPool]
- -[NetworkQualityExecutions initWithConfiguration:].cold.2
- GCC_except_table37
- GCC_except_table49
- _OBJC_IVAR_$_NetworkQualityConfiguration._useL4SServerPool
- _OBJC_IVAR_$_ThroughputDelegate._saturation_reached
- _objc_msgSend$setUseL4SServerPool:
- _objc_msgSend$useL4SServerPool
CStrings:
+ "%s:%u - Canceling with %ld"
+ "%s:%u - Minimum runtime %ld >= maxRuntime %ld, resetting minimum to %ld"
+ "%s:%u - Received non-HTTP message, canceling %@"
+ "%s:%u - [%d] Respawned task %@ using session %@ for %@"
+ "%s:%u - [%d] Task completed successfully, respawning to maintain flow count"
+ "-[NetworkQualityExecutions validateAndAdjustRuntimeParameters:]"
+ "_saturationReached"
+ "hasCustomConfigurationSet"
+ "validateAndAdjustRuntimeParameters:"
- "%s:%u - Cancelling with %ld"
- "%s:%u - Minimum runtime %ld >= maxRuntime %ld, resetting minimum to 0"
- "%s:%u - Received non-HTTP message, cancelling %@"
- "%s:%u - [Staging] parallel saturated - moving to draining"
- "TB,V_useL4SServerPool"
- "_useL4SServerPool"
- "setUseL4SServerPool:"
- "useL4SServerPool"

```
