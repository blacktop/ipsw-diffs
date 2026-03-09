## VoiceShortcutClient

> `/System/Library/PrivateFrameworks/VoiceShortcutClient.framework/VoiceShortcutClient`

```diff

-4527.0.1.0.0
-  __TEXT.__text: 0x13dc54
-  __TEXT.__auth_stubs: 0x37d0
+4528.0.4.2.0
+  __TEXT.__text: 0x13dc48
+  __TEXT.__auth_stubs: 0x37c0
   __TEXT.__objc_methlist: 0xc644
   __TEXT.__const: 0xd188
   __TEXT.__dlopen_cstrs: 0xdb4
-  __TEXT.__cstring: 0x16fe1
+  __TEXT.__cstring: 0x16eb0
   __TEXT.__swift5_typeref: 0x2fc3
   __TEXT.__swift5_reflstr: 0x136a
   __TEXT.__swift5_assocty: 0x390

   __DATA_CONST.__objc_protorefs: 0xa0
   __DATA_CONST.__objc_superrefs: 0x798
   __DATA_CONST.__objc_arraydata: 0x1a10
-  __AUTH_CONST.__auth_got: 0x1c00
+  __AUTH_CONST.__auth_got: 0x1bf8
   __AUTH_CONST.__const: 0x8488
   __AUTH_CONST.__cfstring: 0x18ac0
   __AUTH_CONST.__objc_const: 0x19428

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 32D1A788-D845-3FAE-9C37-B937EDE9AB4B
+  UUID: F2DF6FE3-6ED4-3C0A-91FE-236EB04C98EC
   Functions: 9496
-  Symbols:   19559
-  CStrings:  12709
+  Symbols:   19558
+  CStrings:  12708
 
Symbols:
+ _BiomeLibraryLibraryCore.frameworkLibrary.20530
+ _ContentKitLibrary.19119
+ _ContentKitLibraryCore.frameworkLibrary.19130
+ _UIKitLibrary.19641
+ _UIKitLibraryCore.frameworkLibrary.19155
+ _UIKitLibraryCore.frameworkLibrary.19651
+ __ZNSt3__119__allocate_at_leastB9nqe210106INS_9allocatorIPU8__strongP21WFDebouncerPokeReasonEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS9_m
+ __ZNSt3__15dequeIU8__strongP21WFDebouncerPokeReasonNS_9allocatorIS3_EEED2B9nqe210106Ev
+ __ZSt28__throw_bad_array_new_lengthB9nqe210106v
+ ___BiomeLibraryLibraryCore_block_invoke.20531
+ ___Block_byref_object_copy_.19139
+ ___Block_byref_object_copy_.21072
+ ___Block_byref_object_dispose_.19140
+ ___Block_byref_object_dispose_.21073
+ ___ContentKitLibraryCore_block_invoke.19131
+ ___UIKitLibraryCore_block_invoke.19156
+ ___UIKitLibraryCore_block_invoke.19652
+ ___block_literal_global.17674
+ ___block_literal_global.18308
+ ___block_literal_global.18370
+ ___block_literal_global.185.21078
+ ___block_literal_global.19149
+ ___block_literal_global.19199
+ ___block_literal_global.19210
+ ___block_literal_global.194.21070
+ ___block_literal_global.19468
+ ___block_literal_global.19728
+ ___block_literal_global.20209
+ ___block_literal_global.20397
+ ___block_literal_global.21218
+ ___block_literal_global.50.17955
+ ___getBiomeLibrarySymbolLoc_block_invoke.20521
+ ___getWFContentItemClass_block_invoke.19143
+ ___getWFStringContentItemClass_block_invoke.19118
+ _audit_stringBiomeLibrary.20535
+ _audit_stringContentKit.19136
+ _audit_stringUIKit.19159
+ _audit_stringUIKit.19655
+ _getBiomeLibrarySymbolLoc.ptr.20520
+ _getWFContentItemClass.softClass.19142
+ _getWFStringContentItemClass.softClass.19117
- _BiomeLibraryLibraryCore.frameworkLibrary.20531
- _ContentKitLibrary.19120
- _ContentKitLibraryCore.frameworkLibrary.19131
- _UIKitLibrary.19642
- _UIKitLibraryCore.frameworkLibrary.19156
- _UIKitLibraryCore.frameworkLibrary.19652
- __ZNSt3__119__allocate_at_leastB9foe210106INS_9allocatorIPU8__strongP21WFDebouncerPokeReasonEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS9_m
- __ZNSt3__132__internal_log_hardening_failureEPKc
- __ZNSt3__15dequeIU8__strongP21WFDebouncerPokeReasonNS_9allocatorIS3_EEED2B9foe210106Ev
- __ZSt28__throw_bad_array_new_lengthB9foe210106v
- ___BiomeLibraryLibraryCore_block_invoke.20532
- ___Block_byref_object_copy_.19140
- ___Block_byref_object_copy_.21073
- ___Block_byref_object_dispose_.19141
- ___Block_byref_object_dispose_.21074
- ___ContentKitLibraryCore_block_invoke.19132
- ___UIKitLibraryCore_block_invoke.19157
- ___UIKitLibraryCore_block_invoke.19653
- ___block_literal_global.17675
- ___block_literal_global.18309
- ___block_literal_global.18371
- ___block_literal_global.185.21079
- ___block_literal_global.19150
- ___block_literal_global.19200
- ___block_literal_global.19211
- ___block_literal_global.194.21071
- ___block_literal_global.19469
- ___block_literal_global.19729
- ___block_literal_global.20210
- ___block_literal_global.20398
- ___block_literal_global.21219
- ___block_literal_global.50.17956
- ___getBiomeLibrarySymbolLoc_block_invoke.20522
- ___getWFContentItemClass_block_invoke.19144
- ___getWFStringContentItemClass_block_invoke.19119
- _audit_stringBiomeLibrary.20536
- _audit_stringContentKit.19137
- _audit_stringUIKit.19160
- _audit_stringUIKit.19656
- _getBiomeLibrarySymbolLoc.ptr.20521
- _getWFContentItemClass.softClass.19143
- _getWFStringContentItemClass.softClass.19118
Functions:
~ -[WFAutoShortcutEntityInfo initWithCoder:] : 284 -> 296
~ __ZNSt3__15dequeIU8__strongP21WFDebouncerPokeReasonNS_9allocatorIS3_EEE9pop_frontEv : 152 -> 128
CStrings:
- "/AppleInternal/Library/BuildRoots/4~CJl1ugASpRaqYl2qoYAASrB1dy9AESDksCxUR9w/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:2296: libc++ Hardening assertion !empty() failed: deque::pop_front called on an empty deque\n"

```
