## OnBoardingKit

> `/System/Library/PrivateFrameworks/OnBoardingKit.framework/OnBoardingKit`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`

```diff

 3977.0.23.0.0
-  __TEXT.__text: 0x48988
+  __TEXT.__text: 0x48830
   __TEXT.__objc_methlist: 0x61bc
   __TEXT.__cstring: 0x1939
   __TEXT.__const: 0x504

   __DATA_CONST.__objc_arraydata: 0x90
   __DATA_CONST.__got: 0x4f8
   __AUTH_CONST.__const: 0x1c0
-  __AUTH_CONST.__cfstring: 0x2080
+  __AUTH_CONST.__cfstring: 0x2060
   __AUTH_CONST.__objc_const: 0xdb38
   __AUTH_CONST.__objc_intobj: 0x1f8
   __AUTH_CONST.__objc_dictobj: 0x28

   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 1874
   Symbols:   5006
-  CStrings:  376
+  CStrings:  375
 
Functions:
~ +[OBPrivacyFlow _splashPlistFromBundle:forContentName:] : 172 -> 4
~ -[OBPrivacyFlow _splashLocalizedStringForKey:language:preferredDeviceType:] : 368 -> 192
CStrings:
- "-seed"
```
