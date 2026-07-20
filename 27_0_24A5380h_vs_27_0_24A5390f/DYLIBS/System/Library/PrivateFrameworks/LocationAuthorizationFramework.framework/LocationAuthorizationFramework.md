## LocationAuthorizationFramework

> `/System/Library/PrivateFrameworks/LocationAuthorizationFramework.framework/LocationAuthorizationFramework`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__weak_got`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__weak_auth_got`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__data`

```diff

-3176.0.0.0.0
-  __TEXT.__text: 0x66624
-  __TEXT.__objc_methlist: 0x12b8
+3183.0.0.0.0
+  __TEXT.__text: 0x67730
+  __TEXT.__objc_methlist: 0x1330
   __TEXT.__const: 0x2ae8
-  __TEXT.__cstring: 0x2891
+  __TEXT.__cstring: 0x292d
   __TEXT.__swift5_typeref: 0xb97
-  __TEXT.__oslogstring: 0x6ff4
-  __TEXT.__constg_swiftt: 0xa58
+  __TEXT.__oslogstring: 0x7277
+  __TEXT.__constg_swiftt: 0xa60
   __TEXT.__swift5_reflstr: 0x645
   __TEXT.__swift5_fieldmd: 0x878
   __TEXT.__swift5_builtin: 0x14

   __TEXT.__swift_as_entry: 0x48
   __TEXT.__swift_as_ret: 0x30
   __TEXT.__swift_as_cont: 0x94
-  __TEXT.__gcc_except_tab: 0x101c
-  __TEXT.__unwind_info: 0x1650
+  __TEXT.__gcc_except_tab: 0x1060
+  __TEXT.__unwind_info: 0x1668
   __TEXT.__eh_frame: 0x16dc
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x860
+  __DATA_CONST.__const: 0x870
   __DATA_CONST.__objc_classlist: 0xa8
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0xe88
+  __DATA_CONST.__objc_selrefs: 0xed0
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x30
   __DATA_CONST.__objc_arraydata: 0x80
-  __DATA_CONST.__got: 0x348
+  __DATA_CONST.__got: 0x368
   __AUTH_CONST.__const: 0x1968
-  __AUTH_CONST.__cfstring: 0x14c0
-  __AUTH_CONST.__objc_const: 0x1c50
+  __AUTH_CONST.__cfstring: 0x1560
+  __AUTH_CONST.__objc_const: 0x1c80
   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__objc_intobj: 0x180
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x48
-  __AUTH_CONST.__auth_got: 0xd20
+  __AUTH_CONST.__auth_got: 0xd18
   __AUTH.__objc_data: 0x3b0
   __AUTH.__data: 0x320
-  __DATA.__objc_ivar: 0x94
+  __DATA.__objc_ivar: 0x98
   __DATA.__data: 0x958
   __DATA.__bss: 0x3910
-  __DATA_DIRTY.__objc_data: 0x848
+  __DATA_DIRTY.__objc_data: 0x850
   __DATA_DIRTY.__data: 0x848
   __DATA_DIRTY.__common: 0x40
   __DATA_DIRTY.__bss: 0x800

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 1912
-  Symbols:   435
-  CStrings:  555
+  Functions: 1922
+  Symbols:   439
+  CStrings:  562
 
Symbols:
+ _CLAuthorizationDatabaseErrorDomain
+ _NSLocalizedDescriptionKey
+ _OBJC_CLASS_$_CLSettingsDictionary
+ _OBJC_CLASS_$_NSError
+ ___kCFBooleanTrue
+ _memset
+ _swift_retain_x25
- __os_feature_enabled_impl
- _swift_retain_x26
- _swift_retain_x27
CStrings:
+ "#AuthorizationDatabase promote: not a known system service"
+ "%@ is already a bellwether or standalone; nothing to promote"
+ "%@ is not a known system service"
+ "Attempting to remove System Service from #AuthorizationDatabase! Refusing removal, since it's not a symlink'd or quarantine'd system service."
+ "Quarantined"
+ "QuarantinedClients"
+ "com.apple.locationd.authorizationdatabase.errorDomain"
+ "{\"msg%{public}.0s\":\"#AuthorizationDatabase promote: already a bellwether/standalone\", \"BundlePath\":%{public, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#AuthorizationDatabase promote: not a known system service\", \"BundlePath\":%{public, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#AuthorizationDatabase promoted innate system service to standalone\", \"BundlePath\":%{public, location:escape_only}@, \"StandaloneKey\":%{public, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"Attempting to remove System Service from #AuthorizationDatabase! Refusing removal, since it's not a symlink'd or quarantine'd system service.\", \"System Service\":%{public, location:escape_only}@}"
- "Attempting to remove System Service from #AuthDatabase! Refusing removal."
- "AuthSync2"
- "CoreLocation"
- "{\"msg%{public}.0s\":\"Attempting to remove System Service from #AuthDatabase! Refusing removal.\", \"System Service\":%{public, location:escape_only}@}"
```
