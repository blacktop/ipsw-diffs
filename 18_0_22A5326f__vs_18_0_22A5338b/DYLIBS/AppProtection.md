## AppProtection

> `/System/Library/PrivateFrameworks/AppProtection.framework/AppProtection`

```diff

-34.0.0.0.0
-  __TEXT.__text: 0x8f100
-  __TEXT.__auth_stubs: 0x1e40
-  __TEXT.__objc_methlist: 0xcf8
-  __TEXT.__const: 0x3660
-  __TEXT.__oslogstring: 0x32f8
-  __TEXT.__cstring: 0x4a24
-  __TEXT.__swift5_typeref: 0x26c0
-  __TEXT.__swift5_fieldmd: 0x1a08
-  __TEXT.__constg_swiftt: 0x2ebc
-  __TEXT.__swift5_reflstr: 0x16df
+35.0.0.0.0
+  __TEXT.__text: 0x9108c
+  __TEXT.__auth_stubs: 0x1e80
+  __TEXT.__objc_methlist: 0xd08
+  __TEXT.__const: 0x3670
+  __TEXT.__oslogstring: 0x3408
+  __TEXT.__cstring: 0x4b64
+  __TEXT.__swift5_typeref: 0x26d2
+  __TEXT.__swift5_fieldmd: 0x1a14
+  __TEXT.__constg_swiftt: 0x2f2c
+  __TEXT.__swift5_reflstr: 0x16ff
   __TEXT.__swift5_builtin: 0x154
   __TEXT.__swift5_assocty: 0x420
-  __TEXT.__swift5_capture: 0x11e0
+  __TEXT.__swift5_capture: 0x1234
   __TEXT.__swift5_protos: 0xa4
   __TEXT.__swift5_proto: 0x290
   __TEXT.__swift5_types: 0x22c
   __TEXT.__swift5_mpenum: 0x50
-  __TEXT.__unwind_info: 0x1fe0
-  __TEXT.__eh_frame: 0x26c0
+  __TEXT.__unwind_info: 0x2048
+  __TEXT.__eh_frame: 0x2778
   __TEXT.__objc_classname: 0x1f6
-  __TEXT.__objc_methname: 0x1e1a
+  __TEXT.__objc_methname: 0x1e75
   __TEXT.__objc_methtype: 0x628
   __TEXT.__objc_stubs: 0x440
-  __DATA_CONST.__got: 0x550
+  __DATA_CONST.__got: 0x558
   __DATA_CONST.__const: 0x338
   __DATA_CONST.__objc_classlist: 0x220
   __DATA_CONST.__objc_protolist: 0x180
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x858
+  __DATA_CONST.__objc_selrefs: 0x878
   __DATA_CONST.__objc_protorefs: 0xf8
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0xf28
-  __AUTH_CONST.__auth_ptr: 0x940
-  __AUTH_CONST.__const: 0x5d50
+  __AUTH_CONST.__auth_got: 0xf48
+  __AUTH_CONST.__auth_ptr: 0x910
+  __AUTH_CONST.__const: 0x5e68
   __AUTH_CONST.__cfstring: 0x4e0
-  __AUTH_CONST.__objc_const: 0x3fe0
+  __AUTH_CONST.__objc_const: 0x4000
   __AUTH.__objc_data: 0x19f0
-  __AUTH.__data: 0x1dc8
+  __AUTH.__data: 0x1de8
   __DATA.__objc_ivar: 0xc
   __DATA.__data: 0x1f00
   __DATA.__bss: 0x3ab0
-  __DATA.__common: 0xe0
+  __DATA.__common: 0xd8
   __DATA_DIRTY.__objc_data: 0x408
   __DATA_DIRTY.__data: 0x800
   __DATA_DIRTY.__bss: 0x2f0

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 3085
-  Symbols:   807
-  CStrings:  1189
+  Functions: 3125
+  Symbols:   813
+  CStrings:  1205
 
Symbols:
+ _OBJC_CLASS_$_ACAccountStore
+ _xpc_array_apply
CStrings:
+ "B24@?0q8@\"<OS_xpc_object>\"16"
+ "Client is missing com.apple.private.accounts.allaccounts entitlement"
+ "LocalAuthenticationAuthProvider has no fence age"
+ "No fence age cached: %!@(MISSING)"
+ "No fence age for underlying provider %!s(MISSING): %!@(MISSING)"
+ "Should not guard and track %!d(MISSING); access allowed to %!s(MISSING) by entitlement"
+ "_lastFenceTimeNS"
+ "aa_ageCategory"
+ "aa_primaryAppleAccount"
+ "com.apple.appprotection.uncheckedTCCServices"
+ "com.apple.private.accounts.allaccounts"
+ "defaultStore"
+ "errorPreventingMutatingHiddenState(of:)"
+ "errorPreventingMutatingLockedState(of:)"
+ "initWithExtensionUUID:bundleIdentifier:"
+ "primary account is nil"

```
