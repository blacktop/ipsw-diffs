## com.apple.iokit.IOHIDFamily

> `com.apple.iokit.IOHIDFamily`

```diff

   __TEXT.__cstring: 0x4d6d
   __TEXT.__os_log: 0x4921
   __TEXT.__const: 0x1d80
-  __TEXT_EXEC.__text: 0xa1ce8
+  __TEXT_EXEC.__text: 0xa1cbc
   __TEXT_EXEC.__auth_stubs: 0xd50
   __DATA.__data: 0xbea
   __DATA.__common: 0xe88
Sections:
~ __DATA.__data : content changed
~ __DATA_CONST.__mod_init_func : content changed
~ __DATA_CONST.__mod_term_func : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__kalloc_type : content changed
~ __DATA_CONST.__assert : content changed
~ __DATA_CONST.__kalloc_var : content changed
~ __DATA_CONST.__auth_got : content changed
~ __DATA_CONST.__got : content changed
~ __DATA_CONST.__auth_ptr : content changed
Functions:
~ _HIDGetReportLength : 232 -> 200
~ _HIDUsageAndPageFromIndex : 200 -> 212
~ __ZN11IOHIDSystem19registerScreenGatedEP16IOGraphicsDeviceP9IOGBoundsS3_Pi : 944 -> 972
~ __ZN12IOHIPointing12scalePointerEPiS0_ : 544 -> 528
~ __ZL17SetupAccelerationP6OSDataiiiPPvPj : 1172 -> 1148
~ __ZN12IOHIPointing37dispatchScrollWheelEventWithAccelInfoEiiiP15ScrollAccelInfoy : 1720 -> 1708

```
