## SoftwareUpdateUIMobileSettingsPlugin

> `/System/Library/PreferenceBundles/SoftwareUpdateUIMobileSettingsPlugin.bundle/SoftwareUpdateUIMobileSettingsPlugin`

```diff

-508.80.83.0.0
-  __TEXT.__text: 0x4f768
-  __TEXT.__auth_stubs: 0x1240
-  __TEXT.__objc_methlist: 0x44
-  __TEXT.__const: 0x2078
-  __TEXT.__constg_swiftt: 0x56c
-  __TEXT.__swift5_typeref: 0x1b0a
-  __TEXT.__swift5_fieldmd: 0x250
-  __TEXT.__swift5_reflstr: 0x355
-  __TEXT.__swift5_assocty: 0xf0
-  __TEXT.__swift5_proto: 0x44
-  __TEXT.__swift5_types: 0x64
-  __TEXT.__swift5_capture: 0x1ec4
-  __TEXT.__cstring: 0x10bd
-  __TEXT.__objc_methname: 0x36b
-  __TEXT.__oslogstring: 0xc0a
+508.100.172.0.0
+  __TEXT.__text: 0x508e0
+  __TEXT.__auth_stubs: 0x15e0
+  __TEXT.__objc_stubs: 0x4e0
+  __TEXT.__objc_methlist: 0x50
+  __TEXT.__swift5_typeref: 0x1bb2
+  __TEXT.__const: 0x22d8
+  __TEXT.__objc_methname: 0x4a8
+  __TEXT.__objc_classname: 0x185
+  __TEXT.__objc_methtype: 0x3f
+  __TEXT.__constg_swiftt: 0x6c8
+  __TEXT.__swift5_reflstr: 0x3c5
+  __TEXT.__swift5_fieldmd: 0x2e4
+  __TEXT.__swift5_proto: 0x60
+  __TEXT.__swift5_types: 0x7c
+  __TEXT.__cstring: 0x1172
+  __TEXT.__swift5_assocty: 0x138
+  __TEXT.__swift5_capture: 0x1c50
+  __TEXT.__oslogstring: 0xa8a
   __TEXT.__swift_as_entry: 0x38
   __TEXT.__swift_as_ret: 0x30
   __TEXT.__swift5_builtin: 0x14
-  __TEXT.__unwind_info: 0x15a0
-  __TEXT.__eh_frame: 0x570
-  __DATA_CONST.__auth_got: 0x920
-  __DATA_CONST.__got: 0x390
-  __DATA_CONST.__auth_ptr: 0x488
-  __DATA_CONST.__const: 0x50a0
-  __DATA_CONST.__objc_classlist: 0x20
+  __TEXT.__unwind_info: 0x14e0
+  __TEXT.__eh_frame: 0x610
+  __DATA_CONST.__auth_got: 0xaf8
+  __DATA_CONST.__got: 0x438
+  __DATA_CONST.__auth_ptr: 0x580
+  __DATA_CONST.__const: 0x4b80
+  __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_const: 0x260
-  __DATA.__objc_selrefs: 0x128
-  __DATA.__objc_data: 0x108
-  __DATA.__data: 0x860
-  __DATA.__bss: 0xa10
+  __DATA.__objc_const: 0x310
+  __DATA.__objc_selrefs: 0x158
+  __DATA.__objc_data: 0x168
+  __DATA.__data: 0x9d0
+  __DATA.__bss: 0xdb8
+  __DATA.__common: 0x20
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/CoreTelephony.framework/CoreTelephony

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: BF2FF5F8-5DC2-37CE-A9AE-4D15F1D19C58
-  Functions: 1856
-  Symbols:   107
-  CStrings:  154
+  UUID: 82666092-4429-32CA-BBAC-9CFCD8F736AB
+  Functions: 1898
+  Symbols:   122
+  CStrings:  188
 
Symbols:
+ _OBJC_CLASS_$_LSApplicationWorkspace
+ _OBJC_CLASS_$_NSProcessInfo
+ _OBJC_CLASS_$_UIImage
+ __availability_version_check
+ _dispatch_once_f
+ _dlsym
+ _fclose
+ _fopen
+ _fread
+ _fseek
+ _ftell
+ _rewind
+ _sscanf
+ _swift_allocBox
+ _swift_getAssociatedTypeWitness
+ _swift_slowAlloc
- _swift_dynamicCast
CStrings:
+ "%d.%d.%d"
+ "+shouldShowTip"
+ "-mini-tip-see-whats-new"
+ "/System/Library/CoreServices/SystemVersion.plist"
+ ":"
+ "@16@0:8"
+ "CFDataCreateWithBytesNoCopy"
+ "CFDictionaryGetValue"
+ "CFGetTypeID"
+ "CFPropertyListCreateFromXMLData"
+ "CFPropertyListCreateWithData"
+ "CFRelease"
+ "CFStringCreateWithCStringNoCopy"
+ "CFStringGetCString"
+ "CFStringGetTypeID"
+ "General"
+ "Learn more…"
+ "ProductVersion"
+ "SUUISettingsSoftwareUpdateController"
+ "SoftwareUpdateUIMobileSettingsPlugin/MobileComingSoonTipAdapter.swift"
+ "SoftwareUpdateUIMobileSettingsPlugin/MockedComingSoonTip.swift"
+ "SoftwareUpdateUIMobileSettingsPlugin/UserDefaultsBasedComingSoonTip.swift"
+ "View.task @ "
+ "_TtC36SoftwareUpdateUIMobileSettingsPlugin26MobileComingSoonTipAdapter"
+ "comingSoonTipImageSystemName"
+ "comingSoonTipLearnMoreLink"
+ "comingSoonTipMessage"
+ "comingSoonTipTitle"
+ "defaultWorkspace"
+ "imageWithRenderingMode:"
+ "init"
+ "kCFAllocatorNull"
+ "openSensitiveURL:withOptions:"
+ "operatingSystemVersion"
+ "preferencesManager"
+ "preview"
+ "r"
+ "reactivePlatformEnvironment"
+ "shouldShowComingSoonTip"
+ "sparkles"
+ "systemImageNamed:"
+ "tipType"
- "%s.%s: Skipping on assignment of automatic security responses to \"%{bool}d\" because the automatic security response toggle is disabled"
- "%s.%s: Skipping on assignment of automatic system files & data to \"%{bool}d\" because the automatic security response toggle is disabled"
- "User Action: Sets %{bool}d for auto Install Security Response in AutomaticUpdatesView"
- "autoInstallSecurityResponse"
- "previousUserSpecifiedAutoInstallSecurityResponse"
- "setAutoInstallSecurityResponse:"
- "setPreviousUserSpecifiedAutoInstallSecurityResponse:"
- "shouldDisableRSR"

```
