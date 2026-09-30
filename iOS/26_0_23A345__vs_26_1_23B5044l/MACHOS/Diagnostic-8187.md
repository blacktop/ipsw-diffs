## Diagnostic-8187

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8187.appex/Diagnostic-8187`

```diff

-1066.2.1.0.0
-  __TEXT.__text: 0x7cec
-  __TEXT.__auth_stubs: 0x670
+1066.40.34.0.0
+  __TEXT.__text: 0x7cdc
+  __TEXT.__auth_stubs: 0x650
   __TEXT.__objc_stubs: 0x1dc0
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0xa14
   __TEXT.__const: 0x200
   __TEXT.__gcc_except_tab: 0x270
-  __TEXT.__cstring: 0x785
-  __TEXT.__oslogstring: 0xb1a
+  __TEXT.__cstring: 0x788
+  __TEXT.__oslogstring: 0xbac
   __TEXT.__objc_methname: 0x21f0
   __TEXT.__objc_classname: 0x13a
   __TEXT.__objc_methtype: 0x436
-  __TEXT.__unwind_info: 0x290
-  __DATA_CONST.__auth_got: 0x350
-  __DATA_CONST.__got: 0x168
+  __TEXT.__unwind_info: 0x298
+  __DATA_CONST.__auth_got: 0x340
+  __DATA_CONST.__got: 0x158
   __DATA_CONST.__const: 0xe0
   __DATA_CONST.__cfstring: 0x780
   __DATA_CONST.__objc_classlist: 0x58

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x38
   __DATA_CONST.__objc_intobj: 0xc0
-  __DATA_CONST.__objc_floatobj: 0x30
+  __DATA_CONST.__objc_floatobj: 0x20
+  __DATA_CONST.__objc_doubleobj: 0x30
   __DATA.__objc_const: 0x15b8
   __DATA.__objc_selrefs: 0x920
   __DATA.__objc_ivar: 0x134
   __DATA.__objc_data: 0x370
   __DATA.__data: 0x188
   __DATA.__common: 0x60
-  __DATA.__bss: 0xc
+  __DATA.__bss: 0x18
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Accelerate

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 63466C4C-47CD-32FD-858A-3B6AD8528802
+  UUID: B7460947-D551-32EC-A4BA-37FFD65E89CA
   Functions: 228
-  Symbols:   207
-  CStrings:  688
+  Symbols:   204
+  CStrings:  691
 
Symbols:
+ _IOPSLimitBatteryLevel
+ _IOPSLimitBatteryLevelCancel
+ _IOPSLimitBatteryLevelRegister
+ _OBJC_CLASS_$_NSConstantDoubleNumber
+ _cblas_sgemm$NEWLAPACK$ILP64
- _CFDictionaryCreateMutable
- _CFDictionarySetValue
- _CFRelease
- _IORegistryEntrySetCFProperties
- _IOServiceGetMatchingService
- _cblas_sgemm
- _kCFBooleanFalse
- _kCFBooleanTrue
Functions:
~ sub_100004c00 -> sub_100004c50 : 400 -> 452
~ sub_100004d90 -> sub_100004e14 : 400 -> 320
~ sub_100005854 -> sub_100005888 : 884 -> 908
~ sub_100006d88 -> sub_100006dd4 : 1132 -> 1120
CStrings:
+ "Battery Service Drain Test"
+ "Not disabling charging as it was already disabled."
+ "Not enabling charging as it was already enabled."
+ "Successfully disabled charging."
+ "Successfully enabled charging."
+ "Unable to acquire battery limit token. Reason: 0x%x"
- "FieldDiagsInflowInhibit"
- "Successfully disabled charging: %d"
- "Successfully enabled charging: %d"

```
