## BackupAgent2

> `/usr/libexec/BackupAgent2`

```diff

-2899.0.11.0.0
-  __TEXT.__text: 0x9edd4
+2899.40.32.0.0
+  __TEXT.__text: 0x9f398
   __TEXT.__auth_stubs: 0x1a30
-  __TEXT.__objc_stubs: 0xd8e0
-  __TEXT.__objc_methlist: 0x6b98
+  __TEXT.__objc_stubs: 0xd980
+  __TEXT.__objc_methlist: 0x6be0
   __TEXT.__const: 0x4d0
-  __TEXT.__cstring: 0x1ba82
-  __TEXT.__oslogstring: 0xe708
-  __TEXT.__objc_methname: 0xfc6c
+  __TEXT.__cstring: 0x1bafb
+  __TEXT.__oslogstring: 0xe7d2
+  __TEXT.__objc_methname: 0xfd20
   __TEXT.__objc_classname: 0xaeb
   __TEXT.__objc_methtype: 0x2176
   __TEXT.__gcc_except_tab: 0x2740
-  __TEXT.__unwind_info: 0x1bb8
+  __TEXT.__unwind_info: 0x1bc0
   __DATA_CONST.__auth_got: 0xd28
-  __DATA_CONST.__got: 0x538
+  __DATA_CONST.__got: 0x540
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x1600
-  __DATA_CONST.__cfstring: 0xa360
+  __DATA_CONST.__cfstring: 0xa3a0
   __DATA_CONST.__objc_classlist: 0x3c0
   __DATA_CONST.__objc_catlist: 0x60
   __DATA_CONST.__objc_protolist: 0xa8

   __DATA_CONST.__objc_arraydata: 0x100
   __DATA_CONST.__objc_arrayobj: 0xc0
   __DATA_CONST.__objc_dictobj: 0x78
-  __DATA.__objc_const: 0xaac0
-  __DATA.__objc_selrefs: 0x4348
+  __DATA.__objc_const: 0xaad0
+  __DATA.__objc_selrefs: 0x4368
   __DATA.__objc_ivar: 0x638
   __DATA.__objc_data: 0x2580
   __DATA.__data: 0x8d8

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprequelite.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 375C1BF2-F8B9-3165-8742-8F2BE7D34121
-  Functions: 2705
-  Symbols:   601
-  CStrings:  8924
+  UUID: 0BC1BFD9-2F84-35BB-B8B2-EFA1D87B0E62
+  Functions: 2712
+  Symbols:   602
+  CStrings:  8935
 
Symbols:
+ _kLockdownDeviceClassKey
CStrings:
+ "+[MBTemporaryDirectory sharedTemporaryDirectoryForTest:error:]"
+ "+[MBTemporaryDirectory sharedTemporaryDirectoryIdentifiedBy:error:]"
+ "+[MBTemporaryDirectory userTemporaryDirectoryForPersona:identifiedBy:error:]"
+ "+[MBTemporaryDirectory userTemporaryDirectoryForTest:error:]"
+ "AlwaysRestoreSystemFiles"
+ "DeviceClass"
+ "_copyPersonalPreferencesValueForKey:"
+ "copyPersonalPreferencesValueForKey:class:"
+ "currentDeviceClass: %@, sourceDeviceClass not present in backup, using host provided argument for shouldRestoreSystemFiles: %d"
+ "currentDeviceClass: %@, sourceDeviceClass: %@ shouldRestoreSystemFiles: %d"
+ "getPersonalBooleanValueForKey:keyExists:"
+ "iPad"
+ "setPersonalPreferencesValue:forKey:"
+ "sharedTemporaryDirectoryForTest:error:"
+ "sharedTemporaryDirectoryIdentifiedBy:error:"
+ "userTemporaryDirectoryForPersona:identifiedBy:error:"
+ "userTemporaryDirectoryForTest:error:"
- "+[MBTemporaryDirectory sharedTemporaryDirectoryForTest:]"
- "+[MBTemporaryDirectory sharedTemporaryDirectoryIdentifiedBy:]"
- "+[MBTemporaryDirectory userTemporaryDirectoryForPersona:identifiedBy:]"
- "+[MBTemporaryDirectory userTemporaryDirectoryForTest:]"
- "TempDir: Failed to create %s directory (mkdtemp error: %d)"
- "char * _Nullable _mkdtemp(const char *, NSString *__strong, NSError *__autoreleasing *)"
- "sharedTemporaryDirectoryForTest:"
- "sharedTemporaryDirectoryIdentifiedBy:"
- "userTemporaryDirectoryForPersona:identifiedBy:"
- "userTemporaryDirectoryForTest:"

```
