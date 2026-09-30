## progressd

> `/System/Library/Frameworks/ClassKit.framework/progressd`

```diff

-150.4.6.0.0
-  __TEXT.__text: 0x16cd98
-  __TEXT.__auth_stubs: 0x16c0
-  __TEXT.__objc_stubs: 0x14c80
-  __TEXT.__objc_methlist: 0x141a4
+150.4.11.0.0
+  __TEXT.__text: 0x16f058
+  __TEXT.__auth_stubs: 0x16e0
+  __TEXT.__objc_stubs: 0x14e40
+  __TEXT.__objc_methlist: 0x1434c
   __TEXT.__const: 0x10b0
   __TEXT.__swift5_typeref: 0x39e
   __TEXT.__swift5_reflstr: 0x288
   __TEXT.__swift5_assocty: 0x48
   __TEXT.__constg_swiftt: 0x5c0
   __TEXT.__swift5_fieldmd: 0x354
-  __TEXT.__objc_methname: 0x1b946
-  __TEXT.__cstring: 0x1bbb4
+  __TEXT.__objc_methname: 0x1bb58
+  __TEXT.__cstring: 0x1bfaa
   __TEXT.__swift5_proto: 0xb8
   __TEXT.__swift5_types: 0x50
   __TEXT.__swift5_capture: 0xe0
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__objc_classname: 0x1892
-  __TEXT.__objc_methtype: 0x3d35
-  __TEXT.__gcc_except_tab: 0x3b1c
-  __TEXT.__oslogstring: 0xd9a4
+  __TEXT.__objc_classname: 0x18b3
+  __TEXT.__objc_methtype: 0x3de6
+  __TEXT.__gcc_except_tab: 0x3c10
+  __TEXT.__oslogstring: 0xda25
   __TEXT.__ustring: 0x58
-  __TEXT.__unwind_info: 0x4bd0
+  __TEXT.__unwind_info: 0x4c30
   __TEXT.__eh_frame: 0x300
-  __DATA_CONST.__auth_got: 0xb78
-  __DATA_CONST.__got: 0xa78
+  __DATA_CONST.__auth_got: 0xb88
+  __DATA_CONST.__got: 0xa98
   __DATA_CONST.__auth_ptr: 0x1e0
-  __DATA_CONST.__const: 0x4d68
-  __DATA_CONST.__cfstring: 0x133c0
+  __DATA_CONST.__const: 0x4db0
+  __DATA_CONST.__cfstring: 0x13540
   __DATA_CONST.__objc_classlist: 0x798
-  __DATA_CONST.__objc_catlist: 0x200
+  __DATA_CONST.__objc_catlist: 0x218
   __DATA_CONST.__objc_protolist: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x50
-  __DATA_CONST.__objc_superrefs: 0x968
+  __DATA_CONST.__objc_superrefs: 0x980
   __DATA_CONST.__objc_intobj: 0x330
   __DATA_CONST.__objc_arraydata: 0x130
   __DATA_CONST.__objc_arrayobj: 0x168
   __DATA_CONST.__objc_dictobj: 0x50
-  __DATA.__objc_const: 0x21028
-  __DATA.__objc_selrefs: 0x7278
-  __DATA.__objc_ivar: 0x1304
+  __DATA.__objc_const: 0x21408
+  __DATA.__objc_selrefs: 0x72f0
+  __DATA.__objc_ivar: 0x1308
   __DATA.__objc_data: 0x4ef8
   __DATA.__data: 0x14f0
   __DATA.__objc_stublist: 0x28

   - /System/Library/PrivateFrameworks/CrashReporterSupport.framework/CrashReporterSupport
   - /System/Library/PrivateFrameworks/InternalSwiftProtobuf.framework/InternalSwiftProtobuf
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
+  - /System/Library/PrivateFrameworks/ManagedOrganizationContacts.framework/ManagedOrganizationContacts
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /System/Library/PrivateFrameworks/UserManagement.framework/UserManagement

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 7912
-  Symbols:   792
-  CStrings:  9490
+  Functions: 7947
+  Symbols:   798
+  CStrings:  9526
 
Symbols:
+ _CLSPredicateKeyPathObjectID
+ _ManagedOrganizationContactsQueryRequest
+ _ManagedOrganizationContactsQueryResponse
+ _OBJC_CLASS_$_ManagedOrganizationContactsClassObject
+ _OBJC_CLASS_$_ManagedOrganizationContactsGroupObject
+ _OBJC_CLASS_$_ManagedOrganizationContactsPersonObject
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_initStructMetadataWithLayoutString
+ _swift_cvw_initWithCopy
+ _swift_cvw_initWithTake
+ _swift_cvw_initializeBufferWithCopyOfBuffer
- _swift_generic_assignWithCopy
- _swift_generic_assignWithTake
- _swift_generic_destroy
- _swift_generic_initWithCopy
- _swift_generic_initWithTake
- _swift_generic_initializeBufferWithCopyOfBuffer
- _swift_initStructMetadataWithLayoutString
CStrings:
+ "\x02D"
+ " && isSearchable == 1"
+ "%K IN %@"
+ "(%K BEGINSWITH %@ || %K LIKE %@)"
+ "(%K LIKE %@)"
+ "@\"ManagedOrganizationContactsQuery\""
+ "@?64@0:8@16@24@32@40Q48Q56"
+ "Invalid user.  No server query"
+ "ManagedOrganizationContactsClassObject"
+ "ManagedOrganizationContactsGroupObject"
+ "ManagedOrganizationContactsPersonObject"
+ "ManagedOrganizationContactsQuery"
+ "Server search not requested, finishing up."
+ "Skipping remote_executeRosterQuery from invalid client"
+ "T@\"ManagedOrganizationContactsQuery\",R,N,V_rosterQuery"
+ "Vv40@0:8@\"NSObject<ManagedOrganizationContactsResponseInterface>\"16@\"ManagedOrganizationContactsQuery\"24@?<v@?>32"
+ "_rosterQuery"
+ "asmRosterSearchFinishBlock:query:asmConfig:buffer:buffSize:nextOffset:"
+ "create view ManagedOrganizationContactsClassObject (\n    objectID,\n    className,\n    searchText\n) AS\nSELECT\n    objectID,\n    className,\n    searchText\nFROM CLSClass"
+ "create view ManagedOrganizationContactsGroupObject (\n    objectID,\n    groupName,\n    emailAddress,\n    searchText\n) AS\nSELECT\n    objectID,\n    groupName,\n    emailAddress,\n    searchText\nFROM CLSGroup"
+ "create view ManagedOrganizationContactsPersonObject (\n    objectID,\n    givenName,\n    middleName,\n    familyName,\n    appleID,\n    emailAddress,\n    searchText,\n    isSearchable\n) AS\nSELECT\n    objectID,\n    givenName,\n    middleName,\n    familyName,\n    appleID,\n    emailAddress,\n    searchText,\n    isSearchable\nFROM CLSPerson"
+ "displayNameForRow:"
+ "groupExpansionPredicate:"
+ "groupID"
+ "groupSearchPredicate:"
+ "initWithDatabase:rosterQuery:enumerationBlock:finishBlock:"
+ "localizedStringFromPersonNameComponents:style:options:"
+ "personSearchPredicate:"
+ "remote_executeRosterQuery:executeQuery:completion:"
+ "requestDataForRosterQuery"
+ "requestDataForSearchSpec"
+ "rosterQuery"
+ "rosterSearchBehaviors"
+ "rosterSearchOptions"
+ "select personID from CLSClassMember where parentObjectID=?"
+ "select personID from CLSGroupMember where parentObjectID=?"
+ "setRosterSearchOptions:"
- "\x02C"

```
