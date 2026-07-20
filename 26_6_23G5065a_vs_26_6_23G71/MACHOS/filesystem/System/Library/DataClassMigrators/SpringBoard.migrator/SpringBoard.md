## SpringBoard

> `/System/Library/DataClassMigrators/SpringBoard.migrator/SpringBoard`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

 4557.6.2.0.0
-  __TEXT.__text: 0xf098
-  __TEXT.__auth_stubs: 0x5b0
-  __TEXT.__objc_stubs: 0x1a60
+  __TEXT.__text: 0xf2b8
+  __TEXT.__auth_stubs: 0x5c0
+  __TEXT.__objc_stubs: 0x1bc0
   __TEXT.__objc_methlist: 0x64c
   __TEXT.__const: 0x78
   __TEXT.__cstring: 0x17ba
-  __TEXT.__objc_methname: 0x1a41
-  __TEXT.__oslogstring: 0x130b
+  __TEXT.__objc_methname: 0x1b3b
+  __TEXT.__oslogstring: 0x1355
   __TEXT.__objc_classname: 0x125
   __TEXT.__objc_methtype: 0x329
   __TEXT.__gcc_except_tab: 0x170
   __TEXT.__unwind_info: 0x710
-  __DATA_CONST.__auth_got: 0x2e8
-  __DATA_CONST.__got: 0x240
+  __DATA_CONST.__auth_got: 0x2f0
+  __DATA_CONST.__got: 0x250
   __DATA_CONST.__const: 0x14c0
   __DATA_CONST.__cfstring: 0xf20
   __DATA_CONST.__objc_classlist: 0x40

   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA.__objc_const: 0xd28
-  __DATA.__objc_selrefs: 0x7e8
+  __DATA.__objc_selrefs: 0x840
   __DATA.__objc_ivar: 0x5c
   __DATA.__objc_data: 0x280
   __DATA.__data: 0x128

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 614
-  Symbols:   369
-  CStrings:  686
+  Functions: 615
+  Symbols:   372
+  CStrings:  698
 
Symbols:
+ _OBJC_CLASS_$_FBSDeviceEmulationConfiguration
+ _OBJC_CLASS_$_FBSDisplayConfigurationBuilder
+ _SBLogDisplayTransforming
CStrings:
+ "Unable to create redacted display configuration: %@ from configuration:%@"
+ "_copyWithOverrideSize:"
+ "_nativeBounds"
+ "buildConfigurationWithError:"
+ "emulatedDeviceBounds"
+ "hasEmulatedDeviceBounds"
+ "initWithConfiguration:"
+ "isEmulatedDevice"
+ "isMainRootDisplay"
+ "scale"
+ "setCurrentMode:preferredMode:otherModes:"
+ "setPixelSize:nativeBounds:bounds:"
```
