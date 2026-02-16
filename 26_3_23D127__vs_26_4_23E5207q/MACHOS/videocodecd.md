## videocodecd

> `/usr/libexec/videocodecd`

```diff

-3300.7.1.1.1
-  __TEXT.__text: 0x1ac
+3305.19.1.0.0
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
-  UUID: 4CA9A845-6519-380F-A3E3-811D44A389BA
+  UUID: FBA416EF-024C-3D19-A6E4-D5ECA23363CC
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
