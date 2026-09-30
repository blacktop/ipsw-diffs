## CoreServices

> `/System/Library/Frameworks/CoreServices.framework/CoreServices`

```diff

-1444.1.2.0.0
-  __TEXT.__text: 0x1aa274
+1444.1.3.100.0
+  __TEXT.__text: 0x1aa3a8
   __TEXT.__auth_stubs: 0x3080
   __TEXT.__delay_stubs: 0x2c
   __TEXT.__delay_helper: 0x16c
   __TEXT.__objc_methlist: 0xccb4
   __TEXT.__const: 0x910
   __TEXT.__cstring: 0x2479f
-  __TEXT.__oslogstring: 0x135c7
-  __TEXT.__gcc_except_tab: 0x26eac
+  __TEXT.__oslogstring: 0x13623
+  __TEXT.__gcc_except_tab: 0x26ebc
   __TEXT.__ustring: 0x23c
   __TEXT.__unwind_info: 0xb028
   __TEXT.__eh_frame: 0x60

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 937EA931-547F-31EC-9C06-848B87B6F557
+  UUID: C28F44CA-1E64-3EE8-9990-D036B2CED8C5
   Functions: 8624
-  Symbols:   28028
-  CStrings:  13615
+  Symbols:   28030
+  CStrings:  13616
 
Symbols:
+ -[LSAltIconManager changeIconWithAlertForApplicationIdentity:withIconsDictionary:toAlternateIconName:completion:].cold.6
+ -[LSApplicationRestrictionsManager isRatingAllowed:forBundleIdentifier:]
+ __LSApplicationRestrictionsManagerIsRatingAllowedForBundleIdentifier
- -[LSApplicationRestrictionsManager isRatingAllowed:]
- __LSApplicationRestrictionsManagerIsRatingAllowed
Functions:
~ __ZN14LaunchServices17BindingEvaluationL11isBindingOKERNS0_5StateERKNS0_15ExtendedBindingE : 1660 -> 1700
~ __LSPluginIsValid : 2080 -> 2084
~ -[LSAltIconManager changeIconWithAlertForApplicationIdentity:withIconsDictionary:toAlternateIconName:completion:] : 1096 -> 1296
~ __LSBundleCouldBeSelectedForActivityContinuation : 528 -> 532
~ -[LSApplicationRestrictionsManager isRatingAllowed:] -> -[LSApplicationRestrictionsManager isRatingAllowed:forBundleIdentifier:] : 144 -> 204
CStrings:
+ "#ChangeIconWithAlert existing icon name %@ equal to new name %@, doing nothing successfully"

```
