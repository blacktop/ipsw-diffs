## softwareupdate

> `/usr/sbin/softwareupdate`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-2412.1.1.0.0
-  __TEXT.__text: 0xa204
-  __TEXT.__auth_stubs: 0x530
+2412.40.11.0.0
+  __TEXT.__text: 0xa198
+  __TEXT.__auth_stubs: 0x510
   __TEXT.__objc_stubs: 0x1d00
   __TEXT.__objc_methlist: 0x72c
   __TEXT.__const: 0x68
-  __TEXT.__gcc_except_tab: 0x1c0
-  __TEXT.__oslogstring: 0xa1b
-  __TEXT.__cstring: 0x22bb
+  __TEXT.__gcc_except_tab: 0x1b8
+  __TEXT.__oslogstring: 0xa2b
+  __TEXT.__cstring: 0x2270
   __TEXT.__objc_methname: 0x2371
   __TEXT.__objc_classname: 0xcd
   __TEXT.__objc_methtype: 0x893
   __TEXT.__unwind_info: 0x428
   __DATA_CONST.__const: 0xb60
-  __DATA_CONST.__cfstring: 0x700
+  __DATA_CONST.__cfstring: 0x6c0
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x18
   __DATA_CONST.__objc_intobj: 0x30
-  __DATA_CONST.__auth_got: 0x2a8
+  __DATA_CONST.__auth_got: 0x298
   __DATA_CONST.__got: 0x240
   __DATA_CONST.__auth_ptr: 0x8
   __DATA.__objc_const: 0xa88

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 257
-  Symbols:   166
-  CStrings:  712
+  Symbols:   164
+  CStrings:  710
 
Symbols:
+ _OBJC_CLASS_$_SUOSUScanOptions
- _CFPreferencesAppValueIsForced
- _CFPreferencesGetAppBooleanValue
- _OBJC_CLASS_$_SUOSUMSUScanOptions
Functions:
~ sub_100002d44 : 1312 -> 1204
CStrings:
+ "%@: Requiring admin authorization prompt for standard user because admin install is required"
- "%@: Requiring admin authorization prompt for standard user because %s is set"
- "com.apple.SoftwareUpdate"
- "restrict-software-update-require-admin-to-install"
```
