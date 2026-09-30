## AppleCIOFusion

> `/System/Library/PrivateFrameworks/AppleCIOFusion.framework/AppleCIOFusion`

```diff

-6.0.0.0.0
-  __TEXT.__text: 0xc748 sha256:6838d707eb71d1264bd014e2dfa0d9a5dd1627fdde43bd1e8d97e89098b9ba4b
-  __TEXT.__auth_stubs: 0x460 sha256:4c1da3f15db6323725acf767f1fd109ac4c6505cbfc5bc9b3a23ee5c60e5ef6e
-  __TEXT.__cstring: 0x8b3 sha256:21e7dd359453e9503456a6aeab6238be0172271dbb936ee3ac26b113ff5c43ba
-  __TEXT.__const: 0x4d sha256:153dedc5f45ea89a0d71e274e68b6c4e28c5c0d0a2ed0cfc6cd9806219078221
-  __TEXT.__oslogstring: 0x185e sha256:532026b1873f4c26e617df3e7aa5552e033ded8be856ec24cb9fcdcea7870bb7
-  __TEXT.__unwind_info: 0x80 sha256:2ce4af42b6f76aa9b77a870c174112c1923901fc67a79e54ff38d177f3b623f4
-  __DATA_CONST.__got: 0x18 sha256:9d908ecfb6b256def8b49a7c504e6c889c4b0e41fe6ce3e01863dd7b61a20aa0
-  __AUTH_CONST.__auth_got: 0x230 sha256:df4c9c97af19e0249f4ecd2092184f3751e052d37ddffb883c15a10391de62e7
+8.0.0.0.0
+  __TEXT.__text: 0xd598 sha256:9311080593537af5fbef51eac3e3d69d67d23d481d186b1f5d6a593712ccc77a
+  __TEXT.__cstring: 0x8d7 sha256:d478a4cba2fd7564df77d71a587515047b8d8ff4d9951a2e93c2c2dd9135b40b
+  __TEXT.__const: 0x7f sha256:a575f2ff518d9e588927cd793d5156895c942e498ba579e04c33e916827e1729
+  __TEXT.__oslogstring: 0x185c sha256:7dc68977ef866e4af0b1c50514ce2471ff0bae3ae8b7d4cb67e82c8be3998b32
+  __TEXT.__unwind_info: 0x470 sha256:e0bbe3bc514a539a60d626ede1729132c58956689f6f98d3303f2a40a41cff46
+  __TEXT.__auth_stubs: 0x0
+  __DATA_CONST.__got: 0x0
+  __AUTH_CONST.__weak_auth_got: 0x28 sha256:b040bc26e673bc567968b6c6b44265d87612b5bc20e5693f068f11eff3cf2277
+  __AUTH_CONST.__auth_got: 0x248 sha256:62ec1707572ac5078d31a687a5d23de0c6d2a58d3462efb7039957548a7986cc
   __DATA.__bss: 0x10 sha256:374708fff7719dd5979ec875d56cd2286f6d3cf7ec317a3b25632aab28ec37bb
+  - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
+  - /System/Library/Frameworks/Security.framework/Security
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: CC6983F9-B4BD-3F0A-A347-1CD503ECA07A
-  Functions: 257
-  Symbols:   82
+  UUID: 45D13374-1C4D-359F-9C8B-AA371A81CF85
+  Functions: 263
+  Symbols:   102
   CStrings:  175
 
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
+ "chunk_tag"
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
