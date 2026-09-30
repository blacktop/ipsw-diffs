## GameControllerFoundation

> `/System/Library/PrivateFrameworks/GameControllerFoundation.framework/Versions/A/GameControllerFoundation`

```diff

-  __TEXT.__text: 0x76124
-  __TEXT.__objc_methlist: 0x6bac
+  __TEXT.__text: 0x76534
+  __TEXT.__objc_methlist: 0x6c14
   __TEXT.__const: 0x128
-  __TEXT.__gcc_except_tab: 0x33c0
-  __TEXT.__cstring: 0x722f
-  __TEXT.__oslogstring: 0x3373
+  __TEXT.__gcc_except_tab: 0x33bc
+  __TEXT.__cstring: 0x7243
+  __TEXT.__oslogstring: 0x33f5
   __TEXT.__ustring: 0x58
-  __TEXT.__unwind_info: 0x2190
+  __TEXT.__unwind_info: 0x21a8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x78
   __DATA_CONST.__objc_protolist: 0x160
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1e48
+  __DATA_CONST.__objc_selrefs: 0x1e70
   __DATA_CONST.__objc_protorefs: 0xb8
   __DATA_CONST.__objc_superrefs: 0x440
   __DATA_CONST.__objc_arraydata: 0x140
-  __DATA_CONST.__got: 0x4e0
+  __DATA_CONST.__got: 0x530
   __AUTH_CONST.__const: 0x1980
-  __AUTH_CONST.__cfstring: 0x6f80
-  __AUTH_CONST.__objc_const: 0x14b28
+  __AUTH_CONST.__cfstring: 0x6fc0
+  __AUTH_CONST.__objc_const: 0x14b58
   __AUTH_CONST.__objc_intobj: 0x1f8
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x48
-  __AUTH_CONST.__auth_got: 0x990
-  __AUTH.__objc_data: 0x2620
+  __AUTH_CONST.__auth_got: 0x998
+  __AUTH.__objc_data: 0x2670
   __AUTH.__data: 0x1170
   __DATA.__objc_ivar: 0x89c
   __DATA.__data: 0x1080
   __DATA.__crash_info: 0x148
   __DATA.__bss: 0x110
-  __DATA_DIRTY.__objc_data: 0x690
+  __DATA_DIRTY.__objc_data: 0x640
   __DATA_DIRTY.__bss: 0xb8
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3044
-  Symbols:   7399
-  CStrings:  2235
+  Functions: 3048
+  Symbols:   7409
+  CStrings:  2241
 
Sections:
~ __TEXT.__const : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH.__data : content changed
~ __DATA.__data : content changed
Symbols:
+ +[GCIOService getService:matching:error:]
+ +[GCIOService getServices:matching:error:]
+ -[GCIOService waitQuiet:error:]
+ -[GCIOService waitQuietWithError:]
+ _IOServiceGetMatchingService
+ _modf
+ _objc_msgSend$array
+ _objc_msgSend$numberPropertyForKey:
+ _objc_msgSend$stringPropertyForKey:
CStrings:
+ "<IOService> Error creating iterator for matching services: %{public}@"
+ "<IOService> Error finding matching services: %{mach.errno}d"
+ "GameControllerCategory"
+ "GameControllerSupport"
+ "dynamic"
- "GameControllerSupportedHIDDevice"

```
