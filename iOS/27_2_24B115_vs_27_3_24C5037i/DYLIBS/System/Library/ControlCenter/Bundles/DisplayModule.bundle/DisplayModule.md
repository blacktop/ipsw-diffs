## DisplayModule

> `/System/Library/ControlCenter/Bundles/DisplayModule.bundle/DisplayModule`

```diff

-704.2.4.100.0
-  __TEXT.__text: 0x3370
-  __TEXT.__objc_methlist: 0x7fc
-  __TEXT.__const: 0x58
-  __TEXT.__cstring: 0x499
-  __TEXT.__gcc_except_tab: 0x48
-  __TEXT.__unwind_info: 0x208
+704.3.7.100.0
+  __TEXT.__text: 0x35cc
+  __TEXT.__objc_methlist: 0x854
+  __TEXT.__const: 0x68
+  __TEXT.__cstring: 0x469
+  __TEXT.__gcc_except_tab: 0x28
+  __TEXT.__oslogstring: 0x11e
+  __TEXT.__unwind_info: 0x210
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1d0
+  __DATA_CONST.__const: 0x180
   __DATA_CONST.__objc_classlist: 0x18
-  __DATA_CONST.__objc_protolist: 0x28
+  __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x760
+  __DATA_CONST.__objc_selrefs: 0x7b8
   __DATA_CONST.__objc_superrefs: 0x10
-  __DATA_CONST.__objc_arraydata: 0x10
-  __DATA_CONST.__got: 0x118
-  __AUTH_CONST.__cfstring: 0x4e0
-  __AUTH_CONST.__objc_const: 0xbe8
-  __AUTH_CONST.__objc_arrayobj: 0x18
+  __DATA_CONST.__got: 0x128
+  __AUTH_CONST.__cfstring: 0x4c0
+  __AUTH_CONST.__objc_const: 0xc88
   __AUTH_CONST.__auth_got: 0x0
-  __DATA.__objc_ivar: 0x4c
-  __DATA.__data: 0x1e0
+  __DATA.__objc_ivar: 0x50
+  __DATA.__data: 0x240
   __DATA_DIRTY.__objc_data: 0xf0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 106
-  Symbols:   100
-  CStrings:  47
+  Functions: 113
+  Symbols:   102
+  CStrings:  49
 
Symbols:
+ _CCUILogUserInterface
+ _OBJC_CLASS_$_NSSet
+ __os_log_error_impl
+ _objc_opt_new
+ _os_log_type_enabled
- _BKSDisplayBrightnessIsBrightnessLevelControlAvailable
- _OBJC_CLASS_$_BrightnessSystemClient
- _OBJC_CLASS_$_NSConstantArray
CStrings:
+ "Q"
+ "[Display Module] Failed to activate CBClient: %{public}@"
+ "[Display Module] Failed to copy brightness control available property: %{public}@"
+ "[Display Module] Failed to create CBDisplayClient for displayID %lu: %{public}@"
+ "[Display Module] Failed to register CBPropertyObserver: %{public}@"
- "A"
- "CBAutoBrightnessAvailable"
- "v24@?0@\"NSString\"8@16"
```
