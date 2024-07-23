## BTAvrcp

> `/usr/sbin/BTAvrcp`

```diff

-340.41.0.0.0
-  __TEXT.__text: 0xdb88
-  __TEXT.__auth_stubs: 0x800
-  __TEXT.__objc_stubs: 0x2500
-  __TEXT.__objc_methlist: 0x1154
-  __TEXT.__const: 0x40
-  __TEXT.__objc_methname: 0x2247
-  __TEXT.__cstring: 0x760
-  __TEXT.__objc_classname: 0x26a
-  __TEXT.__objc_methtype: 0x453
-  __TEXT.__oslogstring: 0x2c0
+340.43.0.0.0
+  __TEXT.__text: 0xde4c
+  __TEXT.__auth_stubs: 0x810
+  __TEXT.__objc_stubs: 0x2560
+  __TEXT.__objc_methlist: 0x1174
+  __TEXT.__const: 0x50
+  __TEXT.__objc_methname: 0x232e
+  __TEXT.__cstring: 0x797
+  __TEXT.__objc_classname: 0x278
+  __TEXT.__objc_methtype: 0x464
+  __TEXT.__oslogstring: 0x31c
   __TEXT.__gcc_except_tab: 0x40
   __TEXT.__info_plist: 0x446
-  __TEXT.__unwind_info: 0x4d0
-  __DATA_CONST.__auth_got: 0x410
-  __DATA_CONST.__got: 0x338
-  __DATA_CONST.__const: 0x5c8
-  __DATA_CONST.__cfstring: 0xb80
-  __DATA_CONST.__objc_classlist: 0xc8
+  __TEXT.__unwind_info: 0x4d8
+  __DATA_CONST.__auth_got: 0x418
+  __DATA_CONST.__got: 0x360
+  __DATA_CONST.__const: 0x608
+  __DATA_CONST.__cfstring: 0xbe0
+  __DATA_CONST.__objc_classlist: 0xd0
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_intobj: 0xc0
   __DATA_CONST.__objc_arraydata: 0x38
   __DATA_CONST.__objc_arrayobj: 0x60
-  __DATA.__objc_const: 0x1c48
-  __DATA.__objc_selrefs: 0xa80
+  __DATA.__objc_const: 0x1cd8
+  __DATA.__objc_selrefs: 0xaa8
   __DATA.__objc_ivar: 0xa8
-  __DATA.__objc_data: 0x7d0
+  __DATA.__objc_data: 0x820
   __DATA.__data: 0x140
   __DATA.__bss: 0x38
   __DATA.__common: 0x8

   - /System/Library/Frameworks/MobileCoreServices.framework/MobileCoreServices
   - /System/Library/PrivateFrameworks/CrashReporterSupport.framework/CrashReporterSupport
   - /System/Library/PrivateFrameworks/MediaRemote.framework/MediaRemote
+  - /System/Library/PrivateFrameworks/SymptomDiagnosticReporter.framework/SymptomDiagnosticReporter
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 431
-  Symbols:   241
-  CStrings:  699
+  Functions: 434
+  Symbols:   247
+  CStrings:  712
 
Symbols:
+ _OBJC_CLASS_$_SDRDiagnosticReporter
+ _kSymptomDiagnosticReplyReason
+ _kSymptomDiagnosticReplyReasonString
+ _kSymptomDiagnosticReplySessionID
+ _kSymptomDiagnosticReplySuccess
+ _os_variant_has_internal_diagnostics
CStrings:
+ "ABC Snapshot failed with code %!l(MISSING)ld and reason: %!s(MISSING)"
+ "ABC Snapshot successful with SessionID %!s(MISSING)"
+ "BTDiagnostics"
+ "Bluetooth"
+ "Networking"
+ "OI_IsInternalDiagnosticsEnabled"
+ "bluetoothd"
+ "fileABCSnapshot:subTypeContext:duration:"
+ "intValue"
+ "signatureWithDomain:type:subType:subtypeContext:detectedProcess:triggerThresholdValues:"
+ "snapshotWithSignature:duration:events:payload:actions:reply:"
+ "v16@?0@\"NSDictionary\"8"
+ "v40@0:8@16@24d32"

```
