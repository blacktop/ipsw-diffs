## ControlStrip

> `/System/Library/CoreServices/ControlStrip.app/Contents/MacOS/ControlStrip`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__swift5_reflstr`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_entry`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_selrefs`

```diff

-238.0.0.0.0
-  __TEXT.__text: 0x53694
-  __TEXT.__auth_stubs: 0x2270
+238.400.0.0.0
+  __TEXT.__text: 0x53458
+  __TEXT.__auth_stubs: 0x2280
   __TEXT.__objc_stubs: 0x2080
-  __TEXT.__objc_methlist: 0x122c
+  __TEXT.__objc_methlist: 0x121c
   __TEXT.__const: 0x31b8
   __TEXT.__objc_classname: 0x9a4
-  __TEXT.__objc_methname: 0x3759
+  __TEXT.__objc_methname: 0x3739
   __TEXT.__objc_methtype: 0x9fe
-  __TEXT.__constg_swiftt: 0x28d8
-  __TEXT.__swift5_typeref: 0x12d4
+  __TEXT.__constg_swiftt: 0x28c0
+  __TEXT.__swift5_typeref: 0x12cc
   __TEXT.__swift5_reflstr: 0xdb9
-  __TEXT.__swift5_fieldmd: 0x132c
+  __TEXT.__swift5_fieldmd: 0x1320
   __TEXT.__swift5_builtin: 0x12c
   __TEXT.__swift5_assocty: 0x298
   __TEXT.__swift5_capture: 0x914
   __TEXT.__swift5_proto: 0x1ec
   __TEXT.__swift5_types: 0x1fc
-  __TEXT.__cstring: 0x1887
+  __TEXT.__cstring: 0x18a7
   __TEXT.__oslogstring: 0x531
   __TEXT.__swift5_protos: 0x1c
   __TEXT.__swift5_entry: 0x8
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x1b28
+  __TEXT.__unwind_info: 0x1b20
   __TEXT.__eh_frame: 0x588
   __DATA_CONST.__const: 0x46f0
   __DATA_CONST.__objc_classlist: 0x168
   __DATA_CONST.__objc_protolist: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x78
-  __DATA_CONST.__auth_got: 0x1140
-  __DATA_CONST.__got: 0x690
+  __DATA_CONST.__auth_got: 0x1148
+  __DATA_CONST.__got: 0x688
   __DATA_CONST.__auth_ptr: 0x660
-  __DATA.__objc_const: 0x2fa8
+  __DATA.__objc_const: 0x2f88
   __DATA.__objc_selrefs: 0xe00
-  __DATA.__objc_data: 0x30d8
-  __DATA.__data: 0x2778
+  __DATA.__objc_data: 0x30b8
+  __DATA.__data: 0x2758
   __DATA.__bss: 0x2e70
   __DATA.__common: 0x158
   __CGPreLoginApp.__cgpreloginapp: 0x0

   - /System/Library/PrivateFrameworks/OSD.framework/Versions/A/OSD
   - /System/Library/PrivateFrameworks/SiriUI.framework/Versions/A/SiriUI
   - /System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/SkyLight
+  - /System/Library/PrivateFrameworks/SystemBanner.framework/Versions/A/SystemBanner
   - /usr/lib/libDiagnosticMessagesClient.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib

   - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3126
+  Functions: 3122
   Symbols:   905
-  CStrings:  968
+  CStrings:  969
 
Symbols:
+ _$s12SystemBanner0aB7ServiceSo0abC8Protocol_pyF
- _OBJC_CLASS_$_OSDManager
CStrings:
+ "SystemBannerServiceConnection"
+ "showDisplayBrightness:value:max:isEnabled:"
+ "showVolume:max:isEnabled:"
- "sharedManager"
- "showImage:onDisplayID:priority:msecUntilFade:filledChiclets:totalChiclets:locked:"
```
