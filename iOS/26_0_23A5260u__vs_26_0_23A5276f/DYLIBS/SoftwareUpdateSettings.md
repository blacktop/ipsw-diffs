## SoftwareUpdateSettings

> `/System/Library/PrivateFrameworks/SoftwareUpdateSettings.framework/SoftwareUpdateSettings`

```diff

-486.0.0.0.4
-  __TEXT.__text: 0x1e788
-  __TEXT.__auth_stubs: 0xa40
-  __TEXT.__objc_methlist: 0x10f4
-  __TEXT.__cstring: 0x1dda
+492.0.0.0.5
+  __TEXT.__text: 0x1f054
+  __TEXT.__auth_stubs: 0xa50
+  __TEXT.__objc_methlist: 0x110c
+  __TEXT.__cstring: 0x1e7a
   __TEXT.__gcc_except_tab: 0x1c4
-  __TEXT.__oslogstring: 0x784
+  __TEXT.__oslogstring: 0x7ad
   __TEXT.__dlopen_cstrs: 0xfe
-  __TEXT.__const: 0x404
+  __TEXT.__const: 0x434
   __TEXT.__swift5_typeref: 0x16a
   __TEXT.__swift5_capture: 0x30
-  __TEXT.__swift5_reflstr: 0x97
+  __TEXT.__swift5_reflstr: 0xd7
   __TEXT.__swift5_assocty: 0x48
   __TEXT.__constg_swiftt: 0x130
-  __TEXT.__swift5_fieldmd: 0xa4
+  __TEXT.__swift5_fieldmd: 0xbc
   __TEXT.__swift5_proto: 0x18
   __TEXT.__swift5_types: 0x14
-  __TEXT.__unwind_info: 0x4f8
+  __TEXT.__unwind_info: 0x510
   __TEXT.__objc_classname: 0x29d
-  __TEXT.__objc_methname: 0x41bf
-  __TEXT.__objc_methtype: 0xf32
+  __TEXT.__objc_methname: 0x4264
+  __TEXT.__objc_methtype: 0xf46
   __TEXT.__objc_stubs: 0x2e80
   __DATA_CONST.__got: 0x398
-  __DATA_CONST.__const: 0x850
+  __DATA_CONST.__const: 0x838
   __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x11e0
+  __DATA_CONST.__objc_selrefs: 0x1200
   __DATA_CONST.__objc_superrefs: 0x78
   __DATA_CONST.__objc_arraydata: 0xe0
-  __AUTH_CONST.__auth_got: 0x530
-  __AUTH_CONST.__const: 0x208
-  __AUTH_CONST.__cfstring: 0x1ca0
-  __AUTH_CONST.__objc_const: 0x2c90
+  __AUTH_CONST.__auth_got: 0x538
+  __AUTH_CONST.__const: 0x268
+  __AUTH_CONST.__cfstring: 0x1ce0
+  __AUTH_CONST.__objc_const: 0x2ca0
   __AUTH_CONST.__objc_dictobj: 0x118
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_doubleobj: 0x30
   __AUTH.__objc_data: 0x5d8
   __AUTH.__data: 0xc0
   __DATA.__objc_ivar: 0x134
-  __DATA.__data: 0x390
+  __DATA.__data: 0x398
   __DATA.__bss: 0x440
   __DATA.__common: 0x98
   __DATA_DIRTY.__objc_data: 0x50

   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: A39A233C-E01C-3358-9F00-E5F62A42F870
-  Functions: 524
-  Symbols:   1802
-  CStrings:  1385
+  UUID: 5F9B94F1-01B7-30FD-8608-8322BB4055EB
+  Functions: 541
+  Symbols:   1803
+  CStrings:  1395
 
Symbols:
+ -[SUSettingsTipsManager configureManualComingSoonTipWithTitle:andContent:learnMoreLink:imageSystemName:]
+ -[SUSettingsUserDefaults comingSoonTipImageSystemName:]
+ -[SUSettingsUserDefaults comingSoonTipImageSystemName]
+ ___swift_memcpy16_8
+ ___swift_memcpy64_8
+ _kSUSettingsUserDefaultsComingSoonTipImageSystemName
+ _objc_msgSend$configureManualComingSoonTipWithTitle:andContent:learnMoreLink:imageSystemName:
+ _objc_release_x27
+ _type_layout_string 22SoftwareUpdateSettings26ConstellationComingSoonTipV
- -[SUSettingsTipsManager configureManualComingSoonTipWithTitle:andContent:learnMoreLink:]
- ___swift_memcpy48_8
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swiftDarwin_$_SoftwareUpdateSettings
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_SoftwareUpdateSettings
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_SoftwareUpdateSettings
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_SoftwareUpdateSettings
- _objc_msgSend$configureManualComingSoonTipWithTitle:andContent:learnMoreLink:
CStrings:
+ "%s Overring the default Coming Soon tip content and returning UserDefaultsBasedComingSoonTip instead.\nForce show: %{bool}d\nForce hide: %{bool}d\nTitle: %s\nMessage: %s\nImageSystemName: %s\nLearn More URL: %s"
+ "%s: Setting up the Mocked Coming Soon tip with:\n    title: %s\n    content: %s\n    learnMoreLink: %s\n    imageSystemName: %s "
+ "SUComingSoonTipImageSystemName"
+ "T@\"NSString\",&,N,ScomingSoonTipImageSystemName:"
+ "The image system name for the \"Coming Soon\" tip. This field will override the value returned by Constellation."
+ "comingSoonTipImageSystemName"
+ "comingSoonTipImageSystemName:"
+ "configureManualComingSoonTip(withTitle:andContent:learnMoreLink:imageSystemName:)"
+ "configureManualComingSoonTipWithTitle:andContent:learnMoreLink:imageSystemName:"
+ "imageWithRenderingMode:"
+ "systemImageNamed:"
+ "v48@0:8@16@24@32@40"
- "%s Overring the default Coming Soon tip content and returning UserDefaultsBasedComingSoonTip instead.\nForce show: %{bool}d\nForce hide: %{bool}d\nTitle: %s\nMessage: %s\nLearn More URL: %s"
- "%s: Setting up the Mocked Coming Soon tip with:\n    title: %s\n    content: %s\n    learnMoreLink: %s"
- "configureManualComingSoonTip(withTitle:andContent:learnMoreLink:)"
- "configureManualComingSoonTipWithTitle:andContent:learnMoreLink:"

```
