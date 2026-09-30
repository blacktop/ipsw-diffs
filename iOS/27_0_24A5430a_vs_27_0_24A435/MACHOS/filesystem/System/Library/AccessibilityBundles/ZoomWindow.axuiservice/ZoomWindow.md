## ZoomWindow

> `/System/Library/AccessibilityBundles/ZoomWindow.axuiservice/ZoomWindow`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`
- `__DATA.__objc_stublist`

```diff

 909.1.0.0.0
-  __TEXT.__text: 0x6ba38
+  __TEXT.__text: 0x6bcdc
   __TEXT.__auth_stubs: 0x2260
-  __TEXT.__objc_stubs: 0xbc80
-  __TEXT.__objc_methlist: 0x4d60
+  __TEXT.__objc_stubs: 0xbd20
+  __TEXT.__objc_methlist: 0x4d90
   __TEXT.__const: 0x1fc0
-  __TEXT.__objc_methname: 0x113eb
-  __TEXT.__objc_classname: 0x920
+  __TEXT.__objc_methname: 0x1149b
+  __TEXT.__objc_classname: 0x93a
   __TEXT.__objc_methtype: 0x3a81
   __TEXT.__constg_swiftt: 0xd50
   __TEXT.__swift5_typeref: 0x2da0

   __TEXT.__swift5_reflstr: 0x632
   __TEXT.__swift5_builtin: 0x64
   __TEXT.__swift5_assocty: 0x188
-  __TEXT.__oslogstring: 0x920
+  __TEXT.__oslogstring: 0x975
   __TEXT.__cstring: 0x2617
   __TEXT.__swift5_capture: 0x240
   __TEXT.__swift5_proto: 0x64

   __TEXT.__swift_as_ret: 0xc
   __TEXT.__swift_as_cont: 0x10
   __TEXT.__gcc_except_tab: 0x8c0
-  __TEXT.__unwind_info: 0x1a78
+  __TEXT.__unwind_info: 0x1a80
   __TEXT.__eh_frame: 0x420
   __DATA_CONST.__const: 0x1820
   __DATA_CONST.__cfstring: 0x1880
   __DATA_CONST.__objc_classlist: 0x178
   __DATA_CONST.__objc_catlist: 0x18
-  __DATA_CONST.__objc_protolist: 0x110
+  __DATA_CONST.__objc_protolist: 0x118
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x118

   __DATA_CONST.__auth_got: 0x1140
   __DATA_CONST.__got: 0x960
   __DATA_CONST.__auth_ptr: 0x630
-  __DATA.__objc_const: 0x79b8
-  __DATA.__objc_selrefs: 0x3860
+  __DATA.__objc_const: 0x79e0
+  __DATA.__objc_selrefs: 0x3890
   __DATA.__objc_ivar: 0x6a4
   __DATA.__objc_data: 0x19d0
-  __DATA.__data: 0x1ab0
+  __DATA.__data: 0x1b10
   __DATA.__objc_stublist: 0x10
   __DATA.__common: 0x28
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2546
-  Symbols:   4995
-  CStrings:  3282
+  Functions: 2548
+  Symbols:   5007
+  CStrings:  3290
 
Symbols:
+ -[ZWUIServer _activeDisplaySceneIsForegroundActive]
+ -[ZWUIServer activeDisplayDidChangeToDisplayID:]
+ GCC_except_table1127
+ GCC_except_table1145
+ GCC_except_table1192
+ GCC_except_table1236
+ GCC_except_table1265
+ GCC_except_table1361
+ GCC_except_table1531
+ GCC_except_table1542
+ GCC_except_table772
+ GCC_except_table808
+ _AXDeviceIsViridian
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AXUIActiveDisplayObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AXUIActiveDisplayObserver
+ __OBJC_$_PROTOCOL_REFS_AXUIActiveDisplayObserver
+ __OBJC_LABEL_PROTOCOL_$_AXUIActiveDisplayObserver
+ __OBJC_PROTOCOL_$_AXUIActiveDisplayObserver
+ _objc_msgSend$_activeDisplaySceneIsForegroundActive
+ _objc_msgSend$activeDisplayID
+ _objc_msgSend$addActiveDisplayObserver:
+ _objc_msgSend$removeActiveDisplayObserver:
+ _objc_msgSend$shouldPresentUIForWindowScene:
- GCC_except_table1125
- GCC_except_table1143
- GCC_except_table1190
- GCC_except_table1234
- GCC_except_table1255
- GCC_except_table1359
- GCC_except_table1529
- GCC_except_table1540
- GCC_except_table770
- GCC_except_table806
- _objc_retain_x28
CStrings:
+ "AXUIActiveDisplayObserver"
+ "[ActiveDisplay] Active display changed to displayID=%u; reconciling zoom visibility."
+ "_activeDisplaySceneIsForegroundActive"
+ "activeDisplayDidChangeToDisplayID:"
+ "activeDisplayID"
+ "addActiveDisplayObserver:"
+ "removeActiveDisplayObserver:"
+ "shouldPresentUIForWindowScene:"
```
