## SpringBoard

> `/System/Library/DataClassMigrators/SpringBoard.migrator/SpringBoard`

```diff

-4557.3.9.102.0
-  __TEXT.__text: 0xe768
-  __TEXT.__auth_stubs: 0x5f0
-  __TEXT.__objc_stubs: 0x1b80
-  __TEXT.__objc_methlist: 0x63c
+4557.4.7.100.0
+  __TEXT.__text: 0xf098
+  __TEXT.__auth_stubs: 0x5b0
+  __TEXT.__objc_stubs: 0x1a60
+  __TEXT.__objc_methlist: 0x64c
   __TEXT.__const: 0x78
   __TEXT.__cstring: 0x17ba
-  __TEXT.__objc_methname: 0x1b10
-  __TEXT.__oslogstring: 0x1355
+  __TEXT.__objc_methname: 0x1a41
+  __TEXT.__oslogstring: 0x130b
   __TEXT.__objc_classname: 0x125
   __TEXT.__objc_methtype: 0x329
-  __TEXT.__gcc_except_tab: 0x194
-  __TEXT.__unwind_info: 0x280
-  __DATA_CONST.__auth_got: 0x308
-  __DATA_CONST.__got: 0x248
+  __TEXT.__gcc_except_tab: 0x170
+  __TEXT.__unwind_info: 0x710
+  __DATA_CONST.__auth_got: 0x2e8
+  __DATA_CONST.__got: 0x240
   __DATA_CONST.__const: 0x14c0
   __DATA_CONST.__cfstring: 0xf20
   __DATA_CONST.__objc_classlist: 0x40

   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA.__objc_const: 0xd28
-  __DATA.__objc_selrefs: 0x830
+  __DATA.__objc_selrefs: 0x7e8
   __DATA.__objc_ivar: 0x5c
   __DATA.__objc_data: 0x280
   __DATA.__data: 0x128

   - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices
   - /System/Library/PrivateFrameworks/GraphicsServices.framework/GraphicsServices
   - /System/Library/PrivateFrameworks/IconServices.framework/IconServices
+  - /System/Library/PrivateFrameworks/MDMClientLibrary.framework/MDMClientLibrary
   - /System/Library/PrivateFrameworks/PaperBoardUI.framework/PaperBoardUI
   - /System/Library/PrivateFrameworks/PosterBoardServices.framework/PosterBoardServices
   - /System/Library/PrivateFrameworks/SplashBoard.framework/SplashBoard

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: ECDBAB6B-E885-3C39-B360-815087995F11
-  Functions: 606
-  Symbols:   374
-  CStrings:  823
+  UUID: 71F2B3B1-80FA-322B-A665-FF0CE540DCCF
+  Functions: 614
+  Symbols:   369
+  CStrings:  813
 
Symbols:
+ _OBJC_CLASS_$_MDMCloudConfiguration
+ _objc_retain_x28
- _OBJC_CLASS_$_FBSDeviceEmulationConfiguration
- _OBJC_CLASS_$_FBSDisplayConfigurationBuilder
- _SBLogDisplayTransforming
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x8
CStrings:
+ "isRapidReturnToService"
+ "sharedConfiguration"
- "Unable to create redacted display configuration: %@ from configuration:%@"
- "_copyWithOverrideSize:"
- "_nativeBounds"
- "buildConfigurationWithError:"
- "emulatedDeviceBounds"
- "hasEmulatedDeviceBounds"
- "initWithConfiguration:"
- "isEmulatedDevice"
- "isMainRootDisplay"
- "scale"
- "setCurrentMode:preferredMode:otherModes:"
- "setPixelSize:nativeBounds:bounds:"

```
