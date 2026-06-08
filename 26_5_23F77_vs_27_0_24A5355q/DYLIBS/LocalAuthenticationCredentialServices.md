## LocalAuthenticationCredentialServices

> `/System/Library/PrivateFrameworks/LocalAuthenticationCredentialServices.framework/LocalAuthenticationCredentialServices`

```diff

-2005.120.18.0.0
-  __TEXT.__text: 0x18800
-  __TEXT.__auth_stubs: 0x700
-  __TEXT.__objc_methlist: 0x69c
+2305.0.0.0.1
+  __TEXT.__text: 0x18cdc
+  __TEXT.__objc_methlist: 0x6bc
   __TEXT.__const: 0x290
-  __TEXT.__gcc_except_tab: 0x7c
-  __TEXT.__cstring: 0x217a
+  __TEXT.__gcc_except_tab: 0x84
+  __TEXT.__cstring: 0x221e
   __TEXT.__oslogstring: 0x3e0
   __TEXT.__dlopen_cstrs: 0x5d
   __TEXT.__swift5_typeref: 0x52

   __TEXT.__swift5_reflstr: 0x10
   __TEXT.__swift5_fieldmd: 0x48
   __TEXT.__swift5_types: 0xc
-  __TEXT.__unwind_info: 0x600
-  __TEXT.__eh_frame: 0x4b8
-  __TEXT.__objc_classname: 0x1b3
-  __TEXT.__objc_methname: 0x827
-  __TEXT.__objc_methtype: 0x38c
-  __TEXT.__objc_stubs: 0x520
-  __DATA_CONST.__got: 0xa0
+  __TEXT.__unwind_info: 0x658
+  __TEXT.__eh_frame: 0x588
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x190
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x228
+  __DATA_CONST.__objc_selrefs: 0x230
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x390
+  __DATA_CONST.__got: 0xa8
   __AUTH_CONST.__const: 0xf0
-  __AUTH_CONST.__cfstring: 0x140
+  __AUTH_CONST.__cfstring: 0x160
   __AUTH_CONST.__objc_const: 0x1700
+  __AUTH_CONST.__auth_got: 0x3c0
   __AUTH.__objc_data: 0x240
   __DATA.__objc_ivar: 0x10
   __DATA.__data: 0x222

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: F74FCB99-D268-3184-A9D9-CCE579C9981B
-  Functions: 672
-  Symbols:   1136
-  CStrings:  425
+  UUID: 542EF792-B4BF-3BAD-90ED-8CACB1140919
+  Functions: 678
+  Symbols:   1125
+  CStrings:  286
 
Symbols:
+ _ACMGetEnvironmentVariableData
+ _NSDataDeallocatorFree
+ _OUTLINED_FUNCTION_69
+ _OUTLINED_FUNCTION_70
+ ___block_descriptor_48_e8_32s40r_e26_B24?0^{__ACMHandle=}8^16lr40l8s32l8
+ _malloc_type_malloc
+ _objc_alloc_init
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$_newZeroingDataWithBytesNoCopy:length:deallocator:
+ _objc_retain_x1
+ _objc_retain_x3
- ___block_descriptor_48_e8_32s40r_e26_B24?0^{__ACMHandle=}8^16ls32l8r40l8
- _objc_msgSend$isCredentialSet:
CStrings:
+ "ACMCredential - ACMCredentialDataPKITokenValidated"
+ "ACMCredential - ACMCredentialDataPKITokenValidated2"
+ "ACMGetEnvironmentVariableData"
+ "Failed to allocate decryption buffer"
- "#16@0:8"
- ".cxx_destruct"
- "@\"<LACSContext>\""
- "@\"LACSExtractablePassword\""
- "@\"LACSSecurePassword\""
- "@\"LAContext\""
- "@\"NSData\""
- "@\"NSData\"16@0:8"
- "@\"NSData\"24@0:8^@16"
- "@\"NSString\"16@0:8"
- "@\"_TtC37LocalAuthenticationCredentialServices12LACSPassword\""
- "@\"_TtC37LocalAuthenticationCredentialServices21LACSUnmanagedPassword\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@24@0:8^@16"
- "@24@0:8q16"
- "@28@0:8^{__ACMHandle=}16B24"
- "@32@0:8:16@24"
- "@32@0:8@16^@24"
- "@32@0:8^{__ACMHandle=}16^@24"
- "@32@0:8q16@24"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24^@32"
- "@48@0:8@16@24@32^@40"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B32@0:8@?16^@24"
- "B36@0:8@\"NSData\"16B24^@28"
- "B36@0:8@16B24^@28"
- "LACSContext"
- "LACSError"
- "LACSExtractableCredential"
- "LACSExtractablePassword"
- "LACSSecureCredential"
- "LACSSecurePassword"
- "LACSUnmanagedContext"
- "LACSUnmanagedExtractablePassword"
- "LACSUnmanagedSecurePassword"
- "NSCoding"
- "NSObject"
- "NSSecureCoding"
- "Q16@0:8"
- "T#,R"
- "T@\"<LACSContext>\",N,R,Vcontext"
- "T@\"LACSExtractablePassword\",N,R,Vpassword"
- "T@\"LACSSecurePassword\",N,R,Vpassword"
- "T@\"LAContext\",R,N,V_context"
- "T@\"NSData\",R,N"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSUUID\",N,R"
- "T@\"_TtC37LocalAuthenticationCredentialServices12LACSPassword\",N,R,Vpassword"
- "T@\"_TtC37LocalAuthenticationCredentialServices21LACSUnmanagedPassword\",N,R,Vpassword"
- "TB,N,R"
- "TB,R"
- "TQ,R"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "^{__ACMHandle=}"
- "_TtC37LocalAuthenticationCredentialServices12LACSPassword"
- "_TtC37LocalAuthenticationCredentialServices21LACSUnmanagedPassword"
- "_context"
- "_contextRef"
- "_decryptData:seed:externalizedContext:error:"
- "_encryptData:seed:externalizedContext:error:"
- "_encryptionSeedForContext:error:"
- "_errorWithCode:userInfo:"
- "_externalizedContextRef"
- "_ownsContextRef"
- "_withContext:error:"
- "autorelease"
- "bytes"
- "class"
- "conformsToProtocol:"
- "context"
- "contextRef"
- "credentialOfType:reply:"
- "data"
- "data:"
- "dataWithBytes:length:"
- "dataWithLength:"
- "dealloc"
- "debugDescription"
- "description"
- "dictionaryWithObjects:forKeys:count:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "errorWithCode:"
- "errorWithCode:debugDescription:"
- "errorWithDomain:code:userInfo:"
- "externalize"
- "externalizedContext"
- "fetchCredentialData:"
- "hash"
- "init:"
- "initWithACMContextRef:ownsContextRef:"
- "initWithBytes:length:"
- "initWithCoder:"
- "initWithContext:"
- "initWithContextRef:"
- "initWithContextRef:error:"
- "initWithData:contextRef:error:"
- "initWithData:error:"
- "initWithExternalizedContext:userSession:"
- "initWithPassword:"
- "initWithUUID:password:error:"
- "isCredentialSet:"
- "isEqual:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "length"
- "mutableBytes"
- "password"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "release"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "secureCopy"
- "self"
- "setCredential:type:error:"
- "storeCredentialData:securely:error:"
- "stringWithFormat:"
- "superclass"
- "supportsSecureCoding"
- "unsafeContextRef"
- "uuid"
- "uuidBytes"
- "v16@0:8"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "withContextRef:"
- "zone"

```
