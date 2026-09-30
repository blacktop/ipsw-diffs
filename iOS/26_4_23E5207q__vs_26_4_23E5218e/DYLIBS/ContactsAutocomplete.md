## ContactsAutocomplete

> `/System/Library/PrivateFrameworks/ContactsAutocomplete.framework/ContactsAutocomplete`

```diff

-1356.500.31.0.0
-  __TEXT.__text: 0x59b0c
+1356.500.32.0.0
+  __TEXT.__text: 0x59ae4
   __TEXT.__auth_stubs: 0x1130
   __TEXT.__objc_methlist: 0x4544
   __TEXT.__const: 0x3620
-  __TEXT.__oslogstring: 0x369c
+  __TEXT.__oslogstring: 0x36ac
   __TEXT.__cstring: 0x2485
   __TEXT.__gcc_except_tab: 0x6fc
   __TEXT.__constg_swiftt: 0xc84

   __TEXT.__objc_methtype: 0x1217
   __TEXT.__objc_stubs: 0x88e0
   __DATA_CONST.__got: 0x890
-  __DATA_CONST.__const: 0x1798
+  __DATA_CONST.__const: 0x1790
   __DATA_CONST.__objc_classlist: 0x3c0
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x100

   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
-  - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 12B7FF18-1157-38DF-AA4B-98ACDA300EBA
+  UUID: C017DFA3-E072-3AB7-856C-FA29F8982F32
   Functions: 2792
-  Symbols:   6724
+  Symbols:   6722
   CStrings:  2925
 
Symbols:
- __swift_FORCE_LOAD_$_swiftCoreImage
- __swift_FORCE_LOAD_$_swiftCoreImage_$_ContactsAutocomplete
Functions:
~ ___74+[CNAutocompleteRecentContactsLibrary addLoggingHandlersToFuture:request:]_block_invoke : 796 -> 792
~ sub_21bbe3d70 -> sub_21bbf7d24 : 1388 -> 1452
~ sub_21bbe9868 -> sub_21bbfd85c : 1480 -> 1472
~ sub_21bc03350 -> sub_21bc1733c : 2516 -> 2476
~ sub_21bc03e1c -> sub_21bc17de0 : 3624 -> 3604
~ sub_21bc05b84 -> sub_21bc19b34 : 1524 -> 1492
CStrings:
+ "CoreRecents results (first 200 out of %@): %{private}@"
+ "Repro string: %{private}@"
- "CoreRecents results (first 200 out of %@): %@"
- "Repro string: %@"

```
