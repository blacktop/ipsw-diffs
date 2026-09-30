## MediaServices

> `/System/Library/PrivateFrameworks/MediaServices.framework/Versions/A/MediaServices`

```diff

-4026.100.70.0.0
-  __TEXT.__text: 0x5c72c
-  __TEXT.__objc_methlist: 0x5784
+4026.140.1.0.0
+  __TEXT.__text: 0x5cd90
+  __TEXT.__objc_methlist: 0x578c
   __TEXT.__const: 0x3ac
   __TEXT.__dlopen_cstrs: 0x70
   __TEXT.__gcc_except_tab: 0x1008
-  __TEXT.__cstring: 0x5dad
-  __TEXT.__oslogstring: 0x2c0a
+  __TEXT.__cstring: 0x5dc7
+  __TEXT.__oslogstring: 0x2d8f
   __TEXT.__ustring: 0x18
-  __TEXT.__unwind_info: 0x16f0
+  __TEXT.__unwind_info: 0x1700
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0x2fb0
+  __DATA_CONST.__objc_selrefs: 0x2fb8
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x258
   __DATA_CONST.__objc_arraydata: 0x138
   __DATA_CONST.__got: 0x660
   __AUTH_CONST.__const: 0x1950
-  __AUTH_CONST.__cfstring: 0x5800
+  __AUTH_CONST.__cfstring: 0x5820
   __AUTH_CONST.__objc_const: 0x9c68
   __AUTH_CONST.__weak_auth_got: 0x18
   __AUTH_CONST.__objc_arrayobj: 0x48

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 2138
-  Symbols:   5413
-  CStrings:  1086
+  Functions: 2142
+  Symbols:   5417
+  CStrings:  1092
 
Symbols:
+ -[MSVSonicAssertionObserver assertionWillInvalidate:]
+ GCC_except_table2073
+ GCC_except_table2088
+ GCC_except_table2093
+ GCC_except_table2094
+ __MSVSonicPerformRenewalLocked
+ __MSVSonicScheduleRenewalLocked
+ ____MSVSonicScheduleRenewalLocked_block_invoke
+ _objc_msgSend$removeObserver:
- GCC_except_table2069
- GCC_except_table2084
- GCC_except_table2085
- GCC_except_table2090
- _objc_msgSend$hasBoolEntitlement:
CStrings:
+ "MSVSonicAssertion-renewal"
+ "[MSVSonicAssertion] Failed to renew RBSAssertion %p error=%{public}@"
+ "[MSVSonicAssertion] Invalidating RBSAssertion %p"
+ "[MSVSonicAssertion] Invalidating RBSAssertion %p [proactive age-out, unused]"
+ "[MSVSonicAssertion] Proactive renewal timer fired [still in use] assertion=%p"
+ "[MSVSonicAssertion] RBSAssertion %p received expiration warning from RunningBoard"
+ "[MSVSonicAssertion] Renewed RBSAssertion %p -> %p [proactive renewal before expiration]"
+ "[MSVSonicAssertion] Scheduling RBSAssertion %p Invalidation"
- "[MSVSonicAssertion] Invalidating RBSAssertion %p] Timeout"
- "[MSVSonicAssertion] Releasing os_transaction %p Timeout"
```
