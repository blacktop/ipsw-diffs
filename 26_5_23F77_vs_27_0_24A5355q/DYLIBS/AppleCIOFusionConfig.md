## AppleCIOFusionConfig

> `/System/Library/PrivateFrameworks/AppleCIOFusionConfig.framework/AppleCIOFusionConfig`

```diff

-6.0.0.0.0
-  __TEXT.__text: 0x7cd8
-  __TEXT.__auth_stubs: 0x360
-  __TEXT.__cstring: 0x4a0
-  __TEXT.__const: 0x40
-  __TEXT.__oslogstring: 0x113e
-  __TEXT.__unwind_info: 0x78
-  __DATA_CONST.__got: 0x18
-  __AUTH_CONST.__auth_got: 0x1b0
+8.0.0.0.0
+  __TEXT.__text: 0x8b50
+  __TEXT.__cstring: 0x4ba
+  __TEXT.__const: 0x50
+  __TEXT.__oslogstring: 0x113c
+  __TEXT.__unwind_info: 0x310
+  __TEXT.__auth_stubs: 0x0
+  __DATA_CONST.__got: 0x0
+  __AUTH_CONST.__weak_auth_got: 0x20
+  __AUTH_CONST.__auth_got: 0x1d0
   __DATA.__bss: 0x10
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
