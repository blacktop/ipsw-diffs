## ColourSensorFilterPlugin

> `/System/Library/HIDPlugins/ColourSensorFilterPlugin.plugin/ColourSensorFilterPlugin`

```diff

-1902.120.21.0.1
-  __TEXT.__text: 0x143e4
+2079.0.9.502.1
+  __TEXT.__text: 0x145a4
   __TEXT.__auth_stubs: 0x8d0
-  __TEXT.__const: 0x570
-  __TEXT.__cstring: 0x11e1
-  __TEXT.__oslogstring: 0x1c56
-  __TEXT.__gcc_except_tab: 0x2cc
-  __TEXT.__unwind_info: 0x328
+  __TEXT.__const: 0x4d0
+  __TEXT.__cstring: 0x1265
+  __TEXT.__oslogstring: 0x1ca7
+  __TEXT.__gcc_except_tab: 0x2dc
+  __TEXT.__unwind_info: 0x358
   __DATA_CONST.__auth_got: 0x470
   __DATA_CONST.__got: 0x78
   __DATA_CONST.__auth_ptr: 0x20
-  __DATA_CONST.__const: 0x328
-  __DATA_CONST.__cfstring: 0x780
+  __DATA_CONST.__const: 0x3a0
+  __DATA_CONST.__cfstring: 0x8a0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__data: 0x80
-  __DATA.__bss: 0x90
+  __DATA.__bss: 0xa0
   __DATA.__common: 0x8
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 3ECAEE0C-E094-3E55-A846-B9CEF3A2F49D
-  Functions: 239
-  Symbols:   287
-  CStrings:  434
+  UUID: B709D7F7-28AA-3134-A424-F3BCE3F3DB39
+  Functions: 254
+  Symbols:   296
+  CStrings:  456
 
Symbols:
+ _CBU_GetBacklightNode
+ _CBU_IsAppleSiliconMac
+ _CBU_IsInternalBuild
+ _CBU_IsTestModeEnabled
+ _CBU_PlatformNativelySupportsALS
+ _CBU_PlatformNativelySupportsColorALS
+ _CFAllocatorAllocateTyped
+ _IORegistryEntryFromPath
+ _ModelPrefix
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6resizeEmc
+ __ZNSt3__16localeC1Ev
+ __ZTVNSt3__115basic_streambufIcNS_11char_traitsIcEEEE
+ _create_uint32_array_from_cfdata
+ _find_bound
+ _get_float_from_bootarg
+ _get_uint32_from_cfdata
+ _load_bool_from_edt
+ _strtof
- _CBU_SyncDisplayStateControlSupported
- _CFAllocatorAllocate
- _CFPreferencesGetAppBooleanValue
- __Z10find_boundPKfmfPmS1_
- __Z22get_uint32_from_cfdataPKvPj
- __ZNSt3__115basic_streambufIcNS_11char_traitsIcEEEC2Ev
- __ZNSt3__115basic_streambufIcNS_11char_traitsIcEEED2Ev
- __Znwm
- _kCFPreferencesCurrentApplication
CStrings:
+ "CoreBrightness Test Mode is %s by %s = %d"
+ "EXBright calibration failed. CSFP will not load the calibration!"
+ "EXBright calibration succeeded."
+ "EXBrightCalibration"
+ "EXBrightCalibrationSuccess"
+ "IODeviceTree:/backlight"
+ "InternalBuild"
+ "MacBook"
+ "MacBookAir"
+ "MacBookPro"
+ "MacPro"
+ "Macmini"
+ "cb_enable_test_mode"
+ "iMac"
+ "iMacPro"
- "Synchronous display state control default override -> %i "
- "SynchronousDisplayStateControl"

```
