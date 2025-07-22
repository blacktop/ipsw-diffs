## PeopleLegacyMessageService

> `/Applications/PeopleMessageService.app/Extensions/PeopleLegacyMessageService.appex/PeopleLegacyMessageService`

```diff

-119.0.0.0.0
+120.0.0.0.0
   __TEXT.__text: 0xa1e0
   __TEXT.__auth_stubs: 0x9e0
   __TEXT.__objc_stubs: 0x100

   __DATA_CONST.__auth_got: 0x4f8
   __DATA_CONST.__got: 0x130
   __DATA_CONST.__auth_ptr: 0xc0
-  __DATA_CONST.__const: 0x1a0
+  __DATA_CONST.__const: 0x1a8
   __DATA_CONST.__cfstring: 0x20
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_catlist: 0x10

   - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftAppleArchive.dylib
+  - /usr/lib/swift/libswiftCallKit.dylib
   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 995E3162-2683-31C7-AC59-4632905F608E
+  UUID: 23A830E9-616E-3623-8F4F-FCD33AB6F61D
   Functions: 95
-  Symbols:   117
+  Symbols:   118
   CStrings:  62
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCallKit

```
