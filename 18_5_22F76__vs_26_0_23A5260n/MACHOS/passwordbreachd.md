## passwordbreachd

> `/usr/libexec/passwordbreachd`

```diff

-7621.2.5.10.10
-  __TEXT.__text: 0x6c
-  __TEXT.__auth_stubs: 0x50
+7622.1.14.10.4
+  __TEXT.__text: 0x84
+  __TEXT.__auth_stubs: 0x70
+  __TEXT.__cstring: 0x3c
   __TEXT.__unwind_info: 0x58
-  __DATA_CONST.__auth_got: 0x28
+  __DATA_CONST.__auth_got: 0x38
   __DATA_CONST.__got: 0x10
+  __DATA_CONST.__cfstring: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__bss: 0x10
+  - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/SafariCore.framework/SafariCore
   - /System/Library/PrivateFrameworks/SafariShared.framework/SafariShared
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D2B2C2FD-52FC-3367-B364-EFF67E3993D3
+  UUID: 8D4B3341-F6AC-3C88-AF08-2F26E6DDE971
   Functions: 1
-  Symbols:   9
-  CStrings:  0
+  Symbols:   12
+  CStrings:  3
 
Symbols:
+ _WBSSetUpAccessToAppDataContainerWithIdentifier
+ ___CFConstantStringClassReference
+ __set_user_dir_suffix
Functions:
~ sub_1000006e0 -> sub_1000007e0 : 108 -> 132
CStrings:
+ "com.apple.Safari.PasswordBreachAgent"
+ "com.apple.mobilesafari"

```
