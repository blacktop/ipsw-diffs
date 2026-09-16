## managedappsd

> `/usr/libexec/managedappsd`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_entry`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA.__objc_selrefs`

```diff

-113.2.5.0.0
-  __TEXT.__text: 0x112c
-  __TEXT.__auth_stubs: 0x300
+113.40.17.0.0
+  __TEXT.__text: 0x12f0
+  __TEXT.__auth_stubs: 0x360
   __TEXT.__objc_stubs: 0x60
-  __TEXT.__const: 0x52
-  __TEXT.__oslogstring: 0x63
+  __TEXT.__const: 0x62
+  __TEXT.__oslogstring: 0x93
+  __TEXT.__swift5_typeref: 0x15
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__swift5_typeref: 0xd
   __TEXT.__cstring: 0x16
   __TEXT.__objc_methname: 0x37
   __TEXT.__unwind_info: 0xa8
   __TEXT.__eh_frame: 0x48
   __DATA_CONST.__const: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__auth_got: 0x188
-  __DATA_CONST.__got: 0x28
-  __DATA_CONST.__auth_ptr: 0x18
+  __DATA_CONST.__auth_got: 0x1b8
+  __DATA_CONST.__got: 0x30
+  __DATA_CONST.__auth_ptr: 0x20
   __DATA.__objc_selrefs: 0x18
-  __DATA.__data: 0x10
+  __DATA.__data: 0x18
   __DATA.__common: 0x60
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   Functions: 16
-  Symbols:   68
-  CStrings:  8
+  Symbols:   76
+  CStrings:  9
 
Symbols:
+ _$sSS10describingSSx_tclufC
+ _$sSo13os_log_type_ta0A0E5faultABvgZ
+ _$ss5ErrorMp
+ _$sypN
+ _exit
+ _objc_release_x26
+ _swift_arrayDestroy
+ _swift_errorRelease
+ _swift_errorRetain
- _swift_errorInMain
Functions:
~ sub_100000d60 : 1772 -> 2224
~ sub_100001cc0 -> sub_100001e84 : 48 -> 84
~ sub_100001cf0 -> sub_100001ed8 : 84 -> 48
CStrings:
+ "%s failed to set up services: %{public}s"
```
