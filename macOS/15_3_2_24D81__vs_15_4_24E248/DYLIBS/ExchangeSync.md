## ExchangeSync

> `/System/Library/PrivateFrameworks/ExchangeSync.framework/Versions/A/ExchangeSync`

```diff

 2060.20.1.0.0
-  __TEXT.__text: 0x7820c
+  __TEXT.__text: 0x78198
   __TEXT.__auth_stubs: 0x7c0
-  __TEXT.__objc_methlist: 0x5924
+  __TEXT.__objc_methlist: 0x5f3c
   __TEXT.__const: 0x458
   __TEXT.__gcc_except_tab: 0xfd8
   __TEXT.__cstring: 0x653e
   __TEXT.__oslogstring: 0x668e
-  __TEXT.__unwind_info: 0x1568
+  __TEXT.__unwind_info: 0x1600
   __TEXT.__objc_classname: 0xaac
   __TEXT.__objc_methname: 0x10ce2
   __TEXT.__objc_methtype: 0x141c

   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3b38
+  __DATA_CONST.__objc_selrefs: 0x3bc0
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x1f0
   __DATA_CONST.__objc_arraydata: 0x20
   __AUTH_CONST.__auth_got: 0x3f0
   __AUTH_CONST.__const: 0x1070
   __AUTH_CONST.__cfstring: 0x47c0
-  __AUTH_CONST.__objc_const: 0xbde0
+  __AUTH_CONST.__objc_const: 0xb2a8
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x1c20
   __DATA.__objc_ivar: 0x75c

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprequelite.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 0970D56A-993B-3D2B-AC2D-10F540D63942
-  Functions: 2370
-  Symbols:   6147
+  UUID: 1A2ABC08-F567-3CDB-A459-E76F176B03F2
+  Functions: 2404
+  Symbols:   6183
   CStrings:  4697
 
Symbols:
+ +[EWSAttachmentManager log].cold.1
+ +[EXSAccount log].cold.1
+ +[EXSAccountAuthUpgrader log].cold.1
+ +[EXSAccountManager dataclassesToWatch].cold.1
+ +[EXSAccountManager log].cold.1
+ +[EXSAttachment log].cold.1
+ +[EXSBaseProperties exsUTCCalendar].cold.1
+ +[EXSBaseProperties log].cold.1
+ +[EXSChangeItem log].cold.1
+ +[EXSDataConsumerPlugin log].cold.1
+ +[EXSEWSAddDelegateOperation log].cold.1
+ +[EXSEWSGetAttachmentOperation log].cold.1
+ +[EXSEWSGetDelegateFolderPermissionsOperation log].cold.1
+ +[EXSEWSGetGrantedDelegatesOperation log].cold.1
+ +[EXSEWSMoveFolderOperation log].cold.1
+ +[EXSEWSOperation log].cold.1
+ +[EXSEWSProtocolSubscription log].cold.1
+ +[EXSEWSRemoveDelegateOperation log].cold.1
+ +[EXSEWSSearchDirectoryOperation log].cold.1
+ +[EXSEWSSyncProtocol accountGenericLog].cold.1
+ +[EXSEWSUpdateDelegatePermissionsOperation log].cold.1
+ +[EXSEWSUpdateFolderOperation log].cold.1
+ +[EXSGlobalDataManager log].cold.1
+ +[EXSGraphAddFolderOperation log].cold.1
+ +[EXSGraphOperation log].cold.1
+ +[EXSGraphSyncProtocol log].cold.1
+ +[EXSIDNADecoder posixLocale].cold.1
+ +[EXSIDNAEncoder unsafeDomainNameCharacterSet].cold.1
+ +[EXSLogging timeIntervalBetweenMachStartTime:andMachEndTime:].cold.1
+ +[EXSMain log].cold.1
+ +[EXSMaintenanceActivity log].cold.1
+ +[EXSNetworkController log].cold.1
+ +[EXSNotificationController log].cold.1
+ +[EXSPersonaPersistenceLayoutManager log].cold.1
+ +[EXSProtocolSubscription log].cold.1
+ +[EXSSyncEngine log].cold.1
+ +[EXSSyncEngineInstance log].cold.1
+ +[EXSXPCInterfaceImplementation log].cold.1
+ +[EXSXPCServiceDelegate log].cold.1
+ -[EXSEWSGetMeetingRequestItemsOperation findItemsResponseShape].cold.1
+ -[EXSSyncEngine loadDataConsumerPlugins:].cold.1
+ EXSIDNALog.cold.1
+ _stringByApplyingIDNATranslationWithRange.cold.2
+ machTimebaseForLiveMachine.cold.1
- _OUTLINED_FUNCTION_10
- _OUTLINED_FUNCTION_11
- _OUTLINED_FUNCTION_9

```
