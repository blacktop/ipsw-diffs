## libsystem_eligibility.dylib

> `/usr/lib/system/libsystem_eligibility.dylib`

```diff

-289.80.56.0.0
-  __TEXT.__text: 0x42e4
+319.100.51.502.1
+  __TEXT.__text: 0x3ab8
   __TEXT.__auth_stubs: 0x280
-  __TEXT.__const: 0x80
-  __TEXT.__cstring: 0x4044
-  __TEXT.__oslogstring: 0x3d6
+  __TEXT.__const: 0x5c0
+  __TEXT.__cstring: 0x45d3
+  __TEXT.__oslogstring: 0x39b
   __TEXT.__unwind_info: 0xb8
   __DATA_CONST.__got: 0x28
-  __DATA_CONST.__const: 0x600
+  __DATA_CONST.__const: 0xb88
   __AUTH_CONST.__auth_got: 0x140
   __AUTH_CONST.__const: 0x40
   __DATA_DIRTY.__bss: 0x10

   - /usr/lib/system/libsystem_malloc.dylib
   - /usr/lib/system/libsystem_trace.dylib
   - /usr/lib/system/libxpc.dylib
-  UUID: 48E209A4-AA7D-35FB-BB71-EC29242F1120
-  Functions: 26
+  UUID: 29BD257B-0716-38D7-9EDD-77FEB487ECEF
+  Functions: 25
   Symbols:   86
-  CStrings:  416
+  CStrings:  434
 
Symbols:
+ ___block_descriptor_tmp.400
- ___block_descriptor_tmp.380
CStrings:
+ "OS_ELIGIBILITY_DOMAIN_ADULT_AGE_VERIFICATION_REQUIRED_SCREEN_TIME"
+ "OS_ELIGIBILITY_DOMAIN_AGE_VERIFICATION_REQUIRED_SCREEN_TIME"
+ "OS_ELIGIBILITY_DOMAIN_CHILD_AND_TEEN_RESTRICTION_REQUIRED_MINI_BUDDY"
+ "OS_ELIGIBILITY_DOMAIN_CHILD_TEEN_AGE_VERIFICATION_REQUIRED_SCREEN_TIME"
+ "OS_ELIGIBILITY_DOMAIN_DECLARED_AGE_RANGE_REQUIRES_AGE_RANGE_FETCH"
+ "OS_ELIGIBILITY_DOMAIN_DECLARED_AGE_RANGE_SIGNIFICANT_APP_CHANGE_ADULT"
+ "OS_ELIGIBILITY_DOMAIN_DECLARED_AGE_RANGE_SIGNIFICANT_APP_CHANGE_CHILD_TEEN"
+ "OS_ELIGIBILITY_DOMAIN_REVOKE_APP_ACCESS_REQUIRED"
+ "OS_ELIGIBILITY_DOMAIN_SIRI_MODE"
+ "OS_ELIGIBILITY_DOMAIN_SIRI_MODE_NEEDS_CONSENT"
+ "OS_ELIGIBILITY_DOMAIN_UNVERIFIED_ADULT_RESTRICTION_REQUIRED_MINI_BUDDY"
+ "com.apple.os-eligibility-domain.change.adult-age-verification-required-screen-time"
+ "com.apple.os-eligibility-domain.change.age-verification-required-screen-time"
+ "com.apple.os-eligibility-domain.change.child-and-teen-restriction-required-mini-buddy"
+ "com.apple.os-eligibility-domain.change.child-teen-age-verification-required-screen-time"
+ "com.apple.os-eligibility-domain.change.declared-age-range-requires-age-range-fetch"
+ "com.apple.os-eligibility-domain.change.declared-age-range-significant-app-change-adult"
+ "com.apple.os-eligibility-domain.change.declared-age-range-significant-app-change-child-teen"
+ "com.apple.os-eligibility-domain.change.revoke-app-access-required"
+ "com.apple.os-eligibility-domain.change.siri-mode"
+ "com.apple.os-eligibility-domain.change.siri-mode-needs-consent"
+ "com.apple.os-eligibility-domain.change.unverified-adult-restriction-required-mini-buddy"
- "%s: Unsupported domain %llu; falling back to private plist"
- "OS_ELIGIBILITY_INPUT_DEVICE_AND_SIRI_LANGUAGE_MATCH"
- "OS_ELIGIBILITY_INPUT_SIRI_LANGUAGE"
- "eligibility_domain_to_file"

```
