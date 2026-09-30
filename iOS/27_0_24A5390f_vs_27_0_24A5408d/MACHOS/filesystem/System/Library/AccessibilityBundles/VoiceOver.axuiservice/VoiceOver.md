## VoiceOver

> `/System/Library/AccessibilityBundles/VoiceOver.axuiservice/VoiceOver`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_proto`
- `__TEXT.__cstring`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_protos`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`
- `__DATA.__objc_stublist`

```diff

-2475.0.0.0.0
-  __TEXT.__text: 0x24fd0
-  __TEXT.__auth_stubs: 0x13c0
-  __TEXT.__objc_stubs: 0x4b60
+2478.0.0.0.0
+  __TEXT.__text: 0x25048
+  __TEXT.__auth_stubs: 0x13d0
+  __TEXT.__objc_stubs: 0x4b40
   __TEXT.__objc_methlist: 0x1dfc
   __TEXT.__dlopen_cstrs: 0x5e
-  __TEXT.__const: 0xc80
+  __TEXT.__const: 0xc90
   __TEXT.__objc_classname: 0x626
-  __TEXT.__objc_methname: 0x6e56
+  __TEXT.__objc_methname: 0x6e76
   __TEXT.__constg_swiftt: 0xaa4
   __TEXT.__swift5_typeref: 0x10ce
   __TEXT.__swift5_reflstr: 0x413

   __TEXT.__swift5_assocty: 0x98
   __TEXT.__objc_methtype: 0x1de8
   __TEXT.__swift5_capture: 0x198
-  __TEXT.__oslogstring: 0x10d
+  __TEXT.__oslogstring: 0x251
   __TEXT.__swift_as_entry: 0x1c
   __TEXT.__swift_as_ret: 0x10
   __TEXT.__swift_as_cont: 0x2c
   __TEXT.__swift5_protos: 0xc
   __TEXT.__gcc_except_tab: 0x250
-  __TEXT.__unwind_info: 0x9e0
+  __TEXT.__unwind_info: 0x9d8
   __TEXT.__eh_frame: 0x4a0
   __DATA_CONST.__const: 0x2040
   __DATA_CONST.__cfstring: 0xcc0

   __DATA_CONST.__objc_intobj: 0x150
   __DATA_CONST.__objc_arraydata: 0x38
   __DATA_CONST.__objc_arrayobj: 0x30
-  __DATA_CONST.__auth_got: 0x9f0
+  __DATA_CONST.__auth_got: 0x9f8
   __DATA_CONST.__got: 0x4b0
   __DATA_CONST.__auth_ptr: 0x2f8
-  __DATA.__objc_const: 0x3878
+  __DATA.__objc_const: 0x3898
   __DATA.__objc_selrefs: 0x1a20
-  __DATA.__objc_ivar: 0x1fc
+  __DATA.__objc_ivar: 0x200
   __DATA.__objc_data: 0xae0
   __DATA.__data: 0x1648
   __DATA.__objc_stublist: 0x8

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 833
-  Symbols:   413
-  CStrings:  1491
+  Symbols:   414
+  CStrings:  1496
 
Symbols:
+ _VOTLogLifeCycle
Functions:
~ sub_8a1c : 332 -> 448
~ sub_8d5c -> sub_8dd0 : 272 -> 8
~ sub_8e6c -> sub_8dd8 : 364 -> 444
~ sub_a2e8 -> sub_a2a4 : 652 -> 720
~ sub_12f20 : 336 -> 456
CStrings:
+ "Adding screen curtain view controller for scene (displayID=%@), current commanded state=%d"
+ "Removing screen curtain view controller for scene, commanded state (_screenCurtainEnabled=%d) unchanged"
+ "VOTUIScreenCurtainViewController setEnabled: %d -> %d (animate=%d)"
+ "_handleScreenCurtainEnabled:%d (%lu curtain view controllers)"
+ "_screenCurtainEnabled"
```
