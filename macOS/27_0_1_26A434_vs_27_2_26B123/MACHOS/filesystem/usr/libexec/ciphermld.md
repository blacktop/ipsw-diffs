## ciphermld

> `/usr/libexec/ciphermld`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_entry`
- `__TEXT.__swift5_typeref`
- `__TEXT.__info_plist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_selrefs`

```diff

-383.0.24.0.0
-  __TEXT.__text: 0x2870
+383.40.16.0.0
+  __TEXT.__text: 0x2928
   __TEXT.__auth_stubs: 0x510
   __TEXT.__objc_stubs: 0x40
-  __TEXT.__const: 0xa0
-  __TEXT.__cstring: 0x1ed
+  __TEXT.__const: 0xa8
+  __TEXT.__cstring: 0x193
   __TEXT.__objc_methtype: 0x6
-  __TEXT.__oslogstring: 0x67
+  __TEXT.__oslogstring: 0x12f
   __TEXT.__swift5_entry: 0x8
   __TEXT.__swift5_typeref: 0x6b
   __TEXT.__info_plist: 0x46a

   __DATA_CONST.__const: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__auth_got: 0x290
-  __DATA_CONST.__got: 0x88
+  __DATA_CONST.__got: 0x60
   __DATA_CONST.__auth_ptr: 0x38
   __DATA.__objc_selrefs: 0x10
   __DATA.__data: 0x58

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
   Functions: 39
-  Symbols:   117
-  CStrings:  20
+  Symbols:   112
+  CStrings:  19
 
Symbols:
+ _$s8CipherML23DataProtectionMigrationO15migrateIfNeededyyFZ
+ _$sSS10FoundationE36_unconditionallyBridgeFromObjectiveCySSSo8NSStringCSgFZ
+ _$sSo13os_log_type_ta0A0E5errorABvgZ
+ _$sypN
+ _NSHomeDirectory
- _$sSSSTsWP
- _$sSSs25LosslessStringConvertiblesWP
- _$sSSySSxcs25LosslessStringConvertibleRzSTRzSJ7ElementSTRtzlufC
- _$ss23CustomStringConvertibleP11descriptionSSvgTj
- _$ss5Int32VN
- _$ss5Int32Vs23CustomStringConvertiblesWP
- _$ss6UInt32VN
- _$ss6UInt32Vs23CustomStringConvertiblesWP
- _getpwuid
- _getuid
Functions:
~ sub_100000d30 : 1220 -> 1224
~ sub_1000015c4 -> sub_1000015c8 : 588 -> 716
~ sub_100002d68 -> sub_100002dec : 800 -> 852
CStrings:
+ "/private/var/empty"
+ "Sandbox: realpath('%{public}s') failed, errno %{public}d (%{public}s); binding HOME to %{public}s. HOME-relative cache rules will not grant access until the real home directory is reachable."
- ") for home directory failed "
- "Failed to get passwd entry for uid "
- "Sandbox: realpath("
```
