## Diagnostics

> `/Applications/Diagnostics.app/Diagnostics`

```diff

-820.120.91.0.0
-  __TEXT.__text: 0x14b5f4
-  __TEXT.__auth_stubs: 0x3a30
+820.122.1.0.0
+  __TEXT.__text: 0x14cbb0
+  __TEXT.__auth_stubs: 0x3a40
   __TEXT.__objc_stubs: 0x6ee0
   __TEXT.__objc_methlist: 0x6724
   __TEXT.__gcc_except_tab: 0xc6c
-  __TEXT.__objc_methname: 0xe0eb
+  __TEXT.__objc_methname: 0xe103
   __TEXT.__objc_classname: 0xabf
   __TEXT.__objc_methtype: 0x36ec
   __TEXT.__const: 0x6e74
-  __TEXT.__cstring: 0xd64b
+  __TEXT.__cstring: 0xd7ab
   __TEXT.__oslogstring: 0x3ae0
   __TEXT.__dlopen_cstrs: 0xfc
   __TEXT.__ustring: 0x64
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__constg_swiftt: 0x5b80
-  __TEXT.__swift5_typeref: 0x4e8e
+  __TEXT.__constg_swiftt: 0x5b88
+  __TEXT.__swift5_typeref: 0x4f12
   __TEXT.__swift5_builtin: 0x208
   __TEXT.__swift5_reflstr: 0x4547
   __TEXT.__swift5_fieldmd: 0x3704
   __TEXT.__swift5_assocty: 0x638
   __TEXT.__swift5_proto: 0x3a0
   __TEXT.__swift5_types: 0x334
-  __TEXT.__swift5_capture: 0x2314
+  __TEXT.__swift5_capture: 0x2390
   __TEXT.__swift_as_entry: 0x168
   __TEXT.__swift_as_ret: 0x148
   __TEXT.__swift5_protos: 0x48
   __TEXT.__swift5_mpenum: 0x20
   __TEXT.__swift5_acfuncs: 0x154
-  __TEXT.__unwind_info: 0x4398
+  __TEXT.__unwind_info: 0x43d0
   __TEXT.__eh_frame: 0x2f1c
-  __DATA_CONST.__auth_got: 0x1d28
-  __DATA_CONST.__got: 0x1138
-  __DATA_CONST.__auth_ptr: 0x1690
-  __DATA_CONST.__const: 0xb780
+  __DATA_CONST.__auth_got: 0x1d30
+  __DATA_CONST.__got: 0x1140
+  __DATA_CONST.__auth_ptr: 0x1398
+  __DATA_CONST.__const: 0xb928
   __DATA_CONST.__cfstring: 0x1dc0
   __DATA_CONST.__objc_classlist: 0x540
   __DATA_CONST.__objc_catlist: 0x28

   __DATA_CONST.__objc_arrayobj: 0x78
   __DATA_CONST.__objc_floatobj: 0x20
   __DATA.__objc_const: 0x208b8
-  __DATA.__objc_selrefs: 0x3d30
+  __DATA.__objc_selrefs: 0x3d40
   __DATA.__objc_ivar: 0x394
-  __DATA.__objc_data: 0x93d8
-  __DATA.__data: 0x6d78
+  __DATA.__objc_data: 0x93e0
+  __DATA.__data: 0x6d88
   __DATA.__bss: 0x6370
   __DATA.__common: 0x210
   - /System/Library/Frameworks/Combine.framework/Combine

   - /System/Library/PrivateFrameworks/CoreRepairCore.framework/CoreRepairCore
   - /System/Library/PrivateFrameworks/CoreSVG.framework/CoreSVG
   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
+  - /System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi
   - /System/Library/PrivateFrameworks/CosmeticAssessment.framework/CosmeticAssessment
   - /System/Library/PrivateFrameworks/DeviceIdentity.framework/DeviceIdentity
   - /System/Library/PrivateFrameworks/DiagnosticExtensionsDaemon.framework/DiagnosticExtensionsDaemon

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 6509
-  Symbols:   1807
-  CStrings:  4781
+  Functions: 6538
+  Symbols:   1809
+  CStrings:  4791
 
Symbols:
+ _$sSo21OS_dispatch_semaphoreC8DispatchE4waityyF
+ _OBJC_CLASS_$_CWFInterface
CStrings:
+ "ASSESSMENT_ALERT_ENABLE"
+ "ASSESSMENT_ALERT_ENABLE_WIFI_ENABLE_BUTTON_TITLE"
+ "ASSESSMENT_ALERT_ENABLE_WIFI_EXIT_BUTTON_TITLE"
+ "Failed to power on WiFi, error: %s"
+ "WiFi is active, allowing to proceed"
+ "WiFi is not active, prompting to enable"
+ "powerOn"
+ "setPower:error:"
+ "tapTurnOnFromEnableWiFi"
+ "viewWifiDisabled"

```
