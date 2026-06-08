## AppleMesaLib

> `/System/Library/Extensions/AppleBiometricSensor.kext/PlugIns/AppleMesaLib.plugin/AppleMesaLib`

```diff

-273.100.3.0.0
-  __TEXT.__text: 0x30c0
-  __TEXT.__auth_stubs: 0x1d0
+288.0.0.0.0
+  __TEXT.__text: 0x2b94
+  __TEXT.__auth_stubs: 0x1c0
   __TEXT.__const: 0x20
-  __TEXT.__gcc_except_tab: 0x1c
+  __TEXT.__gcc_except_tab: 0x14
   __TEXT.__oslogstring: 0x75
   __TEXT.__cstring: 0x1c7
   __TEXT.__unwind_info: 0xe8
-  __DATA_CONST.__auth_got: 0xf0
+  __DATA_CONST.__auth_got: 0xe8
   __DATA_CONST.__got: 0x38
   __DATA.__data: 0x110
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: 53265C03-E7AD-39C2-9643-1838B24CDCBE
+  UUID: E1B4E50D-4D28-3E11-BA79-8818FDE6025F
   Functions: 74
-  Symbols:   112
+  Symbols:   111
   CStrings:  42
 
Symbols:
- __Unwind_Resume
Functions:
~ __ZN10MesaPlugIn18SetCaptureCallbackEPvPFvmEmS0_m : 236 -> 192
~ _AppleMesaFactory : 512 -> 468
~ __ZN10MesaPlugInC2EPK8__CFUUID : 240 -> 196
~ __ZN10MesaPlugInD2Ev : 224 -> 172
~ __ZN10MesaPlugIn14QueryInterfaceE11CFUUIDBytesPPv : 516 -> 472
~ __ZN10MesaPlugIn6AddRefEv : 204 -> 160
~ __ZN10MesaPlugIn7ReleaseEv : 240 -> 196
~ __ZN10MesaPlugIn5ProbeEPK14__CFDictionaryjPi : 208 -> 164
~ __ZN10MesaPlugIn5StartEPK14__CFDictionaryj : 228 -> 184
~ __ZN10MesaPlugIn4StopEv : 204 -> 160
~ __ZN10MesaPlugIn5ResetE10eResetTypePhm : 396 -> 400
~ __ZN10MesaPlugIn4IdleEPhm : 356 -> 312
~ __ZN10MesaPlugIn12StartCaptureEPhm : 356 -> 312
~ __ZN10MesaPlugIn11StopCaptureEPhm : 356 -> 312
~ __ZN10MesaPlugIn12PauseCaptureEPhm : 356 -> 312
~ __ZN10MesaPlugIn9GetStatusEPhm : 356 -> 312
~ __ZN10MesaPlugIn15GetSerialNumberEPhm : 368 -> 324
~ __ZN10MesaPlugIn21GetModuleSerialNumberEPhm : 368 -> 324
~ __ZN10MesaPlugIn28GetModuleSerialNumberDynamicEPhPm : 416 -> 372
~ __ZN10MesaPlugIn18GoToProductionModeEPhm : 356 -> 312
~ __ZN10MesaPlugIn9LoadPatchEPvm : 356 -> 312
~ __ZN10MesaPlugIn9ProvisionEPhS0_m : 360 -> 316
~ __ZN10MesaPlugIn19ScheduleWithRunLoopEP11__CFRunLoopPK10__CFString : 280 -> 236
~ __ZN10MesaPlugIn21UnscheduleWithRunLoopEP11__CFRunLoopPK10__CFString : 268 -> 224
~ __ZN10MesaPlugIn13SetParametersEPhm : 352 -> 308
~ __ZN10MesaPlugIn10TriggerESDEv : 336 -> 292
~ __ZN10MesaPlugIn15TriggerSPIErrorEv : 336 -> 292
~ __ZN10MesaPlugIn18ClearPatchOverrideEv : 336 -> 292
~ __ZN10MesaPlugIn17StartFingerDetectEPhm : 356 -> 312
~ __ZN10MesaPlugIn11StartBurnInEPhm : 356 -> 312
~ __ZN10MesaPlugIn10StopSSHBHBEhPhm : 360 -> 316

```
