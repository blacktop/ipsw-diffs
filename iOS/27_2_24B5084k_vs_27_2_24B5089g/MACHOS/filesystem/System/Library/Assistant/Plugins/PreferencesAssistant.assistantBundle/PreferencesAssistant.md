## PreferencesAssistant

> `/System/Library/Assistant/Plugins/PreferencesAssistant.assistantBundle/PreferencesAssistant`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-2027.1.4.0.0
-  __TEXT.__text: 0x8430
-  __TEXT.__auth_stubs: 0x3c0
-  __TEXT.__objc_stubs: 0xb20
-  __TEXT.__objc_methlist: 0x8fc
-  __TEXT.__const: 0x98
-  __TEXT.__oslogstring: 0xce7
-  __TEXT.__cstring: 0x606
+2027.1.6.0.0
+  __TEXT.__text: 0x85c8
+  __TEXT.__auth_stubs: 0x400
+  __TEXT.__objc_stubs: 0xb80
+  __TEXT.__objc_methlist: 0x924
+  __TEXT.__const: 0xa0
+  __TEXT.__oslogstring: 0xd0b
+  __TEXT.__cstring: 0x68e
   __TEXT.__objc_classname: 0x6ba
-  __TEXT.__objc_methname: 0x916
-  __TEXT.__objc_methtype: 0x221
+  __TEXT.__objc_methname: 0x976
+  __TEXT.__objc_methtype: 0x22f
   __TEXT.__gcc_except_tab: 0x30
-  __TEXT.__unwind_info: 0x258
+  __TEXT.__unwind_info: 0x260
   __DATA_CONST.__const: 0x120
-  __DATA_CONST.__cfstring: 0x640
+  __DATA_CONST.__cfstring: 0x680
   __DATA_CONST.__objc_classlist: 0x230
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x18
   __DATA_CONST.__objc_intobj: 0x30
-  __DATA_CONST.__auth_got: 0x1f0
-  __DATA_CONST.__got: 0x330
+  __DATA_CONST.__auth_got: 0x210
+  __DATA_CONST.__got: 0x338
   __DATA.__objc_const: 0x13390
-  __DATA.__objc_selrefs: 0x3b0
+  __DATA.__objc_selrefs: 0x3c8
   __DATA.__objc_ivar: 0x2c
   __DATA.__objc_data: 0x15e0
   __DATA.__data: 0xd8

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 112
-  Symbols:   312
-  CStrings:  368
+  Functions: 115
+  Symbols:   317
+  CStrings:  377
 
Symbols:
+ _TCCAccessResetForBundleIdWithOptions
+ ___NSDictionary0__struct
+ __os_feature_enabled_impl
+ _notify_post
+ _objc_retain_x28
CStrings:
+ "########## PASetSiriAuthorizationForApp: %@ (%@ / prev: %@ / value: %@ / excluded: %@ / resetExclusion: %@ / %@)"
+ "AppExclusions"
+ "B32@0:8@16@24"
+ "IntelligenceFlow"
+ "TCC App Access exclusion reset failed"
+ "_clearSiriExclusionForAppID:"
+ "_isAppAccessFeatureEnabled"
+ "_isExcludedFromSiri:"
+ "_siriAccessForBundle:tccAccessInfo:"
+ "com.apple.assistant.siri_settings_did_change"
+ "kTCCServiceSiriAccess"
- "########## PASetSiriAuthorizationForApp: %@ (%@ / prev: %@ / value: %@ / %@)"
- "_accessForAppID:"
```
