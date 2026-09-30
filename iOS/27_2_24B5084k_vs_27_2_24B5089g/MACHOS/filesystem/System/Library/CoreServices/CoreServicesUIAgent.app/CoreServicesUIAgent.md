## CoreServicesUIAgent

> `/System/Library/CoreServices/CoreServicesUIAgent.app/CoreServicesUIAgent`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift5_entry`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`

```diff

-469.1.6.0.0
-  __TEXT.__text: 0x14e30
-  __TEXT.__auth_stubs: 0xe20
-  __TEXT.__objc_stubs: 0xf80
-  __TEXT.__objc_methlist: 0xd90
-  __TEXT.__cstring: 0xd13
+469.1.7.0.0
+  __TEXT.__text: 0x16e94
+  __TEXT.__auth_stubs: 0xe30
+  __TEXT.__objc_stubs: 0x1020
+  __TEXT.__objc_methlist: 0xd60
+  __TEXT.__cstring: 0x1143
   __TEXT.__objc_classname: 0x4c3
-  __TEXT.__objc_methtype: 0x17d1
-  __TEXT.__objc_methname: 0x2e19
-  __TEXT.__const: 0xac4
-  __TEXT.__constg_swiftt: 0x808
-  __TEXT.__swift5_typeref: 0x630
-  __TEXT.__swift5_reflstr: 0x1e9
-  __TEXT.__swift5_fieldmd: 0x360
+  __TEXT.__objc_methtype: 0x1801
+  __TEXT.__objc_methname: 0x2eb6
+  __TEXT.__const: 0xb34
+  __TEXT.__constg_swiftt: 0x83c
+  __TEXT.__swift5_typeref: 0x662
+  __TEXT.__swift5_reflstr: 0x209
+  __TEXT.__swift5_fieldmd: 0x394
   __TEXT.__swift5_builtin: 0x3c
   __TEXT.__swift5_assocty: 0x78
   __TEXT.__swift5_proto: 0x48
-  __TEXT.__swift5_types: 0x5c
-  __TEXT.__swift5_capture: 0x128
-  __TEXT.__oslogstring: 0x9af
-  __TEXT.__swift_as_entry: 0x1c
-  __TEXT.__swift_as_ret: 0x1c
-  __TEXT.__swift_as_cont: 0x5c
+  __TEXT.__swift5_types: 0x60
+  __TEXT.__swift5_capture: 0x124
+  __TEXT.__oslogstring: 0xa7f
+  __TEXT.__swift_as_entry: 0x20
+  __TEXT.__swift_as_ret: 0x20
+  __TEXT.__swift_as_cont: 0x78
   __TEXT.__swift5_protos: 0x10
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0x6a8
-  __TEXT.__eh_frame: 0x538
-  __DATA_CONST.__const: 0x8c0
+  __TEXT.__unwind_info: 0x728
+  __TEXT.__eh_frame: 0x740
+  __DATA_CONST.__const: 0x990
   __DATA_CONST.__cfstring: 0x80
   __DATA_CONST.__objc_classlist: 0x88
   __DATA_CONST.__objc_protolist: 0xb0

   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA_CONST.__auth_got: 0x718
-  __DATA_CONST.__got: 0x240
-  __DATA_CONST.__auth_ptr: 0x228
-  __DATA.__objc_const: 0x11e8
-  __DATA.__objc_selrefs: 0xa30
+  __DATA_CONST.__auth_got: 0x720
+  __DATA_CONST.__got: 0x268
+  __DATA_CONST.__auth_ptr: 0x240
+  __DATA.__objc_const: 0x1208
+  __DATA.__objc_selrefs: 0xa68
   __DATA.__objc_ivar: 0x8
-  __DATA.__objc_data: 0xb68
-  __DATA.__data: 0xd48
-  __DATA.__common: 0xa0
+  __DATA.__objc_data: 0xb88
+  __DATA.__data: 0xd78
+  __DATA.__common: 0xb0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 430
-  Symbols:   398
-  CStrings:  655
+  Functions: 450
+  Symbols:   403
+  CStrings:  687
 
Symbols:
+ _$s10Foundation3URLV6stringACSgSSh_tcfC
+ _$s10Foundation3URLVs23CustomStringConvertibleAAMc
+ _IXAppReplacementErrorDomain
+ _OBJC_CLASS_$_LSApplicationWorkspace
+ _OBJC_CLASS_$__LSOpenConfiguration
CStrings:
+ "AppMigrationNothingIsHappening"
+ "AppMigrationSomethingIsHappening"
+ "CoreServicesUIAgent/MigrationErrorHandler.swift"
+ "Could Not Move App Data and Settings from “%1$@”"
+ "Not Enough Free Space"
+ "Some data and settings failed to transfer. %@"
+ "The existing “%1$@” is being restored from backup. Try again later."
+ "The existing “%1$@” is busy. Try again later."
+ "The existing “%1$@” is installing. Try again later."
+ "The existing “%1$@” is updating. Try again later."
+ "Transferring your data to this app requires at least 1 GB of available storage. You can manage storage in Settings."
+ "_createCheckedThrowingContinuation(_:)"
+ "code"
+ "couldn't open %s: %@"
+ "defaultWorkspace"
+ "describes an app that is installing"
+ "describes an app that is restoring from backup"
+ "describes an app that is updating"
+ "describes an app whose install state is busy"
+ "domain"
+ "errorHandler"
+ "generic exposition on failure for app migration. Error's localized description is interpolated"
+ "generic failure explaination for app migration"
+ "migration failed for %@: %@"
+ "noteMigrationIsDoingSomethingWithNotification:"
+ "noteMigrationIsntDoingAnythingWithNotification:"
+ "openURL:configuration:completionHandler:"
+ "prefs:root=General&path=STORAGE_MGMT"
+ "setSensitive:"
+ "showing storage settings per user request"
+ "unexpected error code from IX %{public}ld"
+ "unexpected error from IX %{public}@"
+ "unexpectedly asked to localize name for error code %{public}ld"
+ "v24@?0@\"NSDictionary\"8@\"NSError\"16"
- "App Replacement Failed"
- "migration failed for %@: %@, releasing preflight on scene"
```
