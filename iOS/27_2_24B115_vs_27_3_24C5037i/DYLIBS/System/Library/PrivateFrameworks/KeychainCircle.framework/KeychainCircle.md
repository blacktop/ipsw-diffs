## KeychainCircle

> `/System/Library/PrivateFrameworks/KeychainCircle.framework/KeychainCircle`

```diff

-62460.40.78.0.0
-  __TEXT.__text: 0x29134
+62460.60.42.502.1
+  __TEXT.__text: 0x294d0
   __TEXT.__lazy_helpers: 0x1a4
   __TEXT.__objc_methlist: 0x1ebc
   __TEXT.__const: 0xe0

   __TEXT.__cstring: 0x37f6
   __TEXT.__oslogstring: 0x3ac2
   __TEXT.__ustring: 0x32
-  __TEXT.__unwind_info: 0x9b8
+  __TEXT.__unwind_info: 0x9c0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1080
+  __DATA_CONST.__objc_selrefs: 0x1098
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x98
   __DATA_CONST.__got: 0x2f0
Symbols:
+ -[KCAESGCMDuplexSession initWithSecret:context:as:altDSID:pairingUUID:piggybackingVersion:epoch:flowID:deviceSessionID:]
+ ___120-[KCAESGCMDuplexSession initWithSecret:context:as:altDSID:pairingUUID:piggybackingVersion:epoch:flowID:deviceSessionID:]_block_invoke
+ _initWithSecret:context:as:altDSID:pairingUUID:piggybackingVersion:epoch:flowID:deviceSessionID:.onceToken
- -[KCAESGCMDuplexSession initWithSecret:context:as:altDSID:pairingUUID:piggybackingVersion:epoch:]
- ___97-[KCAESGCMDuplexSession initWithSecret:context:as:altDSID:pairingUUID:piggybackingVersion:epoch:]_block_invoke
- _initWithSecret:context:as:altDSID:pairingUUID:piggybackingVersion:epoch:.onceToken
Functions:
~ -[KCJoiningRequestSecretSession setupSession:] : 308 -> 404
~ -[KCAESGCMDuplexSession encodeWithCoder:] : 288 -> 376
~ -[KCAESGCMDuplexSession initWithCoder:] : 332 -> 416
~ -[KCAESGCMDuplexSession initWithSecret:context:as:] : 52 -> 56
~ -[KCAESGCMDuplexSession initWithSecret:context:as:altDSID:pairingUUID:piggybackingVersion:epoch:] -> -[KCAESGCMDuplexSession initWithSecret:context:as:altDSID:pairingUUID:piggybackingVersion:epoch:flowID:deviceSessionID:] : 532 -> 608
~ -[KCJoiningRequestCircleSession setContextIDForSession:] : 204 -> 300
~ -[KCJoiningRequestCircleSession initWithCircleDelegate:session:altDSID:flowID:deviceSessionID:error:] : 168 -> 224
~ -[KCJoiningRequestCircleSession initWithCircleDelegate:session:otcontrol:altDSID:flowID:deviceSessionID:error:] : 612 -> 676
~ -[KCJoiningAcceptSession initWithSecretDelegate:circleDelegate:dsid:altDSID:flowID:deviceSessionID:rng:error:] : 712 -> 732
~ -[KCJoiningAcceptSession setSessionControlArguments:] : 4 -> 344
```
