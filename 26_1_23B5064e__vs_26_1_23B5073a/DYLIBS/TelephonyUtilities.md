## TelephonyUtilities

> `/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`

```diff

-1576.200.75.0.0
-  __TEXT.__text: 0x16e57c
+1576.200.81.2.2
+  __TEXT.__text: 0x16ec18
   __TEXT.__auth_stubs: 0x2390
-  __TEXT.__objc_methlist: 0x1a2d0
-  __TEXT.__cstring: 0x13568
-  __TEXT.__const: 0x1044
-  __TEXT.__oslogstring: 0x12592
+  __TEXT.__objc_methlist: 0x1a2f0
+  __TEXT.__cstring: 0x13598
+  __TEXT.__const: 0x1218
+  __TEXT.__oslogstring: 0x125c2
   __TEXT.__gcc_except_tab: 0x1974
   __TEXT.__ustring: 0xde
   __TEXT.__dlopen_cstrs: 0x8df

   __TEXT.__unwind_info: 0x5df0
   __TEXT.__eh_frame: 0x1378
   __TEXT.__objc_classname: 0x274f
-  __TEXT.__objc_methname: 0x3c5b5
+  __TEXT.__objc_methname: 0x3c5f8
   __TEXT.__objc_methtype: 0x7f83
-  __TEXT.__objc_stubs: 0x20f20
+  __TEXT.__objc_stubs: 0x20f40
   __DATA_CONST.__got: 0xe60
   __DATA_CONST.__const: 0x3678
   __DATA_CONST.__objc_classlist: 0x830
   __DATA_CONST.__objc_catlist: 0xb8
   __DATA_CONST.__objc_protolist: 0x410
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xafc0
+  __DATA_CONST.__objc_selrefs: 0xafd0
   __DATA_CONST.__objc_protorefs: 0x108
   __DATA_CONST.__objc_superrefs: 0x6b0
   __DATA_CONST.__objc_arraydata: 0x6f8
   __AUTH_CONST.__auth_got: 0x11d8
   __AUTH_CONST.__const: 0x31a8
-  __AUTH_CONST.__cfstring: 0x11c80
-  __AUTH_CONST.__objc_const: 0x28368
+  __AUTH_CONST.__cfstring: 0x11ca0
+  __AUTH_CONST.__objc_const: 0x28390
   __AUTH_CONST.__objc_intobj: 0x540
   __AUTH_CONST.__objc_arrayobj: 0x228
   __AUTH_CONST.__objc_doubleobj: 0x40
   __AUTH.__objc_data: 0x2648
   __AUTH.__data: 0x5e8
   __DATA.__objc_ivar: 0x17fc
-  __DATA.__data: 0x3370
+  __DATA.__data: 0x3368
   __DATA.__bss: 0x18b0
   __DATA.__common: 0x28
   __DATA_DIRTY.__objc_data: 0x2c60

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 1EF0E029-17FD-3679-BDE0-855BAA25BAFE
-  Functions: 10062
-  Symbols:   30072
-  CStrings:  16498
+  UUID: 131AB4A9-72A4-3808-A8BA-081E0867B4F5
+  Functions: 10064
+  Symbols:   30077
+  CStrings:  16503
 
Symbols:
+ -[TUCallHistoryController markUnreadRecentCallsAsReadWithPredicate:]
+ -[TUFeatureFlags imageBadgeRendererEnabled]
+ -[TUFeatureFlags phoneAppCoupledRelayEnabled]
+ GCC_except_table41
+ GCC_except_table59
+ GCC_except_table65
+ __OBJC_$_CLASS_PROP_LIST_TUFeatureFlags.663
+ __OBJC_$_PROP_LIST_TUFeatureFlags.667
+ ___swift_instantiateConcreteTypeFromMangledNameAbstractV2
+ ___swift_instantiateConcreteTypeFromMangledNameV2
+ _objc_msgSend$markUnreadRecentCallsAsReadWithPredicate:
+ _objc_msgSend$phoneAppCoupledRelayEnabled
- -[TUFeatureFlags contactsIntroductionsEnabled]
- GCC_except_table47
- GCC_except_table49
- GCC_except_table61
- GCC_except_table69
- __OBJC_$_CLASS_PROP_LIST_TUFeatureFlags.660
- __OBJC_$_PROP_LIST_TUFeatureFlags.664
- ___swift_instantiateConcreteTypeFromMangledName
- ___swift_instantiateConcreteTypeFromMangledNameAbstract
- _objc_msgSend$callExperiencePhoneAppEnabled
CStrings:
+ "+N9mZUAHooNvMiQnjeTJ8g"
+ "Default is not set but relay/thumper is enabled, AND phoneAppCoupledRelay is enabled, so returning TUDefaultAppRelayTelephonySettingNotApplicable"
+ "Default is not set but relay/thumper is enabled, and phone app is decoupled from relay so returning TUDefaultAppRelayTelephonySettingCallsFromIPhone"
+ "ImageBadgeRenderer"
+ "PhoneAppCoupledRelay"
+ "imageBadgeRendererEnabled"
+ "markUnreadRecentCallsAsReadWithPredicate:"
+ "phoneAppCoupledRelayEnabled"
- "Default is not set but relay/thumper is enabled, AND we have PhoneApp, so returning TUDefaultAppRelayTelephonySettingNotApplicable"
- "Default is not set but relay/thumper is enabled, also NO PhoneApp, so returning TUDefaultAppRelayTelephonySettingCallsFromIPhone"
- "contactsIntroductionsEnabled"
- "introductions"

```
