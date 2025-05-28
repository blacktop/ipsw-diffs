## security-sysdiagnose

> `/usr/libexec/security-sysdiagnose`

```diff

-61040.42.1.0.0
-  __TEXT.__text: 0x29b0
-  __TEXT.__auth_stubs: 0x6e0
-  __TEXT.__objc_stubs: 0x2c0
+61040.62.1.0.0
+  __TEXT.__text: 0x2cd8
+  __TEXT.__auth_stubs: 0x710
+  __TEXT.__objc_stubs: 0x360
   __TEXT.__objc_methlist: 0x50
   __TEXT.__const: 0x60
   __TEXT.__gcc_except_tab: 0x114
   __TEXT.__objc_classname: 0x2f
-  __TEXT.__objc_methname: 0x270
+  __TEXT.__objc_methname: 0x2b6
   __TEXT.__objc_methtype: 0xfa
-  __TEXT.__cstring: 0x6bb
+  __TEXT.__cstring: 0x709
   __TEXT.__oslogstring: 0xa8
   __TEXT.__unwind_info: 0xe8
-  __DATA_CONST.__auth_got: 0x380
-  __DATA_CONST.__got: 0xc0
+  __DATA_CONST.__auth_got: 0x398
+  __DATA_CONST.__got: 0xd0
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x310
-  __DATA_CONST.__cfstring: 0x6e0
+  __DATA_CONST.__cfstring: 0x780
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0x188
-  __DATA.__objc_selrefs: 0xc0
+  __DATA.__objc_selrefs: 0xe8
   __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_classrefs: 0x28
+  __DATA.__objc_classrefs: 0x38
   __DATA.__data: 0x60
   __DATA.__bss: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 32
-  Symbols:   147
-  CStrings:  138
+  Symbols:   154
+  CStrings:  148
 
Symbols:
+ _OBJC_CLASS_$_NSMutableArray
+ _OBJC_CLASS_$_NSMutableDictionary
+ _SecIsInternalRelease
+ _kSecAttrLabel
+ _kSecAttrSynchronizableAny
+ _objc_release_x27
+ _objc_release_x28
CStrings:
+ "<REDACTED-LABL-%llu>"
+ "Notes keychain state:\n"
+ "addObject:"
+ "array"
+ "dictionary"
+ "group.com.apple.notes"
+ "isEqualToString:"
+ "local"
+ "notes"
+ "sortUsingSelector:"

```
