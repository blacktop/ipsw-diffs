## security

> `/usr/bin/security`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__dof_security_`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`
- `__DATA.__thread_vars`

```diff

-62460.0.38.0.1
-  __TEXT.__text: 0x23020
-  __TEXT.__auth_stubs: 0x1f70
+62460.0.55.0.1
+  __TEXT.__text: 0x23228
+  __TEXT.__auth_stubs: 0x1f80
   __TEXT.__objc_stubs: 0x9a0
   __TEXT.__objc_methlist: 0x128
   __TEXT.__const: 0x840
   __TEXT.__gcc_except_tab: 0xd3c
-  __TEXT.__cstring: 0xc1b6
+  __TEXT.__cstring: 0xc214
   __TEXT.__oslogstring: 0x336
   __TEXT.__objc_methname: 0x6d0
   __TEXT.__objc_classname: 0xe
   __TEXT.__objc_methtype: 0xed
   __TEXT.__dof_security_: 0x2a0
   __TEXT.__unwind_info: 0x830
-  __DATA_CONST.__const: 0x1c50
-  __DATA_CONST.__cfstring: 0xb60
+  __DATA_CONST.__const: 0x1c90
+  __DATA_CONST.__cfstring: 0xbe0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_intobj: 0x60
   __DATA_CONST.__objc_arraydata: 0x40
   __DATA_CONST.__objc_arrayobj: 0x60
-  __DATA_CONST.__auth_got: 0xfd0
-  __DATA_CONST.__got: 0x438
+  __DATA_CONST.__auth_got: 0xfd8
+  __DATA_CONST.__got: 0x468
   __DATA_CONST.__auth_ptr: 0x8
   __DATA.__objc_const: 0x220
   __DATA.__objc_selrefs: 0x2b0

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 434
-  Symbols:   661
-  CStrings:  1238
+  Symbols:   668
+  CStrings:  1243
 
Symbols:
+ _getopt_long
+ _kSecPolicyContext
+ _kSecPolicyIntermediateMarkerOid
+ _kSecPolicyLeafMarkerOid
+ _kSecPolicyPolicyName
+ _kSecPolicyRootDigest
+ _kSecPolicyTeamIdentifier
Functions:
~ sub_100019080 : 3252 -> 3772
CStrings:
+ "1.2.840.113635.100.99.98"
+ "1.2.840.113635.100.99.99"
+ "AAAAAAAAAA"
+ "AnchorBindingTest"
+ "anchor-binding"
```
