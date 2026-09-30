## amsaccountsd

> `/System/Library/PrivateFrameworks/AppleMediaServices.framework/Versions/Current/Resources/amsaccountsd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_classname`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift5_types2`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__common`

```diff

-10.0.50.0.0
-  __TEXT.__text: 0x27afd0
+10.0.52.0.0
+  __TEXT.__text: 0x27c83c
   __TEXT.__auth_stubs: 0x41b0
-  __TEXT.__objc_stubs: 0xa020
-  __TEXT.__objc_methlist: 0x5474
-  __TEXT.__const: 0x201e8
-  __TEXT.__objc_methname: 0xfb9b
-  __TEXT.__oslogstring: 0xd4e9
-  __TEXT.__cstring: 0xae8b
-  __TEXT.__objc_methtype: 0x45a5
+  __TEXT.__objc_stubs: 0xa120
+  __TEXT.__objc_methlist: 0x54a4
+  __TEXT.__const: 0x202d8
+  __TEXT.__cstring: 0xafcb
   __TEXT.__objc_classname: 0x1662
-  __TEXT.__gcc_except_tab: 0x738
+  __TEXT.__objc_methname: 0xfc3b
+  __TEXT.__objc_methtype: 0x45b5
+  __TEXT.__oslogstring: 0xd679
+  __TEXT.__gcc_except_tab: 0x734
   __TEXT.__dlopen_cstrs: 0x14a
-  __TEXT.__swift5_typeref: 0x78e6
-  __TEXT.__constg_swiftt: 0x61b8
-  __TEXT.__swift5_reflstr: 0x4f0c
-  __TEXT.__swift5_fieldmd: 0x74bc
+  __TEXT.__swift5_typeref: 0x7926
+  __TEXT.__constg_swiftt: 0x61e0
+  __TEXT.__swift5_fieldmd: 0x74f0
   __TEXT.__swift5_builtin: 0x168
-  __TEXT.__swift5_assocty: 0xa18
-  __TEXT.__swift5_proto: 0x1b20
-  __TEXT.__swift5_types: 0x7f0
   __TEXT.__swift5_capture: 0xf08
+  __TEXT.__swift5_reflstr: 0x4f1c
+  __TEXT.__swift5_assocty: 0xa18
+  __TEXT.__swift5_proto: 0x1b28
+  __TEXT.__swift5_types: 0x7f4
   __TEXT.__swift_as_entry: 0x354
   __TEXT.__swift_as_ret: 0x424
   __TEXT.__swift_as_cont: 0x8a0
   __TEXT.__swift5_protos: 0xc8
   __TEXT.__swift5_mpenum: 0x90
   __TEXT.__swift5_types2: 0x4
-  __TEXT.__unwind_info: 0xa0e0
-  __TEXT.__eh_frame: 0x12cb0
-  __DATA_CONST.__const: 0x183d8
-  __DATA_CONST.__cfstring: 0x41c0
+  __TEXT.__unwind_info: 0xa518
+  __TEXT.__eh_frame: 0x12c68
+  __DATA_CONST.__const: 0x18438
+  __DATA_CONST.__cfstring: 0x42a0
   __DATA_CONST.__objc_classlist: 0x398
   __DATA_CONST.__objc_catlist: 0x90
   __DATA_CONST.__objc_protolist: 0x220

   __DATA_CONST.__objc_intobj: 0xa8
   __DATA_CONST.__linkguard: 0x33
   __DATA_CONST.__auth_got: 0x20e8
-  __DATA_CONST.__got: 0x13b0
-  __DATA_CONST.__auth_ptr: 0x2ca0
+  __DATA_CONST.__got: 0x13b8
+  __DATA_CONST.__auth_ptr: 0x2cb8
   __DATA.__objc_const: 0xb440
-  __DATA.__objc_selrefs: 0x3988
+  __DATA.__objc_selrefs: 0x39c8
   __DATA.__objc_ivar: 0x348
   __DATA.__objc_data: 0x2748
-  __DATA.__data: 0xbc1c
-  __DATA.__bss: 0x357c0
+  __DATA.__data: 0xbcec
+  __DATA.__bss: 0x358c0
   __DATA.__common: 0x250
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
   - /System/Library/Frameworks/CloudKit.framework/Versions/A/CloudKit

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 15584
-  Symbols:   2016
-  CStrings:  5038
+  Functions: 15623
+  Symbols:   2017
+  CStrings:  5059
 
Symbols:
+ _OBJC_CLASS_$_AMSAuthenticateRequest
CStrings:
+ "%{public}@: [%{public}@] Completed BOP token update with biometricsState: %lu, passcodeState: %ld"
+ "%{public}@: [%{public}@] Pre-flight authenticate result: %{public}@, error: %{public}@"
+ "%{public}@: [%{public}@] Pre-flight authentication failed, skipping token update: %{public}@"
+ "%{public}@: [%{public}@] Running pre-flight authentication before token update"
+ "%{public}@Current passcode state = %ld"
+ "AMSDBiometricsTokenUpdateTask pre-flight authenticate"
+ "No delegate available to present pre-flight authentication"
+ "PREFLIGHT_PROMPT_REASON_FACE_ID_GENERIC"
+ "PREFLIGHT_PROMPT_REASON_OPTIC_ID_GENERIC"
+ "PREFLIGHT_PROMPT_REASON_TOUCH_ID_GENERIC"
+ "Pre-flight Authentication Failed"
+ "URLWithString:"
+ "_currentSystemUptime"
+ "_performPreflightAuthentication"
+ "_performProtocolUpdate"
+ "_preflightPromptReason"
+ "newState request "
+ "setIconURL:"
+ "setReason:"
+ "shouldPerformPreflightAuthentication"
+ "systemimage://lock"
```
