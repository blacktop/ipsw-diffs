## DigitalSeparation

> `/System/Library/PrivateFrameworks/DigitalSeparation.framework/DigitalSeparation`

```diff

-425.0.114.0.0
-  __TEXT.__text: 0x1f87c
-  __TEXT.__auth_stubs: 0x660
-  __TEXT.__objc_methlist: 0x144c
-  __TEXT.__cstring: 0x1112
-  __TEXT.__const: 0x90
-  __TEXT.__gcc_except_tab: 0x898
-  __TEXT.__oslogstring: 0x1b51
+552.0.0.0.0
+  __TEXT.__text: 0x259c4
+  __TEXT.__auth_stubs: 0x680
+  __TEXT.__objc_methlist: 0x1974
+  __TEXT.__cstring: 0x12d9
+  __TEXT.__const: 0x98
+  __TEXT.__gcc_except_tab: 0xcf0
+  __TEXT.__oslogstring: 0x1f61
   __TEXT.__dlopen_cstrs: 0x68
-  __TEXT.__unwind_info: 0x638
-  __TEXT.__objc_classname: 0x19e
-  __TEXT.__objc_methname: 0x3bf4
-  __TEXT.__objc_methtype: 0x86a
-  __TEXT.__objc_stubs: 0x35c0
-  __DATA_CONST.__got: 0x390
-  __DATA_CONST.__const: 0xba0
-  __DATA_CONST.__objc_classlist: 0xa0
-  __DATA_CONST.__objc_catlist: 0x38
-  __DATA_CONST.__objc_protolist: 0x28
+  __TEXT.__unwind_info: 0x760
+  __TEXT.__objc_classname: 0x22a
+  __TEXT.__objc_methname: 0x4521
+  __TEXT.__objc_methtype: 0x971
+  __TEXT.__objc_stubs: 0x3c60
+  __DATA_CONST.__got: 0x3b8
+  __DATA_CONST.__const: 0xc68
+  __DATA_CONST.__objc_classlist: 0xc0
+  __DATA_CONST.__objc_catlist: 0x40
+  __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1040
-  __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x50
-  __AUTH_CONST.__auth_got: 0x340
-  __AUTH_CONST.__const: 0x1a0
-  __AUTH_CONST.__cfstring: 0x11e0
-  __AUTH_CONST.__objc_const: 0x25a0
-  __AUTH.__objc_data: 0x640
-  __DATA.__objc_ivar: 0xe4
-  __DATA.__data: 0x1e8
-  __DATA.__bss: 0xe8
+  __DATA_CONST.__objc_selrefs: 0x1258
+  __DATA_CONST.__objc_protorefs: 0x18
+  __DATA_CONST.__objc_superrefs: 0x70
+  __AUTH_CONST.__auth_got: 0x350
+  __AUTH_CONST.__const: 0x200
+  __AUTH_CONST.__cfstring: 0x13e0
+  __AUTH_CONST.__objc_const: 0x38c0
+  __AUTH.__objc_data: 0x410
+  __DATA.__objc_ivar: 0x144
+  __DATA.__data: 0x368
+  __DATA.__bss: 0x68
+  __DATA_DIRTY.__objc_data: 0x370
+  __DATA_DIRTY.__bss: 0x98
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 5176838B-000E-30A4-8104-7906A751BF4D
-  Functions: 571
-  Symbols:   2242
-  CStrings:  1230
+  UUID: 6214920E-E4B8-39B0-990A-E26F9F388552
+  Functions: 700
+  Symbols:   2683
+  CStrings:  1403
 
Symbols:
+ +[CNContactStore(DSContactHelpers) contactMatchingEmailAddress:]
+ +[CNContactStore(DSContactHelpers) contactMatchingIdentity:]
+ +[CNContactStore(DSContactHelpers) contactMatchingPhoneNumber:]
+ +[DSSourceDescriptor descriptorCache].cold.1
+ +[DSSourceDescriptor sourceDescriptorForSource:localizationBundle:].cold.1
+ +[DSXPCSharingPermissions interface]
+ +[DSXPCSharingPerson sortedXPCArray:]
+ +[DSXPCSharingPerson supportsSecureCoding]
+ -[CNContact(DigitalSeparation) ds_emailAddresses]
+ -[CNContact(DigitalSeparation) ds_isLikeContact:]
+ -[CNContact(DigitalSeparation) ds_name]
+ -[CNContact(DigitalSeparation) ds_phoneNumbers]
+ -[CNContact(DigitalSeparation) isLikeIdentifiable:]
+ -[DSContactIdentity .cxx_destruct]
+ -[DSContactIdentity emailAddress]
+ -[DSContactIdentity initWithEmail:withPhone:]
+ -[DSContactIdentity nameComponents]
+ -[DSContactIdentity phoneNumber]
+ -[DSContactIdentity unifiedContactIdentifier]
+ -[DSIdentity .cxx_destruct]
+ -[DSIdentity contactNameComponents]
+ -[DSIdentity contactName]
+ -[DSIdentity contact]
+ -[DSIdentity displayGivenName]
+ -[DSIdentity displayName]
+ -[DSIdentity emailAddress]
+ -[DSIdentity emailAddresses]
+ -[DSIdentity hash]
+ -[DSIdentity identifier]
+ -[DSIdentity initWithContact:]
+ -[DSIdentity initWithEmail:]
+ -[DSIdentity initWithPhone:]
+ -[DSIdentity isEqual:]
+ -[DSIdentity isEqualToIdentity:]
+ -[DSIdentity isEqualToPerson:]
+ -[DSIdentity nameComponents]
+ -[DSIdentity phoneNumber]
+ -[DSIdentity phoneNumbers]
+ -[DSIdentity setContact:]
+ -[DSIdentity setContactName:]
+ -[DSIdentity setContactNameComponents:]
+ -[DSIdentity setDisplayGivenName:]
+ -[DSIdentity setDisplayName:]
+ -[DSIdentity setEmailAddresses:]
+ -[DSIdentity setIdentifier:]
+ -[DSIdentity setPhoneNumbers:]
+ -[DSIdentity unifiedContactIdentifier]
+ -[DSIdentity updateIdentityFromContact:]
+ -[DSSharingPerson matchesXPCRepresentation:]
+ -[DSSharingPerson removeSourceWithName:]
+ -[DSSharingPerson stopSharingSources:queue:completion:].cold.3
+ -[DSSharingPerson stopSharingSources:queue:completion:].cold.4
+ -[DSSharingPerson xpcRepresentation]
+ -[DSSharingType stopAllSharingOnQueue:completion:].cold.1
+ -[DSSharingType stopSharingWithPeople:asParticipantsOnQueue:completion:].cold.1
+ -[DSSourceDescriptor _localizedStopByPerson:detailTextForDirectlySharedResources:isBlocking:]
+ -[DSSourceDescriptor _localizedStopByPerson:detailTextForIndirectlySharedResources:isBlocking:]
+ -[DSSourceDescriptor _localizedStopByPerson:isBlocking:]
+ -[DSSourceDescriptor attributedStopByPerson:direction:format:namedResourceList:isBlocking:]
+ -[DSSourceDescriptor localizedStopByPersonBlocking:]
+ -[DSSourceDescriptor stopByPerson:direction:format:namedResources:isBlocking:]
+ -[DSSourceDescriptor stopByPersonLocKey:resourceTypes:isBlocking:]
+ -[DSXPCSharingPermissions .cxx_destruct]
+ -[DSXPCSharingPermissions allPeople]
+ -[DSXPCSharingPermissions cachedFetchError]
+ -[DSXPCSharingPermissions connectXPC]
+ -[DSXPCSharingPermissions disconnect]
+ -[DSXPCSharingPermissions fetchCompletedTime]
+ -[DSXPCSharingPermissions fetchSharingPeopleWithCompletion:]
+ -[DSXPCSharingPermissions fetchSharingWithCompletion:]
+ -[DSXPCSharingPermissions init]
+ -[DSXPCSharingPermissions isFetchNeeded]
+ -[DSXPCSharingPermissions isFetchNeeded].cold.1
+ -[DSXPCSharingPermissions people]
+ -[DSXPCSharingPermissions requestImmediateFetch]
+ -[DSXPCSharingPermissions setCachedFetchError:]
+ -[DSXPCSharingPermissions setFetchCompletedTime:]
+ -[DSXPCSharingPermissions setPeople:]
+ -[DSXPCSharingPermissions setXpcConnection:]
+ -[DSXPCSharingPermissions stopAllSharingWithPerson:completion:]
+ -[DSXPCSharingPermissions stopSharingSources:withPerson:completion:]
+ -[DSXPCSharingPermissions xpcConnection]
+ -[DSXPCSharingPerson .cxx_destruct]
+ -[DSXPCSharingPerson _setPriority]
+ -[DSXPCSharingPerson contact]
+ -[DSXPCSharingPerson displayName]
+ -[DSXPCSharingPerson encodeWithCoder:]
+ -[DSXPCSharingPerson hash]
+ -[DSXPCSharingPerson identifier]
+ -[DSXPCSharingPerson initWithCoder:]
+ -[DSXPCSharingPerson isEqual:]
+ -[DSXPCSharingPerson isLikeContact:]
+ -[DSXPCSharingPerson localizedAlertTextBySourceName]
+ -[DSXPCSharingPerson localizedDetail]
+ -[DSXPCSharingPerson localizedStopSharingTextBySourceName]
+ -[DSXPCSharingPerson priority]
+ -[DSXPCSharingPerson removeSources:]
+ -[DSXPCSharingPerson setContact:]
+ -[DSXPCSharingPerson setDisplayName:]
+ -[DSXPCSharingPerson setIdentifier:]
+ -[DSXPCSharingPerson setLocalizedAlertTextBySourceName:]
+ -[DSXPCSharingPerson setLocalizedStopSharingTextBySourceName:]
+ -[DSXPCSharingPerson setPriority:]
+ -[DSXPCSharingPerson setSourceNames:]
+ -[DSXPCSharingPerson sourceNames]
+ GCC_except_table17
+ GCC_except_table19
+ GCC_except_table25
+ _NSObjectInaccessibleException
+ _OBJC_CLASS_$_DSContactIdentity
+ _OBJC_CLASS_$_DSIdentity
+ _OBJC_CLASS_$_DSXPCSharingPermissions
+ _OBJC_CLASS_$_DSXPCSharingPerson
+ _OBJC_CLASS_$_NSXPCConnection
+ _OBJC_CLASS_$_NSXPCInterface
+ _OBJC_IVAR_$_DSContactIdentity._email
+ _OBJC_IVAR_$_DSContactIdentity._phone
+ _OBJC_IVAR_$_DSContactIdentity.nameComponents
+ _OBJC_IVAR_$_DSContactIdentity.unifiedContactIdentifier
+ _OBJC_IVAR_$_DSIdentity._contact
+ _OBJC_IVAR_$_DSIdentity._contactName
+ _OBJC_IVAR_$_DSIdentity._contactNameComponents
+ _OBJC_IVAR_$_DSIdentity._displayGivenName
+ _OBJC_IVAR_$_DSIdentity._displayName
+ _OBJC_IVAR_$_DSIdentity._emailAddresses
+ _OBJC_IVAR_$_DSIdentity._identifier
+ _OBJC_IVAR_$_DSIdentity._phoneNumbers
+ _OBJC_IVAR_$_DSXPCSharingPermissions._cachedFetchError
+ _OBJC_IVAR_$_DSXPCSharingPermissions._fetchCompletedTime
+ _OBJC_IVAR_$_DSXPCSharingPermissions._people
+ _OBJC_IVAR_$_DSXPCSharingPermissions._queue
+ _OBJC_IVAR_$_DSXPCSharingPermissions._xpcConnection
+ _OBJC_IVAR_$_DSXPCSharingPerson._contact
+ _OBJC_IVAR_$_DSXPCSharingPerson._displayName
+ _OBJC_IVAR_$_DSXPCSharingPerson._identifier
+ _OBJC_IVAR_$_DSXPCSharingPerson._localizedAlertTextBySourceName
+ _OBJC_IVAR_$_DSXPCSharingPerson._localizedStopSharingTextBySourceName
+ _OBJC_IVAR_$_DSXPCSharingPerson._priority
+ _OBJC_IVAR_$_DSXPCSharingPerson._sourceNames
+ _OBJC_METACLASS_$_DSContactIdentity
+ _OBJC_METACLASS_$_DSIdentity
+ _OBJC_METACLASS_$_DSXPCSharingPermissions
+ _OBJC_METACLASS_$_DSXPCSharingPerson
+ _OUTLINED_FUNCTION_23
+ _OUTLINED_FUNCTION_24
+ _OUTLINED_FUNCTION_25
+ _OUTLINED_FUNCTION_26
+ _OUTLINED_FUNCTION_27
+ __OBJC_$_CATEGORY_CNContact_$_DigitalSeparation
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_CNContact_$_DigitalSeparation
+ __OBJC_$_CLASS_METHODS_DSXPCSharingPermissions
+ __OBJC_$_CLASS_METHODS_DSXPCSharingPerson
+ __OBJC_$_CLASS_PROP_LIST_DSXPCSharingPerson
+ __OBJC_$_CLASS_PROP_LIST_NSSecureCoding
+ __OBJC_$_INSTANCE_METHODS_DSContactIdentity
+ __OBJC_$_INSTANCE_METHODS_DSIdentity
+ __OBJC_$_INSTANCE_METHODS_DSXPCSharingPermissions
+ __OBJC_$_INSTANCE_METHODS_DSXPCSharingPerson
+ __OBJC_$_INSTANCE_VARIABLES_DSContactIdentity
+ __OBJC_$_INSTANCE_VARIABLES_DSIdentity
+ __OBJC_$_INSTANCE_VARIABLES_DSXPCSharingPermissions
+ __OBJC_$_INSTANCE_VARIABLES_DSXPCSharingPerson
+ __OBJC_$_PROP_LIST_DSContactIdentity
+ __OBJC_$_PROP_LIST_DSIdentifiable
+ __OBJC_$_PROP_LIST_DSIdentity
+ __OBJC_$_PROP_LIST_DSXPCSharingPermissions
+ __OBJC_$_PROP_LIST_DSXPCSharingPerson
+ __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_DSIdentifiable
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_DSSafetyCheckBlocking
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_DSIdentifiable
+ __OBJC_$_PROTOCOL_METHOD_TYPES_DSSafetyCheckBlocking
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding
+ __OBJC_$_PROTOCOL_REFS_DSIdentifiable
+ __OBJC_$_PROTOCOL_REFS_DSSafetyCheckBlocking
+ __OBJC_$_PROTOCOL_REFS_NSSecureCoding
+ __OBJC_CLASS_PROTOCOLS_$_DSContactIdentity
+ __OBJC_CLASS_PROTOCOLS_$_DSIdentity
+ __OBJC_CLASS_PROTOCOLS_$_DSXPCSharingPermissions
+ __OBJC_CLASS_PROTOCOLS_$_DSXPCSharingPerson
+ __OBJC_CLASS_RO_$_DSContactIdentity
+ __OBJC_CLASS_RO_$_DSIdentity
+ __OBJC_CLASS_RO_$_DSXPCSharingPermissions
+ __OBJC_CLASS_RO_$_DSXPCSharingPerson
+ __OBJC_LABEL_PROTOCOL_$_DSIdentifiable
+ __OBJC_LABEL_PROTOCOL_$_DSSafetyCheckBlocking
+ __OBJC_LABEL_PROTOCOL_$_NSCoding
+ __OBJC_LABEL_PROTOCOL_$_NSSecureCoding
+ __OBJC_METACLASS_RO_$_DSContactIdentity
+ __OBJC_METACLASS_RO_$_DSIdentity
+ __OBJC_METACLASS_RO_$_DSXPCSharingPermissions
+ __OBJC_METACLASS_RO_$_DSXPCSharingPerson
+ __OBJC_PROTOCOL_$_DSIdentifiable
+ __OBJC_PROTOCOL_$_DSSafetyCheckBlocking
+ __OBJC_PROTOCOL_$_NSCoding
+ __OBJC_PROTOCOL_$_NSSecureCoding
+ __OBJC_PROTOCOL_REFERENCE_$_DSSafetyCheckBlocking
+ ___37+[DSSourceDescriptor descriptorCache]_block_invoke
+ ___37+[DSXPCSharingPerson sortedXPCArray:]_block_invoke
+ ___37-[DSXPCSharingPermissions connectXPC]_block_invoke
+ ___37-[DSXPCSharingPermissions connectXPC]_block_invoke.69
+ ___37-[DSXPCSharingPermissions connectXPC]_block_invoke.69.cold.1
+ ___37-[DSXPCSharingPermissions connectXPC]_block_invoke.cold.1
+ ___50-[DSSharingType stopAllSharingOnQueue:completion:]_block_invoke.309
+ ___50-[DSSharingType stopAllSharingOnQueue:completion:]_block_invoke.309.cold.1
+ ___50-[DSSharingType stopAllSharingOnQueue:completion:]_block_invoke.311
+ ___50-[DSSharingType stopAllSharingOnQueue:completion:]_block_invoke.314
+ ___52-[DSSharingType stopSharingPeople:queue:completion:]_block_invoke.321
+ ___54-[DSAppSharing resetShortcutsAutomationTimer:handler:]_block_invoke.388
+ ___54-[DSXPCSharingPermissions fetchSharingWithCompletion:]_block_invoke
+ ___54-[DSXPCSharingPermissions fetchSharingWithCompletion:]_block_invoke.4
+ ___55-[DSSharingPerson stopSharingSources:queue:completion:]_block_invoke.325.cold.1
+ ___55-[DSSharingPerson stopSharingSources:queue:completion:]_block_invoke.326
+ ___60-[DSXPCSharingPermissions fetchSharingPeopleWithCompletion:]_block_invoke
+ ___60-[DSXPCSharingPermissions fetchSharingPeopleWithCompletion:]_block_invoke.8
+ ___60-[DSXPCSharingPermissions fetchSharingPeopleWithCompletion:]_block_invoke.cold.1
+ ___63-[DSXPCSharingPermissions stopAllSharingWithPerson:completion:]_block_invoke
+ ___63-[DSXPCSharingPermissions stopAllSharingWithPerson:completion:]_block_invoke.9
+ ___63-[DSXPCSharingPermissions stopAllSharingWithPerson:completion:]_block_invoke.cold.1
+ ___68-[DSXPCSharingPermissions stopSharingSources:withPerson:completion:]_block_invoke
+ ___68-[DSXPCSharingPermissions stopSharingSources:withPerson:completion:]_block_invoke.10
+ ___68-[DSXPCSharingPermissions stopSharingSources:withPerson:completion:]_block_invoke.cold.1
+ ___72-[DSSharingType stopSharingWithPeople:asParticipantsOnQueue:completion:]_block_invoke.316
+ ___72-[DSSharingType stopSharingWithPeople:asParticipantsOnQueue:completion:]_block_invoke.316.cold.1
+ ___72-[DSSharingType stopSharingWithPeople:asParticipantsOnQueue:completion:]_block_invoke.317
+ ___72-[DSSharingType stopSharingWithPeople:asParticipantsOnQueue:completion:]_block_invoke.318
+ ___85-[DSSharingPermissions fetchPermissionsFromSources:includingErrors:queue:completion:]_block_invoke.cold.2
+ ___85-[DSSharingPermissions fetchPermissionsFromSources:includingErrors:queue:completion:]_block_invoke.cold.3
+ ___block_descriptor_32_e51_q24?0"DSXPCSharingPerson"8"DSXPCSharingPerson"16l
+ ___block_descriptor_40_e8_32w_e5_v8?0lw32l8
+ ___block_descriptor_48_e8_32bs40w_e29_v24?0"NSArray"8"NSError"16lw40l8s32l8
+ ___block_descriptor_48_e8_32bs_e29_v24?0"NSArray"8"NSError"16ls32l8
+ ___block_descriptor_56_e8_32s40bs_e17_v16?0"NSError"8ls40l8s32l8
+ ___block_literal_global.327
+ ___block_literal_global.331
+ ___block_literal_global.348
+ _descriptorCache.onceToken
+ _dispatch_queue_attr_make_with_autorelease_frequency
+ _dispatch_queue_attr_make_with_qos_class
+ _kSafetyCheckWhenBlockingEntitlement
+ _objc_msgSend$_setPriority
+ _objc_msgSend$cachedFetchError
+ _objc_msgSend$componentsForContact:
+ _objc_msgSend$connectXPC
+ _objc_msgSend$contactMatchingEmailAddress:
+ _objc_msgSend$contactMatchingPhoneNumber:
+ _objc_msgSend$contactNameComponents
+ _objc_msgSend$decodeObjectOfClass:forKey:
+ _objc_msgSend$decodeObjectOfClasses:forKey:
+ _objc_msgSend$ds_emailAddresses
+ _objc_msgSend$ds_isLikeContact:
+ _objc_msgSend$ds_name
+ _objc_msgSend$ds_phoneNumbers
+ _objc_msgSend$encodeObject:forKey:
+ _objc_msgSend$fetchCompletedTime
+ _objc_msgSend$fetchSharingPeopleWithCompletion:
+ _objc_msgSend$initWithEmail:withPhone:
+ _objc_msgSend$initWithMachServiceName:options:
+ _objc_msgSend$interface
+ _objc_msgSend$interfaceWithProtocol:
+ _objc_msgSend$invalidate
+ _objc_msgSend$isEqual:
+ _objc_msgSend$isEqualToIdentity:
+ _objc_msgSend$isEqualToPerson:
+ _objc_msgSend$isFetchNeeded
+ _objc_msgSend$isLikeContact:
+ _objc_msgSend$isLikeIdentifiable:
+ _objc_msgSend$localizedAlertTextForPerson:
+ _objc_msgSend$localizedStopByPersonBlocking:
+ _objc_msgSend$remoteObjectProxyWithErrorHandler:
+ _objc_msgSend$removeObjectsInArray:
+ _objc_msgSend$removeSourceWithName:
+ _objc_msgSend$requestImmediateFetch
+ _objc_msgSend$resume
+ _objc_msgSend$setCachedFetchError:
+ _objc_msgSend$setClasses:forSelector:argumentIndex:ofReply:
+ _objc_msgSend$setContact:
+ _objc_msgSend$setContactName:
+ _objc_msgSend$setContactNameComponents:
+ _objc_msgSend$setEmailAddresses:
+ _objc_msgSend$setFetchCompletedTime:
+ _objc_msgSend$setIdentifier:
+ _objc_msgSend$setInterruptionHandler:
+ _objc_msgSend$setInvalidationHandler:
+ _objc_msgSend$setLocalizedAlertTextBySourceName:
+ _objc_msgSend$setLocalizedStopSharingTextBySourceName:
+ _objc_msgSend$setPriority:
+ _objc_msgSend$setRemoteObjectInterface:
+ _objc_msgSend$setSourceNames:
+ _objc_msgSend$sourceNames
+ _objc_msgSend$stopAllSharingWithPerson:completion:
+ _objc_msgSend$stopSharingSources:withPerson:completion:
+ _objc_msgSend$updateIdentityFromContact:
+ _objc_msgSend$xpcConnection
- -[DSSharingPerson removeSource:]
- -[DSSharingPerson removeSource:].cold.1
- -[DSSourceDescriptor _localizedStopByPerson:detailTextForDirectlySharedResources:]
- -[DSSourceDescriptor _localizedStopByPerson:detailTextForIndirectlySharedResources:]
- GCC_except_table18
- GCC_except_table23
- ___50-[DSSharingType stopAllSharingOnQueue:completion:]_block_invoke.306
- ___50-[DSSharingType stopAllSharingOnQueue:completion:]_block_invoke.306.cold.1
- ___50-[DSSharingType stopAllSharingOnQueue:completion:]_block_invoke.308
- ___52-[DSSharingType stopSharingPeople:queue:completion:]_block_invoke.316
- ___54-[DSAppSharing resetShortcutsAutomationTimer:handler:]_block_invoke.385
- ___55-[DSSharingPerson stopSharingSources:queue:completion:]_block_invoke.324
- ___55-[DSSharingPerson stopSharingSources:queue:completion:]_block_invoke.324.cold.1
- ___72-[DSSharingType stopSharingWithPeople:asParticipantsOnQueue:completion:]_block_invoke.312
- ___72-[DSSharingType stopSharingWithPeople:asParticipantsOnQueue:completion:]_block_invoke.312.cold.1
- ___72-[DSSharingType stopSharingWithPeople:asParticipantsOnQueue:completion:]_block_invoke.313
- ___block_literal_global.324
- ___block_literal_global.328
- ___block_literal_global.345
- _objc_msgSend$removeSource:
CStrings:
+ "%#"
+ "@\"NSArray\""
+ "@\"NSError\""
+ "@\"NSNumber\""
+ "@\"NSPersonNameComponents\""
+ "@\"NSPersonNameComponents\"16@0:8"
+ "@\"NSXPCConnection\""
+ "@24@0:8@\"NSCoder\"16"
+ "Cannot connect to remote service with error: %{public}@"
+ "Connection with blocking service interrupted."
+ "Connection with blocking service invalidated."
+ "DSContactIdentity"
+ "DSIdentifiable"
+ "DSIdentity"
+ "DSIdentity initializing from contact %@"
+ "DSIdentity[%@] initializing"
+ "DSSafetyCheckBlocking"
+ "DSXPCSharingPermissions"
+ "DSXPCSharingPerson"
+ "Failed to fetch shared resources from %{public}@ because exception %{public}@"
+ "Failed to find source named %{public}@"
+ "Failed to stop all sharing with %{public}@ because exception %{public}@"
+ "Failed to stop sharing on source %{public}@ for %{public}@ because exception %{public}@"
+ "Failed to stop sharing on source %{public}@ for participants %{private}@ because exception %{public}@"
+ "Failed to stop sharing with participants for %{public}@ because exception %{public}@"
+ "Last fetch was %{public}fs ago"
+ "NSCoding"
+ "NSSecureCoding"
+ "No loc key found named %@"
+ "No source descriptor for provided source name and bundle"
+ "SCWB"
+ "STOP_BY_PERSON_INDIRECT_SINGLE_%@"
+ "SafetyCheckWhenBlocking"
+ "Skipping because we recently fetched"
+ "Starting sharing fetch"
+ "T@\"CNContact\",&,N,V_contact"
+ "T@\"CNContact\",C,N,V_contact"
+ "T@\"NSArray\",&,N,V_sourceNames"
+ "T@\"NSDictionary\",&,N,V_localizedAlertTextBySourceName"
+ "T@\"NSDictionary\",&,N,V_localizedStopSharingTextBySourceName"
+ "T@\"NSError\",&,N,V_cachedFetchError"
+ "T@\"NSNumber\",C,N,V_priority"
+ "T@\"NSPersonNameComponents\",&,N,V_contactNameComponents"
+ "T@\"NSPersonNameComponents\",R,C,N"
+ "T@\"NSPersonNameComponents\",R,C,N,VnameComponents"
+ "T@\"NSSet\",&,N,V_emailAddresses"
+ "T@\"NSSet\",&,N,V_phoneNumbers"
+ "T@\"NSString\",&,N,V_contactName"
+ "T@\"NSString\",C,N,V_displayGivenName"
+ "T@\"NSString\",C,N,V_identifier"
+ "T@\"NSString\",R,C,N,VunifiedContactIdentifier"
+ "T@\"NSXPCConnection\",&,N,V_xpcConnection"
+ "TB,R"
+ "TQ,V_fetchCompletedTime"
+ "XPC connection failed, completion should be called in proxy error handler"
+ "_cachedFetchError"
+ "_contactName"
+ "_contactNameComponents"
+ "_displayGivenName"
+ "_email"
+ "_fetchCompletedTime"
+ "_localizedAlertTextBySourceName"
+ "_localizedStopSharingTextBySourceName"
+ "_phone"
+ "_priority"
+ "_queue"
+ "_setPriority"
+ "_sourceNames"
+ "_xpcConnection"
+ "cached"
+ "cachedFetchError"
+ "com.apple.DigitalSeparation.DSXPCSharingPermissions"
+ "com.apple.private.safetycheckd.scblocking"
+ "com.apple.safetycheckd"
+ "componentsForContact:"
+ "connectXPC"
+ "contactMatchingEmailAddress:"
+ "contactMatchingPhoneNumber:"
+ "contactName"
+ "contactNameComponents"
+ "decodeObjectOfClass:forKey:"
+ "decodeObjectOfClasses:forKey:"
+ "ds_emailAddresses"
+ "ds_isLikeContact:"
+ "ds_name"
+ "ds_phoneNumbers"
+ "encodeObject:forKey:"
+ "encodeWithCoder:"
+ "fetchCompletedTime"
+ "fetchSharingPeopleWithCompletion:"
+ "fetchSharingWithCompletion:"
+ "initWithCoder:"
+ "initWithContact:"
+ "initWithEmail:"
+ "initWithEmail:withPhone:"
+ "initWithMachServiceName:options:"
+ "initWithPhone:"
+ "interface"
+ "interfaceWithProtocol:"
+ "invalidate"
+ "isEqualToIdentity:"
+ "isEqualToPerson:"
+ "isFetchNeeded"
+ "isLikeContact:"
+ "isLikeIdentifiable:"
+ "localizationBundle"
+ "localizedAlertTextBySourceName"
+ "localizedStopByPersonBlocking:"
+ "localizedStopSharingTextBySourceName"
+ "mach_continuous_time walked backwards (now: %{public}llu, then: %{public}llu)"
+ "matchesXPCRepresentation:"
+ "q24@?0@\"DSXPCSharingPerson\"8@\"DSXPCSharingPerson\"16"
+ "remoteObjectProxyWithErrorHandler:"
+ "removeObjectsInArray:"
+ "removeSourceWithName:"
+ "removeSources:"
+ "requestImmediateFetch"
+ "resume"
+ "setCachedFetchError:"
+ "setClasses:forSelector:argumentIndex:ofReply:"
+ "setContact:"
+ "setContactName:"
+ "setContactNameComponents:"
+ "setDisplayGivenName:"
+ "setEmailAddresses:"
+ "setFetchCompletedTime:"
+ "setIdentifier:"
+ "setInterruptionHandler:"
+ "setInvalidationHandler:"
+ "setLocalizedAlertTextBySourceName:"
+ "setLocalizedStopSharingTextBySourceName:"
+ "setPriority:"
+ "setRemoteObjectInterface:"
+ "setSourceNames:"
+ "setXpcConnection:"
+ "sortedXPCArray:"
+ "sourceNames"
+ "stopAllSharingWithPerson:"
+ "stopAllSharingWithPerson:completion:"
+ "stopSharingSources:withPerson:"
+ "stopSharingSources:withPerson:completion:"
+ "supportsSecureCoding"
+ "updateIdentityFromContact:"
+ "v24@0:8@\"NSCoder\"16"
+ "v32@0:8@\"DSXPCSharingPerson\"16@?<v@?@\"NSError\">24"
+ "v40@0:8@\"NSArray\"16@\"DSXPCSharingPerson\"24@?<v@?@\"NSError\">32"
+ "xpcConnection"
+ "xpcRepresentation"
- "removeSource:"

```
