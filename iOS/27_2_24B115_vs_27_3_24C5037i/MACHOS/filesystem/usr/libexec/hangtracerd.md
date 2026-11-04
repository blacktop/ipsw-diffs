## hangtracerd

> `/usr/libexec/hangtracerd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-430.0.0.0.0
-  __TEXT.__text: 0x36880
-  __TEXT.__auth_stubs: 0xfb0
-  __TEXT.__objc_stubs: 0x5d00
+430.1.0.0.0
+  __TEXT.__text: 0x37ea4
+  __TEXT.__auth_stubs: 0xfd0
+  __TEXT.__objc_stubs: 0x5da0
   __TEXT.__objc_methlist: 0x28a4
-  __TEXT.__const: 0x430
-  __TEXT.__cstring: 0x4dde
-  __TEXT.__objc_methname: 0x9c9a
+  __TEXT.__const: 0x400
+  __TEXT.__cstring: 0x4e92
+  __TEXT.__objc_methname: 0x9cfc
   __TEXT.__objc_classname: 0x37d
   __TEXT.__objc_methtype: 0x1355
   __TEXT.__gcc_except_tab: 0x450
-  __TEXT.__oslogstring: 0x69bc
-  __TEXT.__unwind_info: 0x1040
-  __DATA_CONST.__const: 0x2260
-  __DATA_CONST.__cfstring: 0x6560
+  __TEXT.__oslogstring: 0x6c9e
+  __TEXT.__unwind_info: 0x1088
+  __DATA_CONST.__const: 0x2338
+  __DATA_CONST.__cfstring: 0x6680
   __DATA_CONST.__objc_classlist: 0x128
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arraydata: 0x90
   __DATA_CONST.__objc_dictobj: 0x78
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA_CONST.__auth_got: 0x7e8
+  __DATA_CONST.__auth_got: 0x7f8
   __DATA_CONST.__got: 0x490
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA.__objc_const: 0x5af0
-  __DATA.__objc_selrefs: 0x1f18
-  __DATA.__objc_ivar: 0x52c
+  __DATA.__objc_const: 0x5b10
+  __DATA.__objc_selrefs: 0x1f40
+  __DATA.__objc_ivar: 0x530
   __DATA.__objc_data: 0xb90
   __DATA.__data: 0x548
   __DATA.__common: 0x70

   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
-  Functions: 1396
-  Symbols:   403
-  CStrings:  3175
+  Functions: 1411
+  Symbols:   405
+  CStrings:  3199
 
Symbols:
+ _NSStringFromRBSRole
+ ___exp10
CStrings:
+ "Failed to create state info JSON blob for hang (start %llu, end %llu, state info %@). Returning 0ms background duration."
+ "Failed to parse State info dictionary object from sorted array '%@', object is type of class '%@'"
+ "Failed to parse State info dictionary object of key '%@' from sorted array '%@', object is type of class '%@'"
+ "Hang %{public}@ detected: %.2fs (Siri AI in background CPU role with no visible UI, ignoring)"
+ "Invalid timestamp(s) of class '%@' and '%@' found in dictionary during sorting."
+ "No states were present in the state info array before a hang occurred."
+ "Object in state info array is not a dictionary. Is kind of class %@"
+ "The provided stateInfoArray '%@' only has state objects AFTER then end of the hang (%llu matu)."
+ "com.apple.campo"
+ "cpuRoleBreakdown"
+ "cpuRoleName"
+ "endCPURole"
+ "intervalsInCPURole"
+ "isSiriAIProcess"
+ "lastObject"
+ "mutableCopy"
+ "numberWithUnsignedLong:"
+ "percentInCPURole"
+ "secondsSinceCPURoleTransitionBeforeHangStart"
+ "setValue:forKey:"
+ "startCPURole"
+ "timeInCPURole"
+ "unsignedCharValue"
+ "v32@?0@8@16^B24"
```
