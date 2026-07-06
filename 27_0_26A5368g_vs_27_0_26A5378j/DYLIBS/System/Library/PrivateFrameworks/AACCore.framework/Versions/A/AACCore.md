## AACCore

> `/System/Library/PrivateFrameworks/AACCore.framework/Versions/A/AACCore`

```diff

-  __TEXT.__text: 0x1367c
-  __TEXT.__objc_methlist: 0x1a24
+  __TEXT.__text: 0x138a8
+  __TEXT.__objc_methlist: 0x1a3c
   __TEXT.__const: 0xe0
-  __TEXT.__cstring: 0x19fa
+  __TEXT.__cstring: 0x1a4e
   __TEXT.__oslogstring: 0x5c3
   __TEXT.__gcc_except_tab: 0x124
   __TEXT.__unwind_info: 0x598

   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0xd0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xca0
+  __DATA_CONST.__objc_selrefs: 0xcb8
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x120
   __DATA_CONST.__got: 0x1d8
   __AUTH_CONST.__const: 0x600
-  __AUTH_CONST.__cfstring: 0x15c0
-  __AUTH_CONST.__objc_const: 0x4698
+  __AUTH_CONST.__cfstring: 0x1620
+  __AUTH_CONST.__objc_const: 0x46c8
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0xa50
-  __DATA.__objc_ivar: 0x284
-  __DATA.__data: 0x9f0
+  __DATA.__objc_ivar: 0x288
+  __DATA.__data: 0x9f8
   __DATA.__bss: 0x10
   __DATA_DIRTY.__objc_data: 0x6e0
   __DATA_DIRTY.__bss: 0x10

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 637
-  Symbols:   1837
-  CStrings:  392
+  Functions: 639
+  Symbols:   1843
+  CStrings:  398
 
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
+ OBJC_IVAR_$_AEAssessmentApplicationDescriptor._pid
+ _AECoreNotAliveParticipantPIDsKey
+ _objc_msgSend$numberWithInt:
+ _objc_msgSend$pid
CStrings:
+ "<%@: %p { bundleIdentifier = %@, teamIdentifier = %@, requiresSignatureValidation = %@, pid = %@ }>"
+ "AENotAliveParticipantPIDs"
+ "One or more participant PIDs are not alive."
+ "pid"
- "<%@: %p { bundleIdentifier = %@, teamIdentifier = %@, requiresSignatureValidation = %@ }>"

```
