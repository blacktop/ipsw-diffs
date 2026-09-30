## aned

> `/usr/libexec/aned`

```diff

-370.31.1.0.0
-  __TEXT.__text: 0x1c310
-  __TEXT.__auth_stubs: 0x800
-  __TEXT.__objc_stubs: 0x2860
-  __TEXT.__objc_methlist: 0xb10
+370.55.0.0.0
+  __TEXT.__text: 0x1bdb4
+  __TEXT.__auth_stubs: 0x7d0
+  __TEXT.__objc_stubs: 0x2800
+  __TEXT.__objc_methlist: 0xcac
   __TEXT.__const: 0x110
-  __TEXT.__oslogstring: 0x296c
-  __TEXT.__cstring: 0xd6c
-  __TEXT.__objc_methname: 0x3067
-  __TEXT.__objc_classname: 0x1b1
-  __TEXT.__objc_methtype: 0xbde
-  __TEXT.__gcc_except_tab: 0x2d58
+  __TEXT.__gcc_except_tab: 0x2dcc
+  __TEXT.__cstring: 0xd44
+  __TEXT.__oslogstring: 0x28be
+  __TEXT.__objc_classname: 0x1a0
+  __TEXT.__objc_methname: 0x2eb9
+  __TEXT.__objc_methtype: 0xb97
   __TEXT.__unwind_info: 0x5c0
-  __DATA_CONST.__auth_got: 0x418
+  __DATA_CONST.__auth_got: 0x400
   __DATA_CONST.__got: 0x190
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x488
-  __DATA_CONST.__cfstring: 0xce0
-  __DATA_CONST.__objc_classlist: 0x60
+  __DATA_CONST.__const: 0x4b0
+  __DATA_CONST.__cfstring: 0xcc0
+  __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x48
+  __DATA_CONST.__objc_superrefs: 0x40
   __DATA_CONST.__objc_intobj: 0x30
-  __DATA.__objc_const: 0x1690
-  __DATA.__objc_selrefs: 0xbc8
-  __DATA.__objc_ivar: 0xb4
-  __DATA.__objc_data: 0x3c0
+  __DATA.__objc_const: 0x1120
+  __DATA.__objc_selrefs: 0xc38
+  __DATA.__objc_ivar: 0xa4
+  __DATA.__objc_data: 0x370
   __DATA.__data: 0x4f0
   __DATA.__bss: 0x68
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 403
-  Symbols:   190
-  CStrings:  982
+  Functions: 384
+  Symbols:   187
+  CStrings:  958
 
Symbols:
+ _OBJC_CLASS_$__ANEModelToken
+ _fcntl
- _CFRelease
- _SecTaskCopySigningIdentifier
- _SecTaskCopyTeamIdentifier
- _SecTaskCreateWithAuditToken
- _kCFAllocatorDefault
CStrings:
+ "%@: fcntl(F_RDADVISE). errno=%d : %s"
+ "@24@0:8^{ANEProgramInstanceStruct=^v^vQQC^[512c]^Q^{ANEProgramIOInfoStruct}^{ANEProgramIOInfoStruct}C^[512c]^QC^{ANEProgramProcedureStruct}QIQQcQQiC}16"
+ "T^{ANEProgramInstanceStruct=^v^vQQC^[512c]^Q^{ANEProgramIOInfoStruct}^{ANEProgramIOInfoStruct}C^[512c]^QC^{ANEProgramProcedureStruct}QIQQcQQiC},N,V_programInstance"
+ "^{ANEProgramInstanceStruct=^v^vQQC^[512c]^Q^{ANEProgramIOInfoStruct}^{ANEProgramIOInfoStruct}C^[512c]^QC^{ANEProgramProcedureStruct}QIQQcQQiC}"
+ "^{ANEProgramInstanceStruct=^v^vQQC^[512c]^Q^{ANEProgramIOInfoStruct}^{ANEProgramIOInfoStruct}C^[512c]^QC^{ANEProgramProcedureStruct}QIQQcQQiC}16@0:8"
+ "v24@0:8^{ANEProgramInstanceStruct=^v^vQQC^[512c]^Q^{ANEProgramIOInfoStruct}^{ANEProgramIOInfoStruct}C^[512c]^QC^{ANEProgramProcedureStruct}QIQQcQQiC}16"
- "\x13"
- "%@: SecTaskCopySigningIdentifier() returned csIdentity=\"%@\""
- "%@: SecTaskCopyTeamIdentifier() returned teamIdentity=\"%@\""
- "%@: client(%d) : SecTaskCreateWithAuditToken() failed"
- "%@: client(%d) : missing teamIdentity"
- "%@: { csIdentity=%@ : teamIdentity=%@ }"
- "@24@0:8^{ANEProgramInstanceStruct=^v^vQQC^[512c]^Q^{ANEProgramIOInfoStruct}^{ANEProgramIOInfoStruct}C^[512c]^QC^{ANEProgramProcedureStruct}QIQQcQQi}16"
- "@44@0:8@16@24@32i40"
- "@52@0:8{?=[8I]}16i48"
- "@60@0:8{?=[8I]}16@48i56"
- "T@\"NSString\",R,N,V_csIdentity"
- "T@\"NSString\",R,N,V_modelIdentifier"
- "T@\"NSString\",R,N,V_teamIdentity"
- "T^{ANEProgramInstanceStruct=^v^vQQC^[512c]^Q^{ANEProgramIOInfoStruct}^{ANEProgramIOInfoStruct}C^[512c]^QC^{ANEProgramProcedureStruct}QIQQcQQi},N,V_programInstance"
- "Ti,R,N,V_processIdentifier"
- "^{ANEProgramInstanceStruct=^v^vQQC^[512c]^Q^{ANEProgramIOInfoStruct}^{ANEProgramIOInfoStruct}C^[512c]^QC^{ANEProgramProcedureStruct}QIQQcQQi}"
- "^{ANEProgramInstanceStruct=^v^vQQC^[512c]^Q^{ANEProgramIOInfoStruct}^{ANEProgramIOInfoStruct}C^[512c]^QC^{ANEProgramProcedureStruct}QIQQcQQi}16@0:8"
- "_ANEModelToken"
- "_csIdentity"
- "_modelIdentifier"
- "_processIdentifier"
- "_teamIdentity"
- "i16@0:8"
- "initWithAuditToken:modelIdentifier:processIdentifier:"
- "initWithCsIdentity:teamIdentity:modelIdentifier:processIdentifier:"
- "processNameFor:identifier:"
- "teamIDFor:processIdentifier:"
- "tokenWithCsIdentity:teamIdentity:modelIdentifier:processIdentifier:"
- "v24@0:8^{ANEProgramInstanceStruct=^v^vQQC^[512c]^Q^{ANEProgramIOInfoStruct}^{ANEProgramIOInfoStruct}C^[512c]^QC^{ANEProgramProcedureStruct}QIQQcQQi}16"

```
