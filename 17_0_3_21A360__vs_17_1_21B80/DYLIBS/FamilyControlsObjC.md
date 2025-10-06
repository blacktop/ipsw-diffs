## FamilyControlsObjC

> `/System/Library/PrivateFrameworks/FamilyControlsObjC.framework/FamilyControlsObjC`

```diff

-1112.0.0.0.0
-  __TEXT.__text: 0x278c
-  __TEXT.__auth_stubs: 0x2a0
-  __TEXT.__objc_methlist: 0x1c8
-  __TEXT.__const: 0x58
-  __TEXT.__oslogstring: 0x31f
-  __TEXT.__gcc_except_tab: 0x1c
-  __TEXT.__cstring: 0xce
-  __TEXT.__unwind_info: 0xf0
-  __TEXT.__objc_classname: 0xcf
-  __TEXT.__objc_methname: 0x82a
-  __TEXT.__objc_methtype: 0x173
-  __TEXT.__objc_stubs: 0x560
-  __DATA_CONST.__got: 0x20
-  __DATA_CONST.__const: 0x168
-  __DATA_CONST.__objc_classlist: 0x30
+1121.0.0.0.0
+  __TEXT.__text: 0x2740
+  __TEXT.__auth_stubs: 0x300
+  __TEXT.__objc_methlist: 0x1f4
+  __TEXT.__const: 0x50
+  __TEXT.__gcc_except_tab: 0x44
+  __TEXT.__cstring: 0xf7
+  __TEXT.__oslogstring: 0x278
+  __TEXT.__unwind_info: 0x110
+  __TEXT.__objc_classname: 0xa1
+  __TEXT.__objc_methname: 0x951
+  __TEXT.__objc_methtype: 0x18a
+  __TEXT.__objc_stubs: 0x6a0
+  __DATA_CONST.__got: 0x28
+  __DATA_CONST.__const: 0x140
+  __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x4a0
-  __DATA_CONST.__objc_selrefs: 0x1e0
-  __AUTH_CONST.__objc_const: 0x240
+  __DATA_CONST.__objc_selrefs: 0x230
+  __AUTH_CONST.__objc_const: 0x1f8
   __AUTH_CONST.__const: 0x20
-  __AUTH_CONST.__cfstring: 0xc0
-  __AUTH_CONST.__auth_got: 0x160
+  __AUTH_CONST.__cfstring: 0x140
+  __AUTH_CONST.__auth_got: 0x190
   __AUTH.__objc_data: 0xa0
   __DATA.__objc_protorefs: 0x8
   __DATA.__objc_classrefs: 0x68
   __DATA.__objc_superrefs: 0x10
-  __DATA.__objc_ivar: 0x18
+  __DATA.__objc_ivar: 0x1c
   __DATA.__data: 0x120
-  __DATA_DIRTY.__objc_data: 0x140
+  __DATA_DIRTY.__objc_data: 0xf0
   __DATA_DIRTY.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 15A86A45-5821-393E-B19C-086FEE7861E0
-  Functions: 71
-  Symbols:   322
-  CStrings:  139
+  UUID: 5471B80F-84A5-3CE4-93CB-14038AF0CCFE
+  Functions: 73
+  Symbols:   339
+  CStrings:  159
 
Symbols:
+ +[FOLocations familyControlsAuthorization]
+ +[FOLocations familyControlsDirectory]
+ +[FOLocations sharedDirectory]
+ -[FOAuthorizationCenter authorizationsPlist]
+ -[FOAuthorizationCenter authorizationsPlist].cold.1
+ -[FOAuthorizationCenter clearCurrentConnectionAndInvalidate:]
+ -[FOAuthorizationCenter connectionLock]
+ -[FOAuthorizationCenter currentConnection]
+ -[FOAuthorizationCenter setCurrentConnection:]
+ GCC_except_table4
+ GCC_except_table7
+ _OBJC_CLASS_$_FOLocations
+ _OBJC_CLASS_$_NSURL
+ _OBJC_IVAR_$_FOAuthorizationCenter._connectionLock
+ _OBJC_IVAR_$_FOAuthorizationCenter._currentConnection
+ _OBJC_METACLASS_$_FOLocations
+ __OBJC_$_CLASS_METHODS_FOLocations
+ __OBJC_$_CLASS_PROP_LIST_FOLocations
+ __OBJC_CLASS_RO_$_FOLocations
+ __OBJC_METACLASS_RO_$_FOLocations
+ ___38-[FOAuthorizationCenter xpcConnection]_block_invoke
+ ___38-[FOAuthorizationCenter xpcConnection]_block_invoke_2
+ ___NSArray0__struct
+ ___block_descriptor_40_e8_32w_e5_v8?0lw32l8
+ _objc_alloc_init
+ _objc_copyWeak
+ _objc_destroyWeak
+ _objc_initWeak
+ _objc_loadWeakRetained
+ _objc_msgSend$URLByAppendingPathComponent:isDirectory:
+ _objc_msgSend$activate
+ _objc_msgSend$authorizationsPlist
+ _objc_msgSend$clearCurrentConnectionAndInvalidate:
+ _objc_msgSend$familyControlsAuthorization
+ _objc_msgSend$familyControlsDirectory
+ _objc_msgSend$fileURLWithPath:
+ _objc_msgSend$fileURLWithPath:isDirectory:
+ _objc_msgSend$initWithBundleIdentifier:teamIdentifier:recordIdentifier:status:type:
+ _objc_msgSend$initWithContentsOfURL:error:
+ _objc_msgSend$initWithUUIDString:
+ _objc_msgSend$integerValue
+ _objc_msgSend$path
+ _objc_msgSend$setInterruptionHandler:
+ _objc_msgSend$setInvalidationHandler:
+ _objc_msgSend$sharedDirectory
+ _objc_msgSend$valueForKey:
+ _objc_release_x28
+ _objc_sync_enter
+ _objc_sync_exit
- +[FOAuthorizationRecordDecoder decodeRecordDatas:]
- +[FOAuthorizationRecordEncoder encodeRecords:]
- -[FOAuthorizationCenter initWithXPCConnection:]
- GCC_except_table5
- _OBJC_CLASS_$_FOAuthorizationRecordDecoder
- _OBJC_CLASS_$_FOAuthorizationRecordEncoder
- _OBJC_CLASS_$_NSKeyedArchiver
- _OBJC_CLASS_$_NSKeyedUnarchiver
- _OBJC_IVAR_$_FOAuthorizationCenter._xpcConnection
- _OBJC_METACLASS_$_FOAuthorizationRecordDecoder
- _OBJC_METACLASS_$_FOAuthorizationRecordEncoder
- __Block_object_dispose
- __OBJC_$_CLASS_METHODS_FOAuthorizationRecordDecoder
- __OBJC_$_CLASS_METHODS_FOAuthorizationRecordEncoder
- __OBJC_CLASS_RO_$_FOAuthorizationRecordDecoder
- __OBJC_CLASS_RO_$_FOAuthorizationRecordEncoder
- __OBJC_METACLASS_RO_$_FOAuthorizationRecordDecoder
- __OBJC_METACLASS_RO_$_FOAuthorizationRecordEncoder
- ___45-[FOAuthorizationCenter authorizationRecords]_block_invoke
- ___45-[FOAuthorizationCenter authorizationRecords]_block_invoke.cold.1
- ___45-[FOAuthorizationCenter authorizationRecords]_block_invoke_2
- ___45-[FOAuthorizationCenter authorizationRecords]_block_invoke_2.cold.1
- ___Block_byref_object_copy_
- ___Block_byref_object_dispose_
- ___block_descriptor_40_e8_32r_e29_v24?0"NSArray"8"NSError"16lr32l8
- ___block_descriptor_40_e8_32r_e52_v24?0"<FOFamilyControlsAgentPrivate>"8"NSError"16lr32l8
- _objc_msgSend$archivedDataWithRootObject:requiringSecureCoding:error:
- _objc_msgSend$authorizationRecordsWithReplyHandler:
- _objc_msgSend$count
- _objc_msgSend$decodeRecordDatas:
- _objc_msgSend$initWithCapacity:
- _objc_msgSend$resume
- _objc_msgSend$unarchivedObjectOfClass:fromData:error:
- _objc_release_x9
CStrings:
+ "\x02"
+ "/var/mobile"
+ "@\"NSObject\""
+ "Authorizations.plist"
+ "FOLocations"
+ "Failed to read Authorizations.plist: %{public}@"
+ "Library"
+ "T@\"NSObject\",R,N,V_connectionLock"
+ "T@\"NSURL\",R"
+ "T@\"NSXPCConnection\",&,N,V_currentConnection"
+ "URLByAppendingPathComponent:isDirectory:"
+ "_connectionLock"
+ "_currentConnection"
+ "activate"
+ "authorizationsPlist"
+ "clearCurrentConnectionAndInvalidate:"
+ "com.apple.FamilyControlsAgent"
+ "connectionLock"
+ "currentConnection"
+ "familyControlsAuthorization"
+ "familyControlsDirectory"
+ "fileURLWithPath:"
+ "fileURLWithPath:isDirectory:"
+ "initWithContentsOfURL:error:"
+ "initWithUUIDString:"
+ "integerValue"
+ "path"
+ "setCurrentConnection:"
+ "setInterruptionHandler:"
+ "setInvalidationHandler:"
+ "sharedDirectory"
+ "v20@0:8B16"
+ "valueForKey:"
- "\x01"
- "FOAuthorizationRecordDecoder"
- "FOAuthorizationRecordEncoder"
- "Failed to decode record from record data: %{public}@ with error: %{public}@"
- "Failed to encode record with record data: %{public}@ with error: %{public}@"
- "Failed to request authorization records with error: %{public}@"
- "T@\"NSXPCConnection\",R,V_xpcConnection"
- "_xpcConnection"
- "archivedDataWithRootObject:requiringSecureCoding:error:"
- "count"
- "decodeRecordDatas:"
- "encodeRecords:"
- "initWithCapacity:"
- "initWithXPCConnection:"
- "resume"
- "unarchivedObjectOfClass:fromData:error:"
- "v24@?0@\"NSArray\"8@\"NSError\"16"

```
