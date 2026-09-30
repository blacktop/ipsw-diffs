## ContinuitySing

> `/System/Library/PrivateFrameworks/ContinuitySing.framework/ContinuitySing`

```diff

-664.40.15.122.3
-  __TEXT.__text: 0x58e44
-  __TEXT.__auth_stubs: 0x1820
-  __TEXT.__objc_methlist: 0x34cc
-  __TEXT.__const: 0xc34
+664.40.18.0.0
+  __TEXT.__text: 0x59438
+  __TEXT.__auth_stubs: 0x1830
+  __TEXT.__objc_methlist: 0x34d4
+  __TEXT.__const: 0xbc4
   __TEXT.__gcc_except_tab: 0xb28
-  __TEXT.__cstring: 0x5f29
-  __TEXT.__oslogstring: 0x2e89
+  __TEXT.__cstring: 0x60f9
+  __TEXT.__oslogstring: 0x2eb9
   __TEXT.__ustring: 0x2a
   __TEXT.__swift5_typeref: 0x95c
   __TEXT.__swift5_fieldmd: 0x340

   __TEXT.__swift_as_ret: 0x94
   __TEXT.__swift5_assocty: 0x78
   __TEXT.__swift5_builtin: 0x28
-  __TEXT.__unwind_info: 0x1788
+  __TEXT.__unwind_info: 0x17a0
   __TEXT.__eh_frame: 0xee8
   __TEXT.__objc_classname: 0x842
-  __TEXT.__objc_methname: 0x9af0
-  __TEXT.__objc_methtype: 0x1457
-  __TEXT.__objc_stubs: 0x7ae0
+  __TEXT.__objc_methname: 0x9b22
+  __TEXT.__objc_methtype: 0x144c
+  __TEXT.__objc_stubs: 0x7b20
   __DATA_CONST.__got: 0x980
-  __DATA_CONST.__const: 0x14a0
+  __DATA_CONST.__const: 0x14b0
   __DATA_CONST.__objc_classlist: 0x2c8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2938
+  __DATA_CONST.__objc_selrefs: 0x2940
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x270
   __DATA_CONST.__objc_arraydata: 0x20
-  __AUTH_CONST.__auth_got: 0xc20
+  __AUTH_CONST.__auth_got: 0xc28
   __AUTH_CONST.__const: 0x1320
-  __AUTH_CONST.__cfstring: 0x2880
+  __AUTH_CONST.__cfstring: 0x2980
   __AUTH_CONST.__objc_const: 0x70e8
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__objc_arrayobj: 0x18

   - /System/Library/Frameworks/TipKit.framework/TipKit
   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/Frameworks/_GroupActivities_UIKit.framework/_GroupActivities_UIKit
+  - /System/Library/PrivateFrameworks/CMCapture.framework/CMCapture
   - /System/Library/PrivateFrameworks/CMContinuityCaptureCore.framework/CMContinuityCaptureCore
   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
   - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: BB81336A-7D34-380E-B572-D940A7738B00
-  Functions: 1817
-  Symbols:   5451
-  CStrings:  3295
+  UUID: 818C3D62-5C51-3639-90EE-441CD55A693D
+  Functions: 1823
+  Symbols:   5464
+  CStrings:  3315
 
Symbols:
+ -[CSShieldViewController _presentContinuityCameraDisabledError]
+ _FigContinuityCaptureGetUserPreferenceDisabled
+ ___53-[CSShieldConnectionManager _requestGroupSessionURL:]_block_invoke.52
+ ___57-[CSShieldConnectionManager _bootstrapFromSingQRCodeURL:]_block_invoke.38
+ ___63-[CSShieldViewController _presentContinuityCameraDisabledError]_block_invoke
+ ___63-[CSShieldViewController _presentContinuityCameraDisabledError]_block_invoke.327
+ ___63-[CSShieldViewController _presentContinuityCameraDisabledError]_block_invoke.327.cold.1
+ ___63-[CSShieldViewController _presentContinuityCameraDisabledError]_block_invoke.334
+ ___63-[CSShieldViewController _presentContinuityCameraDisabledError]_block_invoke.335
+ ___block_literal_global.347
+ _objc_msgSend$_presentContinuityCameraDisabledError
+ _objc_msgSend$openSensitiveURL:withOptions:error:
- -[CSShieldConnectionManager _subsystemForErrorCode:]
- ___53-[CSShieldConnectionManager _requestGroupSessionURL:]_block_invoke.49
- ___57-[CSShieldConnectionManager _bootstrapFromSingQRCodeURL:]_block_invoke.35
- ___block_literal_global.329
CStrings:
+ "%s: %@ %s open settings"
+ "%s: error launching preferences: %@"
+ "-[CSShieldViewController _presentContinuityCameraDisabledError]"
+ "-[CSShieldViewController _presentContinuityCameraDisabledError]_block_invoke"
+ "CONTINUITY_CAMERA_DISABLED_ALERT_CANCEL_BUTTON"
+ "CONTINUITY_CAMERA_DISABLED_ALERT_MESSAGE"
+ "CONTINUITY_CAMERA_DISABLED_ALERT_OPEN_SETTINGS_BUTTON"
+ "CONTINUITY_CAMERA_DISABLED_ALERT_TITLE"
+ "Continuity Camera disabled"
+ "Continuity Camera is disabled"
+ "ContinuitySingErrorCodeContinuityCameraDisabled"
+ "_presentContinuityCameraDisabledError"
+ "openSensitiveURL:withOptions:error:"
+ "prefs:root=General&path=CONTINUITY_SPEC"
- "_subsystemForErrorCode:"
- "q24@0:8q16"

```
