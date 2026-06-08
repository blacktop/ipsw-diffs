## ContactsAssistantServices

> `/System/Library/PrivateFrameworks/ContactsAssistantServices.framework/ContactsAssistantServices`

```diff

 29.0.0.0.0
-  __TEXT.__text: 0x5840
-  __TEXT.__auth_stubs: 0x210
+  __TEXT.__text: 0x524c
   __TEXT.__objc_methlist: 0x244
   __TEXT.__const: 0x10
   __TEXT.__cstring: 0x292
   __TEXT.__gcc_except_tab: 0x38
-  __TEXT.__unwind_info: 0x138
-  __TEXT.__objc_classname: 0x3e
-  __TEXT.__objc_methname: 0x1008
-  __TEXT.__objc_methtype: 0xad
-  __TEXT.__objc_stubs: 0x17c0
-  __DATA_CONST.__got: 0x1e8
+  __TEXT.__unwind_info: 0x130
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x1a8
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x658
-  __AUTH_CONST.__auth_got: 0x118
+  __DATA_CONST.__got: 0x1e8
   __AUTH_CONST.__const: 0x120
   __AUTH_CONST.__cfstring: 0x220
   __AUTH_CONST.__objc_const: 0x1b8
+  __AUTH_CONST.__auth_got: 0x0
   __DATA_DIRTY.__objc_data: 0xa0
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/SAObjects.framework/SAObjects
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D13E7079-0789-3EFA-A67F-419D096910F4
+  UUID: B5E81EE5-ABCC-3509-9997-7663C1804D5B
   Functions: 67
-  Symbols:   460
-  CStrings:  267
+  Symbols:   462
+  CStrings:  47
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x4
+ _objc_retain_x8
+ _objc_storeStrong
- _objc_release_x28
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x25
- _objc_retain_x26
- _objc_retain_x27
Functions:
~ +[CNAssistantConversion descriptorsForRequiredKeys] -> +[CNAssistantConversion descriptorsForRequiredKeysForConversionType:] : 16 -> 812
~ +[CNAssistantConversion descriptorsForRequiredKeysForConversionType:] -> +[CNAssistantConversion descriptorsForRequiredKeys] : 824 -> 16
~ +[CNAssistantConversion createSAPersonFromCNContact:conversionType:] : 252 -> 232
~ +[CNAssistantConversion verifyContact:hasDescriptorsForRequiredKeys:] : 328 -> 324
~ +[CNAssistantConversion personFromContact:useABPerson:] : 1360 -> 1204
~ +[CNAssistantID assistantIDFromContact:] : 416 -> 392
~ +[CNAssistantID databaseID] : 88 -> 84
~ +[CNAssistantID assistantIDOfType:recordID:databaseID:identifier:] : 520 -> 492
~ _NonEmptyOrNilString : 88 -> 84
~ +[CNAssistantConversion emailAddressesFromContact:] : 816 -> 780
~ +[CNAssistantConversion filterLabeledValues:droppingEmptyLabels:droppingDuplicates:] : 240 -> 236
~ -[NSArray(MapAndFilter) mapUsingBlock:] : 240 -> 228
~ _NonEmptyOrNilArray : 88 -> 84
~ +[CNAssistantConversion phoneNumbersFromContact:] : 1000 -> 952
~ +[CNAssistantConversion addressesFromContact:] : 192 -> 176
~ +[CNAssistantConversion relationsFromContact:] : 196 -> 180
~ -[NSArray(MapAndFilter) filterUsingBlock:] : 240 -> 228
~ ___39-[NSArray(MapAndFilter) mapUsingBlock:]_block_invoke : 108 -> 104
~ ___42-[NSArray(MapAndFilter) filterUsingBlock:]_block_invoke : 108 -> 104
~ ___72-[CNContactStore(CASAdditions) contactWithIdentifier:keysToFetch:error:]_block_invoke : 72 -> 16
~ +[CNAssistantID assistantIDFromContactID:] : 324 -> 308
~ +[CNAssistantID assistantIDFromContainer:] : 172 -> 156
~ +[CNAssistantID assistantIDFromGroup:] : 172 -> 156
~ +[CNAssistantID contactIDFromAssistantID:] : 216 -> 196
~ _GetURLParameters : 528 -> 516
~ +[CNAssistantID containerIDFromAssistantID:] : 216 -> 196
~ +[CNAssistantID groupIDFromAssistantID:] : 216 -> 196
~ +[CNAssistantID assistantIDFromExternalIdentifier:] : 124 -> 116
~ +[CNAssistantID externalIdentifierFromAssistantID:] : 168 -> 152
~ +[CNAssistantConversion personFromMeContact:] : 516 -> 464
~ +[CNAssistantConversion personForSyncFromContact:] : 1132 -> 1000
~ +[CNAssistantConversion createSAPersonFromCNContactWithExternalIdentifier:] : 288 -> 268
~ +[CNAssistantConversion createSASourceFromCNContainer:] : 212 -> 204
~ ___84+[CNAssistantConversion filterLabeledValues:droppingEmptyLabels:droppingDuplicates:]_block_invoke : 140 -> 136
~ ___51+[CNAssistantConversion emailAddressesFromContact:]_block_invoke : 312 -> 292
~ +[CNAssistantConversion emailAddressesForSyncFromContact:] : 812 -> 776
~ ___58+[CNAssistantConversion emailAddressesForSyncFromContact:]_block_invoke : 256 -> 244
~ ___49+[CNAssistantConversion phoneNumbersFromContact:]_block_invoke : 388 -> 360
~ +[CNAssistantConversion phoneNumbersForSyncFromContact:] : 1000 -> 952
~ ___56+[CNAssistantConversion phoneNumbersForSyncFromContact:]_block_invoke : 312 -> 296
~ ___46+[CNAssistantConversion addressesFromContact:]_block_invoke : 536 -> 468
~ +[CNAssistantConversion addressesForSyncFromContact:] : 192 -> 176
~ ___53+[CNAssistantConversion addressesForSyncFromContact:]_block_invoke : 124 -> 120
~ ___46+[CNAssistantConversion relationsFromContact:]_block_invoke : 184 -> 172
~ +[CNAssistantConversion relationsForSyncFromContact:] : 196 -> 180
~ ___53+[CNAssistantConversion relationsForSyncFromContact:]_block_invoke : 124 -> 120
~ +[CNAssistantConversion socialProfilesFromContact:] : 196 -> 180
~ ___51+[CNAssistantConversion socialProfilesFromContact:]_block_invoke : 328 -> 292
~ +[CNAssistantConversion keysFromPerson:] : 716 -> 660
~ +[CNAssistantConversion addressesFromPerson:] : 96 -> 88
~ ___45+[CNAssistantConversion addressesFromPerson:]_block_invoke : 332 -> 304
~ +[CNAssistantConversion emailAddressesFromPerson:] : 96 -> 88
~ ___50+[CNAssistantConversion emailAddressesFromPerson:]_block_invoke : 152 -> 136
~ +[CNAssistantConversion phoneNumbersFromPerson:] : 96 -> 88
~ ___48+[CNAssistantConversion phoneNumbersFromPerson:]_block_invoke : 188 -> 168
~ +[CNAssistantConversion relationsFromPerson:] : 96 -> 88
~ ___45+[CNAssistantConversion relationsFromPerson:]_block_invoke : 188 -> 168
~ +[CNAssistantConversion addFieldsFromPerson:toContactWithIdentifier:usingStore:saveRequest:] : 964 -> 900
~ +[CNAssistantConversion setFieldsFromPerson:toContactWithIdentifier:usingStore:saveRequest:] : 1404 -> 1292
~ +[CNAssistantConversion removeFieldsFromPerson:toContactWithIdentifier:usingStore:saveRequest:] : 296 -> 300
~ +[CNAssistantConversion applyUpdate:toContactWithIdentifier:usingStore:saveRequest:] : 400 -> 376
CStrings:
- "@16@0:8"
- "@24@0:8@16"
- "@24@0:8@?16"
- "@24@0:8q16"
- "@28@0:8@16B24"
- "@32@0:8@16@24"
- "@32@0:8@16B24B28"
- "@32@0:8@16q24"
- "@40@0:8@16@24^@32"
- "@44@0:8@16i24@28@36"
- "CASAdditions"
- "CNAssistantConversion"
- "CNAssistantID"
- "ISOCountryCode"
- "MapAndFilter"
- "T@\"NSArray\",R,N"
- "URLWithString:"
- "_crossPlatformUnifiedMeContactWithKeysToFetch:error:"
- "actionType"
- "addFields"
- "addFieldsFromPerson:toContactWithIdentifier:usingStore:saveRequest:"
- "addObject:"
- "addresses"
- "addressesForSyncFromContact:"
- "addressesFromContact:"
- "addressesFromPerson:"
- "applyUpdate:toContactWithIdentifier:usingStore:saveRequest:"
- "areKeysAvailable:"
- "array"
- "arrayByAddingObjectsFromArray:"
- "arrayWithCapacity:"
- "arrayWithObjects:count:"
- "assistantIDFromContact:"
- "assistantIDFromContactID:"
- "assistantIDFromContainer:"
- "assistantIDFromExternalIdentifier:"
- "assistantIDFromGroup:"
- "assistantIDOfType:recordID:databaseID:identifier:"
- "birthday"
- "boolValue"
- "bundleIdentifier"
- "calendarWithIdentifier:"
- "city"
- "company"
- "components:fromDate:"
- "componentsJoinedByString:"
- "componentsSeparatedByString:"
- "contactIDFromAssistantID:"
- "contactProperty"
- "contactRelationWithName:"
- "contactRelations"
- "contactWithIdentifier:keysToFetch:error:"
- "containerIDFromAssistantID:"
- "containsObject:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "countryCode"
- "createSAPersonFromCNContact:"
- "createSAPersonFromCNContact:conversionType:"
- "createSAPersonFromCNContactWithExternalIdentifier:"
- "createSASourceFromCNContainer:"
- "currentCalendar"
- "dateFromComponents:"
- "descriptorForRequiredKeysForStyle:"
- "descriptorsForRequiredKeys"
- "descriptorsForRequiredKeysForConversionType:"
- "dictionaryWithCapacity:"
- "emailAddress"
- "emailAddresses"
- "emailAddressesForSyncFromContact:"
- "emailAddressesFromContact:"
- "emailAddressesFromPerson:"
- "emails"
- "entriesForContact:propertyKey:labeledValueIdentifier:actionType:bundleIdentifier:"
- "enumerateContactsWithFetchRequest:error:usingBlock:"
- "enumerateObjectsUsingBlock:"
- "externalIdentifierFromAssistantID:"
- "familyName"
- "filterLabeledValues:droppingEmptyLabels:droppingDuplicates:"
- "filterUsingBlock:"
- "firstName"
- "firstObject"
- "formattedInternationalStringValue"
- "givenName"
- "groupIDFromAssistantID:"
- "host"
- "iOSLegacyIdentifier"
- "identifierWithError:"
- "initWithKeysToFetch:"
- "internalGUID"
- "isEqualToString:"
- "isKeyAvailable:"
- "keysFromPerson:"
- "label"
- "labeledValueWithLabel:value:"
- "lastName"
- "length"
- "mapUsingBlock:"
- "markMeContactInPeople:usingStore:"
- "me"
- "middleName"
- "mutableCopy"
- "name"
- "namePrefix"
- "nameSuffix"
- "nickName"
- "nickname"
- "number"
- "numberWithBool:"
- "objectAtIndexedSubscript:"
- "objectForKeyedSubscript:"
- "organizationName"
- "personForSyncFromContact:"
- "personFromContact:"
- "personFromContact:useABPerson:"
- "personFromMeContact:"
- "phoneNumberWithStringValue:"
- "phoneNumbers"
- "phoneNumbersForSyncFromContact:"
- "phoneNumbersFromContact:"
- "phoneNumbersFromPerson:"
- "phonemeData"
- "phones"
- "phoneticFamilyName"
- "phoneticGivenName"
- "postalAddresses"
- "postalCode"
- "predicateForContactsMatchingFullTextSearch:containerIdentifiers:groupIdentifiers:"
- "predicateForContactsWithIdentifiers:"
- "prefix"
- "query"
- "relatedNames"
- "relationsForSyncFromContact:"
- "relationsFromContact:"
- "relationsFromPerson:"
- "removeFields"
- "removeFieldsFromPerson:toContactWithIdentifier:usingStore:saveRequest:"
- "scheme"
- "service"
- "set"
- "setAddresses:"
- "setBirthday:"
- "setCity:"
- "setCompany:"
- "setContactRelations:"
- "setCountryCode:"
- "setDomainIdentifier:"
- "setEmailAddress:"
- "setEmailAddresses:"
- "setEmails:"
- "setFamilyName:"
- "setFavoriteFacetime:"
- "setFavoriteFacetimeAudio:"
- "setFavoriteVoice:"
- "setFields"
- "setFieldsFromPerson:toContactWithIdentifier:usingStore:saveRequest:"
- "setFirstName:"
- "setFirstNamePhonetic:"
- "setFullName:"
- "setGivenName:"
- "setISOCountryCode:"
- "setIdentifier:"
- "setInternalGUID:"
- "setLabel:"
- "setLastName:"
- "setLastNamePhonetic:"
- "setMe:"
- "setMiddleName:"
- "setName:"
- "setNamePrefix:"
- "setNameSuffix:"
- "setNickName:"
- "setNickname:"
- "setNumber:"
- "setObject:forKeyedSubscript:"
- "setOrganizationName:"
- "setPhoneNumbers:"
- "setPhonemeData:"
- "setPhones:"
- "setPostalAddresses:"
- "setPostalCode:"
- "setPredicate:"
- "setPrefix:"
- "setRelatedNames:"
- "setRemote:"
- "setServiceType:"
- "setState:"
- "setStateCode:"
- "setStreet:"
- "setSuffix:"
- "setTimeZone:"
- "setUnifyResults:"
- "setUrl:"
- "setUserName:"
- "setYear:"
- "sharedInstance"
- "socialProfiles"
- "socialProfilesFromContact:"
- "state"
- "stateCode"
- "street"
- "stringByAppendingString:"
- "stringFromContact:style:"
- "stringWithFormat:"
- "suffix"
- "timeZone"
- "timeZoneWithName:"
- "type"
- "unifiedContactWithIdentifier:keysToFetch:error:"
- "unifiedContactsMatchingPredicate:keysToFetch:error:"
- "updateContact:"
- "urlString"
- "username"
- "v32@0:8@16@24"
- "v48@0:8@16@24@32@40"
- "value"
- "verifyContact:hasDescriptorsForRequiredKeys:"
- "year"

```
