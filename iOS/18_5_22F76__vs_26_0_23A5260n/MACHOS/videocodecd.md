## videocodecd

> `/usr/libexec/videocodecd`

```diff

-3225.7.1.0.0
-  __TEXT.__text: 0x194
-  __TEXT.__auth_stubs: 0x100
-  __TEXT.__const: 0x8
-  __TEXT.__cstring: 0x1b
-  __TEXT.__oslogstring: 0x33
+3255.61.4.11.7
+  __TEXT.__text: 0x34c
+  __TEXT.__auth_stubs: 0x110
+  __TEXT.__const: 0x10
+  __TEXT.__cstring: 0x46
+  __TEXT.__oslogstring: 0xcc
   __TEXT.__unwind_info: 0x58
-  __DATA_CONST.__auth_got: 0x80
+  __DATA_CONST.__auth_got: 0x88
   __DATA_CONST.__got: 0x8
+  __DATA_CONST.__cfstring: 0x40
+  __DATA.__common: 0x10
+  - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/MediaToolbox.framework/MediaToolbox
   - /System/Library/Frameworks/VideoToolbox.framework/VideoToolbox
   - /System/Library/PrivateFrameworks/AudioToolboxCore.framework/AudioToolboxCore
   - /System/Library/PrivateFrameworks/Celestial.framework/Celestial
+  - /System/Library/PrivateFrameworks/DuetActivityScheduler.framework/DuetActivityScheduler
   - /System/Library/PrivateFrameworks/MediaExperience.framework/MediaExperience
   - /usr/lib/libSystem.B.dylib
-  UUID: 46B14A65-5706-3A76-AF7C-9BACBB8E929B
+  UUID: F5FDC697-C97C-3113-BC33-1920E5356321
   Functions: 1
-  Symbols:   19
-  CStrings:  3
+  Symbols:   21
+  CStrings:  9
 
Symbols:
+ _FigGetCFPreferenceNumberWithDefault
+ ___CFConstantStringClassReference
Functions:
~ sub_100000838 -> sub_1000009f8 : 404 -> 844
CStrings:
+ "<<<< videocodecd >>>> %s: Failed to elevate inactive jetsam priority, error: %d"
+ "<<<< videocodecd >>>> %s: Succeeded to elevate inactive jetsam priority."
+ "asan_crash_videocodecd"
+ "com.apple.coremedia"

```
