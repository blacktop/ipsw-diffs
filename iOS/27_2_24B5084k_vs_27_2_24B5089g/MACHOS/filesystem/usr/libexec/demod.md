## demod

> `/usr/libexec/demod`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_proto`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1871.40.45.0.0
-  __TEXT.__text: 0xf55d8
+1871.40.52.0.0
+  __TEXT.__text: 0xf5c44
   __TEXT.__auth_stubs: 0x2150
-  __TEXT.__objc_stubs: 0x1ba40
-  __TEXT.__objc_methlist: 0xdc5c
+  __TEXT.__objc_stubs: 0x1bb80
+  __TEXT.__objc_methlist: 0xdc8c
   __TEXT.__const: 0x538
-  __TEXT.__cstring: 0x11542
+  __TEXT.__cstring: 0x115b2
   __TEXT.__objc_classname: 0x18ea
   __TEXT.__objc_methtype: 0x40bb
   __TEXT.__gcc_except_tab: 0x47f8
-  __TEXT.__oslogstring: 0x1d56c
-  __TEXT.__objc_methname: 0x21696
+  __TEXT.__oslogstring: 0x1d6bc
+  __TEXT.__objc_methname: 0x2174e
   __TEXT.__swift5_typeref: 0x11a
   __TEXT.__swift5_capture: 0xcc
   __TEXT.__constg_swiftt: 0x80

   __TEXT.__swift5_assocty: 0x18
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_proto: 0x20
-  __TEXT.__unwind_info: 0x5138
+  __TEXT.__unwind_info: 0x5158
   __TEXT.__eh_frame: 0x3d0
-  __DATA_CONST.__const: 0x3280
-  __DATA_CONST.__cfstring: 0xef00
+  __DATA_CONST.__const: 0x32a0
+  __DATA_CONST.__cfstring: 0xef60
   __DATA_CONST.__objc_classlist: 0x738
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0x168

   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA_CONST.__objc_dictobj: 0x140
   __DATA_CONST.__auth_got: 0x10b8
-  __DATA_CONST.__got: 0xf30
+  __DATA_CONST.__got: 0xf58
   __DATA_CONST.__auth_ptr: 0x198
   __DATA.__objc_const: 0x19a60
-  __DATA.__objc_selrefs: 0x82f8
+  __DATA.__objc_selrefs: 0x8348
   __DATA.__objc_ivar: 0xb40
   __DATA.__objc_data: 0x48f0
   __DATA.__data: 0x2a00

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 6139
-  Symbols:   1061
-  CStrings:  11047
+  Functions: 6148
+  Symbols:   1066
+  CStrings:  11064
 
Symbols:
+ _OBJC_CLASS_$_MSDKDemoState
+ _kSecAttrDescription
+ _kSecAttrGeneric
+ _kSecAttrIsInvisible
+ _kSecAttrType
CStrings:
+ "/var/mobile/Library/Preferences/com.apple.voicetrigger.plist"
+ "Disabled explicit music for the primary home's current user."
+ "EnableSiriAI"
+ "Failed to disable explicit music.  Could not find a primary home for where user belongs to."
+ "Failed to disable explicit music.  Error code: %ld, description: %{public}@"
+ "Failed to disable explicit music.  No '%s' setting in the current user's settings for the primary home."
+ "_findSettingWithKeyPath:inGroup:"
+ "currentUser"
+ "disableExplicitMusic"
+ "enableSiriAI"
+ "enableSiriAI:"
+ "groups"
+ "isPressDemoModeEnabled:"
+ "keyPath"
+ "root.music.allowExplicitContent"
+ "updateValue:completionHandler:"
+ "userSettingsForHome:"
```
