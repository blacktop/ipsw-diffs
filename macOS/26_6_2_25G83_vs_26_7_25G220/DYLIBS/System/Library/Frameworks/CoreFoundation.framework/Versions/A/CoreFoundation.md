## CoreFoundation

> `/System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation`

```diff

-5026.6.7.0.0
-  __TEXT.__text: 0x1f9e24
+5026.6.7.2.0
+  __TEXT.__text: 0x1fa0c8
   __TEXT.__auth_stubs: 0x33a0
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0x839c
   __TEXT.__const: 0x1a8414
   __TEXT.__oslogstring: 0xae7a
-  __TEXT.__cstring: 0xbce73
+  __TEXT.__cstring: 0xbcf21
   __TEXT.__gcc_except_tab: 0x50a0
   __TEXT.__ustring: 0x1446
   __TEXT.__dlopen_cstrs: 0xcc
   __TEXT.__dof_NSAppNap: 0x4cf
   __TEXT.__dof_CFRunLoop: 0x964
   __TEXT.__dof_Cocoa_Aut: 0x486
-  __TEXT.__unwind_info: 0x6928
+  __TEXT.__unwind_info: 0x6930
   __TEXT.__eh_frame: 0x560
   __TEXT.__objc_classname: 0xc18
   __TEXT.__objc_methname: 0x9f33

   __DATA_CONST.__objc_arraydata: 0x5730
   __AUTH_CONST.__auth_got: 0x19e8
   __AUTH_CONST.__const: 0x92e8
-  __AUTH_CONST.__cfstring: 0xd9f80
+  __AUTH_CONST.__cfstring: 0xd9fc0
   __AUTH_CONST.__objc_const: 0xb0b8
   __AUTH_CONST.__const_cfobj2: 0x40
   __AUTH_CONST.__objc_dictobj: 0x2620

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/liboah.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 9365
-  Symbols:   14672
-  CStrings:  48670
+  Functions: 9366
+  Symbols:   14673
+  CStrings:  48672
 
Symbols:
+ ___CFStringContainsNullCharacter
Functions:
~ ___CFPropertyListIsValidAux : 744 -> 792
~ ___CFPropertyListIsDictPlistAux : 308 -> 328
~ ___27-[__NSSetI containsObject:]_block_invoke : 24 -> 36
~ ___CFMessagePortPerform : 1480 -> 1532
+ ___CFStringContainsNullCharacter
CStrings:
+ "property list dictionary keys cannot contain embedded null characters for XML format"
+ "property list strings cannot contain embedded null characters for XML or OpenStep format"
```
