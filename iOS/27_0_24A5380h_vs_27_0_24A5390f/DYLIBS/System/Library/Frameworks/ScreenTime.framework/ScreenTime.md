## ScreenTime

> `/System/Library/Frameworks/ScreenTime.framework/ScreenTime`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__AUTH_CONST.__cfstring`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-645.1.100.0.0
-  __TEXT.__text: 0x54ac
-  __TEXT.__objc_methlist: 0x7ac
-  __TEXT.__const: 0x80
-  __TEXT.__cstring: 0x35d
+649.0.0.0.0
+  __TEXT.__text: 0x5888
+  __TEXT.__objc_methlist: 0x7ec
+  __TEXT.__const: 0x78
+  __TEXT.__cstring: 0x366
   __TEXT.__gcc_except_tab: 0xf0
   __TEXT.__oslogstring: 0x588
-  __TEXT.__unwind_info: 0x270
+  __TEXT.__unwind_info: 0x2a0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x348
+  __DATA_CONST.__const: 0x3e8
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x630
+  __DATA_CONST.__objc_selrefs: 0x668
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x28
-  __DATA_CONST.__got: 0x168
-  __AUTH_CONST.__const: 0xc0
+  __DATA_CONST.__got: 0x170
+  __AUTH_CONST.__const: 0x120
   __AUTH_CONST.__cfstring: 0x220
-  __AUTH_CONST.__objc_const: 0xf40
+  __AUTH_CONST.__objc_const: 0xf10
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x50
-  __DATA.__objc_ivar: 0x64
+  __DATA.__objc_ivar: 0x60
   __DATA.__data: 0x240
+  __DATA.__bss: 0x10
   __DATA_DIRTY.__objc_data: 0x230
   __DATA_DIRTY.__bss: 0x10
   - /System/Library/Frameworks/AVKit.framework/AVKit

   - /System/Library/PrivateFrameworks/ScreenTimeCore.framework/ScreenTimeCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 185
-  Symbols:   557
-  CStrings:  52
+  Functions: 198
+  Symbols:   582
+  CStrings:  53
 
Symbols:
+ +[STWebHistory _legacyConnection]
+ -[STWebHistory _deleteAllHistoryWithHasMigrated:]
+ -[STWebHistory _deleteHistoryDuringInterval:hasMigrated:]
+ -[STWebHistory _deleteHistoryForURL:hasMigrated:]
+ -[STWebHistory _fetchAllHistoryWithHasMigrated:completionHandler:]
+ -[STWebHistory _fetchHistoryDuringInterval:hasMigrated:completionHandler:]
+ __OBJC_$_CLASS_METHODS_STWebHistory
+ ___33+[STWebHistory _legacyConnection]_block_invoke
+ ___49-[STWebHistory _deleteAllHistoryWithHasMigrated:]_block_invoke
+ ___49-[STWebHistory _deleteAllHistoryWithHasMigrated:]_block_invoke_2
+ ___49-[STWebHistory _deleteHistoryForURL:hasMigrated:]_block_invoke
+ ___49-[STWebHistory _deleteHistoryForURL:hasMigrated:]_block_invoke_2
+ ___57-[STWebHistory _deleteHistoryDuringInterval:hasMigrated:]_block_invoke
+ ___57-[STWebHistory _deleteHistoryDuringInterval:hasMigrated:]_block_invoke_2
+ ___66-[STWebHistory _fetchAllHistoryWithHasMigrated:completionHandler:]_block_invoke
+ ___66-[STWebHistory _fetchAllHistoryWithHasMigrated:completionHandler:]_block_invoke_2
+ ___66-[STWebHistory _fetchAllHistoryWithHasMigrated:completionHandler:]_block_invoke_3
+ ___74-[STWebHistory _fetchHistoryDuringInterval:hasMigrated:completionHandler:]_block_invoke
+ ___74-[STWebHistory _fetchHistoryDuringInterval:hasMigrated:completionHandler:]_block_invoke_2
+ ___74-[STWebHistory _fetchHistoryDuringInterval:hasMigrated:completionHandler:]_block_invoke_3
+ ___block_descriptor_40_e8_32bs_e27_v24?0"NSSet"8"NSError"16ls32l8
+ ___block_descriptor_40_e8_32s_e8_v12?0B8ls32l8
+ ___block_descriptor_48_e8_32s40bs_e8_v12?0B8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e8_v12?0B8ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s48bs_e8_v12?0B8ls32l8s40l8s48l8
+ __legacyConnection.connection
+ __legacyConnection.onceToken
+ _objc_msgSend$_deleteAllHistoryWithHasMigrated:
+ _objc_msgSend$_deleteHistoryDuringInterval:hasMigrated:
+ _objc_msgSend$_deleteHistoryForURL:hasMigrated:
+ _objc_msgSend$_fetchAllHistoryWithHasMigrated:completionHandler:
+ _objc_msgSend$_fetchHistoryDuringInterval:hasMigrated:completionHandler:
+ _objc_msgSend$_legacyConnection
+ _objc_msgSend$hasMigratedWithReplyHandler:
- -[STWebHistory dealloc]
- -[STWebHistory xpcConnection]
- _OBJC_IVAR_$_STWebHistory._xpcConnection
- ___32-[STWebHistory deleteAllHistory]_block_invoke_2
- ___36-[STWebHistory deleteHistoryForURL:]_block_invoke_2
- ___44-[STWebHistory deleteHistoryDuringInterval:]_block_invoke_2
- ___53-[STWebHistory fetchAllHistoryWithCompletionHandler:]_block_invoke_3
- ___61-[STWebHistory fetchHistoryDuringInterval:completionHandler:]_block_invoke_3
- ___block_descriptor_48_e8_32s40s_e17_v16?0"NSError"8ls32l8s40l8
CStrings:
+ "v12@?0B8"
```
