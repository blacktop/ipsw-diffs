## AppleAccountMigrator

> `/System/Library/DataClassMigrators/AppleAccountMigrator.migrator/AppleAccountMigrator`

```diff

-1007.230.0.0.0
-  __TEXT.__text: 0x2240
-  __TEXT.__auth_stubs: 0x220
-  __TEXT.__objc_stubs: 0x6e0
-  __TEXT.__objc_methlist: 0xe0
+1007.456.0.0.0
+  __TEXT.__text: 0x2140
+  __TEXT.__auth_stubs: 0x200
+  __TEXT.__objc_stubs: 0x700
+  __TEXT.__objc_methlist: 0xd4
   __TEXT.__const: 0x2c
   __TEXT.__gcc_except_tab: 0x44
   __TEXT.__cstring: 0xff
-  __TEXT.__objc_methname: 0x5ca
-  __TEXT.__oslogstring: 0x748
+  __TEXT.__objc_methname: 0x5e6
+  __TEXT.__oslogstring: 0x707
   __TEXT.__objc_classname: 0x18
   __TEXT.__objc_methtype: 0x4a
   __TEXT.__dlopen_cstrs: 0x56
   __TEXT.__unwind_info: 0xc0
-  __DATA_CONST.__auth_got: 0x120
-  __DATA_CONST.__got: 0xe8
+  __DATA_CONST.__auth_got: 0x110
+  __DATA_CONST.__got: 0xb8
   __DATA_CONST.__const: 0x60
   __DATA_CONST.__cfstring: 0x140
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA.__objc_const: 0xf8
-  __DATA.__objc_selrefs: 0x1e8
+  __DATA.__objc_selrefs: 0x1f0
   __DATA.__objc_ivar: 0xc
   __DATA.__objc_data: 0x50
   __DATA.__bss: 0x10

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 32
-  Symbols:   73
+  Functions: 30
+  Symbols:   65
   CStrings:  127
 
Symbols:
+ _OBJC_CLASS_$_AAAppleAccountInformationCache
- _AAPrefsDomain
- _CFPreferencesSetAppValue
- _CFPreferencesSynchronize
- _kAAAccountFullName
- _kAAAccountIsSignedInKey
- _kAAAccountUsername
- _kAAProfilePictureCacheURL
- _kCFPreferencesAnyHost
- _kCFPreferencesCurrentUser
CStrings:
+ "clearNonSecureAAPrefsDomain"
+ "migrateToPrimaryAccountSignInState"
- "Cleared Apple Account Information Properties from AAPrefsDomain."
- "_clearAppleAccountInformationCache"

```
