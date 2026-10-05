## installcoordinationd

> `/System/Library/PrivateFrameworks/InstallCoordination.framework/Support/installcoordinationd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_protos`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-849.40.4.0.1
-  __TEXT.__text: 0x9e474
-  __TEXT.__auth_stubs: 0x1ae0
-  __TEXT.__objc_stubs: 0xa660
+849.40.7.0.2
+  __TEXT.__text: 0x9ebd4
+  __TEXT.__auth_stubs: 0x1af0
+  __TEXT.__objc_stubs: 0xa6e0
   __TEXT.__objc_methlist: 0x5184
   __TEXT.__const: 0x5e0
-  __TEXT.__cstring: 0x16a7a
-  __TEXT.__oslogstring: 0xd57c
+  __TEXT.__cstring: 0x16ada
+  __TEXT.__oslogstring: 0xd6cc
   __TEXT.__objc_classname: 0x9f6
   __TEXT.__objc_methtype: 0x28a5
-  __TEXT.__objc_methname: 0x1007b
+  __TEXT.__objc_methname: 0x1015b
   __TEXT.__gcc_except_tab: 0x2ce8
   __TEXT.__ustring: 0x1b64
   __TEXT.__dlopen_cstrs: 0x68

   __TEXT.__swift5_assocty: 0x48
   __TEXT.__swift5_proto: 0x18
   __TEXT.__swift5_types: 0x10
-  __TEXT.__swift5_capture: 0x1c0
+  __TEXT.__swift5_capture: 0x1d0
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x3100
-  __TEXT.__eh_frame: 0x5a0
+  __TEXT.__unwind_info: 0x3110
+  __TEXT.__eh_frame: 0x5c8
   __DATA_CONST.__const: 0x2e08
   __DATA_CONST.__cfstring: 0x85c0
   __DATA_CONST.__objc_classlist: 0x1c8

   __DATA_CONST.__objc_intobj: 0x138
   __DATA_CONST.__objc_arraydata: 0x41d0
   __DATA_CONST.__objc_dictobj: 0x6dd8
-  __DATA_CONST.__auth_got: 0xd80
-  __DATA_CONST.__got: 0x5a8
+  __DATA_CONST.__auth_got: 0xd88
+  __DATA_CONST.__got: 0x5b8
   __DATA_CONST.__auth_ptr: 0xb8
   __DATA.__objc_const: 0xb4d0
-  __DATA.__objc_selrefs: 0x3110
+  __DATA.__objc_selrefs: 0x3130
   __DATA.__objc_ivar: 0x378
   __DATA.__objc_data: 0x1318
   __DATA.__data: 0xe70

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3245
-  Symbols:   638
-  CStrings:  5091
+  Functions: 3249
+  Symbols:   641
+  CStrings:  5101
 
Symbols:
+ _MobileInstallationEndAppReplacement
+ _MobileInstallationSetAppLaunchProhibited
+ _OBJC_CLASS_$_IXAppInstallCoordinator
+ _OBJC_CLASS_$_IXAppReplacementSourceResolver
- _MobileInstallationSetAppReplacementStatus
CStrings:
+ "%s: Failed to clear the app launch prohibition marker for %@: %@"
+ "%s: Failed to determine what MDM manages, so the app replacement source for %@ can't be resolved: %@"
+ "%s: Failed to resolve app replacement source for %@: %@"
+ "%s: Failed to subscribe to managed app events: %@"
+ "-[IXSCoordinatedAppInstall _finishAppInstallAtURL:result:recordPromise:error:]_block_invoke"
+ "Failed to push replacement info for %@ to LS: %s"
+ "initWithIdentity:managedAppBundleIdentifiers:"
+ "managedAppBundleIdentifiersWithError:"
+ "prepareForAppReplacementSourceLookupWithOptions:error:"
+ "resolveAppReplacementSource:replacementRuledOut:replacementCandidate:error:"
```
