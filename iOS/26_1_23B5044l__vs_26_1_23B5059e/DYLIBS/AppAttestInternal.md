## AppAttestInternal

> `/System/Library/PrivateFrameworks/AppAttestInternal.framework/AppAttestInternal`

```diff

-132.0.0.0.0
-  __TEXT.__text: 0x69f90
+132.1.0.0.0
+  __TEXT.__text: 0x69f60
   __TEXT.__auth_stubs: 0x1690
   __TEXT.__objc_methlist: 0x6c4
   __TEXT.__const: 0x3450

   __AUTH_CONST.__objc_const: 0x1938
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_arrayobj: 0x90
-  __AUTH.__objc_data: 0x458
-  __AUTH.__data: 0x310
+  __AUTH.__objc_data: 0x3b8
+  __AUTH.__data: 0x1d0
   __DATA.__objc_ivar: 0x40
-  __DATA.__data: 0x4a8
-  __DATA.__bss: 0x3178
-  __DATA.__common: 0x60
-  __DATA_DIRTY.__objc_data: 0x798
-  __DATA_DIRTY.__data: 0xa88
-  __DATA_DIRTY.__bss: 0x11e0
-  __DATA_DIRTY.__common: 0x128
+  __DATA.__data: 0x490
+  __DATA.__bss: 0x3130
+  __DATA.__common: 0x38
+  __DATA_DIRTY.__objc_data: 0x838
+  __DATA_DIRTY.__data: 0xbe0
+  __DATA_DIRTY.__bss: 0x1220
+  __DATA_DIRTY.__common: 0x150
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/CryptoKit.framework/CryptoKit

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 52D0638F-B250-35B8-9893-EF64B505E81E
+  UUID: F454A32D-BCEA-3F5C-B6E3-77A6562790F7
   Functions: 1367
   Symbols:   1967
   CStrings:  1366
Functions:
~ sub_225c3e118 -> sub_225a71118 : 7464 -> 7508
~ sub_225c40668 -> sub_225a73694 : 10200 -> 10240
~ sub_225c44930 -> sub_225a77984 : 16908 -> 16824
~ sub_225c48ff0 -> sub_225a7bff0 : 5316 -> 5300
~ sub_225c4a5c4 -> sub_225a7d5b4 : 4284 -> 4276
~ sub_225c4ba3c -> sub_225a7ea24 : 7524 -> 7480
~ sub_225c4d7a0 -> sub_225a8075c : 10512 -> 10508
~ sub_225c500b0 -> sub_225a83068 : 17072 -> 17108
~ sub_225c54360 -> sub_225a8733c : 5264 -> 5276
~ sub_225c557f0 -> sub_225a887d8 : 4260 -> 4236
CStrings:
+ "AppAttest (%@-132.1) - %@"
+ "Client connection is ineligible. { clientUUID="
- "AppAttest (%@-132) - %@"
- "Client connection is ineligible. { "

```
