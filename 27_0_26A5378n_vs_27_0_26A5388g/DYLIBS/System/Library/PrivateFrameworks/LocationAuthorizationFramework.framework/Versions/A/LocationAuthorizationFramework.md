## LocationAuthorizationFramework

> `/System/Library/PrivateFrameworks/LocationAuthorizationFramework.framework/Versions/A/LocationAuthorizationFramework`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_capture`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__weak_got`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-3176.0.0.0.0
-  __TEXT.__text: 0x2f8e4
-  __TEXT.__objc_methlist: 0xd5c
+3183.0.0.0.0
+  __TEXT.__text: 0x302f8
+  __TEXT.__objc_methlist: 0xdd4
   __TEXT.__const: 0x2248
   __TEXT.__swift5_typeref: 0x6c1
   __TEXT.__constg_swiftt: 0x4b8

   __TEXT.__swift5_proto: 0x1c0
   __TEXT.__swift5_types: 0x78
   __TEXT.__swift5_assocty: 0x60
-  __TEXT.__cstring: 0x271d
-  __TEXT.__oslogstring: 0x54b7
+  __TEXT.__cstring: 0x27b9
+  __TEXT.__oslogstring: 0x573a
   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift_as_entry: 0x48
   __TEXT.__swift_as_ret: 0x30
   __TEXT.__swift_as_cont: 0x94
   __TEXT.__swift5_capture: 0x1b0
-  __TEXT.__gcc_except_tab: 0xf60
-  __TEXT.__unwind_info: 0x1080
+  __TEXT.__gcc_except_tab: 0xfa8
+  __TEXT.__unwind_info: 0x1090
   __TEXT.__eh_frame: 0x120c
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x628
+  __DATA_CONST.__const: 0x638
   __DATA_CONST.__objc_classlist: 0x78
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0xb40
+  __DATA_CONST.__objc_selrefs: 0xb88
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x30
   __DATA_CONST.__objc_arraydata: 0x70
-  __DATA_CONST.__got: 0x238
+  __DATA_CONST.__got: 0x248
   __AUTH_CONST.__const: 0x13d0
-  __AUTH_CONST.__cfstring: 0x1480
-  __AUTH_CONST.__objc_const: 0x1390
+  __AUTH_CONST.__cfstring: 0x1520
+  __AUTH_CONST.__objc_const: 0x13d0
   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__objc_intobj: 0x150
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x48
-  __AUTH_CONST.__auth_got: 0x7f8
+  __AUTH_CONST.__auth_got: 0x7f0
   __AUTH.__objc_data: 0x290
   __AUTH.__data: 0x320
-  __DATA.__objc_ivar: 0x90
+  __DATA.__objc_ivar: 0x94
   __DATA.__data: 0x638
   __DATA.__bss: 0x3390
   __DATA_DIRTY.__objc_data: 0x280

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 1326
-  Symbols:   351
-  CStrings:  424
+  Functions: 1334
+  Symbols:   353
+  CStrings:  431
 
Symbols:
+ _CLAuthorizationDatabaseErrorDomain
+ _NSLocalizedDescriptionKey
+ _OBJC_CLASS_$_NSError
- __os_feature_enabled_impl
CStrings:
+ "#AuthorizationDatabase promote: not a known system service"
+ "%@ is already a bellwether or standalone; nothing to promote"
+ "%@ is not a known system service"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Daemon/Core/CSI/CLMachThreadSupport.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Daemon/Core/ClientManagement/CLAuthorizationDatabase.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Daemon/Core/ClientManagement/CLClientKeyPath.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Daemon/Shared/Utilities/CLPersistentDictionary.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.4MNlur/Sources/CoreLocation/Shared/Utilities/CLClientManagerAuthorizationContext.mm"
+ "Attempting to remove System Service from #AuthorizationDatabase! Refusing removal, since it's not a symlink'd or quarantine'd system service."
+ "Quarantined"
+ "QuarantinedClients"
+ "com.apple.locationd.authorizationdatabase.errorDomain"
+ "{\"msg%{public}.0s\":\"#AuthorizationDatabase promote: already a bellwether/standalone\", \"BundlePath\":%{public, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#AuthorizationDatabase promote: not a known system service\", \"BundlePath\":%{public, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#AuthorizationDatabase promoted innate system service to standalone\", \"BundlePath\":%{public, location:escape_only}@, \"StandaloneKey\":%{public, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"Attempting to remove System Service from #AuthorizationDatabase! Refusing removal, since it's not a symlink'd or quarantine'd system service.\", \"System Service\":%{public, location:escape_only}@}"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Daemon/Core/CSI/CLMachThreadSupport.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Daemon/Core/ClientManagement/CLAuthorizationDatabase.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Daemon/Core/ClientManagement/CLClientKeyPath.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Daemon/Shared/Utilities/CLPersistentDictionary.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.EFNobC/Sources/CoreLocation/Shared/Utilities/CLClientManagerAuthorizationContext.mm"
- "Attempting to remove System Service from #AuthDatabase! Refusing removal."
- "AuthSync2"
- "CoreLocation"
- "{\"msg%{public}.0s\":\"Attempting to remove System Service from #AuthDatabase! Refusing removal.\", \"System Service\":%{public, location:escape_only}@}"
```
