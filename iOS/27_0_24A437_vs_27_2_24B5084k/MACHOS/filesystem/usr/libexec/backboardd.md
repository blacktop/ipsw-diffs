## backboardd

> `/usr/libexec/backboardd`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`

```diff

-877.0.0.0.0
-  __TEXT.__text: 0x56ef8
-  __TEXT.__auth_stubs: 0x1550
-  __TEXT.__objc_stubs: 0x9e80
-  __TEXT.__objc_methlist: 0x4a0c
+877.2.1.0.0
+  __TEXT.__text: 0x585a4
+  __TEXT.__auth_stubs: 0x1570
+  __TEXT.__objc_stubs: 0x9fc0
+  __TEXT.__objc_methlist: 0x4b24
   __TEXT.__const: 0x320
   __TEXT.__dlopen_cstrs: 0x62
   __TEXT.__gcc_except_tab: 0x770
-  __TEXT.__objc_methname: 0xdbe8
-  __TEXT.__objc_classname: 0x13c1
-  __TEXT.__cstring: 0x4cd3
-  __TEXT.__objc_methtype: 0x2ed7
-  __TEXT.__oslogstring: 0x7144
-  __TEXT.__unwind_info: 0x1b40
-  __DATA_CONST.__const: 0x3318
-  __DATA_CONST.__cfstring: 0x5000
-  __DATA_CONST.__objc_classlist: 0x338
-  __DATA_CONST.__objc_protolist: 0x240
+  __TEXT.__objc_methname: 0xdc67
+  __TEXT.__objc_classname: 0x13fd
+  __TEXT.__cstring: 0x4d19
+  __TEXT.__objc_methtype: 0x2ee4
+  __TEXT.__oslogstring: 0x72cb
+  __TEXT.__unwind_info: 0x1ba0
+  __DATA_CONST.__const: 0x3348
+  __DATA_CONST.__cfstring: 0x5080
+  __DATA_CONST.__objc_classlist: 0x340
+  __DATA_CONST.__objc_protolist: 0x248
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x98
-  __DATA_CONST.__objc_superrefs: 0x270
+  __DATA_CONST.__objc_superrefs: 0x278
   __DATA_CONST.__linkguard: 0x18
   __DATA_CONST.__objc_doubleobj: 0x40
   __DATA_CONST.__objc_intobj: 0x1f8
   __DATA_CONST.__objc_arraydata: 0x20
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA_CONST.__auth_got: 0xab8
+  __DATA_CONST.__auth_got: 0xac8
   __DATA_CONST.__got: 0x898
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA.__objc_const: 0xaf20
-  __DATA.__objc_selrefs: 0x30e8
-  __DATA.__objc_ivar: 0x7fc
-  __DATA.__objc_data: 0x2030
-  __DATA.__data: 0x1b88
+  __DATA.__objc_const: 0xb0f8
+  __DATA.__objc_selrefs: 0x3118
+  __DATA.__objc_ivar: 0x800
+  __DATA.__objc_data: 0x2080
+  __DATA.__data: 0x1be8
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsp.dylib
-  Functions: 1904
-  Symbols:   618
-  CStrings:  4091
+  Functions: 1929
+  Symbols:   620
+  CStrings:  4111
 
Symbols:
+ _dispatch_get_specific
+ _dispatch_queue_set_specific
CStrings:
+ "@\"<BKDisplayRenderOverlayPresentable>\""
+ "BKDisplayRenderOverlayPresentable"
+ "BKDisplayRenderOverlaySet"
+ "Current bootUI for display %{public}@ is an Apple Logo, level %g"
+ "Current bootUI for display %{public}@ is the spinny because the Apple Logo can only be laid out for the legacy main display, level %g"
+ "Current bootUI for display %{public}@ is the spinny, level %g"
+ "T@\"NSArray\",R,N"
+ "TB,R,N,GisEmpty"
+ "Using %{public}@ for %{public}@"
+ "Using default display for %{public}@"
+ "_displaysForBootUI"
+ "_members"
+ "_overlayForDisplays:level:"
+ "_queue_appendDescriptionToStream:"
+ "addOverlay(%d-%{public}@): Adding the overlay: %{public}@"
+ "addOverlay(%d-%{public}@): no displays to add the overlay to"
+ "addUnderlay: Adding the underlay: %{public}@"
+ "addUnderlay: no displays to add the underlay to"
+ "appendCollection:withName:itemBlock:"
+ "arrayWithCapacity:"
+ "dismissWhenUnsustained"
+ "initWithOverlays:"
+ "isEmpty"
+ "overlaySustained"
+ "overlays"
+ "screenOwner"
+ "screenOwnerPID"
+ "setInterstitial:"
+ "setWithOverlays:"
- "@\"BKDisplayRenderOverlay\""
- "Current bootUI is an Apple Logo"
- "Current bootUI is the spinny, level %@"
- "T@\"BKDisplayRenderOverlay\",&,N,V_overlay"
- "T@\"BKDisplayRenderOverlay\",&,N,V_underlay"
- "addOverlay(%d-%{public}@): Adding the overlay"
- "addUnderlay:  Adding the underlay"
- "setOverlay:"
- "setUnderlay:"
```
