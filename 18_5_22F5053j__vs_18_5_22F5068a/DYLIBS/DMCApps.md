## DMCApps

> `/System/Library/PrivateFrameworks/DMCApps.framework/DMCApps`

```diff

-20.5.1.0.0
-  __TEXT.__text: 0x22aa0
-  __TEXT.__auth_stubs: 0x7d0
-  __TEXT.__const: 0xdbc
+20.5.1.2.0
+  __TEXT.__text: 0x22dfc
+  __TEXT.__auth_stubs: 0x800
+  __TEXT.__const: 0xdcc
   __TEXT.__cstring: 0x612
   __TEXT.__swift5_typeref: 0x41d
   __TEXT.__constg_swiftt: 0x8c4

   __TEXT.__swift5_proto: 0x84
   __TEXT.__swift5_types: 0x74
   __TEXT.__swift5_protos: 0x30
-  __TEXT.__oslogstring: 0x928
+  __TEXT.__oslogstring: 0x978
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_mpenum: 0x10
   __TEXT.__swift_as_entry: 0xec
   __TEXT.__swift_as_ret: 0x174
-  __TEXT.__unwind_info: 0x960
-  __TEXT.__eh_frame: 0x22b0
+  __TEXT.__unwind_info: 0x968
+  __TEXT.__eh_frame: 0x22e8
   __TEXT.__objc_methname: 0x414
   __DATA_CONST.__got: 0x1b8
   __DATA_CONST.__const: 0x78
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x1a8
-  __AUTH_CONST.__auth_got: 0x3e8
+  __AUTH_CONST.__auth_got: 0x400
   __AUTH_CONST.__auth_ptr: 0x168
   __AUTH_CONST.__const: 0x1160
   __AUTH_CONST.__objc_const: 0x188

   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
   Functions: 659
-  Symbols:   353
-  CStrings:  140
+  Symbols:   355
+  CStrings:  141
 
Symbols:
+ _swift_release_n
+ _swift_retain_n
CStrings:
+ "Failed to fetch any bundleIDs for protected apps: %{public}@"
+ "Failed to fetch apps with error: %{public}@"
+ "Failed to perform start managing request with error: %{public}@"
+ "Failed to perform update app attributes request with error: %{public}@"
+ "Failed to remove DMF app data: %{public}@"
+ "Start managing app: %{public}s"
+ "Stop managing app: %{public}s"
+ "Unable to create DMFMDMv1StartManagingAppRequest for %{public}s"
+ "Unable to create DMFStopManagingAppRequest for %{public}s"
+ "Unable to create DMFUpdateAppAttributesRequest for %{public}s"
+ "Update managing app: %{public}s"
+ "appsWithNonDefaultProtectionAttributes = %{public}s"
+ "non-bool value specified for %{public}s, using default value"
- "Failed to fetch any bundleIDs for protected apps."
- "Failed to fetch apps with error: %@"
- "Failed to perform start managing request with error: %@"
- "Failed to perform update app attributes request with error: %@"
- "Failed to remove DMF app data: %@"
- "Start managing app: %s"
- "Stop managing app: %s"
- "Unable to create DMFMDMv1StartManagingAppRequest for %s"
- "Unable to create DMFStopManagingAppRequest for %s"
- "Unable to create DMFUpdateAppAttributesRequest for %s"
- "Update managing app: %s"
- "non-bool value specified for %s, using default value"

```
