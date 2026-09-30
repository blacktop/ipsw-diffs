## AACCore

> `/System/Library/PrivateFrameworks/AACCore.framework/AACCore`

```diff

-  __TEXT.__text: 0x11d1c
-  __TEXT.__objc_methlist: 0x1a64
+  __TEXT.__text: 0x11f20
+  __TEXT.__objc_methlist: 0x1a7c
   __TEXT.__const: 0xd8
-  __TEXT.__cstring: 0x19d5
+  __TEXT.__cstring: 0x1a29
   __TEXT.__oslogstring: 0x5c3
   __TEXT.__gcc_except_tab: 0x120
   __TEXT.__unwind_info: 0x598

   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0xd8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc98
+  __DATA_CONST.__objc_selrefs: 0xcb0
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x120
   __DATA_CONST.__got: 0x1e0
   __AUTH_CONST.__const: 0x60
-  __AUTH_CONST.__cfstring: 0x15e0
-  __AUTH_CONST.__objc_const: 0x4780
+  __AUTH_CONST.__cfstring: 0x1640
+  __AUTH_CONST.__objc_const: 0x47b0
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0xe10
-  __DATA.__objc_ivar: 0x284
-  __DATA.__data: 0xa50
+  __DATA.__objc_ivar: 0x288
+  __DATA.__data: 0xa58
   __DATA.__bss: 0x20
   __DATA_DIRTY.__objc_data: 0x370
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 609
-  Symbols:   2462
-  CStrings:  394
+  Functions: 611
+  Symbols:   2470
+  CStrings:  400
 
Sections:
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__got : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH.__objc_data : content changed
~ __DATA_DIRTY.__objc_data : content changed
Symbols:
+ -[AEAssessmentApplicationDescriptor initWithPID:teamIdentifier:requiresSignatureValidation:]
+ -[AEAssessmentApplicationDescriptor pid]
+ _AECoreNotAliveParticipantPIDsKey
+ _OBJC_IVAR_$_AEAssessmentApplicationDescriptor._pid
+ _objc_msgSend$numberWithInt:
+ _objc_msgSend$pid
CStrings:
+ "<%@: %p { bundleIdentifier = %@, teamIdentifier = %@, requiresSignatureValidation = %@, pid = %@ }>"
+ "AENotAliveParticipantPIDs"
+ "One or more participant PIDs are not alive."
+ "pid"
- "<%@: %p { bundleIdentifier = %@, teamIdentifier = %@, requiresSignatureValidation = %@ }>"

```
