## AnisetteMigrator

> `/System/Library/DataClassMigrators/AnisetteMigrator.migrator/AnisetteMigrator`

```diff

-20.9.0.0.0
-  __TEXT.__text: 0x544
+21.1.0.1.0
+  __TEXT.__text: 0x53c
   __TEXT.__auth_stubs: 0x100
   __TEXT.__objc_stubs: 0x80
   __TEXT.__objc_methlist: 0x2c

   __TEXT.__objc_methname: 0x82
   __TEXT.__objc_methtype: 0x18
   __TEXT.__unwind_info: 0x88
-  __DATA_CONST.__auth_got: 0x88
-  __DATA_CONST.__got: 0x28
   __DATA_CONST.__const: 0x40
   __DATA_CONST.__cfstring: 0x60
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__auth_got: 0x88
+  __DATA_CONST.__got: 0x28
   __DATA.__objc_const: 0x90
   __DATA.__objc_selrefs: 0x38
   __DATA.__objc_data: 0x50

   - /System/Library/PrivateFrameworks/DataMigration.framework/DataMigration
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 05B658E7-F522-37DB-ACDC-CD442A27E229
+  UUID: 394FD101-DA7C-3D56-9039-8BFA2BB84D35
   Functions: 12
   Symbols:   117
   CStrings:  22
Symbols:
+ /AppleInternal/Library/BuildRoots/4~CQQ_ugBQxgh55akxK1fK_xktESItrvjY_1jiBdk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/local/lib/libaks.a(libaks.o)
+ /AppleInternal/Library/BuildRoots/4~CQQ_ugBQxgh55akxK1fK_xktESItrvjY_1jiBdk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/local/lib/libaks.a(libaks_internal.o)
+ /Library/Caches/com.apple.xbs/821B7119-4616-4491-AFC8-3A66BE82F1E2/TemporaryDirectory.P4ojXR/Binaries/Anisette/install/TempContent/Objects/AnisetteMigrator.build/AnisetteMigrator.build/Objects-normal/arm64e/AnisetteMigrator.o
+ /Library/Caches/com.apple.xbs/821B7119-4616-4491-AFC8-3A66BE82F1E2/TemporaryDirectory.P4ojXR/Sources/Anisette/MigratorPlugin/AnisetteMigrator/
+ /Library/Caches/com.apple.xbs/92EE715A-F6E0-410A-96FF-2FB84842CF6C/TemporaryDirectory.rfuYaj/Sources/AppleKeyStore_libs/
+ _objc_claimAutoreleasedReturnValue
- /AppleInternal/Library/BuildRoots/4~CNptugDD7hidYkJ9qpXxOPcp6c4XqaDnG3NbH0Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.5.Internal.sdk/usr/local/lib/libaks.a(libaks.o)
- /AppleInternal/Library/BuildRoots/4~CNptugDD7hidYkJ9qpXxOPcp6c4XqaDnG3NbH0Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.5.Internal.sdk/usr/local/lib/libaks.a(libaks_internal.o)
- /Library/Caches/com.apple.xbs/8463C95E-7775-42C8-A728-A805DBCB5364/TemporaryDirectory.DHo4RD/Sources/AppleKeyStore_libs/
- /Library/Caches/com.apple.xbs/C611421B-698A-4E1C-A450-F6844EB22DC0/TemporaryDirectory.FUQZ2h/Binaries/Anisette/install/TempContent/Objects/AnisetteMigrator.build/AnisetteMigrator.build/Objects-normal/arm64e/AnisetteMigrator.o
- /Library/Caches/com.apple.xbs/C611421B-698A-4E1C-A450-F6844EB22DC0/TemporaryDirectory.FUQZ2h/Sources/Anisette/MigratorPlugin/AnisetteMigrator/
- _objc_retainAutoreleasedReturnValue
Functions:
~ -[AnisetteMigrator performMigration] : 220 -> 212

```
