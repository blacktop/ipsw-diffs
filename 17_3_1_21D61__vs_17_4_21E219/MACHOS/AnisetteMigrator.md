## AnisetteMigrator

> `/System/Library/DataClassMigrators/AnisetteMigrator.migrator/AnisetteMigrator`

```diff

-18.4.0.0.0
+18.7.0.0.0
   __TEXT.__text: 0x4f8
   __TEXT.__auth_stubs: 0x100
   __TEXT.__objc_stubs: 0x80

   __DATA_CONST.__cfstring: 0x60
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_classrefs: 0x8
   __DATA.__objc_const: 0x90
   __DATA.__objc_selrefs: 0x38
-  __DATA.__objc_classrefs: 0x8
   __DATA.__objc_data: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/DataMigration.framework/DataMigration
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6AB6DEE9-5B7A-3748-B134-B7917E68A394
+  UUID: C587D794-2ABE-3847-9CBA-769345F8F859
   Functions: 8
   Symbols:   97
   CStrings:  22
Symbols:
+ /AppleInternal/Library/BuildRoots/7f1e11ec-d0b2-11ee-9ae5-9ab3b1a34a63/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.4.Internal.sdk/usr/local/lib/libaks.a(libaks.o)
+ /AppleInternal/Library/BuildRoots/7f1e11ec-d0b2-11ee-9ae5-9ab3b1a34a63/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.4.Internal.sdk/usr/local/lib/libaks.a(libaks_internal.o)
- /AppleInternal/Library/BuildRoots/5a481bbe-9f57-11ee-9024-8efc15467d2d/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.3.Internal.sdk/usr/local/lib/libaks.a(libaks.o)
- /AppleInternal/Library/BuildRoots/5a481bbe-9f57-11ee-9024-8efc15467d2d/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.3.Internal.sdk/usr/local/lib/libaks.a(libaks_internal.o)

```
