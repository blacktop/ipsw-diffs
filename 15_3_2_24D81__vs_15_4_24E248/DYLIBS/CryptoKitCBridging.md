## CryptoKitCBridging

> `/System/Library/PrivateFrameworks/CryptoKitCBridging.framework/Versions/A/CryptoKitCBridging`

```diff

-241.60.5.0.0
-  __TEXT.__text: 0x2168
+241.100.42.0.0
+  __TEXT.__text: 0x2104
   __TEXT.__auth_stubs: 0x3c0
   __TEXT.__objc_methlist: 0x1f8
   __TEXT.__const: 0x40

   - /System/Library/Frameworks/Security.framework/Versions/A/Security
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 29A3FD89-F5E6-36DD-96B7-2E54D0B3E299
+  UUID: A5E13E31-AE28-31D4-B067-08C55455A140
   Functions: 53
   Symbols:   176
   CStrings:  76
Functions:
~ _keyIsCompactRepresentable : 348 -> 344
~ -[CKSSShare initWithParams:x:y:] : 264 -> 260
~ -[CKCBCorecryptoECScalar initWithx963Representation:group:] : 360 -> 356
~ -[CKCBCorecryptoECScalar x963Representation] : 688 -> 672
~ -[CKCBCorecryptoECScalar serializedBigEndianScalar] : 304 -> 284
~ -[CKCBCorecryptoECScalar add:corecryptoError:] : 244 -> 240
~ -[CKCBCorecryptoECScalar sub:corecryptoError:] : 268 -> 264
~ -[CKCBCorecryptoECScalar multiply:corecryptoError:] : 260 -> 256
~ -[CKCBCorecryptoECScalar inverseModOrder] : 176 -> 172
~ -[CKCBCorecryptoECPoint initFromPublicKeyBytes:inGroup:compressed:corecryptoError:] : 372 -> 368
~ -[CKCBCorecryptoECPoint initWithGeneratorForCP:] : 148 -> 144
~ -[CKCBCorecryptoECPoint serializedPublicKey:] : 452 -> 448
~ -[CKCBCorecryptoECPoint add:corecryptoError:] : 644 -> 636
~ -[CKCBCorecryptoECPoint sub:corecryptoError:] : 644 -> 636
~ -[CKCBCorecryptoECPoint multiply:corecryptoError:] : 616 -> 608

```
