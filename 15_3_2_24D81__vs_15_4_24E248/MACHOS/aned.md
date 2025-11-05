## aned

> `/usr/libexec/aned`

```diff

-370.31.1.0.0
-  __TEXT.__text: 0x1fe18
-  __TEXT.__auth_stubs: 0x6a0
-  __TEXT.__objc_stubs: 0x2840
-  __TEXT.__objc_methlist: 0xb10
+370.56.0.0.0
+  __TEXT.__text: 0x1f480
+  __TEXT.__auth_stubs: 0x650
+  __TEXT.__objc_stubs: 0x27c0
+  __TEXT.__objc_methlist: 0xcac
   __TEXT.__const: 0x118
-  __TEXT.__oslogstring: 0x2a20
-  __TEXT.__cstring: 0xd11
-  __TEXT.__objc_methname: 0x3056
-  __TEXT.__objc_classname: 0x1b1
-  __TEXT.__objc_methtype: 0xbde
-  __TEXT.__gcc_except_tab: 0x2c80
-  __TEXT.__unwind_info: 0x5f8
-  __DATA_CONST.__auth_got: 0x368
+  __TEXT.__gcc_except_tab: 0x2cf4
+  __TEXT.__cstring: 0xce9
+  __TEXT.__oslogstring: 0x28ac
+  __TEXT.__objc_classname: 0x1a0
+  __TEXT.__objc_methname: 0x2ea8
+  __TEXT.__objc_methtype: 0xb97
+  __TEXT.__unwind_info: 0x5f0
+  __DATA_CONST.__auth_got: 0x340
   __DATA_CONST.__got: 0x180
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x530
-  __DATA_CONST.__cfstring: 0xc80
-  __DATA_CONST.__objc_classlist: 0x60
+  __DATA_CONST.__const: 0x560
+  __DATA_CONST.__cfstring: 0xc60
+  __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x48
+  __DATA_CONST.__objc_superrefs: 0x40
   __DATA_CONST.__objc_intobj: 0x30
-  __DATA.__objc_const: 0x1690
-  __DATA.__objc_selrefs: 0xbc0
-  __DATA.__objc_ivar: 0xb4
-  __DATA.__objc_data: 0x3c0
+  __DATA.__objc_const: 0x1120
+  __DATA.__objc_selrefs: 0xc30
+  __DATA.__objc_ivar: 0xa4
+  __DATA.__objc_data: 0x370
   __DATA.__data: 0x4f0
   __DATA.__bss: 0x68
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9E260E98-1F55-3664-AF2D-DCF1910404FC
-  Functions: 438
-  Symbols:   166
-  CStrings:  1077
+  UUID: F1F30FC0-CB77-35C2-88B5-CC0747D8FCEF
+  Functions: 415
+  Symbols:   161
+  CStrings:  1049
 
Symbols:
+ _OBJC_CLASS_$__ANEModelToken
+ _fcntl
- _CFRelease
- _SecTaskCopySigningIdentifier
- _SecTaskCopyTeamIdentifier
- _SecTaskCreateWithAuditToken
- _kCFAllocatorDefault
- _proc_name
- _proc_pidpath_audittoken
CStrings:
+ "%@: fcntl(F_RDADVISE). errno=%d : %s"
+ "@24@0:8^{ANEProgramInstanceStruct=^v^vQQC^[512c]^Q^{ANEProgramIOInfoStruct}^{ANEProgramIOInfoStruct}C^[512c]^QC^{ANEProgramProcedureStruct}QIQQcQQiC}16"
+ "T^{ANEProgramInstanceStruct=^v^vQQC^[512c]^Q^{ANEProgramIOInfoStruct}^{ANEProgramIOInfoStruct}C^[512c]^QC^{ANEProgramProcedureStruct}QIQQcQQiC},N,V_programInstance"
+ "^{ANEProgramInstanceStruct=^v^vQQC^[512c]^Q^{ANEProgramIOInfoStruct}^{ANEProgramIOInfoStruct}C^[512c]^QC^{ANEProgramProcedureStruct}QIQQcQQiC}"
+ "^{ANEProgramInstanceStruct=^v^vQQC^[512c]^Q^{ANEProgramIOInfoStruct}^{ANEProgramIOInfoStruct}C^[512c]^QC^{ANEProgramProcedureStruct}QIQQcQQiC}16@0:8"
+ "v24@0:8^{ANEProgramInstanceStruct=^v^vQQC^[512c]^Q^{ANEProgramIOInfoStruct}^{ANEProgramIOInfoStruct}C^[512c]^QC^{ANEProgramProcedureStruct}QIQQcQQiC}16"
- "%@: SecTaskCopySigningIdentifier() returned csIdentity=\"%@\""
- "%@: SecTaskCopyTeamIdentifier() returned teamIdentity=\"%@\""
- "%@: client(%d) : SecTaskCreateWithAuditToken() failed"
- "%@: client(%d) : missing teamIdentity"
- "%@: proc_name(%d) failed. %{darwin.errno}d"
- "%@: proc_pidpath_audittoken(%d) failed. %{darwin.errno}d"
- "%@: proc_pidpath_audittoken(%d) procName=%@ procPath=%@"
- "%@: processNameForIdentifier: returned %@"
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
