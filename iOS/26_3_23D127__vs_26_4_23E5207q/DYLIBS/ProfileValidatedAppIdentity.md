## ProfileValidatedAppIdentity

> `/System/Library/PrivateFrameworks/ProfileValidatedAppIdentity.framework/ProfileValidatedAppIdentity`

```diff

 132.1.0.0.0
-  __TEXT.__text: 0xe3c
-  __TEXT.__auth_stubs: 0x260
+  __TEXT.__text: 0xea0
+  __TEXT.__auth_stubs: 0x1f0
   __TEXT.__objc_methlist: 0x10c
   __TEXT.__const: 0x50
   __TEXT.__cstring: 0xd7
-  __TEXT.__unwind_info: 0xb8
+  __TEXT.__unwind_info: 0xb0
   __TEXT.__objc_classname: 0x67
   __TEXT.__objc_methname: 0x2d7
   __TEXT.__objc_methtype: 0x109

   __DATA_CONST.__objc_selrefs: 0xf8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x138
+  __AUTH_CONST.__auth_got: 0x100
   __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__cfstring: 0x140
   __AUTH_CONST.__objc_const: 0x258

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 97674B02-6F64-33AC-B6AB-9F1DC747877D
+  UUID: EDE5062B-C3CB-3A22-B80D-493761101CEF
   Functions: 21
-  Symbols:   161
+  Symbols:   154
   CStrings:  87
 
Symbols:
+ _objc_retain
+ _objc_retainAutoreleasedReturnValue
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x25
- _objc_retain_x27
- _objc_retain_x28
- _objc_retain_x3
- _objc_retain_x8
Functions:
~ -[PVAppIdentityDigest initWithVersion:data0:data1:data2:data3:data4:data5:] : 340 -> 312
~ -[PVAppIdentityDigest initWithError:version:] : 248 -> 244
~ +[PVAppIdentityDigest digestWithErrorCode:] : 120 -> 124
~ -[PVAppIdentityDigest encodeWithCoder:] : 228 -> 236
~ -[PVAppIdentityDigest initWithCoder:] : 464 -> 496
~ -[PVAppIdentityDigest asDictionary] : 516 -> 552
~ -[PVAppIdentityDigest getError] : 8 -> 56
~ _PVAppIdentity_GenerateDigestWithCompletion : 540 -> 516
~ ___PVAppIdentity_GenerateDigestWithCompletion_block_invoke : 260 -> 268
~ ___PVAppIdentity_GenerateDigestWithCompletion_block_invoke_2 : 204 -> 200
~ __PVAppIdentityLogSystem : 68 -> 84
~ +[NSError(ProfileValidatedAppIdentity) pvai_wrappedError:error:] : 216 -> 224

```
