## uarpd

> `/usr/libexec/uarpd`

### Sections with Same Size but Changed Content

- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1587.40.33.0.0
-  __TEXT.__text: 0xa4830
-  __TEXT.__auth_stubs: 0xa90
-  __TEXT.__objc_stubs: 0xad00
-  __TEXT.__objc_methlist: 0x8a00
-  __TEXT.__objc_methname: 0xfad0
+1587.60.11.0.0
+  __TEXT.__text: 0xa49a8
+  __TEXT.__auth_stubs: 0xab0
+  __TEXT.__objc_stubs: 0xad60
+  __TEXT.__objc_methlist: 0x8a40
+  __TEXT.__objc_methname: 0xfb46
   __TEXT.__objc_classname: 0x1d25
-  __TEXT.__cstring: 0xb6ee
+  __TEXT.__cstring: 0xb6fd
   __TEXT.__objc_methtype: 0x2b3a
   __TEXT.__const: 0x138
   __TEXT.__gcc_except_tab: 0x1ec
-  __TEXT.__oslogstring: 0x98fd
-  __TEXT.__unwind_info: 0x32d8
+  __TEXT.__oslogstring: 0x991b
+  __TEXT.__unwind_info: 0x32e0
   __DATA_CONST.__const: 0x1108
-  __DATA_CONST.__cfstring: 0x5700
+  __DATA_CONST.__cfstring: 0x5720
   __DATA_CONST.__objc_classlist: 0x610
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x70

   __DATA_CONST.__objc_arraydata: 0x70
   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA_CONST.__auth_got: 0x558
+  __DATA_CONST.__auth_got: 0x568
   __DATA_CONST.__got: 0x668
-  __DATA.__objc_const: 0x10a48
-  __DATA.__objc_selrefs: 0x3370
-  __DATA.__objc_ivar: 0xb88
+  __DATA.__objc_const: 0x10ab0
+  __DATA.__objc_selrefs: 0x3390
+  __DATA.__objc_ivar: 0xb90
   __DATA.__objc_data: 0x3ca0
   __DATA.__data: 0x548
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libpcap.A.dylib
-  Functions: 4030
-  Symbols:   241
-  CStrings:  5114
+  Functions: 4036
+  Symbols:   243
+  CStrings:  5123
 
Symbols:
+ _AMAuthInstallSsoSetStealthMode
+ _AMAuthInstallSsoSetToken
CStrings:
+ "AudioAccessory"
+ "T@\"NSData\",&,V_ssoToken"
+ "T@\"NSData\",R,V_ssoToken"
+ "UARP: Failed to set SSO token"
+ "_ssoToken"
+ "initWithSSOToken:"
+ "requiresStealthMode"
+ "setSsoToken:"
+ "ssoToken"
```
