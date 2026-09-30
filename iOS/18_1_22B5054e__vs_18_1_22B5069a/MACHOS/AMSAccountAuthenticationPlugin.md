## AMSAccountAuthenticationPlugin

> `/System/Library/Accounts/Authentication/AMSAccountAuthenticationPlugin.bundle/AMSAccountAuthenticationPlugin`

```diff

-8.1.12.0.0
+8.1.20.0.0
   __TEXT.__text: 0x91f4
   __TEXT.__auth_stubs: 0x500
   __TEXT.__objc_stubs: 0x1fe0

   __DATA_CONST.__auth_got: 0x290
   __DATA_CONST.__got: 0x1a0
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x600
+  __DATA_CONST.__const: 0x608
   __DATA_CONST.__cfstring: 0x9c0
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_catlist: 0x28

   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
+  - /usr/lib/swift/libswiftCryptoTokenKit.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
   Functions: 120
-  Symbols:   176
+  Symbols:   177
   CStrings:  601
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCryptoTokenKit

```
