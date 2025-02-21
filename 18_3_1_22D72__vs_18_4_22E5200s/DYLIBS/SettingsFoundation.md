## SettingsFoundation

> `/System/Library/PrivateFrameworks/SettingsFoundation.framework/SettingsFoundation`

```diff

-1080.2.7.500.0
-  __TEXT.__text: 0x10d30
-  __TEXT.__auth_stubs: 0x760
-  __TEXT.__objc_methlist: 0x604
-  __TEXT.__const: 0x800
-  __TEXT.__cstring: 0x19a7
+1080.3.6.0.0
+  __TEXT.__text: 0x11804
+  __TEXT.__auth_stubs: 0x790
+  __TEXT.__objc_methlist: 0x634
+  __TEXT.__const: 0x7f8
+  __TEXT.__cstring: 0x1aaf
   __TEXT.__ustring: 0x78
-  __TEXT.__oslogstring: 0x158c
+  __TEXT.__oslogstring: 0x1640
   __TEXT.__gcc_except_tab: 0x28
   __TEXT.__dlopen_cstrs: 0x5a
-  __TEXT.__unwind_info: 0x310
+  __TEXT.__unwind_info: 0x380
   __TEXT.__objc_classname: 0x107
-  __TEXT.__objc_methname: 0x1c3f
-  __TEXT.__objc_methtype: 0x144
-  __TEXT.__objc_stubs: 0x1ce0
+  __TEXT.__objc_methname: 0x1d5d
+  __TEXT.__objc_methtype: 0x154
+  __TEXT.__objc_stubs: 0x1de0
   __DATA_CONST.__got: 0x2c0
-  __DATA_CONST.__const: 0x248
+  __DATA_CONST.__const: 0x258
   __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x890
+  __DATA_CONST.__objc_selrefs: 0x8d8
   __DATA_CONST.__objc_superrefs: 0x38
   __DATA_CONST.__objc_arraydata: 0x88
-  __AUTH_CONST.__auth_got: 0x3c0
-  __AUTH_CONST.__const: 0x460
-  __AUTH_CONST.__cfstring: 0x20c0
-  __AUTH_CONST.__objc_const: 0x8b0
+  __AUTH_CONST.__auth_got: 0x3d8
+  __AUTH_CONST.__const: 0x480
+  __AUTH_CONST.__cfstring: 0x2220
+  __AUTH_CONST.__objc_const: 0x8f0
   __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH_CONST.__objc_intobj: 0x48
-  __DATA.__objc_ivar: 0x2c
+  __DATA.__objc_ivar: 0x30
   __DATA.__data: 0x28
-  __DATA.__bss: 0xc8
+  __DATA.__bss: 0xd8
   __DATA_DIRTY.__objc_data: 0x320
   __DATA_DIRTY.__bss: 0x178
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/TCC.framework/TCC
+  - /usr/lib/libCTGreenTeaLogger.dylib
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 286
-  Symbols:   521
-  CStrings:  724
+  Functions: 333
+  Symbols:   574
+  CStrings:  755
 
Symbols:
+ _CTFontManagerCreateFontDescriptorsFromURL
+ _SFBlueStickerFont
+ _SFChinaMIITBlueStickerLabelId
+ _SFChinaMIITBlueStickerLabelImage
+ _SFChinaMIITBlueStickerNalNumber
+ _SFGreenTeaIMEILog
+ _SFIMEINumber
+ _SFRegulatoryMIITDictionaryKeyLabelId
+ _SFRegulatoryMIITDictionaryKeyNal
+ _SFShouldShowChinaBlueSticker
+ _ct_green_tea_logger_create
+ _getCTGreenTeaOsLogHandle
+ _objc_retain_x28
- _objc_release_x10
CStrings:
+ "\x02F"
+ "%{Public}s: Empty MIIT entry: '%@'"
+ "%{Public}s: Invalid MIIT format: '%{Public}@'"
+ "%{Public}s: MIIT e-label: '%{Public}@'"
+ "%{public}s: Cannot load font error."
+ "-[SFDeviceRegulatoryAttributes _resolveMIIT:]"
+ "00"
+ "@\"NSDictionary\""
+ "Charter-Roman"
+ "ChinaBluesticker"
+ "ChinaGreensticker"
+ "HYCuSong-CAICT"
+ "InternationalMobileEquipmentIdentity"
+ "Preferences.IMEI"
+ "Reading IMEI from CTMobileEquipmentInfo"
+ "T@\"NSDictionary\",&,N,V__resolvedMIITDictionary"
+ "UIFont * _Nonnull SFBlueStickerFont()"
+ "[%{public}@] %{public}@"
+ "__resolvedMIITDictionary"
+ "_resolveMIIT:"
+ "_resolvedMIITDictionary"
+ "firstObject"
+ "fontWithDescriptor:size:"
+ "fontWithName:size:"
+ "imageNamed:inBundle:compatibleWithTraitCollection:"
+ "initWithFormat:arguments:"
+ "label"
+ "miit"
+ "miitDictionary"
+ "nal"
+ "set_resolvedMIITDictionary:"
+ "ttf"
- "\x02E"

```
