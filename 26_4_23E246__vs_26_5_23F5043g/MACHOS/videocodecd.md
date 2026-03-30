## videocodecd

> `/usr/libexec/videocodecd`

```diff

-3305.24.1.2.0
-  __TEXT.__text: 0x1ac
+3320.2.1.11.2
+  __TEXT.__text: 0x34c
   __TEXT.__auth_stubs: 0x110
-  __TEXT.__const: 0x8
+  __TEXT.__const: 0x10
   __TEXT.__cstring: 0x46
-  __TEXT.__oslogstring: 0x33
+  __TEXT.__oslogstring: 0xcc
   __TEXT.__unwind_info: 0x58
   __DATA_CONST.__auth_got: 0x88
   __DATA_CONST.__got: 0x8
   __DATA_CONST.__cfstring: 0x40
+  __DATA.__common: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/DuetActivityScheduler.framework/DuetActivityScheduler
   - /System/Library/PrivateFrameworks/MediaExperience.framework/MediaExperience
   - /usr/lib/libSystem.B.dylib
-  UUID: 06D66EA2-9F8E-3311-8939-AA86E0CA601A
+  UUID: F82D9696-9FB5-3802-8F66-1AD1F6FA455F
   Functions: 1
   Symbols:   21
-  CStrings:  7
+  CStrings:  9
 
Functions:
~ sub_100000960 -> sub_1000009f8 : 428 -> 844
CStrings:
+ "<<<< videocodecd >>>> %s: Failed to elevate inactive jetsam priority, error: %d"
+ "<<<< videocodecd >>>> %s: Succeeded to elevate inactive jetsam priority."

```
