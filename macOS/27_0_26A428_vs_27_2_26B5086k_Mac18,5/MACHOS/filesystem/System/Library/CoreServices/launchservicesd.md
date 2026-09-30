## launchservicesd

> `/System/Library/CoreServices/launchservicesd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_classrefs`
- `__DATA.__objc_superrefs`
- `__DATA.__objc_data`

```diff

-1517.0.1.402.0
-  __TEXT.__text: 0x5e1e8
-  __TEXT.__auth_stubs: 0x1900
+1517.1.8.0.0
+  __TEXT.__text: 0x5f740
+  __TEXT.__auth_stubs: 0x1920
   __TEXT.__objc_stubs: 0x6a0
   __TEXT.__objc_methlist: 0x68
   __TEXT.__const: 0x390
-  __TEXT.__cstring: 0x3989
-  __TEXT.__oslogstring: 0xc2fb
+  __TEXT.__cstring: 0x3ad1
+  __TEXT.__oslogstring: 0xc506
   __TEXT.__gcc_except_tab: 0x61c
   __TEXT.__objc_methname: 0x3c6
   __TEXT.__objc_classname: 0x1f
   __TEXT.__objc_methtype: 0x3b
-  __TEXT.__unwind_info: 0x17a0
-  __DATA_CONST.__const: 0x4d60
-  __DATA_CONST.__cfstring: 0xea0
+  __TEXT.__unwind_info: 0x17f0
+  __DATA_CONST.__const: 0x4dd0
+  __DATA_CONST.__cfstring: 0xee0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__auth_got: 0xc90
+  __DATA_CONST.__auth_got: 0xca0
   __DATA_CONST.__got: 0x6a8
   __DATA_CONST.__auth_ptr: 0x20
   __DATA.__objc_const: 0x100

   __DATA.__objc_superrefs: 0x8
   __DATA.__objc_ivar: 0x8
   __DATA.__objc_data: 0x50
-  __DATA.__data: 0x150
+  __DATA.__data: 0x148
   __DATA.__crash_info: 0x148
   __DATA.__common: 0x48
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1408
-  Symbols:   653
-  CStrings:  1331
+  Functions: 1429
+  Symbols:   655
+  CStrings:  1346
 
Symbols:
+ _CFStringFind
+ _CFStringFindAndReplace
CStrings:
+ "\n   "
+ " ("
+ " - MISMATCH: asn "
+ " - MISMATCH: pid "
+ " is registered to asn "
+ " mismatch(es) found between the asn and pid registries."
+ ") records pid "
+ "), but that asn "
+ ", but that pid is registered to a different application: asn "
+ "APP: Application %{public}@ has a different audit_token, %d/%d vs %d/%d, so probably re-execed. 183509309"
+ "ASN %{public}s already in registry when inserting %{public}s; leaving existing entry %{public}s in place."
+ "Application %{public}@/%{private}@ has already checked in and an child pid %{public}d is checking in, so forcing a new application record to be created. 183509309"
+ "Application %{public}@/%{private}@ has already checked in and its audit token exactly matched, so returning existing information and ignoring additional checkin. 183509309"
+ "CopyPendingApplicationByPidOrUnRegisteredParentPid(app=%{public}@/%{private}@ found by pid %{public}d but is already registered."
+ "PID %d already in registry when inserting %{public}s; leaving existing entry %{public}s in place."
+ "Registry consistency check: "
+ "Updating application %{public}s in getProcessesDictionaryQueue(): pid %{public}d -> %{public}d asn=%{public}s"
+ "is registered to a different application"
+ "setting pid in fInfo of %s to %d but ivar is %d, expected them to agree"
+ "was not found in the asn registry at all"
- " -- found application %{public}s as pid or parent pid of %d"
- "APP: Application %{public}@ has a different audit_token, %d/%d vs %d/%d, so probably re-execed."
- "Adding application %{public}s from getProcessesByPidDictionary() with pid=%{public}d asn=%{public}s"
- "CopyMatchingApplication: Checking application %{public}@ against criteria."
- "Removing application %{public}s from getProcessesByPidDictionary() with pid=%{public}d asn=%{public}s"
```
