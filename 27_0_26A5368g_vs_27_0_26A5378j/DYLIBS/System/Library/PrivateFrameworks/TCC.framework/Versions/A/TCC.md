## TCC

> `/System/Library/PrivateFrameworks/TCC.framework/Versions/A/TCC`

```diff

-  __TEXT.__text: 0x1e75c
+  __TEXT.__text: 0x1e748
   __TEXT.__objc_methlist: 0x11c
   __TEXT.__const: 0x3b0
   __TEXT.__cstring: 0x390d
-  __TEXT.__oslogstring: 0x245e
+  __TEXT.__oslogstring: 0x2464
   __TEXT.__unwind_info: 0x6f8
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __AUTH_CONST.__cfstring: 0x1780
   __AUTH_CONST.__objc_const: 0xf58
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0x140
+  __AUTH.__objc_data: 0x190
   __AUTH.__data: 0x208
   __DATA.__data: 0x930
   __DATA.__bss: 0x98
-  __DATA_DIRTY.__objc_data: 0x320
+  __DATA_DIRTY.__objc_data: 0x2d0
   __DATA_DIRTY.__bss: 0xb8
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/Versions/A/CoreServices

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 764
-  Symbols:   1709
+  Symbols:   1708
   CStrings:  909
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH.__data : content changed
~ __DATA.__data : content changed
Symbols:
- _geteuid
Functions:
~ _TCCCheckIfDatabaseIsRegisteredInSystem : 580 -> 560
CStrings:
+ "TCCCheckIfDatabaseIsRegisteredInUser() IPC"
- "TCCCheckIfDatabaseIsRegistered() IPC"

```
