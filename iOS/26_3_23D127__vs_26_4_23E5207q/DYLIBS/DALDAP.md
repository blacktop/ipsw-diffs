## DALDAP

> `/System/Library/PrivateFrameworks/DataAccess.framework/Frameworks/DALDAP.framework/DALDAP`

```diff

-2691.2.2.0.0
-  __TEXT.__text: 0x5714
-  __TEXT.__auth_stubs: 0x400
+2691.4.5.0.0
+  __TEXT.__text: 0x5c5c
+  __TEXT.__auth_stubs: 0x3b0
   __TEXT.__objc_methlist: 0x5e4
   __TEXT.__const: 0x40
-  __TEXT.__gcc_except_tab: 0xa8
+  __TEXT.__gcc_except_tab: 0xa0
   __TEXT.__cstring: 0x552
   __TEXT.__oslogstring: 0x3ca
-  __TEXT.__unwind_info: 0x1c8
+  __TEXT.__unwind_info: 0x210
   __TEXT.__objc_classname: 0x8f
   __TEXT.__objc_methname: 0x1256
   __TEXT.__objc_methtype: 0x234

   __DATA_CONST.__objc_selrefs: 0x658
   __DATA_CONST.__objc_superrefs: 0x30
   __DATA_CONST.__objc_arraydata: 0xd8
-  __AUTH_CONST.__auth_got: 0x210
+  __AUTH_CONST.__auth_got: 0x1e8
   __AUTH_CONST.__const: 0x40
   __AUTH_CONST.__cfstring: 0x940
   __AUTH_CONST.__objc_const: 0x838

   - /System/Library/PrivateFrameworks/DataAccessExpress.framework/DataAccessExpress
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7718606D-EBEB-3569-9F18-9A2DF2D98C9B
+  UUID: 4E3323B9-C010-3075-B73E-6CE1EC5ED0B1
   Functions: 110
-  Symbols:   597
+  Symbols:   592
   CStrings:  467
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
- _objc_claimAutoreleasedReturnValue
- _objc_retain
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x3
- _objc_retain_x8
Functions:
~ -[LDAPAccount ingestBackingAccountInfoProperties] : 556 -> 572
~ ___49-[LDAPAccount ingestBackingAccountInfoProperties]_block_invoke : 364 -> 372
~ -[LDAPAccount _reallyCancelSearchQuery:] : 452 -> 464
~ -[LDAPAccount _reallyCancelAllSearchQueries] : 288 -> 296
~ -[LDAPAccount _reallyPerformSearchQuery:] : 636 -> 688
~ -[LDAPAccount ldapSearchTask:finishedWithError:foundItems:] : 624 -> 640
~ -[LDAPAccount discoverInitialPropertiesWithConsumer:] : 152 -> 156
~ -[LDAPAccount ldapGetDefaultSearchBaseTask:completedWithStatus:error:defaultSearchBase:] : 508 -> 512
~ -[LDAPAccount addSearchSettings:] : 96 -> 100
~ -[LDAPAccount removeSearchSettings:] : 96 -> 100
~ -[LDAPAccount connectionURLWithSSL:] : 184 -> 192
~ -[LDAPAccount isEqualToAccount:] : 460 -> 496
~ -[LDAPAccount localizedIdenticalAccountFailureMessage] : 128 -> 136
~ -[LDAPAccount localizedInvalidPasswordMessage] : 204 -> 220
~ -[LDAPAccount onBehalfOfBundleIdentifier] : 16 -> 64
~ -[LDAPAccount setSearchTaskSet:] : 20 -> 80
~ -[LDAPAccount setMutableSearchSettings:] : 20 -> 80
~ -[LDAPTask disable] : 124 -> 128
~ -[LDAPTask performTask] : 116 -> 120
~ -[LDAPTask _performQuery] : 116 -> 120
~ -[LDAPTask reportStatusWithError:] : 152 -> 164
~ -[LDAPTask finishWithError:] : 88 -> 92
~ -[LDAPTask cancelTaskWithReason:underlyingError:] : 384 -> 400
~ -[LDAPTask taskStatusForError:] : 192 -> 200
~ -[LDAPTask initializeConnection] : 1124 -> 1172
~ ___32-[LDAPTask initializeConnection]_block_invoke : 900 -> 940
~ ___32-[LDAPTask initializeConnection]_block_invoke_2 : 164 -> 168
~ ___32-[LDAPTask initializeConnection]_block_invoke_3 : 320 -> 304
~ ___32-[LDAPTask initializeConnection]_block_invoke_4 : 300 -> 308
~ ___32-[LDAPTask initializeConnection]_block_invoke_5 : 260 -> 264
~ ___32-[LDAPTask initializeConnection]_block_invoke_6 : 328 -> 336
~ ___32-[LDAPTask initializeConnection]_block_invoke.17 : 256 -> 260
~ ___32-[LDAPTask initializeConnection]_block_invoke_2.18 : 316 -> 324
~ -[LDAPTask daLevelErrorForLDAPError:] : 104 -> 108
~ -[LDAPTask setLdConnection:] : 20 -> 80
~ -[LDAPTask setDateConnectionWentOut:] : 20 -> 80
~ -[LDAPSearchTask disable] : 112 -> 120
~ -[LDAPSearchTask _copySearchStringForQueryInput:] : 712 -> 744
~ -[LDAPSearchTask _performQuery] : 996 -> 1032
~ ___31-[LDAPSearchTask _performQuery]_block_invoke_3 : 932 -> 968
~ ___31-[LDAPSearchTask _performQuery]_block_invoke.105 : 156 -> 160
~ ___31-[LDAPSearchTask _performQuery]_block_invoke_2.106 : 408 -> 420
~ -[LDAPSearchTask _appendKey:value:toSearchResultElement:] : 1088 -> 1096
~ -[LDAPSearchTask _promptForPasswordDueToError:] : 304 -> 324
~ -[LDAPSearchTask _failImmediately] : 188 -> 192
~ -[LDAPSearchTask performTask] : 228 -> 244
~ -[LDAPSearchTask finishWithError:] : 484 -> 524
~ -[LDAPSearchTask numDownloadedElements] : 56 -> 60
~ -[LDAPSearchTask setFoundContacts:] : 20 -> 80
~ -[LDAPSearchTask setOperation:] : 20 -> 80
~ -[LDAPGetDefaultSearchBaseTask _performQuery] : 332 -> 340
~ ___45-[LDAPGetDefaultSearchBaseTask _performQuery]_block_invoke_3 : 984 -> 1016
~ -[LDAPGetDefaultSearchBaseTask finishWithError:] : 472 -> 512
~ -[LDAPGetDefaultSearchBaseTask numDownloadedElements] : 52 -> 56
~ -[LDAPGetDefaultSearchBaseTask setDefaultNamingContext:] : 20 -> 80
~ -[LDAPSearchSettings initWithSettingsDict:] : 204 -> 216
~ -[LDAPSearchSettings settingsDict] : 272 -> 296
~ -[LDAPSearchSettings hasSameScopeAndBaseAsOther:] : 276 -> 292
~ -[LDAPSearchSettings hash] : 80 -> 84
~ -[LDAPSearchSettings isEqual:] : 232 -> 248
~ -[LDAPSearchSettings description] : 204 -> 220
~ -[LDAPSearchSettings setSearchDescription:] : 12 -> 64
~ -[LDAPSearchSettings setSearchBase:] : 12 -> 64
~ +[LDAPLocalDBHelper sharedInstance] : 92 -> 96
~ -[NSString(LDAPExtensions) ldapHumanReadableStringFromSearchBase] : 524 -> 544
~ -[LDAPAccount _reallyPerformSearchQuery:].cold.1 : 100 -> 104

```
