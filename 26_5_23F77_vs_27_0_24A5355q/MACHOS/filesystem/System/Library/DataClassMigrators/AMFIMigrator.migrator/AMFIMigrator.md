## AMFIMigrator

> `/System/Library/DataClassMigrators/AMFIMigrator.migrator/AMFIMigrator`

```diff

-1045.120.5.0.0
-  __TEXT.__text: 0x74 sha256:10fccc8508a6a5c43aba50dfb119f31accf9fd6391dabb1ec52c987546f61b86
-  __TEXT.__auth_stubs: 0x20 sha256:1695d59b01c3ea76ec71e53ab2a1c8e0f2696fff1e3accd4a4186ad32d854a8d
+1166.0.0.0.0
+  __TEXT.__text: 0x74 sha256:e32f18919c0db53969fdd996613cf8a2c6244b5669628b0d7d6ca50706071c0c
+  __TEXT.__auth_stubs: 0x20 sha256:1aa8a7025ae84ada663b0d3fe7ba6fad4a5b85f9fb7fc26d4ea8569716978fc4
   __TEXT.__objc_methlist: 0x20 sha256:dc7629dded717b31d5e0251ee8293ddc8875e97ab3a8499fec4b732fe21c7e8a
   __TEXT.__cstring: 0x58 sha256:86e4b92df99feb5fc70accb7444f77f51b1e1ed99b78ed210dcb7116446024ba
   __TEXT.__objc_classname: 0xd sha256:207f816da08d4738101a6384fd90af5b3675b0971beb10c7caa48025380f87a5
   __TEXT.__objc_methname: 0x1f sha256:31f491b8a5bc4af785137578f5351e08889ac6f2747864c0b3953b886ebff873
   __TEXT.__objc_methtype: 0x10 sha256:0884495ad32216332f2e50f97f267011dca0c35b96b95ea2f6aebc7b0adeb28e
-  __TEXT.__unwind_info: 0x60 sha256:e54790307aad41b3a9547fad9a6ff34408b7958c3760e0aa7dcd00be24a1e806
-  __DATA_CONST.__auth_got: 0x10 sha256:935b037c1e1aa06c5bd2fcb6d6056c6f049900ffd3b42115689ec4dfe82b5314
-  __DATA_CONST.__cfstring: 0x60 sha256:71ea72349ba44d831f7c747d9e18a8c7c2b24ded9cdf5a77256481994a4ebf2c
-  __DATA_CONST.__objc_classlist: 0x8 sha256:68a33b498d08a61857c0bd2e5db05517356411ad8bbf1c6398ada80ac5e27b8f
+  __TEXT.__unwind_info: 0x60 sha256:9007e640d52cb246b760d4484deda6c91b7d7fd8e7a522189d8d5a714ff45a9d
+  __DATA_CONST.__cfstring: 0x60 sha256:f63e94d8f1dd829e0acc042433cc768447d4c352239098808d792ea48987fd60
+  __DATA_CONST.__objc_classlist: 0x8 sha256:dfcbbc110fa9c59f513abfc6423f6c07ce278a1a02c6ba64734ab725d836c2e7
   __DATA_CONST.__objc_imageinfo: 0x8 sha256:1fa65ffcccc24c72d5d7f804a2be05ae57dfbb8769ffb33c4272ed6795b7e61c
+  __DATA_CONST.__auth_got: 0x10 sha256:4a019a0711899b0c1668b8f73249479f8620efee97eda814aa5397ae96cfcd99
   __DATA.__objc_const: 0x90 sha256:f01a1921cbfd5b21faea1a0951e910d6cdd24bc94e2ccbd769f97ceadff432d0
   __DATA.__objc_selrefs: 0x10 sha256:25efab1a6461593888c205202228ee881408da762f988fbd2842b4d2e432832a
   __DATA.__objc_data: 0x50 sha256:f3aef4c4062c2488ccbd4f9b351ad641bae678cfe2fb37689648e589cd1f0158

   - /System/Library/PrivateFrameworks/DataMigration.framework/DataMigration
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6C609FF6-C13E-3FB4-83A8-FC135C43F9FB
+  UUID: C90B4BC0-8AE8-38ED-840C-9B873B03CE13
   Functions: 2
   Symbols:   31
   CStrings:  11
Symbols:
+ /Library/Caches/com.apple.xbs/755A80F3-42C3-4523-9AA7-3A1398143F6C/TemporaryDirectory.iOBjAn/Binaries/amfid/install/TempContent/Objects/AppleMobileFileIntegrity.build/AMFIMigrator.build/Objects-normal/arm64e/AMFIMigrator.o
+ /Library/Caches/com.apple.xbs/755A80F3-42C3-4523-9AA7-3A1398143F6C/TemporaryDirectory.iOBjAn/Sources/amfid/AMFIMigrator/
- /Library/Caches/com.apple.xbs/5A1D9E0F-0A54-4357-BE2B-DD91EDBD4FAD/TemporaryDirectory.YCZnaC/Binaries/amfid/install/TempContent/Objects/AppleMobileFileIntegrity.build/AMFIMigrator.build/Objects-normal/arm64e/AMFIMigrator.o
- /Library/Caches/com.apple.xbs/5A1D9E0F-0A54-4357-BE2B-DD91EDBD4FAD/TemporaryDirectory.YCZnaC/Sources/amfid/AMFIMigrator/
Functions:
~ -[AMFIMigrator dataClassName] : sha256 f8a42e1d24ec03208c4845db4c14ef6f1144b34a7f064fe2db75eba2c7d6a760 -> 58375722e0b9bd0fa3ba04cf3fe639bf704a7abba855e7264b75c6fcf6ff4b8e
~ -[AMFIMigrator performMigration] : sha256 54c18c2ed856256c591bf276a19e6b4c0542266ddc2e7e3d4c799e755fee4d7f -> 610f4e126cc1c05996be071d58481f6b1d755fb10055efea97598f3c83888f2d

```
