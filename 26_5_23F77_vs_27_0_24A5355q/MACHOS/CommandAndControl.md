## CommandAndControl

> `/System/Library/CoreServices/CommandAndControl.app/CommandAndControl`

```diff

-148.7.0.0.0
-  __TEXT.__text: 0x145c
-  __TEXT.__auth_stubs: 0x280
-  __TEXT.__objc_stubs: 0x700
+179.0.0.0.0
+  __TEXT.__text: 0x1360
+  __TEXT.__auth_stubs: 0x270
+  __TEXT.__objc_stubs: 0x780
   __TEXT.__objc_methlist: 0x30c
-  __TEXT.__const: 0x78
-  __TEXT.__cstring: 0x136
-  __TEXT.__objc_classname: 0x76
-  __TEXT.__objc_methname: 0x9bf
+  __TEXT.__const: 0x80
+  __TEXT.__cstring: 0x125
+  __TEXT.__objc_classname: 0x74
+  __TEXT.__objc_methname: 0xa42
   __TEXT.__objc_methtype: 0x265
-  __TEXT.__oslogstring: 0x197
-  __TEXT.__unwind_info: 0xc0
-  __DATA_CONST.__auth_got: 0x148
-  __DATA_CONST.__got: 0xd8
+  __TEXT.__oslogstring: 0x175
+  __TEXT.__unwind_info: 0xc8
   __DATA_CONST.__const: 0x130
   __DATA_CONST.__cfstring: 0x160
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_const: 0x530
-  __DATA.__objc_selrefs: 0x340
-  __DATA.__objc_ivar: 0x10
+  __DATA_CONST.__auth_got: 0x140
+  __DATA_CONST.__got: 0xe0
+  __DATA.__objc_const: 0x570
+  __DATA.__objc_selrefs: 0x360
+  __DATA.__objc_ivar: 0x18
   __DATA.__objc_data: 0x140
   __DATA.__data: 0x120
   __DATA.__bss: 0x10

   - /System/Library/PrivateFrameworks/CarKit.framework/CarKit
   - /System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset
   - /System/Library/PrivateFrameworks/SpeechRecognitionCommandAndControl.framework/SpeechRecognitionCommandAndControl
+  - /System/Library/PrivateFrameworks/VoiceControl.framework/VoiceControl
   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C3431B0C-1750-336F-A766-914B84700FFA
+  UUID: EDA7F145-0C48-3365-BA35-187D6DEC105B
   Functions: 31
   Symbols:   81
-  CStrings:  187
+  CStrings:  191
 
Symbols:
+ _OBJC_CLASS_$_VCSignposts
+ _OBJC_CLASS_$_VCSpeechAssetManager
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
- ___stack_chk_fail
- ___stack_chk_guard
- __os_feature_enabled_impl
- _objc_retain
- _objc_retainAutoreleasedReturnValue
CStrings:
+ "Checked Mobile assets available on disk = %d"
+ "_assetAlreadyInstalled"
+ "_didCheckAssetInstalled"
+ "isAssetInstalledForLocaleIdentifier:"
+ "lifecycleFirstLaunch"
+ "lifecycleTerminate"
+ "shared"
- "CarPlay"
- "OliveShell"
- "OliveShell feature flag not enabled. Not connecting to CarPlay's UIWindowScene"

```
