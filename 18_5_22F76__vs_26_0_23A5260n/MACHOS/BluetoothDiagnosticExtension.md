## BluetoothDiagnosticExtension

> `/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/BluetoothDiagnosticExtension.appex/BluetoothDiagnosticExtension`

```diff

-185.7.0.0.0
-  __TEXT.__text: 0xf8c
-  __TEXT.__auth_stubs: 0x240
+190.40.1.2.0
+  __TEXT.__text: 0x112c
+  __TEXT.__auth_stubs: 0x250
   __TEXT.__objc_stubs: 0x400
   __TEXT.__objc_methlist: 0x2c
-  __TEXT.__gcc_except_tab: 0x260
-  __TEXT.__cstring: 0x15c
-  __TEXT.__oslogstring: 0xf4
+  __TEXT.__gcc_except_tab: 0x2a0
+  __TEXT.__cstring: 0x1a2
+  __TEXT.__oslogstring: 0xf1
   __TEXT.__objc_classname: 0x1f
   __TEXT.__objc_methname: 0x325
   __TEXT.__objc_methtype: 0x21
   __TEXT.__unwind_info: 0xc8
-  __DATA_CONST.__auth_got: 0x130
+  __DATA_CONST.__auth_got: 0x138
   __DATA_CONST.__got: 0x88
   __DATA_CONST.__const: 0x40
-  __DATA_CONST.__cfstring: 0x180
+  __DATA_CONST.__cfstring: 0x1c0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0x90

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9B0018EC-6FC4-39FA-ACD6-8FA4ECD4DA5E
+  UUID: B97985A7-C91E-30E7-8BB7-D8BF53BD69CC
   Functions: 10
-  Symbols:   67
-  CStrings:  70
+  Symbols:   68
+  CStrings:  74
 
Symbols:
+ __ZnwmSt19__type_descriptor_t
+ _objc_release_x25
+ _objc_release_x28
+ _objc_retain
- __Znwm
- _objc_release_x24
- _objc_release_x27
Functions:
~ sub_100000edc : 2400 -> 2804
~ sub_10000183c -> sub_1000019d0 : 160 -> 184
~ sub_1000018dc -> sub_100001a88 : 156 -> 160
~ sub_100001978 -> sub_100001b28 : 172 -> 156
CStrings:
+ ".*\\.bin$"
+ "/Library/Logs/CrashReporter/CoreCapture/MultiFunctionManager"
+ "UnlimitedHCIFileSize is not enabled or maxFileSize is less than 200MB. Returning only fwlogs if there are any. Exiting."
- "ERROR: Extension launch failed. Use extension only when UnlimitedHCIFileSize is enabled or maxFileSize is less than 200MB."

```
