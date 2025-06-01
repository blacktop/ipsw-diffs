## BiomeStreams

> `/System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams`

```diff

-123.1.9.1.0
-  __TEXT.__text: 0x4999fc
+123.2.4.0.0
+  __TEXT.__text: 0x49a038
   __TEXT.__auth_stubs: 0x2290
-  __TEXT.__objc_methlist: 0x14ae0
-  __TEXT.__const: 0xaa464
-  __TEXT.__cstring: 0x34c4e
-  __TEXT.__oslogstring: 0xaaed
-  __TEXT.__gcc_except_tab: 0xad8
+  __TEXT.__objc_methlist: 0x14af8
+  __TEXT.__const: 0xaa484
+  __TEXT.__cstring: 0x34c8e
+  __TEXT.__oslogstring: 0xabba
+  __TEXT.__gcc_except_tab: 0xb00
   __TEXT.__dlopen_cstrs: 0x5d4
-  __TEXT.__constg_swiftt: 0xafa4
+  __TEXT.__constg_swiftt: 0xafac
   __TEXT.__swift5_typeref: 0x575f
   __TEXT.__swift5_reflstr: 0x69c1
   __TEXT.__swift5_fieldmd: 0xb6a4

   __TEXT.__swift5_mpenum: 0x44
   __TEXT.__swift5_protos: 0x34
   __TEXT.__swift5_assocty: 0xc60
-  __TEXT.__unwind_info: 0xdbdc
-  __TEXT.__eh_frame: 0xe318
+  __TEXT.__unwind_info: 0xdc28
+  __TEXT.__eh_frame: 0xe348
   __TEXT.__objc_classname: 0x2757
-  __TEXT.__objc_methname: 0x1ba0a
+  __TEXT.__objc_methname: 0x1bac6
   __TEXT.__objc_methtype: 0x3653
-  __TEXT.__objc_stubs: 0x102a0
+  __TEXT.__objc_stubs: 0x10380
   __DATA_CONST.__got: 0x410
-  __DATA_CONST.__const: 0x2a388
+  __DATA_CONST.__const: 0x2a398
   __DATA_CONST.__objc_classlist: 0xed8
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x1c8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x44678
-  __DATA_CONST.__objc_selrefs: 0x59a0
+  __DATA_CONST.__objc_const: 0x44698
+  __DATA_CONST.__objc_selrefs: 0x59c8
   __DATA_CONST.__objc_arraydata: 0xa0
-  __AUTH_CONST.__cfstring: 0x8c80
+  __AUTH_CONST.__cfstring: 0x8ce0
   __AUTH_CONST.__objc_const: 0x9268
   __AUTH_CONST.__const: 0xd988
   __AUTH_CONST.__objc_intobj: 0x48

   __AUTH.__objc_data: 0x24a0
   __AUTH.__data: 0x12e00
   __DATA.__objc_protorefs: 0x80
-  __DATA.__objc_classrefs: 0xc78
+  __DATA.__objc_classrefs: 0xc80
   __DATA.__objc_superrefs: 0x9e8
-  __DATA.__objc_ivar: 0x180c
+  __DATA.__objc_ivar: 0x1810
   __DATA.__data: 0xdd40
   __DATA.__thread_vars: 0x420
   __DATA.__thread_data: 0x112

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: FABD46AD-7D2E-3183-8A88-60D39B187067
-  Functions: 27711
-  Symbols:   77151
-  CStrings:  16287
+  UUID: CBCFBA34-C7EE-31A4-998D-87BD220CD1CC
+  Functions: 27717
+  Symbols:   77171
+  CStrings:  16301
 
Symbols:
+ -[BMComputeXPCSubscription initWithToken:descriptor:].cold.7
+ -[BMSQLDatabase _attachDatabase:name:error:]
+ -[BMSQLDatabase attachDatabaseWithResourceIdentifier:useCase:error:]
+ GCC_except_table20
+ _$s12BiomeStreams16DatabaseResourceP03sqlC07useCaseSo13BMSQLDatabaseCSS_tKFZ
+ _$s12BiomeStreams16DatabaseResourceP03sqlC07useCaseSo13BMSQLDatabaseCSS_tKFZTj
+ _$s12BiomeStreams16DatabaseResourceP03sqlC07useCaseSo13BMSQLDatabaseCSS_tKFZTq
+ _$s12BiomeStreams16DatabaseResourcePAAE03sqlC07useCaseSo13BMSQLDatabaseCSS_tKFZ
+ _OBJC_IVAR_$_BMSQLDatabase._resourceAccessAssertions
+ __unnamed_array_storage.283
+ _objc_msgSend$_attachDatabase:name:error:
+ _objc_msgSend$dateWithTimeIntervalSinceNow:
+ _objc_msgSend$initFileURLWithPath:
+ _objc_msgSend$initWithType:name:
+ _objc_msgSend$initWithUseCase:
+ _objc_msgSend$requestAccessToResource:mode:error:
+ _objc_msgSend$stringByAppendingPathExtension:
- __unnamed_array_storage.270
CStrings:
+ "\x12\x11\x11"
+ "ATTACH DATABASE \"%@\" AS \"%@\""
+ "Access assertion %@ has a nil path"
+ "Vision"
+ "_attachDatabase:name:error:"
+ "_resourceAccessAssertions"
+ "attachDatabaseWithResourceIdentifier:useCase:error:"
+ "dateWithTimeIntervalSinceNow:"
+ "initFileURLWithPath:"
+ "sqlite3"
+ "stringByAppendingPathExtension:"
+ "xpc_event subscription %@ is missing createdAt date - and could not fetch boot time, defaulting to 30 days ago %@"
+ "xpc_event subscription %@ is missing createdAt date - defaulting to device boot time of %@"
- "\x11\x11\x11"
- "ATTACH DATABASE \"%@\" AS %@"

```
