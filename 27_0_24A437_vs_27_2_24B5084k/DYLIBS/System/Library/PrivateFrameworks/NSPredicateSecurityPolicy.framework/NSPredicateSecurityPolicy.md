## NSPredicateSecurityPolicy

> `/System/Library/PrivateFrameworks/NSPredicateSecurityPolicy.framework/NSPredicateSecurityPolicy`

```diff

-10.0.1.0.0
-  __TEXT.__text: 0xa20
+10.40.2.0.0
+  __TEXT.__text: 0xa80
   __TEXT.__const: 0x8cb0
-  __TEXT.__cstring: 0x13c
+  __TEXT.__cstring: 0x198
   __TEXT.__unwind_info: 0x80
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x9e40

   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 9
-  Symbols:   317
-  CStrings:  14
+  Functions: 10
+  Symbols:   322
+  CStrings:  18
 
Symbols:
+ _RTPredicateSecurityPolicyRaiseException
+ _RTShouldApplyNSPredicateSecurityPolicy.entitlementState
+ __xpc_type_bool
+ _objc_exception_throw
+ _objc_msgSend
+ _xpc_bool_get_value
+ _xpc_copy_entitlement_for_self
+ _xpc_get_type
+ _xpc_release
- _RTShouldApplyNSPredicateSecurityPolicy.policyState
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
