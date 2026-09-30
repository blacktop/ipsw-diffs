## RestorePostProcess

> `/System/Library/DataClassMigrators/RestorePostProcess.migrator/RestorePostProcess`

```diff

-2349.60.119.0.0
-  __TEXT.__text: 0x1465c
+2349.80.18.0.0
+  __TEXT.__text: 0x14b94
   __TEXT.__auth_stubs: 0xcd0
-  __TEXT.__objc_stubs: 0x24e0
-  __TEXT.__objc_methlist: 0xa68
+  __TEXT.__objc_stubs: 0x2540
+  __TEXT.__objc_methlist: 0xa70
   __TEXT.__const: 0x420
-  __TEXT.__cstring: 0x3985
-  __TEXT.__objc_methname: 0x2d45
-  __TEXT.__objc_classname: 0xf2
-  __TEXT.__objc_methtype: 0x5b3
+  __TEXT.__cstring: 0x3a05
+  __TEXT.__objc_methname: 0x2d0f
+  __TEXT.__objc_classname: 0x118
+  __TEXT.__objc_methtype: 0x5c5
   __TEXT.__oslogstring: 0x261d
   __TEXT.__gcc_except_tab: 0x38c
   __TEXT.__constg_swiftt: 0x18c

   __TEXT.__swift5_proto: 0x28
   __TEXT.__swift5_types: 0x1c
   __TEXT.__swift5_assocty: 0x18
-  __TEXT.__unwind_info: 0x478
+  __TEXT.__unwind_info: 0x470
   __TEXT.__eh_frame: 0x158
   __DATA_CONST.__auth_got: 0x678
   __DATA_CONST.__got: 0x2b8
   __DATA_CONST.__auth_ptr: 0x128
   __DATA_CONST.__const: 0x828
   __DATA_CONST.__cfstring: 0xe40
-  __DATA_CONST.__objc_classlist: 0x68
+  __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x30
+  __DATA_CONST.__objc_superrefs: 0x38
   __DATA_CONST.__objc_intobj: 0x48
   __DATA_CONST.__objc_arraydata: 0x50
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0x1628
-  __DATA.__objc_selrefs: 0xbb0
-  __DATA.__objc_ivar: 0x6c
-  __DATA.__objc_data: 0x4c0
+  __DATA.__objc_const: 0x16d8
+  __DATA.__objc_selrefs: 0xb78
+  __DATA.__objc_ivar: 0x64
+  __DATA.__objc_data: 0x510
   __DATA.__data: 0x360
   __DATA.__bss: 0x5f0
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 367
-  Symbols:   297
-  CStrings:  1127
+  Functions: 368
+  Symbols:   299
+  CStrings:  1121
 
Symbols:
+ _OBJC_CLASS_$__MBImmutableServiceAccountProperties
+ _OBJC_METACLASS_$__MBImmutableServiceAccountProperties
CStrings:
+ "\x06"
+ "\x11"
+ "-[_MBImmutableServiceAccountProperties _initWithPersona:accountIdentifier:dsid:altDSID:serviceURL:chunkStoreURL:options:]"
+ "@\"_MBImmutableServiceAccountProperties\""
+ "T@\"MBPersona\",R,N"
+ "T@\"MBPersona\",R,N,V_persona"
+ "T@\"NSString\",R,N,V_accountIdentifier"
+ "T@\"NSString\",R,N,V_altDSID"
+ "T@\"NSString\",R,N,V_dsid"
+ "T@\"NSURL\",R,N"
+ "T@\"NSURL\",R,N,V_chunkStoreURL"
+ "T@\"NSURL\",R,N,V_serviceURL"
+ "T@\"_MBImmutableServiceAccountProperties\",&,V_properties"
+ "TB,R,N,V_useMockChunkStore"
+ "TQ,R,N,V_options"
+ "_MBImmutableServiceAccountProperties"
+ "_URLByInsertingUser:"
+ "_deriveNewAccountPropertiesFromACAccount:"
+ "_initWithPersona:accountIdentifier:dsid:altDSID:serviceURL:chunkStoreURL:options:"
+ "_properties"
+ "_updateAppleAccount:"
+ "_updateApplePassword:completionHandler:"
+ "_updateApplePasswordSync:"
+ "options"
+ "properties"
+ "setProperties:"
- "\x05\""
- "Q24@0:8Q16"
- "T@\"MBPersona\",&,N,V_persona"
- "T@\"NSObject<OS_dispatch_queue>\",R,N"
- "T@\"NSString\",&,V_accountIdentifier"
- "T@\"NSString\",&,V_altDSID"
- "T@\"NSString\",&,V_dsid"
- "T@\"NSURL\",&,N,V_chunkStoreURL"
- "T@\"NSURL\",&,N,V_serviceURL"
- "TB,N,V_enabled"
- "TB,N,V_enabledForBackup"
- "TB,N,V_useMockChunkStore"
- "URLByInsertingUser:"
- "_clientInfoHeader"
- "_enabled"
- "_enabledForBackup"
- "_refreshIsBackupOnCellularEnabledWithCurrentOptions:"
- "enabled"
- "enabledForBackup"
- "setAccountIdentifier:"
- "setAltDSID:"
- "setChunkStoreURL:"
- "setDsid:"
- "setEnabled:"
- "setEnabledForBackup:"
- "setPersona:"
- "setServiceURL:"
- "setUseMockChunkStore:"
- "updateAppleAccount:"
- "updateApplePassword:completionHandler:"
- "updateApplePasswordSync:"
- "v20@0:8B16"

```
