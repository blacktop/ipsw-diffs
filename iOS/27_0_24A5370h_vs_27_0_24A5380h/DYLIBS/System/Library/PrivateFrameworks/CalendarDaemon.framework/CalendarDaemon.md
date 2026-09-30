## CalendarDaemon

> `/System/Library/PrivateFrameworks/CalendarDaemon.framework/CalendarDaemon`

```diff

-  __TEXT.__text: 0x76e0c
-  __TEXT.__objc_methlist: 0x6934
+  __TEXT.__text: 0x76ebc
+  __TEXT.__objc_methlist: 0x6954
   __TEXT.__cstring: 0x7520
   __TEXT.__const: 0x190
   __TEXT.__oslogstring: 0x8da3
   __TEXT.__gcc_except_tab: 0x1b20
   __TEXT.__dlopen_cstrs: 0xc0
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x1d40
+  __TEXT.__unwind_info: 0x1d48
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x1c8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3520
+  __DATA_CONST.__objc_selrefs: 0x3538
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x2d0
   __DATA_CONST.__objc_arraydata: 0x350
-  __DATA_CONST.__got: 0xa20
+  __DATA_CONST.__got: 0xa70
   __AUTH_CONST.__const: 0x8c0
   __AUTH_CONST.__cfstring: 0x7e60
-  __AUTH_CONST.__objc_const: 0xce78
+  __AUTH_CONST.__objc_const: 0xce80
   __AUTH_CONST.__objc_intobj: 0x498
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__auth_got: 0x1c68
-  __AUTH.__objc_data: 0x1540
+  __AUTH.__objc_data: 0x1b80
   __AUTH.__data: 0xa50
   __DATA.__objc_ivar: 0x860
   __DATA.__data: 0x1728
   __DATA.__bss: 0x220
   __DATA.__common: 0x18
-  __DATA_DIRTY.__objc_data: 0x1400
+  __DATA_DIRTY.__objc_data: 0xdc0
   __DATA_DIRTY.__bss: 0xd8
   __DATA_DIRTY.__common: 0x18
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 2345
-  Symbols:   9619
+  Functions: 2347
+  Symbols:   9626
   CStrings:  2846
 
Sections:
~ __TEXT.__gcc_except_tab : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH.__data : content changed
~ __DATA.__data : content changed
Symbols:
+ -[CADDatabaseConnectionPool performWithAllDatabasesWithConfiguration:options:block:]
+ -[CADDatabaseConnectionPool performWithConfiguration:options:databaseID:block:]
+ -[CADDatabaseSingleConnectionProvider performWithAllDatabasesWithConfiguration:options:block:]
+ -[CADDatabaseSingleConnectionProvider performWithConfiguration:options:databaseID:block:]
+ -[CADXPCImplementation(CADInternalOperationGroup) CADInternalGetMagicComposeRestrictedByMDM:]
+ -[ClientConnection _currentPriorityOptions]
+ -[ClientConnection withDatabaseID:options:perform:]
+ GCC_except_table72
+ _OBJC_CLASS_$_CalDeviceConfigurationReader
+ ___51-[ClientConnection withDatabaseID:options:perform:]_block_invoke
+ ___51-[ClientConnection withDatabaseID:options:perform:]_block_invoke_2
+ ___79-[CADDatabaseConnectionPool performWithConfiguration:options:databaseID:block:]_block_invoke
+ ___84-[CADDatabaseConnectionPool performWithAllDatabasesWithConfiguration:options:block:]_block_invoke
+ _objc_msgSend$_currentPriorityOptions
+ _objc_msgSend$isMagicComposeRestrictedByMDM
+ _objc_msgSend$performWithAllDatabasesWithConfiguration:options:block:
+ _objc_msgSend$performWithConfiguration:options:databaseID:block:
+ _objc_msgSend$withDatabaseID:options:perform:
- -[CADDatabaseConnectionPool performWithAllDatabasesWithConfiguration:priority:block:]
- -[CADDatabaseConnectionPool performWithConfiguration:priority:databaseID:block:]
- -[CADDatabaseSingleConnectionProvider performWithAllDatabasesWithConfiguration:priority:block:]
- -[CADDatabaseSingleConnectionProvider performWithConfiguration:priority:databaseID:block:]
- -[ClientConnection _currentPriority]
- ___43-[ClientConnection withDatabaseID:perform:]_block_invoke
- ___43-[ClientConnection withDatabaseID:perform:]_block_invoke_2
- ___80-[CADDatabaseConnectionPool performWithConfiguration:priority:databaseID:block:]_block_invoke
- ___85-[CADDatabaseConnectionPool performWithAllDatabasesWithConfiguration:priority:block:]_block_invoke
- _objc_msgSend$_currentPriority
- _objc_msgSend$performWithAllDatabasesWithConfiguration:priority:block:
- _objc_msgSend$performWithConfiguration:priority:databaseID:block:

```
