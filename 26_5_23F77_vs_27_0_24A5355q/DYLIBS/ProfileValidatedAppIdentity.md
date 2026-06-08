## ProfileValidatedAppIdentity

> `/System/Library/PrivateFrameworks/ProfileValidatedAppIdentity.framework/ProfileValidatedAppIdentity`

```diff

-132.2.0.0.0
-  __TEXT.__text: 0xea0
-  __TEXT.__auth_stubs: 0x1f0
+151.0.0.0.0
+  __TEXT.__text: 0xe3c
   __TEXT.__objc_methlist: 0x10c
   __TEXT.__const: 0x50
-  __TEXT.__cstring: 0xd7
-  __TEXT.__unwind_info: 0xb0
-  __TEXT.__objc_classname: 0x67
-  __TEXT.__objc_methname: 0x2d7
-  __TEXT.__objc_methtype: 0x109
-  __TEXT.__objc_stubs: 0x2c0
-  __DATA_CONST.__got: 0x58
+  __TEXT.__cstring: 0xd9
+  __TEXT.__unwind_info: 0xb8
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0xa0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_catlist: 0x8

   __DATA_CONST.__objc_selrefs: 0xf8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x100
+  __DATA_CONST.__got: 0x58
   __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__cfstring: 0x140
   __AUTH_CONST.__objc_const: 0x258
   __AUTH_CONST.__objc_intobj: 0x30
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0x20
   __DATA.__data: 0x120

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 59B1D6EF-DCF6-3D47-81E0-32FAC641C7BF
+  UUID: 069BA480-C4BE-3D5D-9056-43472E5C74FA
   Functions: 21
-  Symbols:   154
-  CStrings:  87
+  Symbols:   159
+  CStrings:  26
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x25
+ _objc_retain_x27
+ _objc_retain_x3
+ _objc_retain_x8
- _objc_release_x26
- _objc_retain
- _objc_retainAutoreleasedReturnValue
Functions:
~ -[PVAppIdentityDigest initWithVersion:data0:data1:data2:data3:data4:data5:] : 312 -> 340
~ -[PVAppIdentityDigest initWithError:version:] : 244 -> 248
~ +[PVAppIdentityDigest digestWithErrorCode:] : 124 -> 120
~ -[PVAppIdentityDigest encodeWithCoder:] : 236 -> 228
~ -[PVAppIdentityDigest initWithCoder:] : 496 -> 464
~ -[PVAppIdentityDigest asDictionary] : 552 -> 516
~ -[PVAppIdentityDigest getError] : 56 -> 8
~ _PVAppIdentity_GenerateDigestWithCompletion : 516 -> 540
~ ___PVAppIdentity_GenerateDigestWithCompletion_block_invoke : 268 -> 260
~ ___PVAppIdentity_GenerateDigestWithCompletion_block_invoke_2 : 200 -> 204
~ __PVAppIdentityLogSystem : 84 -> 68
~ +[NSError(ProfileValidatedAppIdentity) pvai_wrappedError:error:] : 224 -> 216
CStrings:
- ".cxx_destruct"
- "@\"NSData\""
- "@\"NSError\""
- "@\"NSNumber\""
- "@16@0:8"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@24@0:8q16"
- "@32@0:8@16@24"
- "@32@0:8q16@24"
- "@72@0:8@16@24@32@40@48@56@64"
- "B16@0:8"
- "NSCoding"
- "NSSecureCoding"
- "PVAppIdentityDigest"
- "PVAppIdentityServiceProtocol"
- "ProfileValidatedAppIdentity"
- "TB,R"
- "asDictionary"
- "base64EncodedStringWithOptions:"
- "code"
- "decodeObjectOfClass:forKey:"
- "dictionaryWithObjects:forKeys:count:"
- "digestWithErrorCode:"
- "digestWithTimeoutError"
- "domain"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "errorWithDomain:code:userInfo:"
- "generateDigest:ppqAppId:withReply:"
- "getError"
- "init"
- "initWithCoder:"
- "initWithError:version:"
- "initWithServiceName:"
- "initWithVersion:data0:data1:data2:data3:data4:data5:"
- "interfaceWithProtocol:"
- "invalidate"
- "isEqualToString:"
- "numberWithInteger:"
- "pvai_errorWithCode:"
- "pvai_errorWithCode:userInfo:"
- "pvai_wrappedError:error:"
- "remoteObjectProxyWithErrorHandler:"
- "resume"
- "setObject:forKeyedSubscript:"
- "setRemoteObjectInterface:"
- "supportsSecureCoding"
- "v16@0:8"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@16"
- "v40@0:8@\"NSURL\"16@\"NSData\"24@?<v@?@\"PVAppIdentityDigest\">32"
- "v40@0:8@16@24@?32"

```
