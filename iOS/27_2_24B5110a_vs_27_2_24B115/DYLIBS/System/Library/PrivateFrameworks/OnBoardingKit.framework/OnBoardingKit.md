## OnBoardingKit

> `/System/Library/PrivateFrameworks/OnBoardingKit.framework/OnBoardingKit`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`

```diff

 3977.1.4.0.0
-  __TEXT.__text: 0x47824
+  __TEXT.__text: 0x476d8
   __TEXT.__objc_methlist: 0x62c4
   __TEXT.__cstring: 0x19c9
   __TEXT.__const: 0x504

   __DATA_CONST.__objc_arraydata: 0x90
   __DATA_CONST.__got: 0x4f8
   __AUTH_CONST.__const: 0x1c0
-  __AUTH_CONST.__cfstring: 0x20e0
+  __AUTH_CONST.__cfstring: 0x20c0
   __AUTH_CONST.__objc_const: 0xdcd8
   __AUTH_CONST.__objc_intobj: 0x228
   __AUTH_CONST.__objc_dictobj: 0x28

   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 1898
   Symbols:   3484
-  CStrings:  382
+  CStrings:  381
 
Functions:
~ +[OBPrivacyFlow _splashPlistFromBundle:forContentName:] : 160 -> 4
~ -[OBPrivacyFlow _splashLocalizedStringForKey:language:preferredDeviceType:] : 356 -> 180
CStrings:
- "-seed"
```
