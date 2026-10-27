## security

> `/usr/bin/security`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__dof_security_`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`
- `__DATA.__thread_vars`

```diff

-62460.1.3.0.0
-  __TEXT.__text: 0x22f14
+62460.40.78.0.0
+  __TEXT.__text: 0x22ec4
   __TEXT.__auth_stubs: 0x1f80
   __TEXT.__objc_stubs: 0x9a0
   __TEXT.__objc_methlist: 0x128

   __DATA_CONST.__objc_arraydata: 0x40
   __DATA_CONST.__objc_arrayobj: 0x60
   __DATA_CONST.__auth_got: 0xfd8
-  __DATA_CONST.__got: 0x468
+  __DATA_CONST.__got: 0x470
   __DATA_CONST.__auth_ptr: 0x8
   __DATA.__objc_const: 0x220
   __DATA.__objc_selrefs: 0x2b0

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 434
-  Symbols:   668
+  Symbols:   669
   CStrings:  1243
 
Symbols:
+ _kSecPolicyAppleGenericApplePinned
+ _kSecPolicyAppleGenericAppleSSLPinned
- _kSecPolicyRootDigest
Functions:
~ sub_100018fdc : 3772 -> 3692
```
