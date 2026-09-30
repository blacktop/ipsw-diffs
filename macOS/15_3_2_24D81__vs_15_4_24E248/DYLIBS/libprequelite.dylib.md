## libprequelite.dylib

> `/usr/lib/libprequelite.dylib`

```diff

-138.0.0.0.0
-  __TEXT.__text: 0xd5bc
+139.0.0.0.0
+  __TEXT.__text: 0xd8d8
   __TEXT.__auth_stubs: 0x890
-  __TEXT.__objc_methlist: 0xd7c
-  __TEXT.__const: 0xa0
-  __TEXT.__cstring: 0xe16
-  __TEXT.__oslogstring: 0x5df
-  __TEXT.__gcc_except_tab: 0x9c
-  __TEXT.__unwind_info: 0x378
+  __TEXT.__objc_methlist: 0xf98
+  __TEXT.__const: 0xb8
+  __TEXT.__cstring: 0xe8f
+  __TEXT.__oslogstring: 0x655
+  __TEXT.__gcc_except_tab: 0xc4
+  __TEXT.__unwind_info: 0x390
   __TEXT.__objc_classname: 0x14e
   __TEXT.__objc_methname: 0x2021
   __TEXT.__objc_methtype: 0x7f2

   __DATA_CONST.__objc_catlist: 0x60
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x930
+  __DATA_CONST.__objc_selrefs: 0x9c8
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x30
   __AUTH_CONST.__auth_got: 0x458
   __AUTH_CONST.__const: 0x220
   __AUTH_CONST.__cfstring: 0xc40
-  __AUTH_CONST.__objc_const: 0x2a00
+  __AUTH_CONST.__objc_const: 0x2660
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH.__objc_data: 0x1e0
   __DATA.__objc_ivar: 0x124

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 665490F9-9A34-3762-8772-E64C909D672A
-  Functions: 325
-  Symbols:   987
-  CStrings:  873
+  UUID: E385BC54-2A4A-3887-B38A-625642DD60D8
+  Functions: 343
+  Symbols:   1054
+  CStrings:  876
 
Symbols:
+ +[NSError(PQLValuable) newFromSqliteStatement:atIndex:].cold.1
+ +[NSError(PQLValuable) newFromSqliteValue:].cold.1
+ +[PQLConnection initialize].cold.1
+ -[NSError(PQLValuable) sqliteBind:index:].cold.1
+ -[PQLConnection _batchStartIfNeeded:].cold.2
+ -[PQLConnection _batchStopIfNeeded].cold.2
+ -[PQLConnection _batchStopIfNeeded].cold.3
+ -[PQLConnection _batchStopIfNeeded].cold.4
+ -[PQLConnection _batchStopIfNeeded].cold.5
+ -[PQLConnection _clearCleanupCacheQueueIfNeeded].cold.1
+ -[PQLConnection _createCacheIfNeeded].cold.1
+ -[PQLConnection _fullSync].cold.1
+ -[PQLConnection _fullSync].cold.2
+ -[PQLConnection _fullSync].cold.3
+ -[PQLConnection _incrementalVacuum:].cold.1
+ -[PQLConnection _performWithFlags:action:whenFlushed:].cold.2
+ -[PQLConnection _performWithFlags:action:whenFlushed:].cold.3
+ -[PQLConnection _performWithFlags:action:whenFlushed:].cold.4
+ -[PQLConnection _vacuumIfNeeded].cold.10
+ -[PQLConnection _vacuumIfNeeded].cold.4
+ -[PQLConnection _vacuumIfNeeded].cold.5
+ -[PQLConnection _vacuumIfNeeded].cold.6
+ -[PQLConnection _vacuumIfNeeded].cold.7
+ -[PQLConnection _vacuumIfNeeded].cold.8
+ -[PQLConnection _vacuumIfNeeded].cold.9
+ -[PQLConnection backupToURL:progress:].cold.1
+ -[PQLConnection close:].cold.1
+ -[PQLConnection close:].cold.2
+ -[PQLConnection close:].cold.3
+ -[PQLConnection close:].cold.4
+ -[PQLConnection currentOperationDuration].cold.1
+ -[PQLConnection flush].cold.1
+ -[PQLConnection flush].cold.2
+ -[PQLConnection openAtURL:withFlags:error:].cold.1
+ -[PQLConnection openAtURL:withFlags:error:].cold.2
+ -[PQLConnection openAtURL:withFlags:error:].cold.3
+ -[PQLConnection setSynchronousMode:].cold.1
+ -[PQLConnection useBatchingOnTargetQueue:delay:changeCount:].cold.1
+ -[PQLResultSet defaultUnarchivingAllowedClasses].cold.1
+ -[PQLResultSet enumerateObjectsOfClass:initializer:].cold.1
+ -[PQLStatement bindArguments:db:].cold.1
+ -[PQLStatement bindArguments:db:].cold.2
+ -[PQLStatement initWithFormat:arguments:db:cache:preparationTime:].cold.1
+ -[PQLStatement initWithFormat:arguments:db:cache:preparationTime:].cold.2
+ -[PQLStatement initWithFormat:arguments:db:cache:preparationTime:].cold.3
+ -[PQLStatement initWithFormat:arguments:db:cache:preparationTime:].cold.4
+ -[PQLStatement initWithFormat:arguments:db:cache:preparationTime:].cold.5
+ -[PQLStatement initWithStatement:forDB:preparationTime:].cold.1
+ -[PQLStatement(Swift) bindFromArray:db:].cold.1
+ -[PQLStatement(Swift) bindFromArray:db:].cold.2
+ -[PQLStatement(Swift) bindFromArray:db:].cold.3
+ -[PQLStatement(Swift) initWithQueryBuilder:db:cache:preparationTime:].cold.1
+ -[PQLStatement(Swift) initWithQueryBuilder:db:cache:preparationTime:].cold.2
+ -[PQLStatement(Swift) initWithQueryBuilder:db:cache:preparationTime:].cold.3
+ _OUTLINED_FUNCTION_0
+ _OUTLINED_FUNCTION_1
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_3
+ __21-[PQLConnection init]_block_invoke.cold.1
+ __37-[PQLConnection _batchStartIfNeeded:]_block_invoke.cold.1
+ __PQLCacheValueRelease.cold.2
+ db_trace.cold.1
+ timeInSeconds.cold.1
CStrings:
+ "%s:%d: PQLStatement [%p] sqlite stmt [%p] sql [%s]"
+ "-[PQLStatement initWithFormat:arguments:db:cache:preparationTime:]"
+ "-[PQLStatement initWithStatement:forDB:preparationTime:]"
+ "cleaning - conn - cache - PQL - SQL: %p, %p, %p, %p"
+ "sqlite3_close(%p, %@) failed: %@"
+ "sqlite3_close(%p, %@) fails: [%s, %p] isn't finalized"
+ "uncaching: <%@:%p:%p>"
- "sp"
- "sqlite3_close(%@) failed: %@"
- "sqlite3_close(%@) fails: [%s] isn't finalized"
- "uncaching: <%@:%p>"

```
