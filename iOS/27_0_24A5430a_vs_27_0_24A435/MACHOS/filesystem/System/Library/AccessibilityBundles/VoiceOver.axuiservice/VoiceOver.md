## VoiceOver

> `/System/Library/AccessibilityBundles/VoiceOver.axuiservice/VoiceOver`

### Sections with Same Size but Changed Content

- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_assocty`
- `__TEXT.__objc_methtype`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_protos`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`
- `__DATA.__objc_stublist`

```diff

 2478.2.0.0.0
-  __TEXT.__text: 0x25048
-  __TEXT.__auth_stubs: 0x13d0
-  __TEXT.__objc_stubs: 0x4b40
-  __TEXT.__objc_methlist: 0x1dfc
+  __TEXT.__text: 0x255d8
+  __TEXT.__auth_stubs: 0x13e0
+  __TEXT.__objc_stubs: 0x4c40
+  __TEXT.__objc_methlist: 0x1e44
   __TEXT.__dlopen_cstrs: 0x5e
-  __TEXT.__const: 0xc90
-  __TEXT.__objc_classname: 0x626
-  __TEXT.__objc_methname: 0x6e76
+  __TEXT.__const: 0xca0
+  __TEXT.__objc_classname: 0x640
+  __TEXT.__objc_methname: 0x6f76
   __TEXT.__constg_swiftt: 0xaa4
   __TEXT.__swift5_typeref: 0x10ce
   __TEXT.__swift5_reflstr: 0x413
   __TEXT.__swift5_fieldmd: 0x4e8
   __TEXT.__swift5_proto: 0x80
   __TEXT.__swift5_types: 0x44
-  __TEXT.__cstring: 0x137a
+  __TEXT.__cstring: 0x1389
   __TEXT.__swift5_assocty: 0x98
   __TEXT.__objc_methtype: 0x1de8
   __TEXT.__swift5_capture: 0x198
-  __TEXT.__oslogstring: 0x251
+  __TEXT.__oslogstring: 0x2e7
   __TEXT.__swift_as_entry: 0x1c
   __TEXT.__swift_as_ret: 0x10
   __TEXT.__swift_as_cont: 0x2c
   __TEXT.__swift5_protos: 0xc
-  __TEXT.__gcc_except_tab: 0x250
-  __TEXT.__unwind_info: 0x9d8
+  __TEXT.__gcc_except_tab: 0x25c
+  __TEXT.__unwind_info: 0x9e8
   __TEXT.__eh_frame: 0x4a0
   __DATA_CONST.__const: 0x2040
   __DATA_CONST.__cfstring: 0xcc0
   __DATA_CONST.__objc_classlist: 0x120
-  __DATA_CONST.__objc_protolist: 0xa0
+  __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0xa0
   __DATA_CONST.__objc_intobj: 0x150
   __DATA_CONST.__objc_arraydata: 0x38
   __DATA_CONST.__objc_arrayobj: 0x30
-  __DATA_CONST.__auth_got: 0x9f8
+  __DATA_CONST.__auth_got: 0xa00
   __DATA_CONST.__got: 0x4b0
   __DATA_CONST.__auth_ptr: 0x2f8
-  __DATA.__objc_const: 0x3898
-  __DATA.__objc_selrefs: 0x1a20
+  __DATA.__objc_const: 0x38c0
+  __DATA.__objc_selrefs: 0x1a68
   __DATA.__objc_ivar: 0x200
   __DATA.__objc_data: 0xae0
-  __DATA.__data: 0x1648
+  __DATA.__data: 0x16a8
   __DATA.__objc_stublist: 0x8
   __DATA.__common: 0x28
   - /System/Library/Frameworks/AVRouting.framework/AVRouting

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 833
-  Symbols:   414
-  CStrings:  1496
+  Functions: 837
+  Symbols:   415
+  CStrings:  1510
 
Symbols:
+ _AXDeviceIsViridian
CStrings:
+ "AXUIActiveDisplayObserver"
+ "Hiding"
+ "Showing"
+ "[ActiveDisplay] %{public}s VoiceOver UI on displayID=%@."
+ "[ActiveDisplay] Active display changed to displayID=%u; reconciling VoiceOver UI visibility."
+ "_activeDisplaySceneIsForegroundActive"
+ "_reconcileDisplayVisibility"
+ "_setVoiceOverUIHidden:forScene:"
+ "activationState"
+ "activeDisplayDidChangeToDisplayID:"
+ "activeDisplayID"
+ "addActiveDisplayObserver:"
+ "removeActiveDisplayObserver:"
+ "shouldPresentUIForWindowScene:"
```
