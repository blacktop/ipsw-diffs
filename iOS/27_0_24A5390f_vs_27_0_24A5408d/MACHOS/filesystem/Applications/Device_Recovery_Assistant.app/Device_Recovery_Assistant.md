## Device Recovery Assistant

> `/Applications/Device Recovery Assistant.app/Device Recovery Assistant`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_data`

```diff

-149.0.0.0.0
-  __TEXT.__text: 0x1e4c0
-  __TEXT.__auth_stubs: 0x830
-  __TEXT.__objc_stubs: 0x6180
-  __TEXT.__objc_methlist: 0x2d38
-  __TEXT.__cstring: 0x35aa
+150.0.2.0.0
+  __TEXT.__text: 0x1e77c
+  __TEXT.__auth_stubs: 0x840
+  __TEXT.__objc_stubs: 0x6220
+  __TEXT.__objc_methlist: 0x2d90
   __TEXT.__const: 0xa8
-  __TEXT.__objc_methname: 0x8928
-  __TEXT.__oslogstring: 0x35a0
+  __TEXT.__objc_methname: 0x8b1c
+  __TEXT.__oslogstring: 0x35e9
+  __TEXT.__cstring: 0x35b5
   __TEXT.__objc_classname: 0x689
-  __TEXT.__objc_methtype: 0x2551
+  __TEXT.__objc_methtype: 0x257a
   __TEXT.__gcc_except_tab: 0x118
   __TEXT.__ustring: 0x18
-  __TEXT.__unwind_info: 0x6e0
-  __DATA_CONST.__const: 0xa18
+  __TEXT.__unwind_info: 0x6f8
+  __DATA_CONST.__const: 0xa08
   __DATA_CONST.__cfstring: 0x1960
   __DATA_CONST.__objc_classlist: 0x118
   __DATA_CONST.__objc_protolist: 0x110
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x108
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA_CONST.__auth_got: 0x428
+  __DATA_CONST.__auth_got: 0x430
   __DATA_CONST.__got: 0x4c0
-  __DATA.__objc_const: 0x64f8
-  __DATA.__objc_selrefs: 0x2280
-  __DATA.__objc_ivar: 0x204
+  __DATA.__objc_const: 0x6558
+  __DATA.__objc_selrefs: 0x22c0
+  __DATA.__objc_ivar: 0x20c
   __DATA.__objc_data: 0xaf0
-  __DATA.__data: 0xcdc
+  __DATA.__data: 0xce0
   __DATA.__bss: 0x90
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 785
-  Symbols:   306
-  CStrings:  2339
+  Functions: 793
+  Symbols:   307
+  CStrings:  2355
 
Symbols:
+ _BKHIDServicesGetNonFlatDeviceOrientation
CStrings:
+ "$"
+ "%{public}s: DREOrientationManager: Boot orientation from BKS = %ld"
+ "%{public}s: DREOrientationManager: Orientation %ld -> %ld (animated=%d)"
+ "-[DREOrientationManager _applyDeviceOrientation:animated:]"
+ "@\"FBSDisplayConfiguration\""
+ "T@\"FBSDisplayConfiguration\",&,N,V_activeDisplayConfiguration"
+ "Tq,N,V_dr_activeInterfaceOrientation"
+ "_activeDisplayConfiguration"
+ "_applyDeviceOrientation:animated:"
+ "_bindScene:"
+ "_dr_activeInterfaceOrientation"
+ "_unbindScene:"
+ "activeDisplayConfiguration"
+ "activeInterfaceOrientation"
+ "dr_activeInterfaceOrientation"
+ "noteActiveInterfaceOrientationDidChangeToOrientation:willAnimateWithSettings:fromOrientation:screen:"
+ "noteActiveInterfaceOrientationWillChangeToOrientation:screen:"
+ "setActiveDisplayConfiguration:"
+ "setDr_activeInterfaceOrientation:"
+ "v28@0:8q16B24"
+ "windowRotationDuration"
- "%{public}s: DREOrientationManager: Orientation changed %ld -> %ld"
- "-[DREOrientationManager _applyDeviceOrientation:]"
- "_referenceBounds"
- "traitCollection"
- "userInterfaceStyle"
```
