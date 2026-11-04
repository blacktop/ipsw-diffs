## dmd

> `/usr/libexec/dmd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-267.0.0.0.0
-  __TEXT.__text: 0x7faac
+269.0.0.0.0
+  __TEXT.__text: 0x7fce8
   __TEXT.__auth_stubs: 0xf60
-  __TEXT.__objc_stubs: 0xea00
+  __TEXT.__objc_stubs: 0xea40
   __TEXT.__objc_methlist: 0x7fdc
   __TEXT.__const: 0x178
   __TEXT.__objc_classname: 0x1e43
-  __TEXT.__objc_methname: 0x118ed
+  __TEXT.__objc_methname: 0x1190f
   __TEXT.__objc_methtype: 0x1d98
-  __TEXT.__cstring: 0x57ff
-  __TEXT.__oslogstring: 0xb69f
-  __TEXT.__gcc_except_tab: 0x10bc
+  __TEXT.__cstring: 0x581c
+  __TEXT.__oslogstring: 0xb6e2
+  __TEXT.__gcc_except_tab: 0x10d4
   __TEXT.__ustring: 0x80a
   __TEXT.__dlopen_cstrs: 0xaf
   __TEXT.__unwind_info: 0x2bf0
-  __DATA_CONST.__const: 0x2748
-  __DATA_CONST.__cfstring: 0x5920
+  __DATA_CONST.__const: 0x2750
+  __DATA_CONST.__cfstring: 0x5940
   __DATA_CONST.__objc_classlist: 0x6f8
   __DATA_CONST.__objc_catlist: 0x1a0
   __DATA_CONST.__objc_protolist: 0x108

   __DATA_CONST.__auth_got: 0x7c0
   __DATA_CONST.__got: 0x13e8
   __DATA.__objc_const: 0x1d6e8
-  __DATA.__objc_selrefs: 0x41c0
+  __DATA.__objc_selrefs: 0x41d0
   __DATA.__objc_ivar: 0x430
   __DATA.__objc_data: 0x45b0
   __DATA.__data: 0xc60

   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsysdiagnose.dylib
-  Functions: 3231
+  Functions: 3232
   Symbols:   926
-  CStrings:  4548
+  CStrings:  4552
 
Symbols:
+ _MOEffectiveSettingsGroupApplication
- _MOScreenTimeShieldPolicyBlocked
CStrings:
+ "Skipping launch restricted application without a bundle identifier"
+ "application"
+ "applicationsexcludingblocked"
+ "launchRestrictedApplications"
+ "setByAddingObject:"
- "applicationShieldPolicies"
```
