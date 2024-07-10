## CallHistory

> `/System/Library/PrivateFrameworks/CallHistory.framework/Versions/A/CallHistory`

```diff

-1251.100.11.0.0
-  __TEXT.__text: 0x386ec
+1253.100.1.0.0
+  __TEXT.__text: 0x39a74
   __TEXT.__auth_stubs: 0x640
-  __TEXT.__objc_methlist: 0x2ad0
+  __TEXT.__objc_methlist: 0x2b48
   __TEXT.__const: 0x2d0
-  __TEXT.__cstring: 0x2166
-  __TEXT.__oslogstring: 0x37fc
+  __TEXT.__cstring: 0x2174
+  __TEXT.__oslogstring: 0x3d82
   __TEXT.__gcc_except_tab: 0x6c4
   __TEXT.__dlopen_cstrs: 0x95
-  __TEXT.__unwind_info: 0xe68
+  __TEXT.__unwind_info: 0xe88
   __TEXT.__eh_frame: 0x50
   __TEXT.__objc_classname: 0x5a5
-  __TEXT.__objc_methname: 0x805c
-  __TEXT.__objc_methtype: 0xda7
-  __TEXT.__objc_stubs: 0x6560
-  __DATA_CONST.__got: 0x378
+  __TEXT.__objc_methname: 0x82cb
+  __TEXT.__objc_methtype: 0xdd2
+  __TEXT.__objc_stubs: 0x6740
+  __DATA_CONST.__got: 0x380
   __DATA_CONST.__const: 0x648
   __DATA_CONST.__objc_classlist: 0x1a8
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1ec0
+  __DATA_CONST.__objc_selrefs: 0x1f38
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x130
   __AUTH_CONST.__auth_got: 0x330
   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__const: 0xe90
-  __AUTH_CONST.__cfstring: 0x26c0
+  __AUTH_CONST.__cfstring: 0x26e0
   __AUTH_CONST.__objc_const: 0x8328
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH.__objc_data: 0x5a0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1257
-  Symbols:   3419
-  CStrings:  379
+  Functions: 1272
+  Symbols:   3451
+  CStrings:  380
 
Symbols:
+ +[DBManager deleteDirectoryAtLocation:]
+ +[DBManager deleteDirectoryAtLocation:].cold.1
+ +[DBManager destroyDBAtLocation:withModel:]
+ +[DBManager destroyDBAtLocation:withModel:].cold.1
+ +[DBManager destroyDBAtLocation:withModel:].cold.2
+ +[DBManager getManagedObjectModelFromDB:orModelURL:]
+ +[DBManager getPersistentCoordinatorWithModel:]
+ +[DBManager getPersistentCoordinatorWithModel:].cold.1
+ +[DBManager migrationDirectoryFromSourceURL:]
+ +[DBManager migrationDirectoryFromSourceURL:].cold.1
+ +[DBManager migrationStoreURLIn:fromSourceURL:andModelURL:]
+ +[DBManager modelForDBMetadata:]
+ +[DBManager modelForDBMetadata:].cold.1
+ +[DBManager moveDBAtLocation:toLocation:withModel:]
+ +[DBManager moveDBAtLocation:toLocation:withModel:].cold.1
+ +[DBManager performMigrationFrom:sourceModel:toDestinationURL:destinationModel:mappingModel:isEncrypted:]
+ +[DBManager performMigrationFrom:sourceModel:toDestinationURL:destinationModel:mappingModel:isEncrypted:].cold.1
+ +[DBManager performMigrationFrom:sourceModel:toDestinationURL:destinationModel:mappingModel:isEncrypted:].cold.2
+ +[DBManager sourceMetadataForDBAtLocation:withOptions:]
+ +[DBManager sourceMetadataForDBAtLocation:withOptions:].cold.1
+ -[CallDBManager initWithDeviceObserver:]
+ -[CallDBManagerServer initWithDeviceObserver:]
+ GCC_except_table15
+ GCC_except_table22
+ _OBJC_CLASS_$_NSPersistentStore
+ __block_literal_global.36
+ __block_literal_global.41
+ _objc_msgSend$cachedModelForPersistentStoreWithURL:options:error:
+ _objc_msgSend$createDirectoryAtPath:withIntermediateDirectories:attributes:error:
+ _objc_msgSend$deleteDirectoryAtLocation:
+ _objc_msgSend$destroyDBAtLocation:withModel:
+ _objc_msgSend$getManagedObjectModelFromDB:orModelURL:
+ _objc_msgSend$getPersistentCoordinatorWithModel:
+ _objc_msgSend$initWithDeviceObserver:
+ _objc_msgSend$metadataForPersistentStoreOfType:URL:options:error:
+ _objc_msgSend$migrationDirectoryFromSourceURL:
+ _objc_msgSend$migrationStoreURLIn:fromSourceURL:andModelURL:
+ _objc_msgSend$modelForDBMetadata:
+ _objc_msgSend$moveDBAtLocation:toLocation:withModel:
+ _objc_msgSend$pathExtension
+ _objc_msgSend$performMigrationFrom:sourceModel:toDestinationURL:destinationModel:mappingModel:isEncrypted:
+ _objc_msgSend$removeItemAtURL:error:
+ _objc_msgSend$sourceMetadataForDBAtLocation:withOptions:
+ _objc_msgSend$stringByDeletingPathExtension
- +[DBManager destroyDBAtLocation:withModelAtLocation:].cold.1
- +[DBManager getPersistentCoordinator:]
- +[DBManager getPersistentCoordinator:].cold.1
- +[DBManager modelForDBAtLocation:]
- +[DBManager modelForDBAtLocation:].cold.1
- GCC_except_table21
- _OUTLINED_FUNCTION_8
- __block_literal_global.35
- __block_literal_global.40
- _objc_msgSend$getPersistentCoordinator:
- _objc_msgSend$modelForDBAtLocation:
CStrings:
+ "%!@(MISSING).%!@(MISSING).%!@(MISSING)"
+ "1253.100.1"
+ "1253.100.1~169"
+ "Migration"
- "1251.100.11"
- "1251.100.11~96"
- "_%!@(MISSING)"

```
