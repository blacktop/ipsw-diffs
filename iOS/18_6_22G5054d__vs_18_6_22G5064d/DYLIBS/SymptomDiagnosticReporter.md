## SymptomDiagnosticReporter

> `/System/Library/PrivateFrameworks/SymptomDiagnosticReporter.framework/SymptomDiagnosticReporter`

```diff

-383.120.2.0.0
-  __TEXT.__text: 0x84d4
+383.140.2.0.0
+  __TEXT.__text: 0x8700
   __TEXT.__auth_stubs: 0x470
   __TEXT.__objc_methlist: 0x56c
   __TEXT.__const: 0xac
-  __TEXT.__gcc_except_tab: 0x88
+  __TEXT.__gcc_except_tab: 0xbc
   __TEXT.__cstring: 0x1370
-  __TEXT.__oslogstring: 0xf2d
-  __TEXT.__unwind_info: 0x290
+  __TEXT.__oslogstring: 0xf79
+  __TEXT.__unwind_info: 0x2a0
   __TEXT.__objc_classname: 0x57
   __TEXT.__objc_methname: 0x1327
   __TEXT.__objc_methtype: 0x6b0
   __TEXT.__objc_stubs: 0xae0
   __DATA_CONST.__got: 0xa0
-  __DATA_CONST.__const: 0xa10
+  __DATA_CONST.__const: 0xa38
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8

   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3F724D0A-9A8B-3351-A274-58D04285DB38
-  Functions: 188
-  Symbols:   816
-  CStrings:  835
+  UUID: E55F9928-A859-3D24-BCDC-F8B8C1E435FF
+  Functions: 191
+  Symbols:   824
+  CStrings:  836
 
Symbols:
+ -[SDRDiagnosticReporter _replyOnQueueToBlock:withConfig:]
+ -[SDRDiagnosticReporter getAutoBugCaptureConfiguration:].cold.2
+ GCC_except_table133
+ ___57-[SDRDiagnosticReporter _replyOnQueueToBlock:withConfig:]_block_invoke
+ ___block_descriptor_48_e8_32bs40w_e17_v16?0"NSError"8lw40l8s32l8
+ ___block_descriptor_48_e8_32bs40w_e22_v16?0"NSDictionary"8lw40l8s32l8
- ___block_descriptor_40_e8_32bs_e22_v16?0"NSDictionary"8ls32l8
CStrings:
+ "SDRDiagnosticReporter: (getAutoBugCaptureConfiguration:) ABC is not enabled"

```
