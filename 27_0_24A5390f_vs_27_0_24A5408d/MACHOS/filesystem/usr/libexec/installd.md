## installd

> `/usr/libexec/installd`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1673.0.0.0.0
-  __TEXT.__text: 0x70f48
+1674.2.1.0.0
+  __TEXT.__text: 0x70dfc
   __TEXT.__auth_stubs: 0x1760
-  __TEXT.__objc_stubs: 0x8fe0
-  __TEXT.__objc_methlist: 0x390c
+  __TEXT.__objc_stubs: 0x9000
+  __TEXT.__objc_methlist: 0x391c
   __TEXT.__const: 0x1c8
-  __TEXT.__cstring: 0x18723
+  __TEXT.__cstring: 0x18813
   __TEXT.__objc_classname: 0x69f
   __TEXT.__objc_methtype: 0x2405
-  __TEXT.__objc_methname: 0xd567
-  __TEXT.__gcc_except_tab: 0x3c00
+  __TEXT.__objc_methname: 0xd5c7
+  __TEXT.__gcc_except_tab: 0x3bb0
   __TEXT.__oslogstring: 0x14e7
   __TEXT.__ustring: 0x84
   __TEXT.__swift5_typeref: 0xe6

   __TEXT.__swift5_fieldmd: 0x10
   __TEXT.__swift5_types: 0x4
   __TEXT.__swift5_capture: 0x80
-  __TEXT.__unwind_info: 0x14f8
+  __TEXT.__unwind_info: 0x14f0
   __TEXT.__eh_frame: 0x218
-  __DATA_CONST.__const: 0x1638
-  __DATA_CONST.__cfstring: 0xa620
+  __DATA_CONST.__const: 0x1610
+  __DATA_CONST.__cfstring: 0xa600
   __DATA_CONST.__objc_classlist: 0x160
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xe0

   __DATA_CONST.__got: 0x478
   __DATA_CONST.__auth_ptr: 0x68
   __DATA.__objc_const: 0x6348
-  __DATA.__objc_selrefs: 0x28d8
+  __DATA.__objc_selrefs: 0x28e0
   __DATA.__objc_ivar: 0x2a4
   __DATA.__objc_data: 0xe40
   __DATA.__data: 0xbf8
Symbols:
+ _MIMachOFileImageSlices
+ _MIMachOHasRunnableSliceSupportingPAC
- _MGGetBoolAnswer
- _MIMachOFileIterateImageVersions
Functions:
~ sub_100050aa8 : 2720 -> 472
~ sub_100051548 -> sub_100050c80 : 16 -> 2084
~ sub_100051558 -> sub_1000514a4 : 8 -> 16
~ sub_100051560 -> sub_1000514b4 : 456 -> 8
~ sub_100051728 -> sub_1000514bc : 52 -> 340
CStrings:
+ "\"%@\" is not built for an architecture that both supports pointer authentication and that is runnable on this device. A runnable architecture supporting pointer authentication (eg. arm64e, or newer) is required for all components of a browser app."
+ "%@ has both the \"%@\" entitlement and the \"%@\" entitlement. Only one of these entitlements can be present at a time. Remove one of these entitlements to allow this app to be installed."
+ "%@ has the \"%@\" entitlement, so it cannot also have the \"%@\" entitlement. Apps that have embedded browser engines may not be default web browsers. Remove one of these entitlements to allow this app to be installed."
+ "+[MIInstallableBundle _requireHasExecutableSliceForArchSupportingPACForBundles:error:]"
+ "Skipping PAC architecture requirement for %@ and all of its contained executables because it is signed for development or testing."
+ "_requireHasExecutableSliceForArchSupportingPACForBundles:error:"
+ "getHasExecutableSliceForArchSupportingPAC:withError:"
- "\"%@\" is not built for the ARM64e architecture. The ARM64e architecture is required for all components of a browser app."
- "%@ has both the \"%@\" entitlement and the \"%@\" entitlement. Only one of these entitlements may be present at a time. Remove one of these entitlements to allow this app to be installed."
- "%@ has the \"%@\" entitlement so it may not also have the \"%@\" entitlement. Remove one of these entitlements to allow this app to be installed."
- "B28@?0i8i12I16I20I24"
- "Skipping ARM64e architecture requirement for %@ and all of its contained executables because it is signed for development or testing."
- "hasExecutableSliceForCPUType:subtype:error:"
- "li+w2foswFu0srn5UxdOug"
```
