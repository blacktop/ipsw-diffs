## ContactProvider

> `/System/Library/Frameworks/ContactProvider.framework/ContactProvider`

```diff

-55.500.1.0.0
-  __TEXT.__text: 0x26ba4
-  __TEXT.__auth_stubs: 0xdf0
+57.100.2.0.0
+  __TEXT.__text: 0x26f78
   __TEXT.__objc_methlist: 0x1b0
-  __TEXT.__const: 0x1ba0
+  __TEXT.__const: 0x1b98
   __TEXT.__swift5_typeref: 0x782
   __TEXT.__swift5_fieldmd: 0x7bc
   __TEXT.__constg_swiftt: 0xf54

   __TEXT.__swift5_types: 0x78
   __TEXT.__swift5_proto: 0xb4
   __TEXT.__oslogstring: 0xbc3
-  __TEXT.__swift5_capture: 0x1e4
-  __TEXT.__swift_as_entry: 0x9c
-  __TEXT.__swift_as_ret: 0xa8
-  __TEXT.__cstring: 0x5b5
+  __TEXT.__swift5_capture: 0x204
+  __TEXT.__swift_as_entry: 0xa0
+  __TEXT.__swift_as_ret: 0xac
+  __TEXT.__swift_as_cont: 0x198
+  __TEXT.__cstring: 0x5c5
   __TEXT.__swift5_mpenum: 0x30
-  __TEXT.__unwind_info: 0xd00
-  __TEXT.__eh_frame: 0x1de0
-  __TEXT.__objc_classname: 0x326
-  __TEXT.__objc_methname: 0xc81
-  __TEXT.__objc_methtype: 0x19f
-  __TEXT.__objc_stubs: 0x8e0
-  __DATA_CONST.__got: 0x2f8
+  __TEXT.__unwind_info: 0xcf8
+  __TEXT.__eh_frame: 0x1c90
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x178
   __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x318
   __DATA_CONST.__objc_protorefs: 0x40
-  __AUTH_CONST.__auth_got: 0x700
-  __AUTH_CONST.__const: 0xf08
+  __DATA_CONST.__got: 0x0
+  __AUTH_CONST.__const: 0xf58
   __AUTH_CONST.__objc_const: 0x1b00
+  __AUTH_CONST.__auth_got: 0x7b8
   __AUTH.__objc_data: 0x190
   __AUTH.__data: 0x1060
-  __DATA.__data: 0x768
+  __DATA.__data: 0x7a8
   __DATA.__bss: 0x1230
   __DATA.__common: 0x88
   - /System/Library/Frameworks/Combine.framework/Combine

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 5E2E6B31-E851-358F-B8F0-10F4782D9252
-  Functions: 1032
-  Symbols:   621
-  CStrings:  285
+  UUID: B8C693AF-040B-37F5-9961-72BF0025DB41
+  Functions: 1030
+  Symbols:   695
+  CStrings:  85
 
Symbols:
+ ___swift__destructor
+ ___swift_async_cont_functlets
+ ___swift_closure_destructor
+ ___swift_closure_destructor.13
+ ___swift_closure_destructor.14
+ ___swift_closure_destructor.17
+ ___swift_closure_destructor.25
+ ___swift_closure_destructor.29
+ ___swift_closure_destructor.33
+ ___swift_closure_destructor.46
+ ___swift_closure_destructor.5
+ ___swift_closure_destructor.50
+ ___swift_closure_destructor.56
+ ___swift_closure_destructor.60
+ ___swift_closure_destructor.66
+ ___swift_closure_destructor.69
+ ___swift_exist.box.addr_destructor
+ __swift_implicitisolationactor_to_executor_cast
+ _swift_release_x19
+ _swift_release_x20
+ _swift_release_x21
+ _swift_release_x22
+ _swift_release_x23
+ _swift_release_x24
+ _swift_release_x25
+ _swift_release_x26
+ _swift_release_x27
+ _swift_release_x8
+ _swift_retain_x19
+ _swift_retain_x20
+ _swift_retain_x21
+ _swift_retain_x22
+ _swift_retain_x23
+ _swift_retain_x24
+ _swift_retain_x25
+ _swift_retain_x26
+ _swift_task_addCancellationHandler
+ _swift_task_removeCancellationHandler
CStrings:
- "#16@0:8"
- "$defaultActor"
- ".cxx_destruct"
- "@\"NSString\"16@0:8"
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@24@0:8^{_NSZone=}16"
- "@32@0:8:16@24"
- "@40@0:8:16@24@32"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "CNKeyDescriptor"
- "NSCoding"
- "NSCopying"
- "NSObject"
- "NSSecureCoding"
- "OS_os_activity"
- "OS_os_transaction"
- "Q16@0:8"
- "T#,R"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "TB,R"
- "TQ,R"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_TtC15ContactProvider10LocalStore"
- "_TtC15ContactProvider10OSActivity"
- "_TtC15ContactProvider11SyncManager"
- "_TtC15ContactProvider13OSTransaction"
- "_TtC15ContactProvider13ProviderStore"
- "_TtC15ContactProvider14ExtensionState"
- "_TtC15ContactProvider15StampedeManager"
- "_TtC15ContactProvider17ItemChangeSession"
- "_TtC15ContactProvider18ItemContentSession"
- "_TtC15ContactProvider22ContactProviderManager"
- "_TtC15ContactProvider22ItemChangeObserverImpl"
- "_TtC15ContactProvider23ItemContentObserverImpl"
- "_TtC15ContactProvider43ItemContentObserverActivityLoggingDecorator"
- "_TtP8Contacts44CNContactProviderSupportExtensionXPCProtocol_"
- "_domain"
- "_overrideDomain"
- "_state"
- "activity"
- "activityState"
- "addContact:toContainerWithIdentifier:"
- "addDomain:error:"
- "addGroup:toContainerWithIdentifier:"
- "appExtension"
- "autorelease"
- "bundleIdentifier"
- "class"
- "code"
- "conformsToProtocol:"
- "contactByApplyingUpdatesToContact:"
- "contactProviderSupport"
- "contactStore"
- "contacts"
- "container"
- "containerIdentifier"
- "containersMatchingPredicate:error:"
- "copyWithZone:"
- "dealloc"
- "debugDescription"
- "deleteContact:"
- "description"
- "didClose"
- "didFinishBatch"
- "didFinishChanges"
- "didFinishContent"
- "didFinishWithError"
- "diffContact:to:options:error:"
- "disableDomain:bundleIdentifier:error:"
- "disableDomainWithCompletionHandler:"
- "displayName"
- "domain"
- "domainContainerIdentifier"
- "domainIdentifier"
- "enableDomain:bundleIdentifier:shouldSynchronize:error:"
- "enableDomainWithCompletionHandler:"
- "encodeWithCoder:"
- "enumerator"
- "error"
- "executeFetchRequest:error:"
- "executeSaveRequest:error:"
- "extensionState"
- "externalIdentifier"
- "externalURI"
- "externalUUID"
- "groups"
- "hash"
- "identifier"
- "init"
- "initWithCoder:"
- "initWithDomainIdentifer:displayName:userInfo:bundleIdentifier:registered:enabled:"
- "initWithDomainIdentifier:"
- "initWithKeysToFetch:"
- "interfaceWithProtocol:"
- "internalActivity"
- "internalTransaction"
- "invalidateExtensionWithCompletionHandler:"
- "invalidateFor:reply:"
- "isContainerDirty"
- "isContentEnumerated"
- "isDomainEnabled"
- "isEqual:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isMoreComing"
- "isProxy"
- "isResetRequested"
- "isSupportedOnThisPlatform"
- "isSynchronizing"
- "isiOSAppOnMac"
- "isiOSAppOnVision"
- "itemAnchor"
- "itemCount"
- "itemOffset"
- "logger"
- "maxPageRetries"
- "maxSyncAnchorRetries"
- "mutableCopy"
- "name"
- "nextPage"
- "nextSyncAnchor"
- "notifyBatchSize"
- "observer"
- "page"
- "pageRetryCount"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "predicateForContactsMatchingExternalUUIDs:"
- "predicateForContainersWithIdentifiers:"
- "processInfo"
- "provider"
- "providerIdentifier"
- "providerMetadata"
- "providerSupport"
- "release"
- "removeDomain:error:"
- "resetEnumerationWithCompletionHandler:"
- "respondsToSelector:"
- "resume"
- "retain"
- "retainCount"
- "saveRequest"
- "self"
- "setDisplayName:"
- "setExportedInterface:"
- "setExportedObject:"
- "setExternalIdentifier:"
- "setExternalUUID:"
- "setIgnoreUnavailableKeys:"
- "setIgnoredKeys:"
- "setIgnoresContactProviderRestrictions:"
- "setIsContentEnumerated:"
- "setIsMoreComing:"
- "setItemAnchor:"
- "setItemOffset:"
- "setPredicate:"
- "setProviderMetadata:"
- "setSuppressChangeNotifications:"
- "setSynchronizationReason:"
- "setTransactionAuthor:"
- "setUnifyResults:"
- "setUserInfo:"
- "shouldInvalidate"
- "shouldWait"
- "stampedeManager"
- "stateToken"
- "store"
- "suggestedBatchSize"
- "suggestedPageSize"
- "superclass"
- "supportsSecureCoding"
- "syncAnchor"
- "syncAnchorRetryCount"
- "synchronizationReason"
- "synchronizeUsing:reply:"
- "updateContact:"
- "updateContainer:"
- "userInfo"
- "v16@0:8"
- "v16@?0@\"NSError\"8"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@16"
- "v32@0:8@\"CNContactProviderSupportSession\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"NSString\"16@?<v@?@\"NSError\">24"
- "v32@0:8@16@?24"
- "value"
- "verbose"
- "waitDivisor"
- "waitTimeInterval"
- "zone"

```
