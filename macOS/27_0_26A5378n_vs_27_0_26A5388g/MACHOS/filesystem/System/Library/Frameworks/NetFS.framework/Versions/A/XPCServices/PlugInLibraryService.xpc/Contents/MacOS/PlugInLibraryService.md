## PlugInLibraryService

> `/System/Library/Frameworks/NetFS.framework/Versions/A/XPCServices/PlugInLibraryService.xpc/Contents/MacOS/PlugInLibraryService`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__cstring`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-70.0.0.0.0
-  __TEXT.__text: 0xc424
-  __TEXT.__auth_stubs: 0xaf0
-  __TEXT.__objc_stubs: 0x580
+71.0.0.0.0
+  __TEXT.__text: 0xc560
+  __TEXT.__auth_stubs: 0xb20
+  __TEXT.__objc_stubs: 0x5e0
   __TEXT.__objc_methlist: 0x2c8
   __TEXT.__const: 0x98
   __TEXT.__objc_classname: 0x61
-  __TEXT.__objc_methname: 0x674
+  __TEXT.__objc_methname: 0x6a8
   __TEXT.__objc_methtype: 0x3c4
   __TEXT.__oslogstring: 0x886
   __TEXT.__cstring: 0x128d

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA_CONST.__auth_got: 0x588
-  __DATA_CONST.__got: 0xd8
+  __DATA_CONST.__auth_got: 0x5a0
+  __DATA_CONST.__got: 0xe8
   __DATA_CONST.__auth_ptr: 0x8
   __DATA.__objc_const: 0x6b0
-  __DATA.__objc_selrefs: 0x280
+  __DATA.__objc_selrefs: 0x298
   __DATA.__objc_ivar: 0xc
   __DATA.__objc_data: 0xa0
   __DATA.__data: 0x374

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 228
-  Symbols:   323
-  CStrings:  357
+  Symbols:   328
+  CStrings:  360
 
Symbols:
+ _OBJC_CLASS_$_NSNumber
+ __DefaultRuneLocale
+ ___maskrune
+ _objc_opt_class
+ _objc_opt_isKindOfClass
Functions:
~ sub_100001d8c : 548 -> 732
~ sub_10000208c -> sub_100002144 : 456 -> 588
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.IiBXAl/Sources/NetFSFramework/URLMount.c"
+ "mutableCopy"
+ "numberWithUnsignedInt:"
+ "unsignedIntValue"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.kMbYgZ/Sources/NetFSFramework/URLMount.c"
```
