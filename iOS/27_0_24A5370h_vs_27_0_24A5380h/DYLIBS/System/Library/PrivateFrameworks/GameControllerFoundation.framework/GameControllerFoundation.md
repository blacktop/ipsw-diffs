## GameControllerFoundation

> `/System/Library/PrivateFrameworks/GameControllerFoundation.framework/GameControllerFoundation`

```diff

-  __TEXT.__text: 0x6f844
-  __TEXT.__objc_methlist: 0x6b1c
+  __TEXT.__text: 0x6fc24
+  __TEXT.__objc_methlist: 0x6b84
   __TEXT.__const: 0x120
-  __TEXT.__gcc_except_tab: 0x33a4
-  __TEXT.__cstring: 0x71a6
-  __TEXT.__oslogstring: 0x3275
+  __TEXT.__gcc_except_tab: 0x33a0
+  __TEXT.__cstring: 0x71ba
+  __TEXT.__oslogstring: 0x32f7
   __TEXT.__ustring: 0x58
-  __TEXT.__unwind_info: 0x20f8
+  __TEXT.__unwind_info: 0x2110
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x78
   __DATA_CONST.__objc_protolist: 0x160
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1e08
+  __DATA_CONST.__objc_selrefs: 0x1e30
   __DATA_CONST.__objc_protorefs: 0xb8
   __DATA_CONST.__objc_superrefs: 0x438
   __DATA_CONST.__objc_arraydata: 0x140
-  __DATA_CONST.__got: 0x4d0
+  __DATA_CONST.__got: 0x520
   __AUTH_CONST.__const: 0x568
-  __AUTH_CONST.__cfstring: 0x6f40
-  __AUTH_CONST.__objc_const: 0x14988
+  __AUTH_CONST.__cfstring: 0x6f80
+  __AUTH_CONST.__objc_const: 0x149b8
   __AUTH_CONST.__objc_intobj: 0x1f8
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x48
-  __AUTH_CONST.__auth_got: 0xa50
-  __AUTH.__objc_data: 0x2850
+  __AUTH_CONST.__auth_got: 0xa58
+  __AUTH.__objc_data: 0x2940
   __AUTH.__data: 0x1170
   __DATA.__objc_ivar: 0x880
   __DATA.__data: 0x1080
   __DATA.__crash_info: 0x148
   __DATA.__bss: 0x130
-  __DATA_DIRTY.__objc_data: 0x410
+  __DATA_DIRTY.__objc_data: 0x320
   __DATA_DIRTY.__bss: 0x78
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2952
-  Symbols:   10215
-  CStrings:  2221
+  Functions: 2957
+  Symbols:   10232
+  CStrings:  2227
 
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
