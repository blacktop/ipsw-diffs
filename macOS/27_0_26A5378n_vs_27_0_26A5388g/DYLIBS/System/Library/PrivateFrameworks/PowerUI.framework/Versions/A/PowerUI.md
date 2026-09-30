## PowerUI

> `/System/Library/PrivateFrameworks/PowerUI.framework/Versions/A/PowerUI`

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
-  __TEXT.__text: 0xc8160
-  __TEXT.__objc_methlist: 0x1bb6c
-  __TEXT.__const: 0x698
-  __TEXT.__cstring: 0xd99d
-  __TEXT.__oslogstring: 0xbfd3
+753.0.15.0.0
+  __TEXT.__text: 0xc8430
+  __TEXT.__objc_methlist: 0x1bbac
+  __TEXT.__const: 0x6a8
+  __TEXT.__cstring: 0xd9b3
+  __TEXT.__oslogstring: 0xc010
   __TEXT.__gcc_except_tab: 0xe08
   __TEXT.__dlopen_cstrs: 0x62
   __TEXT.__unwind_info: 0x1c98

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5298
+  __DATA_CONST.__objc_selrefs: 0x52c0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x340
   __DATA_CONST.__objc_arraydata: 0x70d8
   __DATA_CONST.__got: 0x4f0
   __AUTH_CONST.__const: 0x1810
-  __AUTH_CONST.__cfstring: 0xc640
-  __AUTH_CONST.__objc_const: 0x35e00
+  __AUTH_CONST.__cfstring: 0xc660
+  __AUTH_CONST.__objc_const: 0x35e30
   __AUTH_CONST.__objc_intobj: 0x9d8
   __AUTH_CONST.__objc_arrayobj: 0x498
   __AUTH_CONST.__objc_dictobj: 0x2d0

   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH_CONST.__auth_got: 0x4b8
   __AUTH.__objc_data: 0x19a0
-  __DATA.__objc_ivar: 0x3cd4
+  __DATA.__objc_ivar: 0x3cd8
   __DATA.__data: 0x5d8
   __DATA.__bss: 0xc8
   __DATA_DIRTY.__objc_data: 0x910

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 10020
-  Symbols:   16545
-  CStrings:  2718
+  Functions: 10027
+  Symbols:   16554
+  CStrings:  2720
 
Symbols:
+ +[PowerUISmartChargeUtilities batteryStateAvailableWithContext:]
+ -[PowerUICECAlgoControlManager clearChargePolicy]
+ -[PowerUIDemoCECManager batteryContextRetryPending]
+ -[PowerUIDemoCECManager scheduleBatteryContextRetry]
+ -[PowerUIDemoCECManager setBatteryContextRetryPending:]
+ GCC_except_table103
+ GCC_except_table55
+ GCC_except_table62
+ GCC_except_table91
+ GCC_except_table99
+ OBJC_IVAR_$_PowerUIDemoCECManager._batteryContextRetryPending
+ ___52-[PowerUIDemoCECManager scheduleBatteryContextRetry]_block_invoke
+ _objc_msgSend$batteryStateAvailableWithContext:
+ _objc_msgSend$clearChargePolicy
+ _objc_msgSend$scheduleBatteryContextRetry
+ _objc_msgSend$setBatteryContextRetryPending:
- GCC_except_table102
- GCC_except_table40
- GCC_except_table46
- GCC_except_table54
- GCC_except_table61
- GCC_except_table90
- GCC_except_table98
CStrings:
+ "Battery context retry"
+ "Battery-state context not available yet; skipping evaluation for trigger: %@"
+ "Total time computed (%.0f hrs) is below the %.0f hr minimum coverage. Data may be incomplete or corrupted."
- "Total time computed (%.0f hrs) differs from expected 24 hours by %.0f hrs (>2 hours). Data may be incomplete or corrupted."
```
