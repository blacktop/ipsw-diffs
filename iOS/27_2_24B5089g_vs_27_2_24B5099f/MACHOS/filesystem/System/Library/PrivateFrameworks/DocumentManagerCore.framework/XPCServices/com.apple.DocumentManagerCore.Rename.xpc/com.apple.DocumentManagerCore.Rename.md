## com.apple.DocumentManagerCore.Rename

> `/System/Library/PrivateFrameworks/DocumentManagerCore.framework/XPCServices/com.apple.DocumentManagerCore.Rename.xpc/com.apple.DocumentManagerCore.Rename`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-401.1.5.0.0
-  __TEXT.__text: 0xaf4
+403.1.8.0.0
+  __TEXT.__text: 0xc5c
   __TEXT.__auth_stubs: 0x190
-  __TEXT.__objc_stubs: 0x280
+  __TEXT.__objc_stubs: 0x2a0
   __TEXT.__objc_methlist: 0x188
   __TEXT.__const: 0x80
   __TEXT.__objc_classname: 0x53
-  __TEXT.__objc_methname: 0x3c7
+  __TEXT.__objc_methname: 0x3df
   __TEXT.__objc_methtype: 0x1b5
-  __TEXT.__oslogstring: 0x1bc
+  __TEXT.__oslogstring: 0x250
   __TEXT.__cstring: 0x85
-  __TEXT.__unwind_info: 0xa0
+  __TEXT.__unwind_info: 0xa8
   __DATA_CONST.__const: 0x28
   __DATA_CONST.__cfstring: 0x20
   __DATA_CONST.__objc_classlist: 0x10

   __DATA_CONST.__auth_got: 0xd0
   __DATA_CONST.__got: 0x50
   __DATA.__objc_const: 0x2b0
-  __DATA.__objc_selrefs: 0x160
+  __DATA.__objc_selrefs: 0x168
   __DATA.__objc_data: 0xa0
   __DATA.__data: 0x120
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/DocumentManagerExecutables.framework/DocumentManagerExecutables
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 15
+  Functions: 17
   Symbols:   49
-  CStrings:  84
+  CStrings:  87
 
Symbols:
+ _objc_retain_x22
- _objc_retain_x2
CStrings:
+ "[Rename] Import API failed, could not build a nofollow wrapper. Error: %@"
+ "[Rename] Rename API failed, could not build a nofollow wrapper. Error: %@"
+ "doc_noFollowSafeWrapper"
```
