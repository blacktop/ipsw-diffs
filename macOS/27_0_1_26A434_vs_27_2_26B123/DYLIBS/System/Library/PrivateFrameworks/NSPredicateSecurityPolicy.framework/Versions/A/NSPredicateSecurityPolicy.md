## NSPredicateSecurityPolicy

> `/System/Library/PrivateFrameworks/NSPredicateSecurityPolicy.framework/Versions/A/NSPredicateSecurityPolicy`

```diff

-10.0.1.0.0
-  __TEXT.__text: 0xa24
-  __TEXT.__const: 0x8cb0
-  __TEXT.__cstring: 0x13c
-  __TEXT.__unwind_info: 0x70
+10.40.3.0.0
+  __TEXT.__text: 0xa84
+  __TEXT.__const: 0x91d0
+  __TEXT.__cstring: 0x198
+  __TEXT.__unwind_info: 0x78
   __TEXT.__auth_stubs: 0x0
-  __DATA_CONST.__const: 0x9e40
+  __DATA_CONST.__const: 0xa0e0
   __DATA_CONST.__got: 0x0
   __AUTH_CONST.__auth_got: 0x0
   __DATA.__bss: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 9
-  Symbols:   316
-  CStrings:  14
+  Functions: 10
+  Symbols:   328
+  CStrings:  18
 
Symbols:
+ RTGetNSPredicateSecurityPolicyData.selector_list_281
+ RTGetNSPredicateSecurityPolicyData.selector_list_282
+ RTGetNSPredicateSecurityPolicyData.selector_list_283
+ RTGetNSPredicateSecurityPolicyData.selector_list_284
+ RTGetNSPredicateSecurityPolicyData.selector_list_285
+ RTGetNSPredicateSecurityPolicyData.selector_list_286
+ RTGetNSPredicateSecurityPolicyData.selector_list_287
+ RTShouldApplyNSPredicateSecurityPolicy.entitlementState
+ _RTPredicateSecurityPolicyRaiseException
+ __xpc_type_bool
+ _objc_exception_throw
+ _objc_msgSend
+ _xpc_bool_get_value
+ _xpc_copy_entitlement_for_self
+ _xpc_get_type
+ _xpc_release
- RTShouldApplyNSPredicateSecurityPolicy.policyState
- _amfi_interface_cdhash_in_trustcache
- _csops
- _getpid
Functions:
~ _RTShouldApplyNSPredicateSecurityPolicy : 284 -> 252
+ _RTPredicateSecurityPolicyRaiseException
CStrings:
+ "NSException"
+ "alloc"
+ "com.apple.security.nspredicate-restrictions"
+ "initWithName:reason:userInfo:"
```
