## AppStoreDaemon

> `/System/Library/PrivateFrameworks/AppStoreDaemon.framework/AppStoreDaemon`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-13.0.40.0.0
-  __TEXT.__text: 0x838d4
-  __TEXT.__objc_methlist: 0xb3b4
+13.0.43.0.0
+  __TEXT.__text: 0x83b58
+  __TEXT.__objc_methlist: 0xb3cc
   __TEXT.__const: 0x3d8
   __TEXT.__dlopen_cstrs: 0x5b
-  __TEXT.__cstring: 0x5948
+  __TEXT.__cstring: 0x5960
   __TEXT.__constg_swiftt: 0x7c
   __TEXT.__swift5_typeref: 0x61
   __TEXT.__swift5_builtin: 0x28

   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__oslogstring: 0x4d86
   __TEXT.__gcc_except_tab: 0xb60
-  __TEXT.__unwind_info: 0x27c0
+  __TEXT.__unwind_info: 0x27c8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x210
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x45c0
+  __DATA_CONST.__objc_selrefs: 0x45d0
   __DATA_CONST.__objc_protorefs: 0x158
   __DATA_CONST.__objc_superrefs: 0x4a8
   __DATA_CONST.__objc_arraydata: 0xc8
-  __DATA_CONST.__got: 0x628
+  __DATA_CONST.__got: 0x630
   __AUTH_CONST.__const: 0x8e0
-  __AUTH_CONST.__cfstring: 0x6d60
-  __AUTH_CONST.__objc_const: 0x164a8
+  __AUTH_CONST.__cfstring: 0x6e00
+  __AUTH_CONST.__objc_const: 0x164d8
   __AUTH_CONST.__objc_intobj: 0xc0
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__auth_got: 0x610
   __AUTH.__objc_data: 0x1680
-  __DATA.__objc_ivar: 0xdf8
+  __DATA.__objc_ivar: 0xdfc
   __DATA.__data: 0x18f8
   __DATA.__bss: 0x310
   __DATA_DIRTY.__objc_ivar: 0x18c

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 4482
-  Symbols:   8912
-  CStrings:  1422
+  Functions: 4487
+  Symbols:   8920
+  CStrings:  1426
 
Symbols:
+ -[ASDTestFlightPackageMetadata diskSpaceMetadata]
+ -[ASDTestFlightPackageMetadata setDiskSpaceMetadata:]
+ _ASDDebugConfigureFileLogging
+ _ASDDebugFileFormatFromOSLogFormat
+ _ASDDebugLogOSStyle
+ _OBJC_IVAR_$_ASDTestFlightPackageMetadata._diskSpaceMetadata
+ _objc_msgSend$setLogDirectoryPath:
+ _objc_msgSend$setLogFileBaseName:
CStrings:
+ "%"
+ "%\\{[^}]*\\}"
+ "DM"
+ "Logs"
```
