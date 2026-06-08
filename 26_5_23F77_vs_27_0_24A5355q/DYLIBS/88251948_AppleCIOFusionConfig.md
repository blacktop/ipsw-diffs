## AppleCIOFusionConfig

> `/System/Library/PrivateFrameworks/AppleCIOFusionConfig.framework/AppleCIOFusionConfig`

```diff

-6.0.0.0.0
-  __TEXT.__text: 0x7cd8 sha256:fd61568cc6116b5cf196392bc201a46e492bd60de9b246f9391aad44235c74cf
-  __TEXT.__auth_stubs: 0x360 sha256:43dd1c015f2daa238a9e1ef67374c30335a4493f9d2c9004f76dd8d9b676c652
-  __TEXT.__cstring: 0x4a0 sha256:18261e38cc3ffced34aba227c7ebc29130a46d8c7f3b0fae1a5070994f31e1e8
-  __TEXT.__const: 0x40 sha256:59936b04cdfd694b482237b6f02584a373b3c94fad7a06a9c622653f7fcfd6d2
-  __TEXT.__oslogstring: 0x113e sha256:150663bf43713ed3344cfcd2745047e18d126facddc7eca416740244e93ae6e5
-  __TEXT.__unwind_info: 0x78 sha256:dea7dc762947b0c126cc7af4738a1d13da5748f39e928fc0b1b63f8d6d1d1d3a
-  __DATA_CONST.__got: 0x18 sha256:9d908ecfb6b256def8b49a7c504e6c889c4b0e41fe6ce3e01863dd7b61a20aa0
-  __AUTH_CONST.__auth_got: 0x1b0 sha256:aa79d41be45f6e84fdf18d40d2a9d92f6fb6532642b2ea4f175f708a5d98eb18
+8.0.0.0.0
+  __TEXT.__text: 0x8b50 sha256:fd71602694a3a4d77becfad6e2fa3477ba8b7d0c3a7ceafa7fc6c86190d924fc
+  __TEXT.__cstring: 0x4ba sha256:3d4c30c7ba78b65a5118c6ac5c99fc2a6f0f827ceeb6618a4a57513176b5fbf2
+  __TEXT.__const: 0x50 sha256:f6cbed802b949fe197bf4c6d8ac5eccac906fe49cc6d2ee9d899b4f42044aa61
+  __TEXT.__oslogstring: 0x113c sha256:2b2dd951aa534b28fd2156a3b234975827ac79e81763aeb6937710b1765ad4f1
+  __TEXT.__unwind_info: 0x310 sha256:3ef94c02eef35ae68caf96e6d350218cbfda325dd305edbb6f74e3b35875c61c
+  __TEXT.__auth_stubs: 0x0
+  __DATA_CONST.__got: 0x0
+  __AUTH_CONST.__weak_auth_got: 0x20 sha256:c72c4599d3c96a5e0183ff61c11bf482e7f4b47a643231ca4b01bdc04aa217a4
+  __AUTH_CONST.__auth_got: 0x1d0 sha256:7c4c2b940c41426e36a4cf6c83afababacfb8bb1a1dc39162a95bb812e1d109f
   __DATA.__bss: 0x10 sha256:374708fff7719dd5979ec875d56cd2286f6d3cf7ec317a3b25632aab28ec37bb
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
-  - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
+  - /System/Library/Frameworks/Security.framework/Security
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: 3C41E2BE-3ED0-3A93-97CE-069BA10FB119
-  Functions: 175
-  Symbols:   65
-  CStrings:  113
+  UUID: 674FDD6E-0CC0-3F70-9850-08FF19B1CCB9
+  Functions: 178
+  Symbols:   85
+  CStrings:  112
 
Symbols:
+ _CFDataCreate
+ _CFDataGetBytePtr
+ _CFDataGetLength
+ _CFDictionaryCreateMutable
+ _CFDictionaryGetValue
+ _CFDictionarySetValue
+ _CFRelease
+ _CFStringCreateWithCString
+ _SecItemAdd
+ _SecItemCopyMatching
+ _SecItemUpdate
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEPKcm
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE9push_backEc
+ __ZNSt3__19to_stringEj
+ _kCFBooleanTrue
+ _kCFTypeDictionaryKeyCallBacks
+ _kCFTypeDictionaryValueCallBacks
+ _kSecAttrAccount
+ _kSecAttrGeneric
+ _kSecAttrService
+ _kSecClass
+ _kSecClassGenericPassword
+ _kSecMatchLimit
+ _kSecMatchLimitOne
+ _kSecReturnAttributes
+ _kSecReturnData
+ _kSecUseDataProtectionKeychain
+ _kSecValueData
+ _memchr
+ _strtoul
- _IOConnectCallMethod
- _IOConnectRelease
- _IOObjectRelease
- _IOServiceGetMatchingService
- _IOServiceMatching
- _IOServiceOpen
- _kIOMainPortDefault
- _mach_error_string
- _mach_task_self_
- _strlcpy
CStrings:
+ "(%s:%s:%u) CryptoKey size mismatch."
+ "(%s:%s:%u) ensemble info field count mismatch: expected %u hostnames, got %zu"
+ "(%s:%s:%u) ensemble info parse error: mode"
+ "(%s:%s:%u) ensemble info parse error: node_count"
+ "(%s:%s:%u) ensemble info parse error: node_rank"
+ "(%s:%s:%u) ensemble info too few fields: %zu"
+ "(%s:%s:%u) hostname strdup failed: %u"
+ "(%s:%s:%u) load_ensemble_info failed: %d"
+ "(%s:%s:%u) save_ensemble_info failed: %d"
+ "deserialize_ensemble_info"
- "(%s:%s:%u) Failed to create matching dictionary"
- "(%s:%s:%u) IOServiceOpen: %s"
- "(%s:%s:%u) Service not found: %s"
- "(%s:%s:%u) get_field CryptoKey failed"
- "(%s:%s:%u) get_field EnsembleInfo failed"
- "(%s:%s:%u) hostname strdup failedL: %u"
- "(%s:%s:%u) invalid hostname length: %u"
- "(%s:%s:%u) invlalid null info pointer"
- "(%s:%s:%u) service connection failed"
- "(%s:%s:%u) set_field CryptoKey failed"
- "(%s:%s:%u) set_field EnsembleInfo failed"

```
