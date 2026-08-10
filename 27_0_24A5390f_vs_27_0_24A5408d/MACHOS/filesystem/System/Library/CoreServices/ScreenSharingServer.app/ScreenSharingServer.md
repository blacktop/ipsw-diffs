## ScreenSharingServer

> `/System/Library/CoreServices/ScreenSharingServer.app/ScreenSharingServer`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-166.11.0.0.0
-  __TEXT.__text: 0x3f8a8
-  __TEXT.__auth_stubs: 0xe40
-  __TEXT.__objc_stubs: 0x4760
-  __TEXT.__objc_methlist: 0x1d94
+166.13.0.0.0
+  __TEXT.__text: 0x40064
+  __TEXT.__auth_stubs: 0xe80
+  __TEXT.__objc_stubs: 0x46e0
+  __TEXT.__objc_methlist: 0x1d9c
   __TEXT.__const: 0xf2
-  __TEXT.__objc_methname: 0x6160
-  __TEXT.__cstring: 0xb69e
-  __TEXT.__oslogstring: 0x7539
+  __TEXT.__objc_methname: 0x6198
+  __TEXT.__cstring: 0xb87e
+  __TEXT.__oslogstring: 0x760f
   __TEXT.__objc_classname: 0x2a7
-  __TEXT.__objc_methtype: 0x322c
+  __TEXT.__objc_methtype: 0x32b5
   __TEXT.__gcc_except_tab: 0x3c4
-  __TEXT.__unwind_info: 0x560
-  __DATA_CONST.__const: 0x610
-  __DATA_CONST.__cfstring: 0x1d60
+  __TEXT.__unwind_info: 0x580
+  __DATA_CONST.__const: 0x590
+  __DATA_CONST.__cfstring: 0x1e20
   __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x78

   __DATA_CONST.__objc_arrayobj: 0x48
   __DATA_CONST.__objc_intobj: 0x60
   __DATA_CONST.__objc_dictobj: 0x78
-  __DATA_CONST.__auth_got: 0x730
+  __DATA_CONST.__auth_got: 0x750
   __DATA_CONST.__got: 0x400
   __DATA.__objc_const: 0x2740
-  __DATA.__objc_selrefs: 0x1718
+  __DATA.__objc_selrefs: 0x16f0
   __DATA.__objc_ivar: 0x200
   __DATA.__objc_data: 0x410
   __DATA.__data: 0x5f0

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 619
-  Symbols:   369
-  CStrings:  3330
+  Functions: 624
+  Symbols:   373
+  CStrings:  3344
 
Symbols:
+ _CGPointZero
+ _CGRectFromString
+ _CGRectIsNull
+ _CGRectNull
+ _MGGetFloat32Answer
+ _NSStringFromClass
- _OBJC_CLASS_$_UIScreen
- _UIScreenModeDidChangeNotification
CStrings:
+ "%@/%@"
+ "%@[%lu]"
+ "-[SSAnnotationRenderer convertScaledCoordinates:]"
+ "MGGetSInt32Answer(kMGQMainScreenHeight) returned 0"
+ "MGGetSInt32Answer(kMGQMainScreenWidth) returned 0"
+ "StripNonSerializableValues"
+ "StripNonSerializableValues_block_invoke"
+ "T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_currentDisplayBounds"
+ "[%s:%d] MGGetSInt32Answer(kMGQMainScreenHeight) returned 0"
+ "[%s:%d] MGGetSInt32Answer(kMGQMainScreenWidth) returned 0"
+ "[%s:%d] convertScaledCoordinates called before currentDisplayBounds was known"
+ "[%s:%d] sendServiceMessage dict: %s  destination %s  service %p"
+ "[%s:%d] stripping non-serializable value <%s> at %s"
+ "[%s:%d] stripping non-string key <%s> under %s"
+ "_currentDisplayBounds"
+ "_updateDisplayBoundsFromReply:"
+ "convertScaledCoordinates called before currentDisplayBounds was known"
+ "currentDisplayBounds"
+ "currentDisplayBounds updated: %s"
+ "displayBounds"
+ "enumerateKeysAndObjectsUsingBlock:"
+ "main screen point width: %f height: %f orientation %ld landscape: %d"
+ "main-screen-height"
+ "main-screen-scale"
+ "main-screen-width"
+ "sendServiceMessage dict: %s  destination %s  service %p"
+ "setCurrentDisplayBounds:"
+ "stripping non-serializable value <%s> at %s"
+ "stripping non-string key <%s> under %s"
+ "v32@?0@8@16^B24"
+ "v48@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16"
+ "{CGRect=\"origin\"{CGPoint=\"x\"d\"y\"d}\"size\"{CGSize=\"width\"d\"height\"d}}"
+ "{CGRect={CGPoint=dd}{CGSize=dd}}16@0:8"
- "@\"UIScreen\""
- "T@\"UIScreen\",&,V_mainScreen"
- "[%s:%d] sendServiceMessage dict = %s  destination %s  sercice %p"
- "_mainScreen"
- "bounds"
- "currentMode"
- "main screen point width: %f height: %f  scaling: %f orientation %ld landscape: %d"
- "mainScreen"
- "mainScreen init"
- "mainScreen init main"
- "mainThread"
- "nativeBounds"
- "scale"
- "screenDidChange"
- "screenDidChange:"
- "screenRect: %s, scale: %f, modesize: (%f, %f)"
- "sendServiceMessage dict = %s  destination %s  sercice %p"
- "setMainScreen:"
- "size"
```
