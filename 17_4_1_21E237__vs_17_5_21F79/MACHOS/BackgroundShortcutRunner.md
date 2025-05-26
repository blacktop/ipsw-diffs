## BackgroundShortcutRunner

> `/System/Library/PrivateFrameworks/WorkflowKit.framework/XPCServices/BackgroundShortcutRunner.xpc/BackgroundShortcutRunner`

```diff

-2510.5.1.0.0
-  __TEXT.__text: 0x144ec
+2605.0.5.0.0
+  __TEXT.__text: 0x148b0
   __TEXT.__auth_stubs: 0x980
-  __TEXT.__objc_stubs: 0x40a0
-  __TEXT.__objc_methlist: 0xa2c
+  __TEXT.__objc_stubs: 0x4160
+  __TEXT.__objc_methlist: 0xa54
   __TEXT.__const: 0x170
-  __TEXT.__objc_methname: 0x4d71
+  __TEXT.__objc_methname: 0x4e99
   __TEXT.__swift5_typeref: 0x11d
-  __TEXT.__cstring: 0x2a1a
+  __TEXT.__cstring: 0x2a91
   __TEXT.__swift5_fieldmd: 0xac
   __TEXT.__constg_swiftt: 0x120
   __TEXT.__swift5_reflstr: 0x86
   __TEXT.__swift5_assocty: 0x18
   __TEXT.__swift5_proto: 0x10
   __TEXT.__swift5_types: 0xc
-  __TEXT.__objc_classname: 0x254
-  __TEXT.__objc_methtype: 0x15eb
+  __TEXT.__objc_classname: 0x274
+  __TEXT.__objc_methtype: 0x162a
   __TEXT.__gcc_except_tab: 0x170
-  __TEXT.__oslogstring: 0x1640
+  __TEXT.__oslogstring: 0x16f6
   __TEXT.__ustring: 0x6a
-  __TEXT.__unwind_info: 0x460
+  __TEXT.__unwind_info: 0x470
   __DATA_CONST.__auth_got: 0x4d0
-  __DATA_CONST.__got: 0x150
+  __DATA_CONST.__got: 0x158
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0xe40
-  __DATA_CONST.__cfstring: 0xaa0
+  __DATA_CONST.__cfstring: 0xac0
   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_catlist: 0x0
-  __DATA_CONST.__objc_protolist: 0x98
+  __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x28
-  __DATA_CONST.__objc_classrefs: 0x3a8
+  __DATA_CONST.__objc_classrefs: 0x3b0
   __DATA_CONST.__objc_superrefs: 0x30
-  __DATA.__objc_const: 0x1f00
-  __DATA.__objc_selrefs: 0x1258
-  __DATA.__objc_ivar: 0x80
+  __DATA.__objc_const: 0x1f60
+  __DATA.__objc_selrefs: 0x1290
+  __DATA.__objc_ivar: 0x84
   __DATA.__objc_data: 0x460
-  __DATA.__data: 0x660
+  __DATA.__data: 0x6c0
   __DATA.__bss: 0x220
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreData.framework/CoreData

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 371
-  Symbols:   317
-  CStrings:  1184
+  Functions: 374
+  Symbols:   319
+  CStrings:  1201
 
Symbols:
+ _NSPOSIXErrorDomain
+ _OBJC_CLASS_$_WFAssessmentModeManager
CStrings:
+ "\x01\x12\x1f\x01"
+ "%s Assessment Mode became active stopping workflow execution."
+ "%s Device is NOT in assessmentMode observing for changes."
+ "%s Device is in assessmentMode cancelling shortcut execution."
+ "-[WFBackgroundShortcutRunner assessmentModeManagerDidBecomeActive:]"
+ "@\"WFAssessmentModeManager\""
+ "A shortcut cannot be run while in Assessment Mode."
+ "T@\"WFAssessmentModeManager\",R,N,V_assessmentModeManager"
+ "WFAssessmentModeManagerDelegate"
+ "_assessmentModeManager"
+ "assessmentModeActiveError"
+ "assessmentModeManager"
+ "assessmentModeManagerDidBecomeActive:"
+ "initWithQueue:delegate:"
+ "isAssessmentModeSupportedOnCurrentDevice"
+ "isInAssessmentMode"
+ "startObservingForAssesmentModeChangesIfNeeded"
+ "v24@0:8@\"WFAssessmentModeManager\"16"
- "\x01\x11\x1f\x01"

```
