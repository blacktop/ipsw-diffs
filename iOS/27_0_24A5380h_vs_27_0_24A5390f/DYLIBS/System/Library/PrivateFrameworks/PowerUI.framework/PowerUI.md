## PowerUI

> `/System/Library/PrivateFrameworks/PowerUI.framework/PowerUI`

### Sections with Same Size but Changed Content

- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH_CONST.__objc_floatobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-753.0.10.0.0
-  __TEXT.__text: 0xd99d0
-  __TEXT.__objc_methlist: 0x1d6d4
-  __TEXT.__const: 0x6c0
-  __TEXT.__cstring: 0xf77a
-  __TEXT.__oslogstring: 0xf09d
+753.0.15.0.0
+  __TEXT.__text: 0xd9c7c
+  __TEXT.__objc_methlist: 0x1d71c
+  __TEXT.__const: 0x6d0
+  __TEXT.__cstring: 0xf790
+  __TEXT.__oslogstring: 0xf0da
   __TEXT.__gcc_except_tab: 0x10c0
   __TEXT.__unwind_info: 0x2208
   __TEXT.__objc_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5e40
+  __DATA_CONST.__objc_selrefs: 0x5e78
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x3a0
   __DATA_CONST.__objc_arraydata: 0x71c0
   __DATA_CONST.__got: 0x5e0
   __AUTH_CONST.__const: 0x720
-  __AUTH_CONST.__cfstring: 0xdba0
-  __AUTH_CONST.__objc_const: 0x39f68
+  __AUTH_CONST.__cfstring: 0xdbc0
+  __AUTH_CONST.__objc_const: 0x39f98
   __AUTH_CONST.__objc_intobj: 0xab0
   __AUTH_CONST.__objc_arrayobj: 0x4e0
   __AUTH_CONST.__objc_dictobj: 0x2d0

   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH_CONST.__auth_got: 0x5e8
   __AUTH.__objc_data: 0x1b30
-  __DATA.__objc_ivar: 0x3ecc
+  __DATA.__objc_ivar: 0x3ed0
   __DATA.__data: 0x788
   __DATA.__bss: 0xc8
   __DATA_DIRTY.__objc_data: 0xb40

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 10642
-  Symbols:   17574
-  CStrings:  3202
+  Functions: 10650
+  Symbols:   17588
+  CStrings:  3204
 
Symbols:
+ +[PowerUIRuntimeAwarenessNotifier _ppsMaxRetryAttempts]
+ +[PowerUISmartChargeUtilities batteryStateAvailableWithContext:]
+ -[PowerUICECAlgoControlManager clearChargePolicy]
+ -[PowerUIDemoCECManager batteryContextRetryPending]
+ -[PowerUIDemoCECManager scheduleBatteryContextRetry]
+ -[PowerUIDemoCECManager setBatteryContextRetryPending:]
+ GCC_except_table38
+ GCC_except_table42
+ GCC_except_table48
+ GCC_except_table53
+ GCC_except_table57
+ GCC_except_table80
+ _OBJC_IVAR_$_PowerUIDemoCECManager._batteryContextRetryPending
+ ___52-[PowerUIDemoCECManager scheduleBatteryContextRetry]_block_invoke
+ _objc_msgSend$batteryStateAvailableWithContext:
+ _objc_msgSend$clearChargePolicy
+ _objc_msgSend$isCurrentPowerModeUserInitiated
+ _objc_msgSend$scheduleBatteryContextRetry
+ _objc_msgSend$setBatteryContextRetryPending:
- GCC_except_table37
- GCC_except_table56
- GCC_except_table79
- GCC_except_table85
- GCC_except_table89
CStrings:
+ "Battery context retry"
+ "Battery-state context not available yet; skipping evaluation for trigger: %@"
+ "Total time computed (%.0f hrs) is below the %.0f hr minimum coverage. Data may be incomplete or corrupted."
- "Total time computed (%.0f hrs) differs from expected 24 hours by %.0f hrs (>2 hours). Data may be incomplete or corrupted."
```
