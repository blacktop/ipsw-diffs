## passd

> `/System/Library/PrivateFrameworks/PassKitCore.framework/passd`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__auth_ptr`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_doubleobj`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`
- `__DATA.__bss`
- `__DATA.__common`

```diff

-1642.7.2.0.0
-  __TEXT.__text: 0x5b5b50
+1642.7.4.0.0
+  __TEXT.__text: 0x5b7480
   __TEXT.__auth_stubs: 0x59d0
-  __TEXT.__objc_stubs: 0x6efc0
-  __TEXT.__objc_methlist: 0x3422c
+  __TEXT.__objc_stubs: 0x6f0a0
+  __TEXT.__objc_methlist: 0x3424c
   __TEXT.__const: 0x3b48
-  __TEXT.__cstring: 0x608a4
+  __TEXT.__cstring: 0x60904
   __TEXT.__objc_classname: 0x7898
   __TEXT.__objc_methtype: 0x13032
-  __TEXT.__gcc_except_tab: 0x8890
-  __TEXT.__objc_methname: 0x9d13c
-  __TEXT.__oslogstring: 0x4ecdb
+  __TEXT.__gcc_except_tab: 0x8908
+  __TEXT.__objc_methname: 0x9d21c
+  __TEXT.__oslogstring: 0x4eeab
   __TEXT.__ustring: 0x10
   __TEXT.__swift5_typeref: 0x1f30
   __TEXT.__constg_swiftt: 0x151c

   __TEXT.__swift_as_entry: 0x28
   __TEXT.__swift5_mpenum: 0x30
   __TEXT.__swift_as_ret: 0x34
-  __TEXT.__unwind_info: 0x128a0
+  __TEXT.__unwind_info: 0x128d8
   __TEXT.__eh_frame: 0x1098
   __DATA_CONST.__auth_got: 0x2cf8
-  __DATA_CONST.__got: 0x32a8
+  __DATA_CONST.__got: 0x32b0
   __DATA_CONST.__auth_ptr: 0x668
-  __DATA_CONST.__const: 0x2d408
+  __DATA_CONST.__const: 0x2d468
   __DATA_CONST.__cfstring: 0x31b40
   __DATA_CONST.__objc_classlist: 0x18f0
   __DATA_CONST.__objc_catlist: 0x40

   __DATA_CONST.__objc_arrayobj: 0x558
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA.__objc_const: 0x3fae8
-  __DATA.__objc_selrefs: 0x1eb08
+  __DATA.__objc_selrefs: 0x1eb20
   __DATA.__objc_ivar: 0x2754
   __DATA.__objc_data: 0x10768
   __DATA.__data: 0x5b60

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 26602
-  Symbols:   3243
-  CStrings:  33303
+  Functions: 26618
+  Symbols:   3244
+  CStrings:  33316
 
Symbols:
+ _OBJC_CLASS_$_PKAccountWebServiceCreditRecoveryPaymentPlansRequest
CStrings:
+ "Completed updating payment plans proactively for account %@. Error: %@"
+ "Could not determine recovery payment plan enrollment (error: %@); suppressing past due notification: %@"
+ "Could not fetch payment plans with error %@"
+ "Fetching payment plans for account with identifier %@"
+ "Inserted or updated payment plans from fetch: %@"
+ "TB,N,V_useGenericMessaging"
+ "Updating past due notification (%@) Mini-Miranda generic messaging flag (from:%d to:%d)"
+ "creditRecoveryPaymentPlansWithRequest:completion:"
+ "paymentPlans"
+ "recoveryPaymentPlansSupported false for account %@"
+ "setUseGenericMessaging:"
+ "updatePastDueNotificationWithAccount:userNotification:"
+ "v20@?0B8@\"PKAccount\"12"
+ "v24@?0@\"PKAccountWebServiceCreditRecoveryPaymentPlansResponse\"8@\"NSError\"16"
- "second"
```
