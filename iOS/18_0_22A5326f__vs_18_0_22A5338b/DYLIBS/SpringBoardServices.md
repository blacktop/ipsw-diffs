## SpringBoardServices

> `/System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices`

```diff

-4493.1.101.0.0
-  __TEXT.__text: 0x6731c
-  __TEXT.__auth_stubs: 0xf50
-  __TEXT.__objc_methlist: 0x6078
-  __TEXT.__cstring: 0xc0ac
+4494.104.0.0.0
+  __TEXT.__text: 0x67cdc
+  __TEXT.__auth_stubs: 0xf60
+  __TEXT.__objc_methlist: 0x61d8
+  __TEXT.__cstring: 0xc0f4
   __TEXT.__const: 0x588
-  __TEXT.__oslogstring: 0x3733
-  __TEXT.__gcc_except_tab: 0x954
+  __TEXT.__oslogstring: 0x378b
+  __TEXT.__gcc_except_tab: 0x95c
   __TEXT.__dlopen_cstrs: 0x17a
   __TEXT.__ustring: 0x58
-  __TEXT.__unwind_info: 0x2130
-  __TEXT.__objc_classname: 0x241e
-  __TEXT.__objc_methname: 0xdc49
-  __TEXT.__objc_methtype: 0x25cd
-  __TEXT.__objc_stubs: 0x7980
-  __DATA_CONST.__got: 0x7b8
-  __DATA_CONST.__const: 0x30c8
-  __DATA_CONST.__objc_classlist: 0x5b8
+  __TEXT.__unwind_info: 0x2170
+  __TEXT.__objc_classname: 0x243e
+  __TEXT.__objc_methname: 0xde21
+  __TEXT.__objc_methtype: 0x2645
+  __TEXT.__objc_stubs: 0x7a40
+  __DATA_CONST.__got: 0x7c8
+  __DATA_CONST.__const: 0x3108
+  __DATA_CONST.__objc_classlist: 0x5c0
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x248
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2aa8
+  __DATA_CONST.__objc_selrefs: 0x2b08
   __DATA_CONST.__objc_protorefs: 0x188
-  __DATA_CONST.__objc_superrefs: 0x390
-  __AUTH_CONST.__auth_got: 0x7b8
-  __AUTH_CONST.__const: 0x25f0
-  __AUTH_CONST.__cfstring: 0x9240
-  __AUTH_CONST.__objc_const: 0x20188
+  __DATA_CONST.__objc_superrefs: 0x398
+  __AUTH_CONST.__auth_got: 0x7c0
+  __AUTH_CONST.__const: 0x2650
+  __AUTH_CONST.__cfstring: 0x92c0
+  __AUTH_CONST.__objc_const: 0x207d8
   __AUTH_CONST.__objc_intobj: 0x90
-  __AUTH.__objc_data: 0x24e0
-  __DATA.__objc_ivar: 0x678
+  __AUTH.__objc_data: 0x2530
+  __DATA.__objc_ivar: 0x680
   __DATA.__data: 0x1c60
-  __DATA.__bss: 0x7d0
+  __DATA.__bss: 0x800
   __DATA_DIRTY.__objc_data: 0x1450
   __DATA_DIRTY.__data: 0x40
   __DATA_DIRTY.__bss: 0x248

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3348
-  Symbols:   4643
-  CStrings:  4429
+  Functions: 3379
+  Symbols:   4677
+  CStrings:  4452
 
Symbols:
+ _OBJC_CLASS_$_SBSHomeScreenIconStyleConfiguration
+ _OBJC_CLASS_$_SBSHomeScreenServiceIconStyleObservationAssertion
+ _OBJC_METACLASS_$_SBSHomeScreenIconStyleConfiguration
+ _OBJC_METACLASS_$_SBSHomeScreenServiceIconStyleObservationAssertion
+ ___stderrp
+ _fprintf
- _OBJC_CLASS_$_SBSHomeScreenServiceIconTintColorObservationAssertion
- _OBJC_METACLASS_$_SBSHomeScreenServiceIconTintColorObservationAssertion
CStrings:
+ "@\"<SBSHomeScreenServiceIconStyleObserver>\""
+ "@\"SBSHomeScreenIconStyleConfiguration\""
+ "@\"SBSHomeScreenIconStyleConfiguration\"16@0:8"
+ "Lost an observer for icon style without invalidating the assertion"
+ "SBSHomeScreenIconStyleConfiguration"
+ "SBSHomeScreenService: failed addHomeScreenIconStyleObserver: request (no target)."
+ "SBSHomeScreenService: failed homeScreenIconStyleConfiguration request (no target)."
+ "SBSHomeScreenService: failed setHomeScreenIconStyleConfiguration: request (no target)."
+ "SBSHomeScreenServiceIconStyleObservationAssertion"
+ "T@\"<SBSHomeScreenServiceIconStyleObserver>\",R,W,N,V_observer"
+ "T@\"BSColor\",R,C,N,V_tintColor"
+ "T@\"SBSHomeScreenIconStyleConfiguration\",C,N"
+ "T@\"SBSHomeScreenIconStyleConfiguration\",C,N,V_cachedIconStyleConfiguration"
+ "T@\"SBSHomeScreenIconStyleConfiguration\",R"
+ "TB,N,GisCachedIconStyleConfigurationValid,V_cachedIconStyleConfigurationValid"
+ "Tq,R,N,V_configurationType"
+ "Unable to set icon style to %!s(MISSING)\n"
+ "Vv24@0:8@\"SBSHomeScreenIconStyleConfiguration\"16"
+ "[ContentAssertion] Action is nil after initialization, dropping content entirely. slot: %!{(MISSING)public}@ identifier: %!{(MISSING)public}@"
+ "_cachedIconStyleConfiguration"
+ "_cachedIconStyleConfigurationValid"
+ "_configurationType"
+ "_iconStyleObservers"
+ "addHomeScreenIconStyleObserver:"
+ "auto"
+ "automaticStyleConfiguration"
+ "cachedIconStyleConfiguration"
+ "cachedIconStyleConfigurationValid"
+ "classForCoder"
+ "configurationType"
+ "configurationType"
+ "darkStyleConfiguration"
+ "defaultStyleConfiguration"
+ "homeScreenIconStyleConfiguration"
+ "homeScreenIconStyleConfigurationDidChange:"
+ "homeScreenService:homeScreenIconStyleConfigurationDidChange:"
+ "initWithConfigurationType:"
+ "initWithConfigurationType:tintColor:"
+ "isCachedIconStyleConfigurationValid"
+ "lightStyleConfiguration"
+ "removeIconStyleObservationAssertion:"
+ "setCachedIconStyleConfiguration:"
+ "setCachedIconStyleConfigurationValid:"
+ "setHomeScreenIconStyleConfiguration:"
+ "tinted"
+ "tintedStyleConfigurationWithTintColor:"
+ "v24@0:8@\"SBSHomeScreenIconStyleConfiguration\"16"
- "@\"<SBSHomeScreenServiceIconTintColorObserver>\""
- "@\"BSColor\"16@0:8"
- "Lost an observer for icon tint color without invalidating the assertion"
- "SBSHomeScreenService: failed addIconTintColorObserver: request (no target)."
- "SBSHomeScreenService: failed iconTintColor request (no target)."
- "SBSHomeScreenService: failed iconUserInterfaceStyle request (no target)."
- "SBSHomeScreenService: failed setIconTintColor: request (no target)."
- "SBSHomeScreenServiceIconTintColorObservationAssertion"
- "T@\"<SBSHomeScreenServiceIconTintColorObserver>\",R,W,N,V_observer"
- "T@\"NSData\",C,N,V_cachedIconStyleConfigurationData"
- "T@\"NSString\",N"
- "TB,N,GisCachedIconStyleConfigurationDataValid,V_cachedIconStyleConfigurationDataValid"
- "Vv24@0:8@\"NSData\"16"
- "_cachedIconStyleConfigurationData"
- "_cachedIconStyleConfigurationDataValid"
- "_iconTintColorObservers"
- "cachedIconStyleConfigurationData"
- "cachedIconStyleConfigurationDataValid"
- "homeScreenService:iconImageStyleConfigurationDidChange:"
- "iconImageStyleConfigurationDidChange:"
- "isCachedIconStyleConfigurationDataValid"
- "removeIconTintColorObservationAssertion:"
- "setCachedIconStyleConfigurationData:"
- "setCachedIconStyleConfigurationDataValid:"
- "v24@0:8@\"BSColor\"16"

```
