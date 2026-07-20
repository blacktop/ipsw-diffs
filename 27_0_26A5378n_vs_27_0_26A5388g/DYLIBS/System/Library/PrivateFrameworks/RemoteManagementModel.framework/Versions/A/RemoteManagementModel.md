## RemoteManagementModel

> `/System/Library/PrivateFrameworks/RemoteManagementModel.framework/Versions/A/RemoteManagementModel`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_arrayobj`
- `__DATA.__data`
- `__DATA_DIRTY.__data`

```diff

-624.0.8.0.0
-  __TEXT.__text: 0x5b3b8
-  __TEXT.__objc_methlist: 0x81a4
+624.0.10.0.0
+  __TEXT.__text: 0x5c540
+  __TEXT.__objc_methlist: 0x8394
   __TEXT.__const: 0x70
-  __TEXT.__cstring: 0x4a22
+  __TEXT.__cstring: 0x4b85
   __TEXT.__oslogstring: 0x5dc
-  __TEXT.__unwind_info: 0x14a0
+  __TEXT.__unwind_info: 0x14d0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x830
-  __DATA_CONST.__objc_classlist: 0x530
+  __DATA_CONST.__objc_classlist: 0x540
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x21f8
-  __DATA_CONST.__objc_superrefs: 0x420
+  __DATA_CONST.__objc_selrefs: 0x2290
+  __DATA_CONST.__objc_superrefs: 0x430
   __DATA_CONST.__objc_arraydata: 0x32f0
-  __DATA_CONST.__got: 0x5f8
+  __DATA_CONST.__got: 0x608
   __AUTH_CONST.__const: 0xae0
-  __AUTH_CONST.__cfstring: 0x7340
-  __AUTH_CONST.__objc_const: 0xecb8
+  __AUTH_CONST.__cfstring: 0x7540
+  __AUTH_CONST.__objc_const: 0xf068
   __AUTH_CONST.__objc_arrayobj: 0x4fb0
-  __AUTH_CONST.__objc_intobj: 0x2a48
+  __AUTH_CONST.__objc_intobj: 0x2a60
   __AUTH_CONST.__auth_got: 0xf8
-  __AUTH.__objc_data: 0x1298
-  __DATA.__objc_ivar: 0x874
+  __AUTH.__objc_data: 0xa0
+  __DATA.__objc_ivar: 0x8a4
   __DATA.__data: 0x1e0
   __DATA.__bss: 0x1b0
-  __DATA_DIRTY.__objc_data: 0x2148
+  __DATA_DIRTY.__objc_data: 0x33e0
   __DATA_DIRTY.__data: 0x10
   __DATA_DIRTY.__bss: 0x68
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /System/Library/PrivateFrameworks/DMCUtilities.framework/Versions/A/DMCUtilities
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2691
-  Symbols:   5790
-  CStrings:  983
+  Functions: 2731
+  Symbols:   5876
+  CStrings:  999
 
