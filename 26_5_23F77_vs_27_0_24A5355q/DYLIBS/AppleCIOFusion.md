## AppleCIOFusion

> `/System/Library/PrivateFrameworks/AppleCIOFusion.framework/AppleCIOFusion`

```diff

-6.0.0.0.0
-  __TEXT.__text: 0xc748
-  __TEXT.__auth_stubs: 0x460
-  __TEXT.__cstring: 0x8b3
-  __TEXT.__const: 0x4d
-  __TEXT.__oslogstring: 0x185e
-  __TEXT.__unwind_info: 0x80
-  __DATA_CONST.__got: 0x18
-  __AUTH_CONST.__auth_got: 0x230
+8.0.0.0.0
+  __TEXT.__text: 0xd598
+  __TEXT.__cstring: 0x8d7
+  __TEXT.__const: 0x7f
+  __TEXT.__oslogstring: 0x185c
+  __TEXT.__unwind_info: 0x470
+  __TEXT.__auth_stubs: 0x0
+  __DATA_CONST.__got: 0x0
+  __AUTH_CONST.__weak_auth_got: 0x28
+  __AUTH_CONST.__auth_got: 0x248
   __DATA.__bss: 0x10
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
