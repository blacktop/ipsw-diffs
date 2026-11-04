## EmailCore

> `/System/Library/PrivateFrameworks/EmailCore.framework/EmailCore`

```diff

-3901.200.71.2.2
-  __TEXT.__text: 0x5b034
+3901.300.26.0.0
+  __TEXT.__text: 0x60214
   __TEXT.__objc_methlist: 0x5108
   __TEXT.__gcc_except_tab: 0x7344
-  __TEXT.__const: 0x11e0
-  __TEXT.__cstring: 0x837e
+  __TEXT.__const: 0x1560
+  __TEXT.__cstring: 0x83fe
   __TEXT.__oslogstring: 0xcc5
   __TEXT.__ustring: 0x90
-  __TEXT.__constg_swiftt: 0x88
-  __TEXT.__swift5_typeref: 0x124
-  __TEXT.__swift5_reflstr: 0x4e3
-  __TEXT.__swift5_fieldmd: 0x360
-  __TEXT.__swift5_proto: 0xc
-  __TEXT.__swift5_types: 0xc
+  __TEXT.__constg_swiftt: 0x148
+  __TEXT.__swift5_typeref: 0x1ac
+  __TEXT.__swift5_reflstr: 0x5a3
+  __TEXT.__swift5_fieldmd: 0x430
+  __TEXT.__swift5_proto: 0x24
+  __TEXT.__swift5_types: 0x20
   __TEXT.__swift5_assocty: 0x18
-  __TEXT.__unwind_info: 0x2df8
+  __TEXT.__unwind_info: 0x2f10
+  __TEXT.__eh_frame: 0x1c0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x278
   __DATA_CONST.__objc_arraydata: 0x80
-  __DATA_CONST.__got: 0x6b0
-  __AUTH_CONST.__const: 0x2288
+  __DATA_CONST.__got: 0x778
+  __AUTH_CONST.__const: 0x24f9
   __AUTH_CONST.__cfstring: 0x5480
   __AUTH_CONST.__objc_const: 0xa990
   __AUTH_CONST.__objc_arrayobj: 0xf0
   __AUTH_CONST.__objc_intobj: 0x198
-  __AUTH_CONST.__auth_got: 0xa28
+  __AUTH_CONST.__auth_got: 0xc98
   __AUTH.__objc_data: 0x128
-  __AUTH.__data: 0xba0
+  __AUTH.__data: 0xc20
   __DATA.__objc_ivar: 0x4bc
-  __DATA.__data: 0xe00
+  __DATA.__data: 0xec8
   __DATA.__common: 0x24
   __DATA_DIRTY.__objc_data: 0x2058
   __DATA_DIRTY.__data: 0x378
   __DATA_DIRTY.__bss: 0x1b8
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
+  - /System/Library/Frameworks/CryptoKit.framework/CryptoKit
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/GSS.framework/GSS
   - /System/Library/Frameworks/Network.framework/Network

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2051
-  Symbols:   4180
-  CStrings:  1540
+  Functions: 2135
+  Symbols:   4239
+  CStrings:  1544
 
Symbols:
+ _SecItemAdd
+ _SecItemCopyMatching
+ _SecItemDelete
+ ___swift_destroy_boxed_opaque_existential_0Tm
+ ___swift_memcpy56_8
+ ___swift_memcpy5_4
+ ___swift_project_boxed_opaque_existential_1
+ __swiftEmptyDictionarySingleton
+ _associated conformance 9EmailCore13ECWebPushKeysV15DecryptionErrorOSHAASQ
+ _get_enum_tag_for_layout_string 10Foundation4DataV15_RepresentationO
+ _kSecAttrAccessGroup
+ _kSecAttrAccessible
+ _kSecAttrAccessibleAfterFirstUnlockThisDeviceOnly
+ _kSecAttrAccount
+ _kSecAttrLabel
+ _kSecAttrService
+ _kSecAttrSynchronizable
+ _kSecClass
+ _kSecClassGenericPassword
+ _kSecMatchLimit
+ _kSecMatchLimitOne
+ _kSecReturnData
+ _kSecUseDataProtectionKeychain
+ _kSecValueData
+ _swift_allocError
+ _swift_cvw_initStructMetadataWithLayoutString
+ _swift_cvw_initWithTake
+ _swift_errorRelease
+ _swift_getEnumTagSinglePayloadGeneric
+ _swift_getForeignTypeMetadata
+ _swift_getSingletonMetadata
+ _swift_release_x1
+ _swift_release_x21
+ _swift_release_x23
+ _swift_release_x26
+ _swift_release_x28
+ _swift_release_x8
+ _swift_retain
+ _swift_retain_x22
+ _swift_retain_x23
+ _swift_setDeallocating
+ _swift_storeEnumTagSinglePayloadGeneric
+ _swift_willThrow
+ _symbolic SS_ypt
+ _symbolic Say_____G s5UInt8V
+ _symbolic _____ 10Foundation4DataV
+ _symbolic _____ 9CryptoKit4P256O12KeyAgreementO07PrivateD0V
+ _symbolic _____ 9EmailCore13ECWebPushKeysV
+ _symbolic _____ 9EmailCore13ECWebPushKeysV13KeychainErrorO
+ _symbolic _____ 9EmailCore13ECWebPushKeysV15DecryptionErrorO
+ _symbolic _____ 9EmailCore13ECWebPushKeysV6Header33_4462BD5618A41328107C4FE85D9C2F6FLLV
+ _symbolic _____ s5Int32V
+ _symbolic _____ s6UInt32V
+ _symbolic ______p 10Foundation15ContiguousBytesP
+ _symbolic _____ySS_yptG s23_ContiguousArrayStorageC
+ _symbolic _____ySSypG s18_DictionaryStorageC
+ _symbolic _____y_____G 9CryptoKit24HashedAuthenticationCodeV AA6SHA256V
+ _symbolic _____y_____G s23_ContiguousArrayStorageC s5UInt8V
+ _type_layout_string 9EmailCore13ECWebPushKeysV6Header33_4462BD5618A41328107C4FE85D9C2F6FLLV
CStrings:
+ "Content-Encoding: aes128gcm"
+ "Content-Encoding: nonce"
+ "ECWebPushKeys(<redacted>)"
+ "com.apple.email.webpush.keys"
```
