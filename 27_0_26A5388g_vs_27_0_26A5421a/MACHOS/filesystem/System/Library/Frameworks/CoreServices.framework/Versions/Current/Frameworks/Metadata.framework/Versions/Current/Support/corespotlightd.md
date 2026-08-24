## corespotlightd

> `/System/Library/Frameworks/CoreServices.framework/Versions/Current/Frameworks/Metadata.framework/Versions/Current/Support/corespotlightd`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-2454.100.0.0.0
-  __TEXT.__text: 0x9c2c
-  __TEXT.__auth_stubs: 0xd90
-  __TEXT.__objc_stubs: 0xa80
+2459.405.0.0.0
+  __TEXT.__text: 0x9c74
+  __TEXT.__auth_stubs: 0xda0
+  __TEXT.__objc_stubs: 0xaa0
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0x6ac
   __TEXT.__const: 0xf0
   __TEXT.__cstring: 0x1419
   __TEXT.__oslogstring: 0xb30
   __TEXT.__gcc_except_tab: 0xa4
-  __TEXT.__objc_methname: 0xe17
+  __TEXT.__objc_methname: 0xe2d
   __TEXT.__objc_classname: 0x8e
   __TEXT.__objc_methtype: 0x47d
-  __TEXT.__unwind_info: 0x3c0
+  __TEXT.__unwind_info: 0x3c8
   __DATA_CONST.__const: 0xe28
   __DATA_CONST.__cfstring: 0xc40
   __DATA_CONST.__objc_classlist: 0x28

   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_arraydata: 0x28
   __DATA_CONST.__objc_arrayobj: 0x30
-  __DATA_CONST.__auth_got: 0x6d8
-  __DATA_CONST.__got: 0x180
+  __DATA_CONST.__auth_got: 0x6e0
+  __DATA_CONST.__got: 0x188
   __DATA_CONST.__auth_ptr: 0x8
   __DATA.__objc_const: 0x778
-  __DATA.__objc_selrefs: 0x498
+  __DATA.__objc_selrefs: 0x4a0
   __DATA.__objc_ivar: 0x38
   __DATA.__objc_data: 0x190
   __DATA.__data: 0x8b0

   - /System/Library/PrivateFrameworks/MetadataUtilities.framework/Versions/A/MetadataUtilities
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/Versions/A/MobileKeyBag
   - /System/Library/PrivateFrameworks/ServerInformation.framework/Versions/A/ServerInformation
+  - /System/Library/PrivateFrameworks/SetupAssistantFramework.framework/Versions/A/SetupAssistantFramework
   - /System/Library/PrivateFrameworks/SpotlightDaemon.framework/Versions/A/SpotlightDaemon
   - /System/Library/PrivateFrameworks/SpotlightIndex.framework/Versions/A/SpotlightIndex
   - /System/Library/PrivateFrameworks/SpotlightResources.framework/Versions/A/SpotlightResources

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 376
-  Symbols:   278
-  CStrings:  558
+  Symbols:   280
+  CStrings:  559
 
Symbols:
+ _OBJC_CLASS_$_SAUserSetupState
+ _getuid
Functions:
~ sub_1000040c8 -> sub_100004150 : 8 -> 80
CStrings:
+ "getSetupStateForUser:"
```
