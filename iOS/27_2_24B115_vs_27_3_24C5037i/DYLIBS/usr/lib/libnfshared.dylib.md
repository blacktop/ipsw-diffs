## libnfshared.dylib

> `/usr/lib/libnfshared.dylib`

```diff

-371.8.0.0.0
-  __TEXT.__text: 0x25098
+372.4.1.0.0
+  __TEXT.__text: 0x2664c
   __TEXT.__delay_stubs: 0x40
-  __TEXT.__delay_helper: 0xdc
-  __TEXT.__objc_methlist: 0x23ac
+  __TEXT.__delay_helper: 0x2d0
+  __TEXT.__objc_methlist: 0x23c4
   __TEXT.__const: 0x2c8
-  __TEXT.__cstring: 0x4dde
-  __TEXT.__oslogstring: 0x18dc
-  __TEXT.__unwind_info: 0x9c0
+  __TEXT.__cstring: 0x5243
+  __TEXT.__oslogstring: 0x1ac3
+  __TEXT.__unwind_info: 0x9e0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x610
-  __DATA_CONST.__objc_classlist: 0x128
+  __DATA_CONST.__const: 0x688
+  __DATA_CONST.__objc_classlist: 0x130
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1430
+  __DATA_CONST.__objc_selrefs: 0x1468
   __DATA_CONST.__objc_superrefs: 0xe0
   __DATA_CONST.__objc_arraydata: 0x660
-  __DATA_CONST.__got: 0x1d0
+  __DATA_CONST.__got: 0x200
   __AUTH_CONST.__const: 0x248
-  __AUTH_CONST.__cfstring: 0x48e0
-  __AUTH_CONST.__objc_const: 0x4258
+  __AUTH_CONST.__cfstring: 0x4a00
+  __AUTH_CONST.__objc_const: 0x42e8
   __AUTH_CONST.__objc_intobj: 0x498
   __AUTH_CONST.__objc_dictobj: 0x1b8
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__auth_got: 0x600
+  __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0x2c4
-  __DATA.__data: 0x3d0
+  __DATA.__data: 0x3d4
   __DATA.__common: 0x88
   __DATA_DIRTY.__objc_ivar: 0x10
   __DATA_DIRTY.__objc_data: 0xb90

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
+  - /System/Library/PrivateFrameworks/SymptomDiagnosticReporter.framework/SymptomDiagnosticReporter
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 777
-  Symbols:   423
-  CStrings:  961
+  Functions: 785
+  Symbols:   432
+  CStrings:  994
 
Symbols:
+ _NFProductSupportsBackgroundTagRead
+ _OBJC_CLASS_$_NFAutoBugCapture
+ _OBJC_CLASS_$_SDRDiagnosticReporter
+ _OBJC_METACLASS_$_NFAutoBugCapture
+ _kSymptomDiagnosticKeyPayloadPath
+ _kSymptomDiagnosticReplyRateLimitExpiresIn
+ _kSymptomDiagnosticReplyReason
+ _kSymptomDiagnosticReplyReasonString
+ _kSymptomDiagnosticReplySuccess
CStrings:
+ "%s:%i ABC Request submitted successfully"
+ "%s:%i ABC Request was rejected. Reason Code: %ld"
+ "%s:%i ABC is prohibited until %{public}@"
+ "%s:%i Ignoring ABC callback with no error subtype context."
+ "%s:%i Ignoring ABC callback with no error subtype."
+ "%s:%i Ignoring ABC callback with no error type."
+ "%s:%i Maximum TLV nesting (%u) reached"
+ "%s:%i Requesting Auto Bug Capture!"
+ "%s:%i Unexpected data found; removing invalid entry"
+ "%{public}s:%i ABC Request submitted successfully"
+ "%{public}s:%i ABC Request was rejected. Reason Code: %ld"
+ "%{public}s:%i ABC is prohibited until %{public}@"
+ "%{public}s:%i Ignoring ABC callback with no error subtype context."
+ "%{public}s:%i Ignoring ABC callback with no error subtype."
+ "%{public}s:%i Ignoring ABC callback with no error type."
+ "%{public}s:%i Maximum TLV nesting (%u) reached"
+ "%{public}s:%i Requesting Auto Bug Capture!"
+ "%{public}s:%i Unexpected data found; removing invalid entry"
+ "+[NFAutoBugCapture requestSnapshotWithType:subType:subTypeContext:detectedProcess:attachments:preferencesDomain:queue:completion:]"
+ "+[NFAutoBugCapture requestSnapshotWithType:subType:subTypeContext:detectedProcess:attachments:preferencesDomain:queue:completion:]_block_invoke"
+ "+[NFAutoBugCapture requestSnapshotWithType:subType:subTypeContext:detectedProcess:attachments:preferencesDomain:queue:completion:]_block_invoke_3"
+ "+[NFTLV _parseTLVs:end:simple:definite:depth:]"
+ "/System/Library/PrivateFrameworks/SymptomDiagnosticReporter.framework/SymptomDiagnosticReporter"
+ "Invalid subType"
+ "Invalid subTypeContext"
+ "Invalid type"
+ "NFABCProhibitRequestsUntil"
+ "NFAutoBugCaptureCheckRateLimit"
+ "NFC/SE"
+ "T:%@_S:%@"
+ "Time limited"
+ "Unknown reason"
+ "nfcd.abc"
+ "v16@?0@\"NSDictionary\"8"
- "+[NFTLV _parseTLVs:end:simple:definite:]"
```
