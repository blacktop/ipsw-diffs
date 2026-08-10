## MediaServices

> `/System/Library/PrivateFrameworks/MediaServices.framework/MediaServices`

### Sections with Same Size but Changed Content

- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__weak_got`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__weak_auth_got`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-4026.100.70.0.0
-  __TEXT.__text: 0x59e3c
-  __TEXT.__objc_methlist: 0x5784
+4026.110.1.0.0
+  __TEXT.__text: 0x5a444
+  __TEXT.__objc_methlist: 0x578c
   __TEXT.__const: 0x3bc
   __TEXT.__dlopen_cstrs: 0xd4
   __TEXT.__gcc_except_tab: 0x10a4
-  __TEXT.__cstring: 0x6050
-  __TEXT.__oslogstring: 0x2c42
+  __TEXT.__cstring: 0x606a
+  __TEXT.__oslogstring: 0x2dc7
   __TEXT.__ustring: 0x18
-  __TEXT.__unwind_info: 0x16f8
+  __TEXT.__unwind_info: 0x1710
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0x2fb8
+  __DATA_CONST.__objc_selrefs: 0x2fc0
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x258
   __DATA_CONST.__objc_arraydata: 0x138
   __DATA_CONST.__got: 0x690
   __AUTH_CONST.__const: 0x720
-  __AUTH_CONST.__cfstring: 0x5a40
+  __AUTH_CONST.__cfstring: 0x5a60
   __AUTH_CONST.__objc_const: 0x9cc8
   __AUTH_CONST.__weak_auth_got: 0x18
   __AUTH_CONST.__objc_arrayobj: 0x48

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 2118
-  Symbols:   5455
-  CStrings:  1120
+  Functions: 2122
+  Symbols:   5459
+  CStrings:  1126
 
Symbols:
+ -[MSVSonicAssertionObserver assertionWillInvalidate:]
+ GCC_except_table2055
+ GCC_except_table2071
+ GCC_except_table2073
+ GCC_except_table2074
+ __MSVSonicPerformRenewalLocked
+ __MSVSonicScheduleRenewalLocked
+ ____MSVSonicScheduleRenewalLocked_block_invoke
+ _objc_msgSend$removeObserver:
- GCC_except_table2051
- GCC_except_table2066
- GCC_except_table2067
- GCC_except_table2069
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
