## EmailFoundation

> `/System/Library/PrivateFrameworks/EmailFoundation.framework/EmailFoundation`

```diff

-3774.100.2.2.5
-  __TEXT.__text: 0x5a158
+3774.200.91.2.1
+  __TEXT.__text: 0x5a918
   __TEXT.__auth_stubs: 0x1350
-  __TEXT.__objc_methlist: 0x55bc
-  __TEXT.__gcc_except_tab: 0xa064
+  __TEXT.__objc_methlist: 0x560c
+  __TEXT.__gcc_except_tab: 0xa12c
   __TEXT.__const: 0xda
-  __TEXT.__cstring: 0x41cb
+  __TEXT.__cstring: 0x425b
   __TEXT.__oslogstring: 0xda3
   __TEXT.__ustring: 0xee
   __TEXT.__swift5_typeref: 0xbd

   __TEXT.__swift5_reflstr: 0x13
   __TEXT.__swift5_fieldmd: 0x38
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x43c4
+  __TEXT.__unwind_info: 0x43fc
   __TEXT.__eh_frame: 0x100
   __TEXT.__objc_classname: 0xd6b
-  __TEXT.__objc_methname: 0xad33
-  __TEXT.__objc_methtype: 0x1ada
-  __TEXT.__objc_stubs: 0x7d00
-  __DATA_CONST.__got: 0x1b8
-  __DATA_CONST.__const: 0x1e38
+  __TEXT.__objc_methname: 0xaea9
+  __TEXT.__objc_methtype: 0x1af1
+  __TEXT.__objc_stubs: 0x7da0
+  __DATA_CONST.__got: 0x1c8
+  __DATA_CONST.__const: 0x1e88
   __DATA_CONST.__objc_classlist: 0x3e0
   __DATA_CONST.__objc_catlist: 0x100
   __DATA_CONST.__objc_protolist: 0x120
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x88d0
-  __DATA_CONST.__objc_selrefs: 0x2fa0
+  __DATA_CONST.__objc_const: 0x8940
+  __DATA_CONST.__objc_selrefs: 0x2fd8
   __DATA_CONST.__objc_arraydata: 0x48
   __AUTH_CONST.__objc_const: 0x3548
   __AUTH_CONST.__const: 0xeb0
-  __AUTH_CONST.__cfstring: 0x5060
+  __AUTH_CONST.__cfstring: 0x5140
   __AUTH_CONST.__auth_ptr: 0x30
   __AUTH_CONST.__objc_intobj: 0x120
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__auth_got: 0x9c0
   __AUTH.__objc_data: 0x410
+  __DATA.__objc_protorefs: 0x8
   __DATA.__objc_classrefs: 0x4f8
   __DATA.__objc_superrefs: 0x340
-  __DATA.__objc_ivar: 0x494
+  __DATA.__objc_ivar: 0x49c
   __DATA.__data: 0xf00
   __DATA.__crash_info: 0x40
   __DATA.__bss: 0xf0

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 2320
-  Symbols:   8982
-  CStrings:  3354
+  Functions: 2329
+  Symbols:   9016
+  CStrings:  3374
 
Symbols:
+ +[EFPrivacy redactedQueryStringForQueryString:]
+ -[EFSQLConnection preparedStatementForQueryString:transactionLabel:queryLogger:]
+ -[EFSQLConnection test_resultsForQueryString:]
+ -[EFSQLPreparedStatement .cxx_destruct]
+ -[EFSQLPreparedStatement initWithString:connection:transactionLabel:queryLogger:]
+ -[EFSQLPreparedStatement initWithString:connection:transactionLabel:queryLogger:].cold.1
+ -[EFSQLPreparedStatement queryLogger]
+ -[EFSQLPreparedStatement setQueryLogger:]
+ -[EFSQLPreparedStatement setTransactionLabel:]
+ -[EFSQLPreparedStatement transactionLabel]
+ -[NSError(EmailFoundationAdditions) ef_secureCodableError]
+ _NSMultipleUnderlyingErrorsKey
+ _NSURLErrorFailingURLPeerTrustErrorKey
+ _OBJC_IVAR_$_EFSQLPreparedStatement._queryLogger
+ _OBJC_IVAR_$_EFSQLPreparedStatement._transactionLabel
+ __OBJC_PROTOCOL_REFERENCE_$_NSSecureCoding
+ ___46-[EFSQLConnection test_resultsForQueryString:]_block_invoke
+ ___58-[NSError(EmailFoundationAdditions) ef_secureCodableError]_block_invoke
+ ___58-[NSError(EmailFoundationAdditions) ef_secureCodableError]_block_invoke_2
+ ___block_descriptor_40_ea8_32r_e26_"NSError"16?0"NSError"8lr32l8
+ ___block_descriptor_48_ea8_32s40r_e25_v32?0"NSString"816^B24ls32l8r40l8
+ ___block_literal_global.161
+ ___block_literal_global.164
+ _objc_msgSend$ef_secureCodableError
+ _objc_msgSend$initWithString:connection:transactionLabel:queryLogger:
+ _objc_msgSend$logQueryString:label:firstRowExecutionTime:totalExecutionTime:numberOfRows:
+ _objc_msgSend$preparedStatementForQueryString:transactionLabel:queryLogger:
+ _objc_msgSend$queryLogger
+ _objc_msgSend$supportsSecureCoding
+ _objc_msgSend$transactionLabel
- -[EFSQLConnection preparedStatementForQueryString:]
- -[EFSQLConnection resultsForQueryString:]
- -[EFSQLPreparedStatement initWithString:connection:]
- -[EFSQLPreparedStatement initWithString:connection:].cold.1
- ___41-[EFSQLConnection resultsForQueryString:]_block_invoke
- ___block_literal_global.160
- ___block_literal_global.163
- _objc_msgSend$initWithString:connection:
- _objc_msgSend$preparedStatementForQueryString:
CStrings:
+ "'(.*?)'"
+ "(?)"
+ "@\"<EFSQLQueryLogging>\""
+ "@\"NSError\"16@?0@\"NSError\"8"
+ "CAST\\(X\\? AS TEXT\\)"
+ "NSErrorClientCertificateChainKey"
+ "NSErrorPeerCertificateChainKey"
+ "T@\"<EFSQLQueryLogging>\",&,N,V_queryLogger"
+ "T@\"NSString\",C,N,V_transactionLabel"
+ "[0-9]+"
+ "\\(\\?+(, \\?+)*\\)"
+ "_queryLogger"
+ "_transactionLabel"
+ "ef_secureCodableError"
+ "initWithString:connection:transactionLabel:queryLogger:"
+ "logQueryString:label:firstRowExecutionTime:totalExecutionTime:numberOfRows:"
+ "preparedStatementForQueryString:transactionLabel:queryLogger:"
+ "queryLogger"
+ "redactedQueryStringForQueryString:"
+ "setQueryLogger:"
+ "setTransactionLabel:"
+ "test_resultsForQueryString:"
+ "transactionLabel"
- "initWithString:connection:"
- "preparedStatementForQueryString:"
- "resultsForQueryString:"

```
