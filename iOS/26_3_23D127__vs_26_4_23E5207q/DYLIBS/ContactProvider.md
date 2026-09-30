## ContactProvider

> `/System/Library/Frameworks/ContactProvider.framework/ContactProvider`

```diff

-55.200.2.0.0
-  __TEXT.__text: 0x26c80
-  __TEXT.__auth_stubs: 0xde0
+55.500.1.0.0
+  __TEXT.__text: 0x26b88
+  __TEXT.__auth_stubs: 0xdf0
   __TEXT.__objc_methlist: 0x1b0
-  __TEXT.__const: 0x1b80
+  __TEXT.__const: 0x1ba0
   __TEXT.__swift5_typeref: 0x782
   __TEXT.__swift5_fieldmd: 0x7bc
   __TEXT.__constg_swiftt: 0xf54

   __TEXT.__swift5_protos: 0x24
   __TEXT.__swift5_types: 0x78
   __TEXT.__swift5_proto: 0xb4
-  __TEXT.__cstring: 0xce1
   __TEXT.__oslogstring: 0xbc3
   __TEXT.__swift5_capture: 0x1e4
   __TEXT.__swift_as_entry: 0x9c
   __TEXT.__swift_as_ret: 0xa8
+  __TEXT.__cstring: 0x5b5
   __TEXT.__swift5_mpenum: 0x30
-  __TEXT.__unwind_info: 0xd20
-  __TEXT.__eh_frame: 0x1e70
-  __TEXT.__objc_classname: 0x5c
-  __TEXT.__objc_methname: 0x7e6
-  __TEXT.__objc_methtype: 0x100
+  __TEXT.__unwind_info: 0xd00
+  __TEXT.__eh_frame: 0x1de0
+  __TEXT.__objc_classname: 0x326
+  __TEXT.__objc_methname: 0xc81
+  __TEXT.__objc_methtype: 0x19f
+  __TEXT.__objc_stubs: 0x8e0
   __DATA_CONST.__got: 0x2f8
   __DATA_CONST.__const: 0x180
   __DATA_CONST.__objc_classlist: 0x68

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x318
   __DATA_CONST.__objc_protorefs: 0x40
-  __AUTH_CONST.__auth_got: 0x6f0
+  __AUTH_CONST.__auth_got: 0x700
   __AUTH_CONST.__const: 0xf08
   __AUTH_CONST.__objc_const: 0x1b00
   __AUTH.__objc_data: 0x190
-  __AUTH.__data: 0x1068
-  __DATA.__data: 0x798
+  __AUTH.__data: 0x1060
+  __DATA.__data: 0x768
   __DATA.__bss: 0x1230
   __DATA.__common: 0x88
   - /System/Library/Frameworks/Combine.framework/Combine

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 1E9B67E7-5BC9-387A-8F08-2472AA3B4CC1
-  Functions: 1047
-  Symbols:   550
-  CStrings:  288
+  UUID: 0BAD2C4C-37F3-366B-B11D-5B412BB389A6
+  Functions: 1032
+  Symbols:   623
+  CStrings:  285
 
Symbols:
+ _objc_msgSend$addContact:toContainerWithIdentifier:
+ _objc_msgSend$addDomain:error:
+ _objc_msgSend$addGroup:toContainerWithIdentifier:
+ _objc_msgSend$bundleIdentifier
+ _objc_msgSend$code
+ _objc_msgSend$contactByApplyingUpdatesToContact:
+ _objc_msgSend$contactStore
+ _objc_msgSend$containersMatchingPredicate:error:
+ _objc_msgSend$deleteContact:
+ _objc_msgSend$diffContact:to:options:error:
+ _objc_msgSend$disableDomain:bundleIdentifier:error:
+ _objc_msgSend$disableDomainWithCompletionHandler:
+ _objc_msgSend$displayName
+ _objc_msgSend$domain
+ _objc_msgSend$domainContainerIdentifier
+ _objc_msgSend$domainIdentifier
+ _objc_msgSend$enableDomain:bundleIdentifier:shouldSynchronize:error:
+ _objc_msgSend$enableDomainWithCompletionHandler:
+ _objc_msgSend$executeFetchRequest:error:
+ _objc_msgSend$executeSaveRequest:error:
+ _objc_msgSend$externalIdentifier
+ _objc_msgSend$externalURI
+ _objc_msgSend$externalUUID
+ _objc_msgSend$identifier
+ _objc_msgSend$init
+ _objc_msgSend$initWithDomainIdentifer:displayName:userInfo:bundleIdentifier:registered:enabled:
+ _objc_msgSend$initWithDomainIdentifier:
+ _objc_msgSend$initWithKeysToFetch:
+ _objc_msgSend$interfaceWithProtocol:
+ _objc_msgSend$invalidateExtensionWithCompletionHandler:
+ _objc_msgSend$isContentEnumerated
+ _objc_msgSend$isDomainEnabled
+ _objc_msgSend$isMoreComing
+ _objc_msgSend$isResetRequested
+ _objc_msgSend$isiOSAppOnMac
+ _objc_msgSend$isiOSAppOnVision
+ _objc_msgSend$itemAnchor
+ _objc_msgSend$itemOffset
+ _objc_msgSend$mutableCopy
+ _objc_msgSend$predicateForContactsMatchingExternalUUIDs:
+ _objc_msgSend$predicateForContainersWithIdentifiers:
+ _objc_msgSend$processInfo
+ _objc_msgSend$providerIdentifier
+ _objc_msgSend$providerMetadata
+ _objc_msgSend$removeDomain:error:
+ _objc_msgSend$resetEnumerationWithCompletionHandler:
+ _objc_msgSend$resume
+ _objc_msgSend$setDisplayName:
+ _objc_msgSend$setExportedInterface:
+ _objc_msgSend$setExportedObject:
+ _objc_msgSend$setExternalIdentifier:
+ _objc_msgSend$setExternalUUID:
+ _objc_msgSend$setIgnoreUnavailableKeys:
+ _objc_msgSend$setIgnoredKeys:
+ _objc_msgSend$setIgnoresContactProviderRestrictions:
+ _objc_msgSend$setIsContentEnumerated:
+ _objc_msgSend$setIsMoreComing:
+ _objc_msgSend$setItemAnchor:
+ _objc_msgSend$setItemOffset:
+ _objc_msgSend$setPredicate:
+ _objc_msgSend$setProviderMetadata:
+ _objc_msgSend$setSuppressChangeNotifications:
+ _objc_msgSend$setSynchronizationReason:
+ _objc_msgSend$setTransactionAuthor:
+ _objc_msgSend$setUnifyResults:
+ _objc_msgSend$setUserInfo:
+ _objc_msgSend$synchronizationReason
+ _objc_msgSend$updateContact:
+ _objc_msgSend$updateContainer:
+ _objc_msgSend$userInfo
+ _objc_msgSend$value
+ _swift_bridgeObjectRetain_n
+ _swift_release_n
+ _swift_retain_n
- _swift_bridgeObjectRelease_n

```
