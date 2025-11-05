## SecurityFoundation

> `/System/Library/Frameworks/SecurityFoundation.framework/Versions/A/SecurityFoundation`

```diff

-55289.0.0.0.0
-  __TEXT.__text: 0x42c00
+55290.0.0.0.0
+  __TEXT.__text: 0x435b4
   __TEXT.__auth_stubs: 0x1c20
-  __TEXT.__objc_methlist: 0x4630
+  __TEXT.__objc_methlist: 0x4aa0
   __TEXT.__const: 0x27fef
-  __TEXT.__cstring: 0x7b43
-  __TEXT.__gcc_except_tab: 0x1634
+  __TEXT.__cstring: 0x7b40
+  __TEXT.__gcc_except_tab: 0x1824
   __TEXT.__oslogstring: 0xd8
   __TEXT.__dof_security_: 0x3c6
   __TEXT.__unwind_info: 0x1a70
+  __TEXT.__eh_frame: 0x50
   __TEXT.__objc_classname: 0xe58
   __TEXT.__objc_methname: 0x7f98
   __TEXT.__objc_methtype: 0x2bb2

   __DATA_CONST.__objc_classlist: 0x4a8
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1d08
+  __DATA_CONST.__objc_selrefs: 0x1de0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x2a8
   __AUTH_CONST.__auth_got: 0xe28
   __AUTH_CONST.__const: 0x15d8
   __AUTH_CONST.__cfstring: 0x5760
-  __AUTH_CONST.__objc_const: 0xb858
+  __AUTH_CONST.__objc_const: 0xb0a8
   __AUTH.__objc_data: 0x2e90
   __AUTH.__data: 0x50
   __DATA.__objc_ivar: 0x720

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 4FDFC8E3-483F-37EB-A643-03715E827D61
-  Functions: 1862
-  Symbols:   5351
-  CStrings:  3788
+  UUID: FFE5D70E-5BB4-31E9-9D2D-7BFDD7E41AF3
+  Functions: 1883
+  Symbols:   5393
+  CStrings:  3787
 
Symbols:
+ +[OIDStringCache instance].cold.1
+ +[_SFKeychainManager defaultManager].cold.1
+ +[_SFKeychainManager defaultOverCommitManager].cold.1
+ -[SFMachPort initWithCoder:].cold.1
+ -[SFRSAEncryptionOperation initWithKeySpecifier:].cold.1
+ -[SFRSA_OAEPEncryptionOperation initWithKeySpecifier:maskGenerationFunction:].cold.1
+ -[SFRSA_OAEPEncryptionOperation initWithKeySpecifier:maskGenerationFunction:].cold.2
+ -[SFSymmetricEncryptionOperation initWithKeySpecifier:mode:].cold.1
+ -[SFWrappedKeyCiphertext initWithCiphertext:ciphertextKey:].cold.1
+ -[SFWrappedKeyCiphertext initWithCiphertext:ciphertextKey:].cold.2
+ -[_SFAuthenticatedCiphertext initWithCiphertext:authenticationCode:initializationVector:].cold.1
+ -[_SFAuthenticatedCiphertext initWithCiphertext:authenticationCode:initializationVector:].cold.2
+ -[_SFAuthenticatedCiphertext initWithCiphertext:authenticationCode:initializationVector:].cold.3
+ -[_SFAuthenticatedEncryptionOperation decrypt:withKey:additionalAuthenticatedData:error:].cold.1
+ -[_SFAuthenticatedEncryptionOperation encrypt:withKey:additionalAuthenticatedData:ivGenerator:error:].cold.1
+ -[_SFAuthenticatedEncryptionOperation initWithKeySpecifier:authenticationMode:].cold.1
+ -[_SFAuthenticatedEncryptionOperation initWithKeySpecifier:authenticationMode:].cold.2
+ -[_SFAuthenticatedEncryptionOperation setAuthenticationMode:].cold.1
+ -[_SFCiphertext initWithCiphertext:].cold.1
+ -[_SFECKeyPair initRandomKeyPairWithSpecifier:privateKeyDomain:].cold.1
+ -[_SFIESCiphertext initWithCiphertext:ephemeralSenderPublicKey:authenticationCode:].cold.1
+ -[_SFIESCiphertext initWithCiphertext:ephemeralSenderPublicKey:authenticationCode:].cold.2
+ -[_SFIESCiphertext initWithCiphertext:ephemeralSenderPublicKey:authenticationCode:].cold.3
+ -[_SFIESOperation decrypt:withKey:error:].cold.1
+ -[_SFIESOperation decrypt:withKey:error:].cold.2
+ -[_SFIESOperation encrypt:withKey:error:].cold.1
+ -[_SFIESOperation encrypt:withKey:error:].cold.2
+ -[_SFKeyPair initWithData:specifier:error:].cold.1
+ -[_SFKeyPair initWithData:specifier:error:].cold.2
+ -[_SFKeyPair initWithSecKey:].cold.1
+ -[_SFPublicKey initWithData:specifier:error:].cold.1
+ -[_SFPublicKey initWithData:specifier:error:].cold.2
+ -[_SFPublicKey initWithSecKey:].cold.1
+ -[_SFSymmetricKey initRandomKeyWithSpecifier:error:].cold.1
+ -[_SFSymmetricKey initWithData:specifier:error:].cold.1
+ -[_SFSymmetricKey initWithData:specifier:error:].cold.2
+ GCC_except_table102
+ GCC_except_table104
+ GCC_except_table114
+ GCC_except_table140
+ GCC_except_table146
+ GCC_except_table149
+ GCC_except_table155
+ GCC_except_table176
+ GCC_except_table191
+ GCC_except_table195
+ GCC_except_table198
+ GCC_except_table48
+ GCC_except_table51
+ GCC_except_table62
+ GCC_except_table65
+ GCC_except_table67
+ GCC_except_table69
+ GCC_except_table71
+ GCC_except_table73
+ GCC_except_table75
+ GCC_except_table78
+ GCC_except_table83
+ GCC_except_table87
+ GCC_except_table92
+ GCC_except_table96
+ GCC_except_table99
+ _OUTLINED_FUNCTION_0
+ _OUTLINED_FUNCTION_1
+ __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIP13PWADictionaryNS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIP15CP_FetchedFieldNS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIPKcNS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIPN8Security12CssmAutoDataENS_9allocatorIS3_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIcNS_9allocatorIcEEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIjNS_9allocatorIjEEE20__throw_length_errorB8ne190102Ev
+ __ZNSt12length_errorC1B8ne190102EPKc
+ __ZNSt3__110unique_ptrINS_11__tree_nodeINS_12__value_typeIN8Security4GuidENS3_10CssmClient6ModuleEEEPvEENS_22__tree_node_destructorINS_9allocatorIS9_EEEEE5resetB8ne190102EPS9_
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ne190102ENS_24__uninitialized_size_tagEmRKS4_
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ne190102EPKcm
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ne190102ILi0EEEPKc
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIP13PWADictionaryEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIP15CP_FetchedFieldEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIPKcEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIPN8Security12CssmAutoDataEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIjEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
+ __ZNSt3__120__throw_length_errorB8ne190102EPKc
+ __ZSt28__throw_bad_array_new_lengthB8ne190102v
- GCC_except_table100
- GCC_except_table103
- GCC_except_table105
- GCC_except_table116
- GCC_except_table143
- GCC_except_table147
- GCC_except_table151
- GCC_except_table157
- GCC_except_table183
- GCC_except_table192
- GCC_except_table196
- GCC_except_table199
- GCC_except_table50
- GCC_except_table63
- GCC_except_table66
- GCC_except_table68
- GCC_except_table70
- GCC_except_table72
- GCC_except_table74
- GCC_except_table77
- GCC_except_table85
- GCC_except_table89
- GCC_except_table93
- GCC_except_table97
- __ZN8Security10CssmClient7Context8unstagedEv
- __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIP13PWADictionaryNS_9allocatorIS2_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIP15CP_FetchedFieldNS_9allocatorIS2_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIPKcNS_9allocatorIS2_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIPN8Security12CssmAutoDataENS_9allocatorIS3_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIcNS_9allocatorIcEEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIjNS_9allocatorIjEEE20__throw_length_errorB8ne180100Ev
- __ZNSt12length_errorC1B8ne180100EPKc
- __ZNSt3__110unique_ptrINS_11__tree_nodeINS_12__value_typeIN8Security4GuidENS3_10CssmClient6ModuleEEEPvEENS_22__tree_node_destructorINS_9allocatorIS9_EEEEE5resetB8ne180100EPS9_
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ne180100ENS_24__uninitialized_size_tagEmRKS4_
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ne180100EPKcm
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ne180100ILi0EEEPKc
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIP13PWADictionaryEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIP15CP_FetchedFieldEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIPKcEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIPN8Security12CssmAutoDataEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIjEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__120__throw_length_errorB8ne180100EPKc
- __ZSt28__throw_bad_array_new_lengthB8ne180100v
CStrings:
- "\t "

```
