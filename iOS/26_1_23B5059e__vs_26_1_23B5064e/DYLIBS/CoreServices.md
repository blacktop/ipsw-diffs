## CoreServices

> `/System/Library/Frameworks/CoreServices.framework/CoreServices`

```diff

-1443.3.0.0.0
-  __TEXT.__text: 0x1aa050
-  __TEXT.__auth_stubs: 0x3070
+1444.1.2.0.0
+  __TEXT.__text: 0x1aa274
+  __TEXT.__auth_stubs: 0x3080
   __TEXT.__delay_stubs: 0x2c
   __TEXT.__delay_helper: 0x16c
   __TEXT.__objc_methlist: 0xccb4
   __TEXT.__const: 0x910
-  __TEXT.__cstring: 0x24765
-  __TEXT.__oslogstring: 0x13580
-  __TEXT.__gcc_except_tab: 0x26e70
+  __TEXT.__cstring: 0x2479f
+  __TEXT.__oslogstring: 0x135c7
+  __TEXT.__gcc_except_tab: 0x26eac
   __TEXT.__ustring: 0x23c
-  __TEXT.__unwind_info: 0xb020
+  __TEXT.__unwind_info: 0xb028
   __TEXT.__eh_frame: 0x60
   __TEXT.__objc_classname: 0x1ea9
   __TEXT.__objc_methname: 0x1d02e
   __TEXT.__objc_methtype: 0xa6a4
   __TEXT.__objc_stubs: 0x10300
   __DATA_CONST.__got: 0xa90
-  __DATA_CONST.__const: 0x6c30
+  __DATA_CONST.__const: 0x6c58
   __DATA_CONST.__objc_classlist: 0x6b0
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x138

   __DATA_CONST.__objc_protorefs: 0x90
   __DATA_CONST.__objc_superrefs: 0x568
   __DATA_CONST.__objc_arraydata: 0x180
-  __AUTH_CONST.__auth_got: 0x1858
+  __AUTH_CONST.__auth_got: 0x1860
   __AUTH_CONST.__const: 0x35f0
-  __AUTH_CONST.__cfstring: 0x169c0
+  __AUTH_CONST.__cfstring: 0x169e0
   __AUTH_CONST.__objc_const: 0x12f08
   __AUTH_CONST.__objc_intobj: 0x810
   __AUTH_CONST.__objc_dictobj: 0x50

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 3B5F4141-1213-3805-B5E0-263B16A2BF34
-  Functions: 8623
-  Symbols:   28023
-  CStrings:  13610
+  UUID: 937EA931-547F-31EC-9C06-848B87B6F557
+  Functions: 8624
+  Symbols:   28028
+  CStrings:  13615
 
Symbols:
+ GCC_except_table174
+ _MGGetSInt32Answer
+ ____ZN14LaunchServices17BindingEvaluationL31weaklyBoundAppHasRequiredClaimsERKNS0_5StateERK9LSBinding_block_invoke
+ ___block_descriptor_56_ea8_32r_e14_v24?0I8I12*16lr32l8
+ ___block_literal_global.43
+ ___block_literal_global.52
- GCC_except_table192
- ___block_literal_global.46
Functions:
~ __ZN14LaunchServices17BindingEvaluationL18addUserPreferencesERNS0_5StateE : 1132 -> 1388
+ ____ZN14LaunchServices17BindingEvaluationL31weaklyBoundAppHasRequiredClaimsERKNS0_5StateERK9LSBinding_block_invoke
~ __ZL25BundleIsPhoneAppCandidateP11_LSDatabasejPK12LSBundleDataP12NSDictionaryb : 312 -> 436
~ __ZN13LSHandlerPref4LoadEP11_LSDatabasePK9__CFArray : 2424 -> 2416
CStrings:
+ "DeviceClassNumber"
+ "MobilePhone is not a candidate for default calling app on this device."
+ "PhoneAppCoupledRelay"
+ "TelephonyUtilities"
+ "static NSInteger LaunchServices::PrefsStorage::_GetIndexOfValueInPrefsArrayWithPredicate(NSArray *__strong, const Pred &) [Pred = (lambda at /Library/Caches/com.apple.xbs/Sources/CoreServices/LaunchServices.subprj/Source/LaunchServices/Info/LSPrefs.mm:1428:63)]"
- "static NSInteger LaunchServices::PrefsStorage::_GetIndexOfValueInPrefsArrayWithPredicate(NSArray *__strong, const Pred &) [Pred = (lambda at /Library/Caches/com.apple.xbs/Sources/CoreServices/LaunchServices.subprj/Source/LaunchServices/Info/LSPrefs.mm:1416:63)]"

```
