## MobileActivationMigrator

> `/System/Library/DataClassMigrators/MobileActivationMigrator.migrator/MobileActivationMigrator`

```diff

-1076.100.26.0.0
-  __TEXT.__text: 0x2a68
+1076.100.28.0.0
+  __TEXT.__text: 0x2a60
   __TEXT.__auth_stubs: 0x270
   __TEXT.__objc_stubs: 0x800
   __TEXT.__objc_methlist: 0x334
-  __TEXT.__cstring: 0x330a
+  __TEXT.__cstring: 0x333b
   __TEXT.__objc_classname: 0x47
   __TEXT.__objc_methname: 0xc6d
   __TEXT.__objc_methtype: 0x2da

   __DATA_CONST.__auth_got: 0x148
   __DATA_CONST.__got: 0xd0
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x1020
-  __DATA_CONST.__cfstring: 0x5020
+  __DATA_CONST.__const: 0x1028
+  __DATA_CONST.__cfstring: 0x5060
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_arraydata: 0x4d0
+  __DATA_CONST.__objc_arraydata: 0x4d8
   __DATA_CONST.__objc_arrayobj: 0x60
   __DATA.__objc_const: 0x330
   __DATA.__objc_selrefs: 0x3c8

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B46712DB-ADB8-3EE2-AF9F-CE6865B8D3FD
-  Functions: 68
-  Symbols:   1560
-  CStrings:  1455
+  UUID: A20040A7-C8CD-391A-810D-A379E54F1EDB
+  Functions: 67
+  Symbols:   1557
+  CStrings:  1459
 
Symbols:
+ /Library/Caches/com.apple.xbs/53DD53B8-F12F-4B74-9B41-3805AB4ED204/TemporaryDirectory.LZ2YvF/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/MobileActivationMigrator.build/Objects-normal/arm64e/GestaltHlpr.o
+ /Library/Caches/com.apple.xbs/53DD53B8-F12F-4B74-9B41-3805AB4ED204/TemporaryDirectory.LZ2YvF/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/MobileActivationMigrator.build/Objects-normal/arm64e/MobileActivationError.o
+ /Library/Caches/com.apple.xbs/53DD53B8-F12F-4B74-9B41-3805AB4ED204/TemporaryDirectory.LZ2YvF/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/MobileActivationMigrator.build/Objects-normal/arm64e/MobileActivationErrorPrivate.o
+ /Library/Caches/com.apple.xbs/53DD53B8-F12F-4B74-9B41-3805AB4ED204/TemporaryDirectory.LZ2YvF/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/MobileActivationMigrator.build/Objects-normal/arm64e/MobileActivationMigrator.o
+ /Library/Caches/com.apple.xbs/53DD53B8-F12F-4B74-9B41-3805AB4ED204/TemporaryDirectory.LZ2YvF/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/MobileActivationMigrator.build/Objects-normal/arm64e/common.o
+ /Library/Caches/com.apple.xbs/53DD53B8-F12F-4B74-9B41-3805AB4ED204/TemporaryDirectory.LZ2YvF/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/MobileActivationMigrator.build/Objects-normal/arm64e/data_migration_support.o
+ /Library/Caches/com.apple.xbs/53DD53B8-F12F-4B74-9B41-3805AB4ED204/TemporaryDirectory.LZ2YvF/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/MobileActivationMigrator.build/Objects-normal/arm64e/keylist.o
+ /Library/Caches/com.apple.xbs/53DD53B8-F12F-4B74-9B41-3805AB4ED204/TemporaryDirectory.LZ2YvF/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/MobileActivationMigrator.build/Objects-normal/arm64e/vm_support.o
+ /Library/Caches/com.apple.xbs/53DD53B8-F12F-4B74-9B41-3805AB4ED204/TemporaryDirectory.LZ2YvF/Sources/MobileActivation/MobileActivationMigrator/
+ /Library/Caches/com.apple.xbs/53DD53B8-F12F-4B74-9B41-3805AB4ED204/TemporaryDirectory.LZ2YvF/Sources/MobileActivation/shared/
+ __block_literal_global.416
+ __block_literal_global.448
+ __block_literal_global.456
+ _kMAIsFactoryRestoredOverride
- /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/MobileActivationMigrator.build/Objects-normal/arm64e/GestaltHlpr.o
- /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/MobileActivationMigrator.build/Objects-normal/arm64e/MobileActivationError.o
- /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/MobileActivationMigrator.build/Objects-normal/arm64e/MobileActivationErrorPrivate.o
- /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/MobileActivationMigrator.build/Objects-normal/arm64e/MobileActivationMigrator.o
- /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/MobileActivationMigrator.build/Objects-normal/arm64e/common.o
- /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/MobileActivationMigrator.build/Objects-normal/arm64e/data_migration_support.o
- /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/MobileActivationMigrator.build/Objects-normal/arm64e/keylist.o
- /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Binaries/MobileActivation/install/TempContent/Objects/MobileActivation.build/MobileActivationMigrator.build/Objects-normal/arm64e/vm_support.o
- /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Sources/MobileActivation/MobileActivationMigrator/
- /Library/Caches/com.apple.xbs/856C29A2-BA38-4844-8FB6-44959BD96B70/TemporaryDirectory.zMkAyY/Sources/MobileActivation/shared/
- __block_literal_global.413
- __block_literal_global.445
- __block_literal_global.453
- _isRunningInRecovery
Functions:
- _isRunningInRootLaunchdContext
CStrings:
+ "IsFactoryRestoredOverride"
+ "wirelesseventanalyzerd"

```
