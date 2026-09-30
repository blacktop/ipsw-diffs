## CoreMediaStream

> `/System/Library/PrivateFrameworks/CoreMediaStream.framework/CoreMediaStream`

```diff

-710.7.140.0.0
-  __TEXT.__text: 0xbdb74
-  __TEXT.__auth_stubs: 0xfa0
-  __TEXT.__objc_methlist: 0x63d8
-  __TEXT.__const: 0x223
-  __TEXT.__gcc_except_tab: 0x2604
-  __TEXT.__cstring: 0x9dc3
-  __TEXT.__oslogstring: 0xe564
+710.14.102.0.0
+  __TEXT.__text: 0xbe43c
+  __TEXT.__auth_stubs: 0xfb0
+  __TEXT.__objc_methlist: 0x6410
+  __TEXT.__const: 0x22b
+  __TEXT.__gcc_except_tab: 0x266c
+  __TEXT.__cstring: 0x9e2b
+  __TEXT.__oslogstring: 0xe631
   __TEXT.__dlopen_cstrs: 0x47
-  __TEXT.__unwind_info: 0x2808
-  __TEXT.__objc_classname: 0x800
-  __TEXT.__objc_methname: 0x124b5
-  __TEXT.__objc_methtype: 0x421e
-  __TEXT.__objc_stubs: 0xc3c0
-  __DATA_CONST.__got: 0x470
-  __DATA_CONST.__const: 0x2090
-  __DATA_CONST.__objc_classlist: 0x1f8
+  __TEXT.__unwind_info: 0x2828
+  __TEXT.__objc_classname: 0x813
+  __TEXT.__objc_methname: 0x127d3
+  __TEXT.__objc_methtype: 0x4243
+  __TEXT.__objc_stubs: 0xc700
+  __DATA_CONST.__got: 0x4b8
+  __DATA_CONST.__const: 0x20d8
+  __DATA_CONST.__objc_classlist: 0x200
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0xe0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3bf8
+  __DATA_CONST.__objc_selrefs: 0x3cd0
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x1c0
-  __AUTH_CONST.__auth_got: 0x7e0
+  __AUTH_CONST.__auth_got: 0x7e8
   __AUTH_CONST.__const: 0x890
-  __AUTH_CONST.__cfstring: 0x7de0
-  __AUTH_CONST.__objc_const: 0xa598
+  __AUTH_CONST.__cfstring: 0x7e80
+  __AUTH_CONST.__objc_const: 0xa628
   __AUTH_CONST.__objc_intobj: 0x30
+  __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0x650
   __DATA.__data: 0xaa0
   __DATA.__bss: 0x228

   __DATA_DIRTY.__objc_data: 0x13b0
   __DATA_DIRTY.__bss: 0x1b0
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
+  - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 3258
-  Symbols:   4060
-  CStrings:  5196
+  Functions: 3265
+  Symbols:   4082
+  CStrings:  5238
 
Symbols:
+ _CKCurrentUserDefaultName
+ _OBJC_CLASS_$_CKRecordID
+ _kMSASRecordID
+ _OBJC_CLASS_$_CKContainer
+ _kMSASModelFetchClientOrgKeyFn
+ __os_feature_enabled_impl
+ _OBJC_CLASS_$_CKContainerOptions
+ _kMSASOwnerUserID
+ _kMSASZoneName
+ _OBJC_METACLASS_$_MSASCloudKitPlugin
+ _OBJC_CLASS_$_MSASCloudKitPlugin
+ _OBJC_CLASS_$_CKFetchRecordsOperation
+ _OBJC_CLASS_$_CKRecordZoneID
+ _OBJC_CLASS_$_CKOperationConfiguration
+ _OBJC_CLASS_$_CKContainerID
CStrings:
+ "No valid userRecord for recordID: %!@(MISSING)"
+ "recordName"
+ "clientOrgKeyForRecordID:zoneName:ownerUserID:personID:"
+ "sharedCloudDatabase"
+ "isSubclassOfClass:"
+ "MSASCloudKitPlugin"
+ "Fetched userRecord: %!@(MISSING)"
+ "decryptedObjectForRecord:forKey:validateClass:"
+ "setConfiguration:"
+ "com.apple.icloud-photos.fdb"
+ "privateCloudDatabase"
+ "setFetchRecordsCompletionBlock:"
+ "initWithZoneName:ownerName:"
+ "fetchClientOrgKeyForRecordID:zoneName:ownerUserID:isOwned:"
+ "Invalid zoneID for zoneName: %!@(MISSING)"
+ "setApplicationBundleIdentifierOverride:"
+ "initWithRecordName:zoneID:"
+ "initWithContainerID:options:"
+ "recordType"
+ "waitUntilFinished"
+ "modelFetchClientOrgKey"
+ "SharedAlbumsDBR"
+ "addOperation:"
+ "recordID"
+ "setContainer:"
+ "Photos"
+ "currentOwnerCKUserID"
+ "initWithContainerIdentifier:environment:"
+ "base64EncodedStringWithOptions:"
+ "setApplicationBundleIdentifierOverrideForNetworkAttribution:"
+ "Failed to fetch userRecord: %!@(MISSING)"
+ "@44@0:8@16@24@32B40"
+ "setDesiredKeys:"
+ "@40@0:8@16@24#32"
+ "encryptedValues"
+ "ownerUserID"
+ "zoneName"
+ "setApplicationBundleIdentifierOverrideForContainerAccess:"
+ "setApplicationBundleIdentifierOverrideForPushTopicGeneration:"
+ "Unexpected object instead of encrypted data for %!{(MISSING)public}@.%!{(MISSING)public}@: %!{(MISSING)public}@"
+ "initWithRecordIDs:"

```
