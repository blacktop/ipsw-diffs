## AppAttestInternal

> `/System/Library/PrivateFrameworks/AppAttestInternal.framework/AppAttestInternal`

```diff

-154.0.0.0.0
-  __TEXT.__text: 0x69b78
+156.0.0.0.0
+  __TEXT.__text: 0x69c58
   __TEXT.__objc_methlist: 0x6c4
   __TEXT.__const: 0x4550
-  __TEXT.__cstring: 0x651e
+  __TEXT.__cstring: 0x659e
   __TEXT.__oslogstring: 0x386a
   __TEXT.__gcc_except_tab: 0x724
   __TEXT.__swift5_typeref: 0xb06

   __AUTH_CONST.__objc_const: 0x1938
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_arrayobj: 0x90
-  __AUTH_CONST.__auth_got: 0xbe8
+  __AUTH_CONST.__auth_got: 0xbf0
   __AUTH.__objc_data: 0x3b8
   __AUTH.__data: 0x2e0
   __DATA.__objc_ivar: 0x40

   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 1489
   Symbols:   1344
-  CStrings:  826
+  CStrings:  829
 
Functions:
~ sub_22c4e2670 -> sub_22bd0e670 : 8796 -> 8800
~ sub_22c4e53d8 -> sub_22bd113dc : 564 -> 784
CStrings:
+ "AppAttest (%@-156) - %@"
+ "Not fetching CD hash."
+ "Should fetch CD hash. { source=default }"
+ "Should fetch CD hash. { source=entitlement }"
- "AppAttest (%@-154) - %@"
```
