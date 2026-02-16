## CryptoKitCBridging

> `/System/Library/PrivateFrameworks/CryptoKitCBridging.framework/CryptoKitCBridging`

```diff

-324.40.4.0.0
-  __TEXT.__text: 0x2044
-  __TEXT.__auth_stubs: 0x470
+324.100.31.0.0
+  __TEXT.__text: 0x2064
+  __TEXT.__auth_stubs: 0x460
   __TEXT.__objc_methlist: 0x1f8
   __TEXT.__const: 0x40
   __TEXT.__cstring: 0x23
-  __TEXT.__unwind_info: 0xf0
+  __TEXT.__unwind_info: 0xe8
   __TEXT.__objc_classname: 0x40
   __TEXT.__objc_methname: 0x3b1
   __TEXT.__objc_methtype: 0x33b

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x130
   __DATA_CONST.__objc_superrefs: 0x18
-  __AUTH_CONST.__auth_got: 0x240
+  __AUTH_CONST.__auth_got: 0x238
   __AUTH_CONST.__objc_const: 0x368
   __DATA.__objc_ivar: 0x18
   __DATA_DIRTY.__objc_data: 0x140

   - /System/Library/Frameworks/Security.framework/Security
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 42E4253A-23E4-3705-8ACB-9DC3F4CC5E2A
-  Functions: 54
+  UUID: EB33BC0F-53D7-3C39-A2F9-C3EFB41E31CF
+  Functions: 55
   Symbols:   226
   CStrings:  76
 
Symbols:
+ _ccShake256CtxSize
+ _objc_retain_x21
+ _objc_retain_x22
+ _objc_retain_x25
- _objc_claimAutoreleasedReturnValue
- _objc_retain
- _objc_retain_x2
- _objc_retain_x4
Functions:
+ +[CKCBCorecryptoECPoint groupOrderByteCountForCP:]
~ _keyIsCompactRepresentable : 340 -> 344
+ _ccShake256CtxSize
~ -[CKCBCorecryptoECScalar x963Representation] : 636 -> 652
~ -[CKCBCorecryptoECScalar initWithRandomScalarInGroup:] : 196 -> 204
~ -[CKCBCorecryptoECScalar initWithData:inGroup:reduction:corecryptoError:] : 344 -> 336
~ -[CKCBCorecryptoECScalar serializedBigEndianScalar] : 276 -> 280
- +[CKCBCorecryptoECPoint groupOrderByteCountForCP:]

```
