## libsystem_eligibility.dylib

> `/usr/lib/system/libsystem_eligibility.dylib`

```diff

-181.120.32.0.0
-  __TEXT.__text: 0x3854
+263.0.0.502.2
+  __TEXT.__text: 0x3230
   __TEXT.__auth_stubs: 0x290
-  __TEXT.__const: 0x80
-  __TEXT.__cstring: 0x2d5b
-  __TEXT.__oslogstring: 0x326
+  __TEXT.__const: 0x4b0
+  __TEXT.__cstring: 0x2f9b
+  __TEXT.__oslogstring: 0x2eb
   __TEXT.__unwind_info: 0xb8
   __DATA_CONST.__got: 0x28
-  __DATA_CONST.__const: 0x470
+  __DATA_CONST.__const: 0x8b8
   __AUTH_CONST.__auth_got: 0x148
   __AUTH_CONST.__const: 0x40
   __DATA_DIRTY.__bss: 0x10

   - /usr/lib/system/libsystem_malloc.dylib
   - /usr/lib/system/libsystem_trace.dylib
   - /usr/lib/system/libxpc.dylib
-  UUID: 9F63A433-C5E8-30FE-ADD7-38C03A90DC17
+  UUID: 6005BA87-0A29-396B-BA9F-08C9A00419BB
   Functions: 24
-  Symbols:   85
-  CStrings:  329
+  Symbols:   86
+  CStrings:  342
 
Symbols:
+ ___block_descriptor_tmp.226
+ _os_eligibility_get_answer_for_mobilegestalt
- ___block_descriptor_tmp.215
CStrings:
+ "/private/var/db/eligibilityd/gestalt_data.plist"
+ "CA-AB"
+ "CA-NB"
+ "CA-NS"
+ "OS_ELIGIBILITY_DOMAIN_AI_LABELING"
+ "OS_ELIGIBILITY_DOMAIN_CORE_NFC_PAYMENT_TAG_READER"
+ "OS_ELIGIBILITY_DOMAIN_FORCED_SHUTTER_SOUND"
+ "OS_ELIGIBILITY_DOMAIN_FOUNDATION_MODELS"
+ "OS_ELIGIBILITY_DOMAIN_SMS_MMS_RCS_API"
+ "com.apple.os-eligibility-domain.change.ai-labeling"
+ "com.apple.os-eligibility-domain.change.core-nfc-payment-tag-reader"
+ "com.apple.os-eligibility-domain.change.forced-shutter-sound"
+ "com.apple.os-eligibility-domain.change.foundation-models"
+ "com.apple.os-eligibility-domain.change.sms-mms-rcs-api"
+ "copy_eligibility_domain_gestalt_data_path"
- "%s: Unsupported domain %llu; falling back to private plist"
- "eligibility_domain_to_file"

```