Symbols:
+ +[RMModelAccountCalDAVDeclaration buildWithIdentifier:visibleName:hostName:port:path:authenticationCredentialsAssetReference:VPNUUID:]
+ +[RMModelAccountExchangeDeclaration buildWithIdentifier:visibleName:enabledProtocolTypes:userIdentityAssetReference:hostName:port:path:externalHostName:externalPort:externalPath:graphHostName:oAuth:authenticationCredentialsAssetReference:authenticationIdentityAssetReference:SMIME:allowMove:allowAppSheet:allowMailRecentsSyncing:enableMailDrop:mailNumberOfPastDaysToSync:mailServiceActive:lockMailService:contactsServiceActive:lockContactsService:calendarServiceActive:lockCalendarService:remindersServiceActive:lockRemindersService:notesServiceActive:lockNotesService:VPNUUID:communicationServiceRules:]
+ +[RMModelAccountExchangeDeclaration_CommunicationServiceRules allowedPayloadKeys]
+ +[RMModelAccountExchangeDeclaration_CommunicationServiceRules buildRequiredOnly]
+ +[RMModelAccountExchangeDeclaration_CommunicationServiceRules buildWithDefaultServiceHandlers:]
+ +[RMModelAccountExchangeDeclaration_CommunicationServiceRulesDefaultServiceHandlers allowedPayloadKeys]
+ +[RMModelAccountExchangeDeclaration_CommunicationServiceRulesDefaultServiceHandlers buildRequiredOnly]
+ +[RMModelAccountExchangeDeclaration_CommunicationServiceRulesDefaultServiceHandlers buildWithAudioCall:]
+ +[RMModelAccountLDAPDeclaration buildWithIdentifier:visibleName:hostName:port:authenticationCredentialsAssetReference:searchSettings:VPNUUID:]
+ +[RMModelAccountSubscribedCalendarDeclaration buildWithIdentifier:visibleName:calendarURL:authenticationCredentialsAssetReference:VPNUUID:]
+ -[RMModelAccountCalDAVDeclaration payloadVPNUUID]
+ -[RMModelAccountCalDAVDeclaration setPayloadVPNUUID:]
+ -[RMModelAccountExchangeDeclaration payloadAllowAppSheet]
+ -[RMModelAccountExchangeDeclaration payloadAllowMailRecentsSyncing]
+ -[RMModelAccountExchangeDeclaration payloadAllowMove]
+ -[RMModelAccountExchangeDeclaration payloadCommunicationServiceRules]
+ -[RMModelAccountExchangeDeclaration payloadEnableMailDrop]
+ -[RMModelAccountExchangeDeclaration payloadMailNumberOfPastDaysToSync]
+ -[RMModelAccountExchangeDeclaration payloadVPNUUID]
+ -[RMModelAccountExchangeDeclaration setPayloadAllowAppSheet:]
+ -[RMModelAccountExchangeDeclaration setPayloadAllowMailRecentsSyncing:]
+ -[RMModelAccountExchangeDeclaration setPayloadAllowMove:]
+ -[RMModelAccountExchangeDeclaration setPayloadCommunicationServiceRules:]
+ -[RMModelAccountExchangeDeclaration setPayloadEnableMailDrop:]
+ -[RMModelAccountExchangeDeclaration setPayloadMailNumberOfPastDaysToSync:]
+ -[RMModelAccountExchangeDeclaration setPayloadVPNUUID:]
+ -[RMModelAccountExchangeDeclaration_CommunicationServiceRules .cxx_destruct]
+ -[RMModelAccountExchangeDeclaration_CommunicationServiceRules copyWithZone:]
+ -[RMModelAccountExchangeDeclaration_CommunicationServiceRules loadFromDictionary:serializationType:error:]
+ -[RMModelAccountExchangeDeclaration_CommunicationServiceRules payloadDefaultServiceHandlers]
+ -[RMModelAccountExchangeDeclaration_CommunicationServiceRules serializeWithType:]
+ -[RMModelAccountExchangeDeclaration_CommunicationServiceRules setPayloadDefaultServiceHandlers:]
+ -[RMModelAccountExchangeDeclaration_CommunicationServiceRulesDefaultServiceHandlers .cxx_destruct]
+ -[RMModelAccountExchangeDeclaration_CommunicationServiceRulesDefaultServiceHandlers copyWithZone:]
+ -[RMModelAccountExchangeDeclaration_CommunicationServiceRulesDefaultServiceHandlers loadFromDictionary:serializationType:error:]
+ -[RMModelAccountExchangeDeclaration_CommunicationServiceRulesDefaultServiceHandlers payloadAudioCall]
+ -[RMModelAccountExchangeDeclaration_CommunicationServiceRulesDefaultServiceHandlers serializeWithType:]
+ -[RMModelAccountExchangeDeclaration_CommunicationServiceRulesDefaultServiceHandlers setPayloadAudioCall:]
+ -[RMModelAccountLDAPDeclaration payloadVPNUUID]
+ -[RMModelAccountLDAPDeclaration setPayloadVPNUUID:]
+ -[RMModelAccountSubscribedCalendarDeclaration payloadVPNUUID]
+ -[RMModelAccountSubscribedCalendarDeclaration setPayloadVPNUUID:]
+ OBJC_IVAR_$_RMModelAccountCalDAVDeclaration._payloadVPNUUID
+ OBJC_IVAR_$_RMModelAccountExchangeDeclaration._payloadAllowAppSheet
+ OBJC_IVAR_$_RMModelAccountExchangeDeclaration._payloadAllowMailRecentsSyncing
+ OBJC_IVAR_$_RMModelAccountExchangeDeclaration._payloadAllowMove
+ OBJC_IVAR_$_RMModelAccountExchangeDeclaration._payloadCommunicationServiceRules
+ OBJC_IVAR_$_RMModelAccountExchangeDeclaration._payloadEnableMailDrop
+ OBJC_IVAR_$_RMModelAccountExchangeDeclaration._payloadMailNumberOfPastDaysToSync
+ OBJC_IVAR_$_RMModelAccountExchangeDeclaration._payloadVPNUUID
+ OBJC_IVAR_$_RMModelAccountExchangeDeclaration_CommunicationServiceRules._payloadDefaultServiceHandlers
+ OBJC_IVAR_$_RMModelAccountExchangeDeclaration_CommunicationServiceRulesDefaultServiceHandlers._payloadAudioCall
+ OBJC_IVAR_$_RMModelAccountLDAPDeclaration._payloadVPNUUID
+ OBJC_IVAR_$_RMModelAccountSubscribedCalendarDeclaration._payloadVPNUUID
+ _OBJC_CLASS_$_RMModelAccountExchangeDeclaration_CommunicationServiceRules
+ _OBJC_CLASS_$_RMModelAccountExchangeDeclaration_CommunicationServiceRulesDefaultServiceHandlers
+ _OBJC_METACLASS_$_RMModelAccountExchangeDeclaration_CommunicationServiceRules
+ _OBJC_METACLASS_$_RMModelAccountExchangeDeclaration_CommunicationServiceRulesDefaultServiceHandlers
+ __OBJC_$_CLASS_METHODS_RMModelAccountExchangeDeclaration_CommunicationServiceRules
+ __OBJC_$_CLASS_METHODS_RMModelAccountExchangeDeclaration_CommunicationServiceRulesDefaultServiceHandlers
+ __OBJC_$_CLASS_PROP_LIST_RMModelAccountExchangeDeclaration_CommunicationServiceRules
+ __OBJC_$_CLASS_PROP_LIST_RMModelAccountExchangeDeclaration_CommunicationServiceRulesDefaultServiceHandlers
+ __OBJC_$_INSTANCE_METHODS_RMModelAccountExchangeDeclaration_CommunicationServiceRules
+ __OBJC_$_INSTANCE_METHODS_RMModelAccountExchangeDeclaration_CommunicationServiceRulesDefaultServiceHandlers
+ __OBJC_$_INSTANCE_VARIABLES_RMModelAccountExchangeDeclaration_CommunicationServiceRules
+ __OBJC_$_INSTANCE_VARIABLES_RMModelAccountExchangeDeclaration_CommunicationServiceRulesDefaultServiceHandlers
+ __OBJC_$_PROP_LIST_RMModelAccountExchangeDeclaration_CommunicationServiceRules
+ __OBJC_$_PROP_LIST_RMModelAccountExchangeDeclaration_CommunicationServiceRulesDefaultServiceHandlers
+ __OBJC_CLASS_RO_$_RMModelAccountExchangeDeclaration_CommunicationServiceRules
+ __OBJC_CLASS_RO_$_RMModelAccountExchangeDeclaration_CommunicationServiceRulesDefaultServiceHandlers
+ __OBJC_METACLASS_RO_$_RMModelAccountExchangeDeclaration_CommunicationServiceRules
+ __OBJC_METACLASS_RO_$_RMModelAccountExchangeDeclaration_CommunicationServiceRulesDefaultServiceHandlers
+ ___62-[RMModelAccountExchangeDeclaration serializePayloadWithType:]_block_invoke_4
+ ___81-[RMModelAccountExchangeDeclaration_CommunicationServiceRules serializeWithType:]_block_invoke
+ _objc_msgSend$payloadAllowAppSheet
+ _objc_msgSend$payloadAllowMailRecentsSyncing
+ _objc_msgSend$payloadAllowMove
+ _objc_msgSend$payloadAudioCall
+ _objc_msgSend$payloadCommunicationServiceRules
+ _objc_msgSend$payloadDefaultServiceHandlers
+ _objc_msgSend$payloadEnableMailDrop
+ _objc_msgSend$payloadMailNumberOfPastDaysToSync
+ _objc_msgSend$setPayloadAllowAppSheet:
+ _objc_msgSend$setPayloadAllowMailRecentsSyncing:
+ _objc_msgSend$setPayloadAllowMove:
+ _objc_msgSend$setPayloadAudioCall:
+ _objc_msgSend$setPayloadCommunicationServiceRules:
+ _objc_msgSend$setPayloadDefaultServiceHandlers:
+ _objc_msgSend$setPayloadEnableMailDrop:
+ _objc_msgSend$setPayloadMailNumberOfPastDaysToSync:
- +[RMModelAccountCalDAVDeclaration buildWithIdentifier:visibleName:hostName:port:path:authenticationCredentialsAssetReference:]
- +[RMModelAccountExchangeDeclaration buildWithIdentifier:visibleName:enabledProtocolTypes:userIdentityAssetReference:hostName:port:path:externalHostName:externalPort:externalPath:graphHostName:oAuth:authenticationCredentialsAssetReference:authenticationIdentityAssetReference:SMIME:mailServiceActive:lockMailService:contactsServiceActive:lockContactsService:calendarServiceActive:lockCalendarService:remindersServiceActive:lockRemindersService:notesServiceActive:lockNotesService:]
- +[RMModelAccountLDAPDeclaration buildWithIdentifier:visibleName:hostName:port:authenticationCredentialsAssetReference:searchSettings:]
- +[RMModelAccountSubscribedCalendarDeclaration buildWithIdentifier:visibleName:calendarURL:authenticationCredentialsAssetReference:]
CStrings:
+ "AllowAppSheet"
+ "AllowMailRecentsSyncing"
+ "AllowMove"
+ "AudioCall"
+ "CommunicationServiceRules"
+ "DefaultServiceHandlers"
+ "EnableMailDrop"
+ "MailNumberOfPastDaysToSync"
+ "payloadAllowAppSheet"
+ "payloadAllowMailRecentsSyncing"
+ "payloadAllowMove"
+ "payloadAudioCall"
+ "payloadCommunicationServiceRules"
+ "payloadDefaultServiceHandlers"
+ "payloadEnableMailDrop"
+ "payloadMailNumberOfPastDaysToSync"
```
