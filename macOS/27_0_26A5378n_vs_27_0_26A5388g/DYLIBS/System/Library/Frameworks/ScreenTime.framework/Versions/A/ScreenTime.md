## ScreenTime

> `/System/Library/Frameworks/ScreenTime.framework/Versions/A/ScreenTime`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__AUTH_CONST.__cfstring`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-645.1.401.0.0
-  __TEXT.__text: 0x6204
-  __TEXT.__objc_methlist: 0x7bc
-  __TEXT.__const: 0x88
-  __TEXT.__cstring: 0x424
+649.0.0.0.0
+  __TEXT.__text: 0x6618
+  __TEXT.__objc_methlist: 0x7fc
+  __TEXT.__const: 0x80
+  __TEXT.__cstring: 0x42d
   __TEXT.__gcc_except_tab: 0xf4
   __TEXT.__oslogstring: 0x626
-  __TEXT.__unwind_info: 0x2a8
+  __TEXT.__unwind_info: 0x2d8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x660
+  __DATA_CONST.__objc_selrefs: 0x698
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x28
-  __DATA_CONST.__got: 0x158
-  __AUTH_CONST.__const: 0x450
+  __DATA_CONST.__got: 0x160
+  __AUTH_CONST.__const: 0x570
   __AUTH_CONST.__cfstring: 0x2c0
-  __AUTH_CONST.__objc_const: 0xfe8
+  __AUTH_CONST.__objc_const: 0xfb8
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0xa0
-  __DATA.__objc_ivar: 0x64
+  __DATA.__objc_ivar: 0x60
   __DATA.__data: 0x240
+  __DATA.__bss: 0x10
   __DATA_DIRTY.__objc_data: 0x230
   __DATA_DIRTY.__bss: 0x10
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit

   - /System/Library/PrivateFrameworks/ViewBridge.framework/Versions/A/ViewBridge
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 201
-  Symbols:   582
-  CStrings:  58
+  Functions: 214
+  Symbols:   607
+  CStrings:  59
 
Symbols:
+ +[STWebHistory _legacyConnection]
+ -[STWebHistory _deleteAllHistoryWithHasMigrated:]
+ -[STWebHistory _deleteHistoryDuringInterval:hasMigrated:]
+ -[STWebHistory _deleteHistoryForURL:hasMigrated:]
+ -[STWebHistory _fetchAllHistoryWithHasMigrated:completionHandler:]
+ -[STWebHistory _fetchHistoryDuringInterval:hasMigrated:completionHandler:]
+ __49-[STWebHistory _deleteAllHistoryWithHasMigrated:]_block_invoke
+ __49-[STWebHistory _deleteAllHistoryWithHasMigrated:]_block_invoke_2
+ __49-[STWebHistory _deleteHistoryForURL:hasMigrated:]_block_invoke
+ __49-[STWebHistory _deleteHistoryForURL:hasMigrated:]_block_invoke_2
+ __57-[STWebHistory _deleteHistoryDuringInterval:hasMigrated:]_block_invoke
+ __57-[STWebHistory _deleteHistoryDuringInterval:hasMigrated:]_block_invoke_2
+ __66-[STWebHistory _fetchAllHistoryWithHasMigrated:completionHandler:]_block_invoke_2
+ __74-[STWebHistory _fetchHistoryDuringInterval:hasMigrated:completionHandler:]_block_invoke
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
+ ___block_descriptor_40_e8_32bs_e27_v24?0"NSSet"8"NSError"16l
+ ___block_descriptor_40_e8_32s_e8_v12?0B8l
+ ___block_descriptor_48_e8_32s40bs_e8_v12?0B8l
+ ___block_descriptor_48_e8_32s40s_e8_v12?0B8l
+ ___block_descriptor_56_e8_32s40s48bs_e8_v12?0B8l
+ _legacyConnection.connection
+ _legacyConnection.onceToken
+ _objc_msgSend$_deleteAllHistoryWithHasMigrated:
+ _objc_msgSend$_deleteHistoryDuringInterval:hasMigrated:
+ _objc_msgSend$_deleteHistoryForURL:hasMigrated:
+ _objc_msgSend$_fetchAllHistoryWithHasMigrated:completionHandler:
+ _objc_msgSend$_fetchHistoryDuringInterval:hasMigrated:completionHandler:
+ _objc_msgSend$_legacyConnection
+ _objc_msgSend$hasMigratedWithReplyHandler:
- -[STWebHistory dealloc]
- -[STWebHistory xpcConnection]
- OBJC_IVAR_$_STWebHistory._xpcConnection
- __32-[STWebHistory deleteAllHistory]_block_invoke
- __32-[STWebHistory deleteAllHistory]_block_invoke_2
- __36-[STWebHistory deleteHistoryForURL:]_block_invoke
- __36-[STWebHistory deleteHistoryForURL:]_block_invoke_2
- __44-[STWebHistory deleteHistoryDuringInterval:]_block_invoke
- __44-[STWebHistory deleteHistoryDuringInterval:]_block_invoke_2
- __53-[STWebHistory fetchAllHistoryWithCompletionHandler:]_block_invoke_2
- __61-[STWebHistory fetchHistoryDuringInterval:completionHandler:]_block_invoke
- ___32-[STWebHistory deleteAllHistory]_block_invoke_2
- ___36-[STWebHistory deleteHistoryForURL:]_block_invoke_2
- ___44-[STWebHistory deleteHistoryDuringInterval:]_block_invoke_2
- ___53-[STWebHistory fetchAllHistoryWithCompletionHandler:]_block_invoke_3
- ___block_descriptor_48_e8_32s40s_e17_v16?0"NSError"8l
CStrings:
+ "v12@?0B8"
```
