## managedappsd

> `/usr/libexec/managedappsd`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_entry`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA.__objc_selrefs`

```diff

-113.1.9.0.0
-  __TEXT.__text: 0x1160
-  __TEXT.__auth_stubs: 0x2c0
+113.40.17.0.0
+  __TEXT.__text: 0x1318
+  __TEXT.__auth_stubs: 0x310
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
   __DATA_CONST.__const: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__auth_got: 0x168
-  __DATA_CONST.__got: 0x28
-  __DATA_CONST.__auth_ptr: 0x18
+  __DATA_CONST.__auth_got: 0x190
+  __DATA_CONST.__got: 0x30
+  __DATA_CONST.__auth_ptr: 0x20
   __DATA.__objc_selrefs: 0x18
-  __DATA.__data: 0x10
+  __DATA.__data: 0x18
   __DATA.__common: 0x60
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   Functions: 16
-  Symbols:   65
-  CStrings:  8
+  Symbols:   72
+  CStrings:  9
 
Symbols:
+ _$sSS10describingSSx_tclufC
+ _$sSo13os_log_type_ta0A0E5faultABvgZ
+ _$ss5ErrorMp
+ _$sypN
+ _exit
+ _swift_arrayDestroy
+ _swift_errorRelease
+ _swift_errorRetain
- _swift_errorInMain
Functions:
~ sub_100000de0 : 1808 -> 2248
~ sub_100001d74 -> sub_100001f2c : 48 -> 84
~ sub_100001da4 -> sub_100001f80 : 84 -> 48
CStrings:
+ "%s failed to set up services: %{public}s"
```
