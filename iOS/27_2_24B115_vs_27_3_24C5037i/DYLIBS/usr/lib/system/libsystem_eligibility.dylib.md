## libsystem_eligibility.dylib

> `/usr/lib/system/libsystem_eligibility.dylib`

```diff

-446.42.1.0.0
-  __TEXT.__text: 0x42ac
-  __TEXT.__const: 0x760
-  __TEXT.__cstring: 0x5821
+446.60.26.502.1
+  __TEXT.__text: 0x43a8
+  __TEXT.__const: 0x778
+  __TEXT.__cstring: 0x5956
   __TEXT.__oslogstring: 0x39b
   __TEXT.__unwind_info: 0xf8
   __TEXT.__auth_stubs: 0x0
-  __DATA_CONST.__const: 0xf18
+  __DATA_CONST.__const: 0xf48
   __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x40
   __AUTH_CONST.__auth_got: 0x0

   - /usr/lib/system/libxpc.dylib
   Functions: 33
   Symbols:   83
-  CStrings:  553
+  CStrings:  560
 
Functions:
~ sub_2c6ef6858 -> sub_2cb0f8858 : 880 -> 888
~ _os_eligibility_get_domain_answer : 2564 -> 2752
~ _os_eligibility_domain_for_name : 6224 -> 6280
CStrings:
+ "OS_ELIGIBILITY_DOMAIN_FIRST_PARTY_APP_CONSENT_REQUIRED"
+ "OS_ELIGIBILITY_DOMAIN_TEEN_ATTACHED_TO_FAMILY_OFFER_TO_JOIN"
+ "OS_ELIGIBILITY_INPUT_DEVICE_TYPE"
+ "US-AL"
+ "US-CA"
+ "com.apple.os-eligibility-domain.change.first-party-app-consent-required"
+ "com.apple.os-eligibility-domain.change.teen-attached-to-family-offer-to-join"
```
