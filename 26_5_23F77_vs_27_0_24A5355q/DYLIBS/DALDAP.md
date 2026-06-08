## DALDAP

> `/System/Library/PrivateFrameworks/DataAccess.framework/Frameworks/DALDAP.framework/DALDAP`

```diff

-2691.4.6.0.0
-  __TEXT.__text: 0x5c5c
-  __TEXT.__auth_stubs: 0x3b0
+2703.0.0.0.0
+  __TEXT.__text: 0x55a8
   __TEXT.__objc_methlist: 0x5e4
   __TEXT.__const: 0x40
-  __TEXT.__gcc_except_tab: 0xa0
-  __TEXT.__cstring: 0x552
+  __TEXT.__gcc_except_tab: 0xa8
+  __TEXT.__cstring: 0x55c
   __TEXT.__oslogstring: 0x3ca
-  __TEXT.__unwind_info: 0x210
-  __TEXT.__objc_classname: 0x8f
-  __TEXT.__objc_methname: 0x1256
-  __TEXT.__objc_methtype: 0x234
-  __TEXT.__objc_stubs: 0x13a0
-  __DATA_CONST.__got: 0x138
+  __TEXT.__unwind_info: 0x1c8
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x2f8
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_catlist: 0x8

   __DATA_CONST.__objc_selrefs: 0x658
   __DATA_CONST.__objc_superrefs: 0x30
   __DATA_CONST.__objc_arraydata: 0xd8
-  __AUTH_CONST.__auth_got: 0x1e8
+  __DATA_CONST.__got: 0x138
   __AUTH_CONST.__const: 0x40
   __AUTH_CONST.__cfstring: 0x940
   __AUTH_CONST.__objc_const: 0x838
   __AUTH_CONST.__objc_arrayobj: 0x30
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x1e0
   __DATA.__objc_ivar: 0x38
   __DATA.__data: 0xc0

   - /System/Library/PrivateFrameworks/DataAccessExpress.framework/DataAccessExpress
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: AEAFDC7A-3F0B-3FE9-8AC8-6339F33636DB
+  UUID: D3154798-3553-330B-B97F-8DC1A6C31004
   Functions: 110
-  Symbols:   592
-  CStrings:  467
+  Symbols:   597
+  CStrings:  181
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x3
+ _objc_retain_x8
- _objc_retainAutoreleasedReturnValue
Functions:
~ -[LDAPAccount ingestBackingAccountInfoProperties] : 572 -> 560
~ ___49-[LDAPAccount ingestBackingAccountInfoProperties]_block_invoke : 372 -> 368
~ -[LDAPAccount initWithBackingAccountInfo:] : 156 -> 164
~ -[LDAPAccount _reallyCancelSearchQuery:] : 464 -> 456
~ -[LDAPAccount _reallyCancelAllSearchQueries] : 296 -> 292
~ -[LDAPAccount _reallyPerformSearchQuery:] : 688 -> 592
~ -[LDAPAccount ldapSearchTask:finishedWithError:foundItems:] : 640 -> 580
~ -[LDAPAccount discoverInitialPropertiesWithConsumer:] : 156 -> 152
~ -[LDAPAccount addSearchSettings:] : 100 -> 96
~ -[LDAPAccount removeSearchSettings:] : 100 -> 96
~ -[LDAPAccount connectionURLWithSSL:] : 192 -> 184
~ -[LDAPAccount isEqualToAccount:] : 496 -> 460
~ -[LDAPAccount localizedIdenticalAccountFailureMessage] : 136 -> 128
~ -[LDAPAccount localizedInvalidPasswordMessage] : 220 -> 204
~ -[LDAPAccount onBehalfOfBundleIdentifier] : 64 -> 16
~ -[LDAPAccount searchTaskSet] : 16 -> 20
~ -[LDAPAccount setSearchTaskSet:] : 80 -> 20
~ -[LDAPAccount mutableSearchSettings] : 16 -> 20
~ -[LDAPAccount setMutableSearchSettings:] : 80 -> 20
~ -[LDAPTask dealloc] : 88 -> 92
~ -[LDAPTask disable] : 128 -> 124
~ -[LDAPTask performTask] : 120 -> 116
~ -[LDAPTask _performQuery] : 120 -> 116
~ -[LDAPTask reportStatusWithError:] : 164 -> 152
~ -[LDAPTask finishWithError:] : 92 -> 88
~ -[LDAPTask cancelTaskWithReason:underlyingError:] : 400 -> 384
~ -[LDAPTask taskStatusForError:] : 200 -> 192
~ -[LDAPTask initializeConnection] : 1172 -> 1108
~ ___32-[LDAPTask initializeConnection]_block_invoke : 940 -> 900
~ ___32-[LDAPTask initializeConnection]_block_invoke_2 : 168 -> 164
~ ___32-[LDAPTask initializeConnection]_block_invoke_3 : 304 -> 300
~ ___32-[LDAPTask initializeConnection]_block_invoke_4 : 308 -> 300
~ ___32-[LDAPTask initializeConnection]_block_invoke_5 : 264 -> 260
~ ___32-[LDAPTask initializeConnection]_block_invoke_6 : 336 -> 260
~ ___32-[LDAPTask initializeConnection]_block_invoke.17 : 260 -> 256
~ ___32-[LDAPTask initializeConnection]_block_invoke_2.18 : 324 -> 248
~ -[LDAPTask daLevelErrorForLDAPError:] : 108 -> 104
~ -[LDAPTask ldConnection] : 16 -> 20
~ -[LDAPTask setLdConnection:] : 80 -> 20
~ -[LDAPTask dateConnectionWentOut] : 16 -> 20
~ -[LDAPTask setDateConnectionWentOut:] : 80 -> 20
~ -[LDAPTask isFinished] : 16 -> 20
~ -[LDAPTask setIsFinished:] : 16 -> 20
~ -[LDAPSearchTask initWithQuery:] : 156 -> 160
~ -[LDAPSearchTask disable] : 120 -> 112
~ -[LDAPSearchTask _copySearchStringForQueryInput:] : 744 -> 716
~ -[LDAPSearchTask _performQuery] : 1032 -> 952
~ ___31-[LDAPSearchTask _performQuery]_block_invoke_3 : 968 -> 924
~ ___31-[LDAPSearchTask _performQuery]_block_invoke.105 : 160 -> 156
~ ___31-[LDAPSearchTask _performQuery]_block_invoke_2.106 : 420 -> 360
~ -[LDAPSearchTask _appendKey:value:toSearchResultElement:] : 1096 -> 1044
~ -[LDAPSearchTask _promptForPasswordDueToError:] : 324 -> 304
~ -[LDAPSearchTask _failImmediately] : 192 -> 188
~ -[LDAPSearchTask performTask] : 244 -> 228
~ -[LDAPSearchTask finishWithError:] : 524 -> 484
~ -[LDAPSearchTask numDownloadedElements] : 60 -> 56
~ -[LDAPSearchTask query] : 16 -> 20
~ -[LDAPSearchTask foundContacts] : 16 -> 20
~ -[LDAPSearchTask setFoundContacts:] : 80 -> 20
~ -[LDAPSearchTask operation] : 16 -> 20
~ -[LDAPSearchTask setOperation:] : 80 -> 20
~ -[LDAPGetDefaultSearchBaseTask _performQuery] : 340 -> 288
~ ___45-[LDAPGetDefaultSearchBaseTask _performQuery]_block_invoke_3 : 1016 -> 984
~ -[LDAPGetDefaultSearchBaseTask finishWithError:] : 512 -> 472
~ -[LDAPGetDefaultSearchBaseTask numDownloadedElements] : 56 -> 52
~ -[LDAPGetDefaultSearchBaseTask defaultNamingContext] : 16 -> 20
~ -[LDAPGetDefaultSearchBaseTask setDefaultNamingContext:] : 80 -> 20
~ -[LDAPSearchSettings initWithSettingsDict:] : 216 -> 204
~ -[LDAPSearchSettings settingsDict] : 296 -> 272
~ -[LDAPSearchSettings hasSameScopeAndBaseAsOther:] : 292 -> 276
~ -[LDAPSearchSettings hash] : 84 -> 80
~ -[LDAPSearchSettings isEqual:] : 248 -> 232
~ -[LDAPSearchSettings description] : 220 -> 204
~ -[LDAPSearchSettings setSearchDescription:] : 64 -> 12
~ -[LDAPSearchSettings setSearchBase:] : 64 -> 12
~ +[LDAPLocalDBHelper sharedInstance] : 96 -> 92
~ -[NSString(LDAPExtensions) ldapHumanReadableStringFromSearchBase] : 544 -> 528
~ -[LDAPAccount _reallyPerformSearchQuery:].cold.1 : 104 -> 100
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@"
- "@\"DAContactsSearchQuery\""
- "@\"DATaskManager\""
- "@\"NSDate\""
- "@\"NSMutableArray\""
- "@\"NSMutableSet\""
- "@\"NSObject<OS_ldap_connection>\""
- "@\"NSObject<OS_ldap_operation>\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@16@0:8"
- "@20@0:8B16"
- "@20@0:8i16"
- "@24@0:8:16"
- "@24@0:8@16"
- "@32@0:8:16@24"
- "@40@0:8:16@24@32"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "DATask"
- "LDAPAccount"
- "LDAPExtensions"
- "LDAPGetDefaultSearchBaseTask"
- "LDAPLocalDBHelper"
- "LDAPSearchSettings"
- "LDAPSearchTask"
- "LDAPTask"
- "NSObject"
- "Q"
- "Q16@0:8"
- "T#,R"
- "T@\"DAContactsSearchQuery\",R,N,V_query"
- "T@\"DATaskManager\",W,N,V_taskManager"
- "T@\"NSDate\",&,N,V_dateConnectionWentOut"
- "T@\"NSMutableArray\",&,N,V_foundContacts"
- "T@\"NSMutableArray\",&,N,V_mutableSearchSettings"
- "T@\"NSMutableSet\",&,N,V_searchTaskSet"
- "T@\"NSObject<OS_ldap_connection>\",&,N,V_ldConnection"
- "T@\"NSObject<OS_ldap_operation>\",&,N,V_operation"
- "T@\"NSString\",&,N,V_defaultNamingContext"
- "T@\"NSString\",&,N,V_searchBase"
- "T@\"NSString\",&,N,V_searchDescription"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@,W,N,V_delegate"
- "TB,N,V_isFinished"
- "TQ,N,V_scope"
- "TQ,R"
- "Ti,R,N"
- "URLWithString:"
- "UTF8String"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_appendKey:value:toSearchResultElement:"
- "_copySearchStringForQueryInput:"
- "_dateConnectionWentOut"
- "_defaultNamingContext"
- "_delegate"
- "_failImmediately"
- "_foundContacts"
- "_isFinished"
- "_ldConnection"
- "_mutableSearchSettings"
- "_operation"
- "_performQuery"
- "_promptForPasswordDueToError:"
- "_query"
- "_reallyCancelAllSearchQueries"
- "_reallyCancelSearchQuery:"
- "_reallyPerformSearchQuery:"
- "_scope"
- "_searchBase"
- "_searchDescription"
- "_searchStringForWord:"
- "_searchTaskSet"
- "_taskManager"
- "account"
- "account:isValid:validationError:"
- "accountDescription"
- "addObject:"
- "addSearchSettings:"
- "allKeys"
- "appendFormat:"
- "appendString:"
- "arrayWithArray:"
- "autorelease"
- "backingAccountInfo"
- "bundleForClass:"
- "cancelTask:"
- "cancelTaskWithReason:underlyingError:"
- "class"
- "code"
- "componentsJoinedByString:"
- "componentsSeparatedByString:"
- "conformsToProtocol:"
- "connectionURL"
- "connectionURLWithSSL:"
- "consumer"
- "consumerForTask:"
- "contactsSearchQueryWithSearchString:searchBase:searchScope:consumer:"
- "containsObject:"
- "copy"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "currentHandler"
- "daLevelErrorForLDAPError:"
- "date"
- "dateConnectionWentOut"
- "dealloc"
- "debugDescription"
- "defaultNamingContext"
- "delegate"
- "description"
- "dictionaryWithCapacity:"
- "dictionaryWithObjects:forKeys:count:"
- "disable"
- "discoverInitialPropertiesWithConsumer:"
- "domain"
- "dropAssertionsAndRenewCredentialsInQueue:withHandler:"
- "emailAddress"
- "errorWithDomain:code:userInfo:"
- "finishWithError:"
- "foundContacts"
- "handleFailureInMethod:object:file:lineNumber:description:"
- "hasSameScopeAndBaseAsOther:"
- "hash"
- "host"
- "i16@0:8"
- "ignoreBadLDAPCerts"
- "includePhotos"
- "ingestBackingAccountInfoProperties"
- "init"
- "initWithBackingAccountInfo:"
- "initWithCapacity:"
- "initWithDomain:code:userInfo:"
- "initWithObjects:"
- "initWithQuery:"
- "initWithSettingsDict:"
- "initializeConnection"
- "intValue"
- "isDisabled"
- "isEqual:"
- "isEqualToAccount:"
- "isEqualToString:"
- "isFinished"
- "isKindOfClass:"
- "isLDAPAccount"
- "isMemberOfClass:"
- "isProxy"
- "ldConnection"
- "ldapGetDefaultSearchBaseTask:completedWithStatus:error:defaultSearchBase:"
- "ldapHumanReadableStringFromSearchBase"
- "ldapSanitizedAddress"
- "ldapSearchTask:finishedWithError:foundItems:"
- "length"
- "localizedIdenticalAccountFailureMessage"
- "localizedInvalidPasswordMessage"
- "localizedStringForKey:value:table:"
- "lowercaseString"
- "maxResults"
- "mutableCopy"
- "mutableSearchSettings"
- "noteFailedNetworkRequest"
- "noteSuccessfulRequestWithNumDownloadedElements:"
- "noteTimeSpentInNetworking:"
- "numDownloadedElements"
- "numberWithInteger:"
- "numberWithUnsignedInteger:"
- "objectAtIndexedSubscript:"
- "objectForKeyedSubscript:"
- "onBehalfOfBundleIdentifier"
- "operation"
- "password"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:afterDelay:inModes:"
- "performSelector:withObject:withObject:"
- "performTask"
- "port"
- "q24@0:8@16"
- "query"
- "range"
- "rangeOfString:options:"
- "release"
- "removeConsumerForTask:"
- "removeObject:"
- "removeObjectAtIndex:"
- "removeSearchSettings:"
- "replaceOccurrencesOfString:withString:options:range:"
- "reportStatusWithError:"
- "requestCancelTaskWithReason:"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "scope"
- "searchBase"
- "searchDescription"
- "searchQuery:finishedWithError:"
- "searchQuery:returnedResults:"
- "searchScope"
- "searchSettings"
- "searchString"
- "searchTaskSet"
- "self"
- "setAccount:"
- "setAccountPropertiesTransformer:"
- "setAppleFloor:"
- "setBuildingName:"
- "setCity:"
- "setCompany:"
- "setConsumer:forTask:"
- "setCountry:"
- "setDateConnectionWentOut:"
- "setDefaultNamingContext:"
- "setDelegate:"
- "setDisplayName:"
- "setEmailAddress:"
- "setFaxPhone:"
- "setFirstName:"
- "setFoundContacts:"
- "setHomePhone:"
- "setHomePostalAddress:"
- "setIdentifierOnServer:"
- "setImUsername:"
- "setIsFinished:"
- "setJpegPhoto:"
- "setLastName:"
- "setLdConnection:"
- "setMobilePhone:"
- "setMutableSearchSettings:"
- "setObject:forKeyedSubscript:"
- "setOperation:"
- "setPagerNumber:"
- "setPostalAddress:"
- "setScope:"
- "setSearchBase:"
- "setSearchDescription:"
- "setSearchTaskSet:"
- "setShouldDoInitialAutodiscovery:"
- "setStreet:"
- "setTaskManager:"
- "setTitle:"
- "setUri:"
- "setWorkPhone:"
- "setZip:"
- "settingsDict"
- "sharedInstance"
- "sharedInstanceForAccountType:creatingClass:"
- "shouldFailAllTasks"
- "shouldForceNetworking"
- "shouldHoldPowerAssertion"
- "startModal"
- "statusReport"
- "stringByTrimmingCharactersInSet:"
- "stringWithFormat:"
- "submitQueuedTask:"
- "substringFromIndex:"
- "superclass"
- "taskDidFinish:"
- "taskManager"
- "taskStatusForError:"
- "timeIntervalSinceDate:"
- "timeLimit"
- "useSSL"
- "user"
- "username"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8i16"
- "v24@0:8@\"DATaskManager\"16"
- "v24@0:8@\"NSError\"16"
- "v24@0:8@16"
- "v24@0:8Q16"
- "v28@0:8i16@\"NSError\"20"
- "v28@0:8i16@20"
- "v40@0:8@16@24@32"
- "v48@0:8@16q24@32@40"
- "whitespaceAndNewlineCharacterSet"
- "whitespaceCharacterSet"
- "zone"

```
