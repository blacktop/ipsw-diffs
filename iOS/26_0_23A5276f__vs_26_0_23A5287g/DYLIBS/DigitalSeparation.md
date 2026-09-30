## DigitalSeparation

> `/System/Library/PrivateFrameworks/DigitalSeparation.framework/DigitalSeparation`

```diff

-565.0.1.0.0
-  __TEXT.__text: 0x28f6c
-  __TEXT.__auth_stubs: 0x680
-  __TEXT.__objc_methlist: 0x19bc
-  __TEXT.__cstring: 0x12d9
-  __TEXT.__const: 0x98
-  __TEXT.__gcc_except_tab: 0x11ac
-  __TEXT.__oslogstring: 0x1f61
+574.0.0.0.0
+  __TEXT.__text: 0x2b2e4
+  __TEXT.__auth_stubs: 0x6d0
+  __TEXT.__objc_methlist: 0x1dc4
+  __TEXT.__cstring: 0x13b0
+  __TEXT.__const: 0xb0
+  __TEXT.__gcc_except_tab: 0xd40
+  __TEXT.__oslogstring: 0x243a
   __TEXT.__dlopen_cstrs: 0x68
-  __TEXT.__unwind_info: 0x790
-  __TEXT.__objc_classname: 0x228
-  __TEXT.__objc_methname: 0x458d
-  __TEXT.__objc_methtype: 0x971
-  __TEXT.__objc_stubs: 0x3cc0
-  __DATA_CONST.__got: 0x3b8
-  __DATA_CONST.__const: 0xc68
-  __DATA_CONST.__objc_classlist: 0xc0
+  __TEXT.__unwind_info: 0x898
+  __TEXT.__objc_classname: 0x2a1
+  __TEXT.__objc_methname: 0x4a26
+  __TEXT.__objc_methtype: 0xa50
+  __TEXT.__objc_stubs: 0x4100
+  __DATA_CONST.__got: 0x3f8
+  __DATA_CONST.__const: 0xca0
+  __DATA_CONST.__objc_classlist: 0xd8
   __DATA_CONST.__objc_catlist: 0x40
-  __DATA_CONST.__objc_protolist: 0x48
+  __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1270
-  __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x70
-  __AUTH_CONST.__auth_got: 0x350
-  __AUTH_CONST.__const: 0x200
-  __AUTH_CONST.__cfstring: 0x13e0
-  __AUTH_CONST.__objc_const: 0x38f0
-  __AUTH.__objc_data: 0x410
-  __DATA.__objc_ivar: 0x148
-  __DATA.__data: 0x368
-  __DATA.__bss: 0x68
+  __DATA_CONST.__objc_selrefs: 0x13e8
+  __DATA_CONST.__objc_protorefs: 0x20
+  __DATA_CONST.__objc_superrefs: 0x88
+  __AUTH_CONST.__auth_got: 0x378
+  __AUTH_CONST.__const: 0x280
+  __AUTH_CONST.__cfstring: 0x1500
+  __AUTH_CONST.__objc_const: 0x4290
+  __AUTH_CONST.__objc_intobj: 0x30
+  __AUTH.__objc_data: 0x500
+  __DATA.__objc_ivar: 0x17c
+  __DATA.__data: 0x4e8
+  __DATA.__bss: 0x88
   __DATA_DIRTY.__objc_data: 0x370
   __DATA_DIRTY.__bss: 0xa0
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4B66B9BD-945D-3B3D-834C-C47B1277C524
-  Functions: 708
-  Symbols:   2723
-  CStrings:  1407
+  UUID: EEB41300-CD95-326D-ADA1-AD2A1494AA2D
+  Functions: 803
+  Symbols:   3069
+  CStrings:  1524
 
Symbols:
+ +[DSContactProvider defaultProvider]
+ +[DSContactProvider defaultProvider].cold.1
+ +[DSIdentity supportsSecureCoding]
+ +[DSXPCParticipant participants:]
+ +[DSXPCParticipant supportsSecureCoding]
+ +[DSXPCSharedResource supportsSecureCoding]
+ +[DSXPCSharingPermissions sharedInstance]
+ +[DSXPCSharingPermissions sharedInstance].cold.1
+ -[DSContactProvider .cxx_destruct]
+ -[DSContactProvider initWithStore:]
+ -[DSContactProvider init]
+ -[DSContactProvider keysToFetch]
+ -[DSContactProvider sanitizeContacts:]
+ -[DSContactProvider setStore:]
+ -[DSContactProvider store]
+ -[DSContactProvider unifiedContactInDictionary:forIdentity:]
+ -[DSContactProvider unifiedContactInDictionary:forIdentity:].cold.1
+ -[DSContactProvider unifiedContactsDictionaryForHandleStrings:]
+ -[DSContactProvider unifiedContactsDictionaryForIdentities:]
+ -[DSContactProvider unifiedContactsDictionaryForIdentities:].cold.1
+ -[DSContactProvider unifiedContactsForContactIdentifiers:]
+ -[DSIdentity copyWithZone:]
+ -[DSIdentity ds_identifier]
+ -[DSIdentity email]
+ -[DSIdentity encodeWithCoder:]
+ -[DSIdentity initWithCoder:]
+ -[DSIdentity initWithIdentity:]
+ -[DSIdentity isLikeIdentity:]
+ -[DSIdentity name]
+ -[DSIdentity phone]
+ -[DSIdentity setEmail:]
+ -[DSIdentity setName:]
+ -[DSIdentity setPhone:]
+ -[DSMe initWithMeIdentifier:emails:phoneNumbers:]
+ -[DSSharingPerson initWithSource:sharedResource:participant:deviceOwnerRole:contact:]
+ -[DSSharingPerson initWithSource:sharedResource:unknownParticipant:deviceOwnerRole:]
+ -[DSSharingPerson init]
+ -[DSSharingPerson updateContactFromIdentity:]
+ -[DSSharingPerson updateContactFromIdentity:].cold.1
+ -[DSSharingPerson updateContactFromIdentity:].cold.2
+ -[DSSharingPerson updateContactFromIdentity:].cold.3
+ -[DSXPCParticipant .cxx_destruct]
+ -[DSXPCParticipant encodeWithCoder:]
+ -[DSXPCParticipant identity]
+ -[DSXPCParticipant initWithCoder:]
+ -[DSXPCParticipant initWithIdentity:role:permission:]
+ -[DSXPCParticipant initWithParticipant:]
+ -[DSXPCParticipant isEqual:]
+ -[DSXPCParticipant participantIdentity]
+ -[DSXPCParticipant participationPermission]
+ -[DSXPCParticipant participationRole]
+ -[DSXPCParticipant permission]
+ -[DSXPCParticipant role]
+ -[DSXPCParticipant setParticipantIdentity:]
+ -[DSXPCParticipant setParticipationPermission:]
+ -[DSXPCParticipant setParticipationRole:]
+ -[DSXPCSharedResource .cxx_destruct]
+ -[DSXPCSharedResource access]
+ -[DSXPCSharedResource detail]
+ -[DSXPCSharedResource displayDetail]
+ -[DSXPCSharedResource displayName]
+ -[DSXPCSharedResource encodeWithCoder:]
+ -[DSXPCSharedResource initPrivateResourceWithName:detail:participants:]
+ -[DSXPCSharedResource initWithCoder:]
+ -[DSXPCSharedResource initWithResource:]
+ -[DSXPCSharedResource name]
+ -[DSXPCSharedResource participantArray]
+ -[DSXPCSharedResource participants]
+ -[DSXPCSharedResource participationAccess]
+ -[DSXPCSharedResource resourceVisibility]
+ -[DSXPCSharedResource setAccess:]
+ -[DSXPCSharedResource setDetail:]
+ -[DSXPCSharedResource setName:]
+ -[DSXPCSharedResource setParticipantArray:]
+ -[DSXPCSharedResource setResourceVisibility:]
+ -[DSXPCSharedResource visibility]
+ -[DSXPCSharingPermissions _fetchSharingWithCompletion:]
+ -[DSXPCSharingPermissions _fetchSharingWithCompletion:].cold.1
+ -[DSXPCSharingPermissions addSharingPerson:participant:forSource:sharedResource:deviceOwnerRole:]
+ -[DSXPCSharingPermissions deviceOwnerRoleForSharedResource:]
+ -[DSXPCSharingPermissions makeSharingPeopleWithResources:]
+ -[DSXPCSharingPermissions makeSharingPeopleWithResources:].cold.1
+ -[DSXPCSharingPermissions makeSharingPeople]
+ -[DSXPCSharingPermissions me]
+ -[DSXPCSharingPermissions setDSMe:]
+ -[DSXPCSharingPermissions setMe:]
+ -[DSXPCSharingPermissions setSharedResourcesBySource:]
+ -[DSXPCSharingPermissions setSharing:]
+ -[DSXPCSharingPermissions sharedResourcesBySource]
+ -[DSXPCSharingPermissions sharingPeopleForContacts:]
+ -[DSXPCSharingPermissions sharingPeopleForContacts:].cold.1
+ -[DSXPCSharingPermissions sharingPeopleForIdentities:]
+ -[DSXPCSharingPerson addSource:sharedResource:participant:deviceOwnerRole:]
+ -[DSXPCSharingPerson alertTextForSource:]
+ -[DSXPCSharingPerson detailTextForSource:]
+ -[DSXPCSharingPerson displayGivenName]
+ -[DSXPCSharingPerson displayName].cold.1
+ -[DSXPCSharingPerson emailAddresses]
+ -[DSXPCSharingPerson initWithSource:sharedResource:participant:deviceOwnerRole:contact:]
+ -[DSXPCSharingPerson initWithSource:sharedResource:participant:deviceOwnerRole:unknownHandle:]
+ -[DSXPCSharingPerson init]
+ -[DSXPCSharingPerson isIdentity:]
+ -[DSXPCSharingPerson isIdentity:].cold.1
+ -[DSXPCSharingPerson isIdentity:].cold.2
+ -[DSXPCSharingPerson isLikeContact:].cold.1
+ -[DSXPCSharingPerson isMe:]
+ -[DSXPCSharingPerson names]
+ -[DSXPCSharingPerson participationForSources:]
+ -[DSXPCSharingPerson phoneNumbers]
+ -[DSXPCSharingPerson setEmailAddresses:]
+ -[DSXPCSharingPerson setNames:]
+ -[DSXPCSharingPerson setPhoneNumbers:]
+ -[DSXPCSharingPerson setShareDirectionByResource:]
+ -[DSXPCSharingPerson setShareDirectionBySourceName:]
+ -[DSXPCSharingPerson setSharedResourcesBySource:]
+ -[DSXPCSharingPerson setSources:]
+ -[DSXPCSharingPerson shareDirectionByResource]
+ -[DSXPCSharingPerson shareDirectionBySourceName]
+ -[DSXPCSharingPerson shareDirectionForSharedResource:]
+ -[DSXPCSharingPerson shareDirectionForSourceName:]
+ -[DSXPCSharingPerson sharedResourcesBySource]
+ -[DSXPCSharingPerson sharedResourcesForSourceName:]
+ -[DSXPCSharingPerson sortedSourceNames]
+ -[DSXPCSharingPerson sources]
+ -[DSXPCSharingPerson termsOfAddress]
+ -[DSXPCSharingPerson updateContactFromIdentity:]
+ -[DSXPCSharingPerson updateContactFromIdentity:].cold.1
+ -[DSXPCSharingPerson updateContactFromIdentity:].cold.2
+ -[DSXPCSharingPerson updateContactFromIdentity:].cold.3
+ -[DSXPCSharingPerson updateKnownEmailAddressesForParticipant:]
+ -[DSXPCSharingPerson updateKnownEmailAddressesForParticipant:].cold.1
+ -[DSXPCSharingPerson updateKnownNameForParticipant:]
+ -[DSXPCSharingPerson updateKnownNameForParticipant:].cold.1
+ -[DSXPCSharingPerson updateKnownNameForParticipant:].cold.2
+ -[DSXPCSharingPerson updateKnownPhoneNumbersForParticipant:]
+ -[DSXPCSharingPerson updateKnownPhoneNumbersForParticipant:].cold.1
+ -[DSXPCSharingPerson updateShareDirectionForParticipant:source:sharedResource:deviceOwnerRole:]
+ GCC_except_table27
+ GCC_except_table49
+ _OBJC_CLASS_$_CNContactFetchRequest
+ _OBJC_CLASS_$_CNMutableContact
+ _OBJC_CLASS_$_DSContactProvider
+ _OBJC_CLASS_$_DSXPCParticipant
+ _OBJC_CLASS_$_DSXPCSharedResource
+ _OBJC_CLASS_$_NSConstantIntegerNumber
+ _OBJC_CLASS_$_NSProcessInfo
+ _OBJC_IVAR_$_DSContactProvider._contactStoreWorkQueue
+ _OBJC_IVAR_$_DSContactProvider._store
+ _OBJC_IVAR_$_DSIdentity._email
+ _OBJC_IVAR_$_DSIdentity._name
+ _OBJC_IVAR_$_DSIdentity._phone
+ _OBJC_IVAR_$_DSXPCParticipant._participantIdentity
+ _OBJC_IVAR_$_DSXPCParticipant._participationPermission
+ _OBJC_IVAR_$_DSXPCParticipant._participationRole
+ _OBJC_IVAR_$_DSXPCSharedResource._access
+ _OBJC_IVAR_$_DSXPCSharedResource._detail
+ _OBJC_IVAR_$_DSXPCSharedResource._name
+ _OBJC_IVAR_$_DSXPCSharedResource._participantArray
+ _OBJC_IVAR_$_DSXPCSharedResource._resourceVisibility
+ _OBJC_IVAR_$_DSXPCSharingPermissions._dispatchGroup
+ _OBJC_IVAR_$_DSXPCSharingPermissions._me
+ _OBJC_IVAR_$_DSXPCSharingPermissions._permissionsLock
+ _OBJC_IVAR_$_DSXPCSharingPermissions._sharedResourcesBySource
+ _OBJC_IVAR_$_DSXPCSharingPerson._emailAddresses
+ _OBJC_IVAR_$_DSXPCSharingPerson._names
+ _OBJC_IVAR_$_DSXPCSharingPerson._phoneNumbers
+ _OBJC_IVAR_$_DSXPCSharingPerson._shareDirectionByResource
+ _OBJC_IVAR_$_DSXPCSharingPerson._shareDirectionBySourceName
+ _OBJC_IVAR_$_DSXPCSharingPerson._sharedResourcesBySource
+ _OBJC_IVAR_$_DSXPCSharingPerson._sources
+ _OBJC_METACLASS_$_DSContactProvider
+ _OBJC_METACLASS_$_DSXPCParticipant
+ _OBJC_METACLASS_$_DSXPCSharedResource
+ __OBJC_$_CLASS_METHODS_DSContactProvider
+ __OBJC_$_CLASS_METHODS_DSIdentity
+ __OBJC_$_CLASS_METHODS_DSXPCParticipant
+ __OBJC_$_CLASS_METHODS_DSXPCSharedResource
+ __OBJC_$_CLASS_PROP_LIST_DSIdentity
+ __OBJC_$_CLASS_PROP_LIST_DSXPCParticipant
+ __OBJC_$_CLASS_PROP_LIST_DSXPCSharedResource
+ __OBJC_$_INSTANCE_METHODS_DSContactProvider
+ __OBJC_$_INSTANCE_METHODS_DSXPCParticipant
+ __OBJC_$_INSTANCE_METHODS_DSXPCSharedResource
+ __OBJC_$_INSTANCE_VARIABLES_DSContactProvider
+ __OBJC_$_INSTANCE_VARIABLES_DSXPCParticipant
+ __OBJC_$_INSTANCE_VARIABLES_DSXPCSharedResource
+ __OBJC_$_PROP_LIST_DSContactProvider
+ __OBJC_$_PROP_LIST_DSParticipation
+ __OBJC_$_PROP_LIST_DSPersonDescribable
+ __OBJC_$_PROP_LIST_DSSharedResource
+ __OBJC_$_PROP_LIST_DSXPCParticipant
+ __OBJC_$_PROP_LIST_DSXPCSharedResource
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_DSParticipation
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_DSPersonDescribable
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_DSSharedResource
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_DSSharedResource
+ __OBJC_$_PROTOCOL_METHOD_TYPES_DSParticipation
+ __OBJC_$_PROTOCOL_METHOD_TYPES_DSPersonDescribable
+ __OBJC_$_PROTOCOL_METHOD_TYPES_DSSharedResource
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying
+ __OBJC_$_PROTOCOL_REFS_DSParticipation
+ __OBJC_$_PROTOCOL_REFS_DSPersonDescribable
+ __OBJC_$_PROTOCOL_REFS_DSSharedResource
+ __OBJC_CLASS_PROTOCOLS_$_DSXPCParticipant
+ __OBJC_CLASS_PROTOCOLS_$_DSXPCSharedResource
+ __OBJC_CLASS_RO_$_DSContactProvider
+ __OBJC_CLASS_RO_$_DSXPCParticipant
+ __OBJC_CLASS_RO_$_DSXPCSharedResource
+ __OBJC_LABEL_PROTOCOL_$_DSParticipation
+ __OBJC_LABEL_PROTOCOL_$_DSPersonDescribable
+ __OBJC_LABEL_PROTOCOL_$_DSSharedResource
+ __OBJC_LABEL_PROTOCOL_$_NSCopying
+ __OBJC_METACLASS_RO_$_DSContactProvider
+ __OBJC_METACLASS_RO_$_DSXPCParticipant
+ __OBJC_METACLASS_RO_$_DSXPCSharedResource
+ __OBJC_PROTOCOL_$_DSParticipation
+ __OBJC_PROTOCOL_$_DSPersonDescribable
+ __OBJC_PROTOCOL_$_DSSharedResource
+ __OBJC_PROTOCOL_$_NSCopying
+ __OBJC_PROTOCOL_REFERENCE_$_DSIdentifiable
+ ___25-[DSContactProvider init]_block_invoke
+ ___31-[DSXPCSharingPermissions init]_block_invoke
+ ___35-[DSXPCSharingPermissions setDSMe:]_block_invoke
+ ___36+[DSContactProvider defaultProvider]_block_invoke
+ ___37-[DSXPCSharingPermissions connectXPC]_block_invoke.92
+ ___37-[DSXPCSharingPermissions connectXPC]_block_invoke.92.cold.1
+ ___39-[DSXPCSharingPerson sortedSourceNames]_block_invoke
+ ___41+[DSXPCSharingPermissions sharedInstance]_block_invoke
+ ___55-[DSXPCSharingPermissions _fetchSharingWithCompletion:]_block_invoke
+ ___55-[DSXPCSharingPermissions _fetchSharingWithCompletion:]_block_invoke.22
+ ___55-[DSXPCSharingPermissions _fetchSharingWithCompletion:]_block_invoke.24
+ ___55-[DSXPCSharingPermissions _fetchSharingWithCompletion:]_block_invoke.24.cold.1
+ ___55-[DSXPCSharingPermissions _fetchSharingWithCompletion:]_block_invoke.25
+ ___58-[DSContactProvider unifiedContactsForContactIdentifiers:]_block_invoke
+ ___58-[DSContactProvider unifiedContactsForContactIdentifiers:]_block_invoke.cold.1
+ ___63-[DSContactProvider unifiedContactsDictionaryForHandleStrings:]_block_invoke
+ ___63-[DSContactProvider unifiedContactsDictionaryForHandleStrings:]_block_invoke.cold.1
+ ___68-[DSXPCSharingPermissions stopSharingSources:withPerson:completion:]_block_invoke.33
+ ___97-[DSXPCSharingPermissions addSharingPerson:participant:forSource:sharedResource:deviceOwnerRole:]_block_invoke
+ ___97-[DSXPCSharingPermissions addSharingPerson:participant:forSource:sharedResource:deviceOwnerRole:]_block_invoke.32
+ ___97-[DSXPCSharingPermissions addSharingPerson:participant:forSource:sharedResource:deviceOwnerRole:]_block_invoke.32.cold.1
+ ___Block_byref_object_copy_
+ ___Block_byref_object_dispose_
+ ___block_descriptor_32_e19_"NSDictionary"8?0l
+ ___block_descriptor_48_e8_32bs40w_e17_v16?0"NSError"8ls32l8w40l8
+ ___block_descriptor_48_e8_32bs40w_e5_v8?0lw40l8s32l8
+ ___block_descriptor_48_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_56_e8_32bs40w_e34_v24?0"NSDictionary"8"NSError"16lw40l8s32l8
+ ___block_descriptor_56_e8_32s40s48r_e5_v8?0ls32l8s40l8r48l8
+ ___block_literal_global.12
+ ___block_literal_global.317
+ ___block_literal_global.91
+ _defaultProvider._defaultProvider
+ _defaultProvider.onceToken
+ _dispatch_group_wait
+ _dispatch_sync
+ _dispatch_time
+ _objc_msgSend$_fetchSharingWithCompletion:
+ _objc_msgSend$access
+ _objc_msgSend$addSharingPerson:participant:forSource:sharedResource:deviceOwnerRole:
+ _objc_msgSend$defaultProvider
+ _objc_msgSend$detail
+ _objc_msgSend$deviceOwnerRoleForSharedResource:
+ _objc_msgSend$ds_identifier
+ _objc_msgSend$email
+ _objc_msgSend$executeFetchRequest:error:
+ _objc_msgSend$initWithIdentity:
+ _objc_msgSend$initWithKeysToFetch:
+ _objc_msgSend$initWithParticipant:
+ _objc_msgSend$initWithSource:sharedResource:participant:deviceOwnerRole:contact:
+ _objc_msgSend$initWithSource:sharedResource:participant:deviceOwnerRole:unknownHandle:
+ _objc_msgSend$initWithStore:
+ _objc_msgSend$intValue
+ _objc_msgSend$isEqualToDictionary:
+ _objc_msgSend$isLikeIdentity:
+ _objc_msgSend$isLikePhoneNumber:
+ _objc_msgSend$keysToFetch
+ _objc_msgSend$makeSharingPeopleWithResources:
+ _objc_msgSend$participantArray
+ _objc_msgSend$participantIdentity
+ _objc_msgSend$participants:
+ _objc_msgSend$participationForSources:
+ _objc_msgSend$participationPermission
+ _objc_msgSend$participationRole
+ _objc_msgSend$permission
+ _objc_msgSend$phone
+ _objc_msgSend$predicateForContactsMatchingHandleStrings:
+ _objc_msgSend$processInfo
+ _objc_msgSend$processName
+ _objc_msgSend$removeObjectForKey:
+ _objc_msgSend$resourceVisibility
+ _objc_msgSend$sanitizeContacts:
+ _objc_msgSend$setAccess:
+ _objc_msgSend$setDetail:
+ _objc_msgSend$setEmail:
+ _objc_msgSend$setName:
+ _objc_msgSend$setParticipantArray:
+ _objc_msgSend$setParticipantIdentity:
+ _objc_msgSend$setParticipationPermission:
+ _objc_msgSend$setParticipationRole:
+ _objc_msgSend$setPhone:
+ _objc_msgSend$setPredicate:
+ _objc_msgSend$setResourceVisibility:
+ _objc_msgSend$setSharedResourcesBySource:
+ _objc_msgSend$sharedResourcesBySource
+ _objc_msgSend$store
+ _objc_msgSend$unifiedContactInDictionary:forIdentity:
+ _objc_msgSend$unifiedContactsDictionaryForHandleStrings:
+ _objc_msgSend$unifiedContactsDictionaryForIdentities:
+ _objc_msgSend$unifiedContactsForContactIdentifiers:
+ _objc_msgSend$unsignedIntValue
+ _objc_msgSend$updateContactFromIdentity:
+ _objc_retain_x25
+ _objc_unsafeClaimAutoreleasedReturnValue
+ _sharedInstance._defaultProvider
+ _sharedInstance.onceToken
- +[DSXPCSharingPerson supportsSecureCoding]
- -[DSIdentity contactNameComponents]
- -[DSIdentity contactName]
- -[DSIdentity contact]
- -[DSIdentity displayGivenName]
- -[DSIdentity displayName]
- -[DSIdentity emailAddresses]
- -[DSIdentity hash]
- -[DSIdentity isEqualToIdentity:]
- -[DSIdentity isEqualToPerson:]
- -[DSIdentity phoneNumbers]
- -[DSIdentity setContact:]
- -[DSIdentity setContactName:]
- -[DSIdentity setContactNameComponents:]
- -[DSIdentity setDisplayGivenName:]
- -[DSIdentity setDisplayName:]
- -[DSIdentity setEmailAddresses:]
- -[DSIdentity setPhoneNumbers:]
- -[DSIdentity updateIdentityFromContact:]
- -[DSSharingPerson matchesXPCRepresentation:]
- -[DSSharingPerson xpcRepresentation]
- -[DSXPCSharingPermissions fetchSharingPeopleWithCompletion:]
- -[DSXPCSharingPerson encodeWithCoder:]
- -[DSXPCSharingPerson initWithCoder:]
- -[DSXPCSharingPerson localizedAlertTextBySourceName]
- -[DSXPCSharingPerson localizedStopSharingTextBySourceName]
- -[DSXPCSharingPerson removeParticipant:fromSource:]
- -[DSXPCSharingPerson setContact:]
- -[DSXPCSharingPerson setDisplayName:]
- -[DSXPCSharingPerson setLocalizedAlertTextBySourceName:]
- -[DSXPCSharingPerson setLocalizedStopSharingTextBySourceName:]
- -[DSXPCSharingPerson setParticipation:]
- -[DSXPCSharingPerson setSourceNames:]
- -[DSXPCSharingPerson stopSharingSources:queue:completion:]
- -[DSXPCSharingPerson stopSharingSources:queue:completion:].cold.1
- -[DSXPCSharingPerson stopSharingSources:queue:completion:].cold.2
- -[DSXPCSharingPerson stopSharingSources:queue:completion:].cold.3
- -[DSXPCSharingPerson stopSharingSources:queue:completion:].cold.4
- GCC_except_table17
- GCC_except_table45
- _OBJC_IVAR_$_DSIdentity._contact
- _OBJC_IVAR_$_DSIdentity._contactName
- _OBJC_IVAR_$_DSIdentity._contactNameComponents
- _OBJC_IVAR_$_DSIdentity._displayGivenName
- _OBJC_IVAR_$_DSIdentity._displayName
- _OBJC_IVAR_$_DSIdentity._emailAddresses
- _OBJC_IVAR_$_DSIdentity._phoneNumbers
- _OBJC_IVAR_$_DSXPCSharingPerson._displayName
- _OBJC_IVAR_$_DSXPCSharingPerson._localizedAlertTextBySourceName
- _OBJC_IVAR_$_DSXPCSharingPerson._localizedStopSharingTextBySourceName
- _OBJC_IVAR_$_DSXPCSharingPerson._sourceNames
- __OBJC_$_CLASS_PROP_LIST_DSXPCSharingPerson
- __OBJC_CLASS_PROTOCOLS_$_DSXPCSharingPermissions
- ___37-[DSXPCSharingPermissions connectXPC]_block_invoke.69
- ___37-[DSXPCSharingPermissions connectXPC]_block_invoke.69.cold.1
- ___54-[DSXPCSharingPermissions fetchSharingWithCompletion:]_block_invoke.4
- ___58-[DSXPCSharingPerson stopSharingSources:queue:completion:]_block_invoke
- ___58-[DSXPCSharingPerson stopSharingSources:queue:completion:]_block_invoke.346
- ___58-[DSXPCSharingPerson stopSharingSources:queue:completion:]_block_invoke.346.cold.1
- ___58-[DSXPCSharingPerson stopSharingSources:queue:completion:]_block_invoke.347
- ___58-[DSXPCSharingPerson stopSharingSources:queue:completion:]_block_invoke.cold.1
- ___60-[DSXPCSharingPermissions fetchSharingPeopleWithCompletion:]_block_invoke
- ___60-[DSXPCSharingPermissions fetchSharingPeopleWithCompletion:]_block_invoke.8
- ___60-[DSXPCSharingPermissions fetchSharingPeopleWithCompletion:]_block_invoke.cold.1
- ___63-[DSXPCSharingPermissions stopAllSharingWithPerson:completion:]_block_invoke
- ___63-[DSXPCSharingPermissions stopAllSharingWithPerson:completion:]_block_invoke.9
- ___63-[DSXPCSharingPermissions stopAllSharingWithPerson:completion:]_block_invoke.cold.1
- ___68-[DSXPCSharingPermissions stopSharingSources:withPerson:completion:]_block_invoke.10
- ___block_descriptor_48_e8_32bs40w_e29_v24?0"NSArray"8"NSError"16lw40l8s32l8
- ___block_descriptor_48_e8_32bs_e29_v24?0"NSArray"8"NSError"16ls32l8
- _objc_msgSend$cachedFetchError
- _objc_msgSend$contactMatchingEmailAddress:
- _objc_msgSend$contactMatchingPhoneNumber:
- _objc_msgSend$contactNameComponents
- _objc_msgSend$fetchSharingPeopleWithCompletion:
- _objc_msgSend$isEqualToIdentity:
- _objc_msgSend$isEqualToPerson:
- _objc_msgSend$participantsBySource
- _objc_msgSend$removeObjectsInArray:
- _objc_msgSend$setContact:
- _objc_msgSend$setContactName:
- _objc_msgSend$setContactNameComponents:
- _objc_msgSend$setEmailAddresses:
- _objc_msgSend$setLocalizedAlertTextBySourceName:
- _objc_msgSend$setLocalizedStopSharingTextBySourceName:
- _objc_msgSend$setParticipantsBySource:
- _objc_msgSend$setParticipation:
- _objc_msgSend$setPriority:
- _objc_msgSend$setSourceNames:
- _objc_msgSend$stopAllSharingWithPerson:completion:
- _objc_msgSend$updateIdentityFromContact:
CStrings:
+ "\v"
+ "!"
+ "@\"<DSIdentifiable>\"16@0:8"
+ "@\"CNContactStore\""
+ "@\"DSIdentity\""
+ "@\"NSObject<OS_dispatch_group>\""
+ "@\"NSSet\"24@0:8@\"NSString\"16"
+ "@40@0:8@16@24@32"
+ "@40@0:8@16q24q32"
+ "@56@0:8@16@24@32q40@48"
+ "Adding a shared resource from %@ for contact %@ to person %@"
+ "Adding a shared resource from %@ for identity %@ to person %@"
+ "Adding contact %@ to sharing model for resource %@"
+ "Adding contact identifier %{private}@ to predicate"
+ "Adding identity email address %{private}@ to predicate"
+ "Adding identity phone number %{private}@ to predicate"
+ "Adding unknown participant with identity %@ to sharing model for resource %@"
+ "Can't make sharing people-- found %ld sources but no identities"
+ "Creating new sharing person for %@"
+ "DSContactProvider"
+ "DSContactProviderContactStoreWork"
+ "DSParticipation"
+ "DSPersonDescribable"
+ "DSSharedResource"
+ "DSXPCParticipant"
+ "DSXPCSharedResource"
+ "Disconnecting xpc"
+ "Error fetching full contacts for %@ -- expected %ld but got back %ld"
+ "Error while fetching contact for fetchRequest %@ [%@]"
+ "Failed due to hang(s) and/or timeout"
+ "Failed fetchSharedResource call due to timeout"
+ "Fetching all contacts related to the sharing model"
+ "Found contact based on identity %@ %{private}@"
+ "Found no identifying handles within %@ -- this should never happen!"
+ "Identity %@ has a unified contact identifier, but no matching contact was found"
+ "NSCopying"
+ "Q24@0:8@\"<DSSharedResource>\"16"
+ "Q24@0:8@\"NSString\"16"
+ "Skipping makeSharingPeople because sharedResourcesBySource is empty"
+ "Skipping makeSharingPeople because we already have a people model"
+ "Skipping makeSharingPeopleWithResources: because the fetch completed with the same shared resources"
+ "T@\"<DSIdentifiable>\",R,N"
+ "T@\"CNContact\",R,N,V_contact"
+ "T@\"CNContactStore\",&,N,V_store"
+ "T@\"DSIdentity\",&,N,V_participantIdentity"
+ "T@\"NSArray\",&,N,V_participantArray"
+ "T@\"NSDictionary\",&,N,V_sharedResourcesBySource"
+ "T@\"NSNumber\",N,V_access"
+ "T@\"NSNumber\",N,V_participationPermission"
+ "T@\"NSNumber\",N,V_participationRole"
+ "T@\"NSNumber\",N,V_resourceVisibility"
+ "T@\"NSPersonNameComponents\",&,N,V_name"
+ "T@\"NSString\",&,N,V_detail"
+ "T@\"NSString\",&,N,V_email"
+ "T@\"NSString\",&,N,V_identifier"
+ "T@\"NSString\",&,N,V_name"
+ "T@\"NSString\",&,N,V_phone"
+ "T@\"NSString\",R,N"
+ "TQ,?,R,N"
+ "_access"
+ "_contactStoreWorkQueue"
+ "_detail"
+ "_dispatchGroup"
+ "_fetchSharingWithCompletion:"
+ "_name"
+ "_participantArray"
+ "_participantIdentity"
+ "_participationPermission"
+ "_participationRole"
+ "_resourceVisibility"
+ "_store"
+ "access"
+ "addSharingPerson:participant:forSource:sharedResource:deviceOwnerRole:"
+ "alertTextForSource:"
+ "com.apple.DigitalSeparation.SafetyCheckWhenBlockingExited"
+ "copyWithZone:"
+ "defaultProvider"
+ "detail"
+ "detailTextForSource:"
+ "deviceOwnerRoleForSharedResource:"
+ "ds_identifier"
+ "email"
+ "entrypoint"
+ "executeFetchRequest:error:"
+ "fetchErrorCode"
+ "fetchSharingWithProxy: starting sharing fetch over xpc"
+ "initPrivateResourceWithName:detail:participants:"
+ "initWithIdentity:"
+ "initWithIdentity:role:permission:"
+ "initWithKeysToFetch:"
+ "initWithMeIdentifier:emails:phoneNumbers:"
+ "initWithParticipant:"
+ "initWithResource:"
+ "initWithSource:sharedResource:participant:deviceOwnerRole:contact:"
+ "initWithSource:sharedResource:participant:deviceOwnerRole:unknownHandle:"
+ "initWithSource:sharedResource:unknownParticipant:deviceOwnerRole:"
+ "initWithStore:"
+ "intValue"
+ "isEqualToDictionary:"
+ "isIdentity:"
+ "isLikeIdentity:"
+ "isLikePhoneNumber:"
+ "keysToFetch"
+ "lookup"
+ "makeSharingPeople"
+ "makeSharingPeopleWithResources:"
+ "participantArray"
+ "participantIdentity"
+ "participants:"
+ "participationForSources:"
+ "participationPermission"
+ "participationRole"
+ "permission"
+ "phone"
+ "predicateForContactsMatchingHandleStrings:"
+ "processInfo"
+ "processName"
+ "q"
+ "removeObjectForKey:"
+ "resourceVisibility"
+ "sanitizeContacts:"
+ "setAccess:"
+ "setDSMe:"
+ "setDetail:"
+ "setEmail:"
+ "setName:"
+ "setParticipantArray:"
+ "setParticipantIdentity:"
+ "setParticipationPermission:"
+ "setParticipationRole:"
+ "setPhone:"
+ "setPredicate:"
+ "setResourceVisibility:"
+ "setSharedResourcesBySource:"
+ "setSharing:"
+ "setStore:"
+ "sharedResourcesBySource"
+ "sharingPeopleForContacts:"
+ "sharingPeopleForIdentities:"
+ "sharingPersonForContacts:completion: checking %ld sources for participants"
+ "sharingPersonForIdentities:completion: checking %ld sources for participants"
+ "store"
+ "unifiedContactInDictionary:forIdentity:"
+ "unifiedContactsDictionaryForHandleStrings:"
+ "unifiedContactsDictionaryForIdentities:"
+ "unifiedContactsForContactIdentifiers:"
+ "unsignedIntValue"
+ "updateContactFromIdentity:"
+ "v24@0:8@?<v@?@\"NSDictionary\"@\"NSError\">16"
+ "v32@0:8@\"NSDictionary\"16@?<v@?@\"NSError\">24"
+ "v56@0:8@16@24@32@40q48"
- "DSIdentity initializing from contact %@"
- "DSIdentity[%@] initializing"
- "Starting sharing fetch"
- "T@\"CNContact\",&,N,V_contact"
- "T@\"CNContact\",C,N,V_contact"
- "T@\"NSArray\",&,N,V_sourceNames"
- "T@\"NSDictionary\",&,N,V_localizedAlertTextBySourceName"
- "T@\"NSDictionary\",&,N,V_localizedStopSharingTextBySourceName"
- "T@\"NSDictionary\",&,N,V_participantsBySource"
- "T@\"NSNumber\",C,N,V_priority"
- "T@\"NSPersonNameComponents\",&,N,V_contactNameComponents"
- "T@\"NSSet\",&,N,V_emailAddresses"
- "T@\"NSSet\",&,N,V_phoneNumbers"
- "T@\"NSString\",&,N,V_contactName"
- "T@\"NSString\",C,N,V_displayGivenName"
- "T@\"NSString\",C,N,V_identifier"
- "_contactName"
- "_contactNameComponents"
- "_displayGivenName"
- "_localizedAlertTextBySourceName"
- "_localizedStopSharingTextBySourceName"
- "_sourceNames"
- "contactName"
- "contactNameComponents"
- "fetchSharingPeopleWithCompletion:"
- "isEqualToIdentity:"
- "isEqualToPerson:"
- "localizedAlertTextBySourceName"
- "localizedStopSharingTextBySourceName"
- "matchesXPCRepresentation:"
- "participantsBySource"
- "removeObjectsInArray:"
- "setContact:"
- "setContactName:"
- "setContactNameComponents:"
- "setDisplayGivenName:"
- "setEmailAddresses:"
- "setLocalizedAlertTextBySourceName:"
- "setLocalizedStopSharingTextBySourceName:"
- "setParticipantsBySource:"
- "setParticipation:"
- "setPriority:"
- "setSourceNames:"
- "stopAllSharingWithPerson:"
- "updateIdentityFromContact:"
- "v32@0:8@\"DSXPCSharingPerson\"16@?<v@?@\"NSError\">24"
- "v40@0:8@\"NSArray\"16@\"DSXPCSharingPerson\"24@?<v@?@\"NSError\">32"
- "xpcRepresentation"

```
