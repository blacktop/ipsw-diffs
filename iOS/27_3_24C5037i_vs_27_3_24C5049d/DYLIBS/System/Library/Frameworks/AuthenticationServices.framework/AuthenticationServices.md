## AuthenticationServices

> `/System/Library/Frameworks/AuthenticationServices.framework/AuthenticationServices`

```diff

-626.1.12.10.3
-  __TEXT.__text: 0x142354
+626.1.17.0.0
+  __TEXT.__text: 0x142750
   __TEXT.__objc_methlist: 0x82d0
   __TEXT.__cstring: 0xb708
   __TEXT.__const: 0x14484
   __TEXT.__gcc_except_tab: 0x13a4
-  __TEXT.__oslogstring: 0x393b
+  __TEXT.__oslogstring: 0x3acb
   __TEXT.__dlopen_cstrs: 0x308
   __TEXT.__ustring: 0x6d36
   __TEXT.__swift5_typeref: 0x3662

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 8443
-  Symbols:   6663
-  CStrings:  1377
+  Symbols:   6662
+  CStrings:  1381
 
Symbols:
- ___87-[_ASPasswordManagerIconController _fetchTouchIconForDomain:requestID:responseHandler:]_block_invoke_3
Functions:
~ ___87-[_ASPasswordManagerIconController _fetchTouchIconForDomain:requestID:responseHandler:]_block_invoke_2 : 32 -> 188
~ ___97-[_ASPasswordManagerIconController _requestTouchIconForDomain:options:requestID:responseHandler:]_block_invoke : 852 -> 960
~ ___97-[_ASPasswordManagerIconController _requestTouchIconForDomain:options:requestID:responseHandler:]_block_invoke_2 : 740 -> 1020
~ -[ASAuthorizationController _convertCoreErrorToPublicError:] : 528 -> 596
~ sub_1aecdfe70 -> sub_1aee0e0d4 : 112 -> 124
~ sub_1aecfca5c -> sub_1aee2accc : 252 -> 276
~ sub_1aed17928 -> sub_1aee45bb0 : 276 -> 308
~ sub_1aed17ca8 -> sub_1aee45f50 : 436 -> 480
~ sub_1aed17e5c -> sub_1aee46130 : 260 -> 284
~ sub_1aed17f60 -> sub_1aee4624c : 260 -> 284
~ sub_1aed18064 -> sub_1aee46368 : 260 -> 276
~ sub_1aed27704 -> sub_1aee55a18 : 432 -> 476
~ sub_1aed278b4 -> sub_1aee55bf4 : 256 -> 280
~ sub_1aed279b4 -> sub_1aee55d0c : 272 -> 308
~ sub_1aed27ac4 -> sub_1aee55e40 : 248 -> 272
~ sub_1aed27bbc -> sub_1aee55f50 : 256 -> 272
~ sub_1aed27cbc -> sub_1aee56060 : 272 -> 308
~ sub_1aed3f4c0 -> sub_1aee6d888 : 2052 -> 2064
~ sub_1aed42f1c -> sub_1aee712f0 : 3436 -> 3464
~ sub_1aed43d60 -> sub_1aee72150 : 524 -> 536
CStrings:
+ "Checked for a local visit before fetching touch icon; domain=%{sensitive, mask.hash}@; foundLocalVisit=%{bool}d"
+ "Finished fetching touch icon; domain=%{sensitive, mask.hash}@; isGenerated=%{bool}d"
+ "Received generated touch icon; domain=%{sensitive, mask.hash}@"
+ "Skipping touch icon fetch until the retry date; domain=%{sensitive, mask.hash}@; retryDate=%{public}@"
+ "Will not retry touch icon fetch until the retry date; domain=%{sensitive, mask.hash}@; retryDate=%{public}@"
- "Finished fetching touch icon; domain=%{sensitive, mask.hash}@"
```
