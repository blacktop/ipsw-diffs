## AutomaticAssessmentConfiguration

> `/System/Library/Frameworks/AutomaticAssessmentConfiguration.framework/AutomaticAssessmentConfiguration`

```diff

-  __TEXT.__text: 0x78b4
-  __TEXT.__objc_methlist: 0x854
+  __TEXT.__text: 0x7a7c
+  __TEXT.__objc_methlist: 0x87c
   __TEXT.__const: 0x3ae
-  __TEXT.__cstring: 0x346
+  __TEXT.__cstring: 0x34f
   __TEXT.__swift5_typeref: 0x12b
   __TEXT.__constg_swiftt: 0x64
   __TEXT.__swift5_reflstr: 0x22

   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6b0
+  __DATA_CONST.__objc_selrefs: 0x6e0
   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__got: 0x120
   __AUTH_CONST.__const: 0x68
-  __AUTH_CONST.__cfstring: 0x1c0
-  __AUTH_CONST.__objc_const: 0xfe0
+  __AUTH_CONST.__cfstring: 0x1e0
+  __AUTH_CONST.__objc_const: 0x1010
   __AUTH_CONST.__auth_got: 0x338
   __AUTH.__objc_data: 0x190
-  __DATA.__objc_ivar: 0x100
+  __DATA.__objc_ivar: 0x104
   __DATA.__data: 0x180
   __DATA.__bss: 0x490
   - /System/Library/Frameworks/AutomaticAssessmentConfiguration.framework/Frameworks/AACClient.framework/AACClient

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  Functions: 252
-  Symbols:   814
-  CStrings:  31
+  Functions: 256
+  Symbols:   828
+  CStrings:  32
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_fieldmd : content changed
~ __TEXT.__swift5_assocty : content changed
~ __TEXT.__swift5_builtin : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__unwind_info : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__got : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH.__objc_data : content changed
~ __DATA.__data : content changed
Symbols:
+ -[AEAssessmentApplication initWithBundleIdentifier:teamIdentifier:requiresSignatureValidation:pid:]
+ -[AEAssessmentApplication initWithPID:]
+ -[AEAssessmentApplication initWithPID:teamIdentifier:]
+ -[AEAssessmentApplication pid]
+ _OBJC_IVAR_$_AEAssessmentApplication._pid
+ _objc_msgSend$initWithPID:teamIdentifier:
+ _objc_msgSend$initWithPID:teamIdentifier:requiresSignatureValidation:
+ _objc_msgSend$intValue
+ _objc_msgSend$numberWithInt:
+ _objc_msgSend$pid
- -[AEAssessmentApplication initWithBundleIdentifier:teamIdentifier:requiresSignatureValidation:]
CStrings:
+ ""
+ "<%@: %p { bundleIdentifier = %@, teamIdentifier = %@, requiresSignatureChecks = %@, pid = %@ }>"
- "<%@: %p { bundleIdentifier = %@, teamIdentifier = %@, requiresSignatureChecks = %@ }>"

```
