## appinstalld

> `/System/Library/PrivateFrameworks/MobileInstallation.framework/Support/appinstalld`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1674.0.0.0.0
-  __TEXT.__text: 0x3e810
-  __TEXT.__auth_stubs: 0x1130
-  __TEXT.__objc_stubs: 0x5d60
-  __TEXT.__objc_methlist: 0x2404
-  __TEXT.__const: 0x130
-  __TEXT.__cstring: 0xf48a
+1680.40.6.501.1
+  __TEXT.__text: 0x3ea48
+  __TEXT.__auth_stubs: 0x1110
+  __TEXT.__objc_stubs: 0x5dc0
+  __TEXT.__objc_methlist: 0x241c
+  __TEXT.__const: 0x140
+  __TEXT.__cstring: 0xf63a
   __TEXT.__objc_classname: 0x4e7
-  __TEXT.__objc_methname: 0x87a1
-  __TEXT.__objc_methtype: 0x1ca4
-  __TEXT.__gcc_except_tab: 0x1850
+  __TEXT.__objc_methname: 0x886f
+  __TEXT.__objc_methtype: 0x1cb9
+  __TEXT.__gcc_except_tab: 0x1800
   __TEXT.__oslogstring: 0x6f7
   __TEXT.__ustring: 0x84
   __TEXT.__swift5_typeref: 0x1f

   __TEXT.__swift5_fieldmd: 0x10
   __TEXT.__swift5_types: 0x4
   __TEXT.__unwind_info: 0xd80
-  __DATA_CONST.__const: 0xdc8
+  __DATA_CONST.__const: 0xd98
   __DATA_CONST.__cfstring: 0x6d80
   __DATA_CONST.__objc_classlist: 0x100
   __DATA_CONST.__objc_protolist: 0xc0

   __DATA_CONST.__objc_intobj: 0x2a0
   __DATA_CONST.__objc_arraydata: 0x2f0
   __DATA_CONST.__objc_dictobj: 0x758
-  __DATA_CONST.__auth_got: 0x8a8
+  __DATA_CONST.__auth_got: 0x898
   __DATA_CONST.__got: 0x398
   __DATA_CONST.__auth_ptr: 0x30
   __DATA.__objc_const: 0x44a8
-  __DATA.__objc_selrefs: 0x1b68
+  __DATA.__objc_selrefs: 0x1b80
   __DATA.__objc_ivar: 0x1dc
   __DATA.__objc_data: 0xa00
   __DATA.__data: 0xa30

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 919
-  Symbols:   416
-  CStrings:  2641
+  Functions: 922
+  Symbols:   414
+  CStrings:  2646
 
Symbols:
+ _MIMachOHasRunnableSliceSupportingPAC
- _MGCopyAnswer
- _MGGetBoolAnswer
- _MIMachOFileIterateImageVersions
CStrings:
+ "\"%@\" has the entitlement \"%@\" = TRUE which is not allowed for this type of app."
+ "\"%@\" is not built for an architecture that both supports pointer authentication and that is runnable on this device. A runnable architecture supporting pointer authentication (eg. arm64e, or newer) is required for all components of a browser app."
+ "%@ has both the \"%@\" entitlement and the \"%@\" entitlement. Only one of these entitlements can be present at a time. Remove one of these entitlements to allow this app to be installed."
+ "%@ has the \"%@\" entitlement, so it cannot also have the \"%@\" entitlement. Apps that have embedded browser engines may not be default web browsers. Remove one of these entitlements to allow this app to be installed."
+ "+[MIInstallableBundle _requireHasExecutableSliceForArchSupportingPACForBundles:error:]"
+ "-[MIInstallableBundle _performAppExtensionValidationForAppBundleSigningInfo:validatingResources:allowFreeProfileValidation:error:]"
+ "App Clips are not supported on this platform."
+ "B40@0:8@16B24B28^@32"
+ "OSBuildVersionWithError:"
+ "Skipping PAC architecture requirement for %@ and all of its contained executables because it is signed for development or testing."
+ "The XPCService at \"%@\" has the \"%@\" entitlement, which is not allowed on an XPCService."
+ "_performAppExtensionValidationForAppBundleSigningInfo:validatingResources:allowFreeProfileValidation:error:"
+ "_requireHasExecutableSliceForArchSupportingPACForBundles:error:"
+ "com.apple.developer.homekit"
+ "com.apple.developer.superseded-application-identifiers"
+ "getHasExecutableSliceForArchSupportingPAC:withError:"
- "\"%@\" is not built for the ARM64e architecture. The ARM64e architecture is required for all components of a browser app."
- "%@ has both the \"%@\" entitlement and the \"%@\" entitlement. Only one of these entitlements may be present at a time. Remove one of these entitlements to allow this app to be installed."
- "%@ has the \"%@\" entitlement so it may not also have the \"%@\" entitlement. Remove one of these entitlements to allow this app to be installed."
- "Attempted to install an app clip with bundleID %@ on a platform that doesn't support it"
- "B28@?0i8i12I16I20I24"
- "BuildVersion"
- "Failed to copy build version for %@"
- "Skipping ARM64e architecture requirement for %@ and all of its contained executables because it is signed for development or testing."
- "The XPCService extension at \"%@\" has the \"%@\" entitlement, which is not allowed on an XPCService."
- "hasExecutableSliceForCPUType:subtype:error:"
- "li+w2foswFu0srn5UxdOug"
```
