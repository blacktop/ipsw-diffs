## videocodecd

> `/usr/libexec/videocodecd`

```diff

-3235.10.1.0.0
-  __TEXT.__text: 0x334
+3235.12.2.0.0
+  __TEXT.__text: 0x194
   __TEXT.__auth_stubs: 0x100
-  __TEXT.__const: 0x10
+  __TEXT.__const: 0x8
   __TEXT.__cstring: 0x1b
-  __TEXT.__oslogstring: 0xcc
+  __TEXT.__oslogstring: 0x33
   __TEXT.__unwind_info: 0x58
   __DATA_CONST.__auth_got: 0x80
   __DATA_CONST.__got: 0x8
-  __DATA.__common: 0x10
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/MediaToolbox.framework/MediaToolbox

   - /System/Library/PrivateFrameworks/Celestial.framework/Celestial
   - /System/Library/PrivateFrameworks/MediaExperience.framework/MediaExperience
   - /usr/lib/libSystem.B.dylib
-  UUID: 9E81B81C-C20C-33B1-A7D1-08B61F632AD2
+  UUID: C0B57427-5E21-3973-9627-8DDF2C52F3B4
   Functions: 1
   Symbols:   19
-  CStrings:  5
+  CStrings:  3
 
Functions (added):
+ sub_100000838

Functions (removed):
- sub_1000008d0
CStrings:
- "<<<< videocodecd >>>> %s: Failed to elevate inactive jetsam priority, error: %d"
- "<<<< videocodecd >>>> %s: Succeeded to elevate inactive jetsam priority."

```
