## CarPlaySetup

> `/Applications/CarPlaySetup.app/CarPlaySetup`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-799.3.0.0.0
-  __TEXT.__text: 0x77c4
-  __TEXT.__auth_stubs: 0x3a0
-  __TEXT.__objc_stubs: 0x12a0
+807.2.0.0.0
+  __TEXT.__text: 0x7bd8
+  __TEXT.__auth_stubs: 0x3d0
+  __TEXT.__objc_stubs: 0x1320
   __TEXT.__objc_methlist: 0xc40
   __TEXT.__const: 0x68
-  __TEXT.__objc_methname: 0x2c11
-  __TEXT.__cstring: 0x1b1
-  __TEXT.__oslogstring: 0xc6d
+  __TEXT.__objc_methname: 0x2c8b
+  __TEXT.__cstring: 0x1e6
+  __TEXT.__oslogstring: 0xccc
   __TEXT.__objc_classname: 0x1af
   __TEXT.__objc_methtype: 0x11b9
-  __TEXT.__gcc_except_tab: 0x44
-  __TEXT.__unwind_info: 0x318
-  __DATA_CONST.__const: 0x428
+  __TEXT.__gcc_except_tab: 0xa0
+  __TEXT.__unwind_info: 0x338
+  __DATA_CONST.__const: 0x478
   __DATA_CONST.__cfstring: 0x160
   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x28
-  __DATA_CONST.__auth_got: 0x1e0
-  __DATA_CONST.__got: 0x178
+  __DATA_CONST.__auth_got: 0x1f8
+  __DATA_CONST.__got: 0x188
   __DATA.__objc_const: 0x1888
-  __DATA.__objc_selrefs: 0x8b0
+  __DATA.__objc_selrefs: 0x8d0
   __DATA.__objc_ivar: 0x3c
   __DATA.__objc_data: 0x2d0
   __DATA.__data: 0x3c0

   - /System/Library/PrivateFrameworks/SpringBoardUIServices.framework/SpringBoardUIServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 190
-  Symbols:   122
-  CStrings:  563
+  Functions: 193
+  Symbols:   127
+  CStrings:  569
 
Symbols:
+ _OBJC_CLASS_$_UITraitHorizontalSizeClass
+ _OBJC_CLASS_$_UITraitVerticalSizeClass
+ _objc_release_x25
+ _objc_retain_x24
+ _objc_unsafeClaimAutoreleasedReturnValue
CStrings:
+ "horizontalSizeClass"
+ "onboarding prompt confirmed, proceeding to car key setup: %{public}@"
+ "presenter deallocated before onboarding was confirmed"
+ "registerForTraitChanges:withHandler:"
+ "setNeedsUpdateOfSupportedInterfaceOrientations"
+ "v24@?0@\"<UITraitEnvironment>\"8@\"UITraitCollection\"16"
+ "verticalSizeClass"
- "Onboarding prompt confirmed"
```
