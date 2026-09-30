## Mail

> `/System/Library/Assistant/Plugins/Mail.assistantBundle/Mail`

```diff

-  __TEXT.__text: 0x3338
-  __TEXT.__auth_stubs: 0x300
+  __TEXT.__text: 0x33d0
+  __TEXT.__auth_stubs: 0x320
   __TEXT.__objc_stubs: 0xb00
   __TEXT.__objc_methlist: 0x314
   __TEXT.__gcc_except_tab: 0x8a8
   __TEXT.__const: 0x20
   __TEXT.__cstring: 0x1e3
   __TEXT.__objc_classname: 0xa4
-  __TEXT.__objc_methname: 0x83c
-  __TEXT.__objc_methtype: 0x295
+  __TEXT.__objc_methname: 0x851
+  __TEXT.__objc_methtype: 0x2c2
   __TEXT.__oslogstring: 0x64
-  __TEXT.__unwind_info: 0x1f0
+  __TEXT.__unwind_info: 0x1f8
   __DATA_CONST.__const: 0xb8
   __DATA_CONST.__cfstring: 0x180
   __DATA_CONST.__objc_classlist: 0x30

   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA_CONST.__auth_got: 0x190
+  __DATA_CONST.__auth_got: 0x1a0
   __DATA_CONST.__got: 0x170
-  __DATA.__objc_const: 0x738
+  __DATA.__objc_const: 0x758
   __DATA.__objc_selrefs: 0x3b8
-  __DATA.__objc_ivar: 0x20
+  __DATA.__objc_ivar: 0x24
   __DATA.__objc_data: 0x1e0
   __DATA.__data: 0x120
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 44
-  Symbols:   131
-  CStrings:  208
+  Symbols:   134
+  CStrings:  210
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__gcc_except_tab : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__got : content changed
~ __DATA.__objc_selrefs : content changed
~ __DATA.__objc_data : content changed
~ __DATA.__data : content changed
Symbols:
+ OBJC_IVAR_$_MFAssistantEmailSearch._searchCompletedLock
+ _os_unfair_lock_lock
+ _os_unfair_lock_unlock
Functions:
~ sub_3444 : 536 -> 568
~ sub_392c -> sub_394c : 52 -> 172
CStrings:
+ "_searchCompletedLock"
+ "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"

```
