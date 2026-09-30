## ContinuousRecordingsDiagnosticExtension

> `/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/ContinuousRecordingsDiagnosticExtension.appex/ContinuousRecordingsDiagnosticExtension`

```diff

-9130.2.0.0.0
-  __TEXT.__text: 0x7c4
-  __TEXT.__auth_stubs: 0x230
+9140.1.0.0.0
+  __TEXT.__text: 0x820
+  __TEXT.__auth_stubs: 0x220
   __TEXT.__objc_stubs: 0x280
   __TEXT.__objc_methlist: 0x44
   __TEXT.__const: 0x70

   __TEXT.__objc_classname: 0x28
   __TEXT.__objc_methname: 0x250
   __TEXT.__objc_methtype: 0x1b
-  __TEXT.__unwind_info: 0x70
-  __DATA_CONST.__auth_got: 0x120
+  __TEXT.__unwind_info: 0x78
+  __DATA_CONST.__auth_got: 0x118
   __DATA_CONST.__got: 0x50
   __DATA_CONST.__const: 0x68
   __DATA_CONST.__cfstring: 0xc0

   - /System/Library/PrivateFrameworks/DiagnosticExtensions.framework/DiagnosticExtensions
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6F097C5C-481E-368D-9BBB-E4E8E81E2B04
+  UUID: 02A0E317-93C1-3912-BC6A-6A7017361D70
   Functions: 9
-  Symbols:   96
+  Symbols:   95
   CStrings:  49
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
+ _objc_retain_x23
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x2
- _objc_retain_x8
Functions:
~ +[ContinuousRecordingsDiagnosticExtension log] : 68 -> 84
~ -[ContinuousRecordingsDiagnosticExtension attachmentsForParameters:] : 908 -> 952
~ -[ContinuousRecordingsDiagnosticExtension directoryRegexForComponentID:] : 264 -> 292
~ -[ContinuousRecordingsDiagnosticExtension forceFlushHIDContinuousRecorder] : 456 -> 460

```
