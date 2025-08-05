## libprequelite.dylib

> `/usr/lib/libprequelite.dylib`

```diff

-133.0.0.0.0
-  __TEXT.__text: 0xc664
-  __TEXT.__auth_stubs: 0xa30
-  __TEXT.__objc_methlist: 0xd1c
+135.0.0.0.0
+  __TEXT.__text: 0xc9b0
+  __TEXT.__auth_stubs: 0xa40
+  __TEXT.__objc_methlist: 0xd7c
   __TEXT.__const: 0x68
   __TEXT.__cstring: 0xe16
   __TEXT.__oslogstring: 0x5df
   __TEXT.__gcc_except_tab: 0x80
-  __TEXT.__unwind_info: 0x340
-  __TEXT.__objc_classname: 0x122
-  __TEXT.__objc_methname: 0x1e45
-  __TEXT.__objc_methtype: 0x775
-  __TEXT.__objc_stubs: 0x15a0
+  __TEXT.__unwind_info: 0x354
+  __TEXT.__objc_classname: 0x14e
+  __TEXT.__objc_methname: 0x2041
+  __TEXT.__objc_methtype: 0x7f2
+  __TEXT.__objc_stubs: 0x15e0
   __DATA_CONST.__got: 0x50
   __DATA_CONST.__const: 0x238
-  __DATA_CONST.__objc_classlist: 0x40
+  __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_catlist: 0x60
-  __DATA_CONST.__objc_protolist: 0x40
+  __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x20b0
-  __DATA_CONST.__objc_selrefs: 0x900
+  __DATA_CONST.__objc_const: 0x2300
+  __DATA_CONST.__objc_selrefs: 0x930
+  __DATA_CONST.__objc_protorefs: 0x20
+  __DATA_CONST.__objc_classrefs: 0xf0
+  __DATA_CONST.__objc_superrefs: 0x30
   __AUTH_CONST.__cfstring: 0xc40
-  __AUTH_CONST.__objc_const: 0x0
+  __AUTH_CONST.__objc_const: 0x48
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH_CONST.__auth_got: 0x528
-  __DATA.__objc_protorefs: 0x20
-  __DATA.__objc_classrefs: 0xe8
-  __DATA.__objc_superrefs: 0x28
-  __DATA.__objc_ivar: 0x10c
-  __DATA.__data: 0x308
+  __AUTH_CONST.__auth_got: 0x530
+  __AUTH.__objc_data: 0x50
+  __DATA.__objc_ivar: 0x124
+  __DATA.__data: 0x368
   __DATA.__bss: 0x18
   __DATA_DIRTY.__const: 0x40
   __DATA_DIRTY.__objc_const: 0x660

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 0301D0C7-4EBA-3FE9-AD8F-2A861BDA2D4A
-  Functions: 305
-  Symbols:   1258
-  CStrings:  854
+  UUID: DD7A51E9-6984-3FDD-844F-AF408BF4942C
+  Functions: 313
+  Symbols:   1296
+  CStrings:  878
 
Symbols:
+ -[PQLConnection _executeStmt:mustSucceed:preparationTime:]
+ -[PQLConnection _newStatementForFormat:preparationTime:arguments:]
+ -[PQLConnection profilingHookV2]
+ -[PQLConnection setProfilingHookV2:]
+ -[PQLConnection(Swift) _newStatementForBuilder:preparationTime:]
+ -[PQLResultSet initWithStatement:usingDatabase:preparationTime:]
+ -[PQLStatement _prepare:withDB:preparationTime:]
+ -[PQLStatement initWithFormat:arguments:db:cache:preparationTime:]
+ -[PQLStatement initWithStatement:forDB:preparationTime:]
+ -[PQLStatement unbindForDB:returnedRows:executionTime:preparationTime:]
+ -[PQLStatement(Swift) initWithQueryBuilder:db:cache:preparationTime:]
+ -[PQLStatementMetricsData executionTime]
+ -[PQLStatementMetricsData initWithStmt:returnedRows:executionTime:preparationTime:]
+ -[PQLStatementMetricsData preparationTime]
+ -[PQLStatementMetricsData returnedRows]
+ -[PQLStatementMetricsData stmt]
+ GCC_except_table11
+ GCC_except_table17
+ GCC_except_table51
+ GCC_except_table55
+ _OBJC_CLASS_$_PQLStatementMetricsData
+ _OBJC_IVAR_$_PQLConnection._profilingHookV2
+ _OBJC_IVAR_$_PQLResultSet._executionTime
+ _OBJC_IVAR_$_PQLResultSet._preparationTime
+ _OBJC_IVAR_$_PQLStatementMetricsData._executionTime
+ _OBJC_IVAR_$_PQLStatementMetricsData._preparationTime
+ _OBJC_IVAR_$_PQLStatementMetricsData._returnedRows
+ _OBJC_IVAR_$_PQLStatementMetricsData._stmt
+ _OBJC_METACLASS_$_PQLStatementMetricsData
+ __OBJC_$_INSTANCE_METHODS_PQLStatementMetricsData
+ __OBJC_$_INSTANCE_VARIABLES_PQLStatementMetricsData
+ __OBJC_$_PROP_LIST_PQLStatementMetrics
+ __OBJC_$_PROP_LIST_PQLStatementMetricsData
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_PQLStatementMetrics
+ __OBJC_$_PROTOCOL_METHOD_TYPES_PQLStatementMetrics
+ __OBJC_CLASS_PROTOCOLS_$_PQLStatementMetricsData
+ __OBJC_CLASS_RO_$_PQLStatementMetricsData
+ __OBJC_LABEL_PROTOCOL_$_PQLStatementMetrics
+ __OBJC_METACLASS_RO_$_PQLStatementMetricsData
+ __OBJC_PROTOCOL_$_PQLStatementMetrics
+ ___21-[PQLConnection init]_block_invoke.12
+ ___block_literal_global.15
+ ___block_literal_global.3
+ ___block_literal_global.6
+ ___timeInSeconds_block_invoke
+ _objc_msgSend$_executeStmt:mustSucceed:preparationTime:
+ _objc_msgSend$_newStatementForBuilder:preparationTime:
+ _objc_msgSend$_newStatementForFormat:preparationTime:arguments:
+ _objc_msgSend$_prepare:withDB:preparationTime:
+ _objc_msgSend$initWithFormat:arguments:db:cache:preparationTime:
+ _objc_msgSend$initWithQueryBuilder:db:cache:preparationTime:
+ _objc_msgSend$initWithStatement:forDB:preparationTime:
+ _objc_msgSend$initWithStatement:usingDatabase:preparationTime:
+ _objc_msgSend$initWithStmt:returnedRows:executionTime:preparationTime:
+ _objc_msgSend$profilingHookV2
+ _objc_msgSend$unbindForDB:returnedRows:executionTime:preparationTime:
+ _objc_retain_x26
+ _objc_retain_x28
+ _timeInSeconds
+ _timeInSeconds.factor
+ _timeInSeconds.once
- -[PQLConnection _executeStmt:mustSucceed:]
- -[PQLConnection _newStatementForFormat:arguments:]
- -[PQLConnection(Swift) _newStatementForBuilder:]
- -[PQLResultSet initWithStatement:usingDatabase:]
- -[PQLStatement _prepare:withDB:]
- -[PQLStatement initWithFormat:arguments:db:cache:]
- -[PQLStatement initWithStatement:forDB:]
- -[PQLStatement unbindForDB:returnedRows:]
- -[PQLStatement(Swift) initWithQueryBuilder:db:cache:]
- GCC_except_table15
- GCC_except_table47
- GCC_except_table53
- GCC_except_table9
- _OBJC_IVAR_$_PQLStatement._profilingHook
- ___21-[PQLConnection init]_block_invoke.10
- ___block_literal_global.13
- ___block_literal_global.4
- ___block_literal_global.515
- ___durationInSeconds_block_invoke
- _durationInSeconds.factor
- _durationInSeconds.once
- _objc_msgSend$_executeStmt:mustSucceed:
- _objc_msgSend$_newStatementForBuilder:
- _objc_msgSend$_newStatementForFormat:arguments:
- _objc_msgSend$_prepare:withDB:
- _objc_msgSend$initWithFormat:arguments:db:cache:
- _objc_msgSend$initWithQueryBuilder:db:cache:
- _objc_msgSend$initWithStatement:forDB:
- _objc_msgSend$initWithStatement:usingDatabase:
- _objc_msgSend$unbindForDB:returnedRows:
- _objc_retain_x25
CStrings:
+ "\x0122!"
+ "\x12"
+ "!#B\x11\x1e"
+ "@32@0:8@?16^Q24"
+ "@40@0:8@16@24Q32"
+ "@40@0:8@16@24^Q32"
+ "@40@0:8@16^Q24*32"
+ "@48@0:8@?16@24^{cache_s=}32^Q40"
+ "@48@0:8^{sqlite3_stmt=}16Q24d32d40"
+ "@56@0:8@16*24@32^{cache_s=}40^Q48"
+ "B36@0:8@16B24Q28"
+ "B40@0:8r*16@24^Q32"
+ "PQLStatementMetrics"
+ "PQLStatementMetricsData"
+ "T@\"NSString\",?,R,C"
+ "T@?,C,N,V_profilingHookV2"
+ "TQ,R,N"
+ "TQ,R,N,V_returnedRows"
+ "T^{sqlite3_stmt=},R,N,V_stmt"
+ "Td,R,N,V_executionTime"
+ "Td,R,N,V_preparationTime"
+ "_executeStmt:mustSucceed:preparationTime:"
+ "_executionTime"
+ "_newStatementForBuilder:preparationTime:"
+ "_newStatementForFormat:preparationTime:arguments:"
+ "_preparationTime"
+ "_prepare:withDB:preparationTime:"
+ "_profilingHookV2"
+ "_returnedRows"
+ "executionTime"
+ "initWithFormat:arguments:db:cache:preparationTime:"
+ "initWithQueryBuilder:db:cache:preparationTime:"
+ "initWithStatement:forDB:preparationTime:"
+ "initWithStatement:usingDatabase:preparationTime:"
+ "initWithStmt:returnedRows:executionTime:preparationTime:"
+ "preparationTime"
+ "profilingHookV2"
+ "returnedRows"
+ "setProfilingHookV2:"
+ "unbindForDB:returnedRows:executionTime:preparationTime:"
+ "v48@0:8@16Q24Q32Q40"
- "\x012\x12!"
- "\x13"
- "!#B\x11\x1d"
- "@40@0:8@?16@24^{cache_s=}32"
- "@48@0:8@16*24@32^{cache_s=}40"
- "B28@0:8@16B24"
- "B32@0:8r*16@24"
- "_executeStmt:mustSucceed:"
- "_newStatementForBuilder:"
- "_newStatementForFormat:arguments:"
- "_prepare:withDB:"
- "initWithFormat:arguments:db:cache:"
- "initWithQueryBuilder:db:cache:"
- "initWithStatement:forDB:"
- "initWithStatement:usingDatabase:"
- "unbindForDB:returnedRows:"
- "v32@0:8@16Q24"

```
