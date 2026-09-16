## SpringBoard

> `/System/Library/DataClassMigrators/SpringBoard.migrator/SpringBoard`

### Sections with Same Size but Changed Content

- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA.__data`

```diff

-4636.115.0.0.0
-  __TEXT.__text: 0xda64
-  __TEXT.__auth_stubs: 0x610
-  __TEXT.__objc_stubs: 0x1be0
-  __TEXT.__objc_methlist: 0x67c
+4637.1.7.0.0
+  __TEXT.__text: 0xd380
+  __TEXT.__auth_stubs: 0x5e0
+  __TEXT.__objc_stubs: 0x19a0
+  __TEXT.__objc_methlist: 0x64c
   __TEXT.__const: 0x80
-  __TEXT.__cstring: 0x18d9
-  __TEXT.__objc_methname: 0x1b92
-  __TEXT.__oslogstring: 0x153e
-  __TEXT.__objc_classname: 0x145
+  __TEXT.__cstring: 0x18bb
+  __TEXT.__objc_methname: 0x19e1
+  __TEXT.__oslogstring: 0x139e
+  __TEXT.__objc_classname: 0x11a
   __TEXT.__objc_methtype: 0x329
   __TEXT.__gcc_except_tab: 0x14c
-  __TEXT.__unwind_info: 0x830
+  __TEXT.__unwind_info: 0x818
   __DATA_CONST.__const: 0x15f8
-  __DATA_CONST.__cfstring: 0xf40
-  __DATA_CONST.__objc_classlist: 0x48
+  __DATA_CONST.__cfstring: 0xf20
+  __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arraydata: 0x120
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__objc_arrayobj: 0x30
-  __DATA_CONST.__auth_got: 0x318
-  __DATA_CONST.__got: 0x248
-  __DATA.__objc_const: 0xdb8
-  __DATA.__objc_selrefs: 0x848
+  __DATA_CONST.__auth_got: 0x300
+  __DATA_CONST.__got: 0x228
+  __DATA.__objc_const: 0xd28
+  __DATA.__objc_selrefs: 0x7b8
   __DATA.__objc_ivar: 0x5c
-  __DATA.__objc_data: 0x2d0
+  __DATA.__objc_data: 0x280
   __DATA.__data: 0x128
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 647
-  Symbols:   387
-  CStrings:  717
+  Functions: 642
+  Symbols:   379
+  CStrings:  692
 
Symbols:
- _CATransform3DMakeTranslation
- _CFPreferencesGetAppBooleanValue
- _OBJC_CLASS_$_FBSDeviceEmulationConfiguration
- _OBJC_CLASS_$_FBSDisplayConfigurationBuilder
- _OBJC_CLASS_$_NSValue
- _OBJC_CLASS_$_SBScreenEdgeCompensationDisplayTransformer
- _OBJC_METACLASS_$_SBScreenEdgeCompensationDisplayTransformer
- _SBLogDisplayTransforming
CStrings:
- "%{public}@: screen edge compensation transform built: %{BOOL}u"
- "Applying screen edge compensation: D76 main display size matched; rewriting bounds from %{public}@ to %{public}@"
- "EdgeSwipeBandExpansionEnabled"
- "SBScreenEdgeCompensationDisplayTransformer"
- "Skipping screen edge compensation: isMainD76Display=%{BOOL}u"
- "Unable to build screen edge compensated display configuration: %{public}@ from configuration: %{public}@"
- "Unable to create redacted display configuration: %@ from configuration:%@"
- "_copyWithOverrideSize:"
- "_fbsDisplayConfiguration"
- "_fbsDisplayIdentity"
- "_nativeBounds"
- "buildConfigurationWithError:"
- "emulatedDeviceBounds"
- "hasEmulatedDeviceBounds"
- "initWithConfiguration:"
- "isEmulatedDevice"
- "isMainRootDisplay"
- "isScreenEdgeCompensationEnabled"
- "pixelSize"
- "scale"
- "sceneTransformForWindowScene:"
- "setCurrentMode:preferredMode:otherModes:"
- "setPixelSize:nativeBounds:bounds:"
- "transformedConfigurationForConfiguration:"
- "valueWithCATransform3D:"
```
