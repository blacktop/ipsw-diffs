## PasscodePolicy

> `/System/Library/CoreServices/ManagedClient.app/Contents/PlugIns/PasscodePolicy.profileDomainPlugin/Contents/MacOS/PasscodePolicy`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`

```diff

-1842.1.1.0.0
-  __TEXT.__text: 0x8290
-  __TEXT.__auth_stubs: 0x630
+1847.40.6.0.0
+  __TEXT.__text: 0x85f4
+  __TEXT.__auth_stubs: 0x650
   __TEXT.__objc_stubs: 0x9e0
   __TEXT.__objc_methlist: 0x14c
   __TEXT.__const: 0x88
-  __TEXT.__cstring: 0x32fe
-  __TEXT.__oslogstring: 0x1c34
+  __TEXT.__cstring: 0x3427
+  __TEXT.__oslogstring: 0x1d59
   __TEXT.__objc_methname: 0xade
   __TEXT.__objc_classname: 0x56
   __TEXT.__objc_methtype: 0xc5

   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
-  __DATA_CONST.__auth_got: 0x328
+  __DATA_CONST.__auth_got: 0x338
   __DATA_CONST.__got: 0x100
   __DATA_CONST.__auth_ptr: 0x20
   __DATA.__objc_const: 0x320

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 148
-  Symbols:   140
-  CStrings:  407
+  Symbols:   142
+  CStrings:  411
 
Symbols:
+ _class_getName
+ _object_getClassName
Functions:
~ sub_4c20 : 2016 -> 2188
~ sub_5400 -> sub_54ac : 1748 -> 1980
~ sub_5ef8 -> sub_608c : 1176 -> 1640
CStrings:
+ "MergeAllPasscodePolicies kPasscodeMinutesUntilFailedLoginReset ignored - unexpected class '%s'"
+ "MergeAndSetPasscodePolicy kPasscodeMinutesUntilFailedLoginReset skipped: newPolicyValue class '%s', failedAttempts class '%s'"
+ "MergePolicyDictionary ignoring policy key '%s' - expected %s but got %s"
+ "nil"
```
