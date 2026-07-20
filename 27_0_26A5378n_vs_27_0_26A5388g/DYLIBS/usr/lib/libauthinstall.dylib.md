## libauthinstall.dylib

> `/usr/lib/libauthinstall.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__cstring`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__weak_got`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__AUTH.__thread_vars`
- `__DATA.__objc_classrefs`
- `__DATA.__objc_superrefs`
- `__DATA.__data`
- `__DATA_DIRTY.__data`

```diff

-1155.0.3.0.0
-  __TEXT.__text: 0xb19bc
+1155.0.4.0.0
+  __TEXT.__text: 0xb1c90
   __TEXT.__objc_methlist: 0x262c
   __TEXT.__cstring: 0x21a59
-  __TEXT.__const: 0xc1db
-  __TEXT.__gcc_except_tab: 0x3a78
+  __TEXT.__const: 0xc23b
+  __TEXT.__gcc_except_tab: 0x3af8
   __TEXT.__dlopen_cstrs: 0x63
   __TEXT.__oslogstring: 0xad5
-  __TEXT.__unwind_info: 0x2910
+  __TEXT.__unwind_info: 0x2938
   __TEXT.__eh_frame: 0x7c
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __AUTH_CONST.__cfstring: 0xf120
   __AUTH_CONST.__objc_const: 0x4908
   __AUTH_CONST.__weak_auth_got: 0x20
-  __AUTH_CONST.__auth_got: 0xd98
+  __AUTH_CONST.__auth_got: 0xda0
   __AUTH.__objc_data: 0x13b0
   __AUTH.__data: 0x20
   __AUTH.__thread_vars: 0x18

   - /usr/lib/libz.1.dylib
   - /usr/lib/updaters/libAppleTconUARPUpdater.dylib
   - /usr/lib/updaters/libT200Updater.dylib
-  Functions: 3814
-  Symbols:   5403
+  Functions: 3813
+  Symbols:   5405
   CStrings:  4818
 
Symbols:
+ _AMAuthInstallErrorFromAMSupportError
+ __ZN11ACFULogging14getUpdaterNameEv
+ __ZNSt3__1plIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_12basic_stringIT_T0_T1_EEPKS6_RKS9_
- _ZN9ACFUError10getCFErrorEv
CStrings:
+ "Helsinki_Restore_Host-58.0.44"
+ "libauthinstall-1155.0.4"
- "Helsinki_Restore_Host-58.0.42"
- "libauthinstall-1155.0.3"
```
