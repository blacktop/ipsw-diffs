## AnisetteMigrator

> `/System/Library/DataClassMigrators/AnisetteMigrator.migrator/AnisetteMigrator`

```diff

-20.6.0.0.0
-  __TEXT.__text: 0x530
+20.9.0.0.0
+  __TEXT.__text: 0x544
   __TEXT.__auth_stubs: 0x100
   __TEXT.__objc_stubs: 0x80
   __TEXT.__objc_methlist: 0x2c

   - /System/Library/PrivateFrameworks/DataMigration.framework/DataMigration
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C15217F1-0839-3D61-A5F5-2C735B7130FE
-  Functions: 10
-  Symbols:   107
+  UUID: 2A4825CE-FBD8-3A00-B5B4-BFB5A4F6C361
+  Functions: 12
+  Symbols:   117
   CStrings:  22
 
Symbols:
+ /AppleInternal/Library/BuildRoots/4~CIU-ugAMFu5F4ZgMvGLxpzN-0z-1bVdsnfh8vBQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/lib/libaks.a(libaks.o)
+ /AppleInternal/Library/BuildRoots/4~CIU-ugAMFu5F4ZgMvGLxpzN-0z-1bVdsnfh8vBQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/lib/libaks.a(libaks_internal.o)
+ /Library/Caches/com.apple.xbs/6ABECE83-92AB-47BA-A55B-FD3830B429C4/TemporaryDirectory.kWIQnh/Binaries/Anisette/install/TempContent/Objects/AnisetteMigrator.build/AnisetteMigrator.build/Objects-normal/arm64e/AnisetteMigrator.o
+ /Library/Caches/com.apple.xbs/6ABECE83-92AB-47BA-A55B-FD3830B429C4/TemporaryDirectory.kWIQnh/Sources/Anisette/MigratorPlugin/AnisetteMigrator/
+ /Library/Caches/com.apple.xbs/BED3B4D7-0AE0-4137-801C-27DCB7197E88/TemporaryDirectory.lcvZrq/Sources/AppleKeyStore_libs/
+ _OUTLINED_FUNCTION_0
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_3
+ _objc_retainAutoreleasedReturnValue
- /AppleInternal/Library/BuildRoots/4~CHKxugAVBgF0yDF_OseEybT5vuE5uwbWfbWc51A/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/lib/libaks.a(libaks.o)
- /AppleInternal/Library/BuildRoots/4~CHKxugAVBgF0yDF_OseEybT5vuE5uwbWfbWc51A/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/lib/libaks.a(libaks_internal.o)
- /Library/Caches/com.apple.xbs/Binaries/Anisette/install/TempContent/Objects/AnisetteMigrator.build/AnisetteMigrator.build/Objects-normal/arm64e/AnisetteMigrator.o
- /Library/Caches/com.apple.xbs/Sources/Anisette/MigratorPlugin/AnisetteMigrator/
- /Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/
- _OUTLINED_FUNCTION_4
- _objc_claimAutoreleasedReturnValue
Functions:
~ -[AnisetteMigrator performMigration] : 216 -> 220
+ _OUTLINED_FUNCTION_0
+ _OUTLINED_FUNCTION_11
~ _aks_migrate_path : 316 -> 288

```
