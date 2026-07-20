## launchservicesd

> `/System/Library/CoreServices/launchservicesd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_classrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1507.0.0.0.0
-  __TEXT.__text: 0x5d4c8
-  __TEXT.__auth_stubs: 0x18f0
+1510.400.0.0.0
+  __TEXT.__text: 0x5d69c
+  __TEXT.__auth_stubs: 0x1900
   __TEXT.__objc_stubs: 0x6a0
   __TEXT.__objc_methlist: 0x68
   __TEXT.__const: 0x390
-  __TEXT.__cstring: 0x3885
-  __TEXT.__oslogstring: 0xbdf2
-  __TEXT.__gcc_except_tab: 0x5f8
+  __TEXT.__cstring: 0x3909
+  __TEXT.__oslogstring: 0xbe32
+  __TEXT.__gcc_except_tab: 0x61c
   __TEXT.__objc_methname: 0x3c6
   __TEXT.__objc_classname: 0x1f
   __TEXT.__objc_methtype: 0x3b
   __TEXT.__unwind_info: 0x1718
-  __DATA_CONST.__const: 0x4bd0
-  __DATA_CONST.__cfstring: 0xe40
+  __DATA_CONST.__const: 0x4bd8
+  __DATA_CONST.__cfstring: 0xe60
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__auth_got: 0xc88
+  __DATA_CONST.__auth_got: 0xc90
   __DATA_CONST.__got: 0x688
-  __DATA_CONST.__auth_ptr: 0x18
+  __DATA_CONST.__auth_ptr: 0x20
   __DATA.__objc_const: 0x100
   __DATA.__objc_selrefs: 0x1b8
   __DATA.__objc_classrefs: 0x50

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1396
-  Symbols:   648
-  CStrings:  1312
+  Functions: 1397
+  Symbols:   649
+  CStrings:  1313
 
Symbols:
+ _proc_name
CStrings:
+ "App %{public}@ still has non-application process in its coalition %{public}lld, pid=%{public}d/%{public}@ running."
+ "Attempting to acquire the running board assertion for pid %{public}ld/%{public}@ took %{public}g seconds, which is much longer than expected; please get a sysdiagnose, file a bug against RunningBoard / All and relate it to <rdar://problem/53521039>"
+ "Caller is missing the _kLSClientAllowedToForciblyRemoveApplication or _kLSClientAllowedToBeQuitReallyHandler entitlement."
+ "Unexpected job type %{public}d for job %{public}d/%{public}@/%{public}@/%{public}@"
+ "com.apple.private.launchservices.allowedtoforciblyremoveapplicationfromrunninglist"
+ "copyJobsLoadedByCoalition: coalitionID=%{public}lld hostPid=%{public}d/%{public}@ job=%{public}@ PID domain job allowed by quit."
+ "enableQuitTrackingSupport: %{BOOL}d, log version %d."
- "App %{public}@ still has non-application process in its coalition %{public}lld, pid=%{public}d running."
- "Attempting to acquire the running board assertion for pid %{public}ld took %{public}g seconds, which is much longer than expected; please get a sysdiagnose, file a bug against RunningBoard / All and relate it to <rdar://problem/53521039>"
- "Caller is missing the kLSClientAllowedToBeQuitReallyHandler entitlement."
- "Unexpected job type %{public}d for job %{public}d/%{public}@/%{public}@"
- "copyJobsLoadedByCoalition: coalitionID=%{public}lld hostPid=%{public}d job=%{public}@ PID domain job allowed by quit."
- "enableQuitReally: %{BOOL}d, log version %d."
```
