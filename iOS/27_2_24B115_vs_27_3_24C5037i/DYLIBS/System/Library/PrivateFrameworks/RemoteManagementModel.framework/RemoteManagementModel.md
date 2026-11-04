## RemoteManagementModel

> `/System/Library/PrivateFrameworks/RemoteManagementModel.framework/RemoteManagementModel`

```diff

-624.40.16.0.0
-  __TEXT.__text: 0x56134
-  __TEXT.__objc_methlist: 0x8684
+624.60.9.0.0
+  __TEXT.__text: 0x567a0
+  __TEXT.__objc_methlist: 0x874c
   __TEXT.__const: 0x68
-  __TEXT.__cstring: 0x4ba4
+  __TEXT.__cstring: 0x4c44
   __TEXT.__oslogstring: 0x5dc
-  __TEXT.__unwind_info: 0x1998
+  __TEXT.__unwind_info: 0x19b8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x890
-  __DATA_CONST.__objc_classlist: 0x558
+  __DATA_CONST.__const: 0x938
+  __DATA_CONST.__objc_classlist: 0x560
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x22c8
-  __DATA_CONST.__objc_superrefs: 0x450
+  __DATA_CONST.__objc_selrefs: 0x2310
+  __DATA_CONST.__objc_superrefs: 0x458
   __DATA_CONST.__objc_arraydata: 0x3220
-  __DATA_CONST.__got: 0x628
+  __DATA_CONST.__got: 0x630
   __AUTH_CONST.__const: 0xa80
-  __AUTH_CONST.__cfstring: 0x75e0
-  __AUTH_CONST.__objc_const: 0xf588
+  __AUTH_CONST.__cfstring: 0x77a0
+  __AUTH_CONST.__objc_const: 0xf700
   __AUTH_CONST.__objc_arrayobj: 0x4e00
   __AUTH_CONST.__objc_intobj: 0x29d0
   __AUTH_CONST.__auth_got: 0x1f0
-  __AUTH.__objc_data: 0x1e0
-  __DATA.__objc_ivar: 0x8e0
+  __AUTH.__objc_data: 0x230
+  __DATA.__objc_ivar: 0x8f0
   __DATA.__data: 0x1e0
   __DATA_DIRTY.__objc_data: 0x3390
   __DATA_DIRTY.__data: 0x10

   - /System/Library/PrivateFrameworks/DMCUtilities.framework/DMCUtilities
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2790
-  Symbols:   5150
-  CStrings:  1003
+  Functions: 2806
+  Symbols:   5200
+  CStrings:  1017
 
Symbols:
+ +[RMModelAccountExchangeDeclaration buildWithIdentifier:visibleName:enabledProtocolTypes:userIdentityAssetReference:hostName:port:path:externalHostName:externalPort:externalPath:oAuth:authenticationCredentialsAssetReference:authenticationIdentityAssetReference:SMIME:allowMove:allowAppSheet:allowMailRecentsSyncing:enableMailDrop:mailNumberOfPastDaysToSync:mailServiceActive:lockMailService:contactsServiceActive:lockContactsService:calendarServiceActive:lockCalendarService:remindersServiceActive:lockRemindersService:notesServiceActive:lockNotesService:VPNUUID:communicationServiceRules:]
+ +[RMModelStatusAccountListExchange buildWithIdentifier:removed:declarationIdentifier:visibleName:protocolType:graphMigrationState:graphSupport:hostname:port:username:isMailEnabled:areCalendarsEnabled:areContactsEnabled:areNotesEnabled:areRemindersEnabled:]
+ +[RMModelStatusAccountListExchange_GraphMigrationState allowedStatusKeys]
+ +[RMModelStatusAccountListExchange_GraphMigrationState buildRequiredOnly]
+ +[RMModelStatusAccountListExchange_GraphMigrationState buildWithMail:contacts:other:]
+ -[RMModelStatusAccountListExchange setStatusGraphMigrationState:]
+ -[RMModelStatusAccountListExchange setStatusGraphSupport:]
+ -[RMModelStatusAccountListExchange statusGraphMigrationState]
+ -[RMModelStatusAccountListExchange statusGraphSupport]
+ -[RMModelStatusAccountListExchange_GraphMigrationState .cxx_destruct]
+ -[RMModelStatusAccountListExchange_GraphMigrationState copyWithZone:]
+ -[RMModelStatusAccountListExchange_GraphMigrationState loadFromDictionary:serializationType:error:]
+ -[RMModelStatusAccountListExchange_GraphMigrationState serializeWithType:]
+ -[RMModelStatusAccountListExchange_GraphMigrationState setStatusContacts:]
+ -[RMModelStatusAccountListExchange_GraphMigrationState setStatusMail:]
+ -[RMModelStatusAccountListExchange_GraphMigrationState setStatusOther:]
+ -[RMModelStatusAccountListExchange_GraphMigrationState statusContacts]
+ -[RMModelStatusAccountListExchange_GraphMigrationState statusMail]
+ -[RMModelStatusAccountListExchange_GraphMigrationState statusOther]
+ _OBJC_CLASS_$_RMModelStatusAccountListExchange_GraphMigrationState
+ _OBJC_IVAR_$_RMModelStatusAccountListExchange._statusGraphMigrationState
+ _OBJC_IVAR_$_RMModelStatusAccountListExchange._statusGraphSupport
+ _OBJC_IVAR_$_RMModelStatusAccountListExchange_GraphMigrationState._statusContacts
+ _OBJC_IVAR_$_RMModelStatusAccountListExchange_GraphMigrationState._statusMail
+ _OBJC_IVAR_$_RMModelStatusAccountListExchange_GraphMigrationState._statusOther
+ _OBJC_METACLASS_$_RMModelStatusAccountListExchange_GraphMigrationState
+ _RMModelStatusAccountListExchange_GraphMigrationState_Contacts_converting
+ _RMModelStatusAccountListExchange_GraphMigrationState_Contacts_eligible
+ _RMModelStatusAccountListExchange_GraphMigrationState_Contacts_failed
+ _RMModelStatusAccountListExchange_GraphMigrationState_Contacts_migrated
+ _RMModelStatusAccountListExchange_GraphMigrationState_Contacts_skipped
+ _RMModelStatusAccountListExchange_GraphMigrationState_Contacts_syncing
+ _RMModelStatusAccountListExchange_GraphMigrationState_Mail_converting
+ _RMModelStatusAccountListExchange_GraphMigrationState_Mail_eligible
+ _RMModelStatusAccountListExchange_GraphMigrationState_Mail_failed
+ _RMModelStatusAccountListExchange_GraphMigrationState_Mail_migrated
+ _RMModelStatusAccountListExchange_GraphMigrationState_Mail_skipped
+ _RMModelStatusAccountListExchange_GraphMigrationState_Mail_syncing
+ _RMModelStatusAccountListExchange_GraphMigrationState_Other_converting
+ _RMModelStatusAccountListExchange_GraphMigrationState_Other_eligible
+ _RMModelStatusAccountListExchange_GraphMigrationState_Other_failed
+ _RMModelStatusAccountListExchange_GraphMigrationState_Other_migrated
+ _RMModelStatusAccountListExchange_GraphMigrationState_Other_skipped
+ _RMModelStatusAccountListExchange_GraphMigrationState_Other_syncing
+ _RMModelStatusAccountListExchange_GraphSupport_supported
+ _RMModelStatusAccountListExchange_GraphSupport_unknown
+ _RMModelStatusAccountListExchange_GraphSupport_unsupported
+ __OBJC_$_CLASS_METHODS_RMModelStatusAccountListExchange_GraphMigrationState
+ __OBJC_$_CLASS_PROP_LIST_RMModelStatusAccountListExchange_GraphMigrationState
+ __OBJC_$_INSTANCE_METHODS_RMModelStatusAccountListExchange_GraphMigrationState
+ __OBJC_$_INSTANCE_VARIABLES_RMModelStatusAccountListExchange_GraphMigrationState
+ __OBJC_$_PROP_LIST_RMModelStatusAccountListExchange_GraphMigrationState
+ __OBJC_CLASS_RO_$_RMModelStatusAccountListExchange_GraphMigrationState
+ __OBJC_METACLASS_RO_$_RMModelStatusAccountListExchange_GraphMigrationState
+ ___61-[RMModelStatusAccountListExchange serializePayloadWithType:]_block_invoke
- +[RMModelAccountExchangeDeclaration buildWithIdentifier:visibleName:enabledProtocolTypes:userIdentityAssetReference:hostName:port:path:externalHostName:externalPort:externalPath:graphHostName:oAuth:authenticationCredentialsAssetReference:authenticationIdentityAssetReference:SMIME:allowMove:allowAppSheet:allowMailRecentsSyncing:enableMailDrop:mailNumberOfPastDaysToSync:mailServiceActive:lockMailService:contactsServiceActive:lockContactsService:calendarServiceActive:lockCalendarService:remindersServiceActive:lockRemindersService:notesServiceActive:lockNotesService:VPNUUID:communicationServiceRules:]
- +[RMModelStatusAccountListExchange buildWithIdentifier:removed:declarationIdentifier:visibleName:protocolType:hostname:port:username:isMailEnabled:areCalendarsEnabled:areContactsEnabled:areNotesEnabled:areRemindersEnabled:]
- -[RMModelAccountExchangeDeclaration payloadGraphHostName]
- -[RMModelAccountExchangeDeclaration setPayloadGraphHostName:]
- _OBJC_IVAR_$_RMModelAccountExchangeDeclaration._payloadGraphHostName
CStrings:
+ "contacts"
+ "converting"
+ "eligible"
+ "graph-migration-state"
+ "graph-support"
+ "mail"
+ "migrated"
+ "other"
+ "skipped"
+ "statusContacts"
+ "statusGraphMigrationState"
+ "statusGraphSupport"
+ "statusMail"
+ "statusOther"
+ "supported"
+ "syncing"
- "GraphHostName"
- "payloadGraphHostName"
```
