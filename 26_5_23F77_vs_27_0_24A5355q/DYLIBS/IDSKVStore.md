## IDSKVStore

> `/System/Library/PrivateFrameworks/IDSKVStore.framework/IDSKVStore`

```diff

-1969.600.51.2.5
-  __TEXT.__text: 0x2fe0
-  __TEXT.__auth_stubs: 0x550
+1992.100.7.2.1
+  __TEXT.__text: 0x2eb4
   __TEXT.__objc_methlist: 0x1d4
   __TEXT.__const: 0x68
-  __TEXT.__gcc_except_tab: 0x198
-  __TEXT.__cstring: 0x744
+  __TEXT.__gcc_except_tab: 0x170
+  __TEXT.__cstring: 0x748
   __TEXT.__oslogstring: 0x19b
-  __TEXT.__unwind_info: 0x190
-  __TEXT.__objc_classname: 0x22
-  __TEXT.__objc_methname: 0x604
-  __TEXT.__objc_methtype: 0x1b9
-  __TEXT.__objc_stubs: 0x460
-  __DATA_CONST.__got: 0x40
+  __TEXT.__unwind_info: 0x180
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x490
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x170
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x2b8
+  __DATA_CONST.__got: 0x38
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x500
   __AUTH_CONST.__objc_const: 0x2c0
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0x24
   __DATA_DIRTY.__objc_data: 0xa0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/IMFoundation.framework/IMFoundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0BBA7129-A361-33C0-914D-0BE0358954AE
+  UUID: 4628756E-B403-38C9-A012-AB761692532B
   Functions: 76
-  Symbols:   106
-  CStrings:  198
+  Symbols:   110
+  CStrings:  102
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x2
+ _objc_retain_x24
+ _objc_retain_x8
- ___stack_chk_fail
- ___stack_chk_guard
Functions:
~ sub_25c939d48 -> sub_266f70d48 : 604 -> 544
~ sub_25c93a104 -> sub_266f710c8 : 220 -> 224
~ sub_25c93a3d0 -> sub_266f71398 : 168 -> 160
~ sub_25c93a4dc -> sub_266f7149c : 404 -> 400
~ sub_25c93a7c8 -> sub_266f71784 : 192 -> 188
~ sub_25c93a95c -> sub_266f71914 : 232 -> 240
~ sub_25c93aa44 -> sub_266f71a04 : 156 -> 168
~ sub_25c93ac0c -> sub_266f71bd8 : 164 -> 156
~ sub_25c93ad00 -> sub_266f71cc4 : 300 -> 304
~ sub_25c93ae2c -> sub_266f71df4 : 144 -> 148
~ sub_25c93af60 -> sub_266f71f2c : 192 -> 200
~ sub_25c93b034 -> sub_266f72008 : 276 -> 272
~ sub_25c93b148 -> sub_266f72118 : 88 -> 84
~ sub_25c93b1a0 -> sub_266f7216c : 240 -> 244
~ sub_25c93b290 -> sub_266f72260 : 88 -> 84
~ sub_25c93b2e8 -> sub_266f722b4 : 276 -> 272
~ sub_25c93b3fc -> sub_266f723c4 : 84 -> 80
~ sub_25c93b450 -> sub_266f72414 : 192 -> 200
~ sub_25c93b624 -> sub_266f725f0 : 100 -> 92
~ sub_25c93b6a0 -> sub_266f72664 : 172 -> 168
~ sub_25c93b74c -> sub_266f7270c : 548 -> 536
~ sub_25c93b970 -> sub_266f72924 : 276 -> 280
~ sub_25c93ba84 -> sub_266f72a3c : 100 -> 96
~ sub_25c93bba0 -> sub_266f72b54 : 1412 -> 1388
~ sub_25c93c134 -> sub_266f730d0 : 168 -> 160
~ sub_25c93c1dc -> sub_266f73170 : 768 -> 688
~ sub_25c93c8ec -> sub_266f73830 : 284 -> 280
~ sub_25c93ca08 -> sub_266f73948 : 536 -> 480
~ sub_25c93cc48 -> sub_266f73b50 : 64 -> 12
CStrings:
- ".cxx_destruct"
- "@\"CSDBThreadedRecordStore\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSObject<OS_dispatch_source>\""
- "@\"NSString\""
- "@16@0:8"
- "@24@0:8@16"
- "@28@0:8@16c24"
- "@32@0:8@16^@24"
- "@36@0:8@16@24I32"
- "@36@0:8Q16c24^@28"
- "@40@0:8Q16^@24^@32"
- "B32@0:8@16^@24"
- "B40@0:8@16@24^@32"
- "I"
- "I16@0:8"
- "IDSKVDeleteContext"
- "Q"
- "Q16@0:8"
- "T@\"CSDBThreadedRecordStore\",&,N,V_messageStore"
- "T@\"NSString\",C,N,V_path"
- "T@\"NSString\",C,N,V_storeName"
- "TI,N,V_dataProtectionClass"
- "TQ,N,V_rowIDCutoff"
- "Tc,N,V_valueType"
- "UTF8String"
- "__closeDatabaseOnIvarQueue"
- "_clearDatabaseCloseTimerOnIvarQueue"
- "_dataProtectionClass"
- "_databaseCloseTimer"
- "_databaseLastUpdateTime"
- "_initializeMessageStoreIfNeeded:path:dataProtectionClass:"
- "_invalidateCachesForMessageStore:"
- "_ivarQueue"
- "_messageStore"
- "_onIvarQueue_deleteDatesBefore:after:"
- "_onIvarQueue_deleteSerializedValueForKey:valueType:"
- "_onIvarQueue_deleteUpToRowID:valueType:"
- "_onIvarQueue_performBlock:initializeStore:"
- "_onIvarQueue_performBlock:initializeStore:waitUntilDone:"
- "_onIvarQueue_persistSerializedValue:forKey:valueType:"
- "_onIvarQueue_serializedValueForKey:valueType:"
- "_onIvarQueue_serializedValuesUpToLimit:valueType:deleteContext:"
- "_onIvarQueue_storedKeysAfter:"
- "_path"
- "_performInitialHousekeepingOnIvarQueue"
- "_rowIDCutoff"
- "_setDatabaseCloseTimerOnIvarQueue"
- "_storeName"
- "_valueType"
- "c"
- "c16@0:8"
- "closeDatabaseSynchronously:"
- "d"
- "dataForKey:error:"
- "dataProtectionClass"
- "datasUpToLimit:deleteContext:error:"
- "deleteBatchWithContext:error:"
- "deleteDatabase"
- "deleteEntriesBeforeDate:afterDate:error:"
- "fileSystemRepresentation"
- "init"
- "initWithFormat:"
- "initWithPath:storeName:dataProtectionClass:"
- "messageStore"
- "path"
- "persistData:forKey:error:"
- "rowIDCutoff"
- "setDataProtectionClass:"
- "setMessageStore:"
- "setPath:"
- "setRowIDCutoff:"
- "setStoreName:"
- "setValueType:"
- "storeName"
- "storedKeysAfterDate:error:"
- "stringByResolvingAndStandardizingPath"
- "stringGUID"
- "stringWithFormat:"
- "timeIntervalSince1970"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8I16"
- "v20@0:8c16"
- "v24@0:8@16"
- "v24@0:8Q16"
- "v28@0:8@16c24"
- "v28@0:8@?16B24"
- "v28@0:8Q16c24"
- "v32@0:8@16@24"
- "v32@0:8@?16B24B28"
- "v36@0:8@16@24I32"
- "v36@0:8@16@24c32"
- "valueType"

```
