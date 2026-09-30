## SpringBoard

> `/System/Library/DataClassMigrators/SpringBoard.migrator/SpringBoard`

```diff

-4557.0.10.113.0
-  __TEXT.__text: 0xe030
-  __TEXT.__auth_stubs: 0x5d0
-  __TEXT.__objc_stubs: 0x1940
-  __TEXT.__objc_methlist: 0x61c
-  __TEXT.__cstring: 0x16a9
-  __TEXT.__const: 0x70
-  __TEXT.__objc_methname: 0x1945
-  __TEXT.__oslogstring: 0x1193
+4557.0.10.114.0
+  __TEXT.__text: 0xe6c8
+  __TEXT.__auth_stubs: 0x5f0
+  __TEXT.__objc_stubs: 0x1b80
+  __TEXT.__objc_methlist: 0x63c
+  __TEXT.__cstring: 0x177b
+  __TEXT.__const: 0x78
+  __TEXT.__objc_methname: 0x1b10
+  __TEXT.__oslogstring: 0x1355
   __TEXT.__objc_classname: 0x125
   __TEXT.__objc_methtype: 0x329
   __TEXT.__gcc_except_tab: 0x194
-  __TEXT.__unwind_info: 0x270
-  __DATA_CONST.__auth_got: 0x2f8
-  __DATA_CONST.__got: 0x238
+  __TEXT.__unwind_info: 0x278
+  __DATA_CONST.__auth_got: 0x308
+  __DATA_CONST.__got: 0x248
   __DATA_CONST.__const: 0x1490
-  __DATA_CONST.__cfstring: 0xd20
+  __DATA_CONST.__cfstring: 0xee0
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x38
-  __DATA_CONST.__objc_arraydata: 0x80
+  __DATA_CONST.__objc_arraydata: 0x120
+  __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA.__objc_const: 0xd28
-  __DATA.__objc_selrefs: 0x7a0
+  __DATA.__objc_selrefs: 0x830
   __DATA.__objc_ivar: 0x5c
   __DATA.__objc_data: 0x280
   __DATA.__data: 0x128

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A82E17DB-7FCF-3EC0-A79C-D9113A45E100
-  Functions: 599
-  Symbols:   366
-  CStrings:  766
+  UUID: 23A5305F-D7E7-3534-A832-A25A17A19C9D
+  Functions: 603
+  Symbols:   371
+  CStrings:  818
 
Symbols:
+ _MGCopyAnswer
+ _OBJC_CLASS_$_FBSDeviceEmulationConfiguration
+ _OBJC_CLASS_$_FBSDisplayConfigurationBuilder
+ _OBJC_CLASS_$_NSConstantDictionary
+ _SBLogDisplayTransforming
CStrings:
+ "Coming from AOD-off-by-default device with no explicit preference. Leaving AOD enabled by default."
+ "Coming from AOD-on-by-default device with no explicit preference. Enabling AOD"
+ "DeviceDisablesAODByDefault"
+ "SBDeviceEnablesAlwaysOnByDefault"
+ "SBEnableAlwaysOn"
+ "Unable to create redacted display configuration: %@ from configuration:%@"
+ "[AOD migration] default is unset. Old device on-by-default: %@. New device on-by-default: %{BOOL}u"
+ "[AOD migration] product type: %@"
+ "[AOD migration] supportsAOD: %{BOOL}u isFromOtherDevice: %{BOOL}u"
+ "_copyWithOverrideSize:"
+ "_nativeBounds"
+ "boolValue"
+ "buildConfigurationWithError:"
+ "currentDeviceSupportsAlwaysOnByDefault"
+ "emulatedDeviceBounds"
+ "hasEmulatedDeviceBounds"
+ "iPhone15,2"
+ "iPhone15,3"
+ "iPhone16,1"
+ "iPhone16,2"
+ "iPhone17,1"
+ "iPhone17,2"
+ "iPhone18,1"
+ "iPhone18,2"
+ "iPhone18,3"
+ "iPhone18,4"
+ "initWithConfiguration:"
+ "isEmulatedDevice"
+ "isMainRootDisplay"
+ "j8/Omm6s1lsmTDFsXjsBfA"
+ "numberWithInt:"
+ "performImplicitAODPreferenceMigrationIfNecessary"
+ "restoredBackupProductType"
+ "scale"
+ "setCurrentMode:preferredMode:otherModes:"
+ "setPixelSize:nativeBounds:bounds:"
+ "sourceDeviceSupportsAODByDefaultWithUserDefaults:"
+ "userDataDisposition"

```
